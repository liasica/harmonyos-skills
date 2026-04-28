---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/geometric-shape-drawing-c
title: 几何形状绘制（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 几何形状绘制（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38914501b91f473d2916969b31c30250071ce1da13b774f1e8b1754aa0ec1121
---

## 场景介绍

当前支持绘制的几何形状，主要包括以下几种：

* 点
* 圆弧
* 圆
* 路径
* 区域
* 矩形
* 圆角矩形

大部分的几何形状均可以选择使用画笔或者使用画刷来实现绘制，其中点的绘制只能使用画笔。

## 接口说明

几何形状绘制的常用接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](../harmonyos-references/capi-drawing-canvas-h.md)。

| 接口 | 描述 |
| --- | --- |
| OH\_Drawing\_Point\* OH\_Drawing\_PointCreate (float x, float y) | 用于创建一个坐标点对象。 |
| OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPoint (OH\_Drawing\_Canvas \*canvas, const OH\_Drawing\_Point2D \*point) | 用于画一个点。 |
| OH\_Drawing\_Rect\* OH\_Drawing\_RectCreate (float left, float top, float right, float bottom) | 用于创建一个矩形对象。 |
| void OH\_Drawing\_CanvasDrawArc (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Rect\*, float startAngle, float sweepAngle) | 用于画一个弧。 |
| void OH\_Drawing\_CanvasDrawCircle (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Point\*, float radius) | 用于画一个圆形。 |
| OH\_Drawing\_Path\* OH\_Drawing\_PathCreate (void) | 用于创建一个路径对象。 |
| void OH\_Drawing\_CanvasDrawPath (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Path\*) | 用于画一个自定义路径。 |
| OH\_Drawing\_Region\* OH\_Drawing\_RegionCreate (void) | 用于创建一个区域对象。 |
| void OH\_Drawing\_CanvasDrawRegion (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Region\*) | 用于画一块区域。 |
| void OH\_Drawing\_CanvasDrawRect (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Rect\*) | 用于画一个矩形。 |
| OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCreate (const OH\_Drawing\_Rect\*, float xRad, float yRad) | 用于创建一个圆角矩形对象。 |
| void OH\_Drawing\_CanvasDrawRoundRect (OH\_Drawing\_Canvas\*, const OH\_Drawing\_RoundRect\*) | 用于画一个圆角矩形。 |

## 绘制点

点只能基于画笔在画布上进行绘制，通过使用OH\_Drawing\_CanvasDrawPoint()接口绘制点。接口接受两个参数，一个是画布对象Canvas，请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](canvas-get-result-draw-c.md)；另一个是要绘制的点的指针。

简单示例如下：

