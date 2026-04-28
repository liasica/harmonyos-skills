---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-scheme-handler
title: 拦截Web组件发起的网络请求
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页加载与浏览记录 > 拦截Web组件发起的网络请求
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0bf6aed5e0b9ea94505fed72acafb03f6c9a3517444b7bb942fd8b4fec6c8a57
---

应用可以通过[onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)拦截Web组件发起的网络请求，也可以通过SchemeHandler来拦截Web组件发起的网络请求。SchemeHandler提供了ArkTS与NDK两套接口。

注意

* onInterceptRequest接口中无法获取Post Data，如果想要获取Post Data需使用SchemeHandler机制来进行拦截。

## 网络请求拦截处理 (onInterceptRequest接口)

通过onInterceptRequest接口拦截Web组件发起的网络请求可参考[自定义页面请求响应](web-resource-interception-request-mgmt.md)。

## 网络请求拦截处理 (SchemeHandler机制)

通过SchemeHandler机制来拦截Web组件发起的网络请求。

### 为Web组件设置SchemeHandler

ArkWeb支持通过SchemeHandler拦截Web组件或者ServiceWorker发出的HTTP(s)及自定义协议的请求。

当Web内核发出相应scheme请求时，会触发为该scheme设置的SchemeHandler的回调。SchemeHandler包含请求开始与请求结束两个回调，应用需要在请求开始的回调中告知Web内核是否进行拦截，在请求结束后清理相关的资源，避免内存泄漏。

请求开始的回调：

