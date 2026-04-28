---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events
title: 事件
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > 事件
category: harmonyos-references
scraped_at: 2026-04-28T08:05:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e68088dc0dced9709b060b6b7d047096cabbeeaccb0bed6b7f5116d680f53a2
---

通用事件仅支持[onAppear](ts-universal-events-show-hide.md#onappear)、[onDisAppear](ts-universal-events-show-hide.md#ondisappear)、[onBlur](ts-universal-focus-event.md#onblur)、[onFocus](ts-universal-focus-event.md#onfocus)、[onDragEnd](ts-universal-events-drag-drop.md#ondragend10)、[onDragEnter](ts-universal-events-drag-drop.md#ondragenter)、[onDragStart](ts-universal-events-drag-drop.md#ondragstart)、[onDragMove](ts-universal-events-drag-drop.md#ondragmove)、[onDragLeave](ts-universal-events-drag-drop.md#ondragleave)、[onDrop](ts-universal-events-drag-drop.md#ondrop)、[onHover](ts-universal-events-hover.md#onhover)、[onMouse](ts-universal-mouse-key.md#onmouse)、[onKeyEvent](ts-universal-events-key.md#onkeyevent)、[onTouch](ts-universal-events-touch.md#ontouch)、[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。

## onAlert

PhonePC/2in1TabletTVWearable

onAlert(callback: Callback<OnAlertEvent, boolean>)

网页触发alert()告警弹窗时触发回调。若不调用[handleCancel](arkts-basic-components-web-jsresult.md#handlecancel)或[handleConfirm](arkts-basic-components-web-jsresult.md#handleconfirm)接口，会造成render进程阻塞。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnAlertEvent](arkts-basic-components-web-i.md#onalertevent12), boolean> | 是 | 网页触发alert()告警弹窗时触发。  返回值boolean。当回调返回true时，应用可以调用自定义弹窗能力（包括确认和取消），并且需要根据用户的确认或取消操作调用JsResult通知Web组件最终确认结果。当回调返回false时，弹窗的处理结果会被视为取消。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. uiContext: UIContext = this.getUIContext();

10. build() {
11. Column() {
12. Web({ src: $rawfile("index.html"), controller: this.controller })
13. .onAlert((event) => {
14. if (event) {
15. console.info("event.url:" + event.url);
16. console.info("event.message:" + event.message);
17. this.uiContext.showAlertDialog({
18. title: 'onAlert',
19. message: 'text',
20. primaryButton: {
21. value: 'ok',
22. action: () => {
23. event.result.handleConfirm();
24. }
25. },
26. cancel: () => {
27. event.result.handleCancel();
28. }
29. })
30. }
31. return true;
32. })
33. }
34. }
35. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
6. </head>
7. <body>
8. <h1>WebView onAlert Demo</h1>
9. <button onclick="myFunction()">Click here</button>
10. <script>
11. function myFunction() {
12. alert("Hello World");
13. }
14. </script>
15. </body>
16. </html>
```

## onBeforeUnload

PhonePC/2in1TabletTVWearable

onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean>)

即将完成页面刷新或关闭当前页面时触发此回调。

说明

* 如果当前Web组件没有得到焦点，刷新或关闭当前页面时onBeforeUnload不会触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnBeforeUnloadEvent](arkts-basic-components-web-i.md#onbeforeunloadevent12), boolean> | 是 | 即将完成页面刷新或关闭当前页面时触发。  返回值boolean。当回调返回true时，应用可以调用自定义弹窗能力（包括确认和取消），并且需要根据用户的确认或取消操作调用JsResult通知Web组件最终是否离开当前页面。当回调返回false时，函数中绘制的自定义弹窗无效。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. uiContext: UIContext = this.getUIContext();

10. build() {
11. Column() {
12. Web({ src: $rawfile("index.html"), controller: this.controller })
13. .onBeforeUnload((event) => {
14. if (event) {
15. console.info("event.url:" + event.url);
16. console.info("event.message:" + event.message);
17. console.info("event.isReload:" + event?.isReload ?? 'false');
18. this.uiContext.showAlertDialog({
19. title: 'onBeforeUnload',
20. message: 'text',
21. primaryButton: {
22. value: 'cancel',
23. action: () => {
24. event.result.handleCancel();
25. }
26. },
27. secondaryButton: {
28. value: 'ok',
29. action: () => {
30. event.result.handleConfirm();
31. }
32. },
33. cancel: () => {
34. event.result.handleCancel();
35. }
36. })
37. }
38. return true;
39. })
40. }
41. }
42. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
6. </head>
7. <body onbeforeunload="return myFunction()">
8. <h1>WebView onBeforeUnload Demo</h1>
9. <a href="https://www.example.com">Click here</a>
10. <script>
11. function myFunction() {
12. return "onBeforeUnload Event";
13. }
14. </script>
15. </body>
16. </html>
```

## onConfirm

PhonePC/2in1TabletTVWearable

onConfirm(callback: Callback<OnConfirmEvent, boolean>)

网页调用confirm()告警时触发此回调。若不调用[handleCancel](arkts-basic-components-web-jsresult.md#handlecancel)或[handleConfirm](arkts-basic-components-web-jsresult.md#handleconfirm)接口，会造成render进程阻塞。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnConfirmEvent](arkts-basic-components-web-i.md#onconfirmevent12), boolean> | 是 | 网页调用confirm()告警时触发。  返回值boolean。当回调返回true时，应用可以调用自定义弹窗能力（包括确认和取消），并且需要根据用户的确认或取消操作调用JsResult通知Web组件最终确认结果。当回调返回false时，弹窗的处理结果会被视为取消。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. uiContext: UIContext = this.getUIContext();

10. build() {
11. Column() {
12. Web({ src: $rawfile("index.html"), controller: this.controller })
13. .onConfirm((event) => {
14. if (event) {
15. console.info("event.url:" + event.url);
16. console.info("event.message:" + event.message);
17. this.uiContext.showAlertDialog({
18. title: 'onConfirm',
19. message: 'text',
20. primaryButton: {
21. value: 'cancel',
22. action: () => {
23. event.result.handleCancel();
24. }
25. },
26. secondaryButton: {
27. value: 'ok',
28. action: () => {
29. event.result.handleConfirm();
30. }
31. },
32. cancel: () => {
33. event.result.handleCancel();
34. }
35. })
36. }
37. return true;
38. })
39. }
40. }
41. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
6. </head>

8. <body>
9. <h1>WebView onConfirm Demo</h1>
10. <button onclick="myFunction()">Click here</button>
11. <p id="demo"></p>
12. <script>
13. function myFunction() {
14. let x;
15. let r = confirm("click button!");
16. if (r == true) {
17. x = "ok";
18. } else {
19. x = "cancel";
20. }
21. document.getElementById("demo").innerHTML = x;
22. }
23. </script>
24. </body>
25. </html>
```

## onPrompt9+

PhonePC/2in1TabletTVWearable

onPrompt(callback: Callback<OnPromptEvent, boolean>)

网页调用prompt()告警时触发此回调。若不调用[handleCancel](arkts-basic-components-web-jsresult.md#handlecancel)或[handlePromptConfirm](arkts-basic-components-web-jsresult.md#handlepromptconfirm9)接口，会造成render进程阻塞。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnPromptEvent](arkts-basic-components-web-i.md#onpromptevent12), boolean> | 是 | 网页调用prompt()告警时触发。  返回值boolean。当回调返回true时，应用可以调用自定义弹窗能力（包括确认、取消和输入），并且需要根据用户的确认或取消操作调用JsResult通知Web组件最终处理结果。当回调返回false时，弹窗的处理结果会被视为取消。 |

**示例：**

```
1. // xxx.ets
2. import { CustomContentDialog } from '@kit.ArkUI';
3. import { webview } from '@kit.ArkWeb';

5. @Entry
6. @Component
7. struct WebComponent {
8. @State message: string = 'Hello World';
9. @State title: string = 'Hello World';
10. @State result: JsResult | null = null;
11. promptResult: string = '';
12. webviewController: webview.WebviewController = new webview.WebviewController();
13. dialogController: CustomDialogController = new CustomDialogController({
14. builder: CustomContentDialog({
15. primaryTitle: this.title,
16. contentBuilder: () => {
17. this.buildContent();
18. },
19. buttons: [
20. {
21. value: '取消',
22. buttonStyle: ButtonStyleMode.TEXTUAL,
23. action: () => {
24. console.info('Callback when the button is clicked');
25. this.result?.handleCancel()
26. }
27. },
28. {
29. value: '确认',
30. buttonStyle: ButtonStyleMode.TEXTUAL,
31. action: () => {
32. this.result?.handlePromptConfirm(this.promptResult);
33. }
34. }
35. ],
36. }),
37. onWillDismiss: () => {
38. this.result?.handleCancel();
39. this.dialogController.close();
40. }
41. });

43. // 自定义弹出框的内容区
44. @Builder
45. buildContent(): void {
46. Column() {
47. Text(this.message)
48. TextInput()
49. .onChange((value) => {
50. this.promptResult = value;
51. })
52. .defaultFocus(true)
53. }
54. .width('100%')
55. }

57. build() {
58. Column() {
59. Web({ src: $rawfile('index.html'), controller: this.webviewController })
60. .onPrompt((event) => {
61. if (event) {
62. console.info("event.url:" + event.url);
63. console.info("event.message:" + event.message);
64. console.info("event.value:" + event.value);
65. this.title = "来自" + event.url + "的消息";
66. this.message = event.message;
67. this.promptResult = event.value;
68. this.result = event.result;
69. this.dialogController.open();
70. }
71. return true;
72. })
73. }
74. }
75. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
6. </head>

8. <body>
9. <h1>WebView onPrompt Demo</h1>
10. <button onclick="myFunction()">Click here</button>
11. <p id="demo"></p>
12. <script>
13. function myFunction() {
14. let message = prompt("Message info", "Hello World");
15. if (message != null && message != "") {
16. document.getElementById("demo").innerHTML = message;
17. }
18. }
19. </script>
20. </body>
21. </html>
```

## onConsole

PhonePC/2in1TabletTVWearable

onConsole(callback: Callback<OnConsoleEvent, boolean>)

通知宿主应用JavaScript console消息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnConsoleEvent](arkts-basic-components-web-i.md#onconsoleevent12), boolean> | 是 | 网页收到JavaScript控制台消息时触发。  返回值boolean。当返回true时，该条消息将不会再打印至hilog日志，返回false时仍会打印至hilog日志。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('onconsole message')
12. .onClick(() => {
13. this.controller.runJavaScript('myFunction()');
14. })
15. Web({ src: $rawfile('index.html'), controller: this.controller })
16. .onConsole((event) => {
17. if (event) {
18. console.info('getMessage:' + event.message.getMessage());
19. console.info('getSourceId:' + event.message.getSourceId());
20. console.info('getLineNumber:' + event.message.getLineNumber());
21. console.info('getMessageLevel:' + event.message.getMessageLevel());
22. console.info('getSource:' + event.message.getSource());
23. }
24. return false;
25. })
26. }
27. }
28. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <script>
6. function myFunction() {
7. console.info("onconsole printf");
8. }
9. </script>
10. </body>
11. </html>
```

## onDownloadStart

PhonePC/2in1TabletTVWearable

onDownloadStart(callback: Callback<OnDownloadStartEvent>)

通知主应用开始下载一个文件。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnDownloadStartEvent](arkts-basic-components-web-i.md#ondownloadstartevent12)> | 是 | 开始下载时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onDownloadStart((event) => {
13. if (event) {
14. console.info('url:' + event.url)
15. console.info('userAgent:' + event.userAgent)
16. console.info('contentDisposition:' + event.contentDisposition)
17. console.info('contentLength:' + event.contentLength)
18. console.info('mimetype:' + event.mimetype)
19. }
20. })
21. }
22. }
23. }
```

## onErrorReceive

PhonePC/2in1TabletTVWearable

onErrorReceive(callback: Callback<OnErrorReceiveEvent>)

网页加载遇到错误时触发该回调。主资源与子资源出错都会回调该接口，可以通过[isMainFrame](arkts-basic-components-web-webresourcerequest.md#ismainframe)来判断是否是主资源报错。出于性能考虑，建议此回调中尽量执行简单逻辑。在无网络的情况下，触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnErrorReceiveEvent](arkts-basic-components-web-i.md#onerrorreceiveevent12)> | 是 | 网页收到 Web 资源加载错误时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onErrorReceive((event) => {
13. if (event) {
14. console.info('getErrorInfo:' + event.error.getErrorInfo());
15. console.info('getErrorCode:' + event.error.getErrorCode());
16. console.info('url:' + event.request.getRequestUrl());
17. console.info('isMainFrame:' + event.request.isMainFrame());
18. console.info('isRedirect:' + event.request.isRedirect());
19. console.info('isRequestGesture:' + event.request.isRequestGesture());
20. console.info('getRequestHeader_headerKey:' + event.request.getRequestHeader().toString());
21. let result = event.request.getRequestHeader();
22. console.info('The request header result size is ' + result.length);
23. for (let i of result) {
24. console.info('The request header key is : ' + i.headerKey + ', value is : ' + i.headerValue);
25. }
26. }
27. })
28. }
29. }
30. }
```

## onHttpErrorReceive

PhonePC/2in1TabletTVWearable

onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent>)

网页加载资源遇到的HTTP错误（响应码>=400）时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnHttpErrorReceiveEvent](arkts-basic-components-web-i.md#onhttperrorreceiveevent12)> | 是 | 网页收到加载资源返回HTTP错误码时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onHttpErrorReceive((event) => {
13. if (event) {
14. console.info('url:' + event.request.getRequestUrl());
15. console.info('isMainFrame:' + event.request.isMainFrame());
16. console.info('isRedirect:' + event.request.isRedirect());
17. console.info('isRequestGesture:' + event.request.isRequestGesture());
18. console.info('getResponseData:' + event.response.getResponseData());
19. console.info('getResponseEncoding:' + event.response.getResponseEncoding());
20. console.info('getResponseMimeType:' + event.response.getResponseMimeType());
21. console.info('getResponseCode:' + event.response.getResponseCode());
22. console.info('getReasonMessage:' + event.response.getReasonMessage());
23. let result = event.request.getRequestHeader();
24. console.info('The request header result size is ' + result.length);
25. for (let i of result) {
26. console.info('The request header key is : ' + i.headerKey + ' , value is : ' + i.headerValue);
27. }
28. let resph = event.response.getResponseHeader();
29. console.info('The response header result size is ' + resph.length);
30. for (let i of resph) {
31. console.info('The response header key is : ' + i.headerKey + ' , value is : ' + i.headerValue);
32. }
33. }
34. })
35. }
36. }
37. }
```

## onPageBegin

PhonePC/2in1TabletTVWearable

onPageBegin(callback: Callback<OnPageBeginEvent>)

网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnPageBeginEvent](arkts-basic-components-web-i.md#onpagebeginevent12)> | 是 | 网页加载开始时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onPageBegin((event) => {
13. if (event) {
14. console.info('url:' + event.url);
15. }
16. })
17. }
18. }
19. }
```

## onPageEnd

PhonePC/2in1TabletTVWearable

onPageEnd(callback: Callback<OnPageEndEvent>)

网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnPageEndEvent](arkts-basic-components-web-i.md#onpageendevent12)> | 是 | 网页加载结束时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onPageEnd((event) => {
13. if (event) {
14. console.info('url:' + event.url);
15. }
16. })
17. }
18. }
19. }
```

## onLoadStarted20+

PhonePC/2in1TabletTVWearable

onLoadStarted(callback: Callback<OnLoadStartedEvent>)

通知宿主应用页面开始加载。此方法在每次主frame加载时调用一次，因此对于包含iframes或frameset的页面，onLoadStarted仅针对主frame调用一次。这意味着当嵌入式frame的内容发生变化时，如点击iframe中的链接或Fragment跳转（即跳转到#fragment\_id的导航）等，不会调用onLoadStarted。

说明

* 当弹出窗口的文档在加载之前被JavaScript修改时，它将模拟触发onLoadStarted，并将URL设置为空，因为显示当前正在加载的URL可能不安全。onPageBegin将不会被模拟。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnLoadStartedEvent](arkts-basic-components-web-i.md#onloadstartedevent20)> | 是 | 网页加载开始时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onLoadStarted((event) => {
13. if (event) {
14. console.info('url:' + event.url);
15. }
16. })
17. }
18. }
19. }
```

