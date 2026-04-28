---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadowlayer
title: Class (ShadowLayer)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (ShadowLayer)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:52efea0eab7b36029936ea8b10a0648d6866c573eb45aba37c8365e1ec110e21
---

阴影层对象。

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

## create12+

PhonePC/2in1TabletTVWearable

static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer

创建阴影层对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | number | 是 | 阴影的半径，必须为大于零的浮点数。 |
| x | number | 是 | x轴上的偏移点，该参数为浮点数。 |
| y | number | 是 | Y轴上的偏移点，该参数为浮点数。 |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | ARGB格式的颜色，每个颜色通道的值是0到255之间的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShadowLayer](arkts-apis-graphics-drawing-shadowlayer.md) | 返回创建的阴影层对象。 |

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
7. let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
8. let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
9. }
10. }
```

## create18+

PhonePC/2in1TabletTVWearable

static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer

创建阴影层对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | number | 是 | 阴影的半径，必须为大于零的浮点数。 |
| x | number | 是 | x轴上的偏移点，该参数为浮点数。 |
| y | number | 是 | Y轴上的偏移点，该参数为浮点数。 |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | number | 是 | 颜色，可以用16进制ARGB格式的无符号整数表示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShadowLayer](arkts-apis-graphics-drawing-shadowlayer.md) | 返回创建的阴影层对象。 |

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
7. let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, 0xff00ff00);
8. }
9. }
```
