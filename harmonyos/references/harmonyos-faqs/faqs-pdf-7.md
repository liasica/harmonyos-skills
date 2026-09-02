---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-7
title: 如何将不同尺寸的图片添加到PDF里
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 如何将不同尺寸的图片添加到PDF里
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:16bb77e8f3e99af4278b8b14b71eb89e73530da07c9329ada4146a7399293f2b
---

## 问题现象

如何将不同尺寸的图片添加到PDF里？创建PDF文件时，createDocument(width: number, height: number)如果宽高定的过小会导致尺寸大一点的图片显示不全。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/KZznVyhwT8iMEooxQvHIjw/zh-cn_image_0000002628394348.png "点击放大")

## 背景知识

* [fs.listFileSync](../harmonyos-references/js-apis-file-fs.md#fileiolistfilesync)：默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。
* [getImageInfoSync](../harmonyos-references/arkts-apis-image-pixelmap.md#getimageinfosync12)：以同步方法获取图像像素信息。
* [createDocument](../harmonyos-references/pdf-arkts-pdfservice.md#createdocument)：创建空白文档。
* [insertBlankPage](../harmonyos-references/pdf-arkts-pdfservice.md#insertblankpage)：在指定位置插入PDF页。
* [addImageObject](../harmonyos-references/pdf-arkts-pdfservice.md#addimageobject)：在PDF文档的页面中添加图片。
* [saveDocument](../harmonyos-references/pdf-arkts-pdfservice.md#savedocument)：保存文档。

## 解决方案

以将context.filesDir目录下图片添加到PDF为例。

1. 引入相关kit。

   ```ts
   import { common } from '@kit.AbilityKit';
   import { fileIo as fs, ListFileOptions } from '@kit.CoreFileKit';
   import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
   import { image } from '@kit.ImageKit';
   import { ArrayList } from '@kit.ArkTS';
   import { systemDateTime } from '@kit.BasicServicesKit';
   ```
2. 声明全局变量。

   ```ts
   private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
   private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   ```
3. 使用PdfView组件展示PDF文件。

   ```ts
   PdfView({
     controller: this.controller,
     pageFit: pdfService.PageFit.FIT_PAGE,
     showScroll: false
   })
     .height('90%')
     .width('90%')
     .id('pdfview_app_view')
     .borderWidth(0)
     .layoutWeight(1);
   ```
4. 构造ImgInfo类。

   ```ts
   export class ImgInfo {
     path: string = '';
     width: number = 0;
     height: number = 0;
   }
   ```
5. 创建PDF文件。
   * 以所有图片中的最大宽高创建PDF文件。

     ```ts
     Button('根据所有图片中的最大宽高值创建PDF文件').onClick(async () => {
       // 获取目录下所有图片中的最大宽高值，并记录每张图片的路径、宽高（保证该沙箱目录下有对应格式图片）
       let dir: string = this.context.filesDir;
       let listFileOption: ListFileOptions = {
         recursion: false,
         listNum: 0,
         filter: {
           suffix: ['.png', '.jpg', '.jpeg']
         }
       };
       let imgInfoList: ArrayList<ImgInfo> = new ArrayList();
       let maxImgWidthNum: number = 0;
       let maxImgHeightNum: number = 0;
       let filenames = fs.listFileSync(dir, listFileOption);
       if (filenames.length <= 0) {
         console.info('no file be found');
         return;
       }
       // 遍历出目录下的图片文件
       for (let i = 0; i < filenames.length; i++) {
         console.info('filename: %s', filenames[i]);
         let imageSource = image.createImageSource(dir + '/' + filenames[i]);
         let imageInfo = imageSource.getImageInfoSync(0);
         // 记录图片路径、宽高信息
         let img = new ImgInfo();
         img.path = dir + '/' + filenames[i];
         img.width = imageInfo.size.width;
         img.height = imageInfo.size.height;
         imgInfoList.add(img);
         // 更新宽高最大值
         if (imageInfo.size.height > maxImgHeightNum) {
           maxImgHeightNum = imageInfo.size.height;
         }
         if (imageInfo.size.width > maxImgWidthNum) {
           maxImgWidthNum = imageInfo.size.width;
         }
       }

       // 创建PDF文件时以获取到的图片最大宽高值作为PDF文件的宽高，根据记录下来的图片信息调用addImageObject将图片添加到PDF中，并保存PDF文件
       let pdfDocument = new pdfService.PdfDocument();
       // 创建PDF文件，宽高为获取到的图片最大宽高值
       pdfDocument.createDocument(maxImgWidthNum, maxImgHeightNum);
       for (let index = 0; index < imgInfoList.length; index++) {
         let pdfPage: pdfService.PdfPage | undefined;
         if (index > 0) {
           // 插入空白页
           pdfDocument.insertBlankPage(index, maxImgWidthNum, maxImgHeightNum);
         }
         pdfPage = pdfDocument.getPage(index);
         // 将图片添加到PDF中
         pdfPage.addImageObject(imgInfoList[index].path, 0, 0, imgInfoList[index].width,
           imgInfoList[index].height);
       }
       let pdfFileName = systemDateTime.getTime().toString();
       let pdfFilePath = this.context.tempDir + `/${pdfFileName}.pdf`;
       // 保存PDF文件
       pdfDocument.saveDocument(pdfFilePath);
       this.controller.releaseDocument();
       // 将PDF文件加载到PdfView组件中
       let loadResult: pdfService.ParseResult = await this.controller.loadDocument(pdfFilePath, '');
       if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
         this.controller.setPageZoom(1.5);
       }
     });
     ```
   * 创建PDF文件每页PDF的宽高跟随图片宽高。

     ```ts
     Button('创建PDF文件每页PDF的宽高跟随图片宽高').onClick(async () => {
       // 记录每张图片的路径、宽高（保证该沙箱目录下有对应格式图片）
       let dir: string = this.context.filesDir;
       let listFileOption: ListFileOptions = {
         recursion: false,
         listNum: 0,
         filter: {
           suffix: ['.png', '.jpg', '.jpeg']
         }
       };
       let imgInfoList: ArrayList<ImgInfo> = new ArrayList();
       let filenames = fs.listFileSync(dir, listFileOption);
       if (filenames.length <= 0) {
         console.info('no file be found');
         return;
       }
       // 遍历出目录下的图片文件
       for (let i = 0; i < filenames.length; i++) {
         console.info('filename: %s', filenames[i]);
         let imageSource = image.createImageSource(dir + '/' + filenames[i]);
         let imageInfo = imageSource.getImageInfoSync(0);
         // 记录图片路径、宽高信息
         let img = new ImgInfo();
         img.path = dir + '/' + filenames[i];
         img.width = imageInfo.size.width;
         img.height = imageInfo.size.height;
         imgInfoList.add(img);
       }

       // 创建PDF文件时每一页宽高跟随添加到该页的图片的宽高，根据记录下来的图片信息调用addImageObject将图片添加到PDF中，并保存PDF文件
       let pdfDocument = new pdfService.PdfDocument();
       // 创建PDF文件，第一页宽高跟随第一张图片宽高。
       pdfDocument.createDocument(imgInfoList[0].width, imgInfoList[0].height);
       for (let index = 0; index < imgInfoList.length; index++) {
         let pdfPage: pdfService.PdfPage | undefined;
         if (index > 0) {
           // 插入空白页，每一页宽高跟随图片宽高。
           pdfDocument.insertBlankPage(index, imgInfoList[index].width, imgInfoList[index].height);
         }
         pdfPage = pdfDocument.getPage(index);
         // 将图片添加到pdf中
         pdfPage.addImageObject(imgInfoList[index].path, 0, 0, imgInfoList[index].width,
           imgInfoList[index].height);
       }
       let pdfFileName = systemDateTime.getTime().toString();
       let pdfFilePath = this.context.tempDir + `/${pdfFileName}.pdf`;
       // 保存pdf文件
       pdfDocument.saveDocument(pdfFilePath);
       this.controller.releaseDocument();
       // 将PDF文件加载到PdfView组件中
       let loadResult: pdfService.ParseResult = await this.controller.loadDocument(pdfFilePath, '');
       if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
         this.controller.setPageZoom(1.5);
       }
     });
     ```

   完整示例参考如下：

   ```ts
   import { common } from '@kit.AbilityKit';
   import { fileIo as fs, ListFileOptions } from '@kit.CoreFileKit';
   import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
   import { image } from '@kit.ImageKit';
   import { ArrayList } from '@kit.ArkTS';
   import { systemDateTime } from '@kit.BasicServicesKit';
   @Entry
   @Component
   struct PdfPreview {
     private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       Column({ space: 5 }) {
         PdfView({
           controller: this.controller,
           pageFit: pdfService.PageFit.FIT_PAGE,
           showScroll: false
         })
           .height('90%')
           .width('90%')
           .id('pdfview_app_view')
           .borderWidth(0)
           .layoutWeight(1);

         Button('根据所有图片中的最大宽高值创建PDF文件').onClick(async () => {
           // 获取目录下所有图片中的最大宽高值，并记录每张图片的路径、宽高（保证该沙箱目录下有对应格式图片）
           let dir: string = this.context.filesDir;
           let listFileOption: ListFileOptions = {
             recursion: false,
             listNum: 0,
             filter: {
               suffix: ['.png', '.jpg', '.jpeg']
             }
           };
           let imgInfoList: ArrayList<ImgInfo> = new ArrayList();
           let maxImgWidthNum: number = 0;
           let maxImgHeightNum: number = 0;
           let filenames = fs.listFileSync(dir, listFileOption);
           if (filenames.length <= 0) {
             console.info('no file be found');
             return;
           }
           // 遍历出目录下的图片文件
           for (let i = 0; i < filenames.length; i++) {
             console.info('filename: %s', filenames[i]);
             let imageSource = image.createImageSource(dir + '/' + filenames[i]);
             let imageInfo = imageSource.getImageInfoSync(0);
             // 记录图片路径、宽高信息
             let img = new ImgInfo();
             img.path = dir + '/' + filenames[i];
             img.width = imageInfo.size.width;
             img.height = imageInfo.size.height;
             imgInfoList.add(img);
             // 更新宽高最大值
             if (imageInfo.size.height > maxImgHeightNum) {
               maxImgHeightNum = imageInfo.size.height;
             }
             if (imageInfo.size.width > maxImgWidthNum) {
               maxImgWidthNum = imageInfo.size.width;
             }
           }

           // 创建PDF文件时以获取到的图片最大宽高值作为PDF文件的宽高，根据记录下来的图片信息调用addImageObject将图片添加到PDF中，并保存PDF文件
           let pdfDocument = new pdfService.PdfDocument();
           // 创建PDF文件，宽高为获取到的图片最大宽高值
           pdfDocument.createDocument(maxImgWidthNum, maxImgHeightNum);
           for (let index = 0; index < imgInfoList.length; index++) {
             let pdfPage: pdfService.PdfPage | undefined;
             if (index > 0) {
               // 插入空白页
               pdfDocument.insertBlankPage(index, maxImgWidthNum, maxImgHeightNum);
             }
             pdfPage = pdfDocument.getPage(index);
             // 将图片添加到PDF中
             pdfPage.addImageObject(imgInfoList[index].path, 0, 0, imgInfoList[index].width,
               imgInfoList[index].height);
           }
           let pdfFileName = systemDateTime.getTime().toString();
           let pdfFilePath = this.context.tempDir + `/${pdfFileName}.pdf`;
           // 保存PDF文件
           pdfDocument.saveDocument(pdfFilePath);
           this.controller.releaseDocument();
           // 将PDF文件加载到PdfView组件中
           let loadResult: pdfService.ParseResult = await this.controller.loadDocument(pdfFilePath, '');
           if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
             this.controller.setPageZoom(1.5);
           }
         });

         Button('创建PDF文件每页PDF的宽高跟随图片宽高').onClick(async () => {
           // 记录每张图片的路径、宽高（保证该沙箱目录下有对应格式图片）
           let dir: string = this.context.filesDir;
           let listFileOption: ListFileOptions = {
             recursion: false,
             listNum: 0,
             filter: {
               suffix: ['.png', '.jpg', '.jpeg']
             }
           };
           let imgInfoList: ArrayList<ImgInfo> = new ArrayList();
           let filenames = fs.listFileSync(dir, listFileOption);
           if (filenames.length <= 0) {
             console.info('no file be found');
             return;
           }
           // 遍历出目录下的图片文件
           for (let i = 0; i < filenames.length; i++) {
             console.info('filename: %s', filenames[i]);
             let imageSource = image.createImageSource(dir + '/' + filenames[i]);
             let imageInfo = imageSource.getImageInfoSync(0);
             // 记录图片路径、宽高信息
             let img = new ImgInfo();
             img.path = dir + '/' + filenames[i];
             img.width = imageInfo.size.width;
             img.height = imageInfo.size.height;
             imgInfoList.add(img);
           }

           // 创建PDF文件时每一页宽高跟随添加到该页的图片的宽高，根据记录下来的图片信息调用addImageObject将图片添加到PDF中，并保存PDF文件
           let pdfDocument = new pdfService.PdfDocument();
           // 创建PDF文件，第一页宽高跟随第一张图片宽高。
           pdfDocument.createDocument(imgInfoList[0].width, imgInfoList[0].height);
           for (let index = 0; index < imgInfoList.length; index++) {
             let pdfPage: pdfService.PdfPage | undefined;
             if (index > 0) {
               // 插入空白页，每一页宽高跟随图片宽高。
               pdfDocument.insertBlankPage(index, imgInfoList[index].width, imgInfoList[index].height);
             }
             pdfPage = pdfDocument.getPage(index);
             // 将图片添加到pdf中
             pdfPage.addImageObject(imgInfoList[index].path, 0, 0, imgInfoList[index].width,
               imgInfoList[index].height);
           }
           let pdfFileName = systemDateTime.getTime().toString();
           let pdfFilePath = this.context.tempDir + `/${pdfFileName}.pdf`;
           // 保存pdf文件
           pdfDocument.saveDocument(pdfFilePath);
           this.controller.releaseDocument();
           // 将PDF文件加载到PdfView组件中
           let loadResult: pdfService.ParseResult = await this.controller.loadDocument(pdfFilePath, '');
           if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
             this.controller.setPageZoom(1.5);
           }
         });
       }
       .width('100%')
       .height('100%');
     }
   }

   export class ImgInfo {
     path: string = '';
     width: number = 0;
     height: number = 0;
   }
   ```

## 常见FAQ

Q：如何将自定义组件转为PDF文档？

A：使用[组件截图](../harmonyos-references/js-apis-arkui-componentsnapshot.md)将自定义组件截图为图片，然后可以将图片添加到PDF文档中。
