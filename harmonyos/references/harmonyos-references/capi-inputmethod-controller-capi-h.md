---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-controller-capi-h
title: inputmethod_controller_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_controller_capi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b7795fdfafbbf85af890e5bb8aad4755ef439776cdc2e7b3409926e61f2b5313
---

## 概述

提供绑定、解绑输入法的方法，是应用与输入法服务交互的核心入口。

功能：通过OH\_InputMethodController\_Attach将应用绑定到输入法服务，建立双向交互通道；通过OH\_InputMethodController\_Detach将应用从输入法服务解除绑定，关闭交互通道并释放相关资源。

使用场景：适用于使用NDK开发自绘输入框的应用，需要在应用启动或输入框获得焦点时绑定输入法服务，在应用退出或输入框失去焦点时解绑输入法服务的场景。

使用后效果：OH\_InputMethodController\_Attach成功后，应用可通过返回的InputMethodProxy与输入法交互（如显示/隐藏键盘、通知光标更新等），同时输入法可通过TextEditorProxy的回调向应用发送文本插入、删除等通知。OH\_InputMethodController\_Detach后，交互通道关闭，inputMethodProxy不再有效。

**引用文件：** <inputmethod/inputmethod\_controller\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_ErrorCode OH\_InputMethodController\_Attach(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_AttachOptions \*options, InputMethod\_InputMethodProxy \*\*inputMethodProxy)](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach) | 将应用绑定到输入法服务。必须在创建TextEditorProxy和AttachOptions之后调用，绑定成功后返回InputMethodProxy用于后续交互。必须与OH\_InputMethodController\_Detach配对调用。 |
| [InputMethod\_ErrorCode OH\_InputMethodController\_AttachWithUIContext(ArkUI\_ContextHandle context, InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_AttachOptions \*options, InputMethod\_InputMethodProxy \*\*inputMethodProxy)](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attachwithuicontext) | 将应用绑定到输入法服务，同时携带UI上下文信息。适用于需要将输入法与特定UI页面关联的场景（如多窗口场景下指定绑定到哪个页面）。必须在创建TextEditorProxy和AttachOptions之后调用，必须与OH\_InputMethodController\_Detach配对调用。 |
| [InputMethod\_ErrorCode OH\_InputMethodController\_Detach(InputMethod\_InputMethodProxy \*inputMethodProxy)](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_detach) | 将应用从输入法服务解除绑定。必须在OH\_InputMethodController\_Attach或AttachWithUIContext之后调用，解绑后inputMethodProxy不再有效，不可继续使用。 |

## 函数说明

### OH\_InputMethodController\_Attach()

```c
InputMethod_ErrorCode OH_InputMethodController_Attach(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)
```

**描述**

将应用绑定到输入法服务，建立应用与输入法之间的双向交互通道。绑定成功后，应用可通过返回的InputMethodProxy主动向输入法发送请求和通知，同时输入法可通过TextEditorProxy中注册的回调函数向应用发送文本插入、删除等通知。

前置条件：

1. 必须先通过OH\_TextEditorProxy\_Create创建InputMethod\_TextEditorProxy实例，并通过OH\_TextEditorProxy\_SetXXXFunc系列函数注册必要的回调（如InsertTextFunc、DeleteForwardFunc、GetTextConfigFunc等）。
2. 必须先通过OH\_AttachOptions\_Create或OH\_AttachOptions\_CreateWithRequestKeyboardReason创建InputMethod\_AttachOptions实例。
3. TextEditorProxy中注册的回调函数必须已正确实现，否则输入法交互将不完整。

配对调用：

* 调用OH\_InputMethodController\_Attach后，必须在使用完毕后调用OH\_InputMethodController\_Detach解除绑定。
* 未调用OH\_InputMethodController\_Detach会导致输入法资源泄漏。
* 建议在应用退出或输入框不再需要输入法时及时调用OH\_InputMethodController\_Detach。

调用顺序：

1. OH\_TextEditorProxy\_Create → 创建TextEditorProxy
2. OH\_TextEditorProxy\_SetXXXFunc → 注册回调函数
3. OH\_AttachOptions\_Create → 创建AttachOptions
4. OH\_InputMethodController\_Attach → 绑定输入法（返回InputMethodProxy）
5. OH\_InputMethodProxy\_ShowKeyboard / NotifyCursorUpdate 等 → 使用输入法功能
6. OH\_InputMethodController\_Detach → 解绑输入法
7. OH\_TextEditorProxy\_Destroy / OH\_AttachOptions\_Destroy → 销毁创建的对象

