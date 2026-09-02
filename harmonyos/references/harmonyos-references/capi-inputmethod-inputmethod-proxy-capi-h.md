---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-proxy-capi-h
title: inputmethod_inputmethod_proxy_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_inputmethod_proxy_capi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8090d1f431153a2b47a9bfb54bf0ee51c50fa5382cbbd668d910d8e3d1e7c597
---

## 概述

提供使用输入法的方法，可以向输入法应用发送请求和通知，适用于需要控制输入法显示、隐藏、配置变更通知等功能的应用开发场景。

**引用文件：** <inputmethod/inputmethod\_inputmethod\_proxy\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) | InputMethod\_InputMethodProxy | 输入法代理对象。使用此对象可以调用输入法的方法。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_showkeyboard) | 显示键盘。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowTextInput(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_AttachOptions \*options)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_showtextinput) | 显示文本输入框。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_HideKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_hidekeyboard) | 隐藏键盘。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifySelectionChange(InputMethod\_InputMethodProxy \*inputMethodProxy, char16\_t text[], size\_t length, int start, int end)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-proxy-capi-h#oh_inputmethodproxy_notifyselectionchange) | 通知文本框选区变化。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyConfigurationChange(InputMethod\_InputMethodProxy \*inputMethodProxy,InputMethod\_EnterKeyType enterKey, InputMethod\_TextInputType textType)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_notifyconfigurationchange) | 通知输入框配置变化。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyCursorUpdate(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_CursorInfo \*cursorInfo)](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_notifycursorupdate) | 通知光标位置变化。 |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_SendPrivateCommand(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_PrivateCommand \*privateCommand[], size\_t size)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-proxy-capi-h#oh_inputmethodproxy_sendprivatecommand) | 发送私有数据命令。 |

## 函数说明

### OH\_InputMethodProxy\_ShowKeyboard()

