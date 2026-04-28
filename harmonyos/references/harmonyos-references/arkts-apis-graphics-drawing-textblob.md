---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-textblob
title: Class (TextBlob)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (TextBlob)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf4ab1fc9edb69f699a14866e9d5b4d8eff3332e3d7acdba2e2b970328d59abc
---

由一个或多个具有相同字体的字符组成的字块。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## makeFromPosText12+

PhonePC/2in1TabletTVWearable

static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob

使用文本创建TextBlob对象，TextBlob对象中每个字形的坐标由points中对应的坐标信息决定。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 绘制字形的文本内容。 |
| len | number | 是 | 字形个数，由[countText](arkts-apis-graphics-drawing-font.md#counttext12)获取，该参数为整数。 |
| points | [common2D.Point](js-apis-graphics-common2d.md#point12)[] | 是 | 点数组，用于指定每个字形的坐标，长度必须为len。 |
| font | [Font](arkts-apis-graphics-drawing-font.md) | 是 | 字型对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-apis-graphics-drawing-textblob.md) | TextBlob对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing,common2D} from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let text : string = 'makeFromPosText';
8. let font : drawing.Font = new drawing.Font();
9. font.setSize(100);
10. let length = font.countText(text);
11. let points : common2D.Point[] = [];
12. for (let i = 0; i !== length; ++i) {
13. points.push({ x: i * 35, y: i * 35 });
14. }
15. let textblob : drawing.TextBlob =drawing.TextBlob.makeFromPosText(text, points.length, points, font);
16. canvas.drawTextBlob(textblob, 100, 100);
17. }
18. }
```

## uniqueID12+

PhonePC/2in1TabletTVWearable

uniqueID(): number

获取该TextBlob对象的唯一的非零标识符。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回TextBlob对象的唯一的非零标识符。 |

**示例：**

```
1. import {drawing} from "@kit.ArkGraphics2D";

3. let text : string = 'TextBlobUniqueId';
4. let font : drawing.Font = new drawing.Font();
5. font.setSize(100);
6. let textBlob = drawing.TextBlob.makeFromString(text, font, 0);
7. let id = textBlob.uniqueID();
8. console.info("uniqueID---------------" +id);
```

## makeFromString

PhonePC/2in1TabletTVWearable

static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob

将string类型的值转化成TextBlob对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 绘制字形的文本内容。 |
| font | [Font](arkts-apis-graphics-drawing-font.md) | 是 | 字型对象。 |
| encoding | [TextEncoding](arkts-apis-graphics-drawing-e.md#textencoding) | 否 | 编码类型，默认值为TEXT\_ENCODING\_UTF8。当前只有TEXT\_ENCODING\_UTF8生效，其余编码类型也会被视为TEXT\_ENCODING\_UTF8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-apis-graphics-drawing-textblob.md) | TextBlob对象。 |

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
11. const textBlob = drawing.TextBlob.makeFromString("drawing", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
12. canvas.attachBrush(brush);
13. canvas.drawTextBlob(textBlob, 20, 20);
14. canvas.detachBrush();
15. }
16. }
```

## makeFromRunBuffer

PhonePC/2in1TabletTVWearable

static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob

基于RunBuffer信息创建TextBlob对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | Array<[TextBlobRunBuffer](arkts-apis-graphics-drawing-i.md#textblobrunbuffer)> | 是 | TextBlobRunBuffer数组。 |
| font | [Font](arkts-apis-graphics-drawing-font.md) | 是 | 字型对象。 |
| bounds | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 否 | 可选，如果不设置，则无边界框。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-apis-graphics-drawing-textblob.md) | TextBlob对象。 |

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
7. const font = new drawing.Font();
8. font.setSize(20);
9. let runBuffer : Array<drawing.TextBlobRunBuffer> = [
10. { glyph: 65, positionX: 0, positionY: 0 },
11. { glyph: 227, positionX: 14.9, positionY: 0 },
12. { glyph: 283, positionX: 25.84, positionY: 0 },
13. { glyph: 283, positionX: 30.62, positionY: 0 },
14. { glyph: 299, positionX: 35.4, positionY: 0}
15. ];
16. const textBlob = drawing.TextBlob.makeFromRunBuffer(runBuffer, font, null);
17. const brush = new drawing.Brush();
18. brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
19. canvas.attachBrush(brush);
20. canvas.drawTextBlob(textBlob, 20, 20);
21. canvas.detachBrush();
22. }
23. }
```

## bounds

PhonePC/2in1TabletTVWearable

bounds(): common2D.Rect

获取文字边界框的矩形区域。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Rect](js-apis-graphics-common2d.md#rect) | 文字边界框的矩形区域。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. const font = new drawing.Font();
4. font.setSize(20);
5. const textBlob = drawing.TextBlob.makeFromString("drawing", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
6. let bounds = textBlob.bounds();
```
