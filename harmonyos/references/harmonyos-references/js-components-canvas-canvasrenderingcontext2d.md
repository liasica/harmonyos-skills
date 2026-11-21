---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-11-21T09:14:24+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:5329428aa0a6bfae71d5ce4bba4969f8d39a3adf28ce2c1ce0057f82e0126383
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用CanvasRenderingContext2D在[canvas组件](js-components-canvas-canvas.md)上进行绘制，绘制对象可以是矩形、文本、图片等。

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="handleClick" onclick="handleClick" />
  <input type="button" style="width: 180px; height: 60px;" value="antialias" onclick="antialias" />
</div>
```

```js
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  },
  antialias() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d', { antialias: true });
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  }
}
```

* 示意图（关闭抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/_qYQEitYT7ytU5b-xHnOFQ/zh-cn_image_0000002793039482.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=96AC3D986A49CEA33ADC5727E7096108E9A5D4C95DBC51169BF5BA3EDD44BE17)
* 示意图（开启抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/SfrIuXmWQ8qmdOj9sGbvUQ/zh-cn_image_0000002792879508.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2BC1D31CBD08ACB8B06A32A4816580901E93586C900813456889039DA12F38F)

## 属性

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| [fillStyle](js-components-canvas-canvasrenderingcontext2d.md#fillstyle) | <color> | [CanvasGradient](js-components-canvas-canvasgradient.md) | [CanvasPattern](ts-components-canvas-canvaspattern.md) | 指定绘制的填充色。  - 类型为<color>时，表示设置填充区域的颜色。  - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。  - 类型为CanvasPattern时，使用 createPattern()方法创建。  超出取值范围填充为黑色。 |
| [lineWidth](js-components-canvas-canvasrenderingcontext2d.md#linewidth) | number | 设置绘制线条的宽度。 |
| [strokeStyle](js-components-canvas-canvasrenderingcontext2d.md#strokestyle) | <color> | [CanvasGradient](js-components-canvas-canvasgradient.md) | [CanvasPattern](ts-components-canvas-canvaspattern.md) | 设置描边的颜色。  - 类型为<color>时，表示设置描边使用的颜色。  - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。  - 类型为CanvasPattern时，使用 createPattern()方法创建。 |
| [lineCap](js-components-canvas-canvasrenderingcontext2d.md#linecap) | string | 指定线端点的样式，可选值为：  - butt：线端点以方形结束。  - round：线端点以圆形结束。  - square：线端点以方形结束，该样式下会增加一个长度和线段厚度相同，宽度是线段厚度一半的矩形。  默认值：butt |
| [lineJoin](js-components-canvas-canvasrenderingcontext2d.md#linejoin) | string | 指定线段间相交的交点样式，可选值为：  - round：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。  - bevel：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。  - miter：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。  默认值：miter |
| [miterLimit](js-components-canvas-canvasrenderingcontext2d.md#miterlimit) | number | 设置斜接面限制值，该值指定了线条相交处内角和外角的距离。  默认值：10 |
| [font](js-components-canvas-canvasrenderingcontext2d.md#font) | string | 设置文本绘制中的字体样式。  语法：ctx.font="font-style font-weight font-size font-family"5+  - font-style(可选)，用于指定字体样式，支持如下几种样式：normal, italic。  - font-weight(可选)，用于指定字体的粗细，支持如下几种类型：normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900。  - font-size(可选)，指定字号和行高，单位只支持px。  - font-family(可选)，指定字体系列，支持如下几种类型：sans-serif, serif, monospace。  默认值："normal normal 14px sans-serif" |
| [textAlign](js-components-canvas-canvasrenderingcontext2d.md#textalign) | string | 设置文本绘制中的文本对齐方式，可选值为：  - left：文本左对齐。  - right：文本右对齐。  - center：文本居中对齐。  - start：文本对齐界线开始的地方。  - end：文本对齐界线结束的地方。  ltr布局模式下start和left一致，rtl布局模式下start和right一致。  默认值：left |
| [textBaseline](js-components-canvas-canvasrenderingcontext2d.md#textbaseline) | string | 设置文本绘制中的基线对齐方式，可选值为：  - alphabetic：文本基线是标准的字母基线。  - top：文本基线在文本块的顶部。  - hanging：文本基线是悬挂基线。  - middle：文本基线在文本块的中间。  - ideographic：文字基线是表意字基线；如果字符本身超出了alphabetic 基线，那么ideographic基线位置在字符本身的底部。  - bottom：文本基线在文本块的底部。 与 ideographic 基线的区别在于 ideographic 基线不需要考虑下行字母。  默认值： alphabetic |
| [globalAlpha](js-components-canvas-canvasrenderingcontext2d.md#globalalpha) | number | 设置透明度。  范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。 |
| [lineDashOffset](js-components-canvas-canvasrenderingcontext2d.md#linedashoffset) | number | 设置画布的虚线偏移量，精度为float。  默认值：0.0 |
| [globalCompositeOperation](js-components-canvas-canvasrenderingcontext2d.md#globalcompositeoperation) | string | 设置合成操作的方式。类型字段可选值有source-over，source-atop，source-in，source-out，destination-over，destination-atop，destination-in，destination-out，lighter，copy，xor。具体请参考[类型字段说明](js-components-canvas-canvasrenderingcontext2d.md#globalcompositeoperation)。  默认值：source-over |
| [shadowBlur](js-components-canvas-canvasrenderingcontext2d.md#shadowblur) | number | 设置绘制阴影时的模糊级别，值越大越模糊，精度为float。  默认值：0.0 |
| [shadowColor](js-components-canvas-canvasrenderingcontext2d.md#shadowcolor) | <color> | 设置绘制阴影时的阴影颜色。 |
| [shadowOffsetX](js-components-canvas-canvasrenderingcontext2d.md#shadowoffsetx) | number | 设置绘制阴影时和原有对象的水平偏移值。 |
| [shadowOffsetY](js-components-canvas-canvasrenderingcontext2d.md#shadowoffsety) | number | 设置绘制阴影时和原有对象的垂直偏移值。 |
| [imageSmoothingEnabled](js-components-canvas-canvasrenderingcontext2d.md#imagesmoothingenabled) | boolean | 用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。  默认值：true |

### fillStyle

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = '#0000ff';
    ctx.fillRect(20, 20, 150, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/x9AZeAvaROGYmfoPij-q5g/zh-cn_image_0000002821839413.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=485F6D2AFD37B130EB829F2C3F05432E4B65F2B72B56C3DB291717E03384A755)

### lineWidth

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 5;
    ctx.strokeRect(25, 25, 85, 105);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/kDSwf1MCQr2g4QCKNu0X2A/zh-cn_image_0000002821759415.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=93C84E5346AE704516DCA97112BBEA9B7E260481C804FF43EFFE7D5A99D24100)

### strokeStyle

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 10;
    ctx.strokeStyle = '#0000ff';
    ctx.strokeRect(25, 25, 155, 105);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/0yQAr1-dSRK2-lE7OqH83Q/zh-cn_image_0000002793039484.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=934F744466E8C4172DF4E5ADF6FCFE43DEBD7A664070FC80DF030D7D98B46821)

### lineCap

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.lineCap = 'round';
    ctx.moveTo(30, 50);
    ctx.lineTo(220, 50);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/9RZ9hfaKTtO8PFDIECyYDQ/zh-cn_image_0000002792879510.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9CD7FCD10E98BB1A57891690BE133D1CB80ADE4B881CE040CB1718E6472650F)

### lineJoin

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = 8;
    ctx.lineJoin = 'miter';
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 110);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/L1p_b0DVQHqw5M7dqln5Zw/zh-cn_image_0000002821839415.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=735F6BEAE0F90BBEF11DB1103B599833B50C97941FE49D5CC1D69BA40A0F50BC)

### miterLimit

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 14;
    ctx.lineJoin = 'miter';
    ctx.miterLimit = 3;
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 70);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/yXnw-AAGS8uzWwUrGlmTkw/zh-cn_image_0000002821759417.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BBC85EBFEA6C457AE42384A511F7565771834C5E5B2CC8CC0F9C3179CCF2179)

### font

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '30px sans-serif';
    ctx.fillText("Hello World", 20, 60);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/9CaWiA5PTUuffZdV9VaAdw/zh-cn_image_0000002793039486.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=472AAB69F95FE4CCF997168C15C0D95F998B6E089F5613AD7BBF062FE18954F4)

### textAlign

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(140, 10);
    ctx.lineTo(140, 160);
    ctx.stroke();
    ctx.font = '18px sans-serif';
    // Show the different textAlign values
    ctx.textAlign = 'start';
    ctx.fillText('textAlign=start', 140, 60);
    ctx.textAlign = 'end';
    ctx.fillText('textAlign=end', 140, 80);
    ctx.textAlign = 'left';
    ctx.fillText('textAlign=left', 140, 100);
    ctx.textAlign = 'center';
    ctx.fillText('textAlign=center',140, 120);
    ctx.textAlign = 'right';
    ctx.fillText('textAlign=right',140, 140);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/xsjLuWSBSfeknduUv7PKig/zh-cn_image_0000002792879512.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=14A0787504ACBF617E189A7B9356C2078D91DA5BF01D5D6E817B53E6AC35C4F8)

### textBaseline

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(0, 120);
    ctx.lineTo(400, 120);
    ctx.stroke();
    ctx.font = '20px sans-serif';
    ctx.textBaseline = 'top';
    ctx.fillText('Top', 10, 120);
    ctx.textBaseline = 'bottom';
    ctx.fillText('Bottom', 55, 120);
    ctx.textBaseline = 'middle';
    ctx.fillText('Middle', 125, 120);
    ctx.textBaseline = 'alphabetic';
    ctx.fillText('Alphabetic', 195, 120);
    ctx.textBaseline = 'hanging';
    ctx.fillText('Hanging', 295, 120);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Br2MttYhR6a9CLE6nF07LQ/zh-cn_image_0000002821839417.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=6115CF0C42F881D6FC70B217B82FFC5F5D9C2D3E7C3319E8F24CE3FF948052A6)

### globalAlpha

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 50, 50);
    ctx.globalAlpha = 0.4;
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/cjdfpHxGT9WVbxucs6Yczw/zh-cn_image_0000002821759419.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9895CA9699FAB457B445812616FC3C8B2581CED3B19939769327E1715369C8E)

### lineDashOffset

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10, 20]);
    ctx.lineDashOffset = 10.0;
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/u1U5smLcQ0ed1GuWz2aeRQ/zh-cn_image_0000002793039488.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA629D4CA6B07C4A0B1F184569BCE32EF7BE353A0E50B4B783D2939012C95614)

### globalCompositeOperation

类型字段说明。

| 值 | 描述 |
| --- | --- |
| source-over | 在现有绘制内容上显示新绘制内容，属于默认值。 |
| source-atop | 在现有绘制内容顶部显示新绘制内容。 |
| source-in | 在现有绘制内容中显示新绘制内容。 |
| source-out | 在现有绘制内容之外显示新绘制内容。 |
| destination-over | 在新绘制内容上方显示现有绘制内容。 |
| destination-atop | 在新绘制内容顶部显示现有绘制内容。 |
| destination-in | 在新绘制内容中显示现有绘制内容。 |
| destination-out | 在新绘制内容外显示现有绘制内容。 |
| lighter | 显示新绘制内容和现有绘制内容。 |
| copy | 显示新绘制内容而忽略现有绘制内容。 |
| xor | 使用异或操作对新绘制内容与现有绘制内容进行融合。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 50, 50);
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);
    // Start drawing second example
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(120, 20, 50, 50);
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(150, 50, 50, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/muyHWt3TS_eauAwv_d8htw/zh-cn_image_0000002792879514.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DDA468E38FE91EF73F03A526D0AF245BC09556123097A7EF22F29EC8DB1FE03)

示例中，新绘制内容是蓝色矩形，现有绘制内容是红色矩形。

### shadowBlur

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/QDCcJjn5Q46KsRTJ_XBnug/zh-cn_image_0000002821839419.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9D7A1558E69A0505452C47156C2241AB5369BCF6C7E9E8DE8CBF4563A2A66B8)

### shadowColor

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,255)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/JzIKij_uSOuqyU7rDjCX9g/zh-cn_image_0000002821759421.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3E5D9E6C230AA0B2D7ABC6FAFF4344C0318DC0F9B83490578521418A2DCA83B)

### shadowOffsetX

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetX = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/fwzUWT50Svi2G5W21bKjqQ/zh-cn_image_0000002793039490.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=698F7E54D491249420024FBD96BD51CC18E0ECB28E14E29972C3D98C09F3C7BE)

### shadowOffsetY

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetY = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/DzbW-3eAT3a4XA7Y7HgJxQ/zh-cn_image_0000002792879516.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=336411BEDD5CDBF30442B08C2684E1A2414F68A6A69600726914C9EA1C3AAD7D)

### imageSmoothingEnabled

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/image/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/example.jpg';
    img.onload = function() {
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(img, 0, 0, 400, 200);
    };
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/qylvxygYQG2iUdDteWr0lg/zh-cn_image_0000002821839421.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2A2DA7DBECF837DFDE44F3886FE8492D1FECFC237590056D86A3354ACB2C0A3)

## 方法

### fillRect

fillRect(x: number, y: number, width:number, height: number): void

填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形左上角点的x坐标。  单位：vp |
| y | number | 是 | 指定矩形左上角点的y坐标。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

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
    ctx.fillRect(20, 20, 200, 150);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/e8KLIDz8RhGpnaOd1-mD7g/zh-cn_image_0000002821759423.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5C52CFE114AFE114C755D22C7667A12FC51DA8D8778E7420FABB6E2AFB6B238)

### clearRect

clearRect(x: number, y: number, width:number, height: number): void

删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形上的左上角x坐标。  单位：vp |
| y | number | 是 | 指定矩形上的左上角y坐标。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

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
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(100, 100, 200, 200);
    ctx.clearRect(110, 110, 80, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/8rq9UdFFS-219PdOKLSmuw/zh-cn_image_0000002793039492.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5E701DC0543DFF1761475F44D00F245819A4A4B66AA92224810D63567AF8887)

### strokeRect

strokeRect(x: number, y: number, width:number, height: number): void

绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标。  单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(100, 100, 200, 150);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/tHnmuk4TRj2I5oUOnkmF2g/zh-cn_image_0000002792879518.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4C6E76F857A35740DF2AEC74643F182A3B6414E3DBF25831D8AF34EE3AD5357)

### fillText

fillText(text: string, x: number, y: number): void

绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 需要绘制的文本的左下角x坐标。  单位：vp |
| y | number | 是 | 需要绘制的文本的左下角y坐标。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '35px sans-serif';
    ctx.fillText("Hello World!", 10, 60);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/fvTx6IQMQeeGsoRrApxW5w/zh-cn_image_0000002821839423.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BA7B461AC9F33074F8AC3B7D9376322B6E8989D3A5C474F6B5F967127458785)

### strokeText

strokeText(text: string, x: number, y: number): void

绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 需要绘制的文本的左下角x坐标。  单位：vp |
| y | number | 是 | 需要绘制的文本的左下角y坐标。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '25px sans-serif';
    ctx.strokeText("Hello World!", 10, 60);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/sCO_6JX-Ql6q97ZACDXZ6g/zh-cn_image_0000002821759425.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=C36862E15FCFA6C61A16EE961ACAC0A79E28DDE66A91B2175BC29C3B3A50C205)

### measureText

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TextMetrics | 包含指定字体的宽度，该宽度可以通过TextMetrics.width来获取。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '20px sans-serif';
    var txt = 'Hello World';
    ctx.fillText("width:" + ctx.measureText(txt).width, 20, 60);
    ctx.fillText(txt, 20, 110);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/PhB2oIaPR8C7iqTKcp_eLg/zh-cn_image_0000002793039494.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDA88799A57E9B3F635D17528250C08B414F93F0DC3CEC034D407827BADAD650)

### stroke

stroke(): void

进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(25, 25);
    ctx.lineTo(25, 250);
    ctx.lineWidth = 6;
    ctx.strokeStyle = 'rgb(0,0,255)';
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/rsHXgCLfR6i8TkKawfmbEw/zh-cn_image_0000002792879520.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=0163C1043C6F081430BA1618E0001F7615B5F18C2EB1077F9CBFDFB7627AED2E)

### beginPath

beginPath(): void

创建一个新的绘制路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = 6;
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(15, 80);
    ctx.lineTo(280, 80);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/-SehVCXNQwSslpE7w8MLgA/zh-cn_image_0000002821839425.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DB84AD095D9AA96CF2A27A4ED3314FF96CBF8BED0191A4EA2FF20C0B59E1A2C)

### moveTo

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  单位：vp |
| y | number | 是 | 指定位置的y坐标。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/5C-O8dkaR7KZbxEvuf7vMw/zh-cn_image_0000002821759427.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=99214B8F87F789F902805A1B69CE7F48276BB78D1A495B1F9943D38DC31A08C2)

### lineTo

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  单位：vp |
| y | number | 是 | 指定位置的y坐标。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/zkV6rsMiRBueC4Ojsu1Rag/zh-cn_image_0000002793039496.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAC5CA4CD1EED93E1E0B8D68B26FF2A628BB9E8A3F6770B5255D8EE4ADE9E9BF)

### closePath

closePath(): void

结束当前路径形成一个封闭路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(30, 30);
    ctx.lineTo(110, 30);
    ctx.lineTo(70, 90);
    ctx.closePath();
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/h1gjoVSlRFuhbywqW9m3Yw/zh-cn_image_0000002792879524.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D0F53732AA8197E14BBC800EA38A6E5B98FC8FE39C8259082F3A68081539C6A)

### createPattern

createPattern(image: Image, repetition: string): Object

通过指定图像和重复方式创建图片填充的模板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image | 是 | 图源对象，具体参考[Image对象](js-components-canvas-image.md)。 |
| repetition | string | 是 | 设置图像重复的方式，取值为：'repeat'、'repeat-x'、 'repeat-y'、'no-repeat'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 指定图像填充的Pattern对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 1000px; height: 1000px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/images/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/images/example.jpg';
    var pat = ctx.createPattern(img, 'repeat');
    ctx.fillStyle = pat;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/4_3vAapLQk-wlzMOtd5omA/zh-cn_image_0000002821839427.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=700F34D4B0090DBC61426F6A86B1ED544E36842546A803D8AE94B5CA9400FC5F)

### bezierCurveTo

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。  单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。  单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。  单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。  单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/002IUyExQz605LBAaOWIzg/zh-cn_image_0000002821759429.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB5589606C405EF0448868AC9214CD944D944B40F3A69E415568C79C1DFAC4D7)

### quadraticCurveTo

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。  单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。  单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(20, 20);
    ctx.quadraticCurveTo(100, 100, 200, 20);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/iE-CPdVuSdyyTOBQKWdGpA/zh-cn_image_0000002793039498.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7F39E774CD0FFC2B6D942490F41183B1C9BD8B50FA8204C8380FDE679B45F46)

### arc

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。  单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。  单位：vp |
| radius | number | 是 | 弧线的圆半径。  单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。  单位：弧度 |
| endAngle | number | 是 | 弧线的终止弧度。  单位：弧度 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧，true为逆时针，false为顺时针。  默认值：false |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/1-wv-ilySQa7QBmZaTjtVw/zh-cn_image_0000002792879526.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB280C4EC26B59A87C7594326567CBCFAC77FE8F8B82767AEB34EEAE730640D4)

### arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 圆弧经过的第一个点的x坐标值。  单位：vp |
| y1 | number | 是 | 圆弧经过的第一个点的y坐标值。  单位：vp |
| x2 | number | 是 | 圆弧经过的第二个点的x坐标值。  单位：vp |
| y2 | number | 是 | 圆弧经过的第二个点的y坐标值。  单位：vp |
| radius | number | 是 | 圆弧的圆半径值。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(100, 20);
    ctx.arcTo(150, 20, 150, 70, 50); // Create an arc
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/nmfS4wA9SKu5VOfX2S_pyw/zh-cn_image_0000002821839429.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=B983BD4E7E51AD2D3A524B6BEFAED145543FA1871A10F0EF0579354D6BD057F6)

### ellipse

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。  单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。  单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。  单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。  单位：vp |
| rotation | number | 是 | 椭圆的旋转角度。  单位：弧度 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。  单位：弧度 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。  单位：弧度 |
| counterclockwise | number | 否 | 是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。  默认值：0 |

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
    ctx.beginPath();
    ctx.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Z8UD7cRJQMei98XtPstmYw/zh-cn_image_0000002821759431.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=96236BB94435023956C27E10C0DA5C8C3236C4F29E4F30DA88D704A0281EE685)

### rect

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  单位：vp |
| width | number | 是 | 指定矩形的宽度。  单位：vp |
| height | number | 是 | 指定矩形的高度。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.stroke(); // Draw it
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/HJfR2h8DQiSrio39FQEVeg/zh-cn_image_0000002793039500.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=17A986185F7E32ADC1FD85B367D10656D5A98203BC301BEFD7D69311084F4D66)

### fill

fill(): void

对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.fill(); // Draw it in default setting
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/N3TRDe95TFWK0dJ7m6Dz0Q/zh-cn_image_0000002792879528.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F458EBE9FC7FB076AB9CF9F86CA7D319B3B1FDF8E7FD38B526E15C1A35F538B)

### clip

clip(): void

设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(100, 100, 200, 200);
    ctx.stroke();
    ctx.clip();
    // Draw red rectangle after clip
    ctx.fillStyle = "rgb(255,0,0)";
    ctx.fillRect(100, 100, 150, 150);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/mfJuTDOMQ22A0SEDbW1E6w/zh-cn_image_0000002821839433.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=95C4E47259B6E1DFD3EB29D37BDB0FBBE0A0FE13B03715732413A7BD035D7875)

### rotate

rotate(rotate: number): void

针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotate | number | 是 | 设置顺时针旋转的弧度值，可以通过Math.PI / 180将角度转换为弧度值。  单位：弧度 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rotate(45 * Math.PI / 180); // Rotate the rectangle 45 degrees
    ctx.fillRect(70, 20, 50, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/6V17Szz-QYGO6d_LcqyWNQ/zh-cn_image_0000002821759433.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=86E8B142FB308C1D90B76B69B73F40E398781848B89B52D11CD5B4CFDB2AAF13)

### scale

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平方向的缩放值。 |
| y | number | 是 | 设置垂直方向的缩放值。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(10, 10, 25, 25);
    ctx.scale(2, 2);// Scale to 200%
    ctx.strokeRect(10, 10, 25, 25);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/0J7sDv8bSbilZgOIWBVmJg/zh-cn_image_0000002793039502.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=36364A44CE9615D0BBF03BCBB84F351AF74C261B22B82EEFDE9DA1AD8B194756)

### transform

transform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

transform方法对应一个变换矩阵，当需要对一个图形进行变换的时候，只要设置此变换矩阵相应的参数，对图形的各个顶点的坐标分别乘以这个矩阵，就能得到新的顶点的坐标。矩阵变换效果可叠加。

**说明** 

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

* x' = scaleX \* x + skewY \* y + translateX
* y' = skewX \* x + scaleY \* y + translateY

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。 |
| skewX | number | 是 | 指定水平倾斜值。 |
| skewY | number | 是 | 指定垂直倾斜值。 |
| scaleY | number | 是 | 指定垂直缩放值。 |
| translateX | number | 是 | 指定水平移动值。  单位：vp |
| translateY | number | 是 | 指定垂直移动值。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(0,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/49j3EQsLS0C2NGVigqm-Jw/zh-cn_image_0000002792879530.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E95F9E137F0885077529393BA86347EC335FD09FC319E5F59D55C9D3697A187)

### setTransform

setTransform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。 |
| skewX | number | 是 | 指定水平倾斜值。 |
| skewY | number | 是 | 指定垂直倾斜值。 |
| scaleY | number | 是 | 指定垂直缩放值。 |
| translateX | number | 是 | 指定水平移动值。  单位：vp |
| translateY | number | 是 | 指定垂直移动值。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.setTransform(1,0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/5QH7ZVfsRrqagjjqBxS2GA/zh-cn_image_0000002821839435.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD1E8C0C9B2343E1CBB372E952BD0C1CA0F1412C7E3FBB513E7975E7F7B71481)

### translate

translate(x: number, y: number): void

移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平平移量。  单位：vp |
| y | number | 是 | 设置竖直平移量。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(10, 10, 50, 50);
    ctx.translate(70, 70);
    ctx.fillRect(10, 10, 50, 50);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/UCg7IN2vQPWq8m4WrjO0Sg/zh-cn_image_0000002821759435.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=BED234393C28B60A81704CE2FA005929CF3C94FC809423A1A5D1363D4ED4AC7E)

### createPath2D

createPath2D(path?: Path2D): Path2D

创建一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 否 | Path2D对象。  默认值：空的Path2D对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Path2D | 返回创建的[Path2D对象](js-components-canvas-path2d.md)。 |

### createPath2D

createPath2D(cmds?: string): Path2D

创建一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cmds | string | 否 | SVG的Path描述字符串。  默认值：""。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Path2D | 返回创建的[Path2D对象](js-components-canvas-path2d.md)。 |

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
    var path1 = ctx.createPath2D();
    path1.moveTo(100, 100);
    path1.lineTo(200, 100);
    path1.lineTo(100, 200);
    path1.closePath();
    ctx.stroke(path1);
    var path2 = ctx.createPath2D("M150 150 L50 250 L250 250 Z");
    ctx.stroke(path2);
    var path3 = ctx.createPath2D(path2);
    ctx.stroke(path3);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/ltMDUJ7xTmCx6JXw6zd4Kg/zh-cn_image_0000002793039504.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0AF0D3C7A5B9F704C757187D0B0EA5AD657A3C9A3B493250F757DFCAA5F0E07)

### drawImage

drawImage(image: Image | PixelMap, sx: number, sy: number, sWidth: number, sHeight: number, dx: number, dy: number, dWidth: number, dHeight: number):void

进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image | PixelMap9+ | 是 | 图片资源，请参考[Image对象](js-components-canvas-image.md) 或[PixelMap](arkts-apis-image-pixelmap.md)对象。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。  单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。  单位：vp |
| sWidth | number | 是 | 裁切源图像时需要裁切的宽度。  单位：vp |
| sHeight | number | 是 | 裁切源图像时需要裁切的高度。  单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  单位：vp |
| dy | number | 是 | 绘制区域左上角在y 轴的位置。  单位：vp |
| dWidth | number | 是 | 绘制区域的宽度。  单位：vp |
| dHeight | number | 是 | 绘制区域的高度。  单位：vp |

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
    var test = this.$refs.canvas;
    var ctx = test.getContext('2d');
    var img = new Image();
    // 'common/image/test.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/test.jpg';
    ctx.drawImage(img, 0, 0, 200, 200, 10, 10, 200, 200);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/AkuIxoE2SLO7lR0Z7xldog/zh-cn_image_0000002792879532.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E16037DCF048F5C9EA65617D2090FEF9F0C705EDE9B9BD860E6BD8751480E41)

### restore

restore(): void

对保存的绘图上下文进行恢复。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.restore();
  }
}
```

