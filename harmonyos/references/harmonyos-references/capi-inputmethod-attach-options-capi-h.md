---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-attach-options-capi-h
title: inputmethod_attach_options_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_attach_options_capi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2cc56cb1e5ae3b4a61dd2110827ab68c5f7502968d45e938dda1d5a34ac59d4c
---

## 概述

提供输入法绑定选项对象的创建、销毁与读写方法，用于管理应用绑定输入法时的配置参数。

功能：创建和管理InputMethod\_AttachOptions实例，支持配置绑定时是否显示键盘（showKeyboard）以及触发输入法拉起的场景原因（requestKeyboardReason）。AttachOptions是调用OH\_InputMethodController\_Attach时的必要参数，用于控制绑定输入法服务时的初始行为。

使用场景：在应用绑定输入法服务前，创建AttachOptions配置绑定行为：

* showKeyboard=true时，绑定时自动拉起键盘，适用于输入框获得焦点后需要立即输入的场景。
* showKeyboard=false时，绑定时不拉起键盘，适用于需要先建立交互通道但暂不输入的场景（如搜索框先绑定输入法，等用户点击后再拉起键盘）。
* requestKeyboardReason用于标识触发输入法拉起的原因（如鼠标点击、触摸事件等），帮助系统识别输入场景以提供更好的用户体验。

使用后效果：创建AttachOptions后，将其传入Attach函数，Attach函数将读取其中的配置来决定绑定行为。Attach完成后，AttachOptions可销毁，因为配置信息已被读取。

**引用文件：** <inputmethod/inputmethod\_attach\_options\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) | InputMethod\_AttachOptions | 输入法绑定选项，用于在绑定输入法时携带相关配置。这是一个不透明类型（opaque type），调用者不可直接访问其成员变量，只能通过本头文件提供的函数操作。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_AttachOptions \*OH\_AttachOptions\_Create(bool showKeyboard)](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_create) | 创建一个InputMethod\_AttachOptions实例，适用于仅需控制键盘显示状态的简单绑定场景。 |
| [InputMethod\_AttachOptions \*OH\_AttachOptions\_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod\_RequestKeyboardReason requestKeyboardReason)](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_createwithrequestkeyboardreason) | 创建一个InputMethod\_AttachOptions实例，同时指定键盘显示状态和请求键盘的原因，适用于需要标识触发输入法拉起场景的绑定场景。 |
| [void OH\_AttachOptions\_Destroy(InputMethod\_AttachOptions \*options)](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_destroy) | 销毁一个InputMethod\_AttachOptions实例，释放由OH\_AttachOptions\_Create函数分配的内存资源。 |
| [InputMethod\_ErrorCode OH\_AttachOptions\_IsShowKeyboard(InputMethod\_AttachOptions \*options, bool \*showKeyboard)](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_isshowkeyboard) | 从InputMethod\_AttachOptions中获取是否显示键盘的值。 |
| [InputMethod\_ErrorCode OH\_AttachOptions\_GetRequestKeyboardReason(InputMethod\_AttachOptions \*options, int \*requestKeyboardReason)](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_getrequestkeyboardreason) | 从InputMethod\_AttachOptions中获取请求键盘的原因。 |

## 函数说明

### OH\_AttachOptions\_Create()

```c
InputMethod_AttachOptions *OH_AttachOptions_Create(bool showKeyboard)
```

**描述**

创建一个[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)实例，适用于仅需控制键盘显示状态的简单场景。如需同时指定触发输入法拉起的场景原因，建议使用[OH\_AttachOptions\_CreateWithRequestKeyboardReason](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_createwithrequestkeyboardreason)。

配对调用：必须与[OH\_AttachOptions\_Destroy](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_destroy)配对调用，OH\_AttachOptions\_Create创建的对象必须通过OH\_AttachOptions\_Destroy销毁，否则会导致内存泄漏。

生命周期管理：

* 创建后可多次读取（IsShowKeyboard）。
* 将options传入Attach函数后，Attach函数将读取配置信息。Attach完成后options可立即销毁，因为配置已被读取。
* 不可将已销毁的options再次使用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool showKeyboard | 输入参数，表示绑定时是否显示键盘。  使用场景：true适用于输入框获得焦点后需要立即输入的场景（如文本编辑框）；false适用于先建立交互通道但暂不需要键盘的场景（如搜索框，等用户主动点击后再拉起键盘）。  使用后效果：showKeyboard=true时，绑定成功后键盘将自动弹出；showKeyboard=false时，绑定成功后键盘不弹出，需后续通过OH\_InputMethodProxy\_ShowKeyboard主动拉起。  取值范围：true或false。  默认值：无默认值，调用者必须显式指定。  取值原则：根据业务场景决定。需要立即输入的场景设为true；需要延迟拉起键盘的场景设为false，后续通过ShowKeyboard主动拉起。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \* | 返回指针类型。  创建成功：返回一个指向新创建的InputMethod\_AttachOptions实例的指针，该指针有效且可用于后续操作。  创建失败：返回NULL，可能的失败原因包括应用地址空间满（内存不足）。  NULL判断：调用者必须在使用返回值前检查是否为NULL，若为NULL则不可使用该指针，应排查内存状况或稍后重试。  内存管理：返回的指针由Create函数内部分配内存，调用者需通过OH\_AttachOptions\_Destroy释放，不可使用free()或其他方式释放。 |

