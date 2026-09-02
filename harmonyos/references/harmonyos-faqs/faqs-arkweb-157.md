---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-157
title: Web组件加载网页如何获取网页的标题及标题来源
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件加载网页如何获取网页的标题及标题来源
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f05bc64fcbf325357f3693e1b5020fd3f9de2f64998e6a610a55a5cffca7ae91
---

## 问题现象

Web组件加载网页可以通过什么方式获取网页的标题以及标题来源？

## 背景知识

* [onTitleReceive](../harmonyos-references/arkts-basic-components-web-events.md#ontitlereceive)：当页面文档标题<title>元素发生变更时，触发回调。若当前页面未显示设置标题，ArkWeb将在加载完成前基于页面的URL生成标题并返回给应用。
* [getTitle](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#gettitle)：获取当前网页的标题。
* [OnTitleReceiveEvent](../harmonyos-references/arkts-basic-components-web-i.md#ontitlereceiveevent12)：定义网页document标题更改时触发该回调。

## 解决方案

1. 获取网页标题来源：

   onTitleReceive的callback回调参数OnTitleReceiveEvent中的isRealTitle表示document标题来源，true表示来自网页的title标签，false表示该title是根据URL自动生成，默认返回为false。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebComponent {
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Web({ src: 'www.example.com', controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
           .domStorageAccess(true)
           .onTitleReceive((event) => {
             if (event) {
               console.info(`title:${event.title}, is from title: ${event?.isRealTitle}`);
             } else {
               console.error('onTitleReceive callback error');
             }
           });
       };
     }
   }
   ```
2. 根据场景，获取网页标题有以下三种方式：
   * 如果当前网页标题发生了改变，可以在onTitleReceive事件中直接获取。
   * 如果是正常网页加载，可以在[onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)中使用getTitle获取网页的标题。
   * 通过[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)执行JavaScript代码来获取文档的标题。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct Index {
     wController: webview.WebviewController = new webview.WebviewController();
     @State url: string = 'xxx'; // 实际场景请替换为可访问地址

     build() {
       Column() {
         Column() {
           Web({ src: this.url, controller: this.wController })
             .geolocationAccess(false)
             .fileAccess(true)
             .javaScriptAccess(true)
             .domStorageAccess(true) // 设置是否开启文档对象模型存储接口（DOM Storage API）权限，默认未开启。
             .overviewModeAccess(true)
             .verticalScrollBarAccess(false)
             .onTitleReceive((event) => {
               if (event) {
                 // 方式一：在onTitleReceive回调中获取标题，只有当网页标题发生变化时触发
                 console.info(`onTitleReceive title: ${event.title}`);
               }
             })
             .onPageEnd(() => {
               // 方式二：在onPageEnd回调中使用getTitle获取标题
               console.info('onPageEnd title：', this.wController.getTitle());
               // 方式三：通过runJavaScript执行JavaScript脚本获取标题
               // 异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果
               this.wController.runJavaScript('document.title', (error, result) => {
                 if (error) {
                   console.error(`Failed to get title. Code is ${error.code}, message is ${error.message}`);
                 } else {
                   console.info('Page title:', result);
                 }
               });
             });
         }
         .width('100%')
         .height('100%');
       };
     }
   }
   ```

   **说明** 

   访问在线网页时需添加网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 常见FAQ

Q：onTitleReceive或者是通过getTitle获取标题为什么返回的是URL？

A：如果加载的页面未设置title元素来指定标题，Web组件将基于URL生成标题并返回给应用程序。
