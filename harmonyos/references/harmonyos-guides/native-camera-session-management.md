---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management
title: 会话管理(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(C/C++) > 会话管理(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:932f4d95792160402bb50612cbed231826c7ce4fa19e5f06f8015e64c9572795
---

相机使用预览、拍照、录像、元数据功能前，均需要创建相机会话。

在会话中，可以完成以下功能：

* 配置相机的输入流和输出流。相机在拍摄前，必须完成输入输出流的配置。

  配置输入流即添加设备输入，对用户而言，相当于选择设备的某一相机拍摄；配置输出流，即选择数据将以什么形式输出。当应用需要实现拍照时，输出流应配置为预览流和拍照流，预览流的数据将显示在XComponent组件上，拍照流的数据将通过ImageReceiver接口的能力保存到相册中。
* 添加闪光灯、调整焦距等配置。具体支持的配置及接口说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。
* 会话切换控制。应用可以通过移除和添加输出流的方式，切换相机模式。如当前会话的输出流为拍照流，应用可以将拍照流移除，然后添加视频流作为输出流，即完成了拍照到录像的切换。

完成会话配置后，应用提交和开启会话，可以开始调用相机相关功能。

## 开发步骤

1. 导入NDK相关接口，导入方法如下。

   ```
   #include "hilog/log.h"
   #include "ohcamera/camera.h"
   #include "ohcamera/camera_input.h"
   #include "ohcamera/capture_session.h"
   #include "ohcamera/photo_output.h"
   #include "ohcamera/preview_output.h"
   #include "ohcamera/video_output.h"
   #include "ohcamera/camera_manager.h"
   ```
2. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC
       libace_napi.z.so
       libohcamera.so
       libhilog_ndk.z.so
   )
   ```
3. 调用[OH\_CameraManager\_CreateCaptureSession()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createcapturesession)方法创建一个会话。

   ```
   Camera_CaptureSession* CreateCaptureSession(Camera_Manager* cameraManager)
   {
       Camera_CaptureSession* captureSession = nullptr;
       if (cameraManager == nullptr) {
           OH_LOG_ERROR(LOG_APP, "cameraManager is nullptr.");
           return captureSession;
       }
       Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
       if (captureSession == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
       }
       return captureSession;
   }
   ```
4. 调用[OH\_CaptureSession\_SetSessionMode()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setsessionmode)方法配置会话模式。

   ```
   Camera_ErrorCode SetSessionMode(Camera_CaptureSession* captureSession)
   {
       Camera_ErrorCode ret = OH_CaptureSession_SetSessionMode(captureSession, NORMAL_VIDEO);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetSessionMode failed.");
       }
       return ret;
   }
   ```
5. 调用[OH\_CaptureSession\_BeginConfig()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_beginconfig)方法配置会话。

   ```
   Camera_ErrorCode BeginConfig(Camera_CaptureSession* captureSession)
   {
       Camera_ErrorCode ret = OH_CaptureSession_BeginConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
       }
       return ret;
   }
   ```
6. 使能。向会话中添加相机的输入流和输出流，调用[OH\_CaptureSession\_AddInput()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_addinput)添加相机的输入流；调用[OH\_CaptureSession\_AddPreviewOutput()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_addpreviewoutput)和[OH\_CaptureSession\_AddPhotoOutput()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_addphotooutput)添加相机的输出流。以下示例代码以添加预览流previewOutput和拍照流photoOutput为例，即当前模式支持拍照和预览。

   调用[OH\_CaptureSession\_CommitConfig()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)和[OH\_CaptureSession\_Start()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_start)方法提交相关配置，并启动会话。

   ```
   Camera_ErrorCode StartSession(Camera_CaptureSession* captureSession, Camera_Input* cameraInput,
       Camera_PreviewOutput* previewOutput, Camera_PhotoOutput* photoOutput)
   {
       // 向会话中添加相机输入流。
       Camera_ErrorCode ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
           return ret;
       }

       // 向会话中添加预览输出流。
       ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
           return ret;
       }

       // 向会话中添加拍照输出流。
       ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
           return ret;
       }

       // 提交会话配置。
       ret = OH_CaptureSession_CommitConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
           return ret;
       }

       // 启动会话。
       ret = OH_CaptureSession_Start(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
       }
       return ret;
   }
   ```
7. 会话控制。调用[OH\_CaptureSession\_Stop()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_stop)方法可以停止当前会话。调用[OH\_CaptureSession\_RemovePhotoOutput()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_removephotooutput)和[OH\_CaptureSession\_AddVideoOutput()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_addvideooutput)方法可以完成会话切换控制。以下示例代码以移除拍照流photoOutput，添加视频流videoOutput为例，完成了拍照到录像的切换。

   ```
   Camera_ErrorCode ReloadSession(Camera_CaptureSession* captureSession, Camera_PhotoOutput* photoOutput,
       Camera_VideoOutput* videoOutput)
   {
       Camera_ErrorCode ret = OH_CaptureSession_Stop(captureSession);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. %d ", ret);
       }
       ret = OH_CaptureSession_BeginConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
           return ret;
       }
       // 从会话中移除拍照输出流。
       ret = OH_CaptureSession_RemovePhotoOutput(captureSession, photoOutput);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_RemovePhotoOutput success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RemovePhotoOutput failed. %d ", ret);
       }
       // 释放photoOutput。
       ret = OH_PhotoOutput_Release(photoOutput);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Release success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Release failed. %d ", ret);
       }
       // 向会话中添加视频输出流。
       ret = OH_CaptureSession_AddVideoOutput(captureSession, videoOutput);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_AddVideoOutput success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddVideoOutput failed. %d ", ret);
           return ret;
       }
       // 提交会话配置。
       ret = OH_CaptureSession_CommitConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
           return ret;
       }

       // 启动会话。
       ret = OH_CaptureSession_Start(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
       }
       return ret;
   }
   ```
