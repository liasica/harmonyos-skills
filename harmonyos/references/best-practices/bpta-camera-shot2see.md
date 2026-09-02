---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-camera-shot2see
title: 相机分段式拍照性能优化
breadcrumb: 最佳实践 > 媒体 > 相机 > 相机分段式拍照性能优化
category: best-practices
scraped_at: 2026-09-02T14:53:40+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:018704a20bcdc0fdbc4a2dceacabf821b31fb8a8292cc9f19307c50ea173687e
---

## 概述

相机拍照性能依赖算法处理的速度，而处理效果依赖算法的复杂度，算法复杂度越高的情况下会导致处理时间越长。目前系统相机开发有两种相机拍照方案，分别是[相机分段式拍照](../harmonyos-guides/camera-deferred-capture.md)和[相机单段式拍照](../harmonyos-guides/camera-shooting.md)：

* **分段式拍照**是系统相机开发的重要功能之一，即相机拍照可输出低质量图用作缩略图，提升用户感知拍照速度，同时使用高质量图保证最后的成图质量达到系统相机的水平，既满足了图像处理算法的需求，又不会阻塞前台的拍照速度，构筑相机性能竞争力，提升了用户的体验。

* **单段式拍照**是指在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，这样导致Shot2See（用户点击拍照控件到在缩略图显示区域显示缩略图的过程）完成时延比较长。

分段式与单段式拍照的全质量图输出质量一致，但输出低质量图场景下单段式更优。如果开发者不需要获取全质量图并且也不考虑Shot2See的完成时延，建议使用单段式拍照，否则的话，建议使用分段式拍照。本篇文章主要以相机Shot2See场景为例，来展示分段式拍照Shot2See的完成时延要低于单段式拍照。

**图1** **分段式拍照流程示意图**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/JbgAB0QEQNuxeO_XIpE6pA/zh-cn_image_0000002229450197.png "点击放大")

## 效果展示

**图2** **单段式拍照效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/tMnm5rz7RKCnNToLCE-Fvw/zh-cn_image_0000002193850332.gif "点击放大")

**图3** **分段式拍照效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/hlskcNaoS-Sdu8wp7FgJaw/zh-cn_image_0000002229450193.gif "点击放大")

从上述效果图中可以看出，分段式拍照从用户点击拍照控件到在缩略图显示区域显示缩略图的耗时比单段式拍照要短。

## 性能对比分析方式

静态校验：在相机类应用中，如果使用单段式拍照，拍照过程中该场景下仅会返回一张图片，将图片用作Shot2See后的缩略图则会导致Shot2See完成时延比较长。

动态校验：开发者可以通过DevEco Studio中的Profiler工具去抓取Trace，获取到Trace之后，根据PhotoOutputNapi::Capture()和OnBufferAvailable()找到对应的Trace Marker，并通过两者之间的时间段来分析耗时，单段式拍照的时长为1900ms，而分段式拍照的时长为672.7ms。

**图4** **单段式拍照性能数据图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/yN1W7t2CRiqkIrN7P1hCLg/zh-cn_image_0000002229450189.png "点击放大")

**图5** **分段式拍照耗时数据****图**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/6xmx3IwZSy22vnASe1B37w/zh-cn_image_0000002229450205.png "点击放大")

**性能对比分析表**

| **拍照实现方式** | **耗时(局限不同设备和场景，数据仅供参考)** |
| --- | --- |
| 单段式拍照 | 1900ms |
| 分段式拍照 | 672.7ms |

优化思路：在需要加快Shot2See完成时延的场景下，使用相机框架开发的分段式拍照方案，加快阶段一照片生成的速度。

## 场景示例

下面以应用中相机Shot2See（拍照之后自动跳转到照片编辑界面）为例，通过单段式拍照和分段式拍照的性能功耗对比，来展示两者的性能差异。

**单段式拍照：**

单段式拍照使用了[on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)接口注册了高质量图的监听，默认不使能分段式拍照。具体操作步骤如下所示：

1.相机媒体数据写入[XComponent组件](../harmonyos-references/ts-basic-components-xcomponent.md)中，用来显示图像效果。具体代码如下所示：

