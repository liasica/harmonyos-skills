---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas
title: Class (Canvas)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Canvas)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc3ac0770acbc3f2e033e57cebd6377418c09dc42ea8d2e55d1e67bbe3975bb1
---

承载绘制内容与绘制状态的载体。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

说明

画布自带一个默认画刷，该画刷为黑色，开启反走样，不具备其他任何样式效果。当画布中没有主动设置画刷和画笔时，该默认画刷生效。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(pixelmap: image.PixelMap)

创建一个以PixelMap作为绘制目标的Canvas对象。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 构造函数入参。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. import { image } from '@kit.ImageKit';

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. const canvas = new drawing.Canvas(pixelMap);
15. })
```

## drawRect

PhonePC/2in1TabletTVWearable

drawRect(rect: common2D.Rect): void

绘制一个矩形，默认使用黑色填充。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 绘制的矩形区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawRect({ left : 0, right : 10, top : 0, bottom : 10 });
12. canvas.detachPen();
13. }
14. }
```

## drawRect12+

PhonePC/2in1TabletTVWearable

drawRect(left: number, top: number, right: number, bottom: number): void

绘制一个矩形，默认使用黑色填充。性能优于[drawRect](arkts-apis-graphics-drawing-canvas.md#drawrect)接口，推荐使用本接口。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | number | 是 | 矩形的左上角x轴坐标，该参数为浮点数。 |
| top | number | 是 | 矩形的左上角y轴坐标，该参数为浮点数。 |
| right | number | 是 | 矩形的右下角x轴坐标，该参数为浮点数。 |
| bottom | number | 是 | 矩形的右下角y轴坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {

6. draw(context : DrawContext) {
7. const canvas = context.canvas;
8. const pen = new drawing.Pen();
9. pen.setStrokeWidth(5);
10. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
11. canvas.attachPen(pen);
12. canvas.drawRect(0, 0, 10, 10);
13. canvas.detachPen();
14. }
15. }
```

## drawRoundRect12+

PhonePC/2in1TabletTVWearable

drawRoundRect(roundRect: RoundRect): void

画一个圆角矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roundRect | [RoundRect](arkts-apis-graphics-drawing-roundrect.md) | 是 | 圆角矩形对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let rect: common2D.Rect = { left : 100, top : 100, right : 400, bottom : 500 };
8. let roundRect = new drawing.RoundRect(rect, 10, 10);
9. canvas.drawRoundRect(roundRect);
10. }
11. }
```

## drawNestedRoundRect12+

PhonePC/2in1TabletTVWearable

drawNestedRoundRect(outer: RoundRect, inner: RoundRect): void

绘制两个嵌套的圆角矩形，外部矩形边界必须包含内部矩形边界，否则无绘制效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outer | [RoundRect](arkts-apis-graphics-drawing-roundrect.md) | 是 | 圆角矩形对象，表示外部圆角矩形边界。 |
| inner | [RoundRect](arkts-apis-graphics-drawing-roundrect.md) | 是 | 圆角矩形对象，表示内部圆角矩形边界。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let inRect: common2D.Rect = { left : 200, top : 200, right : 400, bottom : 500 };
8. let outRect: common2D.Rect = { left : 100, top : 100, right : 400, bottom : 500 };
9. let outRoundRect = new drawing.RoundRect(outRect, 10, 10);
10. let inRoundRect = new drawing.RoundRect(inRect, 10, 10);
11. canvas.drawNestedRoundRect(outRoundRect, inRoundRect);
12. canvas.drawRoundRect(outRoundRect);
13. }
14. }
```

## drawBackground12+

PhonePC/2in1TabletTVWearable

drawBackground(brush: Brush): void

使用画刷填充画布的可绘制区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brush | [Brush](arkts-apis-graphics-drawing-brush.md) | 是 | 画刷对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const brush = new drawing.Brush();
8. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
9. brush.setColor(color);
10. canvas.drawBackground(brush);
11. }
12. }
```

## drawShadow12+

PhonePC/2in1TabletTVWearable

drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag) : void

绘制射灯类型阴影，使用路径描述环境光阴影的轮廓。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 路径对象，可生成阴影。 |
| planeParams | [common2D.Point3d](js-apis-graphics-common2d.md#point3d12) | 是 | 表示一个三维向量，用于计算遮挡物相对于画布在z轴上的偏移量，其值取决于x与y坐标。 |
| devLightPos | [common2D.Point3d](js-apis-graphics-common2d.md#point3d12) | 是 | 光线相对于画布的位置。 |
| lightRadius | number | 是 | 圆形灯半径，该参数为浮点数。 |
| ambientColor | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | 环境阴影颜色。 |
| spotColor | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | 点阴影颜色。 |
| flag | [ShadowFlag](arkts-apis-graphics-drawing-e.md#shadowflag12) | 是 | 阴影标志枚举。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const path = new drawing.Path();
8. path.addCircle(100, 200, 100, drawing.PathDirection.CLOCKWISE);
9. let pen = new drawing.Pen();
10. pen.setAntiAlias(true);
11. let pen_color : common2D.Color = { alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00 };
12. pen.setColor(pen_color);
13. pen.setStrokeWidth(10.0);
14. canvas.attachPen(pen);
15. let brush = new drawing.Brush();
16. let brush_color : common2D.Color = { alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00 };
17. brush.setColor(brush_color);
18. canvas.attachBrush(brush);
19. let point1 : common2D.Point3d = {x: 100, y: 80, z:80};
20. let point2 : common2D.Point3d = {x: 200, y: 10, z:40};
21. let color1 : common2D.Color = {alpha: 0xFF, red:0, green:0, blue:0xFF};
22. let color2 : common2D.Color = {alpha: 0xFF, red:0xFF, green:0, blue:0};
23. let shadowFlag : drawing.ShadowFlag = drawing.ShadowFlag.ALL;
24. canvas.drawShadow(path, point1, point2, 30, color1, color2, shadowFlag);
25. }
26. }
```

## drawShadow18+

PhonePC/2in1TabletTVWearable

drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color | number, spotColor: common2D.Color | number, flag: ShadowFlag) : void

绘制射灯类型阴影，使用路径描述环境光阴影的轮廓。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 路径对象，可生成阴影。 |
| planeParams | [common2D.Point3d](js-apis-graphics-common2d.md#point3d12) | 是 | 表示一个三维向量，用于计算z轴方向的偏移量。 |
| devLightPos | [common2D.Point3d](js-apis-graphics-common2d.md#point3d12) | 是 | 光线相对于画布的位置。 |
| lightRadius | number | 是 | 圆形灯半径，该参数为浮点数。 |
| ambientColor | [common2D.Color](js-apis-graphics-common2d.md#color) | number | 是 | 环境阴影颜色，可以用16进制ARGB格式的32位无符号整数表示。 |
| spotColor | [common2D.Color](js-apis-graphics-common2d.md#color) | number | 是 | 点阴影颜色，可以用16进制ARGB格式的32位无符号整数表示。 |
| flag | [ShadowFlag](arkts-apis-graphics-drawing-e.md#shadowflag12) | 是 | 阴影标志枚举。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const path = new drawing.Path();
8. path.addCircle(300, 600, 100, drawing.PathDirection.CLOCKWISE);
9. let point1 : common2D.Point3d = {x: 100, y: 80, z:80};
10. let point2 : common2D.Point3d = {x: 200, y: 10, z:40};
11. let shadowFlag : drawing.ShadowFlag = drawing.ShadowFlag.ALL;
12. canvas.drawShadow(path, point1, point2, 30, 0xFF0000FF, 0xFFFF0000, shadowFlag);
13. }
14. }
```

## getLocalClipBounds12+

PhonePC/2in1TabletTVWearable

getLocalClipBounds(): common2D.Rect

获取画布裁剪区域的边界。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Rect](js-apis-graphics-common2d.md#rect) | 返回画布裁剪区域的矩形边界。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let clipRect: common2D.Rect = {
8. left : 150, top : 150, right : 300, bottom : 400
9. };
10. canvas.clipRect(clipRect,drawing.ClipOp.DIFFERENCE, true);
11. console.info("test rect.left: " + clipRect.left);
12. console.info("test rect.top: " + clipRect.top);
13. console.info("test rect.right: " + clipRect.right);
14. console.info("test rect.bottom: " + clipRect.bottom);
15. canvas.getLocalClipBounds();
16. }
17. }
```

## getTotalMatrix12+

PhonePC/2in1TabletTVWearable

getTotalMatrix(): Matrix

获取画布矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix](arkts-apis-graphics-drawing-matrix.md) | 返回画布矩阵。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let matrix = new drawing.Matrix();
8. matrix.setMatrix([5, 0, 0, 0, 1, 1, 0, 0, 1]);
9. canvas.setMatrix(matrix);
10. let matrixResult =canvas.getTotalMatrix();
11. }
12. }
```

