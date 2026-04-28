---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-region
title: Class (Region)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Region)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9c2b8c6935547466a8801550cb0efa5942d791add43fb6d619881a1bde41b5a8
---

区域对象，用于描述所绘制图形的区域信息。

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

## constructor20+

PhonePC/2in1TabletTVWearable

constructor()

构造一个区域对象。

**系统能力：** SystemCapability.Graphics.Drawing

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. region.setRect(200, 200, 400, 400);
18. canvas.drawRegion(region);
19. canvas.detachPen();
20. }
21. }
```

## constructor20+

PhonePC/2in1TabletTVWearable

constructor(region: Region)

拷贝一个区域对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 用于拷贝的区域。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. region.setRect(200, 200, 400, 400);
18. let region2 = new drawing.Region(region);
19. canvas.drawRegion(region2);
20. canvas.detachPen();
21. }
22. }
```

## constructor20+

PhonePC/2in1TabletTVWearable

constructor(left: number, top: number, right: number, bottom: number)

构造矩形区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | number | 是 | 矩形区域的左侧位置（矩形左上角横坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。 |
| top | number | 是 | 矩形区域的顶部位置（矩形左上角纵坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。 |
| right | number | 是 | 矩形区域的右侧位置（矩形右下角横坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。 |
| bottom | number | 是 | 矩形区域的底部位置（矩形右下角纵坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region(100, 100, 200, 200);
17. canvas.drawRegion(region);
18. canvas.detachPen();
19. }
20. }
```

## isEqual20+

PhonePC/2in1TabletTVWearable

isEqual(other: Region): boolean

用于判断其他区域是否与当前区域相等。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 区域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回其他区域是否与当前区域相等的结果。true表示相等，false表示不相等。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let other = new drawing.Region();
18. region.setRect(100, 100, 400, 400);
19. other.setRect(150, 150, 250, 250);
20. let flag: boolean = false;
21. flag = region.isEqual(other);
22. console.info('flag: ', flag);
23. canvas.drawRegion(region);
24. canvas.drawRegion(other);
25. canvas.detachPen();
26. }
27. }
```

## isComplex20+

PhonePC/2in1TabletTVWearable

isComplex(): boolean

判断当前区域是否包含多个矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域是否包含多个矩形的结果。true表示当前区域包含多个矩形，false表示当前区域不包含多个矩形。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. import { RenderNode } from '@kit.ArkUI';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let other = new drawing.Region();
18. region.setRect(100, 100, 200, 200);
19. region.op(new drawing.Region(220, 200, 280, 280), drawing.RegionOp.UNION);
20. let flag: boolean = false;
21. flag = region.isComplex();
22. console.info('flag :', flag);
23. canvas.drawRegion(region);
24. canvas.drawRegion(other);
25. canvas.detachPen();
26. }
27. }
```

## isEmpty20+

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

判断当前区域是否为空。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域是否为空。true表示当前区域为空，false表示当前区域不为空。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let flag: boolean = region.isEmpty();
18. console.info('flag: ', flag);
19. region.setRect(100, 100, 400, 400);
20. flag = region.isEmpty();
21. console.info('flag: ', flag);
22. canvas.drawRegion(region);
23. canvas.detachPen();
24. }
25. }
```

## getBounds20+

PhonePC/2in1TabletTVWearable

getBounds(): common2D.Rect

