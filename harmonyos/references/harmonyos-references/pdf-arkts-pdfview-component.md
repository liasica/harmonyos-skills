---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfview-component
title: PdfView（PDF预览组件）
breadcrumb: API参考 > 应用服务 > PDF Kit（PDF服务） > ArkTS组件 > PdfView（PDF预览组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b23b61e086ac94f16108039ea7979629943dc5b6ecf6d5a8095245640a57b6ad
---

本模块提供PdfView组件，HarmonyOS应用通过集成该组件完成PDF文件的预览功能。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';
```

## PdfView

PhonePC/2in1Tablet

该类是用来展示PDF文档预览的UI组件。

**装饰器类型：** @Component

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | pdfViewManager.[PdfController](pdf-arkts-pdfviewmanage.md#pdfcontroller) | 否 | 否 | PdfView组件控制器。 |
| pageLayout | pdfService.[PageLayout](pdf-arkts-pdfservice.md#pagelayout) | 否 | 否 | 页面布局显示模式。 |
| isContinuous | boolean | 否 | 否 | 是否连续预览，true：是，false：否。 |
| showScroll | boolean | 否 | 否 | 是否显示滚动条，true：显示，false：隐藏。 |
| pageFit | pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit) | 否 | 否 | 页面适配模式。 |

### build

PhonePC/2in1Tablet

build(): void

用于创建[PdfView](pdf-arkts-pdfview-component.md#pdfview)对象的构造函数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

10. aboutToAppear(): void {
11. let context = this.getUIContext().getHostContext() as Context;
12. let dir: string = context.filesDir
13. // 确保在工程目录src/main/resources/rawfile里存在input.pdf文档
14. let filePath: string = dir + '/input.pdf';
15. let res = fileIo.accessSync(filePath);
16. if (!res) {
17. let content: Uint8Array = context.resourceManager.getRawFileContentSync('rawfile/input.pdf');
18. let fdSand =
19. fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
20. fileIo.writeSync(fdSand.fd, content.buffer);
21. fileIo.closeSync(fdSand.fd);
22. }
23. (async () => {
24. // 该监听方法只能在文档加载前调用一次
25. this.controller.registerPageCountChangedListener((pageCount: number) => {
26. hilog.info(0x0000, 'registerPageCountChanged-', pageCount.toString());
27. });
28. let loadResult1: pdfService.ParseResult = await this.controller.loadDocument(filePath);
29. // 注意：这里刚加载文档，请不要在这里立即设置PDF文档的预览方式
30. })()
31. }

33. build() {
34. Row() {
35. PdfView({
36. controller: this.controller,
37. pageFit: pdfService.PageFit.FIT_WIDTH,
38. showScroll: true
39. })
40. .id('pdfview_app_view')
41. .layoutWeight(1);
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```
