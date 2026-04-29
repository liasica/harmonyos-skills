---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d
title: Path2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > Path2D对象
category: harmonyos-references
scraped_at: 2026-04-29T13:53:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4e834700ef716867e451719bdf03d32195711067f5c645ca6a0d1a69de4480ea
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/tlEWxyPcRn-Djvza4kAaYg/zh-cn_image_0000002558766758.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=D8F27FF7E97C416346E4128733A9BD09532B8811F997EEDAEFFCF84718233DA6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/i3Q_SpGTRVif3j2aKeVQzg/zh-cn_image_0000002558607098.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=3C208BB014713134E43C717AD65B4D527482BC7D900794EF46D06E551AF253E1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/4V2TcH6QQnaPF3cGf7Qx3g/zh-cn_image_0000002589326625.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=35A42B1C792136BA34B4AA8214A4CB56A0CA4D5400809DF78733266F5499E6D1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/kXFfBABdSVGJDDrngfoqhg/zh-cn_image_0000002589246567.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=CE64A6AB6EB45BEC461CC9BFFEE3A841C123AD1E20FB6FA45319DBF5881B2C79)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/NH04Ro0ATgiClHYiUoqZsw/zh-cn_image_0000002558766760.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=501B58CF35D63A0AB385590E01DE05D954D91E7152A3E745B6AB75E5B8D69F8F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/CR1JuAhXTTSECO_o0N3uIw/zh-cn_image_0000002558607100.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=E364BDDC9C69B5789FCBE88DB267824B4CEC2CC5EC836630D384A1C489683295)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/WJpoC9neSaGt7onRWEJB4A/zh-cn_image_0000002589326627.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=4B8866C02F9FEB9807755D586AD6B4A863ED6868BDED287CAC5C2B54ED85B764)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5R9J9EuqQjGEnLeS7CJmNQ/zh-cn_image_0000002589246569.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=7ECD8BBF339C2967580D2D93F1D37F2C7F98C313693BEAF728A0C419CCA2F102)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/wS6aB0INRq2yQ3IncNs0qg/zh-cn_image_0000002558766762.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=9513355F990E33AF727FF04017F19F0ED4014E1DDFCBD6228A9F12CCE397034F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/IcYApuzYT8muUB4nP0TJ_g/zh-cn_image_0000002558607102.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=FB8E61DE335A58ADDBB5D781519E09B6D2CE266384A11BE62D2215D21304E878)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/OlGhkv4-TSW-J5vADUuZOg/zh-cn_image_0000002589326629.png?HW-CC-KV=V1&HW-CC-Date=20260429T055333Z&HW-CC-Expire=86400&HW-CC-Sign=023FC9A503C20C7BC7E30958B184B97CF98E314DA4E035BC92F6201BD5BD8E5D)
