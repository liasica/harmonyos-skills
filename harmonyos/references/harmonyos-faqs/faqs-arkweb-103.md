---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-103
title: Web页面点击无响应
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web页面点击无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dcf1ce41056f4ca6f550cbd867af797db67df857c90ce501ba8c799a2a573867
---

## 问题现象

* 问题一：Web页面里的按钮，点击后无响应。
* 问题二：触屏点击有响应，用鼠标点击无响应。

## 背景知识

* 建立应用侧与Web侧的交互通道有两种方式，一种在Web组件初始化调用，使用[javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)接口。另外一种在Web组件初始化完成后调用，使用[registerJavaScriptProxy](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)接口。两种方式都需要和[deleteJavaScriptRegister](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#deletejavascriptregister)接口配合使用，防止内存泄漏。
* [Devtools](../harmonyos-guides/web-debugging-with-devtools.md)：可以用来在电脑上调试手机、平板等移动设备前端页面，查看页面加载的信息、页面样式等。
* 不同类型的智能设备，用户可能有不同的交互方式，如通过触摸屏、鼠标、触控板等。如果针对不同的交互方式单独做适配，会增加开发工作量同时产生大量重复代码。为解决这一问题，系统统一了各种交互方式的API，即实现了交互归一。常见的基础输入方式及其在各输入设备上的表现如[下图](../best-practices/bpta-multi-interaction.md#section182814229423)所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/sJRhDfCXTK2TLG-O9V4Exw/zh-cn_image_0000002628899124.png "点击放大")

## 问题定位

* 问题一：
  1. 日志过滤ARKWEB-CONSOLE，查看H5页面有没有报错日志输出，获得如下日志，可知UNIApp未被定义。

     ```shell
     A01194/com.example/ARKWEB-CONSOLE   com.example     I     [CONSOLE:16] "Uncaught ReferenceError: UNIApp is not defined", source: https://www.example.com/index.html
     ```
  2. 检查是否将ArkTS对象注册到Web组件中，成功注册会有如下日志输出。

     ```shell
     A04510/com.example/chromium         com.example     I     [nweb_delegate.cc:2712] RegisterArkJSfunction name : UNIApp
     ```
* 问题二：

  使用Devtools调试Web页面，选择要点击的组件，查看事件侦听器，检查该组件绑定的事件是click还是touch。

## 分析结论

* 问题一：应用侧未正确将ArkTS对象注册到Web侧。
* 问题二：组件绑定的是touch事件，用鼠标点击不会触发。

## 修改建议

* 问题一：以下是将ArkTS对象注册到Web侧的案例。

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { PromptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct WebPage {
    controller: webview.WebviewController = new webview.WebviewController();
    private prompt: PromptAction = this.getUIContext().getPromptAction();
    @State testObj: TestObj = new TestObj(this.prompt);

    build() {
      Column() {
        Button('refresh')
          .onClick(() => {
            try {
              this.controller.refresh();
              this.prompt.showToast({message: '成功刷新'});
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
          .margin({top: 20, bottom: 20})
        Button('Register JavaScript To Window')
          .onClick(() => {
            try {
              // 同时注册同步和异步函数
              this.controller.registerJavaScriptProxy(this.testObj, 'objName', ['test']);
              this.prompt.showToast({message: '成功注册'});
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
          .margin({bottom: 20})
        Button('deleteJavaScriptRegister')
          .onClick(() => {
            try {
              this.controller.deleteJavaScriptRegister('objName');
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
          .margin({bottom: 20})
        Web({ src: $rawfile('testWebPage.html'), controller: this.controller })
          .javaScriptAccess(true)
          .fileAccess(true)
          .geolocationAccess(false)
      }
    }
  }

  class TestObj {
    prompt: PromptAction | undefined = undefined;
    constructor(prompt: PromptAction) {
      this.prompt = prompt;
    }

    test(): void {
      if (this.prompt) {
        this.prompt.showToast({message: '成功调用ArkUI侧方法'});
      }
    }
  }
  ```

  ```html
  <!-- index.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
  </head>
  <body>
  <div style="text-align:center;">
      <button type="button" onclick="htmlTest()" style="width:200px;height:80px;font-size:30px;">Click Me!</button>
  </div>

  <script type="text/javascript">
      function htmlTest() {
        objName.test();
      }
  </script>
  </body>
  </html>
  ```
* 问题二：将touch事件改成click事件。
