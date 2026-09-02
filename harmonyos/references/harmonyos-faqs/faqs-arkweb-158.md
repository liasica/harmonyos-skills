---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-158
title: 如何解决H5页面的输入框在聚焦和失焦时，键盘的自动拉起和隐藏问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决H5页面的输入框在聚焦和失焦时，键盘的自动拉起和隐藏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f8c53dbd84cc3f58cba4de1063cc4d3303dbfa461022501295e3e4a971ce4ce4
---

## 问题现象

H5侧获焦或者失焦，但是Web侧未感知到H5侧焦点变化，具体问题有如下两种：

1. H5页面的Input输入框显示焦点但是无法输入文字。
2. H5页面的Input输入框焦点在键盘回收后无法自动失焦。

## 背景知识

* [Web组件焦点管理](../harmonyos-guides/web-focus.md)：
  + 组件焦点：指当前应用界面上唯一的一个可交互元素。
  + 网页内元素焦点：指当前网页界面上唯一的一个可交互元素。
* [onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)：当前组件获取焦点时触发的回调。
* [onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)：当前组件失去焦点时触发的回调。

## 问题定位

1. 检查元素焦点获取与清除的状态是否执行成功。
2. 检查输入框唤起的键盘是否自动失去焦点。

## 分析结论

H5侧焦点变化与Web侧焦点变化未同步，需要手动实现两侧同步。

## 修改建议

* 问题1中Web内输入框自动聚焦后弹出键盘实现示例：

  ArkTS示例代码如下：

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { inputMethod } from '@kit.IMEKit';
  import { webview } from '@kit.ArkWeb';

  let textConfig: inputMethod.TextConfig = {
    inputAttribute: {
      textInputType: 0,
      enterKeyType: 1
    }
  };

  @Entry
  @Component
  struct WebFocus1 {
    controller: webview.WebviewController = new webview.WebviewController();
    inputMethodController = inputMethod.getController();

    onPageShow(): void {
      setTimeout(() => { // 因为inputController的挂载时间点晚于onPageShow，应用在启动时可以自动聚焦并且弹出软键盘，但是退出后台后再进入app焦点在输入框，没有弹出键盘，此时需要增加延时代码。
        console.info(`Failed to attach:${this.inputMethodController}`);
        try {
          this.inputMethodController.attach(true, textConfig, (err: BusinessError) => {
            if (err) {
              console.error(`Failed to attach: ${err.code}, ${err.message}`); // 从后台切进来，报错Input method client error
              return;
            }
            console.info('Succeeded in attaching the inputMethod.');
          });
        } catch (err) {
          console.error(`Failed to attach: ${err.code}, ${err.message}`);
        }
      }, 100);
    }

    build() {
      Row() {
        Column() {
          Web({ src: $rawfile('index1.html'), controller: this.controller })
            .javaScriptAccess(true)
            .domStorageAccess(true)
            .fileAccess(false)
            .geolocationAccess(false)
            .onPageVisible(() => {
              this.inputMethodController.showTextInput((err: BusinessError) => {
                if (err) {
                  console.error(`Failed to showTextInput: ${err.code}, ${err.message}`);
                  return;
                }
                console.info('Succeeded in showing the inputMethod.');
              });
            });
        }.width('100%');
      }.height('100%');
    }
  }
  ```

  html示例代码如下：

  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>输入框获焦</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
      <script type="text/javascript">
          function handleFocus() {
             console.info("输入框已获焦");
          }
      </script>
  </head>
  <body>
  <input type="text" autofocus="true" placeholder="点击我" />
  </body>
  </html>
  ```
