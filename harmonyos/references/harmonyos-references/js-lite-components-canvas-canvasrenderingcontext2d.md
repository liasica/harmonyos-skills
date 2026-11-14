---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-11-14T08:50:34+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:04fb58c57d84f3c7bca96551cf8caa9e004185b46f6af43b6b0588db7d5a2182
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/nv6PuX0iTViLSo_avZgz8A/zh-cn_image_0000002788469650.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE91EB682871E49B22677452D44A9AFDC47FA331A38C3E00ECFB9DF7F9F2ADBD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/gym80CXuQs6eMtNbnSL_1Q/zh-cn_image_0000002817509139.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDFE78A5CCEFFC6F72E619911749B1B55841A49B5AF1C1C224CC1CF62A47E78B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/PcIDyawVSxa7tDNT1bfmAQ/zh-cn_image_0000002788309708.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDF29B49F8906C0D810C9AB5CC95B24CE08527F89EE111B7DE547D59AA55E29B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/-g6m16txStefhukIbef6Nw/zh-cn_image_0000002817429071.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=D06A76C9F89A2AE4ED7BE22AB61100A819C5E2D5B86356AFCFB25BD13B64C4A3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/APx6l-9ATh-hvEIbPv_DJg/zh-cn_image_0000002788469652.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=409E1119BFE8987C5A767D8E656B29CE50A32FDE99381782563C1D2631277773)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/2keErHmBTomqSuNGm0KLlA/zh-cn_image_0000002817509141.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=B88B32568978EB0A2FC65F98B650B9AAC08DCBF67E03F87BB6ABE4818A7C7228)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/r2ir9D6AQfyR4JP0OyAkUQ/zh-cn_image_0000002788309710.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=E94866E0B2B8CE930309B18718AA977852222D676738CBD6801543EFBBED1244)

```javascript
ctx.lineWidth = 10;
ctx.strokeStyle = '#0000ff';
ctx.strokeRect(25, 25, 155, 105);
```

### stroke()5+

进行边框绘制操作。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/eM5-6xH1TBq1mJV4zbaR0g/zh-cn_image_0000002817429073.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=27B4C8AC6885CF3A75CD5B903A6E3A5803E1146934FCEBE216573032AA4CE687)

```javascript
ctx.moveTo(25, 25);
ctx.lineTo(25, 105);
ctx.strokeStyle = 'rgb(0,0,255)';
ctx.stroke();
```

### beginPath()5+

创建一个新的绘制路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Z91bbvPESCSKVKpEcAQ5qg/zh-cn_image_0000002788469654.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BCF229C7E3C554199D813F5DA7FBE84C30AE692ED8FA41FD0238CDBE410291C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/7mT-GC6wR26cmFk0AoKjSg/zh-cn_image_0000002817509143.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC6EC32C57B47B0D0D2ACA4A196AE9820F7B8DB1879D2177E5251E517C2ABCF9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Ia6XLqzvRqKmRCw0rVfAbw/zh-cn_image_0000002788309712.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CA8A8B2D2D4806B7C898F4070D81910CEF31AB99B63C6FEA9D0BE0A332257CB)

```javascript
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### closePath()5+

结束当前路径形成一个封闭路径。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kTvffPqIS7Ob7cH1plDrCw/zh-cn_image_0000002817429075.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=09205DA856783939FF29D145B2BAE2ADA75B797CBA2766226BCC47878EFBF5E4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/IrJv0BbnTHGbDVzBqaYmMw/zh-cn_image_0000002788469656.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB27431079294C5A4DEA846B2DE718F51E8CEF5E7FF5F3D28E927826FF69F531)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/RWYOMkrdQqOSYmirVWS_Vg/zh-cn_image_0000002817509145.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=11635A7C23D71E488BAE082E84F3D7F2DD6A84EE9B607B8D1DD7315743532D82)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/vqprecJySL-VEHaAm4ExrA/zh-cn_image_0000002788309714.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE70778E7A445ED9E72427C9291E4478B103F95B5CED8EB2A5DF3BCDCA485656)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/KZZtrygJTJ2P_7TtGdMWzg/zh-cn_image_0000002817429077.png?HW-CC-KV=V1&HW-CC-Date=20261114T005034Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FCD8EEA4470F7094B444ED8A2DB964D929F8FD1AC874FA4AED30EA9798885B3)

```javascript
ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
ctx.stroke(); // Draw it
```
