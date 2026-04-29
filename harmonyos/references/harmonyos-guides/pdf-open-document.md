---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-open-document
title: 打开和保存PDF文档
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 打开和保存PDF文档
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:43+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a7683090f17bc0f4660667d55c39823205f9d19c5afc0b2afb4f1feaa4b1ea50
---

对PDF文档[添加内容](pdf-add-txt-img-annot.md)、[页眉页脚](pdf-add-headerfooter.md)、[水印](pdf-add-watermark.md)、[背景图片](pdf-add-background.md)或[书签](pdf-add-bookmark.md)等操作前，需要打开文档，并且在文档操作完成后，保存PDF文档。

pdfService和PdfView都可实现打开和保存文档，使用场景上有如下区别：

* 需要对PDF文档做相关的编辑和操作，建议使用pdfService的能力打开和保存文档。
* 需要预览、搜索关键字、监听PDF文档回调和批注等操作，推荐使用PdfView打开。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadDocument](../harmonyos-references/pdf-arkts-pdfservice.md#loaddocument)(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult | 加载指定文档路径。 |
| [saveDocument](../harmonyos-references/pdf-arkts-pdfservice.md#savedocument)(path: string, onProgress?: (progress: number) => number): boolean | 保存文档。 |

## 示例代码

1. 调用loadDocument方法，加载PDF文档。
2. 在【Save As】和【Save】两个按钮中调用saveDocument方法，分别实现了另存为PDF文档和保存覆盖源PDF文档的两种方式。

```
1. import { pdfService } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { fileIo } from '@kit.CoreFileKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct PdfPage {
9. private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
10. private context = this.getUIContext().getHostContext() as Context;
11. private filePath = '';
12. @State saveEnable: boolean = false;

14. aboutToAppear(): void {
15. this.filePath = this.context.filesDir + '/input.pdf';
16. try {
17. let res = fileIo.accessSync(this.filePath);
18. if(!res) {
19. // 确保在工程目录src/main/resources/resfile里有input.pdf文档
20. let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('rawfile/input.pdf');
21. let fdSand =
22. fileIo.openSync(this.filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
23. fileIo.writeSync(fdSand.fd, content.buffer);
24. fileIo.closeSync(fdSand.fd);
25. }
26. this.pdfDocument.loadDocument(this.filePath);
27. } catch (e) {
28. let error: BusinessError = e as BusinessError;
29. hilog.error(0x0000, 'PdfPage', `Failed to loadDocument. Code: ${error.code}, message: ${error.message} `);
30. }
31. }

33. build() {
34. Column() {
35. // 另存为一份PDF文档
36. Button('Save As').onClick(() => {
37. // 可以对PDF文档添加页眉页脚，水印，背景等一些内容，然后另存文档
38. let outPdfPath = this.context.filesDir + '/testSaveAsPdf.pdf';
39. let result = this.pdfDocument.saveDocument(outPdfPath);
40. this.saveEnable = true;
41. hilog.info(0x0000, 'PdfPage', 'saveAsPdf %{public}s!', result ? 'success' : 'fail');
42. })
43. // 保存覆盖源PDF文档
44. Button('Save').enabled(this.saveEnable).onClick(() => {
45. // 这里可以对PDF文档添加内容、页眉页脚、水印、背景等一些内容，然后保存文档
46. let tempDir = this.context.tempDir;
47. let tempFilePath = tempDir + `/temp${Math.random()}.pdf`;
48. try {
49. fileIo.copyFileSync(this.filePath, tempFilePath);
50. } catch (e) {
51. let error: BusinessError = e as BusinessError;
52. hilog.error(0x0000, 'PdfPage', `Failed to copyFileSync. Code: ${error.code}, message: ${error.message} `);
53. }
54. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
55. // 加载临时文档
56. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
57. if (loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
58. let result = pdfDocument.saveDocument(this.filePath);
59. hilog.info(0x0000, 'PdfPage', 'savePdf %{public}s!', result ? 'success' : 'fail');
60. }
61. })
62. }
63. }
64. }
```
