---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-147
title: Web组件加载链接，如何修改链接网页中的文本
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件加载链接，如何修改链接网页中的文本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e830abd22e4147036f714a3082a3d22056efd0d10f0e91a3baf59a18158fa21e
---

## 问题现象

使用Web组件加载第三方的网页时，需要修改网页中的文本信息，如何实现？

## 背景知识

* 在H5（HTML5）中，可以使用getElementById获取到指定ID的标签：
  + 根据ID获取指定的Span标签：

    ```screen
    const spanElement = document.getElementById('mySpan');
    ```
  + 也可以通过getElementsByTagName获取到指定名称标签的集合：

    ```screen
    const spanElements = document.getElementsByTagName('span');
    ```
* [runJavaScriptExt](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)：WebView提供了runJavaScriptExt实现异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。

## 解决方案

1. 可以通过runJavaScriptExt注入脚本实现修改三方网页中文本。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct Index {
     private controller: webview.WebviewController = new webview.WebviewController();
     private context: Context = this.getUIContext().getHostContext() as Context;

     initJavaScrip() {
       // 注入本地的js脚本
       this.context.resourceManager.getRawFileContent('index.js')
         .then((value: ESObject) => {
           // 获取js脚本的ArrayBuffer数据
           let rawfile: ArrayBuffer = value.buffer;
           console.info('开始注入脚本');
           this.controller.runJavaScriptExt(rawfile).then(() => {
             console.info('开始注入脚本成功');
           }).catch(() => {
             console.info('开始注入脚本失败');
           });
         });
     }

     build() {
       RelativeContainer() {
         Web({
           src: $rawfile('span.html'),
           controller: this.controller
         })
           .onPageEnd(() => {
             setTimeout(() => {
               this.initJavaScrip();
             }, 3000);
           })
           .fileAccess(false)
           .geolocationAccess(false)
           .domStorageAccess(true)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. 在js中通过getElementById获取指定ID的标签，并修改其文本内容。

   index.js：

   ```screen
   let spanLabels = document.getElementById('mySpan');
   console.info(`mySpan:${spanLabels.innerHTML}`)
   spanLabels.innerHTML = "修改后的文本"
   ```
3. 加载的本地页面。

   span.html：

   ```html
   <!DOCTYPE html>
   <html>
   <body>
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <h1 id="example">示例文本</h1>
   <span id="mySpan">这是默认文本</span>
   </body>
   </html>
   ```

## 常见FAQ

Q：runJavaScript()和runJavaScriptExt()有什么区别？

A：[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和runJavaScriptExt()的区别主要体现在参数和返回值的类型上。runJavaScript()仅支持string类型参数，而runJavaScriptExt()支持string和ArrayBuffer类型参数；runJavaScript()返回脚本执行的结果只能是string，而runJavaScriptExt()可以返回的类型支持[JsMessageType](../harmonyos-references/arkts-apis-webview-jsmessageext.md)，包括字符串、数组类型等。
