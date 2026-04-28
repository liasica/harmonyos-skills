---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-path-iterator-h
title: drawing_path_iterator.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_path_iterator.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ba21e7a9513d9ea997b40cefd97608b91c32bbb9acc7ee20f939d934778c037
---

## 概述

PhonePC/2in1TabletTVWearable

声明与路径操作迭代器对象相关的函数。

**引用文件：** <native\_drawing/drawing\_path\_iterator.h>

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
| [OH\_Drawing\_PathIteratorVerb](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratorverb) | OH\_Drawing\_PathIteratorVerb | 迭代器包含的路径操作类型枚举，可用于读取路径的操作指令。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIteratorCreate(const OH\_Drawing\_Path\* path, OH\_Drawing\_PathIterator\*\* pathIterator)](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratorcreate) | 创建路径操作迭代器对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIteratorDestroy(OH\_Drawing\_PathIterator\* pathIterator)](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratordestroy) | 销毁路径操作迭代器对象并回收该对象占有的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIteratorHasNext(const OH\_Drawing\_PathIterator\* pathIterator, bool\* hasNext)](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratorhasnext) | 判断路径操作迭代器中是否还有下一个操作。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIteratorNext(OH\_Drawing\_PathIterator\* pathIterator, OH\_Drawing\_Point2D\* points, uint32\_t count, uint32\_t offset, OH\_Drawing\_PathIteratorVerb\* verb)](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratornext) | 返回当前路径的下一个操作，并将迭代器置于该操作。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIteratorPeek(const OH\_Drawing\_PathIterator\* pathIterator, OH\_Drawing\_PathIteratorVerb\* verb)](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratorpeek) | 返回当前路径的下一个操作，迭代器保持在原操作。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_PathIteratorVerb

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PathIteratorVerb
```

**描述**

迭代器包含的路径操作类型枚举，可用于读取路径的操作指令。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| MOVE = 0 | 设置路径的起始点。 |
| LINE = 1 | 添加线段。 |
| QUAD = 2 | 添加二阶贝塞尔圆滑曲线。 |
| CONIC = 3 | 添加圆锥曲线。 |
| CUBIC = 4 | 添加三阶贝塞尔圆滑曲线。 |
| CLOSE = 5 | 闭合路径。 |
| DONE = CLOSE + 1 | 完成路径设置。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_PathIteratorCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIteratorCreate(const OH_Drawing_Path* path, OH_Drawing_PathIterator** pathIterator)
```

**描述**

创建路径操作迭代器对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)\*\* pathIterator | 指向路径操作迭代器对象[OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)的二级指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示path或pathIterator是空指针。 |

### OH\_Drawing\_PathIteratorDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIteratorDestroy(OH_Drawing_PathIterator* pathIterator)
```

**描述**

销毁路径操作迭代器对象并回收该对象占有的内存。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)\* pathIterator | 指向路径操作迭代器对象[OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示pathIterator是空指针。 |

### OH\_Drawing\_PathIteratorHasNext()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIteratorHasNext(const OH_Drawing_PathIterator* pathIterator, bool* hasNext)
```

**描述**

判断路径操作迭代器中是否还有下一个操作。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)\* pathIterator | 指向路径操作迭代器对象[OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)的指针。 |
| bool\* hasNext | 表示路径操作迭代器中是否还有下一个操作。作为出参使用。true表示还有下一个操作，false表示没有下一个操作。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示pathIterator或hasNext是空指针。 |

### OH\_Drawing\_PathIteratorNext()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIteratorNext(OH_Drawing_PathIterator* pathIterator, OH_Drawing_Point2D* points, uint32_t count, uint32_t offset, OH_Drawing_PathIteratorVerb* verb)
```

**描述**

返回当前路径的下一个操作，并将迭代器置于该操作。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)\* pathIterator | 指向路径操作迭代器对象[OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)的指针。 |
| [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* points | 表示坐标点数组。 |
| uint32\_t count | 表示坐标点数组的大小。 |
| uint32\_t offset | 数组中写入位置相对起始点的偏移量，取值范围为[0, count-4]。 |
| [OH\_Drawing\_PathIteratorVerb](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratorverb)\* verb | 表示当前路径的下一个操作。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示pathIterator或points或verb是空指针。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示count小于offset + 4。 |

### OH\_Drawing\_PathIteratorPeek()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIteratorPeek(const OH_Drawing_PathIterator* pathIterator, OH_Drawing_PathIteratorVerb* verb)
```

**描述**

返回当前路径的下一个操作，迭代器保持在原操作。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)\* pathIterator | 指向路径操作迭代器对象[OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md)的指针。 |
| [OH\_Drawing\_PathIteratorVerb](capi-drawing-path-iterator-h.md#oh_drawing_pathiteratorverb)\* verb | 表示当前路径的下一个操作。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示pathIterator或verb是空指针。 |
