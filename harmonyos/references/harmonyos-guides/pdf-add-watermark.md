---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-watermark
title: 添加、删除水印
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除水印
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:45+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ff24f54dad3c1775ee5e5b6ea8e1dc6f810e0458b3d108a269abc27abe0a7e39
---

对指定页面添加水印，包括文本水印或图片水印。

* 文本水印可以设置字体、大小、旋转，位置等属性。
* 图片水印可以设置缩放、旋转、透明度和位置等属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/jR1Km9m_T2esGNhpWFampQ/zh-cn_image_0000002558605948.png?HW-CC-KV=V1&HW-CC-Date=20260429T053944Z&HW-CC-Expire=86400&HW-CC-Sign=DFA6147E8FBDA838CA842484A2D059536088B0EC5BC0F8977191D51FB557CCFB)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [addWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#addwatermark)(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void | 插入水印到PDF文档。如果插入的是图片，支持的图片格式参考[ImageFormat](../harmonyos-references/pdf-arkts-pdfservice.md#imageformat)，文本字符无限制。 |
| [removeWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#removewatermark)(): boolean | 删除PDF文档水印。 |

注意

[addWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#addwatermark)方法属于耗时业务，需要遍历每一页去添加水印，添加页面较多时建议放到线程里去处理。

## 示例代码

### 添加、删除文本水印

**添加文本水印**

1. 调用loadDocument方法，加载PDF文档。
2. 实例化文本水印TextWatermarkInfo类，并设置相关属性，包括字体、大小、旋转，位置等。
3. 调用addWatermark，添加文本水印。
4. 保存PDF文档到应用沙箱。

**删除文本水印**

1. 调用loadDocument方法，加载PDF文档。
2. 调用removeWatermark，删除文本水印。
3. 保存PDF文档到应用沙箱。

```
1. import { pdfService } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { Font } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct PdfPage {
8. private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
9. private context = this.getUIContext().getHostContext() as Context;

11. build() {
12. Column() {
13. Button('addTextWatermark').onClick(async () => {
14. // 确保在工程目录src/main/resources/resfile里有input.pdf文档
15. let filePath = this.context.resourceDir + '/input.pdf';
16. let res = this.pdfDocument.loadDocument(filePath);
17. if (res === pdfService.ParseResult.PARSE_SUCCESS) {
18. let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
19. wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
20. wminfo.content = 'This is Watermark';
21. wminfo.textSize = 30;
22. wminfo.textColor = 200;
23. wminfo.fontInfo = new pdfService.FontInfo();
24. // 确保字体路径存在
25. let font: Font = new Font()
26. wminfo.fontInfo.fontPath = font.getFontByName('HarmonyOS Sans').path;
27. wminfo.opacity = 0.5;
28. wminfo.isOnTop = true;
29. wminfo.rotation = 45;
30. wminfo.scale = 1.5;
31. wminfo.opacity = 0.5;
32. wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
33. wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
34. wminfo.horizontalSpace = 1.0;
35. wminfo.verticalSpace = 1.0;
36. this.pdfDocument.addWatermark(wminfo, 0, 5, true, true);
37. let outPdfPath = this.context.filesDir + '/testTextWatermark.pdf';
38. let result = this.pdfDocument.saveDocument(outPdfPath);
39. hilog.info(0x0000, 'PdfPage', 'addTextWatermark %{public}s!', result ? 'success' : 'fail');
40. }
41. this.pdfDocument.releaseDocument();
42. })
43. Button('removeTextWatermark').onClick(async () => {
44. let filePath = this.context.filesDir + '/testTextWatermark.pdf';
45. let res = this.pdfDocument.loadDocument(filePath);
46. if (res === pdfService.ParseResult.PARSE_SUCCESS && this.pdfDocument.hasWatermark()) {
47. let removeResult = this.pdfDocument.removeWatermark();
48. if (removeResult) {
49. let outPdfPath = this.context.filesDir + '/removeWatermark.pdf';
50. let result = this.pdfDocument.saveDocument(outPdfPath);
51. hilog.info(0x0000, 'PdfPage', 'removeWatermark %{public}s!', result ? 'success' : 'fail');
52. }
53. }
54. this.pdfDocument.releaseDocument();
55. })
56. }
57. }
58. }
```

### 添加、删除图片水印

**添加图片水印**

1. 调用loadDocument方法加载PDF文档。
2. 实例化图片水印ImageWatermarkInfo类，并设置相关属性，包括缩放、旋转、透明度和位置等。
3. 调用addWatermark添加图片水印。
4. 保存PDF文档到应用沙箱。

**删除图片水印**

1. 调用loadDocument方法加载PDF文档。
2. 调用removeWatermark删除图片水印。
3. 保存PDF文档到应用沙箱。

```
1. import { pdfService } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct PdfPage {
7. private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
8. private context = this.getUIContext().getHostContext() as Context;

10. build() {
11. Column() {
12. Button('addImageWatermark').onClick(async () => {
13. let filePath = this.context.filesDir + '/input.pdf';
14. let res = this.pdfDocument.loadDocument(filePath);
15. if (res === pdfService.ParseResult.PARSE_SUCCESS) {
16. let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
17. wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_IMAGE;
18. // 确保沙箱目录有img.jpg文档
19. wminfo.imagePath = this.context.filesDir + '/img.jpg';
20. wminfo.opacity = 0.5;
21. wminfo.isOnTop = true;
22. wminfo.rotation = 45;
23. wminfo.scale = 0.5;
24. wminfo.opacity = 0.5;
25. wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
26. wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
27. wminfo.horizontalSpace = 1.0;
28. wminfo.verticalSpace = 1.0;
29. this.pdfDocument.addWatermark(wminfo, 0, 5, true, true);
30. let outPdfPath = this.context.filesDir + '/testImageWatermark.pdf';
31. let result = this.pdfDocument.saveDocument(outPdfPath);
32. hilog.info(0x0000, 'PdfPage', 'addImageWatermark %{public}s!', result ? 'success' : 'fail');
33. }
34. this.pdfDocument.releaseDocument();
35. })
36. Button('removeImageWatermark').onClick(async () => {
37. let filePath = this.context.filesDir + '/testImageWatermark.pdf';
38. let res = this.pdfDocument.loadDocument(filePath);
39. if (res === pdfService.ParseResult.PARSE_SUCCESS && this.pdfDocument.hasWatermark()) {
40. let removeResult = this.pdfDocument.removeWatermark();
41. if (removeResult) {
42. let outPdfPath = this.context.filesDir + '/removeImageWatermark.pdf';
43. let result = this.pdfDocument.saveDocument(outPdfPath);
44. hilog.info(0x0000, 'PdfPage', 'removeImageWatermark %{public}s!', result ? 'success' : 'fail');
45. }
46. }
47. this.pdfDocument.releaseDocument();
48. })
49. }
50. }
51. }
```
