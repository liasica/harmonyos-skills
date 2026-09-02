---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview
title: 预览(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 预览(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ed3a5e9660b73ddb5f54ee4a3c232facb06aad9c0edc2dad9de68938032f2c40
---

预览是启动相机后看见的画面，通常在拍照和录像前执行。

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

   XComponent组件为预览流提供的SurfaceId，而XComponent的能力由UI提供，相关介绍可参考[XComponent组件参考](../harmonyos-references/ts-basic-components-xcomponent.md)。
4. 根据传入的SurfaceId，通过[OH\_CameraManager\_GetSupportedCameraOutputCapability()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)方法获取当前设备支持的预览能力。通过[OH\_CameraManager\_CreatePreviewOutput()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createpreviewoutput)方法创建预览输出流，其中，OH\_CameraManager\_CreatePreviewOutput()方法中的参数分别是cameraManager指针，previewProfiles数组中的第一项，步骤三中获取的surfaceId，以及返回的previewOutput指针。

   ```
   Camera_ErrorCode NDKCamera::CreatePreviewOutput(void)
   {
       if (previewProfile_ == nullptr) {
           OH_LOG_ERROR(LOG_APP, "Get previewProfiles failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       ret_ = OH_CameraManager_CreatePreviewOutput(cameraManager_, previewProfile_, previewSurfaceId_, &previewOutput_);
       OH_LOG_ERROR(LOG_APP, "create preview width: %{public}d, height: %{public}d, format: %{public}d",
           previewProfile_->size.width, previewProfile_->size.height, previewProfile_->format);
       if (previewSurfaceId_ == nullptr || previewOutput_ == nullptr || ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "CreatePreviewOutput failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       PreviewOutputRegisterCallback();
       return ret_;
   }
   ```
5. 使能。当session完成CommitConfig后通过调用[OH\_CaptureSession\_Start()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_start)方法输出预览流，接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

   ```
   Camera_ErrorCode NDKCamera::SessionStart(void)
   {
       Camera_ErrorCode ret = OH_CaptureSession_Start(captureSession_);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Start success.");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed. %d ", ret);
       }
       return ret;
   }
   ```
6. 通过[OH\_CaptureSession\_Stop()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_stop)方法停止预览流，接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

   ```
   Camera_ErrorCode NDKCamera::SessionStop(void)
   {
       Camera_ErrorCode ret = OH_CaptureSession_Stop(captureSession_);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success.");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. %d ", ret);
       }
       return ret;
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听预览输出流状态，包括预览流启动、预览流结束、预览流输出错误。

* 通过注册固定的frameStart回调函数获取监听预览启动结果，previewOutput创建成功时即可监听，预览第一次曝光时触发，有该事件返回结果则认为预览流已启动。

  ```
  void PreviewOutputOnFrameStart(Camera_PreviewOutput *previewOutput)
  {
      OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
  }
  ```
* 通过注册固定的frameEnd回调函数获取监听预览结束结果，previewOutput创建成功时即可监听，预览完成最后一帧时触发，有该事件返回结果则认为预览流已结束。

  ```
  void PreviewOutputOnFrameEnd(Camera_PreviewOutput *previewOutput, int32_t frameCount)
  {
      OH_LOG_INFO(LOG_APP, "PreviewOutput frameCount = %{public}d", frameCount);
  }
  ```
* 通过注册固定的error回调函数获取监听预览输出错误结果，callback返回预览输出接口使用错误时对应的错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  void PreviewOutputOnError(Camera_PreviewOutput *previewOutput, Camera_ErrorCode errorCode)
  {
      OH_LOG_INFO(LOG_APP, "PreviewOutput errorCode = %{public}d", errorCode);
  }
  ```

  ```
  PreviewOutput_Callbacks *NDKCamera::GetPreviewOutputListener(void)
  {
      static PreviewOutput_Callbacks previewOutputListener = {
          .onFrameStart = PreviewOutputOnFrameStart,
          .onFrameEnd = PreviewOutputOnFrameEnd,
          .onError = PreviewOutputOnError
      };
      return &previewOutputListener;
  }

  Camera_ErrorCode NDKCamera::PreviewOutputRegisterCallback(void)
  {
      ret_ = OH_PreviewOutput_RegisterCallback(previewOutput_, GetPreviewOutputListener());
      if (ret_ != CAMERA_OK) {
          OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
      }
      return ret_;
  }
  ```
