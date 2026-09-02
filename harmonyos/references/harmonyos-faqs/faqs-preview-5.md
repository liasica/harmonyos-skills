---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-5
title: 如何使用预览打开OFD文件
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > 如何使用预览打开OFD文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e6378fb568e7ce84eeb635ed96a00559a33060037bfd7750071c311a517b0fe4
---

## 问题现象

mimeType写了ofd类型之后，但是Preview不能正确预览ofd文件。

```ts
let fileInfo: filePreview.PreviewInfo = {
      title: 'test.ofd',
      uri: this.filePath, 
      mimeType: 'text/plain/ofd' // 预览文件类型
    };
    filePreview.openPreview(context, fileInfo, displayInfo)
```

## 背景知识

* [Preview Kit](../harmonyos-guides/preview-introduction.md)（文件预览服务）为应用提供便捷的文件快速预览和文件打开加速能力。
* Preview Kit能够对图片、视频、音频、文本、html等进行预览查看。详情参考[文件预览支持的文件类型](../harmonyos-guides/preview-introduction.md#文件预览支持的文件类型)。

## 解决方案

首先要检查文件是否支持预览，预览参数配置是否正确。

1. 判断文件是否支持预览。

   先通过filePreview.[canPreview](../harmonyos-references/preview-arkts.md#canpreview)接口判断文件是否可预览，当前预览组件仅支持用户文件，不支持网络文件。如果想要预览网络文件，可以考虑先将文件下载到本地，然后再进行预览。

   ```ts
   filePreview.canPreview(this.uiContext, this.fileInfo.uri).then((result) => {
     console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
     if (result) {
       filePreview.openPreview(this.uiContext, this.fileInfo).then(() => {
         console.info('openPreview success');
       }).catch((err: BusinessError) => {
         console.error(`openPreview failed, error message: ${err.message}`);
       });
     } else {
       console.error('File cannot be previewed');
     }
   }).catch((err: BusinessError) => {
     console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
   });
   ```
2. 检查预览参数配置是否正确。

   Preview Kit支持的文件类型只有文件后缀类型与mimeType类型相匹配时，才能正常预览文件。ofd文件的mimeType类型为general.ofd，也可以传入空值由Preview Kit判断文件类型。

   ```ts
   // 文件预览信息
   private fileInfo: filePreview.PreviewInfo = {
     title: 'test.ofd', // 文件的标题名称
     uri: 'file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.ofd', // 文件的uri，此处com.example.myapplication为包名，请按照应用的实际包名替换
     mimeType: 'general.ofd' // 文件（夹）的类型，ofd文件的类型为general.ofd，也可以传入空值由Preview Kit判断文件类型
   };
   ```
3. 完整代码示例如下：

   ```ts
   import common from '@ohos.app.ability.common';
   import fs from '@ohos.file.fs';
   import { filePreview } from '@kit.PreviewKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct OfdPreviewDemo {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     uiContext: Context = this.getUIContext().getHostContext() as common.Context;
     // 文件预览信息
     private fileInfo: filePreview.PreviewInfo = {
       title: 'test.ofd', // 文件的标题名称
       uri: 'file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.ofd', // 文件的uri，此处com.example.myapplication为包名，请按照应用的实际包名替换
       mimeType: 'general.ofd' // 文件（夹）的类型，ofd文件的类型为general.ofd，也可以传入空值由Preview Kit判断文件类型
     };

     copyFile() {
       let file: fs.File | undefined = undefined;
       try {
         // 获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）
         let srcFileDescriptor = this.context.resourceManager.getRawFdSync('test.ofd'); // 需要在rawfile目录下手动添加名为test.ofd的文件
         // 判断文件是否是普通文件。true：是普通文件；false：不是普通文件。
         if (!fs.statSync(srcFileDescriptor.fd).isFile()) {
           console.error('Not a regular file');
           return;
         }
         let pathDir = this.context.filesDir; // 通过UIAbilityContext获取沙箱地址filesDir
         let filePath = pathDir + '/test.ofd';
         // 以同步方法打开文件或目录。若文件不存在，则创建文件/读写打开
         file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE) as fs.File;
         let bufsize = 4096;
         let buf = new ArrayBuffer(bufsize); // 用于保存读取到的文件数据的缓冲区。
         let off = 0, len = 0, readLen = 0; // 动态调整目标文件的写入位置. 写入实际读取的字节数,累计已读取的总字节数
         len = fs.readSync(srcFileDescriptor.fd, buf, { offset: srcFileDescriptor.offset + off, length: bufsize });
         while (len) {
           readLen += len;
           fs.writeSync(file.fd, buf, { offset: off, length: len });
           off = off + len;
           // 当剩余未读取的字节数小于当前分块大小时，调整bufsize为剩余大小，避免无效读取
           if ((srcFileDescriptor.length - readLen) < bufsize) {
             bufsize = srcFileDescriptor.length - readLen;
           }
           len = fs.readSync(srcFileDescriptor.fd, buf, { offset: srcFileDescriptor.offset + off, length: bufsize });
         }
       } catch (error) {
         console.error('openPreview failed, err = ' + error.message);
       } finally {
         // 关闭文件或目录
         if (file) {
           fs.closeSync(file);
         }
         this.context.resourceManager.closeRawFdSync('test.ofd');
       }
     }

     build() {
       Row() {
         Column() {
           Button('传到沙箱')
             .onClick(() => {
               this.copyFile();
             })
             .margin({ bottom: 10 });
           Button('预览文件')
             .onClick(() => {
               filePreview.canPreview(this.uiContext, this.fileInfo.uri).then((result) => {
                 console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
                 if (result) {
                   filePreview.openPreview(this.uiContext, this.fileInfo).then(() => {
                     console.info('openPreview success');
                   }).catch((err: BusinessError) => {
                     console.error(`openPreview failed, error message: ${err.message}`);
                   });
                 } else {
                   console.error('File cannot be previewed');
                 }
               }).catch((err: BusinessError) => {
                 console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
               });
             })
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```

## 总结

Preview Kit提供了系统级的文件快速预览功能，只需要几行代码就能实现多种类型的文件预览。主要优势在于简单易用，不需要复杂的配置，能够大大提高开发效率。但同时也有局限性，例如不支持网络文件的预览。对于网络文件，可以考虑先下载到本地再使用Preview Kit预览，或者使用Web组件处理。

ofd文件的mimeType类型为general.ofd，也可以传入空值由Preview Kit判断文件类型。
