---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-consolemessage
title: Class (ConsoleMessage)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (ConsoleMessage)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a8a11109f1477b6dc2564b45be7179df9c0d85dce6bb9d8b34ed27e6b704e56
---

Web组件获取控制台信息对象。示例代码参考[onConsole事件](arkts-basic-components-web-events.md#onconsole)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)

ConsoleMessage的构造函数。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[constructor](arkts-basic-components-web-consolemessage.md#constructor9)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | ConsoleMessage的日志输出信息。 |
| sourceId | string | 是 | 网页源文件的路径和文件名。 |
| lineNumber | number | 是 | ConsoleMessage的行号。 |
| messageLevel | [MessageLevel](arkts-basic-components-web-e.md#messagelevel) | 是 | ConsoleMessage的日志级别。 |

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

ConsoleMessage的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## getLineNumber

PhonePC/2in1TabletTVWearable

getLineNumber(): number

获取ConsoleMessage的行数。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回ConsoleMessage的行数。 |

## getMessage

PhonePC/2in1TabletTVWearable

getMessage(): string

获取ConsoleMessage的日志信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回ConsoleMessage的日志信息。 |

## getMessageLevel

PhonePC/2in1TabletTVWearable

getMessageLevel(): MessageLevel

获取ConsoleMessage的信息级别。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MessageLevel](arkts-basic-components-web-e.md#messagelevel) | 返回ConsoleMessage的信息级别。 |

## getSourceId

PhonePC/2in1TabletTVWearable

getSourceId(): string

获取网页源文件路径和文件名。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回网页源文件路径和文件名。 |

## getSource23+

PhonePC/2in1TabletTVWearable

getSource(): ConsoleMessageSource

获取ConsoleMessage的日志来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConsoleMessageSource](arkts-basic-components-web-e.md#consolemessagesource23) | 返回ConsoleMessage的日志来源。 |
