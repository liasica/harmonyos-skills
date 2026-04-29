---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics
title: Graphics
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > Graphics
category: harmonyos-references
scraped_at: 2026-04-29T13:50:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0b6adc47d968012e1a655b6980102145a4a68a153b44c5d2d10824b607646cdd
---

自定义节点相关属性定义的详细信息。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { DrawContext, Size, Offset, Position, Pivot, Scale, Translation, Matrix4, Rotation, Frame, LengthMetricsUnit } from "@kit.ArkUI";
```

## Size

PhonePC/2in1TabletTVWearable

用于返回组件布局大小的宽和高。默认单位为vp，不同的接口使用Size类型时会再定义单位，以接口定义的单位为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 组件大小的宽度。  单位：vp  取值范围：[0, +∞) |
| height | number | 否 | 否 | 组件大小的高度。  单位：vp  取值范围：[0, +∞) |

## Position

PhonePC/2in1TabletTVWearable

type Position = Vector2

用于设置或返回组件的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector2](js-apis-arkui-graphics.md#vector2) | 包含x和y两个值的向量。  单位：vp |

## PositionT12+

PhonePC/2in1TabletTVWearable

type PositionT<T> = Vector2T<T>

用于设置或返回组件的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector2T<T>](js-apis-arkui-graphics.md#vector2tt12) | 包含x和y两个值的向量。  单位：vp |

## Frame

PhonePC/2in1TabletTVWearable

用于设置或返回组件的布局大小和位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 水平方向位置。  单位：vp  取值范围：(-∞, +∞) |
| y | number | 否 | 否 | 垂直方向位置。  单位：vp  取值范围：(-∞, +∞) |
| width | number | 否 | 否 | 组件的宽度。  单位：vp  取值范围：[0, +∞) |
| height | number | 否 | 否 | 组件的高度。  单位：vp  取值范围：[0, +∞) |

## Pivot

PhonePC/2in1TabletTVWearable

type Pivot = Vector2

用于设置组件的轴心坐标，轴心会作为组件的旋转/缩放中心点，影响旋转和缩放效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector2](js-apis-arkui-graphics.md#vector2) | 轴心的x和y轴坐标。该参数为浮点数，默认值为0.5， 取值范围为[0.0, 1.0]。 |

## Scale

PhonePC/2in1TabletTVWearable

type Scale = Vector2

用于设置组件的缩放比例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector2](js-apis-arkui-graphics.md#vector2) | x和y轴的缩放参数。该参数为浮点数，默认值为1.0。 |

## Translation

PhonePC/2in1TabletTVWearable

type Translation = Vector2

用于设置组件的平移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector2](js-apis-arkui-graphics.md#vector2) | x和y轴的平移量。  单位：px |

## Rotation

PhonePC/2in1TabletTVWearable

type Rotation = Vector3

用于设置组件的旋转角度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector3](js-apis-arkui-graphics.md#vector3) | x、y、z轴方向的旋转角度。  单位：度 |

## Offset

PhonePC/2in1TabletTVWearable

type Offset = Vector2

用于设置组件或效果的偏移。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector2](js-apis-arkui-graphics.md#vector2) | x和y轴方向的偏移量。  单位：vp |

## Matrix4

PhonePC/2in1TabletTVWearable

type Matrix4 = [number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number]

设置四阶矩阵。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [number,number,number,number,  number,number,number,number,  number,number,number,number,  number,number,number,number] | 参数为长度为16（4\*4）的number数组。  各number取值范围：(-∞, +∞) |

用于设置组件的变换信息，该类型为一个 4x4 矩阵，使用一个长度为16的number[]进行表示，例如：

```
1. const transform: Matrix4 = [
2. 1, 0, 45, 0,
3. 0, 1,  0, 0,
4. 0, 0,  1, 0,
5. 0, 0,  0, 1
6. ]
```

## Vector2

PhonePC/2in1TabletTVWearable

用于表示包含x和y两个值的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 向量x轴方向的值。  取值范围：(-∞, +∞) |
| y | number | 否 | 否 | 向量y轴方向的值。  取值范围：(-∞, +∞) |

## Vector3

PhonePC/2in1TabletTVWearable

用于表示包含x、y、z三个值的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x轴方向的旋转角度。  取值范围：(-∞, +∞) |
| y | number | 否 | 否 | y轴方向的旋转角度。  取值范围：(-∞, +∞) |
| z | number | 否 | 否 | z轴方向的旋转角度。  取值范围：(-∞, +∞) |

## Vector2T<T>12+

PhonePC/2in1TabletTVWearable

用于表示T类型的包含x和y两个值的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | T | 否 | 否 | 向量x轴方向的值。 |
| y | T | 否 | 否 | 向量y轴方向的值。 |

## DrawContext

PhonePC/2in1TabletTVWearable

图形绘制上下文，提供绘制所需的画布宽度和高度。

### size

PhonePC/2in1TabletTVWearable

get size(): Size

获取画布的宽度和高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Size](js-apis-arkui-graphics.md#size) | 画布的宽度和高度。 |

### sizeInPixel12+

PhonePC/2in1TabletTVWearable

get sizeInPixel(): Size

获取以px为单位的画布的宽度和高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Size](js-apis-arkui-graphics.md#size) | 画布的宽度和高度，以px为单位。 |

### canvas

PhonePC/2in1TabletTVWearable

get canvas(): drawing.Canvas

获取用于绘制的画布。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [drawing.Canvas](arkts-apis-graphics-drawing-canvas.md) | 用于绘制的画布。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, DrawContext } from "@kit.ArkUI";

3. class MyRenderNode extends RenderNode {
4. flag: boolean = false;

6. draw(context: DrawContext) {
7. const size = context.size;
8. const canvas = context.canvas;
9. const sizeInPixel = context.sizeInPixel;
10. }
11. }

13. const renderNode = new MyRenderNode();
14. renderNode.frame = { x: 0, y: 0, width: 100, height: 100 };
15. renderNode.backgroundColor = 0xff519db4;

17. class MyNodeController extends NodeController {
18. private rootNode: FrameNode | null = null;

20. makeNode(uiContext: UIContext): FrameNode | null {
21. this.rootNode = new FrameNode(uiContext);

23. const rootRenderNode = this.rootNode.getRenderNode();
24. if (rootRenderNode !== null) {
25. rootRenderNode.appendChild(renderNode);
26. }

28. return this.rootNode;
29. }
30. }

32. @Entry
33. @Component
34. struct Index {
35. private myNodeController: MyNodeController = new MyNodeController();

37. build() {
38. Row() {
39. NodeContainer(this.myNodeController)
40. }
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/YzAfUsc_SNivg8fCONIpYA/zh-cn_image_0000002558606312.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=D5E9823D87F231E1DDEB050C9C10A3BB2D93F7892FA78F0D66C97622C25D8323)

## Edges<T>12+

PhonePC/2in1TabletTVWearable

用于设置边框的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | T | 否 | 否 | 左侧边框的属性。 |
| top | T | 否 | 否 | 顶部边框的属性。 |
| right | T | 否 | 否 | 右侧边框的属性。 |
| bottom | T | 否 | 否 | 底部边框的属性。 |

## LengthUnit12+

PhonePC/2in1TabletTVWearable

长度属性单位枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PX | 0 | 长度类型，用于描述以px像素单位为单位的长度。 |
| VP | 1 | 长度类型，用于描述以vp像素单位为单位的长度。 |
| FP | 2 | 长度类型，用于描述以fp像素单位为单位的长度。 |
| PERCENT | 3 | 长度类型，用于描述以%像素单位为单位的长度。 |
| LPX | 4 | 长度类型，用于描述以lpx像素单位为单位的长度。 |

## SizeT<T>12+

PhonePC/2in1TabletTVWearable

用于设置宽高的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | T | 否 | 否 | 宽度的属性。 |
| height | T | 否 | 否 | 高度的属性。 |

## LengthMetricsUnit12+

PhonePC/2in1TabletTVWearable

长度属性单位枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 长度类型，用于描述以默认的vp像素单位为单位的长度。 |
| PX | 1 | 长度类型，用于描述以px像素单位为单位的长度。 |

## LengthMetrics12+

PhonePC/2in1TabletTVWearable

用于设置长度属性，当长度单位为PERCENT时，值为1表示100%。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 否 | 长度属性的值。 |
| unit | [LengthUnit](js-apis-arkui-graphics.md#lengthunit12) | 否 | 否 | 长度属性的单位，默认为VP。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(value: number, unit?: LengthUnit)

LengthMetrics的构造函数。若参数unit不传入值或传入undefined，返回值使用默认单位VP；若unit传入非LengthUnit类型的值，返回默认值0VP。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 长度属性的值。  取值范围：[0, +∞) |
| unit | [LengthUnit](js-apis-arkui-graphics.md#lengthunit12) | 否 | 长度属性的单位。 |

### px12+

PhonePC/2in1TabletTVWearable

static px(value: number): LengthMetrics

用于生成单位为PX的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 长度属性的值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | LengthMetrics 类的实例。 |

### vp12+

PhonePC/2in1TabletTVWearable

static vp(value: number): LengthMetrics

用于生成单位为VP的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 长度属性的值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | LengthMetrics 类的实例。 |

### fp12+

PhonePC/2in1TabletTVWearable

static fp(value: number): LengthMetrics

用于生成单位为FP的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 长度属性的值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | LengthMetrics 类的实例。 |

### percent12+

PhonePC/2in1TabletTVWearable

static percent(value: number): LengthMetrics

用于生成单位为PERCENT的长度属性，值为1表示100%。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 长度属性的值。  取值范围：[0, 1] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | LengthMetrics 类的实例。 |

### lpx12+

PhonePC/2in1TabletTVWearable

static lpx(value: number): LengthMetrics

用于生成单位为LPX的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 长度属性的值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | LengthMetrics 类的实例。 |

### resource12+

PhonePC/2in1TabletTVWearable

static resource(value: Resource): LengthMetrics

用于生成Resource类型资源的长度属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Resource | 是 | 长度属性的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | LengthMetrics 类的实例。 |

**示例：**

使用LengthMetrics设置Row的padding和margin属性。

```
1. import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SizeExample {
6. build() {
7. Column({ space: 10 }) {
8. Text('margin and padding:')
9. .fontSize(12)
10. .fontColor(0xCCCCCC)
11. .width('90%')
12. Row() {
13. Row() {
14. Row()
15. .size({ width: '100%', height: '100%' })
16. .backgroundColor('#ffd5d5d5')
17. }
18. .width(80)
19. .height(80)
20. .padding({
21. top: new LengthMetrics(20, LengthUnit.VP),
22. bottom: LengthMetrics.px(15),
23. start: LengthMetrics.vp(10),
24. end: LengthMetrics.fp(20)
25. })
26. .margin({
27. top: LengthMetrics.percent(0.1),
28. bottom: LengthMetrics.lpx(20),
29. start: LengthMetrics.resource($r('app.float.row_margin_start')),
30. end: LengthMetrics.vp(10)
31. })
32. .backgroundColor(Color.White)
33. }
34. .backgroundColor("#ff2787d9")
35. }
36. .width('100%')
37. .margin({ top: 5 })
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/oePaQ9LOQj62LFsCzPXOYw/zh-cn_image_0000002589325839.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=C841B9AC38666A3461B86EEE6A60C1FD012C5B02958314CC57B41C2C770BBD9F)

## ColorMetrics12+

PhonePC/2in1TabletTVWearable

用于混合颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### numeric12+

PhonePC/2in1TabletTVWearable

static numeric(value: number): ColorMetrics

使用HEX格式颜色实例化 ColorMetrics 类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | HEX格式颜色。  取值范围：支持rgb或者argb |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | ColorMetrics 类的实例。 |

### rgba12+

PhonePC/2in1TabletTVWearable

static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics

使用rgb或者rgba格式颜色实例化 ColorMetrics 类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| red | number | 是 | 颜色的R分量（红色），值是0~255的整数。 |
| green | number | 是 | 颜色的G分量（绿色），值是0~255的整数。 |
| blue | number | 是 | 颜色的B分量（蓝色），值是0~255的整数。 |
| alpha | number | 否 | 颜色的A分量（透明度），值是0.0~1.0的浮点数，默认值为1.0，不透明。  **说明：** alpha小于0为全透明，大于1为不透明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | ColorMetrics 类的实例。 |

### colorWithSpace20+

PhonePC/2in1TabletTVWearable

static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics

使用[ColorSpace](ts-appendix-enums.md#colorspace20)和rgba格式颜色实例化ColorMetrics类。仅部分属性支持在display-p3色彩空间中设置颜色。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [ColorSpace](ts-appendix-enums.md#colorspace20) | 是 | 颜色空间，用于指定颜色的色彩空间。使用ColorSpace.DISPLAY\_P3，需要对应窗口调用[setWindowColorSpace](arkts-apis-window-window.md#setwindowcolorspace9-1)接口，将当前窗口设置为广色域模式。 |
| red | number | 是 | 颜色的R分量（红色），值是0~1的浮动数值。 |
| green | number | 是 | 颜色的G分量（绿色），值是0~1的浮动数值。 |
| blue | number | 是 | 颜色的B分量（蓝色），值是0~1的浮动数值。 |
| alpha | number | 否 | 颜色的A分量（透明度），值是0.0~1.0的浮点数，默认值为1.0，不透明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | ColorMetrics类的实例。 |

### resourceColor12+

PhonePC/2in1TabletTVWearable

static resourceColor(color: ResourceColor): ColorMetrics

使用资源格式颜色实例化 ColorMetrics 类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 资源格式颜色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | ColorMetrics 类的实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[系统资源错误码](errorcode-system-resource.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause:1.The type of the input color parameter is not ResourceColor;2.The format of the input color string is not RGB or RGBA. |
| 180003 | Failed to obtain the color resource. |

### blendColor12+

PhonePC/2in1TabletTVWearable

blendColor(overlayColor: ColorMetrics): ColorMetrics

在当前颜色的上方叠加上一层指定的颜色（overlayColor），并返回混合后的新颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| overlayColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 是 | 要叠加在上方的颜色对象。alpha属性决定叠加强度。1.0表示完全覆盖，0.0表示完全透明，混合结果为原色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 新的颜色对象，其red、green、blue和alpha通道均为当前颜色与叠加颜色混合后的结果值。 |

**混合公式：**

混合后透明度为完全不透明，rgb按照以下公式计算：

result\_rgb = overlay\_rgb\*(overlay\_alpha) + (1 - overlay\_alpha) \* base\_rgb

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. The type of the input parameter is not ColorMetrics. |

### color12+

PhonePC/2in1TabletTVWearable

get color(): string

获取ColorMetrics的颜色，返回的是rgba字符串的格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | rgba字符串格式的颜色。 示例：'rgba(255, 100, 255, 0.5)' |

### red12+

PhonePC/2in1TabletTVWearable

get red(): number

获取ColorMetrics颜色的R分量（红色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 颜色的R分量（红色），值是0~255的整数。 |

### green12+

PhonePC/2in1TabletTVWearable

get green(): number

获取ColorMetrics颜色的G分量（绿色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 颜色的G分量（绿色），值是0~255的整数。 |

### blue12+

PhonePC/2in1TabletTVWearable

get blue(): number

获取ColorMetrics颜色的B分量（蓝色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 颜色的B分量（蓝色），值是0~255的整数。 |

### alpha12+

PhonePC/2in1TabletTVWearable

get alpha(): number

获取ColorMetrics颜色的A分量（透明度）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 颜色的A分量（透明度），值是0~255的整数。 |

**示例：**

```
1. import { ColorMetrics } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function getBlendColor(baseColor: ResourceColor): ColorMetrics {
5. let sourceColor: ColorMetrics;
6. try {
7. // 在使用ColorMetrics的resourceColor和blendColor需要追加捕获异常处理
8. // 可能返回的arkui子系统错误码有401和180003
9. // 61 157 180
10. sourceColor = ColorMetrics.resourceColor(baseColor).blendColor(ColorMetrics.resourceColor("#083d9db4"));
11. console.info(`current color is ${sourceColor.color} r:${sourceColor.red} g:${sourceColor.green} b:${sourceColor.blue} a :${sourceColor.alpha}`);
12. } catch (error) {
13. console.error("getBlendColor failed, code = " + (error as BusinessError).code + ", message = " +
14. (error as BusinessError).message);
15. sourceColor = ColorMetrics.resourceColor("#19000000");
16. }
17. return sourceColor;
18. }

20. @Entry
21. @Component
22. struct ColorMetricsSample {
23. build() {
24. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
25. Button("ColorMetrics blendColor")
26. .width('80%')
27. .align(Alignment.Center)
28. .height(50)
29. .backgroundColor(getBlendColor("#ff3d9db4").color)
30. .margin(10)
31. Button("ColorMetrics numeric")
32. .width('80%')
33. .align(Alignment.Center)
34. .height(50)
35. .backgroundColor(ColorMetrics.numeric(0xff707070).color)
36. .margin(10)
37. Button("ColorMetrics rgba")
38. .width('80%')
39. .align(Alignment.Center)
40. .height(50)
41. .backgroundColor(ColorMetrics.rgba(0, 74, 175, 255).color)
42. .margin(10)
43. Button("ColorMetrics colorWithSpace")
44. .width('80%')
45. .align(Alignment.Center)
46. .height(50)
47. .backgroundColor(ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.4392, 0.4392, 0.4392).color)
48. .margin(10)
49. }
50. .width('100%')
51. .height('100%')
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/3Psol7vXQjCVeAXDy-Gz7Q/zh-cn_image_0000002589245781.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=E0EAE3C95F98F17A8AF66273EFB4B9ED865DDF2357EAE01F6C90B4D22344E625)

## Corners<T>12+

PhonePC/2in1TabletTVWearable

用于设置四个角的圆角属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| topLeft | T | 否 | 否 | 左上边框的圆角属性。 |
| topRight | T | 否 | 否 | 右上边框的圆角属性。 |
| bottomLeft | T | 否 | 否 | 左下边框的圆角属性。 |
| bottomRight | T | 否 | 否 | 右下边框的圆角属性。 |

## CornerRadius12+

PhonePC/2in1TabletTVWearable

type CornerRadius = Corners<Vector2>

设置四个角的圆角x轴与y轴的半轴长。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Corners](js-apis-arkui-graphics.md#cornerst12)<[Vector2](js-apis-arkui-graphics.md#vector2)> | 四个角的圆角x轴与y轴的半轴长。 |

## BorderRadiuses12+

PhonePC/2in1TabletTVWearable

type BorderRadiuses = Corners<number>

设置四个角的圆角半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Corners](js-apis-arkui-graphics.md#cornerst12)<number> | 四个角的圆角半径。 |

## Rect12+

PhonePC/2in1TabletTVWearable

type Rect = common2D.Rect

用于设置矩形的形状。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [common2D.Rect](js-apis-graphics-common2d.md#rect) | 矩形区域。 |

## RoundRect12+

PhonePC/2in1TabletTVWearable

用于设置带有圆角的矩形。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | [Rect](js-apis-arkui-graphics.md#rect12) | 否 | 否 | 设置矩形的属性。 |
| corners | [CornerRadius](js-apis-arkui-graphics.md#cornerradius12) | 否 | 否 | 设置圆角的属性。 |

## Circle12+

PhonePC/2in1TabletTVWearable

用于设置圆形的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| centerX | number | 否 | 否 | 圆心x轴的位置，单位为px。 |
| centerY | number | 否 | 否 | 圆心y轴的位置，单位为px。 |
| radius | number | 否 | 否 | 圆形的半径，单位为px。  取值范围：[0, +∞) |

## CommandPath12+

PhonePC/2in1TabletTVWearable

用于设置路径绘制的指令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [commands](ts-drawing-components-path.md#commands) | string | 否 | 否 | 路径绘制的指令字符串。像素单位的转换方法请参考[像素单位](ts-pixel-units.md)。  单位：px |

## ShapeMask12+

PhonePC/2in1TabletTVWearable

用于设置图形遮罩。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fillColor | number | 否 | 否 | 遮罩的填充颜色，使用ARGB格式。默认值为0XFF000000。  通过fillColor的透明度和亮度生成一个仅含透明度的颜色。亮度越高，颜色越透明。然后，使用[BlendMode.SRC\_IN](arkts-apis-graphics-drawing-e.md#blendmode)方式与RenderNode本身的颜色混合，生成最终颜色。 |
| strokeColor | number | 否 | 否 | 遮罩的边框颜色，使用ARGB格式。默认值为0XFF000000。  通过strokeColor的透明度和亮度生成一个仅含透明度的颜色。亮度越高，颜色越透明。然后，使用[BlendMode.SRC\_IN](arkts-apis-graphics-drawing-e.md#blendmode)方式与RenderNode本身的颜色混合，生成最终颜色。 |
| strokeWidth | number | 否 | 否 | 遮罩的边框宽度，单位为px。默认值为0。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor()

ShapeMask的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setRectShape12+

PhonePC/2in1TabletTVWearable

setRectShape(rect: Rect): void

用于设置矩形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [Rect](js-apis-arkui-graphics.md#rect12) | 是 | 矩形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. private rootNode: FrameNode | null = null;

6. makeNode(uiContext: UIContext): FrameNode | null {
7. this.rootNode = new FrameNode(uiContext);

9. const mask = new ShapeMask();
10. mask.setRectShape({
11. left: 0,
12. right: uiContext.vp2px(150),
13. top: 0,
14. bottom: uiContext.vp2px(150)
15. });
16. mask.fillColor = 0X55FF0000;

18. const renderNode = new RenderNode();
19. renderNode.frame = {
20. x: 0,
21. y: 0,
22. width: 150,
23. height: 150
24. };
25. renderNode.backgroundColor = 0XFF00FF00;
26. renderNode.shapeMask = mask;

28. const rootRenderNode = this.rootNode.getRenderNode();
29. if (rootRenderNode !== null) {
30. rootRenderNode.appendChild(renderNode);
31. }

33. return this.rootNode;
34. }
35. }

37. @Entry
38. @Component
39. struct Index {
40. private myNodeController: MyNodeController = new MyNodeController();

42. build() {
43. Row() {
44. NodeContainer(this.myNodeController)
45. }
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aOhIV802Qzq8Xixy6DreHw/zh-cn_image_0000002558765970.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=8C78CF2A7377206ABA3E1514B6A4C2E9DEAF1D273B76331D39499EF846EB9A12)

### setRoundRectShape12+

PhonePC/2in1TabletTVWearable

setRoundRectShape(roundRect: RoundRect): void

用于设置圆角矩形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roundRect | [RoundRect](js-apis-arkui-graphics.md#roundrect12) | 是 | 圆角矩形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeMask,RoundRect} from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. private rootNode: FrameNode | null = null;

6. makeNode(uiContext: UIContext): FrameNode | null {
7. this.rootNode = new FrameNode(uiContext);

9. const mask = new ShapeMask();
10. const roundRect: RoundRect = {
11. rect: { left: 0, top: 0, right: uiContext.vp2px(150), bottom: uiContext.vp2px(150) },
12. corners: {
13. topLeft: { x: 32, y: 32 },
14. topRight: { x: 32, y: 32 },
15. bottomLeft: { x: 32, y: 32 },
16. bottomRight: { x: 32, y: 32 }
17. }
18. }
19. mask.setRoundRectShape(roundRect);
20. mask.fillColor = 0X55FF0000;

22. const renderNode = new RenderNode();
23. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
24. renderNode.backgroundColor = 0XFF00FF00;
25. renderNode.shapeMask = mask;

27. const rootRenderNode = this.rootNode.getRenderNode();
28. if (rootRenderNode !== null) {
29. rootRenderNode.appendChild(renderNode);
30. }

32. return this.rootNode;
33. }
34. }

36. @Entry
37. @Component
38. struct Index {
39. private myNodeController: MyNodeController = new MyNodeController();

41. build() {
42. Row() {
43. NodeContainer(this.myNodeController)
44. }
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/xZHf1CTZRRq2WwNz1twHHA/zh-cn_image_0000002558606314.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=214D0EF085B9478A82BBF3C5D6A421F0E74F47A20B7A8F4741A323CBF6B68F03)

### setCircleShape12+

PhonePC/2in1TabletTVWearable

setCircleShape(circle: Circle): void

用于设置圆形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| circle | [Circle](js-apis-arkui-graphics.md#circle12) | 是 | 圆形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. private rootNode: FrameNode | null = null;

6. makeNode(uiContext: UIContext): FrameNode | null {
7. this.rootNode = new FrameNode(uiContext);

9. const mask = new ShapeMask();
10. mask.setCircleShape({ centerY: uiContext.vp2px(75), centerX: uiContext.vp2px(75), radius: uiContext.vp2px(75) });
11. mask.fillColor = 0X55FF0000;

13. const renderNode = new RenderNode();
14. renderNode.frame = {
15. x: 0,
16. y: 0,
17. width: 150,
18. height: 150
19. };
20. renderNode.backgroundColor = 0XFF00FF00;
21. renderNode.shapeMask = mask;

23. const rootRenderNode = this.rootNode.getRenderNode();
24. if (rootRenderNode !== null) {
25. rootRenderNode.appendChild(renderNode);
26. }

28. return this.rootNode;
29. }
30. }

32. @Entry
33. @Component
34. struct Index {
35. private myNodeController: MyNodeController = new MyNodeController();

37. build() {
38. Row() {
39. NodeContainer(this.myNodeController)
40. }
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/D3wKwk81Tf6pnqVKgRYryg/zh-cn_image_0000002589325841.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=6F45D7A9AFF5576B91CB347E8047C43FE0B34ADEEC2DCA92B04BFEB58AD14B45)

### setOvalShape12+

PhonePC/2in1TabletTVWearable

setOvalShape(oval: Rect): void

用于设置椭圆形遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oval | [Rect](js-apis-arkui-graphics.md#rect12) | 是 | 椭圆形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. private rootNode: FrameNode | null = null;

6. makeNode(uiContext: UIContext): FrameNode | null {
7. this.rootNode = new FrameNode(uiContext);

9. const mask = new ShapeMask();
10. mask.setOvalShape({ left: 0, right: uiContext.vp2px(150), top: 0, bottom: uiContext.vp2px(100) });
11. mask.fillColor = 0X55FF0000;

13. const renderNode = new RenderNode();
14. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
15. renderNode.backgroundColor = 0XFF00FF00;
16. renderNode.shapeMask = mask;

18. const rootRenderNode = this.rootNode.getRenderNode();
19. if (rootRenderNode !== null) {
20. rootRenderNode.appendChild(renderNode);
21. }

23. return this.rootNode;
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();

32. build() {
33. Row() {
34. NodeContainer(this.myNodeController)
35. }
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/I-fRPys6SZ60130C0Hx4Yg/zh-cn_image_0000002589245783.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=F29BDC551CD80D58060C745D73081831C219F19A6470D80B492A6489E32A8D63)

### setCommandPath12+

PhonePC/2in1TabletTVWearable

setCommandPath(path: CommandPath): void

用于设置路径绘制指令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [CommandPath](js-apis-arkui-graphics.md#commandpath12) | 是 | 路径绘制指令。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

3. const mask = new ShapeMask();
4. mask.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });
5. mask.fillColor = 0X55FF0000;

7. const renderNode = new RenderNode();
8. renderNode.frame = {
9. x: 0,
10. y: 0,
11. width: 150,
12. height: 150
13. };
14. renderNode.backgroundColor = 0XFF00FF00;
15. renderNode.shapeMask = mask;

18. class MyNodeController extends NodeController {
19. private rootNode: FrameNode | null = null;

21. makeNode(uiContext: UIContext): FrameNode | null {
22. this.rootNode = new FrameNode(uiContext);

24. const rootRenderNode = this.rootNode.getRenderNode();
25. if (rootRenderNode !== null) {
26. rootRenderNode.appendChild(renderNode);
27. }

29. return this.rootNode;
30. }
31. }

33. @Entry
34. @Component
35. struct Index {
36. private myNodeController: MyNodeController = new MyNodeController();

38. build() {
39. Row() {
40. NodeContainer(this.myNodeController)
41. }
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/hS-W9LUVRZWbGRY4C3ys_g/zh-cn_image_0000002558765972.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=E1423D229904C39A17570E950C226E3E8A6338C25E90067BF5A271E99F49BD11)

## ShapeClip12+

PhonePC/2in1TabletTVWearable

用于设置图形裁剪。

### constructor12+

PhonePC/2in1TabletTVWearable

constructor()

ShapeClip的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

### setRectShape12+

PhonePC/2in1TabletTVWearable

setRectShape(rect: Rect): void

用于裁剪矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [Rect](js-apis-arkui-graphics.md#rect12) | 是 | 矩形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

3. const clip = new ShapeClip();
4. clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

6. const renderNode = new RenderNode();
7. renderNode.frame = {
8. x: 0,
9. y: 0,
10. width: 150,
11. height: 150
12. };
13. renderNode.backgroundColor = 0xff519db4;
14. renderNode.shapeClip = clip;
15. const shapeClip = renderNode.shapeClip;

17. class MyNodeController extends NodeController {
18. private rootNode: FrameNode | null = null;

20. makeNode(uiContext: UIContext): FrameNode | null {
21. this.rootNode = new FrameNode(uiContext);

23. const rootRenderNode = this.rootNode.getRenderNode();
24. if (rootRenderNode !== null) {
25. rootRenderNode.appendChild(renderNode);
26. }

28. return this.rootNode;
29. }
30. }

32. @Entry
33. @Component
34. struct Index {
35. private myNodeController: MyNodeController = new MyNodeController();

37. build() {
38. Column() {
39. NodeContainer(this.myNodeController)
40. .borderWidth(1)
41. .margin({ bottom: 20 })
42. Button("setRectShape")
43. .onClick(() => {
44. shapeClip.setRectShape({
45. left: 0,
46. right: 150,
47. top: 0,
48. bottom: 150
49. });
50. renderNode.shapeClip = shapeClip;
51. })
52. }.margin(20)
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/RsxUMXM0Qsal5z4YUNLQ8Q/zh-cn_image_0000002558606316.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=4606F20029BB7CFF9E958286357FB9D613583B67C4D9DD64593D07D3AB7DA7E9)

### setRoundRectShape12+

PhonePC/2in1TabletTVWearable

setRoundRectShape(roundRect: RoundRect): void

用于裁剪圆角矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roundRect | [RoundRect](js-apis-arkui-graphics.md#roundrect12) | 是 | 圆角矩形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

3. const clip = new ShapeClip();
4. clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

6. const renderNode = new RenderNode();
7. renderNode.frame = {
8. x: 0,
9. y: 0,
10. width: 150,
11. height: 150
12. };
13. renderNode.backgroundColor = 0XFF00FF00;
14. renderNode.shapeClip = clip;

16. class MyNodeController extends NodeController {
17. private rootNode: FrameNode | null = null;

19. makeNode(uiContext: UIContext): FrameNode | null {
20. this.rootNode = new FrameNode(uiContext);

22. const rootRenderNode = this.rootNode.getRenderNode();
23. if (rootRenderNode !== null) {
24. rootRenderNode.appendChild(renderNode);
25. }

27. return this.rootNode;
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. private myNodeController: MyNodeController = new MyNodeController();

36. build() {
37. Column() {
38. NodeContainer(this.myNodeController)
39. .borderWidth(1)
40. Button("setRoundRectShape")
41. .onClick(() => {
42. renderNode.shapeClip.setRoundRectShape({
43. rect: {
44. left: 0,
45. top: 0,
46. right: this.getUIContext().vp2px(150),
47. bottom: this.getUIContext().vp2px(150)
48. },
49. corners: {
50. topLeft: { x: 32, y: 32 },
51. topRight: { x: 32, y: 32 },
52. bottomLeft: { x: 32, y: 32 },
53. bottomRight: { x: 32, y: 32 }
54. }
55. });
56. })
57. }
58. }
59. }
```

### setCircleShape12+

PhonePC/2in1TabletTVWearable

setCircleShape(circle: Circle): void

用于裁剪圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| circle | [Circle](js-apis-arkui-graphics.md#circle12) | 是 | 圆形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

3. const clip = new ShapeClip();
4. clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

6. const renderNode = new RenderNode();
7. renderNode.frame = {
8. x: 0,
9. y: 0,
10. width: 150,
11. height: 150
12. };
13. renderNode.backgroundColor = 0XFF00FF00;
14. renderNode.shapeClip = clip;

16. class MyNodeController extends NodeController {
17. private rootNode: FrameNode | null = null;

19. makeNode(uiContext: UIContext): FrameNode | null {
20. this.rootNode = new FrameNode(uiContext);

22. const rootRenderNode = this.rootNode.getRenderNode();
23. if (rootRenderNode !== null) {
24. rootRenderNode.appendChild(renderNode);
25. }

27. return this.rootNode;
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. private myNodeController: MyNodeController = new MyNodeController();

36. build() {
37. Column() {
38. NodeContainer(this.myNodeController)
39. .borderWidth(1)
40. Button("setCircleShape")
41. .onClick(() => {
42. renderNode.shapeClip.setCircleShape({ centerY: 75, centerX: 75, radius: 75 });

44. })
45. }
46. }
47. }
```

### setOvalShape12+

PhonePC/2in1TabletTVWearable

setOvalShape(oval: Rect): void

用于裁剪椭圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oval | [Rect](js-apis-arkui-graphics.md#rect12) | 是 | 椭圆形的形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

3. const clip = new ShapeClip();
4. clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

6. const renderNode = new RenderNode();
7. renderNode.frame = {
8. x: 0,
9. y: 0,
10. width: 150,
11. height: 150
12. };
13. renderNode.backgroundColor = 0XFF00FF00;
14. renderNode.shapeClip = clip;

16. class MyNodeController extends NodeController {
17. private rootNode: FrameNode | null = null;

19. makeNode(uiContext: UIContext): FrameNode | null {
20. this.rootNode = new FrameNode(uiContext);

22. const rootRenderNode = this.rootNode.getRenderNode();
23. if (rootRenderNode !== null) {
24. rootRenderNode.appendChild(renderNode);
25. }

27. return this.rootNode;
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. private myNodeController: MyNodeController = new MyNodeController();

36. build() {
37. Column() {
38. NodeContainer(this.myNodeController)
39. .borderWidth(1)
40. Button("setOvalShape")
41. .onClick(() => {
42. renderNode.shapeClip.setOvalShape({
43. left: 0,
44. right: this.getUIContext().vp2px(150),
45. top: 0,
46. bottom: this.getUIContext().vp2px(100)
47. });
48. })
49. }
50. }
51. }
```

### setCommandPath12+

PhonePC/2in1TabletTVWearable

setCommandPath(path: CommandPath): void

用于裁剪路径绘制指令。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [CommandPath](js-apis-arkui-graphics.md#commandpath12) | 是 | 路径绘制指令。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

3. const clip = new ShapeClip();
4. clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

6. const renderNode = new RenderNode();
7. renderNode.frame = {
8. x: 0,
9. y: 0,
10. width: 150,
11. height: 150
12. };
13. renderNode.backgroundColor = 0XFF00FF00;
14. renderNode.shapeClip = clip;

16. class MyNodeController extends NodeController {
17. private rootNode: FrameNode | null = null;

19. makeNode(uiContext: UIContext): FrameNode | null {
20. this.rootNode = new FrameNode(uiContext);

22. const rootRenderNode = this.rootNode.getRenderNode();
23. if (rootRenderNode !== null) {
24. rootRenderNode.appendChild(renderNode);
25. }

27. return this.rootNode;
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. private myNodeController: MyNodeController = new MyNodeController();

36. build() {
37. Column() {
38. NodeContainer(this.myNodeController)
39. .borderWidth(1)
40. Button("setCommandPath")
41. .onClick(() => {
42. renderNode.shapeClip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });
43. })
44. }
45. }
46. }
```

## edgeColors12+

PhonePC/2in1TabletTVWearable

edgeColors(all: number): Edges<number>

用于生成边框颜色均设置为传入值的边框颜色对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| all | number | 是 | 边框颜色，ARGB格式，示例：0xffff00ff。  取值范围：[0, 0xffffffff] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<number> | 边框颜色均设置为传入值的边框颜色对象。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, edgeColors } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
5. renderNode.backgroundColor = 0xffd5d5d5;
6. renderNode.borderWidth = { left: 8, top: 8, right: 8, bottom: 8 };
7. renderNode.borderColor = edgeColors(0xff519db4);

10. class MyNodeController extends NodeController {
11. private rootNode: FrameNode | null = null;

13. makeNode(uiContext: UIContext): FrameNode | null {
14. this.rootNode = new FrameNode(uiContext);

16. const rootRenderNode = this.rootNode.getRenderNode();
17. if (rootRenderNode !== null) {
18. rootRenderNode.appendChild(renderNode);
19. }

21. return this.rootNode;
22. }
23. }

25. @Entry
26. @Component
27. struct Index {
28. private myNodeController: MyNodeController = new MyNodeController();

30. build() {
31. Row() {
32. NodeContainer(this.myNodeController)
33. }.margin(30)
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/puY5ZejSR92lcHLrz9ilXA/zh-cn_image_0000002589325843.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=ADD759D7ED50F3CDEED8643229A4A5EDFA6A0AC3E4A5C6C95AA49A3E3DE24E2D)

## edgeWidths12+

PhonePC/2in1TabletTVWearable

edgeWidths(all: number): Edges<number>

用于生成边框宽度均设置为传入值的边框宽度对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| all | number | 是 | 边框宽度，单位为vp。  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<number> | 边框宽度均设置为传入值的边框宽度对象。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, edgeWidths } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 150,
8. height: 150
9. };
10. renderNode.backgroundColor = 0xffd5d5d5;
11. renderNode.borderWidth = edgeWidths(8);
12. renderNode.borderColor = {
13. left: 0xff519db4,
14. top: 0xff519db4,
15. right: 0xff519db4,
16. bottom: 0xff519db4
17. };

20. class MyNodeController extends NodeController {
21. private rootNode: FrameNode | null = null;

23. makeNode(uiContext: UIContext): FrameNode | null {
24. this.rootNode = new FrameNode(uiContext);

26. const rootRenderNode = this.rootNode.getRenderNode();
27. if (rootRenderNode !== null) {
28. rootRenderNode.appendChild(renderNode);
29. }

31. return this.rootNode;
32. }
33. }

35. @Entry
36. @Component
37. struct Index {
38. private myNodeController: MyNodeController = new MyNodeController();

40. build() {
41. Row() {
42. NodeContainer(this.myNodeController)
43. }.margin(30)
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/rN2nxdvUQMuuwXmr2JlRMA/zh-cn_image_0000002589245785.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=932DD6F780404706B0A440FCFA53B164FF957DD24AEC93FE179A501387F0D82C)

## borderStyles12+

PhonePC/2in1TabletTVWearable

borderStyles(all: BorderStyle): Edges<BorderStyle>

用于生成边框样式均设置为传入值的边框样式对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| all | [BorderStyle](ts-appendix-enums.md#borderstyle) | 是 | 边框样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[BorderStyle](ts-appendix-enums.md#borderstyle)> | 边框样式均设置为传入值的边框样式对象。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, borderStyles } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 150,
8. height: 150
9. };
10. renderNode.backgroundColor = 0xffd5d5d5;
11. renderNode.borderWidth = {
12. left: 8,
13. top: 8,
14. right: 8,
15. bottom: 8
16. };
17. renderNode.borderColor = {
18. left: 0xff519db4,
19. top: 0xff519db4,
20. right: 0xff519db4,
21. bottom: 0xff519db4
22. };
23. renderNode.borderStyle = borderStyles(BorderStyle.Dotted);

26. class MyNodeController extends NodeController {
27. private rootNode: FrameNode | null = null;

29. makeNode(uiContext: UIContext): FrameNode | null {
30. this.rootNode = new FrameNode(uiContext);

32. const rootRenderNode = this.rootNode.getRenderNode();
33. if (rootRenderNode !== null) {
34. rootRenderNode.appendChild(renderNode);
35. }

37. return this.rootNode;
38. }
39. }

41. @Entry
42. @Component
43. struct Index {
44. private myNodeController: MyNodeController = new MyNodeController();

46. build() {
47. Row() {
48. NodeContainer(this.myNodeController)
49. }.margin(30)
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Ybd1j07RTb23FLter2zZOg/zh-cn_image_0000002558765974.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=9BE7F97D8C2C97BCCB1966AE35E434CC22267164ECA4ADAB590325C9481E709B)

## borderRadiuses12+

PhonePC/2in1TabletTVWearable

borderRadiuses(all: number): BorderRadiuses

用于生成边框圆角均设置为传入值的边框圆角对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| all | number | 是 | 边框圆角。  单位：vp  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BorderRadiuses](js-apis-arkui-graphics.md#borderradiuses12) | 边框圆角均设置为传入值的边框圆角对象。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, borderRadiuses } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 150,
8. height: 150
9. };
10. renderNode.backgroundColor = 0xff519db4;
11. renderNode.borderRadius = borderRadiuses(32);

14. class MyNodeController extends NodeController {
15. private rootNode: FrameNode | null = null;

17. makeNode(uiContext: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(uiContext);

20. const rootRenderNode = this.rootNode.getRenderNode();
21. if (rootRenderNode !== null) {
22. rootRenderNode.appendChild(renderNode);
23. }

25. return this.rootNode;
26. }
27. }

29. @Entry
30. @Component
31. struct Index {
32. private myNodeController: MyNodeController = new MyNodeController();

34. build() {
35. Row() {
36. NodeContainer(this.myNodeController)
37. }.margin(20)
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/GevMDGoWQh-1SRn_V_Fyew/zh-cn_image_0000002558606318.png?HW-CC-KV=V1&HW-CC-Date=20260429T055046Z&HW-CC-Expire=86400&HW-CC-Sign=4B27CBE0A42852B8C73DAA8FDD51A3184DC115200B53437615A967757D0F0B54)
