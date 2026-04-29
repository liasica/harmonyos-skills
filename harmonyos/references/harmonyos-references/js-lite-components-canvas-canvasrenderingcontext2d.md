---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-04-29T13:53:55+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:0daa2990abb309881faed5eb49c8962d3bb0e3b482076815bc35ba8286e150ef
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ZowuRf6kTg2ljeGfqwvohA/zh-cn_image_0000002558607280.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=7FBCFD64D5DB74641FB21CC55786D129343FDEC2A7CA1AB9093AEAC4D925A035)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/E-uESs8QRXyHvWzriC--Tg/zh-cn_image_0000002589326809.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=3E04F180DA2246DC5A20B206157B724E2F03546FFEC3133977A558DA9B55B9BB)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/UiIx7b92Sf6sepgUd5kEPQ/zh-cn_image_0000002589246749.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=AC09D71136F5F8BB0A358628B2CE49CD74DB2766E9E4124F63D453DEED7977C8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/qf9llpstSD-SHKF2bwKqOw/zh-cn_image_0000002558766942.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=47E7562837D0A178C90A5B758E1F505D60304A21A7FB13045FBF31D3CF263DAE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/jlsJ2HpyQQu7OMrA__ag0g/zh-cn_image_0000002558607282.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=F067AF91428E10A663B111308FB2FE8A4CF8E80F043BA384ABCBD183B62239E9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/S4bTf18NQsOhzq-Lu58JUg/zh-cn_image_0000002589326811.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=BD7CE87D194359BB9488FA7C001F6EB1C16FD8782E75559F1694FDEFD5920602)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/CODM1RQESum8daTFxBRbRQ/zh-cn_image_0000002589246751.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=1ECA234B4D8687307BED6E4515CEC09219CFD22AD4A01506671972B3C421188C)

```
1. ctx.lineWidth = 10;
2. ctx.strokeStyle = '#0000ff';
3. ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

PhonePC/2in1TabletTVWearableLite Wearable

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/r3vdVgB7RbCa4Gd1QvmcuQ/zh-cn_image_0000002558766944.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=DAF43A47CABA76902B4E27F63DC845DD89EE0CC369B990D60DB5AC0FF0C7E4A1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/zW6rZ_KLRdS_7Y3L5Dpj4g/zh-cn_image_0000002558607284.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=C0E464E748727055DC89D4AF059F5C6AEEA54ED1CA849DB43EB8510E5CFF557F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/xxJLuLv2QjSlaEDRCBlMlg/zh-cn_image_0000002589326813.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=4C7241AB46CD0269FD00A2E0AE1302E174A06A56B402FDA5C24575077218E556)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/m8kJNRxvTLGumamVZMfEuQ/zh-cn_image_0000002589246753.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=3EEF6F0EF0FF8C9504F4D567DDFD285797B57290BB23F6BD60687B8B9CFCBD1C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/MwWZtQy4TYO9KsS80kNqAw/zh-cn_image_0000002558766946.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=87FFB25E8AECA2D99E716DF4D50372BFE65C7C2ACF1A3DD3280295C9AA71AC51)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/YRlTfpMIRWGGyKA5XJ9DwA/zh-cn_image_0000002558607286.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=FAD68D07C96F25A98EE3FE7F5F1C084C632F993C3F7ABE3B0B010B15C35B404F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/bO9TF9FgQIGr7N_YWINlgw/zh-cn_image_0000002589326815.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=1DEAE18DBCC9821E7B1FE0FE521825469EA54044BB50BF3CFA117C3568931CB0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/0-q_uaXXSGKzbcNe7_x-dg/zh-cn_image_0000002589246755.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=919139CDF7E5A038E1CCCAF481EB413C4BB1898A7125F8574D409F1A8AD42962)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/R299acfyROKlygeSMxsPvQ/zh-cn_image_0000002558766948.png?HW-CC-KV=V1&HW-CC-Date=20260429T055354Z&HW-CC-Expire=86400&HW-CC-Sign=0B0E715FBB8B848E152528B68103F1B452B9C8CB3775E42114E8636CE0CD9352)

```
1. ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
2. ctx.stroke(); // Draw it
```