## drawCircle

PhonePC/2in1TabletTVWearable

drawCircle(x: number, y: number, radius: number): void

绘制一个圆形。如果半径小于等于零，则不绘制。默认使用黑色填充。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 圆心的x坐标，该参数为浮点数。 |
| y | number | 是 | 圆心的y坐标，该参数为浮点数。 |
| radius | number | 是 | 圆的半径，大于0的浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawCircle(10, 10, 2);
12. canvas.detachPen();
13. }
14. }
```

## drawImage

PhonePC/2in1TabletTVWearable

drawImage(pixelmap: image.PixelMap, left: number, top: number, samplingOptions?: SamplingOptions): void

画一张图片，图片的左上角坐标为(left, top)。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片的PixelMap。 |
| left | number | 是 | 图片位置的左上角x轴坐标，该参数为浮点数。 |
| top | number | 是 | 图片位置的左上角y轴坐标，该参数为浮点数。 |
| samplingOptions12+ | [SamplingOptions](arkts-apis-graphics-drawing-samplingoptions.md) | 否 | 采样选项对象，默认为不使用任何参数构造的原始采样选项对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { drawing } from '@kit.ArkGraphics2D';

5. class DrawingRenderNode extends RenderNode {
6. draw(context : DrawContext) {
7. const width = 1000;
8. const height = 1000;
9. const bufferSize = width * height * 4;
10. const color: ArrayBuffer = new ArrayBuffer(bufferSize);

12. const colorData = new Uint8Array(color);
13. for (let i = 0; i < colorData.length; i += 4) {
14. colorData[i] = 255;
15. colorData[i+1] = 156;
16. colorData[i+2] = 0;
17. colorData[i+3] = 255;
18. }

20. let opts : image.InitializationOptions = {
21. editable: true,
22. pixelFormat: 3,
23. size: { height, width }
24. }

26. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
27. const canvas = context.canvas;
28. let options = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
29. if (pixelMap != null) {
30. canvas.drawImage(pixelMap, 0, 0, options);
31. }
32. }
33. }
```

## drawImageRect12+

PhonePC/2in1TabletTVWearable

drawImageRect(pixelmap: image.PixelMap, dstRect: common2D.Rect, samplingOptions?: SamplingOptions): void

将图片绘制到画布的指定区域上。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片的PixelMap。 |
| dstRect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 矩形对象，用于指定画布上图片的绘制区域。 |
| samplingOptions | [SamplingOptions](arkts-apis-graphics-drawing-samplingoptions.md) | 否 | 采样选项对象，默认为不使用任何参数构造的原始采样选项对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { common2D, drawing } from '@kit.ArkGraphics2D';

5. class DrawingRenderNode extends RenderNode {
6. draw(context : DrawContext) {
7. const width = 1000;
8. const height = 1000;
9. const bufferSize = width * height * 4;
10. const color: ArrayBuffer = new ArrayBuffer(bufferSize);

12. const colorData = new Uint8Array(color);
13. for (let i = 0; i < colorData.length; i += 4) {
14. colorData[i] = 255;
15. colorData[i+1] = 156;
16. colorData[i+2] = 0;
17. colorData[i+3] = 255;
18. }

20. let opts : image.InitializationOptions = {
21. editable: true,
22. pixelFormat: 3,
23. size: { height, width }
24. }

26. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
27. const canvas = context.canvas;
28. let pen = new drawing.Pen();
29. canvas.attachPen(pen);
30. let rect: common2D.Rect = { left: 0, top: 0, right: 200, bottom: 200 };
31. canvas.drawImageRect(pixelMap, rect);
32. canvas.detachPen();
33. }
34. }
```

## drawImageRectWithSrc12+

PhonePC/2in1TabletTVWearable

drawImageRectWithSrc(pixelmap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect, samplingOptions?: SamplingOptions, constraint?: SrcRectConstraint): void

将图片的指定区域绘制到画布的指定区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片的PixelMap。 |
| srcRect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 矩形对象，用于指定图片的待绘制区域。 |
| dstRect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 矩形对象，用于指定画布上图片的绘制区域。 |
| samplingOptions | [SamplingOptions](arkts-apis-graphics-drawing-samplingoptions.md) | 否 | 采样选项对象，默认为不使用任何参数构造的原始采样选项对象。 |
| constraint | [SrcRectConstraint](arkts-apis-graphics-drawing-e.md#srcrectconstraint12) | 否 | 源矩形区域约束类型，默认为STRICT。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { common2D, drawing } from '@kit.ArkGraphics2D';

5. class DrawingRenderNode extends RenderNode {
6. draw(context : DrawContext) {
7. const width = 1000;
8. const height = 1000;
9. const bufferSize = width * height * 4;
10. const color: ArrayBuffer = new ArrayBuffer(bufferSize);

12. const colorData = new Uint8Array(color);
13. for (let i = 0; i < colorData.length; i += 4) {
14. colorData[i] = 255;
15. colorData[i+1] = 156;
16. colorData[i+2] = 0;
17. colorData[i+3] = 255;
18. }

20. let opts : image.InitializationOptions = {
21. editable: true,
22. pixelFormat: 3,
23. size: { height, width }
24. }

26. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
27. const canvas = context.canvas;
28. let pen = new drawing.Pen();
29. canvas.attachPen(pen);
30. let srcRect: common2D.Rect = { left: 0, top: 0, right: 100, bottom: 100 };
31. let dstRect: common2D.Rect = { left: 100, top: 100, right: 200, bottom: 200 };
32. canvas.drawImageRectWithSrc(pixelMap, srcRect, dstRect);
33. canvas.detachPen();
34. }
35. }
```

