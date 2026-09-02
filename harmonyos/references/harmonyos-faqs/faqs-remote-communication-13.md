---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-13
title: RCP下载文件，会重复回调同一个进度，如何解决
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > RCP下载文件，会重复回调同一个进度，如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:27778703947add5617704630425be091598e429d6ca4823c95a264af7799e2bc
---

## 问题现象

使用RCP接口下载文件，onDownloadProgress会重复回调同一个进度，导致业务逻辑重复执行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/UGBRbAeHR9SMgcqhPcymbg/zh-cn_image_0000002628612488.png "点击放大")

## 背景知识

* 通过[downloadToFile](../harmonyos-references/remote-communication-rcp.md#downloadtofile)接口下载文件，会在[onDownloadProgress](../harmonyos-references/remote-communication-rcp.md#ondownloadprogress)回调中返回当前下载进度，该接口需要配置ohos.permission.INTERNET权限，如果使用[PathPreference](../harmonyos-references/remote-communication-rcp.md#pathpreference)的'cellular'模式，则额外需要ohos.permission.GET\_NETWORK\_INFO权限。
* [onHeaderReceive](../harmonyos-references/remote-communication-rcp.md#onheaderreceive)回调中可以通过content-length获取下载文件的总长度。
* [onDataReceive](../harmonyos-references/remote-communication-rcp.md#ondatareceive)回调可以获取到当前返回内容的长度。

## 解决方案

* **方案一**：

  5.0系统版本，onDownloadProgress存在冗余回调bug，5.1及以上系统版本已经修复该问题，可升级系统至5.1以上版本。
* **方案二**：

  业务侧可通过文件总大小和当前已接收的文件大小计算下载进度：

  ```ts
  import rcp from '@hms.collaboration.rcp';

  @Entry
  @Component
  struct Index {
    @State curValue: number = 0;
    @State totalData: number = 0;
    @State progress: number = 0;
    @State enableDownload: boolean = true;
    // 需要替换成实际的url
    downloadUrl: string = '';

    build() {
      Column({ space: 20 }) {
        Progress({ value: this.curValue, total: this.totalData, type: ProgressType.Capsule })
          .width(200)
          .height(40)
          .style({ enableSmoothEffect: true, content: this.progress.toFixed(2) + '%' });

        Button('点击开始下载')
          .onClick(() => {
            this.enableDownload = false;
            this.curValue = 0;
            this.progress = 0;
            // 下载文件数据
            this.startDownload(this.downloadUrl);
          })
          .enabled(this.enableDownload);
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }

    // 下载文件
    startDownload(url: string) {
      // 响应数据处理
      const eventsHandler: rcp.HttpEventsHandler = {
        onHeaderReceive: (headers: rcp.ResponseHeaders) => {
          this.totalData = Number(headers['content-length']);
        },
        onDataReceive: (incomingData: ArrayBuffer) => {
          this.curValue += incomingData.byteLength;
          this.progress = (this.curValue / this.totalData) * 100;
          console.info('Download progress:', this.curValue, 'of', this.totalData);
        },
        // 数据完成接收监听
        onDataEnd: () => {
          console.info('Data transfer complete');
          this.enableDownload = true;
        },
        // 取消数据接收监听
        onCanceled: () => {
          console.info('Request/response canceled');
        },
      };
      // 建立session对象
      let session = rcp.createSession({
        requestConfiguration: {
          tracing: {
            verbose: true,
            collectTimeInfo: true,
            httpEventsHandler: eventsHandler,
          }
        }
      });
      session.downloadToFile(url, {
        kind: 'file',
        file: `${this.getUIContext().getHostContext()?.filesDir}/test`,
      }).then((response) => {
        console.info(`Download result ${response.toJSON()}`);
        session.close();
      }).catch((err: Error) => {
        console.error(`${JSON.stringify(err)}`);
        session.close();
      });
    }
  }
  ```
