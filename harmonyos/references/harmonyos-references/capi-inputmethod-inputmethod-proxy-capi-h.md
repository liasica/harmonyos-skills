---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-proxy-capi-h
title: inputmethod_inputmethod_proxy_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_inputmethod_proxy_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:836d8627cd9933c8adda0576a84b957d41ab0239d346f5a55ef5f4de23563de8
---

## 概述

PhonePC/2in1TabletTVWearable

提供使用输入法的方法，可以向输入法应用发送请求和通知。

**引用文件：** <inputmethod/inputmethod\_inputmethod\_proxy\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) | InputMethod\_InputMethodProxy | 输入法代理对象。使用此对象可以用于调用使用输入法的方法。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_showkeyboard) | 显示键盘。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowTextInput(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_AttachOptions \*options)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_showtextinput) | 显示文本输入框。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_HideKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_hidekeyboard) | 隐藏键盘。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifySelectionChange(InputMethod\_InputMethodProxy \*inputMethodProxy, char16\_t text[], size\_t length, int start, int end)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-proxy-capi-h#oh_inputmethodproxy_notifyselectionchange) | 通知文本框选区变化。当输入框内文本内容、光标位置或选中文本发生变化时，通过此接口将信息通知给输入法应用。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyConfigurationChange(InputMethod\_InputMethodProxy \*inputMethodProxy,InputMethod\_EnterKeyType enterKey, InputMethod\_TextInputType textType)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_notifyconfigurationchange) | 通知输入框配置变化。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyCursorUpdate(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_CursorInfo \*cursorInfo)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_notifycursorupdate) | 通知光标位置变化。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_SendPrivateCommand(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_PrivateCommand \*privateCommand[], size\_t size)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-proxy-capi-h#oh_inputmethodproxy_sendprivatecommand) | 发送私有数据命令。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_InputMethodProxy\_ShowKeyboard()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodProxy_ShowKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

显示键盘。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_ShowTextInput()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodProxy_ShowTextInput(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_AttachOptions *options)
```

**描述**

显示文本输入框。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 表示指向[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)实例的指针，用于获取配置选项。  此接口中只需关注[InputMethod\_RequestKeyboardReason](capi-inputmethod-types-capi-h.md#inputmethod_requestkeyboardreason) - 表示请求键盘输入的原因。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_HideKeyboard()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodProxy_HideKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

隐藏键盘。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_NotifySelectionChange()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodProxy_NotifySelectionChange(InputMethod_InputMethodProxy *inputMethodProxy, char16_t text[], size_t length, int start, int end)
```

**描述**

通知文本框选区变化。当输入框内文本内容、光标位置或选中文本发生变化时，通过此接口将信息通知给输入法应用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |
| text | 整个输入文本。 |
| size\_t length | text参数的长度。最大长度为8K。 |
| int start | 所选文本的起始位置。 |
| int end | 所选文本的结束位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_NotifyConfigurationChange()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodProxy_NotifyConfigurationChange(InputMethod_InputMethodProxy *inputMethodProxy,InputMethod_EnterKeyType enterKey, InputMethod_TextInputType textType)
```

**描述**

通知输入框配置变化。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |
| [InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype) enterKey | 回车键类型。 |
| [InputMethod\_TextInputType](capi-inputmethod-types-capi-h.md#inputmethod_textinputtype) textType | 输入框类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_NotifyCursorUpdate()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodProxy_NotifyCursorUpdate(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_CursorInfo *cursorInfo)
```

**描述**

通知光标位置变化。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |
| [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md) \*cursorInfo | 指向[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例的指针。表示光标信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_SendPrivateCommand()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodProxy_SendPrivateCommand(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_PrivateCommand *privateCommand[], size_t size)
```

**描述**

发送私有数据命令。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*privateCommand[] | 私有命令, 定义在[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)，最大大小为32KB。 |
| size\_t size | 私有命令数组的大小，最大为5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
