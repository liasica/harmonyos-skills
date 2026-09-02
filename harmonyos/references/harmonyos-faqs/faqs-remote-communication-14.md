---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-14
title: RCP下载进度监听
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > RCP下载进度监听
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4864e672012184a3ef4a7514ba150b50cbaf4ca83f10547dc71248e3d527f9cd
---

## 问题现象

RCP进行文件下载时，如何对下载进度实时监听？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JTiYw05CRq-LOP658KiVsA/zh-cn_image_0000002658851747.png "点击放大")

## 解决方案

使用[OnDownloadProgress](../harmonyos-references/remote-communication-rcp.md#ondownloadprogress)接口实时监听下载进度，回调函数会返回三个参数：

* totalSize：要下载文件的总大小（number类型）。
* transferredSize：已下载文件大小（number类型）。
* request：触发回调的HTTP请求。

以下为文件下载进度监听案例：

```ts
import rcp from '@hms.collaboration.rcp';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct ProgressListen {
  @State progress: number = 0;
  downloadUrl: string = 'xxxxxxx'; // 需更换为真实地址
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  filePath = `${this.context.filesDir}/test.png`;

  build() {
    Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Column({ space: 16 }) {
        Button('下载文件').onClick(() => {
          this.getDownloadProgress(this.downloadUrl);
        });
        Column({ space: 16 }) {
          Flex({ justifyContent: FlexAlign.SpaceBetween }) {
            Text('downloadProgress');
            Text(this.progress.toFixed(2) + '%');
          };

          Progress({ value: 0, total: 100, type: ProgressType.Linear }).value(this.progress).color('#0A59F7');
        }.width('90%').height(50);
      };
    }
    .height('100%')
    .width('100%');
  }

  // 下载文件监听进度
  getDownloadProgress(url: string) {
    const customHttpEventsHandler: rcp.HttpEventsHandler = {
      onDownloadProgress: (totalSize: number, transferredSize: number) => {
        this.progress = transferredSize / totalSize * 100;
      },

      // 数据完成接收监听
      onDataEnd: () => {
        console.info('Data transfer complete');
      },

      // 取消数据接收监听
      onCanceled: () => {
        console.info('Request/response canceled');
      },
    };

    // TracingConfiguration用于获取请求期间详细信息
    const tracingConfig: rcp.TracingConfiguration = {
      verbose: true,
      collectTimeInfo: true,
      httpEventsHandler: customHttpEventsHandler,
    };

    let session = rcp.createSession({
      requestConfiguration: {
        tracing: tracingConfig
      }
    });

    // 下载文件
    session.downloadToFile(url, { kind: 'file', file: this.filePath }).then(() => {
      session.close();
    }).catch(() => {
      session.close();
    });
  }
}
```
