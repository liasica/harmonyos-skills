---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-146
title: 如何获取runJavaScript执行异步方法后的返回值
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何获取runJavaScript执行异步方法后的返回值
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c0a77badade598be2706d4e66fa67346f41a31de06620bccf775723ebc80f80
---

## 问题现象

官方文档中提到[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)执行异步方法无法获取返回值，该如何解决这个问题？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/B4XjQ3oaQU-T9DFx9Z_K_A/zh-cn_image_0000002659138407.png "点击放大")

## 背景知识

* [应用侧调用前端页面函数](../harmonyos-guides/web-in-app-frontend-page-function-invoking.md)：应用侧可以通过[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)方法，来调用前端页面的JavaScript相关函数。
* [前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)：注册应用侧代码有两种方式，一种在Web组件初始化调用，使用[javaScriptProxy()](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)接口；另外一种在Web组件初始化完成后调用，使用[registerJavaScriptProxy()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)接口。两种方式都需要和[deleteJavaScriptRegister](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#deletejavascriptregister)接口配合使用，防止内存泄漏。

## 解决方案

runJavaScript执行异步方法无法获取返回值的原因如下：

**说明** 

runJavaScript本身以异步方式执行，可视为一个异步方法，在当前调用机制下，尚无可行方案直接获取执行异步方法的返回值。

因此我们只能从其他角度加以考虑。

* runJavaScript执行前端异步方法。
* 前端获取结果后，通过调用应用侧方法将结果作为入参传递至应用侧。

进而解决了runJavaScript执行异步方法无法获取返回值的问题。

* index.html示例代码：

  ```html
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport"
            content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
      <title>title</title>
  </head>
  <body>
  <p>Web端页面</p>
  </body>
  <script>
      function generateAsyncResult(a, b, c) {
         return new Promise((resolve) => {
             setTimeout(() => {
                resolve(`异步返回${a}、${b}、${c}`)
             }, 1000)
         })
      }
      async function asyncMethod(a, b, c) {
        const result = await generateAsyncResult(a, b, c)
        javaScriptProxy.syncCallback(result)
      }
  </script>
  </html>
  ```
* Index.ets示例代码：

  ```ts
  import { webview } from '@kit.ArkWeb';

  class JavaScriptProxyObject {
    obj?: Index;

    constructor(obj: Index) {
      this.obj = obj;
    }

    syncCallback(res: string) {
      if (this.obj) {
        this.obj.changeMsg(res);
      }
    }
  }

  @Entry
  @Component
  struct Index {
    private webviewController: WebviewController = new webview.WebviewController();
    private localPath = $rawfile('index.html');
    private javaScriptProxyObject = new JavaScriptProxyObject(this);
    @State msg: string = '';

    aboutToDisappear(): void {
      this.webviewController.deleteJavaScriptRegister('javaScriptProxy');
    }

    changeMsg(msg: string) {
      this.msg = msg;
    }

    build() {
      Column() {
        Web({ controller: this.webviewController, src: this.localPath })
          .fileAccess(false)
          .geolocationAccess(false)
          .javaScriptAccess(true)
          .javaScriptProxy({
            object: this.javaScriptProxyObject,
            name: 'javaScriptProxy',
            methodList: ['syncCallback'],
            controller: this.webviewController
          })
          .width('100%')
          .height('70%');
        Text(this.msg ? `JS返回的数据: ${this.msg}` : '')
          .padding(20);
        Button('获取异步函数返回值')
          .onClick(() => {
            this.webviewController.runJavaScript('asyncMethod(1, 2, "3")');
          });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

## 总结

由于[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)调用前端异步方法时无法直接获取其返回结果，可以通过间接方式：由前端在异步结果获取完成后，主动调用应用侧方法，将结果作为参数传递至应用侧。
