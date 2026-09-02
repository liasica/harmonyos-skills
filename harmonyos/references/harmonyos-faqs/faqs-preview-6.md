---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-6
title: 如何实现Word文件预览功能
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > 如何实现Word文件预览功能
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:27+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:49f471e7c0bf4e64a4bf6ba594afe873ff47966c36a224073cc3c20624e887ff
---

## 问题现象

如何实现预览rawfile里的Word文件功能？

## 背景知识

* [Preview Kit](../harmonyos-guides/preview-introduction.md)：为应用提供便捷的文件快速预览和文件打开加速能力。目前，Preview Kit实现Office的预览能力，主要是借助WPS的能力实现的，预览界面会有WPS提供的技术支持，并展示WPS的入口，统一按照文件预览的风格进行页面布局。

| 约束与限制 | 说明 |
| --- | --- |
| 支持的国家和地区 | 当前Preview Kit仅支持中国境内（不包含中国香港、中国澳门、中国台湾）。 |
| 支持的设备 | 当前Preview Kit相关能力只支持在真机上运行，暂不支持在模拟器上运行。  文件预览功能支持华为Phone、Tablet和2in1， 文件打开加速功能仅支持2in1设备。 |

* [filePreview](../harmonyos-references/preview-arkts.md)：为应用提供便捷的文件快速预览能力。应用可以通过文件预览提供的系统级预览API，可快速启动预览界面，实现对各类文件的预览。
* [getRawFdSync](../harmonyos-references/js-apis-resource-manager.md#getrawfdsync10)：获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）。
* [@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)：提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

## 解决方案

通过HarmonyOS提供的Preview Kit（文件预览服务）实现Word文件预览。实现思路如下：

1. 使用resourceManager.getRawFdSync获取resources/rawfile目录下文件的HAP包描述符（fd）。

   ```ts
   let srcFileDescriptor = this.context.resourceManager.getRawFdSync('test.docx'); // 需要在rawfile目录下手动添加名为test.docx的文件
   ```
2. 通过fs.statSync获取文件属性，调用isFile()判断是否为普通文件。

   ```ts
   if (!fs.statSync(srcFileDescriptor.fd).isFile()) {
     console.error('Not a regular file');
     return;
   }
   ```
3. 通过UIAbilityContext获取沙箱地址filesDir，fs.openSync打开文件，readSync/writeSync执行数据读写，操作完成后调用closeSync释放资源。

   ```ts
   let pathDir = this.context.filesDir; // 通过UIAbilityContext获取沙箱地址filesDir
   let filePath = pathDir + '/test.docx';
   // 以同步方法打开文件或目录。若文件不存在，则创建文件/读写打开
   file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE) as fs.File;
   let bufsize = 4096;
   let buf = new ArrayBuffer(bufsize); //  用于保存读取到的文件数据的缓冲区。
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
4. 通过filePreview.openPreview传入文件预览信息，打开预览窗口。

   **说明** 

   * 文件预览信息mimeType参数必须和文件一致，否则无法打开。例如docx对应application/vnd.openxmlformats-officedocument.wordprocessingml.document。详细参考：[文件预览支持的文件类型](../harmonyos-guides/preview-introduction.md#文件预览支持的文件类型)。
   * 文件预览信息uri参数file://com.example.myapplication中com.example.myapplication为应用包名，实际使用时需要替换为当前工程项目中的应用包名。

   ```ts
   filePreview.openPreview(this.uiContext, this.fileInfo).then(() => {
     console.info('openPreview success');
   }).catch((err: BusinessError) => {
     console.error('openPreview failed, err = ' + err.message);
   });
   ```
5. 完整示例参考如下：

   ```ts
   import common from '@ohos.app.ability.common';
   import fs from '@ohos.file.fs';
   import { filePreview } from '@kit.PreviewKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct filePreviewDemo {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     uiContext: Context = this.getUIContext().getHostContext() as common.Context;
     // 文件预览信息
     private fileInfo: filePreview.PreviewInfo = {
       title: 'test.docx', // 文件的标题名称
       uri: 'file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.docx', // 文件的uri，此处com.example.myapplication为包名，请按照应用的实际包名替换
       mimeType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' // 文件(夹)的媒体资源类型
     };

     copyFile() {
       let file: fs.File | undefined = undefined;
       try {
         // 获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）
         let srcFileDescriptor = this.context.resourceManager.getRawFdSync('test.docx'); // 需要在rawfile目录下手动添加名为test.docx的文件
         // 判断文件是否是普通文件。true：是普通文件；false：不是普通文件。
         if (!fs.statSync(srcFileDescriptor.fd).isFile()) {
           console.error('Not a regular file');
           return;
         }
         let pathDir = this.context.filesDir; // 通过UIAbilityContext获取沙箱地址filesDir
         let filePath = pathDir + '/test.docx';
         // 以同步方法打开文件或目录。若文件不存在，则创建文件/读写打开
         file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE) as fs.File;
         let bufsize = 4096;
         let buf = new ArrayBuffer(bufsize); //  用于保存读取到的文件数据的缓冲区。
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

## 常见FAQ

Q：如何在代码判断文件是否支持使用openPreview接口进行预览？

A：使用[canPreview](../harmonyos-references/preview-arkts.md#canpreview)接口根据文件的uri判断文件是否可预览，接口仅针对文件是否存在以及文件格式是否为支持的文件类型进行检验，后续openPreview进行文件查看时需要调用方保证文件可以被转授权。