## drawColor

PhonePC/2in1TabletTVWearable

drawColor(color: common2D.Color, blendMode?: BlendMode): void

使用指定颜色并按照指定的[BlendMode](arkts-apis-graphics-drawing-e.md#blendmode)对画布当前可绘制区域进行填充。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | ARGB格式的颜色，每个颜色通道的值是0到255之间的整数。 |
| blendMode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 否 | 颜色混合模式，默认模式为SRC\_OVER。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let color: common2D.Color = {
8. alpha : 255,
9. red: 0,
10. green: 10,
11. blue: 10
12. }
13. canvas.drawColor(color, drawing.BlendMode.CLEAR);
14. }
15. }
```

## drawColor12+

PhonePC/2in1TabletTVWearable

drawColor(alpha: number, red: number, green: number, blue: number, blendMode?: BlendMode): void

使用指定颜色并按照指定的[BlendMode](arkts-apis-graphics-drawing-e.md#blendmode)对画布当前可绘制区域进行填充。性能优于[drawColor](arkts-apis-graphics-drawing-canvas.md#drawcolor)接口，推荐使用本接口。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | number | 是 | ARGB格式颜色的透明度通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |
| red | number | 是 | ARGB格式颜色的红色通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |
| green | number | 是 | ARGB格式颜色的绿色通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |
| blue | number | 是 | ARGB格式颜色的蓝色通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |
| blendMode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 否 | 颜色混合模式，默认模式为SRC\_OVER。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. canvas.drawColor(255, 0, 10, 10, drawing.BlendMode.CLEAR);
8. }
9. }
```

## drawColor18+

PhonePC/2in1TabletTVWearable

drawColor(color: number, blendMode?: BlendMode): void

使用指定颜色并按照指定的[BlendMode](arkts-apis-graphics-drawing-e.md#blendmode)对画布当前可绘制区域进行填充。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 16进制ARGB格式的颜色。 |
| blendMode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 否 | 颜色混合模式，默认模式为SRC\_OVER。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. canvas.drawColor(0xff000a0a, drawing.BlendMode.CLEAR);
8. }
9. }
```

## drawVertices23+

PhonePC/2in1TabletTVWearable

drawVertices(vertexMode: VertexMode, vertexCount: number, positions: Array<common2D.Point>, texs: Array<common2D.Point> | null, colors: Array<number> | null, indexCount: number, indices: Array<number> | null, mode: BlendMode): void

绘制顶点数组描述的三角网格。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vertexMode | [VertexMode](arkts-apis-graphics-drawing-e.md#vertexmode23) | 是 | 绘制顶点的连接方式。 |
| vertexCount | number | 是 | 顶点数组元素的数量，值为大于等于3的整数。 |
| positions | [Array<common2D.Point>](js-apis-graphics-common2d.md#point12) | 是 | 描述顶点位置的数组，不能为空，其长度必须等于vertexCount。 |
| texs | [Array<common2D.Point>](js-apis-graphics-common2d.md#point12) | null | 是 | 描述顶点对应纹理空间坐标的数组。其可以为空，表明纹理空间失效；若不为空，其长度必须等于vertexCount。 |
| colors | Array<number> | null | 是 | 描述顶点对应颜色的数组，用于在三角形中进行插值。其可以为空，表明颜色效果为用户所设置的默认色；若不为空其长度必须等于vertexCount。 |
| indexCount | number | 是 | 索引的数量。其值可以为0，且indices数组长度为0时可以画图；若不为0，则值必须为大于等于3的整数。 |
| indices | Array<number> | null | 是 | 描述顶点对应索引的数组。其可以为空，此时将忽略indexCount的合理传值（大于等于3的整数或等于0）；若不为空其长度必须等于indexCount。 |
| mode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 颜色混合模式。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext): void {
6. const canvas = context.canvas;
7. let pointsArray = new Array<common2D.Point>();
8. const point1: common2D.Point = { x: 100.0, y: 100.0 };
9. const point2: common2D.Point = { x: 200.0, y: 100.0 };
10. const point3: common2D.Point = { x: 150.0, y: 200.0 };
11. pointsArray.push(point1);
12. pointsArray.push(point2);
13. pointsArray.push(point3);
14. let texsArray = new Array<common2D.Point>();
15. const texs1: common2D.Point = { x: 0.0, y: 0.0 };
16. const texs2: common2D.Point = { x: 1.0, y: 0.0 };
17. const texs3: common2D.Point = { x: 0.5, y: 1.0 };
18. texsArray.push(texs1);
19. texsArray.push(texs2);
20. texsArray.push(texs3);
21. const colors = [0xFFFF0000, 0xFF00FF00, 0xFF0000FF];
22. const indices = [0, 1, 2];
23. canvas.drawVertices(drawing.VertexMode.TRIANGLESSTRIP_VERTEXMODE, 3, pointsArray, texsArray, colors, 3, indices,drawing.BlendMode.SRC);
24. }
25. }
```

## drawPixelMapMesh12+

PhonePC/2in1TabletTVWearable

drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number, vertices: Array<number>, vertOffset: number, colors: Array<number>, colorOffset: number): void

