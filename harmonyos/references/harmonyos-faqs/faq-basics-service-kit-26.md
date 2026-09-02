---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-26
title: 实现文件下载并打开分享功能
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 实现文件下载并打开分享功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0c6375aecf9f4f8020d7bd536a93cc53972b423cfd045a62e50647f746475b62
---

## 问题现象

对于文件下载并分享给三方，是应用开发过程中常见的一类场景，那么，如何实现文件下载并打开分享功能呢？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/2wG0fFHGRlC0fqu5bzBlng/zh-cn_image_0000002628613416.png "点击放大")

## 背景知识

* 开发者可以使用上传下载模块（[ohos.request](../harmonyos-references/js-apis-request.md)）的下载接口将网络资源文件下载到应用文件目录。
* 对已下载的网络资源文件，开发者可以使用基础文件IO接口（[ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)）对其进行访问，使用方式与应用文件访问一致。
* 通过[文件URI](../harmonyos-references/js-apis-file-fileuri.md)模块可以获取文件统一资源标志符（Uniform Resource Identifier，URI）。
* [系统分享服务](../harmonyos-references/share-system-share.md)提供分享数据创建及分享面板拉起的功能。

## 解决方案

实现文件下载并打开分享功能可参考如下流程进行：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/h32pDyW9RZ-O2eTY6MZOWA/zh-cn_image_0000002658852697.png "点击放大")

各步骤实现样例参考如下：

* 可根据业务需要自行确定文件的下载路径，以下是创建待下载文件沙箱保存路径样例：

  ```ts
  //创建/down_export目录
  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let cacheDir = context.cacheDir;
    this.dirPath = cacheDir + '/down_export';
    fs.mkdir(this.dirPath).then(() => {
      console.info('mkdir succeed');
    }).catch((err: BusinessError) => {
      console.error('mkdir failed with error message: ' + err.message + ', error code: ' + err.code);
    });
    //文件名称、文件所在的沙箱路径
  }
  ```
* 可根据业务需要对下载文件进行命名，以下是获取当前时间，使用当前时间和文件后缀命名文件：

  ```ts
  //获取当前时间
  getTime() {
    let date = new Date();
    let year = date.getFullYear();
    // 月份从0开始，所以需要加1
    let month = date.getMonth() + 1;
    let day = date.getDate();
    let hour = date.getHours();
    let minute = date.getMinutes();
    let seconds = date.getSeconds();
    this.fileName = `${year}${month}${day}${hour}${minute}${seconds}.pdf`;
  }
  ```
* 拉起分享页面：

  ```ts
  //调起分享页面
  shareData(context: common.UIAbilityContext, uri: string) {
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PDF,
      content: this.fileName,
      uri: uri
    });
    let controller: systemShare.ShareController = new systemShare.ShareController(data);
    controller.on('dismiss', () => {
      // 分享结束，可处理其他业务。
    });
    // 进行分享面板显示
    controller.show(context, {
      previewMode: systemShare.SharePreviewMode.DETAIL,
      selectionMode: systemShare.SelectionMode.SINGLE
    });
  }
  ```
* 下载文件并分享文件：

  ```ts
  downLoad2Share() {
    // 获取UIContext
    const uiContext = this.getUIContext();
    // 通过UIContext获取PromptAction实例
    const promptAction = uiContext.getPromptAction();
    let context = uiContext.getHostContext() as common.UIAbilityContext;
    this.getTime();
    this.filePath = this.dirPath + '/' + this.fileName;
    try {
      // 判断是否已下载过文件
      let res = fs.accessSync(this.filePath);
      if (res) {
        promptAction.showToast({
          message: '文件已存在'
        });
        let uri = fileUri.getUriFromPath(this.filePath);
        this.shareData(context, uri);
      } else {
        // 此处地址实际使用过程中替换为真实地址
        let url = 'xx://xx.xx.xx/xxxx.pdf';
        // 下载文件
        request.downloadFile(context, {
          // 替换下载地址
          url: url,
          // 文件下载后保存的沙箱路径
          filePath: this.filePath
        }).then((downloadTask: request.DownloadTask,) => {
          let progressCallback = (receivedSize: number, totalSize: number) => {
            this.progress = ((receivedSize / totalSize) * 100).toFixed(2);
            promptAction.showToast({
              message: `下载进度:${this.progress}%`,
              duration: this.showProgress,
            });
          };
          downloadTask.on('progress', progressCallback);
          // 开启回调
          downloadTask.on('complete', () => {
            this.showProgress = 0;
            let uri = fileUri.getUriFromPath(this.filePath);
            promptAction.showToast({
              message: `下载完成，存储目录：${uri}`
            });
            this.shareData(context, uri);
          });
        }).catch((err: BusinessError) => {
          // 下载请求失败回调，可以弹窗提示失败
          if (err.code == 13900015) {
            console.info('目录已存在');
          } else {
            console.info(JSON.stringify(err));
          }
        });
      }
    } catch (error) {
      // 下载请求失败回调，可以弹窗提示失败
      let err: BusinessError = error as BusinessError;
      console.error(`Invoke downloadTask downloadFile failed, code is ${err.code}, message is ${err.message}`);
    }
  }
  ```

