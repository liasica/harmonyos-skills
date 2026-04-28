---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-get-img
title: 转换指定页面或指定区域为图片
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 转换PDF文档为图片 > 转换指定页面或指定区域为图片
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6fd08122221dbd8968e44ce8ade38447a0966d1203818a72f3f36431cd0dc19f
---

## 场景介绍

PDF文档页面转换为图片，或将页面的指定区域转换为图片时使用。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [getPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getpagepixelmap)(): image.PixelMap | 获取当前页的图片。 |
| [getCustomPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getcustompagepixelmap)(matrix: PdfMatrix, isGray: boolean, drawAnnotations: boolean): image.PixelMap | 获取指定PdfPage区域的图片内容。 |
| [getAreaPixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getareapixelmap)(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap | 获取指定PdfPage区域的图片内容，并指定图片的宽和高。 |
| [getAreaPixelMapWithOptions](../harmonyos-references/pdf-arkts-pdfservice.md#getareapixelmapwithoptions)(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap | 获取指定PdfPage区域的图片内容，并指定图片的宽和高等参数。 |

## 示例代码

1. 调用loadDocument方法加载PDF文档。
2. 调用getPage方法获取某个页面。
3. 调用getPagePixelMap，getAreaPixelMapWithOptions或getCustomPagePixelMap方法获取当前页面或者页面区域，这时获取的是image.PixelMap图像类型。
4. 将image.PixelMap图像类型转化为二进制图片文件并保存，参考以下方法pixelMap2Buffer。

   ```
   1. import { pdfService } from '@kit.PDFKit';
   2. import { image } from '@kit.ImageKit';
   3. import { fileIo as fs } from '@kit.CoreFileKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';

   7. @Entry
   8. @Component
   9. struct PdfPage {
   10. private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
   11. private context = this.getUIContext().getHostContext() as Context;
   12. private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

   14. aboutToAppear(): void {
   15. // 确保沙箱目录有input.pdf文档
   16. let filePath = this.context.filesDir + '/input.pdf';
   17. this.loadResult = this.pdfDocument.loadDocument(filePath);
   18. }

   20. // 将 pixelMap 转成图片格式
   21. pixelMap2Buffer(pixelMap: image.PixelMap): Promise<ArrayBuffer> {
   22. return new Promise((resolve, reject) => {
   23. /**
   24. 设置打包参数
   25. format：图片打包格式
   26. quality：JPEG 编码输出图片质量
   27. bufferSize：图片大小
   28. */
   29. let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 }
   30. // 创建ImagePacker实例
   31. const imagePackerApi = image.createImagePacker()
   32. imagePackerApi.packToData(pixelMap, packOpts).then((buffer: ArrayBuffer) => {
   33. resolve(buffer)
   34. }).catch((err: BusinessError) => {
   35. reject()
   36. })
   37. })
   38. }

   40. build() {
   41. Column() {
   42. // 获取为图片并保存到应用沙箱
   43. Button('getPagePixelMap').onClick(async () => {
   44. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
   45. let page = this.pdfDocument.getPage(0)
   46. let pixmap: image.PixelMap = page.getPagePixelMap();
   47. if (!pixmap) {
   48. return
   49. }
   50. const imgBuffer = await this.pixelMap2Buffer(pixmap)
   51. try {
   52. const file =
   53. fs.openSync(this.context.filesDir + `/${Date.now()}.png`, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
   54. await fs.write(file.fd, imgBuffer)
   55. // 关闭文档
   56. await fs.close(file.fd)
   57. } catch (e) {
   58. let error: BusinessError = e as BusinessError;
   59. hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
   60. }
   61. }
   62. })
   63. // 获取指定PdfPage区域的图片内容。
   64. Button('getCustomPagePixelMap').onClick(async () => {
   65. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
   66. let page = this.pdfDocument.getPage(0);
   67. let matrix = new pdfService.PdfMatrix();
   68. matrix.x = 100;
   69. matrix.y = 100;
   70. matrix.width = 500;
   71. matrix.height = 500;
   72. matrix.rotate = 0;
   73. let pixmap: image.PixelMap = page.getCustomPagePixelMap(matrix, false, false);
   74. if (!pixmap) {
   75. return;
   76. }
   77. const imgBuffer = await this.pixelMap2Buffer(pixmap);
   78. try {
   79. const file =
   80. fs.openSync(this.context.filesDir + `/${Date.now()}.jpeg`, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
   81. await fs.write(file.fd, imgBuffer);
   82. // 关闭文件
   83. await fs.close(file.fd);
   84. } catch (e) {
   85. let error: BusinessError = e as BusinessError;
   86. hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
   87. }
   88. }
   89. })
   90. // 获取指定PdfPage区域的图片内容
   91. Button('getAreaPixelMap').onClick(async () => {
   92. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
   93. //获取对应的page
   94. let page = this.pdfDocument.getPage(0);
   95. let matrix = new pdfService.PdfMatrix();
   96. //设置matrix来控制需要获取的区域
   97. matrix.x = 100;
   98. matrix.y = 100;
   99. matrix.width = 500;
   100. matrix.height = 500;
   101. matrix.rotate = 0;
   102. let pixmap: image.PixelMap = page.getAreaPixelMap(matrix, 400, 400, true, false);
   103. if (!pixmap) {
   104. return
   105. }
   106. const imgBuffer = await this.pixelMap2Buffer(pixmap)
   107. try {
   108. const file =
   109. fs.openSync(this.context.filesDir + `/${Date.now()}.bmp`, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
   110. await fs.write(file.fd, imgBuffer)
   111. // 关闭文件
   112. await fs.close(file.fd);
   113. } catch (e) {
   114. let error: BusinessError = e as BusinessError;
   115. hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
   116. }
   117. }
   118. })
   119. // 获取指定PdfPage区域的图片内容
   120. Button('getAreaPixelMapWithOptions').onClick(async () => {
   121. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
   122. //获取对应page
   123. let page = this.pdfDocument.getPage(0);
   124. let matrix = new pdfService.PdfMatrix();
   125. //设置matrix来控制需要获取的区域
   126. matrix.x = 100;
   127. matrix.y = 100;
   128. matrix.width = 500;
   129. matrix.height = 500;
   130. matrix.rotate = 0;
   131. //设置pixelmap是否黑白，背景是否透明等参数
   132. let options = new pdfService.PixelOptions();
   133. options.isGray = false;
   134. options.drawAnnotations = true;
   135. options.isTransparent = true;
   136. let pixmap: image.PixelMap = page.getAreaPixelMapWithOptions(matrix, 400, 400, options);
   137. if (!pixmap) {
   138. return
   139. }
   140. const imgBuffer = await this.pixelMap2Buffer(pixmap)
   141. try {
   142. const file =
   143. fs.openSync(this.context.filesDir + `/${Date.now()}.bmp`, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
   144. await fs.write(file.fd, imgBuffer)
   145. // 关闭文件
   146. await fs.close(file.fd);
   147. } catch (e) {
   148. let error: BusinessError = e as BusinessError;
   149. hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
   150. }
   151. }
   152. })
   153. }
   154. }
   155. }
   ```
