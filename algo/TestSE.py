import SimpleITK as sitk
import numpy as np
import cv2


if __name__ == "__main__":
    
   """ print "start script"
    SimpleElastix = sitk.SimpleElastix()

    iterationNumbers = 512
    samplingAttemps = 8
    spatialSamples = 512

    np_fix_image = sitk.ReadImage("/home/mass/GRD/thomas.vessiere/images/fix_large.jpeg", sitk.sitkFloat32)
    np_moving_image = sitk.ReadImage("/home/mass/GRD/thomas.vessiere/images/fix_large.jpeg", sitk.sitkFloat32)

    image_mov_cv = cv2.imread("/home/mass/GRD/thomas.vessiere/images/fix_large.jpeg")

    array_0 = sitk.GetImageFromArray(image_mov_cv[:,:,0])
    array_1 = sitk.GetImageFromArray(image_mov_cv[:,:,1])
    array_2 = sitk.GetImageFromArray(image_mov_cv[:,:,2])

    SimpleElastix.SetFixedImage(np_fix_image)
    SimpleElastix.SetMovingImage(np_moving_image)

    parameterMapTranslation = sitk.GetDefaultParameterMap("translation")
    parameterMapAffine = sitk.GetDefaultParameterMap("affine")

    SimpleElastix.SetParameterMap(parameterMapTranslation)
    SimpleElastix.AddParameterMap(parameterMapAffine)

    SimpleElastix.SetParameter("MaximumNumberOfIterations", str(iterationNumbers))
    SimpleElastix.SetParameter("MaximumNumberOfSamplingAttempts", str(samplingAttemps))
    SimpleElastix.SetParameter("NumberOfSpatialSamples", str(spatialSamples))
    SimpleElastix.SetParameter("WriteIterationInfo", "true")

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

    cv2.imwrite("result_colorcv.png", img_color_final)"""

    print "go"


