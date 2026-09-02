---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-metadata
title: 元数据（ArkTS）
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 元数据（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:ac6a2f9a1b735b82b9b2acb4e15530563e98390a8c6356d59dac54241a0ecd5f
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

元数据（Metadata）是对相机返回的图像信息的描述和上下文。针对图像信息，提供更详细的数据，如照片或视频中，识别人像的取景框坐标的信息等。

Metadata主要是通过一个TAG（Key），去找对应的Data，用于传递参数和配置信息，减少内存拷贝操作。

## 适用场景

检测图片中的人脸，返回高精度的人脸矩形框坐标。应用可基于人脸定位结果，灵活集成后处理算法，将其应用于多样化场景。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入相关接口，导入方法如下。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的supportedMetadataObjectTypes属性，获取当前设备支持的元数据类型，并通过[createMetadataOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createmetadataoutput)方法创建元数据输出流。

   ```ts
   function getMetadataOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability): camera.MetadataOutput | undefined {
     let metadataObjectTypes: Array<camera.MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes;
     let metadataOutput: camera.MetadataOutput | undefined = undefined;
     try {
       metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to createMetadataOutput, error code: ${err.code}`);
     }
     return metadataOutput;
   }
   ```
3. 调用[Session.start](../harmonyos-references/arkts-apis-camera-session.md#start11)方法开启metadata数据输出，再通过监听事件metadataObjectsAvailable回调拿到数据，接口调用失败时，会返回相应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

   previewOutput获取方式请参考[相机预览开发步骤](camera-preview.md#开发步骤)。

   ```ts
   async function startMetadataOutput(previewOutput: camera.PreviewOutput, metadataOutput: camera.MetadataOutput, cameraManager: camera.CameraManager): Promise<void> {
     let cameraArray: Array<camera.CameraDevice> = [];
     try {
       cameraArray = cameraManager.getSupportedCameras();
       if (cameraArray.length == 0) {
         console.error('no camera.');
         return;
       }
       // 示例代码默认选择第一个镜头，实际开发需根据所需镜头。
       const cameraDevice: camera.CameraDevice = cameraArray[0];
       // 获取支持的模式类型。
       let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraDevice);
       let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
       if (!isSupportPhotoMode) {
         console.error('photo mode not support');
         return;
       }
       let cameraInput: camera.CameraInput | undefined = undefined;
       cameraInput = cameraManager.createCameraInput(cameraDevice);
       if (cameraInput === undefined) {
         console.error('cameraInput is undefined');
         return;
       }
       // 打开相机。
       await cameraInput.open();
       let session = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
       if (!session) {
         console.error('session is null');
         return;
       }
       let photoSession: camera.PhotoSession = session as camera.PhotoSession;
       photoSession.beginConfig();
       photoSession.addInput(cameraInput);
       photoSession.addOutput(previewOutput);
       photoSession.addOutput(metadataOutput);
       await photoSession.commitConfig();
       await photoSession.start();
     } catch (error) {
       console.error('startMetadataOutput call failed');
     }
   }
   ```
4. 调用[Session.stop](../harmonyos-references/arkts-apis-camera-session.md#stop11)方法停止输出metadata数据，接口调用失败会返回相应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

   ```ts
   function stopMetadataOutput(session: camera.Session): void {
     session.stop().then(() => {
       console.info('Callback returned with session stopped.');
     }).catch((err: BusinessError) => {
       console.error(`Failed to session stop, error code: ${err.code}`);
     });
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听metadata数据以及输出流的状态。

* 通过注册监听获取metadata对象，监听事件固定为metadataObjectsAvailable。检测到有效metadata数据时，callback返回相应的metadata数据信息，metadataOutput创建成功时可监听。

  ```ts
  function onMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
    metadataOutput.on('metadataObjectsAvailable', (err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>) => {
      if (err !== undefined && err.code !== 0) {
        return;
      }
      console.info('metadata output metadataObjectsAvailable');
    });
  }
  ```

  **说明** 

  当前的元数据类型仅支持人脸检测（FACE\_DETECTION）功能。元数据信息对象为识别到的人脸区域的矩形信息（Rect），包含矩形区域的左上角x坐标、y坐标和矩形的宽高数据。
* 通过注册回调函数，获取监听metadata流的错误结果，callback返回metadata输出接口使用错误时返回的错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```ts
  function onMetadataError(metadataOutput: camera.MetadataOutput): void {
    metadataOutput.on('error', (metadataOutputError: BusinessError) => {
      console.error(`Metadata output error code: ${metadataOutputError.code}`);
    });
  }
  ```
