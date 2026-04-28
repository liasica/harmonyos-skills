---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-cursor-info-capi-h
title: inputmethod_cursor_info_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_cursor_info_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:11+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:86dc222ba37357e5f0ed99ee146698537e0fd78c25931a3209594ee0974cf90d
---

## 概述

PhonePC/2in1TabletTVWearable

提供光标信息对象的创建、销毁与读写方法。

**引用文件：** <inputmethod/inputmethod\_cursor\_info\_capi.h>

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
| [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md) | InputMethod\_CursorInfo | 光标信息。光标的坐标位置、宽度和高度。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [InputMethod\_CursorInfo \*OH\_CursorInfo\_Create(double left, double top, double width, double height)](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_create) | 创建一个新的[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例。 |
| [void OH\_CursorInfo\_Destroy(InputMethod\_CursorInfo \*cursorInfo)](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_destroy) | 销毁一个[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例。 |
| [InputMethod\_ErrorCode OH\_CursorInfo\_SetRect(InputMethod\_CursorInfo \*cursorInfo, double left, double top, double width, double height)](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_setrect) | 设置光标信息内容。 |
| [InputMethod\_ErrorCode OH\_CursorInfo\_GetRect(InputMethod\_CursorInfo \*cursorInfo, double \*left, double \*top, double \*width, double \*height)](capi-inputmethod-cursor-info-capi-h.md#oh_cursorinfo_getrect) | 获取光标信息内容。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CursorInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_CursorInfo *OH_CursorInfo_Create(double left, double top, double width, double height)
```

**描述**

创建一个新的[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| double left | 光标靠左点与物理屏幕左侧距离的绝对值，单位px。 |
| double top | 光标顶点与物理屏幕上侧距离的绝对值，单位px。 |
| double width | 宽度，单位px。 |
| double height | 高度，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md) \* | 如果创建成功，返回一个指向新创建的[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用程序的地址空间耗尽。 |

### OH\_CursorInfo\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CursorInfo_Destroy(InputMethod_CursorInfo *cursorInfo)
```

**描述**

销毁一个[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md) \*cursorInfo | 表示指向即将被销毁的[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例的指针。 |

### OH\_CursorInfo\_SetRect()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_CursorInfo_SetRect(InputMethod_CursorInfo *cursorInfo, double left, double top, double width, double height)
```

**描述**

设置光标信息内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md) \*cursorInfo | 表示指向[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例的指针。 |
| double left | 光标靠左点与物理屏幕左侧距离的绝对值，单位px。 |
| double top | 光标顶点与物理屏幕上侧距离的绝对值，单位px。 |
| double width | 宽度，单位px。 |
| double height | 高度，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_CursorInfo\_GetRect()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_CursorInfo_GetRect(InputMethod_CursorInfo *cursorInfo, double *left, double *top, double *width, double *height)
```

**描述**

获取光标信息内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md) \*cursorInfo | 表示指向[InputMethod\_CursorInfo](capi-inputmethod-inputmethod-cursorinfo.md)实例的指针。 |
| double \*left | 靠左点与物理屏幕左侧距离的绝对值，单位px。 |
| double \*top | 顶点与物理屏幕上侧距离的绝对值，单位px。 |
| double \*width | 宽度，单位px。 |
| double \*height | 高度，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
