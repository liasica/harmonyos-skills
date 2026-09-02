---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-127
title: 如何通过Rcp跳过HTTPS证书验证以及传递请求体实现文件下载
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何通过Rcp跳过HTTPS证书验证以及传递请求体实现文件下载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4b62ecb38a4c5d2cffd1600726d3383da2a4f9c6977b581f1b7bf7477e8b9cdf
---

## 问题现象

在下载文件时使用HTTPS请求，需要通过请求体（Request Body）传递参数给服务端。服务端根据请求体参数鉴权通过后，将文件通过响应体返回给客户端。

由于request.agent和rcp.DownloadToFile均不支持传请求体（Request Body）。服务端鉴权不通过，无法完成下载；并且无HTTPS证书，需要跳过证书验证。

## 背景知识

[Remote Communication Kit](../harmonyos-guides/remote-communication-kit-guide.md)提供请求网络数据的功能，当前包含以下能力：

* HTTP请求能力。Remote Communication Kit构建了一种场景化HTTP通信能力。和Network Kit提供的标准HTTP能力不同的是，Remote Communication Kit构建了场景化API，强调易用性，详见[支持的HTTP网络请求场景](../harmonyos-guides/remote-communication-introduction.md#支持的http网络请求场景)。开发者可根据需要选择合适的Kit。
* URPC（Unified Remote Procedure Call）高性能RPC通信库。可实现远程函数调用能力，且具有抗弱网传输、多径传输（蜂窝网络和Wi-Fi）等特性。开发者可通过URPC完成简单方便的远程过程调用。

[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)：文件选择器对象，用来支撑选择和保存各种格式文档。

## 解决方案

1. 通过RCP请求，跳过证书验证、传递请求体获取文件的数据。
2. 通过DocumentViewPicker将获取到的文件数据保存到本地。

示例代码如下：

```ts
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
import fs from '@ohos.file.fs';

@Entry
@Component
struct Index {
  downloadFile(fileName: string) {
    let url: string = 'xxxx://xxxxxxxx/xxxxxx';
    let headers: rcp.RequestHeaders = {
      'content-type': 'application/json',
      'xxxxxx': 'xxxxxx'
    };
    const postContent =
      `{'xxxxxx':'xxxxxx', 'xxxxxx':'xxxxxx', 'xxxxxx':'xxxxxx'}`;
    let req = new rcp.Request(url, 'POST', headers, postContent);
    req.configuration = {
      security: {
        remoteValidation: 'skip'
      }
    };

    const session = rcp.createSession();
    session.fetch(req).then(async (response) => {
      let reqBody = response.body;
      const documentSaveOptions = new picker.DocumentSaveOptions();
      documentSaveOptions.newFileNames = [fileName];
      let uris: Array<string> = [];
      const documentViewPicker = new picker.DocumentViewPicker();
      documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
        if (documentSaveResult.length === 0) {
          console.error('未保存任何文件');
          return;
        }
        uris = documentSaveResult;
        let uri = uris[0];
        let file: fs.File = fs.openSync(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
        try {
          if (!reqBody) {
            console.error('响应体为空');
            return;
          }
          fs.writeSync(file.fd, reqBody!);
          this.getUIContext().getPromptAction().showToast({message:`文件保存成功${file.path}}`});
        } finally {
          if (file) {
            fs.closeSync(file);
          }
        }

      }).catch((err: BusinessError) => {
        console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
      });
    }).catch((err: BusinessError) => {
      console.error(`err: err code is ${err.code}, err message is ${err.message}`);
    });
  }

  build() {
    Column() {
      Button('文件下载')
        .onClick(() => {
          this.downloadFile('测试文件.pdf');
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