## onLoadFinished20+

PhonePC/2in1TabletTVWearable

onLoadFinished(callback: Callback<OnLoadFinishedEvent>)

通知宿主应用页面已加载完成。此方法仅在主frame加载完成时被调用。对于片段跳转（即导航至#fragment\_id），onLoadFinished同样会被触发。

说明

* 片段导航也会触发onLoadFinished，但onPageEnd不会被触发。
* 如果主框架在页面完全加载之前被自动重定向，onLoadFinished只会触发一次。onPageEnd会在每次主框架导航时触发。
* 当弹出窗口的文档在加载之前被JavaScript修改时，它将模拟触发onLoadStarted，并将URL设置为空，因为显示当前正在加载的URL可能不安全。onPageBegin将不会被模拟。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnLoadFinishedEvent](arkts-basic-components-web-i.md#onloadfinishedevent20)> | 是 | 网页加载结束时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onLoadFinished((event) => {
13. if (event) {
14. console.info('url:' + event.url);
15. }
16. })
17. }
18. }
19. }
```

## onProgressChange

PhonePC/2in1TabletTVWearable

onProgressChange(callback: Callback<OnProgressChangeEvent>)

网页加载进度变化时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnProgressChangeEvent](arkts-basic-components-web-i.md#onprogresschangeevent12)> | 是 | 页面加载进度变化时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .onProgressChange((event) => {
12. if (event) {
13. console.info('newProgress:' + event.newProgress);
14. }
15. })
16. }
17. }
18. }
```

## onTitleReceive

PhonePC/2in1TabletTVWearable

onTitleReceive(callback: Callback<OnTitleReceiveEvent>)

当页面文档标题<title>元素发生变更时，触发回调。若当前页面未显示设置标题，ArkWeb将在加载完成前基于页面的URL生成标题并返回给应用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnTitleReceiveEvent](arkts-basic-components-web-i.md#ontitlereceiveevent12)> | 是 | 页面文档标题发生变更时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onTitleReceive((event) => {
13. if (event) {
14. console.info('title:' + event.title);
15. console.info('isRealTitle:' + event.isRealTitle);
16. }
17. })
18. }
19. }
20. }
```

## onRefreshAccessedHistory

PhonePC/2in1TabletTVWearable

onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent>)

导航完成时触发该回调，用于应用更新其访问的历史链接。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnRefreshAccessedHistoryEvent](arkts-basic-components-web-i.md#onrefreshaccessedhistoryevent12)> | 是 | 在导航完成时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onRefreshAccessedHistory((event) => {
13. if (event) {
14. console.info('url:' + event.url + ' isReload:' + event.isRefreshed);
15. console.info('isMainFrame:' + event.isMainFrame);
16. }
17. })
18. }
19. }
20. }
```

## onRenderExited9+

PhonePC/2in1TabletTVWearable

onRenderExited(callback: Callback<OnRenderExitedEvent>)

应用渲染进程异常退出时触发该回调。

多个Web组件可能共享单个渲染进程，每个受影响的Web组件都会触发该回调。

应用处理该回调时，可以调用绑定的webviewController相关接口来恢复页面。例如[refresh](arkts-apis-webview-webviewcontroller.md#refresh)、[loadUrl](arkts-apis-webview-webviewcontroller.md#loadurl)等。

组件生命周期回调详情可参考[Web组件的生命周期](../harmonyos-guides/web-event-sequence.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnRenderExitedEvent](arkts-basic-components-web-i.md#onrenderexitedevent12)> | 是 | 渲染过程退出时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'chrome://crash/', controller: this.controller })
12. .onRenderExited((event) => {
13. if (event) {
14. console.info('reason:' + event.renderExitReason);
15. }
16. })
17. }
18. }
19. }
```

## onRenderProcessNotResponding12+

PhonePC/2in1TabletTVWearable

onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback)

渲染进程无响应时触发该回调函数。如果Web组件无法处理输入事件，或者无法在合理的时间范围内导航到新的URL，则认为网页进程无响应，并将触发该回调。

只要网页进程一直无响应，此回调仍可能会持续触发，直到网页进程再次响应，此时[onRenderProcessResponding](arkts-basic-components-web-events.md#onrenderprocessresponding12)将会触发。

应用可以通过WebviewController接口[terminateRenderProcess](arkts-apis-webview-webviewcontroller.md#terminaterenderprocess12)来终止关联的渲染进程，这可能会影响同一渲染进程的其他Web组件。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnRenderProcessNotRespondingCallback](arkts-basic-components-web-t.md#onrenderprocessnotrespondingcallback12) | 是 | 渲染进程无响应时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onRenderProcessNotResponding((data) => {
13. console.info("onRenderProcessNotResponding: [jsStack]= " + data.jsStack +
14. ", [process]=" + data.pid + ", [reason]=" + data.reason);
15. })
16. }
17. }
18. }
```

## onRenderProcessResponding12+

PhonePC/2in1TabletTVWearable

onRenderProcessResponding(callback: OnRenderProcessRespondingCallback)

渲染进程由无响应状态变回正常运行状态时触发该回调函数，该回调表明该网页并非真正卡死。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnRenderProcessRespondingCallback](arkts-basic-components-web-t.md#onrenderprocessrespondingcallback12) | 是 | 渲染进程由无响应状态变回正常运行状态时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onRenderProcessResponding(() => {
13. console.info("onRenderProcessResponding again");
14. })
15. }
16. }
17. }
```

## onShowFileSelector9+

PhonePC/2in1TabletTVWearable

onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean>)

调用此函数以处理具有“文件”输入类型的HTML表单。若不调用此函数或返回false，Web组件会提供默认的“选择文件”处理界面。若返回true，应用可以自定义“选择文件”的响应行为。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnShowFileSelectorEvent](arkts-basic-components-web-i.md#onshowfileselectorevent12), boolean> | 是 | 用于通知Web组件文件选择的结果。  返回值boolean。当返回值为true时，用户可以调用系统提供的弹窗能力。当返回值为false时，函数中绘制的自定义弹窗无效。 |

**示例：**

1. 拉起文件选择器。

   ```
   1. // xxx.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { picker } from '@kit.CoreFileKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   6. @Entry
   7. @Component
   8. struct WebComponent {
   9. controller: webview.WebviewController = new webview.WebviewController()

   11. build() {
   12. Column() {
   13. Web({ src: $rawfile('index.html'), controller: this.controller })
   14. .onShowFileSelector((event) => {
   15. console.info('MyFileUploader onShowFileSelector invoked')
   16. const documentSelectOptions = new picker.DocumentSelectOptions();
   17. let uri: string | null = null;
   18. const documentViewPicker = new picker.DocumentViewPicker();
   19. documentViewPicker.select(documentSelectOptions).then((documentSelectResult) => {
   20. uri = documentSelectResult[0];
   21. console.info('documentViewPicker.select to file succeed and uri is:' + uri);
   22. if (event) {
   23. event.result.handleFileList([uri]);
   24. }
   25. }).catch((err: BusinessError) => {
   26. console.error(`Invoke documentViewPicker.select failed, code is ${err.code},  message is ${err.message}`);
   27. })
   28. return true;
   29. })
   30. }
   31. }
   32. }
   ```
2. 拉起图库选择器。

   ```
   1. // xxx.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { picker } from '@kit.CoreFileKit';
   4. import { photoAccessHelper } from '@kit.MediaLibraryKit';

   6. @Entry
   7. @Component
   8. struct WebComponent {
   9. controller: webview.WebviewController = new webview.WebviewController();

   11. async selectFile(result: FileSelectorResult): Promise<void> {
   12. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   13. let photoPicker = new photoAccessHelper.PhotoViewPicker();
   14. // 过滤选择媒体文件类型为IMAGE_VIDEO
   15. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
   16. // 设置最大选择数量
   17. photoSelectOptions.maxSelectNumber = 5;
   18. let chooseFile: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
   19. // 获取选择的文件列表
   20. result.handleFileList(chooseFile.photoUris);
   21. }

   23. build() {
   24. Column() {
   25. Web({ src: $rawfile('index.html'), controller: this.controller })
   26. .onShowFileSelector((event) => {
   27. if (event) {
   28. this.selectFile(event.result);
   29. }
   30. return true;
   31. })
   32. }
   33. }
   34. }
   ```
3. 拉起相机选择器。

   ```
   1. // xxx.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { cameraPicker, camera } from '@kit.CameraKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { common } from '@kit.AbilityKit';

   7. async function openCamera(callback: Callback<string>, uiContext: UIContext) {
   8. let mContext = uiContext.getHostContext() as common.Context;
   9. try {
   10. let pickerProfile: cameraPicker.PickerProfile = {
   11. cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
   12. };
   13. let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(mContext,
   14. [cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO], pickerProfile);
   15. callback(pickerResult.resultUri);
   16. } catch (error) {
   17. let err = error as BusinessError;
   18. console.error(`the pick call failed. error code: ${err.code}`);
   19. }
   20. }

   22. @Entry
   23. @Component
   24. struct WebComponent {
   25. controller: webview.WebviewController = new webview.WebviewController();

   27. build() {
   28. Column() {
   29. Web({ src: $rawfile('index.html'), controller: this.controller })
   30. .onShowFileSelector((event) => {
   31. openCamera((result) => {
   32. if (event) {
   33. console.info('Title is ' + event.fileSelector.getTitle());
   34. console.info('Mode is ' + event.fileSelector.getMode());
   35. console.info('Accept types are ' + event.fileSelector.getAcceptType());
   36. console.info('Capture is ' + event.fileSelector.isCapture());
   37. console.info('Mime types are ' + event.fileSelector.getMimeTypes());
   38. event.result.handleFileList([result]);
   39. }
   40. }, this.getUIContext())
   41. return true;
   42. })
   43. }
   44. }
   45. }
   ```

   加载的html文件。

   ```
   1. <!DOCTYPE html>
   2. <html>
   3. <head>
   4. <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
   5. </head>
   6. <body>
   7. <form id="upload-form" enctype="multipart/form-data">
   8. <input type="file" id="upload" name="upload" accept="image/*, video/*"/>
   9. </form>
   10. </body>
   11. </html>
   ```

## onResourceLoad9+

PhonePC/2in1TabletTVWearable

onResourceLoad(callback: Callback<OnResourceLoadEvent>)

通知Web组件所加载的资源文件url信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnResourceLoadEvent](arkts-basic-components-web-i.md#onresourceloadevent12)> | 是 | 加载url时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onResourceLoad((event) => {
13. console.info('onResourceLoad: ' + event.url);
14. })
15. }
16. }
17. }
```

## onScaleChange9+

PhonePC/2in1TabletTVWearable

onScaleChange(callback: Callback<OnScaleChangeEvent>)

当页面显示比例发生变化时，触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnScaleChangeEvent](arkts-basic-components-web-i.md#onscalechangeevent12)> | 是 | 当页面显示比例发生变化时，触发该回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onScaleChange((event) => {
13. console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
14. })
15. }
16. }
17. }
```

## onInterceptRequest9+

PhonePC/2in1TabletTVWearable

onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse>)

当Web组件加载URL之前触发该回调，用于拦截URL并返回响应数据。onInterceptRequest可拦截所有跳转请求并返回响应数据，但无法访问POST请求体（Body）内容，且不支持分片缓冲（buffer）类型数据获取。此类场景需改用[WebSchemeHandler](arkts-apis-webview-webschemehandler.md)实现，依据具体业务需求进行判断。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnInterceptRequestEvent](arkts-basic-components-web-i.md#oninterceptrequestevent12), [WebResourceResponse](arkts-basic-components-web-webresourceresponse.md)> | 是 | 当Web组件加载url之前触发。  返回值[WebResourceResponse](arkts-basic-components-web-webresourceresponse.md)。返回响应数据则按照响应数据加载，无响应数据则返回null表示按照原来的方式加载。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. responseWeb: WebResourceResponse = new WebResourceResponse();
9. heads: Header[] = new Array();
10. webData: string = "<!DOCTYPE html>\n" +
11. "<html>\n" +
12. "<head>\n" +
13. "<title>intercept test</title>\n" +
14. "</head>\n" +
15. "<body>\n" +
16. "<h1>intercept test</h1>\n" +
17. "</body>\n" +
18. "</html>";

20. build() {
21. Column() {
22. Web({ src: 'www.example.com', controller: this.controller })
23. .onInterceptRequest((event) => {
24. if (event) {
25. console.info('url:' + event.request.getRequestUrl());
26. }
27. let head1: Header = {
28. headerKey: "Connection",
29. headerValue: "keep-alive"
30. }
31. let head2: Header = {
32. headerKey: "Cache-Control",
33. headerValue: "no-cache"
34. }
35. // 将新元素追加到数组的末尾，并返回数组的新长度。
36. let length = this.heads.push(head1);
37. length = this.heads.push(head2);
38. console.info('The response header result length is :' + length);
39. const promise: Promise<String> = new Promise((resolve: Function, reject: Function) => {
40. this.responseWeb.setResponseHeader(this.heads);
41. this.responseWeb.setResponseData(this.webData);
42. this.responseWeb.setResponseEncoding('utf-8');
43. this.responseWeb.setResponseMimeType('text/html');
44. this.responseWeb.setResponseCode(200);
45. this.responseWeb.setReasonMessage('OK');
46. resolve("success");
47. })
48. promise.then(() => {
49. console.info("prepare response ready");
50. this.responseWeb.setResponseIsReady(true);
51. })
52. this.responseWeb.setResponseIsReady(false);
53. return this.responseWeb;
54. })
55. }
56. }
57. }
```

## onHttpAuthRequest9+

PhonePC/2in1TabletTVWearable

onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean>)

通知收到http auth认证请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnHttpAuthRequestEvent](arkts-basic-components-web-i.md#onhttpauthrequestevent12), boolean> | 是 | 当浏览器需要用户的凭据时触发。  返回值boolean。返回true表示http auth认证成功，返回false表示http auth认证失败。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. uiContext: UIContext = this.getUIContext();
9. httpAuth: boolean = false;

11. build() {
12. Column() {
13. Web({ src: 'www.example.com', controller: this.controller })
14. .onHttpAuthRequest((event) => {
15. if (event) {
16. this.uiContext.showAlertDialog({
17. title: 'onHttpAuthRequest',
18. message: 'text',
19. primaryButton: {
20. value: 'cancel',
21. action: () => {
22. event.handler.cancel();
23. }
24. },
25. secondaryButton: {
26. value: 'ok',
27. action: () => {
28. this.httpAuth = event.handler.isHttpAuthInfoSaved();
29. if (this.httpAuth == false) {
30. webview.WebDataBase.saveHttpAuthCredentials(
31. event.host,
32. event.realm,
33. "2222",
34. "2222"
35. )
36. event.handler.cancel();
37. }
38. }
39. },
40. cancel: () => {
41. event.handler.cancel();
42. }
43. })
44. }
45. return true;
46. })
47. }
48. }
49. }
```

## onSslErrorEventReceive9+

PhonePC/2in1TabletTVWearable

onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent>)

通知用户加载资源时发生SSL错误，只支持主资源。

如果需要支持子资源，请使用[OnSslErrorEvent](arkts-basic-components-web-events.md#onsslerrorevent12)接口。

说明

* 主资源：浏览器加载网页的入口文件，通常是HTML文档。
* 子资源：主资源中引用的依赖文件，由主资源解析过程中遇到特定标签时触发加载。
* 应用程序需要调用[handler.handleCancel()](arkts-basic-components-web-sslerrorhandler.md#handlecancel9)或[handler.handleConfirm()](arkts-basic-components-web-sslerrorhandler.md#handleconfirm9)处理该回调，如果没有处理该回调则默认取消资源加载。handleConfirm()或者handleCancel()的行为可能会被记录下来，以便为将来的SSL错误做出响应。
* 应用程序可以用于显示自定义错误页面或静默记录问题。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnSslErrorEventReceiveEvent](arkts-basic-components-web-i.md#onsslerroreventreceiveevent12)> | 是 | 当网页收到SSL错误时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { cert } from '@kit.DeviceCertificateKit';

5. function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
6. if (!(certChainData instanceof Array)) {
7. console.error('failed, cert chain data type is not array');
8. return;
9. }

11. for (let i = 0; i < certChainData.length; i++) {
12. let encodeBlobData: cert.EncodingBlob = {
13. data: certChainData[i],
14. encodingFormat: cert.EncodingFormat.FORMAT_DER
15. }
16. cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
17. if (error) {
18. console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
19. } else {
20. console.info('createX509Cert success');
21. console.info(ParseX509CertInfo(x509Cert));
22. }
23. });
24. }
25. return;
26. }

28. function Uint8ArrayToString(dataArray: Uint8Array) {
29. let dataString = '';
30. for (let i = 0; i < dataArray.length; i++) {
31. dataString += String.fromCharCode(dataArray[i]);
32. }
33. return dataString;
34. }

36. function ParseX509CertInfo(x509Cert: cert.X509Cert) {
37. let res: string = 'getCertificate success, '
38. + 'issuer name = '
39. + Uint8ArrayToString(x509Cert.getIssuerName().data) + ', subject name = '
40. + Uint8ArrayToString(x509Cert.getSubjectName().data) + ', valid start = '
41. + x509Cert.getNotBeforeTime()
42. + ', valid end = ' + x509Cert.getNotAfterTime();
43. return res;
44. }

46. @Entry
47. @Component
48. struct WebComponent {
49. controller: webview.WebviewController = new webview.WebviewController();
50. uiContext: UIContext = this.getUIContext();

52. build() {
53. Column() {
54. Web({ src: 'www.example.com', controller: this.controller })
55. .onSslErrorEventReceive((event) => {
56. LogCertInfo(event.certChainData);
57. this.uiContext.showAlertDialog({
58. title: 'onSslErrorEventReceive',
59. message: 'text',
60. primaryButton: {
61. value: 'confirm',
62. action: () => {
63. event.handler.handleConfirm();
64. }
65. },
66. secondaryButton: {
67. value: 'cancel',
68. action: () => {
69. event.handler.handleCancel();
70. }
71. },
72. cancel: () => {
73. event.handler.handleCancel();
74. }
75. })
76. })
77. }
78. }
79. }
```

