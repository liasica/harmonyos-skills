---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-deferred-capture
title: 分段式拍照(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 分段式拍照(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:01+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:6bdd3edf91920f2f76924cfdd196a483d76bfe8ad99d907f426b6b25ac8a9e30
---

分段式拍照是相机的重要功能之一，即应用下发拍照任务后，系统将分多阶段上报不同质量的图片。

* 在第一阶段，系统快速上报轻量处理的图片，轻量处理的图片比全质量图低，出图速度快。应用通过回调会收到一个[PhotoAsset](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md)对象，通过该对象可调用媒体库接口，读取图片或落盘图片。
* 在第二阶段，相机框架会根据应用的请求图片诉求或在相机进入后台时，进行图像增强处理得到全质量图，并将处理好的图片传回给媒体库，替换轻量处理的图片。

通过分段式拍照，优化了系统的拍照响应时延，从而提升用户体验。

应用开发分段式拍照主要分为以下步骤：

* 通过PhotoOutput，监听photoAssetAvailable回调，获取[photoAccessHelper](../harmonyos-references/arkts-apis-photoaccesshelper.md)的PhotoAsset对象。
* 通过PhotoAsset对象，调用媒体库相关接口，读取或落盘图片。

**说明** 

* 分段式拍照能力由**设备**和**模式**决定，不同的设备支持的模式各异，对应分段式能力也有所差异，因此应用在切换设备或模式后分段式能力可能会发生变化。
* 应用无需主动使能分段式拍照能力，相机框架会在配流期间判断设备和模式是否支持分段式，如果支持会使能该功能。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入依赖，需要导入相机框架、媒体库、图片相关领域依赖。

   ```typescript
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 查询相机是否支持拍照模式。

   通过[getSupportedSceneModes](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedscenemodes11)接口获取传入镜头支持的模式，查询是否支持拍照模式。

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
3. 确定拍照输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的photoProfiles属性，可获取当前设备支持的拍照输出流，通过[createPhotoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法创建拍照输出流。

   ```typescript
   getPhotoOutput(cameraManager: camera.CameraManager,
     cameraOutputCapability: camera.CameraOutputCapability): camera.PhotoOutput | undefined {
     let photoProfilesArray: camera.Profile[] = cameraOutputCapability.photoProfiles;
     if (!photoProfilesArray || photoProfilesArray.length === 0) {
       console.error(`photoProfilesArray is null or []`);
       return undefined;
     }
     let photoOutput: camera.PhotoOutput | undefined = undefined;
     try {
       if (photoProfilesArray.length > 0) {
         photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
       } else {
         console.error(`the length of photoProfiles=0!`);
         return undefined;
       }
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to createPhotoOutput. error: ${err}`);
     }
     return photoOutput;
   }
   ```
4. 设置拍照photoAssetAvailable的回调。

   **注意** 

   如果已经注册了photoAssetAvailable回调，并且在Session开始之后又注册了photoAvailable回调，photoAssetAvailable和photoAvailable同时注册，会导致流被重启，仅photoAssetAvailable生效。

   不建议开发者同时注册[photoAvailable](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)和[photoAssetAvailable](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoassetavailable12)。

   ```typescript
   getPhotoAccessHelper(context: Context): photoAccessHelper.PhotoAccessHelper {
     let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
     return phAccessHelper;
   }

   onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput, context: Context): void {
     photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
       if (err) {
         console.error(`photoAssetAvailable error: ${err}.`);
         return;
       }
       console.info(`photoOutputCallBack photoAssetAvailable`);
       // 开发者可通过photoAsset调用媒体库相关接口，自定义处理图片。
       // 处理方式一：调用媒体库落盘接口保存一阶段图，二阶段图就绪后媒体库会主动帮应用替换落盘图片。
       this.mediaLibSavePhoto(photoAsset, this.getPhotoAccessHelper(context));
       // 处理方式二：调用媒体库接口请求图片并注册一阶段图或二阶段图buffer回调，自定义使用。
       this.mediaLibRequestBuffer(photoAsset, context);
     });
   }

   async mediaLibSavePhoto(photoAsset: photoAccessHelper.PhotoAsset,
     phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<void> {
     try {
       let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
         new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
       assetChangeRequest.saveCameraPhoto();
       await phAccessHelper.applyChanges(assetChangeRequest);
       console.info(`apply saveCameraPhoto successfully`);
     } catch (err) {
       console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
     }
   }

   async mediaLibRequestBuffer(photoAsset: photoAccessHelper.PhotoAsset, context: Context) {
     let requestOptions: photoAccessHelper.RequestOptions = {
       // 按照业务需求配置回图模式。
       // FAST_MODE：仅接收一阶段低质量图回调。
       // HIGH_QUALITY_MODE：仅接收二阶段全质量图回调。
       // BALANCE_MODE：接收一阶段及二阶段图片回调。
       deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
     }
     const handler = new MediaDataHandler();
     await photoAccessHelper.MediaAssetManager.requestImageData(context, photoAsset, requestOptions, handler);
     console.info(`requestImageData successfully`);
   }
   ```

   落盘图片参考媒体库接口：[saveCameraPhoto](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#savecameraphoto12)

   请求图片参考媒体库接口：[requestImageData](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager.md#requestimagedata11) 和 [onDataPrepared](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler.md#ondataprepared11)
5. 拍照时的会话配置及触发拍照的方式，与普通拍照相同，请参考[拍照](camera-shooting.md)的步骤6-7。

## 状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍照输出流的错误。

* 通过注册固定的captureStartWithInfo回调函数获取监听拍照开始结果，photoOutput创建成功时即可监听，相机设备已经准备开始这次拍照时触发，该事件返回此次拍照的captureId。

  ```typescript
  onPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
    photoOutput.on('captureStartWithInfo', (err: BusinessError, captureStartInfo: camera.CaptureStartInfo) => {
      if (err !== undefined && err.code !== 0) {
        return;
      }
      console.info(`photo capture started, captureId : ${captureStartInfo.captureId}`);
    });
  }
  ```
* 通过注册固定的captureEnd回调函数获取监听拍照结束结果，photoOutput创建成功时即可监听，该事件返回结果为拍照完全结束后的相关信息[CaptureEndInfo](../harmonyos-references/arkts-apis-camera-i.md#captureendinfo)。

  ```typescript
  onPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
    photoOutput.on('captureEnd', (err: BusinessError, captureEndInfo: camera.CaptureEndInfo) => {
      if (err !== undefined && err.code !== 0) {
        return;
      }
      console.info(`photo capture end, captureId : ${captureEndInfo.captureId}`);
      console.info(`frameCount : ${captureEndInfo.frameCount}`);
    });
  }
  ```
* 通过注册固定的captureReady回调函数获取监听可拍下一张结果，photoOutput创建成功时即可监听，当下一张可拍时触发，该事件返回结果为下一张可拍的相关信息。

  ```typescript
  onPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
    photoOutput.on('captureReady', (err: BusinessError) => {
      if (err !== undefined && err.code !== 0) {
        return;
      }
      console.info(`photo capture ready`);
    });
  }
  ```
* 通过注册固定的error回调函数获取监听拍照输出流的错误结果。callback返回拍照输出接口使用错误时的对应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```typescript
  onPhotoOutputError(photoOutput: camera.PhotoOutput): void {
    photoOutput.on('error', (error: BusinessError) => {
      console.error(`Photo output error code: ${error.code}`);
    });
  }
  ```
