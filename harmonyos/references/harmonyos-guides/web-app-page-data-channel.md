---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-app-page-data-channel
title: 建立应用侧与前端页面数据通道
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 在应用中使用前端页面JavaScript > 建立应用侧与前端页面数据通道
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c52c0738facdb190685c8ffc00500841538c0eed44ffbb725160d50d44847209
---

前端页面和应用侧之间可以用[createWebMessagePorts()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#createwebmessageports)接口创建消息端口来实现两端的通信。

在下面的示例中，应用侧页面中通过createWebMessagePorts方法创建两个消息端口，再把其中一个端口通过[postMessage()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#postmessage)接口发送到前端页面，便可以在前端页面和应用侧之间互相发送消息。端口使用完毕后或Webview对象销毁前通过[close](../harmonyos-references/arkts-apis-webview-webmessageport.md#close)接口关闭端口。

* 应用侧代码。

  ```
  1. // xxx.ets
  2. import { webview } from '@kit.ArkWeb';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. @Entry
  6. @Component
  7. struct WebComponent {
  8. controller: webview.WebviewController = new webview.WebviewController();
  9. ports: webview.WebMessagePort[] = [];
  10. @State sendFromEts: string = 'Send this message from ets to HTML';
  11. @State receivedFromHtml: string = 'Display received message send from HTML';

  13. build() {
  14. Column() {
  15. // 展示接收到的来自HTML的内容
  16. Text(this.receivedFromHtml);
  17. // 输入框的内容发送到HTML
  18. TextInput({ placeholder: 'Send this message from ets to HTML' })
  19. .onChange((value: string) => {
  20. this.sendFromEts = value;
  21. })

  23. // 该内容可以放在onPageEnd生命周期中调用。
  24. Button('postMessage')
  25. .onClick(() => {
  26. try {
  27. // 1、创建两个消息端口。
  28. this.ports = this.controller.createWebMessagePorts();
  29. if (this.ports && this.ports[0] && this.ports[1]) {
  30. // 2、在应用侧的消息端口(如端口1)上注册回调事件。
  31. this.ports[1].onMessageEvent((result: webview.WebMessage) => {
  32. let msg = 'Got msg from HTML:';
  33. if (typeof (result) === 'string') {
  34. console.info(`received string message from html5, string is: ${result}`);
  35. msg = msg + result;
  36. } else if (typeof (result) === 'object') {
  37. if (result instanceof ArrayBuffer) {
  38. console.info(`received arraybuffer from html5, length is: ${result.byteLength}`);
  39. msg = msg + 'length is ' + result.byteLength;
  40. } else {
  41. console.info('not support');
  42. }
  43. } else {
  44. console.info('not support');
  45. }
  46. this.receivedFromHtml = msg;
  47. })
  48. // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
  49. this.controller.postMessage('__init_port__', [this.ports[0]], '*');
  50. } else {
  51. console.error(`ports is null, Please initialize first`);
  52. }
  53. } catch (error) {
  54. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  55. }
  56. })

  58. // 4、使用应用侧的端口给另一个已经发送到html的端口发送消息。
  59. Button('SendDataToHTML')
  60. .onClick(() => {
  61. try {
  62. if (this.ports && this.ports[1]) {
  63. this.ports[1].postMessageEvent(this.sendFromEts);
  64. } else {
  65. console.error(`ports is null, Please initialize first`);
  66. }
  67. } catch (error) {
  68. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  69. }
  70. })

  72. // 5、关闭端口。
  73. Button('closePort')
  74. .onClick(() => {
  75. try {
  76. if (this.ports && this.ports.length == 2) {
  77. this.ports[0].close();
  78. this.ports = [];
  79. } else {
  80. console.error("ports is null, not need close");
  81. }
  82. } catch (error) {
  83. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  84. }
  85. })
  86. Web({ src: $rawfile('index.html'), controller: this.controller })
  87. }
  88. }
  89. }
  ```
* 前端页面代码。

  ```
  1. <!--index.html-->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
  6. <title>WebView Message Port Demo</title>
  7. </head>
  8. <body>
  9. <h1>WebView Message Port Demo</h1>
  10. <div>
  11. <input type="button" value="SendToEts" onclick="PostMsgToEts(msgFromJS.value);"/><br/>
  12. <input id="msgFromJS" type="text" value="send this message from HTML to ets"/><br/>
  13. </div>
  14. <p class="output">display received message send from ets</p>
  15. </body>
  16. <script>
  17. var h5Port;
  18. var output = document.querySelector('.output');
  19. window.addEventListener('message', function (event) {
  20. if (event.data === '__init_port__') {
  21. if (event.ports[0] !== null) {
  22. h5Port = event.ports[0]; // 1. 保存从应用侧发送过来的端口。
  23. h5Port.onmessage = function (event) {
  24. // 2. 接收ets侧发送过来的消息。
  25. var msg = 'Got message from ets:';
  26. var result = event.data;
  27. if (typeof(result) === 'string') {
  28. console.info(`received string message from ets, string is: ${result}`);
  29. msg = msg + result;
  30. } else if (typeof(result) === 'object') {
  31. if (result instanceof ArrayBuffer) {
  32. console.info(`received arraybuffer from ets, length is: ${result.byteLength}`);
  33. msg = msg + 'length is ' + result.byteLength;
  34. } else {
  35. console.info('not support');
  36. }
  37. } else {
  38. console.info('not support');
  39. }
  40. output.innerHTML = msg;
  41. }
  42. }
  43. }
  44. })

  46. // 3. 使用h5Port向应用侧发送消息。
  47. function PostMsgToEts(data) {
  48. if (h5Port) {
  49. h5Port.postMessage(data);
  50. } else {
  51. console.error('h5Port is null, Please initialize first');
  52. }
  53. }
  54. </script>
  55. </html>
  ```

## 常见问题

### 为什么H5向应用侧发送消息接收不到？

检查传递的数据类型是否正确，WebMessage支持的数据类型有string和ArrayBuffer。

如果想要传递对象类型则需要将对象类型通过JSON.stringify方法转换为string类型再进行传递。示例如下：

```
1. function PostMsgToEts(data) {
2. if (h5Port) {
3. let obj = {name:'exampleName',id:10}
4. h5Port.postMessage(JSON.stringify(obj));
5. } else {
6. console.error('h5Port is null. Please initialize it first.');
7. }
8. }
```

### onControllerAttached与javaScriptOnDocumentStart的执行顺序是什么？

[javaScriptOnDocumentStart](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptondocumentstart11)在[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)之后执行。
