---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-04-28T08:03:31+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:ab05f0e1c3458fea237a37f16894e8f951def44b79658d3a547eef8d5503f76c
---

使用CanvasRenderingContext2D在canvas画布组件上进行绘制，绘制对象可以是矩形、文本。

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
5. </div>
```

```
1. // xxx.js
2. export default {
3. handleClick() {
4. const el = this.$refs.canvas1;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.arc(100, 75, 50, 0, 6.28);
8. ctx.stroke();
9. },
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/JZlBKqxwQkC19tDfZ01g2A/zh-cn_image_0000002552960414.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=71C71B9B2F562DB107A7726A9C7BDF1BDA6220057DB331B8E533FCDB2B86F18E)

## fillRect()

PhonePC/2in1TabletTVWearableLite Wearable

填充一个矩形。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形左上角点的x坐标。 |
| y | number | 指定矩形左上角点的y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/RG2fgDSvQY-nklAjshOImA/zh-cn_image_0000002583480415.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=051DA9E42F229D78839A7A94F0A8BEB28EBE3A2A02F96F0BA827E28EB61F5A0E)

```
1. ctx.fillRect(20, 20, 200, 150);
```

## fillStyle

PhonePC/2in1TabletTVWearableLite Wearable

指定绘制的填充色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 设置填充区域的颜色。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/xfR1YODhT-iwjkntiNUQQQ/zh-cn_image_0000002552800766.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=4D2CE8BA07F4560E78196ECE8E44825A8208E276804A2E46EDBD426694668EAA)

```
1. ctx.fillStyle = '#0000ff';
2. ctx.fillRect(20, 20, 150, 100);
```

## strokeRect()

PhonePC/2in1TabletTVWearableLite Wearable

绘制具有边框的矩形，矩形内部不填充。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形的左上角x坐标。 |
| y | number | 指定矩形的左上角y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/1_DEszGTSTmA0BGQNofeAA/zh-cn_image_0000002583440461.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=1185331772752734D23714E651E80C03448E08C1C7A5A1B3205FF73DF32EE35E)

```
1. ctx.strokeRect(30, 30, 200, 150);
```

## fillText()

PhonePC/2in1TabletTVWearableLite Wearable

绘制填充类文本。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| text | string | 需要绘制的文本内容。 |
| x | number | 需要绘制的文本的左下角x坐标。 |
| y | number | 需要绘制的文本的左下角y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/3PskztQbR4i6p2-WhFigZQ/zh-cn_image_0000002552960416.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=1CA059A24F54621B495C0F15E6EAED3BFB9B44A9FD637DB79ACC349E001ECBDB)

```
1. ctx.font = '35px sans-serif';
2. ctx.fillText("Hello World!", 20, 60);
```

## lineWidth

PhonePC/2in1TabletTVWearableLite Wearable

指定绘制线条的宽度值。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| lineWidth | number | 设置绘制线条的宽度。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/SaxEmOrhQdq3tNjk7nOIiw/zh-cn_image_0000002583480417.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=926E577CFA5D86DF50603BB3B9FFE1BEE2C64D6264B45C93EA64B6394D050477)

```
1. ctx.lineWidth = 5;
2. ctx.strokeRect(25, 25, 85, 105);
```

## strokeStyle

PhonePC/2in1TabletTVWearableLite Wearable

设置描边的颜色。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 指定描边使用的颜色 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/h9DtBZvYREapWKKUqanROQ/zh-cn_image_0000002552800768.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=B36E2CF7E4A1AAC1738CA8EB128913D2663D629A31820A451FA95EAE6C475CC1)

