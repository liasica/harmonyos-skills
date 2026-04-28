---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-pen
title: Class (Pen)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Pen)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eaadb1292371f09a1ea39903d47d84db092b310f73f1d8de791833115d5cf0c3
---

画笔对象，描述所绘制图形形状的轮廓信息。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## constructor12+

PhonePC/2in1TabletTVWearable

constructor()

构造一个新的画笔对象。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
```

## constructor12+

PhonePC/2in1TabletTVWearable

constructor(pen: Pen)

复制构造一个新的画笔对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pen | [Pen](arkts-apis-graphics-drawing-pen.md) | 是 | 待复制的画笔对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. const penColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
5. pen.setColor(penColor);
6. pen.setStrokeWidth(10);
7. const newPen = new drawing.Pen(pen);
```

## setMiterLimit12+

PhonePC/2in1TabletTVWearable

setMiterLimit(miter: number): void

设置折线尖角长度与线宽的最大比值，当画笔绘制一条折线，并且[JoinStyle](arkts-apis-graphics-drawing-e.md#joinstyle12)为MITER\_JOIN时，若尖角长度与线宽的比值大于限制值，则该折角使用BEVEL\_JOIN绘制。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| miter | number | 是 | 折线尖角长度与线宽的最大比值，负数在绘制时会被视作4.0处理，非负数正常生效，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setMiterLimit(5);
```

## getMiterLimit12+

PhonePC/2in1TabletTVWearable

getMiterLimit(): number

获取折线尖角的限制值。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回折线尖角长度与线宽的最大比值。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. let miter = pen.getMiterLimit();
```

## setImageFilter12+

PhonePC/2in1TabletTVWearable

setImageFilter(filter: ImageFilter | null): void

设置画笔的图像滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | null | 是 | 图像滤波器，null表示清空画笔的图像滤波器效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let colorfilter = drawing.ColorFilter.createSRGBGammaToLinear();
4. let imgFilter = drawing.ImageFilter.createFromColorFilter(colorfilter);
5. let pen = new drawing.Pen();
6. pen.setImageFilter(imgFilter);
7. pen.setImageFilter(null);
```

## getColorFilter12+

PhonePC/2in1TabletTVWearable

getColorFilter(): ColorFilter

获取画笔的颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let pen = new drawing.Pen();
4. let colorfilter = drawing.ColorFilter.createLumaColorFilter();
5. pen.setColorFilter(colorfilter);
6. let filter = pen.getColorFilter();
```

## setColor

PhonePC/2in1TabletTVWearable

setColor(color: common2D.Color) : void

设置画笔的颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | ARGB格式的颜色，每个颜色通道的值是0到255之间的整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
4. const pen = new drawing.Pen();
5. pen.setColor(color);
```

## setColor12+

PhonePC/2in1TabletTVWearable

setColor(alpha: number, red: number, green: number, blue: number): void

设置画笔的颜色。性能优于[setColor](arkts-apis-graphics-drawing-pen.md#setcolor)接口，推荐使用本接口。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | number | 是 | ARGB格式颜色的透明度通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |
| red | number | 是 | ARGB格式颜色的红色通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |
| green | number | 是 | ARGB格式颜色的绿色通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |
| blue | number | 是 | ARGB格式颜色的蓝色通道值，该参数是0到255之间的整数，传入范围内的浮点数会向下取整。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setColor(255, 255, 0, 0);
```

## setColor18+

PhonePC/2in1TabletTVWearable

setColor(color: number) : void

设置画笔的颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 16进制ARGB格式的颜色。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setColor(0xffff0000);
```

## setColor4f20+

PhonePC/2in1TabletTVWearable

setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void

设置画笔的颜色以及标准色域，与[setColor](arkts-apis-graphics-drawing-pen.md#setcolor)区别在于可以单独设置色域，适用于需要单独设置色域的场景。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color4f | [common2D.Color4f](js-apis-graphics-common2d.md#color4f20) | 是 | ARGB格式的颜色，每个颜色通道的值是0.0-1.0之间的浮点数，大于1.0时，取1.0，小于0.0时，取0.0。 |
| colorSpace | [colorSpaceManager.ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | null | 是 | 标准色域对象，null表示使用SRGB色域。 |

**示例：**

```
1. import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

3. const pen = new drawing.Pen();
4. let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
5. let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
6. pen.setColor4f(color4f, colorSpace);
```

## getColor12+

PhonePC/2in1TabletTVWearable

getColor(): common2D.Color

获取画笔的颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Color](js-apis-graphics-common2d.md#color) | 返回画笔的颜色。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
4. const pen = new drawing.Pen();
5. pen.setColor(color);
6. let colorGet = pen.getColor();
```

## getColor4f20+

PhonePC/2in1TabletTVWearable

getColor4f(): common2D.Color4f

获取画笔的颜色，与[getColor](arkts-apis-graphics-drawing-pen.md#getcolor12)的区别在于返回值类型为浮点数，适用于需要浮点数类型的场景。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Color4f](js-apis-graphics-common2d.md#color4f20) | 返回画笔的颜色。 |

**示例：**

```
1. import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

3. const pen = new drawing.Pen();
4. let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
5. let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
6. pen.setColor4f(color4f, colorSpace);
7. let color = pen.getColor4f();
```

## getHexColor18+

PhonePC/2in1TabletTVWearable

getHexColor(): number

获取画笔的颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回画笔的颜色，以16进制ARGB格式的32位无符号整数表示。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. let color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
4. let pen = new drawing.Pen();
5. pen.setColor(color);
6. let hex_color: number = pen.getHexColor();
7. console.info('getHexColor: ', hex_color.toString(16));
```

## setStrokeWidth

PhonePC/2in1TabletTVWearable

setStrokeWidth(width: number) : void

设置画笔的线宽。0线宽被视作特殊的极细线宽，在绘制时始终会被绘制为1像素，不随画布的缩放而改变；负数线宽在实际绘制时会被视作0线宽。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 表示线宽，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setStrokeWidth(5);
```

## getWidth12+

PhonePC/2in1TabletTVWearable

getWidth(): number

获取画笔的线宽属性，线宽描述了画笔绘制图形轮廓的宽度。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回画笔的线宽，单位为物理像素px。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. let width = pen.getWidth();
```

## setAntiAlias

PhonePC/2in1TabletTVWearable

setAntiAlias(aa: boolean) : void

设置画笔是否开启抗锯齿。开启后，可以使得图形的边缘在显示时更平滑。未调用此接口设置时，系统默认关闭抗锯齿。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aa | boolean | 是 | 表示是否开启抗锯齿。true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setAntiAlias(true);
```

## isAntiAlias12+

PhonePC/2in1TabletTVWearable

isAntiAlias(): boolean

获取画笔是否开启抗锯齿属性。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回画笔是否开启抗锯齿属性，true表示开启，false表示关闭。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. let isAntiAlias = pen.isAntiAlias();
```

## setAlpha

PhonePC/2in1TabletTVWearable

setAlpha(alpha: number) : void

设置画笔的透明度。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | number | 是 | 用于表示透明度的[0, 255]区间内的整数值，传入浮点类型时向下取整。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setAlpha(128);
```

## getAlpha12+

PhonePC/2in1TabletTVWearable

getAlpha(): number

获取画笔的透明度。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回画笔的透明度，该返回值为0到255之间的整数。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. let alpha = pen.getAlpha();
```

## setColorFilter

PhonePC/2in1TabletTVWearable

setColorFilter(filter: ColorFilter | null) : void

给画笔添加额外的颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | null | 是 | 颜色滤波器。null表示清空颜色滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
5. pen.setColorFilter(colorFilter);
```

## setMaskFilter12+

PhonePC/2in1TabletTVWearable

setMaskFilter(filter: MaskFilter | null): void

给画笔添加额外的蒙版滤镜。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [MaskFilter](arkts-apis-graphics-drawing-maskfilter.md) | null | 是 | 蒙版滤镜。null表示清空蒙版滤镜。 |

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
10. let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
11. pen.setMaskFilter(maskFilter);
12. }
13. }
```

## setPathEffect12+

PhonePC/2in1TabletTVWearable

setPathEffect(effect: PathEffect | null): void

设置画笔路径效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | null | 是 | 路径效果对象。null表示清空路径效果。 |

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
10. let pathEffect = drawing.PathEffect.createDashPathEffect([30, 10], 0);
11. pen.setPathEffect(pathEffect);
12. }
13. }
```