## onSslErrorEvent12+

PhonePC/2in1TabletTVWearable

onSslErrorEvent(callback: OnSslErrorEventCallback)

通知用户加载资源（主资源+子资源）时发生SSL错误，如果只想处理主资源的SSL错误，请用[isMainFrame](arkts-basic-components-web-webresourcerequest.md#ismainframe)字段进行区分。

说明

* 主资源：浏览器加载网页的入口文件，通常是HTML文档。
* 子资源：主资源中引用的依赖文件，由主资源解析过程中遇到特定标签时触发加载。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSslErrorEventCallback](arkts-basic-components-web-t.md#onsslerroreventcallback12) | 是 | 通知用户加载资源时发生SSL错误。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { cert } from '@kit.DeviceCertificateKit';

5. function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
6. if (!(certChainData instanceof Array)) {
7. console.error('failed, cert chain data type is not array');
8. return;
9. }

11. for (let i = 0; i < certChainData.length; i++) {
12. let encodeBlobData: cert.EncodingBlob = {
13. data: certChainData[i],
14. encodingFormat: cert.EncodingFormat.FORMAT_DER
15. }
16. cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
17. if (error) {
18. console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
19. } else {
20. console.info('createX509Cert success');
21. console.info(ParseX509CertInfo(x509Cert));
22. }
23. });
24. }
25. return;
26. }

28. function Uint8ArrayToString(dataArray: Uint8Array) {
29. let dataString = '';
30. for (let i = 0; i < dataArray.length; i++) {
31. dataString += String.fromCharCode(dataArray[i]);
32. }
33. return dataString;
34. }

36. function ParseX509CertInfo(x509Cert: cert.X509Cert) {
37. let res: string = 'getCertificate success, '
38. + 'issuer name = '
39. + Uint8ArrayToString(x509Cert.getIssuerName().data) + ', subject name = '
40. + Uint8ArrayToString(x509Cert.getSubjectName().data) + ', valid start = '
41. + x509Cert.getNotBeforeTime()
42. + ', valid end = ' + x509Cert.getNotAfterTime();
43. return res;
44. }

46. @Entry
47. @Component
48. struct WebComponent {
49. controller: webview.WebviewController = new webview.WebviewController();
50. uiContext: UIContext = this.getUIContext();

52. build() {
53. Column() {
54. Web({ src: 'www.example.com', controller: this.controller })
55. .onSslErrorEvent((event: SslErrorEvent) => {
56. console.info("onSslErrorEvent url: " + event.url);
57. console.info("onSslErrorEvent error: " + event.error);
58. console.info("onSslErrorEvent originalUrl: " + event.originalUrl);
59. console.info("onSslErrorEvent referrer: " + event.referrer);
60. console.info("onSslErrorEvent isFatalError: " + event.isFatalError);
61. console.info("onSslErrorEvent isMainFrame: " + event.isMainFrame);
62. LogCertInfo(event.certChainData);
63. this.uiContext.showAlertDialog({
64. title: 'onSslErrorEvent',
65. message: 'text',
66. primaryButton: {
67. value: 'confirm',
68. action: () => {
69. event.handler.handleConfirm();
70. }
71. },
72. secondaryButton: {
73. value: 'cancel',
74. action: () => {
75. // true表示停止加载页面，停留在当前页面，使用false表示继续加载页面，并展示错误页面
76. event.handler.handleCancel(true);
77. }
78. },
79. cancel: () => {
80. event.handler.handleCancel();
81. }
82. })
83. })
84. }
85. }
86. }
```

## onClientAuthenticationRequest9+

PhonePC/2in1TabletTVWearable

onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent>)

通知用户收到SSL客户端证书请求事件。

说明

* Web组件有三种响应方式：[ClientAuthenticationHandler.confirm](s-basic-components-web-clientauthenticationhandler.md#confirm10)（继续）、[ClientAuthenticationHandler.cancel](s-basic-components-web-clientauthenticationhandler.md#cancel9)（取消）或[ClientAuthenticationHandler.ignore](s-basic-components-web-clientauthenticationhandler.md#ignore9)（忽略）。
* 如果调用ClientAuthenticationHandler.confirm或ClientAuthenticationHandler.cancel，ArkWeb会将认证结果存储在内存中（在应用程序的生命周期内），并且不会对相同的主机和端口再次调用onClientAuthenticationRequest()。如果调用onClientAuthenticationRequest.ignore，ArkWeb则不会存储该认证结果。
* 需配置"ohos.permission.ACCESS\_CERT\_MANAGER"权限。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnClientAuthenticationEvent](arkts-basic-components-web-i.md#onclientauthenticationevent12)> | 是 | 当需要用户提供的SSL客户端证书时触发的回调。 |

**示例：**

安装私有凭证以实现双向认证。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { common } from '@kit.AbilityKit';
4. import { certificateManager } from '@kit.DeviceCertificateKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. @Entry
8. @Component
9. struct Index {
10. controller: WebviewController = new webview.WebviewController();
11. uiContext : UIContext = this.getUIContext();
12. context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
13. uri: string = ''

15. aboutToAppear(): void {
16. webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
17. }

19. build() {
20. Column() {
21. Button("installPrivateCertificate").onClick(() => {
22. if (!this.context) {
23. return;
24. }

26. // 注：badssl.com-client.p12需要替换为实际使用的证书文件
27. let value: Uint8Array = this.context.resourceManager.getRawFileContentSync("badssl.com-client.p12");
28. certificateManager.installPrivateCertificate(value, 'badssl.com', "1",
29. async (err: BusinessError, data: certificateManager.CMResult) => {
30. console.info(`installPrivateCertificate, uri==========${JSON.stringify(data.uri)}`)
31. if (!err && data.uri) {
32. this.uri = data.uri;
33. }
34. });
35. })
36. Button('加载需要客户端SSL证书的网站')
37. .onClick(() => {
38. this.controller.loadUrl("https://client.badssl.com")
39. })
40. Web({
41. src: "https://www.bing.com/",
42. controller: this.controller,
43. }).domStorageAccess(true)
44. .fileAccess(true)
45. .onPageBegin(event => {
46. console.info("extensions onpagebegin url " + event.url);
47. })
48. .onClientAuthenticationRequest((event) => {
49. console.info("onClientAuthenticationRequest ");
50. event.handler.confirm(this.uri);
51. })
52. .onSslErrorEventReceive(e => {
53. console.info(`onSslErrorEventReceive->${e.error.toString()}`);
54. })
55. .onErrorReceive((event) => {
56. if (event) {
57. this.getUIContext().getPromptAction().showToast({
58. message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
59. alignment: Alignment.Center
60. })
61. console.info('getErrorInfo:' + event.error.getErrorInfo());
62. console.info('getErrorCode:' + event.error.getErrorCode());
63. console.info('url:' + event.request.getRequestUrl());
64. }
65. })
66. .onTitleReceive(event  => {
67. console.info("title received " + event.title);
68. })

70. }
71. }
72. }
```

对接证书管理，实现双向认证功能。

1. 构造 GlobalContext 单例对象。

   ```
   1. // GlobalContext.ets
   2. export class GlobalContext {
   3. private constructor() {}
   4. private static instance: GlobalContext;
   5. private _objects = new Map<string, Object>();

   7. public static getContext(): GlobalContext {
   8. if (!GlobalContext.instance) {
   9. GlobalContext.instance = new GlobalContext();
   10. }
   11. return GlobalContext.instance;
   12. }

   14. getObject(value: string): Object | undefined {
   15. return this._objects.get(value);
   16. }

   18. setObject(key: string, objectClass: Object): void {
   19. this._objects.set(key, objectClass);
   20. }
   21. }
   ```
2. 构造 CertManagerService 对象以对接证书管理。

   ```
   1. // CertMgrService.ets
   2. import { bundleManager, common, Want } from "@kit.AbilityKit";
   3. import { BusinessError } from "@kit.BasicServicesKit";
   4. import { GlobalContext } from './GlobalContext';

   6. export default class CertManagerService {
   7. private static sInstance: CertManagerService;
   8. private authUri = "";
   9. private appUid = "";

   11. public static getInstance(): CertManagerService {
   12. if (CertManagerService.sInstance == null) {
   13. CertManagerService.sInstance = new CertManagerService();
   14. }
   15. return CertManagerService.sInstance;
   16. }

   18. async grantAppPm(): Promise<string> {
   19. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
   20. // 注：com.example.myapplication需要写实际应用名称
   21. try {
   22. const data = await bundleManager.getBundleInfoForSelf(bundleFlags)
   23. .catch((err: BusinessError) => {
   24. console.error('getBundleInfoForSelf failed. Cause: %{public}s', err.message);
   25. return null;
   26. });
   27. this.appUid = data?.appInfo?.uid?.toString() ?? '';
   28. console.info('getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
   29. } catch (err) {
   30. let message = (err as BusinessError).message;
   31. console.error('getBundleInfoForSelf failed: %{public}s', message);
   32. }

   34. // 注：需要在MainAbility.ts文件的onCreate函数里添加GlobalContext.getContext().setObject("AbilityContext", this.context)
   35. let abilityContext = GlobalContext.getContext().getObject("AbilityContext") as common.UIAbilityContext;
   36. await abilityContext.startAbilityForResult(
   37. {
   38. bundleName: "com.ohos.certmanager",
   39. abilityName: "MainAbility",
   40. uri: "requestAuthorize",
   41. parameters: {
   42. appUid: this.appUid, // 传入申请应用的appUid
   43. }
   44. } as Want)
   45. .then((data: common.AbilityResult) => {
   46. if (!data.resultCode && data.want) {
   47. if (data.want.parameters) {
   48. this.authUri = data.want.parameters.authUri as string; // 授权成功后获取返回的authUri
   49. }
   50. }
   51. })
   52. return this.authUri;
   53. }
   54. }
   ```
3. 将当前Ability的上下文存储到GlobalContext中。

   ```
   1. // EntryAbility.ets
   2. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { window } from '@kit.ArkUI';
   5. import { GlobalContext } from '../pages/GlobalContext';

   7. const DOMAIN = 0x0000;

   9. export default class EntryAbility extends UIAbility {
   10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   11. try {
   12. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
   13. GlobalContext.getContext().setObject("AbilityContext", this.context);
   14. } catch (err) {
   15. hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
   16. }
   17. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
   18. }

   20. onDestroy(): void {
   21. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
   22. }

   24. onWindowStageCreate(windowStage: window.WindowStage): void {
   25. // Main window is created, set main page for this ability
   26. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

   28. windowStage.loadContent('pages/Index', (err) => {
   29. if (err.code) {
   30. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
   31. return;
   32. }
   33. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   34. });
   35. }

   37. onWindowStageDestroy(): void {
   38. // Main window is destroyed, release UI related resources
   39. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
   40. }

   42. onForeground(): void {
   43. // Ability has brought to foreground
   44. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
   45. }

   47. onBackground(): void {
   48. // Ability has back to background
   49. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
   50. }
   51. }
   ```
4. 实现双向认证功能。

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import CertManagerService from './CertMgrService';

   4. @Entry
   5. @Component
   6. struct Index {
   7. controller: WebviewController = new webview.WebviewController();
   8. certManager = CertManagerService.getInstance();

   10. aboutToAppear(): void {
   11. webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
   12. }

   14. build() {
   15. Column() {
   16. Button('加载需要客户端SSL证书的网站')
   17. .onClick(() => {
   18. this.controller.loadUrl("https://client.badssl.com")
   19. })
   20. Web({
   21. src: "https://www.bing.com/",
   22. controller: this.controller,
   23. }).domStorageAccess(true)
   24. .fileAccess(true)
   25. .onPageBegin(event => {
   26. console.info("extensions onpagebegin url " + event.url);
   27. })
   28. .onClientAuthenticationRequest((event) => {
   29. console.info("onClientAuthenticationRequest ");

   31. this.certManager.grantAppPm().then(result => {
   32. console.info(`grantAppPm, URI==========${result}`);
   33. event.handler.confirm(result);
   34. })
   35. })
   36. .onSslErrorEventReceive(e => {
   37. console.info(`onSslErrorEventReceive->${e.error.toString()}`);
   38. })
   39. .onErrorReceive((event) => {
   40. if (event) {
   41. this.getUIContext().getPromptAction().showToast({
   42. message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
   43. alignment: Alignment.Center
   44. })
   45. console.info('getErrorInfo:' + event.error.getErrorInfo());
   46. console.info('getErrorCode:' + event.error.getErrorCode());
   47. console.info('url:' + event.request.getRequestUrl());
   48. }
   49. })
   50. .onTitleReceive(event  => {
   51. console.info("title received " + event.title);
   52. })

   54. }
   55. }
   56. }
   ```

## onVerifyPin22+

PhonePC/2in1TabletTVWearable

onVerifyPin(callback: OnVerifyPinCallback)

通知用户进行PIN码认证。使用callback异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnVerifyPinCallback](arkts-basic-components-web-t.md#onverifypincallback22) | 是 | 当需要用户进行PIN码认证时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { common } from '@kit.AbilityKit';
4. import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. @Entry
8. @Component
9. struct Index {
10. controller: WebviewController = new webview.WebviewController();
11. uiContext : UIContext = this.getUIContext();
12. context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;

14. aboutToAppear(): void {
15. webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
16. }

18. build() {
19. Column() {
20. Button('加载需要客户端SSL证书的网站')
21. .onClick(() => {
22. this.controller.loadUrl("https://client.badssl.com")
23. })
24. Web({
25. src: "https://www.bing.com/",
26. controller: this.controller,
27. }).domStorageAccess(true)
28. .fileAccess(true)
29. .onPageBegin(event => {
30. console.info("extensions onpagebegin url " + event.url);
31. })
32. .onClientAuthenticationRequest((event) => {
33. // 收到客户端证书请求事件
34. console.info(`onClientAuthenticationRequest`);
35. try {
36. let certTypes: Array<certificateManagerDialog.CertificateType> = [
37. certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
38. ];
39. // 调用证书管理，打开证书选择框
40. certificateManagerDialog.openAuthorizeDialog(this.context, { certTypes: certTypes })
41. .then((data: certificateManagerDialog.CertReference) => {
42. console.info(`openAuthorizeDialog request cred auth success`)
43. // 通知web选择的为ukey证书
44. event.handler.confirm(data.keyUri, CredentialType.CREDENTIAL_UKEY);
45. }).catch((err: BusinessError) => {
46. console.error(`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(err)}`);
47. })
48. } catch (e) {
49. console.error(`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(e)}`);
50. }
51. })
52. .onVerifyPin((event) => {
53. // 收到PIN码认证请求事件
54. console.info(`onVerifyPin`);
55. // 调用证书管理，打开PIN码输入框
56. certificateManagerDialog.openUkeyAuthDialog(this.context, {keyUri: event.identity})
57. .then(() => {
58. // 通知webPIN码认证成功
59. console.info(`onVerifyPin success`);
60. event.handler.confirm(PinVerifyResult.PIN_VERIFICATION_SUCCESS);
61. }).catch((err: BusinessError) => {
62. // 通知webPIN码认证失败
63. console.info(`onVerifyPin fail`);
64. event.handler.confirm(PinVerifyResult.PIN_VERIFICATION_FAILED);
65. })
66. })
67. .onSslErrorEventReceive(e => {
68. console.info(`onSslErrorEventReceive->${e.error.toString()}`);
69. })
70. .onErrorReceive((event) => {
71. if (event) {
72. this.getUIContext().getPromptAction().showToast({
73. message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
74. alignment: Alignment.Center
75. })
76. console.info('getErrorInfo:' + event.error.getErrorInfo());
77. console.info('getErrorCode:' + event.error.getErrorCode());
78. console.info('url:' + event.request.getRequestUrl());
79. }
80. })
81. .onTitleReceive(event  => {
82. console.info("title received " + event.title);
83. })

85. }
86. }
87. }
```

