---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-concurrent-open
title: 多摄同开(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 多摄同开(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8eafeefc9673c37e085e96a81463d9143306ab6c68b298cfd02d13af53688893
---

从API version 18开始支持多摄同开，即应用同时开启前置/后置相机进行预览和录像（前置/后置相机同时拍照功能待开放）。

说明

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
   1. #include <cstdint>
   2. #include <unistd.h>
   3. #include <string>
   4. #include <thread>
   5. #include <cstdio>
   6. #include <fcntl.h>
   7. #include <map>
   8. #include <vector>
   9. #include <native_buffer/native_buffer.h>
   10. #include "iostream"
   11. #include "mutex"
   12. #include "hilog/log.h"
   13. #include "ohcamera/camera.h"
   14. #include "ohcamera/camera_input.h"
   15. #include "ohcamera/capture_session.h"
   16. #include "ohcamera/photo_output.h"
   17. #include "ohcamera/preview_output.h"
   18. #include "ohcamera/video_output.h"
   19. #include "napi/native_api.h"
   20. #include "ohcamera/camera_manager.h"
   21. #include "common/log_common.h"
   ```
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libohcamera.so
   3. libace_napi.z.so
   4. libnative_buffer.so
   5. libhilog_ndk.z.so
   6. librawfile.z.so)
   ```
3. 通过[OH\_CameraManager\_GetCameraDevice](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getcameradevice)方法获取对应的前置相机和后置相机。如果接口返回值为CAMERA\_SERVICE\_FATAL\_ERROR，基于示例中的配置信息，表示当前设备不支持指定位置（前置/后置）的默认类型相机，无法实现多摄同开功能。

   ```
   1. void GetSupportedCameras(Camera_Manager *cameraManager)
   2. {
   3. Camera_Device *cameras;
   4. uint32_t size = 0;
   5. Camera_ErrorCode ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
   6. if (cameras == nullptr || &size == nullptr || ret != CAMERA_OK) {
   7. return;
   8. }

   10. // 获取后置相机。
   11. ret = OH_CameraManager_GetCameraDevice(cameraManager, Camera_Position::CAMERA_POSITION_BACK, Camera_Type::CAMERA_TYPE_DEFAULT, &cameras[0]);

   13. // 获取前置相机。
   14. ret = OH_CameraManager_GetCameraDevice(cameraManager, Camera_Position::CAMERA_POSITION_FRONT, Camera_Type::CAMERA_TYPE_DEFAULT, &cameras[1]);
   15. }
   ```
4. 获取对应的并发能力集。通过[OH\_CameraManager\_GetCameraConcurrentInfos](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getcameraconcurrentinfos)方法，获取[Camera\_ConcurrentInfo](../harmonyos-references/capi-oh-camera-camera-concurrentinfo.md)相机并发能力集对象数组，数组包含了前置和后置同时开启的相机在指定多摄同开模式下支持的相机模式和相机输出能力，**在多摄同开场景下设置的模式和输出能力必须在并发能力集的范围之内**。

   ```
   1. void GetSupportedOutputCapability(Camera_Manager *cameraManager, Camera_Device *cameras)
   2. {
   3. Camera_ConcurrentInfo* cameraConcurrentInfo;
   4. uint32_t infoSize = 0;
   5. Camera_ErrorCode ret = OH_CameraManager_GetCameraConcurrentInfos(cameraManager, cameras, 2, &cameraConcurrentInfo, &infoSize);
   6. if (cameraConcurrentInfo == nullptr || cameraConcurrentInfo->outputCapabilities == nullptr
   7. || cameraConcurrentInfo->outputCapabilities->previewProfiles == nullptr || ret != CAMERA_OK) {
   8. return;
   9. }
   10. }
   ```
5. 对应并发能力集创建PreviewOutput对象。

   ```
   1. void CreatePreviewOutput(Camera_Manager *cameraManager, Camera_ConcurrentInfo* cameraConcurrentInfo, char* previewSurfaceId)
   2. {
   3. Camera_Profile *profile = cameraConcurrentInfo->outputCapabilities->previewProfiles[0];
   4. if (profile == nullptr) {
   5. return;
   6. }
   7. Camera_PreviewOutput *previewOutput;
   8. Camera_ErrorCode ret = OH_CameraManager_CreatePreviewOutput(cameraManager, profile, previewSurfaceId, &previewOutput);
   9. if (previewOutput == nullptr || ret != CAMERA_OK) {
   10. return;
   11. }
   12. }
   ```
6. 打开相机。通过[OH\_CameraInput\_OpenConcurrentCameras](../harmonyos-references/capi-camera-input-h.md#oh_camerainput_openconcurrentcameras)以并发状态打开指定相机，在使用该接口前，请先查询接口是否支持并发能力集，并优先调用[OH\_CameraManager\_GetCameraConcurrentInfos](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getcameraconcurrentinfos)方法，获取多摄同开状态下的相机并发能力集。请勿在未查询并发能力集的情况下使用[OH\_CameraInput\_OpenConcurrentCameras](../harmonyos-references/capi-camera-input-h.md#oh_camerainput_openconcurrentcameras)，否则会导致打开相机失败。

   ```
   1. void CameraInputOpen(Camera_Manager *cameraManager, Camera_Device *cameras)
   2. {
   3. Camera_Input *cameraInput;
   4. Camera_ErrorCode ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[0], &cameraInput);
   5. if (cameraInput == nullptr || ret != CAMERA_OK) {
   6. return;
   7. }
   8. // 当前版本只支持CAMERA_CONCURRENT_TYPE_LIMITED_CAPABILITY模式并发打开。
   9. ret = OH_CameraInput_OpenConcurrentCameras(cameraInput, Camera_ConcurrentType::CAMERA_CONCURRENT_TYPE_LIMITED_CAPABILITY);
   10. if (ret != CAMERA_OK) {
   11. return;
   12. }
   13. }
   ```
7. 会话流程。配置对应的相机输入流[Camera\_Input](../harmonyos-references/capi-oh-camera-camera-input.md)和需要的相机输出流，此处以预览输出流[Camera\_PreviewOutput](../harmonyos-references/capi-oh-camera-camera-previewoutput.md)为例 。

   ```
   1. void SessionFlowFn(Camera_CaptureSession *captureSession, Camera_Input *cameraInput, Camera_PreviewOutput *previewOutput)
   2. {
   3. // 开始配置会话。
   4. Camera_ErrorCode ret = OH_CaptureSession_BeginConfig(captureSession);

   6. // 向会话中添加相机输入流。
   7. ret = OH_CaptureSession_AddInput(captureSession, cameraInput);

   9. // 向会话中添加预览输出流。
   10. ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);

   12. // 提交配置信息。
   13. ret = OH_CaptureSession_CommitConfig(captureSession);

   15. // 开始会话。
   16. ret = OH_CaptureSession_Start(captureSession);

   18. return;
   19. }
   ```
8. 在多摄同开状态下，前/后置相机可配置的能力示例如下（当前版本仅支持本文开头部分所示的七项基础功能）。

   ```
   1. // 闪光灯能力。
   2. void HasFlashFn(uint32_t mode, Camera_CaptureSession *captureSession)
   3. {
   4. Camera_FlashMode flashMode = static_cast<Camera_FlashMode>(mode);
   5. // 检查闪光灯。
   6. bool hasFlash = false;
   7. Camera_ErrorCode ret = OH_CaptureSession_HasFlash(captureSession, &hasFlash);
   8. if (captureSession == nullptr || ret != CAMERA_OK || !hasFlash) {
   9. return;
   10. }

   12. // 检查闪光灯模式是否支持。
   13. bool isSupported = false;
   14. ret = OH_CaptureSession_IsFlashModeSupported(captureSession, flashMode, &isSupported);
   15. if (ret != CAMERA_OK || !isSupported) {
   16. return;
   17. }

   19. // 设置闪光灯模式。
   20. ret = OH_CaptureSession_SetFlashMode(captureSession, flashMode);
   21. if (ret != CAMERA_OK) {
   22. return;
   23. }

   25. // 获取当前设备的闪光灯模式。
   26. ret = OH_CaptureSession_GetFlashMode(captureSession, &flashMode);
   27. }

   29. // 曝光。
   30. void IsExposureModeSupportedFn(uint32_t mode, Camera_CaptureSession *captureSession)
   31. {
   32. Camera_ExposureMode exposureMode = static_cast<Camera_ExposureMode>(mode);
   33. bool isExposureModeSupported = false;
   34. Camera_ErrorCode ret = OH_CaptureSession_IsExposureModeSupported(captureSession, exposureMode, &isExposureModeSupported);
   35. if (&isExposureModeSupported == nullptr || ret != CAMERA_OK) {
   36. return;
   37. }
   38. ret = OH_CaptureSession_SetExposureMode(captureSession, exposureMode);
   39. if (ret != CAMERA_OK) {
   40. return;
   41. }
   42. ret = OH_CaptureSession_GetExposureMode(captureSession, &exposureMode);
   43. }
   ```
