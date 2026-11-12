---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:52278920dfba9e8a07caa03ee3e6664c0a137ce8bdafb2bbca5c453c9553d00a
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/QdhcNOkRR6SYk64KukWaBA/zh-cn_image_0000002815561185.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=98C9283C595A34B2E8BDB402646832CF4DEDFF7602010D58BD2688984F157F61)
* 示意图（开启抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/9UVjs9LDReCePOS_QJXMnA/zh-cn_image_0000002815401269.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA5E3E27F1FCFDCE765CF3E15FABB9E0B3F77C325D97BD2236A212B879670510)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/hudWWr33Qpe2aonN0fZaBg/zh-cn_image_0000002786521694.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=55C2130BF2EC5E64B3FF430A116F3840EC9A49CBF7BA04E40432C905F0E987B5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/GESiyQfNR7uX_WihNZtacg/zh-cn_image_0000002786361766.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=F53B332785B34192CCB1B106CE4586ECB66E457296FBBAB2D6923C23280E3E50)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/yQxwLG5FTsuEQ7MpJd2Qyw/zh-cn_image_0000002815561187.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=B42954FD51BAAC40F5F094456382B507BFEF178861C7F626EF856ECEA197D515)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/59lzYkdQRZCJGG6VOTVtmQ/zh-cn_image_0000002815401271.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=A624C14A72F51DD246731606568EE8E03AACCDCE8C1BC8E5E29FB7020B87B154)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mjFtYdljR-CT_zIdJH65lA/zh-cn_image_0000002786521696.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=20BAFA557BB31EBAB6F9FF54586E76DF41517EC0B768F9B5228155A2BC6B61BD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/xiyK0198ROKka3hciM-5UQ/zh-cn_image_0000002786361768.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC182096776829DC717A54736BD3D91904245573B1AB8180505D61C32235D29D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/wi-8dAbXT4ObE7OpYRRJgA/zh-cn_image_0000002815561189.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD52EB9E2D8719EC0A1B6D4CA3911D2D887B07B752F4FF0181A6F2B21B09F8AB)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/zg5mSrbiS3WKrqjJFzN19g/zh-cn_image_0000002815401273.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=70DB7D6E7ED2EA47267D094888B4636DF3C2BEB86C2E48C3CBE91F5B7F9AC5C9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/5Vl3Qk4HRxuxof_my0CkrQ/zh-cn_image_0000002786521698.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=25D3DA72B399F9D95D8A5F66810DD413ACB789968DD625DE1B80F9A8C7B35C55)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/uLJBFjhnSbGkrwNSCzQnPQ/zh-cn_image_0000002786361770.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=920DF8F38277EB1C396A66AA47646295629BC9AD3F0691B0BBDCADC2BF0CD6CA)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/tU-o2ocoTIyiC8d_a7DG2w/zh-cn_image_0000002815561191.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=01713145603DF7C4D069B7066006C5D5085C656C797050F5BF40DD8FFD81FD56)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/rRDIS6jlTQ2OEY3hjHq_Ig/zh-cn_image_0000002815401275.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEB29C77A9F25548C99A919C947500D61C69DFF8E8097D6DA30294235294F57C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/1jhxbf2WTEO1Jt61VQodBQ/zh-cn_image_0000002786521700.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA3DBDFF0FF22BD9BDBAD8840FF4E06D95044CE1DEF9C4711716C56234D259F8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/plwaEkgVRPKTffGm0RYOxg/zh-cn_image_0000002786361772.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=E58F70B10F4BFB8FD0071A530609F399257F1210A10414064DCD083055D9354F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/fn1QIVuSRsGrdAe7fYAUGA/zh-cn_image_0000002815561193.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E2B3A8386426951D5C3B2E219C0C3E0FE5D7223B334D90893F23F321D1C51C9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/8nvJWl1qS327cJi2nWd6HA/zh-cn_image_0000002815401277.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=C799C1D8A9A153E3D867A6CA476DA7E0EAA6AA97B078585BA9CF2A5D6CB65040)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/-0njMDlDTNWCQUD7aq58vA/zh-cn_image_0000002786521702.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEEA1BB5DCAC9F3D5D2C5BEFA84B87DD1A1B374DC6799955CB0049465593CE93)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ovcf6TMHSESNltPV9_kJeA/zh-cn_image_0000002786361774.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CA763B4EA93965CF6B4788F205D44577D4547D9C83259DBB18CFFF2058058F3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/hK2S2rgFQG2OrFks3iC7rg/zh-cn_image_0000002815561195.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8AD639E0DAF4EEF4ECA76733230AF25F05CA1B3F37F5BAD6083E6AE758AE057)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/kPCWnbE4Qt2l2FC3toUs6g/zh-cn_image_0000002815401279.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3D29171CA6E60CC82FAFDFC1084C4B5C07A5C571E580BF7C0BCA7DC3E67E4CD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/_XyAIRgKTUerwuFLe_GiHA/zh-cn_image_0000002786521704.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=09098F52EA7B9AEE660232FB50E38F08B091D7752F68C629C0114B63F1482A33)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/qePd7Q_xTBCs2X40NNaMDw/zh-cn_image_0000002786361776.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=538CD6A76FDB56BBE1578C704B63D85FE01419BE9DDC87E4ECCFA9A3E17C5015)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/aCU6bO5IRWWWvkNUB1KDtw/zh-cn_image_0000002815561197.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=A267BF4123319346895BB3A6E1DD9F836C63BC77BFE9EEF33B63B315F0C3F0CA)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/ynQHVhSHQjOvbMUoW8GAwQ/zh-cn_image_0000002815401281.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C100AA78FB2FD9AD8FF4B2A01330909ED4BE454C5E12CEA98A5B65540D53B1A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Cs0L5bgVRKevyeBrZogBBQ/zh-cn_image_0000002786521706.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BCB17914688FBDDBEE6C220ADA02480B0241B42D04D134CD6785811B0357063)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/WZqUQhGXSKOUFtAZY0J5LA/zh-cn_image_0000002786361778.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=39D7ACA3A203C5C5477AD763C1D0460CDA95EE324E637E74DF41DF425F964437)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/xDOFzd47S_ikVA7-9r9SMw/zh-cn_image_0000002815561199.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6112EBAE056C663EBF6166C7D4D229BB272114213FACB525029AE6DFEBDC6BA9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/DQJyuRw4QXO-IxhAp1ntfg/zh-cn_image_0000002815401283.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=1749FF874C8640ABB27E6590CCCB1464098D782E97ECF5AE4D1CDD0CFB7F6EE4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/P5wh4dPeS_2sGbe1WEMjLg/zh-cn_image_0000002786521708.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DACB60505D75D7BBBCF42B9ED7140009D6EC268645AD2E19E3E9B3FAD82BFB7)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/80Abxe1ETceMIPbyhPMV8w/zh-cn_image_0000002786361780.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA49D89536CB5D4A499E2C09629C860AA2059F1A91C0726BAE6B9BEC752E87D3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ieZyo-tMQ26xgieu8FlGEQ/zh-cn_image_0000002815561201.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=530EB66FD34F6799B048E66BFCAA03EC28122A1443519D4DCBC66065CBF747EE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Ww0RHQ2JQYmZ2P9pS-Ymsg/zh-cn_image_0000002815401285.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=416BF28194BBC3E81D1F8CF62D95CBCC99554C5E6F0BCEA75B47270F2121C2C6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/qfKt4CLxRQGkQXkDekv9AA/zh-cn_image_0000002786521710.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0863A94925B015C43629C1DAAA80B26B797BF8EC12E3930CF0970D06415AF65)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/o9M7M0sERTOKfv733iHLfA/zh-cn_image_0000002786361782.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8233E9B482ED6242E6C562E93D7CB2A6A178D68364CBC269D1A530209AD1A37)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/kW0U0Rf_QbaAnAd_bg-9Nw/zh-cn_image_0000002815561203.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=394F9A644663AF2A51984927826F5FD996808DE976789455A79732361FAB3456)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/izAjuoeMRQG-_ryJBqbsYQ/zh-cn_image_0000002815401287.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA206A34491F0B19ECD2E4A45870F9D6F7DB8A687CE739E6D588ECB60BF4F0E8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/_2VOlBtSThu9JXB_zbRL_w/zh-cn_image_0000002786521712.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=42563123AFF9833035965529D48795819515FC2A87BED17160A2FCC868D7234A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Kzz4_YVcRGaX8luTIzB1AA/zh-cn_image_0000002786361784.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B0B95397E59ACE1110BDEAA86DA60884D51A392807C49ED29956F339F0A5803)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/STuwACX3T3KL49kuldX_dw/zh-cn_image_0000002815561205.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=62F17E9C203C848DF7511A28B82D962680BC5FBD2D5D510D12479E3E767F204B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/pQybOMCkTWe9NPUYbnS6Hw/zh-cn_image_0000002815401289.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7506E3AB8421F4B524340FA71AC31525CE165FA744A2CA661A46B3ECC014031)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/KIzGfs04T7WLsm1vJkJgug/zh-cn_image_0000002786521714.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FD36E5DADE7DD4FC3D5ECD3B17B284CA04E96B1D3320EA92DD318F78C8C5452)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/8353qf3YRWiWHrQi63nviA/zh-cn_image_0000002786361786.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=292D90AC00A82CC702D5F1C57F0568D7F2D1868096869CF027F668B3530D1658)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/fMpUMY6zTAy9hheEBnDp-g/zh-cn_image_0000002815561207.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=33D1C9B50F526112F65638D9CC9D18EFAEB88C1E9A0D3E06A17E1E9D1EB2AF28)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/3Hc5OJLsTB2BGx9jjYRu8w/zh-cn_image_0000002815401291.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0619400B43CC55F8C60EF8879CA9116C6244224CA3340F3AC2300906856D51A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/3Ae4eFCYQje8aTHmFHdHHQ/zh-cn_image_0000002786521716.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=32F1D3305D8041700F2C66F3AD4D74ED350238C3CC7A18E02A64C2F2E72916AC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/up2YFFa2QeSbb66fE1Lgdg/zh-cn_image_0000002786361788.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=519DF6238C7F5CB3B0C85D79E5C05ED7292A9B916B806D21A4FAC0F3E4D4D451)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/6JgpLNLETlWYa9GMBn6OOQ/zh-cn_image_0000002815561209.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FDFFCF40D0497DCC48672F2C212E819CC7D9D44457DD39263764B1B670B70D4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ST-us26GSOCd4UJ4yX-EUA/zh-cn_image_0000002815401293.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=255D809BD2AA2328DDBF39DB88C3CD89EF80828B065234EFBD72B149BB851B72)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/MzXiYb8cQIKbnOz84ujgyQ/zh-cn_image_0000002786521718.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5434CD16BBAA651475F7E0E59F0C99CA943693AD8B735090A74233472D6394C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/T95uquABTTmUaNqJi0z2HQ/zh-cn_image_0000002786361790.png?HW-CC-KV=V1&HW-CC-Date=20261112T233239Z&HW-CC-Expire=31536000000&HW-CC-Sign=09C74EA400F96B1E6E6CF7A748C43EF94A0B7505800E060AB865BE92CBB42542)
