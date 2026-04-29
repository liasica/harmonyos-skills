---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadereffect
title: Class (ShaderEffect)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (ShaderEffect)
category: harmonyos-references
scraped_at: 2026-04-29T14:05:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aedecac155b7c5cf44503191331dde2748fdd614553448642cec224c114bc7d0
---

着色器。画刷和画笔设置着色器后，会使用着色器效果而不是颜色属性去绘制，但此时画笔和画刷的透明度属性仍然生效。

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

## createComposeShader20+

PhonePC/2in1TabletTVWearable

static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect, blendMode: BlendMode): ShaderEffect

按照指定的混合模式对两个着色器进行叠加，生成一个新的着色器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dstShaderEffect | [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 是 | 在混合模式中作为目标色的着色器。 |
| srcShaderEffect | [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 是 | 在混合模式中作为源色的着色器。 |
| blendMode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 混合模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 返回创建的着色器对象。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error.Possible causes: Incorrect parameter range. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let dstShader = drawing.ShaderEffect.createColorShader(0xFF0000FF);
4. let srcShader = drawing.ShaderEffect.createColorShader(0xFFFF0000);
5. let shader = drawing.ShaderEffect.createComposeShader(dstShader, srcShader, drawing.BlendMode.SRC);
```

## createImageShader20+

PhonePC/2in1TabletTVWearable

static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode, samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect

基于图片创建一个着色器。此接口不建议用于录制类型的画布，会影响性能。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 进行采样的图片对象。 |
| tileX | [TileMode](arkts-apis-graphics-drawing-e.md#tilemode12) | 是 | 水平方向的平铺模式。 |
| tileY | [TileMode](arkts-apis-graphics-drawing-e.md#tilemode12) | 是 | 竖直方向的平铺模式。 |
| samplingOptions | [SamplingOptions](arkts-apis-graphics-drawing-samplingoptions.md) | 是 | 图片采样参数。 |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | null | 否 | 可选参数，对图片施加的矩阵变换，如果为空，则不施加任何变换。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 返回创建的着色器对象。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error.Possible causes: Incorrect parameter range. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { drawing } from '@kit.ArkGraphics2D';

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
27. let matrix = new drawing.Matrix();
28. let options = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
29. if (pixelMap != null) {
30. let imageShader =
31. drawing.ShaderEffect.createImageShader(pixelMap, drawing.TileMode.REPEAT, drawing.TileMode.MIRROR, options,
32. matrix);
33. }
34. }
35. }
```

## createColorShader12+

PhonePC/2in1TabletTVWearable

static createColorShader(color: number): ShaderEffect

创建具有单一颜色的着色器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 表示着色器的ARGB格式颜色，该参数为32位无符号整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 返回具有单一颜色的着色器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let shaderEffect = drawing.ShaderEffect.createColorShader(0xFFFF0000);
```

## createLinearGradient12+

PhonePC/2in1TabletTVWearable

static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect

创建着色器，在两个指定点之间生成线性渐变。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startPt | [common2D.Point](js-apis-graphics-common2d.md#point12) | 是 | 表示渐变的起点。 |
| endPt | [common2D.Point](js-apis-graphics-common2d.md#point12) | 是 | 表示渐变的终点。 |
| colors | Array<number> | 是 | 表示在两个点之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-apis-graphics-drawing-e.md#tilemode12) | 是 | 着色器效果平铺模式。 |
| pos | Array<number> |null | 否 | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在起点和终点之间。 |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | null | 否 | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/bGKCg1c-ROSssLnLs4FLpw/zh-cn_image_0000002589247199.png?HW-CC-KV=V1&HW-CC-Date=20260429T060517Z&HW-CC-Expire=86400&HW-CC-Sign=614216EE868D740F485337631AB87AAB4AD95793613DFE9F58631C15DD4B8125)

如上图所示，设置颜色数组为红绿蓝，位置数组为0.0、0.75和1.0后的显示效果。三角下标表示对应颜色的起始点和终点之间的相对位置，颜色之间使用渐变填充。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 返回创建的着色器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { common2D,drawing } from '@kit.ArkGraphics2D';

3. let startPt: common2D.Point = { x: 100, y: 100 };
4. let endPt: common2D.Point = { x: 300, y: 300 };
5. let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
```

## createRadialGradient12+

PhonePC/2in1TabletTVWearable

static createRadialGradient(centerPt: common2D.Point, radius: number, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect

创建着色器，使用给定的圆心和半径生成径向渐变。径向渐变是指颜色从圆心逐渐向外扩散形成的渐变。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| centerPt | [common2D.Point](js-apis-graphics-common2d.md#point12) | 是 | 表示渐变的圆心。 |
| radius | number | 是 | 表示渐变的半径，小于等于0时无效，该参数为浮点数。 |
| colors | Array<number> | 是 | 表示在圆心和圆边界之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-apis-graphics-drawing-e.md#tilemode12) | 是 | 着色器效果平铺模式。 |
| pos | Array<number> | null | 否 | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在圆心和圆边界之间。 |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | null | 否 | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/cE4PvmlcTUqrzTSt1VUESg/zh-cn_image_0000002558767392.png?HW-CC-KV=V1&HW-CC-Date=20260429T060517Z&HW-CC-Expire=86400&HW-CC-Sign=334A4AA85CF3E3707B7AACD0485E0C89F84ED2F3584F5307650CA118089F4FC8)

如上图所示，设置颜色数组为红绿蓝，位置数组为0.0、0.75和1.0后的显示效果。三角下标表示对应颜色所在圆心和圆边界之间的相对位置，颜色之间使用渐变填充。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 返回创建的着色器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { common2D,drawing } from '@kit.ArkGraphics2D';

3. let centerPt: common2D.Point = { x: 100, y: 100 };
4. let shaderEffect = drawing.ShaderEffect.createRadialGradient(centerPt, 100, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
```

## createSweepGradient12+

PhonePC/2in1TabletTVWearable

static createSweepGradient(centerPt: common2D.Point, colors: Array<number>, mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect

创建着色器。该着色器以给定中心点为圆心，在顺时针或逆时针方向上生成颜色扫描渐变。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| centerPt | [common2D.Point](js-apis-graphics-common2d.md#point12) | 是 | 表示渐变的圆心。 |
| colors | Array<number> | 是 | 表示在起始角度和结束角度之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-apis-graphics-drawing-e.md#tilemode12) | 是 | 着色器效果平铺模式。 |
| startAngle | number | 是 | 表示扇形渐变的起始角度，单位为度。0度时为x轴正方向，正数往顺时针方向偏移，负数往逆时针方向偏移。该参数为浮点数。 |
| endAngle | number | 是 | 表示扇形渐变的结束角度，单位为度。0度时为x轴正方向，正数往顺时针方向偏移，负数往逆时针方向偏移。小于起始角度时无效。该参数为浮点数。 |
| pos | Array<number> | null | 否 | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在起始角度和结束角度之间。 |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | null | 否 | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/eoVsnpNrShq2CxI-jqOM7A/zh-cn_image_0000002558607734.png?HW-CC-KV=V1&HW-CC-Date=20260429T060517Z&HW-CC-Expire=86400&HW-CC-Sign=46EB34C997A6C22E7704F3079EA552A7EE193F0FE9F1C5168827D1C4204E666D)

如上图所示，设置颜色数组为红绿蓝，位置数组为0.0、0.75和1.0，起始角度设置为0度，结束角度设置为180度后的显示效果。0.0对应0度的位置，0.75对应135度的位置，1.0对应180度的位置，颜色之间使用渐变填充。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 返回创建的着色器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { common2D,drawing } from '@kit.ArkGraphics2D';

3. let centerPt: common2D.Point = { x: 100, y: 100 };
4. let shaderEffect = drawing.ShaderEffect.createSweepGradient(centerPt, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT, 100, 200);
```

## createConicalGradient12+

PhonePC/2in1TabletTVWearable

static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point, endRadius: number, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect

创建着色器，在给定两个圆之间生成径向渐变。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startPt | [common2D.Point](js-apis-graphics-common2d.md#point12) | 是 | 表示渐变的起始圆的圆心。 |
| startRadius | number | 是 | 表示渐变的起始圆的半径，小于0时无效。该参数为浮点数。 |
| endPt | [common2D.Point](js-apis-graphics-common2d.md#point12) | 是 | 表示渐变的结束圆的圆心。 |
| endRadius | number | 是 | 表示渐变的结束圆的半径，小于0时无效。该参数为浮点数。 |
| colors | Array<number> | 是 | 表示在起始圆和结束圆之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-apis-graphics-drawing-e.md#tilemode12) | 是 | 着色器效果平铺模式。 |
| pos | Array<number> | null | 否 | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在起始圆和结束圆之间。 |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | null | 否 | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Vd7gp6tbR-OK4QCxXYqjXQ/zh-cn_image_0000002589327261.png?HW-CC-KV=V1&HW-CC-Date=20260429T060517Z&HW-CC-Expire=86400&HW-CC-Sign=5ED15FEECFF6E860A3DAB4EA7C3CC1E9E1C9EB321018A7978CCB7725717D9BF3)

如上图所示，设置颜色数组为红绿蓝，位置数组为0.0、0.5和1.0的绘制结果。左侧为起始圆不在结束圆内的绘制结果，右侧为起始圆在结束圆内的绘制结果。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShaderEffect](arkts-apis-graphics-drawing-shadereffect.md) | 返回创建的着色器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { common2D,drawing } from '@kit.ArkGraphics2D';

3. let startPt: common2D.Point = { x: 100, y: 100 };
4. let endPt: common2D.Point = {x: 200, y: 200};
5. let shaderEffect = drawing.ShaderEffect.createConicalGradient(startPt, 100, endPt, 50, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
```
