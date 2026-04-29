---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller
title: Class (WebviewController)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebviewController)
category: harmonyos-references
scraped_at: 2026-04-29T13:55:34+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2e6cd0387c38da00b4b9798409485c8ebe5f594d301732dc3a10d2c0492e96a3
---

通过WebviewController可以控制Web组件各种行为（包括页面导航、生命周期状态、JavaScript交互等行为）。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## constructor11+

PhonePC/2in1TabletTVWearable

constructor(webTag?: string)

用于创建 WebviewController 对象的构造函数。

说明

不传参：new webview.WebviewController()表示构造函数为空，不使用C API时不需要传参。

传参且参数是合法字符串：new webview.WebviewController("xxx")，用于开发者区分多实例，并调用对应实例下的方法。

传入参数为空：new webview.WebviewController("")或new webview.WebviewController(undefined)，该场景下参数无意义，无法区分多个实例，直接返回undefined，需要开发者判断返回值是否正常。

Web组件销毁后会解绑WebViewController，之后调用WebviewController的非静态方法会抛出[17100001](errorcode-webview.md#section17100001-webviewcontroller没有和具体的web组件关联)异常，应注意调用时机和捕获异常，防止进程异常退出。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webTag | string | 否 | 指定了 Web 组件的名称。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class WebObj {
6. constructor() {
7. }

9. webTest(): string {
10. console.info('Web test');
11. return "Web test";
12. }

14. webString(): void {
15. console.info('Web test toString');
16. }
17. }

