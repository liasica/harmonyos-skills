---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d
title: Path2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > Path2D对象
category: harmonyos-references
scraped_at: 2026-04-28T08:03:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d0ffab96e0dca15ef18fad8c515724a35d3f97a1221a3eb4e7213d1113de2769
---

路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的[stroke](js-components-canvas-canvasrenderingcontext2d.md#stroke)接口进行绘制。

说明

本模块首批接口从API version 4开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## addPath

PhonePC/2in1TabletTVWearable

addPath(path: Object): void

将另一个路径添加到当前的路径对象中。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| path | Object | 需要添加到当前路径的路径对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path1 = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
7. var path2 = ctx.createPath2D();
8. path2.addPath(path1);
9. ctx.stroke(path2);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/bYDVe1IaRRyNS7olGFX3BA/zh-cn_image_0000002583440277.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=0BF5689A7581E0179E01DAEA8425DFA2A02D240217EAC8769B9035A3ABE9F9A6)

## setTransform

PhonePC/2in1TabletTVWearable

setTransform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

设置路径变换矩阵。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| scaleX | number | x轴的缩放比例。 |
| skewX | number | x轴的倾斜角度。 |
| skewY | number | y轴的倾斜角度。 |
| scaleY | number | y轴的缩放比例。 |
| translateX | number | x轴的平移距离。 |
| translateY | number | y轴的平移距离。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
7. path.setTransform(0.8, 0, 0, 0.4, 0, 0);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/RI4WoV2kTa6-eJqNvia_YA/zh-cn_image_0000002552960232.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=1E24A0F71BEB5F131FBD4BE9098EEE1B8EB12923ED51C080E6C4959BA7199164)

## closePath

PhonePC/2in1TabletTVWearable

closePath(): void

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(200, 100);
8. path.lineTo(300, 100);
9. path.lineTo(200, 200);
10. path.closePath();
11. ctx.stroke(path);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/XNSn56IlRACPF07Xmliz8A/zh-cn_image_0000002583480233.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=34F7C304A902BB6350BEA94CEDEF314C4FE96443A5F213CC49332C609AA97269)

## moveTo

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(50, 100);
8. path.lineTo(250, 100);
9. path.lineTo(150, 200);
10. path.closePath();
11. ctx.stroke(path);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/fn0FGzQ4REmI7vBQTvZqtQ/zh-cn_image_0000002552800584.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=649520200CCB06E554E4DA56EE89C6A99029032B1CE350A4247688E3F1DB8309)

## lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点绘制一条直线到目标点。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 400px; height: 450px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(100, 100);
8. path.lineTo(100, 200);
9. path.lineTo(200, 200);
10. path.lineTo(200, 100);
11. path.closePath();
12. ctx.stroke(path);
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Yt3VV3cTSY6i-VGuYSzemw/zh-cn_image_0000002583440279.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=4A745F98FA8C0335479E7EA7F58AD4F61F3A69FE6E6B3E6CD929E5FDACC1D6BA)

## bezierCurveTo

PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cp1x | number | 第一个贝塞尔参数的x坐标值。 |
| cp1y | number | 第一个贝塞尔参数的y坐标值。 |
| cp2x | number | 第二个贝塞尔参数的x坐标值。 |
| cp2y | number | 第二个贝塞尔参数的y坐标值。 |
| x | number | 路径结束时的x坐标值。 |
| y | number | 路径结束时的y坐标值。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(10, 10);
8. path.bezierCurveTo(20, 100, 200, 100, 200, 20);
9. ctx.stroke(path);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/GBQzSRjHSc-C2PcpVHthQg/zh-cn_image_0000002552960234.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=52F5EF433E6206F84BAF2791BD071D3A7348C9FA29E98FA303CD9FE228916937)

## quadraticCurveTo

PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cpx | number | 贝塞尔参数的x坐标值。 |
| cpy | number | 贝塞尔参数的y坐标值。 |
| x | number | 路径结束时的x坐标值。 |
| y | number | 路径结束时的y坐标值。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.moveTo(10, 10);
8. path.quadraticCurveTo(100, 100, 200, 20);
9. ctx.stroke(path);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/baXauVQQRLyJNkGwV41oxw/zh-cn_image_0000002583480235.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=92859829B6694BB6D17C0EDA0D1CE7AE622157C9656E7259C71E0A1A496ED67B)

## arc

PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。 |
| y | number | 是 | 弧线圆心的y坐标值。 |
| radius | number | 是 | 弧线的圆半径。 |
| startAngle | number | 是 | 弧线的起始弧度。 |
| endAngle | number | 是 | 弧线的终止弧度。 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧，true为逆时针，false为顺时针。  默认值：false |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.arc(100, 75, 50, 0, 6.28);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Pll-vnsPRu-L6RZsBqdg8w/zh-cn_image_0000002552800586.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=338AC9ADC71DAAD4D82D74FF96E8625B381815B6419A4B275A68A2D226FD36C6)

## arcTo

PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x1 | number | 圆弧经过的第一个点的x坐标值。 |
| y1 | number | 圆弧经过的第一个点的y坐标值。 |
| x2 | number | 圆弧经过的第二个点的x坐标值。 |
| y2 | number | 圆弧经过的第二个点的y坐标值。 |
| radius | number | 圆弧的圆半径值。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.arcTo(150, 20, 150, 70, 50);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/MwPAW3c9QSqDQ1bmlsXNjg/zh-cn_image_0000002583440281.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=A9819C452E2E98E0376A669ACF03AF81BFFBEFA85CAF667D7E02F2C3050D722B)

## ellipse

PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。 |
| y | number | 是 | 椭圆圆心的y轴坐标。 |
| radiusX | number | 是 | 椭圆x轴的半径长度。 |
| radiusY | number | 是 | 椭圆y轴的半径长度。 |
| rotation | number | 是 | 椭圆的旋转角度，单位为弧度。 |
| startAngle | number | 是 | 椭圆绘制的起始点角度，以弧度表示。 |
| endAngle | number | 是 | 椭圆绘制的结束点角度，以弧度表示。 |
| counterclockwise | number | 否 | 是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。  默认值：0 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/D66viuE5QZmCqVTlbnIvGw/zh-cn_image_0000002552960236.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=198A0567A60ADF5CDFB960D0B53B53B1BD2B7D1928B2E214356F47FAD00389F4)

## rect

PhonePC/2in1TabletTVWearable

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形的左上角x坐标值。 |
| y | number | 指定矩形的左上角y坐标值。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path = ctx.createPath2D();
7. path.rect(20, 20, 100, 100);
8. ctx.stroke(path);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/64n48_sPQQOfGEmOB9qmJg/zh-cn_image_0000002583480237.png?HW-CC-KV=V1&HW-CC-Date=20260428T000311Z&HW-CC-Expire=86400&HW-CC-Sign=3A14D5055E7FADCFAED63ECBC0FE78263203CB299F2549FE210B43141AF44B9E)
