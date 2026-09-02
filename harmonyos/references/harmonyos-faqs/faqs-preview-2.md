---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-2
title: Preview Kit（文件预览服务）使用指南和注意事项
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > Preview Kit（文件预览服务）使用指南和注意事项
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:c306404adb22074aeabf22aa55cee852de9654ac96cea569e7aebaf3d7752e8d
---

## 问题现象

在HarmonyOS应用开发中，开发者经常需要实现各种文件的预览功能，包括：

1. 本地存储的文件预览。
2. 应用资源目录中的文件预览。
3. 网络文件的下载与预览。

如何利用HarmonyOS提供的filePreview服务统一实现这些不同来源文件的预览，是开发者面临的一个常见需求。

## 背景知识

HarmonyOS提供了[Preview Kit（文件预览服务）](../harmonyos-guides/preview-kit-guide.md)框架，这是一个用于文件预览的统一接口服务。

* 通过Preview Kit，用户可以对用户文件（包括图片、视频、音频、文本、html等）进行内容查看，详见[文件预览支持的文件类型](../harmonyos-guides/preview-introduction.md#文件预览支持的文件类型)。
* 同时用户还可以通过点击右上角的"使用其他应用打开"的按钮跳转到具体的应用进行展示，从而进行其他操作，如图片的旋转、放大等。

## 解决方案

1. 本地文件指存储在应用沙箱目录或公共目录中的文件。
   * 公共目录中的文件预览，见[openPreview](../harmonyos-references/preview-arkts.md#openpreview)接口示例代码；
   * 沙箱目录文件预览，代码示例如下：

     ```ts
     previewLocalFile() {
         try {
           const filePath = `${this.context.filesDir}/sample.pdf`;
           // 检查文件是否存在
           const isExist = fs.accessSync(filePath);
           if (!isExist) {
             console.error('本地文件不存在，请确保文件已放置到应用目录');
             return;
           }
           // 构建PreviewInfo
           let uri = fileUri.getUriFromPath(filePath);
           let fileInfo: filePreview.PreviewInfo = {
             title: 'sample.pdf',
             uri: uri,
             mimeType: 'application/pdf',
           };
           // 打开文件预览
           filePreview.openPreview(this.context, fileInfo).then(() => {
             console.info('Succeeded in opening preview');
           }).catch((err: BusinessError) => {
             console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
           });
         } catch (error) {
           console.error(`预览rawfile文件失败: ${JSON.stringify(error)}`);
         }
       }
     ```
2. rawfile文件预览：预览时需要先将rawfile导入至沙箱路径。代码示例如下：

   ```ts
   previewRawFile() {
       try {
         // 预览rawfile文件,需要将文件复制到沙箱目录
         let filePath = `${this.context.filesDir}/sample.pdf`;
         const resourceMgr = this.context.resourceManager;
         resourceMgr.getRawFileContent('sample.pdf', (err, value) => {
           let myBuffer: ArrayBufferLike = value.buffer;
           // 创建sample.pdf沙箱路径，并写入数据
           let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
           fs.writeSync(file.fd, myBuffer);
           fs.close(file);
         });
         let uri = fileUri.getUriFromPath(filePath);
         let fileInfo: filePreview.PreviewInfo = {
           title: 'sample.pdf',
           uri: uri,
           mimeType: 'application/pdf',
         };
         // 打开文件预览
         filePreview.openPreview(this.context, fileInfo).then(() => {
           console.info('Succeeded in opening preview');
         }).catch((err: BusinessError) => {
           console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
         });
       } catch (error) {
         console.error(`预览rawfile文件失败: ${JSON.stringify(error)}`);
       }
     }
   ```
3. 网络文件预览：需要将网络文件先下载到本地，再进行本地文件预览。代码示例如下：

   ```ts
   previewNetworkFile() {
       // url需替换为实际可用的pdf url
       const url = 'https://****.com/test.pdf';
       let filePath = `${this.context.filesDir}/sample.pdf`;
       try {
         // 网络文件下载到本地
         let res = fs.accessSync(filePath);
         if (res) {
           // 本地文件存在，则直接调用预览方法
           console.info('file exists and ViewFile');
           let uri = fileUri.getUriFromPath(filePath);
           let fileInfo: filePreview.PreviewInfo = {
             title: 'sample.pdf',
             uri: uri,
             mimeType: 'application/pdf',
           };
           // 打开文件预览
           filePreview.openPreview(this.context, fileInfo).then(() => {
             console.info('Succeeded in opening preview');
           }).catch((err: BusinessError) => {
             console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
           });
         } else {
           // 文件下载到本地
           request.downloadFile(this.context, {
             url: url,
             filePath: filePath
           }).then((downloadTask: request.DownloadTask) => {
             // 下载完成回调
             downloadTask.on('complete', () => {
               console.info('download complete');
               let uri = fileUri.getUriFromPath(filePath);
               let fileInfo: filePreview.PreviewInfo = {
                 title: 'sample.pdf',
                 uri: uri,
                 mimeType: 'application/pdf',
               };
               // 打开文件预览
               filePreview.openPreview(this.context, fileInfo).then(() => {
                 console.info('Succeeded in opening preview');
               }).catch((err: BusinessError) => {
                 console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
               });
             });
           }).catch((err: BusinessError) => {
             console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
           });
         }
       } catch (error) {
         let err: BusinessError = error as BusinessError;
         console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
       }
     }
   ```
4. 完整代码示例如下：

   ```ts
   import { fileUri, fileIo as fs } from '@kit.CoreFileKit';
   import { filePreview } from '@kit.PreviewKit';
   import { BusinessError, request } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     // Start solution1
     previewLocalFile() {
       try {
         const filePath = `${this.context.filesDir}/sample.pdf`;
         // 检查文件是否存在
         const isExist = fs.accessSync(filePath);
         if (!isExist) {
           console.error('本地文件不存在，请确保文件已放置到应用目录');
           return;
         }
         // 构建PreviewInfo
         let uri = fileUri.getUriFromPath(filePath);
         let fileInfo: filePreview.PreviewInfo = {
           title: 'sample.pdf',
           uri: uri,
           mimeType: 'application/pdf',
         };
         // 打开文件预览
         filePreview.openPreview(this.context, fileInfo).then(() => {
           console.info('Succeeded in opening preview');
         }).catch((err: BusinessError) => {
           console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
         });
       } catch (error) {
         console.error(`预览rawfile文件失败: ${JSON.stringify(error)}`);
       }
     }
     // End solution1

     // Start solution2
     previewRawFile() {
       try {
         // 预览rawfile文件,需要将文件复制到沙箱目录
         let filePath = `${this.context.filesDir}/sample.pdf`;
         const resourceMgr = this.context.resourceManager;
         resourceMgr.getRawFileContent('sample.pdf', (err, value) => {
           let myBuffer: ArrayBufferLike = value.buffer;
           // 创建sample.pdf沙箱路径，并写入数据
           let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
           fs.writeSync(file.fd, myBuffer);
           fs.close(file);
         });
         let uri = fileUri.getUriFromPath(filePath);
         let fileInfo: filePreview.PreviewInfo = {
           title: 'sample.pdf',
           uri: uri,
           mimeType: 'application/pdf',
         };
         // 打开文件预览
         filePreview.openPreview(this.context, fileInfo).then(() => {
           console.info('Succeeded in opening preview');
         }).catch((err: BusinessError) => {
           console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
         });
       } catch (error) {
         console.error(`预览rawfile文件失败: ${JSON.stringify(error)}`);
       }
     }
     // End solution2

     // Start solution3
     previewNetworkFile() {
       // url需替换为实际可用的pdf url
       const url = 'https://****.com/test.pdf';
       let filePath = `${this.context.filesDir}/sample.pdf`;
       try {
         // 网络文件下载到本地
         let res = fs.accessSync(filePath);
         if (res) {
           // 本地文件存在，则直接调用预览方法
           console.info('file exists and ViewFile');
           let uri = fileUri.getUriFromPath(filePath);
           let fileInfo: filePreview.PreviewInfo = {
             title: 'sample.pdf',
             uri: uri,
             mimeType: 'application/pdf',
           };
           // 打开文件预览
           filePreview.openPreview(this.context, fileInfo).then(() => {
             console.info('Succeeded in opening preview');
           }).catch((err: BusinessError) => {
             console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
           });
         } else {
           // 文件下载到本地
           request.downloadFile(this.context, {
             url: url,
             filePath: filePath
           }).then((downloadTask: request.DownloadTask) => {
             // 下载完成回调
             downloadTask.on('complete', () => {
               console.info('download complete');
               let uri = fileUri.getUriFromPath(filePath);
               let fileInfo: filePreview.PreviewInfo = {
                 title: 'sample.pdf',
                 uri: uri,
                 mimeType: 'application/pdf',
               };
               // 打开文件预览
               filePreview.openPreview(this.context, fileInfo).then(() => {
                 console.info('Succeeded in opening preview');
               }).catch((err: BusinessError) => {
                 console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
               });
             });
           }).catch((err: BusinessError) => {
             console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
           });
         }
       } catch (error) {
         let err: BusinessError = error as BusinessError;
         console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
       }
     }
     // End solution3

     build() {
       Column() {
         Button('预览rawfile pdf文件')
           .onClick(() => {
             this.previewRawFile();
           })
           .width('70%')
           .margin({ bottom: 20 });

         Button('预览沙箱pdf文件')
           .onClick(() => {
             this.previewLocalFile();
           })
           .width('70%')
           .margin({ bottom: 20 });

         Button('预览网络pdf文件')
           .onClick(() => {
             this.previewNetworkFile();
           })
           .width('70%')
           .margin({ bottom: 20 });
       }
       .height('100%')
       .width('100%')
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

注意事项：

* 当前Preview Kit仅支持跳出应用进行文件的预览，暂不支持应用内预览。
* Office类型文档预览借助WPS提供的能力来实现，在预览文档类型文件时会存在"WPS提供技术支持"、"使用WPS Office打开"等相关字样。
* 当前Preview Kit暂不支持安全定制能力，包括禁止截录屏、屏蔽其他应用打开入口、屏蔽分享入口等安全预览能力。
* 当前Preview Kit需要调用方存在对应uri的转授权能力，从而让预览获得该文件的访问权限来正常读取文件，具体问题可以参考[使用DocumentViewPicker拿到的uri通过openPreview打开显示预览失败](../harmonyos-guides/preview-faq-2.md)。
* 在封装[PreviewInfo](../harmonyos-references/preview-arkts.md#previewinfo)的mineType参数时，若无法确定文件格式，该项可直接赋值空字符串（""），系统会通过uri后缀进行文件格式判断。
* [canPreview](../harmonyos-references/preview-arkts.md#canpreview)根据文件的uri判断文件是否可预览，当传入支持的文件uri时，会返回true；传入不可预览的文件uri时，返回false。当前接口仅针对文件是否存在以及文件格式是否为支持的文件类型进行检验，后续openPreview进行文件查看时需要调用方保证文件可以被转授权。

## 常见FAQ

Q：模拟器是否支持Preview Kit文件预览？

A：当前Preview Kit支持模拟器开发，但与真机存在部分能力差异，详情请见[模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)列表。

Q：预览mp4文件时，通过[uniformTypeDescriptor.getTypeDescriptor](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformtypedescriptorgettypedescriptor11)获取的mimeType为video/mp4，video/mp4v，能否直接作为PreviewInfo的mimeType参数？

A：预览mp4文件时，mimeType参数需要为video/mp4，见[文件预览支持的文件类型](../harmonyos-guides/preview-introduction.md#文件预览支持的文件类型)。

Q：使用filePreview预览文件时，能否关闭分享入口、关闭"使用WPS打开"入口以及添加水印，防止文件被上传或泄露到其他地方？

A：当前Preview Kit暂不支持安全定制能力，包括关闭分享入口、屏蔽其他应用打开入口、添加水印等安全预览能力。如需实现应用内安全预览，建议使用三方SDK（如WPS等）提供应用内打开能力。

## 总结

[Preview Kit（文件预览服务）](../harmonyos-guides/preview-kit-guide.md)为文件预览提供了统一的解决方案：

1. **统一接口**：无论文件来源如何，都可使用filePreview.[openPreview](../harmonyos-references/preview-arkts.md#openpreview)接口。
2. **格式丰富**：支持常见办公文档、图片、文本等格式。
3. **权限管理**：需要确保应用有相应文件的访问权限。

实际开发中应根据具体场景选择合适的预览方式，并处理好错误情况和用户权限问题。对于敏感文件，还应该增加额外的安全验证机制。
