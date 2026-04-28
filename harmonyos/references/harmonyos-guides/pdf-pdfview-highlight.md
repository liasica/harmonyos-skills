---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-highlight
title: 高亮显示PDF文档
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 高亮显示PDF文档
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6d375095cecd682de54a6b159fe7458d020bdd4d28ff47d2161c3b5e71135e0
---

PDF文档在预览时，可以对页面的矩形区域或文本设置高亮显示，高亮颜色可以自定义。

[setHighlightText](../harmonyos-references/pdf-arkts-pdfviewmanage.md#sethighlighttext)可以同时高亮多个不同的文本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ZU2LQDAER5izK_X4U3zGUg/zh-cn_image_0000002552799456.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235023Z&HW-CC-Expire=86400&HW-CC-Sign=EF82F10C89DBA909FB1CFEFB75AC9BB31E00F8006D0D9C062B5D7B215AECB75A)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [setHighlightText](../harmonyos-references/pdf-arkts-pdfviewmanage.md#sethighlighttext)(pageIndex: number, textArray: string[], color: number): void | 高亮指定文本。 |

注意

[setHighlightText](../harmonyos-references/pdf-arkts-pdfviewmanage.md#sethighlighttext)和[searchKey](../harmonyos-references/pdf-arkts-pdfviewmanage.md#searchkey)功能互斥。

## 示例代码

1. 加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在按钮【setHighlightText】里，调用setHighlightText方法，设置单个或多个要高亮的文本。

```
1. import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';

3. @Entry
4. @Component
5. struct PdfPage {
6. private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
7. private context = this.getUIContext().getHostContext() as Context;
8. private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

10. aboutToAppear(): void {
11. // 确保沙箱目录有input.pdf文档
12. let filePath = this.context.filesDir + '/input.pdf';
13. (async () => {
14. this.loadResult = await this.controller.loadDocument(filePath);
15. })()
16. }

18. build() {
19. Column() {
20. Row() {
21. // 设置文本的高亮显示风格
22. Button('setHighlightText').onClick(async () => {
23. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
24. this.controller.setHighlightText(0, ['白皮书'], 0xAAF9CC00);
25. }
26. })
27. }

29. // 加载PdfView组件进行预览
30. PdfView({
31. controller: this.controller,
32. pageFit: pdfService.PageFit.FIT_WIDTH,
33. showScroll: true
34. })
35. .id('pdfview_app_view')
36. .layoutWeight(1);
37. }
38. .width('100%').height('100%')
39. }
40. }
```
