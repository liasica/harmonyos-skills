---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-concurrent-open
title: 多摄同开(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 多摄同开(C/C++)
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:03+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:47a6e7be1f4be92050f6820b6c4b9d029793fd471ac0da10d237f7e43ccd0c38
---

从API version 18开始支持多摄同开，即应用同时开启前置/后置相机进行预览和录像（前置/后置相机同时拍照功能待开放）。

**说明** 

由于多摄同开需要前置/后置相机同时运行，所以对于相机功能有较大限制。当前版本仅支持以下七项基础功能，请勿对多摄同开开启的相机进行超出以下七种基础功能范围之外的查询、设置和使能。

1. 闪光灯。
2. 曝光。
3. 变焦。
4. 曝光补偿。
5. 对焦。
6. 防抖。
7. 色彩空间。

## 开发步骤

详细的API说明请参考[Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   #include <cstdint>
   #include <unistd.h>
   #include <string>
   #include <thread>
   #include <cstdio>
   #include <fcntl.h>
   #include <map>
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
   ```
2. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC
      libohcamera.so
      libace_napi.z.so
      libnative_buffer.so
      libhilog_ndk.z.so
      librawfile.z.so)
   ```
3. 通过[OH\_CameraManager\_GetCameraDevice](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getcameradevice)方法获取对应的前置相机和后置相机。如果接口返回值为CAMERA\_SERVICE\_FATAL\_ERROR，基于示例中的配置信息，表示当前设备不支持指定位置（前置/后置）的默认类型相机，无法实现多摄同开功能。

   ```
   void NDKCamera::GetSupportedCamerasForConcurrent(Camera_Manager *cameraManager)
   {
       Camera_Device *cameras = nullptr;
       uint32_t size = 0;
       Camera_ErrorCode ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
       int32_t concurrentDeviceSize = 2;
       if (ret != CAMERA_OK || cameras == nullptr || size < concurrentDeviceSize) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
           return;
       }
       // 获取后置相机。
       ret = OH_CameraManager_GetCameraDevice(cameraManager, Camera_Position::CAMERA_POSITION_BACK,
           Camera_Type::CAMERA_TYPE_DEFAULT, &cameras[0]);
       // 获取前置相机。
       ret = OH_CameraManager_GetCameraDevice(cameraManager, Camera_Position::CAMERA_POSITION_FRONT,
           Camera_Type::CAMERA_TYPE_DEFAULT, &cameras[1]);
       // 使用完毕后释放相机列表并置空指针，防止内存泄漏。
       OH_CameraManager_DeleteSupportedCameras(cameraManager, cameras, size);
       cameras = nullptr;
   }
   ```
4. 获取对应的并发能力集。通过[OH\_CameraManager\_GetCameraConcurrentInfos](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getcameraconcurrentinfos)方法，获取[Camera\_ConcurrentInfo](../harmonyos-references/capi-oh-camera-camera-concurrentinfo.md)相机并发能力集对象数组，数组包含了前置和后置同时开启的相机在指定多摄同开模式下支持的相机模式和相机输出能力，**在多摄同开场景下设置的模式和输出能力必须在并发能力集的范围之内**。

   ```
   void NDKCamera::GetSupportedOutputCapabilityForConcurrent(Camera_Manager *cameraManager, Camera_Device *cameras)
   {
       Camera_ConcurrentInfo* cameraConcurrentInfo = nullptr;
       uint32_t infoSize = 0;
       Camera_ErrorCode ret = OH_CameraManager_GetCameraConcurrentInfos(cameraManager, cameras, 2,
           &cameraConcurrentInfo, &infoSize);
       if (ret != CAMERA_OK || cameraConcurrentInfo == nullptr) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetCameraConcurrentInfos failed.");
           return;
       }
       if (cameraConcurrentInfo->outputCapabilities == nullptr
           || cameraConcurrentInfo->outputCapabilities->previewProfiles == nullptr) {
           OH_LOG_ERROR(LOG_APP, "outputCapabilities or previewProfiles is nullptr.");
       }
   }
   ```
5. 对应并发能力集创建PreviewOutput对象。

   ```
   Camera_ErrorCode NDKCamera::CreatePreviewOutputForConcurrent(Camera_Manager *cameraManager,
       Camera_ConcurrentInfo* cameraConcurrentInfo, Camera_PreviewOutput** previewOutput, char* previewSurfaceId)
   {
       if (cameraManager == nullptr || cameraConcurrentInfo == nullptr || previewOutput == nullptr ||
           cameraConcurrentInfo->outputCapabilities == nullptr ||
           cameraConcurrentInfo->outputCapabilities->previewProfiles == nullptr) {
           OH_LOG_ERROR(LOG_APP, "invalid parameter.");
           return CAMERA_INVALID_ARGUMENT;
       }
       Camera_Profile *profile = cameraConcurrentInfo->outputCapabilities->previewProfiles[0];
       if (profile == nullptr) {
           OH_LOG_ERROR(LOG_APP, "previewProfiles[0] is nullptr.");
           return CAMERA_INVALID_ARGUMENT;
       }
       Camera_ErrorCode ret = OH_CameraManager_CreatePreviewOutput(cameraManager, profile,
           previewSurfaceId, previewOutput);
       if (*previewOutput == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
           return ret;
       }
       return ret;
   }
   ```
6. 打开相机。通过[OH\_CameraInput\_OpenConcurrentCameras](../harmonyos-references/capi-camera-input-h.md#oh_camerainput_openconcurrentcameras)以并发状态打开指定相机，在使用该接口前，请先查询接口是否支持并发能力集，并优先调用[OH\_CameraManager\_GetCameraConcurrentInfos](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getcameraconcurrentinfos)方法，获取多摄同开状态下的相机并发能力集。请勿在未查询并发能力集的情况下使用[OH\_CameraInput\_OpenConcurrentCameras](../harmonyos-references/capi-camera-input-h.md#oh_camerainput_openconcurrentcameras)，否则会导致打开相机失败。

   ```
   void NDKCamera::CameraInputOpenForConcurrent(Camera_Manager *cameraManager, Camera_Device *cameras)
   {
       Camera_Input *cameraInput = nullptr;
       Camera_ErrorCode ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[0], &cameraInput);
       if (cameraInput == nullptr || ret != CAMERA_OK) {
           return;
       }
       // 当前版本只支持CAMERA_CONCURRENT_TYPE_LIMITED_CAPABILITY模式并发打开。
       ret = OH_CameraInput_OpenConcurrentCameras(cameraInput,
           Camera_ConcurrentType::CAMERA_CONCURRENT_TYPE_LIMITED_CAPABILITY);
       if (ret != CAMERA_OK) {
           return;
       }
   }
   ```
7. 会话流程。配置对应的相机输入流[Camera\_Input](../harmonyos-references/capi-oh-camera-camera-input.md)和需要的相机输出流，此处以预览输出流[Camera\_PreviewOutput](../harmonyos-references/capi-oh-camera-camera-previewoutput.md)为例。

   ```
   void NDKCamera::SessionFlowForConcurrentFn(Camera_CaptureSession *captureSession,
       Camera_Input *cameraInput, Camera_PreviewOutput *previewOutput)
   {
       // 开始配置会话。
       Camera_ErrorCode ret = OH_CaptureSession_BeginConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
           return;
       }
       // 向会话中添加相机输入流。
       ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
           return;
       }
       // 向会话中添加预览输出流。
       ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
           return;
       }
       // 提交配置信息。
       ret = OH_CaptureSession_CommitConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
           return;
       }
       // 开始会话。
       ret = OH_CaptureSession_Start(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
       }
   }
   ```
8. 在多摄同开状态下，前/后置相机可配置的能力示例如下（当前版本仅支持本文开头部分所示的七项基础功能）。

   ```
   Camera_ErrorCode NDKCamera::HasFlashFn(uint32_t mode)
   {
       Camera_FlashMode flashMode = static_cast<Camera_FlashMode>(mode);
       // 检查闪光灯。
       bool hasFlash = false;
       Camera_ErrorCode ret = OH_CaptureSession_HasFlash(captureSession_, &hasFlash);
       if (captureSession_ == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_HasFlash failed.");
       }
       if (hasFlash) {
           OH_LOG_INFO(LOG_APP, "hasFlash success-----");
       } else {
           OH_LOG_ERROR(LOG_APP, "hasFlash fail-----");
       }

       // 查询闪光灯模式是否支持。
       bool isSupported = false;
       ret = OH_CaptureSession_IsFlashModeSupported(captureSession_, flashMode, &isSupported);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFlashModeSupported failed.");
       }
       if (isSupported) {
           OH_LOG_INFO(LOG_APP, "isFlashModeSupported success-----");
       } else {
           OH_LOG_ERROR(LOG_APP, "isFlashModeSupported fail-----");
       }

       // 设置闪光灯模式。
       ret = OH_CaptureSession_SetFlashMode(captureSession_, flashMode);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFlashMode success.");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFlashMode failed. %{public}d.", ret);
       }

       // 获取当前设备的闪光灯模式。
       ret = OH_CaptureSession_GetFlashMode(captureSession_, &flashMode);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFlashMode success. flashMode: %{public}d.", flashMode);
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFlashMode failed. %{public}d.", ret);
       }
       return ret;
   }

   // 对焦模式。
   Camera_ErrorCode NDKCamera::IsFocusModeSupported(uint32_t mode)
   {
       Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
       ret_ = OH_CaptureSession_IsFocusModeSupported(captureSession_, focusMode, &isFocusModeSupported_);
       if (&isFocusModeSupported_ == nullptr || ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       return ret_;
   }

   Camera_ErrorCode NDKCamera::IsFocusMode(uint32_t mode)
   {
       OH_LOG_INFO(LOG_APP, "IsFocusMode start.");
       Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
       ret_ = OH_CaptureSession_IsFocusModeSupported(captureSession_, focusMode, &isFocusModeSupported_);
       if (&isFocusModeSupported_ == nullptr || ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       ret_ = OH_CaptureSession_SetFocusMode(captureSession_, focusMode);
       if (ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "SetFocusMode failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       ret_ = OH_CaptureSession_GetFocusMode(captureSession_, &focusMode);
       if (&focusMode == nullptr || ret_ != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "GetFocusMode failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       OH_LOG_INFO(LOG_APP, "IsFocusMode end.");
       return ret_;
   }

   Camera_ErrorCode NDKCamera::setZoomRatioFn(uint32_t zoomRatio)
   {
       float zoom = float(zoomRatio);
       // 获取支持的缩放范围。
       float minZoom;
       float maxZoom;
       Camera_ErrorCode ret = OH_CaptureSession_GetZoomRatioRange(captureSession_, &minZoom, &maxZoom);
       if (captureSession_ == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatioRange failed.");
       } else {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatioRange success. minZoom: %{public}f, maxZoom: %{public}f.",
               minZoom, maxZoom);
       }

       // 设置缩放比例。
       ret = OH_CaptureSession_SetZoomRatio(captureSession_, zoom);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetZoomRatio success.");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetZoomRatio failed. %{public}d.", ret);
       }

       // 获取当前设备的缩放比例。
       ret = OH_CaptureSession_GetZoomRatio(captureSession_, &zoom);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatio success. zoom: %{public}f.", zoom);
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatio failed. %{public}d.", ret);
       }
       return ret;
   }
   ```