生命周期管理：

* textEditorProxy：调用者自行管理生命周期。若OH\_InputMethodController\_Attach成功，在下次OH\_InputMethodController\_Attach或OH\_InputMethodController\_Detach完成之前不可释放textEditorProxy，否则会导致输入法回调时访问无效内存。
* options：调用者自行管理生命周期。OH\_InputMethodController\_Attach调用完成后，options可立即通过OH\_AttachOptions\_Destroy销毁，因为OH\_InputMethodController\_Attach过程已读取完options中的配置信息。
* inputMethodProxy：由OH\_InputMethodController\_Attach函数通过双指针输出参数分配内存，调用者在OH\_InputMethodController\_Detach之前需保持inputMethodProxy有效，OH\_InputMethodController\_Detach后该指针不可继续使用。

线程安全：非线程安全，建议在主线程调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，表示指向InputMethod\_TextEditorProxy实例的指针。含义/功能：作为应用接收输入法回调通知的通道载体，绑定后输入法将通过此对象中注册的回调函数与应用交互。使用场景：在绑定输入法前，应用需先创建TextEditorProxy并注册必要的回调函数。使用后效果：若OH\_InputMethodController\_Attach成功，输入法将通过此对象中的回调函数向应用发送通知；若失败，此对象不受影响可继续使用。  前置条件：必须通过OH\_TextEditorProxy\_Create创建，并通过SetXXXFunc系列函数注册回调。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。  生命周期管理：调用者自行管理。若Attach成功，在下次OH\_InputMethodController\_Attach或OH\_InputMethodController\_Detach完成之前不可释放textEditorProxy，否则输入法回调时将访问已释放的内存导致未定义行为。  内存分配责任：由调用者通过OH\_TextEditorProxy\_Create分配，通过OH\_TextEditorProxy\_Destroy释放。 |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 输入指针，表示指向InputMethod\_AttachOptions实例的指针。含义/功能：指定绑定输入法时的行为配置，包括是否在绑定时显示键盘以及请求键盘的原因。使用场景：在绑定前创建并配置好AttachOptions，用于控制绑定时的键盘显示行为。使用后效果：OH\_InputMethodController\_Attach函数将读取options中的配置参数来决定绑定行为。  前置条件：必须通过OH\_AttachOptions\_Create或OH\_AttachOptions\_CreateWithRequestKeyboardReason创建。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。  生命周期管理：OH\_InputMethodController\_Attach完成后options可立即销毁，因为绑定过程已读取完配置信息。建议在OH\_InputMethodController\_Attach成功后调用OH\_AttachOptions\_Destroy释放内存。  内存分配责任：由调用者通过Create函数分配，通过OH\_AttachOptions\_Destroy释放。 |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*\*inputMethodProxy | 输出双指针，表示指向InputMethod\_InputMethodProxy指针的指针。含义/功能：用于接收OH\_InputMethodController\_Attach成功后返回的InputMethodProxy实例，该实例是应用主动向输入法发送请求和通知的交互通道。使用场景：OH\_InputMethodController\_Attach成功后，调用者通过此指针获取InputMethodProxy，后续调用ShowKeyboard、HideKeyboard、NotifyCursorUpdate等函数时需传入此指针。使用后效果：若OH\_InputMethodController\_Attach成功，\*inputMethodProxy将被赋值为有效的InputMethodProxy指针；若失败，\*inputMethodProxy的值不确定，不应使用。  双指针说明：此参数为双指针（Pointer to Pointer），OH\_InputMethodController\_Attach函数内部将分配InputMethodProxy的内存并通过此双指针输出给调用者。调用者需提供有效的指针变量地址，不可为NULL。  NULL指针处理：inputMethodProxy本身不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。  内存管理：InputMethodProxy的内存由OH\_InputMethodController\_Attach函数内部分配，其生命周期由框架管理直到OH\_InputMethodController\_Detach完成。调用者不可自行释放此内存。OH\_InputMethodController\_Detach后inputMethodProxy指向的内存将被释放，该指针不可继续使用。  相关参数制约：此指针仅在OH\_InputMethodController\_Attach返回IME\_ERR\_OK时有效；OH\_InputMethodController\_Detach后此指针立即失效，不可继续使用，否则会导致未定义行为或崩溃。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。此时\*inputMethodProxy有效，可用于后续交互。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。检查textEditorProxy、options、inputMethodProxy是否为有效指针。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。可能是输入法服务未就绪或连接异常。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。可能是系统输入法管理服务异常。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。textEditorProxy、options或inputMethodProxy为NULL时返回。  错误处理建议：若返回非IME\_ERR\_OK，应检查参数有效性后重试；若返回IME\_ERR\_IMCLIENT或IME\_ERR\_IMMS，说明服务异常，建议稍后重试。具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodController\_AttachWithUIContext()