## onPermissionRequest9+

PhonePC/2in1TabletTVWearable

onPermissionRequest(callback: Callback<OnPermissionRequestEvent>)

通知收到获取权限请求，需配置"ohos.permission.CAMERA"、"ohos.permission.MICROPHONE"权限。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnPermissionRequestEvent](arkts-basic-components-web-i.md#onpermissionrequestevent12)> | 是 | 通知收到获取权限请求触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { abilityAccessCtrl } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();
10. uiContext: UIContext = this.getUIContext();

12. aboutToAppear() {
13. // 配置Web开启调试模式
14. webview.WebviewController.setWebDebuggingAccess(true);
15. let atManager = abilityAccessCtrl.createAtManager();
16. atManager.requestPermissionsFromUser(this.uiContext.getHostContext(), ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
17. .then((data) => {
18. console.info('data:' + JSON.stringify(data));
19. console.info('data permissions:' + data.permissions);
20. console.info('data authResults:' + data.authResults);
21. }).catch((error: BusinessError) => {
22. console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
23. })
24. }

26. build() {
27. Column() {
28. Web({ src: $rawfile('index.html'), controller: this.controller })
29. .onPermissionRequest((event) => {
30. if (event) {
31. this.uiContext.showAlertDialog({
32. title: 'title',
33. message: 'text',
34. primaryButton: {
35. value: 'deny',
36. action: () => {
37. event.request.deny();
38. }
39. },
40. secondaryButton: {
41. value: 'onConfirm',
42. action: () => {
43. event.request.grant(event.request.getAccessibleResource());
44. }
45. },
46. cancel: () => {
47. event.request.deny();
48. }
49. })
50. }
51. })
52. }
53. }
54. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. </head>
7. <body>
8. <video id="video" width="500px" height="500px" autoplay></video>
9. <canvas id="canvas" width="500px" height="500px"></canvas>
10. <br>
11. <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()"/>
12. <script>
13. function getMedia()
14. {
15. let constraints = {
16. video: {width: 500, height: 500},
17. audio: true
18. };
19. // 获取video摄像头区域
20. let video = document.getElementById("video");
21. // 返回的Promise对象
22. let promise = navigator.mediaDevices.getUserMedia(constraints);
23. // then()异步，调用MediaStream对象作为参数
24. promise.then(function (MediaStream) {
25. video.srcObject = MediaStream;
26. video.play();
27. }).catch(function(error) {
28. console.error("Error accessing media devices.", error);
29. });
30. }
31. </script>
32. </body>
33. </html>
```

## onContextMenuShow9+

PhonePC/2in1TabletTVWearable

onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean>)

长按特定元素（例如图片，链接）或鼠标右键，弹出菜单。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnContextMenuShowEvent](arkts-basic-components-web-i.md#oncontextmenushowevent12), boolean> | 是 | 调用时触发的回调，以允许自定义显示上下文菜单。  返回值boolean。返回true表示触发自定义菜单，返回false表示触发的自定义菜单无效。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { pasteboard } from '@kit.BasicServicesKit';

5. const TAG = 'ContextMenu';

7. @Entry
8. @Component
9. struct WebComponent {
10. controller: webview.WebviewController = new webview.WebviewController();
11. private result: WebContextMenuResult | undefined = undefined;
12. @State linkUrl: string = '';
13. @State offsetX: number = 0;
14. @State offsetY: number = 0;
15. @State showMenu: boolean = false;
16. uiContext: UIContext = this.getUIContext();

18. @Builder
19. // 构建自定义菜单及触发功能接口
20. MenuBuilder() {
21. // 以垂直列表形式显示的菜单。
22. Menu() {
23. // 展示菜单Menu中具体的item菜单项。
24. MenuItem({
25. content: '撤销',
26. })
27. .width(100)
28. .height(50)
29. .onClick(() => {
30. this.result?.undo();
31. this.showMenu = false;
32. })
33. MenuItem({
34. content: '重做',
35. })
36. .width(100)
37. .height(50)
38. .onClick(() => {
39. this.result?.redo();
40. this.showMenu = false;
41. })
42. MenuItem({
43. content: '粘贴为纯文本',
44. })
45. .width(100)
46. .height(50)
47. .onClick(() => {
48. this.result?.pasteAndMatchStyle();
49. this.showMenu = false;
50. })
51. MenuItem({
52. content: '复制图片',
53. })
54. .width(100)
55. .height(50)
56. .onClick(() => {
57. this.result?.copyImage();
58. this.showMenu = false;
59. })
60. MenuItem({
61. content: '剪切',
62. })
63. .width(100)
64. .height(50)
65. .onClick(() => {
66. this.result?.cut();
67. this.showMenu = false;
68. })
69. MenuItem({
70. content: '复制',
71. })
72. .width(100)
73. .height(50)
74. .onClick(() => {
75. this.result?.copy();
76. this.showMenu = false;
77. })
78. MenuItem({
79. content: '粘贴',
80. })
81. .width(100)
82. .height(50)
83. .onClick(() => {
84. this.result?.paste();
85. this.showMenu = false;
86. })
87. MenuItem({
88. content: '复制链接',
89. })
90. .width(100)
91. .height(50)
92. .onClick(() => {
93. let pasteData = pasteboard.createData('text/plain', this.linkUrl);
94. pasteboard.getSystemPasteboard().setData(pasteData, (error) => {
95. if (error) {
96. return;
97. }
98. })
99. this.showMenu = false;
100. })
101. MenuItem({
102. content: '全选',
103. })
104. .width(100)
105. .height(50)
106. .onClick(() => {
107. this.result?.selectAll();
108. this.showMenu = false;
109. })
110. }
111. .width(150)
112. .height(450)
113. }

115. build() {
116. Column() {
117. Web({ src: $rawfile("index.html"), controller: this.controller })
118. // 触发自定义弹窗
119. .onContextMenuShow((event) => {
120. if (event) {
121. this.result = event.result
122. console.info(TAG + "x coord = " + event.param.x());
123. console.info(TAG + "link url = " + event.param.getLinkUrl());
124. this.linkUrl = event.param.getLinkUrl();
125. }
126. console.info(TAG, `x: ${this.offsetX}, y: ${this.offsetY}`);
127. this.showMenu = true;
128. this.offsetX = 0;
129. this.offsetY = Math.max(this.uiContext!.px2vp(event?.param.y() ?? 0) - 0, 0);
130. return true;
131. })
132. .bindPopup(this.showMenu,
133. {
134. builder: this.MenuBuilder(),
135. enableArrow: false,
136. placement: Placement.LeftTop,
137. offset: { x: this.offsetX, y: this.offsetY },
138. mask: false,
139. onStateChange: (e) => {
140. if (!e.isVisible) {
141. this.showMenu = false;
142. this.result!.closeContextMenu();
143. }
144. }
145. })
146. }
147. }
148. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html lang="en">
4. <body>
5. <h1>onContextMenuShow</h1>
6. <a href="http://www.example.com" style="font-size:27px">链接www.example.com</a>
7. <!-- rawfile下放任意一张图片命名为example.png -->
8. <div><img src="example.png"></div>
9. <p>选中文字鼠标右键弹出菜单</p>
10. </body>
11. </html>
```

## onContextMenuHide11+

PhonePC/2in1TabletTVWearable

onContextMenuHide(callback: OnContextMenuHideCallback)

长按特定元素（例如图片，链接）或鼠标右键，隐藏菜单。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnContextMenuHideCallback](arkts-basic-components-web-t.md#oncontextmenuhidecallback11) | 是 | 菜单相关回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onContextMenuHide(() => {
13. console.info("onContextMenuHide callback");
14. })
15. }
16. }
17. }
```

## onScroll9+

PhonePC/2in1TabletTVWearable

onScroll(callback: Callback<OnScrollEvent>)

通知网页全局滚动位置。

说明

通知的是页面全局滚动位置，局部滚动位置的变化是无法触发此回调。

判断页面是否是全局滚动，在滚动前后打印window.pageYOffset或者window.pageXOffset。

如果是全局滚动，window.pageYOffset或者window.pageXOffset的值在滚动前后会有变化，反之没有变化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnScrollEvent](arkts-basic-components-web-i.md#onscrollevent12)> | 是 | 当页面滚动到指定位置时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onScroll((event) => {
13. console.info("x = " + event.xOffset);
14. console.info("y = " + event.yOffset);
15. })
16. }
17. }
18. }
```

## onGeolocationShow

PhonePC/2in1TabletTVWearable

onGeolocationShow(callback: Callback<OnGeolocationShowEvent>)

通知用户收到地理位置信息获取请求，需配置"ohos.permission.LOCATION"、"ohos.permission.APPROXIMATELY\_LOCATION"权限。使用callback异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnGeolocationShowEvent](arkts-basic-components-web-i.md#ongeolocationshowevent12)> | 是 | 回调函数，请求显示地理位置权限时触发，返回地理位置信息请求对象。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { abilityAccessCtrl, common } from '@kit.AbilityKit';

6. let atManager = abilityAccessCtrl.createAtManager();

8. @Entry
9. @Component
10. struct WebComponent {
11. controller: webview.WebviewController = new webview.WebviewController();
12. uiContext: UIContext = this.getUIContext();

14. // 组件的声明周期函数，创建组件实例后触发
15. aboutToAppear(): void {
16. let context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
17. if (!context) {
18. console.error("context is undefined");
19. return;
20. }
21. // 向用户请求位置权限
22. atManager.requestPermissionsFromUser(context, ["ohos.permission.LOCATION", "ohos.permission.APPROXIMATELY_LOCATION"]).then((data) => {
23. console.info('data:' + JSON.stringify(data));
24. console.info('data permissions:' + data.permissions);
25. console.info('data authResults:' + data.authResults);
26. }).catch((error: BusinessError) => {
27. console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
28. })
29. }

31. build() {
32. Column() {
33. Web({ src: $rawfile('index.html'), controller: this.controller })
34. .geolocationAccess(true)
35. .onGeolocationShow((event) => {
36. if (event) {
37. this.uiContext.showAlertDialog({
38. title: 'title',
39. message: 'text',
40. confirm: {
41. value: 'onConfirm',
42. action: () => {
43. // invoke的第三个参数表示是否记住当前弹窗的选择状态，如果传入true，则下次不再弹出对话框
44. event.geolocation.invoke(event.origin, true, false);
45. }
46. },
47. cancel: () => {
48. // invoke的第三个参数表示是否记住当前弹窗的选择状态，如果传入true，则下次不再弹出对话框
49. event.geolocation.invoke(event.origin, false, false);
50. }
51. })
52. }
53. })
54. }
55. }
56. }
```

加载的html文件。

```
1. <!DOCTYPE html>
2. <html>
3. <body>
4. <p id="locationInfo">位置信息</p>
5. <button onclick="getLocation()">获取位置</button>
6. <script>
7. var locationInfo=document.getElementById("locationInfo");
8. function getLocation(){
9. if (navigator.geolocation) {
10. // 前端页面访问设备地理位置
11. navigator.geolocation.getCurrentPosition(showPosition);
12. }
13. }
14. function showPosition(position){
15. locationInfo.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;
16. }
17. </script>
18. </body>
19. </html>
```

## onGeolocationHide

PhonePC/2in1TabletTVWearable

onGeolocationHide(callback: () => void)

通知用户先前被调用[onGeolocationShow](arkts-basic-components-web-events.md#ongeolocationshow)时收到地理位置信息获取请求已被取消。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 地理位置信息获取请求已被取消的回调函数。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .geolocationAccess(true)
13. .onGeolocationHide(() => {
14. console.info("onGeolocationHide...");
15. })
16. }
17. }
18. }
```

## onFullScreenEnter9+

PhonePC/2in1TabletTVWearable

onFullScreenEnter(callback: OnFullScreenEnterCallback)

通知开发者Web组件进入全屏模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnFullScreenEnterCallback](arkts-basic-components-web-t.md#onfullscreenentercallback12) | 是 | Web组件进入全屏时的回调信息。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. handler: FullScreenExitHandler | null = null;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .onFullScreenEnter((event) => {
14. console.info("onFullScreenEnter videoWidth: " + event.videoWidth +
15. ", videoHeight: " + event.videoHeight);
16. // 应用可以通过 this.handler.exitFullScreen() 主动退出全屏。
17. this.handler = event.handler;
18. })
19. }
20. }
21. }
```

## onFullScreenExit9+

PhonePC/2in1TabletTVWearable

onFullScreenExit(callback: () => void)

通知开发者Web组件退出全屏模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 退出全屏模式时的回调函数。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. handler: FullScreenExitHandler | null = null;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .onFullScreenExit(() => {
14. console.info("onFullScreenExit...")
15. if (this.handler) {
16. this.handler.exitFullScreen();
17. }
18. })
19. .onFullScreenEnter((event) => {
20. this.handler = event.handler;
21. })
22. }
23. }
24. }
```

## onWindowNew9+

PhonePC/2in1TabletTVWearable

onWindowNew(callback: Callback<OnWindowNewEvent>)

使能multiWindowAccess情况下，通知用户新建窗口请求。

若不调用[setWebController](arkts-basic-components-web-controllerhandler.md#setwebcontroller9)接口，会造成render进程阻塞。

如果没有创建新窗口，调用[setWebController](arkts-basic-components-web-controllerhandler.md#setwebcontroller9)接口时设置成null，通知Web没有创建新窗口。

新窗口需避免直接覆盖在原Web组件上，且应与主页面以相同形式明确显示其URL（如地址栏）以防止用户混淆。若无法实现可信的URL可视化管理，则需考虑禁止创建新窗口。

需注意：新窗口请求来源无法可靠追溯，可能由第三方iframe发起，应用需默认采取沙箱隔离、限制权限等防御性措施以确保安全。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnWindowNewEvent](arkts-basic-components-web-i.md#onwindownewevent12)> | 是 | 网页要求用户创建窗口时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
5. @CustomDialog
6. struct NewWebViewComp {
7. controller?: CustomDialogController;
8. webviewController1: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: "www.example.com", controller: this.webviewController1 })
13. .javaScriptAccess(true)
14. .multiWindowAccess(false)
15. .onWindowExit(() => {
16. console.info("NewWebViewComp onWindowExit");
17. if (this.controller) {
18. this.controller.close();
19. }
20. })
21. }
22. }
23. }

