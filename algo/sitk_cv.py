print "before imports"
import SimpleITK as sitk
import numpy as np
import cv2
import sys
print "after import"

if __name__ == "__main__":
    
    print "start script"
    SimpleElastix = sitk.SimpleElastix()	
    iterationNumbers = 128
    samplingAttemps = 16
    spatialSamples = 2048
    print "before read image"
    print "read img"
    np_fix_image = sitk.ReadImage("/home/mass/ifilesets/ULG/f041985/images/fix_large.jpeg", sitk.sitkFloat32)
    np_moving_image = sitk.ReadImage("/home/mass/ifilesets/ULG/f041985/images/mov_large.jpeg", sitk.sitkFloat32)

    image_mov_cv = cv2.imread("/home/mass/ifilesets/ULG/f041985/images/mov_large.jpeg")

    print "get arrays"
    array_0 = sitk.GetImageFromArray(image_mov_cv[:,:,0])
    array_1 = sitk.GetImageFromArray(image_mov_cv[:,:,1])
    array_2 = sitk.GetImageFromArray(image_mov_cv[:,:,2])

    print "set images"
    SimpleElastix.SetFixedImage(np_fix_image)
    SimpleElastix.SetMovingImage(np_moving_image)
	
    parameterMapTranslation = sitk.GetDefaultParameterMap("translation")
    parameterMapAffine = sitk.GetDefaultParameterMap("affine")

    SimpleElastix.SetParameterMap(parameterMapTranslation)
    SimpleElastix.AddParameterMap(parameterMapAffine)

    SimpleElastix.SetParameter("MaximumNumberOfIterations", str(iterationNumbers))
    SimpleElastix.SetParameter("MaximumNumberOfSamplingAttempts", str(samplingAttemps))
    SimpleElastix.SetParameter("NumberOfSpatialSamples", str(spatialSamples))
    SimpleElastix.SetParameter("WriteIterationInfo" , "true")
    SimpleElastix.SetParameter("AutomaticParameterEstimation", "true")
    #SimpleElastix.SetParameter("UseAdaptiveStepSizes", "true")
    SimpleElastix.SetParameter("NumberOfResolutions", str(16))
    print "exec"
    SimpleElastix.Execute()
    transform_map = SimpleElastix.GetTransformParameterMap()
    properties_map = {}

    np_img = sitk.GetArrayFromImage(SimpleElastix.GetResultImage())
    TransformX = sitk.SimpleTransformix()
    TransformX.SetTransformParameterMap(transform_map)

    TransformX.SetMovingImage(array_0)
    img_to_save_0 = TransformX.Execute()
    TransformX.SetMovingImage(array_1)
    img_to_save_1 = TransformX.Execute()
    TransformX.SetMovingImage(array_2)
    img_to_save_2 = TransformX.Execute()

    img_color_final = np.zeros((np_img.shape[0], np_img.shape[1], 3))

    img_color_final[:, :, 0] = sitk.GetArrayFromImage(img_to_save_0)
    img_color_final[:, :, 1] = sitk.GetArrayFromImage(img_to_save_1)
    img_color_final[:, :, 2] = sitk.GetArrayFromImage(img_to_save_2)

    cv2.imwrite("result_colorcv_16resolution.png", img_color_final)

