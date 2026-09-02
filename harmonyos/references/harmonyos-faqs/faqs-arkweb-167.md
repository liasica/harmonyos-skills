---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-167
title: Web如何拦截网页加载错误并重新加载指定页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web如何拦截网页加载错误并重新加载指定页面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc475ae45316e046831580598b79026cc6f1256e0d64ad36a7ea74e6f402be2a
---

## 问题现象

在Web中加载H5页面时，若页面加载出错，如何拦截错误、切换页面，并触发重新加载H5页面？

## 背景知识

* [onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)：网页资源加载遇到错误或无网络时会触发该回调；
* [javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)：提供了从前端页面调用应用侧ArkTS功能的通道。

## 解决方案

1. ArkTS侧实现加载H5页面的功能，并通过javaScriptProxy接口给H5注入对应的对象和方法，以便H5侧能调用；
2. 使用ArkWeb的onErrorReceive回调拦截网页加载错误，在该回调中加载本地H5页面；

   代码如下：

   ```ts
   import { webview } from '@kit.ArkWeb';

   const WEB_URL: string | Resource = 'www.example.com';

   class WebManager {
     private controller?: webview.WebviewController;

     constructor(controller: webview.WebviewController) {
       this.controller = controller;
     }

     refresh() {
       this.controller?.loadUrl(WEB_URL);
     }
   }

   @Entry
   @Component
   struct WebRefreshDemo {
     webController: webview.WebviewController = new webview.WebviewController;
     webManager: WebManager = new WebManager(this.webController);

     aboutToAppear(): void {
     }

     build() {
       Column() {
         Web({ src: WEB_URL, controller: this.webController })
           .javaScriptProxy({
             object: this.webManager,
             name: 'WebManager',
             methodList: ['refresh'],
             controller: this.webController,
           })
           .fileAccess(false)
           .domStorageAccess(true)
           .geolocationAccess(false)
           .onErrorReceive((event) => {
             console.error(`getErrorInfo: ${event.error.getErrorInfo()}`);
             console.error(`getErrorCode: ${event.error.getErrorCode()}`);
             this.webController.loadUrl($rawfile('webRefresh.html'));
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
3. 在加载的本地H5侧调用该重新加载的方法，加载目标网页地址，H5代码如下：

   ```html
   <!DOCTYPE html>
   <html lang="zh-CN">
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover"/>
   <body>
   <div class="main-page" onclick="refresh()">
       <div><img class="error-img" src="./errorImg.png"/></div>
       <div><span class="refresh-text">当前无网络连接，请点击空白处刷新页面</span></div>
   </div>
   </body>
   </html>
   <script>
       function refresh() {
         console.info('refresh')
         return window.WebManager.refresh()
       }
   </script>

   <style>
       * {
           margin: 0;
           padding: 0;
           box-sizing: border-box;
           font-family: sans-serif;
       }
       html {
          height: 100%;
       }
       body {
           background-color: #f8f8f8;
           padding: 20px;
           height: 100%;
       }
       .main-page {
           width: 100%;
           height: 100%;
           display: flex;
           flex-direction: column;
           align-items: center;
           justify-content: center;
       }
       .error-img {
           width: 120px;
           height: 120px;
       }
       .refresh-text {
          font-size: 14px;
          line-height: 16px;
       }
   </style>
   ```

   **说明** 

   访问在线网页时需添加网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 总结

在网页资源加载遇到问题时，可以通过onErrorReceive回调拦截到网页资源加载错误，在该回调中实现重新加载页面，或引导用户稍后尝试等功能。
