---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-rect-h
title: drawing_rect.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_rect.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b670c412461ca73a3d39b6488d543d2ab564aff1e5486fca833854185f7a025
---

## 概述

文件中定义了与矩形相关的功能函数。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**相关示例：** [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native\_drawing/drawing\_rect.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect\* OH\_Drawing\_RectCreate(float left, float top, float right, float bottom)](capi-drawing-rect-h.md#oh_drawing_rectcreate) | 用于创建一个矩形对象，不会对设置的坐标排序，即允许矩形设置的左上角坐标大于对应的矩形右下角坐标。 |
| [bool OH\_Drawing\_RectIntersect(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other)](capi-drawing-rect-h.md#oh_drawing_rectintersect) | 用于判断两个矩形是否相交，若相交，将rect设置为两个矩形的交集。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect、other任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_RectJoin(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other)](capi-drawing-rect-h.md#oh_drawing_rectjoin) | 将rect设置为两个矩形的并集。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect、other任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_RectSetLeft(OH\_Drawing\_Rect\* rect, float left)](capi-drawing-rect-h.md#oh_drawing_rectsetleft) | 用于设置矩形左上角的横坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_RectSetTop(OH\_Drawing\_Rect\* rect, float top)](capi-drawing-rect-h.md#oh_drawing_rectsettop) | 用于设置矩形左上角的纵坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_RectSetRight(OH\_Drawing\_Rect\* rect, float right)](capi-drawing-rect-h.md#oh_drawing_rectsetright) | 用于设置矩形右下角的横坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_RectSetBottom(OH\_Drawing\_Rect\* rect, float bottom)](capi-drawing-rect-h.md#oh_drawing_rectsetbottom) | 用于设置矩形右下角的纵坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_RectGetLeft(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectgetleft) | 用于获取给矩形设置的左上角的横坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_RectGetTop(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectgettop) | 用于获取给矩形设置的左上角的纵坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_RectGetRight(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectgetright) | 用于获取给矩形设置的右下角的横坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_RectGetBottom(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectgetbottom) | 用于获取给矩形设置的右下角的纵坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_RectGetHeight(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectgetheight) | 用于获取矩形对象的高度，计算方式为设置的矩形的右下角纵坐标减去左上角纵坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_RectGetWidth(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectgetwidth) | 用于获取矩形对象的宽度，计算方式为设置的矩形的右下角横坐标减去左上角横坐标。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_RectCopy(OH\_Drawing\_Rect\* src, OH\_Drawing\_Rect\* dst)](capi-drawing-rect-h.md#oh_drawing_rectcopy) | 用于将源矩形对象复制到目标矩形对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  src、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_RectDestroy(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectdestroy) | 用于销毁矩形对象并回收该对象占用的内存。 |
| [OH\_Drawing\_Array\* OH\_Drawing\_RectCreateArray(size\_t size)](capi-drawing-rect-h.md#oh_drawing_rectcreatearray) | 用于创建一个矩形数组对象，以存储多个矩形对象。不再需要[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)时，请使用[OH\_Drawing\_RectDestroyArray](capi-drawing-rect-h.md#oh_drawing_rectdestroyarray)接口释放该对象的指针。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectGetArraySize(OH\_Drawing\_Array\* rectArray, size\_t\* pSize)](capi-drawing-rect-h.md#oh_drawing_rectgetarraysize) | 用于获取矩形数组对象[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的大小。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectGetArrayElement(OH\_Drawing\_Array\* rectArray, size\_t index,OH\_Drawing\_Rect\*\* rect)](capi-drawing-rect-h.md#oh_drawing_rectgetarrayelement) | 用于获取矩形数组对象中指定索引的矩形对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectDestroyArray(OH\_Drawing\_Array\* rectArray)](capi-drawing-rect-h.md#oh_drawing_rectdestroyarray) | 用于销毁矩形数组对象并回收该对象占用的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectContains(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other, bool\* isContains)](capi-drawing-rect-h.md#oh_drawing_rectcontains) | 用于判断一个矩形是否完全包含另一个矩形。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectInset(OH\_Drawing\_Rect\* rect, float left, float top, float right, float bottom)](capi-drawing-rect-h.md#oh_drawing_rectinset) | 将指定的值分别添加到矩形的左、上、右、下边界坐标，调整矩形的大小和位置。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectIsEmpty(const OH\_Drawing\_Rect\* rect, bool\* isEmpty)](capi-drawing-rect-h.md#oh_drawing_rectisempty) | 用于判断矩形是否为空，即矩形的宽度或高度是否小于等于0。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectOffset(OH\_Drawing\_Rect\* rect, float dx, float dy)](capi-drawing-rect-h.md#oh_drawing_rectoffset) | 将矩形分别沿x轴方向和y轴方向偏移由参数dx和dy指定的距离。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectOffsetTo(OH\_Drawing\_Rect\* rect, float newLeft, float newTop)](capi-drawing-rect-h.md#oh_drawing_rectoffsetto) | 将矩形左上角偏移到由参数newLeft和newTop指定的坐标位置，并保持宽度和高度不变。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectSetEmpty(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectsetempty) | 将矩形置空（矩形左上角和右下角的x轴、y轴坐标都置为0）。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectSort(OH\_Drawing\_Rect\* rect)](capi-drawing-rect-h.md#oh_drawing_rectsort) | 将矩形坐标进行排序，确保左上角坐标不大于右下角坐标。  若左上角x轴坐标大于右下角x轴坐标，则交换两者；若左上角y轴坐标大于右下角y轴坐标，则交换两者。如果坐标已经有序，则不执行任何操作。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectUnion(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other)](capi-drawing-rect-h.md#oh_drawing_rectunion) | 将当前矩形设置为本矩形与另一个矩形的并集。 |

## 函数说明

### OH\_Drawing\_RectCreate()

```c
OH_Drawing_Rect* OH_Drawing_RectCreate(float left, float top, float right, float bottom)
```

**描述**

用于创建一个矩形对象，不会对设置的坐标排序，即允许矩形设置的左上角坐标大于对应的矩形右下角坐标。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float left | 矩形左上角的横坐标，单位为物理像素px。 |
| float top | 矩形左上角的纵坐标，单位为物理像素px。 |
| float right | 矩形右下角的横坐标，单位为物理像素px。 |
| float bottom | 矩形右下角的纵坐标，单位为物理像素px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* | 返回指向创建的矩形对象的指针。 |

### OH\_Drawing\_RectIntersect()

```c
bool OH_Drawing_RectIntersect(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other)
```

**描述**

用于判断两个矩形是否相交，若相交，将rect设置为两个矩形的交集。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect、other任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* other | 指向另一个矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回两个矩形是否相交的结果。true表示这两个矩形相交，rect被设置为两个矩形的交集；false表示不相交，rect保持不变。 |

### OH\_Drawing\_RectJoin()

```c
bool OH_Drawing_RectJoin(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other)
```

**描述**

将rect设置为两个矩形的并集。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect、other任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。取并集后，此矩形会被设置为两矩形的并集。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* other | 指向另一个矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回操作执行结果。true表示成功，false表示失败，失败的原因可能是两个矩形至少有一个为NULL，或者other矩形的宽度或高度为0。 |

### OH\_Drawing\_RectSetLeft()

```c
void OH_Drawing_RectSetLeft(OH_Drawing_Rect* rect, float left)
```

**描述**

用于设置矩形左上角的横坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| float left | 矩形左上角的横坐标，单位为物理像素px。 |

### OH\_Drawing\_RectSetTop()

```c
void OH_Drawing_RectSetTop(OH_Drawing_Rect* rect, float top)
```

**描述**

用于设置矩形左上角的纵坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| float top | 矩形左上角的纵坐标，单位为物理像素px。 |

### OH\_Drawing\_RectSetRight()

```c
void OH_Drawing_RectSetRight(OH_Drawing_Rect* rect, float right)
```

**描述**

用于设置矩形右下角的横坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| float right | 矩形右下角的横坐标，单位为物理像素px。 |

### OH\_Drawing\_RectSetBottom()

```c
void OH_Drawing_RectSetBottom(OH_Drawing_Rect* rect, float bottom)
```

**描述**

用于设置矩形右下角的纵坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| float bottom | 矩形右下角的纵坐标，单位为物理像素px。 |

### OH\_Drawing\_RectGetLeft()

```c
float OH_Drawing_RectGetLeft(OH_Drawing_Rect* rect)
```

**描述**

用于获取给矩形设置的左上角的横坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形左上角的横坐标，单位为物理像素px。 |

### OH\_Drawing\_RectGetTop()

```c
float OH_Drawing_RectGetTop(OH_Drawing_Rect* rect)
```

**描述**

用于获取给矩形设置的左上角的纵坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形左上角的纵坐标，单位为物理像素px。 |

### OH\_Drawing\_RectGetRight()

```c
float OH_Drawing_RectGetRight(OH_Drawing_Rect* rect)
```

**描述**

用于获取给矩形设置的右下角的横坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形右下角的横坐标，单位为物理像素px。 |

### OH\_Drawing\_RectGetBottom()

```c
float OH_Drawing_RectGetBottom(OH_Drawing_Rect* rect)
```

**描述**

用于获取给矩形设置的右下角的纵坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形右下角的纵坐标，单位为物理像素px。 |

### OH\_Drawing\_RectGetHeight()

```c
float OH_Drawing_RectGetHeight(OH_Drawing_Rect* rect)
```

**描述**

用于获取矩形对象的高度，计算方式为设置的矩形的右下角纵坐标减去左上角纵坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形对象的高度，单位为物理像素px。 |

### OH\_Drawing\_RectGetWidth()

```c
float OH_Drawing_RectGetWidth(OH_Drawing_Rect* rect)
```

**描述**

用于获取矩形对象的宽度，计算方式为设置的矩形的右下角横坐标减去左上角横坐标。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形对象的宽度，单位为物理像素px。 |

### OH\_Drawing\_RectCopy()

```c
void OH_Drawing_RectCopy(OH_Drawing_Rect* src, OH_Drawing_Rect* dst)
```

**描述**

用于将源矩形对象复制到目标矩形对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

src、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* src | 指向源矩形对象的指针。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* dst | 指向目标矩形对象的指针。 |

### OH\_Drawing\_RectDestroy()

```c
void OH_Drawing_RectDestroy(OH_Drawing_Rect* rect)
```

**描述**

用于销毁矩形对象并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

### OH\_Drawing\_RectCreateArray()

```c
OH_Drawing_Array* OH_Drawing_RectCreateArray(size_t size)
```

**描述**

用于创建一个矩形数组对象，以存储多个矩形对象。不再需要[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)时，请使用[OH\_Drawing\_RectDestroyArray](capi-drawing-rect-h.md#oh_drawing_rectdestroyarray)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| size\_t size | 指定矩形数组的大小，取值范围为[0, 65536]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* | 返回创建的数组对象OH\_Drawing\_Array指针，如果返回的对象指针为空，表示创建失败。  失败的原因可能为：没有可用的内存或参数错误。 |

### OH\_Drawing\_RectGetArraySize()

```c
OH_Drawing_ErrorCode OH_Drawing_RectGetArraySize(OH_Drawing_Array* rectArray, size_t* pSize)
```

**描述**

用于获取矩形数组对象[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的大小。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* rectArray | 指向矩形数组对象OH\_Drawing\_Array的指针。 |
| size\_t\* pSize | 指向size\_t类型的指针，用于存储矩形数组大小，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数rectArray或pSize为NULL。 |

### OH\_Drawing\_RectGetArrayElement()

```c
OH_Drawing_ErrorCode OH_Drawing_RectGetArrayElement(OH_Drawing_Array* rectArray, size_t index, OH_Drawing_Rect** rect)
```

**描述**

用于获取矩形数组对象中指定索引的矩形对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* rectArray | 指向矩形数组对象OH\_Drawing\_Array的指针。 |
| size\_t index | 矩形数组的索引。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\*\* rect | 指向OH\_Drawing\_Rect的二级指针，作为出参，返回给调用者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数rectArray或者rect为空，或者index越界。 |

### OH\_Drawing\_RectDestroyArray()

```c
OH_Drawing_ErrorCode OH_Drawing_RectDestroyArray(OH_Drawing_Array* rectArray)
```

**描述**

用于销毁矩形数组对象并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* rectArray | 指向矩形数组对象OH\_Drawing\_Array的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数rectArray为空。 |

### OH\_Drawing\_RectContains()

```c
OH_Drawing_ErrorCode OH_Drawing_RectContains(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other, bool* isContains)
```

**描述**

用于判断一个矩形是否完全包含另一个矩形。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象OH\_Drawing\_Rect的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* other | 指向矩形对象OH\_Drawing\_Rect的指针。 |
| bool\* isContains | 表示一个矩形是否完全包含另一个矩形的结果，作为出参使用。true表示rect完全包含other，false表示rect不完全包含other。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数rect或other或isContains为空。 |

### OH\_Drawing\_RectInset()

```c
OH_Drawing_ErrorCode OH_Drawing_RectInset(OH_Drawing_Rect* rect, float left, float top, float right, float bottom)
```

**描述**

将指定的值分别添加到矩形的左、上、右、下边界坐标，调整矩形的大小和位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象OH\_Drawing\_Rect的指针。 |
| float left | 添加到矩形左边界横坐标的值（矩形左上角横坐标），单位为物理像素px。正数使左边界右移（矩形从左侧缩小），负数使左边界左移（矩形向左侧扩展），0表示不改变。 |
| float top | 添加到矩形上边界纵坐标的值（矩形左上角纵坐标），单位为物理像素px。正数使上边界下移（矩形从上方缩小），负数使上边界上移（矩形向上方扩展），0表示不改变。 |
| float right | 添加到矩形右边界横坐标的值（矩形右下角横坐标），单位为物理像素px。正数使右边界右移（矩形向右侧扩展），负数使右边界左移（矩形从右侧缩小），0表示不改变。 |
| float bottom | 添加到矩形下边界纵坐标的值（矩形右下角纵坐标），单位为物理像素px。正数使下边界下移（矩形向下方扩展），负数使下边界上移（矩形从下方缩小），0表示不改变。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数rect为空。 |

### OH\_Drawing\_RectIsEmpty()

```c
OH_Drawing_ErrorCode OH_Drawing_RectIsEmpty(const OH_Drawing_Rect* rect, bool* isEmpty)
```

**描述**

用于判断矩形是否为空，即矩形的宽度或高度是否小于等于0。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象OH\_Drawing\_Rect的指针。 |
| bool\* isEmpty | 表示矩形是否为空。作为出参使用。true表示矩形为空，false表示矩形不为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示rect或isEmpty是空指针。 |

### OH\_Drawing\_RectOffset()

```c
OH_Drawing_ErrorCode OH_Drawing_RectOffset(OH_Drawing_Rect* rect, float dx, float dy)
```

**描述**

将矩形分别沿x轴方向和y轴方向偏移由参数dx和dy指定的距离。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象OH\_Drawing\_Rect的指针。 |
| float dx | 表示在x轴上的偏移距离，单位为物理像素px。正数表示沿x轴正方向偏移，负数表示沿x轴负方向偏移，0表示不偏移。 |
| float dy | 表示在y轴上的偏移距离，单位为物理像素px。正数表示沿y轴正方向偏移，负数表示沿y轴负方向偏移，0表示不偏移。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示rect是空指针。 |

### OH\_Drawing\_RectOffsetTo()

```c
OH_Drawing_ErrorCode OH_Drawing_RectOffsetTo(OH_Drawing_Rect* rect, float newLeft, float newTop)
```

**描述**

将矩形左上角偏移到由参数newLeft和newTop指定的坐标位置，并保持宽度和高度不变。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象OH\_Drawing\_Rect的指针。 |
| float newLeft | 表示偏移后矩形左上角的x轴坐标，单位为物理像素px。 |
| float newTop | 表示偏移后矩形左上角的y轴坐标，单位为物理像素px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示rect是空指针。 |

### OH\_Drawing\_RectSetEmpty()

```c
OH_Drawing_ErrorCode OH_Drawing_RectSetEmpty(OH_Drawing_Rect* rect)
```

**描述**

将矩形置空（矩形左上角和右下角的x轴、y轴坐标都置为0）。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象OH\_Drawing\_Rect的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示rect是空指针。 |

### OH\_Drawing\_RectSort()

```c
OH_Drawing_ErrorCode OH_Drawing_RectSort(OH_Drawing_Rect* rect)
```

**描述**

将矩形坐标进行排序，确保左上角坐标不大于右下角坐标。

若左上角x轴坐标大于右下角x轴坐标，则交换两者；若左上角y轴坐标大于右下角y轴坐标，则交换两者。如果坐标已经有序，则不执行任何操作。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象OH\_Drawing\_Rect的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示rect是空指针。 |

### OH\_Drawing\_RectUnion()

```c
OH_Drawing_ErrorCode OH_Drawing_RectUnion(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other)
```

**描述**

将当前矩形设置为本矩形与另一个矩形的并集。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向当前矩形对象OH\_Drawing\_Rect的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* other | 指向另一个矩形对象OH\_Drawing\_Rect的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示rect或other是空指针。 |
