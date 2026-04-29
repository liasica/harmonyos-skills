---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-camera-shot2see
title: 相机分段式拍照性能优化
breadcrumb: 最佳实践 > 媒体 > 相机 > 相机分段式拍照性能优化
category: best-practices
scraped_at: 2026-04-29T14:11:07+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a7704747aa91b5cc1fbb9214931f29093254af27cbabe2715cf24e7614c48624
---

## 概述

相机拍照性能依赖算法处理的速度，而处理效果依赖算法的复杂度，算法复杂度越高的情况下会导致处理时间越长。目前系统相机开发有两种相机拍照方案，分别是[相机分段式拍照](../harmonyos-guides/camera-deferred-capture.md)和[相机单段式拍照](../harmonyos-guides/camera-shooting.md)：

* **分段式拍照**是系统相机开发的重要功能之一，即相机拍照可输出低质量图用作缩略图，提升用户感知拍照速度，同时使用高质量图保证最后的成图质量达到系统相机的水平，既满足了图像处理算法的需求，又不会阻塞前台的拍照速度，构筑相机性能竞争力，提升了用户的体验。

* **单段式拍照**是指在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，这样导致Shot2See（用户点击拍照控件到在缩略图显示区域显示缩略图的过程）完成时延比较长。

分段式与单段式拍照的全质量图输出质量一致，但输出低质量图场景下单段式更优。如果开发者不需要获取全质量图并且也不考虑Shot2See的完成时延，建议使用单段式拍照，否则的话，建议使用分段式拍照。本篇文章主要以相机Shot2See场景为例，来展示分段式拍照Shot2See的完成时延要低于单段式拍照。

**图1** **分段式拍照流程示意图**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/PZ6IHpFZRxCL9upFNnLM4A/zh-cn_image_0000002229450197.png?HW-CC-KV=V1&HW-CC-Date=20260429T061105Z&HW-CC-Expire=86400&HW-CC-Sign=A29C9185485E660404626B06ADF265AEE8EFA7C0E97DE5702B83DAA455566160 "点击放大")

## 效果展示

**图2** **单段式拍照效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/UQbu2nBPTH2d3-D3KAKr4w/zh-cn_image_0000002193850332.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061105Z&HW-CC-Expire=86400&HW-CC-Sign=3E5A50DD49DDE3EBA19371C352E8223F551E516992359EF081B05CD3B3914235)

**图3** **分段式拍照效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/4DuuzZ7wRZ2VWDRi0G3NTA/zh-cn_image_0000002229450193.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061105Z&HW-CC-Expire=86400&HW-CC-Sign=47EED4300E7A6FBA42D3A0D85A8F01434319DE8B8181BCBC02849B5FA4C77D05)

从上述效果图中可以看出，分段式拍照从用户点击拍照控件到在缩略图显示区域显示缩略图的耗时比单段式拍照要短。

## 性能对比分析方式

静态校验：在相机类应用中，如果使用单段式拍照，拍照过程中该场景下仅会返回一张图片，将图片用作Shot2See后的缩略图则会导致Shot2See完成时延比较长。

动态校验：开发者可以通过DevEco Studio中的Profiler工具去抓取Trace，获取到Trace之后，根据PhotoOutputNapi::Capture()和OnBufferAvailable()找到对应的Trace Marker，并通过两者之间的时间段来分析耗时，单段式拍照的时长为1900ms，而分段式拍照的时长为672.7ms。

**图4** **单段式拍照性能数据图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/S2lOs8IrTTK6GHG9jrXCWw/zh-cn_image_0000002229450189.png?HW-CC-KV=V1&HW-CC-Date=20260429T061105Z&HW-CC-Expire=86400&HW-CC-Sign=DAFA635DC8F49E44DC45B453165128380ECF378DCFFE770BC67C6F2F68C27D51 "点击放大")

**图5** **分段式拍照耗时数据****图**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/K_DB-llHQeuQbL2e--Tz2w/zh-cn_image_0000002229450205.png?HW-CC-KV=V1&HW-CC-Date=20260429T061105Z&HW-CC-Expire=86400&HW-CC-Sign=D2267D16F20F952BB15F1D215E2C510484ED94A2B1B4906626EBFB0245F93253 "点击放大")

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

```
1. XComponent({
2. type: XComponentType.SURFACE,
3. controller: this.mXComponentController,
4. imageAIOptions: this.options
5. })
6. .onLoad(async () => {
7. Logger.info(TAG, 'onLoad is called');
8. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
9. GlobalContext.get().setObject('cameraDeviceIndex', this.defaultCameraDeviceIndex);
10. GlobalContext.get().setObject('xComponentSurfaceId', this.surfaceId);
11. Logger.info(TAG, `onLoad surfaceId: ${this.surfaceId}`);
12. await CameraService.initCamera(this.surfaceId, this.defaultCameraDeviceIndex);
13. })
14. .border({
15. width: {
16. top: Constants.X_COMPONENT_BORDER_WIDTH,
17. bottom: Constants.X_COMPONENT_BORDER_WIDTH
18. },
19. color: Color.Black
20. })
21. .width('100%')
22. .height(523)
23. .margin({ top: 75, bottom: 72 })
```

