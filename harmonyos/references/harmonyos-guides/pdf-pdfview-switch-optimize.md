---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-switch-optimize
title: 优化PDF文档切换体验
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 优化PDF文档切换体验
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e9c632a7a1152d0de0fcfe6018bf734a912cba8168fda4129161a742742861b5
---

## 场景介绍

在应用中进行多文档切换时，为了提供更加流畅和清晰的视觉体验，推荐结合状态管理来控制PdfView的渲染时机。

通过引入加载状态，可以在文档加载过程中暂时隐藏预览组件并展示加载动画，待loadDocument异步加载完成且页面布局准备就绪后，再展示清晰的文档内容。这种方式能有效优化切换过程中的视觉跳变，提升交互质感。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadDocument](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument)(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult> | 加载PDF文档。 |
| [setPageFit](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagefit)(pageFit: pdfService.PageFit): void | 设置页面的适配模式。 |

## 示例代码

1. 定义@State变量isLoading，用于标记文档的加载状态，并以此控制PdfView组件的挂载与显示。
2. 将isLoading置为true，显示Loading界面；待异步加载成功后，再将isLoading置为false，展示PDF视图。
3. 通过调用loadDocument加载不同的文件路径，实现PDF文件的切换。

```
1. import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@ohos.base';

6. const DOMAIN: number = 0x0000;
7. const TAG: string = 'SwitchDocumentDemo';

9. @Entry
10. @Component
11. struct Index {
12. private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
13. private filePath1: string = '';
14. private filePath2: string = '';
15. private switchFlag: boolean = true; // true，加载pdf1；false，加载pdf2
16. @State isLoading: boolean = false;

18. private makeSureFileExist(filePath: string): void {
19. let fileName: string = filePath.split('/').pop() || '';
20. try {
21. let context = this.getUIContext().getHostContext() as Context;
22. let res = fileIo.accessSync(filePath);
23. if (!res) {
24. let content: Uint8Array = context.resourceManager.getRawFileContentSync(`rawfile/${fileName}`);
25. let fdSand =
26. fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
27. fileIo.writeSync(fdSand.fd, content.buffer);
28. fileIo.closeSync(fdSand.fd);
29. }
30. } catch (e) {
31. let error: BusinessError = e as BusinessError;
32. hilog.error(DOMAIN, TAG, `Code: ${error.code}, message: ${error.message} `);
33. }
34. }

36. aboutToAppear(): void {
37. let context = this.getUIContext().getHostContext() as Context;
38. let dir: string = context.filesDir
39. // 确保沙箱目录内有pdf1.pdf、pdf2.pdf文档
40. this.filePath1 = dir + '/pdf1.pdf';
41. this.filePath2 = dir + '/pdf2.pdf';
42. this.makeSureFileExist(this.filePath1);
43. this.makeSureFileExist(this.filePath2);

45. (async () => {
46. let filePath: string = this.switchFlag ? this.filePath1 : this.filePath2;
47. this.isLoading = true;
48. let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
49. this.isLoading = false;
50. if (loadResult !== pdfService.ParseResult.PARSE_SUCCESS) {
51. hilog.error(DOMAIN, TAG, 'Controller load PDF failed');
52. return;
53. }
54. })();
55. }

57. build() {
58. Stack({ alignContent: Alignment.TopStart }) {
59. if (!this.isLoading) {
60. PdfView({
61. controller: this.controller,
62. pageFit: pdfService.PageFit.FIT_WIDTH,
63. showScroll: false
64. })
65. .width('100%')
66. .height('100%')
67. } else {
68. // 此处可自定义loading界面
69. }
70. Row() {
71. Button('SwitchDocument')
72. .onClick(async () => {
73. this.switchFlag = !this.switchFlag;
74. let filePath: string = this.switchFlag ? this.filePath1 : this.filePath2;
75. this.controller.releaseDocument();
76. this.isLoading = true;
77. let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
78. this.isLoading = false;
79. if (loadResult !== pdfService.ParseResult.PARSE_SUCCESS) {
80. hilog.error(DOMAIN, TAG, 'Controller load PDF failed');
81. return;
82. }
83. this.controller.setPageFit(pdfService.PageFit.FIT_WIDTH);
84. })
85. }
86. }
87. .height('100%')
88. .width('100%')
89. }
90. }
```
