---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts
title: 复杂绘制效果（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 绘制效果 > 复杂绘制效果（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b5bb816308c67d166fec5247329bdd9f48e5f6248a3607e85535064e546d140
---

除了基础填充颜色、描边颜色和一些样式设置的绘制效果外，还支持通过画刷和画笔实现更多复杂的绘制效果。比如：

* 混合模式。
* 路径效果，如虚线效果。
* 着色器效果，如线性渐变、径向渐变等。
* 滤波效果，如模糊效果等。

## 混合模式

混合模式可以用于画笔或画刷，它定义了如何将源像素（要绘制的内容）与目标像素（已存在于画布上的内容）进行组合。

可以使用setBlendMode()接口将混合模式应用于画刷或画笔中，该接口需要接受一个参数BlendMode，即混合模式的类型，具体可参考[BlendMode](../harmonyos-references/arkts-apis-graphics-drawing-e.md#blendmode)。

关键示例和效果示意图如下所示：

```
1. import { DrawContext, FrameNode, NodeController, RenderNode, UIContext } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L16-L19)

```
1. function drawRenderNode(canvas: drawing.Canvas) {
2. canvas.saveLayer(null, null);
3. const brushCircle = new drawing.Brush();
4. const colorCircle: common2D.Color = {alpha: 255, red: 0, green: 0, blue: 255};
5. brushCircle.setColor(colorCircle);
6. canvas.attachBrush(brushCircle);
7. canvas.drawCircle(500, 500, 200);
8. const brush = new drawing.Brush();
9. //  设置混合模式
10. brush.setBlendMode(drawing.BlendMode.SRC_IN);
11. canvas.saveLayer(null, brush);

13. const brushRect = new drawing.Brush();
14. const colorRect: common2D.Color = {alpha: 255, red: 255, green: 255, blue: 0};
15. brushRect.setColor(colorRect);
16. canvas.attachBrush(brushRect);
17. const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
18. canvas.drawRect(rect);
19. canvas.restore();
20. canvas.restore();
21. canvas.detachBrush();
22. }
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L61-L84)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/w9WW9ZA5R8KK4FwVKilRNA/zh-cn_image_0000002552798994.png?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=A4A553DAA43D70BDE7C47F2213401393F0B5C648D05C4CC30AFF1628AC300AAC)

## 路径效果

路径效果如虚线效果，只用于画笔。

可使用createDashPathEffect()接口设置路径效果。接口接受2个参数，分别为：

* 浮点数数组intervals：表示虚线或者点线的间隔。
* 浮点数phase：表示在intervals数组中的偏移量，即从数组的哪个位置开始应用虚线或点线效果。

此处以绘制矩形虚线路径效果为例，关键示例和效果示意图如下所示：

