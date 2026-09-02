---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-144
title: 如何实现仅wifi网络时加载图片
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何实现仅wifi网络时加载图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b6f7fcf87acb8b8a7a5fbf18ee03cc36119dc268022cb7b20679c1f1ac7bc63a
---

## 问题现象

如何实现应用内设置仅wifi网络时加载图片的功能。

## 背景知识

* [connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)：获取netHandle对应网络的能力信息。
  + 该接口返回[NetCapabilities](../harmonyos-references/js-apis-net-connection.md#netcapabilities)网络能力信息，其中bearerTypes字段表示网络类型[NetBearType](../harmonyos-references/js-apis-net-connection.md#netbeartype)数组，且数组里面只包含了一种网络类型。
  + 该接口需要配置ohos.permission.GET\_NETWORK\_INFO权限才能使用。
* [onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)：当Web组件加载url之前触发该回调，用于拦截url并返回响应数据。
  + onInterceptRequest可以拦截所有跳转，需要根据具体业务去做判断。
  + 返回值[WebResourceResponse](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md)。返回响应数据则按照响应数据加载，无响应数据则返回null表示按照原来的方式加载。
* [getRawFileContentSync](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontentsync10)：获取resources/rawfile目录下对应的rawfile文件内容。

## 解决方案

设置仅wifi加载图片后，应用加载页面内容之前，建议先通过connection.getNetCapabilities接口判断设备当前网络类型，然后再处理不同场景下的图片加载。

* 使用Image组件加载网络图片，设置仅wifi加载图片后，直接加载resources/rawfile目录下或者resources/base/media目录下的图片代替网络图片即可。
* 使用Web组件加载网络页面，设置仅wifi加载图片后，可以使用onInterceptRequest拦截，然后自定义WebResourceResponse构造数据。比如使用fs从rawfile目录中读取本地图片资源到沙箱，再通过setResponseData返回给网页。

示例代码如下：

```ts
import { fileIo as fs } from '@kit.CoreFileKit';
import common from '@ohos.app.ability.common';
import webview from '@ohos.web.webview';
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  webviewController: webview.WebviewController = new webview.WebviewController();
  webResourceResponse: WebResourceResponse = new WebResourceResponse();
  fileName: string = 'test.jpg'; // 根据实际情况，换成业务需要的图片，放在rawfile目录下，需要的时候拷贝到沙箱后使用
  @State isWifiInUse: boolean = false;
  pageUrl: string = 'www.example1.com'; // 根据实际情况，换成业务需要的网页url
  imageUrl: string = 'www.example2.jpg'; // 根据实际情况，换成业务需要的图片url

  aboutToAppear(): void {
    connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
      if (netHandle.netId == 0) {
        // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
        return;
      }
      connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
        if (error) {
          console.error(`Failed to get net capabilities. Code:${error.code}, message:${error.message}`);
          return;
        }
        for (let i = 0; i < data.bearerTypes.length; i++) {
          // 判断设备是否连接wifi网络
          if (data.bearerTypes[i] == connection.NetBearType.BEARER_WIFI) {
            this.isWifiInUse = true;
          }
        }
      });
    }).catch((error: BusinessError) => {
      console.error(JSON.stringify(error));
    });
  }

  // 将rawfile下的文件读取到沙箱
  async saveFileToSandbox(fileName: string) {
    const filePath = this.context.filesDir + '/' + fileName;
    try {
      const file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
      const content = this.context.resourceManager.getRawFileContentSync(fileName);
      const arrayBuffer = content.buffer.slice(0);
      fs.writeSync(file.fd, arrayBuffer);
      fs.closeSync(file.fd);
    } catch (error) {
      console.error(`Code: ${error.code},Message: ${error.message} `);
    }
  }

  async getLocalImage(fileName: string) {
    const filePath = this.context.filesDir + '/' + fileName;
    try {
      this.saveFileToSandbox(fileName);
      let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
      return file.fd;
    } catch (error) {
      console.error(`Code: ${error.code},Message: ${error.message} `);
      return null;
    }
  }

  build() {
    Column() {
      // 场景一：本地Image组件加载网络图片
      Image(this.isWifiInUse ? this.imageUrl : $rawfile(this.fileName))
        .width(100);

      // 场景二：Web组件加载网络页面
      Web({ src: this.pageUrl, controller: this.webviewController })
        .fileAccess(true)
        .javaScriptAccess(true)
        .domStorageAccess(true) // 设置是否开启文档对象模型存储接口（DOM Storage API）权限，默认未开启。
        .overviewModeAccess(true)
        .geolocationAccess(false)
        .onInterceptRequest((event) => {
          if (!this.isWifiInUse) {
            const url = event!.request.getRequestUrl();
            // 可自行添加常见的图片资源类型的判断
            if (!url.includes('jpg') && !url.includes('png') && !url.includes('jpeg') && !url.includes('bmp') &&
              !url.includes('gif')) {
              return null;
            }
            try {
              this.getLocalImage(this.fileName).then(fd => {
                this.webResourceResponse.setResponseData(fd);
                this.webResourceResponse.setResponseCode(200);
                this.webResourceResponse.setReasonMessage('OK');
                this.webResourceResponse.setResponseIsReady(true);
                fs.closeSync(fd);
              });
              this.webResourceResponse.setResponseMimeType('image/*');
              this.webResourceResponse.setResponseIsReady(false);
              return this.webResourceResponse;
            } catch (error) {
              console.error(`Code: ${error.code},Message: ${error.message} `);
              return null;
            }
          } else {
            return null;
          }
        });
    }
    .height('100%');
  }
}
```