获取区域的边界。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Rect](js-apis-graphics-common2d.md#rect) | 返回当前区域的边界矩形。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let region = new drawing.Region();
4. let rect = region.getBounds();
```

## getBoundaryPath20+

PhonePC/2in1TabletTVWearable

getBoundaryPath(): Path

返回一个新路径，该路径取自当前区域的边界。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Path](arkts-apis-graphics-drawing-path.md) | 返回当前区域边界的路径。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let region = new drawing.Region();
4. let path = region.getBoundaryPath();
```

## isPointContained12+

PhonePC/2in1TabletTVWearable

isPointContained(x: number, y: number) : boolean

判断测试点是否在区域内。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 测试点的x轴坐标。该参数必须为整数。如果输入的数字包含小数部分，小数部分将被舍去。 |
| y | number | 是 | 测试点的y轴坐标。该参数必须为整数。如果输入的数字包含小数部分，小数部分将被舍去。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回测试点是否在区域内的结果。true表示测试点在区域内，false表示测试点不在区域内。 |

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
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. region.setRect(100, 100, 400, 400);
18. let flag: boolean = false;
19. flag = region.isPointContained(200, 200);
20. console.info("region isPointContained : " + flag);
21. canvas.drawPoint(200, 200);
22. canvas.drawRegion(region);
23. canvas.detachPen();
24. }
25. }
```

## offset20+

PhonePC/2in1TabletTVWearable

offset(dx: number, dy: number): void

对区域进行平移。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | number | 是 | x轴方向平移量，正数往x轴正方向平移，负数往x轴负方向平移，该参数为整数。 |
| dy | number | 是 | y轴方向平移量，正数往y轴正方向平移，负数往y轴负方向平移，该参数为整数。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. region.setRect(100, 100, 400, 400);
18. region.offset(10, 20);
19. canvas.drawPoint(200, 200);
20. canvas.drawRegion(region);
21. canvas.detachPen();
22. }
23. }
```

## isRegionContained12+

PhonePC/2in1TabletTVWearable

isRegionContained(other: Region) : boolean

判断其他区域是否在当前区域内。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 区域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回其他区域是否在当前区域内的结果。true表示其他区域在当前区域内，false表示其他区域不在当前区域内。 |

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
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let other = new drawing.Region();
18. region.setRect(100, 100, 400, 400);
19. other.setRect(150, 150, 250, 250);
20. let flag: boolean = false;
21. flag = region.isRegionContained(other);
22. console.info("region isRegionContained : " + flag);
23. canvas.drawRegion(region);
24. canvas.drawRegion(other);
25. canvas.detachPen();
26. }
27. }
```

## op12+

PhonePC/2in1TabletTVWearable

op(region: Region, regionOp: RegionOp) : boolean

将当前区域与指定区域进行运算，并替换为运算结果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 区域对象。 |
| regionOp | [RegionOp](arkts-apis-graphics-drawing-e.md#regionop12) | 是 | 区域合并操作类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回区域运算结果是否成功替换当前区域。true表示区域运算结果替换当前区域成功，false表示区域运算结果替换当前区域失败。 |

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
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. region.setRect(200, 200, 400, 400);
18. let othregion = new drawing.Region();
19. othregion.setRect(110, 110, 240, 240);
20. let flag: boolean = false;
21. flag = region.op(othregion, drawing.RegionOp.REPLACE);
22. console.info("region op : " + flag);
23. canvas.drawRegion(region);
24. canvas.detachPen();
25. }
26. }
```

## quickReject12+

PhonePC/2in1TabletTVWearable

quickReject(left: number, top: number, right: number, bottom: number) : boolean

快速判断矩形和区域是否不相交，实际上比较的是矩形和区域的外接矩形是否不相交，因此会有误差。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | number | 是 | 矩形区域的左侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| top | number | 是 | 矩形区域的顶部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| right | number | 是 | 矩形区域的右侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| bottom | number | 是 | 矩形区域的底部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回矩形是否与区域不相交的结果。true表示矩形与区域不相交，false表示矩形与区域相交。 |

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
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. region.setRect(100, 100, 400, 400);
18. let flag: boolean = false;
19. flag = region.quickReject(50, 50, 70, 70);
20. console.info("region quickReject : " + flag);
21. canvas.drawRegion(region);
22. canvas.detachPen();
23. }
24. }
```

## quickRejectRegion20+

PhonePC/2in1TabletTVWearable

quickRejectRegion(region: Region): boolean

判断当前区域是否与另一个区域不相交。实际上比较的是两个区域的外接矩形是否不相交，因此会有误差。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 指定的区域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否当前区域与另外的区域不相交的结果。true表示不相交，false表示相交。仅点和边相交返回true。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let region2 = new drawing.Region();
18. region2.setRect(100, 100, 400, 400);
19. let flag: boolean = false;
20. flag = region.quickRejectRegion(region2);
21. console.info("region quickRejectRegion: " + flag);
22. canvas.drawRegion(region);
23. canvas.detachPen();
24. }
25. }
```

## setPath12+

PhonePC/2in1TabletTVWearable

setPath(path: Path, clip: Region) : boolean

