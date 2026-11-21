---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-device-input
title: 设备输入(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(ArkTS) > 设备输入(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:01+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:a5a63277f3946e72023d592bb42cf196bbb24110692e1862b573f919f9afd8d9
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

相机应用可通过调用和控制相机设备，完成预览、拍照和录像等基础操作。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```

   **说明** 

   在相机设备输入之前需要先完成相机管理，详细开发步骤请参考[相机管理](camera-device-management.md)。
2. 通过[cameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[createCameraInput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createcamerainput)方法创建相机输入流。

   ```typescript
   /**
    * 创建cameraInput对象。
    */
   createCameraInputFn(cameraManager: camera.CameraManager,
     cameraDevice: camera.CameraDevice): camera.CameraInput | undefined {
     console.info(`createCameraInputFn is called.`);
     let cameraInput: camera.CameraInput | undefined = undefined;
     try {
       cameraInput = cameraManager.createCameraInput(cameraDevice);
       console.info(`createCameraInput success`);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`createCameraInput failed: ${err.code}`);
     }
     return cameraInput;
   }

   /**
    * 打开相机。
    */
   async cameraInputOpenFn(cameraInput: camera.CameraInput): Promise<boolean> {
     let isOpenSuccess = false;
     try {
       await cameraInput.open();
       isOpenSuccess = true;
       console.info(`open success`);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`open failed : ${err.code}.`);
     }
     return isOpenSuccess;
   }
   ```
3. 通过[getSupportedSceneModes](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedscenemodes11)方法，获取当前相机设备支持的模式列表，列表中存储了相机设备支持的所有模式[SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)。

   ```typescript
   getSupportedSceneMode(cameraDevice: camera.CameraDevice,
     cameraManager: camera.CameraManager): camera.SceneMode[] {
     // 获取相机设备支持的模式列表。
     let sceneModeArray: camera.SceneMode[] = cameraManager.getSupportedSceneModes(cameraDevice);
     if (sceneModeArray != undefined && sceneModeArray.length > 0) {
       for (let index = 0; index < sceneModeArray.length; index++) {
         console.info(`Camera SceneMode : ${sceneModeArray[index]}`);
       }
       return sceneModeArray;
     } else {
       console.error(`getSupportedSceneModes error`);
       return [];
     }
   }
   ```
4. 通过[getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)方法，获取当前相机设备支持的所有输出流，如预览流、拍照流、录像流等。输出流在[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的各个profile字段中，根据相机设备指定模式[SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)的不同，需要添加不同类型的输出流。

   ```typescript
   async getSupportedOutputCapabilityFn(cameraDevice: camera.CameraDevice, cameraManager: camera.CameraManager,
     sceneMode: camera.SceneMode): Promise<camera.CameraOutputCapability | undefined> {
     let cameraOutputCapability: camera.CameraOutputCapability;
     try {
       // 获取相机设备支持的输出流能力。
       cameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraDevice, sceneMode);
       if (!cameraOutputCapability) {
         console.error(`cameraManager.getSupportedOutputCapability error`);
         return undefined;
       }
       console.info(`outputCapability: ${JSON.stringify(cameraOutputCapability)}`);
       // 以NORMAL_PHOTO模式为例，需要添加预览流、拍照流。
       // previewProfiles属性为获取当前设备支持的预览输出流。
       let previewProfilesArray: camera.Profile[] = cameraOutputCapability.previewProfiles;
       if (!previewProfilesArray) {
         console.error(`createOutput previewProfilesArray == null || undefined`);
       }
       // photoProfiles属性为获取当前设备支持的拍照输出流。
       let photoProfilesArray: camera.Profile[] = cameraOutputCapability.photoProfiles;
       if (!photoProfilesArray) {
         console.error(`createOutput photoProfilesArray == null || undefined`);
       }
       return cameraOutputCapability;
     } catch (error) {
       let err = error as BusinessError;
       console.error(`getSupportedOutputCapability failed, err code: ${err.code}`);
       return undefined;
     }
   }
   ```