```
1. // 创建画笔对象
2. OH_Drawing_Pen* pen = OH_Drawing_PenCreate();
3. // 设置画笔颜色
4. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画笔线宽为40
6. OH_Drawing_PenSetWidth(pen, 40);
7. // 设置画布的画笔
8. OH_Drawing_CanvasAttachPen(canvas, pen);
9. // 绘制5个点
10. AdaptationUtil* adaptationUtil = AdaptationUtil::GetInstance();
11. OH_Drawing_Point2D point1 = {value200_, value200_};
12. OH_Drawing_CanvasDrawPoint(canvas, &point1);
13. OH_Drawing_Point2D point2 = {value400_, value400_};
14. OH_Drawing_CanvasDrawPoint(canvas, &point2);
15. OH_Drawing_Point2D point3 = {value600_, value600_};
16. OH_Drawing_CanvasDrawPoint(canvas, &point3);
17. OH_Drawing_Point2D point4 = {value800_, value800_};
18. OH_Drawing_CanvasDrawPoint(canvas, &point4);
19. OH_Drawing_Point2D point5 = {value1000_, value1000_};
20. OH_Drawing_CanvasDrawPoint(canvas, &point5);
21. // 去除掉画布中的画笔
22. OH_Drawing_CanvasDetachPen(canvas);
23. // 销毁各类对象
24. OH_Drawing_PenDestroy(pen);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L876-L901)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/HGp6SdlRRautJDmfTV_60A/zh-cn_image_0000002583438709.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=FC3539C407CFC977FE22F694F0F9A8226025E4036532CEDB1004C61F5DF363C2)

## 绘制圆弧

可以使用画笔或画刷在画布上进行圆弧的绘制，通过使用OH\_Drawing\_CanvasDrawArc()接口绘制圆弧。使用接口需要传入4个参数，分别如下：

* 需要画布对象Canvas，请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](canvas-get-result-draw-c.md)。
* 绘制圆弧还需要一个矩形，会以矩形的边为轮廓进行绘制。
* 需要一个浮点参数，表示弧形的起始角度。
* 需要另一个浮点参数，表示弧形的扫描角度。

此处以使用画笔绘制圆弧为例，简单示例如下：

```
1. // 创建画笔对象
2. OH_Drawing_Pen* pen = OH_Drawing_PenCreate();
3. // 设置画笔描边颜色
4. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画笔线宽为20
6. OH_Drawing_PenSetWidth(pen, 20);
7. // 设置画布的画笔
8. OH_Drawing_CanvasAttachPen(canvas, pen);
9. // 创建矩形对象，左上坐标为（100，200）右下坐标为（500，300）
10. OH_Drawing_Rect* rect = OH_Drawing_RectCreate(100, 200, 500, 300);
11. // 基于矩形对象绘制圆弧，其实角度10°，扫描角度200°
12. OH_Drawing_CanvasDrawArc(canvas, rect, 10, 200);
13. // 去除掉画布中的画笔
14. OH_Drawing_CanvasDetachPen(canvas);
15. // 销毁各类对象
16. OH_Drawing_PenDestroy(pen);
17. OH_Drawing_RectDestroy(rect);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L906-L924)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/FNuX4F3tSgKGMqjj7hsJ4w/zh-cn_image_0000002552958664.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=DBB5F2DEF91F4093CA481CB8A2683378C61462A4023AF6A78F16FA978B041C7D)

## 绘制圆

可以使用画笔或画刷在画布上进行圆的绘制，通过使用OH\_Drawing\_CanvasDrawCircle()接口绘制圆。使用接口需要传入3个参数，分别如下：

* 需要画布对象Canvas，请确保已创建或获取得到画布Canvas，具体可见[画布的获取与绘制结果的显示（C/C++）](canvas-get-result-draw-c.md)。
* 绘制圆还需要一个指向圆心点对象的指针，会以此点为圆心进行绘制。
* 最后需要一个浮点参数，表示圆的半径。

此处以使用画笔绘制圆为例，简单示例如下：

