import SimpleITK as sitk
import numpy as np
import cv2
import time

if __name__ == "__main__":

    SimpleElastix = sitk.SimpleElastix()
    SimpleElastix.LogToConsoleOn()
    iterationNumbers = 1024
    samplingAttemps = 16
    spatialSamples = 4096

    start = time.time()
    np_fix_image = sitk.ReadImage("/home/mass/ifilesets/ULG/f041985/images/fix_large.jpeg", sitk.sitkFloat32)
    np_moving_image = sitk.ReadImage("/home/mass/ifilesets/ULG/f041985/images/mov_large.jpeg", sitk.sitkFloat32)

    image_mov_cv = cv2.imread("/home/mass/ifilesets/ULG/f041985/images/mov_large.jpeg")

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
    SimpleElastix.SetParameter("NumberOfResolutions", "16")

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
    end = time.time()
    fin = end-start
    print "compute time " + str(fin) + " s"

    start = time.time()
    img_color_final = np.zeros((np_img.shape[0], np_img.shape[1], 3))

    img_color_final[:, :, 0] = sitk.GetArrayFromImage(img_to_save_0)
    img_color_final[:, :, 1] = sitk.GetArrayFromImage(img_to_save_1)
    img_color_final[:, :, 2] = sitk.GetArrayFromImage(img_to_save_2)
    end = time.time()
    fin = end-start
    print "save time " + str(fin) + " s"

    cv2.imwrite("result_colorcvtimed5k5k.png", img_color_final)