```c
InputMethod_ErrorCode OH_InputMethodController_AttachWithUIContext(ArkUI_ContextHandle context, InputMethod_TextEditorProxy *textEditorProxy, InputMethod_AttachOptions *options, InputMethod_InputMethodProxy **inputMethodProxy)
```

**描述**

将应用绑定到输入法服务，同时携带UI上下文信息。与OH\_InputMethodController\_Attach的区别在于，此函数额外接受一个ArkUI\_ContextHandle参数，用于在多窗口或多页面场景下指定绑定到具体的UI上下文，使输入法服务能精确关联到当前活跃的页面。

前置条件：

1. 必须先获取有效的ArkUI\_ContextHandle（通过ArkUI模块创建UI上下文获取）。
2. 必须先通过OH\_TextEditorProxy\_Create创建InputMethod\_TextEditorProxy实例，并通过OH\_TextEditorProxy\_SetXXXFunc系列函数注册必要的回调。
3. 必须先通过OH\_AttachOptions\_Create或OH\_AttachOptions\_CreateWithRequestKeyboardReason创建InputMethod\_AttachOptions实例。

配对调用：

* 调用OH\_InputMethodController\_AttachWithUIContext后，必须在使用完毕后调用OH\_InputMethodController\_Detach解除绑定。
* 未调用OH\_InputMethodController\_Detach会导致输入法资源泄漏。

调用顺序：

1. 获取ArkUI\_ContextHandle
2. OH\_TextEditorProxy\_Create → 创建TextEditorProxy
3. OH\_TextEditorProxy\_SetXXXFunc → 注册回调函数
4. OH\_AttachOptions\_Create → 创建AttachOptions
5. OH\_InputMethodController\_AttachWithUIContext → 绑定输入法（携带UI上下文）
6. OH\_InputMethodProxy\_ShowKeyboard / NotifyCursorUpdate 等 → 使用输入法功能
7. OH\_InputMethodController\_Detach → 解绑输入法
8. 销毁创建的对象

生命周期管理：

* context：由ArkUI模块管理，需在绑定期间保持有效。
* textEditorProxy：调用者自行管理。若OH\_InputMethodController\_AttachWithUIContext成功，在下次OH\_InputMethodController\_AttachWithUIContext或OH\_InputMethodController\_Detach完成之前不可释放。
* options：OH\_InputMethodController\_AttachWithUIContext完成后可立即销毁。
* inputMethodProxy：由AttachWithUIContext函数内部分配，OH\_InputMethodController\_Detach后释放。

使用场景：适用于多窗口或多页面应用场景，需要将输入法绑定到特定UI页面的场景。当应用有多个UI上下文（如多窗口），使用此函数可确保输入法与正确的页面关联，避免输入法事件发送到错误的窗口。

