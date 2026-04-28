---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-avoid-info-capi-h
title: inputmethod_text_avoid_info_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_text_avoid_info_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:46060f2eeb0c3dcdf20159a9166601a959b3ff7bd7159e4cf6245d93e55fdb83
---

## 概述

PhonePC/2in1TabletTVWearable

提供输入框避让信息对象的创建、销毁与读写方法。

**引用文件：** <inputmethod/inputmethod\_text\_avoid\_info\_capi.h>

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
| [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md) | InputMethod\_TextAvoidInfo | 输入框避让信息。输入框用于避让键盘的信息。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_TextAvoidInfo \*OH\_TextAvoidInfo\_Create(double positionY, double height)](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_create) | 创建一个新的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例。 |
| [void OH\_TextAvoidInfo\_Destroy(InputMethod\_TextAvoidInfo \*info)](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_destroy) | 销毁一个[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例。 |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_SetPositionY(InputMethod\_TextAvoidInfo \*info, double positionY)](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_setpositiony) | 设置[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)中的Y坐标值。 |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_SetHeight(InputMethod\_TextAvoidInfo \*info, double height)](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_setheight) | 设置[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)中的高度值。 |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_GetPositionY(InputMethod\_TextAvoidInfo \*info, double \*positionY)](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_getpositiony) | 从[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)获取Y坐标值。 |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_GetHeight(InputMethod\_TextAvoidInfo \*info, double \*height)](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_getheight) | 从[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)获取高度值。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_TextAvoidInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_TextAvoidInfo *OH_TextAvoidInfo_Create(double positionY, double height)
```

**描述**

创建一个新的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| double positionY | 表示输入框位置的Y坐标值，单位px。 |
| double height | 表示输入框高度，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md) \* | 如果创建成功，返回一个指向新创建的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

### OH\_TextAvoidInfo\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_TextAvoidInfo_Destroy(InputMethod_TextAvoidInfo *info)
```

**描述**

销毁一个[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md) \*info | 表示指向即将被销毁的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例的指针。 |

### OH\_TextAvoidInfo\_SetPositionY()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextAvoidInfo_SetPositionY(InputMethod_TextAvoidInfo *info, double positionY)
```

**描述**

设置[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)中的Y坐标值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md) \*info | 指向即将被设置值的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例的指针。 |
| double positionY | Y坐标值，即输入框顶点与物理屏幕上侧距离的绝对值，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextAvoidInfo\_SetHeight()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextAvoidInfo_SetHeight(InputMethod_TextAvoidInfo *info, double height)
```

**描述**

设置[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)中的高度值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md) \*info | 指向即将被设置值的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例的指针。 |
| double height | 高度值，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextAvoidInfo\_GetPositionY()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextAvoidInfo_GetPositionY(InputMethod_TextAvoidInfo *info, double *positionY)
```

**描述**

从[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)获取Y坐标值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md) \*info | 指向即将被获取值的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例的指针。 |
| double \*positionY | Y坐标值，即输入框顶点与物理屏幕上侧距离的绝对值，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextAvoidInfo\_GetHeight()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextAvoidInfo_GetHeight(InputMethod_TextAvoidInfo *info, double *height)
```

**描述**

从[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)获取高度值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md) \*info | 指向即将被获取值的[InputMethod\_TextAvoidInfo](capi-inputmethod-inputmethod-textavoidinfo.md)实例的指针。 |
| double \*height | 输入框高度，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
