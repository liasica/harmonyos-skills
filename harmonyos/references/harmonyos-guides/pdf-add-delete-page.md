---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-delete-page
title: 添加、删除PDF页
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除PDF页
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f93726982bf6a2db5a7291dc040895f2ec99dcfb3f080102d4c8fad78130add
---

在PDF文档中添加或删除页面，包括：

* 添加单个、多个空白页到PDF文档。
* 删除PDF文档中单个、多个指定页。
* 将其他PDF文档页添加到本PDF文档。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [insertBlankPage](../harmonyos-references/pdf-arkts-pdfservice.md#insertblankpage)(index: number, width: number, height: number): PdfPage | 在指定位置插入空白PDF页。 |
| [getPage](../harmonyos-references/pdf-arkts-pdfservice.md#getpage)(index: number): PdfPage | 获取指定页的对象。 |
| [insertPageFromDocument](../harmonyos-references/pdf-arkts-pdfservice.md#insertpagefromdocument)(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage | 将其他文档的页添加到当前文档。 |
| [deletePage](../harmonyos-references/pdf-arkts-pdfservice.md#deletepage)(index: number, count: number): void | 删除指定的PDF页。 |

## 示例代码

1. 调用loadDocument方法，加载PDF文档。
2. 调用getPage方法获取当前页，用于获取页面宽高。
3. 调用insertBlankPage和insertPageFromDocument方法实现如下功能。

   1. 插入单个空白页。
   2. 插入多个空白页。
   3. 将input2.pdf文档的索引1、2、3页插入到input.pdf索引0的位置，并另存文档。
4. 调用deletePage方法删除单个或多个索引页。

```
1. import { pdfService } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct PdfPage {
7. private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
8. private context = this.getUIContext().getHostContext() as Context;

10. aboutToAppear(): void {
11. // 确保沙箱目录有input.pdf文档
12. let filePath = this.context.filesDir + '/input.pdf';
13. this.pdfDocument.loadDocument(filePath);
14. }

16. build() {
17. Column() {
18. // 插入单个空白页
19. Button('insertBlankPage').onClick(async () => {
20. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
21. let page2: pdfService.PdfPage = this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
22. let outPdfPath = this.context.filesDir + '/testInsertBlankPage.pdf';
23. let result = this.pdfDocument.saveDocument(outPdfPath);
24. hilog.info(0x0000, 'PdfPage', 'insertBlankPage %{public}s!', result ? 'success' : 'fail');
25. })
26. // 插入多个空白页
27. Button('insertSomeBlankPage').onClick(async () => {
28. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
29. for (let i = 0; i < 3; i++) {
30. this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
31. }
32. let outPdfPath = this.context.filesDir + '/testInsertSomeBlankPage.pdf';
33. let result = this.pdfDocument.saveDocument(outPdfPath);
34. hilog.info(0x0000, 'PdfPage', 'insertSomeBlankPage %{public}s!', result ? 'success' : 'fail');
35. })
36. // 将input2.pdf文档的索引1,2,3页插入到input.pdf索引0的位置，并另存文档
37. Button('insertPageFromDocument').onClick(async () => {
38. let pdfDoc: pdfService.PdfDocument = new pdfService.PdfDocument();
39. // 确保该沙箱目录下有 input2.pdf文档
40. pdfDoc.loadDocument(this.context.filesDir + '/input2.pdf');
41. this.pdfDocument.insertPageFromDocument(pdfDoc, 1, 3, 0);
42. let outPdfPath = this.context.filesDir + '/testInsertPageFromDocument.pdf';
43. let result = this.pdfDocument.saveDocument(outPdfPath);
44. hilog.info(0x0000, 'PdfPage', 'insertPageFromDocument %{public}s!', result ? 'success' : 'fail');
45. })
46. // 删除单个或多个索引页
47. Button('deletePage').onClick(async () => {
48. this.pdfDocument.deletePage(2, 2);
49. let outPdfPath = this.context.filesDir + '/testDeletePage.pdf';
50. let result = this.pdfDocument.saveDocument(outPdfPath);
51. hilog.info(0x0000, 'PdfPage', 'deletePage %{public}s!', result ? 'success' : 'fail');
52. })
53. }
54. }
55. }
```
