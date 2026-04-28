---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-recording
title: 录像(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 录像(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3be8787163cab478e07228798600e80a7a89cc44d04eeeaff7166eb4760dc2dc
---

录像也是相机应用的最重要功能之一，录像是循环帧的捕获。对于录像的流畅度，开发者可以参考[拍照参考](native-camera-shooting.md)中的步骤5，设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

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

   系统提供的[OH\_AVRecorder\_Create()](../harmonyos-references/capi-avrecorder-h.md#oh_avrecorder_create)接口可以创建一个录像AVRecorder实例，通过该实例的[OH\_AVRecorder\_GetInputSurface()](../harmonyos-references/capi-avrecorder-h.md#oh_avrecorder_getinputsurface)方法获取SurfaceId。
4. 创建录像输出流。

   根据传入的SurfaceId，通过[OH\_CameraManager\_GetSupportedCameraOutputCapability](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)接口获取[Camera\_OutputCapability](../harmonyos-references/capi-oh-camera-camera-outputcapability.md)能力，可以通过[Camera\_OutputCapability](../harmonyos-references/capi-oh-camera-camera-outputcapability.md)中的videoProfiles，获取当前设备支持的录像输出流。然后，定义创建录像的参数，通过OH\_CameraManager\_CreateVideoOutput方法创建录像输出流。

   说明

   * 预览流与录像输出流的分辨率的宽高比要保持一致。如示例代码中宽高比为640:480 = 4:3，则需要预览流中的分辨率的宽高比也为4:3，可选择的分辨率有：640:480、960:720、1440:1080等。
   * 在设置预览输出流的分辨率宽高前，需要先通过[OH\_AVRecorder\_Profile](../harmonyos-references/capi-avrecorder-oh-avrecorder-profile.md)查询视频帧支持可配置的宽高范围。

   ```
   1. Camera_ErrorCode NDKCamera::CreateVideoOutput(char *videoId)
   2. {
   3. if (videoProfile_ == nullptr) {
   4. OH_LOG_ERROR(LOG_APP, "Get videoProfiles failed.");
   5. return CAMERA_INVALID_ARGUMENT;
   6. }
   7. ret_ = OH_CameraManager_CreateVideoOutput(cameraManager_, videoProfile_, videoId, &videoOutput_);
   8. OH_LOG_ERROR(LOG_APP, " create video width: %{public}d, height: %{public}d, format: %{public}d",
   9. videoProfile_->size.width, videoProfile_->size.height, videoProfile_->format);
   10. if (videoId == nullptr || videoOutput_ == nullptr || ret_ != CAMERA_OK) {
   11. OH_LOG_ERROR(LOG_APP, "CreateVideoOutput failed.");
   12. return CAMERA_INVALID_ARGUMENT;
   13. }
   14. VideoOutputRegisterCallback();
   15. return ret_;
   16. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L501-L518)
5. 开始录像。

   通过[OH\_VideoOutput\_Start()](../harmonyos-references/capi-video-output-h.md#oh_videooutput_start)方法启动录像输出流。

   ```
   1. Camera_ErrorCode NDKCamera::VideoOutputStart(void)
   2. {
   3. OH_LOG_INFO(LOG_APP, "VideoOutputStart begin.");
   4. Camera_ErrorCode ret = OH_VideoOutput_Start(videoOutput_);
   5. if (ret == CAMERA_OK) {
   6. OH_LOG_INFO(LOG_APP, "OH_VideoOutput_Start success.");
   7. } else {
   8. OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_Start failed. %d ", ret);
   9. }
   10. return ret;
   11. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L603-L615)
6. 停止录像。

   通过[OH\_VideoOutput\_Stop()](../harmonyos-references/capi-video-output-h.md#oh_videooutput_stop)方法停止录像输出流。

   ```
   1. Camera_ErrorCode NDKCamera::VideoOutputStop(void)
   2. {
   3. OH_LOG_ERROR(LOG_APP, "enter VideoOutputStop.");
   4. ret_ = OH_VideoOutput_Stop(videoOutput_);
   5. if (ret_ != CAMERA_OK) {
   6. OH_LOG_ERROR(LOG_APP, "VideoOutputStop failed.");
   7. return CAMERA_INVALID_ARGUMENT;
   8. }
   9. return ret_;
   10. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1034-L1045)

## 状态监听

在相机应用开发过程中，可以随时监听录像输出流状态，包括录像开始、录像结束、录像流输出的错误。

* 通过注册固定的frameStart回调函数获取监听录像开始结果，videoOutput创建成功时即可监听，录像第一次曝光时触发，当触发该事件回调时表示录像已开始。

  ```
  1. void VideoOutputOnFrameStart(Camera_VideoOutput *videoOutput)
  2. {
  3. OH_LOG_INFO(LOG_APP, "VideoOutputOnFrameStart");
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1221-L1226)
* 通过注册固定的frameEnd回调函数获取监听录像结束结果，videoOutput创建成功时即可监听，录像完成最后一帧时触发，有该事件返回结果则认为录像流已结束。

  ```
  1. void VideoOutputOnFrameEnd(Camera_VideoOutput *videoOutput, int32_t frameCount)
  2. {
  3. OH_LOG_INFO(LOG_APP, "VideoOutput frameCount = %{public}d", frameCount);
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1228-L1233)
* 通过注册固定的error回调函数获取监听录像输出错误结果，callback返回录像输出接口使用错误时对应的错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  1. void VideoOutputOnError(Camera_VideoOutput *videoOutput, Camera_ErrorCode errorCode)
  2. {
  3. OH_LOG_INFO(LOG_APP, "VideoOutput errorCode = %{public}d", errorCode);
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1235-L1240)

  ```
  1. VideoOutput_Callbacks *NDKCamera::GetVideoOutputListener(void)
  2. {
  3. static VideoOutput_Callbacks videoOutputListener = {
  4. .onFrameStart = VideoOutputOnFrameStart,
  5. .onFrameEnd = VideoOutputOnFrameEnd,
  6. .onError = VideoOutputOnError
  7. };
  8. return &videoOutputListener;
  9. }

  11. Camera_ErrorCode NDKCamera::VideoOutputRegisterCallback(void)
  12. {
  13. ret_ = OH_VideoOutput_RegisterCallback(videoOutput_, GetVideoOutputListener());
  14. if (ret_ != CAMERA_OK) {
  15. OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_RegisterCallback failed.");
  16. }
  17. return ret_;
  18. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1242-L1261)
