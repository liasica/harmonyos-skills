---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceerror
title: Class (WebResourceError)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebResourceError)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e39605217798d399b8e113cc478acf05a19b0e521ee3e5d97b4b929ffeaea3a4
---

WebResourceError是Web组件中提供资源加载失败错误信息的类。该错误对象通过onErrorReceive和onHttpErrorReceive事件回调提供给应用，封装了错误详情用于调试和错误处理。通常与WebResourceRequest配合使用以确定哪个资源加载失败。示例代码参考[onErrorReceive事件](arkts-basic-components-web-events.md#onerrorreceive)。

**说明** 

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor

constructor()

WebResourceError的构造函数，创建WebResourceError对象，用于封装Web组件资源加载失败时的错误信息。

**系统能力：** SystemCapability.Web.Webview.Core

## getErrorCode

getErrorCode(): number

获取加载资源的错误码。用于判断资源加载失败的具体原因（如网络错误、服务器错误、权限问题等），以便开发者根据错误类型采取相应的处理策略（如重试、提示用户、降级显示等）。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回加载资源的错误码。错误码含义参考[WebNetErrorList](arkts-apis-neterrorlist.md#webneterrorlist)或HTTP协议状态码。 |

## getErrorInfo

getErrorInfo(): string

获取加载资源的错误信息。用于详细描述资源加载失败的具体原因，开发者可将错误信息输出到日志用于调试分析，或向用户显示友好的错误提示。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回加载资源的错误信息。 |