### save

save(): void

对当前的绘图上下文进行保存。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.save();
  }
}
```

### createLinearGradient6+

createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient

创建一个线性渐变色，返回[CanvasGradient对象](js-components-canvas-canvasgradient.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起点的x轴坐标。  单位：vp |
| y0 | number | 是 | 起点的y轴坐标。  单位：vp |
| x1 | number | 是 | 终点的x轴坐标。  单位：vp |
| y1 | number | 是 | 终点的y轴坐标。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CanvasGradient | 返回创建的CanvasGradient对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```js
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Linear gradient: start(50,0) end(300,100)
    var gradient = ctx.createLinearGradient(50,0, 300,100);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/o3mr3xYHQFiiwBzS6yFFSQ/zh-cn_image_0000002821839437.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B96A911AEC24973F412C29694F778AECD6ECB436B9C748F7C58349052FD97C0)

### createRadialGradient6+

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient

创建一个径向渐变色，返回[CanvasGradient对象](js-components-canvas-canvasgradient.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起始圆的x轴坐标。  单位：vp |
| y0 | number | 是 | 起始圆的y轴坐标。  单位：vp |
| r0 | number | 是 | 起始圆的半径。必须是非负且有限的。  单位：vp |
| x1 | number | 是 | 终点圆的x轴坐标。  单位：vp |
| y1 | number | 是 | 终点圆的y轴坐标。  单位：vp |
| r1 | number | 是 | 终点圆的半径。必须为非负且有限的。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CanvasGradient | 返回创建的CanvasGradient对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```js
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Radial gradient: inner circle(200,200,r:50) outer circle(200,200,r:200)
    var gradient = ctx.createRadialGradient(200,200,50, 200,200,200);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/9Gz20jPRTKGfg6Zo1fK8jw/zh-cn_image_0000002821759437.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F5B41A40ACD0ED80D87E1766539F984A6819B959096326F45C68C8661E816F5)

### createImageData

createImageData(width: number, height: number): ImageData

创建新的、空白的、指定大小的ImageData对象，请参考[ImageData对象](js-components-canvas-imagedata.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | ImageData的宽度。  单位：vp |
| height | number | 是 | ImageData的高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](js-components-canvas-imagedata.md) | 返回创建的ImageData对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
  }
}
```

### createImageData

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象，重新创建一个宽、高相同但不会复制图像数据的ImageData对象，请参考[ImageData对象](js-components-canvas-imagedata.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](js-components-canvas-imagedata.md) | 是 | 复制现有的ImageData对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](js-components-canvas-imagedata.md) | 返回创建的ImageData对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
    var newImageData = ctx.createImageData(imageData);  // Create ImageData using the input imageData
  }
}
```

### getImageData

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData对象](js-components-canvas-imagedata.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。  单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。  单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。  单位：vp |
| sh | number | 是 | 需要输出的区域的高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](js-components-canvas-imagedata.md) | 返回包含指定区域像素的ImageData对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="getImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const test = this.$element('getImageData')
    const ctx = test.getContext('2d');
    var imageData = ctx.getImageData(0, 0, 280, 300);
  }
}
```