设置一个与裁剪区域内路径轮廓相匹配的区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path](arkts-apis-graphics-drawing-path.md) | 是 | 路径对象。 |
| clip | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 区域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置一个与裁剪区域内路径轮廓相匹配的区域是否成功。true表示设置成功，false表示设置失败。 |

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
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let path = new drawing.Path();
18. region.setRect(100, 100, 400, 400);
19. path.arcTo(50, 50, 300, 300, 0, 359);
20. let flag: boolean = false;
21. flag = region.setPath(path, region);
22. console.info("region setPath : " + flag);
23. canvas.drawRegion(region);
24. canvas.detachPen();
25. }
26. }
```

## setRegion20+

PhonePC/2in1TabletTVWearable

setRegion(region: Region): void

设置当前区域为另一块区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-graphics-drawing-region.md) | 是 | 用于赋值的区域。 |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. region.setRect(100, 100, 200, 200);
18. let region2 = new drawing.Region();
19. region2.setRegion(region);
20. canvas.drawRegion(region2);
21. canvas.detachPen();
22. }
23. }
```

## setEmpty20+

PhonePC/2in1TabletTVWearable

setEmpty(): void

设置当前区域为空。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. let region = new drawing.Region();
7. region.setRect(100, 100, 200, 200);
8. let isEmpty = region.isEmpty();
9. console.info("isEmpty :" + isEmpty);
10. region.setEmpty();
11. isEmpty = region.isEmpty();
12. console.info("isEmpty :" + isEmpty);
13. }
14. }
```

## setRect12+

PhonePC/2in1TabletTVWearable

setRect(left: number, top: number, right: number, bottom: number) : boolean

设置一个矩形区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | number | 是 | 矩形区域的左侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| top | number | 是 | 矩形区域的顶部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| right | number | 是 | 矩形区域的右侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| bottom | number | 是 | 矩形区域的底部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置矩形区域是否成功的结果。true表示设置矩形区域成功，false表示设置矩形区域失败。 |

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
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let flag: boolean = false;
18. flag = region.setRect(50, 50, 300, 300);
19. console.info("region setRect : " + flag);
20. canvas.drawRegion(region);
21. canvas.detachPen();
22. }
23. }
```

## isRect23+

PhonePC/2in1TabletTVWearable

isRect(): boolean

判断当前区域是否等同于单个矩形。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域是否等同于单个矩形的结果。true表示当前区域等同于单个矩形，false表示当前区域不等同于单个矩形。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. import { RenderNode } from '@kit.ArkUI';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let flag: boolean = false;
18. flag = region.isRect();
19. console.info('flag :', flag);
20. region.setRect(100, 100, 200, 200);
21. flag = region.isRect();
22. console.info('flag :', flag);
23. let other = new drawing.Region(220, 200, 280, 280);
24. region.op(other, drawing.RegionOp.UNION);
25. flag = region.isRect();
26. console.info('flag :', flag);
27. canvas.drawRegion(region);
28. canvas.detachPen();
29. }
30. }
```

## quickContains23+

PhonePC/2in1TabletTVWearable

quickContains(left: number, top: number, right: number, bottom: number): boolean

判断当前区域是否等同于单个矩形并且包含指定矩形。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | number | 是 | 矩形区域的左侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| top | number | 是 | 矩形区域的顶部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| right | number | 是 | 矩形区域的右侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |
| bottom | number | 是 | 矩形区域的底部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域是否等同于单个矩形并且包含指定矩形的结果。true表示当前区域等同于单个矩形并且包含指定矩形，false表示当前区域不等同于单个矩形或不包含指定矩形。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. import { RenderNode } from '@kit.ArkUI';

4. class DrawingRenderNode extends RenderNode {
5. draw(context: DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. pen.setColor({
9. alpha: 255,
10. red: 255,
11. green: 0,
12. blue: 0
13. });
14. pen.setStrokeWidth(10);
15. canvas.attachPen(pen);
16. let region = new drawing.Region();
17. let flag: boolean = false;
18. flag = region.quickContains(10, 10, 100, 100);
19. console.info('flag :', flag);
20. let other = new drawing.Region();
21. other.setRect(100, 100, 200, 200);
22. flag = other.quickContains(10, 10, 100, 100);
23. console.info('flag :', flag);
24. canvas.drawRegion(region);
25. canvas.drawRegion(other);
26. canvas.detachPen();
27. }
28. }
```
