---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-76
title: 如何读取占用空间不同的文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何读取占用空间不同的文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d63baaea11891ea166bed0237891a0a475863ab3f43f0a6a72a908400613b127
---

## 问题现象

如何读取占用空间不同的文件？例如文本文件、音视频文件。

## 解决方案

1. 读取占用空间较小的文件，例如文本文件，适合使用fs.readText，代码示例如下：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo as fs } from '@kit.CoreFileKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct ReadFile {

     build() {
       Column() {
         Button('fs.readText')
           .onClick(() => {
             let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
             let filePath = context.filesDir + '/test.txt';
             fs.readText(filePath).then((str: string) => {
               console.info(`readText succeed:${str}`);
             }).catch((err: BusinessError) => {
               console.info(`code:${err.code}, message:${err.message}`);
             });
           })
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```
2. 读取占用空间较大的文件，例如音视频文件，则需要分块读取。推荐基于fs.createStream创建文件读取流的方式，也可以使用fs.read的方式读取，需要注意控制缓冲区大小。代码示例参考如下：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { fileIo as fs } from '@kit.CoreFileKit';

   @Entry
   @Component
   struct ReadFile {
     build() {
       Column({ space: 50 }) {
         Button('fs.createStream流式读取')
           .onClick(() => {
             try {
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
               let filePath = context.filesDir + '/test.mp4';
               let inputStream = fs.createStreamSync(filePath, 'r+');
               let stream = fs.createStreamSync(filePath, 'r');
               let bufSize = 1024;
               let buf = new ArrayBuffer(bufSize);
               let readLen: number;
               while ((readLen = stream.readSync(buf)) > 0) {
                 const contentBuf = readLen < bufSize ? buf.slice(0, readLen) : buf;
                 console.info(`数据处理：${contentBuf.byteLength}`);
               }
               inputStream.closeSync();
             } catch (error) {
               let err: BusinessError = error as BusinessError;
               console.error(err.message, err.code);
             }
           })

         Button('fs.read')
           .onClick(() => {
             try {
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
               let filePath = context.filesDir + '/test.mp4';
               let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
               let bufSize = 1024;
               let buf = new ArrayBuffer(bufSize);
               let readLen: number;
               while ((readLen = fs.readSync(file.fd, buf)) > 0) {
                 const contentBuf = readLen < bufSize ? buf.slice(0, readLen) : buf;
                 console.info(`数据处理：${contentBuf.byteLength}`);
               }
               fs.closeSync(file);
             } catch (error) {
               let err = error as BusinessError;
               console.info(`code:${err.code}, message:${err.message}`);
             }
           })
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```