25. @Entry
26. @Component
27. struct WebComponent {
28. controller: webview.WebviewController = new webview.WebviewController();
29. dialogController: CustomDialogController | null = null;

31. build() {
32. Column() {
33. Web({ src: $rawfile("window.html"), controller: this.controller })
34. .javaScriptAccess(true)
35. // 需要使能multiWindowAccess
36. .multiWindowAccess(true)
37. .allowWindowOpenMethod(true)
38. .onWindowNew((event) => {
39. if (this.dialogController) {
40. this.dialogController.close();
41. }
42. let popController: webview.WebviewController = new webview.WebviewController();
43. this.dialogController = new CustomDialogController({
44. builder: NewWebViewComp({ webviewController1: popController })
45. })
46. this.dialogController.open();
47. // 将新窗口对应WebviewController返回给Web内核。
48. // 若不调用event.handler.setWebController接口，会造成render进程阻塞。
49. // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
50. event.handler.setWebController(popController);
51. })
52. }
53. }
54. }
```

```
1. <!-- window.html页面代码 -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. </head>
8. <body>
9. <a href="#" onclick="openNewWindow('https://www.example.com')">打开新页面</a>
10. <script type="text/javascript">
11. function openNewWindow(url) {
12. window.open(url, 'example');
13. return false;
14. }
15. </script>
16. </body>
17. </html>
```

## onWindowNewExt23+

PhonePC/2in1TabletTVWearable

onWindowNewExt(callback: Callback<OnWindowNewExtEvent>)

在启用[multiWindowAccess](arkts-basic-components-web-attributes.md#multiwindowaccess9)的情况下，通知用户新建窗口请求。

说明

* 若不调用[setWebController](arkts-basic-components-web-controllerhandler.md#setwebcontroller9)接口，会造成render进程阻塞。
* 若未创建新窗口，调用[setWebController](arkts-basic-components-web-controllerhandler.md#setwebcontroller9)接口并设置成null，通知Web未创建新窗口。
* 新窗口需避免直接覆盖在原Web组件上，且应与主页面以相同形式明确显示其URL（如地址栏）以防止用户混淆。若无法确保URL的显示和验证机制可靠，则需考虑禁止创建新窗口。
* 新窗口请求来源无法可靠追溯，可能由第三方iframe发起，应用需默认采取沙箱隔离、限制权限等防御性措施以确保安全。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnWindowNewExtEvent](arkts-basic-components-web-i.md#onwindownewextevent23)> | 是 | 网页要求用户创建窗口时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
5. @CustomDialog
6. struct NewWebViewComp {
7. controller?: CustomDialogController;
8. webviewController1: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: "www.example.com", controller: this.webviewController1 })
13. .javaScriptAccess(true)
14. .multiWindowAccess(false)
15. .onWindowExit(() => {
16. console.info("NewWebViewComp onWindowExit");
17. if (this.controller) {
18. this.controller.close();
19. }
20. })
21. }
22. }
23. }

25. @Entry
26. @Component
27. struct WebComponent {
28. controller: webview.WebviewController = new webview.WebviewController();
29. dialogController: CustomDialogController | null = null;

31. build() {
32. Column() {
33. Web({ src: $rawfile("window.html"), controller: this.controller })
34. .javaScriptAccess(true)
35. // 需要开启multiWindowAccess
36. .multiWindowAccess(true)
37. .allowWindowOpenMethod(true)
38. .onWindowNewExt((event) => {
39. // 以event.navigationPolicy请求的方式打开新窗口
40. console.info("navigationAction: ", event.navigationPolicy)
41. // 以event.windowFeatures中的大小及位置信息创建新窗口
42. console.info("windowFeatures: ", JSON.stringify(event.windowFeatures))
43. if (this.dialogController) {
44. this.dialogController.close();
45. }
46. let popController: webview.WebviewController = new webview.WebviewController();
47. this.dialogController = new CustomDialogController({
48. builder: NewWebViewComp({ webviewController1: popController })
49. })
50. this.dialogController.open();
51. // 将新窗口对应WebviewController返回给Web内核。
52. // 若不调用event.handler.setWebController接口，会造成render进程阻塞。
53. // 如果没有创建新窗口，在调用event.handler.setWebController接口时应设置成null，以通知Web没有创建新窗口。
54. event.handler.setWebController(popController);
55. })
56. }
57. }
58. }
```

```
1. <!-- window.html页面代码 -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. </head>
8. <body>
9. <a href="#" onclick="openNewWindow('https://www.example.com')">打开新页面</a>
10. <script type="text/javascript">
11. function openNewWindow(url) {
12. window.open(url, 'example', 'left=60,top=80,width=800,height=600');
13. return false;
14. }
15. </script>
16. </body>
17. </html>
```

## onActivateContent20+

PhonePC/2in1TabletTVWearable

onActivateContent(callback: Callback<void>)

当Web页面触发window.open(url, name)时，会根据name查找是否存在已绑定的Web实例。若存在，该实例将收到此回调以通知应用需将其展示至前端；若不存在，则通过[onWindowNew](arkts-basic-components-web-events.md#onwindownew9)通知应用创建新Web实例。

说明

* 通过name绑定Web实例‌：需在[onWindowNew](arkts-basic-components-web-events.md#onwindownew9)回调中调用event.handler.setWebController方法，并传入新Web实例的controller，以完成绑定。
* name‌命名需符合正则表达式[a-zA-Z0-9\_]+。当该name被用作<a>或<form>标签的target属性值时，已绑定的Web实例同样会触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 再次在原页面触发window.open后，在已打开的新页面触发该回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
5. @CustomDialog
6. struct NewWebViewComp {
7. controller?: CustomDialogController;
8. webviewController1: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: "https://www.example.com", controller: this.webviewController1 })
13. .javaScriptAccess(true)
14. .multiWindowAccess(false)
15. .onWindowExit(() => {
16. if (this.controller) {
17. this.controller.close();
18. }
19. })
20. .onActivateContent(() => {
21. // 该Web需要展示到前面，建议应用在这里进行tab或window切换的动作展示此web
22. console.info("NewWebViewComp onActivateContent")
23. })
24. }.height("50%")
25. }
26. }

28. @Entry
29. @Component
30. struct WebComponent {
31. controller: webview.WebviewController = new webview.WebviewController();
32. dialogController: CustomDialogController | null = null;

34. build() {
35. Column() {
36. Web({ src: $rawfile("window.html"), controller: this.controller })
37. .javaScriptAccess(true)
38. .allowWindowOpenMethod(true)
39. // 需要使能multiWindowAccess
40. .multiWindowAccess(true)
41. .onWindowNew((event) => {
42. if (this.dialogController) {
43. this.dialogController.close()
44. }
45. let popController: webview.WebviewController = new webview.WebviewController();
46. this.dialogController = new CustomDialogController({
47. builder: NewWebViewComp({ webviewController1: popController }),
48. isModal: false
49. })
50. this.dialogController.open();
51. // 将新窗口对应WebviewController返回给Web内核。
52. // 若不调用event.handler.setWebController接口，会造成render进程阻塞。
53. event.handler.setWebController(popController);
54. })
55. }
56. }
57. }
```

```
1. <!-- window.html页面代码 -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. <title>ActivateContentEvent</title>
8. </head>
9. <body>
10. <a href="#" onclick="openNewWindow('https://www.example.com')">打开新页面</a>
11. <script type="text/javascript">
12. function openNewWindow(url) {
13. window.open(url, 'example');
14. return false;
15. }
16. </script>
17. </body>
18. </html>
```

## onWindowExit9+

PhonePC/2in1TabletTVWearable

onWindowExit(callback: () => void)

通知用户窗口关闭请求。和[onWindowNew](arkts-basic-components-web-events.md#onwindownew9)一样，从安全角度讲，应用应该确保用户可以知道他们交互的页面已关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 窗口请求关闭的回调函数。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onWindowExit(() => {
13. console.info("onWindowExit...");
14. })
15. }
16. }
17. }
```

## onSearchResultReceive9+

PhonePC/2in1TabletTVWearable

onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent>)

回调通知调用方网页页内查找的结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnSearchResultReceiveEvent](arkts-basic-components-web-i.md#onsearchresultreceiveevent12)> | 是 | 通知调用方网页页内查找的结果。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onSearchResultReceive(ret => {
13. if (ret) {
14. console.info("on search result receive:" + "[cur]" + ret.activeMatchOrdinal +
15. "[total]" + ret.numberOfMatches + "[isDone]" + ret.isDoneCounting);
16. }
17. })
18. }
19. }
20. }
```

## onDataResubmitted9+

PhonePC/2in1TabletTVWearable

onDataResubmitted(callback: Callback<OnDataResubmittedEvent>)

设置网页表单可以重新提交时触发的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnDataResubmittedEvent](arkts-basic-components-web-i.md#ondataresubmittedevent12)> | 是 | 网页表单可以重新提交时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. // 在网页中点击提交之后，点击refresh按钮可以重新提交时的触发函数。
13. Button('refresh')
14. .onClick(() => {
15. try {
16. this.controller.refresh();
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: $rawfile('index.html'), controller: this.controller })
22. .onDataResubmitted((event) => {
23. console.info('onDataResubmitted');
24. event.handler.resend();
25. })
26. }
27. }
28. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body>
8. <form action="http://httpbin.org/post" method="post">
9. <input type="text" name="username">
10. <input type="submit" name="提交">
11. </form>
12. </body>
13. </html>
```

## onPageVisible9+

PhonePC/2in1TabletTVWearable

onPageVisible(callback: Callback<OnPageVisibleEvent>)

设置旧页面不再呈现，新页面即将可见时触发的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnPageVisibleEvent](arkts-basic-components-web-i.md#onpagevisibleevent12)> | 是 | 旧页面不再呈现，新页面即将可见时触发的回调函数。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onPageVisible((event) => {
13. console.info('onPageVisible url:' + event.url);
14. })
15. }
16. }
17. }
```

## onInterceptKeyEvent9+

PhonePC/2in1TabletTVWearable

onInterceptKeyEvent(callback: (event: KeyEvent) => boolean)

设置键盘事件的回调函数，该回调在被Webview使用前触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event:[KeyEvent](ts-universal-events-key.md#keyevent对象说明)) => boolean | 是 | 触发的KeyEvent事件。  返回值为boolean类型，true表示将该KeyEvent传入Webview内核，false表示不将该KeyEvent传入Webview内核。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onInterceptKeyEvent((event) => {
13. if (event.keyCode == 2017 || event.keyCode == 2018) {
14. console.info(`onInterceptKeyEvent get event.keyCode ${event.keyCode}`);
15. return true;
16. }
17. return false;
18. })
19. }
20. }
21. }
```

## onTouchIconUrlReceived9+

PhonePC/2in1TabletTVWearable

onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent>)

设置接收到apple-touch-icon url地址时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnTouchIconUrlReceivedEvent](arkts-basic-components-web-i.md#ontouchiconurlreceivedevent12)> | 是 | 接收到的apple-touch-icon url地址时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.baidu.com', controller: this.controller })
12. .onTouchIconUrlReceived((event) => {
13. console.info('onTouchIconUrlReceived:' + JSON.stringify(event));
14. })
15. }
16. }
17. }
```

## onFaviconReceived9+

PhonePC/2in1TabletTVWearable

onFaviconReceived(callback: Callback<OnFaviconReceivedEvent>)

设置应用为当前页面接收到新的favicon时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnFaviconReceivedEvent](arkts-basic-components-web-i.md#onfaviconreceivedevent12)> | 是 | 当前页面接收到新的favicon时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { image } from '@kit.ImageKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State icon: image.PixelMap | undefined = undefined;

11. build() {
12. Column() {
13. Web({ src: 'www.example.com', controller: this.controller })
14. .onFaviconReceived((event) => {
15. console.info('onFaviconReceived');
16. this.icon = event.favicon;
17. })
18. }
19. }
20. }
```

## onAudioStateChanged10+

PhonePC/2in1TabletTVWearable

onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent>)

设置网页上的音频播放状态发生改变时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnAudioStateChangedEvent](arkts-basic-components-web-i.md#onaudiostatechangedevent12)> | 是 | 网页上的音频播放状态发生改变时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State playing: boolean = false;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .onAudioStateChanged(event => {
14. this.playing = event.playing;
15. console.info('onAudioStateChanged playing: ' + this.playing);
16. })
17. }
18. }
19. }
```

## onFirstContentfulPaint10+

PhonePC/2in1TabletTVWearable

onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent>)

设置网页首次内容绘制回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnFirstContentfulPaintEvent](arkts-basic-components-web-i.md#onfirstcontentfulpaintevent12)> | 是 | 网页首次内容绘制回调函数。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onFirstContentfulPaint(event => {
13. if (event) {
14. console.info("onFirstContentfulPaint:" + "[navigationStartTick]:" +
15. event.navigationStartTick + ", [firstContentfulPaintMs]:" +
16. event.firstContentfulPaintMs);
17. }
18. })
19. }
20. }
21. }
```

## onFirstMeaningfulPaint12+

PhonePC/2in1TabletTVWearable

onFirstMeaningfulPaint(callback: [OnFirstMeaningfulPaintCallback](arkts-basic-components-web-t.md#onfirstmeaningfulpaintcallback12))

设置网页绘制页面主要内容回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnFirstMeaningfulPaintCallback](arkts-basic-components-web-t.md#onfirstmeaningfulpaintcallback12) | 是 | 网页绘制页面主要内容度量信息的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onFirstMeaningfulPaint((details) => {
13. console.info("onFirstMeaningfulPaint: [navigationStartTime]= " + details.navigationStartTime +
14. ", [firstMeaningfulPaintTime]=" + details.firstMeaningfulPaintTime);
15. })
16. }
17. }
18. }
```

## onLargestContentfulPaint12+

PhonePC/2in1TabletTVWearable

onLargestContentfulPaint(callback: [OnLargestContentfulPaintCallback](arkts-basic-components-web-t.md#onlargestcontentfulpaintcallback12))

设置网页绘制页面最大内容回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnLargestContentfulPaintCallback](arkts-basic-components-web-t.md#onlargestcontentfulpaintcallback12) | 是 | 网页绘制页面最大内容度量信息的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onLargestContentfulPaint((details) => {
13. console.info("onLargestContentfulPaint: [navigationStartTime]= " + details.navigationStartTime +
14. ", [largestImagePaintTime]=" + details.largestImagePaintTime +
15. ", [largestTextPaintTime]=" + details.largestTextPaintTime +
16. ", [largestImageLoadStartTime]=" + details.largestImageLoadStartTime +
17. ", [largestImageLoadEndTime]=" + details.largestImageLoadEndTime +
18. ", [imageBPP]=" + details.imageBPP);
19. })
20. }
21. }
22. }
```

## onLoadIntercept10+

PhonePC/2in1TabletTVWearable

onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean>)

当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnLoadInterceptEvent](arkts-basic-components-web-i.md#onloadinterceptevent12), boolean> | 是 | 导航触发时的回调包括iframe导航，在回调中可以选择允许或者取消此次导航。  返回值为boolean类型。返回true表示取消此次导航，false表示允许此次导航。  返回undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onLoadIntercept((event) => {
13. console.info('url:' + event.data.getRequestUrl());
14. console.info('isMainFrame:' + event.data.isMainFrame());
15. console.info('isRedirect:' + event.data.isRedirect());
16. console.info('isRequestGesture:' + event.data.isRequestGesture());
17. return true;
18. })
19. }
20. }
21. }
```

## onRequestSelected

PhonePC/2in1TabletTVWearable

onRequestSelected(callback: () => void)

当Web组件获取焦点时触发回调。如果组件在未获焦状态下加载网页并成功获取焦点，将触发两次回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 当网页获取焦点时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onRequestSelected(() => {
13. console.info('onRequestSelected');
14. })
15. }
16. }
17. }
```

## onScreenCaptureRequest10+

PhonePC/2in1TabletTVWearable

onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent>)

通知收到屏幕捕获请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnScreenCaptureRequestEvent](arkts-basic-components-web-i.md#onscreencapturerequestevent12)> | 是 | 通知收到屏幕捕获请求。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. uiContext: UIContext = this.getUIContext();

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .onScreenCaptureRequest((event) => {
14. if (event) {
15. this.uiContext.showAlertDialog({
16. title: 'title: ' + event.handler.getOrigin(),
17. message: 'text',
18. primaryButton: {
19. value: 'deny',
20. action: () => {
21. event.handler.deny();
22. }
23. },
24. secondaryButton: {
25. value: 'onConfirm',
26. action: () => {
27. event.handler.grant({ captureMode: WebCaptureMode.HOME_SCREEN });
28. }
29. },
30. cancel: () => {
31. event.handler.deny();
32. }
33. })
34. }
35. })
36. }
37. }
38. }
```

## onOverScroll10+

PhonePC/2in1TabletTVWearable

onOverScroll(callback: Callback<OnOverScrollEvent>)

该接口在网页过度滚动时触发，用于通知网页过度滚动的偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnOverScrollEvent](arkts-basic-components-web-i.md#onoverscrollevent12)> | 是 | 网页过度滚动时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onOverScroll((event) => {
13. console.info("x = " + event.xOffset);
14. console.info("y = " + event.yOffset);
15. })
16. }
17. }
18. }
```

## onControllerAttached10+

PhonePC/2in1TabletTVWearable