```
1. ctx.lineWidth = 10;
2. ctx.strokeStyle = '#0000ff';
3. ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

PhonePC/2in1TabletTVWearableLite Wearable

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/SKOWB9zFQIaYrg-SKWlUiw/zh-cn_image_0000002583440463.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=E709A2B41592241D1499E23054506255ECA2ECD3248434BFBFD8063F71011FBF)

```
1. ctx.moveTo(25, 25);
2. ctx.lineTo(25, 105);
3. ctx.strokeStyle = 'rgb(0,0,255)';
4. ctx.stroke();
```

### beginPath()5+

PhonePC/2in1TabletTVWearableLite Wearable

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/807amDtVSEa6Uf9x4X6sTA/zh-cn_image_0000002552960418.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=D76F7F5EF2E3E5BFE3387C664D864EB09B5AFF9292C0C4947B8820374251AE8B)

```
1. ctx.beginPath();
2. ctx.lineWidth = 6;
3. ctx.strokeStyle = '#0000ff';
4. ctx.moveTo(15, 80);
5. ctx.lineTo(280, 80);
6. ctx.stroke();
```

### moveTo()5+

PhonePC/2in1TabletTVWearableLite Wearable

路径从当前点移动到指定点。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/VnCCAurSRTiRGMSN_rFY4A/zh-cn_image_0000002583480419.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=511F8956D440947CB53C1D58FAB41A294E29FC9495EFF6A28F9B0C15A5AB4C8F)

```
1. ctx.beginPath();
2. ctx.moveTo(10, 10);
3. ctx.lineTo(280, 160);
4. ctx.stroke();
```

### lineTo()5+

PhonePC/2in1TabletTVWearableLite Wearable

从当前点到指定点进行路径连接。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/P0vvVPqJQay9-yoP3-st7w/zh-cn_image_0000002552800770.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=6D9FD8F09B7B91DC58DA43F4A4030E1C777C9C7BFC96FAB0285D58931DA95F01)

```
1. ctx.beginPath();
2. ctx.moveTo(10, 10);
3. ctx.lineTo(280, 160);
4. ctx.stroke();
```

### closePath()5+

PhonePC/2in1TabletTVWearableLite Wearable

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/7pcHGznPQ0CDoGOOcEHaXA/zh-cn_image_0000002583440465.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=56CA26E617FEE58AAD298A8993F2B2FE1BC493D2D617329AC0A2CFEE6C21DC84)

```
1. ctx.beginPath();
2. ctx.moveTo(30, 30);
3. ctx.lineTo(110, 30);
4. ctx.lineTo(70, 90);
5. ctx.closePath();
6. ctx.stroke();
```

## font

PhonePC/2in1TabletTVWearableLite Wearable

设置文本绘制中的字体样式。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| value | string | 字体样式支持：sans-serif, serif, monospace，该属性默认值为30px HYQiHei-65S。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Sf6dIVWWQHS3u1mQzu0o_Q/zh-cn_image_0000002552960420.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=1DD555EDA24214AE7E74FC6C51FCA0D43DB100631959A562BE88F946F9C84978)

```
1. ctx.font = '30px sans-serif';
2. ctx.fillText("Hello World", 20, 60);
```

## textAlign

PhonePC/2in1TabletTVWearableLite Wearable

设置文本绘制中的文本对齐方式。

**参数：**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| align | string | 可选值为：  - left（默认）：文本左对齐；  - right：文本右对齐；  - center：文本居中对齐； |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/LJk95Gt8SwGxJewCQc-xMg/zh-cn_image_0000002583480421.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=A8853B998C70726D48A969CA6D0205C82BF9DA5E3E13EF20680D76377721A9E8)

```
1. ctx.strokeStyle = '#0000ff';
2. ctx.moveTo(140, 10);
3. ctx.lineTo(140, 160);
4. ctx.stroke();

6. ctx.font = '18px sans-serif';

8. // Show the different textAlign values
9. ctx.textAlign = 'left';
10. ctx.fillText('textAlign=left', 140, 100);
11. ctx.textAlign = 'center';
12. ctx.fillText('textAlign=center',140, 120);
13. ctx.textAlign = 'right';
14. ctx.fillText('textAlign=right',140, 140);
```

## arc()5+

PhonePC/2in1TabletTVWearableLite Wearable

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/dckQMBYoQUmssVccmc6-ig/zh-cn_image_0000002552800772.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=5FD834CE26109171E95BDE74E578648BCEB2214E633BEE7AB653037FCED1447E)

```
1. ctx.beginPath();
2. ctx.arc(100, 75, 50, 0, 6.28);
3. ctx.stroke();
```

### rect()5+

PhonePC/2in1TabletTVWearableLite Wearable

创建矩形路径。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值，单位：vp。 |
| y | number | 是 | 指定矩形的左上角y坐标值，单位：vp。 |
| width | number | 是 | 指定矩形的宽度，单位：vp。 |
| height | number | 是 | 指定矩形的高度，单位：vp。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/EzQA7k3yTSKZKSahzPQGRg/zh-cn_image_0000002583440467.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=CE580170FCC6ACBD78198A783C2EF451E0FDE6CEFE11A8F52EDE65A2AC0B669A)

```
1. ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
2. ctx.stroke(); // Draw it
```
