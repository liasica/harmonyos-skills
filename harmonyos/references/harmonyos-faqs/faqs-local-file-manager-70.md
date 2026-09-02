---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-70
title: 如何使用DownloadFileButton组件保存文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何使用DownloadFileButton组件保存文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2bcc772cf4565209b9888d4d0b625519eda4c4f2d4b10024906cad887a7c88d8
---

## 问题现象

如何使用DownloadFileButton组件保存网络文件到Download公共目录中？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/oc8k5MgtSqi3eAmkemYh6A/zh-cn_image_0000002629059026.png "点击放大")

## 背景知识

* [下载文件按钮](../harmonyos-references/ohos-arkui-advanced-downloadfilebutton.md)，通过点击该下载按钮，可以获取到当前应用在Download公共目录中所属的存储路径。
* [DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)文件选择器对象，用来支撑选择和保存各种格式文档。在使用前，需要先创建DocumentViewPicker实例。

## 解决方案

点击下载文件按钮，获取当前应用在Download公共目录中所属的存储路径，将下载好的文件写入，具体步骤如下：

1. 在module.json5文件中配置INTERNET网络权限：

   ```json
   "requestPermissions": [
     {
       "name":"ohos.permission.INTERNET"
     }
   ]
   ```
2. 创建DownloadFileButton组件，示例代码如下：

   ```ts
   DownloadFileButton({
     contentOptions: {
       icon: DownloadIconStyle.FULL_FILLED,
       text: DownloadDescription.DOWNLOAD
     },
     styleOptions: {
       iconSize: '16vp',
       layoutDirection: DownloadLayoutDirection.HORIZONTAL,
       fontSize: '16vp',
       fontStyle: FontStyle.Normal,
       fontWeight: FontWeight.Medium,
       fontFamily: 'HarmonyOS Sans',
       fontColor: '#ffffffff',
       iconColor: '#ffffffff',
       textIconSpace: '4vp'
     }
   })
     .markAnchor({ x: 0, y: 0 })
     .offset({ x: 0, y: 0 })
     .padding({
       top: '12vp',
       bottom: '12vp',
       left: '24vp',
       right: '24vp'
     })
     .backgroundColor('#007dff')
     .borderStyle(BorderStyle.Dotted)
     .borderWidth(0)
     .borderRadius('24vp')
   ```
