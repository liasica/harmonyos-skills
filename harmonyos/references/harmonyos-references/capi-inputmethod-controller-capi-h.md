---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-controller-capi-h
title: inputmethod_controller_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_controller_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7fa4b0976bc8b0890a592e0486da5e013001e839dcb7c0c53b7f290066a540c2
---

## 概述

PhonePC/2in1TabletTVWearable

提供绑定、解绑输入法的方法。

**引用文件：** <inputmethod/inputmethod\_controller\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_ErrorCode OH\_InputMethodController\_Attach(InputMethod\_TextEditorProxy \*textEditorProxy,InputMethod\_AttachOptions \*options, InputMethod\_InputMethodProxy \*\*inputMethodProxy)](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach) | 将应用绑定到输入法服务。 |
| [InputMethod\_ErrorCode OH\_InputMethodController\_AttachWithUIContext(ArkUI\_ContextHandle context, InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_AttachOptions \*options, InputMethod\_InputMethodProxy \*\*inputMethodProxy)](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attachwithuicontext) | 将应用绑定到输入法服务。 |
| [InputMethod\_ErrorCode OH\_InputMethodController\_Detach(InputMethod\_InputMethodProxy \*inputMethodProxy)](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_detach) | 将应用从输入法服务解绑。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_InputMethodController\_Attach()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodController_Attach(InputMethod_TextEditorProxy *textEditorProxy,InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)
```

**描述**

将应用绑定到输入法服务。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 表示指向[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。调用者需要自行管理textEditorProxy的生命周期。并且如果调用成功，调用者在下次发起绑定或解绑之前，不能将textEditorProxy释放。 |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 表示指向[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)实例的指针。该参数用于指定附加输入法时的选项。 |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*\*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。生命周期维持到下一次绑定或解绑的调用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodController\_AttachWithUIContext()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodController_AttachWithUIContext(ArkUI_ContextHandle context, InputMethod_TextEditorProxy *textEditorProxy, InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)
```

**描述**

将应用绑定到输入法服务。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | 表示指向[ArkUI\_Context](capi-arkui-nativemodule-arkui-context.md)实例的指针。 |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 表示指向[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。调用者需要自行管理textEditorProxy的生命周期。并且如果调用成功，调用者在下次发起绑定或解绑之前，不能将textEditorProxy释放。 |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 表示指向[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)实例的指针。该参数用于指定附加输入法时的选项。 |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*\*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。生命周期维持到下一次绑定或解绑的调用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodController\_Detach()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_InputMethodController_Detach(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

将应用从输入法服务解绑。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 表示指向[InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md)实例的指针。inputMethodProxy由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示输入法服务错误。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
