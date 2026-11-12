---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d
title: Path2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > Path2D对象
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d25d81d2d0d589cf1fe3385ce00e3dd1a9e4560695988ed0d7f8e63d37c965be
---

路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的[stroke](js-components-canvas-canvasrenderingcontext2d.md#stroke)接口进行绘制。

**说明** 

本模块首批接口从API version 4开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## addPath

addPath(path: Path2D): void

将另一个路径添加到当前的路径对象中。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| path | Path2D | 需要添加到当前路径的路径对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path1 = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
    var path2 = ctx.createPath2D();
    path2.addPath(path1);
    ctx.stroke(path2);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/peO23eWEQiGXfub7JY_NLQ/zh-cn_image_0000002786521720.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1C5D25E53AF9AD9C3C7E04222EE24E4F80553641F5C6D5F4A398A48EFFF7622)

## setTransform

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

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
    path.setTransform(0.8, 0, 0, 0.4, 0, 0);
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/KkIDq08TTJGFuClz7v6JfA/zh-cn_image_0000002786361792.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=61ADCAB85DB5200CE194D33B9CFA2EB0B12A956D1CF383FC14182069DC2E9FE8)

## closePath

closePath(): void

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**示例：**

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(200, 100);
    path.lineTo(300, 100);
    path.lineTo(200, 200);
    path.closePath();
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/fO8qDYx0TqKdwI5RO-T69A/zh-cn_image_0000002815561213.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA5AA7FC2E5B3404F531A415F376950438E716C87AA4863982866318759E275F)

## moveTo

moveTo(x: number, y: number): void

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(50, 100);
    path.lineTo(250, 100);
    path.lineTo(150, 200);
    path.closePath();
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/zuEwZYRlRRWOT4_mWdBhkg/zh-cn_image_0000002815401297.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A56852CF606AAA550D3887C325EB087BC5F5B57D8E50AB1709408C34D5F1D15)

## lineTo

lineTo(x: number, y: number): void

从当前点绘制一条直线到目标点。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 400px; height: 450px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(100, 100);
    path.lineTo(100, 200);
    path.lineTo(200, 200);
    path.lineTo(200, 100);
    path.closePath();
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/VXyBeT4ERLaCd_YfzyIuNw/zh-cn_image_0000002786521722.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=496BA48947F5F90C06D97D36D2461610A353A8A4A60635895163631BD16EB6D8)

## bezierCurveTo

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

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(10, 10);
    path.bezierCurveTo(20, 100, 200, 100, 200, 20);
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/aWJ_4UpQQ22kRG6AXAi1TA/zh-cn_image_0000002786361794.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD376BB810FF06A9C9B8462F148D1F7EBC272A871FDB42678FF5C9439440A541)

## quadraticCurveTo

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

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(10, 10);
    path.quadraticCurveTo(100, 100, 200, 20);
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/iYf94-7rRqW8HfRzT_OoQQ/zh-cn_image_0000002815561215.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AF2E509EC96054DAB418F9263AC7F581CEE246B9F44375EE6B571E949A19D4D)

## arc

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

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.arc(100, 75, 50, 0, 6.28);
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/EUjSoyVsQ8uKBYutv81Aaw/zh-cn_image_0000002815401299.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=38CA07262269DA342E2C0774D2960A8A89B1D4E4A09C72EA8FC020E65F5FE291)

## arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧控制的点和圆弧半径创建圆弧路径。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x1 | number | 圆弧控制的第一个点的x坐标值。 |
| y1 | number | 圆弧控制的第一个点的y坐标值。 |
| x2 | number | 圆弧控制的第二个点的x坐标值。 |
| y2 | number | 圆弧控制的第二个点的y坐标值。 |
| radius | number | 圆弧的圆半径值。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.arcTo(150, 20, 150, 70, 50);
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/7h8g6qYSQziykF3MF6bbHg/zh-cn_image_0000002786521724.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C29CC2E6AD77B476F1F0BC24B27E57A60B6D496205FCD60BF0A8D588530B13E)

## ellipse

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的区域绘制一个椭圆。

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

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/YBdVL_1gQvu1wwA3HUbEzw/zh-cn_image_0000002786361796.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBF5416FE95DAFC9FA9980EE4DB2BFC45D3812CB0B617BD896EF8FA64525DBBF)

## rect

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

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.rect(20, 20, 100, 100);
    ctx.stroke(path);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/t40nTL9YQIm6BXIliRRPzg/zh-cn_image_0000002815561217.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=94AE2614B38C3D0DC7BEE07AE0C806792770B5550F8678A311A1E9D038E45F65)
