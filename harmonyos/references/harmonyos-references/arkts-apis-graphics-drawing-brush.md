---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-brush
title: Class (Brush)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Brush)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1e6e50fb97cc52fd03242e5655290a07a515ce9dc1ab9d141e06da03a63387f3
---

画刷对象，描述所绘制图形的填充信息。

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

构造一个新的画刷对象。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
```

## constructor12+

PhonePC/2in1TabletTVWearable

constructor(brush: Brush)

复制构造一个新的画刷对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brush | [Brush](arkts-apis-graphics-drawing-brush.md) | 是 | 待复制的画刷对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
4. const brushColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
5. brush.setColor(brushColor);
6. const newBrush = new drawing.Brush(brush);
```

## setColor

PhonePC/2in1TabletTVWearable

setColor(color: common2D.Color) : void

设置画刷的颜色。

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
4. const brush = new drawing.Brush();
5. brush.setColor(color);
```

## setColor12+

PhonePC/2in1TabletTVWearable

setColor(alpha: number, red: number, green: number, blue: number): void

设置画刷的颜色。性能优于[setColor](arkts-apis-graphics-drawing-brush.md#setcolor)接口，推荐使用本接口。

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
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
4. brush.setColor(255, 255, 0, 0);
```

## setColor18+

PhonePC/2in1TabletTVWearable

setColor(color: number) : void

设置画刷的颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 16进制ARGB格式的颜色。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
4. brush.setColor(0xffff0000);
```

## setColor4f20+

PhonePC/2in1TabletTVWearable

setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void

设置画刷的颜色以及标准色域，与[setColor](arkts-apis-graphics-drawing-brush.md#setcolor)区别在于可以单独设置色域，适用于需要单独设置色域的场景。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color4f | [common2D.Color4f](js-apis-graphics-common2d.md#color4f20) | 是 | ARGB格式的颜色，每个颜色通道的值是0.0-1.0之间的浮点数，大于1.0时，取1.0，小于0.0时，取0.0。 |
| colorSpace | [colorSpaceManager.ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | null | 是 | 标准色域对象，null表示使用SRGB色域。 |

**示例：**

```
1. import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

3. const brush = new drawing.Brush();
4. let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
5. let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
6. brush.setColor4f(color4f, colorSpace);
```

## getColor12+

PhonePC/2in1TabletTVWearable

getColor(): common2D.Color

获取画刷的颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color | 返回画刷的颜色。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
4. const brush = new drawing.Brush();
5. brush.setColor(color);
6. let colorGet = brush.getColor();
```

## getColor4f20+

PhonePC/2in1TabletTVWearable

getColor4f(): common2D.Color4f

