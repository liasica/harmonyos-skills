---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-120
title: 下载过程中如何获取真实文件名
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 下载过程中如何获取真实文件名
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6656a316afb7a3792a019bd48d1af59ce9a86e513dc5e3f85853e70258acba88
---

## 问题现象

下载文件url时，需要知道文件类型用来进行预览文件，以及文件名用来判断是否存在相同文件，有些下载链接直接可以显示文件名，有些因为安全、存储机制等原因无法直接显示文件名，提供的是文件请求地址，如何在下载过程中获取文件名。

## 背景知识

* [ohos.request](../harmonyos-references/js-apis-request.md)模块主要给应用提供上传下载文件、后台传输代理的基础能力。
* [getTaskInfo(): Promise<DownloadInfo>](../harmonyos-references/js-apis-request.md#gettaskinfo9)接口查询下载任务的信息，异步方法，使用Promise形式返回DownloadInfo里的信息。
* [DownloadInfo](../harmonyos-references/js-apis-request.md#downloadinfo7)下载任务信息包含文件名信息等。

## 解决方案

通过request.downloadFile()下载任务过程中使用downloadTask.getTaskInfo()接口获取DownloadInfo信息，从而获取文件名fileName。

```ts
import { BusinessError, request } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('Hello World')
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let context = this.getUIContext().getHostContext();
          try {
            // 需要手动将url替换为真实服务器的HTTP协议地址
            request.downloadFile(context, { url: 'xxx.xxx.xxx' }).then((data: request.DownloadTask) => {
              let downloadTask: request.DownloadTask = data;
              downloadTask.getTaskInfo().then((downloadInfo: request.DownloadInfo) => {
                console.info('Succeeded in querying the download task');
                console.info(`filename:  ${downloadInfo.fileName}`);
              }).catch((err: BusinessError) => {
                console.error(`Failed to query the download task. Code: ${err.code}, message: ${err.message}`);
              });
            }).catch((err: BusinessError) => {
              console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
            });
          } catch (err) {
            console.error(`Failed to request the download. err: ${JSON.stringify(err)}`);
          }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