```
1. // 创建画笔
2. let pen = new drawing.Pen();
3. // 设置线宽
4. pen.setStrokeWidth(10.0);
5. // 设置颜色
6. pen.setColor(0xFF, 0xFF, 0x00, 0x00);
7. // 表示10px的实线，5px的间隔，2px的实线，5px的间隔，以此循环
8. let intervals = [10, 5, 2, 5];
9. // 设置虚线路径效果
10. let effect = drawing.PathEffect.createDashPathEffect(intervals, 0);
11. pen.setPathEffect(effect);
12. // 设置画笔描边效果
13. canvas.attachPen(pen);
14. // 创建矩形
15. let rect: common2D.Rect = {
16. left: VALUE_200,
17. top: VALUE_200,
18. right: VALUE_1000,
19. bottom: VALUE_700
20. };
21. // 绘制矩形
22. canvas.drawRect(rect);
23. // 去除描边效果
24. canvas.detachPen();
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L87-L112)

| 原始图 | 设置虚线效果后的效果图 |
| --- | --- |
|  |  |

## 着色器效果

着色器效果基于画刷或画笔实现，可使用setShaderEffect()接口设置画刷或画笔的着色器效果。当前支持不同的着色器效果，如线性渐变着色器效果、径向渐变着色器效果、扇形渐变着色器效果。

着色器相关接口和具体参数的说明请见[ShaderEffect](../harmonyos-references/arkts-apis-graphics-drawing-shadereffect.md)。

### 线性渐变着色器效果

可使用createLinearGradient()接口创建想要设置的线性渐变着色器效果。接口接受6个参数，分别是开始点、结束点、颜色数组、平铺模式、相对位置数组以及矩阵对象。

* 开始点和结束点用来确定渐变方向。
* 颜色数组用于存储渐变使用到的颜色。
* 相对位置数组则用于确定每种颜色在渐变中的相对位置，如果相对位置为空，颜色将会被均匀地分布在开始点和结束点之间。
* 矩阵对象，用于对着色器做矩阵变换，默认为null，表示单位矩阵。
* 平铺模式用于确定如何在渐变区域之外继续渐变效果，平铺模式分为以下4类：

  + CLAMP：当图像超出其原始边界时，复制边缘颜色。
  + REPEAT：在水平和垂直方向上重复图像。
  + MIRROR：在水平和垂直方向上重复图像，并在相邻的图像之间交替使用镜像图像。
  + DECAL：只在原始域内绘制，在其他地方返回透明黑色。

此处以绘制矩形并使用画刷设置线性渐变着色器效果为例，关键示例和效果示意图如下所示：

```
1. let startPt: common2D.Point = { x: VALUE_100, y: VALUE_100 };
2. let endPt: common2D.Point = { x: VALUE_900, y: VALUE_900 };
3. let colors = [0xFFFFFF00, 0xFFFF0000, 0xFF0000FF];
4. // 创建线性渐变着色器
5. let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, colors, drawing.TileMode.CLAMP);
6. // 创建画刷
7. let brush = new drawing.Brush();
8. // 设置线性着色器
9. brush.setShaderEffect(shaderEffect);
10. // 设置画刷填充效果
11. canvas.attachBrush(brush);
12. let rect: common2D.Rect = {
13. left: VALUE_100,
14. top: VALUE_100,
15. right: VALUE_900,
16. bottom: VALUE_900
17. };
18. // 绘制矩形
19. canvas.drawRect(rect);
20. // 去除填充效果
21. canvas.detachBrush();
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L116-L138)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/KVNzCJGUSNmqn7YnUBhfHg/zh-cn_image_0000002583478645.png?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=7728CC8A39EEE628408EB39F9252047AF81D6ADB036B54EEE16D1405B2CBF4E4)

### 径向渐变着色器效果

可使用createRadialGradient()接口创建想要设置的径向渐变着色器效果。接口接受6个参数，分别是圆心坐标（centerPt）、半径（radius）、颜色数组（colors）、平铺模式（TileMode）、相对位置数组（pos）以及矩阵对象（matrix）。

其实现方式与线性渐变着色器类似，不同的是，径向渐变是由圆心开始向外径向渐变的。

此处以绘制矩形并使用画刷设置径向渐变着色器效果为例，关键示例和效果示意图如下所示：

```
1. let centerPt: common2D.Point = { x: VALUE_500, y: VALUE_500 };
2. let colors = [0xFFFF0000, 0xFF00FF00, 0xFF0000FF];
3. // 创建径向渐变着色器
4. let shaderEffect = drawing.ShaderEffect.createRadialGradient(centerPt, VALUE_600, colors, drawing.TileMode.CLAMP);
5. // 创建画刷
6. let brush = new drawing.Brush();
7. // 设置径向渐变着色器
8. brush.setShaderEffect(shaderEffect);
9. // 设置画刷填充效果
10. canvas.attachBrush(brush);
11. let rect: common2D.Rect = {
12. left: VALUE_100,
13. top: VALUE_100,
14. right: VALUE_900,
15. bottom: VALUE_900
16. };
17. // 绘制矩形
18. canvas.drawRect(rect);
19. // 去除填充效果
20. canvas.detachBrush();
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L142-L163)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/fjxGCo4cQS2bELmdiwGFmg/zh-cn_image_0000002552798996.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=367E6E28C401D7AB08DA2F69DD9E4714BA2E6E72BE311C0F2E8695591A719818)

### 扇形渐变着色器效果

可使用createSweepGradient()接口创建想要设置的扇形渐变着色器效果。接口接受7个参数，分别是圆心坐标（centerPt）、颜色数组（colors）、平铺模式（TileMode）、扇形渐变的起始角度（startAngle）、扇形渐变的结束角度（endAngle）、相对位置数组（pos）以及矩阵对象（matrix）。

其实现方式也与线性渐变着色器类似，不同的是，扇形渐变是在围绕中心点旋转的过程中渐变。

此处以绘制矩形并使用画刷设置扇形渐变着色器效果为例，关键示例和效果示意图如下所示：

```
1. let centerPt: common2D.Point = { x: VALUE_500, y: VALUE_500 };
2. let colors = [0xFF00FFFF, 0xFFFF00FF, 0xFFFFFF00];
3. // 创建扇形渐变着色器
4. let shaderEffect = drawing.ShaderEffect.createSweepGradient(centerPt, colors, drawing.TileMode.CLAMP, 0, 360);
5. // 创建画刷
6. let brush = new drawing.Brush();
7. // 设置扇形渐变着色器
8. brush.setShaderEffect(shaderEffect);
9. // 设置画刷填充效果
10. canvas.attachBrush(brush);
11. let rect: common2D.Rect = {
12. left: VALUE_100,
13. top: VALUE_100,
14. right: VALUE_900,
15. bottom: VALUE_900
16. };
17. // 绘制矩形
18. canvas.drawRect(rect);
19. // 去除填充效果
20. canvas.detachBrush();
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L167-L188)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/DvTIUPySQEmefw9Y5iaNjQ/zh-cn_image_0000002583438691.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234710Z&HW-CC-Expire=86400&HW-CC-Sign=B6A6467E0F49F868BEFBABC1FE4FD73CF7912AEF9389038CBFB74B8E8CA98136)

