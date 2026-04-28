---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/geometric-shape-drawing-arkts
title: 几何形状绘制（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 几何形状绘制（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4452f3b2e34b2c80c70efd6645a0a1cb4521a1a8600a8395a8db8b530a4b8ad2
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

大部分的几何形状均可以选择使用画笔或使用画刷来实现绘制，其中点的绘制只能使用画笔。

## 接口说明

几何形状绘制的常用接口如下表所示，详细的使用和参数说明请见[drawing.Canvas](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md)。

| 接口 | 描述 |
| --- | --- |
| drawPoint(x: number, y: number): void | 用于画一个点。 |
| drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void | 用于画一个弧。 |
| drawCircle(x: number, y: number, radius: number): void | 用于画一个圆形。 |
| drawPath(path: Path): void | 用于画一个自定义路径。 |
| drawRegion(region: Region): void | 用于画一块区域。 |
| drawRect(left: number, top: number, right: number, bottom: number): void | 用于画一个矩形。 |
| drawRoundRect(roundRect: RoundRect): void | 用于画一个圆角矩形。 |

## 绘制点

点只能基于画笔在画布上进行绘制，通过使用drawPoint()接口绘制点。绘制点需要接受两个参数，分别为需要绘制的点的x坐标和y坐标。

简单示例如下：

```
1. // 设置画笔
2. let pen = new drawing.Pen();
3. // 设置颜色
4. pen.setColor(0xFF, 0xFF, 0x00, 0x00);
5. // 设置线宽
6. pen.setStrokeWidth(40);
7. // 设置画笔描边效果
8. canvas.attachPen(pen);
9. // 绘制5个点
10. canvas.drawPoint(VALUE_200, VALUE_200);
11. canvas.drawPoint(VALUE_400, VALUE_400);
12. canvas.drawPoint(VALUE_600, VALUE_600);
13. canvas.drawPoint(VALUE_800, VALUE_800);
14. canvas.drawPoint(VALUE_1000, VALUE_1000);
15. // 去除描边效果
16. canvas.detachPen();
```

[ShapeDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ShapeDrawing.ets#L34-L51)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/D24bOnjURyKnDgHfliQcCA/zh-cn_image_0000002583438701.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=94230C91FD13F79AED43BDCEDE6B8A0DC2EE8C90DA0459EB4268C7D89D9B78D2)

## 绘制圆弧

可以使用画笔或画刷在画布上进行圆弧的绘制，通过使用drawArc()接口绘制圆弧。

绘制圆弧需要一个矩形（[common2D.Rect](../harmonyos-references/js-apis-graphics-common2d.md#rect)），以矩形的边为轮廓进行绘制，还需要两个参数，分别表示弧形的起始角度（startAngle）和扫描角度（sweepAngle）。

此处以使用画笔绘制圆弧为例，简单示例如下：

```
1. // 创建画笔
2. let pen = new drawing.Pen();
3. // 设置颜色
4. pen.setColor({
5. alpha: 0xFF,
6. red: 0xFF,
7. green: 0x00,
8. blue: 0x00
9. });
10. // 设置线宽
11. pen.setStrokeWidth(20);
12. // 设置画笔描边效果
13. canvas.attachPen(pen);
14. // 创建矩形对象
15. const rect: common2D.Rect = {
16. left: VALUE_100,
17. top: VALUE_200,
18. right: VALUE_1000,
19. bottom: VALUE_600
20. };
21. // 绘制矩形
22. canvas.drawArc(rect, 0, 180);
23. // 去除描边效果
24. canvas.detachPen();
```

[ShapeDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ShapeDrawing.ets#L55-L80)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/A1LtHkuKQ46Pf1OChAKyHA/zh-cn_image_0000002552958656.png?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=516CC54E71EDDA304C5672452E440C4EC53E3452F418D28445B641966392A398)

## 绘制圆

可以使用画笔或画刷在画布上进行圆的绘制，通过使用drawCircle()接口绘制圆。

绘制圆需要圆心点的x坐标和y坐标，以及圆半径（radius）。

此处以使用画笔绘制圆为例，简单示例如下：

```
1. // 创建画笔
2. let pen = new drawing.Pen();
3. // 设置颜色
4. pen.setColor({
5. alpha: 0xFF,
6. red: 0xFF,
7. green: 0x00,
8. blue: 0x00
9. });
10. // 设置线宽
11. pen.setStrokeWidth(20);
12. // 设置画笔描边效果
13. canvas.attachPen(pen);
14. // 绘制圆
15. canvas.drawCircle(VALUE_630, VALUE_630, VALUE_500);
16. // 去除描边效果
17. canvas.detachPen();
```

[ShapeDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ShapeDrawing.ets#L84-L102)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/0SF99bRbQDuwAnwpspKGEQ/zh-cn_image_0000002583478657.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=07BFD1EDBB1D94944165242A26E7F7E80654A14601334F3B4292FF2B6E773849)

## 绘制路径

可以使用画笔或画刷在画布上进行路径的绘制，路径具体可以用于绘制直线、弧线、贝塞尔曲线等，也可以通过路径组合的方式组成其他复杂的形状。

绘制路径的相关接口和实现如下，详细的使用和参数说明请见[Path](../harmonyos-references/arkts-apis-graphics-drawing-path.md)。常用的接口如下：

1. 使用new drawing.Path()可以创建一个路径对象。
2. 使用moveTo()接口可以设置自定义路径的起始点位置。
3. 使用lineTo()接口可以添加一条从起始点或路径的最后点位置（若路径没有内容则默认为(0,0)）到目标点位置的线段。

此处以使用画笔和画刷绘制五角星为例，简单示例如下：

```
1. let height_ = VALUE_1800;
2. let width_ = VALUE_1800;
3. let len = height_ / 4;
4. let aX = width_ / 3;
5. let aY = height_ / 6;
6. let dX = aX - len * Math.sin(18.0);
7. let dY = aY + len * Math.cos(18.0);
8. let cX = aX + len * Math.sin(18.0);
9. let cY = dY;
10. let bX = aX + (len / 2.0);
11. let bY = aY + Math.sqrt((cX - dX) * (cX - dX) + (len / 2.0) * (len / 2.0));
12. let eX = aX - (len / 2.0);
13. let eY = bY;

15. // 创建一个path对象，然后使用接口连接成一个五角星形状
16. let path = new drawing.Path();
17. // 指定path的起始位置
18. path.moveTo(aX, aY);
19. // 用直线连接到目标点
20. path.lineTo(bX, bY);
21. path.lineTo(cX, cY);
22. path.lineTo(dX, dY);
23. path.lineTo(eX, eY);
24. // 闭合形状，path绘制完毕
25. path.close();

27. // 创建画笔对象
28. let pen = new drawing.Pen();
29. // 设置抗锯齿
30. pen.setAntiAlias(true);
31. // 设置描边颜色
32. pen.setColor(0xFF, 0xFF, 0x00, 0x00);
33. // 设置线宽
34. pen.setStrokeWidth(10.0);
35. // 设置画笔描边效果
36. canvas.attachPen(pen);
37. // 创建画刷
38. let brush = new drawing.Brush();
39. // 设置填充颜色
40. brush.setColor(0xFF, 0x00, 0xFF, 0x00);
41. // 设置画刷填充效果
42. canvas.attachBrush(brush);
43. // 绘制路径
44. canvas.drawPath(path);
45. // 去除填充效果
46. canvas.detachBrush();
47. // 去除描边效果
48. canvas.detachPen();
```

[ShapeDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ShapeDrawing.ets#L106-L155)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dj5qkcsxR5WpenUT4GEJBQ/zh-cn_image_0000002552799008.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=8A21FC95BD24EAAA7395454966B2EFE5BE96F3BBFA7C10097996F1F7C6C57C60)

## 绘制区域

区域不是一个特定的形状，可以设置为指定的矩形或路径，也可以对两个区域进行组合操作。可以使用画笔或画刷对区域进行绘制。详细的API说明请参考[Region](../harmonyos-references/arkts-apis-graphics-drawing-region.md)。

目前支持设置矩形区域和路径区域，分别通过setRect()接口和setPath()接口来设置。

此处以使用画刷绘制矩形的组合区域为例，示例如下：

```
1. // 创建画刷
2. let brush = new drawing.Brush();
3. // 设置颜色
4. brush.setColor(0xFF, 0xFF, 0x00, 0x00);
5. // 设置画刷填充效果
6. canvas.attachBrush(brush);
7. // 创建左上角的region1
8. let region1 = new drawing.Region();
9. region1.setRect(VALUE_100, VALUE_100, VALUE_600, VALUE_600);
10. // 创建右下角的region2
11. let region2 = new drawing.Region();
12. region2.setRect(VALUE_300, VALUE_300, VALUE_900, VALUE_900);
13. // 将两个区域以XOR的方式组合
14. region1.op(region2, drawing.RegionOp.XOR);
15. // 绘制区域
16. canvas.drawRegion(region1);
17. // 去除填充效果
18. canvas.detachBrush();
```

[ShapeDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ShapeDrawing.ets#L159-L178)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/GgUWiaP6TSmlciUqWNvbRw/zh-cn_image_0000002583438703.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=2C4720D3227175147C61DD48728E69A48BC74CC8FC28BF16B21092A7EF3D4258)

## 绘制矩形

可以使用画笔或画刷在画布上进行矩形的绘制。使用drawRect()接口绘制矩形。接口需要传入四个浮点数，分别表示矩形的左、上、右、下四个位置的坐标，连接这4个坐标形成一个矩形。

此处以使用画刷绘制矩形为例，简单示例如下：

```
1. // 创建画刷
2. let brush = new drawing.Brush();
3. // 设置颜色
4. brush.setColor(0xFF, 0xFF, 0x00, 0x00);
5. // 设置画刷填充效果
6. canvas.attachBrush(brush);
7. // 绘制矩形
8. canvas.drawRect(VALUE_200, VALUE_200, VALUE_1000, VALUE_700);
9. // 去除填充效果
10. canvas.detachBrush();
```

[ShapeDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ShapeDrawing.ets#L182-L193)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/CVpX0PbeT8aEaX4ktqW3fw/zh-cn_image_0000002552958658.png?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=FFD5752B89B5F27433181039D2A175C8FE4DD09B0CCB6C60470E5AA253F53987)

## 绘制圆角矩形

可以使用画笔或画刷在画布上进行圆角矩形的绘制。使用drawRoundRect()接口绘制圆角矩形。接口接受1个入参roundRect，对应为圆角矩形对象。

圆角矩形对象通过new drawing.RoundRect()接口构造，构造函数接受3个参数，分别为：

* common2D.Rect（矩形对象），圆角矩形是在该矩形的基础上切圆角形成。
* x轴上的圆角半径。
* y轴上的圆角半径。

此处以使用画刷绘制圆角矩形为例，简单示例代码如下：

```
1. // 创建画刷
2. let brush = new drawing.Brush();
3. // 设置颜色
4. brush.setColor(0xFF, 0xFF, 0x00, 0x00);
5. // 设置画刷填充效果
6. canvas.attachBrush(brush);
7. // 创建矩形对象
8. let rect: common2D.Rect = {
9. left: VALUE_200,
10. top: VALUE_200,
11. right: VALUE_1000,
12. bottom: VALUE_700
13. };
14. console.info('rect:', rect.right);
15. // 创建圆角矩形对象
16. let rrect = new drawing.RoundRect(rect, 30, 30);
17. // 绘制圆角矩形
18. canvas.drawRoundRect(rrect);
19. // 去除填充效果
20. canvas.detachBrush();
```

[ShapeDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ShapeDrawing.ets#L197-L218)

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/uXk46HdMRbqkeOkPn_B1lw/zh-cn_image_0000002583478659.png?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=B8BB8F548D87ACFE3474FDD74F51CE14069DA6ACFCA380AB7F713926F4E44D74)

## 示例代码

* [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