获取画刷的颜色，与[getColor](arkts-apis-graphics-drawing-brush.md#getcolor12)的区别是返回值类型为浮点数，适用于需要浮点数类型的场景。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Color4f](js-apis-graphics-common2d.md#color4f20) | 返回画刷的颜色。 |

**示例：**

```
1. import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

3. const brush = new drawing.Brush();
4. let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
5. let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
6. brush.setColor4f(color4f, colorSpace);
7. let color = brush.getColor4f();
```

## getHexColor18+

PhonePC/2in1TabletTVWearable

getHexColor(): number

获取画刷的颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回画刷的颜色，以16进制ARGB格式的32位无符号整数表示。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. let color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
4. let brush = new drawing.Brush();
5. brush.setColor(color);
6. let hex_color: number = brush.getHexColor();
7. console.info('getHexColor: ', hex_color.toString(16));
```

## setAntiAlias

PhonePC/2in1TabletTVWearable

setAntiAlias(aa: boolean) : void

设置画刷是否开启抗锯齿。开启后，可以使得图形的边缘在显示时更平滑。未调用此接口设置时，系统默认关闭抗锯齿。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aa | boolean | 是 | 表示是否开启抗锯齿，true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
4. brush.setAntiAlias(true);
```

## isAntiAlias12+

PhonePC/2in1TabletTVWearable

isAntiAlias(): boolean

获取画刷是否开启抗锯齿属性。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回画刷是否开启抗锯齿属性，true表示开启，false表示关闭。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
4. let isAntiAlias = brush.isAntiAlias();
```

## setAlpha

PhonePC/2in1TabletTVWearable

setAlpha(alpha: number) : void

设置画刷的透明度。

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

3. const brush = new drawing.Brush();
4. brush.setAlpha(128);
```

## getAlpha12+

PhonePC/2in1TabletTVWearable

getAlpha(): number

获取画刷的透明度。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回画刷的透明度，该返回值为0到255之间的整数。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
4. let alpha = brush.getAlpha();
```

## setColorFilter

PhonePC/2in1TabletTVWearable

setColorFilter(filter: ColorFilter | null) : void

给画刷添加额外的颜色滤波器。

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

3. const brush = new drawing.Brush();
4. let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
5. brush.setColorFilter(colorFilter);
```

## setMaskFilter12+

PhonePC/2in1TabletTVWearable

setMaskFilter(filter: MaskFilter | null): void

给画刷添加额外的蒙版滤镜。

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
7. const brush = new drawing.Brush();
8. let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
9. brush.setMaskFilter(maskFilter);
10. }
11. }
```

## setShaderEffect12+

PhonePC/2in1TabletTVWearable

setShaderEffect(shaderEffect: ShaderEffect | null): void

设置画刷着色器效果。

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

3. const brush = new drawing.Brush();
4. let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100, y: 100}, {x: 300, y: 300}, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
5. brush.setShaderEffect(shaderEffect);
```

## setShadowLayer12+

PhonePC/2in1TabletTVWearable

setShadowLayer(shadowLayer: ShadowLayer | null): void

设置画刷阴影层效果。当前仅在绘制文字时生效。

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

10. let textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
11. let pen = new drawing.Pen();
12. pen.setStrokeWidth(2.0);

14. let pen_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
15. pen.setColor(pen_color);
16. canvas.attachPen(pen);
17. canvas.drawTextBlob(textBlob, 100, 100);
18. canvas.detachPen();

20. let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
21. let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
22. pen.setShadowLayer(shadowLayer);
23. canvas.attachPen(pen);
24. canvas.drawTextBlob(textBlob, 100, 200);
25. canvas.detachPen();

27. let brush = new drawing.Brush();
28. let brush_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
29. brush.setColor(brush_color);
30. canvas.attachBrush(brush);
31. canvas.drawTextBlob(textBlob, 300, 100);
32. canvas.detachBrush();

34. brush.setShadowLayer(shadowLayer);
35. canvas.attachBrush(brush);
36. canvas.drawTextBlob(textBlob, 300, 200);
37. canvas.detachBrush();
38. }
39. }
```

## setBlendMode

PhonePC/2in1TabletTVWearable

setBlendMode(mode: BlendMode) : void

设置画刷的混合模式。未调用此接口设置时，系统默认的混合模式为SRC\_OVER。

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

3. const brush = new drawing.Brush();
4. brush.setBlendMode(drawing.BlendMode.SRC);
```

## setImageFilter12+

PhonePC/2in1TabletTVWearable

setImageFilter(filter: ImageFilter | null): void

为画刷设置图像滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | null | 是 | 图像滤波器，null表示清空图像滤波器效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let brush = new drawing.Brush();
4. let imgFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.DECAL);
5. brush.setImageFilter(imgFilter);
6. brush.setImageFilter(null);
```

## getColorFilter12+

PhonePC/2in1TabletTVWearable

getColorFilter(): ColorFilter

获取画刷的颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let brush = new drawing.Brush();
4. let setColorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
5. brush.setColorFilter(setColorFilter);
6. let filter = brush.getColorFilter();
```

## reset12+

PhonePC/2in1TabletTVWearable

reset(): void

重置当前画刷为初始状态。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. const brush = new drawing.Brush();
4. brush.reset();
```
