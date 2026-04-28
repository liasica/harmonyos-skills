---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview
title: 预览(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 预览(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b8ba480eb0c973a30b2faa8e3817fd3936d9486c9296c20808ca8033754d0f3
---

预览是启动相机后看见的画面，通常在拍照和录像前执行。

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
   3. libohcamera.so
   4. libhilog_ndk.z.so
   5. )
   ```
3. 获取SurfaceId。

   XComponent组件为预览流提供的SurfaceId，而XComponent的能力由UI提供，相关介绍可参考[XComponent组件参考](../harmonyos-references/ts-basic-components-xcomponent.md)。
4. 根据传入的SurfaceId，通过[OH\_CameraManager\_GetSupportedCameraOutputCapability()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)方法获取当前设备支持的预览能力。通过[OH\_CameraManager\_CreatePreviewOutput()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createpreviewoutput)方法创建预览输出流，其中，OH\_CameraManager\_CreatePreviewOutput()方法中的参数分别是cameraManager指针，previewProfiles数组中的第一项，步骤三中获取的surfaceId，以及返回的previewOutput指针。

   ```
   1. Camera_ErrorCode NDKCamera::CreatePreviewOutput(void)
   2. {
   3. if (previewProfile_ == nullptr) {
   4. OH_LOG_ERROR(LOG_APP, "Get previewProfiles failed.");
   5. return CAMERA_INVALID_ARGUMENT;
   6. }
   7. ret_ = OH_CameraManager_CreatePreviewOutput(cameraManager_, previewProfile_, previewSurfaceId_, &previewOutput_);
   8. OH_LOG_ERROR(LOG_APP, "create preview width: %{public}d, height: %{public}d, format: %{public}d",
   9. previewProfile_->size.width, previewProfile_->size.height, previewProfile_->format);
   10. if (previewSurfaceId_ == nullptr || previewOutput_ == nullptr || ret_ != CAMERA_OK) {
   11. OH_LOG_ERROR(LOG_APP, "CreatePreviewOutput failed.");
   12. return CAMERA_INVALID_ARGUMENT;
   13. }
   14. return ret_;
   15. PreviewOutputRegisterCallback();
   16. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L456-L473)
5. 使能。当session完成CommitConfig后通过调用[OH\_CaptureSession\_Start()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_start)方法输出预览流，接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

   ```
   1. Camera_ErrorCode NDKCamera::SessionStart(void)
   2. {
   3. Camera_ErrorCode ret = OH_CaptureSession_Start(captureSession_);
   4. if (ret == CAMERA_OK) {
   5. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Start success.");
   6. } else {
   7. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed. %d ", ret);
   8. }
   9. return ret;
   10. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L234-L245)
6. 通过[OH\_CaptureSession\_Stop()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_stop)方法停止预览流，接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

   ```
   1. Camera_ErrorCode NDKCamera::SessionStop(void)
   2. {
   3. Camera_ErrorCode ret = OH_CaptureSession_Stop(captureSession_);
   4. if (ret == CAMERA_OK) {
   5. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success.");
   6. } else {
   7. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. %d ", ret);
   8. }
   9. return ret;
   10. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L247-L258)

## 状态监听

在相机应用开发过程中，可以随时监听预览输出流状态，包括预览流启动、预览流结束、预览流输出错误。

* 通过注册固定的frameStart回调函数获取监听预览启动结果，previewOutput创建成功时即可监听，预览第一次曝光时触发，有该事件返回结果则认为预览流已启动。

  ```
  1. void PreviewOutputOnFrameStart(Camera_PreviewOutput *previewOutput)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1128-L1133)
* 通过注册固定的frameEnd回调函数获取监听预览结束结果，previewOutput创建成功时即可监听，预览完成最后一帧时触发，有该事件返回结果则认为预览流已结束。

  ```
  1. void PreviewOutputOnFrameEnd(Camera_PreviewOutput *previewOutput, int32_t frameCount)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PreviewOutput frameCount = %{public}d", frameCount);
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1135-L1140)
* 通过注册固定的error回调函数获取监听预览输出错误结果，callback返回预览输出接口使用错误时对应的错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  1. void PreviewOutputOnError(Camera_PreviewOutput *previewOutput, Camera_ErrorCode errorCode)
  2. {
  3. OH_LOG_INFO(LOG_APP, "PreviewOutput errorCode = %{public}d", errorCode);
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1142-L1147)

  ```
  1. PreviewOutput_Callbacks *NDKCamera::GetPreviewOutputListener(void)
  2. {
  3. static PreviewOutput_Callbacks previewOutputListener = {
  4. .onFrameStart = PreviewOutputOnFrameStart,
  5. .onFrameEnd = PreviewOutputOnFrameEnd,
  6. .onError = PreviewOutputOnError
  7. };
  8. return &previewOutputListener;
  9. }

  11. Camera_ErrorCode NDKCamera::PreviewOutputRegisterCallback(void)
  12. {
  13. ret_ = OH_PreviewOutput_RegisterCallback(previewOutput_, GetPreviewOutputListener());
  14. if (ret_ != CAMERA_OK) {
  15. OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
  16. }
  17. return ret_;
  18. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1149-L1168)