onControllerAttached(callback: () => void)

当Controller成功绑定到Web组件时触发该回调，并且该Controller必须为WebviewController，且禁止在该事件回调前调用Web组件相关的接口，否则会抛出js-error异常。

因该回调调用时网页还未加载，无法在回调中使用有关操作网页的接口，例如[zoomIn](arkts-apis-webview-webviewcontroller.md#zoomin)、[zoomOut](arkts-apis-webview-webviewcontroller.md#zoomout)等，可以使用[loadUrl](arkts-apis-webview-webviewcontroller.md#loadurl)、[getWebId](arkts-apis-webview-webviewcontroller.md#getwebid)等操作网页不相关的接口。

组件生命周期详情可参考[Web组件的生命周期](../harmonyos-guides/web-event-sequence.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 当ArkWeb控制器初始化成功时触发的回调。 |

**示例：**

在该回调中使用loadUrl加载网页

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: '', controller: this.controller })
12. .onControllerAttached(() => {
13. this.controller.loadUrl($rawfile("index.html"));
14. })
15. }
16. }
17. }
```

在该回调中使用getWebId

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: $rawfile("index.html"), controller: this.controller })
13. .onControllerAttached(() => {
14. try {
15. let id = this.controller.getWebId();
16. console.info("id: " + id);
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`ErrorCode: ${code},  Message: ${message}`);
21. }
22. })
23. }
24. }
25. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <p>Hello World</p>
6. </body>
7. </html>
```

## onNavigationEntryCommitted11+

PhonePC/2in1TabletTVWearable

onNavigationEntryCommitted(callback: [OnNavigationEntryCommittedCallback](arkts-basic-components-web-t.md#onnavigationentrycommittedcallback11))

当网页跳转提交时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnNavigationEntryCommittedCallback](arkts-basic-components-web-t.md#onnavigationentrycommittedcallback11) | 是 | 网页跳转提交时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onNavigationEntryCommitted((details) => {
13. console.info("onNavigationEntryCommitted: [isMainFrame]= " + details.isMainFrame +
14. ", [isSameDocument]=" + details.isSameDocument +
15. ", [didReplaceEntry]=" + details.didReplaceEntry +
16. ", [navigationType]=" + details.navigationType +
17. ", [url]=" + details.url);
18. })
19. }
20. }
21. }
```

## onSafeBrowsingCheckResult11+

PhonePC/2in1TabletTVWearable

onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback)

收到网站安全风险检查结果时触发的回调。

说明

* 需要使用release包，debug包不生效。
* 开启未成年模式，设置网页内容拦截，触发回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-basic-components-web-t.md#onsafebrowsingcheckresultcallback11) | 是 | 收到网站安全风险检查结果时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onSafeBrowsingCheckResult((callback) => {
13. let json: ThreatType = JSON.parse(JSON.stringify(callback)).threatType;
14. console.info("onSafeBrowsingCheckResult: [threatType]= " + json);
15. })
16. }
17. }
18. }
```

## onSafeBrowsingCheckFinish21+

PhonePC/2in1TabletTVWearable

onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback)

网站安全风险检查结束时触发的回调。

说明

* 需要使用release包，debug包不生效。
* 开启未成年模式，设置网页内容拦截，触发回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-basic-components-web-t.md#onsafebrowsingcheckresultcallback11) | 是 | 收到网站安全风险检查结果时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onSafeBrowsingCheckFinish((callback) => {
13. let json: ThreatType = JSON.parse(JSON.stringify(callback)).threatType;
14. console.info("onSafeBrowsingCheckFinish: [threatType]= " + json);
15. })
16. }
17. }
18. }
```

## onNativeEmbedLifecycleChange11+

PhonePC/2in1TabletTVWearable

onNativeEmbedLifecycleChange(callback: (event: NativeEmbedDataInfo) => void)

当同层标签生命周期变化时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event: [NativeEmbedDataInfo](arkts-basic-components-web-i.md#nativeembeddatainfo11)) => void | 是 | 同层标签生命周期变化时触发该回调。 |

**示例：**

```
1. // EntryAbility.ets

3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { window } from '@kit.ArkUI';
6. import { webview } from '@kit.ArkWeb';

8. export default class EntryAbility extends UIAbility {
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
10. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
11. // API12新增：开启同层渲染BFCache开关
12. let features = new webview.BackForwardCacheSupportedFeatures();
13. features.nativeEmbed = true;
14. features.mediaTakeOver = true;
15. webview.WebviewController.enableBackForwardCache(features);
16. webview.WebviewController.initializeWebEngine();
17. }

19. onDestroy(): void {
20. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
21. }

23. onWindowStageCreate(windowStage: window.WindowStage): void {
24. // Main window is created, set main page for this ability
25. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

27. windowStage.loadContent('pages/Index', (err) => {
28. if (err.code) {
29. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
30. return;
31. }
32. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
33. });
34. }

36. onWindowStageDestroy(): void {
37. // Main window is destroyed, release UI related resources
38. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
39. }

41. onForeground(): void {
42. // Ability has brought to foreground
43. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
44. }

46. onBackground(): void {
47. // Ability has back to background
48. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
49. }
50. }
```

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. @State embedStatus: string = '';
9. controller: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. // 默认行为：点击按钮跳转页面，关闭index页面，使同层标签销毁。
14. // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮跳转页面，关闭index页面，使同层标签进入BFCache。
15. Button('Destroy')
16. .onClick(() => {
17. try {
18. this.controller.loadUrl("www.example.com");
19. } catch (error) {
20. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
21. }
22. })

24. // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮返回页面，使同层标签离开BFCache。
25. Button('backward')
26. .onClick(() => {
27. try {
28. this.controller.backward();
29. } catch (error) {
30. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
31. }
32. })

34. // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮前进页面，使同层标签进入BFCache。
35. Button('forward')
36. .onClick(() => {
37. try {
38. this.controller.forward();
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })

45. // API12新增同层标签进入离开BFCache状态：非http与https协议加载的网页，Web内核不支持进入BFCache;
46. // 因此如果要测试ENTER_BFCACHE/LEAVE_BFCACHE状态，需要将index.html放到Web服务器上，使用http或者https协议加载，如：
47. // Web({ src: "http://xxxx/index.html", controller: this.controller })
48. Web({ src: $rawfile("index.html"), controller: this.controller })
49. .enableNativeEmbedMode(true)
50. .onNativeEmbedLifecycleChange((event) => {
51. // 当加载页面中有同层标签会触发Create。
52. if (event.status == NativeEmbedStatus.CREATE) {
53. this.embedStatus = 'Create';
54. }
55. // 当页面中同层标签移动或者缩放时会触发Update。
56. if (event.status == NativeEmbedStatus.UPDATE) {
57. this.embedStatus = 'Update';
58. }
59. // 退出页面时会触发Destroy。
60. if (event.status == NativeEmbedStatus.DESTROY) {
61. this.embedStatus = 'Destroy';
62. }
63. // 同层标签所在的页面进入BFCache时，会触发Enter BFCache。
64. if (event.status == NativeEmbedStatus.ENTER_BFCACHE) {
65. this.embedStatus = 'Enter BFCache';
66. }
67. // 同层标签所在的页面离开BFCache时，会触发Leave BFCache。
68. if (event.status == NativeEmbedStatus.LEAVE_BFCACHE) {
69. this.embedStatus = 'Leave BFCache';
70. }
71. console.info("status = " + this.embedStatus);
72. console.info("surfaceId = " + event.surfaceId);
73. console.info("embedId = " + event.embedId);
74. if (event.info) {
75. console.info("id = " + event.info.id);
76. console.info("type = " + event.info.type);
77. console.info("src = " + event.info.src);
78. console.info("width = " + event.info.width);
79. console.info("height = " + event.info.height);
80. console.info("url = " + event.info.url);
81. }
82. })
83. }
84. }
85. }
```

加载的html文件

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>同层渲染测试html</title>
6. <meta name="viewport">
7. </head>
8. <body>
9. <div>
10. <div id="bodyId">
11. <embed id="nativeButton" type = "native/button" width="800" height="800" src="test? params1=1" style = "background-color:red"/>
12. </div>
13. </div>
14. </body>
15. </html>
```

## onNativeEmbedGestureEvent11+

PhonePC/2in1TabletTVWearable

onNativeEmbedGestureEvent(callback: (event: NativeEmbedTouchInfo) => void)

当手指触摸到同层标签时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event: [NativeEmbedTouchInfo](arkts-basic-components-web-i.md#nativeembedtouchinfo11)) => void | 是 | 手指触摸到同层标签时触发该回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

5. declare class Params {
6. text: string;
7. width: number;
8. height: number;
9. }

11. declare class NodeControllerParams {
12. surfaceId: string;
13. renderType: NodeRenderType;
14. width: number;
15. height: number;
16. }

18. class MyNodeController extends NodeController {
19. private rootNode: BuilderNode<[Params]> | undefined | null;
20. private surfaceId_: string = "";
21. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
22. private width_: number = 0;
23. private height_: number = 0;

25. setRenderOption(params: NodeControllerParams) {
26. this.surfaceId_ = params.surfaceId;
27. this.renderType_ = params.renderType;
28. this.width_ = params.width;
29. this.height_ = params.height;
30. }

32. makeNode(uiContext: UIContext): FrameNode | null {
33. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
34. this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
35. return this.rootNode.getFrameNode();
36. }

38. postEvent(event: TouchEvent | undefined): boolean {
39. return this.rootNode?.postTouchEvent(event) as boolean;
40. }
41. }

43. @Component
44. struct ButtonComponent {
45. @Prop params: Params;
46. @State bkColor: Color = Color.Red;

48. build() {
49. Column() {
50. Button(this.params.text)
51. .height(50)
52. .width(200)
53. .border({ width: 2, color: Color.Red })
54. .backgroundColor(this.bkColor)

56. }
57. .width(this.params.width)
58. .height(this.params.height)
59. }
60. }

62. @Builder
63. function ButtonBuilder(params: Params) {
64. ButtonComponent({ params: params })
65. .backgroundColor(Color.Green)
66. }

68. @Entry
69. @Component
70. struct WebComponent {
71. @State eventType: string = '';
72. controller: webview.WebviewController = new webview.WebviewController();
73. private nodeController: MyNodeController = new MyNodeController();
74. uiContext: UIContext = this.getUIContext();

76. build() {
77. Column() {
78. Stack() {
79. NodeContainer(this.nodeController)
80. Web({ src: $rawfile("index.html"), controller: this.controller })
81. .enableNativeEmbedMode(true)
82. .onNativeEmbedLifecycleChange((embed) => {
83. if (embed.status == NativeEmbedStatus.CREATE) {
84. this.nodeController.setRenderOption({
85. surfaceId: embed.surfaceId as string,
86. renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
87. width: this.uiContext!.px2vp(embed.info?.width),
88. height: this.uiContext!.px2vp(embed.info?.height)
89. });
90. this.nodeController.rebuild();
91. }
92. })
93. .onNativeEmbedGestureEvent((event) => {
94. if (event && event.touchEvent) {
95. if (event.touchEvent.type == TouchType.Down) {
96. this.eventType = 'Down'
97. }
98. if (event.touchEvent.type == TouchType.Up) {
99. this.eventType = 'Up'
100. }
101. if (event.touchEvent.type == TouchType.Move) {
102. this.eventType = 'Move'
103. }
104. if (event.touchEvent.type == TouchType.Cancel) {
105. this.eventType = 'Cancel'
106. }
107. let ret = this.nodeController.postEvent(event.touchEvent)
108. if (event.result) {
109. event.result.setGestureEventResult(ret, true);
110. }
111. console.info("embedId = " + event.embedId);
112. console.info("touchType = " + this.eventType);
113. console.info("x = " + event.touchEvent.touches[0].x);
114. console.info("y = " + event.touchEvent.touches[0].y);
115. console.info("Component globalPos:(" + event.touchEvent.target.area.globalPosition.x + "," + event.touchEvent.target.area.globalPosition.y + ")");
116. console.info("width = " + event.touchEvent.target.area.width);
117. console.info("height = " + event.touchEvent.target.area.height);
118. }
119. })
120. }
121. }
122. }
123. }
```

加载的html文件

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>同层渲染测试html</title>
6. <meta name="viewport">
7. </head>
8. <body>
9. <div>
10. <div id="bodyId">
11. <embed id="nativeButton" type = "native/button" width="800" height="800" src="test?params1=1" style = "background-color:red"/>
12. </div>
13. </div>
14. </body>
15. </html>
```

## onIntelligentTrackingPreventionResult12+

PhonePC/2in1TabletTVWearable

onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback)

智能防跟踪功能使能时，当追踪者cookie被拦截时触发该回调。

说明

* 需要使用release包，debug包不生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnIntelligentTrackingPreventionCallback](arkts-basic-components-web-t.md#onintelligenttrackingpreventioncallback12) | 是 | 智能防跟踪功能使能时，当追踪者cookie被拦截时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. // 需要打开智能防跟踪功能，才会触发onIntelligentTrackingPreventionResult回调
13. Button('enableIntelligentTrackingPrevention')
14. .onClick(() => {
15. try {
16. this.controller.enableIntelligentTrackingPrevention(true);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. .onIntelligentTrackingPreventionResult((details) => {
23. console.info("onIntelligentTrackingPreventionResult: [websiteHost]= " + details.host +
24. ", [trackerHost]=" + details.trackerHost);
25. })
26. }
27. }
28. }
```

## onOverrideUrlLoading12+

PhonePC/2in1TabletTVWearable

onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback)

当URL将要加载到当前Web中时触发该回调，让宿主应用程序有机会获得控制权，判断是否阻止Web加载URL。

说明

* POST请求不会触发该回调。
* iframe加载HTTP(s)协议或about:blank时不会触发该回调，而加载非HTTP(s)协议的跳转会触发；调用loadUrl(url: string)主动触发的跳转不会触发该回调。
* 不要在回调中使用相同的URL调用loadUrl(url: string)方法，然后返回true。 这样会不必要地中止当前加载，并用相同的URL发起一次新的加载。 要继续加载当前请求URL的正确做法是直接返回false，而不是调用loadUrl(url: string)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnOverrideUrlLoadingCallback](arkts-basic-components-web-t.md#onoverrideurlloadingcallback12) | 是 | onOverrideUrlLoading的回调。  返回值boolean。返回true表示中止加载URL，返回false表示继续在Web中加载URL。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
13. if (webResourceRequest && webResourceRequest.getRequestUrl() == "about:blank") {
14. return true;
15. }
16. return false;
17. })
18. }
19. }
20. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>onOverrideUrlLoading Demo</h1>
9. <a href="about:blank">Click here</a>// 访问about:blank。
10. </body>
11. </html>
```

## onViewportFitChanged12+

PhonePC/2in1TabletTVWearable

onViewportFitChanged(callback: OnViewportFitChangedCallback)

网页meta中viewport-fit配置项更改时触发该回调，应用可在此回调中自适应布局视口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnViewportFitChangedCallback](arkts-basic-components-web-t.md#onviewportfitchangedcallback12) | 是 | 网页meta中viewport-fit配置项更改时触发的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile('index.html'), controller: this.controller })
12. .onViewportFitChanged((data) => {
13. let jsonData = JSON.stringify(data);
14. let viewportFit: ViewportFit = JSON.parse(jsonData).viewportFit;
15. if (viewportFit === ViewportFit.COVER) {
16. // index.html网页支持沉浸式布局，可调用expandSafeArea调整web控件布局视口覆盖避让区域(状态栏或导航条)。
17. } else if (viewportFit === ViewportFit.CONTAINS) {
18. // index.html网页不支持沉浸式布局，可调用expandSafeArea调整web控件布局视口为安全区域。
19. } else {
20. // 默认值，可不作处理。
21. }
22. })
23. }
24. }
25. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width,viewport-fit=cover">
6. </head>
7. <body>
8. <div style="position: absolute; bottom: 0; margin-bottom: env(safe-area-inset-bottom)"></div>
9. </body>
10. </html>
```

## onInterceptKeyboardAttach12+

PhonePC/2in1TabletTVWearable

onInterceptKeyboardAttach(callback: WebKeyboardCallback)