## setShaderEffect12+

PhonePC/2in1TabletTVWearable

setShaderEffect(shaderEffect: ShaderEffect | null): void

设置画笔着色器效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shaderEffect | [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | null | 是 | 着色器对象。null表示清空着色器效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100, y: 100}, {x: 300, y: 300}, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
5. pen.setShaderEffect(shaderEffect);
```

## setShadowLayer12+

PhonePC/2in1TabletTVWearable

setShadowLayer(shadowLayer: ShadowLayer | null): void

设置画笔阴影层效果。当前仅在绘制文字时生效。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-apis-graphics-drawing-shadowlayer.md) | null | 是 | 阴影层对象。null表示清空阴影层效果。 |

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
7. let font = new drawing.Font();
8. font.setSize(60);
9. let textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
10. let pen = new drawing.Pen();
11. pen.setStrokeWidth(2.0);
12. let pen_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
13. pen.setColor(pen_color);
14. canvas.attachPen(pen);
15. canvas.drawTextBlob(textBlob, 100, 100);
16. canvas.detachPen();
17. let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
18. let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
19. pen.setShadowLayer(shadowLayer);
20. canvas.attachPen(pen);
21. canvas.drawTextBlob(textBlob, 100, 200);
22. canvas.detachPen();
23. }
24. }
```

