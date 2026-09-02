---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageext
title: Class (WebMessageExt)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebMessageExt)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5572caf9ed379440843d7f1aeea8afc05ac3a75055afa3dd4ff760aeeb8e3f32
---

WebMessageExt是[WebMessagePort](arkts-apis-webview-webmessageport.md)接口中用于接收和发送的拓展数据对象，支持多种数据类型：字符串（STRING）、数值（NUMBER）、布尔值（BOOLEAN）、二进制数据（ARRAY\_BUFFER）、数组（ARRAY）和错误对象（ERROR）。该类为ArkTS侧与HTML5侧之间的跨语言消息通信提供了结构化的数据载体，通过setType/getType设置和获取数据类型，再通过对应的setter/getter方法读写具体数据。

WebMessageExt与WebMessagePort配合使用：WebMessagePort负责消息通道的建立和消息的收发，WebMessageExt作为消息的有效载荷在不同语言运行时之间传递。使用扩展接口[postMessageEventExt](arkts-apis-webview-webmessageport.md#postmessageeventext10)/[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)时，消息载体即为WebMessageExt对象。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 10开始支持。
* 示例效果请以真机运行为准。

## getType10+

getType(): WebMessageType

获取数据对象的类型。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebMessageType](arkts-apis-webview-e.md#webmessagetype10) | [WebMessagePort](arkts-apis-webview-webmessageport.md)接口所支持的数据类型。 |

## getString10+

getString(): string

获取数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

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

getNumber(): number

获取数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

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

getBoolean(): boolean

获取数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

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

getArrayBuffer(): ArrayBuffer

获取数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

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

getArray(): Array<string | number | boolean>

获取数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

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

## getError10+

getError(): Error

获取数据对象的错误类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Error | 返回错误对象类型的数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |

## setType10+

setType(type: WebMessageType): void

设置数据对象的类型。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [WebMessageType](arkts-apis-webview-e.md#webmessagetype10) | 是 | [WebMessagePort](arkts-apis-webview-webmessageport.md)接口所支持的数据类型。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## setString10+

setString(message: string): void

设置数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## setNumber10+

setNumber(message: number): void

设置数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | number | 是 | 数值类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## setBoolean10+

setBoolean(message: boolean): void

设置数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | boolean | 是 | 布尔类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## setArrayBuffer10+

setArrayBuffer(message: ArrayBuffer): void

设置数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | ArrayBuffer | 是 | 原始二进制类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## setArray10+

setArray(message: Array<string | number | boolean>): void

设置数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Array<string | number | boolean> | 是 | 数组类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## setError10+

setError(message: Error): void

设置数据对象的错误对象类型数据。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Error | 是 | 错误对象类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
