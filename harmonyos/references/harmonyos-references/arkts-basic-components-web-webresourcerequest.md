---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourcerequest
title: Class (WebResourceRequest)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebResourceRequest)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:57be431985545b5e23942ed7e8ecd05cda7db784af8da265d52376897aab9c09
---

Web组件获取资源请求对象。示例代码参考[onErrorReceive事件](arkts-basic-components-web-events.md#onerrorreceive)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor

PhonePC/2in1TabletTVWearable

constructor()

WebResourceRequest的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## getRequestHeader

PhonePC/2in1TabletTVWearable

getRequestHeader(): Array<Header>

获取资源请求头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Header](arkts-basic-components-web-i.md#header)> | 返回资源请求头信息。 |

## getRequestUrl

PhonePC/2in1TabletTVWearable

getRequestUrl(): string

获取资源请求的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回资源请求的URL信息。 |

## isMainFrame

PhonePC/2in1TabletTVWearable

isMainFrame(): boolean

判断资源请求是否为主frame。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源请求是否为主frame。  true表示返回资源请求为主frame，false表示返回资源请求不为主frame。 |

## isRedirect

PhonePC/2in1TabletTVWearable

isRedirect(): boolean

判断资源请求是否被服务端重定向。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源请求是否被服务端重定向。  true表示返回资源请求被服务端重定向，false表示返回资源请求未被服务端重定向。 |

## isRequestGesture

PhonePC/2in1TabletTVWearable

isRequestGesture(): boolean

获取资源请求是否与手势（如点击）相关联。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源请求是否与手势（如点击）相关联。  true表示返回资源请求与手势（如点击）相关联，false表示返回资源请求与手势（如点击）不相关联。 |

## getRequestMethod9+

PhonePC/2in1TabletTVWearable

getRequestMethod(): string

获取请求方法。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回请求方法。 |
