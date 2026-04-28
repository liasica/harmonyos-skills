---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-yuv-shooting
title: YUV拍照(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > YUV拍照(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a27a72d383ffc543ea33e6e1b9c460f48e140b716dc009b9962eb9cf7d0b654
---

从API version 23开始，相机框架提供YUV格式图片拍照能力。与普通拍照相比，YUV拍照获取到的是未经过编码的图像数据，完整保留了传感器捕获的原始亮度和色度信息，适用于视频编码或专业处理。同时，拍摄过程会产生更高的能耗开销，保存会占用更多的存储空间。

## 开发步骤

详细的相机功能API说明请参考Camera模块描述[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. // 导入NDK接口头文件。
   2. #include <cstdint>
   3. #include <cstdlib>
   4. #include <cstring>
   5. #include <string.h>
   6. #include <new>
   7. #include "hilog/log.h"
   8. #include "multimedia/image_framework/image/image_source_native.h"
   9. #include "multimedia/image_framework/image/image_packer_native.h"
   10. #include "multimedia/media_library/media_access_helper_capi.h"
   11. #include "multimedia/media_library/media_asset_base_capi.h"
   12. #include "multimedia/media_library/media_asset_capi.h"
   13. #include "multimedia/media_library/media_asset_change_request_capi.h"
   14. #include "multimedia/media_library/media_asset_manager_capi.h"
   15. #include "ohcamera/camera.h"
   16. #include "ohcamera/camera_input.h"
   17. #include "ohcamera/camera_manager.h"
   18. #include "ohcamera/capture_session.h"
   19. #include "ohcamera/photo_native.h"
   20. #include "ohcamera/photo_output.h"
   21. #include "ohcamera/preview_output.h"
   22. #include "ohcamera/video_output.h"
   ```
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libnative_buffer.so
   5. libohcamera.so
   6. libohimage.so
   7. libohfileuri.so
   8. libmedia_asset_manager.so
   9. libimage_source.so
   10. libpixelmap.so
   11. libimage_packer.so
   12. libpicture.so
   13. )
   ```
3. 创建并打开相机设备，参考[设备输入(C/C++)](native-camera-device-input.md)中的步骤3-4。
4. 获取相机设备完整输出能力。

   通过[OH\_CameraManager\_GetSupportedFullCameraOutputCapabilityWithSceneMode()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedfullcameraoutputcapabilitywithscenemode)方法，获取当前设备支持的所有输出流的能力，包含预览流、拍照流、录像流等。输出流在CameraOutputCapability中的各个profile字段中，其中拍照流支持YUV格式。根据相机设备指定模式[Camera\_SceneMode](../harmonyos-references/capi-camera-h.md#camera_scenemode)的不同，需要添加不同类型的输出流。

   ```
   1. Camera_OutputCapability* GetSupportedFullCameraOutputCapability(Camera_Manager* cameraManager, Camera_Device &camera)
   2. {
   3. Camera_OutputCapability* cameraOutputCapability = nullptr;
   4. // 获取相机设备支持的输出流能力。
   5. const Camera_Profile* previewProfile = nullptr;
   6. const Camera_Profile* photoProfile = nullptr;
   7. Camera_ErrorCode ret = OH_CameraManager_GetSupportedFullCameraOutputCapabilityWithSceneMode(cameraManager, &camera,
   8. Camera_SceneMode::NORMAL_PHOTO, &cameraOutputCapability);
   9. if (cameraOutputCapability == nullptr || ret != CAMERA_OK) {
   10. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameraOutputCapability failed.");
   11. return nullptr;
   12. }
   13. return cameraOutputCapability;
   14. }
   ```
5. 选择设备支持的输出流能力，创建拍照输出流。

   通过[OH\_CameraManager\_CreatePhotoOutputWithoutSurface()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createphotooutputwithoutsurface)方法创建拍照输出流。

   可以通过[OH\_CameraManager\_GetSupportedFullCameraOutputCapabilityWithSceneMode()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedfullcameraoutputcapabilitywithscenemode)获取相机在指定模式下支持的完整输出能力cameraOutputCapability，参考步骤2。在cameraOutputCapability的photoProfiles中选择支持YUV格式的profile，作为创建拍照输出流的参数photoProfile。

   ```
   1. Camera_PhotoOutput* CreatePhotoOutput(Camera_Manager* cameraManager, const Camera_Profile* photoProfile)
   2. {
   3. Camera_PhotoOutput* photoOutput = nullptr;
   4. // 无需传入surfaceId，直接创建拍照流。
   5. Camera_ErrorCode ret = OH_CameraManager_CreatePhotoOutputWithoutSurface(cameraManager, photoProfile, &photoOutput);
   6. if (photoOutput == nullptr || ret != CAMERA_OK) {
   7. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePhotoOutputWithoutSurface failed.");
   8. }
   9. return photoOutput;
   10. }
   ```
6. 注册单段式(PhotoAvailable)或分段式(PhotoAssetAvailable)拍照回调，若应用希望快速得到回图，推荐使用[分段式拍照(PhotoAssetAvailable)](native-camera-deferred-capture.md)回调。

   注意

   如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册会导致流被重启，仅PhotoAssetAvailable生效。

   * **单段式拍照（PhotoAvailable）开发流程**：

     + 在会话[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)前注册单段式拍照回调。
     + 在单段式拍照回调函数中获取图片信息，解析出pixelMap数据，做自定义业务处理。
     + 将处理完的pixelMap通过回调传给ArkTS侧，做图片显示或通过安全控件写文件保存图片。
     + 使用完后解注册单段式拍照回调函数。

     ```
     1. // 单段式拍照回调函数。
     2. void OnPhotoAvailable(Camera_PhotoOutput* photoOutput, OH_PhotoNative* photo)
     3. {
     4. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable start!");
     5. OH_PictureNative* picture;
     6. Camera_ErrorCode errCode = OH_PhotoNative_GetUncompressedImage(photo, &picture);
     7. if (errCode != CAMERA_OK || picture == nullptr) {
     8. OH_LOG_ERROR(LOG_APP, "OH_PhotoNative_GetUncompressedImage call failed, errorCode: %{public}d", errCode);
     9. return;
     10. }
     11. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable errCode:%{public}d picture:%{public}p", errCode, picture);
     12. // 读取OH_PictureNative中的主图mainPixelMap。
     13. OH_PixelmapNative* mainPixelmap;
     14. Image_ErrorCode imageErr = OH_PictureNative_GetMainPixelmap(picture, &mainPixelmap);
     15. if (imageErr != IMAGE_SUCCESS || mainPixelmap == nullptr) {
     16. OH_LOG_ERROR(LOG_APP, "OH_ImageNative_GetImageSize call failed, errorCode: %{public}d", imageErr);
     17. return;
     18. }
     19. OH_LOG_INFO(LOG_APP, "OH_PictureNative_GetMainPixelmap success");
     20. // 获取主图Pixelmap中所有像素所占用的总字节数。
     21. uint32_t byteCount = 0;
     22. imageErr = OH_PixelmapNative_GetByteCount(mainPixelmap, &byteCount);
     23. OH_LOG_INFO(LOG_APP, "OH_PixelmapNative_GetByteCount count:%{public}u", byteCount);
     24. // 获取主图的图像像素信息。
     25. OH_Pixelmap_ImageInfo* imageInfo;
     26. imageErr = OH_PixelmapNative_GetImageInfo(mainPixelmap, imageInfo);
     27. OH_LOG_INFO(LOG_APP, "OH_PixelmapNative_GetImageInfo errorCode:%{public}d", imageErr);

     29. uint32_t width = 0;
     30. uint32_t height = 0;
     31. uint32_t rowStride = 0;
     32. int32_t pixelFormat = PIXEL_FORMAT::PIXEL_FORMAT_UNKNOWN;
     33. int32_t alphaMode = PIXELMAP_ALPHA_TYPE::PIXELMAP_ALPHA_TYPE_UNKNOWN;
     34. int32_t alphaType = PIXELMAP_ALPHA_TYPE::PIXELMAP_ALPHA_TYPE_UNKNOWN;
     35. // 获取主图图像像素信息中的宽度。
     36. OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
     37. // 获取主图图像像素信息中的高度。
     38. OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
     39. // 获取主图图像像素信息中的行跨距。
     40. OH_PixelmapImageInfo_GetRowStride(imageInfo, &rowStride);
     41. // 获取主图图像像素信息中的像素格式。
     42. OH_PixelmapImageInfo_GetPixelFormat(imageInfo, &pixelFormat);
     43. // 获取主图图像像素信息中的透明通道类型。
     44. OH_PixelmapImageInfo_GetAlphaMode(imageInfo, &alphaMode);
     45. // 获取主图图像像素信息中的默认的透明通道类型。
     46. OH_PixelmapImageInfo_GetAlphaType(imageInfo, &alphaType);
     47. OH_LOG_INFO(LOG_APP, "OH_PixelmapNative_GetImageInfo width:%{public}u height:%{public}u rowStride:%{public}u pixelFormat:%{public}d alphaMode:%{public}d alphaType:%{public}d", width, height, rowStride, pixelFormat, alphaMode, alphaType);
     48. // 释放资源。
     49. OH_PixelmapNative_Release(mainPixelmap);
     50. OH_PictureNative_Release(picture);
     51. }

     53. // 注册单段式拍照回调。
     54. Camera_ErrorCode PhotoOutputRegisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput)
     55. {
     56. OH_LOG_INFO(LOG_APP, "PhotoOutputRegisterPhotoAvailableCallback start!");
     57. Camera_ErrorCode ret = OH_PhotoOutput_RegisterPhotoAvailableCallback(photoOutput, OnPhotoAvailable);
     58. if (ret != CAMERA_OK) {
     59. OH_LOG_ERROR(LOG_APP, "PhotoOutputRegisterPhotoAvailableCallback failed.");
     60. }
     61. OH_LOG_INFO(LOG_APP, "PhotoOutputRegisterPhotoAvailableCallback return with ret code: %{public}d!", ret);
     62. return ret;
     63. }

     65. // 解注册单段式拍照回调。
     66. Camera_ErrorCode PhotoOutputUnRegisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput)
     67. {
     68. OH_LOG_INFO(LOG_APP, "PhotoOutputUnRegisterPhotoAvailableCallback start!");
     69. Camera_ErrorCode ret = OH_PhotoOutput_UnregisterPhotoAvailableCallback(photoOutput, OnPhotoAvailable);
     70. if (ret != CAMERA_OK) {
     71. OH_LOG_ERROR(LOG_APP, "PhotoOutputUnRegisterPhotoAvailableCallback failed.");
     72. }
     73. OH_LOG_INFO(LOG_APP, "PhotoOutputUnRegisterPhotoAvailableCallback return with ret code: %{public}d!", ret);
     74. return ret;
     75. }
     ```
   * **分段式拍照（PhotoAvailable）开发流程**：

     + 在会话[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)前注册分段式拍照回调。
     + 在分段式拍照回调函数中获取图片信息，解析出pixelMap数据，做自定义业务处理。
     + 将处理完的pixelMap通过回调传给ArkTS侧，做图片显示或通过安全控件写文件保存图片。
     + 调用[OH\_PhotoOutput\_Capture](../harmonyos-references/capi-photo-output-h.md#oh_photooutput_capture)拍照后，需要及时调用[OH\_MediaAssetChangeRequest\_SaveCameraPhoto](../harmonyos-references/capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_savecameraphoto)保存图片或[OH\_MediaAssetChangeRequest\_DiscardCameraPhoto](../harmonyos-references/capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_discardcameraphoto)取消保存图片，否则会影响后续图片的拍摄。
     + 使用完后解注册分段式拍照回调函数。

     ```
     1. // 声明快速返图回调。
     2. void OnRequestQuickImageDataPreparedWithDetails(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type, OH_ImageSourceNative* imageSourceNative, OH_PictureNative* pictureNative)
     3. {
     4. OH_LOG_INFO(LOG_APP, "OnRequestQuickImageDataPreparedWithDetails start!");
     5. if (!pictureNative && !imageSourceNative) {
     6. OH_LOG_ERROR(LOG_APP, "OnRequestQuickImageDataPreparedWithDetails, pictureNative and imageSourceNative are null.");
     7. return;
     8. } else if (!pictureNative && imageSourceNative) {
     9. OH_LOG_ERROR(LOG_APP, "OnRequestQuickImageDataPreparedWithDetails, pictureNative is null.");
     10. } else if (pictureNative && !imageSourceNative) {
     11. OH_LOG_ERROR(LOG_APP, "OnRequestQuickImageDataPreparedWithDetails, imageSourceNative is null.");
     12. } else {
     13. OH_LOG_INFO(LOG_APP, "OnRequestQuickImageDataPreparedWithDetails, pictureNative and imageSourceNative are not null.");
     14. }
     15. }

     17. // 分段式拍照回调函数。
     18. void OnPhotoAssetAvailable(Camera_PhotoOutput* photoOutput, OH_MediaAsset* mediaAsset)
     19. {
     20. OH_LOG_INFO(LOG_APP, "OnPhotoAssetAvailable start!");
     21. if (mediaAsset == nullptr) {
     22. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable invalid error, mediaAsset is null.");
     23. return;
     24. }
     25. // 尝试获取mediaAsset中的uri信息。
     26. const char* uri = nullptr;
     27. MediaLibrary_ErrorCode result = OH_MediaAsset_GetUri(mediaAsset, &uri);
     28. if (uri == nullptr || result != MEDIA_LIBRARY_OK) {
     29. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to get uri.");
     30. }
     31. // 尝试获取mediaAsset中的displayName信息。
     32. const char* displayName = nullptr;
     33. result = OH_MediaAsset_GetDisplayName(mediaAsset, &displayName);
     34. if (displayName == nullptr || result != MEDIA_LIBRARY_OK) {
     35. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to get displayName.");
     36. }
     37. // 尝试获取mediaAsset中的size信息。
     38. uint32_t mediaAssetSize = 0;
     39. result = OH_MediaAsset_GetSize(mediaAsset, &mediaAssetSize);
     40. if (result != MEDIA_LIBRARY_OK) {
     41. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to get size.");
     42. }
     43. // 尝试获取mediaAsset中的修改时间信息。
     44. uint32_t modifiedMs = 0;
     45. result = OH_MediaAsset_GetDateModifiedMs(mediaAsset, &modifiedMs);
     46. if (result != MEDIA_LIBRARY_OK) {
     47. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to get modifiedMs.");
     48. }
     49. // 尝试获取mediaAsset中的图片宽度信息。
     50. uint32_t width = 0;
     51. result = OH_MediaAsset_GetWidth(mediaAsset, &width);
     52. if (result != MEDIA_LIBRARY_OK) {
     53. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to get width.");
     54. }
     55. // 尝试获取mediaAsset中的图片高度信息。
     56. uint32_t height = 0;
     57. result = OH_MediaAsset_GetHeight(mediaAsset, &height);
     58. if (result != MEDIA_LIBRARY_OK) {
     59. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to get height.");
     60. }
     61. // 尝试获取mediaAsset中的图片方向信息。
     62. uint32_t orientation = 0;
     63. result = OH_MediaAsset_GetOrientation(mediaAsset, &orientation);
     64. if (result != MEDIA_LIBRARY_OK) {
     65. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to get orientation.");
     66. }
     67. // 创建媒体资产管理对象。
     68. OH_MediaAssetManager* mediaAssetManager = OH_MediaAssetManager_Create();
     69. if (mediaAssetManager == nullptr) {
     70. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to create mediaAssetManager.");
     71. return;
     72. }

     74. // 创建媒体资产变更请求。
     75. OH_MediaAssetChangeRequest* changeRequest = OH_MediaAssetChangeRequest_Create(mediaAsset);
     76. if (changeRequest == nullptr) {
     77. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to create changeRequest.");
     78. }
     79. // 注册媒体资产快速请求回调。
     80. MediaLibrary_RequestOptions requestOptions;
     81. requestOptions.deliveryMode = MEDIA_LIBRARY_BALANCED_MODE;
     82. MediaLibrary_RequestId requestId;
     83. result = OH_MediaAssetManager_QuickRequestImage(mediaAssetManager, mediaAsset, requestOptions, &requestId, OnRequestQuickImageDataPreparedWithDetails);
     84. if (result != MEDIA_LIBRARY_OK) {
     85. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to quick image.");
     86. }
     87. // 创建媒体资产保存变更请求。
     88. result = OH_MediaAssetChangeRequest_SaveCameraPhoto(changeRequest, MediaLibrary_ImageFileType::MEDIA_LIBRARY_IMAGE_JPEG);
     89. if (result != MEDIA_LIBRARY_OK) {
     90. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to save camera photo.");
     91. }
     92. result = OH_MediaAccessHelper_ApplyChanges(changeRequest);
     93. if (result != MEDIA_LIBRARY_OK) {
     94. OH_LOG_ERROR(LOG_APP, "OnPhotoAssetAvailable failed to apply changes.");
     95. }
     96. }

     98. // 注册分段式拍照回调函数。
     99. Camera_ErrorCode RegisterPhotoAssetAvailable(Camera_PhotoOutput* photoOutput)
     100. {
     101. Camera_ErrorCode ret = OH_PhotoOutput_RegisterPhotoAssetAvailableCallback(photoOutput, OnPhotoAssetAvailable);
     102. if (ret != CAMERA_OK) {
     103. OH_LOG_ERROR(LOG_APP, "RegisterPhotoAssetAvailable failed. %d ", ret);
     104. }
     105. return ret;
     106. }
     107. // 解注册分段式拍照回调函数。
     108. Camera_ErrorCode UnregisterPhotoAssetAvailable(Camera_PhotoOutput* photoOutput)
     109. {
     110. Camera_ErrorCode ret = OH_PhotoOutput_UnregisterPhotoAssetAvailableCallback(photoOutput, OnPhotoAssetAvailable);
     111. if (ret != CAMERA_OK) {
     112. OH_LOG_ERROR(LOG_APP, "UnregisterPhotoAssetAvailable failed. %d ", ret);
     113. }
     114. return ret;
     115. }
     ```
7. 创建拍照类型会话（参考[会话管理(C/C++)](native-camera-session-management.md)），开启会话，准备拍照。
8. 触发拍照。

   通过[OH\_PhotoOutput\_Capture()](../harmonyos-references/capi-photo-output-h.md#oh_photooutput_capture)方法，执行拍照任务。

   ```
   1. Camera_ErrorCode Capture(Camera_PhotoOutput* photoOutput)
   2. {
   3. Camera_ErrorCode ret = OH_PhotoOutput_Capture(photoOutput);
   4. if (ret == CAMERA_OK) {
   5. OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Capture success ");
   6. } else {
   7. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Capture failed. %d ", ret);
   8. }
   9. return ret;
   10. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍摄下一张图片是否就绪、拍照输出流的错误。

* 通过注册固定的onFrameStart回调函数获取监听拍照开始结果，当photoOutput创建成功时，即可监听。拍照第一次曝光时触发。

  ```
  1. void PhotoOutputOnFrameStart(Camera_PhotoOutput* photoOutput)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameStart");
  4. }
  5. void PhotoOutputOnFrameShutter(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* info)
  6. {
  7. OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameShutter");
  8. }
  ```
* 通过注册固定的onFrameEnd回调函数监听拍照结束结果，当photoOutput创建成功时，即可监听。

  ```
  1. void PhotoOutputOnFrameEnd(Camera_PhotoOutput* photoOutput, int32_t frameCount)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PhotoOutput frameCount = %{public}d", frameCount);
  4. }
  ```
* 通过注册固定的captureReady回调函数监听能否继续拍摄下一张的结果，当photoOutput创建成功时，即可监听。当下一张可拍时触发，该事件返回结果为下一张可拍的相关信息。

  ```
  1. static bool g_captureReadyFlag = false;
  2. void CaptureReadyCb(Camera_PhotoOutput* photoOutput) {
  3. g_captureReadyFlag = true;
  4. OH_LOG_INFO(LOG_APP, "PhotoOutputOnCaptureReady captureReadyFlag = %{public}d", g_captureReadyFlag);
  5. }

  7. void OnPhotoOutputOnCaptureReady(Camera_PhotoOutput* photoOutput)
  8. {
  9. OH_LOG_INFO(LOG_APP, "PhotoOutputOnCaptureReady");
  10. Camera_ErrorCode ret = OH_PhotoOutput_RegisterCaptureReadyCallback(photoOutput, CaptureReadyCb);
  11. }
  ```
* 通过注册固定的onError回调函数获取监听拍照输出流的错误结果。callback返回拍照输出接口使用错误时的对应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  1. void PhotoOutputOnError(Camera_PhotoOutput* photoOutput, Camera_ErrorCode errorCode)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PhotoOutput errorCode = %{public}d", errorCode);
  4. }
  ```

  ```
  1. PhotoOutput_Callbacks* GetPhotoOutputListener()
  2. {
  3. static PhotoOutput_Callbacks photoOutputListener = {
  4. .onFrameStart = PhotoOutputOnFrameStart,
  5. .onFrameShutter = PhotoOutputOnFrameShutter,
  6. .onFrameEnd = PhotoOutputOnFrameEnd,
  7. .onError = PhotoOutputOnError
  8. };
  9. return &photoOutputListener;
  10. }
  11. Camera_ErrorCode RegisterPhotoOutputCallback(Camera_PhotoOutput* photoOutput)
  12. {
  13. Camera_ErrorCode ret = OH_PhotoOutput_RegisterCallback(photoOutput, GetPhotoOutputListener());
  14. if (ret != CAMERA_OK) {
  15. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_RegisterCallback failed.");
  16. }
  17. return ret;
  18. }
  ```
