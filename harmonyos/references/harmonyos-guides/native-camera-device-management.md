---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-device-management
title: 相机管理 (C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(C/C++) > 相机管理 (C/C++)
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:57+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:e234b4097a9ed983f6cba788ceac6351aa6493e26ef25442d00e0ec422ada71b
---

在开发一个相机应用前，需要先通过调用相机接口来创建一个独立的相机设备。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口。选择系统提供的NDK接口能力，导入NDK接口的方法如下。

   ```
   // 导入NDK接口头文件。
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
3. 通过[OH\_Camera\_GetCameraManager()](../harmonyos-references/capi-camera-h.md#oh_camera_getcameramanager)方法，获取cameraManager对象。

   ```
   Camera_ErrorCode NDKCamera::CreateCameraManager(Camera_Manager** cameraManager)
   {
       // 创建CameraManager对象。
       Camera_ErrorCode ret = OH_Camera_GetCameraManager(cameraManager);
       if (*cameraManager == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraManager failed.");
       }
       return ret;
   }
   ```

   **说明** 

   如果获取对象失败，说明相机可能被占用或无法使用。如果被占用，须等到相机被释放后才能重新获取。
4. 获取相机列表。

   方法一：获取逻辑相机，通过[OH\_CameraManager\_GetSupportedCameras()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameras)方法，获取当前设备支持的相机列表，列表中存储了设备支持的所有相机ID。若列表不为空，则说明列表中的每个ID都支持独立创建相机对象；否则，说明当前设备无可用相机，无法进行后续操作。

   **说明** 

   逻辑相机是系统定义的虚拟相机，由多个物理镜头组合而成。系统在内部完成物理镜头间的切换等处理，应用无需感知镜头变化，只需通过[OH\_CameraManager\_GetSupportedCameras()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getsupportedcameras)获取相机镜头列表时，根据[Camera\_Position](../harmonyos-references/capi-camera-h.md#camera_position)区分前置镜头与后置镜头即可。

   ```
   Camera_ErrorCode NDKCamera::GetSupportedCameras(Camera_Manager* cameraManager, Camera_Device** cameras, uint32_t &size)
   {
       // 获取相机列表。
       Camera_ErrorCode ret = OH_CameraManager_GetSupportedCameras(cameraManager, cameras, &size);
       if (*cameras == nullptr || size == 0 || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
           return ret;
       }
       // 在不使用cameras时，需要调用OH_CameraManager_DeleteSupportedCameras()方法释放相机列表并置空指针防止内存泄漏。
       for (uint32_t index = 0; index < size; index++) {
           OH_LOG_INFO(LOG_APP, "cameraId  =  %{public}s ", (*cameras)[index].cameraId);              // 获取相机ID。
           OH_LOG_INFO(LOG_APP, "cameraPosition  =  %{public}d ", (*cameras)[index].cameraPosition);  // 获取相机位置。
           OH_LOG_INFO(LOG_APP, "cameraType  =  %{public}d ", (*cameras)[index].cameraType);          // 获取相机类型。
           OH_LOG_INFO(LOG_APP, "connectionType  =  %{public}d ", (*cameras)[index].connectionType);  // 获取相机连接类型。
       }
       return ret;
   }
   ```

   方法二：获取物理相机，通过[OH\_CameraManager\_GetCameraDevices](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_getcameradevices)方法，获取当前设备支持的相机列表，通过[OH\_CameraDevice\_IsLogicalCamera](../harmonyos-references/capi-camera-device-h.md#oh_cameradevice_islogicalcamera)方法获取物理镜头。

   物理镜头根据[Camera\_Type](../harmonyos-references/capi-camera-h.md#camera_type)区分各自镜头属性，开发者可根据使用场景使用符合采集诉求的相机镜头。

   ```
   Camera_ErrorCode NDKCamera::GetCameraDevices(Camera_Manager* cameraManager, Camera_Device** cameras, uint32_t &size)
   {
       // 获取相机列表。
       Camera_Type type[5] = {
           Camera_Type::CAMERA_TYPE_DEFAULT,
           Camera_Type::CAMERA_TYPE_TELEPHOTO,
           Camera_Type::CAMERA_TYPE_TRUE_DEPTH,
           Camera_Type::CAMERA_TYPE_ULTRA_WIDE,
           Camera_Type::CAMERA_TYPE_WIDE_ANGLE};
       Camera_DeviceQueryInfo deviceInfo = {};
       deviceInfo.cameraType = type;
       deviceInfo.cameraTypeSize = sizeof(type) / sizeof(type[0]);
       deviceInfo.cameraPosition = Camera_Position::CAMERA_POSITION_BACK;
       deviceInfo.connectionType = Camera_Connection::CAMERA_CONNECTION_BUILT_IN;
       Camera_ErrorCode ret = OH_CameraManager_GetCameraDevices(cameraManager, &deviceInfo, &size, cameras);
       if (*cameras == nullptr || size == 0 || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetCameraDevices failed.");
           return ret;
       }
       // 在不使用cameras时，需要调用OH_CameraManager_DeleteSupportedCameras()方法释放相机列表并置空指针防止内存泄漏。
       for (uint32_t index = 0; index < size; index++) {
           OH_LOG_INFO(LOG_APP, "cameraId = %{public}s ", (*cameras)[index].cameraId);              // 获取相机ID。
           OH_LOG_INFO(LOG_APP, "cameraPosition = %{public}d ", (*cameras)[index].cameraPosition);  // 获取相机位置。
           OH_LOG_INFO(LOG_APP, "cameraType = %{public}d ", (*cameras)[index].cameraType);          // 获取相机类型。
           OH_LOG_INFO(LOG_APP, "connectionType = %{public}d ", (*cameras)[index].connectionType);  // 获取相机连接类型。
           bool isLogical = false;
           ret = OH_CameraDevice_IsLogicalCamera(&(*cameras)[index], &isLogical);
           if (ret != CAMERA_OK) {
               OH_LOG_ERROR(LOG_APP, "OH_CameraDevice_IsLogicalCamera failed.");
               continue;
           }
           OH_LOG_INFO(LOG_APP, "cameraId: %{public}s is logical: %{public}d.", (*cameras)[index].cameraId, isLogical);
       }
       return CAMERA_OK;
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听相机状态，包括新相机的出现、相机的移除、相机的可用状态。在回调函数中，通过相机ID、相机状态这两个参数进行监听，如当有新相机出现时，可以将新相机加入到应用的备用相机中。

通过[OH\_CameraManager\_RegisterCallback()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_registercallback)注册cameraStatus事件，通过回调返回监听结果，callback返回Camera\_StatusInfo参数，参数的具体内容可参考相机管理器回调接口实例[Camera\_StatusInfo](../harmonyos-references/capi-oh-camera-camera-statusinfo.md)。

```
void CameraStatusCallback(Camera_Manager* cameraManager, Camera_StatusInfo* status)
{
    OH_LOG_INFO(LOG_APP, "CameraStatusCallback is called");
}
CameraManager_Callbacks* GetCameraManagerListener()
{
    static CameraManager_Callbacks cameraManagerListener = {.onCameraStatus = CameraStatusCallback};
    return &cameraManagerListener;
}

Camera_ErrorCode NDKCamera::RegisterCameraStatusCallback(Camera_Manager &cameraManager)
{
    Camera_ErrorCode ret = OH_CameraManager_RegisterCallback(&cameraManager, GetCameraManagerListener());
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
    }
    return ret;
}
```
