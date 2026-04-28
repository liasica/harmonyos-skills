---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d
title: Path2D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > Path2D
category: harmonyos-references
scraped_at: 2026-04-28T08:02:11+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:0d3b7d17acb5ae6fd4de36569eff4ef9ba49171a29476d0d7235a8d6e7b61d83
---

路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。

说明

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

Path2D对象不支持重置已设置的路径，如需新路径可重新创建一个空的Path2D对象。

Path2D对象的方法无法对[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)和[OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md)对象中设置的路径生效。

## 构造函数

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor()

构造一个空的Path2D对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(unit: LengthMetricsUnit)

构造一个空的Path2D对象，支持配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值NaN和Infinity按默认值处理。  默认值：DEFAULT |

### constructor

PhonePC/2in1TabletTVWearable

constructor(path: Path2D)

使用路径对象构造Path2D对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | 路径对象。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(path: Path2D, unit: LengthMetricsUnit)

使用路径对象构造Path2D对象，支持配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | 路径对象。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值NaN和Infinity按默认值处理。  默认值：DEFAULT |

### constructor

PhonePC/2in1TabletTVWearable

constructor(d: string)

使用符合SVG路径描述规范的路径字符串构造Path2D对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | string | 是 | 符合SVG路径描述规范的路径字符串，格式参考[SVG路径描述规范](ts-drawing-components-path.md#svg路径描述规范)，异常值按无效值处理。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(description: string, unit: LengthMetricsUnit)

使用符合SVG路径描述规范的路径字符串构造Path2D对象，支持配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| description | string | 是 | 符合SVG路径描述规范的路径字符串，格式参考[SVG路径描述规范](ts-drawing-components-path.md#svg路径描述规范)，异常值按无效值处理。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值NaN和Infinity按默认值处理。  默认值：DEFAULT |

## 方法

PhonePC/2in1TabletTVWearable

### addPath

PhonePC/2in1TabletTVWearable

addPath(path: Path2D, transform?: Matrix2D): void

将另一个路径添加到当前的路径对象中，并使用Matrix2D对象对新添加的路径对象进行图形变换。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | 需要添加到当前路径的路径对象，路径单位：px。  异常值undefined和null按无效值处理。 |
| transform | [Matrix2D](ts-components-canvas-matrix2d.md) | 否 | 新增路径的变换矩阵对象。  异常值undefined和null按无效值处理。  默认值：null |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AddPath {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Da: Path2D = new Path2D("M250 150 L150 350 L350 350 Z");
8. private path2Db: Path2D = new Path2D();

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. this.path2Db.addPath(this.path2Da)
18. this.context.stroke(this.path2Db)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/lz3uVAEnRI693y1YvxI0_g/zh-cn_image_0000002583479999.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=8F882CE25BB962CEB4212CE014B70DC1579E25A20ECB34FD8106BAB719CA1BC8)

### closePath

PhonePC/2in1TabletTVWearable

closePath(): void

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClosePath {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.moveTo(200, 100)
17. this.path2Db.lineTo(300, 100)
18. this.path2Db.lineTo(200, 200)
19. this.path2Db.closePath()
20. this.context.stroke(this.path2Db)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ReIKdelXTJWLx4HVs3Tw9g/zh-cn_image_0000002552800350.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=680D463B573C5A4AAE31B0AB1712446C567A20C809ABB621588FC9B2A736A614)

### moveTo

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 目标点X轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 目标点Y轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

说明

* API version 18之前，若未设置moveTo接口或moveTo接口传入无效参数，路径以(0, 0)为起点。
* API version 18及以后，若未设置moveTo接口或moveTo接口传入无效参数，路径以初次调用的lineTo、arcTo、bezierCurveTo或quadraticCurveTo接口中的起始点为起点。

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MoveTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.moveTo(50, 100)
17. this.path2Db.lineTo(250, 100)
18. this.path2Db.lineTo(150, 200)
19. this.path2Db.closePath()
20. this.context.stroke(this.path2Db)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/zISaQw0jQaCHd-rpTFxq9Q/zh-cn_image_0000002583440045.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=48FDC716D1729DEA0C30443F17F3010917B47AF054872723541394D3E898A6A6)

### lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点绘制一条直线到目标点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 目标点X轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 目标点Y轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.moveTo(100, 100)
17. this.path2Db.lineTo(100, 200)
18. this.path2Db.lineTo(200, 200)
19. this.path2Db.lineTo(200, 100)
20. this.path2Db.closePath()
21. this.context.stroke(this.path2Db)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/E_bhqMmCTvW2dzZXd9y_sg/zh-cn_image_0000002552960000.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=B1CCAF1E376D3FF17C5E47E38E83E0F8F1154D3E83236494925FE4BB8B6474D3)

### bezierCurveTo

PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BezierCurveTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.moveTo(10, 10)
17. this.path2Db.bezierCurveTo(20, 100, 200, 100, 200, 20)
18. this.context.stroke(this.path2Db)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/DmqWwErQQ06R7iSV_lTlDw/zh-cn_image_0000002583480001.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=6AF09EA884D9E26AFD62CA268388B1C3CE6AD6BBB2D9A374AD6566A412435949)

### quadraticCurveTo

PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct QuadraticCurveTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.moveTo(10, 10)
17. this.path2Db.quadraticCurveTo(100, 100, 200, 20)
18. this.context.stroke(this.path2Db)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/T6_ozKEQQ-KECIiQnRV8NA/zh-cn_image_0000002552800352.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=EDEA4E3341B404EF062C9A9E58596C67D6469565CAC8556AAB4AB351870C6946)

