---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-jsmessageext
title: Class (JsMessageExt)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (JsMessageExt)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:14c203971841911f7013c2ef841d02e3333baee56e3a0bd1d6d5bdc730cb3486
---

[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)接口执行脚本返回的数据对象。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 10开始支持。
* 示例效果请以真机运行为准。

## getType10+

PhonePC/2in1TabletTVWearable

getType(): JsMessageType

获取数据对象的类型。完整示例代码参考[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsMessageType](arkts-apis-webview-e.md#jsmessagetype10) | [runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)接口脚本执行后返回的结果的类型。 |

## getString10+

PhonePC/2in1TabletTVWearable

getString(): string

获取数据对象的字符串类型数据。完整示例代码参考[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回字符串类型的数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |

## getNumber10+

PhonePC/2in1TabletTVWearable

getNumber(): number

获取数据对象的数值类型数据。完整示例代码参考[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回数值类型的数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |

## getBoolean10+

PhonePC/2in1TabletTVWearable

getBoolean(): boolean

获取数据对象的布尔类型数据。完整示例代码参考[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回布尔类型的数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |

## getArrayBuffer10+

PhonePC/2in1TabletTVWearable

getArrayBuffer(): ArrayBuffer

获取数据对象的原始二进制数据。完整示例代码参考[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回原始二进制数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |

## getArray10+

PhonePC/2in1TabletTVWearable

getArray(): Array<string | number | boolean>

获取数据对象的数组类型数据。完整示例代码参考[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string | number | boolean> | 返回数组类型的数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |

## getErrorDescription22+

PhonePC/2in1TabletTVWearable

getErrorDescription(): string | null

获取JS执行的异常信息。完整示例代码参考[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | null | 若JavaScript脚本执行过程中发生异常，或返回值为object类型，系统会将其格式化为"Not support type: <{exception|object}>"字符串返回，该字符串长度不超过2048个字符，超长部分将被截断；若object对象中包含callback类型的成员，则序列化时将自动忽略该成员；其余情况，接口均返回null。 |
