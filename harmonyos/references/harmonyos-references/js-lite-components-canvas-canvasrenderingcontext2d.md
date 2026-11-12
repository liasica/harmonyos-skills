---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:7d49eecb89c03ac87e5706b5788d69b1811eb6e9e950a1918bd8c92fb35dd7f1
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/JVB_1Z4aQdS79y2MrNCC0w/zh-cn_image_0000002786521902.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FA5B5ADAA00C5C181DF28D2071A3FF42890EF4876F3EF8CA762A6F7313A0D25)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/te7YyZXvSlOnomBjBIuCZA/zh-cn_image_0000002786361974.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=11C6CB60D130401967F249B4C91C78C1535402B11B17493753B807E8259EF23A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/2NuCJK-jSXGM1QgbVsE8xw/zh-cn_image_0000002815561395.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=82597A212CD36ABA4B67CB5EC0D52831E27A9DC4DDFA0F58858CCEA816DBD005)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/sVWh5xWqTMqvfpZmcjuRIg/zh-cn_image_0000002815401479.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=D125120194DA1AEEA8EB6AB92302CA56209F4FB8523CB5831EE442C5989B1F5C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/R4LA4HMUStyGp5bEeqwo_A/zh-cn_image_0000002786521904.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=76014A54BAB6A4003A5E94E52422FF7F7DB261449ABC26E2269857BBA8ACADF1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/UGwUmbtAT9S9BT489i5r4A/zh-cn_image_0000002786361976.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC1F775A220ECA9BA491AE2E64D3631DBFFA0D56B9C63174CF488C85CDD64814)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/0cJGWXepTpmLN7V6OGJ-Tg/zh-cn_image_0000002815561397.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=92FFEF4A43EA0ADE2A895864E6A396734138CB2D240FAD956F2624F5BF3AC936)

```javascript
ctx.lineWidth = 10;
ctx.strokeStyle = '#0000ff';
ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/GrFOaw5kT0ud_HG319yacw/zh-cn_image_0000002815401481.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=924318BD7A4C014882B2AF7702488B2403C76EE1228A8AD37E94179DA49CF892)

```javascript
ctx.moveTo(25, 25);
ctx.lineTo(25, 105);
ctx.strokeStyle = 'rgb(0,0,255)';
ctx.stroke();
```

### beginPath()5+

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/rvU7IDQTQhSp7WOBjKg4cA/zh-cn_image_0000002786521906.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A200C84F4A492D89E9626E824DF15ED6062EE413C3BCBB8F0966AE3EC56976F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/BL-Z4h-DTpOHXg_9Ieq3nQ/zh-cn_image_0000002786361978.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1F59FE99B4CCEB4EABE0E47A76D2A0139EEDDA74A665AFF3E7A6EF90E9880A4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/AjVtRLP6Rt-7E4XUufkcVA/zh-cn_image_0000002815561399.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=48F442FD68CC177E1B6D747129FB7E82EF4CEC6E0D9C90A8C651EE6E1E22738A)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### closePath()5+

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/OHujnJ2USXqpzw2nsYJKug/zh-cn_image_0000002815401483.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8427891B402CED3C31C5DB58945B3AFE12D132E4DF42A73BDCA1F026F2178C9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/KYciRVjzRPyo2t1QbhldHQ/zh-cn_image_0000002786521908.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=167344782BBD190E7AA14A39A12AF2082532F90DBB9EDC1B2E905621051B17CD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/ouCsPui2RVadD_HfLaJJVw/zh-cn_image_0000002786361980.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=E51D4E256FBADA5659E614582EEDBD694A96C029ECF7AF6516B33598178BBD68)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/lmsbPOZyQduD9sbKgKrApA/zh-cn_image_0000002815561401.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8B40F0EF2607486B63EDE53E73AC810AE714EC353C079E3FD8F643C5407D4A1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/VxNYY51jSf2fSPvuqMShxA/zh-cn_image_0000002815401485.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=362007ADB4CF6CD4EC126D3FDCA9F1FBBC1DB22BB6BA4876057ADFF3744C9769)

```javascript
ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
ctx.stroke(); // Draw it
```
