---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-add-watermark
title: 水印添加
breadcrumb: 最佳实践 > 图形 > 图形绘制 > 水印添加
category: best-practices
scraped_at: 2026-04-28T08:20:53+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:0e6a6c75e579eb6b34eab3a3b2fb42faf13bf11f463704d628992f960338d7d4
---

## 概述

在软件开发中，水印是一种在应用页面、图片或文档中嵌入的标记，它通常采用文字或图案的形式展现。水印通常有以下用途：

* 标识来源：可用于标识应用、各种文件的来源或作者，确保产权的归属。
* 版权保护：可携带版权保护信息，有效防止他人篡改、盗用、非法复制。
* 艺术效果：可作为一种艺术效果，为图片或应用增添独特的风格。

本文通过图文与代码结合的方式，对以下几种常见的水印添加场景进行讲解，旨在让开发者理解水印添加的基本原理以及掌握开发的流程与细节。

* [页面上添加水印](bpta-add-watermark.md#section12388834480)
* [图片上添加水印](bpta-add-watermark.md#section987311343125)
* [PDF文档添加水印](bpta-add-watermark.md#section7418171112138)

## 页面上添加水印

### 场景描述

某个页面背景上添加水印文字，实现效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/PobSZSlFQNWTslFD2eNLTQ/zh-cn_image_0000002229451785.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=230046D919E33371F42AD3CC80AAB440340990537F185492070F24C3FFBF119B "点击放大")

### 实现原理

**关键技术**

[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形。使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象在[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件上进行绘制，其中[fillText()](../harmonyos-references/ts-canvasrenderingcontext2d.md#filltext)方法用于绘制文本，[drawImage()](../harmonyos-references/ts-canvasrenderingcontext2d.md#drawimage)方法用于图像绘制。

**开发流程**

1. 创建[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)画布，在画布上绘制水印。
2. 使用[Stack](../harmonyos-references/ts-container-stack.md)组件或[浮层overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)属性，将画布与UI页面组件融合显示。

### 开发步骤

1. 封装水印组件
   1. 创建Canvas组件，监听[Canvas.onReady](../harmonyos-references/ts-components-canvas-canvas.md#事件)事件，该事件回调在Canvas组件初始化完成时或大小变化时执行，在回调中进行水印绘制draw()方法的执行。并通过设置Canvas组件的[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性，使水印组件不影响其他组件的触摸测试，让页面能正常交互。

      ```
      1. @Component
      2. export struct Watermark {
      3. private settings: RenderingContextSettings = new RenderingContextSettings(true);
      4. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
      5. // ...
      6. build() {
      7. Canvas(this.context)
      8. .width('100%')
      9. .height('100%')
      10. .hitTestBehavior(HitTestMode.Transparent)
      11. .onReady(() => this.draw())
      12. }
      13. }
      ```

      [Watermark.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/component/Watermark.ets#L20-L65)
   2. 实现绘制水印draw()方法。绘制的起点默认为坐标轴的原点（画布的左上角），通过坐标轴的平移及旋转，实现在画布的不同位置、不同角度绘制水印。如果水印有一定旋转角度，想保证第一个水印能完整显示，需要对绘制的起点做平移，平移距离通过旋转角度及水印宽高计算。
      * 旋转角度大于0，由下图可知，水印沿x轴方向平移距离positionX = tan(θ) \* 水印高度，即绘制起点为(positionX, 0)。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/zi36IK1xTbaeVVUsvFPo1w/zh-cn_image_0000002229337289.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=7FD8AA2D26D94BD487E30820B888E4A565955DDE8087DB777292B6E71617A7FA "点击放大")
      * 旋转角度小于0，由下图可知，水印沿y轴方向平移距离positionY = tan(θ) \* 水印宽度，即绘制起点为(0, positionY)。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/FNAgVi-cQwW8UdU5emUrrQ/zh-cn_image_0000002229337285.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=2E5633FE85AAB4A11C0F80D35F8721D239CCD5F934D5C4AFD730B9A6531E79E9 "点击放大")

      最终通过[CanvasRenderingContext2D.fillText()](../harmonyos-references/ts-canvasrenderingcontext2d.md#filltext)方法进行水印文字的绘制。

      ```
      1. @Prop watermarkWidth: number = 120;
      2. @Prop watermarkHeight: number = 120;
      3. @Prop watermarkText: string = this.getWatermarkText();
      4. @Prop rotationAngle: number = -30;
      5. @Prop fillColor: string | number | CanvasGradient | CanvasPattern = '#10000000';
      6. @Prop font: string = '16vp';

      8. draw() {
      9. this.context.fillStyle = this.fillColor;
      10. this.context.font = this.font;
      11. const colCount = Math.ceil(this.context.width / this.watermarkWidth);
      12. const rowCount = Math.ceil(this.context.height / this.watermarkHeight);
      13. for (let col = 0; col <= colCount; col++) {
      14. let row = 0;
      15. for (; row <= rowCount; row++) {
      16. const angle = this.rotationAngle * Math.PI / 180;
      17. this.context.rotate(angle);
      18. const positionX = this.rotationAngle > 0 ? this.watermarkHeight * Math.tan(angle) : 0;
      19. const positionY = this.rotationAngle > 0 ? 0 : this.watermarkWidth * Math.tan(-angle);
      20. this.context.fillText(this.watermarkText, positionX, positionY);
      21. this.context.rotate(-angle);
      22. this.context.translate(0, this.watermarkHeight);
      23. }
      24. this.context.translate(0, -this.watermarkHeight * row);
      25. this.context.translate(this.watermarkWidth, 0);
      26. }
      27. }
      ```

      [Watermark.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/component/Watermark.ets#L26-L52)
2. 将水印组件与UI页面组件融合显示。

   方式一：使用Stack将水印组件叠加在UI组件上层。

   ```
   1. Stack({ alignContent: Alignment.Center }) {
   2. Column() {
   3. Image($r('app.media.empty'))
   4. .width(110)
   5. .height(88)
   6. // ...
   7. }
   8. Watermark({ rotationAngle: 20 })
   9. }
   ```

   [WatermarkStackPage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/WatermarkStackPage.ets#L28-L42)

   方式二：设置UI组件的overlay属性，使水印组件作为UI组件的浮层显示。注意watermarkBuilder中嵌套了一层父元素Column，所以需要同时设置Column的[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性，使浮层下方页面能正常交互。

   ```
   1. @Builder
   2. watermarkBuilder() {
   3. Column() {
   4. Watermark()
   5. }
   6. .hitTestBehavior(HitTestMode.Transparent)
   7. }
   8. build() {
   9. // ...
   10. Column() {
   11. Image($r('app.media.empty'))
   12. .width(110)
   13. .height(88)
   14. // ...
   15. }
   16. .justifyContent(FlexAlign.Center)
   17. .alignItems(HorizontalAlign.Center)
   18. .layoutWeight(1)
   19. .overlay(this.watermarkBuilder())
   20. // ...
   21. }
   ```

   [WatermarkOverlayPage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/WatermarkOverlayPage.ets#L24-L60)

说明

如果需要多个页面或应用全局添加水印，可将上述方式二中的watermarkBuilder封装到一个单独的文件，export出一个全局的watermarkBuilder。在需要添加水印页面的根节点上添加.overlay绑定watermarkBuilder即可。

## 图片上添加水印

### 场景描述

保存的图片、拍照生成的图片等场景，需要添加水印。实现效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/SuxDaIXrRGG3G1OgTGXaAQ/zh-cn_image_0000002229451781.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=1C4A77D90455E8B9C91EA27E979C2C5261B4424965D70642AF4C58CB4CBDEA16 "点击放大")

### 实现原理

**关键技术**

[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)提供离屏画布，与[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)使用场景区别在于是否需要将画布渲染在屏幕上。使用[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)在[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)上进行离屏绘制，其中[fillText()](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md#filltext)方法用于绘制文本，[drawImage()](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md#drawimage)方法用于图像绘制。

**开发流程**

1. 解析图片得到pixelMap数据。
2. 创建与图片宽高一致的[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)离屏画布。
3. 将图片和水印依次绘制到离屏画布上。
4. 获取离屏画布的pixelMap数据。
5. 将pixelMap数据写入文件中。

### 开发步骤

1. 解析图片得到pixelMap数据。
   1. 使用[resourceManager.getMediaContent()](../harmonyos-references/js-apis-resource-manager.md#getmediacontent9-1)方法获取图片内容，得到ArrayBuffer数据。使用[image.createImageSource(buf: ArrayBuffer)](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource9-2)方法创建图片源实例。

      说明

      ImagePixelMap为自定义类型：{ pixelMap: image.PixelMap, width: number, height: number }。

      ```
      1. async getImagePixelMap(resource: Resource): Promise<ImagePixelMap | undefined> {
      2. let result: ImagePixelMap | undefined = undefined;
      3. try {
      4. const data: Uint8Array =
      5. await this.getUIContext().getHostContext()?.resourceManager.getMediaContent(resource.id) as Uint8Array;
      6. const arrayBuffer: ArrayBuffer = data.buffer.slice(data.byteOffset, data.byteLength + data.byteOffset);
      7. const imageSource: image.ImageSource = image.createImageSource(arrayBuffer);
      8. result = await imageSource2PixelMap(imageSource);
      9. } catch (e) {
      10. let err = e as BusinessError;
      11. hilog.error(0x0000, TAG, `failed code=${err.code}, message=${err.message}`);
      12. }
      13. return result;
      14. }
      ```

      [SaveImagePage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/SaveImagePage.ets#L47-L60)
   2. 使用[ImageSource.getImageInfo()](../harmonyos-references/arkts-apis-image-imagesource.md#getimageinfo-2)方法获取图片宽、高信息，使用[ImageSource.createPixelMap()](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)方法创建PixelMap对象。

      ```
      1. export async function imageSource2PixelMap(imageSource: image.ImageSource): Promise<ImagePixelMap> {
      2. const imageInfo: image.ImageInfo = await imageSource.getImageInfo();
      3. const height = imageInfo.size.height;
      4. const width = imageInfo.size.width;
      5. const options: image.DecodingOptions = {
      6. editable: true,
      7. desiredSize: { height, width }
      8. };
      9. const pixelMap: PixelMap = await imageSource.createPixelMap(options);
      10. const result: ImagePixelMap = { pixelMap, width, height };
      11. return result;
      12. }
      ```

      [Utils.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/constants/Utils.ets#L61-L72)
2. 通过[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)离屏画布绘制图片及水印，得到融合水印后的pixelMap数据。
   1. 创建与图片宽高一致的[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)离屏画布，这里注意单位保持一致。
   2. 使用[OffscreenCanvasRenderingContext2D.drawImage()](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md#drawimage)将图片绘制到离屏画布上。
   3. 使用[OffscreenCanvasRenderingContext2D.fillText()](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md#filltext)将水印绘制在离屏画布的指定位置。
   4. 使用[OffscreenCanvasRenderingContext2D.getPixelMap()](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md#getpixelmap)以当前离屏画布指定区域内的像素创建PixelMap对象。

      ```
      1. export function addWatermark(
      2. imagePixelMap: ImagePixelMap,
      3. text: string = 'watermark',
      4. drawWatermark?: (OffscreenContext: OffscreenCanvasRenderingContext2D) => void
      5. ): image.PixelMap {
      6. const height = uiContext?.px2vp(imagePixelMap.height) as number;
      7. const width = uiContext?.px2vp(imagePixelMap.width) as number;
      8. const offScreenCanvas = new OffscreenCanvas(width, height);
      9. const offScreenContext = offScreenCanvas.getContext('2d');
      10. offScreenContext.drawImage(imagePixelMap.pixelMap, 0, 0, width, height);
      11. if (drawWatermark) {
      12. drawWatermark(offScreenContext);
      13. } else {
      14. let displayWidth: number = 0;
      15. try {
      16. displayWidth = display.getDefaultDisplaySync().width;
      17. } catch (e) {
      18. let err = e as BusinessError;
      19. hilog.error(0x0000, TAG, `failed code=${err.code}, message=${err.message}`);
      20. }
      21. const vpWidth = uiContext?.px2vp(displayWidth) ?? displayWidth;
      22. const imageScale = width / vpWidth;
      23. offScreenContext.textAlign = 'right';
      24. offScreenContext.fillStyle = '#A2FFFFFF';
      25. offScreenContext.font = 12 * imageScale + 'vp';
      26. const padding = 5 * imageScale;
      27. offScreenContext.fillText(text, width - padding, height - padding);
      28. }
      29. return offScreenContext.getPixelMap(0, 0, width, height);
      30. }
      ```

      [Utils.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/constants/Utils.ets#L75-L104)
3. 将添加水印后得到的pixelMap数据写入文件中。

   ```
   1. export async function saveToFile(pixelMap: image.PixelMap, context: Context): Promise<void> {
   2. try {
   3. const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
   4. const filePath = await phAccessHelper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
   5. const imagePacker = image.createImagePacker();
   6. const imageBuffer = await imagePacker.packToData(pixelMap, {
   7. format: 'image/png',
   8. quality: 100
   9. });
   10. const mode = fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE;
   11. fd = (await fileIo.open(filePath, mode)).fd;
   12. await fileIo.truncate(fd);
   13. await fileIo.write(fd, imageBuffer);
   14. } catch (err) {
   15. hilog.error(0x0000, TAG, 'saveToFile error：', JSON.stringify(err) ?? '');
   16. } finally {
   17. try {
   18. if (fd) {
   19. fileIo.close(fd);
   20. }
   21. } catch (e) {
   22. let err = e as BusinessError;
   23. hilog.error(0x0000, TAG, `close failed code=${err.code}, message=${err.message}`);
   24. }
   25. }
   26. }
   ```

   [Utils.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/constants/Utils.ets#L28-L53)

## PDF文档添加水印

### 场景描述

在PDF预览页面点击添加水印按钮，生成带水印的PDF文档，并显示在预览页面中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/p-rLzXoKSYOSl6i-2n-IYg/zh-cn_image_0000002229337293.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=3476AAD9892AB0CC36B384FAD092853E82A8680081C414223E1CD542693C08E5 "点击放大")

### 实现原理

**关键技术**

[pdfService](../harmonyos-references/pdf-arkts-pdfservice.md)模块为应用提供统一管理PDF页面的页眉页脚、水印、背景、批注、书签的能力。[pdfService.TextWatermarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#section2094113924815)类和[pdfService.ImageWatermarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#section1122165334818)分别提供创建文本水印和图片水印的能力。[pdfService.PdfDocument](../harmonyos-references/pdf-arkts-pdfservice.md#section1319183318231)类提供与文档相关能力，其中[addWatermark()](../harmonyos-references/pdf-arkts-pdfservice.md#section206080386472)方法用于添加水印。

**开发流程**

1. 将应用侧PDF文件写入沙箱中。
2. 使用[pdfService](../harmonyos-references/pdf-arkts-pdfservice.md)模块相关API加载指定沙箱路径的PDF并添加水印。

### 开发步骤

1. 使用[getRawFileContentSync()](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontentsync10)方法获取resource/rawfile目录下的PDF文件内容，使用[fs.writeSync()](../harmonyos-references/js-apis-file-fs.md#writesync10)方法写入沙箱中。

   ```
   1. savePdfToSandbox(): string {
   2. const filePath = this.getPdfSandboxPath();
   3. try {
   4. fileIo.accessSync(filePath);
   5. const content: Uint8Array = this.getUIContext().getHostContext()?.resourceManager.getRawFileContentSync('watermark.pdf') as Uint8Array;
   6. const file = fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
   7. fileIo.writeSync(file.fd, content.buffer);
   8. fileIo.closeSync(file.fd);
   9. } catch (e) {
   10. let err = e as BusinessError;
   11. hilog.error(0x0000, TAG, `savePdfToSandbox failed code=${err.code}, message=${err.message}`);
   12. }
   13. return filePath;
   14. }
   ```

   [WatermarkPdfPage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/WatermarkPdfPage.ets#L60-L73)
2. 使用[pdfViewManager.PdfController](../harmonyos-references/pdf-arkts-pdfviewmanage.md#section15202162183817)控制器中的[loadDocument()](../harmonyos-references/pdf-arkts-pdfviewmanage.md#section073321844615)方法通过沙箱路径加载文件，显示到PDF预览组件[PdfView](../harmonyos-references/pdf-arkts-pdfview-component.md)中。

   ```
   1. private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
   2. // ...
   3. aboutToAppear(): void {
   4. const filePath = this.savePdfToSandbox();
   5. this.controller.loadDocument(filePath);
   6. }
   7. // ...
   8. build() {
   9. // ...
   10. PdfView({
   11. controller: this.controller,
   12. pageFit: pdfService.PageFit.FIT_WIDTH
   13. })
   14. // ...
   ```

   [WatermarkPdfPage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/WatermarkPdfPage.ets#L30-L178)
3. 通过文本水印类[pdfService.TextWatermarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#section2094113924815)创建水印对象，设置水印内容、字体、颜色、位置等相关属性；图片水印对象通过[pdfService.ImageWatermarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#section1122165334818)创建。

   ```
   1. getWatermarkInfo() {
   2. const watermarkInfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
   3. watermarkInfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
   4. watermarkInfo.content = 'This is Watermark';
   5. watermarkInfo.textSize = 32;
   6. watermarkInfo.textColor = 200;
   7. watermarkInfo.rotation = 45;
   8. watermarkInfo.opacity = 0.3;
   9. return watermarkInfo;
   10. }
   ```

   [WatermarkPdfPage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/WatermarkPdfPage.ets#L82-L91)
4. 通过PDF文档类[pdfService.PdfDocument](../harmonyos-references/pdf-arkts-pdfservice.md#section1319183318231)创建文档对象，使用文档对象的[loadDocument()](../harmonyos-references/pdf-arkts-pdfservice.md#section167288392229)方法加载文档，[addWatermark()](../harmonyos-references/pdf-arkts-pdfservice.md#section206080386472)方法添加水印、[saveDocument()](../harmonyos-references/pdf-arkts-pdfservice.md#section660833016157)方法将添加水印后的文档保存到沙箱中。

   ```
   1. addWatermark() {
   2. const filePath = this.getPdfSandboxPath();
   3. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
   4. pdfDocument.loadDocument(filePath);
   5. pdfDocument.addWatermark(this.getWatermarkInfo(), 0, pdfDocument.getPageCount(), true, true);
   6. const watermarkFilePath = this.getAddedWatermarkPdfSandboxPath();
   7. pdfDocument.saveDocument(watermarkFilePath);
   8. this.showInPdfView(watermarkFilePath);
   9. }
   ```

   [WatermarkPdfPage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/WatermarkPdfPage.ets#L94-L102)
5. 将沙箱中添加水印后的文档加载到PDF预览器中。

   ```
   1. async showInPdfView(filePath: string) {
   2. this.hasWatermark = true;
   3. // release before reload avoid crash.
   4. this.controller.releaseDocument();
   5. await this.controller.loadDocument(filePath);
   6. this.controller.setPageFit(pdfService.PageFit.FIT_WIDTH);
   7. }
   ```

   [WatermarkPdfPage.ets](https://gitcode.com/harmonyos_samples/watermark/blob/master/entry/src/main/ets/pages/WatermarkPdfPage.ets#L105-L111)

## 示例代码

* [实现添加水印功能](https://gitcode.com/harmonyos_samples/watermark)
