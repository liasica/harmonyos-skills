---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-print
title: 使用Web组件打印前端页面
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > 使用Web组件打印前端页面
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47968f282ca72c7699f463fd19e73897cfde1ca81b6a042042384c50e9c48b85
---

Web组件打印html页面时可通过W3C标准协议接口和应用接口两种方式实现。

使用打印功能前，请在module.json5中配置相关权限，添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.PRINT"
4. }
5. ]
```

## 使用W3C标准协议接口拉起打印

通过创建打印适配器，拉起打印应用，并对当前Web页面内容进行渲染，渲染后生成的PDF文件信息通过文件描述符（fd）传递给打印框架。W3C标准协议接口window.print()方法用于打印当前页面或弹出打印对话框。该方法没有任何参数，只需要在JavaScript中调用即可。

可通过前端css样式控制是否打印，例如@media print。再通过web加载该html页面的方式运行。

* print.html页面代码。

  示例一：

  ```
  1. <!DOCTYPE html>
  2. <html>

  4. <head>
  5. <meta charset="utf-8">
  6. <title>printTest</title>
  7. <style>
  8. @media print {
  9. h1 {
  10. display: none;
  11. }
  12. }
  13. </style>
  14. </head>

  16. <body>
  17. <div>
  18. <h1><b>
  19. <p style="text-align: center;">This is a test page for printing</p>
  20. </b>
  21. <hr color="#00cc00" width="95%">
  22. </h1>
  23. <button class="Button Button--outline" onclick="window.print();">Print</button>
  24. <p> content content content </p>
  25. <div id="printableTable">
  26. <table>
  27. <thead>
  28. <tr>
  29. <td>Thing</td>
  30. <td>Chairs</td>
  31. </tr>
  32. </thead>
  33. <tbody>
  34. <tr>
  35. <td>1</td>
  36. <td>blue</td>
  37. </tr>
  38. <tr>
  39. <td>2</td>
  40. <td>green</td>
  41. </tr>
  42. </tbody>
  43. </table>
  44. </div>
  45. <p> content content content </p>
  46. <p> content content content </p>
  47. </div>
  48. </body>
  ```

  示例二（iframe嵌套页面的方式）：

  ```
  1. <!DOCTYPE html>
  2. <html lang="en">
  3. <head>
  4. <meta charset="UTF-8">
  5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
  6. <title>iframe嵌套页面打印</title>
  7. </head>
  8. <body>
  9. <button id="printIframe">打印iframe嵌套页面</button>
  10. <iframe id="contentIframe" hidden></iframe>

  12. <script>
  13. document.getElementById("printIframe").addEventListener("click", () => {
  14. var ctIframe = document.getElementById("contentIframe");
  15. if(!ctIframe.contentWindow || !ctIframe.contentWindow.document) {
  16. console.error("iframe页面初始化失败");
  17. return;
  18. }
  19. var ctIframeDoc = ctIframe.contentWindow.document;
  20. ctIframeDoc.write("嵌套页面");
  21. ctIframeDoc.close();
  22. ctIframe.contentWindow.print();
  23. });
  24. </script>
  25. </body>
  26. </html>
  ```
* 应用侧代码。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct Index {
  6. controller: webview.WebviewController = new webview.WebviewController();

  8. build() {
  9. Row() {
  10. Column() {
  11. Web({ src: $rawfile('print.html'), controller: this.controller })
  12. .javaScriptAccess(true)
  13. }
  14. .width('100%')
  15. }
  16. .height('100%')
  17. }
  18. }
  ```

  [InitiatePrintW3CAPI.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ProcessWebPageCont/entry/src/main/ets/pages/InitiatePrintW3CAPI.ets#L16-L35)

## 通过调用应用侧接口拉起打印

应用侧通过调用[createWebPrintDocumentAdapter](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#createwebprintdocumentadapter11)创建打印适配器，通过将适配器传入打印的print接口调起打印。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError, print } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('createWebPrintDocumentAdapter')
12. .onClick(() => {
13. try {
14. let webPrintDocadapter = this.controller.createWebPrintDocumentAdapter('example.pdf');
15. print.print('example_job_id', webPrintDocadapter, null, this.getUIContext().getHostContext());
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller });
21. }
22. }
23. }
```

[InitiatePrintAppAPI.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ProcessWebPageCont/entry/src/main/ets/pages/InitiatePrintAppAPI.ets#L16-L40)
