---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-app-frontend-page-function-invoking
title: 应用侧调用前端页面函数
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 在应用中使用前端页面JavaScript > 应用侧调用前端页面函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d6d77231b9f369f92f3b294ed79576b0b069d7d0d20d460b86294b48a4ba9c99
---

应用侧可以通过[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)方法调用前端页面的JavaScript相关函数。

[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)在参数类型上有以下差异：[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)支持string和ArrayBuffer类型参数，而[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)仅支持string类型参数。

在下面的示例中，点击应用侧的“runJavaScript”按钮时，触发前端页面的htmlTest()方法。

* 前端页面代码。

  ```html
  <!-- index.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
  <button type="button" onclick="callArkTS()">Click Me!</button>
  <h1 id="text">这是一个测试信息，默认字体为黑色，调用runJavaScript方法后字体为黄色、调用runJavaScriptParam方法后字体为绿色、调用runJavaScriptCodePassed方法后字体为红色</h1>
  <script>
      // 有参函数。
      var param = "param: JavaScript Hello World!";
      function htmlTestParam(param) {
          document.getElementById('text').style.color = 'green';
          console.info(param);
      }
      // 无参函数。
      function htmlTest() {
          document.getElementById('text').style.color = 'yellow';
      }
      // 点击“Click Me！”按钮，触发前端页面callArkTS()函数执行JavaScript传递的代码。
      function callArkTS() {
          changeColor();
      }
  </script>
  </body>
  </html>
  ```
* 应用侧代码。

  ```typescript
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebComponent {
    webviewController: webview.WebviewController = new webview.WebviewController();

    aboutToAppear() {
      // 配置Web开启调试模式
      webview.WebviewController.setWebDebuggingAccess(true);
    }

    build() {
      Column() {
        Button('runJavaScriptParam')
          .onClick(() => {
            // 调用前端页面有参函数。
            this.webviewController.runJavaScript('htmlTestParam(param)');
          })
        Button('runJavaScript')
          .onClick(() => {
            // 调用前端页面无参函数。
            this.webviewController.runJavaScript('htmlTest()');
          })
        Button('runJavaScriptCodePassed')
          .onClick(() => {
            // 传递runJavaScript侧代码方法。
            this.webviewController.runJavaScript(
              `function changeColor(){document.getElementById('text').style.color = 'red'}`);
          })
        Web({ src: $rawfile('index.html'), controller: this.webviewController })
      }
    }
  }
  ```
