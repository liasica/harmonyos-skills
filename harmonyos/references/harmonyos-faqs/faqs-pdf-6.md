---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-6
title: 如何打开三方应用分享的PDF文件
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 如何打开三方应用分享的PDF文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a5172ea98076dbe40dfa81de821683ccb49b4123835f6464898ff3f06a00911d
---

## 问题现象

分享PDF文件时，分享面板没有自己开发的应用，如何打开三方应用分享的PDF文件。

## 背景知识

* [分享服务](../harmonyos-guides/share-introduction.md)为应用提供文本、图片、视频等内容跨应用、跨端分享能力。
* [标准化数据类型](../harmonyos-guides/uniform-data-type-list.md)（Uniform Type Descriptor，简称UTD）用于解决系统中的类型模糊问题，即针对同一种数据类型，存在不同的类型描述方式：MIME Type、文件扩展名等。
* [应用沙箱](../harmonyos-guides/app-sandbox-directory.md)是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”。
* [预览PDF文档](../harmonyos-guides/pdf-pdfview-component.md)PDF Kit提供了丰富的PDF文档预览能力，比如：页面跳转、页面缩放、单双页显示、页面适配、滚动视图方式预览。

## 解决方案

1. 目标应用注册支持分享内容的能力。在应用配置文件添加skills。

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             },
             // 添加skill配置
             {
               "actions": [
                 // 必需，声明数据处理能力
                 "ohos.want.action.viewData",
                 "ohos.want.action.sendData"
               ],
               "uris": [
                 {
                   "scheme": "file",
                   // 目标应用在配置支持接收的数据类型时，需穷举支持的UTD
                   "utd": "com.adobe.pdf",
                   // maxFileSupported对于归属指定类型的文件，标识一次支持接收的最大数量。默认为0，代表不支持此类文件的分享
                   "maxFileSupported": 1
                 },
                 {
                   "scheme": "file",
                   "utd": "general.object",
                   "maxFileSupported": 1
                 }
               ]
             }
           ]
         }
       ]
     }
   }
   ```
2. 获取三方应用分享的内容。由于存在应用沙箱隔离，被分享的目标应用无法直接操作宿主应用沙箱中的文件，需拷贝文件至本应用沙箱。

   ```ts
   import { UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { systemShare } from '@kit.ShareKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       this.handleSharedData(want);
     }

     onNewWant(want: Want): void {
       this.handleSharedData(want);
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }

     handleSharedData(want: Want) {
       systemShare.getSharedData(want)
         .then((data: systemShare.SharedData) => {
           data?.getRecords()?.forEach((record: systemShare.SharedRecord) => {
             if (!record.uri) {
               return;
             }

             try {
               // 获取uri，缓存至应用沙箱
               const file = fileIo.openSync(record.uri, fileIo.OpenMode.READ_ONLY);
               const destPath = this.context.cacheDir + '/' + file.name;
               const outFile = fileIo.openSync(destPath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
               const shareFilePath = outFile.path;
               fileIo.copyFileSync(file.fd, outFile.fd);
               fileIo.closeSync(file);
               fileIo.closeSync(outFile);
               AppStorage.setOrCreate('SHARE_FILE_PATH', shareFilePath);
             } catch (error) {
               console.error(`Failed to parse share data. Code: ${error.code}, message: ${error.message}`);
             }
           });
         })
         .catch((error: BusinessError) => {
           console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
         });
     }
   };
   ```
3. 使用PdfView预览PDF文件。

   ```ts
   import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';

   @Entry
   @Component
   struct Index {
     context = this.getUIContext().getHostContext()!;
     private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

     build() {
       Column() {
         Button('预览')
           .onClick(() => {
             const path = AppStorage.get('SHARE_FILE_PATH') as string;
             const pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
             pdfDocument.loadDocument(path);
             this.controller.loadDocument(path);
           })

         PdfView({
           controller: this.controller,
           pageFit: pdfService.PageFit.FIT_WIDTH,
           showScroll: true
         })
           .id('pdfview_app_view')
           .layoutWeight(1)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

## 常见FAQ

Q：为什么WPS移动版分享PDF文件看不到目标应用？

A：宿主应用在发起文件分享时，填写的UTD可能有差异，目标应用需穷举支持的UTD类型“general.object”。
