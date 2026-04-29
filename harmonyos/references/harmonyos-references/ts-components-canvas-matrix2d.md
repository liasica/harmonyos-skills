---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-matrix2d
title: Matrix2D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > Matrix2D
category: harmonyos-references
scraped_at: 2026-04-29T13:52:35+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:7d2b4bf497e882dffc2694a0d09bccc2b882deed9f2c5176ef706cbaac5efdfb
---

用于画布绘制[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)、[OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md)、[CanvasPattern](ts-components-canvas-canvaspattern.md)和[Path2D](ts-components-canvas-path2d.md)的矩阵对象，可以对矩阵进行缩放、旋转和平移等变换。

Matrix2D的使用场景包括：

1. [CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)和[OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md)中调用[getTransform](ts-canvasrenderingcontext2d.md#gettransform)接口获取画布的图形变换矩阵Matrix2D对象，调用[setTransform](ts-canvasrenderingcontext2d.md#settransform-1)接口对后续绘制内容进行Matrix2D对象对应的图形变换。
2. [CanvasPattern](ts-components-canvas-canvaspattern.md)中调用[setTransform](ts-components-canvas-canvaspattern.md#settransform)接口对[CanvasPattern](ts-components-canvas-canvaspattern.md)对象进行Matrix2D对象对应的图形变换。
3. [Path2D](ts-components-canvas-path2d.md)中调用[addPath](ts-components-canvas-path2d.md#addpath)接口对[Path2D](ts-components-canvas-path2d.md)对象进行Matrix2D对象对应的图形变换。

说明

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 构造函数

PhonePC/2in1TabletTVWearable

### constructor10+

PhonePC/2in1TabletTVWearable

constructor()

构造二维变换矩阵对象，默认值是属性全为0的矩阵。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(unit: LengthMetricsUnit)

构造二维变换矩阵对象，默认值是属性全为0的矩阵，支持配置Matrix2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置Matrix2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值NaN和Infinity按默认值处理。  默认值：DEFAULT |

## 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scaleX | number | 否 | 是 | 水平缩放系数，取值范围无限制。  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| scaleY | number | 否 | 是 | 垂直缩放系数，取值范围无限制。  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| rotateX | number | 否 | 是 | 水平倾斜系数，取值范围无限制。  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| rotateY | number | 否 | 是 | 垂直倾斜系数，取值范围无限制。  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| translateX | number | 否 | 是 | 水平平移距离，取值范围无限制。  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。  默认单位：vp |
| translateY | number | 否 | 是 | 垂直平移距离，取值范围无限制。  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。  默认单位：vp |

说明

可使用[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)接口进行单位转换。

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Parameter {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('240vp')
13. .height('180vp')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.context.fillRect(100, 20, 50, 50)
17. this.matrix.scaleX = 1
18. this.matrix.scaleY = 1
19. this.matrix.rotateX = -0.5
20. this.matrix.rotateY = 0.5
21. this.matrix.translateX = 10
22. this.matrix.translateY = 10
23. this.context.setTransform(this.matrix)
24. this.context.fillRect(100, 20, 50, 50)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/nS2y1MlpQjGhVw6X-ljPSA/zh-cn_image_0000002558766496.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=4AB2440234BBCB38E9FE8CBD0E23608B82B2EB73FC080CAC50B527B6648982CD)

## 方法

PhonePC/2in1TabletTVWearable

### identity

PhonePC/2in1TabletTVWearable

identity(): Matrix2D

创建单位矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 单位矩阵。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Identity {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('240vp')
13. .height('180vp')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.context.fillRect(100, 20, 50, 50)
17. this.matrix = this.matrix.identity()
18. this.context.setTransform(this.matrix)
19. this.context.fillRect(100, 100, 50, 50)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/HCfmAjy2QGioFL-5OQq9sw/zh-cn_image_0000002558606836.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=4F27582F5F10622203A03CD5BCFEBEEC178D58CEE15CA925C620D2ABF1B7402A)

### invert

PhonePC/2in1TabletTVWearable

invert(): Matrix2D

获取当前矩阵的逆矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 逆矩阵结果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Invert {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('240vp')
13. .height('180vp')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.context.fillRect(100, 110, 50, 50)
17. this.matrix.scaleX = 1
18. this.matrix.scaleY = 1
19. this.matrix.rotateX = -0.5
20. this.matrix.rotateY = 0.5
21. this.matrix.translateX = 10
22. this.matrix.translateY = 10
23. this.matrix.invert()
24. this.context.setTransform(this.matrix)
25. this.context.fillRect(100, 110, 50, 50)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/eBwh8-zVRrO5nH7XYqlcWA/zh-cn_image_0000002589326363.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=C7D992ED6E8BC5A1D18EA1DC000B7041D4871655D3D8ACD19AE9F580B923DC70)

### multiply(deprecated)

multiply(other?: Matrix2D): Matrix2D

当前矩阵与目标矩阵相乘。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。

该接口从API version 10开始废弃，且无实际绘制效果，故不提供示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Matrix2D | 否 | 目标矩阵。  异常值undefined和null按无效值处理。  默认值：null |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 相乘结果矩阵。 |

### rotate(deprecated)

rotate(rx?: number, ry?: number): Matrix2D

对当前矩阵进行旋转运算。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。

该接口从API version 10开始废弃，推荐使用[rotate](ts-components-canvas-matrix2d.md#rotate10)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：vp |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Rotate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('240vp')
13. .height('180vp')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.context.fillRect(50, 110, 50, 50)
17. this.matrix.scaleX = 1
18. this.matrix.scaleY = 1
19. this.matrix.rotateX = -0.5
20. this.matrix.rotateY = 0.5
21. this.matrix.translateX = 10
22. this.matrix.translateY = 10
23. this.matrix.rotate(5, 5)
24. this.context.setTransform(this.matrix)
25. this.context.fillRect(50, 110, 50, 50)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/EN6lI16fQ_61eLCYUGv8pQ/zh-cn_image_0000002589246305.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=18EB86DDEE5A54096A127E67BC934B7E202F71626C1CE5F279686000980904E6)

### rotate10+

PhonePC/2in1TabletTVWearable

rotate(degree: number, rx?: number, ry?: number): Matrix2D

以旋转点为中心，对当前矩阵进行右乘旋转运算。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | number | 是 | 旋转角度，取值范围无限制。顺时针方向为正角度，可以通过 degree \* Math.PI / 180 将角度转换为弧度值。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：弧度 |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。  默认单位：vp  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：0 |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。  默认单位：vp  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Rotate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('240vp')
13. .height('180vp')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.context.fillRect(60, 80, 50, 50)
17. this.matrix.scaleX = 1
18. this.matrix.scaleY = 1
19. this.matrix.rotateX = -0.5
20. this.matrix.rotateY = 0.5
21. this.matrix.translateX = 10
22. this.matrix.translateY = 10
23. this.matrix.rotate(-60 * Math.PI / 180, 5, 5)
24. this.context.setTransform(this.matrix)
25. this.context.fillRect(60, 80, 50, 50)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/FsrccqgCQFGOWNbEhXq7FQ/zh-cn_image_0000002558766498.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=366AB90FB9400C0AE5F5AC6C7BA4EE3FB67284BAFE586326B35E7BEEA9B603AD)

### translate

PhonePC/2in1TabletTVWearable

translate(tx?: number, ty?: number): Matrix2D

对当前矩阵进行左乘平移运算。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tx | number | 否 | 水平方向平移距离，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：vp  默认值：0 |
| ty | number | 否 | 垂直方向平移距离，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：vp  默认值：0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 平移后结果矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Translate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('240vp')
13. .height('180vp')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.context.fillRect(40, 20, 50, 50)
17. this.matrix.scaleX = 1
18. this.matrix.scaleY = 1
19. this.matrix.rotateX = 0
20. this.matrix.rotateY = 0
21. this.matrix.translateX = 0
22. this.matrix.translateY = 0
23. this.matrix.translate(100, 100)
24. this.context.setTransform(this.matrix)
25. this.context.fillRect(40, 20, 50, 50)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/DU6cjY-ATyah34LhLdvfrw/zh-cn_image_0000002558606838.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=5B0C67EE4DC8A66E22B33A4E1325DD3DE8648A620F070DC4022E32CE63A95E92)

### scale

PhonePC/2in1TabletTVWearable

scale(sx?: number, sy?: number): Matrix2D

对当前矩阵进行右乘缩放运算。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| sx | number | 否 | 水平缩放比例系数，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：1.0 |
| sy | number | 否 | 垂直缩放比例系数，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：1.0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 缩放结果矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Scale {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('240vp')
13. .height('180vp')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.context.fillRect(120, 70, 50, 50)
17. this.matrix.scaleX = 1
18. this.matrix.scaleY = 1
19. this.matrix.rotateX = -0.5
20. this.matrix.rotateY = 0.5
21. this.matrix.translateX = 10
22. this.matrix.translateY = 10
23. this.matrix.scale(0.5, 0.5)
24. this.context.setTransform(this.matrix)
25. this.context.fillRect(120, 70, 50, 50)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/kv-djepkQ5ipnvViYIATXw/zh-cn_image_0000002589326365.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=4F93C1682D7FE693886A373C43B978FD8E0A61598846610D296452D7DFF2E640)
