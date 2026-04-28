---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicserviceweb
title: AtomicServiceWeb
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > AtomicServiceWeb
category: harmonyos-references
scraped_at: 2026-04-28T08:02:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f9c0d9bd72b1d8fd3808d9751f718553a6ce5c0de346ae57094ed2f9fd37349
---

为开发者提供满足定制化诉求的Web高阶组件，屏蔽原生Web组件中无需关注的接口，并提供JS扩展能力。

说明

* 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

## 需要权限

PhonePC/2in1TabletTVWearable

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AtomicServiceWeb } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)

## AtomicServiceWeb

PhonePC/2in1TabletTVWearable

```
1. AtomicServiceWeb({
2. src: ResourceStr,
3. controller: AtomicServiceWebController,
4. navPathStack?: NavPathStack,
5. mixedMode?: MixedMode,
6. darkMode?: WebDarkMode,
7. forceDarkAccess?: boolean,
8. nestedScroll?: NestedScrollOptions | NestedScrollOptionsExt,
9. onMessage?: Callback<OnMessageEvent>,
10. onErrorReceive?: Callback<OnErrorReceiveEvent>,
11. onHttpErrorReceive?: Callback<OnHttpErrorReceiveEvent>,
12. onPageBegin?: Callback<OnPageBeginEvent>,
13. onPageEnd?: Callback<OnPageEndEvent>,
14. onControllerAttached?: Callback<void>,
15. onLoadIntercept?: Callback<OnLoadInterceptEvent, boolean>,
16. onProgressChange?: Callback<OnProgressChangeEvent>
17. })
```

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | 是 | - | 网页资源地址，访问网络资源需要在AGC配置业务域名，访问本地资源仅支持包内文件（$rawfile）。不支持通过状态变量（例如@State）动态更新地址。加载的网页中支持通过JS SDK提供的接口调用系统能力，具体以JS SDK为准。 |
| controller | [AtomicServiceWebController](ohos-atomicservice-atomicserviceweb.md#atomicservicewebcontroller) | 是 | @ObjectLink | 通过AtomicServiceWebController可以控制AtomicServiceWeb组件各种行为。 |
| navPathStack | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 否 | - | 路由栈信息。当使用NavDestination作为页面的根容器时，需传入NavDestination容器对应的NavPathStack处理页面路由。 |
| mixedMode | [MixedMode](arkts-basic-components-web-e.md#mixedmode) | 否 | @Prop | 设置是否允许加载超文本传输协议（HTTP）和超文本传输安全协议（HTTPS）混合内容，默认不允许加载HTTP和HTTPS混合内容。 |
| darkMode | [WebDarkMode](arkts-basic-components-web-e.md#webdarkmode9) | 否 | @Prop | 设置Web深色模式，默认关闭。 |
| forceDarkAccess | boolean | 否 | @Prop | 设置网页是否开启强制深色模式。true表示设置网页开启强制深色模式，false表示设置网页不开启强制深色模式。默认值：false。该属性仅在darkMode开启深色模式时生效。 |
| nestedScroll15+ | [NestedScrollOptions](ts-container-scrollable-common.md#nestedscrolloptions10对象说明) | [NestedScrollOptionsExt](arkts-basic-components-web-i.md#nestedscrolloptionsext14) | 否 | @Prop | 设置嵌套滚动选项。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| onMessage | Callback<[OnMessageEvent](ohos-atomicservice-atomicserviceweb.md#onmessageevent)> | 否 | - | H5页面通过JS SDK的postMessage()发送消息后，Web组件对应的页面返回或销毁时，触发该回调。 |
| onErrorReceive | Callback<[OnErrorReceiveEvent](ohos-atomicservice-atomicserviceweb.md#onerrorreceiveevent)> | 否 | - | 网页加载遇到错误时触发该回调。出于性能考虑，建议此回调中尽量执行简单逻辑。在无网络的情况下，触发此回调。 |
| onHttpErrorReceive | Callback<[OnHttpErrorReceiveEvent](ohos-atomicservice-atomicserviceweb.md#onhttperrorreceiveevent)> | 否 | - | 网页加载资源遇到的HTTP错误（响应码>=400)时触发该回调。 |
| onPageBegin | Callback<[OnPageBeginEvent](ohos-atomicservice-atomicserviceweb.md#onpagebeginevent)> | 否 | - | 网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。 |
| onPageEnd | Callback<[OnPageEndEvent](ohos-atomicservice-atomicserviceweb.md#onpageendevent)> | 否 | - | 网页加载完成时触发该回调，且只在主frame触发。 |
| onControllerAttached | Callback<void> | 否 | - | 当Controller成功绑定到Web组件时触发该回调。 |
| onLoadIntercept | [OnLoadInterceptCallback](ohos-atomicservice-atomicserviceweb.md#onloadinterceptcallback) | 否 | - | 当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。默认允许加载。 |
| onProgressChange | Callback<[OnProgressChangeEvent](arkts-basic-components-web-i.md#onprogresschangeevent12)> | 否 | - | 网页加载进度变化时触发该回调。 |

## AtomicServiceWebController

PhonePC/2in1TabletTVWearable

通过AtomicServiceWebController可以控制AtomicServiceWeb组件各种行为。一个AtomicServiceWebController对象只能控制一个AtomicServiceWeb组件，且必须在AtomicServiceWeb组件和AtomicServiceWebController绑定后，才能调用AtomicServiceWebController上的方法。

**装饰器类型：** @Observed

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getUserAgent

PhonePC/2in1TabletTVWearable

getUserAgent(): string

获取当前默认用户代理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 默认用户代理。默认User-Agent定义与使用场景请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### getCustomUserAgent

PhonePC/2in1TabletTVWearable

getCustomUserAgent(): string

获取自定义用户代理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用户自定义代理信息。默认User-Agent定义与使用场景请参考[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### setCustomUserAgent

PhonePC/2in1TabletTVWearable

setCustomUserAgent(userAgent: string): void

设置自定义用户代理，会覆盖系统的用户代理。

建议在onControllerAttached回调事件中设置User-Agent，设置方式请参考示例。不建议将User-Agent设置在onLoadIntercept回调事件中，会概率性出现设置失败。

说明

当Web组件src设置了url，且未在onControllerAttached回调事件中设置User-Agent。再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 用户自定义代理信息。建议先使用[getUserAgent](ohos-atomicservice-atomicserviceweb.md#getuseragent)获取当前默认用户代理，在此基础上追加自定义用户代理信息。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### refresh

PhonePC/2in1TabletTVWearable

refresh(): void

调用此接口通知AtomicServiceWeb组件刷新网页。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### forward

PhonePC/2in1TabletTVWearable

forward(): void

按照历史栈，前进一个页面。一般结合[accessForward](ohos-atomicservice-atomicserviceweb.md#accessforward)一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### backward

PhonePC/2in1TabletTVWearable

backward(): void

按照历史栈，后退一个页面。一般结合[accessBackward](ohos-atomicservice-atomicserviceweb.md#accessbackward)一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### accessForward

PhonePC/2in1TabletTVWearable

accessForward(): boolean

当前页面是否可前进，即当前页面是否有前进历史记录。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可以前进返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### accessBackward

PhonePC/2in1TabletTVWearable

accessBackward(): boolean

当前页面是否可后退，即当前页面是否有返回历史记录。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 可以后退返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### accessStep

PhonePC/2in1TabletTVWearable

accessStep(step: number): boolean

当前页面是否可前进或者后退给定的step步。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | number | 是 | 要跳转的步数，正数代表前进，负数代表后退。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 页面是否可前进或者后退给定的step步。返回true表示可以前进或者后退，返回false表示不可以前进或后退。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |

### loadUrl

PhonePC/2in1TabletTVWearable

loadUrl(url: string | Resource, headers?: Array<WebHeader>): void

加载指定的URL。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | [Resource](ts-types.md#resource) | 是 | 需要加载的 URL。 |
| headers | Array<[WebHeader](ohos-atomicservice-atomicserviceweb.md#webheader)> | 否 | URL的附加HTTP请求头。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-webview.md).

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The AtomicServiceWebController must be associated with a AtomicServiceWeb component. |
| 17100002 | Invalid url. |
| 17100003 | Invalid resource path or file type. |

## WebHeader

PhonePC/2in1TabletTVWearable

Web组件返回的请求/响应头对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| headerKey | string | 否 | 否 | 请求/响应头的key。 |
| headerValue | string | 否 | 否 | 请求/响应头的value。 |

## OnMessageEvent

PhonePC/2in1TabletTVWearable

定义页面回退或销毁时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | object[] | 否 | 否 | 消息列表。 |

## OnErrorReceiveEvent

PhonePC/2in1TabletTVWearable

定义网页加载遇到错误时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | [WebResourceRequest](arkts-basic-components-web-webresourcerequest.md) | 否 | 否 | 网页请求的封装信息。 |
| error | [WebResourceError](arkts-basic-components-web-webresourceerror.md) | 否 | 否 | 网页加载资源错误的封装信息 。 |

## OnHttpErrorReceiveEvent

PhonePC/2in1TabletTVWearable

定义网页收到加载资源加载HTTP错误时触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | [WebResourceRequest](arkts-basic-components-web-webresourcerequest.md) | 否 | 否 | 网页请求的封装信息。 |
| response | [WebResourceResponse](arkts-basic-components-web-webresourceresponse.md) | 否 | 否 | 资源响应的封装信息。 |

## OnPageBeginEvent

PhonePC/2in1TabletTVWearable

定义网页加载开始时触发的函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |

## OnPageEndEvent

PhonePC/2in1TabletTVWearable

定义网页加载结束时触发的函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 页面的URL地址。 |

## OnLoadInterceptEvent

PhonePC/2in1TabletTVWearable

当资源加载被拦截时，加载拦截事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | [WebResourceRequest](arkts-basic-components-web-webresourcerequest.md) | 否 | 否 | 网页请求的封装信息。 |

## OnProgressChangeEvent

PhonePC/2in1TabletTVWearable

定义网页加载进度变化时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| newProgress | number | 否 | 否 | 新的加载进度，取值范围为0到100的整数。 |

## OnLoadInterceptCallback

PhonePC/2in1TabletTVWearable

type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean

资源加载被拦截时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | OnLoadInterceptEvent | 是 | 当资源加载被拦截时，加载拦截事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源是否被拦截，true表示被拦截。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)

## 示例

PhonePC/2in1TabletTVWearable

### 示例1

加载本地网页。

```
1. // xxx.ets
2. import { AtomicServiceWeb, AtomicServiceWebController } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct WebComponent {
7. @State controller: AtomicServiceWebController = new AtomicServiceWebController();

9. build() {
10. Column() {
11. AtomicServiceWeb({ src: $rawfile("index.html"), controller: this.controller })
12. }
13. }
14. }
```

### 示例2

加载在线网页。

```
1. // xxx.ets
2. import { AtomicServiceWeb, AtomicServiceWebController } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct WebComponent {
7. @State controller: AtomicServiceWebController = new AtomicServiceWebController();

9. build() {
10. Column() {
11. AtomicServiceWeb({ src: 'https://www.example.com', controller: this.controller })
12. }
13. }
14. }
```

### 示例3

NavDestination容器中加载网页。

```
1. // xxx.ets
2. import { AtomicServiceWeb, AtomicServiceWebController } from '@kit.ArkUI';

4. @Builder
5. export function WebComponentBuilder(name: string, param: Object) {
6. WebComponent()
7. }

9. @Component
10. struct WebComponent {
11. navPathStack: NavPathStack = new NavPathStack();
12. @State controller: AtomicServiceWebController = new AtomicServiceWebController();

14. build() {
15. NavDestination() {
16. AtomicServiceWeb({ src: $rawfile("index.html"), controller: this.controller, navPathStack: this.navPathStack })
17. }
18. .onReady((context: NavDestinationContext) => {
19. this.navPathStack = context.pathStack;
20. })
21. }
22. }
```

### 示例4

设置onMessage()事件回调。

```
1. // xxx.ets
2. import { AtomicServiceWeb, AtomicServiceWebController, OnMessageEvent } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct WebComponent {
7. @State controller: AtomicServiceWebController = new AtomicServiceWebController();

9. build() {
10. Column() {
11. AtomicServiceWeb({
12. src: $rawfile("index.html"),
13. controller: this.controller,
14. // H5页面点击“发送消息”后，再点击“返回上一页”，触发该回调
15. onMessage: (event: OnMessageEvent) => {
16. console.info(`[AtomicServiceWebLog] onMessage data = ${JSON.stringify(event.data)}`);
17. }
18. })
19. }
20. }
21. }
```

```
1. <!DOCTYPE html>
2. <html>
3. <meta charset="utf-8">
4. <!-- 引入JS SDK文件 -->
5. <script src="../js/atomicservice-sdk.js" type="text/javascript"></script>
6. <body>
7. <h1>JS SDK - postMessage()</h1>
8. <br/>
9. <button type="button" onclick="postMessage({ name: 'Jerry', age: 18 });">发送消息</button>
10. <br/>
11. <button type="button" onclick="back();">返回上一页</button>
12. </body>
13. <script type="text/javascript">
14. function postMessage(data) {
15. // JS SDK提供的发送消息接口
16. has.asWeb.postMessage({
17. data: data,
18. callback: (err, res) => {
19. if (err) {
20. console.error(`[AtomicServiceWebLog H5] postMessage error err. Code: ${err.code}, message: ${err.message}`);
21. } else {
22. console.info(`[AtomicServiceWebLog H5] postMessage success res = ${JSON.stringify(res)}`);
23. }
24. }
25. });
26. }

28. function back() {
29. // JS SDK提供的Router路由回退接口
30. has.router.back({
31. delta: 1
32. });
33. }
34. </script>
35. </html>
```

### 示例5

设置网页加载事件回调。

```
1. // xxx.ets
2. import {
3. AtomicServiceWeb,
4. AtomicServiceWebController,
5. OnErrorReceiveEvent,
6. OnHttpErrorReceiveEvent,
7. OnPageBeginEvent,
8. OnPageEndEvent
9. } from '@kit.ArkUI';

11. @Entry
12. @Component
13. struct WebComponent {
14. @State controller: AtomicServiceWebController = new AtomicServiceWebController();

16. build() {
17. Column() {
18. AtomicServiceWeb({
19. src: $rawfile('index.html'),
20. controller: this.controller,
21. // 网页加载遇到错误时触发该回调
22. onErrorReceive: (event: OnErrorReceiveEvent) => {
23. console.info(`AtomicServiceWebLog onErrorReceive event = ${JSON.stringify({
24. requestUrl: event.request?.getRequestUrl(),
25. requestMethod: event.request?.getRequestMethod(),
26. errorCode: event.error?.getErrorCode(),
27. errorInfo: event.error?.getErrorInfo()
28. })}`);
29. },
30. // 网页加载遇到HTTP资源加载错误时触发该回调
31. onHttpErrorReceive: (event: OnHttpErrorReceiveEvent) => {
32. console.info(`AtomicServiceWebLog onHttpErrorReceive event = ${JSON.stringify({
33. requestUrl: event.request?.getRequestUrl(),
34. requestMethod: event.request?.getRequestMethod(),
35. responseCode: event.response?.getResponseCode(),
36. responseData: event.response?.getResponseData(),
37. })}`);
38. },
39. // 页面开始加载，触发该回调
40. onPageBegin: (event: OnPageBeginEvent) => {
41. console.info(`AtomicServiceWebLog onPageBegin event = ${JSON.stringify({
42. url: event.url
43. })}`);
44. },
45. // 页面加载完成，触发该回调
46. onPageEnd: (event: OnPageEndEvent) => {
47. console.info(`AtomicServiceWebLog onPageEnd event = ${JSON.stringify({
48. url: event.url
49. })}`);
50. }
51. })
52. }
53. }
54. }
```

### 示例6

AtomicServiceWeb跟AtomicServiceWebController的使用示例。

```
1. // xxx.ets
2. import {
3. AtomicServiceWeb,
4. AtomicServiceWebController,
5. OnErrorReceiveEvent,
6. OnHttpErrorReceiveEvent,
7. OnPageBeginEvent,
8. OnPageEndEvent,
9. OnMessageEvent,
10. OnLoadInterceptEvent,
11. OnProgressChangeEvent
12. } from '@kit.ArkUI';

14. @Entry
15. @Component
16. struct WebComponent {
17. @State darkMode: WebDarkMode = WebDarkMode.On;
18. @State forceDarkAccess: boolean = true;
19. @State mixedMode: MixedMode = MixedMode.None;
20. @State controller: AtomicServiceWebController = new AtomicServiceWebController();
21. @State num: number = 1;

23. build() {
24. Column() {
25. Button('accessForward').onClick(() => {
26. console.info(`AtomicServiceWebLog accessForward = ${this.controller.accessForward()}`);
27. })
28. Button('accessBackward').onClick(() => {
29. console.info(`AtomicServiceWebLog accessBackward = ${this.controller.accessBackward()}`);
30. })
31. Button('accessStep').onClick(() => {
32. console.info(`AtomicServiceWebLog accessStep = ${this.controller.accessStep(1)}`);
33. })
34. Button('forward').onClick(() => {
35. console.info(`AtomicServiceWebLog forward = ${this.controller.forward()}`);
36. })
37. Button('backward').onClick(() => {
38. console.info(`AtomicServiceWebLog backward = ${this.controller.backward()}`);
39. })
40. Button('refresh').onClick(() => {
41. console.info(`AtomicServiceWebLog refresh = ${this.controller.refresh()}`);
42. })
43. Button('loadUrl').onClick(() => {
44. console.info(`AtomicServiceWebLog loadUrl = ${this.controller.loadUrl('https://www.baidu.com/')}`);
45. })
46. Button('深色模式').onClick(() => {
47. this.forceDarkAccess = !this.forceDarkAccess;
48. })
49. Button('mixedMode').onClick(() => {
50. this.mixedMode = this.mixedMode == MixedMode.None ? MixedMode.All : MixedMode.None;
51. })
52. Button('点击').onClick(() => {
53. console.info(`AtomicServiceWebLog getUserAgent = ${this.controller.getUserAgent()}`);
54. console.info(`AtomicServiceWebLog getCustomUserAgent = ${this.controller.getCustomUserAgent()}`);
55. this.controller.setCustomUserAgent('test' + this.num++);

57. console.info(`AtomicServiceWebLog getUserAgent after set = ${this.controller.getUserAgent()}`);
58. console.info(`AtomicServiceWebLog getCustomUserAgent after set = ${this.controller.getCustomUserAgent()}`);
59. })
60. AtomicServiceWeb({
61. src: 'https://www.example.com',
62. mixedMode: this.mixedMode,
63. darkMode: this.darkMode,
64. forceDarkAccess: this.forceDarkAccess,
65. controller: this.controller,
66. onControllerAttached: () => {
67. console.info("AtomicServiceWebLog onControllerAttached call back success");
68. },
69. onLoadIntercept: (event: OnLoadInterceptEvent) => {
70. console.info("AtomicServiceWebLog onLoadIntercept call back success " + JSON.stringify({
71. getRequestUrl: event.data.getRequestUrl(),
72. getRequestMethod: event.data.getRequestMethod(),
73. getRequestHeader: event.data.getRequestHeader(),
74. isRequestGesture: event.data.isRequestGesture(),
75. isMainFrame: event.data.isMainFrame(),
76. isRedirect: event.data.isRedirect(),
77. }))
78. return false;
79. },
80. onProgressChange: (event: OnProgressChangeEvent) => {
81. console.info("AtomicServiceWebLog onProgressChange call back success " + JSON.stringify(event));
82. },
83. onMessage: (event: OnMessageEvent) => {
84. console.info("onMessage call back success " + JSON.stringify(event));
85. },
86. onPageBegin: (event: OnPageBeginEvent) => {
87. console.info("onPageBegin call back success " + JSON.stringify(event));
88. },
89. onPageEnd: (event: OnPageEndEvent) => {
90. console.info("onPageEnd call back success " + JSON.stringify(event));
91. },
92. onHttpErrorReceive: (event: OnHttpErrorReceiveEvent) => {
93. console.info("onHttpErrorReceive call back success " + JSON.stringify(event));
94. },
95. onErrorReceive: (event: OnErrorReceiveEvent) => {
96. console.info("onErrorReceive call back success " + JSON.stringify(event));
97. }
98. })
99. }
100. }
101. }
```

### 示例7

设置嵌套滚动。

```
1. import { AtomicServiceWeb, AtomicServiceWebController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AtomicServiceNestedScroll {
6. @State controller: AtomicServiceWebController = new AtomicServiceWebController();
7. @State mode: string = 'PARALLEL模式（点击切换）';
8. @State nestedScroll: NestedScrollOptions | NestedScrollOptionsExt = {
9. scrollForward: NestedScrollMode.PARALLEL,
10. scrollBackward: NestedScrollMode.PARALLEL
11. };

13. build() {
14. Scroll() {
15. Column() {
16. Text("嵌套AsWeb-头部")
17. .height("15%")
18. .width("100%")
19. .fontSize(30)
20. .backgroundColor(Color.Yellow)
21. Button(this.mode)
22. .margin({ top: 10, bottom: 10 })
23. .onClick(() => {
24. if (!(this.nestedScroll as NestedScrollOptions).scrollForward) {
25. this.mode = 'SELF_FIRST模式（点击切换）';
26. this.nestedScroll = {
27. scrollForward: NestedScrollMode.SELF_FIRST,
28. scrollBackward: NestedScrollMode.SELF_FIRST
29. }
30. } else {
31. this.mode = 'PARENT_FIRST模式（点击切换）';
32. this.nestedScroll = {
33. scrollUp: NestedScrollMode.PARENT_FIRST,
34. scrollDown: NestedScrollMode.PARENT_FIRST
35. }
36. }
37. })
38. AtomicServiceWeb({
39. src: 'https://www.example.com',
40. controller: this.controller,
41. nestedScroll: this.nestedScroll
42. })
43. Text("嵌套AsWeb-尾部")
44. .height("15%")
45. .width("100%")
46. .fontSize(30)
47. .backgroundColor(Color.Yellow)
48. }
49. }
50. }
51. }
```