19. @Entry
20. @Component
21. struct WebComponent {
22. controller: webview.WebviewController = new webview.WebviewController()
23. @State webTestObj: WebObj = new WebObj();

25. build() {
26. Column() {
27. Button('refresh')
28. .onClick(() => {
29. try {
30. this.controller.refresh();
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('deleteJavaScriptRegister')
36. .onClick(() => {
37. try {
38. this.controller.deleteJavaScriptRegister("objTestName");
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: '', controller: this.controller })
44. .javaScriptAccess(true)
45. .onControllerAttached(() => {
46. this.controller.loadUrl($rawfile("index.html"));
47. this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
48. })
49. }
50. }
51. }
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
8. <button type="button" onclick="htmlTest()">Click Me!</button>
9. <p id="demo"></p>
10. <p id="webDemo"></p>
11. <script type="text/javascript">
12. function htmlTest() {
13. // This function call expects to return "Web test"
14. let webStr = objTestName.webTest();
15. document.getElementById("webDemo").innerHTML=webStr;
16. console.info('objTestName.webTest result:'+ webStr)
17. }
18. </script>
19. </body>
20. </html>
```

## initializeWebEngine

PhonePC/2in1TabletTVWearable

static initializeWebEngine(): void

在Web组件初始化之前，通过此接口加载Web引擎的动态库文件，以提高启动性能。自动预连接历史访问过的高频网站。

说明

* initializeWebEngine不支持在异步线程中调用，否则会造成崩溃。
* initializeWebEngine全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

本示例以EntryAbility为例，描述了在Ability创建阶段完成Web组件动态库加载的功能。

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { webview } from '@kit.ArkWeb';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate")
8. webview.WebviewController.initializeWebEngine()
9. console.info("EntryAbility onCreate done")
10. }
11. }
```

## setHttpDns10+

PhonePC/2in1TabletTVWearable

static setHttpDns(secureDnsMode:SecureDnsMode, secureDnsConfig:string): void

设置Web组件是否使用HTTPDNS解析DNS。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| secureDnsMode | [SecureDnsMode](arkts-apis-webview-e.md#securednsmode10) | 是 | 使用HTTPDNS的模式。 |
| secureDnsConfig | string | 是 | HTTPDNS server的配置，必须是https协议并且只允许配置一个server。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { webview } from '@kit.ArkWeb';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. console.info("EntryAbility onCreate")
9. try {
10. webview.WebviewController.setHttpDns(webview.SecureDnsMode.AUTO, "https://example1.test")
11. } catch (error) {
12. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
13. }

15. AppStorage.setOrCreate("abilityWant", want);
16. console.info("EntryAbility onCreate done")
17. }
18. }
```

## setWebDebuggingAccess

PhonePC/2in1TabletTVWearable

static setWebDebuggingAccess(webDebuggingAccess: boolean): void

设置是否启用网页调试功能。详情请参考[DevTools工具](../harmonyos-guides/web-debugging-with-devtools.md)。

安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患，不建议在应用正式发布版本中启用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | 是 | 设置是否启用网页调试功能。  true表示启用网页调试功能。false表示不启用网页调试功能。  默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. aboutToAppear(): void {
11. try {
12. webview.WebviewController.setWebDebuggingAccess(true);
13. } catch (error) {
14. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
15. }
16. }

18. build() {
19. Column() {
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## loadUrl

PhonePC/2in1TabletTVWearable

loadUrl(url: string | Resource, headers?: Array<WebHeader>): void

加载指定的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | Resource | 是 | 需要加载的 URL。 |
| headers | Array<[WebHeader](arkts-apis-webview-i.md#webheader)> | 否 | URL的附加HTTP请求头。  默认值： []。  传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid. |
| 17100003 | Invalid resource path or file type. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

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
12. Button('loadUrl')
13. .onClick(() => {
14. try {
15. // 需要加载的URL是string类型。
16. this.controller.loadUrl('www.example.com');
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

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
12. Button('loadUrl')
13. .onClick(() => {
14. try {
15. // 带参数headers。
16. this.controller.loadUrl('www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }]);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

加载本地网页，加载本地资源文件有三种方式。

1.$rawfile方式。

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
12. Button('loadUrl')
13. .onClick(() => {
14. try {
15. // 通过$rawfile加载本地资源文件。
16. this.controller.loadUrl($rawfile('index.html'));
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

2.resources协议。

使用 resource://rawfile/ 协议前缀可以避免常规 $rawfile 方式在处理带有“#”路由链接时的局限性。当URL中包含“#”号时，“#”后面的内容会被视为锚点（fragment）。

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
12. Button('loadUrl')
13. .onClick(() => {
14. try {
15. // 通过resource协议加载本地资源文件。
16. this.controller.loadUrl("resource://rawfile/index.html#home");
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

在“src\main\resources\rawfile”文件夹下创建index.html：

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <div id="content"></div>

7. <script>
8. function loadContent() {
9. var hash = window.location.hash;
10. var contentDiv = document.getElementById('content');

12. if (hash === '#home') {
13. contentDiv.innerHTML = '<h1>Home Page</h1><p>Welcome to the Home Page!</p>';
14. } else {
15. contentDiv.innerHTML = '<h1>Default Page</h1><p>This is the default content.</p>';
16. }
17. }

19. // 加载界面
20. window.addEventListener('load', loadContent);

22. // 当hash变化时，更新界面
23. window.addEventListener('hashchange', loadContent);
24. </script>
25. </body>
26. </html>
```

3.通过沙箱路径加载本地文件，可以参考[web](../harmonyos-guides/web-page-loading-with-web-components.md#加载本地页面)加载沙箱路径的示例代码。

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

## loadData

PhonePC/2in1TabletTVWearable

loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void

加载指定的数据。

baseUrl与historyUrl同时为空的情况下：

encoding如果为非base64（包括空值），则假定数据对安全URL字符范围内的八位字节使用ASCII编码，对该范围外的八位字节使用URL的标准%xx十六进制编码。

data数据必须使用base64编码或将内容中的任何#字符编码为%23。否则#将被视为内容的结尾而剩余的文本将被用作文档片段标识符。

说明

* 若加载本地图片，可以给baseUrl或historyUrl任一参数赋值空格，详情请参考示例代码。
* 加载本地图片场景，baseUrl和historyUrl不能同时为空，否则图片无法成功加载。
* 若html中的富文本中带有注入#等特殊字符，建议将baseUrl和historyUrl两个参数的值设置为"空格"。
* 加载文字场景，需主动设置<meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">避免文本字体大小不一致。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 按照"base64"或者"URL"编码后的一段字符串。 |
| mimeType | string | 是 | 媒体类型（MIME）。 |
| encoding | string | 是 | 编码类型，具体为"base64"或者"URL"编码。 |
| baseUrl | string | 否 | 指定的一个URL路径（"http"/"https"/"data"协议），并由Web组件赋值给window.origin。当加载大量html文件时，需设置为"data"。  传入undefined或null会抛出异常错误码401。 |
| historyUrl | string | 否 | 用作历史记录所使用的URL。非空时，历史记录以此URL进行管理。当baseUrl为空时，此属性无效。  传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

baseUrl与historyUrl同时为空。

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
12. Button('loadData')
13. .onClick(() => {
14. try {
15. this.controller.loadData(
16. "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
17. "text/html",
18. // UTF-8为charset。
19. "UTF-8"
20. );
21. } catch (error) {
22. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
23. }
24. })
25. Web({ src: 'www.example.com', controller: this.controller })
26. }
27. }
28. }
```

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
12. Button('loadData')
13. .onClick(() => {
14. try {
15. this.controller.loadData(
16. // Coding tests通过base64编码后的字符串。
17. "Q29kaW5nIHRlc3Rz",
18. "text/html",
19. "base64"
20. );
21. } catch (error) {
22. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
23. }
24. })
25. Web({ src: 'www.example.com', controller: this.controller })
26. }
27. }
28. }
```

指定baseURL。

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
12. Button('loadData')
13. .onClick(() => {
14. try {
15. this.controller.loadData(
16. "<img src=aa/bb.jpg>", // 会尝试从"https://xxx.com/" + "aa/bb.jpg"加载该图片
17. "text/html",
18. "UTF-8",
19. "https://xxx.com/",
20. "about:blank"
21. );
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

加载本地资源。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. updateContent: string = '<body><div><image src="resource://rawfile/xxx.png" alt="image -- end" width="500" height="250"></image></div></body>'

11. build() {
12. Column() {
13. Button('loadData')
14. .onClick(() => {
15. try {
16. // UTF-8为charset。
17. this.controller.loadData(this.updateContent, "text/html", "UTF-8", " ", " ");
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

加载沙箱图片。

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
12. Button('loadData')
13. .onClick(() => {
14. try {
15. this.controller.loadData(
16. "<img src=bb.jpg>", // 尝试从"file:///xxx/" + "bb.jpg"加载该图片。
17. "text/html",
18. "UTF-8",
19. // 加载本地应用沙箱内的图片路径，请将路径改为实际使用的沙箱路径。
20. "file:///data/storage/el2/base/haps/entry/files/data/.cache_dir/",
21. ""
22. );
23. } catch (error) {
24. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
25. }
26. })
27. Web({ src: 'www.example.com', controller: this.controller })
28. .fileAccess(true) // 为了加载应用沙箱内的图片，需要启用文件访问功能。
29. }
30. }
31. }
```

## accessForward

PhonePC/2in1TabletTVWearable

accessForward(): boolean

当前页面是否可前进，即当前页面是否有前进历史记录。

可以结合使用[getBackForwardEntries](arkts-apis-webview-webviewcontroller.md#getbackforwardentries)来获取当前WebView的历史信息列表，以及使用[accessStep](arkts-apis-webview-webviewcontroller.md#accessstep)来判断是否可以按照给定的步数前进或后退。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可以前进返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('accessForward')
13. .onClick(() => {
14. try {
15. let result = this.controller.accessForward();
16. console.info('result:' + result);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## forward

PhonePC/2in1TabletTVWearable

forward(): void

按照历史栈，前进一个页面。一般结合accessForward一起使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('forward')
13. .onClick(() => {
14. try {
15. this.controller.forward();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## accessBackward

PhonePC/2in1TabletTVWearable

accessBackward(): boolean

当前页面是否可后退，即当前页面是否有返回历史记录。

可以结合使用[getBackForwardEntries](arkts-apis-webview-webviewcontroller.md#getbackforwardentries)来获取当前WebView的历史信息列表，以及使用[accessStep](arkts-apis-webview-webviewcontroller.md#accessstep)来判断是否可以按照给定的步数前进或后退。

说明

在Web组件首次加载过程中调用[setCustomUserAgent](arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)，可能会导致在当前存在多个历史节点的情况下，获取的accessBackward实际为false，即没有后退节点。建议先调用setCustomUserAgent方法设置UserAgent，再通过loadUrl加载具体页面。

该现象是由于在Web组件首次加载时，调用[setCustomUserAgent](arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)会导致组件重新加载并保持初始历史节点的状态。随后新增的节点将替换初始历史节点，不会生成新的历史节点，导致accessBackward为false。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前页面可以后退返回true,否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('accessBackward')
13. .onClick(() => {
14. try {
15. let result = this.controller.accessBackward();
16. console.info('result:' + result);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## backward

PhonePC/2in1TabletTVWearable

backward(): void

按照历史栈，后退一个页面。一般结合[accessBackward](arkts-apis-webview-webviewcontroller.md#accessbackward)一起使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('backward')
13. .onClick(() => {
14. try {
15. this.controller.backward();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## onActive

PhonePC/2in1TabletTVWearable

onActive(): void

调用此接口通知Web组件进入前台激活状态。

激活状态是应用与用户互动的状态。应用会保持这种状态，直到发生某些事件（例如收到来电或设备屏幕关闭）时将焦点从应用移开。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('onActive')
13. .onClick(() => {
14. try {
15. this.controller.onActive();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## onInactive

PhonePC/2in1TabletTVWearable

onInactive(): void

调用此接口通知Web组件进入未激活状态。开发者可以在此回调中实现应用失去焦点时应表现的恰当行为。

此状态下会尽可能的暂停任何可以安全暂停的内容，例如动画和地理位置。但不会暂停JavaScript，要全局暂停JavaScript，请使用[pauseAllTimers](arkts-apis-webview-webviewcontroller.md#pausealltimers12)。要重新激活Web组件，请调用[onActive](arkts-apis-webview-webviewcontroller.md#onactive)。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('onInactive')
13. .onClick(() => {
14. try {
15. this.controller.onInactive();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## refresh

PhonePC/2in1TabletTVWearable

refresh(): void

调用此接口通知Web组件刷新网页。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('refresh')
13. .onClick(() => {
14. try {
15. this.controller.refresh();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## accessStep

PhonePC/2in1TabletTVWearable

accessStep(step: number): boolean

当前页面是否可前进或者后退给定的step步。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | number | 是 | 要跳转的步数，正数代表前进，负数代表后退。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 页面是否前进或后退。  返回true表示可以前进或者后退，返回false表示不可以前进或后退。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State steps: number = 2;

11. build() {
12. Column() {
13. Button('accessStep')
14. .onClick(() => {
15. try {
16. let result = this.controller.accessStep(this.steps);
17. console.info('result:' + result);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## clearHistory

PhonePC/2in1TabletTVWearable

clearHistory(): void

删除所有前进后退记录，不建议在onErrorReceive与onPageBegin中调用clearHistory，会造成异常退出。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('clearHistory')
13. .onClick(() => {
14. try {
15. this.controller.clearHistory();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## registerJavaScriptProxy

PhonePC/2in1TabletTVWearable

registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string): void

registerJavaScriptProxy提供了应用与Web组件加载的网页之间强大的交互能力。注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。

示例请参考[前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)。

说明

* registerJavaScriptProxy需要和deleteJavaScriptRegister接口配合使用，防止内存泄漏。
* 请尽可能只在可信的URL及安全通信HTTPS场景下进行registerJavaScriptProxy注册。在非可信的Web组件中注入JavaScript对象，可能会导致应用被恶意攻击。
* 在注册registerJavaScriptProxy后，应用会将JavaScript对象暴露给所有的页面frames。
* 同一方法在同步与异步列表中重复注册，将默认异步调用。
* 同步函数列表和异步函数列表不可同时为空，否则此次调用接口注册失败。
* 异步的作用在于：H5线程将异步JavaScript任务提交给ETS主线程后，无需等待任务执行完成并返回结果，H5线程即可继续执行后续任务。这在执行耗时较长的JavaScript任务或ETS线程较为拥堵的情况下，可以有效减少H5线程因JavaScript任务而被阻塞的情况。然而，异步JavaScript任务无法返回值，且任务执行的顺序无法保证，因此需要根据具体情境判断是否使用同步或异步方式。
* 注入的对象在页面下一次（重新）加载前不会出现在JavaScript中。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jsObject | object | 是 | 参与注册的应用侧JavaScript对象。可以单独声明方法和属性，但无法同时进行注册与使用。对象只包含属性时，H5可以访问对象中的属性。对象只包含方法时，H5可以访问对象中的方法。  1. 方法的参数和返回类型可以为string，number，boolean。  2. 方法的参数和返回类型支持Dictionary，Array，最多嵌套10层，每层1w个数据。  3. 方法的参数和返回类型支持Object，需要在Object里添加属性methodNameListForJsProxy:[fun1, fun2]，fun1和fun2为可被调用的方法。  4. 方法的参数支持Function，Promise，它们的Callback不能有返回值。  5. 方法的返回类型支持Promise，Promise的Callback不能有返回值。 |
| name | string | 是 | 注册对象的名称，与window中调用的对象名一致。注册后window对象可以通过此名字访问应用侧JavaScript对象。 |
| methodList | Array<string> | 是 | 参与注册的应用侧JavaScript对象的同步方法。 |
| asyncMethodList12+ | Array<string> | 否 | 参与注册的应用侧JavaScript对象的异步方法，默认为空。异步方法无法获取返回值。  传入undefined或null会抛出异常错误码401。 |
| permission12+ | string | 否 | JSON字符串，默认为空，通过该字符串配置JSBridge的权限管控，可以定义object和method级别的URL白名单。  1. scheme（协议）和host（域名）参数不可为空，且host不支持通配符，只能填写完整的host。  2. 可以仅配置object级别的白名单，该白名单对所有JSBridge方法生效。  3. 若JSBridge方法A设置了method级别的白名单，那么方法A最终的白名单是object级别白名单与method级别白名单的交集。  传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestObj {
6. constructor() {
7. }

9. test(testStr: string): string {
10. console.info('Web Component str' + testStr);
11. return testStr;
12. }

14. toString(): void {
15. console.info('Web Component toString');
16. }

18. testNumber(testNum: number): number {
19. console.info('Web Component number' + testNum);
20. return testNum;
21. }

23. asyncTestBool(testBol: boolean): void {
24. console.info('Web Component boolean' + testBol);
25. }
26. }

28. class WebObj {
29. constructor() {
30. }

32. webTest(): string {
33. console.info('Web test');
34. return "Web test";
35. }

37. webString(): void {
38. console.info('Web test toString');
39. }
40. }

42. class AsyncObj {
43. constructor() {
44. }

46. asyncTest(): void {
47. console.info('Async test');
48. }

50. asyncString(testStr: string): void {
51. console.info('Web async string' + testStr);
52. }
53. }

55. @Entry
56. @Component
57. struct Index {
58. controller: webview.WebviewController = new webview.WebviewController();
59. @State testObjtest: TestObj = new TestObj();
60. @State webTestObj: WebObj = new WebObj();
61. @State asyncTestObj: AsyncObj = new AsyncObj();

63. build() {
64. Column() {
65. Button('refresh')
66. .onClick(() => {
67. try {
68. this.controller.refresh();
69. } catch (error) {
70. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
71. }
72. })
73. Button('Register JavaScript To Window')
74. .onClick(() => {
75. try {
76. // 同时注册同步和异步函数
77. this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber"], ["asyncTestBool"]);
78. // 仅注册同步函数
79. this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
80. // 仅注册异步函数
81. this.controller.registerJavaScriptProxy(this.asyncTestObj, "objAsyncName", [], ["asyncTest", "asyncString"]);
82. } catch (error) {
83. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
84. }
85. })
86. Button('deleteJavaScriptRegister')
87. .onClick(() => {
88. try {
89. this.controller.deleteJavaScriptRegister("objName");
90. this.controller.deleteJavaScriptRegister("objTestName");
91. this.controller.deleteJavaScriptRegister("objAsyncName");
92. } catch (error) {
93. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
94. }
95. })
96. Web({ src: $rawfile('index.html'), controller: this.controller })
97. .javaScriptAccess(true)
98. }
99. }
100. }
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
8. <button type="button" onclick="htmlTest()">Click Me!</button>
9. <p id="demo"></p>
10. <p id="webDemo"></p>
11. <p id="asyncDemo"></p>
12. <script type="text/javascript">
13. function htmlTest() {
14. // This function call expects to return "ArkUI Web Component"
15. let str=objName.test("webtest data");
16. objName.testNumber(1);
17. objName.asyncTestBool(true);
18. document.getElementById("demo").innerHTML=str;
19. console.info('objName.test result:'+ str)

21. // This function call expects to return "Web test"
22. let webStr = objTestName.webTest();
23. document.getElementById("webDemo").innerHTML=webStr;
24. console.info('objTestName.webTest result:'+ webStr)

26. objAsyncName.asyncTest();
27. objAsyncName.asyncString("async test data");
28. }
29. </script>
30. </body>
31. </html>
```

更多示例，请参考[前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)。

## runJavaScript

PhonePC/2in1TabletTVWearable

runJavaScript(script: string, callback : AsyncCallback<string>): void

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过异步回调方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

说明

* 跨导航操作（如loadUrl）时，JavaScript状态将不再保留。例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。
* 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。
* 目前不支持传递对象，支持传递结构体。
* 执行异步方法无法获取返回值，需要根据具体情境判断是否使用同步或异步方式。
* 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |
| callback | AsyncCallback<string> | 是 | 回调执行JavaScript脚本结果。JavaScript脚本若执行失败或无返回值时，返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100003 | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State webResult: string = '';

10. build() {
11. Column() {
12. Text(this.webResult).fontSize(20)
13. Web({ src: $rawfile('index.html'), controller: this.controller })
14. .javaScriptAccess(true)
15. .onPageEnd(e => {
16. try {
17. this.controller.runJavaScript(
18. 'test()',
19. (error, result) => {
20. if (error) {
21. console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. return;
23. }
24. if (result) {
25. this.webResult = result;
26. console.info(`The test() return value is: ${result}`);
27. }
28. });
29. if (e) {
30. console.info('url: ', e.url);
31. }
32. } catch (error) {
33. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
34. }
35. })
36. }
37. }
38. }
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

## runJavaScript

PhonePC/2in1TabletTVWearable

runJavaScript(script: string): Promise<string>

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过Promise方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

说明

* 跨导航操作（如loadUrl）时，JavaScript状态 将不再保留，例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。
* 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。
* 目前不支持传递对象，支持传递结构体。
* 执行异步方法无法获取返回值，需要根据具体情境判断是否使用同步或异步方式。
* 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript脚本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise实例，返回脚本执行的结果，执行失败返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100003 | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

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
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .javaScriptAccess(true)
14. .onPageEnd(e => {
15. try {
16. this.controller.runJavaScript('test()')
17. .then((result) => {
18. console.info('result: ' + result);
19. })
20. .catch((error: BusinessError) => {
21. console.error("error: " + error);
22. })
23. if (e) {
24. console.info('url: ', e.url);
25. }
26. } catch (error) {
27. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
28. }
29. })
30. }
31. }
32. }
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

## runJavaScriptExt10+

PhonePC/2in1TabletTVWearable

runJavaScriptExt(script: string | ArrayBuffer, callback : AsyncCallback<JsMessageExt>): void

异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中调用。

说明

* 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | ArrayBuffer12+ | 是 | JavaScript脚本。 |
| callback | AsyncCallback<[JsMessageExt](arkts-apis-webview-jsmessageext.md)> | 是 | 回调执行JavaScript脚本结果。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State msg1: string = '';
9. @State msg2: string = '';

11. build() {
12. Column() {
13. Text(this.msg1).fontSize(20)
14. Text(this.msg2).fontSize(20)
15. Web({ src: $rawfile('index.html'), controller: this.controller })
16. .javaScriptAccess(true)
17. .onPageEnd(e => {
18. try {
19. this.controller.runJavaScriptExt(
20. 'test()',
21. (error, result) => {
22. if (error) {
23. console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
24. return;
25. }
26. if (result) {
27. try {
28. if (result.getErrorDescription()) {
29. // 若发生异常或返回类型不支持时，getErrorDescription不为空
30. console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
31. return;
32. }
33. let type = result.getType();
34. switch (type) {
35. case webview.JsMessageType.STRING: {
36. this.msg1 = "result type:" + typeof (result.getString());
37. this.msg2 = "result getString:" + ((result.getString()));
38. break;
39. }
40. case webview.JsMessageType.NUMBER: {
41. this.msg1 = "result type:" + typeof (result.getNumber());
42. this.msg2 = "result getNumber:" + ((result.getNumber()));
43. break;
44. }
45. case webview.JsMessageType.BOOLEAN: {
46. this.msg1 = "result type:" + typeof (result.getBoolean());
47. this.msg2 = "result getBoolean:" + ((result.getBoolean()));
48. break;
49. }
50. case webview.JsMessageType.ARRAY_BUFFER: {
51. this.msg1 = "result type:" + typeof (result.getArrayBuffer());
52. this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
53. break;
54. }
55. case webview.JsMessageType.ARRAY: {
56. this.msg1 = "result type:" + typeof (result.getArray());
57. this.msg2 = "result getArray:" + result.getArray();
58. break;
59. }
60. default: {
61. this.msg1 = "default break, type:" + type;
62. break;
63. }
64. }
65. }
66. catch (resError) {
67. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
68. }
69. }
70. });
71. if (e) {
72. console.info('url: ', e.url);
73. }
74. } catch (resError) {
75. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
76. }
77. })
78. }
79. }
80. }
```

```
1. // 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据。
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { common } from '@kit.AbilityKit';

7. @Entry
8. @Component
9. struct WebComponent {
10. controller: webview.WebviewController = new webview.WebviewController();
11. @State msg1: string = ''
12. @State msg2: string = ''

14. build() {
15. Column() {
16. Text(this.msg1).fontSize(20)
17. Text(this.msg2).fontSize(20)
18. Button('runJavaScriptExt')
19. .onClick(() => {
20. try {
21. let uiContext : UIContext = this.getUIContext();
22. let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
23. let filePath = context!.filesDir + 'test.txt';
24. // 新建并打开文件。
25. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
26. // 写入一段内容至文件。
27. fileIo.writeSync(file.fd, "test()");
28. // 从文件中读取内容。
29. let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
30. fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
31. // 关闭文件。
32. fileIo.closeSync(file);
33. this.controller.runJavaScriptExt(
34. arrayBuffer,
35. (error, result) => {
36. if (error) {
37. console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
38. return;
39. }
40. if (result) {
41. try {
42. if (result.getErrorDescription()) {
43. // 若发生异常或返回类型不支持时，getErrorDescription不为空
44. console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
45. return;
46. }
47. let type = result.getType();
48. switch (type) {
49. case webview.JsMessageType.STRING: {
50. this.msg1 = "result type:" + typeof (result.getString());
51. this.msg2 = "result getString:" + ((result.getString()));
52. break;
53. }
54. case webview.JsMessageType.NUMBER: {
55. this.msg1 = "result type:" + typeof (result.getNumber());
56. this.msg2 = "result getNumber:" + ((result.getNumber()));
57. break;
58. }
59. case webview.JsMessageType.BOOLEAN: {
60. this.msg1 = "result type:" + typeof (result.getBoolean());
61. this.msg2 = "result getBoolean:" + ((result.getBoolean()));
62. break;
63. }
64. case webview.JsMessageType.ARRAY_BUFFER: {
65. this.msg1 = "result type:" + typeof (result.getArrayBuffer());
66. this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
67. break;
68. }
69. case webview.JsMessageType.ARRAY: {
70. this.msg1 = "result type:" + typeof (result.getArray());
71. this.msg2 = "result getArray:" + result.getArray();
72. break;
73. }
74. default: {
75. this.msg1 = "default break, type:" + type;
76. break;
77. }
78. }
79. }
80. catch (resError) {
81. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
82. }
83. }
84. });
85. } catch (resError) {
86. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
87. }
88. })
89. Web({ src: $rawfile('index.html'), controller: this.controller })
90. .javaScriptAccess(true)
91. }
92. }
93. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html lang="en-gb">
4. <body>
5. <h1>run JavaScript Ext demo</h1>
6. </body>
7. <script type="text/javascript">
8. function test() {
9. return "hello, world";
10. }
11. </script>
12. </html>
```

## runJavaScriptExt10+

PhonePC/2in1TabletTVWearable

runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>

异步执行JavaScript脚本，并通过Promise方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中调用。

说明

* 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | ArrayBuffer12+ | 是 | JavaScript脚本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[JsMessageExt](arkts-apis-webview-jsmessageext.md)> | Promise实例，返回脚本执行的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State webResult: string = '';
10. @State msg1: string = '';
11. @State msg2: string = '';

13. build() {
14. Column() {
15. Text(this.webResult).fontSize(20)
16. Text(this.msg1).fontSize(20)
17. Text(this.msg2).fontSize(20)
18. Web({ src: $rawfile('index.html'), controller: this.controller })
19. .javaScriptAccess(true)
20. .onPageEnd(() => {
21. this.controller.runJavaScriptExt('test()')
22. .then((result) => {
23. try {
24. if (result.getErrorDescription()) {
25. // 若发生异常或返回类型不支持时，getErrorDescription不为空
26. console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
27. return;
28. }
29. let type = result.getType();
30. switch (type) {
31. case webview.JsMessageType.STRING: {
32. this.msg1 = "result type:" + typeof (result.getString());
33. this.msg2 = "result getString:" + ((result.getString()));
34. break;
35. }
36. case webview.JsMessageType.NUMBER: {
37. this.msg1 = "result type:" + typeof (result.getNumber());
38. this.msg2 = "result getNumber:" + ((result.getNumber()));
39. break;
40. }
41. case webview.JsMessageType.BOOLEAN: {
42. this.msg1 = "result type:" + typeof (result.getBoolean());
43. this.msg2 = "result getBoolean:" + ((result.getBoolean()));
44. break;
45. }
46. case webview.JsMessageType.ARRAY_BUFFER: {
47. this.msg1 = "result type:" + typeof (result.getArrayBuffer());
48. this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
49. break;
50. }
51. case webview.JsMessageType.ARRAY: {
52. this.msg1 = "result type:" + typeof (result.getArray());
53. this.msg2 = "result getArray:" + result.getArray();
54. break;
55. }
56. default: {
57. this.msg1 = "default break, type:" + type;
58. break;
59. }
60. }
61. }
62. catch (resError) {
63. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
64. }
65. }).catch((error: BusinessError) => {
66. console.error("error: " + error);
67. })
68. })
69. }
70. }
71. }
```

```
1. // 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据。
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { common } from '@kit.AbilityKit';

7. @Entry
8. @Component
9. struct WebComponent {
10. controller: webview.WebviewController = new webview.WebviewController();
11. @State msg1: string = '';
12. @State msg2: string = '';

14. build() {
15. Column() {
16. Text(this.msg1).fontSize(20)
17. Text(this.msg2).fontSize(20)
18. Button('runJavaScriptExt')
19. .onClick(() => {
20. try {
21. let uiContext : UIContext = this.getUIContext();
22. let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
23. let filePath = context!.filesDir + 'test.txt';
24. // 新建并打开文件。
25. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
26. // 写入一段内容至文件。
27. fileIo.writeSync(file.fd, "test()");
28. // 从文件中读取内容。
29. let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
30. fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
31. // 关闭文件。
32. fileIo.closeSync(file);
33. this.controller.runJavaScriptExt(arrayBuffer)
34. .then((result) => {
35. try {
36. if (result.getErrorDescription()) {
37. // 若发生异常或返回类型不支持时，getErrorDescription不为空
38. console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
39. return;
40. }
41. let type = result.getType();
42. switch (type) {
43. case webview.JsMessageType.STRING: {
44. this.msg1 = "result type:" + typeof (result.getString());
45. this.msg2 = "result getString:" + ((result.getString()));
46. break;
47. }
48. case webview.JsMessageType.NUMBER: {
49. this.msg1 = "result type:" + typeof (result.getNumber());
50. this.msg2 = "result getNumber:" + ((result.getNumber()));
51. break;
52. }
53. case webview.JsMessageType.BOOLEAN: {
54. this.msg1 = "result type:" + typeof (result.getBoolean());
55. this.msg2 = "result getBoolean:" + ((result.getBoolean()));
56. break;
57. }
58. case webview.JsMessageType.ARRAY_BUFFER: {
59. this.msg1 = "result type:" + typeof (result.getArrayBuffer());
60. this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
61. break;
62. }
63. case webview.JsMessageType.ARRAY: {
64. this.msg1 = "result type:" + typeof (result.getArray());
65. this.msg2 = "result getArray:" + result.getArray();
66. break;
67. }
68. default: {
69. this.msg1 = "default break, type:" + type;
70. break;
71. }
72. }
73. }
74. catch (resError) {
75. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
76. }
77. })
78. .catch((error: BusinessError) => {
79. console.error("error: " + error);
80. })
81. } catch (error) {
82. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
83. }
84. })
85. Web({ src: $rawfile('index.html'), controller: this.controller })
86. .javaScriptAccess(true)
87. }
88. }
89. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html lang="en-gb">
4. <body>
5. <h1>run JavaScript Ext demo</h1>
6. </body>
7. <script type="text/javascript">
8. function test() {
9. return "hello, world";
10. }
11. </script>
12. </html>
```

## deleteJavaScriptRegister

PhonePC/2in1TabletTVWearable

deleteJavaScriptRegister(name: string): void

删除通过[registerJavaScriptProxy](arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)或者[javaScriptProxy](arkts-basic-components-web-attributes.md#javascriptproxy)注册到window上的指定name的应用侧JavaScript对象。删除操作在页面下次（重新）加载后生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 注册对象的名称，可在网页侧JavaScript中通过此名称调用应用侧JavaScript对象。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100008 | Failed to delete JavaScriptProxy because it does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestObj {
6. constructor() {
7. }

9. test(): string {
10. return "ArkUI Web Component";
11. }

13. toString(): void {
14. console.info('Web Component toString');
15. }
16. }

18. @Entry
19. @Component
20. struct WebComponent {
21. controller: webview.WebviewController = new webview.WebviewController();
22. @State testObjtest: TestObj = new TestObj();
23. @State name: string = 'objName';
24. build() {
25. Column() {
26. Button('refresh')
27. .onClick(() => {
28. try {
29. this.controller.refresh();
30. } catch (error) {
31. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. })
34. Button('Register JavaScript To Window')
35. .onClick(() => {
36. try {
37. this.controller.registerJavaScriptProxy(this.testObjtest, this.name, ["test", "toString"]);
38. } catch (error) {
39. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
40. }
41. })
42. Button('deleteJavaScriptRegister')
43. .onClick(() => {
44. try {
45. this.controller.deleteJavaScriptRegister(this.name);
46. } catch (error) {
47. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
48. }
49. })
50. Web({ src: $rawfile('index.html'), controller: this.controller })
51. .javaScriptAccess(true)
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
5. <meta charset="utf-8">
6. </head>
7. <body>
8. <button type="button" onclick="htmlTest()">Click Me!</button>
9. <p id="demo"></p>
10. <script type="text/javascript">
11. function htmlTest() {
12. let str=objName.test();
13. document.getElementById("demo").innerHTML=str;
14. console.info('objName.test result:'+ str)
15. }
16. </script>
17. </body>
18. </html>
```

## zoom

PhonePC/2in1TabletTVWearable

zoom(factor: number): void

调整当前网页的缩放比例，[zoomAccess](arkts-basic-components-web-attributes.md#zoomaccess)需为true。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factor | number | 是 | 基于当前网页所需调整的相对缩放比例，入参要求大于0，当入参为1时为默认加载网页的缩放比例，入参小于1为缩小，入参大于1为放大。  取值范围：(0，100]。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State factor: number = 2;

11. build() {
12. Column() {
13. Button('zoom')
14. .onClick(() => {
15. try {
16. this.controller.zoom(this.factor);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. .zoomAccess(true)
23. }
24. }
25. }
```

## searchAllAsync

PhonePC/2in1TabletTVWearable

searchAllAsync(searchString: string): void

异步查找网页中所有匹配关键字'searchString'的内容并高亮，结果通过[onSearchResultReceive](arkts-basic-components-web-events.md#onsearchresultreceive9)异步返回。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 | 查找的关键字。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State searchString: string = "Hello World";

11. build() {
12. Column() {
13. Button('searchString')
14. .onClick(() => {
15. try {
16. this.controller.searchAllAsync(this.searchString);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: $rawfile('index.html'), controller: this.controller })
22. .onSearchResultReceive(ret => {
23. if (ret) {
24. console.info("on search result receive:" + "[cur]" + ret.activeMatchOrdinal +
25. "[total]" + ret.numberOfMatches + "[isDone]" + ret.isDoneCounting);
26. }
27. })
28. }
29. }
30. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <p>Hello World Highlight Hello World</p>
6. </body>
7. </html>
```

## clearMatches

PhonePC/2in1TabletTVWearable

clearMatches(): void

清除所有通过[searchAllAsync](arkts-apis-webview-webviewcontroller.md#searchallasync)匹配到的高亮字符查找结果。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('clearMatches')
13. .onClick(() => {
14. try {
15. this.controller.clearMatches();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: $rawfile('index.html'), controller: this.controller })
21. }
22. }
23. }
```

加载的html文件，请参考[searchAllAsync](arkts-apis-webview-webviewcontroller.md#searchallasync)接口下加载的html文件。

## searchNext

PhonePC/2in1TabletTVWearable

searchNext(forward: boolean): void

滚动到下一个匹配的查找结果并高亮。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| forward | boolean | 是 | 从前向后或者逆向查找方式。  true表示从前向后查找，false表示从后向前查找。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

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
12. Button('searchNext')
13. .onClick(() => {
14. try {
15. this.controller.searchNext(true);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: $rawfile('index.html'), controller: this.controller })
21. }
22. }
23. }
```

加载的html文件，请参考[searchAllAsync](arkts-apis-webview-webviewcontroller.md#searchallasync)接口下加载的html文件。

## clearSslCache

PhonePC/2in1TabletTVWearable

clearSslCache(): void

清除Web组件记录的SSL证书错误事件对应的用户操作行为。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('clearSslCache')
13. .onClick(() => {
14. try {
15. this.controller.clearSslCache();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## clearClientAuthenticationCache

PhonePC/2in1TabletTVWearable

clearClientAuthenticationCache(): void

清除Web组件记录的客户端证书请求事件对应的用户操作行为。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('clearClientAuthenticationCache')
13. .onClick(() => {
14. try {
15. this.controller.clearClientAuthenticationCache();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## createWebMessagePorts

PhonePC/2in1TabletTVWearable

createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>

创建Web消息端口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isExtentionType10+ | boolean | 否 | 是否使用扩展增强接口。  true表示使用扩展增强接口，false表示不使用扩展增强接口。  默认值：false。  传入undefined或null会抛出异常错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[WebMessagePort](arkts-apis-webview-webmessageport.md)> | web消息端口列表。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

## postMessage

PhonePC/2in1TabletTVWearable

postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void

发送Web消息端口到HTML。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要发送的消息名称。 |
| ports | Array<[WebMessagePort](arkts-apis-webview-webmessageport.md)> | 是 | 要发送的消息端口。 |
| uri | string | 是 | 接收该消息的URI。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

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
16. Text(this.receivedFromHtml)
17. // 输入框的内容发送到html
18. TextInput({ placeholder: 'Send this message from ets to HTML' })
19. .onChange((value: string) => {
20. this.sendFromEts = value;
21. })

23. Button('postMessage')
24. .onClick(() => {
25. try {
26. // 1、创建两个消息端口。
27. this.ports = this.controller.createWebMessagePorts();
28. // 2、在应用侧的消息端口(如端口1)上注册回调事件。
29. this.ports[1].onMessageEvent((result: webview.WebMessage) => {
30. let msg = 'Got msg from HTML:';
31. if (typeof (result) == "string") {
32. console.info("received string message from html5, string is:" + result);
33. msg = msg + result;
34. } else if (typeof (result) == "object") {
35. if (result instanceof ArrayBuffer) {
36. console.info("received arraybuffer from html5, length is:" + result.byteLength);
37. msg = msg + "length is " + result.byteLength;
38. } else {
39. console.info("not support");
40. }
41. } else {
42. console.info("not support");
43. }
44. this.receivedFromHtml = msg;
45. })
46. // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
47. this.controller.postMessage('__init_port__', [this.ports[0]], '*');
48. } catch (error) {
49. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
50. }
51. })

53. // 4、使用应用侧的端口给另一个已经发送到html的端口发送消息。
54. Button('SendDataToHTML')
55. .onClick(() => {
56. try {
57. if (this.ports && this.ports[1]) {
58. this.ports[1].postMessageEvent(this.sendFromEts);
59. } else {
60. console.error(`ports is null, Please initialize first`);
61. }
62. } catch (error) {
63. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
64. }
65. })
66. Web({ src: $rawfile('index.html'), controller: this.controller })
67. }
68. }
69. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
6. <title>WebView Message Port Demo</title>
7. </head>

9. <body>
10. <h1>WebView Message Port Demo</h1>
11. <div>
12. <input type="button" value="SendToEts" onclick="PostMsgToEts(msgFromJS.value);"/><br/>
13. <input id="msgFromJS" type="text" value="send this message from HTML to ets"/><br/>
14. </div>
15. <p class="output">display received message send from ets</p>
16. </body>
17. <script src="xxx.js"></script>
18. </html>
```

```
1. // xxx.js
2. var h5Port;
3. var output = document.querySelector('.output');
4. window.addEventListener('message', function (event) {
5. if (event.data == '__init_port__') {
6. if (event.ports[0] != null) {
7. h5Port = event.ports[0]; // 1. 保存从ets侧发送过来的端口
8. h5Port.onmessage = function (event) {
9. // 2. 接收ets侧发送过来的消息.
10. var msg = 'Got message from ets:';
11. var result = event.data;
12. if (typeof(result) == "string") {
13. console.info("received string message from html5, string is:" + result);
14. msg = msg + result;
15. } else if (typeof(result) == "object") {
16. if (result instanceof ArrayBuffer) {
17. console.info("received arraybuffer from html5, length is:" + result.byteLength);
18. msg = msg + "length is " + result.byteLength;
19. } else {
20. console.info("not support");
21. }
22. } else {
23. console.info("not support");
24. }
25. output.innerHTML = msg;
26. }
27. }
28. }
29. })

31. // 3. 使用h5Port往ets侧发送消息.
32. function PostMsgToEts(data) {
33. if (h5Port) {
34. h5Port.postMessage(data);
35. } else {
36. console.error("h5Port is null, Please initialize first");
37. }
38. }
```

## requestFocus

PhonePC/2in1TabletTVWearable

requestFocus(): void

使当前web页面获取焦点。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('requestFocus')
13. .onClick(() => {
14. try {
15. this.controller.requestFocus();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. });
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## zoomIn

PhonePC/2in1TabletTVWearable

zoomIn(): void

调用此接口将当前网页进行放大，比例为25%。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |

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
12. Button('zoomIn')
13. .onClick(() => {
14. try {
15. this.controller.zoomIn();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## zoomOut

PhonePC/2in1TabletTVWearable

zoomOut(): void

调用此接口将当前网页进行缩小，比例为20%。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |

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
12. Button('zoomOut')
13. .onClick(() => {
14. try {
15. this.controller.zoomOut();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## getWebId

PhonePC/2in1TabletTVWearable

getWebId(): number

获取当前Web组件的索引值，用于多个Web组件的管理。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前Web组件的索引值。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getWebId')
13. .onClick(() => {
14. try {
15. let id = this.controller.getWebId();
16. console.info("id: " + id);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## getUserAgent

PhonePC/2in1TabletTVWearable

getUserAgent(): string

获取当前默认用户代理。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 默认用户代理。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getUserAgent')
13. .onClick(() => {
14. try {
15. let userAgent = this.controller.getUserAgent();
16. console.info("userAgent: " + userAgent);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

支持开发者基于默认的User-Agent去定制User-Agent。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State ua: string = "";

11. aboutToAppear(): void {
12. webview.once('webInited', () => {
13. try {
14. // 应用侧用法示例，定制User-Agent。
15. this.ua = this.controller.getUserAgent() + 'xxx';
16. this.controller.setCustomUserAgent(this.ua);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. }

23. build() {
24. Column() {
25. Web({ src: 'www.example.com', controller: this.controller })
26. }
27. }
28. }
```

## getTitle

PhonePC/2in1TabletTVWearable

getTitle(): string

获取当前网页的标题。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前网页的标题。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例:**

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
12. Button('getTitle')
13. .onClick(() => {
14. try {
15. let title = this.controller.getTitle();
16. console.info("title: " + title);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## getPageHeight

PhonePC/2in1TabletTVWearable

getPageHeight(): number

获取当前网页的页面高度。具体使用详情请参考[获取网页内容高度](../harmonyos-guides/web-getpage-height.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前网页的页面高度。单位：vp。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例:**

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
12. Button('getPageHeight')
13. .onClick(() => {
14. try {
15. let pageHeight = this.controller.getPageHeight();
16. console.info("pageHeight : " + pageHeight);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## storeWebArchive

PhonePC/2in1TabletTVWearable

storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void

以回调方式异步保存当前页面。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseName | string | 是 | 生成的离线网页存储位置，该值不能为空。 |
| autoName | boolean | 是 | 决定是否自动生成文件名。  false表示按baseName的文件名存储，true表示根据当前Url自动生成文件名，并按baseName的文件目录存储。 |
| callback | AsyncCallback<string> | 是 | 返回文件存储路径，保存网页失败会返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100003 | Invalid resource path or file type. |

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
12. Button('storeWebArchive')
13. .onClick(() => {
14. try {
15. this.controller.storeWebArchive("/data/storage/el2/base/", true, (error, filename) => {
16. if (error) {
17. console.error(`save web archive error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. return;
19. }
20. if (filename != null) {
21. console.info(`save web archive success: ${filename}`);
22. }
23. });
24. } catch (error) {
25. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
26. }
27. })
28. Web({ src: 'www.example.com', controller: this.controller })
29. }
30. }
31. }
```

## storeWebArchive

PhonePC/2in1TabletTVWearable

storeWebArchive(baseName: string, autoName: boolean): Promise<string>

以Promise方式异步保存当前页面。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseName | string | 是 | 生成的离线网页存储位置，该值不能为空。 |
| autoName | boolean | 是 | 决定是否自动生成文件名。  false表示按baseName的文件名存储，true表示根据当前Url自动生成文件名，并按baseName的文件目录存储。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise实例，保存成功返回文件路径，保存失败返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100003 | Invalid resource path or file type. |

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
12. Button('storeWebArchive')
13. .onClick(() => {
14. try {
15. this.controller.storeWebArchive("/data/storage/el2/base/", true)
16. .then(filename => {
17. if (filename != null) {
18. console.info(`save web archive success: ${filename}`)
19. }
20. })
21. .catch((error: BusinessError) => {
22. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
23. })
24. } catch (error) {
25. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
26. }
27. })
28. Web({ src: 'www.example.com', controller: this.controller })
29. }
30. }
31. }
```

## getUrl

PhonePC/2in1TabletTVWearable

getUrl(): string

获取当前页面的url地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前页面的url地址。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getUrl')
13. .onClick(() => {
14. try {
15. let url = this.controller.getUrl();
16. console.info("url: " + url);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## stop

PhonePC/2in1TabletTVWearable

stop(): void

停止页面加载。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('stop')
13. .onClick(() => {
14. try {
15. this.controller.stop();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. });
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## backOrForward

PhonePC/2in1TabletTVWearable

backOrForward(step: number): void

按照历史栈，前进或者后退指定步长的页面，当历史栈中不存在对应步长的页面时，不会进行页面跳转。

前进或者后退页面时，直接使用已加载过的网页，无需重新加载网页。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | number | 是 | 需要前进或后退的步长。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State step: number = -2;

11. build() {
12. Column() {
13. Button('backOrForward')
14. .onClick(() => {
15. try {
16. this.controller.backOrForward(this.step);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## scrollTo

PhonePC/2in1TabletTVWearable

scrollTo(x:number, y:number, duration?:number): void

在指定时间内，将页面滚动到指定的绝对位置。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 绝对位置的水平坐标，当传入数值为负数时，按照传入0处理。  单位：vp。 |
| y | number | 是 | 绝对位置的垂直坐标，当传入数值为负数时，按照传入0处理。  单位：vp。 |
| duration14+ | number | 否 | 滚动动画时间。  单位：ms。  不传入为无动画，当传入数值为负数或传入0时，按照不传入处理。  传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

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
12. Button('scrollTo')
13. .onClick(() => {
14. try {
15. this.controller.scrollTo(50, 50, 500);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Button('stopScroll')
21. .onClick(() => {
22. try {
23. this.controller.scrollBy(0, 0, 1); // 如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
24. } catch (error) {
25. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
26. }
27. })
28. Web({ src: $rawfile('index.html'), controller: this.controller })
29. }
30. }
31. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>Demo</title>
6. <style>
7. body {
8. width:2000px;
9. height:2000px;
10. padding-right:170px;
11. padding-left:170px;
12. border:5px solid blueviolet;
13. }
14. </style>
15. </head>
16. <body>
17. Scroll Test
18. </body>
19. </html>
```

## scrollBy

PhonePC/2in1TabletTVWearable

scrollBy(deltaX:number, deltaY:number,duration?:number): void

在指定时间内将页面滚动指定的偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deltaX | number | 是 | 水平偏移量，其中水平向右为正方向。  单位：vp。 |
| deltaY | number | 是 | 垂直偏移量，其中垂直向下为正方向。  单位：vp。 |
| duration14+ | number | 否 | 滚动动画时间。  单位：ms。  不传入为无动画，当传入数值为负数或传入0时，按照不传入处理。  传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

说明

嵌套滚动场景中，调用scrollBy不会触发父组件的嵌套滚动。

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
12. Button('scrollBy')
13. .onClick(() => {
14. try {
15. this.controller.scrollBy(50, 50, 500);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Button('stopScroll')
21. .onClick(() => {
22. try {
23. this.controller.scrollBy(0, 0, 1); // 如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
24. } catch (error) {
25. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
26. }
27. })
28. Web({ src: $rawfile('index.html'), controller: this.controller })
29. }
30. }
31. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>Demo</title>
6. <style>
7. body {
8. width:2000px;
9. height:2000px;
10. padding-right:170px;
11. padding-left:170px;
12. border:5px solid blueviolet;
13. }
14. </style>
15. </head>
16. <body>
17. Scroll Test
18. </body>
19. </html>
```

## scrollByWithResult12+

PhonePC/2in1TabletTVWearable

scrollByWithResult(deltaX: number, deltaY: number): boolean

将页面滚动指定的偏移量，返回值表示此次滚动是否执行成功。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deltaX | number | 是 | 水平偏移量，其中水平向右为正方向。  单位：vp。 |
| deltaY | number | 是 | 垂直偏移量，其中垂直向下为正方向。  单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示当前网页可以滑动，false表示当前网页不可以滑动。  默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

说明

* 返回值场景：Web页面处于触摸中状态时，返回false，否则返回true。
* 同层渲染场景中，Web的同层渲染区域处于触摸中状态时，返回值为true。
* 嵌套滚动场景中，调用scrollByWithResult不会触发父组件的嵌套滚动。
* 此接口不保证滑动帧率性能。

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
12. Button('scrollByWithResult')
13. .onClick(() => {
14. try {
15. let result = this.controller.scrollByWithResult(50, 50);
16. console.info("original result: " + result);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: $rawfile('index.html'), controller: this.controller })
22. }
23. }
24. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>Demo</title>
6. <style>
7. body {
8. width:2000px;
9. height:2000px;
10. padding-right:170px;
11. padding-left:170px;
12. border:5px solid blueviolet;
13. }
14. </style>
15. </head>
16. <body>
17. Scroll Test
18. </body>
19. </html>
```

## slideScroll

PhonePC/2in1TabletTVWearable

slideScroll(vx:number, vy:number): void

按照指定速度模拟对页面的轻扫滚动动作。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vx | number | 是 | 轻扫滚动的水平速度分量，其中水平向右为速度正方向。  单位：vp/s。 |
| vy | number | 是 | 轻扫滚动的垂直速度分量，其中垂直向下为速度正方向。  单位：vp/s。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

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
12. Button('slideScroll')
13. .onClick(() => {
14. try {
15. this.controller.slideScroll(500, 500);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: $rawfile('index.html'), controller: this.controller })
21. }
22. }
23. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>Demo</title>
6. <style>
7. body {
8. width:3000px;
9. height:3000px;
10. padding-right:170px;
11. padding-left:170px;
12. border:5px solid blueviolet;
13. }
14. </style>
15. </head>
16. <body>
17. Scroll Test
18. </body>
19. </html>
```

## getOriginalUrl

PhonePC/2in1TabletTVWearable

getOriginalUrl(): string

获取当前页面的原始url地址。

风险提示：如果想获取url来做JavascriptProxy通信接口认证，请使用[getLastJavascriptProxyCallingFrameUrl12+](arkts-apis-webview-webviewcontroller.md#getlastjavascriptproxycallingframeurl12)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前页面的原始url地址。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getOrgUrl')
13. .onClick(() => {
14. try {
15. let url = this.controller.getOriginalUrl();
16. console.info("original url: " + url);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## getFavicon

PhonePC/2in1TabletTVWearable

getFavicon(): image.PixelMap

获取页面的favicon图标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.[PixelMap](arkts-apis-image-pixelmap.md) | 页面favicon图标的PixelMap对象。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { image } from '@kit.ImageKit';

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();
10. @State pixelmap: image.PixelMap | undefined = undefined;

12. build() {
13. Column() {
14. Button('getFavicon')
15. .onClick(() => {
16. try {
17. this.pixelmap = this.controller.getFavicon();
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## setNetworkAvailable

PhonePC/2in1TabletTVWearable

setNetworkAvailable(enable: boolean): void

设置JavaScript中的window.navigator.onLine属性。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置JavaScript中的window.navigator.onLine属性。  true表示设置JavaScript中的window.navigator.onLine属性为true，false表示设置JavaScript中的window.navigator.onLine属性为false。  默认值：true。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('setNetworkAvailable')
13. .onClick(() => {
14. try {
15. this.controller.setNetworkAvailable(true);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: $rawfile('index.html'), controller: this.controller })
21. }
22. }
23. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <h1>online 属性</h1>
6. <p id="demo"></p>
7. <button onclick="func()">click</button>
8. <script>
9. // 检测浏览器是否在线。
10. var online1 = navigator.onLine;
11. document.getElementById("demo").innerHTML = "浏览器在线：" + online1;

13. function func(){
14. var online2 = navigator.onLine;
15. document.getElementById("demo").innerHTML = "浏览器在线：" + online2;
16. }
17. </script>
18. </body>
19. </html>
```

## hasImage

PhonePC/2in1TabletTVWearable

hasImage(callback: AsyncCallback<boolean>): void

通过Callback方式异步查找当前页面是否存在图像。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 返回查找页面是否存在图像。  true表示页面存在图像；false表示页面不存在图像。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('hasImageCb')
13. .onClick(() => {
14. try {
15. this.controller.hasImage((error, data) => {
16. if (error) {
17. console.error(`hasImage error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. return;
19. }
20. console.info("hasImage: " + data);
21. });
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

## hasImage

PhonePC/2in1TabletTVWearable

hasImage(): Promise<boolean>

通过Promise方式异步查找当前页面是否存在图像。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise实例，返回查找页面是否存在图像。  true表示页面存在图像；false表示页面不存在图像。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

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
12. Button('hasImagePm')
13. .onClick(() => {
14. try {
15. this.controller.hasImage().then((data) => {
16. console.info('hasImage: ' + data);
17. }).catch((error: BusinessError) => {
18. console.error("error: " + error);
19. })
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## removeCache

PhonePC/2in1TabletTVWearable

removeCache(clearRom: boolean): void

清除应用中的资源缓存文件，此方法将会清除同一应用中所有Webview的缓存文件。

说明

可以通过在data/storage/el2/base/cache/web/Cache目录下查看Webview的缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearRom | boolean | 是 | 设置为true时同时清除ROM和RAM中的缓存，设置为false时只清除RAM中的缓存。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('removeCache')
13. .onClick(() => {
14. try {
15. this.controller.removeCache(false);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## removeAllCache18+

PhonePC/2in1TabletTVWearable

static removeAllCache(clearRom: boolean): void

清除应用中的资源缓存文件，此方法将会清除同一应用中所有Webview的缓存文件。

说明

可以通过在data/app/el2/100/base/<applicationPackageName>/cache/web/目录下查看Webview的缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearRom | boolean | 是 | 设置为true时同时清除ROM和RAM中的缓存，设置为false时只清除RAM中的缓存。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('removeAllCache')
13. .onClick(() => {
14. try {
15. webview.WebviewController.removeAllCache(false);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## pageUp

PhonePC/2in1TabletTVWearable

pageUp(top: boolean): void

将Webview的内容向上滚动半个视框大小或者跳转到页面最顶部，通过top入参控制。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| top | boolean | 是 | 是否跳转到页面最顶部。  false表示将页面内容向上滚动半个视框大小，true表示跳转到页面最顶部。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('pageUp')
13. .onClick(() => {
14. try {
15. this.controller.pageUp(false);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: $rawfile("index.html"), controller: this.controller })
21. }
22. }
23. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
6. <style>
7. .blue {
8. background-color: lightblue;
9. }
10. .green {
11. background-color: lightgreen;
12. }
13. .blue, .green {
14. font-size:16px;
15. height:200px;
16. text-align: center;       /* 水平居中 */
17. line-height: 200px;       /* 垂直居中（值等于容器高度） */
18. }
19. </style>
20. </head>
21. <body>
22. <div class="blue" >webArea</div>
23. <div class="green">webArea</div>
24. <div class="blue">webArea</div>
25. <div class="green">webArea</div>
26. <div class="blue">webArea</div>
27. <div class="green">webArea</div>
28. <div class="blue">webArea</div>
29. </body>
30. </html>
```

## pageDown

PhonePC/2in1TabletTVWearable

pageDown(bottom: boolean): void

将Webview的内容向下滚动半个视框大小或者跳转到页面最底部，通过bottom入参控制。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bottom | boolean | 是 | 是否跳转到页面最底部。  false时表示将页面内容向下滚动半个视框大小，true表示跳转到页面最底部。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('pageDown')
13. .onClick(() => {
14. try {
15. this.controller.pageDown(false);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: $rawfile("index.html"), controller: this.controller })
21. }
22. }
23. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
6. <style>
7. .blue {
8. background-color: lightblue;
9. }
10. .green {
11. background-color: lightgreen;
12. }
13. .blue, .green {
14. font-size:16px;
15. height:200px;
16. text-align: center;       /* 水平居中 */
17. line-height: 200px;       /* 垂直居中（值等于容器高度） */
18. }
19. </style>
20. </head>
21. <body>
22. <div class="blue" >webArea</div>
23. <div class="green">webArea</div>
24. <div class="blue">webArea</div>
25. <div class="green">webArea</div>
26. <div class="blue">webArea</div>
27. <div class="green">webArea</div>
28. <div class="blue">webArea</div>
29. </body>
30. </html>
```

## getBackForwardEntries

PhonePC/2in1TabletTVWearable

getBackForwardEntries(): BackForwardList

获取当前Webview的历史信息列表。

说明

[onLoadIntercept](arkts-basic-components-web-events.md#onloadintercept10)在加载开始的时候触发，该时刻还未生成历史节点，所以在onLoadIntercept中调用getBackForwardEntries拿到的历史栈不包括当前正在加载中的跳转。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BackForwardList](arkts-apis-webview-backforwardlist.md) | 当前Webview的历史信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getBackForwardEntries')
13. .onClick(() => {
14. try {
15. let list = this.controller.getBackForwardEntries()
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## serializeWebState

PhonePC/2in1TabletTVWearable

serializeWebState(): Uint8Array

将当前Webview的页面状态历史记录信息序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 当前Webview的页面状态历史记录序列化后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

1.对文件的操作需要导入文件管理模块，详情请参考[文件管理](js-apis-file-fs.md)。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. Button('serializeWebState')
14. .onClick(() => {
15. try {
16. let state = this.controller.serializeWebState();
17. let path:string | undefined = AppStorage.get("cacheDir");
18. if (path) {
19. path += '/WebState';
20. // 以同步方法打开文件。
21. let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
22. fileIo.writeSync(file.fd, state.buffer);
23. fileIo.closeSync(file.fd);
24. }
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. })
29. Web({ src: 'www.example.com', controller: this.controller })
30. }
31. }
32. }
```

2.修改EntryAbility.ets。

获取应用缓存文件路径。

```
1. // xxx.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
7. AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
8. }
9. }
```

## restoreWebState

PhonePC/2in1TabletTVWearable

restoreWebState(state: Uint8Array): void

当前Webview从序列化数据中恢复页面状态历史记录。

如果state过大，可能会导致异常。建议state大于512k时，放弃恢复页面状态历史记录。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | Uint8Array | 是 | 页面状态历史记录序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

1.对文件的操作需要导入文件管理模块，详情请参考[文件管理](js-apis-file-fs.md)。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. Button('RestoreWebState')
14. .onClick(() => {
15. try {
16. let path: string | undefined = AppStorage.get("cacheDir");
17. if (path) {
18. path += '/WebState';
19. // 以同步方法打开文件。
20. let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE);
21. let stat = fileIo.statSync(path);
22. let size = stat.size;
23. let buf = new ArrayBuffer(size);
24. fileIo.read(file.fd, buf, (err, readLen) => {
25. if (err) {
26. console.error("console error with error message: " + err.message + ", error code: " + err.code);
27. } else {
28. console.info("read file data succeed");
29. this.controller.restoreWebState(new Uint8Array(buf.slice(0, readLen)));
30. fileIo.closeSync(file);
31. }
32. });
33. }
34. } catch (error) {
35. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
36. }
37. })
38. Web({ src: 'www.example.com', controller: this.controller })
39. }
40. }
41. }
```

2.修改EntryAbility.ets。

获取应用缓存文件路径。

```
1. // xxx.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
7. AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
8. }
9. }
```

## customizeSchemes

PhonePC/2in1TabletTVWearable

static customizeSchemes(schemes: Array<WebCustomScheme>): void

对Web内核赋予自定义协议url的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议url时，该fetch请求可被[onInterceptRequest](arkts-basic-components-web-events.md#oninterceptrequest9)事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| schemes | Array<[WebCustomScheme](arkts-apis-webview-i.md#webcustomscheme)> | 是 | 自定义协议配置，最多支持同时配置10个自定义协议。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100020 | Failed to register custom schemes. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. responseWeb: WebResourceResponse = new WebResourceResponse();
10. scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
11. scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
12. scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

14. aboutToAppear(): void {
15. try {
16. webview.WebviewController.customizeSchemes([this.scheme1, this.scheme2, this.scheme3]);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. }

22. build() {
23. Column() {
24. Web({ src: 'www.example.com', controller: this.controller })
25. .onInterceptRequest((event) => {
26. if (event) {
27. console.info('url:' + event.request.getRequestUrl());
28. }
29. return this.responseWeb;
30. })
31. }
32. }
33. }
```

## customizeSchemes21+

PhonePC/2in1TabletTVWearable

static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void

对Web内核赋予自定义协议url的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议url时，该fetch请求可被[onInterceptRequest](arkts-basic-components-web-events.md#oninterceptrequest9)事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| schemes | Array<[WebCustomScheme](arkts-apis-webview-i.md#webcustomscheme)> | 是 | 自定义协议配置，最多支持同时配置10个自定义协议。 |
| lazyInitWebEngine | boolean | 是 | 表示接口内部是否跳过初始化WebEngine。  true表示接口内部跳过初始化WebEngine，并将注册的Schemes暂存，当它真正初始化时，这些Schemes将传递给WebEngine。false表示接口内部自动进行WebEngine初始化。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. The length of the schemes array is greater than 10. 2. The character length of the scheme is greater than 32. 3. The character in the scheme is not within the allowed range of lowercase English letters, numbers, and the symbols ".", "+", "-". |
| 17100020 | Failed to register custom schemes. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. responseWeb: WebResourceResponse = new WebResourceResponse();
10. scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
11. scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
12. scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

14. aboutToAppear(): void {
15. try {
16. webview.WebviewController.customizeSchemes([this.scheme1, this.scheme2, this.scheme3], true);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. }

22. build() {
23. Column() {
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## getCertificate10+

PhonePC/2in1TabletTVWearable

getCertificate(): Promise<Array<cert.X509Cert>>

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过Promise异步返回当前网站的X509格式证书（X509Cert证书类型定义见[X509Cert](js-apis-cert.md#x509cert)定义），便于开发者展示网站证书信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<cert.X509Cert>> | Promise实例，用于获取当前加载的https网站的X509格式证书数组。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { cert } from '@kit.DeviceCertificateKit';

6. function Uint8ArrayToString(dataArray: Uint8Array) {
7. let dataString = '';
8. for (let i = 0; i < dataArray.length; i++) {
9. dataString += String.fromCharCode(dataArray[i]);
10. }
11. return dataString;
12. }

14. function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
15. let res: string = 'getCertificate success: len = ' + x509CertArray.length;
16. for (let i = 0; i < x509CertArray.length; i++) {
17. res += ', index = ' + i + ', issuer name = '
18. + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
19. + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
20. + x509CertArray[i].getNotBeforeTime()
21. + ', valid end = ' + x509CertArray[i].getNotAfterTime();
22. }
23. return res;
24. }

26. @Entry
27. @Component
28. struct Index {
29. // outputStr在UI界面显示调试信息
30. @State outputStr: string = '';
31. webviewCtl: webview.WebviewController = new webview.WebviewController();

33. build() {
34. Row() {
35. Column() {
36. List({ space: 20, initialIndex: 0 }) {
37. ListItem() {
38. Button() {
39. Text('load bad ssl')
40. .fontSize(10)
41. .fontWeight(FontWeight.Bold)
42. }
43. .type(ButtonType.Capsule)
44. .onClick(() => {
45. // 加载一个过期的证书网站，查看获取到的证书信息
46. this.webviewCtl.loadUrl('https://expired.badssl.com');
47. })
48. .height(50)
49. }

51. ListItem() {
52. Button() {
53. Text('load example')
54. .fontSize(10)
55. .fontWeight(FontWeight.Bold)
56. }
57. .type(ButtonType.Capsule)
58. .onClick(() => {
59. // 加载一个https网站，查看网站的证书信息
60. this.webviewCtl.loadUrl('https://www.example.com');
61. })
62. .height(50)
63. }

65. ListItem() {
66. Button() {
67. Text('getCertificate Promise')
68. .fontSize(10)
69. .fontWeight(FontWeight.Bold)
70. }
71. .type(ButtonType.Capsule)
72. .onClick(() => {
73. try {
74. this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
75. this.outputStr = ParseX509CertInfo(x509CertArray);
76. })
77. } catch (error) {
78. this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
79. }
80. })
81. .height(50)
82. }

84. ListItem() {
85. Button() {
86. Text('getCertificate AsyncCallback')
87. .fontSize(10)
88. .fontWeight(FontWeight.Bold)
89. }
90. .type(ButtonType.Capsule)
91. .onClick(() => {
92. try {
93. this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
94. if (error) {
95. this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
96. } else {
97. this.outputStr = ParseX509CertInfo(x509CertArray);
98. }
99. })
100. } catch (error) {
101. this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
102. }
103. })
104. .height(50)
105. }
106. }
107. .listDirection(Axis.Horizontal)
108. .height('10%')

110. Text(this.outputStr)
111. .width('100%')
112. .fontSize(10)

114. Web({ src: 'https://www.example.com', controller: this.webviewCtl })
115. .fileAccess(true)
116. .javaScriptAccess(true)
117. .domStorageAccess(true)
118. .onlineImageAccess(true)
119. .onPageEnd((e) => {
120. if (e) {
121. this.outputStr = 'onPageEnd : url = ' + e.url;
122. }
123. })
124. .onSslErrorEventReceive((e) => {
125. // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com
126. e.handler.handleConfirm();
127. })
128. .width('100%')
129. .height('70%')
130. }
131. .height('100%')
132. }
133. }
134. }
```

## getCertificate10+

PhonePC/2in1TabletTVWearable

getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过AsyncCallback异步返回当前网站的X509格式证书（X509Cert证书类型定义见[X509Cert定义](js-apis-cert.md)），便于开发者展示网站证书信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<cert.X509Cert>> | 是 | 通过AsyncCallback异步返回当前网站的X509格式证书。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { cert } from '@kit.DeviceCertificateKit';

6. function Uint8ArrayToString(dataArray: Uint8Array) {
7. let dataString = '';
8. for (let i = 0; i < dataArray.length; i++) {
9. dataString += String.fromCharCode(dataArray[i]);
10. }
11. return dataString;
12. }

14. function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
15. let res: string = 'getCertificate success: len = ' + x509CertArray.length;
16. for (let i = 0; i < x509CertArray.length; i++) {
17. res += ', index = ' + i + ', issuer name = '
18. + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
19. + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
20. + x509CertArray[i].getNotBeforeTime()
21. + ', valid end = ' + x509CertArray[i].getNotAfterTime();
22. }
23. return res;
24. }

26. @Entry
27. @Component
28. struct Index {
29. // outputStr在UI界面显示调试信息
30. @State outputStr: string = '';
31. webviewCtl: webview.WebviewController = new webview.WebviewController();

33. build() {
34. Row() {
35. Column() {
36. List({ space: 20, initialIndex: 0 }) {
37. ListItem() {
38. Button() {
39. Text('load bad ssl')
40. .fontSize(10)
41. .fontWeight(FontWeight.Bold)
42. }
43. .type(ButtonType.Capsule)
44. .onClick(() => {
45. // 加载一个过期的证书网站，查看获取到的证书信息
46. this.webviewCtl.loadUrl('https://expired.badssl.com');
47. })
48. .height(50)
49. }

51. ListItem() {
52. Button() {
53. Text('load example')
54. .fontSize(10)
55. .fontWeight(FontWeight.Bold)
56. }
57. .type(ButtonType.Capsule)
58. .onClick(() => {
59. // 加载一个https网站，查看网站的证书信息
60. this.webviewCtl.loadUrl('https://www.example.com');
61. })
62. .height(50)
63. }

65. ListItem() {
66. Button() {
67. Text('getCertificate Promise')
68. .fontSize(10)
69. .fontWeight(FontWeight.Bold)
70. }
71. .type(ButtonType.Capsule)
72. .onClick(() => {
73. try {
74. this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
75. this.outputStr = ParseX509CertInfo(x509CertArray);
76. })
77. } catch (error) {
78. this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
79. }
80. })
81. .height(50)
82. }

84. ListItem() {
85. Button() {
86. Text('getCertificate AsyncCallback')
87. .fontSize(10)
88. .fontWeight(FontWeight.Bold)
89. }
90. .type(ButtonType.Capsule)
91. .onClick(() => {
92. try {
93. this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
94. if (error) {
95. this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
96. } else {
97. this.outputStr = ParseX509CertInfo(x509CertArray);
98. }
99. })
100. } catch (error) {
101. this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
102. }
103. })
104. .height(50)
105. }
106. }
107. .listDirection(Axis.Horizontal)
108. .height('10%')

110. Text(this.outputStr)
111. .width('100%')
112. .fontSize(10)

114. Web({ src: 'https://www.example.com', controller: this.webviewCtl })
115. .fileAccess(true)
116. .javaScriptAccess(true)
117. .domStorageAccess(true)
118. .onlineImageAccess(true)
119. .onPageEnd((e) => {
120. if (e) {
121. this.outputStr = 'onPageEnd : url = ' + e.url;
122. }
123. })
124. .onSslErrorEventReceive((e) => {
125. // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com
126. e.handler.handleConfirm();
127. })
128. .width('100%')
129. .height('70%')
130. }
131. .height('100%')
132. }
133. }
134. }
```

## setAudioMuted10+

PhonePC/2in1TabletTVWearable

setAudioMuted(mute: boolean): void

设置网页静音。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 表示是否将网页设置为静音状态。  true表示将网页设置为静音状态，false表示将网页取消静音状态。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State muted: boolean = false;

10. build() {
11. Column() {
12. Button("Toggle Mute")
13. .onClick(event => {
14. if (event) {
15. this.muted = !this.muted;
16. this.controller.setAudioMuted(this.muted);
17. }
18. })
19. Web({ src: 'www.example.com', controller: this.controller })
20. }
21. }
22. }
```

## prefetchPage21+

PhonePC/2in1TabletTVWearable

prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void

在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度。

说明

* 下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。
* prefetchPage对302重定向页面同样正常预取。
* 先执行prefetchPage再加载页面时，已预取的资源将直接从缓存中加载。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 预加载的url。 |
| additionalHeaders | Array<[WebHeader](arkts-apis-webview-i.md#webheader)> | 否 | url的附加HTTP请求头。  默认值： [] |
| prefetchOptions | [PrefetchOptions](arkts-apis-webview-prefetchoptions.md) | 否 | 用来自定义预取行为的相关选项。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Button('prefetchPopularPage')
11. .onClick(() => {
12. try {
13. // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
14. let options = new webview.PrefetchOptions();
15. options.ignoreCacheControlNoStore = true;
16. options.minTimeBetweenPrefetchesMs = 100;
17. this.controller.prefetchPage('https://www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }], options);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. // 需要将'www.example1.com'替换成一个真实的网站地址。
23. Web({ src: 'www.example1.com', controller: this.controller })
24. }
25. }
26. }
```

## prefetchPage10+

PhonePC/2in1TabletTVWearable

prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void

在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度。

说明

* 下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。
* prefetchPage对302重定向页面同样正常预取。
* 先执行prefetchPage再加载页面时，已预取的资源将直接从缓存中加载。
* 连续prefetchPage多个url只有第一个生效。
* prefetchPage有时间限制，500ms内不能多次预取。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 预加载的url。 |
| additionalHeaders | Array<[WebHeader](arkts-apis-webview-i.md#webheader)> | 否 | url的附加HTTP请求头。  默认值： [] |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

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
12. Button('prefetchPopularPage')
13. .onClick(() => {
14. try {
15. // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
16. this.controller.prefetchPage('https://www.example.com');
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. // 需要将'www.example1.com'替换成一个真实的网站地址。
22. Web({ src: 'www.example1.com', controller: this.controller })
23. }
24. }
25. }
```

## prefetchResource12+

PhonePC/2in1TabletTVWearable

static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void

根据指定的请求信息和附加的http请求头去预获取资源请求，存入内存缓存，并指定其缓存key和有效期，以加快加载速度。目前仅支持Content-Type为application/x-www-form-urlencoded的post请求。最多可以预获取6个post请求。如果要预获取第7个，请通过[clearPrefetchedResource](arkts-apis-webview-webviewcontroller.md#clearprefetchedresource12)清除不需要的post请求缓存，否则会自动清除最早预获取的post缓存。如果要使用预获取的资源缓存，开发者需要在正式发起的post请求的请求头中增加键值“ArkWebPostCacheKey”，其内容为对应缓存的cacheKey。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [RequestInfo](arkts-apis-webview-i.md#requestinfo12) | 是 | 预获取请求的信息。 |
| additionalHeaders | Array<[WebHeader](arkts-apis-webview-i.md#webheader)> | 否 | 预获取请求的附加HTTP请求头。  传入undefined或null会抛出异常错误码401。 |
| cacheKey | string | 否 | 用于后续查询预获取资源缓存的key。仅支持字母和数字，未传入或传入空则取默认值url作为key。  传入undefined或null会抛出异常错误码401。 |
| cacheValidTime | number | 否 | 预获取资源缓存的有效期。  取值范围：(0, 2147483647]。  默认值：300s。  单位：s。  传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**示例：**

```
1. // EntryAbility.ets
2. import { webview } from '@kit.ArkWeb';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate");
8. webview.WebviewController.initializeWebEngine();
9. // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
10. webview.WebviewController.prefetchResource(
11. {
12. url: "https://www.example1.com/post?e=f&g=h",
13. method: "POST",
14. formData: "a=x&b=y",
15. },
16. [{
17. headerKey: "c",
18. headerValue: "z",
19. },],
20. "KeyX", 500);
21. AppStorage.setOrCreate("abilityWant", want);
22. console.info("EntryAbility onCreate done");
23. }
24. }
```

## clearPrefetchedResource12+

PhonePC/2in1TabletTVWearable

static clearPrefetchedResource(cacheKeyList: Array<string>): void

根据指定的缓存key列表清除对应的预获取资源缓存。入参中的缓存key必须是[prefetchResource](arkts-apis-webview-webviewcontroller.md#prefetchresource12)指定预获取到的资源缓存key。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cacheKeyList | Array<string> | 是 | 用于后续查询预获取资源缓存的key。仅支持字母和数字，未传入或传入空则取默认值url作为key。 |

**示例：**

```
1. // Index.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: "https://www.example.com/", controller: this.controller })
12. .onAppear(() => {
13. // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
14. webview.WebviewController.prefetchResource(
15. {
16. url: "https://www.example1.com/post?e=f&g=h",
17. method: "POST",
18. formData: "a=x&b=y",
19. },
20. [{
21. headerKey: "c",
22. headerValue: "z",
23. },],
24. "KeyX", 500);
25. })
26. .onPageEnd(() => {
27. // 清除后续不再使用的预获取缓存。
28. webview.WebviewController.clearPrefetchedResource(["KeyX",]);
29. })
30. }
31. }
32. }
```

## prepareForPageLoad10+

PhonePC/2in1TabletTVWearable

static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void

预连接url，在加载url之前调用此API，对url只进行DNS解析，socket建链操作，并不获取主资源子资源。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 预连接的url。 |
| preconnectable | boolean | 是 | 是否进行预连接。如果preconnectable为true，则对url进行DNS解析，socket建链预连接；如果preconnectable为false，则不做任何预连接操作。 |
| numSockets | number | 是 | 要预连接的socket数。socket数目连接需要大于0，最多允许6个连接。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |
| 17100013 | The number of preconnect sockets is invalid. |

**示例：**

```
1. // EntryAbility.ets
2. import { webview } from '@kit.ArkWeb';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate");
8. webview.WebviewController.initializeWebEngine();
9. // 预连接时，需要將'https://www.example.com'替换成一个真实的网站地址。
10. webview.WebviewController.prepareForPageLoad("https://www.example.com", true, 2);
11. AppStorage.setOrCreate("abilityWant", want);
12. console.info("EntryAbility onCreate done");
13. }
14. }
```

## setCustomUserAgent10+

PhonePC/2in1TabletTVWearable

setCustomUserAgent(userAgent: string): void

设置自定义用户代理，会覆盖系统的用户代理。

当Web组件src设置了url时，建议在onControllerAttached回调事件中设置User-Agent，设置方式请参考示例。不建议将User-Agent设置在onLoadIntercept回调事件中，会概率性出现设置失败。

当Web组件src设置为空字符串时，建议先调用setCustomUserAgent方法设置User-Agent，再通过loadUrl加载具体页面。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)

说明

当Web组件src设置了url，且未在onControllerAttached回调事件中设置User-Agent。再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 用户自定义代理信息。建议先使用[getUserAgent](arkts-apis-webview-webviewcontroller.md#getuseragent)获取当前默认用户代理，在此基础上追加自定义用户代理信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State customUserAgent: string = ' DemoApp';

11. build() {
12. Column() {
13. Web({ src: 'www.example.com', controller: this.controller })
14. .onControllerAttached(() => {
15. console.info("onControllerAttached");
16. try {
17. let userAgent = this.controller.getUserAgent() + this.customUserAgent;
18. this.controller.setCustomUserAgent(userAgent);
19. } catch (error) {
20. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
21. }
22. })
23. }
24. }
25. }
```

## setDownloadDelegate11+

PhonePC/2in1TabletTVWearable

setDownloadDelegate(delegate: WebDownloadDelegate): void

为当前的Web组件设置一个WebDownloadDelegate，该delegate用来接收页面内触发的下载进度的委托。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-apis-webview-webdownloaddelegate.md) | 是 | 用来接收下载进度的委托。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.controller.setDownloadDelegate(this.delegate);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## startDownload11+

PhonePC/2in1TabletTVWearable

startDownload(url: string): void

使用Web组件的下载能力来下载指定的url, 比如下载网页中指定的图片。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 下载地址。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.controller.setDownloadDelegate(this.delegate);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Button('startDownload')
22. .onClick(() => {
23. try {
24. this.controller.startDownload('https://www.example.com');
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. })
29. Web({ src: 'www.example.com', controller: this.controller })
30. }
31. }
32. }
```

## getCustomUserAgent10+

PhonePC/2in1TabletTVWearable

getCustomUserAgent(): string

获取自定义用户代理。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用户自定义代理信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State userAgent: string = '';

11. build() {
12. Column() {
13. Button('getCustomUserAgent')
14. .onClick(() => {
15. try {
16. this.userAgent = this.controller.getCustomUserAgent();
17. console.info("userAgent: " + this.userAgent);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## setAppCustomUserAgent20+

PhonePC/2in1TabletTVWearable

static setAppCustomUserAgent(userAgent: string): void

设置应用级自定义用户代理，会覆盖系统的用户代理，应用内所有Web组件生效。

当需要设置应用级自定义用户代理时，建议在Web组件创建前调用setAppCustomUserAgent方法设置User-Agent，再创建指定src的Web组件或通过[loadUrl](arkts-apis-webview-webviewcontroller.md#loadurl)加载具体页面。

默认User-Agent定义与使用场景，及相关User-Agent接口定义优先级请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 用户自定义代理信息。建议先使用[getDefaultUserAgent](arkts-apis-webview-webviewcontroller.md#getdefaultuseragent14)获取当前默认用户代理，在此基础上追加自定义用户代理信息。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. aboutToAppear(): void {
11. try {
12. webview.WebviewController.initializeWebEngine();
13. let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
14. let appUA = defaultUserAgent + " appUA";
15. webview.WebviewController.setAppCustomUserAgent(appUA);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. }

21. build() {
22. Column() {
23. Web({ src: 'www.example.com', controller: this.controller })
24. }
25. }
26. }
```

## setUserAgentForHosts20+

PhonePC/2in1TabletTVWearable

static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void

针对特定网站设置自定义用户代理，会覆盖系统的用户代理，应用内所有Web组件生效。

当需要对特定网站设置自定义用户代理时，建议在Web组件创建前调用setUserAgentForHosts方法设置User-Agent，再创建指定src的Web组件或通过[loadUrl](arkts-apis-webview-webviewcontroller.md#loadurl)加载具体页面。

默认User-Agent定义与使用场景，及相关User-Agent接口定义优先级请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 用户自定义代理信息。建议先使用[getDefaultUserAgent](arkts-apis-webview-webviewcontroller.md#getdefaultuseragent14)获取当前默认用户代理，在此基础上追加自定义用户代理信息。 |
| hosts | Array<string> | 是 | 用户自定义代理的相关域名列表，每次调用时仅保留最新传入的列表，并限制最大条目数为两万，超出部分自动截断。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. aboutToAppear(): void {
11. try {
12. webview.WebviewController.initializeWebEngine();
13. let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
14. let appUA = defaultUserAgent + " appUA";
15. webview.WebviewController.setUserAgentForHosts(
16. appUA,
17. [
18. "www.example.com",
19. "www.baidu.com"
20. ]
21. );
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. }

27. build() {
28. Column() {
29. Web({ src: 'www.example.com', controller: this.controller })
30. }
31. }
32. }
```

## setConnectionTimeout11+

PhonePC/2in1TabletTVWearable

static setConnectionTimeout(timeout: number): void

设置网络连接超时时间，使用者可通过Web组件中的onErrorReceive方法获取超时错误码。若未调用该接口则默认超时时间为30秒。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | socket连接超时时间，以秒为单位，必须为大于0的整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

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
12. Button('setConnectionTimeout')
13. .onClick(() => {
14. try {
15. webview.WebviewController.setConnectionTimeout(5);
16. console.info("setConnectionTimeout: 5s");
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. .onErrorReceive((event) => {
23. if (event) {
24. console.info('getErrorInfo:' + event.error.getErrorInfo());
25. console.info('getErrorCode:' + event.error.getErrorCode());
26. }
27. })
28. }
29. }
30. }
```

## warmupServiceWorker12+

PhonePC/2in1TabletTVWearable

static warmupServiceWorker(url: string): void

预热ServiceWorker，以提升首屏页面的加载速度（仅限于会使用ServiceWorker的页面）。在加载url之前调用此API。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 需要预热ServiceWorker的url。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**示例：**

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';
5. import { webview } from '@kit.ArkWeb';

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
9. console.info("EntryAbility onCreate");
10. webview.WebviewController.initializeWebEngine();
11. webview.WebviewController.warmupServiceWorker("https://www.example.com");
12. AppStorage.setOrCreate("abilityWant", want);
13. }
14. }
```

## enableSafeBrowsing11+

PhonePC/2in1TabletTVWearable

enableSafeBrowsing(enable: boolean): void

启用检查网站安全风险的功能，非法和欺诈网站是强制启用的，不能通过此功能禁用。

本功能默认不生效，HarmonyOS只提供恶意网址拦截页WebUI，网址风险检测以及显示WebUI的功能由Vendor实现。推荐在WebContentsObserver中监听跳转[DidStartNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h)、[DidRedirectNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h)进行检测。

说明

该接口不生效，调用不会产生任何实际效果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用检查网站安全风险的功能。  true表示启用检查网站安全风险的功能，false表示不启用检查网站安全风险的功能。  默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('enableSafeBrowsing')
13. .onClick(() => {
14. try {
15. this.controller.enableSafeBrowsing(true);
16. console.info("enableSafeBrowsing: true");
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## isSafeBrowsingEnabled11+

PhonePC/2in1TabletTVWearable

isSafeBrowsingEnabled(): boolean

获取当前网页是否启用了检查网站安全风险。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前网页是否启用了检查网站安全风险的功能。  true表示启用了检查网站安全风险的功能，false表示未启用检查网站安全风险的功能。  默认值：false。 |

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
11. Button('isSafeBrowsingEnabled')
12. .onClick(() => {
13. let result = this.controller.isSafeBrowsingEnabled();
14. console.info("result: " + result);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```

## enableIntelligentTrackingPrevention12+

PhonePC/2in1TabletTVWearable

enableIntelligentTrackingPrevention(enable: boolean): void

启用智能防跟踪功能。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用智能防跟踪功能。  true表示启用智能防跟踪功能，false表示不启用智能防跟踪功能。  默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

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
12. Button('enableIntelligentTrackingPrevention')
13. .onClick(() => {
14. try {
15. this.controller.enableIntelligentTrackingPrevention(true);
16. console.info("enableIntelligentTrackingPrevention: true");
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## isIntelligentTrackingPreventionEnabled12+

PhonePC/2in1TabletTVWearable

isIntelligentTrackingPreventionEnabled(): boolean

获取当前Web是否启用了智能防跟踪功能。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前Web是否启用了智能防跟踪功能。  true表示启用了智能防跟踪功能，false表示未启用智能防跟踪功能。  默认值：false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 801 | Capability not supported. |

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
12. Button('isIntelligentTrackingPreventionEnabled')
13. .onClick(() => {
14. try {
15. let result = this.controller.isIntelligentTrackingPreventionEnabled();
16. console.info("result: " + result);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## addIntelligentTrackingPreventionBypassingList12+

PhonePC/2in1TabletTVWearable

static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void

添加智能防跟踪功能绕过的域名列表。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostList | Array<string> | 是 | 绕过智能防跟踪功能的域名列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

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
12. Button('addIntelligentTrackingPreventionBypassingList')
13. .onClick(() => {
14. try {
15. let hostList = ["www.test1.com", "www.test2.com", "www.test3.com"];
16. webview.WebviewController.addIntelligentTrackingPreventionBypassingList(hostList);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## removeIntelligentTrackingPreventionBypassingList12+

PhonePC/2in1TabletTVWearable

static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void

删除通过addIntelligentTrackingPreventionBypassingList接口添加的部分域名列表。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostList | Array<string> | 是 | 绕过智能防跟踪功能的域名列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

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
12. Button('removeIntelligentTrackingPreventionBypassingList')
13. .onClick(() => {
14. try {
15. let hostList = ["www.test1.com", "www.test2.com"];
16. webview.WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## clearIntelligentTrackingPreventionBypassingList12+

PhonePC/2in1TabletTVWearable

static clearIntelligentTrackingPreventionBypassingList(): void

删除通过addIntelligentTrackingPreventionBypassingList接口添加的所有域名。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用。从API version 18开始，在其他设备类型中返回801错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

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
11. Button('clearIntelligentTrackingPreventionBypassingList')
12. .onClick(() => {
13. webview.WebviewController.clearIntelligentTrackingPreventionBypassingList();
14. })
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```

## getDefaultUserAgent14+

PhonePC/2in1TabletTVWearable

static getDefaultUserAgent(): string

获取默认用户代理。

此接口只允许在UI线程调用。

默认User-Agent定义与使用场景请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | ArkWeb默认User-Agent字符串。 |

**示例：**

```
1. // EntryAbility.ets
2. import { webview } from '@kit.ArkWeb';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate");
8. webview.WebviewController.initializeWebEngine();
9. let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
10. console.info("defaultUserAgent: " + defaultUserAgent);
11. }
12. }
```

## enableAdsBlock12+

PhonePC/2in1TabletTVWearable

enableAdsBlock(enable: boolean): void

启用广告过滤功能。

说明

* 广告过滤功能需要release包，使用debug包不生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用广告过滤功能。  true表示启用广告过滤功能，false表示取消广告过滤功能。  默认值：false。 |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |
| 801 | Capability not supported. |

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
12. Button('enableAdsBlock')
13. .onClick(() => {
14. try {
15. this.controller.enableAdsBlock(true);
16. console.info("enableAdsBlock: true")
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## isAdsBlockEnabled12+

PhonePC/2in1TabletTVWearable

isAdsBlockEnabled() : boolean

查询广告过滤功能是否开启。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true代表广告过滤功能已开启，返回false代表广告过滤功能关闭。  默认值：false。 |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

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
12. Button('isAdsBlockEnabled')
13. .onClick(() => {
14. try {
15. let isAdsBlockEnabled: boolean = this.controller.isAdsBlockEnabled();
16. console.info("isAdsBlockEnabled:", isAdsBlockEnabled);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## isAdsBlockEnabledForCurPage12+

PhonePC/2in1TabletTVWearable

isAdsBlockEnabledForCurPage() : boolean

查询当前网页是否开启广告过滤功能。

当Web组件使能广告过滤功能后，默认所有页面都是开启广告过滤的，支持通过[addAdsBlockDisallowedList](arkts-apis-webview-adsblockmanager.md#addadsblockdisallowedlist12)指定域名禁用广告过滤。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true代表此网页已开启广告过滤，返回false代表当前网页已关闭广告过滤。 |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

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
12. Button('isAdsBlockEnabledForCurPage')
13. .onClick(() => {
14. try {
15. let isAdsBlockEnabledForCurPage: boolean = this.controller.isAdsBlockEnabledForCurPage();
16. console.info("isAdsBlockEnabledForCurPage:", isAdsBlockEnabledForCurPage);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## setRenderProcessMode12+

PhonePC/2in1TabletTVWearable

static setRenderProcessMode(mode: RenderProcessMode): void

设置ArkWeb渲染子进程模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [RenderProcessMode](arkts-apis-webview-e.md#renderprocessmode12) | 是 | 渲染子进程模式。  可以先调用[getRenderProcessMode()](arkts-apis-webview-webviewcontroller.md#getrenderprocessmode12)查看当前设备的ArkWeb渲染子进程模式，枚举值0为单子进程模式，枚举值1为多子进程模式。  手机默认为单渲染子进程模式，平板和PC/2in1默认为多渲染子进程模式。  如果传入RenderProcessMode枚举值之外的非法数字，则默认识别为多渲染子进程模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('setRenderProcessMode')
13. .onClick(() => {
14. try {
15. webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## getRenderProcessMode12+

PhonePC/2in1TabletTVWearable

static getRenderProcessMode(): RenderProcessMode

查询ArkWeb的渲染子进程模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderProcessMode](arkts-apis-webview-e.md#renderprocessmode12) | 渲染子进程模式类型。  调用getRenderProcessMode()获取当前设备的ArkWeb渲染子进程模式，枚举值0为单子进程模式，枚举值1为多子进程模式。  如果获取的值不在RenderProcessMode枚举值范围内，则默认为多渲染子进程模式。 |

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
11. Button('getRenderProcessMode')
12. .onClick(() => {
13. let mode = webview.WebviewController.getRenderProcessMode();
14. console.info("getRenderProcessMode: " + mode);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```

## terminateRenderProcess12+

PhonePC/2in1TabletTVWearable

terminateRenderProcess(): boolean

销毁渲染进程。

调用该接口将会主动销毁相关联的渲染进程。如果渲染进程尚未启动，或者已销毁则没有任何影响。此外销毁渲染进程会同时影响所有与该渲染进程关联的其他实例。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回销毁渲染进程的结果。  返回true表示渲染进程可以被销毁或已被销毁，返回false表示渲染进程不可以被销毁。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
11. Button('terminateRenderProcess')
12. .onClick(() => {
13. let result = this.controller.terminateRenderProcess();
14. console.info("terminateRenderProcess result: " + result);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```

## postUrl11+

PhonePC/2in1TabletTVWearable

postUrl(url: string, postData: ArrayBuffer): void

使用"POST"方法加载带有postData的url。如果url不是网络url，则会使用[loadUrl](arkts-apis-webview-webviewcontroller.md#loadurl)方法加载url，忽略postData参数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 需要加载的 URL。 |
| postData | ArrayBuffer | 是 | 使用"POST"方法传递数据。 该请求必须采用"application/x-www-form-urlencoded"编码。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestObj {
6. constructor() {
7. }

9. test(str: string): ArrayBuffer {
10. let buf = new ArrayBuffer(str.length);
11. let buff = new Uint8Array(buf);

13. for (let i = 0; i < str.length; i++) {
14. buff[i] = str.charCodeAt(i);
15. }
16. return buf;
17. }
18. }

20. @Entry
21. @Component
22. struct WebComponent {
23. controller: webview.WebviewController = new webview.WebviewController();
24. @State testObjtest: TestObj = new TestObj();

26. build() {
27. Column() {
28. Button('postUrl')
29. .onClick(() => {
30. try {
31. // 数据转化为ArrayBuffer类型。
32. let postData = this.testObjtest.test("Name=test&Password=test");
33. this.controller.postUrl('www.example.com', postData);
34. } catch (error) {
35. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
36. }
37. })
38. Web({ src: '', controller: this.controller })
39. }
40. }
41. }
```

## createWebPrintDocumentAdapter11+

PhonePC/2in1TabletTVWearable

createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter

创建web相关打印功能。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobName | string | 是 | 需要打印的文件名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| print.[PrintDocumentAdapter](js-apis-print.md#printdocumentadapter11) | 返回打印文档的适配器。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError, print } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Button('createWebPrintDocumentAdapter')
13. .onClick(() => {
14. try {
15. let webPrintDocadapter = this.controller.createWebPrintDocumentAdapter('example.pdf');
16. print.print('example_jobid', webPrintDocadapter, null, this.getUIContext().getHostContext());
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## isIncognitoMode11+

PhonePC/2in1TabletTVWearable

isIncognitoMode(): boolean

查询当前是否是隐私模式的Webview。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否是隐私模式的Webview。  true表示是隐私模式，false表示不是隐私模式。  默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('isIncognitoMode')
13. .onClick(() => {
14. try {
15. let result = this.controller.isIncognitoMode();
16. console.info('isIncognitoMode' + result);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## getSecurityLevel11+

PhonePC/2in1TabletTVWearable

getSecurityLevel(): SecurityLevel

获取当前网页的安全级别。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SecurityLevel](arkts-apis-webview-e.md#securitylevel11) | 当前网页的安全级别，具体值为NONE、SECURE、WARNING、DANGEROUS。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .onPageEnd((event) => {
12. if (event) {
13. let securityLevel = this.controller.getSecurityLevel();
14. console.info('securityLevel: ', securityLevel);
15. }
16. })
17. }
18. }
19. }
```

## setScrollable12+

PhonePC/2in1TabletTVWearable

setScrollable(enable: boolean, type?: ScrollType): void

设置网页是否允许滚动。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否将网页设置为允许滚动。  true表示设置为允许滚动，false表示禁止滚动。  默认值：true。 |
| type | [ScrollType](arkts-apis-webview-e.md#scrolltype12) | 否 | 网页可触发的滚动类型，支持缺省配置。  - enable为false时，表示禁止ScrollType类型的滚动，当ScrollType缺省时表示禁止所有类型网页滚动。  - enable为true时，ScrollType缺省与否，都表示允许所有类型的网页滚动。  传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('setScrollable')
13. .onClick(() => {
14. try {
15. this.controller.setScrollable(true);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## getScrollable12+

PhonePC/2in1TabletTVWearable

getScrollable(): boolean

获取当前网页是否允许滚动。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前网页是否允许滚动。  true为允许滚动，false为禁止滚动。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getScrollable')
13. .onClick(() => {
14. try {
15. let scrollEnabled = this.controller.getScrollable();
16. console.info("scrollEnabled: " + scrollEnabled);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## setPrintBackground12+

PhonePC/2in1TabletTVWearable

setPrintBackground(enable: boolean): void

设置是否打印网页背景，该接口与[PrintAttributes](js-apis-print.md#printattributes11)打印参数配置不一致时，本接口设置优先级高于打印参数。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否打印网页背景。  true表示设置为打印网页背景，false表示取消网页背景打印。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('setPrintBackground')
12. .onClick(() => {
13. try {
14. this.controller.setPrintBackground(false);
15. } catch (error) {
16. console.error(`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
17. }
18. })
19. Web({ src: 'www.example.com', controller: this.controller })
20. }
21. }
22. }
```

## getPrintBackground12+

PhonePC/2in1TabletTVWearable

getPrintBackground(): boolean

查询webview是否打印网页背景。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回webview是否打印网页背景。  true:打印网页背景；false:不打印网页背景。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('setPrintBackground')
12. .onClick(() => {
13. try {
14. let enable = this.controller.getPrintBackground();
15. console.info("getPrintBackground: " + enable);
16. } catch (error) {
17. console.error(`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## getLastJavascriptProxyCallingFrameUrl12+

PhonePC/2in1TabletTVWearable

getLastJavascriptProxyCallingFrameUrl(): string

通过[registerJavaScriptProxy](arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)或者[javaScriptProxy](arkts-basic-components-web-attributes.md#javascriptproxy)注入JavaScript对象到window对象中。该接口可以获取最后一次调用注入的对象的frame的url。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 最后一次调用注入的对象的frame的url。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestObj {
6. mycontroller: webview.WebviewController;

8. constructor(controller: webview.WebviewController) {
9. this.mycontroller = controller;
10. }

12. test(testStr: string): string {
13. console.info('Web Component str' + testStr + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
14. return testStr;
15. }

17. toString(): void {
18. console.info('Web Component toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
19. }

21. testNumber(testNum: number): number {
22. console.info('Web Component number' + testNum + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
23. return testNum;
24. }

26. testBool(testBol: boolean): boolean {
27. console.info('Web Component boolean' + testBol + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
28. return testBol;
29. }
30. }

32. class WebObj {
33. mycontroller: webview.WebviewController;

35. constructor(controller: webview.WebviewController) {
36. this.mycontroller = controller;
37. }

39. webTest(): string {
40. console.info('Web test ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
41. return "Web test";
42. }

44. webString(): void {
45. console.info('Web test toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
46. }
47. }

49. @Entry
50. @Component
51. struct Index {
52. controller: webview.WebviewController = new webview.WebviewController();
53. @State testObjtest: TestObj = new TestObj(this.controller);
54. @State webTestObj: WebObj = new WebObj(this.controller);

56. build() {
57. Column() {
58. Button('refresh')
59. .onClick(() => {
60. try {
61. this.controller.refresh();
62. } catch (error) {
63. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
64. }
65. })
66. Button('Register JavaScript To Window')
67. .onClick(() => {
68. try {
69. this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber", "testBool"]);
70. this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
71. } catch (error) {
72. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
73. }
74. })
75. Button('deleteJavaScriptRegister')
76. .onClick(() => {
77. try {
78. this.controller.deleteJavaScriptRegister("objName");
79. this.controller.deleteJavaScriptRegister("objTestName");
80. } catch (error) {
81. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
82. }
83. })
84. Web({ src: $rawfile('index.html'), controller: this.controller })
85. .javaScriptAccess(true)
86. }
87. }
88. }
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
8. <button type="button" onclick="htmlTest()">Click Me!</button>
9. <p id="demo"></p>
10. <p id="webDemo"></p>
11. <script type="text/javascript">
12. function htmlTest() {
13. // This function call expects to return "ArkUI Web Component"
14. let str=objName.test("webtest data");
15. objName.testNumber(1);
16. objName.testBool(true);
17. document.getElementById("demo").innerHTML=str;
18. console.info('objName.test result:'+ str)

20. // This function call expects to return "Web test"
21. let webStr = objTestName.webTest();
22. document.getElementById("webDemo").innerHTML=webStr;
23. console.info('objTestName.webTest result:'+ webStr)
24. }
25. </script>
26. </body>
27. </html>
```

## pauseAllTimers12+

PhonePC/2in1TabletTVWearable

static pauseAllTimers(): void

暂停所有WebView的定时器。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Row() {
11. Button('PauseAllTimers')
12. .onClick(() => {
13. webview.WebviewController.pauseAllTimers();
14. })
15. }
16. Web({ src: $rawfile("index.html"), controller: this.controller })
17. }
18. }
19. }
```

加载的html文件。

```
1. <!DOCTYPE html>
2. <html>
3. <body>
4. <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
5. <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
6. <input style="width:300px;height:150px;font-size:50px" value="0" id="show_num">
7. </body>
8. </html>
9. <script>
10. var timer = null;
11. var num = 0;

13. function startTimer() {
14. timer = setInterval(function() {
15. document.getElementById("show_num").value = ++num;
16. }, 1000);
17. }

19. function resetTimer() {
20. clearInterval(timer);
21. document.getElementById("show_num").value = 0;
22. num = 0;
23. }
24. </script>
```

## resumeAllTimers12+

PhonePC/2in1TabletTVWearable

static resumeAllTimers(): void

恢复从pauseAllTimers()接口中被暂停的所有的定时器。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Row() {
11. Button('ResumeAllTimers')
12. .onClick(() => {
13. webview.WebviewController.resumeAllTimers();
14. })
15. Button('PauseAllTimers')
16. .onClick(() => {
17. webview.WebviewController.pauseAllTimers();
18. })
19. }
20. Web({ src: $rawfile("index.html"), controller: this.controller })
21. }
22. }
23. }
```

加载的html文件。

```
1. <!DOCTYPE html>
2. <html>
3. <body>
4. <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
5. <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
6. <input style="width:300px;height:150px;font-size:50px" value="0" id="show_num">
7. </body>
8. </html>
9. <script>
10. var timer = null;
11. var num = 0;

13. function startTimer() {
14. timer = setInterval(function() {
15. document.getElementById("show_num").value = ++num;
16. }, 1000);
17. }

19. function resetTimer() {
20. clearInterval(timer);
21. document.getElementById("show_num").value = 0;
22. num = 0;
23. }
24. </script>
```

## stopAllMedia12+

PhonePC/2in1TabletTVWearable

stopAllMedia(): void

控制网页所有音视频停止。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('stopAllMedia')
13. .onClick(() => {
14. try {
15. this.controller.stopAllMedia();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## pauseAllMedia12+

PhonePC/2in1TabletTVWearable

pauseAllMedia(): void

控制网页所有音视频暂停。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('pauseAllMedia')
13. .onClick(() => {
14. try {
15. this.controller.pauseAllMedia();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## resumeAllMedia12+

PhonePC/2in1TabletTVWearable

resumeAllMedia(): void

控制网页被pauseAllMedia接口暂停的音视频继续播放。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('resumeAllMedia')
13. .onClick(() => {
14. try {
15. this.controller.resumeAllMedia();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## closeAllMediaPresentations12+

PhonePC/2in1TabletTVWearable

closeAllMediaPresentations(): void

控制网页所有全屏视频关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('closeAllMediaPresentations')
13. .onClick(() => {
14. try {
15. this.controller.closeAllMediaPresentations();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## getMediaPlaybackState12+

PhonePC/2in1TabletTVWearable

getMediaPlaybackState(): MediaPlaybackState

查询当前网页音视频播放状态。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaPlaybackState](arkts-apis-webview-e.md#mediaplaybackstate12) | 当前网页的播放状态，具体值为NONE、PLAYING、PAUSED、STOPPED。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getMediaPlaybackState')
13. .onClick(() => {
14. try {
15. console.info("MediaPlaybackState : " + this.controller.getMediaPlaybackState());
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## setWebSchemeHandler12+

PhonePC/2in1TabletTVWearable

setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void

为当前Web组件设置[WebSchemeHandler](arkts-apis-webview-webschemehandler.md), [WebSchemeHandler](arkts-apis-webview-webschemehandler.md)类用于拦截指定scheme的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 是 | 要拦截的协议。 |
| handler | [WebSchemeHandler](arkts-apis-webview-webschemehandler.md) | 是 | 拦截此协议的拦截器。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

11. build() {
12. Column() {
13. Button('setWebSchemeHandler')
14. .onClick(() => {
15. try {
16. this.controller.setWebSchemeHandler('http', this.schemeHandler);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## clearWebSchemeHandler12+

PhonePC/2in1TabletTVWearable

clearWebSchemeHandler(): void

清除当前Web组件设置的所有WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('clearWebSchemeHandler')
13. .onClick(() => {
14. try {
15. this.controller.clearWebSchemeHandler();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## setServiceWorkerWebSchemeHandler12+

PhonePC/2in1TabletTVWearable

setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void

为当前应用的所有Web组件设置用于拦截ServiceWorker的WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 是 | 要拦截的协议。 |
| handler | [WebSchemeHandler](arkts-apis-webview-webschemehandler.md) | 是 | 拦截此协议的拦截器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

11. build() {
12. Column() {
13. Button('setWebSchemeHandler')
14. .onClick(() => {
15. try {
16. webview.WebviewController.setServiceWorkerWebSchemeHandler('http', this.schemeHandler);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## clearServiceWorkerWebSchemeHandler12+

PhonePC/2in1TabletTVWearable

clearServiceWorkerWebSchemeHandler(): void

清除应用中设置的所有用于拦截ServiceWorker的WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

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
11. Button('clearServiceWorkerWebSchemeHandler')
12. .onClick(() => {
13. webview.WebviewController.clearServiceWorkerWebSchemeHandler();
14. })
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```

## startCamera12+

PhonePC/2in1TabletTVWearable

startCamera(): void

开启当前网页摄像头捕获。使用摄像头功能前请在module.json5中添加权限: ohos.permission.CAMERA，具体权限的添加方法请参考[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
70. }
71. }
72. }
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
8. <video id="video" width="400px" height="400px" autoplay>
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
22. promise.then(function(mediaStream) {
23. video.srcObject = mediaStream;
24. video.play();
25. })
26. }
27. </script>
28. </body>
29. </html>
```

## stopCamera12+

PhonePC/2in1TabletTVWearable

stopCamera(): void

停止当前网页摄像头捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

完整示例代码参考[startCamera](arkts-apis-webview-webviewcontroller.md#startcamera12)。

## closeCamera12+

PhonePC/2in1TabletTVWearable

closeCamera(): void

关闭当前网页摄像头捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

完整示例代码参考[startCamera](arkts-apis-webview-webviewcontroller.md#startcamera12)。

## precompileJavaScript12+

PhonePC/2in1TabletTVWearable

precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>

预编译JavaScript生成字节码缓存或根据提供的参数更新已有的字节码缓存。

接口通过提供的文件信息、E-Tag响应头和Last-Modified响应头判断是否需要更新已有的字节码缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 本地JavaScript文件对应的网络地址，即业务网页请求该文件的服务器版本时使用的网络地址。网络地址仅支持http或https协议，长度不超过2048。如果该网络地址对应的缓存失效，则业务网页将通过网络请求对应的资源。 |
| script | string | Uint8Array | 是 | 本地JavaScript的文本内容。内容不能为空。 |
| cacheOptions | [CacheOptions](arkts-apis-webview-i.md#cacheoptions12) | 是 | 用于控制字节码缓存更新。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 生成字节码缓存的错误码，0表示无错误，-1表示内部错误。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter.Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

接口推荐配合动态组件使用，使用离线的Web组件用于生成字节码缓存，并在适当的时机加载业务用Web组件使用这些字节码缓存。下方是代码示例：

1. 首先，在EntryAbility中将[UIContext](arkts-apis-uicontext-uicontext.md)存到[localStorage](../harmonyos-guides/arkts-localstorage.md)中。

   ```
   1. // EntryAbility.ets
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';

   5. const localStorage: LocalStorage = new LocalStorage('uiContext');

   7. export default class EntryAbility extends UIAbility {
   8. storage: LocalStorage = localStorage;

   10. onWindowStageCreate(windowStage: window.WindowStage) {
   11. windowStage.loadContent('pages/Index', this.storage, (err, data) => {
   12. if (err.code) {
   13. return;
   14. }

   16. this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
   17. });
   18. }
   19. }
   ```
2. 编写动态组件所需基础代码。

   ```
   1. // DynamicComponent.ets
   2. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

   4. export interface BuilderData {
   5. url: string;
   6. controller: WebviewController;
   7. context: UIContext;
   8. }

   10. let storage : LocalStorage | undefined = undefined;

   12. export class NodeControllerImpl extends NodeController {
   13. private rootNode: BuilderNode<BuilderData[]> | null = null;
   14. private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

   16. constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
   17. storage = context.getSharedLocalStorage();
   18. super();
   19. this.wrappedBuilder = wrappedBuilder;
   20. }

   22. makeNode(): FrameNode | null {
   23. if (this.rootNode != null) {
   24. return this.rootNode.getFrameNode();
   25. }
   26. return null;
   27. }

   29. initWeb(url: string, controller: WebviewController) {
   30. if(this.rootNode != null) {
   31. return;
   32. }

   34. const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
   35. if (!uiContext) {
   36. return;
   37. }
   38. this.rootNode = new BuilderNode(uiContext);
   39. this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
   40. }
   41. }

   43. export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
   44. const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
   45. baseNode.initWeb(data.url, data.controller);
   46. return baseNode;
   47. }
   ```
3. 编写用于生成字节码缓存的组件，本例中的本地Javascript资源内容通过文件读取接口读取rawfile目录下的本地文件。

   ```
   1. // PrecompileWebview.ets
   2. import { BuilderData } from "./DynamicComponent";
   3. import { Config, configs } from "./PrecompileConfig";

   5. @Builder
   6. function WebBuilder(data: BuilderData) {
   7. Web({ src: data.url, controller: data.controller })
   8. .onControllerAttached(() => {
   9. precompile(data.controller, configs, data.context);
   10. })
   11. .fileAccess(true)
   12. }

   14. export const precompileWebview = wrapBuilder<BuilderData[]>(WebBuilder);

   16. export const precompile = async (controller: WebviewController, configs: Array<Config>, context: UIContext) => {
   17. for (const config of configs) {
   18. let content = await readRawFile(config.localPath, context);

   20. try {
   21. controller.precompileJavaScript(config.url, content, config.options)
   22. .then(errCode => {
   23. console.error("precompile successfully! " + errCode);
   24. }).catch((errCode: number) => {
   25. console.error("precompile failed. " + errCode);
   26. });
   27. } catch (err) {
   28. console.error("precompile failed. " + err.code + " " + err.message);
   29. }
   30. }
   31. }

   33. async function readRawFile(path: string, context: UIContext) {
   34. try {
   35. return await context.getHostContext()!.resourceManager.getRawFileContent(path);
   36. } catch (err) {
   37. return new Uint8Array(0);
   38. }
   39. }
   ```

   JavaScript资源的获取方式也可通过[网络请求](js-apis-http.md)的方式获取，但此方法获取到的HTTP响应头非标准HTTP响应头格式，需额外将响应头转换成标准HTTP响应头格式后使用。如通过网络请求获取到的响应头是e-tag，则需要将其转换成E-Tag后使用。
4. 编写业务用组件代码。

   ```
   1. // BusinessWebview.ets
   2. import { BuilderData } from "./DynamicComponent";

   4. @Builder
   5. function WebBuilder(data: BuilderData) {
   6. // 此处组件可根据业务需要自行扩展
   7. Web({ src: data.url, controller: data.controller })
   8. .cacheMode(CacheMode.Default)
   9. }

   11. export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
   ```
5. 编写资源配置信息。

   ```
   1. // PrecompileConfig.ets
   2. import { webview } from '@kit.ArkWeb'

   4. export interface Config {
   5. url:  string,
   6. localPath: string, // 本地资源路径
   7. options: webview.CacheOptions
   8. }

   10. export let configs: Array<Config> = [
   11. {
   12. url: "https://www.example.com/example.js",
   13. localPath: "example.js",
   14. options: {
   15. responseHeaders: [
   16. { headerKey: "E-Tag", headerValue: "aWO42N9P9dG/5xqYQCxsx+vDOoU="},
   17. { headerKey: "Last-Modified", headerValue: "Wed, 21 Mar 2024 10:38:41 GMT"}
   18. ]
   19. }
   20. }
   21. ]
   ```
6. 在页面中使用。

   ```
   1. // Index.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { NodeController } from '@kit.ArkUI';
   4. import { createNode } from "./DynamicComponent"
   5. import { precompileWebview } from "./PrecompileWebview"
   6. import { businessWebview } from "./BusinessWebview"

   8. @Entry
   9. @Component
   10. struct Index {
   11. @State precompileNode: NodeController | undefined = undefined;
   12. precompileController: webview.WebviewController = new webview.WebviewController();

   14. @State businessNode: NodeController | undefined = undefined;
   15. businessController: webview.WebviewController = new webview.WebviewController();

   17. aboutToAppear(): void {
   18. // 初始化用于注入本地资源的Web组件
   19. this.precompileNode = createNode(precompileWebview,
   20. { url: "https://www.example.com/empty.html", controller: this.precompileController, context: this.getUIContext()});
   21. }

   23. build() {
   24. Column() {
   25. // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
   26. Button("加载页面")
   27. .onClick(() => {
   28. this.businessNode = createNode(businessWebview, {
   29. url:  "https://www.example.com/business.html",
   30. controller: this.businessController,
   31. context: this.getUIContext()
   32. });
   33. })
   34. // 用于业务的Web组件
   35. NodeContainer(this.businessNode);
   36. }
   37. }
   38. }
   ```

当需要更新本地已经生成的编译字节码时，修改cacheOptions参数中responseHeaders中的E-Tag或Last-Modified响应头对应的值，再次调用接口即可。

## onCreateNativeMediaPlayer12+

PhonePC/2in1TabletTVWearable

onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void

注册回调函数，开启[应用接管网页媒体播放功能](arkts-basic-components-web-attributes.md#enablenativemediaplayer12)后，当网页中有播放媒体时，触发注册的回调函数。

如果应用接管网页媒体播放功能未开启，则注册的回调函数不会被触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CreateNativeMediaPlayerCallback](arkts-apis-webview-t.md#createnativemediaplayercallback12) | 是 | 接管网页媒体播放的回调函数。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. class ActualNativeMediaPlayerListener {
5. handler: webview.NativeMediaPlayerHandler;

7. constructor(handler: webview.NativeMediaPlayerHandler) {
8. this.handler = handler;
9. }

11. onPlaying() {
12. // 本地播放器开始播放。
13. this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
14. }
15. onPaused() {
16. // 本地播放器暂停播放。
17. this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
18. }
19. onSeeking() {
20. // 本地播放器开始执行跳转到目标时间点。
21. this.handler.handleSeeking();
22. }
23. onSeekDone() {
24. // 本地播放器 seek 完成。
25. this.handler.handleSeekFinished();
26. }
27. onEnded() {
28. // 本地播放器播放完成。
29. this.handler.handleEnded();
30. }
31. onVolumeChanged() {
32. // 获取本地播放器的音量。
33. let volume: number = getVolume();
34. this.handler.handleVolumeChanged(volume);
35. }
36. onCurrentPlayingTimeUpdate() {
37. // 更新播放时间。
38. let currentTime: number = getCurrentPlayingTime();
39. // 将时间单位换算成秒。
40. let currentTimeInSeconds = convertToSeconds(currentTime);
41. this.handler.handleTimeUpdate(currentTimeInSeconds);
42. }
43. onBufferedChanged() {
44. // 缓存发生了变化。
45. // 获取本地播放器的缓存时长。
46. let bufferedEndTime: number = getCurrentBufferedTime();
47. // 将时间单位换算成秒。
48. let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
49. this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);

51. // 检查缓存状态。
52. // 如果缓存状态发生了变化，则向 ArkWeb 内核通知缓存状态。
53. let lastReadyState: webview.ReadyState = getLastReadyState();
54. let currentReadyState:  webview.ReadyState = getCurrentReadyState();
55. if (lastReadyState != currentReadyState) {
56. this.handler.handleReadyStateChanged(currentReadyState);
57. }
58. }
59. onEnterFullscreen() {
60. // 本地播放器进入了全屏状态。
61. let isFullscreen: boolean = true;
62. this.handler.handleFullscreenChanged(isFullscreen);
63. }
64. onExitFullscreen() {
65. // 本地播放器退出了全屏状态。
66. let isFullscreen: boolean = false;
67. this.handler.handleFullscreenChanged(isFullscreen);
68. }
69. onUpdateVideoSize(width: number, height: number) {
70. // 当本地播放器解析出视频宽高时， 通知 ArkWeb 内核。
71. this.handler.handleVideoSizeChanged(width, height);
72. }
73. onDurationChanged(duration: number) {
74. // 本地播放器解析到了新的媒体时长， 通知 ArkWeb 内核。
75. this.handler.handleDurationChanged(duration);
76. }
77. onError(error: webview.MediaError, errorMessage: string) {
78. // 本地播放器出错了，通知 ArkWeb 内核。
79. this.handler.handleError(error, errorMessage);
80. }
81. onNetworkStateChanged(state: webview.NetworkState) {
82. // 本地播放器的网络状态发生了变化， 通知 ArkWeb 内核。
83. this.handler.handleNetworkStateChanged(state);
84. }
85. onPlaybackRateChanged(playbackRate: number) {
86. // 本地播放器的播放速率发生了变化， 通知 ArkWeb 内核。
87. this.handler.handlePlaybackRateChanged(playbackRate);
88. }
89. onMutedChanged(muted: boolean) {
90. // 本地播放器的静音状态发生了变化， 通知 ArkWeb 内核。
91. this.handler.handleMutedChanged(muted);
92. }

94. // ... 监听本地播放器其他的状态 ...
95. }

97. class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
98. constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
99. // 1. 创建一个本地播放器的状态监听。
100. let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
101. // 2. 创建一个本地播放器。
102. // 3. 监听该本地播放器。
103. // ...
104. }

106. updateRect(x: number, y: number, width: number, height: number) {
107. // <video> 标签的位置和大小发生了变化。
108. // 根据该信息变化，作出相应的改变。
109. }

111. play() {
112. // 启动本地播放器播放。
113. }

115. pause() {
116. // 暂停本地播放器播放。
117. }

119. seek(targetTime: number) {
120. // 本地播放器跳转到指定的时间点。
121. }

123. release() {
124. // 销毁本地播放器。
125. }

127. setVolume(volume: number) {
128. // ArkWeb 内核要求调整本地播放器的音量。
129. // 设置本地播放器的音量。
130. }

132. setMuted(muted: boolean) {
133. // 将本地播放器静音或取消静音。
134. }

136. setPlaybackRate(playbackRate: number) {
137. // 调整本地播放器的播放速度。
138. }

140. enterFullscreen() {
141. // 将本地播放器设置为全屏播放。
142. }

144. exitFullscreen() {
145. // 将本地播放器退出全屏播放。
146. }

148. resumePlayer() {
149. // 重新创建应用内播放器。
150. // 恢复应用内播放器的状态信息。
151. }

153. suspendPlayer(type: webview.SuspendType) {
154. // 记录应用内播放器的状态信息。
155. // 销毁应用内播放器。
156. }
157. }

159. @Entry
160. @Component
161. struct WebComponent {
162. controller: webview.WebviewController = new webview.WebviewController()
163. build() {
164. Column() {
165. Web({ src: 'www.example.com', controller: this.controller })
166. .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
167. .onPageBegin((event) => {
168. this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
169. if (!shouldHandle(mediaInfo)) {
170. // 本地播放器不接管该媒体。
171. // ArkWeb 内核将用自己的播放器来播放该媒体。
172. return null;
173. }
174. let nativePlayer: webview.NativeMediaPlayerBridge = new NativeMediaPlayerImpl(handler, mediaInfo);
175. return nativePlayer;
176. });
177. })
178. }
179. }
180. }

182. // stub
183. function getVolume() {
184. return 1;
185. }
186. function getCurrentPlayingTime() {
187. return 1;
188. }
189. function getCurrentBufferedTime() {
190. return 1;
191. }
192. function convertToSeconds(input: number) {
193. return input;
194. }
195. function getLastReadyState() {
196. return webview.ReadyState.HAVE_NOTHING;
197. }
198. function getCurrentReadyState() {
199. return webview.ReadyState.HAVE_NOTHING;
200. }
201. function shouldHandle(mediaInfo: webview.MediaInfo) {
202. return true;
203. }
```

## enableWholeWebPageDrawing12+

PhonePC/2in1TabletTVWearable

static enableWholeWebPageDrawing(): void

设置开启网页全量绘制能力。仅在web初始化时设置。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. aboutToAppear(): void {
11. try {
12. webview.WebviewController.enableWholeWebPageDrawing();
13. } catch (error) {
14. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
15. }
16. }

18. build() {
19. Column() {
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## webPageSnapshot12+

PhonePC/2in1TabletTVWearable

webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void

获取网页全量绘制结果。

说明

此接口不支持并发调用。

仅支持对渲染进程上的资源进行截图：静态图片和文本。

如果页面有视频则截图时会显示该视频的占位图片，没有占位图片则显示空白。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [SnapshotInfo](arkts-apis-webview-i.md#snapshotinfo12) | 是 | 全量绘制结果入参。 |
| callback | AsyncCallback<[SnapshotResult](arkts-apis-webview-i.md#snapshotresult12)> | 是 | 全量绘制回调结果。 |

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
12. Button('webPageSnapshot')
13. .onClick(() => {
14. try {
15. this.controller.webPageSnapshot({ id: "1234", size: { width: 100, height: 100 } }, (error, result) => {
16. if (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. return;
19. }
20. if (result) {
21. console.info(`return value is:${result}`);
22. // 开发者可以根据需要处理返回结果
23. }
24. });
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. })
29. Web({ src: 'www.example.com', controller: this.controller })
30. }
31. }
32. }
```

## injectOfflineResources12+

PhonePC/2in1TabletTVWearable

injectOfflineResources(resourceMaps: Array<[OfflineResourceMap](arkts-apis-webview-i.md#offlineresourcemap12)>): void

将本地离线资源注入到内存缓存中，以提升页面首次启动速度。

内存缓存中的资源由内核自动管理，当注入的资源过多导致内存压力过大，内核自动释放未使用的资源，应避免注入大量资源到内存缓存中。

正常情况下，资源的有效期由提供的Cache-Control或Expires响应头控制其有效期，默认的有效期为86400秒，即1天。

资源的MIMEType通过提供的Content-Type响应头配置，Content-Type需符合标准，否则无法正常使用，MODULE\_JS必须提供有效的MIMEType，其他类型可不提供。

以此方式注入的资源，仅支持通过HTML中的标签加载。如果业务网页中的script标签使用了crossorigin属性，则必须在接口的responseHeaders参数中设置Cross-Origin响应头的值为anonymous或use-credentials。

当调用webview.WebviewController.SetRenderProcessMode(webview.RenderProcessMode.MULTIPLE)接口后，应用会启动多渲染进程模式，此接口在此场景下不会生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceMaps | Array<[OfflineResourceMap](arkts-apis-webview-i.md#offlineresourcemap12)> | 是 | 本地离线资源配置对象，单次调用最大支持注入30个资源，单个资源最大支持10Mb。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**示例：**

接口推荐配合动态组件使用，使用离线的Web组件用于将资源注入到内核的内存缓存中，并在适当的时机加载业务用Web组件使用这些资源。下方是代码示例：

1. 首先，在EntryAbility中将[UIContext](arkts-apis-uicontext-uicontext.md)存到[localStorage](../harmonyos-guides/arkts-localstorage.md)中。

   ```
   1. // EntryAbility.ets
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';

   5. const localStorage: LocalStorage = new LocalStorage('uiContext');

   7. export default class EntryAbility extends UIAbility {
   8. storage: LocalStorage = localStorage;

   10. onWindowStageCreate(windowStage: window.WindowStage) {
   11. windowStage.loadContent('pages/Index', this.storage, (err, data) => {
   12. if (err.code) {
   13. return;
   14. }

   16. this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
   17. });
   18. }
   19. }
   ```
2. 编写动态组件所需基础代码。

   ```
   1. // DynamicComponent.ets
   2. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

   4. export interface BuilderData {
   5. url: string;
   6. controller: WebviewController;
   7. context: UIContext;
   8. }

   10. let storage : LocalStorage | undefined = undefined;

   12. export class NodeControllerImpl extends NodeController {
   13. private rootNode: BuilderNode<BuilderData[]> | null = null;
   14. private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

   16. constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
   17. storage = context.getSharedLocalStorage();
   18. super();
   19. this.wrappedBuilder = wrappedBuilder;
   20. }

   22. makeNode(): FrameNode | null {
   23. if (this.rootNode != null) {
   24. return this.rootNode.getFrameNode();
   25. }
   26. return null;
   27. }

   29. initWeb(url: string, controller: WebviewController) {
   30. if(this.rootNode != null) {
   31. return;
   32. }

   34. const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
   35. if (!uiContext) {
   36. return;
   37. }
   38. this.rootNode = new BuilderNode(uiContext);
   39. this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
   40. }
   41. }

   43. export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
   44. const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
   45. baseNode.initWeb(data.url, data.controller);
   46. return baseNode;
   47. }
   ```
3. 编写用于注入资源的组件代码，本例中的本地资源内容通过文件读取接口读取rawfile目录下的本地文件。

   ```
   1. // InjectWebview.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { resourceConfigs } from "./Resource";
   4. import { BuilderData } from "./DynamicComponent";

   6. @Builder
   7. function WebBuilder(data: BuilderData) {
   8. Web({ src: data.url, controller: data.controller })
   9. .onControllerAttached(async () => {
   10. try {
   11. data.controller.injectOfflineResources(await getData (data.context));
   12. } catch (err) {
   13. console.error("error: " + err.code + " " + err.message);
   14. }
   15. })
   16. .fileAccess(true)
   17. }

   19. export const injectWebview = wrapBuilder<BuilderData[]>(WebBuilder);

   21. export async function getData(context: UIContext) {
   22. const resourceMapArr: Array<webview.OfflineResourceMap> = [];

   24. // 读取配置，从rawfile目录中读取文件内容
   25. for (let config of resourceConfigs) {
   26. let buf: Uint8Array = new Uint8Array(0);
   27. if (config.localPath) {
   28. buf = await readRawFile(config.localPath, context);
   29. }

   31. resourceMapArr.push({
   32. urlList: config.urlList,
   33. resource: buf,
   34. responseHeaders: config.responseHeaders,
   35. type: config.type,
   36. })
   37. }

   39. return resourceMapArr;
   40. }

   42. export async function readRawFile(url: string, context: UIContext) {
   43. try {
   44. return await context.getHostContext()!.resourceManager.getRawFileContent(url);
   45. } catch (err) {
   46. return new Uint8Array(0);
   47. }
   48. }
   ```
4. 编写业务用组件代码。

   ```
   1. // BusinessWebview.ets
   2. import { BuilderData } from "./DynamicComponent";

   4. @Builder
   5. function WebBuilder(data: BuilderData) {
   6. // 此处组件可根据业务需要自行扩展
   7. Web({ src: data.url, controller: data.controller })
   8. .cacheMode(CacheMode.Default)
   9. }

   11. export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
   ```
5. 编写资源配置信息。

   ```
   1. // Resource.ets
   2. import { webview } from '@kit.ArkWeb';

   4. export interface ResourceConfig {
   5. urlList: Array<string>,
   6. type: webview.OfflineResourceType,
   7. responseHeaders: Array<Header>,
   8. localPath: string, // 本地资源存放在rawfile目录下的路径
   9. }

   11. export const resourceConfigs: Array<ResourceConfig> = [
   12. {
   13. localPath: "example.png",
   14. urlList: [
   15. "https://www.example.com/",
   16. "https://www.example.com/path1/example.png",
   17. "https://www.example.com/path2/example.png",
   18. ],
   19. type: webview.OfflineResourceType.IMAGE,
   20. responseHeaders: [
   21. { headerKey: "Cache-Control", headerValue: "max-age=1000" },
   22. { headerKey: "Content-Type", headerValue: "image/png" },
   23. ]
   24. },
   25. {
   26. localPath: "example.js",
   27. urlList: [ // 仅提供一个url，这个url既作为资源的源，也作为资源的网络请求地址
   28. "https://www.example.com/example.js",
   29. ],
   30. type: webview.OfflineResourceType.CLASSIC_JS,
   31. responseHeaders: [
   32. // 以<script crossorigin="anonymous" />方式使用，提供额外的响应头
   33. { headerKey: "Cross-Origin", headerValue:"anonymous" }
   34. ]
   35. },
   36. ];
   ```
6. 在页面中使用。

   ```
   1. // Index.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { NodeController } from '@kit.ArkUI';
   4. import { createNode } from "./DynamicComponent"
   5. import { injectWebview } from "./InjectWebview"
   6. import { businessWebview } from "./BusinessWebview"

   8. @Entry
   9. @Component
   10. struct Index {
   11. @State injectNode: NodeController | undefined = undefined;
   12. injectController: webview.WebviewController = new webview.WebviewController();

   14. @State businessNode: NodeController | undefined = undefined;
   15. businessController: webview.WebviewController = new webview.WebviewController();

   17. aboutToAppear(): void {
   18. // 初始化用于注入本地资源的Web组件, 提供一个空的html页面作为url即可
   19. this.injectNode = createNode(injectWebview,
   20. { url: "https://www.example.com/empty.html", controller: this.injectController, context: this.getUIContext()});
   21. }

   23. build() {
   24. Column() {
   25. // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
   26. Button("加载页面")
   27. .onClick(() => {
   28. this.businessNode = createNode(businessWebview, {
   29. url: "https://www.example.com/business.html",
   30. controller: this.businessController,
   31. context: this.getUIContext()
   32. });
   33. })
   34. // 用于业务的Web组件
   35. NodeContainer(this.businessNode);
   36. }
   37. }
   38. }
   ```
7. 加载的HTML网页示例。

   ```
   1. <!DOCTYPE html>
   2. <html lang="en">
   3. <head></head>
   4. <body>
   5. <img src="https://www.example.com/path1/request.png" />
   6. <img src="https://www.example.com/path2/request.png" />
   7. <script src="https://www.example.com/example.js" crossorigin="anonymous"></script>
   8. </body>
   9. </html>
   ```

## setHostIP12+

PhonePC/2in1TabletTVWearable

static setHostIP(hostName: string, address: string, aliveTime: number): void

设置主机域名解析后的IP地址。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | 要添加DNS记录的主机域名。 |
| address | string | 是 | 主机域名解析地址（支持IPv4，IPv6）。 |
| aliveTime | number | 是 | 缓存有效时间（秒）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |

**示例：**

请参考[clearHostIP](arkts-apis-webview-webviewcontroller.md#clearhostip12)。

## clearHostIP12+

PhonePC/2in1TabletTVWearable

static clearHostIP(hostName: string): void

清除指定主机域名解析后的IP地址。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | 要清除DNS记录的主机域名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |

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
12. // url加载前设置生效.
13. Button('setHostIP')
14. .onClick(() => {
15. try {
16. webview.WebviewController.setHostIP('www.example.com', '127.0.0.1', 30);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Button('clearHostIP')
22. .onClick(() => {
23. try {
24. webview.WebviewController.clearHostIP('www.example.com');
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. })
29. Web({ src: 'www.example.com', controller: this.controller })
30. }
31. }
32. }
```

## getSurfaceId12+

PhonePC/2in1TabletTVWearable

getSurfaceId(): string

获取ArkWeb对应Surface的ID，此ID可用于网页截图。

说明

仅Web组件渲染模式是ASYNC\_RENDER时有效。getSurfaceId需要在Web组件初始化之后才能获取到值。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | ArkWeb持有Surface的ID。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { image } from '@kit.ImageKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Example{
9. controller: webview.WebviewController = new webview.WebviewController();

11. @State imagePixelMap: image.PixelMap | undefined = undefined;

13. build(){
14. Column(){
15. Button("截图")
16. .onClick(()=>{
17. try {
18. let surfaceId = this.controller.getSurfaceId();
19. console.info("surfaceId: " + surfaceId);
20. if(surfaceId.length != 0) {
21. let region:image.Region = { x: 0, y: 0, size: { height: 800, width: 1000}}
22. this.imagePixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region)
23. }
24. } catch (error) {
25. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
26. }
27. })
28. Image(this.imagePixelMap)
29. .height(100)
30. Web({src: 'www.example.com', controller: this.controller})
31. }
32. }
33. }
```

## setUrlTrustList12+

PhonePC/2in1TabletTVWearable

setUrlTrustList(urlTrustList: string): void

设置Web的URL白名单，只有白名单内的URL才能允许加载/跳转，否则将拦截并弹出告警页。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| urlTrustList | string | 是 | url白名单列表，使用json格式配置，最大支持10MB。  白名单设置接口为覆盖方式，多次调用接口时，以最后一次设置为准。  当本参数为空字符串时，表示取消白名单，放行所有url的访问。  json格式示例：  {  "UrlPermissionList": [  {  "scheme": "https",  "host": "www.example1.com",  "port": 443,  "path": "pathA/pathB"  },  {  "scheme": "http",  "host": "www.example2.com",  "port": 80,  "path": "test1/test2/test3"  }  ]  } |

**白名单json格式参数**

| 字段 | 参数类型 | 必填 | 参数描述 |
| --- | --- | --- | --- |
| scheme | string | 否 | 可选参数，不设置即不匹配该项，支持协议：http、https。 |
| host | string | 是 | 必选参数，精准匹配，即url的host字段和规则字段完全一致才会放行，可允许同一host多条规则同时生效。 |
| port | number | 否 | 可选字段，不设置即不匹配该项。 |
| path | string | 否 | 可选字段，不设置即不匹配该项，匹配方式为前缀匹配，以"pathA/pathB/pathC"为例：pathA/pathB/pathC三级目录下全部允许访问，其中pathC必须是完整的目录名或者文件名，不允许部分匹配。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Parameter string is too long.3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. urltrustList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"port\":80, \"path\":\"test\"}]}"

11. build() {
12. Column() {
13. Button('Setting the trustlist')
14. .onClick(() => {
15. try {
16. // 设置白名单，只允许访问trust网页
17. this.controller.setUrlTrustList(this.urltrustList);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Button('Cancel the trustlist.')
23. .onClick(() => {
24. try {
25. // 白名单传入空字符串表示关闭白名单机制，所有url都可以允许访问
26. this.controller.setUrlTrustList("");
27. } catch (error) {
28. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
29. }
30. })
31. Button('Access the trust web')
32. .onClick(() => {
33. try {
34. // 白名单生效，可以访问trust网页
35. this.controller.loadUrl('http://trust.example.com/test');
36. } catch (error) {
37. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
38. }
39. })
40. Button('Access the untrust web')
41. .onClick(() => {
42. try {
43. // 白名单生效，此时不可以访问untrust网页，并弹出错误页
44. this.controller.loadUrl('http://untrust.example.com/test');
45. } catch (error) {
46. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
47. }
48. })
49. Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
50. try {
51. // onControllerAttached回调中设置白名单，可以保证在加载url之前生效，此时不可以访问untrust网页，并弹出错误页
52. this.controller.setUrlTrustList(this.urltrustList);
53. } catch (error) {
54. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
55. }
56. })
57. }
58. }
59. }
```

## setPathAllowingUniversalAccess12+

PhonePC/2in1TabletTVWearable

setPathAllowingUniversalAccess(pathList: Array<string>): void

设置一个路径列表，当file协议访问该路径列表中的资源时，允许跨域访问本地文件，也允许跨域访问其他在线资源。此外，当设置了路径列表时，file协议仅允许访问路径列表中的资源（[fileAccess](arkts-basic-components-web-attributes.md#fileaccess)的行为将会被此接口行为覆盖）。

setPathAllowingUniversalAccess放开目录的跨域访问限制是一个高风险操作。基于最小权限原则，当前el1，el2放开的路径是固定的，路径列表中的路径应符合以下任一路径格式：

1.应用文件目录的子目录（应用文件目录通过Ability Kit中的[Context.filesDir](js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el2/base/files/example
* /data/storage/el2/base/haps/entry/files/example

2.应用资源目录及其子目录（应用资源目录通过Ability Kit中的[Context.resourceDir](js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el1/bundle/entry/resources/resfile
* /data/storage/el1/bundle/entry/resources/resfile/example

3.从API version 21开始，还包括了应用缓存目录及其子目录（应用缓存目录通过Ability Kit中的[Context.cacheDir](js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el2/base/cache
* /data/storage/el2/base/haps/entry/cache/example
* 设置的目录路径中，不允许包含cache/web，否则会抛出异常码401。如果设置目录路径是cache，cache/web也不允许访问。

4.从API version 21开始，还包括了应用临时目录及其子目录（应用临时目录通过Ability Kit中的[Context.tempDir](js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el2/base/temp
* /data/storage/el2/base/haps/entry/temp/example

当路径列表中有其中一个路径不满足以上条件之一，则会抛出异常码401，并且设置路径列表失败。当设置的路径列表为空，则file协议可访问范围以[fileAccess](arkts-basic-components-web-attributes.md#fileaccess)的行为为准。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathList | Array<string> | 是 | 路径列表 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: WebviewController = new webview.WebviewController();
9. uiContext: UIContext = this.getUIContext();

11. build() {
12. Row() {
13. Web({ src: "", controller: this.controller })
14. .onControllerAttached(() => {
15. try {
16. // 设置允许可以跨域访问的路径列表
17. this.controller.setPathAllowingUniversalAccess([
18. this.uiContext.getHostContext()!.resourceDir,
19. this.uiContext.getHostContext()!.filesDir + "/example"
20. ])
21. this.controller.loadUrl("file://" + this.getUIContext().getHostContext()!.resourceDir + "/index.html")
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. .javaScriptAccess(true)
27. .fileAccess(true)
28. .domStorageAccess(true)
29. }
30. }
31. }
```

加载的html文件，位于应用资源目录resource/resfile/index.html。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html lang="en">

5. <head>
6. <meta charset="utf-8">
7. <title>Demo</title>
8. <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no, viewport-fit=cover">
9. <script>
10. function getFile() {
11. var file = "file:///data/storage/el1/bundle/entry/resources/resfile/js/script.js";
12. var xmlHttpReq = new XMLHttpRequest();
13. xmlHttpReq.onreadystatechange = function(){
14. console.info("readyState:" + xmlHttpReq.readyState);
15. console.info("status:" + xmlHttpReq.status);
16. if(xmlHttpReq.readyState == 4){
17. if (xmlHttpReq.status == 200) {
18. // 如果ets侧正确设置路径列表，则此处能正常获取资源
19. const element = document.getElementById('text');
20. element.textContent = "load " + file + " success";
21. } else {
22. // 如果ets侧不设置路径列表，则此处会触发CORS跨域检查错误
23. const element = document.getElementById('text');
24. element.textContent = "load " + file + " failed";
25. }
26. }
27. }
28. xmlHttpReq.open("GET", file);
29. xmlHttpReq.send(null);
30. }

32. </script>
33. </head>

35. <body>
36. <div class="page">
37. <button id="example" onclick="getFile()">stealFile</button>
38. </div>
39. <div id="text"></div>
40. </body>

42. </html>
```

html中使用file协议通过XMLHttpRequest跨域访问本地js文件，js文件位于resource/resfile/js/script.js。

```
1. const body = document.body;
2. const element = document.createElement('div');
3. element.textContent = 'success';
4. body.appendChild(element);
```

## enableBackForwardCache12+

PhonePC/2in1TabletTVWearable

static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void

开启Web组件前进后退缓存功能，通过参数指定是否允许使用特定的页面进入前进后退缓存。

需要在[initializeWebEngine()](arkts-apis-webview-webviewcontroller.md#initializewebengine)初始化内核之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| features | [BackForwardCacheSupportedFeatures](kts-apis-webview-backforwardcachesupportedfeatures.md) | 是 | 允许使用特定的页面进入前进后退缓存中。 |

**示例：**

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';
5. import { webview } from '@kit.ArkWeb';

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
9. let features = new webview.BackForwardCacheSupportedFeatures();
10. features.nativeEmbed = true;
11. features.mediaTakeOver = true;
12. // 如果一个页面同时使用了同层渲染和视频托管的能力，需要 nativeEmbed 和
13. // mediaTakeOver 同时设置为 true，该页面才可以进入前进后退缓存中。
14. webview.WebviewController.enableBackForwardCache(features);
15. webview.WebviewController.initializeWebEngine();
16. AppStorage.setOrCreate("abilityWant", want);
17. }
18. }
```

## setBackForwardCacheOptions12+

PhonePC/2in1TabletTVWearable

setBackForwardCacheOptions(options: BackForwardCacheOptions): void

可以设置Web组件中前进后退缓存的相关选项。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [BackForwardCacheOptions](arkts-apis-webview-backforwardcacheoptions.md) | 是 | 用来控制Web组件前进后退缓存相关选项。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // xxx.ts
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Row() {
12. Button("Add options").onClick((event: ClickEvent) => {
13. let options = new webview.BackForwardCacheOptions();
14. options.size = 3;
15. options.timeToLive = 10;
16. this.controller.setBackForwardCacheOptions(options);
17. })
18. Button("Backward").onClick((event: ClickEvent) => {
19. this.controller.backward();
20. })
21. Button("Forward").onClick((event: ClickEvent) => {
22. this.controller.forward();
23. })
24. }
25. Web({ src: "https://www.example.com", controller: this.controller })
26. }
27. .height('100%')
28. .width('100%')
29. }
30. }
```

## trimMemoryByPressureLevel14+

PhonePC/2in1TabletTVWearable

trimMemoryByPressureLevel(level: PressureLevel): void

根据指定的内存压力等级，主动清理Web组件占用的缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [PressureLevel](arkts-apis-webview-e.md#pressurelevel14) | 是 | 需要清理内存的内存等级。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: WebviewController = new webview.WebviewController();
9. build() {
10. Column() {
11. Row() {
12. Button('trim_Memory')
13. .onClick(() => {
14. try {
15. // 设置当前内存压力等级为适中，释放少量内存
16. webview.WebviewController.trimMemoryByPressureLevel(
17. webview.PressureLevel.MEMORY_PRESSURE_LEVEL_MODERATE);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. }.height('10%')
23. Web({ src: 'www.example.com', controller: this.controller })
24. }
25. }
26. }
```

## createPdf14+

PhonePC/2in1TabletTVWearable

createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void

异步callback方式获取指定网页的数据流。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | [PdfConfiguration](arkts-apis-webview-i.md#pdfconfiguration14) | 是 | 生成PDF所需参数。 |
| callback | AsyncCallback<[PdfData](arkts-apis-webview-pdfdata.md)> | 是 | 回调返回网页PDF数据流。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例**:

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { common } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct Index {
9. controller: webview.WebviewController = new webview.WebviewController();
10. pdfConfig: webview.PdfConfiguration = {
11. width: 8.27,
12. height: 11.69,
13. marginTop: 0,
14. marginBottom: 0,
15. marginRight: 0,
16. marginLeft: 0,
17. shouldPrintBackground: true
18. }

20. build() {
21. Column() {
22. Button('SavePDF')
23. .onClick(() => {
24. this.controller.createPdf(
25. this.pdfConfig,
26. (error, result: webview.PdfData) => {
27. try {
28. // 获取组件上下文
29. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
30. // 获取沙箱路径，设置pdf文件名
31. let filePath = context.filesDir + "/test.pdf";
32. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
33. fileIo.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
34. console.info("createPDF write data to file succeeded and size is:" + writeLen);
35. }).catch((err: BusinessError) => {
36. console.error("createPDF write data to file failed with error message: " + err.message +
37. ", error code: " + err.code);
38. }).finally(() => {
39. fileIo.closeSync(file);
40. });
41. } catch (resError) {
42. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
43. }
44. });
45. })
46. Web({ src: "www.example.com", controller: this.controller })
47. }
48. }
49. }
```

## createPdf14+

PhonePC/2in1TabletTVWearable

createPdf(configuration: PdfConfiguration): Promise<PdfData>

以Promise方式异步获取指定网页的数据流。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | [PdfConfiguration](arkts-apis-webview-i.md#pdfconfiguration14) | 是 | 生成PDF所需参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PdfData](arkts-apis-webview-pdfdata.md)> | Promise实例，返回网页数据流。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例**:

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { common } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct Index {
9. controller: webview.WebviewController = new webview.WebviewController();
10. pdfConfig: webview.PdfConfiguration = {
11. width: 8.27,
12. height: 11.69,
13. marginTop: 0,
14. marginBottom: 0,
15. marginRight: 0,
16. marginLeft: 0,
17. shouldPrintBackground: true
18. }

20. build() {
21. Column() {
22. Button('SavePDF')
23. .onClick(() => {
24. this.controller.createPdf(this.pdfConfig)
25. .then((result: webview.PdfData) => {
26. try {
27. // 获取组件上下文
28. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
29. // 获取沙箱路径，设置pdf文件名
30. let filePath = context.filesDir + "/test.pdf";
31. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
32. fileIo.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
33. console.info("createPDF write data to file succeeded and size is:" + writeLen);
34. }).catch((err: BusinessError) => {
35. console.error("createPDF write data to file failed with error message: " + err.message +
36. ", error code: " + err.code);
37. }).finally(() => {
38. fileIo.closeSync(file);
39. });
40. } catch (resError) {
41. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
42. }
43. })
44. })
45. Web({ src: "www.example.com", controller: this.controller })
46. }
47. }
48. }
```

## getScrollOffset13+

PhonePC/2in1TabletTVWearable

getScrollOffset(): ScrollOffset

获取网页当前的滚动偏移量（包含过滚动偏移量）。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值**

| 类型 | 说明 |
| --- | --- |
| [ScrollOffset](arkts-apis-webview-i.md#scrolloffset13) | 网页当前的滚动偏移量（包含过滚动偏移量）。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. @State testTitle: string = 'webScroll'
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State controllerX: number =-100;
10. @State controllerY: number =-100;
11. @State mode: OverScrollMode = OverScrollMode.ALWAYS;

13. build() {
14. Column() {
15. Row() {
16. Text(this.testTitle)
17. .fontSize(30)
18. .fontWeight(FontWeight.Bold)
19. .margin(5)
20. }
21. Column() {
22. Text(`controllerX: ${this.controllerX}, controllerY: ${this.controllerY}`)
23. }
24. .margin({ top: 10, bottom: 10 })
25. Web({ src: $rawfile("index.html"), controller: this.controller })
26. .key("web_01")
27. .overScrollMode(this.mode)
28. .onTouch(() => {
29. this.controllerX = this.controller.getScrollOffset().x;
30. this.controllerY = this.controller.getScrollOffset().y;
31. let componentInfo = this.getUIContext().getComponentUtils().getRectangleById("web_01");
32. let webHeight = this.getUIContext().px2vp(componentInfo.size.height);
33. let pageHeight = this.controller.getPageHeight();
34. if (this.controllerY < 0) {
35. // case1：网页向下过滚动时，可直接使用ScrollOffset.y
36. console.info(`get downwards overscroll offsetY = ${this.controllerY}`);
37. } else if ((this.controllerY != 0) && (this.controllerY > (pageHeight - webHeight))) {
38. // case2：网页向上过滚动时，需计算出网页下边界与Web组件下边界的偏移量
39. console.info(`get upwards overscroll offsetY = ${this.controllerY - (pageHeight >= webHeight ? (pageHeight - webHeight) : 0)}`);
40. } else {
41. // case3：网页未发生过滚动时，可直接使用ScrollOffset.y
42. console.info(`get scroll offsetY = ${this.controllerY}`);
43. }
44. })
45. .height(600)
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
6. <title>Demo</title>
7. <style>
8. body {
9. width:3000px;
10. height:6000px;
11. padding-right:170px;
12. padding-left:170px;
13. border:5px solid blueviolet;
14. }
15. </style>
16. </head>
17. <body>
18. Scroll Test
19. </body>
20. </html>
```

## getPageOffset20+

PhonePC/2in1TabletTVWearable

getPageOffset(): ScrollOffset

获取网页当前的滚动偏移量（不包含过滚动偏移量）。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值**

| 类型 | 说明 |
| --- | --- |
| [ScrollOffset](arkts-apis-webview-i.md#scrolloffset13) | 网页当前的滚动偏移量（不包含过滚动偏移量）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { webview } from '@kit.ArkWeb';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .onScroll((event) => {
14. try {
15. console.info("getPageOffset x:" + this.controller.getPageOffset().x + ",y:" +
16. this.controller.getPageOffset().y);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. }
22. }
23. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
6. <style>
7. .blue {
8. background-color: lightblue;
9. }
10. .green {
11. background-color: lightgreen;
12. }
13. .blue, .green {
14. font-size:16px;
15. height:200px;
16. text-align: center;       /* 水平居中 */
17. line-height: 200px;       /* 垂直居中（值等于容器高度） */
18. }
19. </style>
20. </head>
21. <body>
22. <div class="blue" >webArea</div>
23. <div class="green">webArea</div>
24. <div class="blue">webArea</div>
25. <div class="green">webArea</div>
26. <div class="blue">webArea</div>
27. <div class="green">webArea</div>
28. <div class="blue">webArea</div>
29. </body>
30. </html>
```

## getLastHitTest18+

PhonePC/2in1TabletTVWearable

getLastHitTest(): HitTestValue

获取上一次被点击区域的元素信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HitTestValue](arkts-apis-webview-i.md#hittestvalue) | 点击区域的元素信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getLastHitTest')
13. .onClick(() => {
14. try {
15. let hitValue = this.controller.getLastHitTest();
16. console.info("hitType: " + hitValue.type);
17. console.info("extra: " + hitValue.extra);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## getAttachState20+

PhonePC/2in1TabletTVWearable

getAttachState(): ControllerAttachState

查询当前WebViewController是否绑定一个Web组件。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ControllerAttachState](arkts-apis-webview-i.md#controllerattachstate20) | WebViewController与Web组件的绑定状态。 |

**示例：**

点击Button可以获取当前WebViewController的绑定状态并输出日志。

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
12. Button('getAttachState')
13. .onClick(() => {
14. try {
15. if (this.controller.getAttachState() == webview.ControllerAttachState.ATTACHED) {
16. console.info('Controller is attached.');
17. } else {
18. console.info('Controller is unattached.');
19. }
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## on('controllerAttachStateChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void

注册WebViewController绑定状态事件，通过Callback方式获取WebViewController绑定状态的变化通知。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示注册WebViewController绑定状态事件，固定为"controllerAttachStateChange"。 |
| callback | Callback<[ControllerAttachState](arkts-apis-webview-i.md#controllerattachstate20)> | 是 | WebViewController绑定状态改变时的回调函数。 |

**示例：**

请参考[off](arkts-apis-webview-webviewcontroller.md#offcontrollerattachstatechange20)。

## off('controllerAttachStateChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void

取消WebViewController绑定状态事件的注册，取消后将不再接收Callback通知。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示注册WebViewController绑定状态事件，固定为"controllerAttachStateChange"。 |
| callback | Callback<[ControllerAttachState](arkts-apis-webview-i.md#controllerattachstate20)> | 否 | WebViewController绑定状态发生改变时的回调函数，默认情况下不填写回调函数。如果填写了Callback，将仅取消注册该特定的回调。如果不填写Callback，将取消注册所有回调。  传入null或undefined时会抛出异常错误码401。 |

**示例：**

on可以注册多个回调，当绑定状态改变后会获取当前的绑定状态并触发这些回调。off可以取消注册某个回调，也可以取消注册所有回调。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. // 构建回调函数
10. handleControllerAttachStateChange = (state: webview.ControllerAttachState) => {
11. if (state == webview.ControllerAttachState.UNATTACHED) {
12. console.info('handleControllerAttachStateChange: Controller is unattached.');
13. } else {
14. console.info('handleControllerAttachStateChange: Controller is attached.');
15. }
16. };
17. aboutToAppear() {
18. try {
19. this.controller.on('controllerAttachStateChange', this.handleControllerAttachStateChange);
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. try {
24. // 注册回调以接收controller绑定状态更改通知
25. this.controller.on('controllerAttachStateChange', (state: webview.ControllerAttachState) => {
26. if (state == webview.ControllerAttachState.UNATTACHED) {
27. console.info('Controller is unattached.');
28. } else {
29. console.info('Controller is attached.');
30. }
31. })
32. } catch (error) {
33. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
34. }
35. }
36. aboutToDisappear() {
37. // 取消指定注册回调
38. // this.controller.off('controllerAttachStateChange', this.handleControllerAttachStateChange);
39. // 取消所有注册回调
40. this.controller.off('controllerAttachStateChange');
41. }

43. build() {
44. Column() {
45. Web({ src: 'www.example.com', controller: this.controller })
46. }
47. }
48. }
```

## waitForAttached20+

PhonePC/2in1TabletTVWearable

waitForAttached(timeout: number):Promise<ControllerAttachState>

异步等待WebViewController与Web组件绑定完成，绑定完成或超时触发回调，通过Promise方式返回当前[ControllerAttachState](arkts-apis-webview-i.md#controllerattachstate20)状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 异步等待时长。  取值范围: [0, 65535]  单位: ms |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ControllerAttachState](arkts-apis-webview-i.md#controllerattachstate20)> | Promise实例，返回当前[ControllerAttachState](arkts-apis-webview-i.md#controllerattachstate20)状态。 |

**示例：**

在初始化阶段设置WebViewController等待绑定完成，超时时间为1000ms。若绑定完成或者超时则会触发回调。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. async aboutToAppear() {
11. this.controller.waitForAttached(1000).then((state: webview.ControllerAttachState) => {
12. if (state == webview.ControllerAttachState.ATTACHED) {
13. // 绑定完成或者超时都会触发回调
14. console.info('Controller is attached.');
15. }
16. })
17. try {
18. const state = await this.controller.waitForAttached(1000);
19. if (state == webview.ControllerAttachState.ATTACHED) {
20. console.info('Controller is attached.');
21. }
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. }

27. build() {
28. Column() {
29. Web({ src: 'www.example.com', controller: this.controller })
30. }
31. }
32. }
```

## setWebDebuggingAccess20+

PhonePC/2in1TabletTVWearable

static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void

设置是否启用无线网页调试功能，默认不开启。

* 当没有指定端口port时，该接口等同于[setWebDebuggingAccess](arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess)接口，ArkWeb会启动一个本地domain socket监听。
* 当指定了端口port时，ArkWeb会启动一个tcp socket监听。这时可以无线调试网页。详情请参考[无线调试](../harmonyos-guides/web-debugging-with-devtools.md#无线调试)。

由于小于1024的端口号作为熟知或系统端口，在操作系统上需要特权才能开启，因此port的取值必须大于1024，否则该接口会抛出异常。

安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患，不建议在应用正式发布版本中启用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | 是 | 设置是否启用网页调试功能。  true表示开启网页调试功能，false表示关闭网页调试功能。 |
| port | number | 是 | 指定DevTools服务的tcp端口号。如果没有指定port，那么该接口等同于[setWebDebuggingAccess](arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess)接口。  取值范围: (1024, 65535]  如果port的值在区间[0, 1024]内，则会抛出BusinessError异常，错误码为17100023。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100023 | The port number is not within the allowed range. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. aboutToAppear(): void {
11. try {
12. webview.WebviewController.setWebDebuggingAccess(true, 8888);
13. } catch (error) {
14. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
15. }
16. }

18. build() {
19. Column() {
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## getProgress20+

PhonePC/2in1TabletTVWearable

getProgress(): number

获取当前网页加载进度。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值**

| 类型 | 说明 |
| --- | --- |
| number | 当前页面加载进度，取值范围[0, 100] |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .onPageBegin(() => {
12. let curProgress = this.controller.getProgress();
13. console.info("current page loading progress is :" + curProgress);
14. })
15. }
16. }
17. }
```

## getHitTest(deprecated)

PhonePC/2in1TabletTVWearable

getHitTest(): WebHitTestType

获取当前被点击区域的元素类型。

说明

从API version11开始支持，从API version 18开始废弃。建议使用[getLastHitTest](arkts-apis-webview-webviewcontroller.md#getlasthittest18)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebHitTestType](arkts-apis-webview-e.md#webhittesttype) | 被点击区域的元素类型。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getHitTest')
13. .onClick(() => {
14. try {
15. let hitTestType = this.controller.getHitTest();
16. console.info("hitTestType: " + hitTestType);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## getHitTestValue(deprecated)

PhonePC/2in1TabletTVWearable

getHitTestValue(): HitTestValue

获取当前被点击区域的元素信息。

说明

从API version11开始支持，从API version 18开始废弃。建议使用[getLastHitTest](arkts-apis-webview-webviewcontroller.md#getlasthittest18)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HitTestValue](arkts-apis-webview-i.md#hittestvalue) | 点击区域的元素信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
12. Button('getHitTestValue')
13. .onClick(() => {
14. try {
15. let hitValue = this.controller.getHitTestValue();
16. console.info("hitType: " + hitValue.type);
17. console.info("extra: " + hitValue.extra);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## avoidVisibleViewportBottom20+

PhonePC/2in1TabletTVWearable

avoidVisibleViewportBottom(avoidHeight: number): void

设置Web网页可视视口底部避让高度。

说明

* avoidHeight有效值区间为[0, Web组件高度]，超出有效值区间时取边界值。
* 该接口高度设置为非0时，Web组件位置和尺寸不变，可视视口向上避让avoidHeight，表现为Web网页内容抬升avoidHeight。该接口一般用于应用自定义网页底部避让区，不建议和点击web网页可编辑区拉起键盘的场景同时使用。同时使用时，键盘弹起避让模式将使用OVERLAYS\_CONTENT。
* 该接口高度设置为0时，Web网页内容可恢复，键盘弹起避让模式将使用[keyboardAvoidMode()](arkts-basic-components-web-attributes.md#keyboardavoidmode12)声明的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| avoidHeight | number | 是 | 设置Web网页可视视口底部避让高度。  单位：vp  合法取值范围：0~Web组件高度  非法值设置行为：小于0取值为0，大于Web组件高度取值为Web组件高度。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. avoidHeight: number = 100;

11. build() {
12. Column() {
13. Button('avoid')
14. .onClick(() => {
15. try {
16. this.controller.avoidVisibleViewportBottom(this.avoidHeight);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Button('reset')
22. .onClick(() => {
23. try {
24. this.controller.avoidVisibleViewportBottom(0);
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. })
29. Web({ src: 'www.example.com', controller: this.controller })
30. }
31. }
32. }
```

## setErrorPageEnabled20+

PhonePC/2in1TabletTVWearable

setErrorPageEnabled(enable: boolean): void

设置是否启用默认错误页。

在当前接口设置为true时如果页面加载发生错误将触发[onOverrideErrorPage](arkts-basic-components-web-events.md#onoverrideerrorpage20)回调，可在该回调接口中设置自定义的错误展示页面。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否启用默认错误页。true表示启用，false表示不启用。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
9. Web({ src: 'www.example.com', controller: this.controller })
10. .onControllerAttached(() => {
11. this.controller.setErrorPageEnabled(true);
12. if (!this.controller.getErrorPageEnabled()) {
13. this.controller.setErrorPageEnabled(true);
14. }
15. })
16. }
17. }
18. }
```

## getErrorPageEnabled20+

PhonePC/2in1TabletTVWearable

getErrorPageEnabled(): boolean

查询是否启用了默认错误页功能。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否启用默认错误页功能。  true：已启用；false：未启用。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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
9. Web({ src: 'www.example.com', controller: this.controller })
10. .onControllerAttached(() => {
11. this.controller.setErrorPageEnabled(true);
12. if (!this.controller.getErrorPageEnabled()) {
13. this.controller.setErrorPageEnabled(true);
14. }
15. })
16. }
17. }
18. }
```

## enablePrivateNetworkAccess20+

PhonePC/2in1TabletTVWearable

static enablePrivateNetworkAccess(enable: boolean): void

设置私有网络访问检查功能（Private Network Access）的启用状态。

启用后，Web组件将对私有网络请求（如访问本地服务器或内网资源）进行CORS预检。它会先发送OPTIONS预检请求，获取目标服务器的显式授权，然后传输实际数据。禁用此功能将跳过安全检查。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用私有网络访问检查功能开关。true表示启用，false表示禁用。 |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .onControllerAttached(() => {
12. // 设置为false时ArkWeb将不再检查私有网络请求是否合法
13. webview.WebviewController.enablePrivateNetworkAccess(false);
14. })
15. }
16. }
17. }
```

## isPrivateNetworkAccessEnabled20+

PhonePC/2in1TabletTVWearable

static isPrivateNetworkAccessEnabled(): boolean

获取Web组件是否启用了私有网络访问检查功能。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Web组件是否启用了私有网络访问检查功能。true表示已启用；false表示已禁用。 |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('isPrivateNetworkAccessEnabled')
12. .onClick(() => {
13. try {
14. let isEnabled: boolean = webview.WebviewController.isPrivateNetworkAccessEnabled();
15. console.info("isPrivateNetworkAccessEnabled:", isEnabled);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. .onControllerAttached(() => {
22. // 设置为false时ArkWeb将不再检查私有网络请求是否合法
23. webview.WebviewController.enablePrivateNetworkAccess(false);
24. })
25. }
26. }
27. }
```

## getBlanklessInfoWithKey20+

PhonePC/2in1TabletTVWearable

getBlanklessInfoWithKey(key: string): BlanklessInfo

获取页面首屏加载预测信息（详细说明见[BlanklessInfo](arkts-apis-webview-i.md#blanklessinfo20)），并开始本次加载过渡帧生成，应用根据此信息确定是否需要启用无白屏加载。必须与[setBlanklessLoadingWithKey](arkts-apis-webview-webviewcontroller.md#setblanklessloadingwithkey20)接口配套使用，并且必须在触发加载页面的接口之前或在onLoadIntercept中调用。需在WebViewController与Web组件绑定后才能使用。

说明

* 持久缓存容量：默认大小为30MB（约30页），可以通过接口[setBlanklessLoadingCacheCapacity](arkts-apis-webview-webviewcontroller.md#setblanklessloadingcachecapacity20)设置缓存容量，具体见该接口说明。超过容量时根据LRU（Least Recently Used，淘汰不常用缓存的策略）机制更新缓存。自动清理超过7天的持久缓存数据，缓存清除后第三次加载页面开始有优化效果。
* 如果发现快照相似度（即[BlanklessInfo](arkts-apis-webview-i.md#blanklessinfo20)中的similarity）极低，请确认key值是否传递正确。
* 调用本接口后，将启用页面加载快照检测及生成过渡帧计算，会产生一定的资源开销。
* 启用无白屏加载的页面会带来一定的资源开销，开销的大小与Web组件的分辨率相关。假设分辨率的宽度和高度分别为：w, h。页面在打开阶段会增加峰值内存，增加约12 \* w \* h B，页面打开后内存回收，不影响稳态内存。增加固态应用缓存的大小，每个页面增加的缓存约w \* h / 10 B，缓存位于应用缓存的位置。
* 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET\_NETWORK\_INFO，具体权限的添加方法请参考[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 唯一标识本页面的key值。  合法取值范围：非空，长度不超过2048个字符。  设置非法值时不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BlanklessInfo](arkts-apis-webview-i.md#blanklessinfo20) | 页面首屏加载预测信息，主要包括首屏相似度预测值，首屏加载耗时预测值，应用需根据此信息来决策是否启用无白屏加载插帧。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com', controller: this.controller })
11. .javaScriptAccess(true)
12. .onLoadIntercept((event) => {
13. // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
14. try {
15. let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
16. if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
17. if (info.similarity >= 0.5 && info.loadingTime < 1000) {
18. this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
19. } else {
20. this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
21. }
22. } else {
23. console.info('getBlankless info err');
24. }
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. return false;
29. })
30. }
31. }
32. }
```

## setBlanklessLoadingWithKey20+

PhonePC/2in1TabletTVWearable

setBlanklessLoadingWithKey(key: string, is\_start: boolean): WebBlanklessErrorCode

设置无白屏加载是否启用，本接口必须与[getBlanklessInfoWithKey](arkts-apis-webview-webviewcontroller.md#getblanklessinfowithkey20)接口配套使用。

说明

* 需在触发页面加载的接口之后调用，其他约束同[getBlanklessInfoWithKey](arkts-apis-webview-webviewcontroller.md#getblanklessinfowithkey20)。
* 页面加载必须在调用本接口的组件中进行。
* 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。
* 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET\_NETWORK\_INFO，具体权限的添加方法请参考[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 唯一标识本页面的key值。必须与getBlanklessInfoWithKey接口的key值相同。  合法取值范围：非空，长度不超过2048个字符。  非法值设置行为：返回错误码WebBlanklessErrorCode，方案不生效。 |
| is\_start | boolean | 是 | 是否启用开始插帧。true：启用，false：不启用。  传入undefined或null时为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebBlanklessErrorCode](arkts-apis-webview-e.md#webblanklesserrorcode20) | 返回接口调用是否成功，具体见[WebBlanklessErrorCode](arkts-apis-webview-e.md#webblanklesserrorcode20)定义。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com', controller: this.controller })
11. .javaScriptAccess(true)
12. .onLoadIntercept((event) => {
13. // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
14. try {
15. let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
16. if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
17. if (info.similarity >= 0.5 && info.loadingTime < 1000) {
18. this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
19. } else {
20. this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
21. }
22. } else {
23. console.info('getBlankless info err');
24. }
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. return false;
29. })
30. }
31. }
32. }
```

## setBlanklessLoadingWithParams23+

PhonePC/2in1TabletTVWearable

setBlanklessLoadingWithParams(key: string, param: BlanklessLoadingParam): WebBlanklessErrorCode

设置白屏插帧的配置参数，本接口必须与[getBlanklessInfoWithKey](arkts-apis-webview-webviewcontroller.md#getblanklessinfowithkey20)接口配套使用。相比于[setBlanklessLoadingWithKey](arkts-apis-webview-webviewcontroller.md#setblanklessloadingwithkey20)，本接口支持白屏插帧更多的参数设置，包括插帧持续时间，缓存数据有效时间，插帧完成后的自定义回调。

说明

* 需在触发页面加载的接口之后调用，其他约束同[getBlanklessInfoWithKey](arkts-apis-webview-webviewcontroller.md#getblanklessinfowithkey20)。
* 页面加载必须在调用本接口的组件中进行。
* 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。
* 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET\_NETWORK\_INFO，具体权限的添加方法请参考[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 唯一标识本页面的key值。必须与getBlanklessInfoWithKey接口的key值相同。  合法取值范围：非空，长度不超过2048个字符。  非法值设置行为：返回错误码WebBlanklessErrorCode，方案不生效。 |
| param | [BlanklessLoadingParam](arkts-apis-webview-i.md#blanklessloadingparam23) | 是 | 白屏插帧加载的各项参数设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebBlanklessErrorCode](arkts-apis-webview-e.md#webblanklesserrorcode20) | 返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com', controller: this.controller })
11. .javaScriptAccess(true)
12. .onLoadIntercept((event) => {
13. try {
14. let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
15. if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
16. let data = new Date(2026, 5, 10, 0, 0, 0, 0);
17. let param: webview.BlanklessLoadingParam = {
18. enable: info.similarity > 0.4 && info.similarity < 2000,
19. duration: info.loadingTime,
20. expirationTime: data.getTime(),
21. callback: (info: webview.BlanklessFrameInterpolationInfo)=>{
22. // 数据监控
23. },
24. };
25. this.controller.setBlanklessLoadingWithParams('http://www.example.com/page1', param);
26. } else {
27. console.info('getBlankless info err');
28. }
29. } catch (error) {
30. console.error(`ErrorCode: ${(error as BusinessError).code},
31. Message: ${(error as BusinessError).message}`);
32. }
33. return false;
34. })
35. }
36. }
37. }
```

## clearBlanklessLoadingCache20+

PhonePC/2in1TabletTVWearable

static clearBlanklessLoadingCache(keys?: Array<string>): void

清除指定key值页面无白屏优化缓存，本接口只清除缓存。

在小程序或Web应用场景中，当页面加载时内容变化显著，可能会出现一次明显的跳变。若对此跳变有所顾虑，可使用该接口清除页面缓存。

说明

* 清除之后的页面，需在第三次加载页面时才会产生优化效果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array<string> | 否 | 清除Blankless优化方案页面的key值列表，key值为[getBlanklessInfoWithKey](arkts-apis-webview-webviewcontroller.md#getblanklessinfowithkey20)中指定过的。  默认值：所有Blankless优化方案缓存的页面key列表。  合法取值范围：长度不超过2048，key列表长度<=100。key和加载页面时输入给ArkWeb的相同。  非法值设置行为：传入undefined/null会抛出异常错误码401；key长度超过2048时该key不生效；长度超过100时，取前100个；当为空时，使用默认值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate");
8. // 假设应用的Web页面在2025/06/10会进行大幅改动，例如商品促销活动等，该提案清除白屏插帧优化缓存
9. webview.WebviewController.initializeWebEngine();
10. let pageUpdateTime: number = Date.UTC(2025, 5, 10, 0, 0, 0, 0);
11. let pageUpdateTime1: number = Date.UTC(2025, 5, 11, 0, 0, 0, 0);
12. let pageUpdateTimeNow: number = Date.now();
13. if (pageUpdateTimeNow > pageUpdateTime && pageUpdateTime < pageUpdateTime1) {
14. // 清除指定页面的白屏插帧方案缓存
15. try {
16. webview.WebviewController.clearBlanklessLoadingCache(["https://www.example.com", "https://www.example1.com"]);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. }
21. AppStorage.setOrCreate("abilityWant", want);
22. console.info("EntryAbility onCreate done");
23. }
24. }
```

## setBlanklessLoadingCacheCapacity20+

PhonePC/2in1TabletTVWearable

static setBlanklessLoadingCacheCapacity(capacity: number): number

设置无白屏加载方案的持久化缓存容量，返回实际生效值。当接口没有显式调用时，默认缓存容量为30MB。当实际缓存超过容量时，将采用淘汰不常用的过渡帧的方式清理。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capacity | number | 是 | 设置持久化缓存设置，单位MB，最大设置不超过100MB。  合法取值范围：[0, 100]，当设置为0时，无缓存空间，则功能全局不开启。  非法值设置行为：小于0时生效值为0，大于100时生效值为100。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回实际生效的容量值，范围0~100。  小于0时生效值为0，大于100时生效值为100。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate");
8. webview.WebviewController.initializeWebEngine();
9. // 设置缓存容量为10MB
10. try {
11. webview.WebviewController.setBlanklessLoadingCacheCapacity(10);
12. } catch (error) {
13. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
14. }
15. AppStorage.setOrCreate("abilityWant", want);
16. console.info("EntryAbility onCreate done");
17. }
18. }
```

## setWebDestroyMode20+

PhonePC/2in1TabletTVWearable

setWebDestroyMode(mode: WebDestroyMode): void

设置Web组件的销毁模式。当Web组件销毁时，销毁模式会影响Web内核资源释放的时机，例如JavaScript运行上下文、渲染上下文等。默认值：[WebDestroyMode.NORMAL\_MODE](arkts-apis-webview-e.md#webdestroymode20)（普通模式），由系统决定销毁时机。应用可设置[WebDestroyMode.FAST\_MODE](arkts-apis-webview-e.md#webdestroymode20)（快速模式），以立即销毁资源，从而提升特定场景的性能。

说明

[WebDestroyMode.FAST\_MODE](arkts-apis-webview-e.md#webdestroymode20)（快速模式）会改变Web组件销毁时机，应用需关注依赖Web组件销毁时机的错误实现，例如：Web组件销毁后仍调用WebviewController的未定义行为，与[WebDestroyMode.NORMAL\_MODE](arkts-apis-webview-e.md#webdestroymode20)（普通模式）相比，销毁时机提前，有更高的几率触发未关联绑定的异常（17100001），建议应用捕捉异常，或者通过[getAttachState](arkts-apis-webview-webviewcontroller.md#getattachstate20)方法查询是否绑定状态，来避免稳定性问题。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebDestroyMode](arkts-apis-webview-e.md#webdestroymode20) | 是 | 设置Web组件的销毁模式。  默认值：WebDestroyMode.NORMAL\_MODE |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { webview } from '@kit.ArkWeb';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. console.info("EntryAbility onCreate");
7. webview.WebviewController.initializeWebEngine();
8. // 设置快速销毁模式
9. webview.WebviewController.setWebDestroyMode(webview.WebDestroyMode.FAST_MODE);
10. AppStorage.setOrCreate("abilityWant", want);
11. console.info("EntryAbility onCreate done");
12. }
13. }
```

## setScrollbarMode23+

PhonePC/2in1TabletTVWearable

static setScrollbarMode(scrollbarMode: ScrollbarMode): void

在Web页面场景，设置全局滚动条模式。不显式调用时，默认为[ScrollbarMode.OVERLAY\_LAYOUT\_SCROLLBAR](arkts-apis-webview-e.md#scrollbarmode23) （非常驻滚动条）。

说明

* 根据滚动条模式，改变当前应用所有web滚动条模式为常驻滚动条或非常驻滚动条。
* 若[forceDisplayScrollBar](arkts-basic-components-web-attributes.md#forcedisplayscrollbar14)接口与当前接口同时设置，forceDisplayScrollBar接口设置不生效。
* 该接口需要在WebViewController绑定Web组件之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollbarMode | [ScrollbarMode](arkts-apis-webview-e.md#scrollbarmode23) | 是 | 滚动条模式。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. aboutToAppear(): void {
9. webview.WebviewController.setScrollbarMode(webview.ScrollbarMode.FORCE_DISPLAY_SCROLLBAR);
10. }
11. build() {
12. Column() {
13. Web({ src: $rawfile('index.html'), controller: this.controller })
14. .height('90%')
15. }
16. }
17. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
6. <title>Demo</title>
7. <style>
8. body {
9. width:2560px;
10. height:2560px;
11. padding-right:170px;
12. padding-left:170px;
13. border:5px solid blueviolet;
14. }
15. </style>
16. </head>
17. <body>
18. Scroll Test
19. </body>
20. </html>
```

## setActiveWebEngineVersion20+

PhonePC/2in1TabletTVWearable

static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void

设置ArkWeb内核版本。若系统不支持指定版本，则设置无效。该接口为全局静态API，须在调用initializeWebEngine前执行，若已加载任何Web组件，则该设置无效。

**遗留内核适配：**

在HarmonyOS 6.0及以后，使用遗留内核时，部分ArkWeb接口不会生效，参考[M114内核在HarmonyOS6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)。

说明

* setActiveWebEngineVersion不支持在异步线程中调用。
* setActiveWebEngineVersion全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| engineVersion | [ArkWebEngineVersion](arkts-apis-webview-e.md#arkwebengineversion20) | 是 | ArkWeb内核版本。 |

**示例：**

本示例以EntryAbility为例，实现了在Ability创建阶段设置ArkWeb内核版本的功能。

```
1. // xxx.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { webview } from '@kit.ArkWeb';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate")
8. webview.WebviewController.setActiveWebEngineVersion(webview.ArkWebEngineVersion.M114)
9. if (webview.WebviewController.getActiveWebEngineVersion() == webview.ArkWebEngineVersion.M114) {
10. console.info("Active Web Engine Version set to M114")
11. }
12. console.info("EntryAbility onCreate done")
13. }
14. }
```

## getActiveWebEngineVersion20+

PhonePC/2in1TabletTVWearable

static getActiveWebEngineVersion(): ArkWebEngineVersion

获取当前ArkWeb内核版本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArkWebEngineVersion](arkts-apis-webview-e.md#arkwebengineversion20) | 返回由[ArkWebEngineVersion](arkts-apis-webview-e.md#arkwebengineversion20)所定义的当前使用的ArkWeb内核版本。 |

**示例：**

请参考[setActiveWebEngineVersion](arkts-apis-webview-webviewcontroller.md#setactivewebengineversion20)。

## isActiveWebEngineEvergreen23+

PhonePC/2in1TabletTVWearable

static isActiveWebEngineEvergreen(): boolean

判断当前系统是否正在使用常青内核，即系统的最新内核。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否正在使用常青内核。正在使用返回true，否则返回false。 |

**示例：**

本示例以EntryAbility为例，实现了在Ability创建阶段判断应用是否正在使用常青内核的功能。

```
1. // xxx.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { webview } from '@kit.ArkWeb';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate")
8. if (webview.WebviewController.isActiveWebEngineEvergreen()) {
9. console.info("Active Web Engine is Evergreen")
10. }
11. console.info("EntryAbility onCreate done")
12. }
13. }
```

## setAutoPreconnect21+

PhonePC/2in1TabletTVWearable

static setAutoPreconnect(enabled: boolean): void

设置Web内核的自动预连接状态。若未设置，默认启用自动预连接。

需要在[initializeWebEngine()](arkts-apis-webview-webviewcontroller.md#initializewebengine)初始化内核或者创建Web组件之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用Web内核自动预连接的开关。true表示启用，false表示禁用。 |

**示例：**

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { webview } from '@kit.ArkWeb';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. webview.WebviewController.setAutoPreconnect(false);
8. webview.WebviewController.initializeWebEngine();
9. AppStorage.setOrCreate("abilityWant", want);
10. }
11. }
```

## isAutoPreconnectEnabled21+

PhonePC/2in1TabletTVWearable

static isAutoPreconnectEnabled(): boolean

查询Web内核的自动预连接状态。

如果没有使用[setAutoPreconnect](arkts-apis-webview-webviewcontroller.md#setautopreconnect21)设置Web内核自动预连接的状态，则默认启用自动预连接，返回true。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Web内核是否启用了自动预连接。true表示已启用；false表示已禁用。 |

**示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. build() {
8. Column() {
9. Button('isAutoPreconnectEnabled')
10. .onClick(() => {
11. try {
12. let isEnabled: boolean = webview.WebviewController.isAutoPreconnectEnabled();
13. console.info("isAutoPreconnectEnabled:", isEnabled);
14. } catch (error) {
15. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
16. }
17. })
18. }
19. }
20. }
```

## getSiteIsolationMode21+

PhonePC/2in1TabletTVWearable

static getSiteIsolationMode(): SiteIsolationMode

查询当前生效的站点隔离模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SiteIsolationMode](arkts-apis-webview-e.md#siteisolationmode21) | 站点隔离模式类型。  getSiteIsolationMode()查询当前生效的站点隔离模式。 |

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
11. Button('getSiteIsolationMode')
12. .onClick(() => {
13. let mode = webview.WebviewController.getSiteIsolationMode();
14. console.info("getSiteIsolationMode: " + mode);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```

## setSiteIsolationMode21+

PhonePC/2in1TabletTVWearable

setSiteIsolationMode(mode: SiteIsolationMode): void

设置站点隔离模式。站点隔离机制将不同源的网站隔离在不同的Render进程中，减少跨域攻击面。例如：PC等设备上，在未启用站点隔离模式时，原有进程模型是每一个Tab对应一个Render进程，开启站点隔离后，一个Tab下不同源的Iframe可在独立的Render进程中运行。

对于仅加载可信网页的第三方应用，可以关闭此功能，以提升性能并减少内存占用，同时减少跨域访问的拦截。默认值根据不同的设备而定，PC/Table采用严格站点隔离[SiteIsolationMode.STRICT](arkts-apis-webview-e.md#siteisolationmode21)，Phone默认部分站点隔离[SiteIsolationMode.PARTIAL](arkts-apis-webview-e.md#siteisolationmode21)。[坚盾守护模式](../harmonyos-guides/web-secure-shield-mode.md)下采用严格站点隔离。

说明

不能在单子进程模式下设置严格站点隔离。

接口只能在初始化时调用一次，不支持反复修改。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SiteIsolationMode](arkts-apis-webview-e.md#siteisolationmode21) | 是 | 设置站点隔离模式。  默认值取决于设备类型和设备模式：PC/Tablet默认严格站点隔离，Phone默认部分站点隔离；坚盾守护模式默认严格站点隔离。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. Possible causes: 1. Site Isolation mode is already set by the developer. 2. Site Isolation mode cannot be strict in single-render-process mode. 3. Site Isolation mode cannot be changed while Secure Shield mode is active. |

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
12. Button('setSiteIsolationMode')
13. .onClick(() => {
14. try {
15. webview.WebviewController.setSiteIsolationMode(webview.SiteIsolationMode.PARTIAL);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## setSocketIdleTimeout21+

PhonePC/2in1TabletTVWearable

static setSocketIdleTimeout(timeout: number): void

设置ArkWeb中已使用过的空闲socket的超时时间，即已使用过的socket可以处于空闲状态的最大时长。如果设置的值与已存在的空闲socket超时时间不同，则根据新的值对已存在的空闲socket进行清理。

未使用该接口设置空闲socket的超时时间时，ArkWeb的默认值为300s。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | ArkWeb中已经使用过的空闲socket的超时时间。  取值范围：[30,300]，单位：s。  小于30时生效值为30，大于300时生效值为300。 |

**示例：**

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { webview } from '@kit.ArkWeb';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. webview.WebviewController.setSocketIdleTimeout(200);
8. AppStorage.setOrCreate("abilityWant", want);
9. }
10. }
```

## setSoftKeyboardBehaviorMode22+

PhonePC/2in1TabletTVWearable

setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void

设置软键盘自动控制模式，当接口没有显式调用时，Web组件失去焦点或获得焦点、状态切换为inactive或active时，系统均会尝试触发软键盘自动隐藏或拉起。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebSoftKeyboardBehaviorMode](arkts-apis-webview-e.md#websoftkeyboardbehaviormode22) | 是 | Web软键盘自动控制模式。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

```
1. // index.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('Web InActive').onClick(() => {
12. this.controller.setSoftKeyboardBehaviorMode(webview.WebSoftKeyboardBehaviorMode.DISABLE_AUTO_KEYBOARD_ON_ACTIVE);
13. })
14. Web({ src: 'www.example.com', controller: this.controller })
15. .keyboardAvoidMode(WebKeyboardAvoidMode.RETURN_TO_UICONTEXT)
16. }
17. }
18. }
```

## resumeMicrophone23+

PhonePC/2in1TabletTVWearable

resumeMicrophone(): void

恢复当前网页麦克风捕获。使用麦克风功能前请在module.json5中添加权限: ohos.permission.MICROPHONE，具体权限的添加方法请参考[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

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

加载的html文件。

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

## pauseMicrophone23+

PhonePC/2in1TabletTVWearable

pauseMicrophone(): void

暂停当前网页麦克风捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

完整示例代码参考[resumeMicrophone](arkts-apis-webview-webviewcontroller.md#resumemicrophone23)。

## stopMicrophone23+

PhonePC/2in1TabletTVWearable

stopMicrophone(): void

停止当前网页麦克风捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

完整示例代码参考[resumeMicrophone](arkts-apis-webview-webviewcontroller.md#resumemicrophone23)。