在网格上绘制像素图，网格均匀分布在像素图上。（只支持brush，使用pen没有绘制效果。）

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 用于绘制网格的像素图。 |
| meshWidth | number | 是 | 网格中的列数，大于0的整数。 |
| meshHeight | number | 是 | 网格中的行数，大于0的整数。 |
| vertices | Array<number> | 是 | 顶点数组，指定网格的绘制位置，浮点数组，大小必须为((meshWidth+1) \* (meshHeight+1) + vertOffset) \* 2。 |
| vertOffset | number | 是 | 绘图前要跳过的vert元素数，大于等于0的整数。 |
| colors | Array<number> | 是 | 颜色数组，在每个顶点指定一种颜色，整数数组，可为null，大小必须为(meshWidth+1) \* (meshHeight+1) + colorOffset。 |
| colorOffset | number | 是 | 绘制前要跳过的颜色元素数，大于等于0的整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { drawing } from '@kit.ArkGraphics2D';

5. class DrawingRenderNode extends RenderNode {
6. draw(context : DrawContext) {
7. const width = 1000;
8. const height = 1000;
9. const bufferSize = width * height * 4;
10. const color: ArrayBuffer = new ArrayBuffer(bufferSize);

12. const colorData = new Uint8Array(color);
13. for (let i = 0; i < colorData.length; i += 4) {
14. colorData[i] = 255;
15. colorData[i+1] = 156;
16. colorData[i+2] = 0;
17. colorData[i+3] = 255;
18. }

20. let opts : image.InitializationOptions = {
21. editable: true,
22. pixelFormat: 3,
23. size: { height, width }
24. }

26. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
27. const canvas = context.canvas;
28. if (pixelMap != null) {
29. const brush = new drawing.Brush(); // 只支持brush，使用pen没有绘制效果。
30. canvas.attachBrush(brush);
31. let verts : Array<number> = [0, 0, 50, 0, 410, 0, 0, 180, 50, 180, 410, 180, 0, 360, 50, 360, 410, 360]; // 18
32. canvas.drawPixelMapMesh(pixelMap, 2, 2, verts, 0, null, 0);
33. canvas.detachBrush();
34. }
35. }
36. }
```

## clear12+

PhonePC/2in1TabletTVWearable

clear(color: common2D.Color): void

使用指定颜色填充画布上的裁剪区域。效果等同于[drawColor](arkts-apis-graphics-drawing-canvas.md#drawcolor)。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | ARGB格式的颜色，每个颜色通道的值是0到255之间的整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let color: common2D.Color = {alpha: 255, red: 255, green: 0, blue: 0};
8. canvas.clear(color);
9. }
10. }
```

## clear18+

PhonePC/2in1TabletTVWearable

clear(color: common2D.Color | number): void

使用指定颜色填充画布上的裁剪区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | number | 是 | 颜色，可以用16进制ARGB格式的无符号整数表示。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let color: number = 0xffff0000;
8. canvas.clear(color);
9. }
10. }
```

## getWidth12+

PhonePC/2in1TabletTVWearable

getWidth(): number

获取画布的宽度。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回画布的宽度，该参数为浮点数。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let width = canvas.getWidth();
8. console.info('get canvas width:' + width);
9. }
10. }
```

## getHeight12+

PhonePC/2in1TabletTVWearable

getHeight(): number

获取画布的高度。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回画布的高度，该参数为浮点数。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let height = canvas.getHeight();
8. console.info('get canvas height:' + height);
9. }
10. }
```

## drawOval12+

PhonePC/2in1TabletTVWearable

drawOval(oval: common2D.Rect): void

在画布上绘制一个椭圆，椭圆的形状和位置由椭圆的外切矩形给出。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oval | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 矩形区域，该矩形的内切椭圆即为待绘制椭圆。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
10. pen.setColor(color);
11. canvas.attachPen(pen);
12. const rect: common2D.Rect = {left:100, top:50, right:400, bottom:500};
13. canvas.drawOval(rect);
14. canvas.detachPen();
15. }
16. }
```

## drawArc12+

PhonePC/2in1TabletTVWearable

drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void

在画布上绘制圆弧。该方法允许指定起始角度、扫描角度。当扫描角度的绝对值大于360度时，则绘制椭圆。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arc | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 包含要绘制的圆弧的椭圆的矩形边界。 |
| startAngle | number | 是 | 弧的起始角度，单位为度，该参数为浮点数。0度时起始点位于椭圆的右端点，正数时以顺时针方向放置起始点，负数时以逆时针方向放置起始点。 |
| sweepAngle | number | 是 | 弧的扫描角度，单位为度，该参数为浮点数。为正数时顺时针扫描，为负数时逆时针扫描。它的有效范围在-360度到360度之间，当绝对值大于360度时，该方法绘制的是一个椭圆。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
10. pen.setColor(color);
11. canvas.attachPen(pen);
12. const rect: common2D.Rect = {left:100, top:50, right:400, bottom:200};
13. canvas.drawArc(rect, 90, 180);
14. canvas.detachPen();
15. }
16. }
```

## drawPoint

PhonePC/2in1TabletTVWearable

drawPoint(x: number, y: number): void

绘制一个点。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 点的x轴坐标，该参数为浮点数。 |
| y | number | 是 | 点的y轴坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawPoint(10, 10);
12. canvas.detachPen();
13. }
14. }
```

## drawPoints12+

PhonePC/2in1TabletTVWearable

drawPoints(points: Array<common2D.Point>, mode?: PointMode): void

在画布上绘制一组点、线段或多边形。通过指定点的数组和绘制模式来决定绘制方式。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| points | Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 是 | 要绘制的点的数组。长度不能为0。 |
| mode | [PointMode](arkts-apis-graphics-drawing-e.md#pointmode12) | 否 | 绘制数组中的点的方式，默认为drawing.PointMode.POINTS。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(30);
9. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
10. pen.setColor(color);
11. canvas.attachPen(pen);
12. canvas.drawPoints([{x: 100, y: 200}, {x: 150, y: 230}, {x: 200, y: 300}], drawing.PointMode.POINTS);
13. canvas.detachPen();
14. }
15. }
```

## drawPath

PhonePC/2in1TabletTVWearable

drawPath(path: Path): void

绘制一个自定义路径，该路径包含了一组路径轮廓，每个路径轮廓可以是开放的或封闭的。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 要绘制的路径对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. let path = new drawing.Path();
11. path.moveTo(10,10);
12. path.cubicTo(10, 10, 10, 10, 15, 15);
13. path.close();
14. canvas.attachPen(pen);
15. canvas.drawPath(path);
16. canvas.detachPen();
17. }
18. }
```

## drawLine

PhonePC/2in1TabletTVWearable

drawLine(x0: number, y0: number, x1: number, y1: number): void