网页中可编辑元素（如input标签）拉起软键盘之前会回调该接口，应用可以使用该接口拦截系统软键盘的弹出，配置应用定制的软键盘（应用根据该接口可以决定使用系统默认软键盘/定制enter键的系统软键盘/全部由应用自定义的软键盘）。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [WebKeyboardCallback](arkts-basic-components-web-t.md#webkeyboardcallback12) | 是 | 拦截网页拉起软键盘回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { inputMethodEngine } from '@kit.IMEKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. webKeyboardController: WebKeyboardController = new WebKeyboardController()
10. inputAttributeMap: Map<string, number> = new Map([
11. ['UNSPECIFIED', inputMethodEngine.ENTER_KEY_TYPE_UNSPECIFIED],
12. ['GO', inputMethodEngine.ENTER_KEY_TYPE_GO],
13. ['SEARCH', inputMethodEngine.ENTER_KEY_TYPE_SEARCH],
14. ['SEND', inputMethodEngine.ENTER_KEY_TYPE_SEND],
15. ['NEXT', inputMethodEngine.ENTER_KEY_TYPE_NEXT],
16. ['DONE', inputMethodEngine.ENTER_KEY_TYPE_DONE],
17. ['PREVIOUS', inputMethodEngine.ENTER_KEY_TYPE_PREVIOUS]
18. ])

20. /**
21. * 自定义键盘组件Builder
22. */
23. @Builder
24. customKeyboardBuilder() {
25. // 这里实现自定义键盘组件，对接WebKeyboardController实现输入、删除、关闭等操作。
26. Row() {
27. Text("完成")
28. .fontSize(20)
29. .fontColor(Color.Blue)
30. .onClick(() => {
31. this.webKeyboardController.close();
32. })
33. // 插入字符。
34. Button("insertText").onClick(() => {
35. this.webKeyboardController.insertText('insert ');
36. }).margin({
37. bottom: 200,
38. })
39. // 从后往前删除length参数指定长度的字符。
40. Button("deleteForward").onClick(() => {
41. this.webKeyboardController.deleteForward(1);
42. }).margin({
43. bottom: 200,
44. })
45. // 从前往后删除length参数指定长度的字符。
46. Button("deleteBackward").onClick(() => {
47. this.webKeyboardController.deleteBackward(1);
48. }).margin({
49. left: -220,
50. })
51. // 插入功能按键。
52. Button("sendFunctionKey").onClick(() => {
53. this.webKeyboardController.sendFunctionKey(6);
54. })
55. }
56. }

58. build() {
59. Column() {
60. Web({ src: $rawfile('index.html'), controller: this.controller })
61. .onInterceptKeyboardAttach((KeyboardCallbackInfo) => {
62. // option初始化，默认使用系统默认键盘
63. let option: WebKeyboardOptions = {
64. useSystemKeyboard: true,
65. };
66. if (!KeyboardCallbackInfo) {
67. return option;
68. }

70. // 保存WebKeyboardController，使用自定义键盘时候，需要使用该handler控制输入、删除、软键盘关闭等行为
71. this.webKeyboardController = KeyboardCallbackInfo.controller
72. let attributes: Record<string, string> = KeyboardCallbackInfo.attributes
73. // 遍历attributes
74. let attributeKeys = Object.keys(attributes)
75. for (let i = 0; i < attributeKeys.length; i++) {
76. console.info('WebCustomKeyboard key = ' + attributeKeys[i] + ', value = ' + attributes[attributeKeys[i]])
77. }

79. if (attributes) {
80. if (attributes['data-keyboard'] == 'customKeyboard') {
81. // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有data-keyboard，且值为customKeyboard，则使用自定义键盘
82. console.info('WebCustomKeyboard use custom keyboard')
83. option.useSystemKeyboard = false;
84. // 设置自定义键盘builder
85. option.customKeyboard = () => {
86. this.customKeyboardBuilder()
87. }
88. return option;
89. }

91. if (attributes['keyboard-return'] != undefined) {
92. // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有keyboard-return，使用系统键盘，并且指定系统软键盘enterKey类型
93. option.useSystemKeyboard = true;
94. let enterKeyType: number | undefined = this.inputAttributeMap.get(attributes['keyboard-return'])
95. if (enterKeyType != undefined) {
96. option.enterKeyType = enterKeyType
97. }
98. return option;
99. }
100. }

102. return option;
103. })
104. }
105. }
106. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>

5. <head>
6. <meta charset="utf-8">
7. <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0">
8. </head>

10. <body>

12. <p style="font-size:12px">input标签，原有默认行为：</p>
13. <input type="text" style="width: 300px; height: 20px"><br>
14. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

16. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key UNSPECIFIED：</p>
17. <input type="text" keyboard-return="UNSPECIFIED" style="width: 300px; height: 20px"><br>
18. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

20. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key GO：</p>
21. <input type="text" keyboard-return="GO" style="width: 300px; height: 20px"><br>
22. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

24. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key SEARCH：</p>
25. <input type="text" keyboard-return="SEARCH" style="width: 300px; height: 20px"><br>
26. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

28. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key SEND：</p>
29. <input type="text" keyboard-return="SEND" style="width: 300px; height: 20px"><br>
30. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

32. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key NEXT：</p>
33. <input type="text" keyboard-return="NEXT" style="width: 300px; height: 20px"><br>
34. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

36. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key DONE：</p>
37. <input type="text" keyboard-return="DONE" style="width: 300px; height: 20px"><br>
38. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

40. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key PREVIOUS：</p>
41. <input type="text" keyboard-return="PREVIOUS" style="width: 300px; height: 20px"><br>
42. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

44. <p style="font-size:12px">input标签，应用自定义键盘：</p>
45. <input type="text" data-keyboard="customKeyboard" style="width: 300px; height: 20px"><br>

47. </body>

49. </html>
```

## onNativeEmbedVisibilityChange12+

PhonePC/2in1TabletTVWearable

onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback)

当网页中同层标签（例如<embed>标签或<object>标签）在视口内的可见性发生变化时，将触发该回调。同层标签默认不可见，若在页面首次加载时已可见，则会上报；若不可见，则不会上报。同层标签全部不可见才视为不可见，部分可见或全部可见则视为可见。若要获取因同层标签CSS属性（包括visibility、display以及尺寸变化）导致的可见状态变化，需配置[nativeEmbedOptions](arkts-basic-components-web-attributes.md#nativeembedoptions16)，并将[EmbedOptions](arkts-basic-components-web-i.md#embedoptions16)中的supportCssDisplayChange参数设为true。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedVisibilityChangeCallback](arkts-basic-components-web-t.md#onnativeembedvisibilitychangecallback12) | 是 | 同层标签可见性变化时触发该回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

5. declare class Params {
6. text: string;
7. width: number;
8. height: number;
9. }

11. declare class NodeControllerParams {
12. surfaceId: string;
13. renderType: NodeRenderType;
14. width: number;
15. height: number;
16. }

18. class MyNodeController extends NodeController {
19. private rootNode: BuilderNode<[Params]> | undefined | null;
20. private surfaceId_: string = "";
21. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
22. private width_: number = 0;
23. private height_: number = 0;

25. setRenderOption(params: NodeControllerParams) {
26. this.surfaceId_ = params.surfaceId;
27. this.renderType_ = params.renderType;
28. this.width_ = params.width;
29. this.height_ = params.height;
30. }

32. makeNode(uiContext: UIContext): FrameNode | null {
33. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
34. this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
35. return this.rootNode.getFrameNode();
36. }

38. postEvent(event: TouchEvent | undefined): boolean {
39. return this.rootNode?.postTouchEvent(event) as boolean;
40. }
41. }

43. @Component
44. struct ButtonComponent {
45. @Prop params: Params;
46. @State bkColor: Color = Color.Red;

48. build() {
49. Column() {
50. Button(this.params.text)
51. .height(50)
52. .width(200)
53. .border({ width: 2, color: Color.Red })
54. .backgroundColor(this.bkColor)

56. }
57. .width(this.params.width)
58. .height(this.params.height)
59. }
60. }

62. @Builder
63. function ButtonBuilder(params: Params) {
64. ButtonComponent({ params: params })
65. .backgroundColor(Color.Green)
66. }

68. @Entry
69. @Component
70. struct WebComponent {
71. @State embedVisibility: string = '';
72. controller: webview.WebviewController = new webview.WebviewController();
73. private nodeController: MyNodeController = new MyNodeController();
74. uiContext: UIContext = this.getUIContext();

76. build() {
77. Column() {
78. Stack() {
79. NodeContainer(this.nodeController)
80. Web({ src: $rawfile("index.html"), controller: this.controller })
81. .enableNativeEmbedMode(true)
82. .onNativeEmbedLifecycleChange((embed) => {
83. if (embed.status == NativeEmbedStatus.CREATE) {
84. this.nodeController.setRenderOption({
85. surfaceId: embed.surfaceId as string,
86. renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
87. width: this.uiContext!.px2vp(embed.info?.width),
88. height: this.uiContext!.px2vp(embed.info?.height)
89. });
90. this.nodeController.rebuild();
91. }
92. })
93. .onNativeEmbedVisibilityChange((embed) => {
94. if (embed.visibility) {
95. this.embedVisibility = 'Visible';
96. } else {
97. this.embedVisibility = 'Hidden';
98. }
99. console.info("embedId = " + embed.embedId);
100. console.info("visibility = " + embed.visibility);
101. })
102. }
103. }
104. }
105. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>同层渲染测试html</title>
6. <meta name="viewport">
7. </head>
8. <body>
9. <div>
10. <div id="bodyId">
11. <embed id="nativeButton" type = "native/button" width="800" height="800" src="test?params1=1" style = "background-color:red"/>
12. </div>
13. </div>
14. </body>
15. </html>
```

## onNativeEmbedMouseEvent20+

PhonePC/2in1TabletTVWearable

onNativeEmbedMouseEvent(callback: MouseInfoCallback)

在同层标签上执行以下行为时触发该回调：

* 使用鼠标左键、中键、右键进行点击或长按。
* 使用触摸板进行对应鼠标左键、中键、右键点击长按的操作。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MouseInfoCallback](arkts-basic-components-web-t.md#mouseinfocallback20) | 是 | 当鼠标/触摸板点击到同层标签时触发该回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

5. declare class Params {
6. text: string;
7. width: number;
8. height: number;
9. }

11. declare class NodeControllerParams {
12. surfaceId: string;
13. renderType: NodeRenderType;
14. width: number;
15. height: number;
16. }

18. class MyNodeController extends NodeController {
19. private rootNode: BuilderNode<[Params]> | undefined | null;
20. private surfaceId_: string = "";
21. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
22. private width_: number = 0;
23. private height_: number = 0;

25. setRenderOption(params: NodeControllerParams) {
26. this.surfaceId_ = params.surfaceId;
27. this.renderType_ = params.renderType;
28. this.width_ = params.width;
29. this.height_ = params.height;
30. }

32. makeNode(uiContext: UIContext): FrameNode | null {
33. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
34. this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
35. return this.rootNode.getFrameNode();
36. }

38. postInputEvent(event: TouchEvent | MouseEvent | undefined): boolean {
39. return this.rootNode?.postInputEvent(event) as boolean;
40. }
41. }

43. @Component
44. struct ButtonComponent {
45. @Prop params: Params;
46. @State bkColor: Color = Color.Red;

48. build() {
49. Column() {
50. Button(this.params.text)
51. .height(50)
52. .width(200)
53. .border({ width: 2, color: Color.Red })
54. .backgroundColor(this.bkColor)

56. }
57. .width(this.params.width)
58. .height(this.params.height)
59. }
60. }

62. @Builder
63. function ButtonBuilder(params: Params) {
64. ButtonComponent({ params: params })
65. .backgroundColor(Color.Green)
66. }

68. @Entry
69. @Component
70. struct WebComponent {
71. @State mouseAction: string = '';
72. @State mouseButton: string = '';
73. controller: webview.WebviewController = new webview.WebviewController();
74. private nodeController: MyNodeController = new MyNodeController();
75. uiContext: UIContext = this.getUIContext();

77. build() {
78. Column() {
79. Stack() {
80. NodeContainer(this.nodeController)
81. Web({ src: $rawfile("index.html"), controller: this.controller })
82. .enableNativeEmbedMode(true)
83. .onNativeEmbedLifecycleChange((embed) => {
84. if (embed.status == NativeEmbedStatus.CREATE) {
85. this.nodeController.setRenderOption({
86. surfaceId: embed.surfaceId as string,
87. renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
88. width: this.uiContext!.px2vp(embed.info?.width),
89. height: this.uiContext!.px2vp(embed.info?.height)
90. });
91. this.nodeController.rebuild();
92. }
93. })
94. .onNativeEmbedMouseEvent((event) => {
95. if (event && event.mouseEvent) {
96. let ret = this.nodeController.postInputEvent(event.mouseEvent)
97. if (event.result) {
98. event.result.setMouseEventResult(ret, true);
99. }
100. }
101. })
102. }
103. }
104. }
105. }
```

加载的html文件

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>同层渲染测试</title>
6. <meta name="viewport">
7. </head>
8. <body>
9. <div>
10. <div id="bodyId">
11. <embed id="nativeButton" type ="native/button" width="800" height="800" style="background-color:red"/>
12. </div>
13. </div>
14. </body>
15. </html>
```

## onNativeEmbedObjectParamChange21+

PhonePC/2in1TabletTVWearable

onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback)

