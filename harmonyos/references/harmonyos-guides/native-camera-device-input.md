---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-device-input
title: 设备输入(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(C/C++) > 设备输入(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:05+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:d343832868420d23f1cc66369f04da4b9137b3eaec499ccd5e83af6210a04307
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

相机应用通过调用和控制相机设备，完成预览、拍照和录像等基础操作。

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
3. 通过[OH\_CameraManager\_CreateCameraInput()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createcamerainput)方法，获取cameraInput对象。

   ```
   1. // 监听cameraInput错误信息。
   2. void OnCameraInputError(const Camera_Input* cameraInput, Camera_ErrorCode errorCode)
   3. {
   4. OH_LOG_INFO(LOG_APP, "OnCameraInput errorCode: %{public}d", errorCode);
   5. }

   7. CameraInput_Callbacks* GetCameraInputListener(void)
   8. {
   9. static CameraInput_Callbacks cameraInputCallbacks = {
   10. .onError = OnCameraInputError
   11. };
   12. return &cameraInputCallbacks;
   13. }
   ```

   ```
   1. // 监听cameraStatus信息。
   2. void CameraManagerStatusCallback(Camera_Manager* cameraManager, Camera_StatusInfo* status)
   3. {
   4. OH_LOG_INFO(LOG_APP, "CameraManagerStatusCallback is called");
   5. }

   7. CameraManager_Callbacks* GetCameraManagerListener()
   8. {
   9. static CameraManager_Callbacks cameraManagerListener = {
   10. .onCameraStatus = CameraManagerStatusCallback
   11. };
   12. return &cameraManagerListener;
   13. }
   ```

   ```
   1. void CreateAndOpenCamera()
   2. {
   3. Camera_Manager* cameraManager = nullptr;
   4. Camera_Input* cameraInput = nullptr;
   5. Camera_Device* cameras = nullptr;
   6. uint32_t size = 0;
   7. uint32_t cameraDeviceIndex = 0;
   8. // 创建CameraManager对象。
   9. Camera_ErrorCode ret = OH_Camera_GetCameraManager(&cameraManager);
   10. if (cameraManager == nullptr || ret != CAMERA_OK) {
   11. OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraManager failed.");
   12. return;
   13. }
   14. // 监听相机状态变化。
   15. ret = OH_CameraManager_RegisterCallback(cameraManager, GetCameraManagerListener());
   16. if (ret != CAMERA_OK) {
   17. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
   18. }
   19. // 获取相机列表。
   20. ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
   21. if (cameras == nullptr || size == 0 || ret != CAMERA_OK) {
   22. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
   23. return;
   24. }
   25. // 创建相机输入流。
   26. ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[cameraDeviceIndex], &cameraInput);
   27. if (cameraInput == nullptr || ret != CAMERA_OK) {
   28. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.");
   29. return;
   30. }
   31. ret = OH_CameraInput_RegisterCallback(cameraInput, GetCameraInputListener());
   32. if (ret != CAMERA_OK) {
   33. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_RegisterCallback failed.");
   34. }
   35. // 打开相机。
   36. ret = OH_CameraInput_Open(cameraInput);
   37. if (ret != CAMERA_OK) {
   38. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_open failed.");
   39. return;
   40. }
   41. }
   ```

   说明

   在相机设备输入之前需要先完成相机管理，详细开发步骤请参考[相机管理](native-camera-device-management.md)。
4. 通过[OH\_CameraManager\_GetSupportedSceneModes()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedscenemodes)方法，获取当前相机设备支持的模式列表，列表中存储了相机设备支持的所有模式[Camera\_SceneMode](../harmonyos-references/capi-camera-h.md#camera_scenemode)。

   ```
   1. bool IsSupportedSceneMode(Camera_Device camera, Camera_SceneMode sceneMode)
   2. {
   3. Camera_SceneMode* sceneModes = nullptr;
   4. uint32_t sceneModeSize = 0;
   5. Camera_ErrorCode ret = OH_CameraManager_GetSupportedSceneModes(&camera, &sceneModes, &sceneModeSize);
   6. if (sceneModes == nullptr || ret != CAMERA_OK) {
   7. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedSceneModes failed.");
   8. return false;
   9. }
   10. for (uint32_t index = 0; index < sceneModeSize; index++) {
   11. OH_LOG_INFO(LOG_APP, "scene mode = %{public}u ", sceneModes[index]);    // 获取相机指定模式。
   12. if (sceneModes[index] == sceneMode) {
   13. return true;
   14. }
   15. }
   16. return false;
   17. }
   ```
5. 通过[OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapabilitywithscenemode)方法，获取当前设备在当前模式下支持的所有输出流，如预览流、拍照流等。输出流在[Camera\_OutputCapability](../harmonyos-references/capi-oh-camera-camera-outputcapability.md)中的各个profile字段中。根据相机设备指定模式[Camera\_SceneMode](../harmonyos-references/capi-camera-h.md#camera_scenemode)的不同，需要向Session中添加对应类型的输出流，请参考会话管理[开发步骤](native-camera-session-management.md#开发步骤)中的第6步。

   ```
   1. Camera_OutputCapability* GetSupportedCameraOutputCapability(Camera_Manager* cameraManager, Camera_Device &camera)
   2. {
   3. Camera_OutputCapability* cameraOutputCapability = nullptr;
   4. // 示例代码以NORMAL_PHOTO模式为例，查询NORMAL_PHOTO在camera中是否支持。
   5. bool isSupported = IsSupportedSceneMode(camera, Camera_SceneMode::NORMAL_PHOTO);
   6. if (!isSupported) {
   7. OH_LOG_ERROR(LOG_APP, "NORMAL_PHOTO is not supported.");
   8. return cameraOutputCapability;
   9. }
   10. // 获取相机设备支持的输出流能力。
   11. const Camera_Profile* previewProfile = nullptr;
   12. const Camera_Profile* photoProfile = nullptr;
   13. Camera_ErrorCode ret = OH_CameraManager_GetSupportedCameraOutputCapabilityWithSceneMode(cameraManager, &camera,
   14. Camera_SceneMode::NORMAL_PHOTO, &cameraOutputCapability);
   15. if (cameraOutputCapability == nullptr || ret != CAMERA_OK) {
   16. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameraOutputCapability failed.");
   17. return cameraOutputCapability;
   18. }
   19. // 以NORMAL_PHOTO模式为例，需要添加预览流、拍照流。
   20. if (cameraOutputCapability->previewProfiles == nullptr) {
   21. OH_LOG_ERROR(LOG_APP, "previewProfiles == null");
   22. } else {
   23. // 根据所需从cameraOutputCapability->previewProfiles中选择合适的预览分辨率。
   24. previewProfile = cameraOutputCapability->previewProfiles[0];
   25. }
   26. if (cameraOutputCapability->photoProfiles == nullptr) {
   27. OH_LOG_ERROR(LOG_APP, "photoProfiles == null");
   28. } else {
   29. // 根据所需从cameraOutputCapability->photoProfiles中选择合适的拍照分辨率。
   30. photoProfile = cameraOutputCapability->photoProfiles[0];
   31. }
   32. return cameraOutputCapability;
   33. }
   ```
