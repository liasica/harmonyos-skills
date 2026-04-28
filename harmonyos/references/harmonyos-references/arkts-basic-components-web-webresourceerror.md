---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceerror
title: Class (WebResourceError)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebResourceError)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:179bcf1ca1d73db40067a57e712084c7a03727bda2fc27a4084e48af7d7e0f9c
---

Web组件资源管理错误信息对象。示例代码参考[onErrorReceive事件](arkts-basic-components-web-events.md#onerrorreceive)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor

PhonePC/2in1TabletTVWearable

constructor()

WebResourceError的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## getErrorCode

PhonePC/2in1TabletTVWearable

getErrorCode(): number

获取加载资源的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回加载资源的错误码。错误码含义参考[WebNetErrorList](arkts-apis-neterrorlist.md#webneterrorlist)、HTTP协议状态码。 |

## getErrorInfo

PhonePC/2in1TabletTVWearable

getErrorInfo(): string

获取加载资源的错误信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回加载资源的错误信息。 |