### putImageData

putImageData(imageData: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void

使用ImageData数据裁剪后填充至新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](js-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 填充区域在x轴方向的偏移量。  单位：vp |
| dy | number | 是 | 填充区域在y轴方向的偏移量。  单位：vp |
| dirtyX | number | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。  单位：vp |
| dirtyY | number | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。  单位：vp |
| dirtyWidth | number | 是 | 源图像数据矩形裁切范围的宽度。  单位：vp |
| dirtyHeight | number | 是 | 源图像数据矩形裁切范围的高度。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #D5D5D5;"></canvas>
</div>
```

```js
// xxx.js
export default {
    onShow() {
        const test = this.$element('putImageData')
        const ctx = test.getContext('2d');
        var imgData = ctx.createImageData(100, 100);
        for (var i = 0; i < imgData.data.length; i += 4) {
            imgData.data[i + 0] = 39;
            imgData.data[i + 1] = 135;
            imgData.data[i + 2] = 217;
            imgData.data[i + 3] = 255;
        }
        ctx.putImageData(imgData, 10, 10, 0, 0, 100, 50);
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/euBs8H4bTUib-Sv0CtehnQ/zh-cn_image_0000002793039506.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E1A0E4EA6EA741DED8B58FD6F4251C77207D17E2BED2F718A41D3D68E2A1136)

### putImageData

putImageData(imageData: ImageData, dx: number, dy: number): void

使用ImageData数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](js-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 填充区域在x轴方向的偏移量。  单位：vp |
| dy | number | 是 | 填充区域在y轴方向的偏移量。  单位：vp |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const test = this.$element('putImageData')
    const ctx = test.getContext('2d');
    var imgData = ctx.createImageData(100, 100);
    for (var i = 0; i < imgData.data.length; i += 4) {
      imgData.data[i + 0] = 255;
      imgData.data[i + 1] = 0;
      imgData.data[i + 2] = 0;
      imgData.data[i + 3] = 255;
  }
  ctx.putImageData(imgData, 10, 10);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/D4DcBhFgTwq5V4q2D8zB-w/zh-cn_image_0000002792879534.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=659B11B06778C2274519995882FCDC56F7428F16A8BC97AAEED9E1762B18B2B8)

### getPixelMap9+

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

获取用当前canvas指定区域内的像素创建的PixelMap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 指定区域的左上角x坐标。  单位：vp |
| sy | number | 是 | 指定区域的左上角y坐标。  单位：vp |
| sw | number | 是 | 指定区域的宽度。  单位：vp |
| sh | number | 是 | 指定区域的高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 返回包含指定区域像素的PixelMap对象。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas id="canvasId" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const test = this.$element('canvasId')
    const ctx = test.getContext('2d');
    var pixelMap = ctx.getPixelMap(0, 0, 280, 300);
  }
}
```

### setLineDash

setLineDash(segments: Array<number>): void

设置画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segments | Array<number> | 是 | 作为数组用来描述线段如何交替和间距长度。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10, 20]);
    ctx.stroke();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Lmo_T89KQLKuuMwmn-jU5g/zh-cn_image_0000002821839439.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=191C147D62FBE9048DE398B71CD07A78814E9525CD79AF5E3CAC0971F9FE3BE5)

### getLineDash

getLineDash(): Array<number>

获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回数组，该数组用来描述线段如何交替和间距长度。 |

**示例：**

```html
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```js
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var info = ctx.getLineDash();
  }
}
```

### transferFromImageBitmap7+

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的[ImageBitmap对象](js-components-canvas-imagebitmap.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitmap | [ImageBitmap](js-components-canvas-imagebitmap.md) | 是 | 待显示的ImageBitmap对象。 |

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
    var canvas = this.$refs.canvas.getContext('2d');
    var offscreen = new OffscreenCanvas(500, 500);
    var offscreenCanvasCtx = offscreen.getContext("2d");
    offscreenCanvasCtx.fillRect(0, 0, 200, 200);

    var bitmap = offscreen.transferToImageBitmap();
    canvas.transferFromImageBitmap(bitmap);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/QKT8Vp8BSwWB716ZTimwWg/zh-cn_image_0000002821759439.png?HW-CC-KV=V1&HW-CC-Date=20261121T011422Z&HW-CC-Expire=31536000000&HW-CC-Sign=D305A95EAC8E3FE1C9DCADF2B254EE5DFA37A2E5D97FD09F14D63F52DF98CA75)