### arc

PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radius | number | 是 | 弧线的圆半径。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度。 |
| endAngle | number | 是 | 弧线的终止弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度。 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧。  true：逆时针方向绘制圆弧。  false：顺时针方向绘制圆弧。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Arc {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.arc(100, 75, 50, 0, 6.28)
17. this.context.stroke(this.path2Db)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/v0676qZlQFu25XpO9CnefA/zh-cn_image_0000002583440047.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=A42728E93368B5958969235FDB23A1BCDE87E74BD637B76E054A4E64F6931E86)

### arcTo

PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 圆弧经过的第一个点的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y1 | number | 是 | 圆弧经过的第一个点的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x2 | number | 是 | 圆弧经过的第二个点的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y2 | number | 是 | 圆弧经过的第二个点的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radius | number | 是 | 圆弧的圆半径值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ArcTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.moveTo(0, 0)
17. this.path2Db.arcTo(150, 20, 150, 70, 50)
18. this.context.stroke(this.path2Db)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/PEIAcs2nTgGVSZaA7c_CPQ/zh-cn_image_0000002552960002.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=0F8BE0F584796216D3D8D07D646278AD44A4522FBAFB74A1B4C68AE35CCEB7F3)

### ellipse

PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

在规定的矩形区域绘制一个椭圆。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| rotation | number | 是 | 椭圆的旋转角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| counterclockwise | boolean | 否 | 是否以逆时针方向绘制椭圆。  true：逆时针方向绘制椭圆。  false：顺时针方向绘制椭圆。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.ellipse(200, 200, 50, 100, 0, Math.PI * 1, Math.PI * 2)
17. this.context.stroke(this.path2Db)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/f6jk6C2MSLWQBX8s-khrTg/zh-cn_image_0000002583480003.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=E1150D588049FA7BD95AB4BE10B3CB1B8C8FD80A6F546A660DDC104995EF10EC)

### rect

PhonePC/2in1TabletTVWearable

rect(x: number, y: number, w: number, h: number): void

创建矩形路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| h | number | 是 | 指定矩形的高度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private path2Db: Path2D = new Path2D();

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Db.rect(20, 20, 100, 100);
17. this.context.stroke(this.path2Db)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/pyMO0ti8RwqmSvY1KJh_aA/zh-cn_image_0000002552800354.png?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=51FBFA38152CA5F9877138A58905F5B862AA3F097881ED843879CD686C9770B4)

### roundRect20+

PhonePC/2in1TabletTVWearable

roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void

创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[0, Canvas宽度)。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[0, Canvas高度)。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度，设置负值为向左绘制。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[-x, Canvas宽度 - x]。  默认单位：vp |
| h | number | 是 | 指定矩形的高度，设置负值为向上绘制。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[-y, Canvas高度 - y]。  默认单位：vp |
| radii | number | Array<number> | 否 | 指定用于矩形角的圆弧半径的数字或列表。  参数类型为number时，所有矩形角的圆弧半径按该数字设置。  参数类型为Array<number>时，数目为1-4个按下面设置：  [所有矩形角的圆弧半径]  [左上及右下矩形角的圆弧半径, 右上及左下矩形角的圆弧半径]  [左上矩形角的圆弧半径, 右上及左下矩形角的圆弧半径, 右下矩形角的圆弧半径]  [左上矩形角的圆弧半径, 右上矩形角的圆弧半径, 右下矩形角的圆弧半径, 左下矩形角的圆弧半径]  radii存在负数或列表的数目不在[1,4]内时抛出异常，错误码：103701。  默认值：0，null和undefined按默认值处理。  圆弧半径超过矩形宽高时会等比例缩放到宽高的长度。  默认单位：vp |

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](errorcode-canvas.md)。

| 错误码ID | 错误信息 | 可能原因 |
| --- | --- | --- |
| 103701 | Parameter error. | 1. The param radii is a list that has zero or more than four elements; 2. The param radii contains negative value. |

**示例：**

该示例展示了绘制六个圆角矩形：

1. 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
2. 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
3. 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形并描边；
4. 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形并描边；
5. 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边；
6. 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct CanvasExample {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private pathA: Path2D = new Path2D();
10. private pathB: Path2D = new Path2D();

12. build() {
13. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
14. Canvas(this.context)
15. .width('100%')
16. .height('100%')
17. .backgroundColor('#D5D5D5')
18. .onReady(() => {
19. try {
20. this.context.fillStyle = '#707070'
21. // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
22. this.pathA.roundRect(10, 10, 100, 100, 10)
23. // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
24. this.pathA.roundRect(120, 10, 100, 100, [10])
25. this.context.fill(this.pathA)
26. // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
27. this.pathB.roundRect(10, 120, 100, 100, [10, 20])
28. // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
29. this.pathB.roundRect(120, 120, 100, 100, [10, 20, 30])
30. // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
31. this.pathB.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
32. // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
33. this.pathB.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
34. this.context.stroke(this.pathB)
35. } catch (error) {
36. let e: BusinessError = error as BusinessError;
37. console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
38. }
39. })
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/4pXUqgzGR-GJXvHYfYvjFQ/zh-cn_image_0000002552800302.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000207Z&HW-CC-Expire=86400&HW-CC-Sign=6B90C3A3CCB8D0D22687F87A4FEFED1EA011DFF5128732F17BD9727FF25DFBD8)
