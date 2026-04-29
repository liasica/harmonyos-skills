---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-delete-page
title: 添加、删除PDF页
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除PDF页
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:44+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0b9fc718263d71d6e5ffe667bfe4500f47149bd1d564bcab587c7837fd14b3b7
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
11. // 确保在工程目录src/main/resources/resfile里有input.pdf文档
12. let filePath = this.context.resourceDir + '/input.pdf';
13. this.pdfDocument.loadDocument(filePath);
14. }

17. build() {
18. Column() {
19. // 插入单个空白页
20. Button('insertBlankPage').onClick(async () => {
21. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
22. let page2: pdfService.PdfPage = this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
23. let outPdfPath = this.context.filesDir + '/testInsertBlankPage.pdf';
24. let result = this.pdfDocument.saveDocument(outPdfPath);
25. hilog.info(0x0000, 'PdfPage', 'insertBlankPage %{public}s!', result ? 'success' : 'fail');
26. })
27. // 插入多个空白页
28. Button('insertSomeBlankPage').onClick(async () => {
29. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
30. for (let i = 0; i < 3; i++) {
31. this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
32. }
33. let outPdfPath = this.context.filesDir + '/testInsertSomeBlankPage.pdf';
34. let result = this.pdfDocument.saveDocument(outPdfPath);
35. hilog.info(0x0000, 'PdfPage', 'insertSomeBlankPage %{public}s!', result ? 'success' : 'fail');
36. })
37. // 将input2.pdf文档的索引1,2,3页插入到input.pdf索引0的位置，并另存文档
38. Button('insertPageFromDocument').onClick(async () => {
39. let pdfDoc: pdfService.PdfDocument = new pdfService.PdfDocument();
40. // 确保在工程目录src/main/resources/resfile里有input2.pdf文档
41. pdfDoc.loadDocument(this.context.resourceDir + '/input2.pdf');
42. this.pdfDocument.insertPageFromDocument(pdfDoc, 1, 3, 0);
43. let outPdfPath = this.context.filesDir + '/testInsertPageFromDocument.pdf';
44. let result = this.pdfDocument.saveDocument(outPdfPath);
45. hilog.info(0x0000, 'PdfPage', 'insertPageFromDocument %{public}s!', result ? 'success' : 'fail');
46. })
47. // 删除单个或多个索引页
48. Button('deletePage').onClick(async () => {
49. this.pdfDocument.deletePage(2, 2);
50. let outPdfPath = this.context.filesDir + '/testDeletePage.pdf';
51. let result = this.pdfDocument.saveDocument(outPdfPath);
52. hilog.info(0x0000, 'PdfPage', 'deletePage %{public}s!', result ? 'success' : 'fail');
53. })
54. }
55. }
56. }
```
