---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webkeyboardcontroller
title: Class (WebKeyboardController)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebKeyboardController)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:08f066b4b3ec4c107559b75158d1d45a77b61847174f3bb7742288f505d98aaa
---

WebKeyboardController是ArkWeb提供的用于控制Web组件自定义键盘行为的控制器类。当Web页面中的输入框需要弹出键盘时，开发者可通过[onInterceptKeyboardAttach](arkts-basic-components-web-events.md#oninterceptkeyboardattach12)事件拦截系统默认键盘的挂载，并使用WebKeyboardController向当前聚焦的Web输入框执行插入字符、前向/后向删除、发送Enter等功能键以及关闭自定义键盘等操作。该类适用于需要为Web场景实现自定义安全键盘、表情键盘、手写键盘或业务专属输入面板的应用，使开发者能够完全接管Web输入框的键盘输入逻辑。

**说明** 

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class从API version 12开始支持。
* 示例效果请以真机运行为准。

## constructor12+

constructor()

WebKeyboardController的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## insertText12+

insertText(text: string): void

Web输入框中插入字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 在Web输入框当前光标位置插入文本。若存在选中文本则替换为该文本；触发输入事件；光标移动到插入文本末尾。 |

## deleteForward12+

deleteForward(length: number): void

删除光标前面的指定长度字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 删除光标前面的指定长度字符。  取值范围：[-2147483648 , 2147483647]，当参数值大于字符长度时，默认删除光标前面所有字符；参数值为负数时，不执行删除操作。 |

## deleteBackward12+

deleteBackward(length: number): void

删除光标后面的指定长度字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 删除光标后面的指定长度字符。  取值范围：[-2147483648 , 2147483647]，当参数值大于字符长度时，默认删除光标后面所有字符；参数值为负数时，不执行删除操作。 |

## sendFunctionKey12+

sendFunctionKey(key: number): void

插入功能按键，目前仅支持Enter键类型，取值见[EnterKeyType](js-apis-inputmethod.md#enterkeytype10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | number | 是 | 功能键类型，仅支持Enter键。 |

## close12+

close(): void

关闭自定义键盘。

**系统能力：** SystemCapability.Web.Webview.Core
