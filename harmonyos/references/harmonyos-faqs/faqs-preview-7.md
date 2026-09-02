---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-7
title: 如何实现应用外预览pdf文件功能
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > 如何实现应用外预览pdf文件功能
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:27+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:ef0faa092b3ae59761c5fc88b9ff527fcaf26a1cddce7da631e624e2d54e1a93
---

## 问题现象

如何实现在应用外进行pdf文件预览的功能？

## 背景知识

[Preview Kit（文件预览服务）](../harmonyos-guides/preview-kit-guide.md)为应用提供便捷的文件快速预览能力，支持跳出应用进行文件的预览。

| 约束与限制 | 说明 |
| --- | --- |
| 支持的国家和地区 | 当前Preview Kit仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 支持的设备 | 模拟器支持情况，请见模拟器与真机的差异列表中[应用服务](../harmonyos-guides/ide-emulator-specification.md)章节的Preview Kit（文件预览服务）说明。  文件预览功能支持华为Phone、Tablet和2in1，文件打开加速功能仅支持2in1设备。 |

## 解决方案

通过HarmonyOS提供的Preview Kit（文件预览服务）实现pdf文件在应用外预览。实现思路如下：

1. 使用resourceManager.[getRawFdSync](../harmonyos-references/js-apis-resource-manager.md#getrawfdsync10)获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）。

   ```screen
   let srcFileDescriptor = this.context.resourceManager.getRawFdSync('test.pdf'); // 需要在rawfile目录下手动添加名为test.pdf的文件
   ```
2. 通过[fs.statSync](../harmonyos-references/js-apis-file-fs.md#fileiostatsync)获取文件或目录详细属性信息，调用[isFile](../harmonyos-references/js-apis-file-fs.md#isfile)判断文件是否是普通文件。

   ```screen
   if (!fs.statSync(srcFileDescriptor.fd).isFile()) {
     console.error('Not a regular file');
     return;
   }
   ```
3. 通过[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)获取沙箱地址filesDir，调用[fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)打开文件，调用[fs.readSync](../harmonyos-references/js-apis-file-fs.md#fileioreadsync)/[fs.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync)执行数据读写，操作完成后调用[fs.closeSync](../harmonyos-references/js-apis-file-fs.md#fileioclosesync)释放资源。

   ```screen
   let pathDir = this.context.filesDir; // 通过UIAbilityContext获取沙箱地址filesDir
   let filePath = pathDir + '/test.pdf';
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
   ```
4. 通过filePreview.[openPreview](../harmonyos-references/preview-arkts.md#openpreview)传入文件预览信息，打开预览窗口。

   **说明** 

   * 文件预览信息mimeType参数必须和文件一致，否则无法打开。例如pdf文件类型对应application/pdf。详细见[文件预览支持的文件类型](../harmonyos-guides/preview-introduction.md#文件预览支持的文件类型)。
   * 文件预览信息uri参数file://com.example.myapplication中com.example.myapplication为应用包名，实际使用时需要替换为当前工程项目中的应用包名。

   ```screen
   filePreview.openPreview(this.uiContext, this.fileInfo).then(() => {
     console.info('openPreview success');
   }).catch((err: BusinessError) => {
     console.error('openPreview failed, err = ' + err.message);
   });
   ```
5. 完整代码示例如下：

   ```screen
   import common from '@ohos.app.ability.common';
   import fs from '@ohos.file.fs';
   import { filePreview } from '@kit.PreviewKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct pdfPreviewDemo {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     uiContext: Context = this.getUIContext().getHostContext() as common.Context;
     // 文件预览信息
     private fileInfo: filePreview.PreviewInfo = {
       title: 'test.pdf', // 文件的标题名称
       uri: 'file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.pdf', // 文件的uri，此处com.example.myapplication为包名，请按照应用的实际包名替换
       mimeType: 'application/pdf' // 文件（夹）的媒体资源类型
     };

     copyFile() {
       let file: fs.File | undefined = undefined;
       try {
         // 获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）
         let srcFileDescriptor = this.context.resourceManager.getRawFdSync('test.pdf'); // 需要在rawfile目录下手动添加名为test.pdf的文件
         // 判断文件是否是普通文件。true：是普通文件；false：不是普通文件。
         if (!fs.statSync(srcFileDescriptor.fd).isFile()) {
           console.error('Not a regular file');
           return;
         }
         let pathDir = this.context.filesDir; // 通过UIAbilityContext获取沙箱地址filesDir
         let filePath = pathDir + '/test.pdf';
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
         this.context.resourceManager.closeRawFdSync('test.pdf');
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
               filePreview.openPreview(this.uiContext, this.fileInfo).then(() => {
                 console.info('openPreview success');
               }).catch((err: BusinessError) => {
                 console.error('openPreview failed, err = ' + err.message);
               });
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
