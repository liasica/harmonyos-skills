---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler
title: Class (WebSchemeHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebSchemeHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:09+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:46f4369e4346b2b7154ac369bde0a639405b24a5a7fef2ea5217aba04c483d38
---

用于拦截指定scheme的请求的拦截器。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## onRequestStart12+

PhonePC/2in1TabletTVWearable

onRequestStart(callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void

当请求开始时的回调，在该回调函数中可以决定是否拦截该请求。当回调返回false时，表示不拦截此请求，此时handler失效；当回调返回true时，表示拦截此请求。

说明

* 重定向后的URL无法单独拦截。如需拦截，必须同时对原始请求URL进行拦截。

**系统能力：** SystemCapability.Web.Webview.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (request: [WebSchemeHandlerRequest](arkts-apis-webview-webschemehandlerrequest.md), handler: [WebResourceHandler](arkts-apis-webview-webresourcehandler.md)) => boolean | 是 | 拦截对应scheme请求开始时触发的回调。request为请求，handler用于提供自定义的返回头以及返回体给Web组件，返回值表示该请求是否拦截。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. // xxx.ets
2. import { webview, WebNetErrorList } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { buffer } from '@kit.ArkTS';

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();
10. schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();
11. htmlData: string = "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>";

13. build() {
14. Column() {
15. Web({ src: 'https://www.example.com', controller: this.controller })
16. .onControllerAttached(() => {
17. try {
18. this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
19. console.info("[schemeHandler] onRequestStart");
20. try {
21. console.info("[schemeHandler] onRequestStart url:" + request.getRequestUrl());
22. console.info("[schemeHandler] onRequestStart method:" + request.getRequestMethod());
23. console.info("[schemeHandler] onRequestStart referrer:" + request.getReferrer());
24. console.info("[schemeHandler] onRequestStart isMainFrame:" + request.isMainFrame());
25. console.info("[schemeHandler] onRequestStart hasGesture:" + request.hasGesture());
26. console.info("[schemeHandler] onRequestStart header size:" + request.getHeader().length);
27. console.info("[schemeHandler] onRequestStart resource type:" + request.getRequestResourceType());
28. console.info("[schemeHandler] onRequestStart frame url:" + request.getFrameUrl());
29. let header = request.getHeader();
30. for (let i = 0; i < header.length; i++) {
31. console.info("[schemeHandler] onRequestStart header:" + header[i].headerKey + " " + header[i].headerValue);
32. }
33. let stream = request.getHttpBodyStream();
34. if (stream) {
35. console.info("[schemeHandler] onRequestStart has http body stream");
36. } else {
37. console.info("[schemeHandler] onRequestStart has no http body stream");
38. }
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }

43. if (request.getRequestUrl().endsWith("example.com")) {
44. return false;
45. }

47. let response = new webview.WebSchemeHandlerResponse();
48. try {
49. response.setNetErrorCode(WebNetErrorList.NET_OK);
50. response.setStatus(200);
51. response.setStatusText("OK");
52. response.setMimeType("text/html");
53. response.setEncoding("utf-8");
54. response.setHeaderByName("header1", "value1", false);
55. } catch (error) {
56. console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
57. }

59. // 调用 didFinish/didFail 前需要优先调用 didReceiveResponse 将构造的响应头传递给被拦截的请求。
60. let buf = buffer.from(this.htmlData)
61. try {
62. if (buf.length == 0) {
63. console.info("[schemeHandler] length 0");
64. resourceHandler.didReceiveResponse(response);
65. // 如果认为buf.length为0是正常情况，则调用resourceHandler.didFinish，否则调用resourceHandler.didFail
66. resourceHandler.didFail(WebNetErrorList.ERR_FAILED);
67. } else {
68. console.info("[schemeHandler] length 1");
69. resourceHandler.didReceiveResponse(response);
70. resourceHandler.didReceiveResponseBody(buf.buffer);
71. resourceHandler.didFinish();
72. }
73. } catch (error) {
74. console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
75. }
76. return true;
77. })

79. this.schemeHandler.onRequestStop((request: webview.WebSchemeHandlerRequest) => {
80. console.info("[schemeHandler] onRequestStop");
81. });

83. this.controller.setWebSchemeHandler('https', this.schemeHandler);
84. } catch (error) {
85. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
86. }
87. })
88. .javaScriptAccess(true)
89. .domStorageAccess(true)
90. }
91. }
92. }
```

## onRequestStop12+

PhonePC/2in1TabletTVWearable

onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void

当请求完成时的回调，仅当[onRequestStart](arkts-apis-webview-webschemehandler.md#onrequeststart12)回调决定拦截此请求时触发。触发的时机有以下两点：

1.WebResourceHandler调用didFail或者didFinish。

2.此请求因为其他原因中断。

**系统能力：** SystemCapability.Web.Webview.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[WebSchemeHandlerRequest](arkts-apis-webview-webschemehandlerrequest.md)> | 是 | 对应请求结束的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

完整示例代码参考[onRequestStart](arkts-apis-webview-webschemehandler.md#onrequeststart12)。
