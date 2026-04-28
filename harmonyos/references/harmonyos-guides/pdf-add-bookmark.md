---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-bookmark
title: 添加、删除书签
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除书签
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0fbc44ba9e5d300ded4574d350e67ade49682f41b4fdd0939241ad1e6cb1741
---

PDF Kit支持添加和删除PDF文档书签。

添加书签时，可设置标题、颜色，是否粗体、斜体、跳转信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/MLdDQ49FT0edOVw2_QFg8g/zh-cn_image_0000002552959102.png?HW-CC-KV=V1&HW-CC-Date=20260427T235022Z&HW-CC-Expire=86400&HW-CC-Sign=2B1D18D324C4435DD0FF2E9E074C8722C5271B06584FA679D2F4C61D07F1B182)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [createBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#createbookmark)(): Bookmark | 创建PDF文档书签。 |
| [getRootBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#getrootbookmark)(): Bookmark | 获取PDF文档第一个根书签。 |
| [insertBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#insertbookmark)(bookmark: Bookmark, parent: Bookmark, position: number): boolean | 插入PDF文档书签。 |
| [setBookmarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#setbookmarkinfo)(info: BookmarkInfo): void | 设置书签信息。 |
| [removeBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#removebookmark)(bookmark: Bookmark): boolean | 移除PDF文档书签。 |
| [setDestInfo](../harmonyos-references/pdf-arkts-pdfservice.md#setdestinfo)(info: DestInfo): void | 设置书签的跳转信息。 |
| [getBookmarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#getbookmarkinfo)(): BookmarkInfo | 获取书签信息。 |

## 示例代码

**添加书签**：

1. 调用loadDocument方法，加载PDF文档。
2. 调用createBookmark方法，创建书签。
3. 调用setDestInfo方法，设置书签的跳转信息。
4. 调用getBookmarkInfo方法，获取书签信息。
5. 调用setBookmarkInfo方法，设置书签内容及样式。
6. 设置保存文档沙箱路径并保存

**删除书签**：

1. 调用loadDocument方法，加载PDF文档。
2. 调用getRootBookmark方法，获取文档的第一个根书签。
3. 调用removeBookmark方法，删除书签。
4. 设置保存文档沙箱路径并保存

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
12. // 添加书签
13. Button('addBookmark').onClick(async () => {
14. // 确保沙箱目录有input.pdf文档
15. let filePath = this.context.filesDir + '/input.pdf';
16. this.pdfDocument.loadDocument(filePath);
17. // 创建书签
18. let mark1: pdfService.Bookmark = this.pdfDocument.createBookmark();
19. let mark2: pdfService.Bookmark = this.pdfDocument.createBookmark();
20. // 设置书签的跳转信息
21. let destInfo: pdfService.DestInfo = mark1.getDestInfo();
22. destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
23. destInfo.pageIndex = 1;
24. destInfo.left = 20;
25. destInfo.top = 30;
26. destInfo.zoom = 1.5;
27. mark1.setDestInfo(destInfo);
28. // 设置书签内容及样式
29. let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
30. bookInfo.title = '这里是跳到第一页的书签';
31. bookInfo.titleColor = 12;
32. bookInfo.isBold = true;
33. bookInfo.isItalic = true;
34. mark1.setBookmarkInfo(bookInfo);
35. // 把创建的书签插入到PDF页面
36. this.pdfDocument.insertBookmark(mark1, null, 1);
37. this.pdfDocument.insertBookmark(mark2, mark1, 1);
38. // 设置保存文档沙箱路径并保存
39. let outPdfPath = this.context.filesDir + '/testAddBookmark.pdf';
40. let result = this.pdfDocument.saveDocument(outPdfPath);
41. hilog.info(0x0000, 'PdfPage', 'saveAddBookmark %{public}s!', result ? 'success' : 'fail');
42. })
43. // 删除书签
44. Button('removeBookmark').onClick(async () => {
45. // 确保沙箱目录有testAddBookmark.pdf文档
46. this.pdfDocument.loadDocument(this.context.filesDir + '/testAddBookmark.pdf');
47. let bookmarks: pdfService.Bookmark = this.pdfDocument.getRootBookmark();
48. if (bookmarks.isRootBookmark()) {
49. let hasRemoveBookmark: boolean = this.pdfDocument.removeBookmark(bookmarks);
50. hilog.info(0x0000, 'PdfPage', 'removeBookmark %{public}s!', hasRemoveBookmark ? 'success' : 'fail');
51. let outPdfPath = this.context.filesDir + '/testRemoveBookmark.pdf';
52. let result = this.pdfDocument.saveDocument(outPdfPath);
53. hilog.info(0x0000, 'PdfPage', 'saveRemoveBookmark %{public}s!', result ? 'success' : 'fail');
54. }
55. })
56. }
57. }
58. }
```