线程安全：非线程安全，建议在主线程调用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | 输入指针，表示指向ArkUI\_Context实例的指针。含义/功能：指定输入法绑定到哪个UI上下文（页面/窗口），使输入法服务能精确关联到当前活跃的页面。使用场景：在多窗口或多页面应用中，需要将输入法绑定到特定UI上下文时使用。使用后效果：输入法事件将发送到与此上下文关联的页面。  前置条件：必须通过ArkUI模块获取有效的ArkUI\_ContextHandle。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。  生命周期管理：需在绑定期间保持ArkUI\_Context有效，OH\_InputMethodController\_Detach前不可销毁对应的UI上下文。 |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，表示指向InputMethod\_TextEditorProxy实例的指针。含义/功能：与OH\_InputMethodController\_Attach中的textEditorProxy参数相同，作为应用接收输入法回调通知的通道载体。使用场景、前置条件、NULL指针处理、生命周期管理均与OH\_InputMethodController\_Attach中textEditorProxy参数一致。 |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 输入指针，表示指向InputMethod\_AttachOptions实例的指针。含义/功能：与OH\_InputMethodController\_Attach中的options参数相同，用于指定绑定时的行为配置。使用场景、前置条件、NULL指针处理、生命周期管理均与OH\_InputMethodController\_Attach中options参数一致。 |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*\*inputMethodProxy | 输出双指针，表示指向InputMethod\_InputMethodProxy指针的指针。含义/功能、使用场景、双指针说明、NULL指针处理、内存管理、相关参数制约均与OH\_InputMethodController\_Attach中的inputMethodProxy参数一致。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。此时\*inputMethodProxy有效，可用于后续交互。  [IME\_ERR\_PARAMCHECK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示参数错误。检查context、textEditorProxy、options、inputMethodProxy是否为有效指针。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法客户端错误。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 输入法服务错误。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。context、textEditorProxy、options或inputMethodProxy为NULL时返回。  错误处理建议：若返回非IME\_ERR\_OK，应检查参数有效性后重试；若返回IME\_ERR\_IMCLIENT或IME\_ERR\_IMMS，说明服务异常，建议稍后重试。具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_InputMethodController\_Detach()

```c
InputMethod_ErrorCode OH_InputMethodController_Detach(InputMethod_InputMethodProxy *inputMethodProxy)
```

**描述**

将应用从输入法服务解除绑定，关闭交互通道。OH\_InputMethodController\_Detach后，inputMethodProxy不再有效，不可继续使用任何通过inputMethodProxy调用的函数（如ShowKeyboard、HideKeyboard、NotifyCursorUpdate等），否则会导致未定义行为或崩溃。

前置条件：

* 必须先调用OH\_InputMethodController\_Attach或OH\_InputMethodController\_AttachWithUIContext成功绑定输入法，并获得有效的inputMethodProxy。

调用顺序：

* 必须先调用OH\_InputMethodController\_Attach或OH\_InputMethodController\_AttachWithUIContext绑定输入法。
* 调用OH\_InputMethodController\_Detach完成输入法使用后，不能再使用inputMethodProxy。
* OH\_InputMethodController\_Detach完成后，可安全销毁TextEditorProxy（通过OH\_TextEditorProxy\_Destroy）。

错误处理：

* 如果inputMethodProxy无效或未绑定，调用OH\_InputMethodController\_Detach会返回IME\_ERR\_NULL\_POINTER或IME\_ERR\_IMCLIENT。
* 重复调用OH\_InputMethodController\_Detach使用同一个inputMethodProxy可能导致未定义行为，应避免。
* OH\_InputMethodController\_Detach失败后不应继续使用inputMethodProxy。

生命周期管理：

* OH\_InputMethodController\_Detach后，inputMethodProxy指向的内存由框架释放，调用者不可再使用此指针。
* OH\_InputMethodController\_Detach后，应用可安全销毁TextEditorProxy，因为输入法不再会通过回调访问TextEditorProxy。
* 建议OH\_InputMethodController\_Detach成功后立即调用OH\_TextEditorProxy\_Destroy和OH\_AttachOptions\_Destroy释放所有创建的对象。

线程安全：非线程安全，建议在主线程调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_InputMethodProxy](capi-inputmethod-inputmethod-inputmethodproxy.md) \*inputMethodProxy | 输入指针，表示指向InputMethod\_InputMethodProxy实例的指针。含义/功能：指定要解除绑定的输入法代理实例，OH\_InputMethodController\_Detach将关闭此代理对应的交互通道并释放相关资源。使用场景：在应用不再需要输入法交互时调用，如应用退出、输入框失去焦点等。使用后效果：OH\_InputMethodController\_Detach成功后，inputMethodProxy立即失效，不可继续使用；输入法不再向应用发送回调通知。  前置条件：此指针必须由OH\_InputMethodController\_Attach或OH\_InputMethodController\_AttachWithUIContext成功返回。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。  生命周期管理：此指针由OH\_InputMethodController\_Attach/AttachWithUIContext函数分配，OH\_InputMethodController\_Detach成功后由框架释放，调用者不可自行释放，也不可在OH\_InputMethodController\_Detach后继续使用。  使用注意：Detach后此指针立即失效，将此指针传入任何InputMethodProxy相关函数会导致未定义行为。同一inputMethodProxy不可重复调用OH\_InputMethodController\_Detach。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。解绑完成，inputMethodProxy不再有效。  [IME\_ERR\_IMCLIENT](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示输入法客户端错误。可能是客户端连接异常或已断开。  [IME\_ERR\_IMMS](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示输入法服务错误。可能是服务端异常。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。inputMethodProxy为NULL时返回。  错误处理建议：若返回IME\_ERR\_OK，解绑成功，后续可安全销毁所有创建的对象；若返回IME\_ERR\_IMCLIENT，说明客户端状态异常，建议记录日志并销毁相关对象；若返回IME\_ERR\_NULL\_POINTER，说明传入的指针无效，应检查是否已OH\_InputMethodController\_Detach或指针已失效。具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
