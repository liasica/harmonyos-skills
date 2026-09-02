---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-8
title: 如何实现通过文件选择器（FilePicker）选择文件进行预览
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > 如何实现通过文件选择器（FilePicker）选择文件进行预览
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:0d69b2ce4161beeda4d33de149321d41431987394a966751cb6244d6d3ec3684
---

## 问题现象

使用文件选择器（FilePicker）选择文件进行预览时报预览失败，如何解决？

## 背景知识

* Preview Kit[文件预览](../harmonyos-guides/preview-filepreview.md)需要调用方存在对应uri的转授权能力，从而让预览获得该文件的访问权限来正常读取文件。
* [DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)拿到的文件uri应用仅有临时权限，该权限无法分享给预览，导致预览失败。

## 解决方案

可以先将文件选择器打开的文件拷贝至应用沙箱内，再通过传入拷贝的沙箱文件的uri来进行预览。

1. 设置[PreviewInfo](../harmonyos-references/preview-arkts.md#previewinfo)文件预览信息，其中mimeType为空时，Preview Kit会根据文件后缀判断文件类型。

   ```ts
   // 文件预览信息
   private fileInfo: filePreview.PreviewInfo = {
     title: '', // 文件的标题名称
     uri: '', // 文件的uri。Picker打开的文件只有临时权限，需要持久化权限或传入沙箱
     mimeType: '' // 文件（夹）的媒体资源类型，传入空值可以由Preview Kit根据文件后缀自行判断类型
   };
   ```
2. 通过[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)拉起文件选择器选择文件，通过[fs.copyFileSync](../harmonyos-references/js-apis-file-fs.md#fileiocopyfilesync)复制文件到沙箱，通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)将沙箱路径转换为Preview Kit使用的uri。

   ```ts
   // 1. 拉起Picker选择1个文件；2. 复制文件到沙箱；3. 将沙箱路径转uri传递给Preview Kit的uri字段
   docPickerSelectThenCopy2Sandbox() {
     try {
       // 1. 拉起Picker选择1个文件
       let documentSelectOptions = new picker.DocumentSelectOptions();
       documentSelectOptions.maxSelectNumber = 1; // 选择文件最大个数1
       let documentPicker = new picker.DocumentViewPicker(this.context);
       documentPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
         console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' +
         JSON.stringify(documentSelectResult));
         let pickerUri = documentSelectResult[0];

         // 2. 复制文件到沙箱
         let file = fs.openSync(pickerUri, fs.OpenMode.READ_ONLY);
         let pathDir = this.context.filesDir;
         let filePath = pathDir + '/' + file.name; // 沙箱文件路径
         fs.copyFileSync(file.fd, filePath);
         fs.closeSync(file);

         // 3. 将沙箱路径转uri传递给Preview Kit的uri字段
         this.fileInfo.uri = fileUri.getUriFromPath(filePath); // 沙箱路径需要转换为uri才能传递给Preview Kit使用
         this.fileInfo.title = file.name; // 将文件名赋值给Preview Kit中的title字段，可以按需修改
       }).catch((err: BusinessError) => {
         console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
       });
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
     }
   }
   ```
3. 通过filePreview.[canPreview](../harmonyos-references/preview-arkts.md#canpreview)判断文件是否可以预览，通过filePreview.[openPreview](../harmonyos-references/preview-arkts.md#openpreview)打开预览窗口。

   ```ts
   // 根据文件的uri判断文件是否可以预览
   // 当前接口仅针对文件是否存在以及文件格式是否为支持的文件类型进行检验，后续openPreview进行文件查看时需要调用方保证文件可以被转授权
   filePreview.canPreview(this.context, this.fileInfo.uri).then((result) => { // 传入支持的文件类型且文件存在时会返回true
     console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
     // 打开预览窗口
     filePreview.openPreview(this.context, this.fileInfo).then(() => {
       console.info('openPreview success');
     }).catch((err: BusinessError) => {
       console.error('openPreview failed, err = ' + err.message);
     });
   }).catch((err: BusinessError) => {
     console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
   });
   ```

注意事项：

* 沙箱路径需要通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)获取到uri传递给Preview Kit使用。
* 判断文件是否可以预览的接口filePreview.[canPreview](../harmonyos-references/preview-arkts.md#canpreview)，仅针对文件是否存在以及文件格式是否为支持的文件类型进行检验，后续openPreview进行文件查看时需要调用方保证文件可以被转授权。

4. 完整代码示例如下：

   ```ts
   import common from '@ohos.app.ability.common';
   import { filePreview } from '@kit.PreviewKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo as fs, fileUri, picker } from '@kit.CoreFileKit';

   @Entry
   @Component
   struct pickerPreviewDemo {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     // 文件预览信息
     private fileInfo: filePreview.PreviewInfo = {
       title: '', // 文件的标题名称
       uri: '', // 文件的uri。Picker打开的文件只有临时权限，需要持久化权限或传入沙箱
       mimeType: '' // 文件（夹）的媒体资源类型，传入空值可以由Preview Kit根据文件后缀自行判断类型
     };

     // 1. 拉起Picker选择1个文件；2. 复制文件到沙箱；3. 将沙箱路径转uri传递给Preview Kit的uri字段
     docPickerSelectThenCopy2Sandbox() {
       try {
         // 1. 拉起Picker选择1个文件
         let documentSelectOptions = new picker.DocumentSelectOptions();
         documentSelectOptions.maxSelectNumber = 1; // 选择文件最大个数1
         let documentPicker = new picker.DocumentViewPicker(this.context);
         documentPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
           console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' +
           JSON.stringify(documentSelectResult));
           let pickerUri = documentSelectResult[0];

           // 2. 复制文件到沙箱
           let file = fs.openSync(pickerUri, fs.OpenMode.READ_ONLY);
           let pathDir = this.context.filesDir;
           let filePath = pathDir + '/' + file.name; // 沙箱文件路径
           fs.copyFileSync(file.fd, filePath);
           fs.closeSync(file);

           // 3. 将沙箱路径转uri传递给Preview Kit的uri字段
           this.fileInfo.uri = fileUri.getUriFromPath(filePath); // 沙箱路径需要转换为uri才能传递给Preview Kit使用
           this.fileInfo.title = file.name; // 将文件名赋值给Preview Kit中的title字段，可以按需修改
         }).catch((err: BusinessError) => {
           console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
         });
       } catch (error) {
         let err: BusinessError = error as BusinessError;
         console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
       }
     }

     build() {
       Row() {
         Column() {
           Button('拉起Picker选择文件并传入沙箱')
             .onClick(async () => {
               this.docPickerSelectThenCopy2Sandbox();
             })
             .margin({ bottom: 10 });

           Button('预览文件')
             .onClick(() => {
               // 根据文件的uri判断文件是否可以预览
               // 当前接口仅针对文件是否存在以及文件格式是否为支持的文件类型进行检验，后续openPreview进行文件查看时需要调用方保证文件可以被转授权
               filePreview.canPreview(this.context, this.fileInfo.uri).then((result) => { // 传入支持的文件类型且文件存在时会返回true
                 console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
                 // 打开预览窗口
                 filePreview.openPreview(this.context, this.fileInfo).then(() => {
                   console.info('openPreview success');
                 }).catch((err: BusinessError) => {
                   console.error('openPreview failed, err = ' + err.message);
                 });
               }).catch((err: BusinessError) => {
                 console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
               });
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
