---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-lattice-h
title: drawing_lattice.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_lattice.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:82e417b5a28e355cb48c3afb3bad924104e80391a9b542c8267a456ad7b262b4
---

## 概述

PhonePC/2in1TabletTVWearable

声明与矩形网格对象相关的函数。

**引用文件：** <native\_drawing/drawing\_lattice.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 23

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_LatticeRectType](capi-drawing-lattice-h.md#oh_drawing_latticerecttype) | OH\_Drawing\_LatticeRectType | 定义填充网格的矩形类型的枚举。仅在矩形网格对象中使用。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_LatticeDestroy(OH\_Drawing\_Lattice\* lattice)](capi-drawing-lattice-h.md#oh_drawing_latticedestroy) | 用于销毁矩形网格对象并回收该对象占有的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_LatticeCreate(const int\* xDivs, const int\* yDivs, uint32\_t xCount, uint32\_t yCount, const OH\_Drawing\_Rect\* bounds, const OH\_Drawing\_LatticeRectType\* rectTypes, uint32\_t rectTypeCount, const uint32\_t\* colors, uint32\_t colorCount, OH\_Drawing\_Lattice\*\* lattice)](capi-drawing-lattice-h.md#oh_drawing_latticecreate) | 创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制。  如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。  其余网格将进行缩放，来适应剩余的空间。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_LatticeRectType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_LatticeRectType
```

**描述**

定义填充网格的矩形类型的枚举。仅在矩形网格对象中使用。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| DEFAULT | 将图像绘制到矩形网格中。 |
| TRANSPARENT | 将矩形网格设置为透明的。 |
| FIXED\_COLOR | 将矩形网格对象中fColors数组的颜色绘制到矩形网格中。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_LatticeDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_LatticeDestroy(OH_Drawing_Lattice* lattice)
```

**描述**

用于销毁矩形网格对象并回收该对象占有的内存。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Lattice](capi-drawing-oh-drawing-lattice.md)\* lattice | 指向矩形网格对象[OH\_Drawing\_Lattice](capi-drawing-oh-drawing-lattice.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  OH\_DRAWING\_SUCCESS，表示执行成功。  OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示lattice是空指针。 |

### OH\_Drawing\_LatticeCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_LatticeCreate(const int* xDivs, const int* yDivs, uint32_t xCount, uint32_t yCount, const OH_Drawing_Rect* bounds, const OH_Drawing_LatticeRectType* rectTypes, uint32_t rectTypeCount, const uint32_t* colors, uint32_t colorCount, OH_Drawing_Lattice** lattice)
```

**描述**

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制。如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。其余网格将进行缩放，来适应剩余的空间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const int\* xDivs | 用于划分图像的X坐标值数组。该参数为整数。 |
| const int\* yDivs | 用于划分图像的Y坐标值数组。该参数为整数。 |
| uint32\_t xCount | X坐标值数组的大小。取值范围为[0, 5]。 |
| uint32\_t yCount | Y坐标值数组的大小。取值范围为[0, 5]。 |
| [const OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* bounds | 要绘制的原始边界矩形，默认为原始图像矩形大小。参数应为整数，向下取整。 |
| [const OH\_Drawing\_LatticeRectType](capi-drawing-lattice-h.md#oh_drawing_latticerecttype)\* rectTypes | 填充网格的类型数组。 |
| uint32\_t rectTypeCount | rectTypes数组的大小。如果rectTypes不是空指针，数组大小必须等于(xCount + 1)\*(yCount + 1)。  如果rectTypes是空指针，数组大小必须等于0。 |
| const uint32\_t\* colors | 填充网格的颜色数组。 |
| uint32\_t colorCount | colors数组的大小。 如果colors不是空指针，数组大小必须等于(xCount + 1)\*(yCount + 1)。  如果colors是空指针，数组大小必须等于0。 |
| [OH\_Drawing\_Lattice](capi-drawing-oh-drawing-lattice.md)\*\* lattice | 指向矩形网格对象[OH\_Drawing\_Lattice](capi-drawing-oh-drawing-lattice.md)的二级指针，作为出参，返回给调用者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，有以下可能原因：  - xDivs或yDivs是空指针nullptr；  - rectTypes不是空指针，且rectTypeCount不等于(xCount + 1)\*(yCount + 1)。  - colors不是空指针，且colorCount不等于(xCount + 1)\*(yCount + 1)。  - rectTypes是空指针，且rectTypeCount不等于0。  - colors是空指针，且colorCount不等于0。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示rectTypes中的枚举值超过枚举范围。 |
