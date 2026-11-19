---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-11-19T09:51:24+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:2cc946b91251a050f548f0220af0d5d99e7f0d17f01ed191fffc20c007832ed5
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/FzDt76YySh-ALMakSj-1gQ/zh-cn_image_0000002820527989.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=63873F8F9E2E83C551A3ECD029B8D678B3849F2BF466459B92FE67D11B66A219)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/QcjeVQ65RLKBMTHoSsuDhg/zh-cn_image_0000002820407991.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D5C0E0317A21F689745BC16EF1B69D90C285CC2A704D6BF5EFD9F4B3EE73ECC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/k4NuWIKrScOeU_y_j56jJw/zh-cn_image_0000002791728010.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=C832895FDC6E386C9FD4EFAF612F45DC38908DCA534BEA5F5C8C3252914DE4DA)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/qQ1YCLxRSS60cPlm6jg-dQ/zh-cn_image_0000002791568038.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=62D1E0ACFD795C782B3BCE6D8897D8686F3750E62184B5CB7A6661F94782D105)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/x-iCYMq7QfmM1xpC4hBYoA/zh-cn_image_0000002820527991.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=234BFAD216E643828A6766CA0F621E025407D91CFAF605FB42A50B90CC1626E1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/vAkMvJNIRoe5kMpMBE2D8w/zh-cn_image_0000002820407993.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4F116B43C715B2DC518497D53178F1917ECFD5225B38A63C7E924A10B137681)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/1zNhbNVQRVWmaYoOegcSHA/zh-cn_image_0000002791728012.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A81B368D84B663484436EBEF27720B94EC04DBCB331F3891A19886FA0C08596)

```javascript
ctx.lineWidth = 10;
ctx.strokeStyle = '#0000ff';
ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/CncXywyiQ7uB7zZ6tii8Gg/zh-cn_image_0000002791568040.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=3ABB0F5290ACEFE466ACBEE9CDE0A13E8067E87BEC8A5C596F63A2138EAFD4A5)

```javascript
ctx.moveTo(25, 25);
ctx.lineTo(25, 105);
ctx.strokeStyle = 'rgb(0,0,255)';
ctx.stroke();
```

### beginPath()5+

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/8-UZraSRTd-Tp9aTgNLbXA/zh-cn_image_0000002820527993.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAFFB81A7C96F51BEBE50192831266F03A30739AA542127CC2EA728A400BAF31)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/tPEI93FvSm6M0MzKFl55ZQ/zh-cn_image_0000002820407995.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A3BC999C7995B824079459E953F15187DFAB2D1D827520C6B530FD7CE5EB647)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/kT7Gq7TJQyWDgxUXGMW-wQ/zh-cn_image_0000002791728014.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A2D09D2CB78A6D55E5D4DD32161CAFD9B0131CEA4518CB512275BBD4238A760)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### closePath()5+

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/bqaPFWBsSzy82u49URNnhA/zh-cn_image_0000002791568042.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9B526E3F4094630A05C87624F652A5890B538C1DE0947D4A8144AB168E9741A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/dGhJzF_XRFyFftNkloweLg/zh-cn_image_0000002820527995.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=78BC133B91F00239C55AD5A931E100697719F525D89CCD7F56D6E6910C2FD10C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/EEEJaK3CR0aIOA-Ps7EDMA/zh-cn_image_0000002820407997.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=8199C8C2E99BC327B3F9DD9A97386DF30ABDB0E274FC2DF5809E2F47E521AFA1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/8w1_VzcJR2q5XsHGq2oWGg/zh-cn_image_0000002791728016.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F3570B9EEDC149ABEC3D6856D78B03FEF62CA701AF880565E72075513325D18)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/oydB_IPmRlW1BYcVAt3tLw/zh-cn_image_0000002791568044.png?HW-CC-KV=V1&HW-CC-Date=20261119T015124Z&HW-CC-Expire=31536000000&HW-CC-Sign=1390E3491B0B9A960E8E5DE472012E0A9ABA71B5A3E31B5E9B9DBEBCA1251F3C)

```javascript
ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
ctx.stroke(); // Draw it
```
