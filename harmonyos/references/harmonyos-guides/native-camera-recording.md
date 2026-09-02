---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-recording
title: 录像(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 录像(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:39dca0fc68b4b52eabad8d585f35887bdc50c8f1f229a902bf199d95810bb216
---

录像是循环帧的捕获，同时也是相机应用的最重要功能之一。对于录像的流畅度，开发者可以参考拍照(C/C++)中的[开发步骤](native-camera-shooting.md#开发步骤)7，设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```c
   #include <cstdint>
   #include <native_buffer/buffer_common.h>
   #include <unistd.h>
   #include <string>
   #include <thread>
   #include <cstdio>
   #include <fcntl.h>
   #include <map>
   #include <string>
   #include <vector>
   #include <native_buffer/native_buffer.h>
   #include "iostream"
   #include "mutex"

   #include "hilog/log.h"
   #include "ohcamera/camera.h"
   #include "ohcamera/camera_input.h"
   #include "ohcamera/capture_session.h"
   #include "ohcamera/photo_output.h"
   #include "ohcamera/preview_output.h"
   #include "ohcamera/video_output.h"
   #include "napi/native_api.h"
   #include "ohcamera/camera_manager.h"
   #include <window_manager/oh_display_info.h>
   #include <window_manager/oh_display_manager.h>

   namespace OHOS_CAMERA_SAMPLE {
   class NDKCamera {
     public:
       struct CameraBuildingConfig {
           char *str;
           uint32_t focusMode;
           uint32_t cameraDeviceIndex;
           bool isVideo;
           bool isHdr;
           char *videoId;
       };
       ~NDKCamera();
       explicit NDKCamera(CameraBuildingConfig config);
       // ...
   };
   } // namespace OHOS_CAMERA_SAMPLE
   ```
2. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC
       libace_napi.z.so
       libohcamera.so
       libhilog_ndk.z.so
   )
   ```
3. 获取SurfaceId。

   系统提供的[OH\_AVRecorder\_Create()](../harmonyos-references/capi-avrecorder-h.md#oh_avrecorder_create)接口可以创建一个录像AVRecorder实例，通过该实例的[OH\_AVRecorder\_GetInputSurface()](../harmonyos-references/capi-avrecorder-h.md#oh_avrecorder_getinputsurface)方法获取SurfaceId。
4. 创建录像输出流。

   根据传入的SurfaceId，通过[OH\_CameraManager\_GetSupportedCameraOutputCapability](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)接口获取[Camera\_OutputCapability](../harmonyos-references/capi-oh-camera-camera-outputcapability.md)能力，可以通过[Camera\_OutputCapability](../harmonyos-references/capi-oh-camera-camera-outputcapability.md)中的videoProfiles，获取当前设备支持的录像输出流。然后，定义创建录像的参数，通过OH\_CameraManager\_CreateVideoOutput方法创建录像输出流。

   **说明** 

   * 预览流与录像输出流的分辨率的宽高比要保持一致。如示例代码中宽高比为640:480 = 4:3，则需要预览流中的分辨率的宽高比也为4:3，可选择的分辨率有：640:480、960:720、1440:1080等。
   * 在设置预览输出流的分辨率宽高前，需要先通过[OH\_AVRecorder\_Profile](../harmonyos-references/capi-avrecorder-oh-avrecorder-profile.md)查询视频帧支持可配置的宽高范围。

   ```
   Camera_ErrorCode NDKCamera::CreateVideoOutput(char *videoId)
   {
       if (videoProfile_ == nullptr) {
           OH_LOG_ERROR(LOG_APP, "Get videoProfiles failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       ret_ = OH_CameraManager_CreateVideoOutput(cameraManager_, videoProfile_, videoId, &videoOutput_);
       OH_LOG_ERROR(LOG_APP, " create video width: %{public}d, height: %{public}d, format: %{public}d",
           videoProfile_->size.width, videoProfile_->size.height, videoProfile_->format);
       if (videoId == nullptr || videoOutput_ == nullptr || ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "CreateVideoOutput failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       VideoOutputRegisterCallback();
       return ret_;
   }
   ```
5. 开始录像。

   通过[OH\_VideoOutput\_Start()](../harmonyos-references/capi-video-output-h.md#oh_videooutput_start)方法启动录像输出流。

   ```
   Camera_ErrorCode NDKCamera::VideoOutputStart(void)
   {
       OH_LOG_INFO(LOG_APP, "VideoOutputStart begin.");
       Camera_ErrorCode ret = OH_VideoOutput_Start(videoOutput_);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_VideoOutput_Start success.");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_Start failed. %d ", ret);
       }
       return ret;
   }
   ```
6. 停止录像。

   通过[OH\_VideoOutput\_Stop()](../harmonyos-references/capi-video-output-h.md#oh_videooutput_stop)方法停止录像输出流。

   ```
   Camera_ErrorCode NDKCamera::VideoOutputStop(void)
   {
       OH_LOG_ERROR(LOG_APP, "enter VideoOutputStop.");
       ret_ = OH_VideoOutput_Stop(videoOutput_);
       if (ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "VideoOutputStop failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       return ret_;
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听录像输出流状态，包括录像开始、录像结束、录像流输出的错误。

* 通过注册固定的frameStart回调函数获取监听录像开始结果，videoOutput创建成功时即可监听，录像第一次曝光时触发，当触发该事件回调时表示录像已开始。

  ```
  void VideoOutputOnFrameStart(Camera_VideoOutput *videoOutput)
  {
      OH_LOG_INFO(LOG_APP, "VideoOutputOnFrameStart");
  }
  ```
* 通过注册固定的frameEnd回调函数获取监听录像结束结果，videoOutput创建成功时即可监听，录像完成最后一帧时触发，有该事件返回结果则认为录像流已结束。

  ```
  void VideoOutputOnFrameEnd(Camera_VideoOutput *videoOutput, int32_t frameCount)
  {
      OH_LOG_INFO(LOG_APP, "VideoOutput frameCount = %{public}d", frameCount);
  }
  ```
* 通过注册固定的error回调函数获取监听录像输出错误结果，callback返回录像输出接口使用错误时对应的错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  void VideoOutputOnError(Camera_VideoOutput *videoOutput, Camera_ErrorCode errorCode)
  {
      OH_LOG_INFO(LOG_APP, "VideoOutput errorCode = %{public}d", errorCode);
  }
  ```

  ```
  VideoOutput_Callbacks *NDKCamera::GetVideoOutputListener(void)
  {
      static VideoOutput_Callbacks videoOutputListener = {
          .onFrameStart = VideoOutputOnFrameStart,
          .onFrameEnd = VideoOutputOnFrameEnd,
          .onError = VideoOutputOnError
      };
      return &videoOutputListener;
  }

  Camera_ErrorCode NDKCamera::VideoOutputRegisterCallback(void)
  {
      ret_ = OH_VideoOutput_RegisterCallback(videoOutput_, GetVideoOutputListener());
      if (ret_ != CAMERA_OK) {
          OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_RegisterCallback failed.");
      }
      return ret_;
  }
  ```