当同层渲染object标签内嵌param元素变化时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedObjectParamChangeCallback](arkts-basic-components-web-t.md#onnativeembedobjectparamchangecallback21) | 是 | 增加、修改或删除同层渲染object标签内嵌param元素时触发此回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from '@kit.ArkUI';

5. declare class Params {
6. text: string;
7. width: number;
8. height: number;
9. }

11. declare class NodeControllerParams {
12. surfaceId: string;
13. renderType: NodeRenderType;
14. width: number;
15. height: number;
16. }

18. class MyNodeController extends NodeController {
19. private rootNode: BuilderNode<[Params]> | undefined | null;
20. private surfaceId_: string = "";
21. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
22. private width_: number = 0;
23. private height_: number = 0;

25. setRenderOption(params: NodeControllerParams) {
26. this.surfaceId_ = params.surfaceId;
27. this.renderType_ = params.renderType;
28. this.width_ = params.width;
29. this.height_ = params.height;
30. }

32. makeNode(uiContext: UIContext): FrameNode | null {
33. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
34. this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
35. return this.rootNode.getFrameNode();
36. }

38. postInputEvent(event: TouchEvent | MouseEvent | undefined): boolean {
39. return this.rootNode?.postInputEvent(event) as boolean;
40. }
41. }

43. @Component
44. struct ButtonComponent {
45. @Prop params: Params;
46. @State bkColor: Color = Color.Red;

48. build() {
49. Column() {
50. Button(this.params.text)
51. .height(50)
52. .width(200)
53. .border({ width: 2, color: Color.Red })
54. .backgroundColor(this.bkColor)

56. }
57. .width(this.params.width)
58. .height(this.params.height)
59. }
60. }

62. @Builder
63. function ButtonBuilder(params: Params) {
64. ButtonComponent({ params: params })
65. .backgroundColor(Color.Green)
66. }

68. @Entry
69. @Component
70. struct WebComponent {
71. controller: webview.WebviewController = new webview.WebviewController();
72. private nodeController: MyNodeController = new MyNodeController();
73. uiContext: UIContext = this.getUIContext();

75. build() {
76. Column() {
77. Stack() {
78. NodeContainer(this.nodeController)
79. Web({ src: $rawfile('index.html'), controller: this.controller })
80. .enableNativeEmbedMode(true)
81. .registerNativeEmbedRule("object", "native")
82. .onNativeEmbedLifecycleChange((embed) => {
83. if (embed.status == NativeEmbedStatus.CREATE) {
84. this.nodeController.setRenderOption({
85. surfaceId: embed.surfaceId as string,
86. renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
87. width: this.uiContext!.px2vp(embed.info?.width),
88. height: this.uiContext!.px2vp(embed.info?.height)
89. });
90. this.nodeController.rebuild();
91. }
92. })
93. .onNativeEmbedObjectParamChange((event) => {
94. console.info("embed id: " + event.embedId);
95. let paramItems = event.paramItems;
96. if (paramItems) {
97. for (let i = 0; i < paramItems.length; ++i) {
98. console.info("param info: " + JSON.stringify(paramItems[i]));
99. }
100. }
101. })
102. }
103. }
104. }
105. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>同层渲染测试</title>
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. </head>
8. <body>
9. <div>
10. <div id="bodyId">
11. <object id="nativeButton" type ="native/button" width="300" height="300" style="background-color:red">
12. <param id="param-1" name="name-1" value="value1"/>
13. </object>
14. </div>
15. </div>
16. </body>
17. </html>
```

## onOverrideErrorPage20+

PhonePC/2in1TabletTVWearable

onOverrideErrorPage(callback: OnOverrideErrorPageCallback)

网页加载遇到错误时触发，只有主资源出错才会回调该接口，可以使用该接口自定义错误展示页。

说明

该功能需通过调用[setErrorPageEnabled](arkts-apis-webview-webviewcontroller.md#seterrorpageenabled20)接口启用默认错误页后，才会生效。

通过[errorPageEvent.error.getErrorCode()](arkts-basic-components-web-webresourceerror.md#geterrorcode)获取的错误码大于0代表http协议错误，小于0代表网络错误。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnOverrideErrorPageCallback](arkts-basic-components-web-t.md#onoverrideerrorpagecallback20) | 是 | 网页加载遇到错误时触发。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();
7. build() {
8. Column() {
9. Web({ src: "www.error-test.com", controller: this.controller })
10. .onControllerAttached(() => {
11. this.controller.setErrorPageEnabled(true);
12. if (!this.controller.getErrorPageEnabled()) {
13. this.controller.setErrorPageEnabled(true);
14. }
15. })
16. .onOverrideErrorPage(event => {
17. let htmlStr = "<html><h1>error occur : ";
18. htmlStr += event.error.getErrorCode();
19. htmlStr += "</h1></html>";
20. return htmlStr;
21. })
22. }
23. }
24. }
```

## onSslErrorReceive(deprecated)

PhonePC/2in1TabletTVWearable

onSslErrorReceive(callback: (event?: { handler: Function, error: object }) => void)

通知用户加载资源时发生SSL错误。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[onSslErrorEventReceive9+](arkts-basic-components-web-events.md#onsslerroreventreceive9)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event?: { handler: Function, error: object }) => void | 是 | 当网页检测到SSL错误时触发的回调。 |

## onFileSelectorShow(deprecated)

PhonePC/2in1TabletTVWearable

onFileSelectorShow(callback: (event?: { callback: Function, fileSelector: object }) => void)

调用此函数以处理具有“文件”输入类型的HTML表单，以响应用户按下的“选择文件”按钮。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[onShowFileSelector9+](arkts-basic-components-web-events.md#onshowfileselector9)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event?: { callback: Function, fileSelector: object }) => void | 是 | 当触发文件选择器时需要执行的回调。 |

## onUrlLoadIntercept(deprecated)

PhonePC/2in1TabletTVWearable

onUrlLoadIntercept(callback: (event?: { data:string | WebResourceRequest }) => boolean)

当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。

说明

API version 8开始支持，从API version 10开始废弃，建议使用[onLoadIntercept10+](arkts-basic-components-web-events.md#onloadintercept10)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event?: { data:string | [WebResourceRequest](arkts-basic-components-web-webresourcerequest.md) }) => boolean | 是 | url的相关信息。  返回值：boolean，true表示阻止此次加载，false表示允许此次加载。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onUrlLoadIntercept((event) => {
13. if (event) {
14. console.info('onUrlLoadIntercept ' + event.data.toString());
15. }
16. return true
17. })
18. }
19. }
20. }
```

## onPdfLoadEvent20+

PhonePC/2in1TabletTVWearable

onPdfLoadEvent(callback: Callback<OnPdfLoadEvent>)

通知用户PDF页面加载状态，包括成功或失败。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnPdfLoadEvent](arkts-basic-components-web-i.md#onpdfloadevent20)> | 是 | 当PDF加载成功或失败时，会触发回调，通知用户PDF页面加载状态。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. // 使用时需将'https://www.example.com/xxx.pdf'替换为真实可访问的地址
12. Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
13. .onPdfLoadEvent((eventInfo: OnPdfLoadEvent) => {
14. console.info(`Load event callback called. url: ${eventInfo.url}, result: ${eventInfo.result}.`)
15. })
16. }
17. }
18. }
```

## onPdfScrollAtBottom20+

PhonePC/2in1TabletTVWearable

onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent>)

通知用户PDF页面已滚动到底。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[OnPdfScrollEvent](arkts-basic-components-web-i.md#onpdfscrollevent20)> | 是 | 当PDF滚动到垂直方向底部时，会触发回调，通知用户PDF页面已滚动到底。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. // 使用时需将'https://www.example.com/xxx.pdf'替换为真实可访问的地址
12. Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
13. .onPdfScrollAtBottom((eventInfo: OnPdfScrollEvent) => {
14. console.info(`Scroll at bottom callback called. url: ${eventInfo.url}.`)
15. })
16. }
17. }
18. }
```

## onDetectedBlankScreen22+

PhonePC/2in1TabletTVWearable

onDetectedBlankScreen(callback: OnDetectBlankScreenCallback)

Web组件检测到白屏时触发此回调。

说明

* 需配合[blankScreenDetectionConfig](arkts-basic-components-web-attributes.md#blankscreendetectionconfig22)使用。否则，默认关闭白屏检测功能，不会返回检测到白屏时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnDetectBlankScreenCallback](arkts-basic-components-web-t.md#ondetectblankscreencallback22) | 是 | Web组件检测到白屏时的回调函数。 |

**示例：**

```
1. // onDetectedBlankScreen.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .blankScreenDetectionConfig({
13. enable: true,
14. detectionTiming: [2, 4, 6, 8],
15. contentfulNodesCountThreshold: 4,
16. detectionMethods:[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN]
17. })
18. .onDetectedBlankScreen((event: BlankScreenDetectionEventInfo)=>{
19. console.info(`Found blank screen on ${event.url}.`);
20. console.info(`The blank screen reason is ${event.blankScreenReason}.`);
21. console.info(`The blank screen detail is ${event.blankScreenDetails?.detectedContentfulNodesCount}.`);
22. })
23. }
24. }
25. }
```

## onRenderExited(deprecated)

PhonePC/2in1TabletTVWearable

onRenderExited(callback: (event?: { detail: object }) => boolean)

应用渲染进程因错误或崩溃退出时触发回调。

多个Web组件可能共享单个渲染进程，每个受影响的Web组件都会触发该回调。

应用处理该回调时，可以调用绑定的WebViewController接口来恢复页面。例如[refresh](arkts-apis-webview-webviewcontroller.md#refresh)、[loadUrl](arkts-apis-webview-webviewcontroller.md#loadurl)等。

详情可参考[Web组件的生命周期](../harmonyos-guides/web-event-sequence.md)。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[onRenderExited9+](arkts-basic-components-web-events.md#onrenderexited9)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event?: { detail: object }) => boolean | 是 | 渲染过程退出时触发。 |

## onCameraCaptureStateChange23+

PhonePC/2in1TabletTVWearable

onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback)

通知用户当前网页的摄像头状态，摄像头有三个状态，无状态（None），捕获中（Active），暂停中（Paused）。使用callback异步回调。

可以通过startCamera，stopCamera，closeCamera这三个接口来切换摄像头的状态。这三个接口分别对应开启，暂停，停止摄像头功能。示例使用场景详见[startCamera](arkts-apis-webview-webviewcontroller.md#startcamera12)。

说明

当前网页正在使用摄像头时，返回在捕获中状态。

当前网页暂停使用摄像头时，返回暂停中状态。

当前网页完全没有使用摄像头时，返回无状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnCameraCaptureStateChangeCallback](arkts-basic-components-web-t.md#oncameracapturestatechangecallback23) | 是 | 回调函数。当摄像头捕获状态改变时触发该回调，返回原来的状态和改变后的状态。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

6. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

8. @Entry
9. @Component
10. struct WebComponent {
11. controller: webview.WebviewController = new webview.WebviewController();
12. uiContext: UIContext = this.getUIContext();

14. aboutToAppear(): void {
15. let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
16. atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err: BusinessError, data: PermissionRequestResult) => {
17. console.info('data:' + JSON.stringify(data));
18. console.info('data permissions:' + data.permissions);
19. console.info('data authResults:' + data.authResults);
20. })
21. }

23. build() {
24. Column() {
25. Button("startCamera").onClick(() => {
26. try {
27. this.controller.startCamera();
28. } catch (error) {
29. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
30. }
31. })
32. Button("stopCamera").onClick(() => {
33. try {
34. this.controller.stopCamera();
35. } catch (error) {
36. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
37. }
38. })
39. Button("closeCamera").onClick(() => {
40. try {
41. this.controller.closeCamera();
42. } catch (error) {
43. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
44. }
45. })
46. Web({ src: $rawfile('index.html'), controller: this.controller })
47. .onPermissionRequest((event) => {
48. if (event) {
49. this.uiContext.showAlertDialog({
50. title: 'title',
51. message: 'text',
52. primaryButton: {
53. value: 'deny',
54. action: () => {
55. event.request.deny();
56. }
57. },
58. secondaryButton: {
59. value: 'onConfirm',
60. action: () => {
61. event.request.grant(event.request.getAccessibleResource());
62. }
63. },
64. cancel: () => {
65. event.request.deny();
66. }
67. })
68. }
69. })
70. .onCameraCaptureStateChange((event: CameraCaptureStateChangeInfo) => {
71. console.info("CameraCapture from ", event.originalState, " to ", event.newState);
72. })
73. }
74. }
75. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. </head>
7. <body>
8. <video id="video" width="400px" height="400px" autoplay="autoplay">
9. </video>
10. <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()" />
11. <script>
12. function getMedia() {
13. let constraints = {
14. video: {
15. width: 500,
16. height: 500
17. },
18. audio: true
19. }
20. let video = document.getElementById("video");
21. let promise = navigator.mediaDevices.getUserMedia(constraints);
22. promise.then(function(MediaStream) {
23. video.srcObject = MediaStream;
24. video.play();
25. })
26. }
27. </script>
28. </body>
29. </html>
```

## onMicrophoneCaptureStateChange23+

PhonePC/2in1TabletTVWearable

onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback)

通知用户当前网页中麦克风状态，麦克风有三个状态，未工作（None），捕获中（Active），暂停中（Paused）。使用callback异步回调。

可以通过resumeMicrophone，pauseMicrophone，stopMicrophone这三个接口来切换麦克风的状态。这三个接口功能分别对应解除暂停，暂停，停止麦克风。示例使用场景详见[网页中麦克风的使用](arkts-apis-webview-webviewcontroller.md#resumemicrophone23)。

说明

当前网页正在使用麦克风时，返回捕获中状态；当前网页暂停使用麦克风时，返回暂停中状态；当前网页完全没有使用麦克风时，返回未工作状态。

当前麦克风处于捕获中状态时，设置暂停使用，当前麦克风变为暂停中状态。可通过ArkWeb设置麦克风开始使用状态进行恢复捕捉。

当前麦克风处于捕获中状态时，设置停止使用，当前麦克风停止捕捉，麦克风变为未工作状态。除非重新前端开始捕捉，否则无法恢复。

当前麦克风处于暂停中状态时，设置开始使用，当前麦克风继续捕捉，变为捕获中状态。

当前麦克风处于暂停中状态时，设置停止使用，当前麦克风停止捕捉，变为未工作状态。除非重新前端开始捕捉，否则无法恢复。

当前麦克风处于未工作状态时，设置开始使用以及暂停使用，麦克风状态均不发生变化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnMicrophoneCaptureStateChangeCallback](arkts-basic-components-web-t.md#onmicrophonecapturestatechangecallback23) | 是 | 回调函数。当麦克风捕获状态改变时触发该回调，返回原来的状态和改变后的状态。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

6. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

8. @Entry
9. @Component
10. struct WebComponent {
11. controller: webview.WebviewController = new webview.WebviewController();
12. uiContext: UIContext = this.getUIContext();

14. aboutToAppear(): void {
15. let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
16. atManager.requestPermissionsFromUser(context, ['ohos.permission.MICROPHONE'], (err: BusinessError, data: PermissionRequestResult) => {
17. console.info('data:' + JSON.stringify(data));
18. console.info('data permissions:' + data.permissions);
19. console.info('data authResults:' + data.authResults);
20. })
21. }

23. build() {
24. Column() {
25. Button("resumeMicrophone").onClick(() => {
26. try {
27. this.controller.resumeMicrophone();
28. } catch (error) {
29. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
30. }
31. })
32. Button("pauseMicrophone").onClick(() => {
33. try {
34. this.controller.pauseMicrophone();
35. } catch (error) {
36. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
37. }
38. })
39. Button("stopMicrophone").onClick(() => {
40. try {
41. this.controller.stopMicrophone();
42. } catch (error) {
43. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
44. }
45. })
46. Web({ src: $rawfile('index.html'), controller: this.controller })
47. .onPermissionRequest((event) => {
48. if (event) {
49. this.uiContext.showAlertDialog({
50. title: 'title',
51. message: 'text',
52. primaryButton: {
53. value: 'deny',
54. action: () => {
55. event.request.deny();
56. }
57. },
58. secondaryButton: {
59. value: 'onConfirm',
60. action: () => {
61. event.request.grant(event.request.getAccessibleResource());
62. }
63. },
64. cancel: () => {
65. event.request.deny();
66. }
67. })
68. }
69. })
70. .onMicrophoneCaptureStateChange((event: MicrophoneCaptureStateChangeInfo) => {
71. console.info("MicrophoneCapture from ", event.originalState, " to ", event.newState);
72. })
73. }
74. }
75. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. </head>
7. <body>
8. <video id="video" width="400px" height="400px" autoplay="autoplay">
9. </video>
10. <input type="button" title="HTML5麦克风" value="开启麦克风" onclick="getMedia()" />
11. <script>
12. function getMedia() {
13. let constraints = {
14. video: {
15. width: 500,
16. height: 500
17. },
18. audio: true
19. }
20. let video = document.getElementById("video");
21. let promise = navigator.mediaDevices.getUserMedia(constraints);
22. promise.then(function(MediaStream) {
23. video.srcObject = MediaStream;
24. video.play();
25. })
26. }
27. </script>
28. </body>
29. </html>
```

## onTextSelectionChange23+

PhonePC/2in1TabletTVWearable

onTextSelectionChange(callback: TextSelectionChangeCallback)

设置Web组件选区文本改变时的回调函数，使用callback异步回调。

说明

* 支持手势选中、鼠标选中以及JS选中选区。
* 使用上述方式选中内容结束后触发回调。
* 使用同样方式选中和上一次相同内容时，不触发回调；使用不同方式选中和上一次相同内容时，依然触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TextSelectionChangeCallback](arkts-basic-components-web-t.md#textselectionchangecallback23) | 是 | 回调函数，所选区域文本内容改变时触发。 |

**示例：**

```
1. // onTextSelectionChange.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile('index.html'), controller: this.controller })
12. .onTextSelectionChange((selectionText: string) => {
13. console.info(`Selected text is ${selectionText}.`);
14. })
15. }
16. }
17. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>示例页面</title>
6. </head>
7. <body>
8. 示例文本
9. </body>
10. </html>
```

## onFirstScreenPaint23+

PhonePC/2in1TabletTVWearable

onFirstScreenPaint(callback: OnFirstScreenPaintCallback)

网页首屏渲染结束时触发此回调，使用callback异步回调。

说明

* 首屏渲染（First Screen Paint，FSP），记录了视口内图片、文本或视频元素完成渲染所需的时间，是衡量页面首次加载到渲染完成的核心性能指标。当一定时间内视口内没有可见元素超出历史绘制区域时，将视口内元素绘制的历史最大的时刻视为首屏渲染完成时刻。
* 接口在首屏绘制完成后，需要等待一定时间没有新的渲染信息需要处理后，才会上报回调。接口回调时刻和首屏渲染完成时刻不同。
* 渲染未完成时，若用户输入或滚动页面，将会立即上报回调函数。
* 该接口适用于在即时加载场景下获取首屏渲染时间，在预加载或预渲染场景下使用无法达到预期。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnFirstScreenPaintCallback](arkts-basic-components-web-t.md#onfirstscreenpaintcallback23) | 是 | 回调函数，设置Web组件的检测到首屏渲染。 |

**示例：**

```
1. // onFirstScreenPaint.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onFirstScreenPaint((event: FirstScreenPaint)=>{
13. console.info(`Found first screen paint on ${event.url}.`);
14. console.info(`The navigation start time is ${event.navigationStartTime}.`);
15. console.info(`The first screen paint time is ${event.firstScreenPaintTime}.`);
16. })
17. }
18. }
19. }
```
