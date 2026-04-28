---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-txt-img-annot
title: PDF页面文本、图片和批注
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > PDF页面文本、图片和批注
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf5585650b93e10f2ba6912a1dd0a06c0c1868cbfb99643fda7e43b44f834b46
---

支持编辑PDF页面内容，包括：

* 添加、删除文本。
* 添加、删除图片。
* 添加、修改、删除批注。

  通过索引指定PDF页面添加批注，并对批注在页面中的位置，字体、批注边框等设置，批注提供了多种风格样式，包括：文本批注[TextAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#textannotationinfo)、下划线批注[LineAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#lineannotationinfo)、高亮批注[HighlightAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#highlightannotationinfo)、删除线批注[StrikethroughAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#strikethroughannotationinfo)等共13种。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/m2KE9ueiQkmsVxuOFtdJ_Q/zh-cn_image_0000002583439147.png?HW-CC-KV=V1&HW-CC-Date=20260427T235019Z&HW-CC-Expire=86400&HW-CC-Sign=CDDBC9259F500D38B4C465CCB4048D70E0FAD50621A3B21C2A34C9B48B017707)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [addTextObject](../harmonyos-references/pdf-arkts-pdfservice.md#addtextobject)(text: string, x: number, y: number, style: TextStyle): void | 添加文本内容，只可按行添加。 |
| [addImageObject](../harmonyos-references/pdf-arkts-pdfservice.md#addimageobject)(path: string, x: number, y: number, width: number, height: number): void | 在PDF文档的页面中添加图片。 |
| [deleteGraphicsObject](../harmonyos-references/pdf-arkts-pdfservice.md#deletegraphicsobject)(object: GraphicsObject): void | 删除指定的GraphicsObject。 |
| [addAnnotation](../harmonyos-references/pdf-arkts-pdfservice.md#addannotation)(annotationInfo: PdfAnnotationInfo): PdfAnnotation | 在当前页添加批注。 |

## 添加文本和图片

1. 调用loadDocument方法，加载PDF文档。
2. 在【addText】按钮中调用addTextObject的方法插入文本。
3. 在【delText】按钮中调用deleteGraphicsObject方法来删除相应的页面文本。
4. 在【addImage】按钮中调用addImageObject的方法插入图片。

```
1. import { pdfService } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { Font } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct PdfPage {
8. private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
9. private context = this.getUIContext().getHostContext() as Context;

11. aboutToAppear(): void {
12. // 确保resfile目录有input.pdf文档
13. let filePath = this.context.resourceDir + '/input.pdf';
14. this.pdfDocument.loadDocument(filePath);
15. }

17. build() {
18. Column() {
19. // 添加文本
20. Button('addText').onClick(async () => {
21. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
22. let str = 'This is add text object!';
23. let fontInfo = new pdfService.FontInfo();
24. // 确保字体路径存在
25. let font: Font = new Font()
26. fontInfo.fontPath = font.getFontByName('HarmonyOS Sans')?.path;
27. fontInfo.fontName = '';
28. let style: pdfService.TextStyle = { textColor: 0x000000, textSize: 30, fontInfo: fontInfo };
29. page.addTextObject(str, 10, 10, style);
30. let outPdfPath = this.context.filesDir + '/testAddText.pdf';
31. let result = this.pdfDocument.saveDocument(outPdfPath);
32. hilog.info(0x0000, 'PdfPage', 'addText %{public}s!', result ? 'success' : 'fail');
33. })
34. // 删除文本
35. Button('delText').onClick(async () => {
36. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
37. let graphicsObjects = page.getGraphicsObjects();
38. // 找到第一个要删除的文本
39. let index = graphicsObjects.findIndex(item => item.type === pdfService.GraphicsObjectType.OBJECT_TEXT);
40. if (index > -1) {
41. // 删除第一个文本
42. page.deleteGraphicsObject(graphicsObjects[index]);
43. }
44. let outPdfPath = this.context.filesDir + '/testDelText.pdf';
45. let result = this.pdfDocument.saveDocument(outPdfPath);
46. hilog.info(0x0000, 'PdfPage', 'delText %{public}s!', result ? 'success' : 'fail');
47. })
48. // 添加图片
49. Button('addImage').onClick(async () => {
50. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
51. // 插入图片，确保resfile目录有img.jpg图片
52. let imagePath = this.context.resourceDir + '/img.jpg';
53. page.addImageObject(imagePath, 100, 100, 100, 120);
54. let outPdfPath = this.context.filesDir + '/testAddImage.pdf';
55. let result = this.pdfDocument.saveDocument(outPdfPath);
56. hilog.info(0x0000, 'PdfPage', 'addImage %{public}s!', result ? 'success' : 'fail');
57. })
58. }
59. }
60. }
```

## 添加文本批注

1. 调用loadDocument方法，加载PDF文档。
2. 调用getPage方法获取指定页。
3. 实例化TextAnnotationInfo文本批注，并设置相关属性。
4. 调用addAnnotation或setAnnotation方法添加或修改批注。
5. 调用removeAnnotation方法删除批注。

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
12. // 添加批注
13. Button('addTextAnnotation').onClick(async () => {
14. // 确保沙箱目录有input.pdf文档
15. let filePath = this.context.filesDir + '/input.pdf';
16. this.pdfDocument.loadDocument(filePath);
17. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
18. let aInfo = new pdfService.TextAnnotationInfo();
19. aInfo.iconName = 'Document';
20. aInfo.content = 'this is a content';
21. aInfo.subject = 'Annotation';
22. aInfo.title = 'this is a title';
23. aInfo.state = pdfService.TextAnnotationState.MARKED;
24. aInfo.x = 200;
25. aInfo.y = 200;
26. aInfo.color = 0xf9b1b1;
27. aInfo.flag = pdfService.AnnotationFlag.PRINTED;
28. let annotation: pdfService.PdfAnnotation = page.addAnnotation(aInfo);
29. let outPdfPath = this.context.filesDir + '/testAddTextAnnotation.pdf';
30. let result = this.pdfDocument.saveDocument(outPdfPath);
31. this.pdfDocument.releaseDocument();
32. hilog.info(0x0000, 'PdfPage', 'addTextAnnotation %{public}s!', result ? 'success' : 'fail');
33. })
34. // 修改批注
35. Button('setAnnotation').onClick(async () => {
36. let filePath = this.context.filesDir + '/testAddTextAnnotation.pdf';
37. let result = this.pdfDocument.loadDocument(filePath);
38. if (result === pdfService.ParseResult.PARSE_SUCCESS) {
39. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
40. let annotations = page.getAnnotations();
41. if (annotations.length > 0 && annotations[0].type === pdfService.AnnotationType.TEXT) {
42. let newAnno = annotations[0];
43. page.removeAnnotation(newAnno);
44. let annotation = page.addAnnotation(newAnno);
45. let newInfo = new pdfService.TextAnnotationInfo();
46. newInfo.title = "new Title";
47. newInfo.content = "new Info";
48. newInfo.state = pdfService.TextAnnotationState.MARKED;
49. newInfo.x = 100;
50. newInfo.y = 100;
51. page.setAnnotation(annotation, newInfo);
52. let outPdfPath = this.context.filesDir + '/testSetAnnotation.pdf';
53. let result = this.pdfDocument.saveDocument(outPdfPath);
54. this.pdfDocument.releaseDocument();
55. hilog.info(0x0000, 'PdfPage', 'setAnnotation %{public}s!', result ? 'success' : 'fail');
56. }
57. }
58. })
59. // 删除批注
60. Button('removeAnnotation').onClick(async () => {
61. let filePath = this.context.filesDir + '/testAddTextAnnotation.pdf';
62. let result = this.pdfDocument.loadDocument(filePath);
63. if (result === pdfService.ParseResult.PARSE_SUCCESS) {
64. let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
65. let annotations = page.getAnnotations();
66. if (annotations.length > 0 && annotations[0].type === pdfService.AnnotationType.TEXT) {
67. page.removeAnnotation(annotations[0]);
68. let outPdfPath = this.context.filesDir + '/testRemoveAnnotation.pdf';
69. let result = this.pdfDocument.saveDocument(outPdfPath);
70. this.pdfDocument.releaseDocument();
71. hilog.info(0x0000, 'PdfPage', 'removeAnnotation %{public}s!', result ? 'success' : 'fail');
72. }
73. }
74. })
75. }
76. }
77. }
```
