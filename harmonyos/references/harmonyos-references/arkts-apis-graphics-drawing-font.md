---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-font
title: Class (Font)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Font)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3cf2e9c7d520513feb6f51eed65031272837cf784b074108bf4cff7d95b4f7b8
---

描述字型绘制时所使用的属性，如大小、字体等。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## isSubpixel12+

PhonePC/2in1TabletTVWearable

isSubpixel(): boolean

获取字型是否使用次像素渲染。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回字型是否使用次像素渲染的结果，true表示使用，false表示不使用。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. font.enableSubpixel(true)
5. console.info("values=" + font.isSubpixel());
```

## isLinearMetrics12+

PhonePC/2in1TabletTVWearable

isLinearMetrics(): boolean

获取字型是否可以线性缩放。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回字型是否可线性缩放的结果，true表示可线性缩放，false表示不可线性缩放。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. font.enableLinearMetrics(true)
5. console.info("values=" + font.isLinearMetrics());
```

## getSkewX12+

PhonePC/2in1TabletTVWearable

getSkewX(): number

获取字型在x轴方向上的倾斜度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回字型在x轴方向上的倾斜度。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. font.setSkewX(-1)
5. console.info("values=" + font.getSkewX());
```

## isEmbolden12+

PhonePC/2in1TabletTVWearable

isEmbolden(): boolean

获取字型是否设置了粗体效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回字型是否设置粗体效果的结果，true表示设置了粗体效果，false表示未设置粗体效果。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. font.enableEmbolden(true);
5. console.info("values=" + font.isEmbolden());
```

## getScaleX12+

PhonePC/2in1TabletTVWearable

getScaleX(): number

获取字型在x轴方向上的缩放比例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回字型在x轴方向上的缩放比例。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. font.setScaleX(2);
5. console.info("values=" + font.getScaleX());
```

## getHinting12+

PhonePC/2in1TabletTVWearable

getHinting(): FontHinting

获取字型轮廓效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FontHinting](arkts-apis-graphics-drawing-e.md#fonthinting12) | 返回字型轮廓效果。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. console.info("values=" + font.getHinting());
```

## getEdging12+

PhonePC/2in1TabletTVWearable

getEdging(): FontEdging

获取字型边缘效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FontEdging](arkts-apis-graphics-drawing-e.md#fontedging12) | 返回字型边缘效果。 |

**示例：**

```
1. import {drawing} from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. console.info("values=" + font.getEdging());
```

## enableSubpixel

PhonePC/2in1TabletTVWearable

enableSubpixel(isSubpixel: boolean): void

使能字型亚像素级别的文字绘制，显示效果平滑。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSubpixel | boolean | 是 | 表示是否使能字型亚像素级别的文字绘制。true表示使能，false表示不使能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.enableSubpixel(true);
```

## enableEmbolden

PhonePC/2in1TabletTVWearable

enableEmbolden(isEmbolden: boolean): void

使能字型粗体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEmbolden | boolean | 是 | 表示是否使能字型粗体。true表示使能，false表示不使能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.enableEmbolden(true);
```

## enableLinearMetrics

PhonePC/2in1TabletTVWearable

enableLinearMetrics(isLinearMetrics: boolean): void

使能字型的线性缩放。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLinearMetrics | boolean | 是 | 表示是否使能字型的线性缩放。true表示使能，false表示不使能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.enableLinearMetrics(true);
```

## setSize

PhonePC/2in1TabletTVWearable

setSize(textSize: number): void

设置字型大小。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textSize | number | 是 | 字型大小，该参数为浮点数，为负数时字型大小会被置为0。字型大小为0时，绘制的文字不会显示。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.setSize(5);
```

## getSize

PhonePC/2in1TabletTVWearable

getSize(): number

获取字型大小。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 字型大小，浮点数。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.setSize(5);
5. let fontSize = font.getSize();
```

## setTypeface

PhonePC/2in1TabletTVWearable

setTypeface(typeface: Typeface): void

为字型设置字体样式（包括字体名称、粗细、斜体等属性）。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typeface | [Typeface](arkts-apis-graphics-drawing-typeface.md) | 是 | 字体样式，包括字体名称、粗细、斜体等属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.setTypeface(new drawing.Typeface());
```

## getTypeface

PhonePC/2in1TabletTVWearable

getTypeface(): Typeface

获取字体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Typeface](arkts-apis-graphics-drawing-typeface.md) | 字体。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. let typeface = font.getTypeface();
```

## getMetrics

PhonePC/2in1TabletTVWearable

getMetrics(): FontMetrics

获取与字体关联的FontMetrics属性。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FontMetrics](arkts-apis-graphics-drawing-i.md#fontmetrics) | FontMetrics属性。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. let metrics = font.getMetrics();
```