完整代码如下：

```ts
import common from '@ohos.app.ability.common';
import fs from '@ohos.file.fs';
import { BusinessError } from '@kit.BasicServicesKit';
import fileUri from '@ohos.file.fileuri';
import request from '@ohos.request';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare } from '@kit.ShareKit';

@Entry
@Component
struct DownloadAndShare {
  @State showProgress: number = -1;
  @State progress: string = '0';
  @State fileName: string = '';
  @State filePath: string = '';
  @State dirPath: string = '';

  //创建/down_export目录
  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let cacheDir = context.cacheDir;
    this.dirPath = cacheDir + '/down_export';
    fs.mkdir(this.dirPath).then(() => {
      console.info('mkdir succeed');
    }).catch((err: BusinessError) => {
      console.error('mkdir failed with error message: ' + err.message + ', error code: ' + err.code);
    });
    //文件名称、文件所在的沙箱路径
  }

  //获取当前时间
  getTime() {
    let date = new Date();
    let year = date.getFullYear();
    // 月份从0开始，所以需要加1
    let month = date.getMonth() + 1;
    let day = date.getDate();
    let hour = date.getHours();
    let minute = date.getMinutes();
    let seconds = date.getSeconds();
    this.fileName = `${year}${month}${day}${hour}${minute}${seconds}.pdf`;
  }

  //调起分享页面
  shareData(context: common.UIAbilityContext, uri: string) {
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PDF,
      content: this.fileName,
      uri: uri
    });
    let controller: systemShare.ShareController = new systemShare.ShareController(data);
    controller.on('dismiss', () => {
      // 分享结束，可处理其他业务。
    });
    // 进行分享面板显示
    controller.show(context, {
      previewMode: systemShare.SharePreviewMode.DETAIL,
      selectionMode: systemShare.SelectionMode.SINGLE
    });
  }

  downLoad2Share() {
    // 获取UIContext
    const uiContext = this.getUIContext();
    // 通过UIContext获取PromptAction实例
    const promptAction = uiContext.getPromptAction();
    let context = uiContext.getHostContext() as common.UIAbilityContext;
    this.getTime();
    this.filePath = this.dirPath + '/' + this.fileName;
    try {
      // 判断是否已下载过文件
      let res = fs.accessSync(this.filePath);
      if (res) {
        promptAction.showToast({
          message: '文件已存在'
        });
        let uri = fileUri.getUriFromPath(this.filePath);
        this.shareData(context, uri);
      } else {
        // 此处地址实际使用过程中替换为真实地址
        let url = 'xx://xx.xx.xx/xxxx.pdf';
        // 下载文件
        request.downloadFile(context, {
          // 替换下载地址
          url: url,
          // 文件下载后保存的沙箱路径
          filePath: this.filePath
        }).then((downloadTask: request.DownloadTask,) => {
          let progressCallback = (receivedSize: number, totalSize: number) => {
            this.progress = ((receivedSize / totalSize) * 100).toFixed(2);
            promptAction.showToast({
              message: `下载进度:${this.progress}%`,
              duration: this.showProgress,
            });
          };
          downloadTask.on('progress', progressCallback);
          // 开启回调
          downloadTask.on('complete', () => {
            this.showProgress = 0;
            let uri = fileUri.getUriFromPath(this.filePath);
            promptAction.showToast({
              message: `下载完成，存储目录：${uri}`
            });
            this.shareData(context, uri);
          });
        }).catch((err: BusinessError) => {
          // 下载请求失败回调，可以弹窗提示失败
          if (err.code == 13900015) {
            console.info('目录已存在');
          } else {
            console.info(JSON.stringify(err));
          }
        });
      }
    } catch (error) {
      // 下载请求失败回调，可以弹窗提示失败
      let err: BusinessError = error as BusinessError;
      console.error(`Invoke downloadTask downloadFile failed, code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('下载文件并分享')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.downLoad2Share();
          });
      }
      .height('20%');
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：文件下载到沙箱失败，报错Invoke downloadFile failed，code is 13400003。

A：在使用request.downloadFile()接口时，需要保证存储下载文件的父级路径必须存在。

Q：使用request.downloadFile()下载文件，使用的非文件后缀结尾的url，下载成功后文件无法查看。

A：使用request.downloadFile()下载后的沙箱文件默认文件名从url的最后一个"/"后截取，使用非文件后缀结尾的url则下载后的沙箱文件不是一个正常的文件名，故无法正常查看。可以在下载任务的配置信息[DownloadConfig](../harmonyos-references/js-apis-request.md#downloadconfig)中设置下载路径filePath，示例代码如下：

```screen
import { request } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Page {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    RelativeContainer() {
      Button('点击下载')
        .onClick(() => {
          request.downloadFile(this.context, {
            url: 'https://xxx/test.pdf?parama=a',
            filePath: this.context.cacheDir + '/test.pdf',
            header: {
              'User-Agent': '',
            },
          }).then((data: request.DownloadTask) => {
            console.info('data=', data);
          });
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
