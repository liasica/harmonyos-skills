---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-torch-use
title: 手电筒使用(C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 手电筒使用(C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:17+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:cab9de08cc457f87e78667de952b01283eb27a5cb1477c1a5964a9f308a5550f
---

通过操作设备启用手电筒功能，可使设备的手电筒保持常亮状态。

在使用相机应用并操作手电筒功能时，存在以下几种情况说明：

* 当使用后置相机并设置闪光灯模式[Camera\_FlashMode](../harmonyos-references/capi-camera-h.md#camera_flashmode)关闭时，手电筒功能无法启用。
* 当使用前置相机时，手电筒可以正常启用并保持常亮状态。
* 从前置相机切换至后置相机时，如果手电筒原本处于开启状态，它将会被自动关闭。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口。选择系统提供的NDK接口能力，导入NDK接口的方法如下。

   ```
   // 导入NDK接口头文件。
   #include "hilog/log.h"
   #include "ohcamera/camera.h"
   #include "ohcamera/camera_input.h"
   #include "ohcamera/capture_session.h"
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
3. 通过[OH\_CameraManager\_IsTorchSupported()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_istorchsupported)方法，检测当前设备是否支持手电筒。

   ```
   bool IsTorchSupported(Camera_Manager* cameraManager)
   {
       // 判断设备是否支持手电筒模式。
       bool isTorchSupported = false;
       if (cameraManager == nullptr) {
           OH_LOG_ERROR(LOG_APP, "cameraManager is nullptr.");
           return isTorchSupported;
       }
       Camera_ErrorCode ret = OH_CameraManager_IsTorchSupported(cameraManager, &isTorchSupported);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_IsTorchSupported failed.");
       }
       if (isTorchSupported) {
           OH_LOG_INFO(LOG_APP, "isTorchSupported success.");
       } else {
           OH_LOG_ERROR(LOG_APP, "isTorchSupported failed.");
       }
       return isTorchSupported;
   }
   ```
4. 通过[OH\_CameraManager\_IsTorchSupportedByTorchMode()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_istorchsupportedbytorchmode)方法，检测当前设备是否支持指定的手电筒模式。

   ```
   bool IsTorchSupportedByTorchMode(Camera_Manager* cameraManager, Camera_TorchMode torchMode)
   {
       bool torchModeSupported = false;
       Camera_ErrorCode ret = OH_CameraManager_IsTorchSupportedByTorchMode(cameraManager, torchMode, &torchModeSupported);
       if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_IsTorchSupportedByTorchMode failed.");
       }
       if (torchModeSupported) {
            OH_LOG_INFO(LOG_APP, "IsTorchSupportedByTorchMode success.");
       } else {
            OH_LOG_ERROR(LOG_APP, "IsTorchSupportedByTorchMode failed. %{public}d ", ret);
       }
       return torchModeSupported;
   }
   ```
5. 通过[OH\_CameraManager\_SetTorchMode()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_settorchmode)方法，设置当前设备的手电筒模式。

   ```
   Camera_ErrorCode SetTorchMode(Camera_Manager* cameraManager, Camera_TorchMode torchMode)
   {
       // 在torchMode支持的情况下进行设置手电筒模式。
       Camera_ErrorCode ret = OH_CameraManager_SetTorchMode(cameraManager, torchMode);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_SetTorchMode failed. %{public}d ", ret);
       } else {
           OH_LOG_INFO(LOG_APP, "OH_CameraManager_SetTorchMode success.");
       }
       return ret;
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听手电筒状态，包括手电筒打开、手电筒关闭、手电筒不可用、手电筒恢复可用。手电筒状态发生变化，可通过回调函数获取状态的变化。

注册torchStatus事件，回调会返回监听结果，callback返回Camera\_TorchStatusInfo参数，参数的具体内容可参考相机管理器回调接口实例[Camera\_TorchStatusInfo](../harmonyos-references/capi-oh-camera-camera-torchstatusinfo.md)。

```
void TorchStatusCallback(Camera_Manager *cameraManager, Camera_TorchStatusInfo* torchStatus)
{
   OH_LOG_INFO(LOG_APP, "TorchStatusCallback is called.");
}
Camera_ErrorCode RegisterTorchStatusCallback(Camera_Manager *cameraManager)
{
    Camera_ErrorCode ret = OH_CameraManager_RegisterTorchStatusCallback(cameraManager, TorchStatusCallback);
    if (ret != CAMERA_OK) {
       OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterTorchStatusCallback failed.");
    }
    return ret;
}
```