画一条直线段，从指定的起点到终点。如果直线段的起点和终点是同一个点，无法绘制。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 线段起点的X坐标，该参数为浮点数。 |
| y0 | number | 是 | 线段起点的Y坐标，该参数为浮点数。 |
| x1 | number | 是 | 线段终点的X坐标，该参数为浮点数。 |
| y1 | number | 是 | 线段终点的Y坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawLine(0, 0, 20, 20);
12. canvas.detachPen();
13. }
14. }
```

## drawTextBlob

PhonePC/2in1TabletTVWearable

drawTextBlob(blob: TextBlob, x: number, y: number): void

绘制一段文字。若构造blob的字体不支持待绘制字符，则该部分字符无法绘制。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blob | [TextBlob](arkts-apis-graphics-drawing-textblob.md) | 是 | TextBlob对象。 |
| x | number | 是 | 所绘制出的文字基线（下图蓝线）的左端点（下图红点）的横坐标，该参数为浮点数。 |
| y | number | 是 | 所绘制出的文字基线（下图蓝线）的左端点（下图红点）的纵坐标，该参数为浮点数。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/5LHhSsm1T-WwNL2F_E77iw/zh-cn_image_0000002583480863.png?HW-CC-KV=V1&HW-CC-Date=20260428T001436Z&HW-CC-Expire=86400&HW-CC-Sign=956C4661CD21F6EF41D528B5E213A5134C762978C18C15888C0A6B43C69427A8)

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const brush = new drawing.Brush();
8. brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
9. const font = new drawing.Font();
10. font.setSize(20);
11. const textBlob = drawing.TextBlob.makeFromString("Hello, drawing", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
12. canvas.attachBrush(brush);
13. canvas.drawTextBlob(textBlob, 20, 20);
14. canvas.detachBrush();
15. }
16. }
```

## drawSingleCharacter12+

PhonePC/2in1TabletTVWearable

drawSingleCharacter(text: string, font: Font, x: number, y: number): void

绘制单个字符。当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待绘制的单个字符，字符串的长度必须为1。 |
| font | [Font](arkts-apis-graphics-drawing-font.md) | 是 | 字型对象。 |
| x | number | 是 | 所绘制出的字符基线（下图蓝线）的左端点（下图红点）的横坐标，该参数为浮点数。 |
| y | number | 是 | 所绘制出的字符基线（下图蓝线）的左端点（下图红点）的纵坐标，该参数为浮点数。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/PRlOzvi2TXCjmc9mHOS4mQ/zh-cn_image_0000002583480863.png?HW-CC-KV=V1&HW-CC-Date=20260428T001436Z&HW-CC-Expire=86400&HW-CC-Sign=9C7E7A4358B8FC1BEDF71A26BDCA6D4DF86BB32C7F46E4409AD37CA8F65134D2)

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const brush = new drawing.Brush();
8. brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
9. const font = new drawing.Font();
10. font.setSize(20);
11. canvas.attachBrush(brush);
12. canvas.drawSingleCharacter("你", font, 100, 100);
13. canvas.drawSingleCharacter("好", font, 120, 100);
14. canvas.detachBrush();
15. }
16. }
```

## drawSingleCharacterWithFeatures20+

PhonePC/2in1TabletTVWearable

drawSingleCharacterWithFeatures(text: string, font: Font, x: number, y: number, features: Array<FontFeature>): void

绘制单个字符，字符带有字体特征。当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待绘制的单个字符，字符串长度必须为1。 |
| font | [Font](arkts-apis-graphics-drawing-font.md) | 是 | 字型对象。 |
| x | number | 是 | 所绘制字符基线左端点的横坐标，该参数为浮点数。 |
| y | number | 是 | 所绘制字符基线左端点的纵坐标，该参数为浮点数。 |
| features | Array<[FontFeature](arkts-apis-graphics-drawing-i.md#fontfeature20)> | 是 | 字体特征对象数组。参数为空数组时使用TTF(TrueType Font)文件中预设的字体特征。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const brush = new drawing.Brush();
8. brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
9. const font = new drawing.Font();
10. font.setSize(20);
11. let fontFeatures : Array<drawing.FontFeature> = [];
12. fontFeatures.push({name: 'calt', value: 0});
13. canvas.attachBrush(brush);
14. canvas.drawSingleCharacterWithFeatures("你", font, 100, 100, fontFeatures);
15. canvas.drawSingleCharacterWithFeatures("好", font, 180, 100, fontFeatures);
16. canvas.detachBrush();
17. }
18. }
```

## drawRegion12+

PhonePC/2in1TabletTVWearable

drawRegion(region: Region): void

绘制一个区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 绘制的区域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. let region = new drawing.Region();
9. pen.setStrokeWidth(10);
10. pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
11. canvas.attachPen(pen);
12. region.setRect(100, 100, 400, 400);
13. canvas.drawRegion(region);
14. canvas.detachPen();
15. }
16. }
```

## attachPen

PhonePC/2in1TabletTVWearable

attachPen(pen: Pen): void

绑定画笔到画布上，在画布上进行绘制时，将使用画笔的样式去绘制图形形状的轮廓。

说明

执行该方法后，若pen的效果发生改变并且开发者希望该变化生效于接下来的绘制动作，需要再次执行该方法以确保变化生效。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pen | [Pen](arkts-apis-graphics-drawing-pen.md) | 是 | 画笔对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawRect({ left : 0, right : 10, top : 0, bottom : 10 });
12. canvas.detachPen();
13. }
14. }
```

## attachBrush

PhonePC/2in1TabletTVWearable

attachBrush(brush: Brush): void

绑定画刷到画布上，在画布上进行绘制时，将使用画刷的样式对绘制图形形状的内部进行填充。

说明

执行该方法后，若brush的效果发生改变并且开发者希望该变化生效于接下来的绘制动作，需要再次执行该方法以确保变化生效。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brush | [Brush](arkts-apis-graphics-drawing-brush.md) | 是 | 画刷对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const brush = new drawing.Brush();
8. brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
9. canvas.attachBrush(brush);
10. canvas.drawRect({ left : 0, right : 10, top : 0, bottom : 10 });
11. canvas.detachBrush();
12. }
13. }
```

## detachPen

PhonePC/2in1TabletTVWearable

detachPen(): void

将画笔与画布解绑，在画布上进行绘制时，不会再使用画笔去绘制图形形状的轮廓。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawRect({ left : 0, right : 10, top : 0, bottom : 10 });
12. canvas.detachPen();
13. }
14. }
```

## detachBrush

PhonePC/2in1TabletTVWearable

detachBrush(): void