```
1. // 创建画笔对象
2. OH_Drawing_Pen* pen = OH_Drawing_PenCreate();
3. // 设置画笔描边颜色
4. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画笔线宽为20
6. OH_Drawing_PenSetWidth(pen, 20);
7. // 设置画布的画笔
8. OH_Drawing_CanvasAttachPen(canvas, pen);
9. // 创建圆心点
10. OH_Drawing_Point *point = OH_Drawing_PointCreate(value700_, value700_);
11. // 基于圆心点和半径在画布上绘制圆
12. OH_Drawing_CanvasDrawCircle(canvas, point, value600_);
13. // 去除掉画布中的画笔
14. OH_Drawing_CanvasDetachPen(canvas);
15. // 销毁各类对象
16. OH_Drawing_PenDestroy(pen);
17. OH_Drawing_PointDestroy(point);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L929-L947)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ZBDc54CdSuCq4ggm1RRB9g/zh-cn_image_0000002583478665.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=F493BEFCD94FA7910FB6B44B5E7459B906ABB6E2B1ACE1CC920F948B12986C57)

## 绘制路径

可以使用画笔或画刷在画布上进行路径的绘制，路径具体可以用于绘制直线、弧线、贝塞尔曲线等，也可以通过路径组合的方式组成其他复杂的形状。

绘制路径的相关接口和实现如下，详细的使用和参数说明请见[drawing\_path](../harmonyos-references/capi-drawing-path-h.md)。常用的接口如下：

1. 使用OH\_Drawing\_PathCreate()接口可以创建一个路径对象。
2. 使用OH\_Drawing\_PathMoveTo()接口可以设置自定义路径的起始点位置。
3. 使用OH\_Drawing\_PathLineTo()接口可以添加一条从起始点或路径的最后点位置（若路径没有内容则默认为(0,0)）到目标点位置的线段。

此处以使用画笔和画刷绘制五角星为例，示例如下：

```
1. // 创建画笔对象
2. OH_Drawing_Pen* pen = OH_Drawing_PenCreate();
3. // 设置画笔描边颜色
4. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画笔线宽为10
6. OH_Drawing_PenSetWidth(pen, 10);
7. // 设置 画笔转角样式
8. OH_Drawing_PenSetJoin(pen, LINE_ROUND_JOIN);
9. // 设置画布中的画笔
10. OH_Drawing_CanvasAttachPen(canvas, pen);
11. // 创建画刷，此例对闭合路径进行了颜色填充，所以需要使用画刷
12. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
13. OH_Drawing_BrushSetColor(brush, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MIN, RGBA_MAX, RGBA_MIN));
14. // 设置画布中的画刷
15. OH_Drawing_CanvasAttachBrush(canvas, brush);
16. int len = value551_;
17. float aX = value630_;
18. float aY = value551_;
19. float dX = aX - len * std::sin(18.0f);
20. float dY = aY + len * std::cos(18.0f);
21. float cX = aX + len * std::sin(18.0f);
22. float cY = dY;
23. float bX = aX + (len / 2.0);
24. float bY = aY + std::sqrt((cX - dX) * (cX - dX) + (len / 2.0) * (len / 2.0));
25. float eX = aX - (len / 2.0);
26. float eY = bY;
27. // 创建路径
28. OH_Drawing_Path* path = OH_Drawing_PathCreate();
29. // 到起始点
30. OH_Drawing_PathMoveTo(path, aX, aY);
31. // 绘制直线
32. OH_Drawing_PathLineTo(path, bX, bY);
33. OH_Drawing_PathLineTo(path, cX, cY);
34. OH_Drawing_PathLineTo(path, dX, dY);
35. OH_Drawing_PathLineTo(path, eX, eY);
36. // 直线闭合，形成五角星
37. OH_Drawing_PathClose(path);
38. // 绘制闭合路径
39. OH_Drawing_CanvasDrawPath(canvas, path);
40. // 去除掉画布中的画笔和画刷
41. OH_Drawing_CanvasDetachPen(canvas);
42. OH_Drawing_CanvasDetachBrush(canvas);
43. // 销毁各类对象
44. OH_Drawing_PenDestroy(pen);
45. OH_Drawing_BrushDestroy(brush);
46. OH_Drawing_PathDestroy(path);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L952-L999)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/AsPKLvyFSne0NEwwXhO3Hw/zh-cn_image_0000002552799016.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=7AB752DD4562288F3714D0E2E060A3771FE61DDF3E444E948D9260B8073B13B1)

## 绘制区域

区域不是一个特定的形状，可以设置为指定的矩形或路径，也可以对两个区域进行组合操作。可以使用画笔或画刷在画布上进行区域的绘制。详细的API说明请参考[drawing\_region.h](../harmonyos-references/capi-drawing-region-h.md)。

目前支持设置矩形区域和路径区域，分别通过OH\_Drawing\_RegionSetRect()接口和OH\_Drawing\_RegionSetPath()接口来设置。

此处以使用画刷绘制矩形的组合区域为例，示例如下：

