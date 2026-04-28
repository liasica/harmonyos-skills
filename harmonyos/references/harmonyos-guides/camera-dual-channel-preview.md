---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-dual-channel-preview
title: 双路预览(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 双路预览(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c006358b05ed81aaa266ed83da4bc12254c39151d7d2b6aac0424e6398e7402b
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

双路预览，即应用可同时使用两路预览流，一路用于在屏幕上显示，一路用于图像处理等其他操作，提升处理效率。

相机应用通过控制相机，实现图像显示（预览）、照片保存（拍照）、视频录制（录像）等基础操作。相机开发模型为Surface模型，即应用通过Surface进行数据传递，通过[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)的Surface获取拍照流的数据、通过XComponent的Surface获取预览流的数据。

如果要实现双路预览，可以先参考[拍照](camera-shooting.md)，在双路预览中将拍照流改为另一路预览流，通过[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)的Surface创建另一个previewOutput，其余流程与拍照一致。

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

## 约束与限制

* 暂不支持动态添加流，即不能在没有调用[session.stop](../harmonyos-references/arkts-apis-camera-session.md#stop11)的情况下，调用[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)添加流。
* 对ImageReceiver组件获取到的图像数据处理后，需要将对应的图像Buffer释放，确保Surface的BufferQueue正常轮转。

## 调用流程

双路方案调用流程图建议如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/YnIh-wVASpiADwDL9XT18g/zh-cn_image_0000002583438611.png?HW-CC-KV=V1&HW-CC-Date=20260427T234555Z&HW-CC-Expire=86400&HW-CC-Sign=67A1A002DB7FF81886AD45D8469C1C631B27493496D22DA0CCF24FA7882AAA26)

## 开发步骤

* 用于处理图像的第一路预览流：创建ImageReceiver对象，获取SurfaceId创建第一路预览流，注册图像监听，按需处理预览流每帧图像。
* 用于显示画面的第二路预览流：创建XComponent组件，获取SurfaceId创建第二路预览流，预览流画面直接在组件内渲染。
* 创建预览流获取数据：创建上述两路预览流，配置进相机会话，启动会话后，两路预览流同时获取数据。

以下各步骤示例为片段代码，可通过点击示例代码右下方的链接获取完整工程示例。

### 用于处理图像的第一路预览流

1. 导入依赖，本篇文档需要用到图片和相机框架等相关依赖包。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { camera } from '@kit.CameraKit';
   3. import { display } from '@kit.ArkUI';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```

   [ImageReceiverManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/DualPreview/camera/src/main/ets/cameramanagers/ImageReceiverManager.ets#L17-L22)
2. 获取第一路预览流SurfaceId：创建ImageReceiver对象，通过ImageReceiver对象可获取其SurfaceId。

   ```
   1. async init(size: Size, format = image.ImageFormat.JPEG, capacity = 8) {
   2. const receiver = image.createImageReceiver(size, format, capacity);
   3. const surfaceId = await receiver.getReceivingSurfaceId();
   4. this.onImageArrival(receiver);
   5. return surfaceId;
   6. }
   ```

   [ImageReceiverManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/DualPreview/camera/src/main/ets/cameramanagers/ImageReceiverManager.ets#L65-L72)
3. ImageReceiver接收预览流图像数据获取图像格式请参考[Image](../harmonyos-references/arkts-apis-image-image.md)中的format参数，[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)格式请参考[PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)。

   ```
   1. // Image格式与PixelMap格式映射关系。
   2. let formatToPixelMapFormatMap = new Map<number, image.PixelMapFormat>([
   3. [12, image.PixelMapFormat.RGBA_8888],
   4. [25, image.PixelMapFormat.NV21],
   5. [35, image.PixelMapFormat.YCBCR_P010],
   6. [36, image.PixelMapFormat.YCRCB_P010]
   7. ]);
   8. // PixelMapFormat格式的单个像素点大小映射关系。
   9. let pixelMapFormatToSizeMap = new Map<image.PixelMapFormat, number>([
   10. [image.PixelMapFormat.RGBA_8888, 4],
   11. [image.PixelMapFormat.NV21, 1.5],
   12. [image.PixelMapFormat.YCBCR_P010, 3],
   13. [image.PixelMapFormat.YCRCB_P010, 3]
   14. ]);
   ```
4. 注册监听处理预览流每帧图像数据：通过ImageReceiver组件中imageArrival事件监听获取底层返回的图像数据，详细的API说明请参考[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)。

   说明

   * 在通过[createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)接口创建[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)实例时，设置的Size、srcPixelFormat等属性必须和相机预览输出流previewProfile中配置的Size、Format属性保持一致，ImageReceiver图片像素格式请参考[PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)，相机预览输出流previewProfile输出格式请参考[CameraFormat](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)。
   * 由于不同设备产品差异性，应用开发者在创建相机预览输出流前，必须先通过[getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)方法获取当前设备支持的预览输出流previewProfile，再根据实际业务需求选择[CameraFormat](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)和[Size](../harmonyos-references/arkts-apis-camera-i.md#size)适合的预览输出流previewProfile。
   * ImageReceiver接收预览流图像数据实际format格式由应用开发者在创建预览输出流相机预览输出流时，根据实际业务需求选择的previewProfile中format格式参数影响，详细步骤请参考[创建预览流获取数据](camera-dual-channel-preview.md#创建预览流获取数据)。

   ```
   1. onImageArrival(receiver: image.ImageReceiver): void {
   2. receiver.on('imageArrival', () => {
   3. Logger.info(TAG, 'image arrival');
   4. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
   5. if (err || nextImage === undefined) {
   6. Logger.error(TAG, 'readNextImage failed');
   7. return;
   8. }
   9. nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
   10. if (err || imgComponent === undefined) {
   11. Logger.error(TAG, 'getComponent failed');
   12. }
   13. if (imgComponent.byteBuffer) {
   14. // ...
   15. } else {
   16. Logger.error(TAG, 'byteBuffer is null');
   17. }
   18. // ...
   19. });
   20. });
   21. });
   22. }
   ```

   [ImageReceiverManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/DualPreview/camera/src/main/ets/cameramanagers/ImageReceiverManager.ets#L95-L150)

   通过 [image.Component](../harmonyos-references/arkts-apis-image-i.md#component9) 解析图片buffer数据参考：

   注意

   需要确认图像的宽width是否与行距rowStride一致，如果不一致可参考以下方式处理：

   方式一：去除imgComponent.byteBuffer中stride数据，拷贝得到新的buffer，调用不支持stride的接口处理buffer。

   ```
   1. async getPixelMap(imgComponent: image.Component, width: number, height: number, stride: number) {
   2. if (stride === width) {
   3. return await image.createPixelMap(imgComponent.byteBuffer, {
   4. size: { height: height, width: width },
   5. srcPixelFormat: image.PixelMapFormat.NV21,
   6. });
   7. }
   8. const dstBufferSize = width * height * 1.5;
   9. const dstArr = new Uint8Array(dstBufferSize);
   10. for (let j = 0; j < height * 1.5; j++) {
   11. const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
   12. dstArr.set(srcBuf, j * width);
   13. }
   14. return await image.createPixelMap(dstArr.buffer, {
   15. size: { height: height, width: width },
   16. srcPixelFormat: image.PixelMapFormat.NV21,
   17. });
   18. }
   ```

   [ImageReceiverManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/DualPreview/camera/src/main/ets/cameramanagers/ImageReceiverManager.ets#L74-L93)

   方式二：根据stride\*height创建pixelMap，然后调用pixelMap的cropSync方法裁剪掉多余的像素。

   ```
   1. // 创建pixelMap，width宽传行距stride的值。
   2. let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
   3. size:{height: height, width: stride}, srcPixelFormat: pixelMapFormat});
   4. // 裁剪多余的像素。
   5. pixelMap.cropSync({size:{width:width, height:height}, x:0, y:0});
   ```

   方式三：将原始imgComponent.byteBuffer和stride信息一起传给支持stride的接口处理。

### 用于显示画面的第二路预览流

获取第二路预览流SurfaceId：创建XComponent组件用于预览流显示，获取SurfaceId请参考XComponent组件提供的[getXComponentSurfaceId](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)方法，而XComponent的能力由UI提供，相关介绍可参考[XComponent组件参考](../harmonyos-references/ts-basic-components-xcomponent.md)。

```
1. XComponent({
2. type: XComponentType.SURFACE,
3. controller: this.previewVM.xComponentController
4. })
5. .size({ height: '100%', width: '100%' })
6. .onLoad(async () => {
7. // ...
8. this.previewVM.surfaceId = this.previewVM.xComponentController.getXComponentSurfaceId();
9. this.previewVM.setPreviewSize();
10. this.previewVM.xComponentController.setXComponentSurfaceRotation({ lock: true });
11. // ...
12. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/DualPreview/entry/src/main/ets/pages/Index.ets#L241-L267)

### 创建预览流获取数据

通过两个SurfaceId分别创建两路预览流输出，加入相机会话，启动相机会话，获取预览流数据。

```
1. async createOutput(config: CreateOutputConfig) {
2. const cameraOutputCap = config.cameraManager.getSupportedOutputCapability(config.device, config.sceneMode);
3. const displayRatio = config.profile.size.width / config.profile.size.height;
4. const profileWidth = config.profile.size.width;
5. const previewProfile = cameraOutputCap.previewProfiles
6. .sort((a, b) => Math.abs(a.size.width - profileWidth) - Math.abs(b.size.width - profileWidth))
7. .find(pf => {
8. const pfDisplayRatio = pf.size.width / pf.size.height;
9. return pf.format === config.profile.format &&
10. Math.abs(pfDisplayRatio - displayRatio) <= CameraConstant.PROFILE_DIFFERENCE;
11. });
12. if (!previewProfile) {
13. Logger.error(TAG_LOG, 'Failed to get preview profile');
14. return;
15. }
16. this.output = config.cameraManager.createPreviewOutput(previewProfile, config.surfaceId);
17. this.addOutputListener(this.output);
18. return this.output;
19. }
```

[PreviewManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/DualPreview/camera/src/main/ets/cameramanagers/PreviewManager.ets#L33-L53)

## 完整示例

```
1. import { image } from '@kit.ImageKit';
2. import { camera } from '@kit.CameraKit';
3. import { display } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { Logger } from 'commons';
6. import OutputManager, { CreateOutputConfig } from './OutputManager';
7. import CameraConstant from '../constants/CameraConstants';

9. const TAG = 'ImageReceiverManager';

11. export class ImageReceiverManager implements OutputManager {
12. public output?: camera.PreviewOutput;
13. public isActive: boolean = true;
14. public callback: (px: PixelMap) => void;
15. private position: camera.CameraPosition = camera.CameraPosition.CAMERA_POSITION_BACK;

17. constructor(cb: (px: PixelMap) => void) {
18. this.callback = cb;
19. }

21. async createOutput(config: CreateOutputConfig) {
22. const cameraOutputCap = config.cameraManager.getSupportedOutputCapability(config.device, config.sceneMode);
23. const displayRatio = config.profile.size.width / config.profile.size.height;
24. const profileWidth = config.profile.size.width;
25. const previewProfile = cameraOutputCap.previewProfiles
26. .sort((a, b) => Math.abs(a.size.width - profileWidth) - Math.abs(b.size.width - profileWidth))
27. .find(pf => {
28. const pfDisplayRatio = pf.size.width / pf.size.height;
29. return pf.format === config.profile.format &&
30. Math.abs(pfDisplayRatio - displayRatio) <= CameraConstant.PROFILE_DIFFERENCE;
31. });
32. if (!previewProfile) {
33. Logger.error(TAG, 'Failed to get preview profile');
34. return;
35. }
36. const surfaceId = await this.init(config.profile.size);
37. this.output = config.cameraManager.createPreviewOutput(previewProfile, surfaceId);
38. this.position = config.device.cameraPosition;
39. return this.output;
40. }

42. async release() {
43. await this.output?.release();
44. this.output = undefined;
45. }

47. async init(size: Size, format = image.ImageFormat.JPEG, capacity = 8) {
48. const receiver = image.createImageReceiver(size, format, capacity);
49. const surfaceId = await receiver.getReceivingSurfaceId();
50. this.onImageArrival(receiver);
51. return surfaceId;
52. }

54. async getPixelMap(imgComponent: image.Component, width: number, height: number, stride: number) {
55. if (stride === width) {
56. return await image.createPixelMap(imgComponent.byteBuffer, {
57. size: { height: height, width: width },
58. srcPixelFormat: image.PixelMapFormat.NV21,
59. });
60. }
61. const dstBufferSize = width * height * 1.5;
62. const dstArr = new Uint8Array(dstBufferSize);
63. for (let j = 0; j < height * 1.5; j++) {
64. const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
65. dstArr.set(srcBuf, j * width);
66. }
67. return await image.createPixelMap(dstArr.buffer, {
68. size: { height: height, width: width },
69. srcPixelFormat: image.PixelMapFormat.NV21,
70. });
71. }

73. onImageArrival(receiver: image.ImageReceiver): void {
74. receiver.on('imageArrival', () => {
75. Logger.info(TAG, 'image arrival');
76. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
77. if (err || nextImage === undefined) {
78. Logger.error(TAG, 'readNextImage failed');
79. return;
80. }
81. nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
82. if (err || imgComponent === undefined) {
83. Logger.error(TAG, 'getComponent failed');
84. }
85. if (imgComponent.byteBuffer) {
86. const width = nextImage.size.width;
87. const height = nextImage.size.height;
88. const stride = imgComponent.rowStride;
89. Logger.info(TAG, `getComponent with width:${width} height:${height} stride:${stride}`);
90. const pixelMap = await this.getPixelMap(imgComponent, width, height, stride);
91. const displayRotation = display.getDefaultDisplaySync().rotation * camera.ImageRotation.ROTATION_90;
92. const rotation = this.output!.getPreviewRotation(displayRotation);
93. if (this.position === camera.CameraPosition.CAMERA_POSITION_FRONT) {
94. if (displayRotation === 90 || displayRotation === 270) {
95. await pixelMap.rotate((rotation + 180) % 360);
96. } else {
97. await pixelMap.rotate(rotation);
98. }
99. await pixelMap.flip(true, false);
100. } else {
101. await pixelMap.rotate(rotation);
102. }
103. this.callback(pixelMap);
104. } else {
105. Logger.error(TAG, 'byteBuffer is null');
106. }
107. nextImage.release().then(() => {Logger.info(TAG, 'image release done');}).catch((error: BusinessError) => {
108. Logger.error(TAG, `Release failed! Code ${error.code},message is ${error.message}`);
109. });
110. Logger.info(TAG, 'image process done');
111. });
112. });
113. });
114. }
115. }
```

[ImageReceiverManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/DualPreview/camera/src/main/ets/cameramanagers/ImageReceiverManager.ets#L16-L152)