## measureText

PhonePC/2in1TabletTVWearable

measureText(text: string, encoding: TextEncoding): number

测量文本的宽度。

说明

此接口用于测量原始字符串的文本宽度，若想测量排版后的文本宽度，建议使用[measure.measureText](arkts-apis-uicontext-measureutils.md#measuretext12)替代。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |
| encoding | [TextEncoding](arkts-apis-graphics-drawing-e.md#textencoding) | 是 | 编码格式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文本的宽度，浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.measureText("drawing", drawing.TextEncoding.TEXT_ENCODING_UTF8);
```

## measureSingleCharacter12+

PhonePC/2in1TabletTVWearable

measureSingleCharacter(text: string): number

测量单个字符的宽度。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待测量的单个字符，字符串的长度必须为1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 字符的宽度，浮点数。 |

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
7. const font = new drawing.Font();
8. font.setSize(20);
9. let width = font.measureSingleCharacter("你");
10. }
11. }
```

## measureSingleCharacterWithFeatures20+

PhonePC/2in1TabletTVWearable

measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): number

测量单个字符的宽度，字符带有字体特征。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待测量的单个字符。字符串长度必须为1。 |
| features | Array<[FontFeature](arkts-apis-graphics-drawing-i.md#fontfeature20)> | 是 | 字体特征对象数组。参数为空数组时使用TTF(TrueType Font)文件中预设的字体特征。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 字符的宽度，浮点数，单位为px。 |

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
6. const font = new drawing.Font();
7. font.setSize(20);
8. let fontFeatures : Array<drawing.FontFeature> = [];
9. fontFeatures.push({name: 'calt', value: 0});
10. let width = font.measureSingleCharacterWithFeatures("你", fontFeatures);
11. }
12. }
```

## setScaleX12+

PhonePC/2in1TabletTVWearable

setScaleX(scaleX: number): void

设置字型对象在x轴上的缩放比例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 文本在x轴上的缩放比例，该参数为浮点数。 |

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
11. let font = new drawing.Font();
12. font.setSize(100);
13. font.setScaleX(2);
14. const textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
15. canvas.drawTextBlob(textBlob, 200, 200);
16. }
17. }
```

## setSkewX12+

PhonePC/2in1TabletTVWearable

setSkewX(skewX: number): void

设置字型对象在x轴上的倾斜比例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| skewX | number | 是 | 文本在x轴上的倾斜比例，正数表示往左边倾斜，负数表示往右边倾斜，该参数为浮点数。 |

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
11. let font = new drawing.Font();
12. font.setSize(100);
13. font.setSkewX(1);
14. const textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
15. canvas.drawTextBlob(textBlob, 200, 200);
16. }
17. }
```

## setEdging12+

PhonePC/2in1TabletTVWearable

setEdging(edging: FontEdging): void

设置字型边缘效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edging | [FontEdging](arkts-apis-graphics-drawing-e.md#fontedging12) | 是 | 字型边缘效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.setEdging(drawing.FontEdging.SUBPIXEL_ANTI_ALIAS);
```

## setHinting12+

PhonePC/2in1TabletTVWearable

setHinting(hinting: FontHinting): void

