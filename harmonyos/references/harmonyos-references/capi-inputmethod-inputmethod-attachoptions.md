---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-attachoptions
title: InputMethod_AttachOptions
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 结构体 > InputMethod_AttachOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:52:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4a0a646e7e9d35a04382accd324fde40ce9ac9a6cfe833581f59524c5368ba8b
---

```c
typedef struct InputMethod_AttachOptions InputMethod_AttachOptions
```

## 概述

InputMethod\_AttachOptions是输入法绑定选项的不透明类型（opaque type），用于在应用绑定输入法服务时携带配置参数，控制绑定时的初始行为。

用途：作为OH\_InputMethodController\_Attach和OH\_InputMethodController\_AttachWithUIContext的必要参数，用于配置绑定输入法时的行为选项，包括：

* 是否在绑定时自动显示键盘（showKeyboard）：控制绑定完成后键盘是否立即弹出。
* 请求键盘的原因（requestKeyboardReason）：标识触发输入法拉起的场景原因（如触摸点击、鼠标点击或应用主动调用），帮助系统优化输入体验。

使用场景：

* showKeyboard=true：适用于输入框获得焦点后需要立即输入的场景（如文本编辑框），绑定后键盘自动弹出。
* showKeyboard=false：适用于先建立交互通道但暂不需要键盘的场景（如搜索框），绑定后键盘不弹出，后续通过ShowKeyboard主动拉起。
* requestKeyboardReason：适用于需要向系统说明触发输入法的场景原因，帮助系统选择合适的输入策略。

相关函数：

| 函数 | 说明 |
| --- | --- |
| [OH\_AttachOptions\_Create](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_create) | 创建AttachOptions实例。 |
| [OH\_AttachOptions\_CreateWithRequestKeyboardReason](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_createwithrequestkeyboardreason) | 创建AttachOptions实例并指定requestKeyboardReason。 |
| [OH\_AttachOptions\_Destroy](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_destroy) | 销毁AttachOptions实例。 |
| [OH\_AttachOptions\_IsShowKeyboard](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_isshowkeyboard) | 获取showKeyboard值。 |
| [OH\_AttachOptions\_GetRequestKeyboardReason](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_getrequestkeyboardreason) | 获取requestKeyboardReason值。 |

与其他结构体的关系：

* InputMethod\_AttachOptions是OH\_InputMethodController\_Attach和OH\_InputMethodController\_AttachWithUIContext的必要参数之一。Attach函数同时需要InputMethod\_TextEditorProxy和InputMethod\_AttachOptions两个参数。
* InputMethod\_AttachOptions中的requestKeyboardReason使用InputMethod\_RequestKeyboardReason枚举类型，该枚举定义在[inputmethod\_types\_capi.h](capi-inputmethod-types-capi-h.md)中。
* OH\_InputMethodProxy\_ShowTextInput函数也接受InputMethod\_AttachOptions作为参数，用于在已绑定的状态下重新请求显示键盘并指定请求原因。

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

**所在头文件：** [inputmethod\_attach\_options\_capi.h](capi-inputmethod-attach-options-capi-h.md)
