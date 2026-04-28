---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-drawing-customization-on-canvas
title: 使用画布绘制自定义图形 (Canvas)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义绘制 > 使用画布绘制自定义图形 (Canvas)
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca366d223374f90e49e66f0ae651c6f2120bc1424fdf0258f550702327c95d76
---

Canvas提供画布组件，用于自定义绘制图形，开发者使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。

## 使用画布组件绘制自定义图形

可以由以下三种形式在画布绘制自定义图形：

* 使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象在Canvas画布上绘制。

```
1. @Entry
2. @Component
3. struct CanvasExample1 {
4. // 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. // 用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. // 在canvas中调用CanvasRenderingContext2D对象。
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#F5DC62')
16. .onReady(() => {
17. // 可以在这里绘制内容。
18. this.context.strokeRect(50, 50, 200, 150);
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

[CanvasRenderingContext2D.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasRenderingContext2D.ets#L15-L40)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/-E4fd_zoSpOHFBivBX2O9g/zh-cn_image_0000002552798368.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=AF658139C474B0D50890B8448F94C69741560333CDD1C87B231FC3825DBD4FDC)

* 离屏绘制是指将需要绘制的内容先绘制在缓存区，再将其转换成图片，一次性绘制到Canvas上，加快了绘制速度。过程为：

  1. 通过transferToImageBitmap方法将离屏画布最近渲染的图像创建为一个ImageBitmap对象。
  2. 通过CanvasRenderingContext2D对象的transferFromImageBitmap方法显示给定的ImageBitmap对象。

  具体使用参考[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象。

```
1. @Entry
2. @Component
3. struct CanvasExample2 {
4. // 用来配置CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。true表明开启抗锯齿
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // 用来创建OffscreenCanvas对象，width为离屏画布的宽度，height为离屏画布的高度。通过在canvas中调用OffscreenCanvasRenderingContext2D对象来绘制。
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#F5DC62')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext('2d', this.settings);
18. // 可以在这里绘制内容
19. offContext.strokeRect(50, 50, 200, 150);
20. // 将离屏绘制渲染的图像在普通画布上显示
21. let image = this.offCanvas.transferToImageBitmap();
22. this.context.transferFromImageBitmap(image);
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

[OffScreenDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/OffScreenDrawing.ets#L19-L48)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/x-zHqoo_TQ-7Nm_UtrSy9A/zh-cn_image_0000002552798368.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=340EA78834D1FD632C3FF762D0A46D79AAAE98D00579841A2F23CE84B14B4471)

说明

在画布组件中，通过CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制时调用的接口相同，另外，接口参数如无特别说明，单位均为vp。

* 在Canvas上加载Lottie动画时，需要先按照如下方式下载Lottie。

```
1. import lottie from '@ohos/lottie'
```

[OffScreenDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/OffScreenDrawing.ets#L15-L17)

具体接口请参考[lottie](https://gitcode.com/openharmony-tpc/lottieArkTS)。

## 初始化画布组件

onReady(event: () => void)是Canvas组件初始化完成时的事件回调，调用该事件后，可获取Canvas组件的确定宽高，进一步使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象调用相关API进行图形绘制。

```
1. Canvas(this.context)
2. .width('100%')
3. .height('100%')
4. .backgroundColor('#F5DC62')
5. .onReady(() => {
6. this.context.fillStyle = '#0097D4';
7. this.context.fillRect(50, 50, 100, 100);
8. })
```

[InitCanvasComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/InitCanvasComponent.ets#L23-L32)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/d--OumSNQRSYUhWCzhx08w/zh-cn_image_0000002583438063.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=930CB0527531220E9F481671D6205D814EEBEF491998973065407592DC19C91B)

## 画布组件绘制方式

在Canvas组件的事件回调onReady()被调用之后，开发者可以直接使用Canvas组件进行绘制。或者可以脱离Canvas组件和onReady()生命周期，单独定义Path2D对象构造理想的路径，并在onReady()调用之后使用Canvas组件进行绘制。

* 通过CanvasRenderingContext2D对象直接调用相关API进行绘制。

```
1. Canvas(this.context)
2. .width('100%')
3. .height('100%')
4. .backgroundColor('#F5DC62')
5. .onReady(() => {
6. this.context.beginPath();
7. this.context.moveTo(50, 50);
8. this.context.lineTo(280, 160);
9. this.context.stroke();
10. })
```

[CanvasComponentDrawingMethod.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasComponentDrawingMethod.ets#L27-L38)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/fPW7sYy9Sru16lTL34fyXQ/zh-cn_image_0000002552958018.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=8D80C12EFFBA33FC50FEAD2CB164CC555AC74B30086B5861B6BF795D713176B8)

* 先单独定义path2D对象构造理想的路径，再通过调用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的stroke接口或者fill接口进行绘制，具体使用可以参考[Path2D](../harmonyos-references/ts-components-canvas-path2d.md)对象。

```
1. Canvas(this.context2)
2. .width('100%')
3. .height('100%')
4. .backgroundColor('#F5DC62')
5. .onReady(() => {
6. let region = new Path2D();
7. region.arc(100, 75, 50, 0, 6.28);
8. this.context2.stroke(region);
9. })
```

[CanvasComponentDrawingMethod.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasComponentDrawingMethod.ets#L42-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Vqga4qdzTxS9o71-2FmU5g/zh-cn_image_0000002583478019.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=820E2FFC97EE645C3A3B62AD6769589CCC610CAC3A98DC2658EA04084B51805D)

## 画布组件常用方法

OffscreenCanvasRenderingContext2D对象和CanvasRenderingContext2D对象提供了大量的属性和方法，可以用来绘制文本、图形，处理像素等，是Canvas组件的核心。常用接口有[fill](../harmonyos-references/ts-canvasrenderingcontext2d.md#fill)（对封闭路径进行填充）、[clip](../harmonyos-references/ts-canvasrenderingcontext2d.md#clip)（设置当前路径为剪切路径）、[stroke](../harmonyos-references/ts-canvasrenderingcontext2d.md#stroke)（进行边框绘制操作）等等，同时提供了[fillStyle](../harmonyos-references/ts-canvasrenderingcontext2d.md#fillstyle)（指定绘制的填充色）、[globalAlpha](../harmonyos-references/ts-canvasrenderingcontext2d.md#globalalpha)（设置透明度）与[strokeStyle](../harmonyos-references/ts-canvasrenderingcontext2d.md#strokestyle)（设置描边的颜色）等属性修改绘制内容的样式。将通过以下几个方面简单介绍画布组件常见使用方法：

* 绘制基础形状。

  可以通过[arc](../harmonyos-references/ts-canvasrenderingcontext2d.md#arc)（绘制弧线路径）、 [ellipse](../harmonyos-references/ts-canvasrenderingcontext2d.md#ellipse)（绘制一个椭圆）、[rect](../harmonyos-references/ts-canvasrenderingcontext2d.md#rect)（创建矩形路径）等接口绘制基础形状。

```
1. Canvas(this.context)
2. .width('100%')
3. .height('100%')
4. .backgroundColor('#F5DC62')
5. .onReady(() => {
6. // 绘制矩形
7. this.context.beginPath();
8. this.context.rect(100, 50, 100, 100);
9. this.context.stroke();
10. // 绘制圆形
11. this.context.beginPath();
12. this.context.arc(150, 250, 50, 0, 6.28);
13. this.context.stroke();
14. // 绘制椭圆
15. this.context.beginPath();
16. this.context.ellipse(150, 450, 50, 100, Math.PI * 0.25, Math.PI * 0, Math.PI * 2);
17. this.context.stroke();
18. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/oae6C_2hSU2js0v8CS5x5w/zh-cn_image_0000002552798370.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=965EB50C6DF2518C0908831DDE478A0A546DC27BF3F618EE18AD3935B69D8E2D)

* 绘制文本。

  可以通过[fillText](../harmonyos-references/ts-canvasrenderingcontext2d.md#filltext)（文本填充）、[strokeText](../harmonyos-references/ts-canvasrenderingcontext2d.md#stroketext)（文本描边）等接口进行文本绘制，示例中设置了font为50像素高加粗的"sans-serif"字体，然后调用fillText方法在(50, 100)处绘制文本"Hello World!"，设置strokeStyle为红色，lineWidth为2，font为50像素高加粗的"sans-serif"字体，然后调用strokeText方法在(50, 150)处绘制文本"Hello World!"的轮廓。

```
1. Canvas(this.context)
2. .width('100%')
3. .height('100%')
4. .backgroundColor('#F5DC62')
5. .onReady(() => {
6. // 文本填充
7. this.context.font = '50px bolder sans-serif';
8. this.context.fillText('Hello World!', 50, 100);
9. // 文本描边
10. this.context.strokeStyle = '#ff0000';
11. this.context.lineWidth = 2;
12. this.context.font = '50px bolder sans-serif';
13. this.context.strokeText('Hello World!', 50, 150);
14. })
```

[CanvasComponentText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasComponentText.ets#L23-L38)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Klo8Ow3BQniOB0tWphLljw/zh-cn_image_0000002583438065.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=EFD53DF96383C1D76F7E00DC9EF3A81F3414DC640FFB36B07C733029F284A9C2)

* 绘制文本边框。

  可以通过[measureText](../harmonyos-references/ts-canvasrenderingcontext2d.md#measuretext)（文本测量）计算绘制文本的宽度和高度，使用测量的宽度和高度作为边框的尺寸。在示例中，设置textBaseline为'top'，font为30像素的"monospace"字体，通过measureText测量出文本的宽度和高度，然后调用fillText方法在(20, 100)处绘制文本"Hello World!"，并调用strokeRect方法在同一位置使用测量的宽度和高度绘制相应尺寸的边框。接着，设置font为60像素的粗体"sans-serif"字体，再次通过measureText测量文本的宽度和高度，接着调用fillText方法在(20, 150)处绘制文本"Hello World!"，并调用strokeRect方法在同一位置使用测量的宽度和高度绘制对应尺寸的边框。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasComponentTextBorder {
5. drawText: string = 'Hello World'
6. private settings: RenderingContextSettings = new RenderingContextSettings(true);
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#F5DC62')
15. .onReady(() => {
16. // 文本的水平对齐方式为'top'
17. this.context.textBaseline = 'top';
18. // 文本字号为30px，字体系列为monospace
19. this.context.font = '30px monospace';
20. let textWidth = this.context.measureText(this.drawText).width;
21. let textHeight = this.context.measureText(this.drawText).height;
22. this.context.fillText(this.drawText, 20, 100);
23. this.context.strokeRect(20, 100, textWidth, textHeight);
24. // 文本字体粗细为粗体，字号为60px，字体系列为sans-serif
25. this.context.font = 'bold 60px sans-serif';
26. textWidth = this.context.measureText(this.drawText).width;
27. textHeight = this.context.measureText(this.drawText).height;
28. this.context.fillText(this.drawText, 20, 150);
29. this.context.strokeRect(20, 150, textWidth, textHeight);
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

[CanvasComponentTextBorder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasComponentTextBorder.ets#L15-L51)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Kf-uklCJQ4yNGqBgT9yu7A/zh-cn_image_0000002552958020.png?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=3E41B0AE407D9779D56814F50A8AE72F95D10547E37E2977842FB1380369EE1D)

* 使用自定义字体绘制文本。

  从API version 20开始，可以通过[getGlobalInstance](../harmonyos-references/js-apis-graphics-text.md#getglobalinstance)获取应用全局字体管理器的实例，然后使用[loadFontSync](../harmonyos-references/js-apis-graphics-text.md#loadfontsync)接口从设置的路径中加载自定义字体并通过[font](../harmonyos-references/ts-canvasrenderingcontext2d.md#font)（设置文本绘制中的字体样式）接口设置文本绘制中的字体样式，接着通过[fillText](../harmonyos-references/ts-canvasrenderingcontext2d.md#filltext)（绘制填充类文本）、[strokeText](../harmonyos-references/ts-canvasrenderingcontext2d.md#stroketext)（绘制描边类文本）等接口进行文本绘制。

```
1. import { text } from '@kit.ArkGraphics2D';

3. @Entry
4. @Component
5. struct CustomFont {
6. private settings: RenderingContextSettings = new RenderingContextSettings(true);
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#F5DC62')
15. .onReady(() => {
16. // 加载自定义字体
17. let fontCollection = text.FontCollection.getGlobalInstance();
18. fontCollection.loadFontSync('customFont', $rawfile('customFont.ttf'));
19. this.context.font = '30vp customFont';
20. this.context.fillText('Hello World!', 20, 50);
21. this.context.strokeText('Hello World!', 20, 100);
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

[CanvasComponentCustomFontsDrawText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasComponentCustomFontsDrawText.ets#L15-L43)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/nD2TLQOETHOHKeXWtEtvsA/zh-cn_image_0000002583478021.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=7DAA4E6BEE51B7F4C499AB478818AA2A5A1547B5C9E7C9B9C60E6A72F9096311)

* 绘制图片和图像像素信息处理。

  可以通过[drawImage](../harmonyos-references/ts-canvasrenderingcontext2d.md#drawimage)（图像绘制）、[putImageData](../harmonyos-references/ts-canvasrenderingcontext2d.md#putimagedata)（使用[ImageData](../harmonyos-references/ts-components-canvas-imagedata.md)数据填充新的矩形区域）等接口绘制图片，通过[createImageData](../harmonyos-references/ts-canvasrenderingcontext2d.md#createimagedata)（创建新的ImageData 对象）、[getPixelMap](../harmonyos-references/ts-canvasrenderingcontext2d.md#getpixelmap)（以当前canvas指定区域内的像素创建[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)对象）、[getImageData](../harmonyos-references/ts-canvasrenderingcontext2d.md#getimagedata)（以当前canvas指定区域内的像素创建ImageData对象）等接口进行图像像素信息处理。

```
1. @Entry
2. @Component
3. struct CanvasComponentDrawingPictureAndImagePixel {
4. private settings: RenderingContextSettings = new RenderingContextSettings(true);
5. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
6. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
7. // "/common/images/image.png"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap('/common/images/image.png');

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#F5DC62')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext('2d', this.settings);
18. // 使用drawImage接口将图片画在（0，0）为起点，宽高130的区域
19. offContext.drawImage(this.img, 0, 0, 130, 130);
20. // 使用getImageData接口，获得canvas组件区域中，（50，50）为起点，宽高130范围内的绘制内容
21. let imageData = offContext.getImageData(50, 50, 130, 130);
22. // 使用putImageData接口将得到的ImageData画在起点为（150， 150）的区域中
23. offContext.putImageData(imageData, 150, 150);
24. // 将离屏绘制的内容画到canvas组件上
25. let image = this.offCanvas.transferToImageBitmap();
26. this.context.transferFromImageBitmap(image);
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

[CanvasComponentDrawingPictureAndImagePixel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasComponentDrawingPictureAndImagePixel.ets#L15-L48)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/LTII-NxhR_CbT1Fs3PbPHA/zh-cn_image_0000002552798372.png?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=925CB71FA9800DDD2B423193B1BEDA7D4B0C1F5494102DA091A4B15CC0728CEC)

* 其他方法。

  Canvas中还提供其他类型的方法。渐变（[CanvasGradient](../harmonyos-references/ts-components-canvas-canvasgradient.md)对象）相关的方法：[createLinearGradient](../harmonyos-references/ts-canvasrenderingcontext2d.md#createlineargradient)（创建一个线性渐变色）、[createRadialGradient](../harmonyos-references/ts-canvasrenderingcontext2d.md#createradialgradient)（创建一个径向渐变色）等。

```
1. Canvas(this.context)
2. .width('100%')
3. .height('100%')
4. .backgroundColor('#F5DC62')
5. .onReady(() => {
6. // 创建一个径向渐变色的CanvasGradient对象
7. let grad = this.context.createRadialGradient(200, 200, 50, 200, 200, 200);
8. // 为CanvasGradient对象设置渐变断点值，包括偏移和颜色
9. grad.addColorStop(0.0, '#E87361');
10. grad.addColorStop(0.5, '#FFFFF0');
11. grad.addColorStop(1.0, '#BDDB69');
12. // 用CanvasGradient对象填充矩形
13. this.context.fillStyle = grad;
14. this.context.fillRect(0, 0, 400, 400);
15. })
```

[CanvasComponentOtherMethods.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasComponentOtherMethods.ets#L23-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/JzbCdmKLTmWCSTUjdE0yGQ/zh-cn_image_0000002583438067.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=16F4140EBDCC8E0ACF80666CCC4F49E12675292A2F09502BB3AE9713B5015E55)

## 使用状态变量驱动画布刷新

可以使用状态变量来驱动Canvas刷新，将变化的数据通过@Watch监听，并绑定自定义的draw()方法。当数据刷新时，@Watch绑定的方法会执行绘制逻辑，使Canvas刷新。

```
1. @Entry
2. @Component
3. struct CanvasContentUpdate {
4. private settings: RenderingContextSettings = new RenderingContextSettings(true);
5. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
6. @State @Watch('draw')content: string = 'Hello World';

8. draw() {
9. this.context.clearRect(0, 0, 400, 200); // 清空Canvas的内容
10. this.context.fillText(this.content, 50, 100); // 重新绘制
11. }

13. build() {
14. Column() {
15. Canvas(this.context)
16. .width('100%')
17. .height('25%')
18. .backgroundColor('rgb(39, 135, 217)')
19. .onReady(() => {
20. this.context.font = '65px sans-serif';
21. this.context.fillText(this.content, 50, 100);
22. })
23. TextInput({
24. text:$$this.content // 修改文本输入框里的内容时，状态变量的更新会驱动Canvas刷新
25. })
26. .fontSize(35)
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

[CanvasContentUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/CanvasContentUpdate.ets#L15-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/MXv83ZaQQxCsNXZ0v3Kmjw/zh-cn_image_0000002552958022.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=2357AEB704BDC71236A7FA8CC1276C3CD6ECABF0EA1C32CDE86148608A12DBA4)

## 控制在画布组件不可见时不进行绘制

可以使用以下两种方式监听Canvas组件可见性，避免不可见时仍在无效绘制。

* 从API version 13开始，使用[setOnVisibleAreaApproximateChange](../harmonyos-references/ts-uicommonevent.md#setonvisibleareaapproximatechange)接口监听Canvas组件可见性。

  ```
  1. import { ColorMetrics } from '@kit.ArkUI';

  3. @Entry
  4. @Component
  5. struct Page {
  6. private canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D()
  7. private timerId: number = -1;

  9. drawRandomCircle(): void {
  10. let center: [number, number] = [Math.random() * 200 + 50, Math.random() * 200 + 50]
  11. let radius: number = Math.random() * 20 + 10
  12. let color: ColorMetrics =
  13. ColorMetrics.rgba(Math.floor(Math.random() * 255), Math.floor(Math.random() * 255),
  14. Math.floor(Math.random() * 255))

  16. // 清空原先内容与画布状态
  17. this.canvasContext.reset()

  19. // 开始绘制
  20. this.canvasContext.fillStyle = color.color
  21. let path: Path2D = new Path2D()
  22. path.ellipse(center[0], center[1], radius, radius, 0, 0, Math.PI * 2)
  23. this.canvasContext.fill(path)
  24. }

  26. build() {
  27. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
  28. Canvas(this.canvasContext)
  29. .width(300)
  30. .height(300)
  31. .onReady(() => {
  32. let frameNode = this.canvasContext.canvas;
  33. frameNode.commonEvent.setOnVisibleAreaApproximateChange({ ratios: [0.0] },
  34. (isVisible: boolean, currentRatio: number) => {
  35. // canvas不可见
  36. if (!isVisible && currentRatio <= 0) {
  37. clearInterval(this.timerId)
  38. this.timerId = -2
  39. }
  40. // canvas可见
  41. if (isVisible) {
  42. if (this.timerId == -2) {
  43. this.timerId = setInterval(() => {
  44. this.drawRandomCircle()
  45. }, 500)
  46. }
  47. }
  48. })
  49. })
  50. Button("draw sth")
  51. .onClick(() => {
  52. if (this.timerId < 0) {
  53. this.timerId = setInterval(() => {
  54. this.drawRandomCircle()
  55. }, 500)
  56. }
  57. })
  58. }
  59. .width('100%')
  60. .height('100%')
  61. }
  62. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/jKrq1bXJQXuUlrE3xkZC5Q/zh-cn_image_0000002583478023.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=EB17E1E5E9FDC0EE36AB01312517EC0C12D8ABD2F548AD2BE1A917062CDC1882)
* 从API version 17开始，使用[onVisibleAreaApproximateChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareaapproximatechange17)接口监听Canvas组件可见性。

  ```
  1. import { ColorMetrics } from '@kit.ArkUI';

  3. @Entry
  4. @Component
  5. struct Page {
  6. private canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D()
  7. private timerId: number = -1;

  9. drawRandomCircle(): void {
  10. let center: [number, number] = [Math.random() * 200 + 50, Math.random() * 200 + 50]
  11. let radius: number = Math.random() * 20 + 10
  12. let color: ColorMetrics =
  13. ColorMetrics.rgba(Math.floor(Math.random() * 255), Math.floor(Math.random() * 255),
  14. Math.floor(Math.random() * 255))

  16. // 清空原先内容与画布状态
  17. this.canvasContext.reset()

  19. // 开始绘制
  20. this.canvasContext.fillStyle = color.color
  21. let path: Path2D = new Path2D()
  22. path.ellipse(center[0], center[1], radius, radius, 0, 0, Math.PI * 2)
  23. this.canvasContext.fill(path)
  24. }

  26. build() {
  27. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
  28. Canvas(this.canvasContext)
  29. .width(300)
  30. .height(300)
  31. .onVisibleAreaApproximateChange({ ratios: [0.0] },
  32. (isVisible: boolean, currentRatio: number) => {
  33. // canvas不可见
  34. if (!isVisible && currentRatio <= 0) {
  35. clearInterval(this.timerId)
  36. this.timerId = -2
  37. }
  38. // canvas可见
  39. if (isVisible) {
  40. if (this.timerId == -2) {
  41. this.timerId = setInterval(() => {
  42. this.drawRandomCircle()
  43. }, 500)
  44. }
  45. }
  46. })
  47. Button("draw sth")
  48. .onClick(() => {
  49. if (this.timerId < 0) {
  50. this.timerId = setInterval(() => {
  51. this.drawRandomCircle()
  52. }, 500)
  53. }
  54. })
  55. }
  56. .width('100%')
  57. .height('100%')
  58. }
  59. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/QhgiIMlvRKGdH0wwUG5OpQ/zh-cn_image_0000002552798374.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=85DB5591203B905A841801F89980479FD3677F56F090E16A37CD8BB75B706FB8)

## 场景示例

* 绘制规则基础形状。

```
1. @Entry
2. @Component
3. struct ClearRect {
4. private settings: RenderingContextSettings = new RenderingContextSettings(true);
5. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

7. build() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
9. Canvas(this.context)
10. .width('100%')
11. .height('100%')
12. .backgroundColor('#F5DC62')
13. .onReady(() => {
14. // 设定填充样式，填充颜色设为蓝色
15. this.context.fillStyle = '#0097D4';
16. // 以(50, 50)为左上顶点，画一个宽高200的矩形
17. this.context.fillRect(50, 50, 200, 200);
18. // 以(70, 70)为左上顶点，清除宽150高100的区域
19. this.context.clearRect(70, 70, 150, 100);
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

[DrawingRegularBaseShape.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/DrawingRegularBaseShape.ets#L15-L41)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/kaxx8IB8QuWbgUDOlgWgOA/zh-cn_image_0000002583438069.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=0FA403496790ABE283D7CFC39471837AB574CD1E64C2EF19CD7EECA49A8C4B52)

* 绘制不规则图形。

```
1. @Entry
2. @Component
3. struct Path2d {
4. private settings: RenderingContextSettings = new RenderingContextSettings(true);
5. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

7. build() {
8. Row() {
9. Column() {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#F5DC62')
14. .onReady(() => {
15. // 使用Path2D的接口构造一个五边形
16. let path = new Path2D();
17. path.moveTo(150, 50);
18. path.lineTo(50, 150);
19. path.lineTo(100, 250);
20. path.lineTo(200, 250);
21. path.lineTo(250, 150);
22. path.closePath();
23. // 设定填充色为蓝色
24. this.context.fillStyle = '#0097D4';
25. // 使用填充的方式，将Path2D描述的五边形绘制在canvas组件内部
26. this.context.fill(path);
27. })
28. }
29. .width('100%')
30. }
31. .height('100%')
32. }
33. }
```

[DrawIrregularFigures.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/DrawIrregularFigures.ets#L15-L49)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/5oStQQsOSdqDKDs_VpTOPw/zh-cn_image_0000002552958024.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=D8343B41D195CA90AC8E2AF18DA411B3AEDF4B7A82D8C052494A77F8185EA532)

* 绘制可拖动的光标。

  可以通过[beginPath](../harmonyos-references/ts-canvasrenderingcontext2d.md#beginpath)、[moveTo](../harmonyos-references/ts-canvasrenderingcontext2d.md#moveto)、[lineTo](../harmonyos-references/ts-canvasrenderingcontext2d.md#lineto)和[arc](../harmonyos-references/ts-canvasrenderingcontext2d.md#arc)方法设置光标的位置，使用[stroke](../harmonyos-references/ts-canvasrenderingcontext2d.md#stroke)和[fill](../harmonyos-references/ts-canvasrenderingcontext2d.md#fill)方法绘制光标，将是否按下和位置变化通过@Watch监听，并绑定自定义的drawCursor()方法。当拖动光标时，@Watch绑定的方法会执行绘制逻辑，计算并更新光标的颜色和位置。

```
1. @Entry
2. @Component
3. struct CursorMoving {
4. // 监听是否按下，刷新光标颜色
5. @State @Watch('drawCursor') isTouchDown: boolean = false;
6. // 监听位置变化，刷新页面
7. @State @Watch('drawCursor') cursorPosition: RectPosition = {
8. x: 0,
9. y: 0,
10. width: 0,
11. height: 0,
12. };
13. private settings: RenderingContextSettings = new RenderingContextSettings(true);
14. private canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
15. private sw: number = 360; // Canvas固定宽度
16. private sh: number = 270; // Canvas固定高度
17. private cursorWH: number = 50; // 光标区域宽高
18. private dashedLineW: number = 7; // 光标宽高
19. private arcRadius: number = 6; // 光标中心圆半径
20. private isReadyMove: boolean = false;
21. private touchPosition: Position = {
22. x: 0,
23. y: 0,
24. };
25. private cursorCenterPosition: Position = {
26. x: 0,
27. y: 0,
28. };

30. build() {
31. Column() {
32. // 绘制光标
33. Canvas(this.canvasContext)
34. .width(this.sw)
35. .height(this.sh)
36. .backgroundColor('#D5D5D5')
37. .onReady(() => {
38. this.cursorPosition.x = (this.sw - this.cursorWH) / 2;
39. this.cursorPosition.y = (this.sh - this.cursorWH) / 2;
40. this.cursorPosition.width = this.cursorWH;
41. this.cursorPosition.height = this.cursorWH;
42. this.cursorCenterPosition = {
43. x: this.cursorPosition.x + this.cursorPosition.width / 2,
44. y: this.cursorPosition.y + this.cursorPosition.height / 2
45. };
46. this.drawCursor();
47. })
48. .onTouch(event => {
49. if (event.type === TouchType.Down) {
50. this.isReadyMove = this.isTouchCursorArea(event.touches[0]);
51. if (this.isReadyMove) {
52. this.isTouchDown = true;
53. }

55. this.touchPosition = {
56. x: event.touches[0].displayX,
57. y: event.touches[0].displayY
58. };
59. } else if (event.type === TouchType.Move) {
60. if (this.isReadyMove) {
61. let moveX = event.changedTouches[0].displayX - this.touchPosition.x;
62. let moveY = event.changedTouches[0].displayY - this.touchPosition.y;
63. this.touchPosition = {
64. x: event.changedTouches[0].displayX,
65. y: event.changedTouches[0].displayY
66. };
67. this.cursorPosition.x += moveX;
68. this.cursorPosition.y += moveY;

70. this.cursorCenterPosition = {
71. x: this.cursorPosition.x + this.cursorPosition.width / 2,
72. y: this.cursorPosition.y + this.cursorPosition.height / 2
73. };
74. // 光标区域中心点位置限制
75. if (this.cursorCenterPosition.x < 0) {
76. this.cursorPosition.x = -this.cursorPosition.width / 2;
77. }
78. if (this.cursorCenterPosition.y < 0) {
79. this.cursorPosition.y = -this.cursorPosition.height / 2;
80. }
81. if (this.cursorCenterPosition.x > this.sw) {
82. this.cursorPosition.x = this.sw - this.cursorPosition.width / 2;
83. }
84. if (this.cursorCenterPosition.y > this.sh) {
85. this.cursorPosition.y = this.sh - this.cursorPosition.height / 2;
86. }
87. }
88. } else {
89. this.isTouchDown = false;
90. }
91. });
92. }
93. .height('100%')
94. .width('100%')
95. .justifyContent(FlexAlign.Center)
96. }

98. // 绘制裁剪框
99. drawCursor() {
100. // 算出菱形四个点
101. let positionL: Position = { x: this.cursorPosition.x, y: this.cursorPosition.y + this.cursorPosition.height / 2 };
102. let positionT: Position = { x: this.cursorPosition.x + this.cursorPosition.width / 2, y: this.cursorPosition.y };
103. let positionR: Position = {
104. x: this.cursorPosition.x + this.cursorPosition.width,
105. y: this.cursorPosition.y + this.cursorPosition.height / 2
106. };
107. let positionB: Position = {
108. x: this.cursorPosition.x + this.cursorPosition.width / 2,
109. y: this.cursorPosition.y + this.cursorPosition.height
110. };
111. let lineWidth = 2;
112. this.canvasContext.clearRect(0, 0, this.sw, this.sh);
113. this.canvasContext.lineWidth = lineWidth;
114. this.canvasContext.strokeStyle = this.isTouchDown ? '#ff1a5cae' : '#ffffffff';

116. // 画出四角
117. this.canvasContext.beginPath();
118. this.canvasContext.moveTo(positionL.x + this.dashedLineW, positionL.y - this.dashedLineW);
119. this.canvasContext.lineTo(positionL.x, positionL.y);
120. this.canvasContext.lineTo(positionL.x + this.dashedLineW, positionL.y + this.dashedLineW);

122. this.canvasContext.moveTo(positionT.x - this.dashedLineW, positionT.y + this.dashedLineW);
123. this.canvasContext.lineTo(positionT.x, positionT.y);
124. this.canvasContext.lineTo(positionT.x + this.dashedLineW, positionT.y + this.dashedLineW);

126. this.canvasContext.moveTo(positionR.x - this.dashedLineW, positionR.y - this.dashedLineW);
127. this.canvasContext.lineTo(positionR.x, positionR.y);
128. this.canvasContext.lineTo(positionR.x - this.dashedLineW, positionR.y + this.dashedLineW);

130. this.canvasContext.moveTo(positionB.x - this.dashedLineW, positionB.y - this.dashedLineW);
131. this.canvasContext.lineTo(positionB.x, positionB.y);
132. this.canvasContext.lineTo(positionB.x + this.dashedLineW, positionB.y - this.dashedLineW);

134. this.canvasContext.stroke();

136. // 画出中心圆
137. this.canvasContext.beginPath();
138. this.canvasContext.strokeStyle = this.isTouchDown ? '#ff1a5cae' : '#ff9ba59b';
139. this.canvasContext.fillStyle = this.isTouchDown ? '#ff1a5cae' : '#ff9ba59b';
140. this.canvasContext.arc(this.cursorPosition.x + this.cursorPosition.width / 2,
141. this.cursorPosition.y + this.cursorPosition.width / 2, this.arcRadius, 0, 2 * Math.PI);
142. this.canvasContext.fill();
143. this.canvasContext.stroke();

145. // 画出四条线
146. this.canvasContext.beginPath();
147. this.canvasContext.lineWidth = 0.7;
148. this.canvasContext.moveTo(positionL.x, positionL.y);
149. this.canvasContext.lineTo(0, positionL.y);

151. this.canvasContext.moveTo(positionT.x, positionT.y);
152. this.canvasContext.lineTo(positionT.x, 0);

154. this.canvasContext.moveTo(positionR.x, positionR.y);
155. this.canvasContext.lineTo(this.sw, positionR.y);

157. this.canvasContext.moveTo(positionB.x, positionB.y);
158. this.canvasContext.lineTo(positionB.x, this.sh);

160. this.canvasContext.stroke();
161. }

163. // 判断点击位置是否在棱形中
164. isTouchCursorArea(touch: TouchObject) {
165. let tempLength = Math.sqrt((touch.x - this.cursorCenterPosition.x) * (touch.x - this.cursorCenterPosition.x) +
166. (touch.y - this.cursorCenterPosition.y) * (touch.y - this.cursorCenterPosition.y));
167. if (tempLength < (this.cursorWH / 2 / 1.414)) {
168. return true;
169. }
170. return false;
171. }
172. }

174. export interface RectPosition {
175. x: number;
176. y: number;
177. height: number;
178. width: number;
179. };

181. export interface Position {
182. x: number;
183. y: number;
184. };
```

[DrawDraggableCursor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomCanvas/entry/src/main/ets/pages/canvas/DrawDraggableCursor.ets#L15-L200)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/SqFpva2aTT2eG1MyoiiEtQ/zh-cn_image_0000002583478025.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234002Z&HW-CC-Expire=86400&HW-CC-Sign=4A430CCAD048D0B619E553E01A044E21985EC91B70992DF7AF42FF127D3BAD4F)

## 示例代码

* [自定义Canvas画布](https://gitcode.com/HarmonyOS_Samples/custom-canvas)
