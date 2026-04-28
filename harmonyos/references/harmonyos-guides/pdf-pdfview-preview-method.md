---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-preview-method
title: 设置PDF文档预览效果
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 设置PDF文档预览效果
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2c3dcdb83bcfa543d9dab5833dfbc47ed5c3c6f6d710d13c4af03cf080f63cdf
---

pdfViewManager为PDF文档提供了丰富的预览特性。

* 单双页布局，是否连续滚动和页面适配方式。
* 页面跳转，如上一页，下一页，跳转到指定页。
* 页面放大、缩小。

**图1**：提供了双页预览布局，页面宽度适配和连续滚动的预览方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/ZBmGmrZhTNyTuu4bOZe8lQ/zh-cn_image_0000002552959104.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235022Z&HW-CC-Expire=86400&HW-CC-Sign=E1F1D0F27621698114B1D7A7236240D765F69A806CE4F4F38895B5F4EA5A03BB)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [setPageLayout](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagelayout)(columnCount: pdfService.PageLayout): void | 设置页面布局模式。其中“columnCount”取值如下：  - 1：单页面  - 2：双页面 |
| [setPageContinuous](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagecontinuous)(isContinuous: boolean): void | 设置页面滚动是否连续排列。 |
| [setPageFit](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagefit)(pageFit: pdfService.PageFit): void | 设置页面的适配模式。 |
| [goToPage](../harmonyos-references/pdf-arkts-pdfviewmanage.md#gotopage)(pageIndex: number): void | 跳转到指定页。 |
| [setPageZoom](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagezoom)(zoom: number): void | 设置视图的缩放比例。 |

## 示例代码

1. 先加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在按钮【setPreviewMode】里，调用setPageLayout、setPageContinuous等方法，设置文档预览效果。
4. 在按钮【goTopage】里，调用goToPage方法，设置页面跳转。
5. 在按钮【zoomPage2】里，调用setPageZoom方法，将页面放大2倍。

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
15. // 注意：这里刚加载文档，请不要在这里立即设置PDF文档的预览方法。
16. })()
17. }

19. build() {
20. Column() {
21. Row() {
22. // 设置预览方式
23. Button('setPreviewMode').onClick(() => {
24. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
25. // 单页布局
26. this.controller.setPageLayout(pdfService.PageLayout.LAYOUT_SINGLE);
27. // 是否连续滚动预览
28. this.controller.setPageContinuous(true);
29. // 适配页的预览方式
30. this.controller.setPageFit(pdfService.PageFit.FIT_PAGE);
31. }
32. })
33. // 跳转到第11页
34. Button('goTopage').onClick(() => {
35. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
36. this.controller.goToPage(10);
37. }
38. })
39. // 页面放大2倍
40. Button('zoomPage2').onClick(() => {
41. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
42. this.controller.setPageZoom(2);
43. }
44. })
45. }

47. PdfView({
48. controller: this.controller,
49. pageFit: pdfService.PageFit.FIT_WIDTH,
50. showScroll: true
51. })
52. .id('pdfview_app_view')
53. .layoutWeight(1);
54. }
55. }
56. }
```