### OH\_AttachOptions\_CreateWithRequestKeyboardReason()

```c
InputMethod_AttachOptions *OH_AttachOptions_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod_RequestKeyboardReason requestKeyboardReason)
```

**描述**

创建一个[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)实例，同时指定键盘显示状态和请求键盘的原因。requestKeyboardReason参数用于标识触发输入法拉起的场景原因，帮助系统识别输入场景以提供更好的用户体验。

配对调用：必须与[OH\_AttachOptions\_Destroy](capi-inputmethod-attach-options-capi-h.md#oh_attachoptions_destroy)配对调用，Create创建的对象必须通过OH\_AttachOptions\_Destroy销毁。

生命周期管理：与OH\_AttachOptions\_Create一致。创建后可多次读取，Attach完成后可立即销毁。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool showKeyboard | 输入参数，表示绑定时是否显示键盘。含义/功能、使用场景、使用后效果、取值范围、取值原则与OH\_AttachOptions\_Create中的showKeyboard参数一致。 |
| [InputMethod\_RequestKeyboardReason](capi-inputmethod-types-capi-h.md#inputmethod_requestkeyboardreason) requestKeyboardReason | 输入参数，表示请求键盘输入的原因。  含义/功能：标识触发输入法拉起的场景原因，用于帮助系统识别输入场景并优化用户体验。  使用场景：当应用需要告知系统为何拉起键盘时使用，例如区分用户通过鼠标点击、触摸事件还是应用主动调用API触发输入法。  使用后效果：系统可根据此原因调整输入法行为（如选择合适的键盘布局或输入模式）。  取值范围：InputMethod\_RequestKeyboardReason枚举值，包括：  - IME\_REQUEST\_REASON\_NONE (0)：无特定原因。  - IME\_REQUEST\_REASON\_MOUSE (1)：通过鼠标点击触发。  - IME\_REQUEST\_REASON\_TOUCH (2)：通过触摸事件触发。  - IME\_REQUEST\_REASON\_OTHER (20)：其他原因（应用主动调用API等）。  取值原则：根据实际触发场景选择对应的枚举值。用户通过触摸输入框触发时使用IME\_REQUEST\_REASON\_TOUCH；通过鼠标点击触发时使用IME\_REQUEST\_REASON\_MOUSE；应用内部逻辑主动触发时使用IME\_REQUEST\_REASON\_OTHER。  规格限制：仅支持上述枚举值，传入其他值可能导致未定义行为。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \* | 返回指针类型。  创建成功：返回一个指向新创建的InputMethod\_AttachOptions实例的指针。  创建失败：返回NULL，可能的失败原因有应用地址空间满（内存不足）。  NULL判断：调用者必须在使用返回值前检查是否为NULL，若为NULL则不可使用该指针。  内存管理：返回的指针由Create函数内部分配内存，调用者需通过OH\_AttachOptions\_Destroy释放，不可使用free()或其他方式释放。 |

### OH\_AttachOptions\_Destroy()

```c
void OH_AttachOptions_Destroy(InputMethod_AttachOptions *options)
```

**描述**

销毁一个[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)实例，释放由OH\_AttachOptions\_Create函数分配的内存资源。该方法与OH\_AttachOptions\_Create和OH\_AttachOptions\_CreateWithRequestKeyboardReason配对使用。

配对调用：必须与OH\_AttachOptions\_Create或OH\_AttachOptions\_CreateWithRequestKeyboardReason配对调用。每个OH\_AttachOptions\_Create创建的实例必须且只能调用一次OH\_AttachOptions\_Destroy。

生命周期管理：

* OH\_AttachOptions\_Destroy后，options指针不再有效，不可继续使用。
* 不可对同一个options指针调用两次OH\_AttachOptions\_Destroy，否则会导致重复释放（double-free）。
* 建议在Attach成功后立即调用OH\_AttachOptions\_Destroy，因为Attach已读取完配置信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 输入指针，表示即将被销毁的InputMethod\_AttachOptions实例。  含义/功能：指定要销毁的AttachOptions实例，OH\_AttachOptions\_Destroy将释放该实例占用的内存资源。  使用场景：在AttachOptions不再需要时调用，典型时机为Attach绑定完成后。  使用后效果：options指向的内存被释放，该指针不再有效。  NULL指针处理：若options为NULL，OH\_AttachOptions\_Destroy函数不做任何操作（安全处理），不会导致崩溃。但建议调用者避免传入NULL，因为这意味着OH\_AttachOptions\_Create失败未被正确处理。  内存释放责任：由调用者负责在适当时机调用OH\_AttachOptions\_Destroy释放内存。 |

### OH\_AttachOptions\_IsShowKeyboard()

```c
InputMethod_ErrorCode OH_AttachOptions_IsShowKeyboard(InputMethod_AttachOptions *options, bool *showKeyboard)
```

**描述**

从[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)中获取是否显示键盘的值。

前置条件：options必须是通过OH\_AttachOptions\_Create函数创建的有效实例，showKeyboard必须指向有效的bool变量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 输入指针，表示被读取值的InputMethod\_AttachOptions实例。  含义/功能：指定要从哪个AttachOptions实例中读取showKeyboard属性。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。  前提条件：必须通过OH\_AttachOptions\_Create函数创建的有效实例。 |
| bool \*showKeyboard | 输出指针，表示从InputMethod\_AttachOptions中获取的是否显示键盘的值。  含义/功能：用于接收showKeyboard属性的值。true表示绑定完成时需要显示键盘；false表示绑定完成时不需要显示键盘。  使用场景：需要查询AttachOptions的键盘显示配置时使用，如Attach前确认配置、调试时验证配置等。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。调用者需确保showKeyboard指向有效的bool变量。  内存分配责任：由调用者分配bool变量的内存，IsShowKeyboard仅写入值，不分配内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。\*showKeyboard已被赋值为正确的布尔值。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。表示options或showKeyboard为空指针，调用前需确保这两个参数已正确初始化且不为NULL。  错误处理建议：若返回IME\_ERR\_NULL\_POINTER，检查options和showKeyboard是否为有效指针；若返回IME\_ERR\_OK，\*showKeyboard即为正确的配置值。具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_AttachOptions\_GetRequestKeyboardReason()

```c
InputMethod_ErrorCode OH_AttachOptions_GetRequestKeyboardReason(InputMethod_AttachOptions *options, int *requestKeyboardReason)
```

**描述**

从[InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md)中获取请求键盘输入的原因。

前置条件：options必须是通过OH\_AttachOptions\_CreateWithRequestKeyboardReason创建的实例（通过OH\_AttachOptions\_Create创建的实例的requestKeyboardReason默认值为IME\_REQUEST\_REASON\_NONE）。requestKeyboardReason必须指向有效的InputMethod\_RequestKeyboardReason变量。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_AttachOptions](capi-inputmethod-inputmethod-attachoptions.md) \*options | 输入指针，表示被读取值的InputMethod\_AttachOptions实例。  含义/功能：指定要从哪个AttachOptions实例中读取requestKeyboardReason属性。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。  前提条件：必须通过OH\_AttachOptions\_CreateWithRequestKeyboardReason函数创建的有效实例。若实例通过OH\_AttachOptions\_Create（而非CreateWithRequestKeyboardReason）创建，读取的requestKeyboardReason默认值为IME\_REQUEST\_REASON\_NONE。 |
| int \*requestKeyboardReason | 输出指针，表示请求键盘输入的原因。  含义/功能：输出参数，用于获取触发输入法拉起的场景原因枚举值。  使用场景：需要查询AttachOptions的请求键盘原因配置时使用。  取值范围：输出值为[InputMethod\_RequestKeyboardReason](capi-inputmethod-types-capi-h.md#inputmethod_requestkeyboardreason)枚举：IME\_REQUEST\_REASON\_NONE(0)、IME\_REQUEST\_REASON\_MOUSE(1)、IME\_REQUEST\_REASON\_TOUCH(2)、IME\_REQUEST\_REASON\_OTHER(20)。  NULL指针处理：不可为NULL，传入NULL将返回IME\_ERR\_NULL\_POINTER。调用者需确保requestKeyboardReason指向有效的变量。  内存分配责任：由调用者分配变量的内存，GetRequestKeyboardReason仅写入值，不分配内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。\*requestKeyboardReason已被赋值为正确的枚举值。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。表示options或requestKeyboardReason为空指针，调用前需确保这两个参数已正确初始化且不为NULL。  错误处理建议：若返回IME\_ERR\_NULL\_POINTER，检查options和requestKeyboardReason是否为有效指针；若返回IME\_ERR\_OK，\*requestKeyboardReason即为正确的配置值。具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
