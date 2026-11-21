---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-11-21T09:14:25+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:3d7705b560035925bd55e26c8e8a381ef5df513eb7eab6d921dbe6363ddfe09e
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/8dlN9ESMRDGQwISSxZlObA/zh-cn_image_0000002821839627.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=211C403DB3291C2B77AD37F8EBB4D5C8C2CB4A0E9222A8176980FFD6963D9D9A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/poureZPPRJaHn6VJYn5z7Q/zh-cn_image_0000002821759629.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=462644D95F8EB950EE9386E98A66BC66783F3418491DD04123F692FF8F5D6483)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/I-Z1lj4ETkqHOPxIcU4hgA/zh-cn_image_0000002793039696.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=70CB7A43A27267306C4C8F64ED1E91BD2CF9DAC62AE8CCB067B74E603B3AA338)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/8OvzMroXQFC-nsWmFX6udQ/zh-cn_image_0000002792879724.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FC94B564CEA91C4E311E8CFE9B6B634221A0E1B269A378C69DCD27D442B9A48)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/2PZRlXY8Se6B0k59RTnpGQ/zh-cn_image_0000002821839629.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=0962777E87975C98ACCD8684D162517F5789D943A3EA4E5432B19491DC7D2836)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/vmfoCON1SXGK6BhajQHvbw/zh-cn_image_0000002821759631.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=E52A8B09AE0DAFB0478855DEC6607AFD711A8EEF1DB84A42F3D0C5A637E92D06)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/xIPH7jVVQZ-G2PiQFhjRGw/zh-cn_image_0000002793039698.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=84BFC32476E96204428992EEAF538249F88AEF431481E9141D8049140CB29526)

```javascript
ctx.lineWidth = 10;
ctx.strokeStyle = '#0000ff';
ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/k9-gvWT8TuCYASBk1haUZA/zh-cn_image_0000002792879726.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=69E985E23EFCB51686782E3FDC2781DDFFF5ACD764DC8FF0AFEBA154939220D6)

```javascript
ctx.moveTo(25, 25);
ctx.lineTo(25, 105);
ctx.strokeStyle = 'rgb(0,0,255)';
ctx.stroke();
```

### beginPath()5+

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/AnYMuZ6tQQmxEljfknj3AA/zh-cn_image_0000002821839631.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=464A0D8E02E3450126C5F174A53C934D2C8A2E30FCB6D835A34597DCFA7D5E0C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Lnm6ib0oSyGUDIJlZexrsA/zh-cn_image_0000002821759633.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B047EFBC5730536DCBA44486100F41C6DD13D3B43F2BC152B36888E7D816621)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/SyiYBcgnQIyTQUivobhQwQ/zh-cn_image_0000002793039700.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=00E1B728C7CDE30AE426FDEE67666D406AE6C1DC629F187E9205D13A0DB6F5B4)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### closePath()5+

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/A38DN36lQnmIwszIBKxyZg/zh-cn_image_0000002792879728.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=5480F692EF64028D06BF6CFFA7623F061AE2AF8A7E1287A6524818E80215B5B4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/yFNCQ0knQluOqTtKGpRqUA/zh-cn_image_0000002821839633.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D87D407ECD9BA6F245B1A5398DE3E274740ED90D7340D20FB6DDBCF234A83E2)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/JMCVKld_SLuUnE1xQEJmDA/zh-cn_image_0000002821759635.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=27C4FF81F825EE063B38D74042C14E747684FAED006F7570EECD1112156B8A91)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/XauZcd5FTGaOibwtMtq9sQ/zh-cn_image_0000002793039702.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=E13D5F547D21FE1C96C3EBB3E61A5455231BBC2B2C754D223970E7E58D477910)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/X_JjEfeHSc2KlkkXpuaBAw/zh-cn_image_0000002792879730.png?HW-CC-KV=V1&HW-CC-Date=20261121T011425Z&HW-CC-Expire=31536000000&HW-CC-Sign=9394D5A0EDFFF9D88E7A307F41DFC84E4DEC72B05BF74E47C218FD8735C0298F)

```javascript
ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
ctx.stroke(); // Draw it
```
