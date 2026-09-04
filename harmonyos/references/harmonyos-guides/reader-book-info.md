---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-book-info
title: 获取书籍信息
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容解析 > 获取书籍信息
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cbd2262976fc157585ab3b9d9f47fe1bb7c0d815e336756286b66b5a16f766e4
---

在导入本地书籍到书架时，开发者需通过[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)先将书籍文件导入到[应用沙箱目录](app-sandbox-directory.md)，然后利用解析能力获取书籍信息，包括书封、书名及作者等，以完成书架内容的展示。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/P7Gqa5nHSnOoMp9-bGuC6g/zh-cn_image_0000002712245412.png)

## 接口说明

获取书籍信息共涉及3个接口，具体API说明请参考下表。

| 接口名 | 描述 |
| --- | --- |
| [getDefaultHandler](../harmonyos-references/reader-book-parser.md#getdefaulthandler)(path: string): Promise<BookParserHandler> | 获取书籍默认解析器。 |
| [getBookInfo](../harmonyos-references/reader-book-parser.md#getbookinfo)(): BookInfo | 获取书籍信息。 |
| [getResourceContent](../harmonyos-references/reader-book-parser.md#getresourcecontent)(spineIndex: number, filePath: string): ArrayBuffer | 获取书籍内容资源。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { bookParser } from '@kit.ReaderKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { image } from '@kit.ImageKit';
   ```
2. 通过提前导入到[应用沙箱目录](app-sandbox-directory.md)中的书籍文件，初始化书籍解析器。

   ```typescript
   private defaultHandler: bookParser.BookParserHandler | null = null;

   aboutToAppear(): void {
     this.init().then(() => {
     });
   }

   private async init() {
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let path: string = `${context.filesDir}/abc.epub`;
     try {
       this.defaultHandler = await bookParser.getDefaultHandler(path);
     } catch (error) {
       hilog.error(0x0000, "testTAG", `getDefaultHandler failed, Code: ${error.code}, message: ${error.message}`);
     }
   }
   ```
3. 获取书名、作者、书封信息并进行展示。

   ```typescript
   @State bookCover: PixelMap | null = null;
   @State bookTitle: string = '';
   @State author: string = '';

   aboutToAppear(): void {
     this.init().then(() => {
       this.getBookInfo();
     });
   }

   private async getBookInfo() {
     try {
       let bookInfo: bookParser.BookInfo | undefined = this.defaultHandler?.getBookInfo();
       if (bookInfo) {
         this.bookTitle = bookInfo.bookTitle || '';
         this.author = bookInfo?.bookCreator || '';
         let buffer = this.defaultHandler?.getResourceContent(-1, bookInfo.bookCoverImage);
         let imageSource: image.ImageSource = image.createImageSource(buffer);
         this.bookCover = await imageSource.createPixelMap();
         imageSource.release();
       }
       hilog.info(0x0000, 'testTAG', 'getBookInfo bookInfo is: ' + JSON.stringify(bookInfo));
     } catch (error) {
       hilog.error(0x0000, 'testTAG', `getBookInfo failed, Code: ${error.code}, message: ${error.message}`);
     }
   }

   build() {
     Column() {
       Text('书名：' + this.bookTitle)
         .fontSize(20)
         .fontColor("#E6000000")
         .margin({ top: 50 })
       Text('作者：' + this.author)
         .fontSize(20)
         .fontColor("#E6000000")
         .margin({ top: 10 })
       Image(this.bookCover)
         .width(200)
         .aspectRatio(3 / 4)
         .borderRadius(5)
         .margin({ top: 10 })
     }
     .alignItems(HorizontalAlign.Start)
     .margin({ left: 10, right: 10 })
   }
   ```