将画刷与画布解绑，在画布上进行绘制时，不会再使用画刷对绘制图形形状的内部进行填充。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const brush = new drawing.Brush();
8. brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
9. canvas.attachBrush(brush);
10. canvas.drawRect({ left : 0, right : 10, top : 0, bottom : 10 });
11. canvas.detachBrush();
12. }
13. }
```

## clipPath12+

PhonePC/2in1TabletTVWearable

clipPath(path: Path, clipOp?: ClipOp, doAntiAlias?: boolean): void

使用自定义路径对画布的可绘制区域进行裁剪。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 路径对象。 |
| clipOp | [ClipOp](arkts-apis-graphics-drawing-e.md#clipop12) | 否 | 裁剪方式。默认为INTERSECT。 |
| doAntiAlias | boolean | 否 | 表示是否使能抗锯齿绘制。true表示使能，false表示不使能。默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let path = new drawing.Path();
8. path.moveTo(10, 10);
9. path.cubicTo(100, 100, 80, 150, 300, 150);
10. path.close();
11. canvas.clipPath(path, drawing.ClipOp.INTERSECT, true);
12. canvas.clear({alpha: 255, red: 255, green: 0, blue: 0});
13. }
14. }
```

## clipRect12+

PhonePC/2in1TabletTVWearable

clipRect(rect: common2D.Rect, clipOp?: ClipOp, doAntiAlias?: boolean): void

使用矩形对画布的可绘制区域进行裁剪。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 需要裁剪的矩形区域。 |
| clipOp | [ClipOp](arkts-apis-graphics-drawing-e.md#clipop12) | 否 | 裁剪方式。默认为INTERSECT。 |
| doAntiAlias | boolean | 否 | 表示是否使能抗锯齿绘制。true表示使能，false表示不使能。默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. canvas.clipRect({left : 10, right : 500, top : 300, bottom : 900}, drawing.ClipOp.DIFFERENCE, true);
8. canvas.clear({alpha: 255, red: 255, green: 0, blue: 0});
9. }
10. }
```

## save12+

PhonePC/2in1TabletTVWearable

save(): number

保存当前画布状态（画布矩阵和可绘制区域）到栈顶。需要与恢复接口[restore](arkts-apis-graphics-drawing-canvas.md#restore12)配合使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 画布状态个数，该参数为正整数。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let rect: common2D.Rect = {left: 10, right: 200, top: 100, bottom: 300};
8. canvas.drawRect(rect);
9. canvas.save();
10. }
11. }
```

## saveLayer12+

PhonePC/2in1TabletTVWearable

saveLayer(rect?: common2D.Rect | null, brush?: Brush | null): number

保存当前画布的矩阵和裁剪区域，并为后续绘制分配位图。调用恢复接口[restore](arkts-apis-graphics-drawing-canvas.md#restore12)将会舍弃对矩阵和裁剪区域做的更改，并绘制位图。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | null | 否 | 矩形对象，用于限制图层大小，默认为当前画布大小。 |
| brush | [Brush](arkts-apis-graphics-drawing-brush.md) | null | 否 | 画刷对象，绘制位图时会应用画刷对象的透明度，颜色滤波器效果和混合模式，默认不设置额外效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回调用前保存的画布状态数，该参数为正整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. canvas.saveLayer(null, null);
8. const brushRect = new drawing.Brush();
9. const colorRect: common2D.Color = {alpha: 255, red: 255, green: 255, blue: 0};
10. brushRect.setColor(colorRect);
11. canvas.attachBrush(brushRect);
12. const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
13. canvas.drawRect(rect);

15. const brush = new drawing.Brush();
16. brush.setBlendMode(drawing.BlendMode.DST_OUT);
17. canvas.saveLayer(rect, brush);

19. const brushCircle = new drawing.Brush();
20. const colorCircle: common2D.Color = {alpha: 255, red: 0, green: 0, blue: 255};
21. brushCircle.setColor(colorCircle);
22. canvas.attachBrush(brushCircle);
23. canvas.drawCircle(500, 500, 200);
24. canvas.restore();
25. canvas.restore();
26. canvas.detachBrush();
27. }
28. }
```

## scale12+

PhonePC/2in1TabletTVWearable

scale(sx: number, sy: number): void

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个缩放矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个缩放效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | x轴方向的缩放比例，该参数为浮点数。 |
| sy | number | 是 | y轴方向的缩放比例，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.scale(2, 0.5);
12. canvas.drawRect({left : 10, right : 500, top : 300, bottom : 900});
13. canvas.detachPen();
14. }
15. }
```

## skew12+

PhonePC/2in1TabletTVWearable

skew(sx: number, sy: number) : void

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个倾斜矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个倾斜效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | x轴上的倾斜量，该参数为浮点数。正值会使绘制沿y轴增量方向向右倾斜；负值会使绘制沿y轴增量方向向左倾斜。 |
| sy | number | 是 | y轴上的倾斜量，该参数为浮点数。正值会使绘制沿x轴增量方向向下倾斜；负值会使绘制沿x轴增量方向向上倾斜。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.skew(0.1, 0.1);
12. canvas.drawRect({left : 10, right : 500, top : 300, bottom : 900});
13. canvas.detachPen();
14. }
15. }
```

## rotate12+

PhonePC/2in1TabletTVWearable

rotate(degrees: number, sx: number, sy: number) : void

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个旋转矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个旋转效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degrees | number | 是 | 旋转角度，单位为度，该参数为浮点数，正数为顺时针旋转，负数为逆时针旋转。 |
| sx | number | 是 | 旋转中心的横坐标，该参数为浮点数。 |
| sy | number | 是 | 旋转中心的纵坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.rotate(30, 100, 100);
12. canvas.drawRect({left : 10, right : 500, top : 300, bottom : 900});
13. canvas.detachPen();
14. }
15. }
```

## translate12+

PhonePC/2in1TabletTVWearable

translate(dx: number, dy: number): void

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个平移矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个平移效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | number | 是 | x轴方向的移动距离，该参数为浮点数。 |
| dy | number | 是 | y轴方向的移动距离，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.translate(10, 10);
12. canvas.drawRect({left : 10, right : 500, top : 300, bottom : 900});
13. canvas.detachPen();
14. }
15. }
```

## getSaveCount12+

PhonePC/2in1TabletTVWearable

getSaveCount(): number

获取栈中保存的画布状态（画布矩阵和裁剪区域）的数量。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 已保存的画布状态的数量，该参数为正整数。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawRect({left: 10, right: 200, top: 100, bottom: 300});
12. canvas.save();
13. canvas.drawRect({left : 10, right : 500, top : 300, bottom : 900});
14. canvas.getSaveCount();
15. canvas.detachPen();
16. }
17. }
```

## restoreToCount12+

PhonePC/2in1TabletTVWearable