[PhotoPage.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/pages/PhotoPage.ets#L97-L119)

2.initCamera函数完成一个相机生命周期初始化的过程。

(1) [getCameraManager()](../harmonyos-references/arkts-apis-camera-f.md#cameragetcameramanager)获取CameraMananger相机管理器类。

(2) [getSupportedCameras()](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras) 和[getSupportedOutputCapability()](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)方法获取支持的camera设备以及设备能力集。

(3) [createPreviewOutput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createpreviewoutput12)和[createPhotoOutput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法创建预览输出和拍照输出对象。

(4) CameraInput的open()方法打开相机输入。

(5) onCameraStatusChange()函数创建CameraManager注册回调。

(6) 最后调用sessionFlowFn()函数创建并开启Session。具体代码如下所示：

```
1. /**
2. * Initialize Camera Functions
3. * @param surfaceId - Surface ID
4. * @param cameraDeviceIndex - Camera Device Index
5. * @returns No return value
6. */
7. async initCamera(surfaceId: string, cameraDeviceIndex: number): Promise<void> {
8. Logger.debug(TAG, `initCamera cameraDeviceIndex: ${cameraDeviceIndex}`);
9. this.photoMode = AppStorage.get('photoMode');
10. if (!this.photoMode) {
11. return;
12. }
13. try {
14. await this.releaseCamera();
15. // Get Camera Manager Instance
16. this.cameraManager = this.getCameraManagerFn();
17. if (this.cameraManager === undefined) {
18. Logger.error(TAG, 'cameraManager is undefined');
19. return;
20. }
21. // Gets the camera device object that supports the specified
22. this.cameras = this.getSupportedCamerasFn(this.cameraManager);
23. if (this.cameras.length < 1 || this.cameras.length < cameraDeviceIndex + 1) {
24. return;
25. }
26. this.curCameraDevice = this.cameras[cameraDeviceIndex];
27. let isSupported = this.isSupportedSceneMode(this.cameraManager, this.curCameraDevice);
28. if (!isSupported) {
29. Logger.error(TAG, 'The current scene mode is not supported.');
30. return;
31. }
32. let cameraOutputCapability =
33. this.cameraManager.getSupportedOutputCapability(this.curCameraDevice, this.curSceneMode);
34. let previewProfile = this.getPreviewProfile(cameraOutputCapability);
35. if (previewProfile === undefined) {
36. Logger.error(TAG, 'The resolution of the current preview stream is not supported.');
37. return;
38. }
39. this.previewProfileObj = previewProfile;
40. // Creates the previewOutput output object
41. this.previewOutput = this.createPreviewOutputFn(this.cameraManager, this.previewProfileObj, surfaceId);
42. if (this.previewOutput === undefined) {
43. Logger.error(TAG, 'Failed to create the preview stream.');
44. return;
45. }
46. // Listening for preview events
47. this.previewOutputCallBack(this.previewOutput);
48. let photoProfile = this.getPhotoProfile(cameraOutputCapability);
49. if (photoProfile === undefined) {
50. Logger.error(TAG, 'The resolution of the current photo stream is not supported.');
51. return;
52. }
53. this.photoProfileObj = photoProfile;
54. // Creates a photoOutPut output object
55. this.photoOutput = this.createPhotoOutputFn(this.cameraManager, this.photoProfileObj);
56. if (this.photoOutput === undefined) {
57. Logger.error(TAG, 'Failed to create the photo stream.');
58. return;
59. }
60. // Creates a cameraInput output object
61. this.cameraInput = this.createCameraInputFn(this.cameraManager, this.curCameraDevice);
62. if (this.cameraInput === undefined) {
63. Logger.error(TAG, 'Failed to create the camera input.');
64. return;
65. }
66. // Turn on the camera
67. let isOpenSuccess = await this.cameraInputOpenFn(this.cameraInput);
68. if (!isOpenSuccess) {
69. Logger.error(TAG, 'Failed to open the camera.');
70. return;
71. }
72. // Camera status callback
73. this.onCameraStatusChange(this.cameraManager);
74. // Listens to CameraInput error events
75. this.onCameraInputChange(this.cameraInput, this.curCameraDevice);
76. // Session Process
77. await this.sessionFlowFn(this.cameraManager, this.cameraInput, this.previewOutput, this.photoOutput);
78. } catch (error) {
79. let err = error as BusinessError;
80. Logger.error(TAG, `initCamera fail: ${JSON.stringify(err)}`);
81. }
82. }
```

[CameraService.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/mode/CameraService.ets#L124-L206)

3.确定拍照输出流。通过cameraManager.createPhotoOutput()方法创建拍照输出流，参数为[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)类中的photoProfiles属性。

```
1. /**
2. * Creates a photoOutPut output object
3. */
4. createPhotoOutputFn(cameraManager: camera.CameraManager,
5. photoProfileObj: camera.Profile): camera.PhotoOutput | undefined {
6. let photoOutput: camera.PhotoOutput;
7. try {
8. photoOutput = cameraManager.createPhotoOutput(photoProfileObj);
9. Logger.info(TAG, `createPhotoOutputFn success: ${photoOutput}`);
10. return photoOutput;
11. } catch (error) {
12. let err = error as BusinessError;
13. Logger.error(TAG, `createPhotoOutputFn failed: ${JSON.stringify(err)}`);
14. return undefined;
15. }
16. }
```

[CameraService.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/mode/CameraService.ets#L363-L379)

4.触发拍照。通过photoOutput类的[capture()](../harmonyos-references/arkts-apis-camera-photooutput.md#capture)方法，执行拍照任务。该方法有两个参数，分别为拍照设置参数的setting以及回调函数，setting中可以设置照片的质量和旋转角度。具体代码如下所示：

```
1. /**
2. * Trigger a photo taking based on the specified parameters
3. */
4. async takePicture(): Promise<void> {
5. Logger.info(TAG, 'takePicture start');
6. let cameraDeviceIndex = GlobalContext.get().getT<number>('cameraDeviceIndex');
7. let photoSettings: camera.PhotoCaptureSetting = {
8. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
9. mirror: cameraDeviceIndex ? true : false
10. };
11. try {
12. await this.photoOutput?.capture(photoSettings);
13. Logger.info(TAG, 'takePicture end');
14. } catch (error) {
15. let err = error as BusinessError;
16. Logger.warn('testTag', `capture failed, code=${err.code}, message=${err.message}`);
17. }
18. }
```

[CameraService.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/mode/CameraService.ets#L249-L267)

5.设置拍照photoAvailable()的回调来获取Photo对象，点击拍照按钮，触发此回调函数，调用getComponent()方法根据图像的组件类型从图像中获取组件缓存ArrayBuffer，使用createImageSource()方法来创建图片源实例，最后通过createPixelMap()获取PixelMap对象。注意:如果已经注册了photoAssetAvailable()回调，并且在Session开始之后又注册了photoAvailable()回调，会导致流被重启。不建议开发者同时注册photoAvailable()和photoAssetAvailable()。

```
1. photoOutput.on('photoAvailable', (err: BusinessError, photo: camera.Photo) => {
2. Logger.info(TAG, 'photoAvailable begin');
3. if (err) {
4. Logger.error(TAG, `photoAvailable err:${err.code}`);
5. return;
6. }
7. let imageObj: image.Image = photo.main;
8. imageObj.getComponent(image.ComponentType.JPEG, (err: BusinessError, component: image.Component) => {
9. Logger.info(TAG, `getComponent start`);
10. if (err) {
11. Logger.error(TAG, `getComponent err:${err.code}`);
12. return;
13. }
14. let buffer: ArrayBuffer = component.byteBuffer;
15. let imageSource: image.ImageSource = image.createImageSource(buffer);
16. imageSource.createPixelMap((err: BusinessError, pixelMap: image.PixelMap) => {
17. if (err) {
18. Logger.error(TAG, `createPixelMap err:${err.code}`);
19. return;
20. }
21. this.handlePhotoAssetCb(pixelMap);
22. });

24. });
25. })
```

[CameraService.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/mode/CameraService.ets#L522-L546)

以上代码中执行handleImageInfo()函数来对PixelMap进行全局存储并跳转到预览页面。具体代码如下所示：

```
1. handleSavePicture = (photoAsset: photoAccessHelper.PhotoAsset | image.PixelMap): void => {
2. Logger.info(TAG, 'handleSavePicture');
3. this.setImageInfo(photoAsset);
4. AppStorage.set<boolean>('isOpenEditPage', true);
5. Logger.info(TAG, 'setImageInfo end');
6. }

8. setImageInfo(photoAsset: photoAccessHelper.PhotoAsset | image.PixelMap): void {
9. Logger.info(TAG, 'setImageInfo');
10. GlobalContext.get().setObject('photoAsset', photoAsset);
11. }
```

[ModeComponent.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/views/ModeComponent.ets#L44-L54)

6.进入到预览界面，通过GlobalContext.get().getT<image.PixelMap>('imageInfo')方法获取PixelMap信息，并通过Image组件进行渲染显示。

**分段式拍照：**

分段式拍照是应用下发拍照任务后，系统将分多阶段上报不同质量的图片。在一阶段，系统快速上报低质量图，应用通过[on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoassetavailable12)接口会收到一个PhotoAsset对象，通过该对象可调用媒体库接口，读取图片或落盘图片。在二阶段，分段式子服务会根据系统压力以及定制化场景进行调度，将后处理好的原图回传给媒体库，替换低质量图。具体操作步骤如下所示：

由于分段式拍照和单段式拍照步骤1-步骤4相同，就不再进行赘述。

5.设置拍照photoAssetAvailable()的回调来获取photoAsset，点击拍照按钮，触发此回调函数，然后执行handlePhotoAssetCb()函数来完成photoAsset全局的存储并跳转到预览页面。

```
1. photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
2. Logger.info(TAG, 'photoAssetAvailable begin');
3. if (err) {
4. Logger.error(TAG, `photoAssetAvailable err:${err.code}`);
5. return;
6. }
7. this.handlePhotoAssetCb(photoAsset);
8. });
```

[CameraService.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/mode/CameraService.ets#L511-L518)

6.进入预览界面通过GlobalContext.get().getT<image.PixelMap>('imageInfo')方法获取PhotoAsset信息，执行requestImage函数中的photoAccessHelper.MediaAssetManager.requestImageData()方法根据不同的策略模式，请求图片资源数据，这里的请求策略为均衡模式BALANCE\_MODE， 最后分段式子服务会根据系统压力以及定制化场景进行调度，将后处理好的原图回传给媒体库来替换低质量图。具体代码如下所示：

```
1. photoBufferCallback: (arrayBuffer: ArrayBuffer) => void = (arrayBuffer: ArrayBuffer) => {
2. Logger.info(TAG, 'photoBufferCallback is called');
3. let imageSource = image.createImageSource(arrayBuffer);
4. imageSource.createPixelMap((err: BusinessError, data: image.PixelMap) => {
5. if (err) {
6. Logger.info(TAG, `createPixelMap err:${err.code}`);
7. return;
8. }
9. Logger.info(TAG, 'createPixelMap is called');
10. this.curPixelMap = data;
11. });
12. };

14. requestImage(requestImageParams: RequestImageParams): void {
15. class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
16. onDataPrepared(data: ArrayBuffer, map: Map<string, string>): void {
17. Logger.info(TAG, 'onDataPrepared map' + JSON.stringify(map));
18. requestImageParams.callback(data);
19. Logger.info(TAG, 'onDataPrepared end');
20. }
21. };
22. let requestOptions: photoAccessHelper.RequestOptions = {
23. deliveryMode: photoAccessHelper.DeliveryMode.BALANCE_MODE,
24. };
25. const handler = new MediaDataHandler();
26. photoAccessHelper.MediaAssetManager.requestImageData(requestImageParams.context, requestImageParams.photoAsset,
27. requestOptions, handler)
28. .then(() => {
29. Logger.info(TAG, 'requestImageData success');
30. })
31. .catch((err: BusinessError) => {
32. Logger.error(TAG, `requestImageData failed, code=${err.code}, message=${err.message}`)
33. })
34. }

36. aboutToAppear() {
37. Logger.info(TAG, 'aboutToAppear begin');
38. if (this.photoMode === Constants.SUBSECTION_MODE) {
39. let curPhotoAsset = GlobalContext.get().getT<photoAccessHelper.PhotoAsset>('photoAsset');
40. this.photoUri = curPhotoAsset.uri;
41. let requestImageParams: RequestImageParams = {
42. context: this.getUIContext().getHostContext(),
43. photoAsset: curPhotoAsset,
44. callback: this.photoBufferCallback
45. };
46. this.requestImage(requestImageParams);
47. Logger.info(TAG, `aboutToAppear photoUri: ${this.photoUri}`);
48. } else if (this.photoMode === Constants.SINGLE_STAGE_MODE) {
49. this.curPixelMap = GlobalContext.get().getT<image.PixelMap>('photoAsset');
50. }
51. }
```

[EditPage.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SegmentedPhotograph/entry/src/main/ets/pages/EditPage.ets#L42-L93)

7.将步骤6获取的PixelMap对象数据通过Image组件进行渲染显示。

## 总结

通过分段式拍照，确保低质量图可接受的基础上，加快了Shot2See的完成时延，同时第二段保证了高质量照片不损失图片效果，达到与系统相机一致的拍照质量。

## 示例代码

* [实现相机分段式拍照功能](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/SegmentedPhotograph)
