---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point2d
title: OH_Drawing_Point2D
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_Point2D
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3696b336ecaff117338ea2f08f470dbe90c7ef4a671a74ae9217e8e0c4414f7b
---

```c
typedef struct {...} OH_Drawing_Point2D
typedef OH_Drawing_Point2D OH_Drawing_Corner_Radii
```

## 概述

OH\_Drawing\_Point2D: 定义一个二维的坐标点。

OH\_Drawing\_Corner\_Radii: 定义一个圆角半径，该圆角半径由x轴方向和y轴方向上的半径组成。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_types.h](capi-drawing-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float x | x轴坐标 |
| float y | y轴坐标 |
