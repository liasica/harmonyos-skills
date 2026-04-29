---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-operation-state-c
title: 画布操作及状态处理（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 画布操作及状态 > 画布操作及状态处理（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f009f2a4d690123709394b68e97980db120a509217ee02239b0173d6a116f24
---

## 场景介绍

创建或获取Canvas画布之后，可以基于画布进一步地进行图形操作和状态处理。画布操作属于可选操作，开发者可以根据场景需要进行。需要先进行画布操作，再进行后续绘制，只有这样画布操作才有效果。

常见的画布操作如下：

* 裁剪。
* 矩阵变换，如平移、缩放、旋转等。
* 状态保存与恢复。

## 裁剪操作

裁剪是图形处理中的常见操作，裁剪针对的是画布本身，可以用于限制绘图区域，只在指定的区域内进行绘制。需要先进行裁剪操作，再进行绘制，才会有对应效果。

当前支持的裁剪操作主要如下：

* 裁剪矩形。
* 裁剪圆角矩形。
* 裁剪自定义路径。
* 裁剪一个区域。

### 接口说明

裁剪操作常用接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](../harmonyos-references/capi-drawing-canvas-h.md)。

| 接口 | 描述 |
| --- | --- |
| void OH\_Drawing\_CanvasClipRect (OH\_Drawing\_Canvas \*, const OH\_Drawing\_Rect \*, OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias) | 用于裁剪一个矩形。 |
| void OH\_Drawing\_CanvasClipRoundRect (OH\_Drawing\_Canvas \*, const OH\_Drawing\_RoundRect \*, OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias) | 用于裁剪一个圆角矩形。 |
| void OH\_Drawing\_CanvasClipPath (OH\_Drawing\_Canvas \*, const OH\_Drawing\_Path \*, OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias) | 用于裁剪一个自定义路径。 |
| OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasClipRegion (OH\_Drawing\_Canvas \*canvas, const OH\_Drawing\_Region \*region, OH\_Drawing\_CanvasClipOp clipOp) | 用于裁剪一个区域。 |

### 开发示例

此处以在画布上裁剪矩形为例给出示例和效果图，其他裁剪操作的逻辑基本相同，注意调用对应的接口并确保要裁剪的数据类型对应准确即可，此处不再一一展开。详细的使用和参数说明请见[drawing\_canvas.h](../harmonyos-references/capi-drawing-canvas-h.md)。

使用OH\_Drawing\_CanvasClipRect接口裁剪矩形。有以下四个入参：

* 第一个参数是画布Canvas，裁剪操作将在这个画布上进行。请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](canvas-get-result-draw-c.md)。
* 第二个参数是要裁剪的矩形区域。
* 第三个参数是裁剪的操作类型，包括交集（INTERSECT）和差集（DIFFERENCE）。
* 第四个参数表示是否需要进行抗锯齿处理。