## 滤波器效果

滤波器效果可基于画刷或画笔实现。当前支持不同的滤波器效果，比如图像滤波器、颜色滤波器、蒙版滤波器。

滤波器相关接口和具体参数的说明请见[ImageFilter](../harmonyos-references/arkts-apis-graphics-drawing-imagefilter.md)。

### 颜色滤波器效果

颜色滤波器可基于画笔或画刷实现，颜色滤波器的相关接口和具体参数的说明请见[ColorFilter](../harmonyos-references/arkts-apis-graphics-drawing-colorfilter.md)。

目前可实现多种颜色滤波器，包括如下：

* 具有混合模式的颜色滤波器。
* 具有5x4颜色矩阵的颜色滤波器。
* 将SRGB的伽玛曲线应用到RGB颜色通道的颜色滤波器。
* 将RGB颜色通道应用于SRGB的伽玛曲线的颜色滤波器。
* 将其输入的亮度值乘以透明度通道， 并将红色、绿色和蓝色通道设置为零的颜色滤波器。
* 由两个颜色滤波器组合而成的颜色滤波器。

此处以具有5x4颜色矩阵的颜色滤波器为例。

可使用createMatrixColorFilter()接口创建具有5x4颜色矩阵的颜色滤波器。接口接受1个参数，表示为颜色矩阵，它是一个长度为20的浮点数数组。数组格式如下：

[ a0, a1, a2, a3, a4 ]

[ b0, b1, b2, b3, b4 ]

[ c0, c1, c2, c3, c4 ]

[ d0, d1, d2, d3, d4 ]

对于每个原始的像素颜色色值（R, G, B, A），变换后的色值（R', G', B', A'）计算公式为：

R' = a0\*R + a1\*G + a2\*B + a3\*A + a4

G' = b0\*R + b1\*G + b2\*B + b3\*A + b4

B' = c0\*R + c1\*G + c2\*B + c3\*A + c4

A' = d0\*R + d1\*G + d2\*B + d3\*A + d4

此处以绘制矩形并使用画刷设置具有5x4颜色矩阵的颜色滤波器效果为例，关键示例和效果示意图如下所示：

