---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-metadata
title: 元数据(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 元数据(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0bb15cb83cd6197fd01016dc699f006768d3aaa4c27695c41926a1fa9a730fab
---

元数据（Metadata）是对相机返回的图像信息的描述和上下文。针对图像信息，提供更详细的数据，如照片或视频中，识别人像的取景框坐标等信息。

Metadata主要是通过一个TAG（Key），去找对应的Data（Value），用于传递参数和配置信息，减少内存拷贝操作。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，导入方法如下。

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
3. 调用OH\_CameraManager\_GetSupportedCameraOutputCapability()方法，获取当前设备支持的元数据类型metaDataObjectType，并通过OH\_CameraManager\_CreateMetadataOutput()方法创建元数据输出流。

   ```
   Camera_ErrorCode NDKCamera::CreateMetadataOutput(void)
   {
       metaDataObjectType_ = cameraOutputCapability_->supportedMetadataObjectTypes[0];
       if (metaDataObjectType_ == nullptr) {
           OH_LOG_ERROR(LOG_APP, "Get metaDataObjectType failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       ret_ = OH_CameraManager_CreateMetadataOutput(cameraManager_, metaDataObjectType_, &metadataOutput_);
       if (metadataOutput_ == nullptr || ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "CreateMetadataOutput failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       MetadataOutputRegisterCallback();
       return ret_;
   }
   ```
4. 调用[OH\_CameraManager\_CreateCaptureSession()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createcapturesession)方法创建一个会话。

   ```
   ret = OH_CameraManager_CreateCaptureSession(cameraManager_, &captureSession_);
   if (captureSession_ == nullptr || ret != CAMERA_OK) {
       OH_LOG_ERROR(LOG_APP, "Create captureSession failed.");
   }
   ```
5. 配置session，完成后通过调用[OH\_CaptureSession\_Start()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_start)方法输出metadata数据。接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

   ```
   // 开始配置会话。
   Camera_ErrorCode ret = OH_CaptureSession_BeginConfig(captureSession_);

   // 将相机输入流加入会话。
   ret = OH_CaptureSession_AddInput(captureSession_, cameraInput_);

   // 将相机预览流加入会话。
   ret = OH_CaptureSession_AddPreviewOutput(captureSession_, previewOutput_);

   if (isVideo_) {
       // 将相机录像流加入会话。
       AddVideoOutput();
       if (isHdrVideo) {
           // HDR Vivid视频需要设置色彩空间为OH_COLORSPACE_BT2020_HLG_LIMIT。
           OH_NativeBuffer_ColorSpace colorSpace = OH_NativeBuffer_ColorSpace::OH_COLORSPACE_BT2020_HLG_LIMIT;
           SetColorSpace(colorSpace);
       }
   } else {
       // 将相机拍照流加入会话。
       AddPhotoOutput();
       ret = CreateMetadataOutput();
       ret = OH_CaptureSession_AddMetadataOutput(captureSession_, metadataOutput_);
       OH_NativeBuffer_ColorSpace colorSpace = OH_NativeBuffer_ColorSpace::OH_COLORSPACE_P3_FULL;
       SetColorSpace(colorSpace);
   }

   // 提交会话配置信息。
   ret = OH_CaptureSession_CommitConfig(captureSession_);
   // ...

   InitPreviewRotation();
   // 开始会话。
   OH_LOG_INFO(LOG_APP, "session start");
   ret = OH_CaptureSession_Start(captureSession_);
   ```
6. 调用[OH\_MetadataOutput\_Stop()](../harmonyos-references/capi-metadata-output-h.md#oh_metadataoutput_stop)方法停止输出metadata数据，接口调用失败会返回相应错误码。

   ```
   Camera_ErrorCode StopMetadataOutput(Camera_MetadataOutput* metadataOutput)
   {
       Camera_ErrorCode ret = OH_MetadataOutput_Stop(metadataOutput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_MetadataOutput_Stop failed.");
       }
       return ret;
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听metadata数据以及输出流的状态。

* 通过注册监听获取metadata对象，监听事件固定为metadataObjectsAvailable。检测到有效metadata数据时，callback返回相应的metadata数据信息，metadataOutput创建成功时可监听。

  ```
  void OnMetadataObjectAvailable(Camera_MetadataOutput *metadataOutput, Camera_MetadataObject *metadataObject,
      uint32_t size)
  {
      OH_LOG_INFO(LOG_APP, "size = %{public}d", size);
  }
  ```

  **说明** 

  当前的元数据类型仅支持人脸检测（FACE\_DETECTION）功能。元数据信息对象为识别到的人脸区域的矩形信息（Rect），包含矩形区域的左上角x坐标、y坐标和矩形的宽高数据。
* 通过注册回调函数，获取监听metadata流的错误结果，callback返回metadata输出接口使用错误时返回的错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  void OnMetadataOutputError(Camera_MetadataOutput *metadataOutput, Camera_ErrorCode errorCode)
  {
      OH_LOG_INFO(LOG_APP, "OnMetadataOutput errorCode = %{public}d", errorCode);
  }
  ```

  ```
  MetadataOutput_Callbacks *NDKCamera::GetMetadataOutputListener(void)
  {
      static MetadataOutput_Callbacks metadataOutputListener = {
          .onMetadataObjectAvailable = OnMetadataObjectAvailable,
          .onError = OnMetadataOutputError
      };
      return &metadataOutputListener;
  }

  Camera_ErrorCode NDKCamera::MetadataOutputRegisterCallback(void)
  {
      ret_ = OH_MetadataOutput_RegisterCallback(metadataOutput_, GetMetadataOutputListener());
      if (ret_ != CAMERA_OK) {
          OH_LOG_ERROR(LOG_APP, "OH_MetadataOutput_RegisterCallback failed.");
      }
      return ret_;
  }
  ```