NDK：[ArkWeb\_OnRequestStart](../harmonyos-references/capi-arkweb-scheme-handler-h.md#arkweb_onrequeststart)

ArkTS：[onRequestStart](../harmonyos-references/arkts-apis-webview-webschemehandler.md#onrequeststart12)

请求结束的回调：

NDK：[ArkWeb\_OnRequestStop](../harmonyos-references/capi-arkweb-scheme-handler-h.md#arkweb_onrequeststop)

ArkTS：[onRequestStop](../harmonyos-references/arkts-apis-webview-webschemehandler.md#onrequeststop12)

注意

* 需要在Web组件初始化之后设置SchemeHandler，否则会设置失败。
* 若想要拦截Web组件发出的第一个请求，可以通过[initializeWebEngine](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#initializewebengine)方法提前进行Web组件初始化，再设置SchemeHandler实现拦截。详细代码请参考[完整示例](web-scheme-handler.md#完整示例)。

在C++中，通过NDK接口为Web组件设置SchemeHandler：

```
1. // 创建一个ArkWeb_SchemeHandler对象。
2. ArkWeb_SchemeHandler *schemeHandler;
3. OH_ArkWeb_CreateSchemeHandler(&schemeHandler);

5. // 为ArkWeb_SchemeHandler设置ArkWeb_OnRequestStart与ArkWeb_OnRequestStop回调。
6. OH_ArkWebSchemeHandler_SetOnRequestStart(schemeHandler, OnURLRequestStart);
7. OH_ArkWebSchemeHandler_SetOnRequestStop(schemeHandler, OnURLRequestStop);

9. // 拦截webTag为“scheme-handler”的Web组件发出的scheme为“https”的请求。
10. OH_ArkWeb_SetSchemeHandler("https", "scheme-handler", schemeHandler);
11. OH_ArkWebServiceWorker_SetSchemeHandler("https", schemeHandler);

13. // 拦截webTag为“scheme-handler”的Web组件发出的scheme为“custom”的请求。
14. OH_ArkWeb_SetSchemeHandler("custom", "scheme-handler", schemeHandler);
15. OH_ArkWebServiceWorker_SetSchemeHandler("custom", schemeHandler);
```

在ArkTS中，为Web组件设置SchemeHandler：

```
1. // 初始化WebView控制器和Scheme处理器。
2. controller: webview.WebviewController = new webview.WebviewController();
3. schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();
4. // 为当前Web组件设置SchemeHandler。
5. this.controller.setWebSchemeHandler('https', this.schemeHandler);
```

### 设置自定义scheme需要遵循的规则

如果要拦截自定义scheme的请求，需要在Web组件初始化之前将自定义scheme注册到Web内核，初始化后再注册会失败。

Web组件的创建会触发Web内核的初始化。另外ArkWeb还提供了initializeWebEngine接口，用于单独进行Web初始化。

在NDK中可以在ets侧先调用testNapi.registerCustomSchemes注册自定义协议，然后调用[initializeWebEngine](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#initializewebengine)初始化Web内核，示例如下：

```
1. export default class EntryAbility extends UIAbility {
2. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
3. // 注册三方协议的配置。
4. testNapi.registerCustomSchemes();
5. // 初始化Web组件内核，该操作会初始化Browser进程以及创建BrowserContext。
6. webview.WebviewController.initializeWebEngine();
7. // 设置SchemeHandler。
8. testNapi.setSchemeHandler();
9. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebSchemeHandler/entry/src/main/ets/entryability/EntryAbility.ets#L22-L33)

testNapi.registerCustomSchemes的C++实现：

```
1. // 注册“custom“ scheme到Web组件，并指定该scheme需要遵循标准的scheme规则，允许该scheme发出跨域请求。
2. OH_ArkWeb_RegisterCustomSchemes("custom", ARKWEB_SCHEME_OPTION_STANDARD | ARKWEB_SCHEME_OPTION_CORS_ENABLED);
3. // 注册“custom-local” scheme到Web组件，并指定该scheme需要遵循与“file” scheme一样的规则。
4. OH_ArkWeb_RegisterCustomSchemes("custom-local", ARKWEB_SCHEME_OPTION_LOCAL);
5. // 注册“custom-csp-bypassing”到Web组件，并指定该scheme需要遵循标准的scheme规则，允许忽略CSP检查。
6. OH_ArkWeb_RegisterCustomSchemes("custom-csp-bypassing", ARKWEB_SCHEME_OPTION_CSP_BYPASSING | ARKWEB_SCHEME_OPTION_STANDARD);
7. // 注册“custom-isolated”到Web组件，并指定该scheme的请求必须从相同scheme加载的网页中发起。
8. OH_ArkWeb_RegisterCustomSchemes("custom-isolated", ARKWEB_SCHEME_OPTION_DISPLAY_ISOLATED);
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebSchemeHandler/entry/src/main/cpp/hello.cpp#L19-L28)

在ArkTS中可以通过customizeSchemes注册自定义协议，示例如下：

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

### 获取被拦截请求的信息

在请求开始的回调中，应用可以获取请求的基本信息包括url、method、referrer、request headers、resource type、post data等。支持获取PUT/POST类请求的上传数据，数据类型支持BYTES、FILE、BLOB和CHUNKED。

在NDK中，获取被拦截请求的信息：

```
1. char* url;
2. OH_ArkWebResourceRequest_GetUrl(resourceRequest_, &url);
3. OH_ArkWeb_ReleaseString(url);

5. char* method;
6. OH_ArkWebResourceRequest_GetMethod(resourceRequest_, &method);
7. OH_ArkWeb_ReleaseString(method);

9. int32_t resourceType = OH_ArkWebResourceRequest_GetResourceType(resourceRequest_);

11. char* frameUrl;
12. OH_ArkWebResourceRequest_GetFrameUrl(resourceRequest_, &frameUrl);
13. OH_ArkWeb_ReleaseString(frameUrl);

15. // 获取被拦截请求的上传数据。
16. OH_ArkWebResourceRequest_GetHttpBodyStream(resourceRequest(), &stream_);
17. // 设置读取上传数据的读回调。
18. OH_ArkWebHttpBodyStream_SetReadCallback(stream_, ReadCallback);
19. // 初始化ArkWeb_HttpBodyStream，其它OH_ArkWebHttpBodyStream*函数需要在初始化进行调用。
20. OH_ArkWebHttpBodyStream_Init(stream_, InitCallback);
```

在ArkTS中，获取被拦截请求的信息：

```
1. this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
2. try {
3. console.info("[schemeHandler] onRequestStart url:" + request.getRequestUrl());
4. console.info("[schemeHandler] onRequestStart method:" + request.getRequestMethod());
5. console.info("[schemeHandler] onRequestStart referrer:" + request.getReferrer());
6. console.info("[schemeHandler] onRequestStart isMainFrame:" + request.isMainFrame());
7. console.info("[schemeHandler] onRequestStart hasGesture:" + request.hasGesture());
8. console.info("[schemeHandler] onRequestStart header size:" + request.getHeader().length);
9. console.info("[schemeHandler] onRequestStart resource type:" + request.getRequestResourceType());
10. console.info("[schemeHandler] onRequestStart frame url:" + request.getFrameUrl());
11. let header = request.getHeader();
12. for (let i = 0; i < header.length; i++) {
13. console.info("[schemeHandler] onRequestStart header:" + header[i].headerKey + " " + header[i].headerValue);
14. }
15. let stream = request.getHttpBodyStream();
16. if (stream) {
17. console.info("[schemeHandler] onRequestStart has http body stream");
18. } else {
19. console.info("[schemeHandler] onRequestStart has no http body stream");
20. }
21. } catch (error) {
22. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
23. }
24. return true;
25. })
```

### 拦截Web内核的请求，并为被拦截的请求提供自定义的响应信息

网络拦截支持在worker线程以流方式为被拦截的请求提供自定义的响应信息。也可用特定的网络错误码结束当前被拦截的请求。

错误码定义：

NDK：[网络错误码(arkweb\_net\_error\_list.h)](../harmonyos-references/capi-arkweb-net-error-list-h.md)。

ArkTS：[网络错误码(@ohos.web.netErrorList.d.ts)](../harmonyos-references/arkts-apis-neterrorlist.md)。

注意

* ArkWeb不支持自定义错误码，请使用ArkWeb提供的错误码来结束请求。

在NDK中，为被拦截的请求提供自定义的响应信息：

```
1. // 为被拦截的请求创建一个响应头。
2. ArkWeb_Response *response;
3. OH_ArkWeb_CreateResponse(&response);

5. // 设置HTTP状态码为200。
6. OH_ArkWebResponse_SetStatus(response, 200);
7. // 设置响应头中的字符集，指明内容使用UTF-8编码。
8. OH_ArkWebResponse_SetCharset(response, "UTF-8");
9. // 设置响应头中的"content-length"，指明响应体的大小。
10. OH_ArkWebResponse_SetHeaderByName(response, "content-length", "1024", false);
11. // 将为被拦截的请求创建的响应头传递给Web组件。
12. OH_ArkWebResourceHandler_DidReceiveResponse(resourceHandler, response);

14. // 该函数可以调用多次，数据可以分多份来传递给Web组件。
15. OH_ArkWebResourceHandler_DidReceiveData(resourceHandler, buffer, bufLen);

17. // 读取响应体结束，当然如果希望该请求失败的话也可以通过调用OH_ArkWebResourceHandler_DidFailWithError(resourceHandler_, errorCode);
18. // 传递给Web组件一个错误码并结束该请求。
19. OH_ArkWebResourceHandler_DidFinish(resourceHandler);
```

在ArkTS中，为被拦截的请求提供自定义的响应信息：

```
1. this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
2. let response = new webview.WebSchemeHandlerResponse();
3. try {
4. // 设置网络错误代码为OK，表示请求成功。
5. response.setNetErrorCode(WebNetErrorList.NET_OK);

7. // 设置HTTP状态码为200，表示请求处理成功。
8. response.setStatus(200);

10. // 设置状态文本为"OK"，用于描述状态码。
11. response.setStatusText("OK");

13. // 设置MIME类型为"text/html"，指明返回数据的类型为HTML文档。
14. response.setMimeType("text/html");

16. // 设置编码方式为"utf-8"，指明内容使用UTF-8编码。
17. response.setEncoding("utf-8");

19. // 设置自定义响应头"header1"的值为"value1"，false表示不覆盖已经存在的同名头部。
20. response.setHeaderByName("header1", "value1", false);

22. // 调用didReceiveResponse将构造的响应头传递给被拦截的请求。
23. resourceHandler.didReceiveResponse(response);

25. // 调用didReceiveResponseBody将构造的响应体传递给被拦截的请求。
26. resourceHandler.didReceiveResponseBody(buf.buffer);

28. // 调用didFinish通知Web组件被拦截的请求已经完成。
29. resourceHandler.didFinish();
30. } catch (error) {
31. console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. return true;
34. })
```

当希望通过[OH\_ArkWebResourceHandler\_DidFailWithError](../harmonyos-references/capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didfailwitherror)或者[didFail(code: WebNetErrorList)](../harmonyos-references/arkts-apis-webview-webresourcehandler.md#didfail12)结束当前请求时，需要在调用该接口之前通过[OH\_ArkWebResourceHandler\_DidReceiveResponse](../harmonyos-references/capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse)或者[didReceiveResponse](../harmonyos-references/arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)返回给Web内核一个响应头，否则无法结束请求。

从API version 20开始，可以直接通过[OH\_ArkWebResourceHandler\_DidFailWithErrorV2](../harmonyos-references/capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didfailwitherrorv2)或者[didFail(code: WebNetErrorList, completeIfNoResponse: boolean)](../harmonyos-references/arkts-apis-webview-webresourcehandler.md#didfail20)结束网络请求，不再依赖必须通过[OH\_ArkWebResourceHandler\_DidReceiveResponse](../harmonyos-references/capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse)或者[didReceiveResponse](../harmonyos-references/arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)返回给Web内核一个响应头。

NDK示例：

```
1. void OnRequestStart(){
2. // 直接返回网络错误码ARKWEB_ERR_CONNECTION_FAILED结束该请求。
3. OH_ArkWebResourceHandler_DidFailWithErrorV2(resourceHandler_, ARKWEB_ERR_CONNECTION_FAILED, true);
4. }
```

ArkTS示例：

```
1. this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
2. // 直接调用didFail(WebNetErrorList.ERR_CONNECTION_FAILED, true)，自动构造一个网络请求错误ERR_CONNECTION_FAILED。
3. resourceHandler.didFail(WebNetErrorList.ERR_CONNECTION_FAILED, true);
4. return true;
5. })
```

## 完整示例

[拦截Web组件发起的网络请求](https://gitcode.com/harmonyos_samples/guide-snippets/tree/master/ArkWeb/ArkWebSchemeHandler)
