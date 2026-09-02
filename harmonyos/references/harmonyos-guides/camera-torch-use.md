---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-torch-use
title: 手电筒使用(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 手电筒使用(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:1216bf63c233470204ae35961ff2663d63e01aa0dbb7c153ac15a772db295690
---

通过操作设备启用手电筒功能，可使设备的手电筒保持常亮状态。

在使用相机应用并操作手电筒功能时，存在以下几种情况说明：

* 当使用后置相机并设置闪光灯模式[FlashMode](../harmonyos-references/arkts-apis-camera-e.md#flashmode)关闭时，手电筒功能无法启用。
* 当使用前置相机时，手电筒可以正常启用并保持常亮状态。
* 从前置相机切换至后置相机时，如果手电筒原本处于开启状态，它将会被自动关闭。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[isTorchSupported](../harmonyos-references/arkts-apis-camera-cameramanager.md#istorchsupported11)方法，检测当前设备是否支持手电筒功能。

   ```ts
   function isTorchSupported(cameraManager: camera.CameraManager) : boolean {
     let torchSupport: boolean = false;
     try {
       torchSupport = cameraManager.isTorchSupported();
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to torch. errorCode = ' + err.code);
     }
     console.info('Returned with the torch support status:' + torchSupport);
     return torchSupport;
   }
   ```
3. 通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[isTorchModeSupported](../harmonyos-references/arkts-apis-camera-cameramanager.md#istorchmodesupported11)方法，检测是否支持指定的手电筒模式[TorchMode](../harmonyos-references/arkts-apis-camera-e.md#torchmode11)。

   ```ts
   function isTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode) : boolean {
     let isTorchModeSupport: boolean = false;
     try {
       isTorchModeSupport = cameraManager.isTorchModeSupported(torchMode);
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to set the torch mode. errorCode = ' + err.code);
     }
     return isTorchModeSupport;
   }
   ```
4. 通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[setTorchMode](../harmonyos-references/arkts-apis-camera-cameramanager.md#settorchmode11)方法，设置当前设备的手电筒模式。以及通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[getTorchMode](../harmonyos-references/arkts-apis-camera-cameramanager.md#gettorchmode11)方法，获取当前设备的手电筒模式。

   **说明** 

   在使用[getTorchMode](../harmonyos-references/arkts-apis-camera-cameramanager.md#gettorchmode11)方法前，需要先注册监听手电筒的状态变化，请参考[状态监听](camera-torch-use.md#状态监听)。

   ```ts
   function setTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode) : void {
     cameraManager.setTorchMode(torchMode);
     let isTorchMode = cameraManager.getTorchMode();
     console.info(`Returned with the torch mode supported mode: ${isTorchMode}`);
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听手电筒状态，包括手电筒打开、手电筒关闭、手电筒不可用、手电筒恢复可用。手电筒状态发生变化，可通过回调函数获取状态的变化。

注册torchStatusChange事件后，回调会返回监听结果，callback返回TorchStatusInfo参数，参数的具体内容可参考相机管理器回调接口实例[TorchStatusInfo](../harmonyos-references/arkts-apis-camera-i.md#torchstatusinfo11)。

```ts
function onTorchStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('torchStatusChange', (err: BusinessError, torchStatusInfo: camera.TorchStatusInfo) => {
    if (err !== undefined && err.code !== 0) {
      console.error(`Callback Error, errorCode: ${err.code}`);
      return;
    }
    console.info(`onTorchStatusChange, isTorchAvailable: ${torchStatusInfo.isTorchAvailable}, isTorchActive: ${torchStatusInfo.
      isTorchActive}, level: ${torchStatusInfo.torchLevel}`);
  });
}
```
