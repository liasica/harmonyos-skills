---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse
title: Class (WebSchemeHandlerResponse)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebSchemeHandlerResponse)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:09+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:72f7e7f3a8316893951ac75dcf1b5527e9224e0d4c7d84867b2b619177ade483
---

请求的响应，可以为被拦截的请求创建一个Response并填充自定义的内容返回给Web组件。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## constructor12+

PhonePC/2in1TabletTVWearable

constructor()

Response的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

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
13. Button('response').onClick(() => {
14. let response = new webview.WebSchemeHandlerResponse();
15. try {
16. response.setUrl("http://www.example.com")
17. response.setStatus(200)
18. response.setStatusText("OK")
19. response.setMimeType("text/html")
20. response.setEncoding("utf-8")
21. response.setHeaderByName("header1", "value1", false)
22. response.setNetErrorCode(WebNetErrorList.NET_OK)
23. console.info("[schemeHandler] getUrl:" + response.getUrl())
24. console.info("[schemeHandler] getStatus:" + response.getStatus())
25. console.info("[schemeHandler] getStatusText:" + response.getStatusText())
26. console.info("[schemeHandler] getMimeType:" + response.getMimeType())
27. console.info("[schemeHandler] getEncoding:" + response.getEncoding())
28. console.info("[schemeHandler] getHeaderByValue:" + response.getHeaderByName("header1"))
29. console.info("[schemeHandler] getNetErrorCode:" + response.getNetErrorCode())

31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Web({ src: 'https://www.example.com', controller: this.controller })
36. }
37. }
38. }
```

## setUrl12+

PhonePC/2in1TabletTVWearable

setUrl(url: string): void

给当前的Response设置重定向或因HSTS而更改后的URL，设置了url后会触发请求的跳转。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 即将要跳转的URL。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setNetErrorCode12+

PhonePC/2in1TabletTVWearable

setNetErrorCode(code: WebNetErrorList): void

给当前的Response设置网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | [WebNetErrorList](arkts-apis-neterrorlist.md#webneterrorlist) | 是 | 网络错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## setStatus12+

PhonePC/2in1TabletTVWearable

setStatus(code: number): void

给当前的Response设置HTTP状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | Http状态码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## setStatusText12+

PhonePC/2in1TabletTVWearable

setStatusText(text: string): void

给当前的Response设置状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 状态文本。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## setMimeType12+

PhonePC/2in1TabletTVWearable

setMimeType(type: string): void

给当前的Response设置媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 媒体类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## setEncoding12+

PhonePC/2in1TabletTVWearable

setEncoding(encoding: string): void

给当前的Response设置字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 是 | 字符集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## setHeaderByName12+

PhonePC/2in1TabletTVWearable

setHeaderByName(name: string, value: string, overwrite: boolean): void

给当前的Response设置头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 头部（header）的名称。 |
| value | string | 是 | 头部（header）的值。 |
| overwrite | boolean | 是 | 如果为true，将覆盖现有的头部，否则不覆盖。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## getUrl12+

PhonePC/2in1TabletTVWearable

getUrl(): string

获取重定向或由于HSTS而更改后的URL。

风险提示：如果想获取URL来做JavascriptProxy通信接口认证，请使用[getLastJavascriptProxyCallingFrameUrl12+](arkts-apis-webview-webviewcontroller.md#getlastjavascriptproxycallingframeurl12)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 获取经过重定向或由于HSTS而更改后的URL。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## getNetErrorCode12+

PhonePC/2in1TabletTVWearable

getNetErrorCode(): WebNetErrorList

获取Response的网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebNetErrorList](arkts-apis-neterrorlist.md#webneterrorlist) | 获取Response的网络错误码。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## getStatus12+

PhonePC/2in1TabletTVWearable

getStatus(): number

获取Response的Http状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取Response的Http状态码。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## getStatusText12+

PhonePC/2in1TabletTVWearable

getStatusText(): string

获取Response的状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 状态文本。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## getMimeType12+

PhonePC/2in1TabletTVWearable

getMimeType(): string

获取Response的媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 媒体类型。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## getEncoding12+

PhonePC/2in1TabletTVWearable

getEncoding(): string

获取Response的字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符集。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。

## getHeaderByName12+

PhonePC/2in1TabletTVWearable

getHeaderByName(name: string): string

按名称获取Response头部字段值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 头部（header）的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 头部（header）的值。 |

**示例：**

完整示例代码参考[constructor](arkts-apis-webview-webschemehandlerresponse.md#constructor12)。
