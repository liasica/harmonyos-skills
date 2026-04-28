---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-device-management
title: 相机管理 (C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(C/C++) > 相机管理 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:05+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:915272740d979fb32cfbc00de5d7e318117b0523122df40e301650a989edf89f
---

在开发一个相机应用前，需要先通过调用相机接口来创建一个独立的相机设备。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口。选择系统提供的NDK接口能力，导入NDK接口的方法如下。

   ```
   1. // 导入NDK接口头文件。
   2. #include "hilog/log.h"
   3. #include "ohcamera/camera.h"
   4. #include "ohcamera/camera_input.h"
   5. #include "ohcamera/capture_session.h"
   6. #include "ohcamera/photo_output.h"
   7. #include "ohcamera/preview_output.h"
   8. #include "ohcamera/video_output.h"
   9. #include "ohcamera/camera_manager.h"
   ```
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libohcamera.so
   4. libhilog_ndk.z.so
   5. )
   ```
3. 通过[OH\_Camera\_GetCameraManager()](../harmonyos-references/capi-camera-h.md#oh_camera_getcameramanager)方法，获取cameraManager对象。

   ```
   1. Camera_ErrorCode CreateCameraManager(Camera_Manager** cameraManager)
   2. {
   3. // 创建CameraManager对象。
   4. Camera_ErrorCode ret = OH_Camera_GetCameraManager(cameraManager);
   5. if (*cameraManager == nullptr || ret != CAMERA_OK) {
   6. OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraManager failed.");
   7. }
   8. return ret;
   9. }
   ```

   说明

   如果获取对象失败，说明相机可能被占用或无法使用。如果被占用，须等到相机被释放后才能重新获取。
4. 通过[OH\_CameraManager\_GetSupportedCameras()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameras)方法，获取当前设备支持的相机列表，列表中存储了设备支持的所有相机ID。若列表不为空，则说明列表中的每个ID都支持独立创建相机对象；否则，说明当前设备无可用相机，无法进行后续操作。

   ```
   1. Camera_ErrorCode GetSupportedCameras(Camera_Manager* cameraManager, Camera_Device** cameras, uint32_t &size)
   2. {
   3. // 获取相机列表。
   4. Camera_ErrorCode ret = OH_CameraManager_GetSupportedCameras(cameraManager, cameras, &size);
   5. if (cameras == nullptr || size == 0 || ret != CAMERA_OK) {
   6. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
   7. }
   8. // 在不使用cameras时，需要调用delete[]释放。
   9. for (uint32_t index = 0; index < size; index++) {
   10. OH_LOG_INFO(LOG_APP, "cameraId  =  %{public}s ", (*cameras)[index].cameraId);              // 获取相机ID。
   11. OH_LOG_INFO(LOG_APP, "cameraPosition  =  %{public}d ", (*cameras)[index].cameraPosition);  // 获取相机位置。
   12. OH_LOG_INFO(LOG_APP, "cameraType  =  %{public}d ", (*cameras)[index].cameraType);          // 获取相机类型。
   13. OH_LOG_INFO(LOG_APP, "connectionType  =  %{public}d ", (*cameras)[index].connectionType);  // 获取相机连接类型。
   14. }
   15. return ret;
   16. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听相机状态，包括新相机的出现、相机的移除、相机的可用状态。在回调函数中，通过相机ID、相机状态这两个参数进行监听，如当有新相机出现时，可以将新相机加入到应用的备用相机中。

通过[OH\_CameraManager\_RegisterCallback()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_registercallback)注册cameraStatus事件，通过回调返回监听结果，callback返回Camera\_StatusInfo参数，参数的具体内容可参考相机管理器回调接口实例[Camera\_StatusInfo](../harmonyos-references/capi-oh-camera-camera-statusinfo.md)。

```
1. void CameraStatusCallback(Camera_Manager* cameraManager, Camera_StatusInfo* status)
2. {
3. OH_LOG_INFO(LOG_APP, "CameraStatusCallback is called");
4. }
5. CameraManager_Callbacks* GetCameraManagerListener()
6. {
7. static CameraManager_Callbacks cameraManagerListener = {
8. .onCameraStatus = CameraStatusCallback
9. };
10. return &cameraManagerListener;
11. }
```

```
1. Camera_ErrorCode RegisterCameraStatusCallback(Camera_Manager &cameraManager)
2. {
3. Camera_ErrorCode ret = OH_CameraManager_RegisterCallback(&cameraManager, GetCameraManagerListener());
4. if (ret != CAMERA_OK) {
5. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
6. }
7. return ret;
8. }
```
