---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting
title: 拍照(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 拍照(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec1882d934a53c6069ee8aadd274edc4909a927b03d20409f34d1c5ae13eddf7
---

## 概述

拍照是相机的重要功能之一，拍照模块基于相机复杂的逻辑，为了保证用户拍出的照片质量，在中间步骤可以设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

目前相机开发有两种相机拍照方案，分别是相机[分段式拍照](native-camera-deferred-capture.md)和相机单段式拍照（**本文将以单段式拍照为基础进行说明**）。

* 分段式拍照是指相机拍照既可以输出低质量图用作缩略图，提升用户感知拍照速度，也可以使用高质量图保证最后的成图质量达到系统相机的水平。满足了图像处理算法的需求的同时，又不会阻塞前台的拍照速度，构筑相机性能竞争力，提升用户体验。
* 单段式拍照是指在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，所以Shot2See（用户点击拍照控件到在缩略图显示区域显示缩略图的过程）完成时延较长。此外，单段式拍照支持通过[高性能拍照](native-camera-shooting.md#高性能拍照)功能调整[画质优先策略](native-camera-shooting.md#画质优先策略)，以加快出图速度或提升图片质量。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. #include <cstdint>
   2. #include <native_buffer/buffer_common.h>
   3. #include <unistd.h>
   4. #include <string>
   5. #include <thread>
   6. #include <cstdio>
   7. #include <fcntl.h>
   8. #include <map>
   9. #include <string>
   10. #include <vector>
   11. #include <native_buffer/native_buffer.h>
   12. #include "iostream"
   13. #include "mutex"

   15. #include "hilog/log.h"
   16. #include "ohcamera/camera.h"
   17. #include "ohcamera/camera_input.h"
   18. #include "ohcamera/capture_session.h"
   19. #include "ohcamera/photo_output.h"
   20. #include "ohcamera/preview_output.h"
   21. #include "ohcamera/video_output.h"
   22. #include "napi/native_api.h"
   23. #include "ohcamera/camera_manager.h"
   24. #include <window_manager/oh_display_info.h>
   25. #include <window_manager/oh_display_manager.h>

   27. namespace OHOS_CAMERA_SAMPLE {
   28. class NDKCamera {
   29. public:
   30. struct CameraBuildingConfig {
   31. char *str;
   32. uint32_t focusMode;
   33. uint32_t cameraDeviceIndex;
   34. bool isVideo;
   35. bool isHdr;
   36. char *videoId;
   37. };
   38. ~NDKCamera();
   39. explicit NDKCamera(CameraBuildingConfig config);
   40. // ...
   41. };
   42. } // namespace OHOS_CAMERA_SAMPLE
   ```

   [camera\_manager.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.h#L18-L196)
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libnative_buffer.so
   5. libohcamera.so
   6. libohimage.so
   7. libohfileuri.so
   8. )
   ```
3. 创建并打开相机设备，参考 [设备输入(C/C++)](native-camera-device-input.md)步骤3-5。
4. 选择设备支持的输出流能力，创建拍照输出流。

   通过[OH\_CameraManager\_CreatePhotoOutputWithoutSurface()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createphotooutputwithoutsurface)方法创建拍照输出流。

   ```
   1. Camera_ErrorCode NDKCamera::CreatePhotoOutputWithoutSurfaceId()
   2. {
   3. OH_LOG_ERROR(LOG_APP, "CreatePhotoOutputWithoutSurfaceId enter.");
   4. profile_ = cameraOutputCapability_->photoProfiles[0];
   5. Camera_Profile* profile = cameraOutputCapability_->photoProfiles[0];
   6. profile->size.width = NUM_1920;
   7. profile->size.height = NUM_1080;
   8. profile_ = profile;
   9. if (profile_ == nullptr) {
   10. OH_LOG_ERROR(LOG_APP, "Get photoProfiles failed.");
   11. return CAMERA_INVALID_ARGUMENT;
   12. }
   13. ret_ = OH_CameraManager_CreatePhotoOutputWithoutSurface(cameraManager_, profile_, &photoOutput_);
   14. if (photoOutput_ == nullptr || ret_ != CAMERA_OK) {
   15. OH_LOG_ERROR(LOG_APP, "CreatePhotoOutputWithoutSurfaceId failed.");
   16. return CAMERA_INVALID_ARGUMENT;
   17. }
   18. // ...
   19. return ret_;
   20. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L475-L498)
5. 注册单段式(PhotoAvailable)拍照回调，若应用希望快速得到回图，推荐使用[分段式拍照回调(PhotoAssetAvailable)](native-camera-deferred-capture.md)。

   注意

   如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册，会导致流被重启，仅PhotoAssetAvailable生效。

   不建议开发者同时注册PhotoAssetAvailable和PhotoAvailable。

   **单段式拍照开发流程（PhotoAvailable）**：

   * 在会话commitConfig前注册单段式拍照回调。
   * 在单段式拍照回调函数中获取图片信息，解析出buffer数据，做自定义业务处理。
   * 将处理完的buffer通过回调传给ArkTS侧，做图片显示或通过安全控件写文件保存图片。
   * 使用完后解注册单段式拍照回调函数。

     ```
     1. // 保存NAPI侧注册的buffer处理回调函数。
     2. Camera_ErrorCode NDKCamera::RegisterBufferCb(void *cb)
     3. {
     4. OH_LOG_INFO(LOG_APP, " RegisterBufferCb start");
     5. if (cb == nullptr) {
     6. OH_LOG_INFO(LOG_APP, " RegisterBufferCb invalid error");
     7. return CAMERA_INVALID_ARGUMENT;
     8. }
     9. g_bufferCb = cb;
     10. return CAMERA_OK;
     11. }

     13. static bool ProcessImageNative(OH_ImageNative* imageNative, uint32_t** components,
     14. OH_NativeBuffer** nativeBuffer, size_t* nativeBufferSize)
     15. {
     16. if (imageNative == nullptr || components == nullptr || nativeBuffer == nullptr || nativeBufferSize == nullptr) {
     17. return false;
     18. }

     20. Image_Size size;
     21. Image_ErrorCode imageErr = OH_ImageNative_GetImageSize(imageNative, &size);
     22. if (imageErr != IMAGE_SUCCESS) {
     23. return false;
     24. }

     26. size_t componentTypeSize = 0;
     27. imageErr = OH_ImageNative_GetComponentTypes(imageNative, nullptr, &componentTypeSize);
     28. if (imageErr != IMAGE_SUCCESS || componentTypeSize == 0) {
     29. OH_LOG_ERROR(LOG_APP, "GetComponentTypes failed: %{public}d, size: %{public}zu",
     30. imageErr, componentTypeSize);
     31. return false;
     32. }

     34. if (componentTypeSize > (SIZE_MAX / sizeof(uint32_t))) {
     35. OH_LOG_ERROR(LOG_APP, "componentTypeSize too large: %{public}zu", componentTypeSize);
     36. return false;
     37. }

     39. uint32_t* compArray = new (std::nothrow) uint32_t[componentTypeSize];
     40. if (!compArray) {
     41. return false;
     42. }

     44. size_t tempSize = componentTypeSize;
     45. imageErr = OH_ImageNative_GetComponentTypes(imageNative, &compArray, &tempSize);
     46. if (imageErr != IMAGE_SUCCESS) {
     47. delete[] compArray;
     48. return false;
     49. }
     50. *components = compArray;

     52. imageErr = OH_ImageNative_GetByteBuffer(imageNative, compArray[0], nativeBuffer);
     53. if (imageErr != IMAGE_SUCCESS) {
     54. delete[] compArray;
     55. return false;
     56. }

     58. imageErr = OH_ImageNative_GetBufferSize(imageNative, compArray[0], nativeBufferSize);
     59. if (imageErr != IMAGE_SUCCESS) {
     60. delete[] compArray;
     61. return false;
     62. }

     64. int32_t rowStride = 0;
     65. int32_t pixelStride = 0;
     66. OH_ImageNative_GetRowStride(imageNative, compArray[0], &rowStride);
     67. OH_ImageNative_GetPixelStride(imageNative, compArray[0], &pixelStride);
     68. OH_LOG_INFO(LOG_APP, "Buffer size: %{public}zu, strides: %{public}d/%{public}d",
     69. *nativeBufferSize, rowStride, pixelStride);

     71. return true;
     72. }

     75. static void CleanupResources(OH_ImageNative* imageNative, uint32_t* components,
     76. OH_NativeBuffer* nativeBuffer, void* virAddr)
     77. {
     78. if (components) {
     79. delete[] components;
     80. }

     82. if (imageNative) {
     83. int32_t ret = OH_ImageNative_Release(imageNative);
     84. if (ret != 0) {
     85. OH_LOG_ERROR(LOG_APP, "Release image failed: %{public}d", ret);
     86. }
     87. }

     89. if (nativeBuffer && virAddr) {
     90. int32_t ret = OH_NativeBuffer_Unmap(nativeBuffer);
     91. if (ret != 0) {
     92. OH_LOG_ERROR(LOG_APP, "Unmap buffer failed: %{public}d", ret);
     93. }
     94. }
     95. }

     97. void OnPhotoAvailable(Camera_PhotoOutput *photoOutput, OH_PhotoNative *photo)
     98. {
     99. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable start!");

     101. OH_ImageNative *imageNative = nullptr;
     102. Camera_ErrorCode errCode = OH_PhotoNative_GetMainImage(photo, &imageNative);
     103. if (errCode != CAMERA_OK || !imageNative) {
     104. OH_LOG_ERROR(LOG_APP, "GetMainImage failed: %{public}d", errCode);
     105. return;
     106. }

     108. uint32_t* components = nullptr;
     109. OH_NativeBuffer* nativeBuffer = nullptr;
     110. size_t nativeBufferSize = 0;

     112. if (!ProcessImageNative(imageNative, &components, &nativeBuffer, &nativeBufferSize)) {
     113. CleanupResources(imageNative, components, nullptr, nullptr);
     114. return;
     115. }

     117. void* virAddr = nullptr;
     118. int32_t ret = OH_NativeBuffer_Map(nativeBuffer, &virAddr);
     119. if (ret != 0 || !virAddr) {
     120. OH_LOG_ERROR(LOG_APP, "Map buffer failed: %{public}d", ret);
     121. CleanupResources(imageNative, components, nativeBuffer, nullptr);
     122. return;
     123. }

     125. auto cb = (void (*)(void *, size_t))(g_bufferCb);
     126. if (cb && virAddr && nativeBufferSize > 0) {
     127. cb(virAddr, nativeBufferSize);
     128. OH_LOG_INFO(LOG_APP, "Buffer callback called");
     129. } else {
     130. OH_LOG_ERROR(LOG_APP, "Invalid callback parameters");
     131. }

     133. CleanupResources(imageNative, components, nativeBuffer, virAddr);

     135. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable end");
     136. }

     138. Camera_ErrorCode NDKCamera::PhotoOutputRegisterPhotoAvailableCallback(void)
     139. {
     140. OH_LOG_INFO(LOG_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback start!");
     141. Camera_ErrorCode ret = OH_PhotoOutput_RegisterPhotoAvailableCallback(photoOutput_, OnPhotoAvailable);
     142. if (ret != CAMERA_OK) {
     143. OH_LOG_INFO(LOG_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback failed.");
     144. }
     145. OH_LOG_INFO(LOG_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback return with ret code: %{public}d!",
     146. ret_);
     147. return ret;
     148. }

     150. // 解注册单段式拍照回调。
     151. Camera_ErrorCode NDKCamera::PhotoOutputUnRegisterPhotoAvailableCallback()
     152. {
     153. OH_LOG_INFO(LOG_APP, "PhotoOutputUnRegisterPhotoAvailableCallback start!");
     154. Camera_ErrorCode ret = OH_PhotoOutput_UnregisterPhotoAvailableCallback(photoOutput_, OnPhotoAvailable);
     155. if (ret != CAMERA_OK) {
     156. OH_LOG_ERROR(LOG_APP, "PhotoOutputUnRegisterPhotoAvailableCallback failed.");
     157. }
     158. OH_LOG_INFO(LOG_APP, "PhotoOutputUnRegisterPhotoAvailableCallback return with ret code: %{public}d!", ret);
     159. return ret;
     160. }
     ```

     [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1334-L1496)

     NAPI层buffer回调处理参考示例代码：

     ```
     1. // NAPI层buffer回调方法。
     2. static void BufferCb(void* buffer, size_t size)
     3. {
     4. OH_LOG_INFO(LOG_APP, "BufferCb size:%{public}zu", size);
     5. g_size = size;
     6. napi_value asyncResource = nullptr;
     7. napi_value asyncResourceName = nullptr;
     8. napi_async_work work;

     10. if (size == 0 || size > SIZE_MAX) {
     11. OH_LOG_ERROR(LOG_APP, "BufferCb size is invalid");
     12. return;
     13. }
     14. void* copyBuffer = malloc(size);
     15. if (copyBuffer == nullptr) {
     16. return;
     17. }
     18. OH_LOG_INFO(LOG_APP, "BufferCb copyBuffer:%{public}p", copyBuffer);
     19. // 使用std::memcpy复制buffer的内容到copyBuffer。
     20. std::memcpy(copyBuffer, buffer, size);
     21. napi_create_string_utf8(env_, "BufferCb", NAPI_AUTO_LENGTH, &asyncResourceName);
     22. napi_status status = napi_create_async_work(
     23. env_, asyncResource, asyncResourceName, [](napi_env env, void* copyBuffer) {},
     24. [](napi_env env, napi_status status, void* copyBuffer) {
     25. napi_value retVal;
     26. napi_value callback = nullptr;
     27. void* data = nullptr;
     28. napi_value arrayBuffer = nullptr;
     29. size_t bufferSize = g_size;
     30. napi_create_arraybuffer(env, bufferSize, &data, &arrayBuffer);
     31. std::memcpy(data, copyBuffer, bufferSize);
     32. OH_LOG_INFO(LOG_APP, "BufferCb g_size: %{public}zu", g_size);
     33. napi_get_reference_value(env, bufferCbRef_, &callback);
     34. if (callback) {
     35. OH_LOG_INFO(LOG_APP, "BufferCb callback is full");
     36. } else {
     37. OH_LOG_ERROR(LOG_APP, "BufferCb callback is null");
     38. }
     39. // 调用ArkTS的buffer处理回调函数，将图片arrayBuffer传给页面做显示或保存。
     40. napi_call_function(env, nullptr, callback, 1, &arrayBuffer, &retVal);
     41. },
     42. copyBuffer, &work);
     43. // 错误检查：创建异步工作失败时释放内存。
     44. if (status != napi_ok) {
     45. OH_LOG_ERROR(LOG_APP, "Failed to create async work");
     46. free(copyBuffer); // 释放分配的内存。
     47. return;
     48. }
     49. napi_queue_async_work_with_qos(env_, work, napi_qos_user_initiated);
     50. }
     ```

     [main.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/main.cpp#L610-L661)
6. 创建拍照类型会话，参考[会话管理(C/C++)](native-camera-session-management.md)，开启会话，准备拍照。
7. 配置拍照参数（可选）。

   配置相机的参数可以调整拍照的一些功能，包括闪光灯、变焦、焦距等。

   ```
   1. Camera_ErrorCode NDKCamera::HasFlashFn(uint32_t mode)
   2. {
   3. Camera_FlashMode flashMode = static_cast<Camera_FlashMode>(mode);
   4. // 检查闪光灯。
   5. bool hasFlash = false;
   6. Camera_ErrorCode ret = OH_CaptureSession_HasFlash(captureSession_, &hasFlash);
   7. if (captureSession_ == nullptr || ret != CAMERA_OK) {
   8. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_HasFlash failed.");
   9. }
   10. if (hasFlash) {
   11. OH_LOG_INFO(LOG_APP, "hasFlash success-----");
   12. } else {
   13. OH_LOG_ERROR(LOG_APP, "hasFlash fail-----");
   14. }

   16. // 查询闪光灯模式是否支持。
   17. bool isSupported = false;
   18. ret = OH_CaptureSession_IsFlashModeSupported(captureSession_, flashMode, &isSupported);
   19. if (ret != CAMERA_OK) {
   20. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFlashModeSupported failed.");
   21. }
   22. if (isSupported) {
   23. OH_LOG_INFO(LOG_APP, "isFlashModeSupported success-----");
   24. } else {
   25. OH_LOG_ERROR(LOG_APP, "isFlashModeSupported fail-----");
   26. }

   28. // 设置闪光灯模式。
   29. ret = OH_CaptureSession_SetFlashMode(captureSession_, flashMode);
   30. if (ret == CAMERA_OK) {
   31. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFlashMode success.");
   32. } else {
   33. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFlashMode failed. %{public}d ", ret);
   34. }

   36. // 获取当前设备的闪光灯模式。
   37. ret = OH_CaptureSession_GetFlashMode(captureSession_, &flashMode);
   38. if (ret == CAMERA_OK) {
   39. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFlashMode success. flashMode：%{public}d ", flashMode);
   40. } else {
   41. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFlashMode failed. %d ", ret);
   42. }
   43. return ret;
   44. }

   46. // 对焦模式。
   47. Camera_ErrorCode NDKCamera::IsFocusModeSupported(uint32_t mode)
   48. {
   49. Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
   50. ret_ = OH_CaptureSession_IsFocusModeSupported(captureSession_, focusMode, &isFocusModeSupported_);
   51. if (&isFocusModeSupported_ == nullptr || ret_ != CAMERA_OK) {
   52. OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
   53. return CAMERA_INVALID_ARGUMENT;
   54. }
   55. return ret_;
   56. }

   58. Camera_ErrorCode NDKCamera::IsFocusMode(uint32_t mode)
   59. {
   60. OH_LOG_INFO(LOG_APP, "IsFocusMode start.");
   61. Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
   62. ret_ = OH_CaptureSession_IsFocusModeSupported(captureSession_, focusMode, &isFocusModeSupported_);
   63. if (&isFocusModeSupported_ == nullptr || ret_ != CAMERA_OK) {
   64. OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
   65. return CAMERA_INVALID_ARGUMENT;
   66. }
   67. ret_ = OH_CaptureSession_SetFocusMode(captureSession_, focusMode);
   68. if (ret_ != CAMERA_OK) {
   69. OH_LOG_ERROR(LOG_APP, "SetFocusMode failed.");
   70. return CAMERA_INVALID_ARGUMENT;
   71. }
   72. ret_ = OH_CaptureSession_GetFocusMode(captureSession_, &focusMode);
   73. if (&focusMode == nullptr || ret_ != CAMERA_OK) {
   74. OH_LOG_ERROR(LOG_APP, "GetFocusMode failed.");
   75. return CAMERA_INVALID_ARGUMENT;
   76. }
   77. OH_LOG_INFO(LOG_APP, "IsFocusMode end.");
   78. return ret_;
   79. }

   81. Camera_ErrorCode NDKCamera::setZoomRatioFn(uint32_t zoomRatio)
   82. {
   83. float zoom = float(zoomRatio);
   84. // 获取支持的缩放范围。
   85. float minZoom;
   86. float maxZoom;
   87. Camera_ErrorCode ret = OH_CaptureSession_GetZoomRatioRange(captureSession_, &minZoom, &maxZoom);
   88. if (captureSession_ == nullptr || ret != CAMERA_OK) {
   89. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatioRange failed.");
   90. } else {
   91. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
   92. minZoom, maxZoom);
   93. }

   95. // 设置缩放比例。
   96. ret = OH_CaptureSession_SetZoomRatio(captureSession_, zoom);
   97. if (ret == CAMERA_OK) {
   98. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetZoomRatio success.");
   99. } else {
   100. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetZoomRatio failed. %{public}d ", ret);
   101. }

   103. // 获取当前设备的缩放比例。
   104. ret = OH_CaptureSession_GetZoomRatio(captureSession_, &zoom);
   105. if (ret == CAMERA_OK) {
   106. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatio success. zoom：%{public}f ", zoom);
   107. } else {
   108. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatio failed. %{public}d ", ret);
   109. }
   110. return ret;
   111. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L697-L811)
8. 触发拍照。

   通过[OH\_PhotoOutput\_Capture\_WithCaptureSetting()](../harmonyos-references/capi-photo-output-h.md#oh_photooutput_capture_withcapturesetting)方法，执行拍照任务。

   ```
   1. Camera_ErrorCode NDKCamera::TakePicture(int32_t degree)
   2. {
   3. Camera_ErrorCode ret = CAMERA_OK;
   4. Camera_ImageRotation imageRotation;
   5. bool isMirSupported;
   6. OH_PhotoOutput_IsMirrorSupported(photoOutput_, &isMirSupported);
   7. OH_PhotoOutput_GetPhotoRotation(photoOutput_, degree, &imageRotation);

   9. Camera_PhotoCaptureSetting curPhotoSetting = {
   10. quality : QUALITY_LEVEL_HIGH,
   11. rotation : imageRotation,
   12. mirror : isMirSupported
   13. };
   14. ret = OH_PhotoOutput_Capture_WithCaptureSetting(photoOutput_, curPhotoSetting);
   15. OH_LOG_INFO(LOG_APP, "TakePicture get quality %{public}d, rotation %{public}d, mirror %{public}d",
   16. curPhotoSetting.quality, curPhotoSetting.rotation, curPhotoSetting.mirror);
   17. OH_LOG_INFO(LOG_APP, "TakePicture ret = %{public}d.", ret);
   18. return ret;
   19. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1059-L1079)

## 高性能拍照

从API version 21开始支持高性能拍照功能，即在进行单段式拍照时设置明确的[画质优先策略](native-camera-shooting.md#画质优先策略)。

单段式拍照的体验主要由出图速度和最终图片质量衡量。因此，为满足开发者在不同场景下的差异化需求，对这两项指标的侧重也不同。例如，街头抓拍要求快速捕捉瞬间，而风景或人像拍摄则更追求极致的画质。

注意

仅单段式拍照支持设置画质优先策略。若在分段式拍照中设置画质优先策略，该设置将无效。

### 画质优先策略

在使用单段式拍照时，支持设置速度优先和画质优先两种画质优先策略类型，并且分别对应着不同的[Camera\_PhotoQualityPrioritization](../harmonyos-references/capi-camera-h.md#camera_photoqualityprioritization)枚举类型。

* [CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_SPEED](../harmonyos-references/capi-camera-h.md#camera_photoqualityprioritization)对应着速度优先，表示降低画质来提升拍照的速度。如果开发者在进行单段式拍照时没有设置明确的画质优先策略，**单段式拍照就默认为速度优先状态**。
* [CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_HIGH\_QUALITY](../harmonyos-references/capi-camera-h.md#camera_photoqualityprioritization)对应着画质优先，表示通过较长的耗时来得到画质更高的图片。

### 如何正确设置画质优先策略

为了正确的在单段式拍照中设置画质优先策略，高性能拍照功能提供了如下两个接口：

* [OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported](../harmonyos-references/capi-photo-output-h.md#oh_photooutput_isphotoqualityprioritizationsupported)：查询当前设备是否支持指定的画质优先策略。返回true表示支持，返回false表示不支持。在进行设置画质优先策略之前，必须先查询将要设置的画质优先策略在当前设备上是否可用。
* [OH\_PhotoOutput\_SetPhotoQualityPrioritization](../harmonyos-references/capi-photo-output-h.md#oh_photooutput_setphotoqualityprioritization)：画质优先策略设置接口，通过该接口设置对应的画质优先策略，实现高性能拍照。

### 开发步骤

高性能拍照相关接口需要在[会话管理(C/C++)](native-camera-session-management.md)流程的使能步骤中进行调用。

具体调用时机如下：

* 在[会话管理(C/C++)](native-camera-session-management.md)流程中的使能步骤中的[OH\_CaptureSession\_CommitConfig()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)结束之后进行调用。

  ```
  1. Camera_ErrorCode StartSession(Camera_CaptureSession* captureSession, Camera_Input* cameraInput,
  2. Camera_PreviewOutput* previewOutput, Camera_PhotoOutput* photoOutput)
  3. {
  4. // 向会话中添加相机输入流。
  5. Camera_ErrorCode ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
  6. if (ret != CAMERA_OK) {
  7. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
  8. return ret;
  9. }

  11. // 向会话中添加预览输出流。
  12. ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
  13. if (ret != CAMERA_OK) {
  14. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
  15. return ret;
  16. }

  18. // 向会话中添加拍照输出流。
  19. ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
  20. if (ret != CAMERA_OK) {
  21. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
  22. return ret;
  23. }

  25. // 提交会话配置。
  26. ret = OH_CaptureSession_CommitConfig(captureSession);
  27. if (ret != CAMERA_OK) {
  28. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
  29. return ret;
  30. }

  32. // 启动会话。
  33. ret = OH_CaptureSession_Start(captureSession);
  34. if (ret != CAMERA_OK) {
  35. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
  36. }

  38. SetHighQualityPhotoQualityPrioritization(photoOutput);
  39. return ret;
  40. }

  42. void SetHighQualityPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput)
  43. {
  44. Camera_PhotoQualityPrioritization quality = Camera_PhotoQualityPrioritization::CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY;
  45. bool isSupported = false;
  46. Camera_ErrorCode ret = OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
  47. if (isSupported) {
  48. ret = OH_PhotoOutput_SetPhotoQualityPrioritization(photoOutput, quality);
  49. if (ret != 0) {
  50. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_SetPhotoQualityPrioritization failed.");
  51. }
  52. } else {
  53. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_IsPhotoQualityPrioritizationSupported not supported.");
  54. }
  55. }
  ```
* 在[会话管理(C/C++)](native-camera-session-management.md)流程中的使能步骤中的[OH\_CaptureSession\_CommitConfig()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)之前调用。

  ```
  1. Camera_ErrorCode StartSession(Camera_CaptureSession* captureSession, Camera_Input* cameraInput,
  2. Camera_PreviewOutput* previewOutput, Camera_PhotoOutput* photoOutput)
  3. {
  4. // 向会话中添加相机输入流。
  5. Camera_ErrorCode ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
  6. if (ret != CAMERA_OK) {
  7. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
  8. return ret;
  9. }

  11. // 向会话中添加预览输出流。
  12. ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
  13. if (ret != CAMERA_OK) {
  14. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
  15. return ret;
  16. }

  18. // 向会话中添加拍照输出流。
  19. ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
  20. if (ret != CAMERA_OK) {
  21. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
  22. return ret;
  23. }

  25. SetHighQualityPhotoQualityPrioritization(photoOutput);

  27. // 提交会话配置。
  28. ret = OH_CaptureSession_CommitConfig(captureSession);
  29. if (ret != CAMERA_OK) {
  30. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
  31. return ret;
  32. }

  34. // 启动会话。
  35. ret = OH_CaptureSession_Start(captureSession);
  36. if (ret != CAMERA_OK) {
  37. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
  38. }

  40. return ret;
  41. }

  43. void SetHighQualityPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput)
  44. {
  45. Camera_PhotoQualityPrioritization quality = Camera_PhotoQualityPrioritization::CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY;
  46. bool isSupported = false;
  47. Camera_ErrorCode ret = OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
  48. if (isSupported) {
  49. ret = OH_PhotoOutput_SetPhotoQualityPrioritization(photoOutput, quality);
  50. if (ret != 0) {
  51. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_SetPhotoQualityPrioritization failed.");
  52. }
  53. } else {
  54. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_IsPhotoQualityPrioritizationSupported not supported.");
  55. }
  56. }
  ```

## 状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍照输出流的错误。

* 通过注册固定的onFrameStart回调函数获取监听拍照开始结果，photoOutput创建成功时即可监听，拍照第一次曝光时触发。

  ```
  1. // PhotoOutput Callback
  2. void PhotoOutputOnFrameStart(Camera_PhotoOutput *photoOutput)
  3. {
  4. OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameStart");
  5. }

  7. void PhotoOutputOnFrameShutter(Camera_PhotoOutput *photoOutput, Camera_FrameShutterInfo *info)
  8. {
  9. OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameShutter");
  10. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1170-L1181)
* 通过注册固定的onFrameEnd回调函数获取监听拍照结束结果，photoOutput创建成功时即可监听。

  ```
  1. void PhotoOutputOnFrameEnd(Camera_PhotoOutput *photoOutput, int32_t frameCount)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PhotoOutput frameCount = %{public}d", frameCount);
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1183-L1188)
* 通过注册固定的onError回调函数获取监听拍照输出流的错误结果。callback返回拍照输出接口使用错误时的对应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  1. void PhotoOutputOnError(Camera_PhotoOutput *photoOutput, Camera_ErrorCode errorCode)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PhotoOutput errorCode = %{public}d", errorCode);
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1190-L1195)

  ```
  1. PhotoOutput_Callbacks *NDKCamera::GetPhotoOutputListener(void)
  2. {
  3. static PhotoOutput_Callbacks photoOutputListener = {
  4. .onFrameStart = PhotoOutputOnFrameStart,
  5. .onFrameShutter = PhotoOutputOnFrameShutter,
  6. .onFrameEnd = PhotoOutputOnFrameEnd,
  7. .onError = PhotoOutputOnError
  8. };
  9. return &photoOutputListener;
  10. }

  12. Camera_ErrorCode NDKCamera::PhotoOutputRegisterCallback(void)
  13. {
  14. ret_ = OH_PhotoOutput_RegisterCallback(photoOutput_, GetPhotoOutputListener());
  15. if (ret_ != CAMERA_OK) {
  16. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_RegisterCallback failed.");
  17. }
  18. return ret_;
  19. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1197-L1217)