restoreToCount(count: number): void

恢复到指定数量的画布状态（画布矩阵和裁剪区域）。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 要恢复的画布状态深度，该参数为整数。小于等于1时，恢复为初始状态；大于已保存的画布状态数量时，不执行任何操作。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.drawRect({left: 10, right: 200, top: 100, bottom: 300});
12. canvas.save();
13. canvas.drawRect({left: 10, right: 200, top: 100, bottom: 500});
14. canvas.save();
15. canvas.drawRect({left: 100, right: 300, top: 100, bottom: 500});
16. canvas.save();
17. canvas.restoreToCount(2);
18. canvas.drawRect({left : 10, right : 500, top : 300, bottom : 900});
19. canvas.detachPen();
20. }
21. }
```

## restore12+

PhonePC/2in1TabletTVWearable

restore(): void

恢复保存在栈顶的画布状态（画布矩阵和裁剪区域）。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. canvas.attachPen(pen);
11. canvas.restore();
12. canvas.detachPen();
13. }
14. }
```

## concatMatrix12+

PhonePC/2in1TabletTVWearable

concatMatrix(matrix: Matrix): void

画布现有矩阵左乘传入矩阵，不影响之前的绘制操作，后续绘制操作和裁剪操作的形状和位置都会受到该矩阵的影响。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 矩阵对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let matrix = new drawing.Matrix();
8. matrix.setMatrix([5, 0, 0, 0, 1, 2, 0, 0, 1]);
9. canvas.concatMatrix(matrix);
10. canvas.drawRect({left: 10, right: 200, top: 100, bottom: 500});
11. }
12. }
```

## setMatrix12+

PhonePC/2in1TabletTVWearable

setMatrix(matrix: Matrix): void

设置画布的矩阵，后续绘制操作和裁剪操作的形状和位置都会受到该矩阵的影响。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 矩阵对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let matrix = new drawing.Matrix()
8. matrix.setMatrix([5, 0, 0, 0, 1, 1, 0, 0, 1]);
9. canvas.setMatrix(matrix);
10. canvas.drawRect({left: 10, right: 200, top: 100, bottom: 500});
11. }
12. }
```

## isClipEmpty12+

PhonePC/2in1TabletTVWearable

isClipEmpty(): boolean

判断裁剪后的可绘制区域是否为空。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回画布的可绘制区域是否为空的结果，true表示为空，false表示不为空。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. if (canvas.isClipEmpty()) {
8. console.info("canvas.isClipEmpty() returned true");
9. } else {
10. console.info("canvas.isClipEmpty() returned false");
11. }
12. }
13. }
```

## clipRegion12+

PhonePC/2in1TabletTVWearable

clipRegion(region: Region, clipOp?: ClipOp): void

在画布上裁剪一个区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 区域对象，表示裁剪范围。 |
| clipOp | [ClipOp](arkts-apis-graphics-drawing-e.md#clipop12) | 否 | 裁剪方式，默认为INTERSECT。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let region : drawing.Region = new drawing.Region();
8. region.setRect(0, 0, 500, 500);
9. canvas.clipRegion(region);
10. let color: common2D.Color = {alpha: 255, red: 255, green: 0, blue: 0};
11. canvas.clear(color);
12. }
13. }
```

## clipRoundRect12+

PhonePC/2in1TabletTVWearable

clipRoundRect(roundRect: RoundRect, clipOp?: ClipOp, doAntiAlias?: boolean): void

在画布上裁剪一个圆角矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roundRect | [RoundRect](arkts-apis-graphics-drawing-roundrect.md) | 是 | 圆角矩形对象，表示裁剪范围。 |
| clipOp | [ClipOp](arkts-apis-graphics-drawing-e.md#clipop12) | 否 | 裁剪方式，默认为INTERSECT。 |
| doAntiAlias | boolean | 否 | 表示是否使能抗锯齿。true表示使能，false表示不使能。默认为false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let rect: common2D.Rect = { left: 10, top: 100, right: 200, bottom: 300 };
8. let roundRect = new drawing.RoundRect(rect, 10, 10);
9. canvas.clipRoundRect(roundRect);
10. let color: common2D.Color = {alpha: 255, red: 255, green: 0, blue: 0};
11. canvas.clear(color);
12. }
13. }
```

## resetMatrix12+

PhonePC/2in1TabletTVWearable

resetMatrix(): void

将当前画布的矩阵重置为单位矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. canvas.scale(4, 6);
8. canvas.resetMatrix();
9. }
10. }
```

## quickRejectPath18+

PhonePC/2in1TabletTVWearable

quickRejectPath(path: Path): boolean

判断路径与画布区域是否不相交。画布区域包含边界。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 路径对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回路径是否与画布区域不相交的结果。true表示路径与画布区域不相交，false表示路径与画布区域相交。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let path = new drawing.Path();
8. path.moveTo(10, 10);
9. path.cubicTo(10, 10, 10, 10, 15, 15);
10. path.close();
11. if (canvas.quickRejectPath(path)) {
12. console.info("canvas and path do not intersect.");
13. } else {
14. console.info("canvas and path intersect.");
15. }
16. }
17. }
```

## quickRejectRect18+

PhonePC/2in1TabletTVWearable

quickRejectRect(rect: common2D.Rect): boolean

判断矩形和画布区域是否不相交。画布区域包含边界。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 矩形区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回矩形是否与画布区域不相交的结果。true表示矩形与画布区域不相交，false表示矩形与画布区域相交。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let rect: common2D.Rect = { left : 10, top : 20, right : 50, bottom : 30 };
8. if (canvas.quickRejectRect(rect)) {
9. console.info("canvas and rect do not intersect.");
10. } else {
11. console.info("canvas and rect intersect.");
12. }
13. }
14. }
```

## drawArcWithCenter18+

PhonePC/2in1TabletTVWearable

drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void

