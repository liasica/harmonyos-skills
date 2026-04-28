---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webresourcehandler
title: Class (WebResourceHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebResourceHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:19fa3e4ba67d6ec28a13088a922f489bece268efd58558f8121a7400f1264283
---

通过WebResourceHandler，可以提供自定义的返回头以及返回体给Web组件。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## didReceiveResponse12+

PhonePC/2in1TabletTVWearable

didReceiveResponse(response: WebSchemeHandlerResponse): void

将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | [WebSchemeHandlerResponse](arkts-apis-webview-webschemehandlerresponse.md) | 是 | 该拦截请求的响应。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](arkts-apis-webview-webschemehandler.md#onrequeststart12)。

## didReceiveResponseBody12+

PhonePC/2in1TabletTVWearable

didReceiveResponseBody(data: ArrayBuffer): void

将构造的响应体传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 响应体数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](arkts-apis-webview-webschemehandler.md#onrequeststart12)。

## didFinish12+

PhonePC/2in1TabletTVWearable

didFinish(): void

通知Web组件被拦截的请求已经完成，并且没有更多的数据可用，调用前需要优先调用[didReceiveResponse](arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](arkts-apis-webview-webschemehandler.md#onrequeststart12)。

## didFail12+

PhonePC/2in1TabletTVWearable

didFail(code: WebNetErrorList): void

通知ArkWeb内核被拦截请求应该返回失败，调用前需要优先调用[didReceiveResponse](arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | [WebNetErrorList](arkts-apis-neterrorlist.md#webneterrorlist) | 是 | 网络错误码。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](arkts-apis-webview-webschemehandler.md#onrequeststart12)。

## didFail20+

PhonePC/2in1TabletTVWearable

didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void

通知ArkWeb内核，被拦截请求应返回失败。若completeIfNoResponse为false，调用前需优先调用[didReceiveResponse](arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)，将构造的响应头传递给被拦截的请求。若completeIfNoResponse为true，且调用前未调用[didReceiveResponse](arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)，则自动生成一个响应头，网络错误码为-104，详情参见[WebNetErrorList](arkts-apis-neterrorlist.md#webneterrorlist)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | [WebNetErrorList](arkts-apis-neterrorlist.md#webneterrorlist) | 是 | 网络错误码。 |
| completeIfNoResponse | boolean | 是 | 调用当前接口时，若之前未调用过[didReceiveResponse](arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)，是否完成此次网络请求；值为true时，若之前未调用过[didReceiveResponse](arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)，则会自动生成一个response以完成此次网络请求，网络错误码为-104；值为false时，将等待应用调用[didReceiveResponse](arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)并传入response，不会直接完成此次网络请求。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100101 | The errorCode is either ARKWEB\_NET\_OK or outside the range of error codes in WebNetErrorList. |
| 17100021 | The resource handler is invalid. |

**示例：**

```
1. // xxx.ets
2. import { webview, WebNetErrorList } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

11. build() {
12. Column() {
13. Web({ src: 'https://www.example.com', controller: this.controller })
14. .onControllerAttached(() => {
15. try {
16. this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
17. console.info("[schemeHandler] onRequestStart");
18. try {
19. console.info("[schemeHandler] onRequestStart url:" + request.getRequestUrl());
20. console.info("[schemeHandler] onRequestStart method:" + request.getRequestMethod());
21. console.info("[schemeHandler] onRequestStart referrer:" + request.getReferrer());
22. console.info("[schemeHandler] onRequestStart isMainFrame:" + request.isMainFrame());
23. console.info("[schemeHandler] onRequestStart hasGesture:" + request.hasGesture());
24. console.info("[schemeHandler] onRequestStart header size:" + request.getHeader().length);
25. console.info("[schemeHandler] onRequestStart resource type:" + request.getRequestResourceType());
26. console.info("[schemeHandler] onRequestStart frame url:" + request.getFrameUrl());
27. let header = request.getHeader();
28. for (let i = 0; i < header.length; i++) {
29. console.info("[schemeHandler] onRequestStart header:" + header[i].headerKey + " " + header[i].headerValue);
30. }
31. let stream = request.getHttpBodyStream();
32. if (stream) {
33. console.info("[schemeHandler] onRequestStart has http body stream");
34. } else {
35. console.info("[schemeHandler] onRequestStart has no http body stream");
36. }
37. } catch (error) {
38. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
39. }

41. if (request.getRequestUrl().endsWith("example.com")) {
42. return false;
43. }

45. try {
46. // 直接调用didFail(WebNetErrorList.ERR_FAILED, true)，自动构造一个网络请求错误ERR_CONNECTION_FAILED
47. resourceHandler.didFail(WebNetErrorList.ERR_FAILED, true);
48. } catch (error) {
49. // 当error.code为17100101(The errorCode is either ARKWEB_NET_OK or outside the range of error codes in WebNetErrorList)
50. // 且didFail(code: WebNetErrorList, completeIfNoResponse: boolean)的code值不为null时，接口会继续调用不会中断。
51. console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
52. }
53. return true;
54. })

56. this.schemeHandler.onRequestStop((request: webview.WebSchemeHandlerRequest) => {
57. console.info("[schemeHandler] onRequestStop");
58. });

60. this.controller.setWebSchemeHandler('https', this.schemeHandler);
61. } catch (error) {
62. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
63. }
64. })
65. .javaScriptAccess(true)
66. .domStorageAccess(true)
67. }
68. }
69. }
```
