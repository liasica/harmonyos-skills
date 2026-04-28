---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-app-frontend-page-function-invoking
title: 应用侧调用前端页面函数
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 在应用中使用前端页面JavaScript > 应用侧调用前端页面函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6b9a2ca961e042751b3b20ee58e2b0a75d0f16eb1a6935ca4e13df229666c24d
---

应用侧可以通过[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)方法调用前端页面的JavaScript相关函数。

[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)在参数类型上有以下差异：[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)支持string和ArrayBuffer类型参数，而[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)仅支持string类型参数。

在下面的示例中，点击应用侧的“runJavaScript”按钮时，触发前端页面的htmlTest()方法。

* 前端页面代码。

  ```
  1. <!-- index.html -->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
  6. </head>
  7. <body>
  8. <button type="button" onclick="callArkTS()">Click Me!</button>
  9. <h1 id="text">这是一个测试信息，默认字体为黑色，调用runJavaScript方法后字体为黄色、调用runJavaScriptParam方法后字体为绿色、调用runJavaScriptCodePassed方法后字体为红色</h1>
  10. <script>
  11. // 有参函数。
  12. var param = "param: JavaScript Hello World!";
  13. function htmlTestParam(param) {
  14. document.getElementById('text').style.color = 'green';
  15. console.info(param);
  16. }
  17. // 无参函数。
  18. function htmlTest() {
  19. document.getElementById('text').style.color = 'yellow';
  20. }
  21. // 点击“Click Me！”按钮，触发前端页面callArkTS()函数执行JavaScript传递的代码。
  22. function callArkTS() {
  23. changeColor();
  24. }
  25. </script>
  26. </body>
  27. </html>
  ```
* 应用侧代码。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct WebComponent {
  6. webviewController: webview.WebviewController = new webview.WebviewController();

  8. aboutToAppear() {
  9. // 配置Web开启调试模式
  10. webview.WebviewController.setWebDebuggingAccess(true);
  11. }

  13. build() {
  14. Column() {
  15. Button('runJavaScriptParam')
  16. .onClick(() => {
  17. // 调用前端页面有参函数。
  18. this.webviewController.runJavaScript('htmlTestParam(param)');
  19. })
  20. Button('runJavaScript')
  21. .onClick(() => {
  22. // 调用前端页面无参函数。
  23. this.webviewController.runJavaScript('htmlTest()');
  24. })
  25. Button('runJavaScriptCodePassed')
  26. .onClick(() => {
  27. // 传递runJavaScript侧代码方法。
  28. this.webviewController.runJavaScript(
  29. `function changeColor(){document.getElementById('text').style.color = 'red'}`);
  30. })
  31. Web({ src: $rawfile('index.html'), controller: this.webviewController })
  32. }
  33. }
  34. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry/src/main/ets/pages/Index.ets#L16-L51)
