---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-patheffect
title: Class (PathEffect)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (PathEffect)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:49955ddaf396f0ad030c18b4105e673c018142ef867d2e529364d9ea6ce9bf54
---

路径效果对象。

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

## createDashPathEffect12+

PhonePC/2in1TabletTVWearable

static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect

创建将路径变为虚线的路径效果对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intervals | Array<number> | 是 | 表示虚线的ON（实线部分）和OFF（空白部分）长度的数组，数组个数必须是偶数，且>=2，该参数为正整数。 |
| phase | number | 是 | 绘制时的偏移量，该参数为浮点数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 返回创建的路径效果对象。 |

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
7. let intervals = [10, 5];
8. let effect = drawing.PathEffect.createDashPathEffect(intervals, 5);
9. }
10. }
```

## createPathDashEffect18+

PhonePC/2in1TabletTVWearable

static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect

通过路径描述的形状创建一个虚线路径效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 通过该路径生成一个图形，用来填充每个虚线段。 |
| advance | number | 是 | 虚线段的步长，该参数为大于0的浮点数，否则会抛错误码。 |
| phase | number | 是 | 表示虚线段内图形在虚线步长范围内的偏移量，该参数为浮点数，效果为先对偏移量取绝对值，然后对步长取模。 |
| style | [PathDashStyle](arkts-apis-graphics-drawing-e.md#pathdashstyle18) | 是 | 指定虚线效果的样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 返回创建的路径效果对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3. Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let pen = new drawing.Pen();
8. const penColor: common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 }
9. pen.setColor(penColor);
10. pen.setStrokeWidth(10);
11. canvas.attachPen(pen);
12. pen.setAntiAlias(true);

14. const path = new drawing.Path();
15. path.moveTo(100, 100);
16. path.lineTo(150, 50);
17. path.lineTo(200, 100);

19. const path1 = new drawing.Path();
20. path1.moveTo(0, 0);
21. path1.lineTo(10, 0);
22. path1.lineTo(20, 10);
23. path1.lineTo(0,10);

25. let pathEffect1: drawing.PathEffect = drawing.PathEffect.createPathDashEffect(path1, 50, -30,
26. drawing.PathDashStyle.MORPH);
27. pen.setPathEffect(pathEffect1);

29. canvas.attachPen(pen);
30. canvas.drawPath(path);
31. canvas.detachPen();
32. }
33. }
```

## createSumPathEffect18+

PhonePC/2in1TabletTVWearable

static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect

创建一个叠加的路径效果。与createComposePathEffect不同，此接口会分别对两个参数的效果各自独立进行表现，然后将两个效果简单重叠显示。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstPathEffect | [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 是 | 表示第一个路径效果。 |
| secondPathEffect | [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 是 | 表示第二个路径效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 返回创建的路径效果对象。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let intervals = [10, 5];
8. let pathEffectOne = drawing.PathEffect.createDashPathEffect(intervals, 5);
9. let pathEffectTwo = drawing.PathEffect.createDashPathEffect(intervals, 10);
10. let effect = drawing.PathEffect.createSumPathEffect(pathEffectOne, pathEffectTwo);
11. }
12. }
```

## createCornerPathEffect12+

PhonePC/2in1TabletTVWearable

static createCornerPathEffect(radius: number): PathEffect

创建将路径的夹角变成指定半径的圆角的路径效果对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 圆角的半径，必须大于0，该参数为浮点数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 返回创建的路径效果对象。 |

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
7. let effect = drawing.PathEffect.createCornerPathEffect(30);
8. }
9. }
```

## createDiscretePathEffect18+

PhonePC/2in1TabletTVWearable

static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect

创建一种将路径打散，并且在路径上产生不规则分布的效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segLength | number | 是 | 路径中每进行一次打散操作的长度，该长度为浮点数，负数和0时无效果。 |
| dev | number | 是 | 绘制时的末端点的最大移动偏离量，该偏移量为浮点数。 |
| seedAssist | number | 否 | 生成效果伪随机种子辅助变量，默认值为0，该参数为32位无符号整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 返回创建的路径效果对象。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let effect = drawing.PathEffect.createDiscretePathEffect(100, -50, 0);
8. }
9. }
```

## createComposePathEffect18+

PhonePC/2in1TabletTVWearable

static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect

创建路径组合的路径效果对象，首先应用内部路径效果，然后应用外部路径效果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outer | [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 是 | 组合路径效果中外部路径效果。 |
| inner | [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 是 | 组合路径效果中内部路径效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathEffect](arkts-apis-graphics-drawing-patheffect.md) | 返回创建的路径效果对象。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let pathEffect1 = drawing.PathEffect.createCornerPathEffect(100);
8. let pathEffect2 = drawing.PathEffect.createCornerPathEffect(10);
9. let effect = drawing.PathEffect.createComposePathEffect(pathEffect1, pathEffect2);
10. }
11. }
```
