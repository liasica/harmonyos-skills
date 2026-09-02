---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-point-h
title: drawing_point.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_point.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e46d94f3d22800b9e75170179910334c4c348226fd8fca752b44d04fe0ff840c
---

## 概述

文件中定义了与坐标点相关的功能函数，支持创建、获取、设置、取反、偏移及销毁坐标点对象等操作，便于在2D图形绘制中对坐标点进行管理与变换。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_point.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Point\* OH\_Drawing\_PointCreate(float x, float y)](capi-drawing-point-h.md#oh_drawing_pointcreate) | 创建一个坐标点对象。当此坐标点对象不再需要时，必须调用[OH\_Drawing\_PointDestroy](capi-drawing-point-h.md#oh_drawing_pointdestroy)销毁并回收内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetX(const OH\_Drawing\_Point\* point, float\* x)](capi-drawing-point-h.md#oh_drawing_pointgetx) | 获取坐标点的x轴坐标值。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetY(const OH\_Drawing\_Point\* point, float\* y)](capi-drawing-point-h.md#oh_drawing_pointgety) | 获取坐标点的y轴坐标值。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointSet(OH\_Drawing\_Point\* point, float x, float y)](capi-drawing-point-h.md#oh_drawing_pointset) | 设置坐标点的x轴和y轴坐标。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointNegate(OH\_Drawing\_Point\* point)](capi-drawing-point-h.md#oh_drawing_pointnegate) | 对坐标点的x轴和y轴坐标取反。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointOffset(OH\_Drawing\_Point\* point, float dx, float dy)](capi-drawing-point-h.md#oh_drawing_pointoffset) | 将坐标点沿x轴和y轴方向偏移指定距离。 |
| [void OH\_Drawing\_PointDestroy(OH\_Drawing\_Point\* point)](capi-drawing-point-h.md#oh_drawing_pointdestroy) | 销毁坐标点对象并回收该对象占用的内存。需在[OH\_Drawing\_PointCreate](capi-drawing-point-h.md#oh_drawing_pointcreate)创建对象后且该对象不再使用时调用。 |

## 函数说明

### OH\_Drawing\_PointCreate()

```c
OH_Drawing_Point* OH_Drawing_PointCreate(float x, float y)
```

**描述**

创建一个坐标点对象。当此坐标点对象不再需要时，必须调用[OH\_Drawing\_PointDestroy](capi-drawing-point-h.md#oh_drawing_pointdestroy)销毁并回收内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float x | 表示坐标点的x轴坐标，单位为物理像素px。 |
| float y | 表示坐标点的y轴坐标，单位为物理像素px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* | 函数返回指向创建的坐标点对象的指针。 |

### OH\_Drawing\_PointGetX()

```c
OH_Drawing_ErrorCode OH_Drawing_PointGetX(const OH_Drawing_Point* point, float* x)
```

**描述**

获取坐标点的x轴坐标值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* point | 指向坐标点对象[OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)的指针。 |
| float\* x | 输出参数，用于接收坐标点的x轴坐标值，单位为物理像素px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数point或者x为空。 |

### OH\_Drawing\_PointGetY()

```c
OH_Drawing_ErrorCode OH_Drawing_PointGetY(const OH_Drawing_Point* point, float* y)
```

**描述**

获取坐标点的y轴坐标值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* point | 指向坐标点对象[OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)的指针。 |
| float\* y | 输出参数，用于接收坐标点的y轴坐标值，单位为物理像素px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数point或者y为空。 |

### OH\_Drawing\_PointSet()

```c
OH_Drawing_ErrorCode OH_Drawing_PointSet(OH_Drawing_Point* point, float x, float y)
```

**描述**

设置坐标点的x轴和y轴坐标。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* point | 指向坐标点对象[OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)的指针。 |
| float x | 表示坐标点的x轴坐标，单位为物理像素px。 |
| float y | 表示坐标点的y轴坐标，单位为物理像素px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数point为空。 |

### OH\_Drawing\_PointNegate()

```c
OH_Drawing_ErrorCode OH_Drawing_PointNegate(OH_Drawing_Point* point)
```

**描述**

对坐标点的x轴和y轴坐标取反。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* point | 指向坐标点对象[OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数point为空。 |

### OH\_Drawing\_PointOffset()

```c
OH_Drawing_ErrorCode OH_Drawing_PointOffset(OH_Drawing_Point* point, float dx, float dy)
```

**描述**

将坐标点沿x轴和y轴方向偏移指定距离。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* point | 指向坐标点对象[OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)的指针。 |
| float dx | 表示在x轴上的偏移量，单位为物理像素px。正数表示往x轴正方向平移，负数表示往x轴负方向平移。 |
| float dy | 表示在y轴上的偏移量，单位为物理像素px。正数表示往y轴正方向平移，负数表示往y轴负方向平移。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数point为空。 |

### OH\_Drawing\_PointDestroy()

```c
void OH_Drawing_PointDestroy(OH_Drawing_Point* point)
```

**描述**

销毁坐标点对象并回收该对象占用的内存。需在[OH\_Drawing\_PointCreate](capi-drawing-point-h.md#oh_drawing_pointcreate)创建对象后且该对象不再使用时调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* point | 指向坐标点对象的指针。 |
