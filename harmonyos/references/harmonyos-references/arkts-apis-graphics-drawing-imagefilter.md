---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-imagefilter
title: Class (ImageFilter)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (ImageFilter)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bd055093336d05b95c58fab88c315fac1938d5f6dd5a08eba82a811ef511a497
---

图像滤波器。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## createBlurImageFilter12+

PhonePC/2in1TabletTVWearable

static createBlurImageFilter(sigmaX: number, sigmaY: number, tileMode: TileMode, imageFilter?: ImageFilter | null ): ImageFilter

创建具有模糊效果的图像滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sigmaX | number | 是 | 表示沿x轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。 |
| sigmaY | number | 是 | 表示沿y轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。 |
| tileMode | [TileMode](arkts-apis-graphics-drawing-e.md#tilemode12) | 是 | 表示在边缘处应用的平铺模式。 |
| imageFilter | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | null | 否 | 要与当前图像滤波器叠加的输入滤波器，默认为null，表示直接将当前图像滤波器作用于原始图像。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 返回创建的图像滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let imgFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.CLAMP);
```

## createFromImage20+

PhonePC/2in1TabletTVWearable

static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter

基于给定的图像创建一个图像滤波器。此接口不建议用于录制类型的画布，会影响性能。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片对象。 |
| srcRect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | null | 否 | 可选参数，默认为空。图片要被此滤波器使用的像素区域，如果为空，则使用pixelmap全部区域。 |
| dstRect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | null | 否 | 可选参数，默认为空。要进行渲染的区域，如果为空，则和srcRect保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 返回创建的图像滤波器。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { common2D, drawing } from '@kit.ArkGraphics2D';

5. class DrawingRenderNode extends RenderNode {
6. draw(context: DrawContext) {
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

20. let opts: image.InitializationOptions = {
21. editable: true,
22. pixelFormat: 3,
23. size: { height, width }
24. }

26. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
27. let srcRect: common2D.Rect = {
28. left: 10,
29. top: 10,
30. right: 80,
31. bottom: 80
32. };
33. let dstRect: common2D.Rect = {
34. left: 200,
35. top: 200,
36. right: 400,
37. bottom: 400
38. };
39. if (pixelMap != null) {
40. let filter = drawing.ImageFilter.createFromImage(pixelMap, srcRect, dstRect);
41. }
42. }
43. }
```

## createBlendImageFilter20+

PhonePC/2in1TabletTVWearable

static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter

按照指定的混合模式对两个滤波器进行叠加，生成一个新的滤波器。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 颜色混合模式。 |
| background | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 是 | 在混合模式中作为目标色的滤波器。 |
| foreground | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 是 | 在混合模式中作为源色的滤波器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 返回创建的图像滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error.Possible causes: Incorrect parameter range. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let dx = 15.0;
4. let dy = 10.0;
5. let offsetFilter1 = drawing.ImageFilter.createOffsetImageFilter(dx, dy, null);
6. let x = 15.0;
7. let y = 30.0;
8. let offsetFilter2 = drawing.ImageFilter.createOffsetImageFilter(x, y, null);
9. let blendImageFilter = drawing.ImageFilter.createBlendImageFilter(drawing.BlendMode.SRC_IN, offsetFilter1, offsetFilter2);
```

## createComposeImageFilter20+

PhonePC/2in1TabletTVWearable

static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter

将两个图像滤波器进行级联生成新的图像滤波器，级联时会将第一级滤波器的输出作为第二级滤波器的输入，经过第二级滤波器处理后，输出最终的滤波结果。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cOuter | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 是 | 在级联中，作为第二级的滤波器，处理第一级滤波器的输出。如果第二级滤波器为空，第一级滤波器不为空，最后输出第一级滤波器的结果。两级滤波器不能同时为空。 |
| cInner | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 是 | 在级联中，作为第一级的滤波器，直接处理图像的原始内容。如果第一级滤波器为空，第二级滤波器不为空，最后输出第二级滤波器的结果。两级滤波器不能同时为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 返回创建的图像滤波器。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let blurSigmaX = 10.0;
4. let blurSigmaY = 10.0;
5. let blurFilter = drawing.ImageFilter.createBlurImageFilter(blurSigmaX, blurSigmaY, drawing.TileMode.CLAMP, null);
6. let colorMatrix:Array<number> = [
7. 0, 0, 0, 0, 0,
8. 0, 1, 0, 0, 0,
9. 0, 0, 1, 0, 0,
10. 0, 0, 0, 1, 0
11. ];
12. let redRemovalFilter = drawing.ColorFilter.createMatrixColorFilter(colorMatrix);
13. let colorFilter = drawing.ImageFilter.createFromColorFilter(redRemovalFilter, null);
14. let composedImageFilter = drawing.ImageFilter.createComposeImageFilter(colorFilter, blurFilter);
```

## createFromColorFilter12+

PhonePC/2in1TabletTVWearable

static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter

创建一个将颜色滤波器应用于传入的图像滤波器的图像滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorFilter | [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 是 | 表示颜色滤波器。 |
| imageFilter | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | null | 否 | 要与当前图像滤波器叠加的输入滤波器，默认为null，表示直接将当前图像滤波器作用于原始图像。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 返回创建的图像滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let imgFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.CLAMP);
4. let colorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
5. let imgFilter1 = drawing.ImageFilter.createFromColorFilter(colorFilter, imgFilter);
```

## createOffsetImageFilter20+

PhonePC/2in1TabletTVWearable

static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter

创建一个偏移滤波器，将输入的滤波器按照指定向量进行平移。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | number | 是 | 水平方向的平移距离， 该参数为浮点数。 |
| dy | number | 是 | 竖直方向的平移距离， 该参数为浮点数。 |
| input | [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | null | 否 | 需进行平移的滤波器。默认为空，如果为空，则将无滤波效果的绘制结果进行平移。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 返回创建的图像滤波器。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let dx = 15.0;
4. let dy = 10.0;
5. let offsetFilter = drawing.ImageFilter.createOffsetImageFilter(dx, dy, null);
```

## createFromShaderEffect20+

PhonePC/2in1TabletTVWearable

static createFromShaderEffect(shader: ShaderEffect): ImageFilter

基于着色器创建一个图像滤波器。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shader | [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 是 | 表示应用于图像的着色器效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageFilter](arkts-apis-graphics-drawing-imagefilter.md) | 返回创建的图像滤波器。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let shaderEffect = drawing.ShaderEffect.createColorShader(0xFF00FF00);
4. let renderEffect = drawing.ImageFilter.createFromShaderEffect(shaderEffect);
```
