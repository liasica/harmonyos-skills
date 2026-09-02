---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-textconfig
title: InputMethod_TextConfig
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 结构体 > InputMethod_TextConfig
category: harmonyos-references
scraped_at: 2026-09-02T14:52:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:93e321aa84a9d1c13f46f00bf9de3a96b25fa14c03d11653028193282ec2a86f
---

```c
typedef struct InputMethod_TextConfig InputMethod_TextConfig
```

## 概述

文本输入框的文本输入行为配置结构体，用于输入框向输入法框架传递核心输入规则，输入法框架根据配置执行相应输入行为。通过配置输入属性（如输入类型、文本格式等），能够满足不同场景下的输入需求，提升用户输入体验，适用于需要精细化控制输入行为的文本输入场景。该结构体为不透明类型（opaque type），调用者不可直接访问其内部成员，仅可通过本模块提供的函数接口进行操作。

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

**所在头文件：** [inputmethod\_text\_config\_capi.h](capi-inputmethod-text-config-capi-h.md)

## 结构体用途

InputMethod\_TextConfig承载编辑框的配置信息，包括输入类型、回车键类型、预上屏支持、选区范围、光标信息、避让信息、窗口ID、占位符文本、abilityName等。该配置信息在[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)回调中使用，开发者需在回调内对config参数设置各配置项，输入法框架据此调整键盘布局和输入行为。

## 包含关系

InputMethod\_TextConfig内部包含以下子结构体信息：

* [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)：光标信息，包括光标位置、高度等。可通过[OH\_TextConfig\_GetCursorInfo](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getcursorinfo)获取，返回双指针（函数内部分配内存）。
* [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)：避让信息，包括避让区域的位置和尺寸。可通过[OH\_TextConfig\_GetTextAvoidInfo](capi-inputmethod-text-config-capi-h.md#oh_textconfig_gettextavoidinfo)获取，返回双指针（函数内部分配内存）。

相关函数：

* 创建/销毁函数：

| 函数 | 描述 |
| --- | --- |
| [OH\_TextConfig\_Create](capi-inputmethod-text-config-capi-h.md#oh_textconfig_create) | 创建一个新的InputMethod\_TextConfig实例。 |
| [OH\_TextConfig\_Destroy](capi-inputmethod-text-config-capi-h.md#oh_textconfig_destroy) | 销毁一个InputMethod\_TextConfig实例。 |

* 设置函数（Set\*）：

| 函数 | 描述 |
| --- | --- |
| [OH\_TextConfig\_SetInputType](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setinputtype) | 设置文本配置信息中的输入框类型。 |
| [OH\_TextConfig\_SetEnterKeyType](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setenterkeytype) | 设置文本配置信息中的回车键功能类型。 |
| [OH\_TextConfig\_SetPreviewTextSupport](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setpreviewtextsupport) | 设置预上屏支持情况。 |
| [OH\_TextConfig\_SetSelection](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setselection) | 设置选中文本范围。 |
| [OH\_TextConfig\_SetWindowId](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setwindowid) | 设置所属窗口的窗口ID。 |
| [OH\_TextConfig\_SetPlaceholder](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setplaceholder) | 设置占位符文本信息。 |
| [OH\_TextConfig\_SetAbilityName](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setabilityname) | 设置abilityName信息。 |
| [OH\_TextConfig\_SetConsumeKeyEvents](capi-inputmethod-text-config-capi-h.md#oh_textconfig_setconsumekeyevents) | 将编辑框是否具有完整处理字母、字符、功能等按键的能力设置到文本配置信息中。  **起始版本：** 26.0.0 |

* 获取函数（Get\*）：

| 函数 | 描述 |
| --- | --- |
| [OH\_TextConfig\_GetInputType](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getinputtype) | 获取输入框类型。 |
| [OH\_TextConfig\_GetEnterKeyType](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getenterkeytype) | 获取回车键功能类型。 |
| [OH\_TextConfig\_IsPreviewTextSupported](capi-inputmethod-text-config-capi-h.md#oh_textconfig_ispreviewtextsupported) | 获取是否支持预上屏。 |
| [OH\_TextConfig\_GetCursorInfo](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getcursorinfo) | 获取光标信息（双指针，函数内部分配内存）。 |
| [OH\_TextConfig\_GetTextAvoidInfo](capi-inputmethod-text-config-capi-h.md#oh_textconfig_gettextavoidinfo) | 获取避让信息（双指针，函数内部分配内存）。 |
| [OH\_TextConfig\_GetSelection](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getselection) | 获取选区范围信息。 |
| [OH\_TextConfig\_GetWindowId](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getwindowid) | 获取所属窗口的窗口ID。 |
| [OH\_TextConfig\_GetPlaceholder](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getplaceholder) | 获取占位符文本信息。 |
| [OH\_TextConfig\_GetAbilityName](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getabilityname) | 获取abilityName信息。 |
| [OH\_TextConfig\_GetConsumeKeyEvents](capi-inputmethod-text-config-capi-h.md#oh_textconfig_getconsumekeyevents) | 获取文本配置中编辑框是否具有完整处理字母、字符、功能等按键的能力。  **起始版本：** 26.0.0 |