```typescript
XComponent({
  type: XComponentType.SURFACE,
  controller: this.mXComponentController,
  imageAIOptions: this.options
})
  .onLoad(async () => {
    Logger.info(TAG, 'onLoad is called');
    this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
    GlobalContext.get().setObject('cameraDeviceIndex', this.defaultCameraDeviceIndex);
    GlobalContext.get().setObject('xComponentSurfaceId', this.surfaceId);
    Logger.info(TAG, `onLoad surfaceId: ${this.surfaceId}`);
    await CameraService.initCamera(this.surfaceId, this.defaultCameraDeviceIndex);
  })
  .border({
    width: {
      top: Constants.X_COMPONENT_BORDER_WIDTH,
      bottom: Constants.X_COMPONENT_BORDER_WIDTH
    },
    color: Color.Black
  })
  .width('100%')
  .height(523)
  .margin({ top: 75, bottom: 72 })
```

2.initCamera函数完成一个相机生命周期初始化的过程。

(1) [getCameraManager()](../harmonyos-references/arkts-apis-camera-f.md#cameragetcameramanager)获取CameraMananger相机管理器类。

(2) [getSupportedCameras()](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras) 和[getSupportedOutputCapability()](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)方法获取支持的camera设备以及设备能力集。

(3) [createPreviewOutput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createpreviewoutput12)和[createPhotoOutput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法创建预览输出和拍照输出对象。

(4) CameraInput的open()方法打开相机输入。

(5) onCameraStatusChange()函数创建CameraManager注册回调。

(6) 最后调用sessionFlowFn()函数创建并开启Session。具体代码如下所示：

```typescript
/**
 * Initialize Camera Functions
 * @param surfaceId - Surface ID
 * @param cameraDeviceIndex - Camera Device Index
 * @returns No return value
 */
async initCamera(surfaceId: string, cameraDeviceIndex: number): Promise<void> {
  Logger.debug(TAG, `initCamera cameraDeviceIndex: ${cameraDeviceIndex}`);
  this.photoMode = AppStorage.get('photoMode');
  if (!this.photoMode) {
    return;
  }
  try {
    await this.releaseCamera();
    // Get Camera Manager Instance
    this.cameraManager = this.getCameraManagerFn();
    if (this.cameraManager === undefined) {
      Logger.error(TAG, 'cameraManager is undefined');
      return;
    }
    // Gets the camera device object that supports the specified
    this.cameras = this.getSupportedCamerasFn(this.cameraManager);
    if (this.cameras.length < 1 || this.cameras.length < cameraDeviceIndex + 1) {
      return;
    }
    this.curCameraDevice = this.cameras[cameraDeviceIndex];
    let isSupported = this.isSupportedSceneMode(this.cameraManager, this.curCameraDevice);
    if (!isSupported) {
      Logger.error(TAG, 'The current scene mode is not supported.');
      return;
    }
    let cameraOutputCapability =
      this.cameraManager.getSupportedOutputCapability(this.curCameraDevice, this.curSceneMode);
    let previewProfile = this.getPreviewProfile(cameraOutputCapability);
    if (previewProfile === undefined) {
      Logger.error(TAG, 'The resolution of the current preview stream is not supported.');
      return;
    }
    this.previewProfileObj = previewProfile;
    // Creates the previewOutput output object
    this.previewOutput = this.createPreviewOutputFn(this.cameraManager, this.previewProfileObj, surfaceId);
    if (this.previewOutput === undefined) {
      Logger.error(TAG, 'Failed to create the preview stream.');
      return;
    }
    // Listening for preview events
    this.previewOutputCallBack(this.previewOutput);
    let photoProfile = this.getPhotoProfile(cameraOutputCapability);
    if (photoProfile === undefined) {
      Logger.error(TAG, 'The resolution of the current photo stream is not supported.');
      return;
    }
    this.photoProfileObj = photoProfile;
    // Creates a photoOutPut output object
    this.photoOutput = this.createPhotoOutputFn(this.cameraManager, this.photoProfileObj);
    if (this.photoOutput === undefined) {
      Logger.error(TAG, 'Failed to create the photo stream.');
      return;
    }
    // Creates a cameraInput output object
    this.cameraInput = this.createCameraInputFn(this.cameraManager, this.curCameraDevice);
    if (this.cameraInput === undefined) {
      Logger.error(TAG, 'Failed to create the camera input.');
      return;
    }
    // Turn on the camera
    let isOpenSuccess = await this.cameraInputOpenFn(this.cameraInput);
    if (!isOpenSuccess) {
      Logger.error(TAG, 'Failed to open the camera.');
      return;
    }
    // Camera status callback
    this.onCameraStatusChange(this.cameraManager);
    // Listens to CameraInput error events
    this.onCameraInputChange(this.cameraInput, this.curCameraDevice);
    // Session Process
    await this.sessionFlowFn(this.cameraManager, this.cameraInput, this.previewOutput, this.photoOutput);
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `initCamera fail: ${JSON.stringify(err)}`);
  }
}
```

3.确定拍照输出流。通过cameraManager.createPhotoOutput()方法创建拍照输出流，参数为[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)类中的photoProfiles属性。

```typescript
/**
 * Creates a photoOutPut output object
 */
createPhotoOutputFn(cameraManager: camera.CameraManager,
  photoProfileObj: camera.Profile): camera.PhotoOutput | undefined {
  let photoOutput: camera.PhotoOutput;
  try {
    photoOutput = cameraManager.createPhotoOutput(photoProfileObj);
    Logger.info(TAG, `createPhotoOutputFn success: ${photoOutput}`);
    return photoOutput;
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `createPhotoOutputFn failed: ${JSON.stringify(err)}`);
    return undefined;
  }
}
```

4.触发拍照。通过photoOutput类的[capture()](../harmonyos-references/arkts-apis-camera-photooutput.md#capture)方法，执行拍照任务。该方法有两个参数，分别为拍照设置参数的setting以及回调函数，setting中可以设置照片的质量和旋转角度。具体代码如下所示：

```typescript
/**
 * Trigger a photo taking based on the specified parameters
 */
async takePicture(): Promise<void> {
  Logger.info(TAG, 'takePicture start');
  let cameraDeviceIndex = GlobalContext.get().getT<number>('cameraDeviceIndex');
  let photoSettings: camera.PhotoCaptureSetting = {
    quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
    mirror: cameraDeviceIndex ? true : false
  };
  try {
    await this.photoOutput?.capture(photoSettings);
    Logger.info(TAG, 'takePicture end');
  } catch (error) {
    let err = error as BusinessError;
    Logger.warn('testTag', `capture failed, code=${err.code}, message=${err.message}`);
  }
}
```

5.设置拍照photoAvailable()的回调来获取Photo对象，点击拍照按钮，触发此回调函数，调用getComponent()方法根据图像的组件类型从图像中获取组件缓存ArrayBuffer，使用createImageSource()方法来创建图片源实例，最后通过createPixelMap()获取PixelMap对象。注意:如果已经注册了photoAssetAvailable()回调，并且在Session开始之后又注册了photoAvailable()回调，会导致流被重启。不建议开发者同时注册photoAvailable()和photoAssetAvailable()。

```typescript
photoOutput.on('photoAvailable', (err: BusinessError, photo: camera.Photo) => {
  Logger.info(TAG, 'photoAvailable begin');
  if (err) {
    Logger.error(TAG, `photoAvailable err:${err.code}`);
    return;
  }
  let imageObj: image.Image = photo.main;
  imageObj.getComponent(image.ComponentType.JPEG, (err: BusinessError, component: image.Component) => {
    Logger.info(TAG, `getComponent start`);
    if (err) {
      Logger.error(TAG, `getComponent err:${err.code}`);
      return;
    }
    let buffer: ArrayBuffer = component.byteBuffer;
    let imageSource: image.ImageSource = image.createImageSource(buffer);
    imageSource.createPixelMap((err: BusinessError, pixelMap: image.PixelMap) => {
      if (err) {
        Logger.error(TAG, `createPixelMap err:${err.code}`);
        return;
      }
      this.handlePhotoAssetCb(pixelMap);
    });

  });
})
```

以上代码中执行handleImageInfo()函数来对PixelMap进行全局存储并跳转到预览页面。具体代码如下所示：

```typescript
handleSavePicture = (photoAsset: photoAccessHelper.PhotoAsset | image.PixelMap): void => {
  Logger.info(TAG, 'handleSavePicture');
  this.setImageInfo(photoAsset);
  AppStorage.set<boolean>('isOpenEditPage', true);
  Logger.info(TAG, 'setImageInfo end');
}

setImageInfo(photoAsset: photoAccessHelper.PhotoAsset | image.PixelMap): void {
  Logger.info(TAG, 'setImageInfo');
  GlobalContext.get().setObject('photoAsset', photoAsset);
}
```

6.进入到预览界面，通过GlobalContext.get().getT<image.PixelMap>('imageInfo')方法获取PixelMap信息，并通过Image组件进行渲染显示。

**分段式拍照：**

分段式拍照是应用下发拍照任务后，系统将分多阶段上报不同质量的图片。在一阶段，系统快速上报低质量图，应用通过[on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoassetavailable12)接口会收到一个PhotoAsset对象，通过该对象可调用媒体库接口，读取图片或落盘图片。在二阶段，分段式子服务会根据系统压力以及定制化场景进行调度，将后处理好的原图回传给媒体库，替换低质量图。具体操作步骤如下所示：

由于分段式拍照和单段式拍照步骤1-步骤4相同，就不再进行赘述。

5.设置拍照photoAssetAvailable()的回调来获取photoAsset，点击拍照按钮，触发此回调函数，然后执行handlePhotoAssetCb()函数来完成photoAsset全局的存储并跳转到预览页面。

```typescript
photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
  Logger.info(TAG, 'photoAssetAvailable begin');
  if (err) {
    Logger.error(TAG, `photoAssetAvailable err:${err.code}`);
    return;
  }
  this.handlePhotoAssetCb(photoAsset);
});
```

6.进入预览界面通过GlobalContext.get().getT<image.PixelMap>('imageInfo')方法获取PhotoAsset信息，执行requestImage函数中的photoAccessHelper.MediaAssetManager.requestImageData()方法根据不同的策略模式，请求图片资源数据，这里的请求策略为均衡模式BALANCE\_MODE， 最后分段式子服务会根据系统压力以及定制化场景进行调度，将后处理好的原图回传给媒体库来替换低质量图。具体代码如下所示：

```screen
photoBufferCallback: (arrayBuffer: ArrayBuffer) => void = (arrayBuffer: ArrayBuffer) => {
  Logger.info(TAG, 'photoBufferCallback is called');
  let imageSource = image.createImageSource(arrayBuffer);
  imageSource.createPixelMap((err: BusinessError, data: image.PixelMap) => {
    if (err) {
      Logger.info(TAG, `createPixelMap err:${err.code}`);
      return;
    }
    Logger.info(TAG, 'createPixelMap is called');
    this.curPixelMap = data;
  });
};

requestImage(requestImageParams: RequestImageParams): void {
  class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
    onDataPrepared(data: ArrayBuffer, map: Map<string, string>): void {
      Logger.info(TAG, 'onDataPrepared map' + JSON.stringify(map));
      requestImageParams.callback(data);
      Logger.info(TAG, 'onDataPrepared end');
    }
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.BALANCE_MODE,
  };
  const handler = new MediaDataHandler();
  photoAccessHelper.MediaAssetManager.requestImageData(requestImageParams.context, requestImageParams.photoAsset,
    requestOptions, handler)
    .then(() => {
      Logger.info(TAG, 'requestImageData success');
    })
    .catch((err: BusinessError) => {
      Logger.error(TAG, `requestImageData failed, code=${err.code}, message=${err.message}`)
    })
}

aboutToAppear() {
  Logger.info(TAG, 'aboutToAppear begin');
  if (this.photoMode === Constants.SUBSECTION_MODE) {
    let curPhotoAsset = GlobalContext.get().getT<photoAccessHelper.PhotoAsset>('photoAsset');
    this.photoUri = curPhotoAsset.uri;
    let requestImageParams: RequestImageParams = {
      context: this.getUIContext().getHostContext(),
      photoAsset: curPhotoAsset,
      callback: this.photoBufferCallback
    };
    this.requestImage(requestImageParams);
    Logger.info(TAG, `aboutToAppear photoUri: ${this.photoUri}`);
  } else if (this.photoMode === Constants.SINGLE_STAGE_MODE) {
    this.curPixelMap = GlobalContext.get().getT<image.PixelMap>('photoAsset');
  }
}
```

7.将步骤6获取的PixelMap对象数据通过Image组件进行渲染显示。

## 总结

通过分段式拍照，确保低质量图可接受的基础上，加快了Shot2See的完成时延，同时第二段保证了高质量照片不损失图片效果，达到与系统相机一致的拍照质量。

## 示例代码

* [实现相机分段式拍照功能](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/SegmentedPhotograph)
