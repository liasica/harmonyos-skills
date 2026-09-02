---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-150
title: Web组件如何实现屏幕共享功能
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何实现屏幕共享功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:16045befc8ddb74816c411c3ae3f0a348ca15d504089d962c9ecfefd55419e29
---

## 问题现象

Web组件加载的H5中使用navigator.mediaDevices.getDisplayMedia后出现没有权限的问题，如何实现屏幕共享功能？

## 背景知识

* 当H5中的JavaScript代码调用getDisplayMedia尝试进行屏幕捕获时，会触发Web组件的[onScreenCaptureRequest](../harmonyos-references/arkts-basic-components-web-events.md#onscreencapturerequest10)回调。
* [grant](../harmonyos-references/arkts-basic-components-web-screencapturehandler.md#grant10)：对网页访问的屏幕捕获操作进行授权。
* [deny](../harmonyos-references/arkts-basic-components-web-screencapturehandler.md#deny10)：拒绝网页所请求的屏幕捕获操作。

## 解决方案

在H5中调用getDisplayMedia发起屏幕共享，触发Web组件中onScreenCaptureRequest回调，在回调中通过event.handler.grant完成屏幕捕获权限申请。

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Row() {
        Button('refresh')
          .onClick(() => {
            try {
              this.controller.refresh();
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
      };

      Row() {
        Web({
          src: $rawfile('screenCapture.html'), controller: this.controller
        })
          .domStorageAccess(true)
          .databaseAccess(true)
          .imageAccess(true)
          .onlineImageAccess(true)
          .javaScriptAccess(true)
          .geolocationAccess(false)
          .fileAccess(false)
          .onScreenCaptureRequest((event) => {
            if (!event) {
              return;
            }
            console.info(`on onScreenCaptureRequest Origin:  ${(event.handler.getOrigin())}`);
            this.uiContext.showAlertDialog({
              title: 'title',
              message: '请求权限' + event.handler.getOrigin(),
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.handler.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.handler.grant({ captureMode: WebCaptureMode.HOME_SCREEN });
                }
              },
              cancel: () => {
                event.handler.deny();
              }
            });
          });
      };
    };
  }
}
```

screenCapture.html：

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        #video {
            width: 200px;
            height: 400px;
            border: 2px solid red;
        }
    </style>
</head>
<body>
<script>
    function share() {
        navigator.mediaDevices.getDisplayMedia({video: true}).then(stream => {
            document.getElementById('res').innerText = '';
            // 创建一个video元素
            let video = document.getElementById('video');
            // 设置video元素的srcObject为获取到的流
            video.srcObject = stream;
            video.play();
        }).catch(res => {
            document.getElementById('res').innerText = res;
        })
    }
</script>
<button onclick="share()">投屏</button>
<video id="video"></video>
<span id="res"></span>
</body>
</html>
```