```
1. // 创建画刷对象
2. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
3. // 设置画刷填充颜色为蓝色
4. OH_Drawing_BrushSetColor(brush, 0xff0000ff);
5. // 在画布中设置画刷
6. OH_Drawing_CanvasAttachBrush(canvas, brush);
7. OH_Drawing_Rect *rect = OH_Drawing_RectCreate(value400_, value400_, value1200_, value1200_);
8. // 裁剪矩形区域
9. OH_Drawing_CanvasClipRect(canvas, rect, OH_Drawing_CanvasClipOp::INTERSECT, true);
10. OH_Drawing_Point *point = OH_Drawing_PointCreate(value600_, value600_);
11. // 绘制圆形
12. OH_Drawing_CanvasDrawCircle(canvas, point, value600_);
13. // 去除画布中的画刷
14. OH_Drawing_CanvasDetachBrush(canvas);
15. // 销毁画刷对象并收回其占的内存
16. OH_Drawing_BrushDestroy(brush);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L387-L404)

| 原始图 | 裁剪后的图 |
| --- | --- |
|  |  |

## 矩阵变换操作

矩阵变换也是常见的画布操作，是一种坐标系的转换，用于进行图形的变化。

当前支持的矩阵变换主要如下：

* 平移
* 缩放
* 旋转

### 接口说明

矩阵变换操作常用接口如下表所示，详细的使用和参数说明请见[drawing\_matrix.h](../harmonyos-references/capi-drawing-matrix-h.md)。

| 接口 | 描述 |
| --- | --- |
| void OH\_Drawing\_CanvasTranslate (OH\_Drawing\_Canvas \*, float dx, float dy) | 用于平移画布一段距离。 |
| void OH\_Drawing\_CanvasScale (OH\_Drawing\_Canvas \*, float sx, float sy) | 用于画布缩放。 |
| void OH\_Drawing\_CanvasRotate (OH\_Drawing\_Canvas \*, float degrees, float px, float py) | 用于画布旋转一定的角度，正数表示顺时针旋转，负数反之。 |
| void OH\_Drawing\_CanvasSkew (OH\_Drawing\_Canvas \*, float sx, float sy) | 用于画布倾斜变换。等同于将当前画布矩阵左乘（premultiply）倾斜变换矩阵，并应用到画布上。其中倾斜变换矩阵为：|1 sx 0| |sy 1 0| |0 0 1|。 |

### 平移

使用OH\_Drawing\_MatrixCreateTranslation()接口实现画布平移。接口接受2个参数，分别为水平方向和垂直方向的平移量，单位为px。

简单示例和示意图如下所示：

```
1. // 创建画刷对象
2. OH_Drawing_Brush* brush = OH_Drawing_BrushCreate();
3. // 设置填充颜色
4. OH_Drawing_BrushSetColor(brush, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画布中的画刷
6. OH_Drawing_CanvasAttachBrush(canvas, brush);
7. // 创建在水平和垂直方向分别平移300px的矩阵对象
8. OH_Drawing_Matrix *matrix = OH_Drawing_MatrixCreateTranslation(value300_, value300_);
9. // 对Canvas进行矩阵变换
10. OH_Drawing_CanvasConcatMatrix(canvas, matrix);
11. // 绘制矩形
12. OH_Drawing_Rect *rect = OH_Drawing_RectCreate(value200_, value300_, value700_, value600_);
13. OH_Drawing_CanvasDrawRect(canvas, rect);
14. // 去除画布中的画刷
15. OH_Drawing_CanvasDetachBrush(canvas);
16. OH_Drawing_RectDestroy(rect);
17. OH_Drawing_MatrixDestroy(matrix);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L409-L427)

| 原始图 | 平移后的效果图 |
| --- | --- |
|  |  |

### 旋转

使用OH\_Drawing\_MatrixCreateRotation()接口实现画布旋转，接口接受3个参数，分别为：旋转角度、旋转中心的x坐标和y坐标。

简单示例和示意图如下所示：

```
1. // 创建画刷对象
2. OH_Drawing_Brush* brush = OH_Drawing_BrushCreate();
3. // 设置填充颜色
4. OH_Drawing_BrushSetColor(brush, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画布中的画刷
6. OH_Drawing_CanvasAttachBrush(canvas, brush);
7. // 创建旋转的矩阵对象，三个参数分别是旋转角度和旋转中心坐标
8. OH_Drawing_Matrix* matrix = OH_Drawing_MatrixCreateRotation(45, value200_, value300_);
9. // 对Canvas进行矩阵变换
10. OH_Drawing_CanvasConcatMatrix(canvas, matrix);
11. // 绘制矩形
12. OH_Drawing_Rect *rect = OH_Drawing_RectCreate(value200_, value300_, value700_, value600_);
13. OH_Drawing_CanvasDrawRect(canvas, rect);
14. // 去除画布中的画刷
15. OH_Drawing_CanvasDetachBrush(canvas);
16. OH_Drawing_RectDestroy(rect);
17. OH_Drawing_MatrixDestroy(matrix);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L432-L450)

| 原始图 | 旋转后的效果图 |
| --- | --- |
|  |  |

### 缩放

使用OH\_Drawing\_MatrixCreateScale()接口进行画布缩放，接口接受4个参数，分别为沿x轴和y轴的缩放因子、旋转中心的x轴和y轴坐标。

简单示例和示意图如下所示：

```
1. // 创建画刷对象
2. OH_Drawing_Brush* brush = OH_Drawing_BrushCreate();
3. // 设置填充颜色
4. OH_Drawing_BrushSetColor(brush, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画布中的画刷
6. OH_Drawing_CanvasAttachBrush(canvas, brush);
7. // 创建缩放的矩阵对象，4个参数分别是旋转中心坐标和水平垂直方向的缩放因子
8. OH_Drawing_Matrix* matrix = OH_Drawing_MatrixCreateScale(2, 2, value200_, value300_);
9. // 对Canvas进行矩阵变换
10. OH_Drawing_CanvasConcatMatrix(canvas, matrix);
11. // 绘制矩形
12. OH_Drawing_Rect *rect = OH_Drawing_RectCreate(value200_, value300_, value700_, value600_);
13. OH_Drawing_CanvasDrawRect(canvas, rect);
14. // 去除画布中的画刷
15. OH_Drawing_CanvasDetachBrush(canvas);
16. OH_Drawing_RectDestroy(rect);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L455-L472)