## setBlendMode

PhonePC/2in1TabletTVWearable

setBlendMode(mode: BlendMode) : void

设置画笔的混合模式。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 颜色的混合模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setBlendMode(drawing.BlendMode.SRC);
```

## setJoinStyle12+

PhonePC/2in1TabletTVWearable

setJoinStyle(style: JoinStyle): void

设置画笔绘制转角的样式。未调用此接口设置时，系统默认的转角样式为MITER\_JOIN。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [JoinStyle](arkts-apis-graphics-drawing-e.md#joinstyle12) | 是 | 折线转角样式。 |

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
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. pen.setJoinStyle(drawing.JoinStyle.ROUND_JOIN);
11. }
12. }
```

## getJoinStyle12+

PhonePC/2in1TabletTVWearable

getJoinStyle(): JoinStyle

获取画笔绘制转角的样式。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| JoinStyle | 返回折线转角的样式。 |

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
10. pen.setJoinStyle(drawing.JoinStyle.ROUND_JOIN);
11. let joinStyle = pen.getJoinStyle();
12. }
13. }
```

## setCapStyle12+

PhonePC/2in1TabletTVWearable

setCapStyle(style: CapStyle): void

设置画笔的线帽样式。未调用此接口设置时，系统默认的线帽样式为FLAT\_CAP。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CapStyle](arkts-apis-graphics-drawing-e.md#capstyle12) | 是 | 描述画笔的线帽样式。 |

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
7. const pen = new drawing.Pen();
8. pen.setStrokeWidth(5);
9. pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
10. pen.setCapStyle(drawing.CapStyle.SQUARE_CAP);
11. }
12. }
```

## getCapStyle12+

PhonePC/2in1TabletTVWearable

getCapStyle(): CapStyle

获取画笔的线帽样式。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CapStyle | 返回画笔的线帽样式。 |

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
10. pen.setCapStyle(drawing.CapStyle.SQUARE_CAP);
11. let capStyle = pen.getCapStyle();
12. }
13. }
```

## setDither

PhonePC/2in1TabletTVWearable

setDither(dither: boolean) : void

开启画笔的抖动绘制效果。抖动绘制可以使得绘制出的颜色更加真实。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dither | boolean | 是 | 是否开启画笔的抖动绘制效果。true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.setDither(true);
```

## getFillPath12+

PhonePC/2in1TabletTVWearable

getFillPath(src: Path, dst: Path): boolean

获取使用画笔绘制的源路径轮廓，并用目标路径表示。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 源路径对象。 |
| dst | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 目标路径对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回获取源路径轮廓是否成功，true表示成功，false表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let pen = new drawing.Pen();
4. let pathSrc: drawing.Path = new drawing.Path();
5. let pathDst: drawing.Path = new drawing.Path();
6. pathSrc.moveTo(0, 0);
7. pathSrc.lineTo(700, 700);
8. let value = pen.getFillPath(pathSrc, pathDst);
```

## reset12+

PhonePC/2in1TabletTVWearable

reset(): void

重置当前画笔为初始状态。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const pen = new drawing.Pen();
4. pen.reset();
```