```c
InputMethod_ErrorCode OH_InputMethodProxy_ShowKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

显示键盘。调用此函数后，系统将请求输入法应用弹出软键盘界面，用于文本输入。

使用场景：当应用需要主动拉起键盘以便用户进行文本输入时调用此函数，例如编辑框获得焦点后需要显示键盘的场景。

使用后效果：调用成功后，输入法应用将弹出软键盘界面；调用失败后，返回对应的错误码，需根据错误码进行处理。

前置条件：必须先调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取inputMethodProxy实例，且当前处于已绑定（Attached）状态。

生命周期管理：inputMethodProxy由[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)创建输出，不可手动销毁。当调用[OH\_InputMethodController\_Detach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_detach)解除绑定后，inputMethodProxy将失效，此后再调用此函数将返回IME\_ERR\_DETACHED错误码。

调用顺序：OH\_InputMethodController\_Attach → OH\_InputMethodProxy\_ShowKeyboard → OH\_InputMethodProxy\_HideKeyboard → OH\_InputMethodController\_Detach

线程安全：此函数非线程安全，不建议在多线程环境下同时操作同一个inputMethodProxy对象，如需多线程访问请自行加锁保护。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。Detach后该指针失效，不可再用于调用任何InputMethodProxy相关函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功，键盘已请求显示。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误，可能是客户端内部异常。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误，可能是输入法管理服务不可用。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法，表示已调用Detach，需重新Attach后再使用。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针，传入的inputMethodProxy为NULL。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_ShowTextInput()

```c
InputMethod_ErrorCode OH_InputMethodProxy_ShowTextInput(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_AttachOptions *options)
```

**描述**

显示文本输入框。与ShowKeyboard不同，此接口可通过AttachOptions指定请求键盘输入的原因，系统根据原因决定是否弹出键盘。

使用场景：当应用需要在特定场景下（如主动切换输入框、恢复输入等）请求显示文本输入界面时调用此函数，特别适用于需要携带RequestKeyboardReason的场景。

使用后效果：调用成功后，系统将根据options中的RequestKeyboardReason决定是否弹出键盘并激活文本输入；调用失败后，返回对应的错误码。

前置条件：必须先调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取inputMethodProxy实例，且当前处于已绑定（Attached）状态。options参数需先通过[OH\_AttachOptions\_Create](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_create)创建。

生命周期管理：inputMethodProxy由[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)创建输出，不可手动销毁。Detach后失效。options的生命周期由调用者管理，使用完毕后需调用[OH\_AttachOptions\_Destroy](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_destroy)销毁。

线程安全：此函数非线程安全，不建议在多线程环境下同时操作同一个inputMethodProxy对象。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。Detach后该指针失效。 |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 输入指针，表示指向[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)实例的指针，用于获取配置选项。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。此接口中只需关注[InputMethod\_RequestKeyboardReason](capi-inputmethod-types-capi-h.md#inputmethod_requestkeyboardreason)属性，表示请求键盘输入的原因。AttachOptions中的ShowKeyboard属性在此接口中始终为true，无需额外关注。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法，已Detach需重新Attach。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针，inputMethodProxy或options为NULL。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_HideKeyboard()

```c
InputMethod_ErrorCode OH_InputMethodProxy_HideKeyboard(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

隐藏键盘。调用此函数后，系统将请求输入法应用关闭软键盘界面。

使用场景：当应用需要主动收起键盘时调用此函数，例如编辑框失去焦点、用户完成输入后需要隐藏键盘的场景。

使用后效果：调用成功后，输入法应用将收起软键盘界面；调用失败后，返回对应的错误码。

前置条件：必须先调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取inputMethodProxy实例，且当前处于已绑定（Attached）状态。

生命周期管理：inputMethodProxy由[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)创建输出，不可手动销毁。Detach后失效，再调用此函数将返回IME\_ERR\_DETACHED。

线程安全：此函数非线程安全，不建议在多线程环境下同时操作同一个inputMethodProxy对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。Detach后该指针失效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功，键盘已请求隐藏。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法，已Detach需重新Attach。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_NotifySelectionChange()

```c
InputMethod_ErrorCode OH_InputMethodProxy_NotifySelectionChange(InputMethod_InputMethodProxy *inputMethodProxy, char16_t text[], size_t length, int start, int end)
```

**描述**

通知文本框选区变化。当输入框内文本内容、光标位置或选中文本发生变化时，通过此接口将变更信息通知给输入法应用，使输入法能够感知编辑框的文本状态。

使用场景：当编辑框中的文本内容被修改、光标位置发生移动、或用户选中文本发生变化时调用此函数，确保输入法应用与编辑框的文本状态保持同步。

使用后效果：调用成功后，输入法应用将接收到选区变更信息，并据此更新输入法内部状态（如候选词、联想等）；调用失败后，返回对应的错误码。

前置条件：必须先调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取inputMethodProxy实例，且当前处于已绑定（Attached）状态。

生命周期管理：inputMethodProxy由[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)创建输出，不可手动销毁。Detach后失效。

内存管理：text参数为输入指针，由调用者分配内存，函数内部仅读取该数据，不会修改或释放。调用者负责text数组内存的生命周期管理。

线程安全：此函数非线程安全，不建议在多线程环境下同时操作同一个inputMethodProxy对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。Detach后该指针失效。 |
| char16\_t text[] | 输入指针，整个输入文本，采用UTF-16编码。由调用者分配内存，函数仅读取该数据。该指针不可为NULL。长度最大限制为8K（8192个char16\_t字符，对应16384字节），超出此限制将返回IME\_ERR\_PARAMCHECK。 |
| size\_t length | 输入参数，text参数的字符数量（单位：char16\_t字符个数）。取值范围：大于0且不超过8192。超过8192将返回IME\_ERR\_PARAMCHECK错误码。 |
| int start | 输入参数，所选文本的起始位置（单位：char16\_t字符偏移量，从0开始计数）。取值范围：大于等于0且小于等于end。取值原则：start应小于等于end，且不超过text的实际长度。 |
| int end | 输入参数，所选文本的结束位置（单位：char16\_t字符偏移量，从0开始计数）。取值范围：大于等于start且小于等于text的实际长度。取值原则：当无选中文本时，start与end相等，表示光标位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 参数错误，可能是length超过8K限制、start/end范围不合法等，请检查参数值是否在有效范围内。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法，已Detach需重新Attach。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针，inputMethodProxy为NULL。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_NotifyConfigurationChange()

```c
InputMethod_ErrorCode OH_InputMethodProxy_NotifyConfigurationChange(InputMethod_InputMethodProxy *inputMethodProxy,InputMethod_EnterKeyType enterKey, InputMethod_TextInputType textType)
```

**描述**

通知输入框配置变化。当编辑框的回车键类型或输入类型发生变化时，通过此接口将新的配置信息通知给输入法应用，使输入法能够调整键盘布局和输入行为。

使用场景：当编辑框的输入类型（如从文本模式切换为数字模式）或回车键类型（如从"完成"切换为"搜索"）发生变化时调用此函数。

使用后效果：调用成功后，输入法应用将根据新的配置调整键盘布局和回车键显示；调用失败后，返回对应的错误码。

前置条件：必须先调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取inputMethodProxy实例，且当前处于已绑定（Attached）状态。

生命周期管理：inputMethodProxy由[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)创建输出，不可手动销毁。Detach后失效。

线程安全：此函数非线程安全，不建议在多线程环境下同时操作同一个inputMethodProxy对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。Detach后该指针失效。 |
| [InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype) enterKey | 输入参数，回车键类型。取值范围：[InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype)枚举值，如IME\_ENTER\_KEY\_UNSPECIFIED、IME\_ENTER\_KEY\_GO、IME\_ENTER\_KEY\_SEARCH等。使用后效果：输入法将据此调整回车键的显示标签和功能。 |
| [InputMethod\_TextInputType](capi-inputmethod-types-capi-h.md#inputmethod_textinputtype) textType | 输入参数，输入框类型。取值范围：[InputMethod\_TextInputType](capi-inputmethod-types-capi-h.md#inputmethod_textinputtype)枚举值，如IME\_TEXT\_INPUT\_TYPE\_UNSPECIFIED、IME\_TEXT\_INPUT\_TYPE\_TEXT、IME\_TEXT\_INPUT\_TYPE\_NUMBER等。使用后效果：输入法将据此切换键盘布局（如数字键盘、文本键盘等）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 参数错误，可能是enterKey或textType值不合法，请检查枚举值是否在有效范围内。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法，已Detach需重新Attach。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_NotifyCursorUpdate()

```c
InputMethod_ErrorCode OH_InputMethodProxy_NotifyCursorUpdate(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_CursorInfo *cursorInfo)
```

**描述**

通知光标位置变化。当编辑框中光标位置发生变化时，通过此接口将新的光标信息通知给输入法应用，使输入法能够根据光标位置调整候选词窗口的显示位置。

使用场景：当编辑框中光标位置发生移动时调用此函数，例如用户点击编辑框中不同位置、代码主动移动光标等场景。

使用后效果：调用成功后，输入法应用将接收到新的光标信息，并据此调整候选词窗口的定位；调用失败后，返回对应的错误码。

前置条件：必须先调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取inputMethodProxy实例。cursorInfo需先通过[OH\_CursorInfo\_Create](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_create)创建并设置相关属性。

生命周期管理：inputMethodProxy由Attach创建输出，不可手动销毁，Detach后失效。cursorInfo的生命周期由调用者管理，使用完毕后需调用[OH\_CursorInfo\_Destroy](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_destroy)销毁。

线程安全：此函数非线程安全，不建议在多线程环境下同时操作同一个inputMethodProxy对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。Detach后该指针失效。 |
| [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md) \*cursorInfo | 输入指针，指向[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例的指针，表示光标信息。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。cursorInfo由调用者通过[OH\_CursorInfo\_Create](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_create)创建，函数仅读取其内部数据，不会修改或释放。使用完毕后调用者需调用[OH\_CursorInfo\_Destroy](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_destroy)释放cursorInfo。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 参数错误，可能是cursorInfo内部数据不合法，请检查光标信息参数。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法，已Detach需重新Attach。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针，inputMethodProxy或cursorInfo为NULL。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodProxy\_SendPrivateCommand()

```c
InputMethod_ErrorCode OH_InputMethodProxy_SendPrivateCommand(InputMethod_InputMethodProxy *inputMethodProxy, InputMethod_PrivateCommand *privateCommand[], size_t size)
```

**描述**

发送私有数据命令。应用通过此接口向输入法应用发送自定义的私有命令数据，用于实现应用与输入法之间的私有通信协议。

使用场景：当应用需要向输入法应用传递自定义的私有数据（如业务特定的指令、配置参数等）时调用此函数，适用于应用与输入法之间有私有通信协议的场景。

使用后效果：调用成功后，输入法应用将通过[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)回调接收到私有命令数据；调用失败后，返回对应的错误码。

前置条件：必须先调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取inputMethodProxy实例，且当前处于已绑定（Attached）状态。

生命周期管理：inputMethodProxy由Attach创建输出，不可手动销毁，Detach后失效。privateCommand数组中每个元素的生命周期由调用者管理，使用完毕后需调用[OH\_PrivateCommand\_Destroy](capi-inputmethod-private-command-capi-h.md#oh_privatecommand_destroy)逐个销毁。

性能建议：privateCommand数组最多包含5个命令对象（size最大为5），超出此限制将返回IME\_ERR\_PARAMCHECK。单个命令对象最大大小为32KB，超出限制可能导致数据传输失败。

线程安全：此函数非线程安全，不建议在多线程环境下同时操作同一个inputMethodProxy对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。该指针不可为NULL，若传入NULL指针将返回IME\_ERR\_NULL\_POINTER错误码。Detach后该指针失效。 |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*privateCommand[] | 输入指针，私有命令数组，每个元素为指向[InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md)实例的指针。由调用者创建并分配内存，函数仅读取数据。该指针不可为NULL。单个命令对象最大大小为32KB（包含key和value的总大小），超出可能导致传输失败。数组最大长度为5（即size参数最大为5）。 |
| size\_t size | 输入参数，私有命令数组的元素个数。取值范围：大于0且不超过5。超过5将返回IME\_ERR\_PARAMCHECK错误码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功，私有命令已发送。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 参数错误，可能是size超过5、privateCommand为NULL、或单个命令超过32KB，请检查参数值。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_DETACHED](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 未绑定输入法，已Detach需重新Attach。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针，inputMethodProxy或privateCommand为NULL。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
