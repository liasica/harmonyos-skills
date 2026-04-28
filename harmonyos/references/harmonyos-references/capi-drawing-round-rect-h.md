---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-round-rect-h
title: drawing_round_rect.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_round_rect.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2e9e0e22683c7782f1bdda00f2ba0b023f1d293a2bdd2962724eb06bd73cab06
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与圆角矩形相关的功能函数。

**引用文件：** <native\_drawing/drawing\_round\_rect.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_CornerPos](capi-drawing-round-rect-h.md#oh_drawing_cornerpos) | OH\_Drawing\_CornerPos | 用于描述圆角位置的枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCreate(const OH\_Drawing\_Rect\* rect, float xRad, float yRad)](capi-drawing-round-rect-h.md#oh_drawing_roundrectcreate) | 用于创建一个圆角矩形对象。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCopy(const OH\_Drawing\_RoundRect\* roundRect)](capi-drawing-round-rect-h.md#oh_drawing_roundrectcopy) | 用于创建圆角矩形的拷贝。 |
| [void OH\_Drawing\_RoundRectSetCorner(OH\_Drawing\_RoundRect\* roundRect,OH\_Drawing\_CornerPos pos, OH\_Drawing\_Corner\_Radii radii)](capi-drawing-round-rect-h.md#oh_drawing_roundrectsetcorner) | 用于设置圆角矩形中指定圆角位置的圆角半径。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  roundRect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_Corner\_Radii OH\_Drawing\_RoundRectGetCorner(OH\_Drawing\_RoundRect\* roundRect, OH\_Drawing\_CornerPos pos)](capi-drawing-round-rect-h.md#oh_drawing_roundrectgetcorner) | 用于获取圆角矩形中指定圆角位置的圆角半径。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  roundRect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_RoundRectDestroy(OH\_Drawing\_RoundRect\* roundRect)](capi-drawing-round-rect-h.md#oh_drawing_roundrectdestroy) | 用于销毁圆角矩形对象并回收该对象占用的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RoundRectOffset(OH\_Drawing\_RoundRect\* roundRect, float dx, float dy)](capi-drawing-round-rect-h.md#oh_drawing_roundrectoffset) | 用于将圆角矩形沿x轴方向和y轴方向平移指定距离。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_CornerPos

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_CornerPos
```

**描述**

用于描述圆角位置的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CORNER\_POS\_TOP\_LEFT | 左上角圆角位置。 |
| CORNER\_POS\_TOP\_RIGHT | 右上角圆角位置。 |
| CORNER\_POS\_BOTTOM\_RIGHT | 右下角圆角位置。 |
| CORNER\_POS\_BOTTOM\_LEFT | 左下角圆角位置。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_RoundRectCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_RoundRect* OH_Drawing_RoundRectCreate(const OH_Drawing_Rect* rect, float xRad, float yRad)
```

**描述**

用于创建一个圆角矩形对象。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| float xRad | X轴上的圆角半径，小于或等于0时无效。 |
| float yRad | Y轴上的圆角半径，小于或等于0时无效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* | 函数会返回一个指针，指针指向创建的圆角矩形对象。 |

### OH\_Drawing\_RoundRectCopy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_RoundRect* OH_Drawing_RoundRectCopy(const OH_Drawing_RoundRect* roundRect)
```

**描述**

用于创建圆角矩形的拷贝。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向用于拷贝的圆角矩形对象[OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* | 函数会返回一个指针，指针指向创建的新圆角矩形对象。 |

### OH\_Drawing\_RoundRectSetCorner()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_RoundRectSetCorner(OH_Drawing_RoundRect* roundRect,OH_Drawing_CornerPos pos, OH_Drawing_Corner_Radii radii)
```

**描述**

用于设置圆角矩形中指定圆角位置的圆角半径。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

roundRect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向圆角矩形对象的指针。 |
| [OH\_Drawing\_CornerPos](capi-drawing-round-rect-h.md#oh_drawing_cornerpos) pos | 圆角位置的枚举，支持类型可见[OH\_Drawing\_CornerPos](capi-drawing-round-rect-h.md#oh_drawing_cornerpos)。 |
| [OH\_Drawing\_Corner\_Radii](capi-drawing-oh-drawing-point2d.md) radii | 圆角半径结构体OH\_Drawing\_Corner\_Radii，其中包含x轴方向和y轴方向上的半径，半径小于等于0时无效。 |

### OH\_Drawing\_RoundRectGetCorner()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Corner_Radii OH_Drawing_RoundRectGetCorner(OH_Drawing_RoundRect* roundRect, OH_Drawing_CornerPos pos)
```

**描述**

用于获取圆角矩形中指定圆角位置的圆角半径。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

roundRect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向圆角矩形对象的指针。 |
| [OH\_Drawing\_CornerPos](capi-drawing-round-rect-h.md#oh_drawing_cornerpos) pos | 圆角位置的枚举，支持类型可见[OH\_Drawing\_CornerPos](capi-drawing-round-rect-h.md#oh_drawing_cornerpos)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Corner\_Radii](capi-drawing-oh-drawing-point2d.md) | 返回指定圆角位置的圆角半径结构体OH\_Drawing\_Corner\_Radii，其中包含x轴方向和y轴方向上的半径。 |

### OH\_Drawing\_RoundRectDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_RoundRectDestroy(OH_Drawing_RoundRect* roundRect)
```

**描述**

用于销毁圆角矩形对象并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向圆角矩形对象的指针。 |

### OH\_Drawing\_RoundRectOffset()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_RoundRectOffset(OH_Drawing_RoundRect* roundRect, float dx, float dy)
```

**描述**

用于将圆角矩形沿x轴方向和y轴方向平移指定距离。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向圆角矩形对象[OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)的指针。 |
| float dx | x轴方向偏移量。 |
| float dy | y轴方向偏移量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数roundRect为空。 |
