---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-device-management
title: 相机管理(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(ArkTS) > 相机管理(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:56+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:2ff35b3d11de998716b359a54ee15f15af74c9056ad668bdea67da7d455c2005
---

在开发一个相机应用前，需要先通过调用相机接口来创建一个相机管理实例。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 通过[getCameraManager](../harmonyos-references/arkts-apis-camera-f.md#cameragetcameramanager)方法，获取cameraManager对象。

   Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```typescript
   getCameraManagerFn(): camera.CameraManager | undefined {
     if (this.cameraManager) {
       return this.cameraManager;
     }
     let cameraManager: camera.CameraManager | undefined = undefined;
     try {
       cameraManager = camera.getCameraManager(GlobalContext.get().getCameraSettingContext());
       console.info(`getCameraManager success: ${cameraManager}`);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`getCameraManager failed, err code: ${err.code}`);
     }
     return cameraManager;
   }
   ```

   **说明** 

   如果获取对象失败，说明相机可能被占用或无法使用。如果被占用，须等到相机被释放后才能重新获取。
3. 获取相机列表。

   方法一：获取逻辑相机，通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)方法，获取当前设备支持的相机列表，列表中存储了设备支持的所有相机ID。若列表不为空，则说明列表中的每个ID都支持独立创建相机对象；否则，说明当前设备无可用相机，无法进行后续操作。

   **说明** 

   逻辑相机是系统定义的虚拟相机，由多个物理镜头组合而成。系统在内部完成物理镜头间的切换等处理，应用无需感知镜头变化，只需通过[getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)获取相机列表时，根据[CameraPosition](../harmonyos-references/arkts-apis-camera-e.md#cameraposition)区分前置镜头与后置镜头即可。

   ```typescript
   getSupportedCamerasFn(cameraManager: camera.CameraManager): camera.CameraDevice[] {
     let supportedCameras: camera.CameraDevice[] = [];
     try {
       supportedCameras = cameraManager.getSupportedCameras();
     } catch (error) {
       let err = error as BusinessError;
       Logger.error(TAG, `getSupportedCameras failed: ${err.code}`);
     }
     if (supportedCameras != undefined && supportedCameras.length > 0) {
       for (let index = 0; index < supportedCameras.length; index++) {
         console.info(`cameraId : ${supportedCameras[index].cameraId}`);  // 获取相机ID。
         console.info(`cameraPosition : ${supportedCameras[index].cameraPosition}`);  // 获取相机位置。
         console.info(`cameraType : ${supportedCameras[index].cameraType}`);  // 获取相机类型。
         console.info(`connectionType : ${supportedCameras[index].connectionType}`);  // 获取相机连接类型。
       }
       return supportedCameras;
     } else {
       console.error(`cameraManager.getSupportedCameras error`);
       return [];
     }
   }
   ```

   方法二：获取物理相机，通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)的[getCameraDevices](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevices23)方法，获取当前设备支持的相机列表，筛选相机属性[CameraDevice](../harmonyos-references/arkts-apis-camera-i.md#cameradevice).isLogicalCamera为false的相机。

   物理镜头根据[CameraType](../harmonyos-references/arkts-apis-camera-e.md#cameratype)区分各自镜头属性，开发者可根据使用场景使用符合采集诉求的相机镜头。

   ```typescript
   getCameraDevicesFn(cameraManager: camera.CameraManager,
     position: camera.CameraPosition, cameraTypes: camera.CameraType[]): camera.CameraDevice[] {
     let cameraArray: camera.CameraDevice[] = []
     try {
       cameraArray =
         cameraManager.getCameraDevices(position, cameraTypes, camera.ConnectionType.CAMERA_CONNECTION_BUILT_IN);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`getCameraDevices failed, err code: ${err.code}`);
     }
     if (cameraArray != undefined && cameraArray.length > 0) {
       for (let index = 0; index < cameraArray.length; index++) {
         console.info(`cameraId : ${cameraArray[index].cameraId}`);  // 获取相机ID。
         console.info(`cameraPosition : ${cameraArray[index].cameraPosition}`);  // 获取相机位置。
         console.info(`cameraType : ${cameraArray[index].cameraType}`);  // 获取相机类型。
         console.info(`isLogicalCamera : ${cameraArray[index].isLogicalCamera}`);  // 获取相机连接类型。
       }
       // 过滤掉逻辑相机，只保留物理相机。
       cameraArray = cameraArray.filter((item: camera.CameraDevice) => !item.isLogicalCamera);
       return cameraArray;
     } else {
       console.error(`cameraManager.getSupportedCameras error`);
       return [];
     }
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听相机状态，包括新相机的出现、相机的移除、相机的可用状态。在回调函数中，通过相机ID、相机状态这两个参数进行监听，如当有新相机出现时，可以将新相机加入到应用的备用相机中。

通过注册cameraStatus事件，通过回调返回监听结果，callback返回CameraStatusInfo参数，参数的具体内容可参考相机管理器回调接口实例[CameraStatusInfo](../harmonyos-references/arkts-apis-camera-i.md#camerastatusinfo)。

```typescript
registerCameraStatusChange(err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo): void {
  // 如果当通过USB连接相机设备时，回调函数会返回新的相机出现状态。
  if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_APPEAR) {
    console.info(`New Camera device appear.`);
  }
  // 如果当断开相机设备USB连接时，回调函数会返回相机被移除状态。
  if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_DISAPPEAR) {
    console.info(`Camera device has been removed.`);
  }
  // 相机被关闭时，回调函数会返回相机可用状态。
  if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_AVAILABLE) {
    console.info(`Current Camera is available.`);
  }
  // 相机被打开/占用时，回调函数会返回相机不可用状态。
  if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_UNAVAILABLE) {
    console.info(`Current Camera has been occupied.`);
  }
  console.info(`camera: ${cameraStatusInfo.camera.cameraId}`);
  console.info(`status: ${cameraStatusInfo.status}`);
}

/**
 * 监听相机状态变化。
 * @param cameraManager - 相机管理器对象。
 * @returns 无返回值。
 */
onCameraStatusChange(cameraManager: camera.CameraManager): void {
  Logger.info(TAG, 'onCameraStatusChange is called');
  try {
    cameraManager.on('cameraStatus', this.registerCameraStatusChange);
  } catch (error) {
    Logger.error(TAG, 'onCameraStatusChange error');
  }
}
```