```
1. // 创建画刷对象
2. OH_Drawing_Brush* brush = OH_Drawing_BrushCreate();
3. // 设置画刷填充颜色
4. OH_Drawing_BrushSetColor(brush, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
5. // 设置画布的画刷
6. OH_Drawing_CanvasAttachBrush(canvas, brush);
7. // 矩形区域1
8. OH_Drawing_Region *region1 = OH_Drawing_RegionCreate();
9. OH_Drawing_Rect *rect1 = OH_Drawing_RectCreate(value100_, value100_, value600_, value600_);
10. OH_Drawing_RegionSetRect(region1, rect1);
11. // 矩形区域2
12. OH_Drawing_Region *region2 = OH_Drawing_RegionCreate();
13. OH_Drawing_Rect *rect2 = OH_Drawing_RectCreate(value300_, value300_, value900_, value900_);
14. OH_Drawing_RegionSetRect(region2, rect2);
15. // 两个矩形区域组合
16. OH_Drawing_RegionOp(region1, region2, OH_Drawing_RegionOpMode::REGION_OP_MODE_XOR);
17. OH_Drawing_CanvasDrawRegion(canvas, region1);
18. // 去除掉画布中的画刷
19. OH_Drawing_CanvasDetachBrush(canvas);
20. // 销毁各类对象
21. OH_Drawing_BrushDestroy(brush);
22. OH_Drawing_RegionDestroy(region1);
23. OH_Drawing_RegionDestroy(region2);
24. OH_Drawing_RectDestroy(rect1);
25. OH_Drawing_RectDestroy(rect2);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1004-L1030)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/KxvJShtTQWOVMLXfHgOY3Q/zh-cn_image_0000002583438703.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=FE3206C8BC597C0AD95C0B12BBD6024BBD7F1487665A80FE3244B425A61CA9D3)

## 绘制矩形

可以使用画笔或画刷在画布上进行矩形的绘制。使用OH\_Drawing\_RectCreate()接口创建矩形。接口需要传入四个浮点数，分别表示矩形的左、上、右、下四个位置的坐标，连接这4个坐标形成一个矩形。

简单示例如下：

```
1. // 创建画刷对象
2. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
3. // 设置画刷的填充颜色
4. OH_Drawing_BrushSetColor(brush, 0xffff0000);
5. // 设置画布的画刷
6. OH_Drawing_CanvasAttachBrush(canvas, brush);
7. OH_Drawing_Rect* rect = OH_Drawing_RectCreate(0, 0, value800_, value800_);
8. // 绘制矩形
9. OH_Drawing_CanvasDrawRect(canvas, rect);
10. // 去除画布中的画刷
11. OH_Drawing_CanvasDetachBrush(canvas);
12. // 销毁各类对象
13. OH_Drawing_BrushDestroy(brush);
14. OH_Drawing_RectDestroy(rect);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1035-L1050)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/HfJ62pf9RsyA2RIvlQ221w/zh-cn_image_0000002583438711.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=A7C8D0C84DF802A48D19D962412959DC0035E9185632DB64C9D2FC56C01365DB)

## 绘制圆角矩形

可以使用画笔或画刷在画布上进行圆角矩形的绘制。使用OH\_Drawing\_RoundRectCreate()接口创建圆角矩形。接口需要传入3个参数，分别如下：

* 需要传入指向OH\_Drawing\_Rect矩形对象的指针，用于在此矩形的基础上切圆角进行绘制。
* 需要一个浮点参数，表示x轴上的圆角半径。
* 还需要一个浮点参数，表示y轴上的圆角半径。

简单示例如下：

```
1. // 创建画刷对象
2. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
3. // 设置画刷的填充颜色
4. OH_Drawing_BrushSetColor(brush, 0xffff0000);
5. // 设置画布的画刷
6. OH_Drawing_CanvasAttachBrush(canvas, brush);
7. // 创建矩形
8. OH_Drawing_Rect* rect = OH_Drawing_RectCreate(value100_, value100_, value900_, value600_);
9. // 创建圆角矩形
10. OH_Drawing_RoundRect* roundRect = OH_Drawing_RoundRectCreate(rect, 30, 30);
11. // 绘制圆角矩形
12. OH_Drawing_CanvasDrawRoundRect(canvas, roundRect);
13. // 去除掉画布中的画刷
14. OH_Drawing_CanvasDetachBrush(canvas);
15. // 销毁各类对象
16. OH_Drawing_BrushDestroy(brush);
17. OH_Drawing_RectDestroy(rect);
18. OH_Drawing_RoundRectDestroy(roundRect);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1055-L1074)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/XmDnpD4BSPOaJyFRKTgc4Q/zh-cn_image_0000002552958666.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=AF79CBB0C17E161223581F851F55A54A143BD012CAB430FD3375BAA81F22EC2B)

## 示例代码

* [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
