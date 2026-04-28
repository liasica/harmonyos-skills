---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-annotation
title: 批注
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 批注
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:623cd3ecad844e307e6a2d8e7d539197155e7ff8462d7fd604b972765fd6de28
---

进入批注模式，目前支持高亮、下划线和删除线类型批注。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [enableAnnotation](../harmonyos-references/pdf-arkts-pdfviewmanage.md#enableannotation)(annotationType: SupportedAnnotationType, color?: number): void | 在常用操作之间切换并添加批注。 |

## 示例代码

1. 先加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 调用enableAnnotation方法，进入批注模式。

```
1. import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

3. @Entry
4. @Component
5. struct PdfPage {
6. private pdfController = new pdfViewManager.PdfController();
7. private context = this.getUIContext().getHostContext() as Context;

9. aboutToAppear(): void {
10. // 确保沙箱目录有input.pdf文档
11. let filePath = this.context.filesDir + '/input.pdf';
12. (async () => {
13. let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
14. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
15. // 添加删除线批注
16. this.pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAEEEEEE);
17. }
18. })()
19. }

21. build() {
22. Column() {
23. // 加载PdfView组件进行预览
24. PdfView({
25. controller: this.pdfController,
26. pageFit: pdfService.PageFit.FIT_WIDTH,
27. showScroll: true
28. })
29. .id('pdfview_app_view')
30. .layoutWeight(1);
31. }
32. }
33. }
```