| 原始图 | 放大后的效果图 |
| --- | --- |
|  |  |

## 画布状态保存与恢复

保存操作用于保存当前画布的状态到一个栈顶，恢复操作用于恢复保存在栈顶的画布状态，恢复操作一旦执行，保存和恢复操作中间一系列平移、缩放、裁剪等操作都会被清除。

### 接口说明

画布状态保存与恢复使用的接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](../harmonyos-references/capi-drawing-canvas-h.md)。

| 接口 | 描述 |
| --- | --- |
| void OH\_Drawing\_CanvasSave (OH\_Drawing\_Canvas \*) | 用于保存当前画布的状态（画布矩阵）到一个栈顶。 |
| void OH\_Drawing\_CanvasRestore (OH\_Drawing\_Canvas \*) | 用于恢复保存在栈顶的画布状态（画布矩阵）。 |
| void OH\_Drawing\_CanvasRestoreToCount (OH\_Drawing\_Canvas \*, uint32\_t saveCount) | 用于恢复到指定数量的画布状态（画布矩阵）。 |

### 开发示例

```
1. // 创建画笔对象
2. OH_Drawing_Pen* pen = OH_Drawing_PenCreate();
3. // 设置画笔描边颜色
4. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画笔线宽为20
6. OH_Drawing_PenSetWidth(pen, 20);
7. // 在画布中设置画笔
8. OH_Drawing_CanvasAttachPen(canvas, pen);
9. // 保存当前画布状态，当前是不存在放大等操作的，这个原始状态会被保存下来
10. OH_Drawing_CanvasSave(canvas);
11. OH_Drawing_Matrix *matrix = OH_Drawing_MatrixCreateScale(2, 2, 2, 2);
12. // 放大画布
13. OH_Drawing_CanvasConcatMatrix(canvas, matrix);
14. OH_Drawing_Point* point = OH_Drawing_PointCreate(value300_, value300_);
15. // 绘制圆形，因为执行过放大操作，所以此时绘制的是大圆
16. OH_Drawing_CanvasDrawCircle(canvas, point, value200_);
17. // 恢复操作，将恢复到没有放大的原始状态
18. OH_Drawing_CanvasRestore(canvas);
19. // 绘制圆形，因为已经恢复没有放大的原始状态，所以此时绘制的小圆
20. OH_Drawing_CanvasDrawCircle(canvas, point, value200_);
21. // 去除画布中的画笔
22. OH_Drawing_CanvasDetachPen(canvas);
23. // 销毁画笔对象并收回其占的内存
24. OH_Drawing_PenDestroy(pen);
25. OH_Drawing_PointDestroy(point);
26. OH_Drawing_MatrixDestroy(matrix);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L477-L504)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/A9AEVxpOQAyMxADIjLnwFg/zh-cn_image_0000002589244945.png?HW-CC-KV=V1&HW-CC-Date=20260429T053607Z&HW-CC-Expire=86400&HW-CC-Sign=B8FEA5BB31368C0D9EE11426DB41246CCBE3B9E696807EF991045B7C7D92DCA8)

## 示例代码

* [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
