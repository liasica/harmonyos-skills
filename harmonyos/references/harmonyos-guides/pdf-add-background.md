---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-background
title: 添加、删除背景
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除背景
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4dbf8d45a8d9d4c26462165f2b1e5d4df61d622c4ba6767b701cecf0c2b568d1
---

对指定页面添加背景图片或背景颜色，并设置大小、旋转、透明度和位置等属性，支持图片格式：PNG、BMP、JPEG。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/WGMU1QjyS-mUtYpOydZYXQ/zh-cn_image_0000002583439149.png?HW-CC-KV=V1&HW-CC-Date=20260427T235022Z&HW-CC-Expire=86400&HW-CC-Sign=6B880E54D4ECF91420B9850DB40F56CD443D371EE66DEACDBF3681C9F5535C29)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [addBackground](../harmonyos-references/pdf-arkts-pdfservice.md#addbackground)(info: BackgroundInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void | 插入PDF文档背景。 |
| [removeBackground](../harmonyos-references/pdf-arkts-pdfservice.md#removebackground)(): boolean | 删除PDF文档背景。 |

注意

[addBackground](../harmonyos-references/pdf-arkts-pdfservice.md#addbackground)方法属于耗时业务，需要遍历每一页去添加背景，添加页面较多时建议放到线程里去处理。

## 示例代码

**添加背景：**

1. 调用loadDocument方法，加载PDF文档。
2. 实例化背景BackgroundInfo类，并设置相关属性，包括大小、旋转、透明度和位置等。
3. 调用addBackground方法，添加背景。
4. 保存PDF文档到应用沙箱。

**删除背景：**

1. 调用loadDocument方法，加载PDF文档。
2. 调用removeBackground方法，去除背景。
3. 保存PDF文档到应用沙箱。

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
12. Button('addBackground').onClick(async () => {
13. // 确保沙箱目录有input.pdf文档
14. let filePath = this.context.filesDir + '/input.pdf';
15. let res = this.pdfDocument.loadDocument(filePath);
16. if (res === pdfService.ParseResult.PARSE_SUCCESS) {
17. let bginfo: pdfService.BackgroundInfo = new pdfService.BackgroundInfo();
18. // 确保沙箱目录有img.jpg文档
19. bginfo.imagePath = this.context.filesDir + '/img.jpg';
20. bginfo.backgroundColor = 50;
21. bginfo.isOnTop = true;
22. bginfo.rotation = 45;
23. bginfo.scale = 0.5;
24. bginfo.opacity = 0.3;
25. bginfo.verticalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_TOP;
26. bginfo.horizontalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_LEFT;
27. bginfo.horizontalSpace = 1.0;
28. bginfo.verticalSpace = 1.0;
29. this.pdfDocument.addBackground(bginfo, 0, 2, true, true);
30. let outPdfPath = this.context.filesDir + '/testAddBackground.pdf';
31. let result = this.pdfDocument.saveDocument(outPdfPath);
32. hilog.info(0x0000, 'PdfPage', 'addBackground %{public}s!', result ? 'success' : 'fail');
33. }
34. this.pdfDocument.releaseDocument();
35. })
36. Button('removeBackground').onClick(async () => {
37. let filePath = this.context.filesDir + '/testAddBackground.pdf';
38. let res = this.pdfDocument.loadDocument(filePath);
39. if (res === pdfService.ParseResult.PARSE_SUCCESS && this.pdfDocument.hasBackground()) {
40. let removeResult = this.pdfDocument.removeBackground();
41. if (removeResult) {
42. let outPdfPath = this.context.filesDir + '/removeBackground.pdf';
43. let result = this.pdfDocument.saveDocument(outPdfPath);
44. hilog.info(0x0000, 'PdfPage', 'removeBackground %{public}s!', result ? 'success' : 'fail');
45. }
46. }
47. this.pdfDocument.releaseDocument();
48. })
49. }
50. }
51. }
```