* 问题2键盘回收后输入框自动失焦：

  解决方案一：

  在HarmonyOS代码中添加JS函数调用，确保键盘回收后输入框自动失焦。

  ArkTS示例代码如下：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct WebFocus2 {
    lastWindow: window.Window | undefined = undefined;

    onPageShow(): void {
      console.info('onPageShow');
      window.getLastWindow(this.getUIContext().getHostContext()).then((lastWindow) => {
        this.lastWindow = lastWindow;
        lastWindow.on('keyboardHeightChange', (data) => {
          console.info('开始监听');
          if (data == 0) {
            this.webController.runJavaScript('lostFocus()');
          }
          console.info(`Succeeded in enabling the listener for keyboard height changes. Data: ${data}`);
        });
      });

    }

    onPageHide(): void {
      console.info('onPageHide');
      this.lastWindow?.off('keyboardHeightChange');
    }

    webController: webview.WebviewController = new webview.WebviewController();

    build() {
      RelativeContainer() {
        Web({
          src: $rawfile('index2.html'),
          controller: this.webController
        })
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .fileAccess(false)
          .geolocationAccess(false);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  html示例代码如下：

  ```html
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport"
            content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
  <h1>H5侧</h1>
  <div>
      <input id="myInput" type="text" value="" style="margin:10px 0" onload /><br />
  </div>
  </body>
  <script>
      function test() {
        document.getElementById("myInput").focus();
      }
      function lostFocus() {
        console.info('HTML: lostFocus called');
        const inputs = document.querySelectorAll('input');
        if (inputs.length === 0) {
          console.info('HTML: no input selected');
        }
        // 遍历并失焦
        inputs.forEach(input => {
          input.blur();
        });
      }
      // 当文档加载时立即执行函数
      document.addEventListener('DOMContentLoaded', test);
  </script>
  </html>
  <style>
      body {
        width: 100%;
        height: auto;
        margin: 50px auto;
        text-align: center;
      }
  </style>
  ```

  解决方案二：

  若想关闭软键盘时触发Input文本框的失焦事件可设置Web组件的[blurOnKeyboardHideMode](../harmonyos-references/arkts-basic-components-web-attributes.md#bluronkeyboardhidemode14)属性为BlurOnKeyboardHideMode.BLUR。

  ArkTS示例代码如下：

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebFocus3 {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Row() {
        Column() {
          Web({ src: $rawfile('index3.html'), controller: this.controller })
            .javaScriptAccess(true)
            .domStorageAccess(true)
            .fileAccess(false)
            .geolocationAccess(false)
            .blurOnKeyboardHideMode(BlurOnKeyboardHideMode.BLUR)
        }.width('100%');
      }.height('100%');
    }
  }
  ```

  html示例代码如下：

  ```html
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport"
            content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
  <h1>H5侧</h1>
  <div>
      <input id="myInput" type="text" value="" style="margin:10px 0" onload /><br />
  </div>
  </body>
  <script>
      function test() {
        document.getElementById("myInput").focus();
      }
      // 当文档加载时立即执行函数
      document.addEventListener('DOMContentLoaded', test);
  </script>
  </html>
  <style>
      body {
        width: 100%;
        height: auto;
        margin: 50px auto;
        text-align: center;
      }
  </style>
  ```

## 常见FAQ

Q：问题1中Web内输入框自动聚焦后为什么无法自动拉起键盘？

A：采用这种机制，主要是为了避免以下两类问题：

1. 防止误触：在触摸屏设备上，用户可能会无意间触碰到屏幕，或快速滑动、误触到输入框区域。如果仅通过focus自动聚焦就直接弹出键盘，会在用户无输入意图时强行唤起键盘，造成不必要的界面干扰与体验问题。
2. 区分操作意图：区分“通过键盘导航聚焦到文本框”和“通过触摸/点击准备输入”两种不同的用户行为。

   键盘导航：用户通过键盘（如Tab键）将焦点移动到文本框，可能只是浏览、切换表单，并不一定需要立即输入。

   点击输入：用户用手指或鼠标点击文本框时，浏览器通常判断用户正准备输入文本，此时弹出虚拟键盘才合理。

   因此，松开鼠标或抬起手指这个动作，是判断用户“用户输入”的关键信号，而非仅仅是focus事件。
