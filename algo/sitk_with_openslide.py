import openslide
import SimpleITK as sitk
import sldc
from sldc_openslide import OpenSlideImage , OpenSlideTileBuilder
import numpy as np
import scipy.misc as misc

simple_elastix = sitk.SimpleElastix()
transform_x = sitk.SimpleTransformix()
slide_fix = openslide.open_slide("/home/mass/GRD/thomas.vessiere/images/fix_large_tissu.ndpi")
slide_mov = openslide.open_slide("/home/mass/GRD/thomas.vessiere/images/mov_large_tissu.ndpi")

fix_dimension = slide_fix.slide.dimensions
topology_fix = sldc.TileTopology(slide_fix,OpenSlideTileBuilder(),9000,9000,0)

mov_dimension = slide_mov.slide.dimensions
topology_mov = sldc.TileTopology(slide_mov,OpenSlideTileBuilder(),9000,9000,0)

dim_np_fix = (fix_dimension[1],fix_dimension[0],3)
np_image_fix = np.zeros(dim_np_fix,dtype=np.float32)
for tile in topology_fix:
    start_x = tile.abs_offset_x
    start_y = tile.abs_offset_y
    end_x = start_x + tile.width
    end_y = start_y + tile.height
    np_tile = tile.np_image
    np_image_fix[start_y:end_y,start_x:end_x] = np_tile[:,:,:-1]


dim_np_mov = (mov_dimension[1],mov_dimension[0],3)
np_image_mov = np.zeros(dim_np_mov,dtype=np.float32)

for tile in topology_mov:
    start_x = tile.abs_offset_x
    start_y = tile.abs_offset_y
    end_x = start_x + tile.width
    end_y = start_y + tile.height
    np_tile = tile.np_image
    np_image_mov[start_y:end_y,start_x:end_x] = np_tile[:,:,:-1]

itk_img_fix = sitk.GetImageFromArray(np_image_fix)
itk_img_mov = sitk.GetImageFromArray(np_image_mov)
simple_elastix.SetFixedImage(itk_img_fix)
simple_elastix.SetMovingImage(itk_img_mov)

del np_image_fix
del np_image_mov

parameter_map_translation = sitk.GetDefaultParameterMap("translation")
parameter_map_affine = sitk.GetDefaultParameterMap("affine")

# translation & affine #
simple_elastix.SetParameterMap(parameter_map_translation)
simple_elastix.AddParameterMap(parameter_map_affine)

simple_elastix.SetParameter("MaximumNumberOfIterations", "60000")
simple_elastix.SetParameter("NumberOfSpatialSamples", "60000")

simple_elastix.Execute()

transform_map = simple_elastix.GetTransformParameterMap()
# for set shape of images #
np_img = sitk.GetArrayFromImage(simple_elastix.GetResultImage())

itk_mov_image_color_0 = sitk.GetImageFromArray(np_image_mov[:, :, 0])
itk_mov_image_color_1 = sitk.GetImageFromArray(np_image_mov[:, :, 1])
itk_mov_image_color_2 = sitk.GetImageFromArray(np_image_mov[:, :, 2])

transform_x.SetMovingImage(itk_mov_image_color_0)
img_to_save_0 = transform_x.Execute()
transform_x.SetMovingImage(itk_mov_image_color_1)
img_to_save_1 = transform_x.Execute()
transform_x.SetMovingImage(itk_mov_image_color_2)
img_to_save_2 = transform_x.Execute()

# format image color #
img_color_final = np.zeros((np_img.shape[0], np_img.shape[1], 3))

img_color_final[:, :, 0] = sitk.GetArrayFromImage(img_to_save_0)
img_color_final[:, :, 1] = sitk.GetArrayFromImage(img_to_save_1)
img_color_final[:, :, 2] = sitk.GetArrayFromImage(img_to_save_2)

misc.imsave("/home/mass/GRD/thomas.vessiere/images/result_colot.png",img_color_final)