```
1. // 创建画刷
2. let brush = new drawing.Brush();
3. // 设置颜色
4. brush.setColor(0xFF, 0xFF, 0x00, 0x00);
5. // 设置颜色矩阵
6. let matrix: number[] = [
7. 1, 0, 0, 0, 0,
8. 0, 1, 0, 0, 0,
9. 0, 0, 0.5, 0.5, 0,
10. 0, 0, 0.5, 0.5, 0
11. ];
12. // 创建5x4颜色矩阵的颜色滤波器
13. let filter = drawing.ColorFilter.createMatrixColorFilter(matrix);
14. // 设置颜色滤波器
15. brush.setColorFilter(filter);
16. // 设置画刷填充效果
17. canvas.attachBrush(brush);
18. let rect: common2D.Rect = {
19. left: VALUE_300,
20. top: VALUE_300,
21. right: VALUE_900,
22. bottom: VALUE_900
23. };
24. // 绘制矩形
25. canvas.drawRect(rect);
26. // 去除填充效果
27. canvas.detachBrush();
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L192-L220)

| 原始图 | 设置5x4颜色矩阵的颜色滤波器后的效果图 |
| --- | --- |
|  |  |

### 图像滤波器效果

图像滤波器可基于画笔或画刷来实现，图像滤波器的相关接口和具体参数的说明请见[ImageFilter](../harmonyos-references/arkts-apis-graphics-drawing-imagefilter.md)。

目前只支持两种图像滤波器：

* 基于颜色滤波器的图像滤波器。

  可通过createFromColorFilter()接口实现，接口接受2个参数，颜色滤波器colorFilter和图像滤波器imageFilter，即把颜色滤波器的效果叠加到图像滤波器imageFilter上，imageFilter可为空，imageFilter为空则只添加颜色滤波器效果。
* 具有模糊效果的图像滤波器。

  可通过createBlurImageFilter()接口实现，接口接受4个参数，sigmaX，sigmaY，cTileMode和imageFilter。sigmaX和sigmaY是模糊的标准差，cTileMode是平铺模式，imageFilter是输入的图像滤波器。

  最终效果即为在输入的图像滤波器imageFilter的基础上进行模糊化处理，即滤波器效果可叠加，imageFilter可为空，imageFilter为空则只添加模糊效果。

此处以绘制矩形并使用画笔添加模糊效果的图像滤波器效果为例，关键示例和效果示意图如下所示：

```
1. // 设置画笔
2. let pen = new drawing.Pen();
3. // 设置线宽
4. pen.setStrokeWidth(10.0);
5. // 设置颜色
6. pen.setColor(0xFF, 0xFF, 0x00, 0x00);
7. // 创建模糊效果图像滤波器
8. let filter = drawing.ImageFilter.createBlurImageFilter(20, 20, drawing.TileMode.CLAMP);
9. // 设置图像滤波器
10. pen.setImageFilter(filter);
11. // 设置画笔描边效果
12. canvas.attachPen(pen);
13. let rect: common2D.Rect = {
14. left: VALUE_300,
15. top: VALUE_300,
16. right: VALUE_900,
17. bottom: VALUE_900
18. };
19. // 绘制矩形
20. canvas.drawRect(rect);
21. // 去除描边效果
22. canvas.detachPen();
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L224-L247)

| 原始图 | 设置模糊效果后的效果图 |
| --- | --- |
|  |  |

### 蒙版滤波器效果

蒙版滤波器的模糊效果仅对透明度和形状边缘进行模糊处理，相对于图像滤波器的模糊效果来说计算成本更低。

蒙版滤波器可基于画笔或画刷实现，蒙版滤波器的相关接口和具体参数的说明请见[MaskFilter](../harmonyos-references/arkts-apis-graphics-drawing-maskfilter.md)。

可使用createBlurMaskFilter()接口创建想要设置具有模糊效果的蒙版滤波器。接口接受2个参数，分别为：

* blurType：用于指定要应用的模糊类型，详细分类请参考[BlurType](../harmonyos-references/arkts-apis-graphics-drawing-e.md#blurtype12)。
* sigma：用于指定要应用的高斯模糊的标准差，标准差必须大于0。

此处以绘制矩形并使用画笔设置蒙版滤波器效果为例，关键示例和效果示意图如下所示：

```
1. // 创建画笔
2. let pen = new drawing.Pen();
3. // 设置线宽
4. pen.setStrokeWidth(10.0);
5. // 设置颜色
6. pen.setColor(0xFF, 0xFF, 0x00, 0x00);
7. // 创建模糊效果的蒙版滤波器
8. let filter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.NORMAL, 20);
9. // 设置模糊效果
10. pen.setMaskFilter(filter);
11. // 设置画笔描边效果
12. canvas.attachPen(pen);
13. let rect: common2D.Rect = {
14. left: VALUE_300,
15. top: VALUE_300,
16. right: VALUE_900,
17. bottom: VALUE_900
18. };
19. // 绘制矩形
20. canvas.drawRect(rect);
21. // 去除描边效果
22. canvas.detachPen();
```

[ComplexEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/ComplexEffect.ets#L251-L274)

| 原始图 | 设置模糊效果后的效果图 |
| --- | --- |
|  |  |

## 示例代码

* [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
