---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-10-31T07:35:43+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:cbedcd413a45d31dfc5cbee2c0037605d7d8e6afb287de954b88c1d095e5d00a
---

使用CanvasRenderingContext2D在canvas画布组件上进行绘制，绘制对象可以是矩形、文本。

**说明** 

* 从API版本23开始，预览器已取消JS文件48KB的大小限制。对于API版本22及之前，JS文件大小不能超过48KB。
* 由于轻量级设备的资源受限，canvas能力不适用于需要进行重复绘制图形的场景（如不断旋转的指针、不断变幻位置的图形），大量的绘制指令会导致内存不足问题，不建议使用。如需实现组件的旋转或平移效果，可使用CSS动画，具体请参见[动画样式](js-lite-components-common-animation.md)。

**示例：**

```html
<!-- xxx.hml -->
<div>
    <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
    <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```javascript
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/nCJhmv9kQE6qIqyZrsZpgw/zh-cn_image_0000002806031353.png)

## fillRect()

填充一个矩形。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形左上角点的x坐标。 |
| y | number | 指定矩形左上角点的y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/qL7j0fZKT-y3FtSUhFlCSA/zh-cn_image_0000002806111245.png)

```javascript
ctx.fillRect(20, 20, 200, 150);
```

## fillStyle

指定绘制的填充色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 设置填充区域的颜色。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/JYN3ond7TF2kkIww750UOg/zh-cn_image_0000002776911622.png)

```javascript
ctx.fillStyle = '#0000ff';
ctx.fillRect(20, 20, 150, 100);
```

## strokeRect()

绘制具有边框的矩形，矩形内部不填充。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形的左上角x坐标。 |
| y | number | 指定矩形的左上角y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/1TcS2mhmSAmj0389Y7B0Pg/zh-cn_image_0000002776751638.png)

```javascript
ctx.strokeRect(30, 30, 200, 150);
```

## fillText()

绘制填充类文本。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| text | string | 需要绘制的文本内容。 |
| x | number | 需要绘制的文本的左下角x坐标。 |
| y | number | 需要绘制的文本的左下角y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/XymLmb5tSiimGM3vCtbORw/zh-cn_image_0000002806031355.png)

```javascript
ctx.font = '35px sans-serif';
ctx.fillText("Hello World!", 20, 60);
```

## lineWidth

指定绘制线条的宽度值。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| lineWidth | number | 设置绘制线条的宽度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/hUoENYSUTdOQ_RhygS_fqA/zh-cn_image_0000002806111247.png)

```javascript
ctx.lineWidth = 5;
ctx.strokeRect(25, 25, 85, 105);
```

## strokeStyle

设置描边的颜色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 指定描边使用的颜色 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/aqgj7PspRSygP7XHlzVQiA/zh-cn_image_0000002776911626.png)

```javascript
ctx.lineWidth = 10;
ctx.strokeStyle = '#0000ff';
ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/4Pr7CwJ2RdmQgas6AA4htw/zh-cn_image_0000002776751640.png)

```javascript
ctx.moveTo(25, 25);
ctx.lineTo(25, 105);
ctx.strokeStyle = 'rgb(0,0,255)';
ctx.stroke();
```

### beginPath()5+

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Qlu7WLl_Sr-4ZGIjeJjYpQ/zh-cn_image_0000002806031357.png)

```javascript
ctx.beginPath();
ctx.lineWidth = 6;
ctx.strokeStyle = '#0000ff';
ctx.moveTo(15, 80);
ctx.lineTo(280, 80);
ctx.stroke();
```

### moveTo()5+

路径从当前点移动到指定点。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/P9LZuOgGSlW_oORmv07euQ/zh-cn_image_0000002806111249.png)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### lineTo()5+

从当前点到指定点进行路径连接。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/65cpz1coTsuvEx7GjeQIhA/zh-cn_image_0000002776911628.png)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### closePath()5+

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Nm6EWAFbScOFOz4C5kU_OA/zh-cn_image_0000002776751642.png)

```javascript
ctx.beginPath();
ctx.moveTo(30, 30);
ctx.lineTo(110, 30);
ctx.lineTo(70, 90);
ctx.closePath();
ctx.stroke();
```

## font

设置文本绘制中的字体样式。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| value | string | 字体样式支持：sans-serif, serif, monospace，该属性默认值为30px HYQiHei-65S。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/mLvhILBSRtKpppl2kAKBUA/zh-cn_image_0000002806031359.png)

```javascript
ctx.font = '30px sans-serif';
ctx.fillText("Hello World", 20, 60);
```

## textAlign

设置文本绘制中的文本对齐方式。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| align | string | 可选值为：  - left（默认）：文本左对齐；  - right：文本右对齐；  - center：文本居中对齐； |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/O1g9cV2ASG-nktzU3U78zA/zh-cn_image_0000002806111251.png)

```javascript
ctx.strokeStyle = '#0000ff';
ctx.moveTo(140, 10);
ctx.lineTo(140, 160);
ctx.stroke();

ctx.font = '18px sans-serif';

// Show the different textAlign values
ctx.textAlign = 'left';
ctx.fillText('textAlign=left', 140, 100);
ctx.textAlign = 'center';
ctx.fillText('textAlign=center',140, 120);
ctx.textAlign = 'right';
ctx.fillText('textAlign=right',140, 140);
```

## arc()5+

绘制弧线路径。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值，单位：vp。 |
| y | number | 是 | 弧线圆心的y坐标值，单位：vp。 |
| radius | number | 是 | 弧线的圆半径，单位：vp。 |
| startAngle | number | 是 | 弧线的起始弧度，单位：弧度。 |
| endAngle | number | 是 | 弧线的终止弧度，单位：弧度。 |
| anticlockwise | boolean | 否 | 是否逆时针绘制圆弧。  true：逆时针方向绘制弧线。  false：顺时针方向绘制弧线。  默认值：false。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/U7GTMpPmQXCBOYvm9Kr36A/zh-cn_image_0000002776911630.png)

```javascript
ctx.beginPath();
ctx.arc(100, 75, 50, 0, 6.28);
ctx.stroke();
```

### rect()5+

创建矩形路径。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值，单位：vp。 |
| y | number | 是 | 指定矩形的左上角y坐标值，单位：vp。 |
| width | number | 是 | 指定矩形的宽度，单位：vp。 |
| height | number | 是 | 指定矩形的高度，单位：vp。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/n9xi6HprTBeXoQm3oU-SKQ/zh-cn_image_0000002776751644.png)

```javascript
ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
ctx.stroke(); // Draw it
```
