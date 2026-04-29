---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display
title: 显示图片 (Image)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 媒体展示 > 显示图片 (Image)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ded3229ec391b1fd6ebe3113c05a4f771ad073da9bc658930d3d7f75261ea2b
---

开发者经常需要在应用中显示一些图片，例如：按钮中的icon、网络图片、本地图片等。在应用中显示图片需要使用Image组件实现，Image支持多种图片格式，包括png、jpg、jpeg等格式，不支持apng和svga格式，具体支持格式和用法请参考[Image](../harmonyos-references/ts-basic-components-image.md)组件。

Image通过调用接口来创建，接口调用形式如下：

```
1. Image(src: PixelMap | ResourceStr | DrawableDescriptor)
```

该接口通过图片数据源获取图片，支持本地图片和网络图片的渲染展示。其中，src是图片的数据源，加载方式请参考[加载图片资源](arkts-graphics-display.md#加载图片资源)。

如果图片加载过程中出现白色块，请参考[Image白块解决方案](../best-practices/bpta-image-white-lump-solution.md)。如果图片加载时间过长，请参考[预置图片资源加载优化](../best-practices/bpta-texture-compression-improve-performance.md)。

## 加载图片资源

Image支持加载存档图、多媒体像素图和可绘制描述符三种类型。

### 存档图类型数据源

存档图类型的数据源可以分为本地资源、网络资源、Resource资源、媒体库资源和base64。

* 本地资源

  创建文件夹，将本地图片放入ets文件夹下的任意位置。

  Image组件引入本地图片路径，即可显示图片（根目录为ets文件夹）。不支持跨包、跨模块调用该Image组件。

  说明

  从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使相关模块：build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](ide-hvigor-build-profile.md#table1476161719356)相关介绍。

  ```
  1. // 'images/view.jpg'需要替换为开发者所需的资源文件
  2. Image('images/view.jpg')
  3. .width(200)
  ```

  [LoadingResources.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/LoadingResources.ets#L22-L26)

  加载本地图片过程中，如果对图片进行修改或者替换，可能会引起应用崩溃。因此需要覆盖图片文件时，应该先删除该文件再重新创建一个同名文件。
* 网络资源

  引入网络图片需申请权限ohos.permission.INTERNET，具体申请方式请参考[声明权限](declare-permissions.md)。此时，Image组件的src参数为网络图片的链接。

  当前Image组件仅支持加载简单网络图片。

  首次加载网络图片时，Image组件需要请求网络资源；非首次加载时，默认从缓存中直接读取图片。

  更多图片缓存设置请参考[setImageCacheCount](../harmonyos-references/js-apis-system-app.md#setimagecachecount7)、[setImageRawDataCacheSize](../harmonyos-references/js-apis-system-app.md#setimagerawdatacachesize7)和[setImageFileCacheSize](../harmonyos-references/js-apis-system-app.md#setimagefilecachesize7)。这三个图片缓存接口主要用于支持简单、通用的场景，后续不再继续演进，且在灵活和扩展性方面存在一定限制，例如：

  + 无法获取当前缓存占用信息。Image组件目前不支持查询磁盘缓存的实时状态，包括文件总大小和文件数量。
  + 缓存策略不可定制，缺乏缓存状态观测能力。开发者无法通过接口感知缓存命中率、淘汰次数等运行时的指标，难以基于实际缓存效果进行动态调优。

  对于复杂情况，推荐使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)，该图像库提供了更灵活、可扩展的缓存策略以及完善的生命周期管理能力，更适合复杂业务需求。

  网络图片必须支持RFC 9113标准，否则会导致加载失败。如果下载的网络图片大于10MB或一次下载的网络图片数量较多，建议使用[HTTP](http-request.md)工具提前下载，提高图片加载性能，方便应用侧管理数据。

  在显示网络图片时，Image组件在机制上会依赖[缓存下载模块](../harmonyos-references/js-apis-request-cachedownload.md)，开发者可参考[示例3（下载与显示网络gif图片）](../harmonyos-references/ts-basic-components-image.md#示例3下载与显示网络gif图片)了解具体用法。

  缓存下载模块提供独立的预下载接口，允许应用开发者在创建Image组件前预下载所需图片。组件创建后，Image组件可直接从缓存下载模块中获取已下载的图片数据，从而加快图片的显示速度，优化加载体验，并有效避免网络图片加载延迟。网络缓存的位置位于应用根目录下的cache目录中。

  ```
  1. // $r('app.string.LoadingResources')需要替换为开发者所需的资源文件，资源文件中的value值请替换为真实路径
  2. Image($r('app.string.LoadingResources'))
  ```

  [LoadingResources.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/LoadingResources.ets#L28-L31)
* Resource资源

  使用资源格式可以跨包/跨模块引入图片，resources文件夹下的图片都可以通过$r资源接口读取到并转换到Resource格式。

  **图1** resources

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/qH43FZsdTWiD6DCGRoVTcA/zh-cn_image_0000002589244155.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=CA77BD64D9F36BA856F82B410C9A90CE7407C5E89B13E59DFF09E9D1D2DA5F2B)

  调用方式：

  ```
  1. // 请将$r('app.media.icon')替换为实际资源文件
  2. Image($r('app.media.icon'))
  ```

  [LoadingResources.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/LoadingResources.ets#L33-L36)

  还可以将图片放在rawfile文件夹下。

  **图2** rawfile

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Q0ydIK1SRG6Q1mcrHnH7ZA/zh-cn_image_0000002558764348.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=FF0103FC2B498AAD2FB110B337B38AB05C2258A7AA33B2FCA7AC0915F9FDAD33)

  调用方式：

  ```
  1. // $rawfile('example1.png')需要替换为开发者所需的资源文件
  2. Image($rawfile('example1.png'))
  ```

  [LoadingResources.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/LoadingResources.ets#L38-L41)
* 媒体库file://data/storage

  支持file://路径前缀的字符串，用于访问通过[选择器](../harmonyos-references/js-apis-file-picker.md)提供的图片路径。

  1. 调用接口获取图库的照片url。

     ```
     1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
     2. import { BusinessError } from '@kit.BasicServicesKit';
     3. import { hilog } from '@kit.PerformanceAnalysisKit';
     4. const DOMAIN = 0x0001;
     5. const TAG = 'Sample_imagecomponent';

     7. @Entry
     8. @Component
     9. struct MediaLibraryFile {
     10. @State imgDatas: string[] = [];
     11. // 使用PhotoViewPicker唤起图片选择器，选择图片并且渲染到页面中
     12. // 获取照片url集
     13. getAllImg() {
     14. try {
     15. let photoSelectOptions:photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
     16. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
     17. photoSelectOptions.maxSelectNumber = 5;
     18. let photoPicker:photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
     19. photoPicker.select(photoSelectOptions).then((photoSelectResult:photoAccessHelper.PhotoSelectResult) => {
     20. this.imgDatas = photoSelectResult.photoUris;
     21. hilog.info(DOMAIN, TAG,'PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
     22. }).catch((err:Error) => {
     23. let message = (err as BusinessError).message;
     24. let code = (err as BusinessError).code;
     25. hilog.info(DOMAIN, TAG,`PhotoViewPicker.select failed with. Code: ${code}, message: ${message}`);
     26. });
     27. } catch (err) {
     28. let message = (err as BusinessError).message;
     29. let code = (err as BusinessError).code;
     30. hilog.info(DOMAIN, TAG,`PhotoViewPicker failed with. Code: ${code}, message: ${message}`);
     31. };
     32. };

     34. // aboutToAppear中调用上述函数，获取图库的所有图片url，存在imgDatas中
     35. async aboutToAppear() {
     36. this.getAllImg();
     37. };
     38. // 使用imgDatas的url加载图片
     39. build() {
     40. Column() {
     41. Grid() {
     42. ForEach(this.imgDatas, (item:string) => {
     43. GridItem() {
     44. Image(item)
     45. .width(200)
     46. }
     47. }, (item:string):string => JSON.stringify(item))
     48. }
     49. }.width('100%').height('100%')
     50. }
     51. }
     ```

     [LoadImageResources.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/LoadImageResources.ets#L16-L68)
  2. 从媒体库获取的url格式通常如下。

     ```
     1. // 'file://media/Photos/5'需要替换为开发者所需的资源文件，资源文件中的value值请替换为真实路径
     2. Image('file://media/Photos/5')
     3. .width(200)
     ```

     [LoadingResources.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/LoadingResources.ets#L43-L47)
* base64

  路径格式为data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data]，其中[base64 data]为Base64字符串数据。

  Base64格式字符串可用于存储图片的像素数据，在网页上使用较为广泛。

### 多媒体像素图

PixelMap是图片解码后的像素图，具体用法请参考[Image Kit简介](image-overview.md)。以下示例将加载的网络图片返回的数据解码成PixelMap格式，再显示在Image组件上。

```
1. import { http } from '@kit.NetworkKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. const DOMAIN = 0x0001;
6. const TAG = 'Sample_imagecomponent';

8. @Entry
9. @Component
10. struct HttpExample {
11. outData: http.HttpResponse | undefined = undefined;
12. code: http.ResponseCode | number | undefined = undefined;
13. @State image: PixelMap | undefined = undefined; // 创建PixelMap状态变量

15. // 使用createHttp接口将加载的网络图片返回的数据解码成PixelMap格式，再显示在Image组件上
16. aboutToAppear(): void {
17. http.createHttp().request('xxx://xxx.xxx.xxx/example.png', // 需要替换为开发者所需的资源文件，资源文件中的value值请替换为真实路径
18. (error: BusinessError, data: http.HttpResponse) => {
19. if (error) {
20. hilog.error(DOMAIN, TAG, `hello http request failed. Code: ${error.code}, message: ${error.message}`);
21. return;
22. };
23. this.outData = data;
24. // 将网络地址成功返回的数据，编码转码成pixelMap的图片格式
25. if (http.ResponseCode.OK === this.outData.responseCode) {
26. let imageData: ArrayBuffer = this.outData.result as ArrayBuffer;
27. let imageSource: image.ImageSource = image.createImageSource(imageData);
28. let options: image.DecodingOptions = {
29. 'desiredPixelFormat': image.PixelMapFormat.RGBA_8888,
30. };
31. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
32. this.image = pixelMap;
33. });
34. };
35. });
36. };

38. build() {
39. Column() {
40. // 显示图片
41. Image(this.image)
42. .height(100)
43. .width(100)
44. }
45. }
46. }
```

[MultimediaPixelArt.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/MultimediaPixelArt.ets#L17-L64)

### 可绘制描述符

DrawableDescriptor是ArkUI提供的一种高级图片抽象机制，它通过将图片资源封装为可编程对象，实现了传统Image组件难以实现的动态组合与运行时控制功能。开发者可利用它实现图片的分层叠加（如徽章图标）、动态属性调整（如颜色滤镜）、复杂动画序列等高级效果，适用于需要灵活控制图片展现或实现复杂视觉交互的场景。详细使用方法，请参考[DrawableDescriptor](../harmonyos-references/js-apis-arkui-drawabledescriptor.md)。

通过DrawableDescriptor显示图片及动画的示例如下所示：

```
1. import {
2. DrawableDescriptor,
3. PixelMapDrawableDescriptor,
4. LayeredDrawableDescriptor,
5. AnimatedDrawableDescriptor,
6. AnimationOptions
7. } from '@kit.ArkUI';
8. import { image } from '@kit.ImageKit';

10. @Entry
11. @Component
12. struct DrawableDescriptorType {
13. // 声明DrawableDescriptor对象
14. @State pixmapDesc: DrawableDescriptor | null = null;
15. @State pixelMapDesc: PixelMapDrawableDescriptor | null = null;
16. @State layeredDesc: LayeredDrawableDescriptor | null = null;
17. @State animatedDesc: AnimatedDrawableDescriptor | null = null;
18. // 动画配置
19. private animationOptions: AnimationOptions = {
20. duration: 3000,
21. iterations: -1
22. };

24. // 开发者可利用DrawableDescriptor实现图片的分层叠加（如徽章图标），动态属性调整（如颜色滤镜），复杂动画序列等高级效果
25. async aboutToAppear() {
26. const resManager = this.getUIContext().getHostContext()?.resourceManager;
27. if (!resManager) {
28. return;
29. };
30. // 创建普通DrawableDescriptor
31. // 请将$r('app.media.landscape')替换为实际资源文件
32. let pixmapDescResult = resManager.getDrawableDescriptor($r('app.media.landscape').id);
33. if (pixmapDescResult) {
34. this.pixmapDesc = pixmapDescResult as DrawableDescriptor;
35. };
36. // 创建PixelMapDrawableDescriptor
37. // 请将$r('app.media.landscape')替换为实际资源文件
38. const pixelMap = await this.getPixmapFromMedia($r('app.media.landscape'));
39. this.pixelMapDesc = new PixelMapDrawableDescriptor(pixelMap);
40. // 创建分层图标
41. // 请将$r('app.media.foreground')替换为实际资源文件
42. const foreground = await this.getDrawableDescriptor($r('app.media.foreground'));
43. // 请将$r('app.media.landscape')替换为实际资源文件
44. const background = await this.getDrawableDescriptor($r('app.media.landscape'));
45. this.layeredDesc = new LayeredDrawableDescriptor(foreground, background);
46. // 创建动画图片（需加载多张图片）
47. // 请将$r('app.media.sky')替换为实际资源文件
48. const frame1 = await this.getPixmapFromMedia($r('app.media.sky'));
49. // 请将$r('app.media.landscape')替换为实际资源文件
50. const frame2 = await this.getPixmapFromMedia($r('app.media.landscape'));
51. // 请将$r('app.media.clouds')替换为实际资源文件
52. const frame3 = await this.getPixmapFromMedia($r('app.media.clouds'));
53. if (frame1 && frame2 && frame3) {
54. this.animatedDesc = new AnimatedDrawableDescriptor([frame1, frame2, frame3], this.animationOptions);
55. };
56. };

58. // 辅助方法：从资源获取PixelMap
59. private async getPixmapFromMedia(resource: Resource): Promise<image.PixelMap | undefined> {
60. const unit8Array = await this.getUIContext().getHostContext()?.resourceManager.getMediaContent(resource.id);
61. if (!unit8Array) {
62. return undefined;
63. };
64. const imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength));
65. const pixelMap = await imageSource.createPixelMap({
66. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
67. });
68. await imageSource.release();
69. return pixelMap;
70. };

72. // 辅助方法：获取DrawableDescriptor
73. private async getDrawableDescriptor(resource: Resource): Promise<DrawableDescriptor | undefined> {
74. const resManager = this.getUIContext().getHostContext()?.resourceManager;
75. if (!resManager) {
76. return undefined;
77. };
78. return (resManager.getDrawableDescriptor(resource.id)) as DrawableDescriptor;
79. };

81. build() {
82. RelativeContainer() {
83. Column() {
84. // 显示普通图片
85. Image(this.pixmapDesc)
86. .width(100)
87. .height(100)
88. .border({ width: 1, color: Color.Black })
89. // 显示PixelMap图片
90. Image(this.pixelMapDesc)
91. .width(100)
92. .height(100)
93. .border({ width: 1, color: Color.Red })
94. // 显示分层图标
95. if (this.layeredDesc) {
96. Image(this.layeredDesc)
97. .width(100)
98. .height(100)
99. .border({ width: 1, color: Color.Blue })
100. }
101. // 显示动画图片
102. if (this.animatedDesc) {
103. Image(this.animatedDesc)
104. .width(200)
105. .height(200)
106. .margin({ top: 20 })
107. }
108. }
109. }
110. .height('100%')
111. .width('100%')
112. .margin(50)
113. }
114. }
```

[DrawableDescriptor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/DrawableDescriptor.ets#L17-L132)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/sWFG98ixRNyfHIGBqaR4yA/zh-cn_image_0000002558604692.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=42E619C359EB22A4D8068B79F725F005DCDEADB3C85BE748EF4A25B9CCF9325E)

## 显示矢量图

Image组件可显示矢量图（SVG格式的图片），SVG标签文档请参考[SVG标签说明](../harmonyos-references/ts-basic-svg.md)。

如果SVG图片没有原始大小，需要给Image组件设置宽高，否则不显示。SVG图片不支持通过image标签引用SVG格式和gif格式的本地其他图片。

SVG格式的图片可以使用fillColor属性改变图片的绘制颜色。

```
1. // 请将$r('app.media.cloud')替换为实际资源文件
2. Image($r('app.media.cloud'))
3. .width(50)
4. .fillColor(Color.Blue)
```

[DisplayVectorDiagram.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/DisplayVectorDiagram.ets#L23-L28)

**图3** 原始图片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/JkVF9JeTS2WSHYKa07e1-g/zh-cn_image_0000002589324217.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=F32EDBEEDD0CDDE5DCCE2836DBE1AF1AA910EDDAEBD604DB8CA45D7D874E77D8)

**图4** 设置绘制颜色后的SVG图片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/zbjtU9yOTK2x-hEfuyznDw/zh-cn_image_0000002589244157.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=498A3ABAE20CFE06A0924421D9B80AEFF61AF67327D295896AF14A2F41A19FD0)

### 矢量图引用位图

如果Image加载的SVG图源中包含对本地位图的引用，则SVG图源的路径应当设置为以ets为根目录的工程路径，同时，本地位图的路径应设置为与SVG图源同级的相对路径。

Image加载的SVG图源路径设置方法如下所示：

```
1. // 'images/icon.svg'需要替换为开发者所需的资源文件
2. Image('/images/icon.svg')
3. .width(50)
4. .height(50)
```

[DisplayVectorDiagram.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/DisplayVectorDiagram.ets#L30-L35)

SVG图源通过<image>标签的xlink:href属性指定本地位图路径，本地位图路径设置为跟SVG图源同级的相对路径：

```
1. <svg width="200" height="200">
2. <image width="200" height="200" xlink:href="sky.png"></image>
3. </svg>
```

文件工程路径示例如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ZH4Gla4ZSImsV5iRU5Ep6A/zh-cn_image_0000002558764350.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=58C064B86BA2EDB7152717F41C6EBC9CD4262C782540328755322ED14FC19396)

## 添加属性

给Image组件设置属性可以使图片显示更灵活，达到一些自定义的效果。以下是几个常用属性的使用示例，完整属性信息详见[Image](../harmonyos-references/ts-basic-components-image.md)。

### 设置图片缩放类型

通过设置[objectFit](../harmonyos-references/ts-basic-components-imagespan.md#objectfit)属性，可以使图片在高度和宽度确定的框内进行缩放。

```
1. @Entry
2. @Component
3. struct ImageScalingType {
4. scroller: Scroller = new Scroller();

6. build() {
7. Scroll(this.scroller) {
8. Row() {
9. Column() {
10. // 请将$r('app.media.img_2')替换为实际资源文件
11. Image($r('app.media.img_2'))
12. .width(200)
13. .height(150)
14. .border({ width: 1 })
15. // 通过设置objectFit属性，可以使图片在高度和宽度确定的框内进行缩放
16. // 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内
17. .objectFit(ImageFit.Contain)
18. .margin({bottom:25,left:10})
19. // overlay接口暂不支持深色模式
20. .overlay('Contain', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
21. // 请将$r('app.media.img_2')替换为实际资源文件
22. Image($r('app.media.img_2'))
23. .width(200)
24. .height(150)
25. .border({ width: 1 })
26. // 通过设置objectFit属性，可以使图片在高度和宽度确定的框内进行缩放
27. // 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界
28. .objectFit(ImageFit.Cover)
29. .margin({bottom:25,left:10})
30. // overlay接口暂不支持深色模式
31. .overlay('Cover', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
32. // 请将$r('app.media.img_2')替换为实际资源文件
33. Image($r('app.media.img_2'))
34. .width(200)
35. .height(150)
36. .border({ width: 1 })
37. // 通过设置objectFit属性，可以使图片在高度和宽度确定的框内进行缩放
38. // 自适应显示
39. .objectFit(ImageFit.Auto)
40. .margin({bottom:25,left:10})
41. // overlay接口暂不支持深色模式
42. .overlay('Auto', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
43. }

45. Column() {
46. // 请将$r('app.media.img_2')替换为实际资源文件
47. Image($r('app.media.img_2'))
48. .width(200)
49. .height(150)
50. .border({ width: 1 })
51. // 通过设置objectFit属性，可以使图片在高度和宽度确定的框内进行缩放
52. // 不保持宽高比进行放大缩小，使得图片充满显示边界
53. .objectFit(ImageFit.Fill)
54. .margin({bottom:25,left:10})
55. // overlay接口暂不支持深色模式
56. .overlay('Fill', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
57. // 请将$r('app.media.img_2')替换为实际资源文件
58. Image($r('app.media.img_2'))
59. .width(200)
60. .height(150)
61. .border({ width: 1 })
62. // 通过设置objectFit属性，可以使图片在高度和宽度确定的框内进行缩放
63. // 保持宽高比显示，图片缩小或者保持不变
64. .objectFit(ImageFit.ScaleDown)
65. .margin({bottom:25,left:10})
66. // overlay接口暂不支持深色模式
67. .overlay('ScaleDown', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
68. // 请将$r('app.media.img_2')替换为实际资源文件
69. Image($r('app.media.img_2'))
70. .width(200)
71. .height(150)
72. .border({ width: 1 })
73. // 通过设置objectFit属性，可以使图片在高度和宽度确定的框内进行缩放
74. // 保持原有尺寸显示
75. .objectFit(ImageFit.None)
76. .margin({bottom:25,left:10})
77. // overlay接口暂不支持深色模式
78. .overlay('None', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
79. }
80. }
81. }
82. }
83. }
```

[SetImageZoomType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/SetImageZoomType.ets#L17-L101)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/RkQCoj0gTu-jwq0HRSP7jA/zh-cn_image_0000002558604694.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=36CD5D075B109E52A9E592EFBF4AF920FB3282C14908FFB0D27EA59CA242EC97)

### 图片插值

当原图分辨率较低并放大显示时，图片会变得模糊并出现锯齿。这时可以使用[interpolation](../harmonyos-references/ts-basic-components-image.md#interpolation)属性对图片进行插值，以提高显示清晰度。

```
1. @Entry
2. @Component
3. struct ImageInterpolationType {
4. build() {
5. Column() {
6. Row() {
7. // 请将$r('app.media.grass')替换为实际资源文件
8. Image($r('app.media.grass'))
9. .width('40%')
10. // 使用interpolation接口对图片进行插值，显著提升清晰度
11. .interpolation(ImageInterpolation.None)
12. .borderWidth(1)
13. // overlay接口暂不支持深色模式
14. .overlay('Interpolation.None', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
15. .margin(10)
16. // 请将$r('app.media.grass')替换为实际资源文件
17. Image($r('app.media.grass'))
18. .width('40%')
19. // 使用interpolation接口对图片进行插值，显著提升清晰度
20. .interpolation(ImageInterpolation.Low)
21. .borderWidth(1)
22. // overlay接口暂不支持深色模式
23. .overlay('Interpolation.Low', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
24. .margin(10)
25. }.width('100%')
26. .justifyContent(FlexAlign.Center)

28. Row() {
29. // 请将$r('app.media.grass')替换为实际资源文件
30. Image($r('app.media.grass'))
31. .width('40%')
32. // 使用interpolation接口对图片进行插值，显著提升清晰度
33. .interpolation(ImageInterpolation.Medium)
34. .borderWidth(1)
35. // overlay接口暂不支持深色模式
36. .overlay('Interpolation.Medium', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
37. .margin(10)
38. // 请将$r('app.media.grass')替换为实际资源文件
39. Image($r('app.media.grass'))
40. .width('40%')
41. // 使用interpolation接口对图片进行插值，显著提升清晰度
42. .interpolation(ImageInterpolation.High)
43. .borderWidth(1)
44. // overlay接口暂不支持深色模式
45. .overlay('Interpolation.High', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
46. .margin(10)
47. }.width('100%')
48. .justifyContent(FlexAlign.Center)
49. }
50. .height('100%')
51. }
52. }
```

[ImageInterpolation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/ImageInterpolation.ets#L16-L69)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/uZ74hPdHTemH3xUzUzjHug/zh-cn_image_0000002589324219.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=FB58A2E49109AC699E9759BA5B35629BB7A0484A9CB7571CDB3C7D939795E9E2)

### 设置图片重复样式

通过objectRepeat属性设置图片的重复样式方式，重复样式请参考[ImageRepeat](../harmonyos-references/ts-appendix-enums.md#imagerepeat)枚举说明。

```
1. @Entry
2. @Component
3. struct ImageRepetitionStyle {
4. build() {
5. Column({ space: 10 }) {
6. Column({ space: 25 }) {
7. // 请将$r('app.media.ic_public_favor_filled_1')替换为实际资源文件
8. Image($r('app.media.ic_public_favor_filled_1'))
9. .width(160)
10. .height(160)
11. .border({ width: 1 })
12. // 通过objectRepeat属性设置图片的重复样式方式
13. // 在水平轴和竖直轴上同时重复绘制图片
14. .objectRepeat(ImageRepeat.XY)
15. .objectFit(ImageFit.ScaleDown)
16. // overlay接口暂不支持深色模式
17. .overlay('ImageRepeat.XY', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
18. // 请将$r('app.media.ic_public_favor_filled_1')替换为实际资源文件
19. Image($r('app.media.ic_public_favor_filled_1'))
20. .width(160)
21. .height(160)
22. .border({ width: 1 })
23. // 通过objectRepeat属性设置图片的重复样式方式
24. // 只在竖直轴上重复绘制图片
25. .objectRepeat(ImageRepeat.Y)
26. .objectFit(ImageFit.ScaleDown)
27. // overlay接口暂不支持深色模式
28. .overlay('ImageRepeat.Y', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
29. // 请将$r('app.media.ic_public_favor_filled_1')替换为实际资源文件
30. Image($r('app.media.ic_public_favor_filled_1'))
31. .width(160)
32. .height(160)
33. .border({ width: 1 })
34. // 通过objectRepeat属性设置图片的重复样式方式
35. // 只在水平轴上重复绘制图片
36. .objectRepeat(ImageRepeat.X)
37. .objectFit(ImageFit.ScaleDown)
38. // overlay接口暂不支持深色模式
39. .overlay('ImageRepeat.X', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
40. }
41. }.height(150).width('100%').padding(8)
42. }
43. }
```

[SetImageRepetitionStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/SetImageRepetitionStyle.ets#L17-L61)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/_kb_K9IoRFK7h2eA8aADcQ/zh-cn_image_0000002589244159.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=CD3043E10A2D1C42EA9BA0AC36C199CB526A9FEF39B02F7343743023FDFAE4BB)

### 设置图片渲染模式

通过renderMode属性设置图片的渲染模式为原色或黑白。

```
1. @Entry
2. @Component
3. struct SetImageRenderingMode {
4. build() {
5. Column({ space: 10 }) {
6. Row({ space: 50 }) {
7. // 请将$r('app.media.example')替换为实际资源文件
8. Image($r('app.media.example'))
9. // 通过renderMode属性设置图片的渲染模式为原色或黑白
10. .renderMode(ImageRenderMode.Original)
11. .width(100)
12. .height(100)
13. .border({ width: 1 })
14. // overlay接口暂不支持深色模式
15. .overlay('Original', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
16. // 请将$r('app.media.example')替换为实际资源文件
17. Image($r('app.media.example'))
18. // 通过renderMode属性设置图片的渲染模式为原色或黑白
19. .renderMode(ImageRenderMode.Template)
20. .width(100)
21. .height(100)
22. .border({ width: 1 })
23. // overlay接口暂不支持深色模式
24. .overlay('Template', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
25. }
26. }.height(150).width('100%').padding({ top: 20,right: 10 })
27. }
28. }
```

[SetImageRenderingMode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/SetImageRenderingMode.ets#L17-L46)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/taTYdXDyQX6Iu0BE1SyOgw/zh-cn_image_0000002558764352.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=7AE34479AA56F3629C0C4458CC2543CFEAF2D276324FE68021A169688BDC8A88)

### 设置图片解码尺寸

通过sourceSize属性设置图片解码尺寸，降低图片的分辨率。

原图尺寸为1280×960，该示例将图片解码为40×40和90×90两个尺寸。

```
1. @Entry
2. @Component
3. struct SetImageDecodingSize {
4. build() {
5. Column() {
6. Row({ space: 50 }) {
7. // 请将$r('app.media.example')替换为实际资源文件
8. Image($r('app.media.example'))
9. // 使用sourceSize接口对图片设置解码尺寸，降低图片分辨率
10. .sourceSize({
11. width: 40,
12. height: 40
13. })
14. .objectFit(ImageFit.ScaleDown)
15. .aspectRatio(1)
16. .width('25%')
17. .border({ width: 1 })
18. // overlay接口暂不支持深色模式
19. .overlay('width:40 height:40', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
20. // 请将$r('app.media.example')替换为实际资源文件
21. Image($r('app.media.example'))
22. // 使用sourceSize接口对图片设置解码尺寸，降低图片分辨率
23. .sourceSize({
24. width: 90,
25. height: 90
26. })
27. .objectFit(ImageFit.ScaleDown)
28. .width(100)
29. .height(100)
30. .aspectRatio(1)
31. .border({ width: 1 })
32. // overlay接口暂不支持深色模式
33. .overlay('width:90 height:90', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
34. }.height(150).width('100%').padding(20)
35. }
36. }
37. }
```

[SetImageDecodingSize.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/SetImageDecodingSize.ets#L17-L55)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/okwnK0NES-SAGjozcilHvQ/zh-cn_image_0000002558604696.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=B70D46C8E59B81A5264C68CD9AA140E8FD9C27829A5D71F4546540401034C617)

### 为图片添加滤镜效果

通过colorFilter调整图片的像素颜色，为图片添加滤镜。

```
1. @Entry
2. @Component
3. struct AddFilterEffectsToImages {
4. build() {
5. Column() {
6. Row() {
7. // 请将$r('app.media.example')替换为实际资源文件
8. Image($r('app.media.example'))
9. .width('40%')
10. .margin(10)
11. // 请将$r('app.media.example')替换为实际资源文件
12. Image($r('app.media.example'))
13. .width('40%')
14. // 通过colorFilter调整图片的像素颜色，为图片添加滤镜
15. .colorFilter(
16. [1, 1, 0, 0, 0,
17. 0, 1, 0, 0, 0,
18. 0, 0, 1, 0, 0,
19. 0, 0, 0, 1, 0])
20. .margin(10)
21. }.width('100%')
22. .justifyContent(FlexAlign.Center)
23. }
24. }
25. }
```

[AddFilterEffectsToImages.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/AddFilterEffectsToImages.ets#L17-L43)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/l4CU3AYfRIOxuyEMTAvI1A/zh-cn_image_0000002589324221.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=BC8F9C56E2EF3A06BF0689ACCEBFECF43F21D06D29BD11F4E5586C926B53E005)

### 同步加载图片

一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。但是特定情况下，图片刷新时会出现闪烁，这时可以使用syncLoad属性，使图片同步加载，从而避免出现闪烁。不建议图片加载较长时间时使用，会导致页面无法响应。

```
1. // 请将$r('app.media.icon')替换为实际资源文件
2. Image($r('app.media.icon'))
3. .syncLoad(true)
```

[DisplayVectorDiagram.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/DisplayVectorDiagram.ets#L38-L42)

## 事件调用

通过在Image组件上绑定onComplete事件，图片加载成功后可以获取图片的必要信息。如果图片加载失败，也可以通过绑定onError回调来获得结果。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'Sample_imagecomponent';

5. @Entry
6. @Component
7. struct EventCall {
8. @State widthValue: number = 0;
9. @State heightValue: number = 0;
10. @State componentWidth: number = 0;
11. @State componentHeight: number = 0;

13. build() {
14. Column() {
15. Row() {
16. // 请将$r('app.media.ic_img_2')替换为实际资源文件
17. Image($r('app.media.ic_img_2'))
18. .width(200)
19. .height(150)
20. .margin(15)
21. // 图片加载成功后，通过onComplete获取图片必要信息
22. .onComplete(msg => {
23. if(msg){
24. this.widthValue = msg.width;
25. this.heightValue = msg.height;
26. this.componentWidth = msg.componentWidth;
27. this.componentHeight = msg.componentHeight;
28. };
29. hilog.info(DOMAIN, TAG, `${msg}`);
30. })
31. // 如果加载失败，使用onError触发回调函数获取结果
32. .onError(() => {
33. hilog.info(DOMAIN, TAG, 'load image fail');
34. })
35. // overlay接口暂不支持深色模式
36. .overlay('\nwidth: ' + String(this.widthValue) + ', height: ' + String(this.heightValue) + '\ncomponentWidth: ' + String(this.componentWidth) + '\ncomponentHeight: ' + String(this.componentHeight), {
37. align: Alignment.Bottom,
38. offset: { x: 0, y: 60 }
39. })
40. }
41. }
42. }
43. }
```

[EventCall.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ImageComponent/entry/src/main/ets/pages/EventCall.ets#L17-L61)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/wyx4AtjNRouDJNN2HeLvcg/zh-cn_image_0000002589244161.png?HW-CC-KV=V1&HW-CC-Date=20260429T052746Z&HW-CC-Expire=86400&HW-CC-Sign=0770E5D8F65347D1FEED01DAA2A09F53163D2927665068B1440025D6D0B16559)
