---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-search
title: 搜索关键字
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 搜索关键字
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:47+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0e20232e9ae829eb3c5b76d256a9b7fa3433d52c554fb540ba7334a7a2985ce8
---

预览PDF文档时，可以对页面的关键词（英文字符不区分大小写）进行搜索并高亮显示，同时使用[setSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setsearchindex)方法高亮显示指定的搜索结果。

使用[getSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#getsearchindex)方法获取当前高亮的索引，可以使用[clearSearch](../harmonyos-references/pdf-arkts-pdfviewmanage.md#clearsearch)方法清除所有搜索结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/jL9U4JuITrqvJFJU9rhgpw/zh-cn_image_0000002558765606.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053946Z&HW-CC-Expire=86400&HW-CC-Sign=D71E69CFF5D803AC80A7C1345F74A6A89C4403EA9593D4D98F9CA8437300D193)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [searchKey](../harmonyos-references/pdf-arkts-pdfviewmanage.md#searchkey)(text: string, listener: Callback<number>): void | 搜索文本并返回匹配的总数。 |
| [clearSearch](../harmonyos-references/pdf-arkts-pdfviewmanage.md#clearsearch)(): void | 清除搜索文本的高亮，等价于搜索空字符串 。 |
| [setSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setsearchindex)(index: number): void | 设置搜索匹配结果的索引，页面会跳转到索引对应搜索结果处。 |
| [getSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#getsearchindex)(): number | 获取当前命中搜索关键字匹配结果的索引，执行搜索接口后默认命中索引为0。 |

## 示例代码

1. 先加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在按钮【searchKey】里，调用searchKey方法，搜索指定关键字。
4. 上一个、下一个搜索按钮跳转到对应的结果。
5. 在按钮【getSearchIndex】里，调用getSearchIndex方法，获取当前的搜索结果索引。
6. 在按钮【clearSearch】里，调用clearSearch方法，清除搜索结果。

```
1. import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
8. private context = this.getUIContext().getHostContext() as Context;
9. private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;
10. private searchIndex = 0;
11. private charCount = 0;

13. aboutToAppear(): void {
14. // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
15. let filePath = this.context.resourceDir + '/input.pdf';
16. (async () => {
17. this.loadResult = await this.controller.loadDocument(filePath);
18. })()
19. }

21. build() {
22. Column() {
23. Scroll() {
24. Row() {
25. // 搜索关键字
26. Button('searchKey').onClick(async () => {
27. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
28. this.controller.searchKey('C++', (index: number) => {
29. this.charCount = index;
30. hilog.info(0x0000, 'PdfPage', 'searchKey %{public}s!', index + '');
31. })
32. }
33. })
34. .width(100)
35. // 上一个
36. Button('setSearchPrevIndex').onClick(async () => {
37. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
38. if(this.searchIndex > 0) {
39. this.controller.setSearchIndex(--this.searchIndex);
40. }
41. }
42. })
43. .width(200)
44. // 下一个
45. Button('setSearchNextIndex').onClick(async () => {
46. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
47. if(this.searchIndex < this.charCount) {
48. this.controller.setSearchIndex(++this.searchIndex);
49. }
50. }
51. })
52. .width(200)
53. // 获取当前页索引
54. Button('getSearchIndex').onClick(async () => {
55. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
56. let curSearchIndex = this.controller.getSearchIndex();
57. hilog.info(0x0000, 'PdfPage', 'curSearchIndex %{public}s!', curSearchIndex + '');
58. }
59. })
60. .width(150)
61. // 清除搜索文本的高亮
62. Button('clearSearch').onClick(async () => {
63. if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
64. this.controller.clearSearch();
65. }
66. })
67. .width(150)
68. }
69. }
70. .scrollable(ScrollDirection.Horizontal)

72. PdfView({
73. controller: this.controller,
74. pageFit: pdfService.PageFit.FIT_WIDTH,
75. showScroll: true
76. })
77. .id('pdfview_app_view')
78. .layoutWeight(1);
79. }
80. }
81. }
```
