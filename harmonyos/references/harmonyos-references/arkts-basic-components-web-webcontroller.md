---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontroller
title: Class (WebController)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebController)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7a1b04c3f7c10b7dcf61940f89493c4f876c7f26cbfdc2e817aef8cded091d73
---

通过WebController可以控制Web组件各种行为。一个WebController对象只能控制一个Web组件，且必须在Web组件和WebController绑定后，才能调用WebController上的方法。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 该组件从API version 9开始废弃，建议使用[WebviewController9+](arkts-apis-webview-webviewcontroller.md)代替。
* 示例效果请以真机运行为准。

## 创建对象

PhonePC/2in1TabletTVWearable

```
1. let webController: WebController = new WebController()
```

## constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor()

WebController的构造函数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[constructor11+](arkts-apis-webview-webviewcontroller.md#constructor11)代替。

**系统能力：** SystemCapability.Web.Webview.Core

## getCookieManager(deprecated)

PhonePC/2in1TabletTVWearable

getCookieManager(): WebCookie

获取Web组件cookie管理对象。

说明

从API version 9开始支持，从API version 9开始废弃，建议使用[getCookie](arkts-apis-webview-webcookiemanager.md#getcookiedeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WebCookie | Web组件cookie管理对象，参考[WebCookie](arkts-basic-components-web-webcookie.md)定义。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('getCookieManager')
10. .onClick(() => {
11. let cookieManager = this.controller.getCookieManager()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## requestFocus(deprecated)

PhonePC/2in1TabletTVWearable

requestFocus()

使当前Web页面获取焦点。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[requestFocus9+](arkts-apis-webview-webviewcontroller.md#requestfocus)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('requestFocus')
10. .onClick(() => {
11. this.controller.requestFocus()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## accessBackward(deprecated)

PhonePC/2in1TabletTVWearable

accessBackward(): boolean

当前页面是否可后退，即当前页面是否有返回历史记录。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[accessBackward9+](arkts-apis-webview-webviewcontroller.md#accessbackward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可以后退返回true，否则返回false。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('accessBackward')
10. .onClick(() => {
11. let result = this.controller.accessBackward()
12. console.info('result:' + result)
13. })
14. Web({ src: 'www.example.com', controller: this.controller })
15. }
16. }
17. }
```

## accessForward(deprecated)

PhonePC/2in1TabletTVWearable

accessForward(): boolean

当前页面是否可前进，即当前页面是否有前进历史记录。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[accessForward9+](arkts-apis-webview-webviewcontroller.md#accessforward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前页面可以前进，返回false表示当前页面不可以前进。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('accessForward')
10. .onClick(() => {
11. let result = this.controller.accessForward()
12. console.info('result:' + result)
13. })
14. Web({ src: 'www.example.com', controller: this.controller })
15. }
16. }
17. }
```

## accessStep(deprecated)

PhonePC/2in1TabletTVWearable

accessStep(step: number): boolean

当前页面是否可前进或者后退给定的step步。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[accessStep9+](arkts-apis-webview-webviewcontroller.md#accessstep)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | number | 是 | 要跳转的步数，正数代表前进，负数代表后退。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 页面是否前进或后退 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()
6. @State steps: number = 2

8. build() {
9. Column() {
10. Button('accessStep')
11. .onClick(() => {
12. let result = this.controller.accessStep(this.steps)
13. console.info('result:' + result)
14. })
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```

## backward(deprecated)

PhonePC/2in1TabletTVWearable

backward()

按照历史栈，后退一个页面。一般结合accessBackward一起使用。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[backward9+](arkts-apis-webview-webviewcontroller.md#backward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('backward')
10. .onClick(() => {
11. this.controller.backward()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## forward(deprecated)

PhonePC/2in1TabletTVWearable

forward()

按照历史栈，前进一个页面。一般结合accessForward一起使用。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[forward9+](arkts-apis-webview-webviewcontroller.md#forward)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('forward')
10. .onClick(() => {
11. this.controller.forward()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## deleteJavaScriptRegister(deprecated)

PhonePC/2in1TabletTVWearable

deleteJavaScriptRegister(name: string)

删除通过registerJavaScriptProxy注册到window上的指定name的应用侧JavaScript对象。删除后立即生效，无须调用[refresh](arkts-basic-components-web-webcontroller.md#refreshdeprecated)接口。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[deleteJavaScriptRegister9+](arkts-apis-webview-webviewcontroller.md#deletejavascriptregister)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 注册对象的名称，可在网页侧JavaScript中通过此名称调用应用侧JavaScript对象。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()
6. @State name: string = 'Object'

8. build() {
9. Column() {
10. Button('deleteJavaScriptRegister')
11. .onClick(() => {
12. this.controller.deleteJavaScriptRegister(this.name)
13. })
14. Web({ src: 'www.example.com', controller: this.controller })
15. }
16. }
17. }
```

## getHitTest(deprecated)

PhonePC/2in1TabletTVWearable

getHitTest(): HitTestType

获取当前被点击区域的元素类型。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getHitTest9+](arkts-apis-webview-webviewcontroller.md#gethittestdeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HitTestType](arkts-basic-components-web-e.md#hittesttypedeprecated) | 被点击区域的元素类型。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('getHitTest')
10. .onClick(() => {
11. let hitType = this.controller.getHitTest()
12. console.info("hitType: " + hitType)
13. })
14. Web({ src: 'www.example.com', controller: this.controller })
15. }
16. }
17. }
```

## loadData(deprecated)

PhonePC/2in1TabletTVWearable

loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })

baseUrl为空时，通过”data“协议加载指定的一段字符串。

当baseUrl为”data“协议时，编码后的data字符串将被Web组件作为”data"协议加载。

当baseUrl为“http/https"协议时，编码后的data字符串将被Web组件以类似loadUrl的方式以非编码字符串处理。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[loadData9+](arkts-apis-webview-webviewcontroller.md#loaddata)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 按照”Base64“或者”URL"编码后的一段字符串。 |
| mimeType | string | 是 | 媒体类型（MIME）。 |
| encoding | string | 是 | 编码类型，具体为“Base64"或者”URL编码。 |
| baseUrl | string | 否 | 指定的一个URL路径（“http”/“https”/"data"协议），并由Web组件赋值给window.origin。默认值为空字符串。 |
| historyUrl | string | 否 | 历史记录URL。默认值为空字符串。非空时，可被历史记录管理，实现前进后退功能。当baseUrl为空时，此属性无效。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('loadData')
10. .onClick(() => {
11. this.controller.loadData({
12. data: "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
13. mimeType: "text/html",
14. encoding: "UTF-8"
15. })
16. })
17. Web({ src: 'www.example.com', controller: this.controller })
18. }
19. }
20. }
```

## loadUrl(deprecated)

PhonePC/2in1TabletTVWearable

loadUrl(options: { url: string | Resource, headers?: Array<Header> })

使用指定的HTTP头加载指定的URL。

通过loadUrl注入的对象只在当前document有效，即通过loadUrl导航到新的页面会无效。

而通过registerJavaScriptProxy注入的对象，在loadUrl导航到新的页面也会有效。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[loadUrl9+](arkts-apis-webview-webviewcontroller.md#loadurl)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | Resource | 是 | 需要加载的 URL。 |
| headers | Array<[Header](arkts-basic-components-web-i.md#header)> | 否 | URL的附加HTTP请求头。  默认值：[]。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('loadUrl')
10. .onClick(() => {
11. this.controller.loadUrl({ url: 'www.example.com' })
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## onActive(deprecated)

PhonePC/2in1TabletTVWearable

onActive(): void

调用此接口通知Web组件进入前台激活状态。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[onActive9+](arkts-apis-webview-webviewcontroller.md#onactive)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('onActive')
10. .onClick(() => {
11. this.controller.onActive()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## onInactive(deprecated)

PhonePC/2in1TabletTVWearable

onInactive(): void

调用此接口通知Web组件进入未激活状态。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[onInactive9+](arkts-apis-webview-webviewcontroller.md#oninactive)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('onInactive')
10. .onClick(() => {
11. this.controller.onInactive()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## zoom(deprecated)

PhonePC/2in1TabletTVWearable

zoom(factor: number): void

调整当前网页的缩放比例。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[zoom9+](arkts-apis-webview-webviewcontroller.md#zoom)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factor | number | 是 | 基于当前网页所需调整的相对缩放比例，当入参为1时为默认加载网页的缩放比例，小于1为缩小，大于1为放大。取值范围(0, 100]。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()
6. @State factor: number = 1

8. build() {
9. Column() {
10. Button('zoom')
11. .onClick(() => {
12. this.controller.zoom(this.factor)
13. })
14. Web({ src: 'www.example.com', controller: this.controller })
15. }
16. }
17. }
```

## refresh(deprecated)

PhonePC/2in1TabletTVWearable

refresh()

调用此接口通知Web组件刷新网页。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[refresh9+](arkts-apis-webview-webviewcontroller.md#refresh)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('refresh')
10. .onClick(() => {
11. this.controller.refresh()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## registerJavaScriptProxy(deprecated)

PhonePC/2in1TabletTVWearable

registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })

注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。注入的对象在页面下一次（重新）加载前不会出现在JavaScript中。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[registerJavaScriptProxy9+](arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | object | 是 | 参与注册的应用侧JavaScript对象。可以声明方法，也可以声明属性，但是不支持h5直接调用。其中方法的参数和返回类型只能为string，number，boolean |
| name | string | 是 | 注册对象的名称，与window中调用的对象名一致。注册后window对象可以通过此名字访问应用侧JavaScript对象。 |
| methodList | Array<string> | 是 | 参与注册的应用侧JavaScript对象的方法。 |

**示例：**

```
1. // xxx.ets
2. class TestObj {
3. constructor() {
4. }

6. test(): string {
7. return "ArkUI Web Component"
8. }

10. toString(): void {
11. console.info('Web Component toString')
12. }
13. }

15. @Entry
16. @Component
17. struct Index {
18. controller: WebController = new WebController()
19. testObj = new TestObj();
20. build() {
21. Column() {
22. Row() {
23. Button('Register JavaScript To Window').onClick(() => {
24. this.controller.registerJavaScriptProxy({
25. object: this.testObj,
26. name: "objName",
27. methodList: ["test", "toString"],
28. })
29. })
30. }
31. Web({ src: $rawfile('index.html'), controller: this.controller })
32. .javaScriptAccess(true)
33. }
34. }
35. }
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
8. Hello world!
9. <script type="text/javascript">
10. function htmlTest() {
11. str = objName.test("test function")
12. console.info('objName.test result:'+ str)
13. }
14. </script>
15. </body>
16. </html>
```

## runJavaScript(deprecated)

PhonePC/2in1TabletTVWearable

runJavaScript(options: { script: string, callback?: (result: string) => void })

异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScript需要在loadUrl完成后，比如onPageEnd中调用。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[runJavaScript9+](arkts-apis-webview-webviewcontroller.md#runjavascript)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |
| callback | (result: string) => void | 否 | 回调执行JavaScript脚本结果。JavaScript脚本若执行失败或无返回值时，返回null。不传入时不进行回调。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()
6. @State webResult: string = ''
7. build() {
8. Column() {
9. Text(this.webResult).fontSize(20)
10. Web({ src: $rawfile('index.html'), controller: this.controller })
11. .javaScriptAccess(true)
12. .onPageEnd((event) => {
13. this.controller.runJavaScript({
14. script: 'test()',
15. callback: (result: string)=> {
16. this.webResult = result
17. console.info(`The test() return value is: ${result}`)
18. }})
19. if (event) {
20. console.info('url: ', event.url)
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
5. <meta charset="utf-8">
6. </head>
7. <body>
8. Hello world!
9. <script type="text/javascript">
10. function test() {
11. console.info('Ark WebComponent')
12. return "This value is from index.html"
13. }
14. </script>
15. </body>
16. </html>
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop()

停止页面加载。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[stop9+](arkts-apis-webview-webviewcontroller.md#stop)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('stop')
10. .onClick(() => {
11. this.controller.stop()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```

## clearHistory(deprecated)

PhonePC/2in1TabletTVWearable

clearHistory(): void

删除所有前进后退记录。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[clearHistory9+](arkts-apis-webview-webviewcontroller.md#clearhistory)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()

7. build() {
8. Column() {
9. Button('clearHistory')
10. .onClick(() => {
11. this.controller.clearHistory()
12. })
13. Web({ src: 'www.example.com', controller: this.controller })
14. }
15. }
16. }
```
