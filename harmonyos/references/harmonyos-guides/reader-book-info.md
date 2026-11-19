---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-book-info
title: 获取书籍信息
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容解析 > 获取书籍信息
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:11+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:bdf089de4938a634be99c56e4230e51e6890312125063e73a57bee7a3c9d6772
---

在导入本地书籍到书架时，开发者需通过[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)先将书籍文件导入到[应用沙箱目录](app-sandbox-directory.md)，然后利用解析能力获取书籍信息，包括书封、书名及作者等，以完成书架内容的展示。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/rlWWoGRqSBSuWOGmwqpufA/zh-cn_image_0000002820526571.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D7F5EAAD84388553E5163D28AA5CC7218FE57A154749D4D30B1AFC69D75881D)

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
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过提前导入到[应用沙箱目录](app-sandbox-directory.md)中的书籍文件，初始化书籍解析器。

   ```typescript
   private defaultHandler: bookParser.BookParserHandler | null = null;

   aboutToAppear(): void {
     this.init().then(() => {
     }).catch((error: BusinessError) => {
       hilog.error(0x0000, 'ReaderLog', `init failed, Code: ${error.code}, message: ${error.message}`);
     });
   }

   private async init() {
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let path: string = `${context.filesDir}/abc.epub`;
     try {
       this.defaultHandler = await bookParser.getDefaultHandler(path);
     } catch (error) {
       hilog.error(0x0000, "ReaderLog", `getDefaultHandler failed, Code: ${error.code}, message: ${error.message}`);
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
     }).catch((error: BusinessError) => {
       hilog.error(0x0000, 'ReaderLog', `init or getBookInfo failed, Code: ${error.code}, message: ${error.message}`);
     });
   }

   private async getBookInfo() {
     let imageSource: image.ImageSource | null = null;
     try {
       let bookInfo: bookParser.BookInfo | undefined = this.defaultHandler?.getBookInfo();
       if (bookInfo) {
         this.bookTitle = bookInfo.bookTitle || '';
         this.author = bookInfo?.bookCreator || '';
         let buffer = this.defaultHandler?.getResourceContent(-1, bookInfo.bookCoverImage);
         if (buffer) {
           imageSource = image.createImageSource(buffer);
           this.bookCover = await imageSource.createPixelMap();
         }
         hilog.info(0x0000, 'ReaderLog', 'getBookInfo bookInfo is: ' + JSON.stringify(bookInfo));
       }
     } catch (error) {
       hilog.error(0x0000, 'ReaderLog', `getBookInfo failed, Code: ${error.code}, message: ${error.message}`);
     } finally {
       if (imageSource) {
         imageSource.release();
       }
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