3. 点击下载文件按钮，通过[request.downloadFile](../harmonyos-references/js-apis-request.md#requestdownloadfile9)创建下载任务，代码示例如下：

   ```ts
   request.downloadFile(context, {
     url: 'xxx.xxx.xxxx/xxxx.png', // 替换为自有链接
     filePath: sanPath
   })
   ```
4. 下载完成，通过DocumentViewPicker保存文件，代码示例如下：

   ```ts
   const documentSaveOptions = new picker.DocumentSaveOptions();
   // 创建文件管理器保存选项实例
   documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
   // 保存文件
   const documentViewPicker = new picker.DocumentViewPicker;
   documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
     // 获取到文件的URI后进行文件读取等操作
     let uri = documentSaveResult[0];
     this.constUri = uri;
     // 把这里的path存起来，作为后续保存文件的path
     let path: string = new fileUri.FileUri(uri).path;
     let filePath: string = `${path}/${'test.png'}`;
     console.info('pub uri:', uri);
     let sanFile: fs.File | null = null;
     let pubFile: fs.File | null = null;
     try {
       // 沙箱路径文件
       let sanFile = fs.openSync(sanPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
       let pubFile = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
       // 将文件从沙箱路拷贝到公共路径
       fs.copyFileSync(sanFile.fd, pubFile.fd);
     } catch (e) {
       console.error('fs.openSync failed error is : ', JSON.stringify(e));
     } finally {
       if (sanFile !== null) {
         fs.closeSync(sanFile);
       }
       if (pubFile !== null) {
         fs.closeSync(pubFile);
       }
     }
     this.getUIContext().getPromptAction().showToast({
       message: '保存到本地成功',
       duration: 2000,
       showMode: promptAction.ToastShowMode.DEFAULT,
       bottom: 85
     });
   }).catch((err: BusinessError) => {
     console.error(`Invoke documentPicker.select failed, message is ${err.message}`);
   });
   ```

   完整代码示例如下：

   ```ts
   import common from '@ohos.app.ability.common';
   import fs from '@ohos.file.fs';
   import request from '@ohos.request';
   import { BusinessError } from '@ohos.base';
   import { fileUri, picker } from '@kit.CoreFileKit';
   import {
     DownloadDescription,
     DownloadFileButton,
     DownloadIconStyle,
     DownloadLayoutDirection,
     promptAction
   } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     @State constUri: string = '';

     build() {
       Row() {
         Column() {
           DownloadFileButton({
             contentOptions: {
               icon: DownloadIconStyle.FULL_FILLED,
               text: DownloadDescription.DOWNLOAD
             },
             styleOptions: {
               iconSize: '16vp',
               layoutDirection: DownloadLayoutDirection.HORIZONTAL,
               fontSize: '16vp',
               fontStyle: FontStyle.Normal,
               fontWeight: FontWeight.Medium,
               fontFamily: 'HarmonyOS Sans',
               fontColor: '#ffffffff',
               iconColor: '#ffffffff',
               textIconSpace: '4vp'
             }
           })
             .markAnchor({ x: 0, y: 0 })
             .offset({ x: 0, y: 0 })
             .padding({
               top: '12vp',
               bottom: '12vp',
               left: '24vp',
               right: '24vp'
             })
             .backgroundColor('#007dff')
             .borderStyle(BorderStyle.Dotted)
             .borderWidth(0)
             .borderRadius('24vp')
             .onClick(() => {
               console.info('DownloadFileButton Click');
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
               let sanPath = context.filesDir + '/' + Date.now() + '.png';
               try {
                 request.downloadFile(context, {
                   url: 'xxx.xxx.xxxx/xxxx.png', // 替换为自有链接
                   filePath: sanPath
                 })
                   .then((downloadTask: request.DownloadTask) => {
                   downloadTask.on('complete', () => {
                     console.info('download complete');
                     const documentSaveOptions = new picker.DocumentSaveOptions();
                     // 创建文件管理器保存选项实例
                     documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
                     // 保存文件
                     const documentViewPicker = new picker.DocumentViewPicker;
                     documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
                       // 获取到文件的URI后进行文件读取等操作
                       let uri = documentSaveResult[0];
                       this.constUri = uri;
                       // 把这里的path存起来，作为后续保存文件的path
                       let path: string = new fileUri.FileUri(uri).path;
                       let filePath: string = `${path}/${'test.png'}`;
                       console.info('pub uri:', uri);
                       let sanFile: fs.File | null = null;
                       let pubFile: fs.File | null = null;
                       try {
                         // 沙箱路径文件
                         let sanFile = fs.openSync(sanPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                         let pubFile = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                         // 将文件从沙箱路拷贝到公共路径
                         fs.copyFileSync(sanFile.fd, pubFile.fd);
                       } catch (e) {
                         console.error('fs.openSync failed error is : ', JSON.stringify(e));
                       } finally {
                         if (sanFile !== null) {
                           fs.closeSync(sanFile);
                         }
                         if (pubFile !== null) {
                           fs.closeSync(pubFile);
                         }
                       }
                       this.getUIContext().getPromptAction().showToast({
                         message: '保存到本地成功',
                         duration: 2000,
                         showMode: promptAction.ToastShowMode.DEFAULT,
                         bottom: 85
                       });
                     }).catch((err: BusinessError) => {
                       console.error(`Invoke documentPicker.select failed, message is ${err.message}`);
                     });
                   });
                 }).catch((err: BusinessError) => {
                   console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
                 });
               } catch (e) {
                 console.error(e.message);
               }
             })
         }.width('100%')
       }.height('100%')
     }
   }
   ```