在画布上绘制圆弧。该方法允许指定圆弧的起始角度、扫描角度以及圆弧的起点和终点是否连接圆弧的中心点。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arc | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 包含要绘制的圆弧的椭圆的矩形边界。 |
| startAngle | number | 是 | 弧的起始角度，单位为度，该参数为浮点数。0度时起始点位于椭圆的右端点，为正数时以顺时针方向放置起始点，为负数时以逆时针方向放置起始点。 |
| sweepAngle | number | 是 | 弧的扫描角度，单位为度，该参数为浮点数。为正数时顺时针扫描，为负数时逆时针扫描。扫描角度可以超过360度，将绘制一个完整的椭圆。 |
| useCenter | boolean | 是 | 绘制时弧形的起点和终点是否连接弧形的中心点。true表示连接，false表示不连接。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
10. pen.setColor(color);
11. canvas.attachPen(pen);
12. const rect: common2D.Rect = { left: 100, top: 50, right: 400, bottom: 200 };
13. canvas.drawArcWithCenter(rect, 90, 180, false);
14. canvas.detachPen();
15. }
16. }
```

## drawImageNine18+

PhonePC/2in1TabletTVWearable

drawImageNine(pixelmap: image.PixelMap, center: common2D.Rect, dstRect: common2D.Rect, filterMode: FilterMode): void

通过绘制两条水平线和两条垂直线将图像分割成9个部分：四个边，四个角和中心。使用此接口时，设置开启抗锯齿无效。

若角落的4个区域尺寸不超过目标矩形，则会在不缩放的情况下被绘制在目标矩形，反之则会按比例缩放绘制在目标矩形；如果还有剩余空间，剩下的5个区域会通过拉伸或压缩来绘制，以便能够完全覆盖目标矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 用于绘制网格的像素图。 |
| center | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 分割图像的中心矩形。矩形四条边所在的直线将图像分成了9个部分。 |
| dstRect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 在画布上绘制的目标矩形区域。 |
| filterMode | [FilterMode](arkts-apis-graphics-drawing-e.md#filtermode12) | 是 | 过滤模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';
3. import { image } from '@kit.ImageKit';

5. class DrawingRenderNode extends RenderNode {
6. draw(context : DrawContext) {
7. const canvas = context.canvas;
8. const width = 1000;
9. const height = 1000;
10. const bufferSize = width * height * 4;
11. const color: ArrayBuffer = new ArrayBuffer(bufferSize);

13. const colorData = new Uint8Array(color);
14. const blockSize = 50;
15. for (let y = 0; y < height; y++) {
16. for (let x = 0; x < width; x++) {
17. const index = (y * width + x) * 4; // 计算当前像素的索引
18. const blockX = Math.floor(x / blockSize);
19. const blockY = Math.floor(y / blockSize);

21. // 通过方块坐标的奇偶性决定颜色
22. if ((blockX + blockY) % 2 === 0) {
23. // 红色方块 (R, G, B, A)
24. colorData[index] = 255;     // R
25. colorData[index + 1] = 0;   // G
26. colorData[index + 2] = 0;   // B
27. } else {
28. // 蓝色方块
29. colorData[index] = 0;       // R
30. colorData[index + 1] = 0;   // G
31. colorData[index + 2] = 255; // B
32. }
33. colorData[index + 3] = 255;   // Alpha 始终为 255（不透明）
34. }
35. }

37. let opts : image.InitializationOptions = {
38. editable: true,
39. pixelFormat: 3,
40. size: { height, width }
41. }
42. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
43. canvas.drawImage(pixelMap, 0, 0); // 原图
44. let center: common2D.Rect = { left: 20, top: 10, right: 50, bottom: 40 };
45. let dst: common2D.Rect = { left: 70, top: 0, right: 100, bottom: 30 };
46. let dst1: common2D.Rect = { left: 110, top: 0, right: 200, bottom: 90 };
47. canvas.drawImageNine(pixelMap, center, dst, drawing.FilterMode.FILTER_MODE_NEAREST); // 示例1
48. canvas.drawImageNine(pixelMap, center, dst1, drawing.FilterMode.FILTER_MODE_NEAREST); // 示例2
49. }
50. }
```

## drawImageLattice18+

PhonePC/2in1TabletTVWearable

drawImageLattice(pixelmap: image.PixelMap, lattice: Lattice, dstRect: common2D.Rect, filterMode: FilterMode): void

将图像按照矩形网格对象的设置划分为多个网格，并把图像的每个部分按照网格对象的设置绘制到画布上的目标矩形区域。使用此接口时，设置开启抗锯齿无效。

偶数行和列（起始计数为0）的每个交叉点都是固定的，若固定网格区域的尺寸不超过目标矩形，则会在不缩放的情况下被绘制在目标矩形，反之则会按比例缩放绘制在目标矩形；如果还有剩余空间，剩下的区域会通过拉伸或压缩来绘制，以便能够完全覆盖目标矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 用于绘制网格的像素图。 |
| lattice | [Lattice](arkts-apis-graphics-drawing-lattice.md) | 是 | 矩形网格对象。 |
| dstRect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 目标矩形区域。 |
| filterMode | [FilterMode](arkts-apis-graphics-drawing-e.md#filtermode12) | 是 | 过滤模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';
3. import { image } from '@kit.ImageKit';

5. class DrawingRenderNode extends RenderNode {
6. draw(context : DrawContext) {
7. const canvas = context.canvas;
8. const width = 1000;
9. const height = 1000;
10. const bufferSize = width * height * 4;
11. const color: ArrayBuffer = new ArrayBuffer(bufferSize);

13. const colorData = new Uint8Array(color);
14. const blockSize = 50;
15. for (let y = 0; y < height; y++) {
16. for (let x = 0; x < width; x++) {
17. const index = (y * width + x) * 4; // 计算当前像素的索引
18. const blockX = Math.floor(x / blockSize);
19. const blockY = Math.floor(y / blockSize);

21. // 通过方块坐标的奇偶性决定颜色
22. if ((blockX + blockY) % 2 === 0) {
23. // 红色方块 (R, G, B, A)
24. colorData[index] = 255;     // R
25. colorData[index + 1] = 0;   // G
26. colorData[index + 2] = 0;   // B
27. } else {
28. // 蓝色方块
29. colorData[index] = 0;       // R
30. colorData[index + 1] = 0;   // G
31. colorData[index + 2] = 255; // B
32. }
33. colorData[index + 3] = 255;   // Alpha 始终为 255（不透明）
34. }
35. }

37. let opts : image.InitializationOptions = {
38. editable: true,
39. pixelFormat: 3,
40. size: { height, width }
41. }
42. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
43. canvas.drawImage(pixelMap, 0, 0); // 原图
44. let xDivs: Array<number> = [28, 36, 44, 52];
45. let yDivs: Array<number> = [28, 36, 44, 52];
46. let lattice = drawing.Lattice.createImageLattice(xDivs, yDivs, 4, 4);
47. let dst: common2D.Rect = { left: 100, top: 0, right: 164, bottom: 64 };
48. let dst1: common2D.Rect = { left: 200, top: 0, right: 360, bottom: 160 };
49. canvas.drawImageLattice(pixelMap, lattice, dst, drawing.FilterMode.FILTER_MODE_NEAREST); // 示例1
50. canvas.drawImageLattice(pixelMap, lattice, dst1, drawing.FilterMode.FILTER_MODE_NEAREST); // 示例2
51. }
52. }
```
