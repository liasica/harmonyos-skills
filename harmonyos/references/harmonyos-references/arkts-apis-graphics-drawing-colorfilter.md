---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-colorfilter
title: Class (ColorFilter)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (ColorFilter)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4f86bb2f7db925d15faff23fcb458499b5bcc3140ada9be7b3de50152fad2ef8
---

颜色滤波器。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## createBlendModeColorFilter

PhonePC/2in1TabletTVWearable

createBlendModeColorFilter(color: common2D.Color, mode: BlendMode) : ColorFilter

创建指定的颜色和混合模式的颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | ARGB格式的颜色，每个颜色通道的值是0到255之间的整数。 |
| mode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 颜色的混合模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
4. let colorFilter = drawing.ColorFilter.createBlendModeColorFilter(color, drawing.BlendMode.SRC);
```

## createBlendModeColorFilter18+

PhonePC/2in1TabletTVWearable

static createBlendModeColorFilter(color: common2D.Color | number, mode: BlendMode) : ColorFilter

使用指定的颜色和混合模式创建颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | number | 是 | 颜色，可以用16进制ARGB格式的无符号整数表示。 |
| mode | [BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 颜色的混合模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let colorFilter = drawing.ColorFilter.createBlendModeColorFilter(0xffff0000, drawing.BlendMode.SRC);
```

## createComposeColorFilter

PhonePC/2in1TabletTVWearable

createComposeColorFilter(outer: ColorFilter, inner: ColorFilter) : ColorFilter

创建一个先应用inner进行滤波，再应用outer进行滤波的组合颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outer | [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 是 | 组合滤波器中后生效的颜色滤波器。 |
| inner | [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 是 | 组合滤波器中先生效的颜色滤波器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
4. let colorFilter1 = drawing.ColorFilter.createBlendModeColorFilter(color, drawing.BlendMode.SRC);
5. let colorFilter2 = drawing.ColorFilter.createBlendModeColorFilter(color, drawing.BlendMode.DST);
6. let colorFilter = drawing.ColorFilter.createComposeColorFilter(colorFilter1, colorFilter2);
```

## createLinearToSRGBGamma

PhonePC/2in1TabletTVWearable

createLinearToSRGBGamma() : ColorFilter

创建一个从线性颜色空间转换到SRGB颜色空间的颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
```

## createSRGBGammaToLinear

PhonePC/2in1TabletTVWearable

createSRGBGammaToLinear() : ColorFilter

创建一个从SRGB颜色空间转换到线性颜色空间的颜色滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let colorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
```

## createLumaColorFilter

PhonePC/2in1TabletTVWearable

createLumaColorFilter() : ColorFilter

创建一个颜色滤波器将其输入的亮度值乘以透明度通道，并将红色、绿色和蓝色通道设置为零。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let colorFilter = drawing.ColorFilter.createLumaColorFilter();
```

## createMatrixColorFilter12+

PhonePC/2in1TabletTVWearable

static createMatrixColorFilter(matrix: Array<number>): ColorFilter

创建颜色滤波器，通过4x5颜色矩阵变换颜色。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | Array<number> | 是 | 长度为20的数组，表示用于颜色变换的4\*5矩阵。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回颜色滤波器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix: Array<number> = [
4. 1, 0, 0, 0, 0,
5. 0, 1, 0, 0, 0,
6. 0, 0, 100, 0, 0,
7. 0, 0, 0, 1, 0
8. ];
9. let colorFilter = drawing.ColorFilter.createMatrixColorFilter(matrix);
```

## createLightingColorFilter20+

PhonePC/2in1TabletTVWearable

static createLightingColorFilter(mutColor: common2D.Color | number, addColor: common2D.Color | number): ColorFilter

创建一个光照颜色滤波器，此滤波器会将RGB通道的颜色值乘以一种颜色值并加上另一种颜色值，计算结果会被限制在0到255范围内。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mutColor | [common2D.Color](js-apis-graphics-common2d.md#color) | number | 是 | 用来进行乘法运算的颜色，ARGB格式的颜色，每个颜色通道是0到255之间的整数。为number类型时必须是16进制ARGB格式的无符号整数。 |
| addColor | [common2D.Color](js-apis-graphics-common2d.md#color) | number | 是 | 用来进行加法运算的颜色，ARGB格式的颜色，每个颜色通道是0到255之间的整数。为number类型时必须是16进制ARGB格式的无符号整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回一个颜色滤波器。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';
2. let mulColor : common2D.Color = { alpha: 0, red: 0, green: 0, blue: 20 };
3. let addColor : common2D.Color = { alpha: 0, red: 0, green: 0, blue: 125 };
4. let colorFilter = drawing.ColorFilter.createLightingColorFilter(mulColor, addColor);
```
