---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-book-info
title: 获取书籍信息
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容解析 > 获取书籍信息
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:761b620925909deecc40c117fd25a422c1bd350be2cfed9bec5c35f91c05fa42
---

在导入本地书籍到书架时，开发者需通过[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)先将书籍文件导入到[应用沙箱目录](app-sandbox-directory.md)，然后利用解析能力获取书籍信息，包括书封、书名及作者等，以完成书架内容的展示。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/prLOxflVSXKJ_rw2VQ9fLQ/zh-cn_image_0000002589245451.png?HW-CC-KV=V1&HW-CC-Date=20260429T054001Z&HW-CC-Expire=86400&HW-CC-Sign=415324472091CF2605851D3A4440CA943C3131101E549C5822107E344B721690)

## 接口说明

获取书籍信息共涉及3个接口，具体API说明请参考下表。

| 接口名 | 描述 |
| --- | --- |
| [getDefaultHandler](../harmonyos-references/reader-book-parser.md#getdefaulthandler)(path: string): Promise<BookParserHandler> | 获取书籍默认解析器。 |
| [getBookInfo](../harmonyos-references/reader-book-parser.md#getbookinfo)(): BookInfo | 获取书籍信息。 |
| [getResourceContent](../harmonyos-references/reader-book-parser.md#getresourcecontent)(spineIndex: number, filePath: string): ArrayBuffer | 获取书籍内容资源。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { bookParser } from '@kit.ReaderKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { image } from '@kit.ImageKit';
   ```
2. 通过提前导入到[应用沙箱目录](app-sandbox-directory.md)中的书籍文件，初始化书籍解析器。

   ```
   1. private defaultHandler: bookParser.BookParserHandler | null = null;

   3. aboutToAppear(): void {
   4. this.init().then(() => {
   5. });
   6. }

   8. private async init() {
   9. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   10. let path: string = `${context.filesDir}/abc.epub`;
   11. try {
   12. this.defaultHandler = await bookParser.getDefaultHandler(path);
   13. } catch (error) {
   14. hilog.error(0x0000, "testTAG", `getDefaultHandler failed, Code: ${error.code}, message: ${error.message}`);
   15. }
   16. }
   ```
3. 获取书名、作者、书封信息并进行展示。

   ```
   1. @State bookCover: PixelMap | null = null;
   2. @State bookTitle: string = '';
   3. @State author: string = '';

   5. aboutToAppear(): void {
   6. this.init().then(() => {
   7. this.getBookInfo();
   8. });
   9. }

   11. private async getBookInfo() {
   12. try {
   13. let bookInfo: bookParser.BookInfo | undefined = this.defaultHandler?.getBookInfo();
   14. if (bookInfo) {
   15. this.bookTitle = bookInfo.bookTitle || '';
   16. this.author = bookInfo?.bookCreator || '';
   17. // SpineIndex is not required for obtaining the book cover.
   18. let buffer = this.defaultHandler?.getResourceContent(-1, bookInfo.bookCoverImage);
   19. let imageSource: image.ImageSource = image.createImageSource(buffer);
   20. this.bookCover = await imageSource.createPixelMap();
   21. imageSource.release();
   22. }
   23. hilog.info(0x0000, 'testTAG', 'getBookInfo bookInfo is: ' + JSON.stringify(bookInfo));
   24. } catch (error) {
   25. hilog.error(0x0000, 'testTAG', `getBookInfo failed, Code: ${error.code}, message: ${error.message}`);
   26. }
   27. }

   29. build() {
   30. Column() {
   31. Text('书名：' + this.bookTitle)
   32. .fontSize(20)
   33. .fontColor("#E6000000")
   34. .margin({ top: 50 })
   35. Text('作者：' + this.author)
   36. .fontSize(20)
   37. .fontColor("#E6000000")
   38. .margin({ top: 10 })
   39. Image(this.bookCover)
   40. .width(200)
   41. .aspectRatio(3 / 4)
   42. .borderRadius(5)
   43. .margin({ top: 10 })
   44. }
   45. .alignItems(HorizontalAlign.Start)
   46. .margin({ left: 10, right: 10 })
   47. }
   ```
