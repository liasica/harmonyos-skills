---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-5
title: PdfView能否获取目录
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > PdfView能否获取目录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cf4b40a9d0c997a331dce2fa345c5d856ac473b3dc1e16fc454c487a91460e83
---

## 问题现象

如何实现PDF预览的时候需要展示所有的目录？PdfView能否获取目录信息？

## 背景知识

[PDF Kit（PDF服务）](../harmonyos-guides/pdf-kit-guide.md)包含pdfService和PdfView组件。差异可以参照[pdfService与PdfView能力比较](../harmonyos-guides/pdf-introduction.md#pdfservice与pdfview能力比较)。

* pdfService提供了加载和保存PDF文档、在PDF页面中添加文本内容、图片、批注、页眉页脚、水印、背景图片、书签、判断PDF文档是否加密及删除文档加密等相关功能，对PDF文档的操作有更多的应用场景。
* PdfView组件提供了文档预览功能，如：PDF文档预览、高亮显示、搜索关键字，批注等场景。

## 解决方案

PDF展示目录其实是PDF书签功能，PdfView目前不支持该能力，需要使用pdfService添加、查询书签，两者具体区别参考[pdfService与PdfView能力比较](../harmonyos-guides/pdf-introduction.md#pdfservice与pdfview能力比较)，使用示例如下：

1. 本地PDF文件复制到沙箱目录，在项目rawfile文件夹下添加test.pdf（本示例以多页PDF为例）：

   ```ts
   public async copyFile(fileName: string): Promise<void> {
     return new Promise((resolve, reject) => {
       let filePath = this.context.filesDir + '/' + fileName;
       try {
         if (!fileIo.accessSync(filePath)) {
           this.context.resourceManager.getRawFileContent(fileName, (_err, value) => {
             try {
               let myBuffer: ArrayBufferLike = value.buffer;
               let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
               let writeLen = fileIo.writeSync(file.fd, myBuffer);
               console.info(`write data to file succeed and size is:${writeLen}`);
               fileIo.closeSync(file);
               this.filePath = filePath;
               resolve();
             } catch (error) {
               reject(error);
             }
           });
         } else {
           this.filePath = filePath;
           resolve();
         }
       } catch (error) {
         reject(error);
       }
     });
   }
   ```
2. 给PDF增加书签（若原PDF自带书签可忽略步骤）：

   ```ts
   private createBookmarks() {
     // 创建书签
     let mark1: pdfService.Bookmark = this.pdfDocument.createBookmark();
     let mark2: pdfService.Bookmark = this.pdfDocument.createBookmark();
     // 设置书签的跳转信息
     let destInfo: pdfService.DestInfo = mark1.getDestInfo();
     destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
     destInfo.pageIndex = 1;
     destInfo.left = 20;
     destInfo.top = 30;
     destInfo.zoom = 1.5;
     mark1.setDestInfo(destInfo);
     // 设置书签内容及样式
     let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
     bookInfo.title = '这里是跳到第一页的书签';
     bookInfo.titleColor = 12;
     bookInfo.isBold = true;
     bookInfo.isItalic = true;
     mark1.setBookmarkInfo(bookInfo);
     // 把创建的书签插入到PDF页面
     this.pdfDocument.insertBookmark(mark1, null, 1);
     this.pdfDocument.insertBookmark(mark2, mark1, 1);
     // 设置保存文档沙箱路径并保存
     this.outPdfPath = this.context.filesDir + '/testAddBookmark.pdf';
     let result = this.pdfDocument.saveDocument(this.outPdfPath);
     hilog.info(0x0000, 'PdfPage', 'saveAddBookmark %{public}s!', result ? 'success' : 'fail');
   }
   ```
3. 完整示例如下：

   ```ts
   import { pdfService } from '@kit.PDFKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   @Component
   @Entry
   struct PdfGetDirectory {
     @State filePath: string = '';
     @State outPdfPath: string = '';
     private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
     private context = this.getUIContext().getHostContext() as Context;

     build() {
       Column() {
         Button('创建PDF书签')
           .width(200)
           .margin({ top: 100 })
           .onClick(async () => {
             await this.copyFile('test.pdf'); // 此处仅为示例，请开发者替换为实际使用的文件。
             let loadResult = this.pdfDocument.loadDocument(this.filePath, '');
             if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
               // 创建书签
               this.createBookmarks();
             }
           });
         Button('查询PDF书签')
           .width(200)
           .margin({ top: 100 })
           .onClick(() => {
             // 确保加载的是保存了书签的文件
             let loadResult = this.pdfDocument.loadDocument(this.outPdfPath, '');
             if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
               this.verifyBookmarks();
             } else {
               console.error('加载PDF文件失败: ' + loadResult);
             }
           });
       }
       .width('100%')
       .height('100%');
     }
     private createBookmarks() {
       // 创建书签
       let mark1: pdfService.Bookmark = this.pdfDocument.createBookmark();
       let mark2: pdfService.Bookmark = this.pdfDocument.createBookmark();
       // 设置书签的跳转信息
       let destInfo: pdfService.DestInfo = mark1.getDestInfo();
       destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
       destInfo.pageIndex = 1;
       destInfo.left = 20;
       destInfo.top = 30;
       destInfo.zoom = 1.5;
       mark1.setDestInfo(destInfo);
       // 设置书签内容及样式
       let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
       bookInfo.title = '这里是跳到第一页的书签';
       bookInfo.titleColor = 12;
       bookInfo.isBold = true;
       bookInfo.isItalic = true;
       mark1.setBookmarkInfo(bookInfo);
       // 把创建的书签插入到PDF页面
       this.pdfDocument.insertBookmark(mark1, null, 1);
       this.pdfDocument.insertBookmark(mark2, mark1, 1);
       // 设置保存文档沙箱路径并保存
       this.outPdfPath = this.context.filesDir + '/testAddBookmark.pdf';
       let result = this.pdfDocument.saveDocument(this.outPdfPath);
       hilog.info(0x0000, 'PdfPage', 'saveAddBookmark %{public}s!', result ? 'success' : 'fail');
     }
     private verifyBookmarks() {
       // 重新加载并验证书签
       let loadResult = this.pdfDocument.loadDocument(this.outPdfPath, '');
       if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
         let rootBookmark = this.pdfDocument.getRootBookmarks();
         if (rootBookmark.length > 0) {
           console.info('验证书签: ' + JSON.stringify(rootBookmark[0].getBookmarkInfo()));
         } else {
           console.info('验证无书签');
         }
       }
     }
     public async copyFile(fileName: string): Promise<void> {
       return new Promise((resolve, reject) => {
         let filePath = this.context.filesDir + '/' + fileName;
         try {
           if (!fileIo.accessSync(filePath)) {
             this.context.resourceManager.getRawFileContent(fileName, (_err, value) => {
               try {
                 let myBuffer: ArrayBufferLike = value.buffer;
                 let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
                 let writeLen = fileIo.writeSync(file.fd, myBuffer);
                 console.info(`write data to file succeed and size is:${writeLen}`);
                 fileIo.closeSync(file);
                 this.filePath = filePath;
                 resolve();
               } catch (error) {
                 reject(error);
               }
             });
           } else {
             this.filePath = filePath;
             resolve();
           }
         } catch (error) {
           reject(error);
         }
       });
     }
   }
   ```

## 常见FAQ

Q：pdfService和PdfView一起使用对内存会有影响吗？

A：不会增加很多内存，如果想查询应用内存限制，可以参考[hidebug.getAppMemoryLimit](../harmonyos-references/js-apis-hidebug.md#hidebuggetappmemorylimit12)接口。