设置字型轮廓效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hinting | [FontHinting](arkts-apis-graphics-drawing-e.md#fonthinting12) | 是 | 字型轮廓效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. font.setHinting(drawing.FontHinting.FULL);
```

## countText12+

PhonePC/2in1TabletTVWearable

countText(text: string): number

获取文本所表示的字符数量。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回文本所表示的字符数量，整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font = new drawing.Font();
4. let resultNumber: number = font.countText('ABCDE');
5. console.info("count text number: " + resultNumber);
```

## setBaselineSnap12+

PhonePC/2in1TabletTVWearable

setBaselineSnap(isBaselineSnap: boolean): void

当前画布矩阵轴对齐时，设置字型基线是否与像素对齐。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isBaselineSnap | boolean | 是 | 指示字型基线是否和像素对齐，true表示对齐，false表示不对齐。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setBaselineSnap(true);
5. console.info("drawing font isBaselineSnap: " + font.isBaselineSnap());
```

## isBaselineSnap()12+

PhonePC/2in1TabletTVWearable

isBaselineSnap(): boolean

当前画布矩阵轴对齐时，获取字型基线是否与像素对齐的结果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回字型基线是否与像素对齐，true为对齐，false为没有对齐。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setTypeface(new drawing.Typeface());
5. font.setBaselineSnap(true);
6. console.info("drawing font isBaselineSnap: " + font.isBaselineSnap());
```

## setEmbeddedBitmaps12+

PhonePC/2in1TabletTVWearable

setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void

设置字型是否转换成位图处理。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEmbeddedBitmaps | boolean | 是 | 设置字型是否转换成位图处理，true表示转换成位图处理，false表示不转换成位图处理。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setTypeface(new drawing.Typeface());
5. font.setEmbeddedBitmaps(false);
6. console.info("draw isEmbeddedBitmaps: " + font.isEmbeddedBitmaps());
```

## isEmbeddedBitmaps()12+

PhonePC/2in1TabletTVWearable

isEmbeddedBitmaps(): boolean

获取字型是否转换成位图处理的结果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回字型是否转换成位图处理结果，true表示转换成位图处理，false表示不转换成位图处理。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setTypeface(new drawing.Typeface());
5. font.setEmbeddedBitmaps(true);
6. console.info("draw isEmbeddedBitmaps: " + font.isEmbeddedBitmaps());
```

## setForceAutoHinting12+

PhonePC/2in1TabletTVWearable

setForceAutoHinting(isForceAutoHinting: boolean): void

设置是否自动调整字型轮廓。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isForceAutoHinting | boolean | 是 | 是否自动调整字型轮廓，true为自动调整，false为不自动调整。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setTypeface(new drawing.Typeface());
5. font.setForceAutoHinting(false);
6. console.info("drawing isForceAutoHinting:  " + font.isForceAutoHinting());
```

## isForceAutoHinting12+

PhonePC/2in1TabletTVWearable

isForceAutoHinting(): boolean

获取字型轮廓是否自动调整的结果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回字型轮廓是否自动调整，true为自动调整，false为不自动调整。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setTypeface(new drawing.Typeface());
5. font.setForceAutoHinting(false);
6. console.info("drawing isForceAutoHinting:  " + font.isForceAutoHinting());
```

## getWidths12+

PhonePC/2in1TabletTVWearable

getWidths(glyphs: Array<number>): Array<number>

获取字形数组中每个字形对应的宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| glyphs | Array<number> | 是 | 字形索引数组，可由[textToGlyphs](arkts-apis-graphics-drawing-font.md#texttoglyphs12)生成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回字形宽度数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. let text: string = 'hello world';
5. let glyphs: number[] = font.textToGlyphs(text);
6. let fontWidths: Array<number> = font.getWidths(glyphs);
7. for (let index = 0; index < fontWidths.length; index++) {
8. console.info("get fontWidths[", index, "]:", fontWidths[index]);
9. }
```

## textToGlyphs12+

PhonePC/2in1TabletTVWearable

textToGlyphs(text: string, glyphCount?: number): Array<number>

将文本转换为字形索引。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本字符串。 |
| glyphCount | number | 否 | 文本表示的字符数量，必须与[countText](arkts-apis-graphics-drawing-font.md#counttext12)获取的值相等，默认为text的字符数量，该参数为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回转换得到的字形索引数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. let text : string = 'hello world';
5. let glyphs : number[] = font.textToGlyphs(text);
6. console.info("drawing text toglyphs OnTestFunction num =  " + glyphs.length );
```

## getBounds18+

PhonePC/2in1TabletTVWearable

getBounds(glyphs: Array<number>): Array<common2D.Rect>

获取字形数组中每个字形的边界矩形。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| glyphs | Array<number> | 是 | 字形索引数组，可由[textToGlyphs](arkts-apis-graphics-drawing-font.md#texttoglyphs12)生成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common2D.Rect](js-apis-graphics-common2d.md#rect)> | 返回字形边界矩形数组。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. let font: drawing.Font = new drawing.Font();
4. let text: string = 'hello world';
5. let glyphs: number[] = font.textToGlyphs(text);
6. let fontBounds: Array<common2D.Rect> = font.getBounds(glyphs);
7. for (let index = 0; index < fontBounds.length; index++) {
8. console.info("get fontWidths[", index, "] left:", fontBounds[index].left, " top:", fontBounds[index].top,
9. " right:", fontBounds[index].right, " bottom:", fontBounds[index].bottom);
10. }
```

## getTextPath18+

PhonePC/2in1TabletTVWearable

getTextPath(text: string, byteLength: number, x: number, y: number): Path

获取文字的轮廓路径。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 表示存储UTF-8 文本编码的字符。 |
| byteLength | number | 是 | 表示要获取对应文本路径的字节长度，按传入的字节长度和实际的文本字节大小之间的最小值来获取对应的文本路径。 |
| x | number | 是 | 表示文本在绘图区域内以原点为起始位置的X坐标。 |
| y | number | 是 | 表示文本在绘图区域内以原点为起始位置的Y坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Path](arkts-apis-graphics-drawing-path.md) | 返回获取到的文本的路径轮廓。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. import { buffer } from '@kit.ArkTS';
3. import { RenderNode } from '@kit.ArkUI';

5. class DrawingRenderNode extends RenderNode {
6. draw(context : DrawContext) {
7. const canvas = context.canvas;
8. let font = new drawing.Font();
9. font.setSize(50);
10. let myString: string = "Hello";
11. let length: number = buffer.from(myString).length;
12. let path = font.getTextPath(myString, length, 0, 100);
13. canvas.drawPath(path);
14. }
15. }
```

## createPathForGlyph18+

PhonePC/2in1TabletTVWearable

createPathForGlyph(index: number): Path

获取指定字形的路径轮廓。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 字形索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Path](arkts-apis-graphics-drawing-path.md) | 返回指定字形的路径轮廓。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let font = new drawing.Font();
8. font.setSize(50)
9. let text: string = '你好';
10. let glyphs: number[] = font.textToGlyphs(text);
11. for (let index = 0; index < glyphs.length; index++) {
12. let path: drawing.Path = font.createPathForGlyph(glyphs[index])
13. canvas.drawPath(path)
14. }
15. }
16. }
```

## setThemeFontFollowed15+

PhonePC/2in1TabletTVWearable

setThemeFontFollowed(followed: boolean): void

设置字型中的字体是否跟随主题字体。设置跟随主题字体后，若系统启用主题字体并且字型未被设置字体，字型会使用该主题字体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| followed | boolean | 是 | 字型中的字体是否跟随主题字体，true表示跟随主题字体，false表示不跟随主题字体。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setThemeFontFollowed(true);
5. console.info("font is theme font followed: " + font.isThemeFontFollowed());
```

## isThemeFontFollowed()15+

PhonePC/2in1TabletTVWearable

isThemeFontFollowed(): boolean

获取字型中的字体是否跟随主题字体。默认不跟随。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回字型中的字体是否跟随主题字体的结果，true表示跟随主题字体，false表示不跟随主题字体。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let font : drawing.Font = new drawing.Font();
4. font.setThemeFontFollowed(true);
5. console.info("font is theme font followed: " + font.isThemeFontFollowed());
```
