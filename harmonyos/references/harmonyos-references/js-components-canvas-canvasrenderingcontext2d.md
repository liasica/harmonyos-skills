---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-04-29T13:53:32+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:785264c8f8fc0ca525347b381aae725e0e2a02f3ca8845a49569b78365e793cb
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用CanvasRenderingContext2D在[canvas画布组件](js-components-canvas-canvas.md)上进行绘制，绘制对象可以是矩形、文本、图片等。

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="handleClick" onclick="handleClick" />
5. <input type="button" style="width: 180px; height: 60px;" value="antialias" onclick="antialias" />
6. </div>
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
10. antialias() {
11. const el = this.$refs.canvas1;
12. const ctx = el.getContext('2d', { antialias: true });
13. ctx.beginPath();
14. ctx.arc(100, 75, 50, 0, 6.28);
15. ctx.stroke();
16. }
17. }
```

* 示意图（关闭抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/perSqYmYQfaITb0SDbVxFA/zh-cn_image_0000002589326597.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=4849D6DEE774F62CAF2E957046CA78498BD35E89B7C4FD1245FA5CA87FD78A5C)
* 示意图（开启抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/w9nMD19nSbKgDtdWZTkWBw/zh-cn_image_0000002589246539.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=73E362D2B8508C51F399C5D7D893A218B194E4BA13D444193835F2067C20F4CB)

## 属性

PhonePC/2in1TabletTVWearable

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
| [textBaseline](js-components-canvas-canvasrenderingcontext2d.md#textbaseline) | string | 设置文本绘制中的水平对齐方式，可选值为：  - alphabetic：文本基线是标准的字母基线。  - top：文本基线在文本块的顶部。  - hanging：文本基线是悬挂基线。  - middle：文本基线在文本块的中间。  - ideographic：文字基线是表意字基线；如果字符本身超出了alphabetic 基线，那么ideographic基线位置在字符本身的底部。  - bottom：文本基线在文本块的底部。 与 ideographic 基线的区别在于 ideographic 基线不需要考虑下行字母。  默认值： alphabetic |
| [globalAlpha](js-components-canvas-canvasrenderingcontext2d.md#globalalpha) | number | 设置透明度。  范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。 |
| [lineDashOffset](js-components-canvas-canvasrenderingcontext2d.md#linedashoffset) | number | 设置画布的虚线偏移量，精度为float。  默认值：0.0 |
| [globalCompositeOperation](js-components-canvas-canvasrenderingcontext2d.md#globalcompositeoperation) | string | 设置合成操作的方式。类型字段可选值有source-over，source-atop，source-in，source-out，destination-over，destination-atop，destination-in，destination-out，lighter，copy，xor。具体请参考[类型字段说明](js-components-canvas-canvasrenderingcontext2d.md#globalcompositeoperation)。  默认值：source-over |
| [shadowBlur](js-components-canvas-canvasrenderingcontext2d.md#shadowblur) | number | 设置绘制阴影时的模糊级别，值越大越模糊，精度为float。  默认值：0.0 |
| [shadowColor](js-components-canvas-canvasrenderingcontext2d.md#shadowcolor) | <color> | 设置绘制阴影时的阴影颜色。 |
| [shadowOffsetX](js-components-canvas-canvasrenderingcontext2d.md#shadowoffsetx) | number | 设置绘制阴影时和原有对象的水平偏移值。 |
| [shadowOffsetY](js-components-canvas-canvasrenderingcontext2d.md#shadowoffsety) | number | 设置绘制阴影时和原有对象的垂直偏移值。 |
| [imageSmoothingEnabled](js-components-canvas-canvasrenderingcontext2d.md#imagesmoothingenabled) | boolean | 用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。  默认值：true |

### fillStyle

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = '#0000ff';
7. ctx.fillRect(20, 20, 150, 100);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Pxi6H9w7TNCtrqrAKqOxLQ/zh-cn_image_0000002558766732.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=B5AA36B6054FF38739558942A59DDD632D77D79B6081D57EA4550CB821F47078)

### lineWidth

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth = 5;
7. ctx.strokeRect(25, 25, 85, 105);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/BQELtQygT5aSeVzE-9SjbQ/zh-cn_image_0000002558607072.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=8B8EE2BC795DCD7510F59EF745A0F2FB8EB1B13351E3324FC3B532ACF57B657F)

### strokeStyle

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth = 10;
7. ctx.strokeStyle = '#0000ff';
8. ctx.strokeRect(25, 25, 155, 105);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/6omq5q8kSlm7FoeW51kOSw/zh-cn_image_0000002589326599.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=21047DBB6825968706FF204F916F53DB77EB1B02E2FEDDCD50C9365F5EFD1FB9)

### lineCap

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth = 8;
7. ctx.beginPath();
8. ctx.lineCap = 'round';
9. ctx.moveTo(30, 50);
10. ctx.lineTo(220, 50);
11. ctx.stroke();
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/GCjuBrxBTrSEcEyemYKEeA/zh-cn_image_0000002589246541.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=30C78022CEA7DCEEB52F1436F702FEC5FB8D1EBADDC74CAE1E435930623412DD)

### lineJoin

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.lineWidth = 8;
8. ctx.lineJoin = 'miter';
9. ctx.moveTo(30, 30);
10. ctx.lineTo(120, 60);
11. ctx.lineTo(30, 110);
12. ctx.stroke();
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/EWuspKCTRDW6xNZm6A1B-w/zh-cn_image_0000002558766734.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=FEAC674F7E81D3D65135F81D922331729AD821040F1702F1B623AB98E7F730CE)

### miterLimit

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.lineWidth =14;
7. ctx.lineJoin = 'miter';
8. ctx.miterLimit = 3;
9. ctx.moveTo(30, 30);
10. ctx.lineTo(120, 60);
11. ctx.lineTo(30, 70);
12. ctx.stroke();
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Kpd-ACosTCCDZ6rTHSz4_Q/zh-cn_image_0000002558607074.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=056CFCD626DB5C811AE56DE58C5D64BAF8B55CF9F23307963F24FF05B0D5046A)

### font

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '30px sans-serif';
7. ctx.fillText("Hello World", 20, 60);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/6QwroxwyTlqaUMUnVX-0cA/zh-cn_image_0000002589326601.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=B24D0A24D1656A9FB88C5EDBF5D2E3EAD98F08400E9A3F845EB7E28C9C908A91)

### textAlign

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeStyle = '#0000ff';
7. ctx.moveTo(140, 10);
8. ctx.lineTo(140, 160);
9. ctx.stroke();
10. ctx.font = '18px sans-serif';
11. // Show the different textAlign values
12. ctx.textAlign = 'start';
13. ctx.fillText('textAlign=start', 140, 60);
14. ctx.textAlign = 'end';
15. ctx.fillText('textAlign=end', 140, 80);
16. ctx.textAlign = 'left';
17. ctx.fillText('textAlign=left', 140, 100);
18. ctx.textAlign = 'center';
19. ctx.fillText('textAlign=center',140, 120);
20. ctx.textAlign = 'right';
21. ctx.fillText('textAlign=right',140, 140);
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/2dWupBI7TGCLWWK9trT-ZQ/zh-cn_image_0000002589246543.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=93E36F1FF751117F5015FE48E4676650C8DC6403A166EE4F9FB2CDAE815416C9)

### textBaseline

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeStyle = '#0000ff';
7. ctx.moveTo(0, 120);
8. ctx.lineTo(400, 120);
9. ctx.stroke();
10. ctx.font = '20px sans-serif';
11. ctx.textBaseline = 'top';
12. ctx.fillText('Top', 10, 120);
13. ctx.textBaseline = 'bottom';
14. ctx.fillText('Bottom', 55, 120);
15. ctx.textBaseline = 'middle';
16. ctx.fillText('Middle', 125, 120);
17. ctx.textBaseline = 'alphabetic';
18. ctx.fillText('Alphabetic', 195, 120);
19. ctx.textBaseline = 'hanging';
20. ctx.fillText('Hanging', 295, 120);
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/kxFXQIcuQeeD2OcVPm617w/zh-cn_image_0000002558766736.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=23F794DF02BFEB4FCF8A93F27DC815590310E0C072F127B8EFE626494B363D55)

### globalAlpha

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(255,0,0)';
7. ctx.fillRect(0, 0, 50, 50);
8. ctx.globalAlpha = 0.4;
9. ctx.fillStyle = 'rgb(0,0,255)';
10. ctx.fillRect(50, 50, 50, 50);

12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ecpkWH26SjapmHlC2J1V3A/zh-cn_image_0000002558607076.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=6AD448ADC2A4CCC6E1988C0361AB2FBF7D47781DAD827B42B2E3A4497BA09E49)

### lineDashOffset

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.arc(100, 75, 50, 0, 6.28);
7. ctx.setLineDash([10,20]);
8. ctx.lineDashOffset = 10.0;
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/rSIo2IiXTzKtXY5fLbxa7w/zh-cn_image_0000002589326603.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=067B572A41F04454F41F487EADF1448209F7FA35CA348C64C41A976EA7F8C292)

### globalCompositeOperation

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(255,0,0)';
7. ctx.fillRect(20, 20, 50, 50);
8. ctx.globalCompositeOperation = 'source-over';
9. ctx.fillStyle = 'rgb(0,0,255)';
10. ctx.fillRect(50, 50, 50, 50);
11. // Start drawing second example
12. ctx.fillStyle = 'rgb(255,0,0)';
13. ctx.fillRect(120, 20, 50, 50);
14. ctx.globalCompositeOperation = 'destination-over';
15. ctx.fillStyle = 'rgb(0,0,255)';
16. ctx.fillRect(150, 50, 50, 50);
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/_WZAaoTRRhqc9jCkO7KaEQ/zh-cn_image_0000002589246545.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=FAEBA08CEAEF3877E7B5E84861973DDA8C8DA606A4DCB92D1BA2EE0A78D1D6D2)

示例中，新绘制内容是蓝色矩形，现有绘制内容是红色矩形。

### shadowBlur

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 30;
7. ctx.shadowColor = 'rgb(0,0,0)';
8. ctx.fillStyle = 'rgb(255,0,0)';
9. ctx.fillRect(20, 20, 100, 80);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/m7rRH54oTwWJn8JEciMF-w/zh-cn_image_0000002558766738.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=B6FD853C85CFE14AD0F5A0AC7EE9A66A2A3226B6A8596D7E764E99D5FBB8FCEE)

### shadowColor

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 30;
7. ctx.shadowColor = 'rgb(0,0,255)';
8. ctx.fillStyle = 'rgb(255,0,0)';
9. ctx.fillRect(30, 30, 100, 100);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/QekcG8kKQQyZFQhwRJBpqQ/zh-cn_image_0000002558607078.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=9BF93135884DEF5BD6DD1479F4F866496E156EB36AD4148D43641CA35C39CD59)

### shadowOffsetX

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 10;
7. ctx.shadowOffsetX = 20;
8. ctx.shadowColor = 'rgb(0,0,0)';
9. ctx.fillStyle = 'rgb(255,0,0)';
10. ctx.fillRect(20, 20, 100, 80);
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/6KIqZkkFSFqIyumys3sRTQ/zh-cn_image_0000002589326605.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=C3E3F2E3C2C5AE81BAC92503384FE153FE25B504B825542AD5A4868868CFE041)

### shadowOffsetY

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.shadowBlur = 10;
7. ctx.shadowOffsetY = 20;
8. ctx.shadowColor = 'rgb(0,0,0)';
9. ctx.fillStyle = 'rgb(255,0,0)';
10. ctx.fillRect(30, 30, 100, 100);
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/dS1YKMOtTUGGpuBm_vB5_w/zh-cn_image_0000002589246547.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=35FDDECEB6E1836C55B62583D362581C753E838DCCFD89FF73E2F46652279521)

### imageSmoothingEnabled

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var img = new Image();
7. // 'common/image/example.jpg'需要替换为开发者所需的图像资源文件
8. img.src = 'common/image/example.jpg';
9. img.onload = function() {
10. ctx.imageSmoothingEnabled = false;
11. ctx.drawImage(img, 0, 0, 400, 200);
12. };
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/VsAP8YuTQwimMJzPO2CZ9A/zh-cn_image_0000002558766740.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=5D85C1EF871BB3AE53AEA0A386A0E0B0F499D1887FEAEC718A19519275A0EC9D)

## 方法

PhonePC/2in1TabletTVWearable

### fillRect

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillRect(20, 20, 200, 150);
7. }
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/9Wjz-wBeSYqMpy85Myanzw/zh-cn_image_0000002558607080.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=A7E874A2B1B8D2E670C9C3E0FF85247DFA8E6CFDA5FA6BC3C17CB64E1B68EF16)

### clearRect

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(0,0,255)';
7. ctx.fillRect(100, 100, 200, 200);
8. ctx.clearRect(110, 110, 80, 50);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/9Yw-R_mdQA-QL1HieQo55g/zh-cn_image_0000002589326607.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=9D28A7DBEE735F8C7FAA0B2A26FC205FB24FB9051F1F6A86FE46394B561392E6)

### strokeRect

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeRect(100, 100, 200, 150);
7. }
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/iZi2D_tDRbeGqgKYXhq0Ew/zh-cn_image_0000002589246549.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=2019D0CAEA75353FD675D379971E3054B9872DA573824F08B5E8BB794F06803C)

### fillText

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '35px sans-serif';
7. ctx.fillText("Hello World!", 10, 60);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/aUiwNj0hTv-ggx9iIoY3_A/zh-cn_image_0000002558766742.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=B5141DF1A5EED27C810C36DB9A2735713A5B179C7199952C9E9B5F37EE7E9FEF)

### strokeText

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '25px sans-serif';
7. ctx.strokeText("Hello World!", 10, 60);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/xMTF1U9ITHKcqvnu_E2TFQ/zh-cn_image_0000002558607082.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=AFD1C3D5F48153C89F2B4FF74C776A0CB1C99542D3BCB415F7C361235D48E64A)

### measureText

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.font = '20px sans-serif';
7. var txt = 'Hello World';
8. ctx.fillText("width:" + ctx.measureText(txt).width, 20, 60);
9. ctx.fillText(txt, 20, 110);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/R7ucG0GGSaiqmczn77iOeA/zh-cn_image_0000002589326609.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=5E22EE80A0F25FDE5F46F761CC9E96C58F06DDC41E7D9044F40523F575322A7A)

### stroke

PhonePC/2in1TabletTVWearable

stroke(): void

进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.moveTo(25, 25);
7. ctx.lineTo(25, 250);
8. ctx.lineWidth = '6';
9. ctx.strokeStyle = 'rgb(0,0,255)';
10. ctx.stroke();
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Inb0_-MPTbGyb27pp2omWg/zh-cn_image_0000002589246551.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=462BEB702762054CCA625BECB239CAAF3C3A62632A211E4F5CD89DE7820852BA)

### beginPath

PhonePC/2in1TabletTVWearable

beginPath(): void

创建一个新的绘制路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.lineWidth = '6';
8. ctx.strokeStyle = '#0000ff';
9. ctx.moveTo(15, 80);
10. ctx.lineTo(280, 80);
11. ctx.stroke();
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/n22kS4rJSrWgH43Nc36N8g/zh-cn_image_0000002558766744.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=BC70329F9E69BEF90E274D63A6024937BB3AE26ECCDA14898F79E0D28A57EE49)

### moveTo

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  单位：vp |
| y | number | 是 | 指定位置的y坐标。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(10, 10);
8. ctx.lineTo(280, 160);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/8Tyr1-XHSPe7pqNW8t2BBw/zh-cn_image_0000002558607084.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=89CC4A91E38508D4B337440661601ACC5FB954F789E496DC72681DB21B50A616)

### lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  单位：vp |
| y | number | 是 | 指定位置的y坐标。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(10, 10);
8. ctx.lineTo(280, 160);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/OWGkrBQvRr2hTnwe4jkU-w/zh-cn_image_0000002589326611.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=8DD1E645D9B5B29472A81A10D4875EC9DA7679C51EC64DCA3F32C85AC1FEC19E)

### closePath

PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径形成一个封闭路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(30, 30);
8. ctx.lineTo(110, 30);
9. ctx.lineTo(70, 90);
10. ctx.closePath();
11. ctx.stroke();
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/MfukOEaiTLepZ8KA1AjOrA/zh-cn_image_0000002589246553.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=05D1506FFBA02887B228F17713729BBEEE73A37005A275E9D9A58352482A4731)

### createPattern

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 1000px; height: 1000px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var img = new Image();
7. // 'common/images/example.jpg'需要替换为开发者所需的图像资源文件
8. img.src = 'common/images/example.jpg';
9. var pat = ctx.createPattern(img, 'repeat');
10. ctx.fillStyle = pat;
11. ctx.fillRect(0, 0, 500, 500);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/8ywax6hOShKamnlq6S_YHA/zh-cn_image_0000002558766746.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=7DA9689F34D3EBFE4562CEB7D748B7CB425D97DD7886F51AE182FDBE08DFDDA9)

### bezierCurveTo

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(10, 10);
8. ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/JZMuv6dLRwuIto1bUQo2TA/zh-cn_image_0000002558607086.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=A797E45171F66BD3FB1A233C40FCBEB5849C3C12CDE91712D2044B2D229F1EA1)

### quadraticCurveTo

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.moveTo(20, 20);
8. ctx.quadraticCurveTo(100, 100, 200, 20);
9. ctx.stroke();
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/TBVMiapWQWGRdp7hUWAIxA/zh-cn_image_0000002589326613.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=5545CDB0CC209CE16231C06B1C4D26ED5B42C2F4EFD3632FD4287B23CC48AA38)

### arc

PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。  单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。  单位：vp |
| radius | number | 是 | 弧线的圆半径。  单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。  单位：vp |
| endAngle | number | 是 | 弧线的终止弧度。  单位：vp |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧，true为逆时针，false为顺时针。  默认值：false |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.arc(100, 75, 50, 0, 6.28);
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/MMJ8Z0_4Q1-GVBLfUeH6kw/zh-cn_image_0000002589246555.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=59583314D90BFC3DDC41277CE1E7C19FB3374B415D77A5156719BD101B3CAC76)

### arcTo

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.moveTo(100, 20);
7. ctx.arcTo(150, 20, 150, 70, 50); // Create an arc
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/P_idtn-pS8aTOC86ta6zPw/zh-cn_image_0000002558766748.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=BF9D8BF277CC65B934866AAD521CF9FC2059FC2FB98C6F2A99DC3CE27CF61803)

### ellipse

PhonePC/2in1TabletTVWearable

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
| rotation | number | 是 | 椭圆的旋转角度，单位为弧度。  单位：vp |
| startAngle | number | 是 | 椭圆绘制的起始点角度，以弧度表示。  单位：vp |
| endAngle | number | 是 | 椭圆绘制的结束点角度，以弧度表示。  单位：vp |
| counterclockwise | number | 否 | 是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。  单位：vp  默认值：0 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.beginPath();
7. ctx.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/mQP1JHkBTJi515XewWt5Xg/zh-cn_image_0000002558607088.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=74F659807F68CC4DBFE7536364AFE1582D4161DC009E6A71BCCA5F77E9058667)

### rect

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
7. ctx.stroke(); // Draw it
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/68sGRo97T7q3U1n0FShDgg/zh-cn_image_0000002589326615.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=A05DB6857032737BF45442FFE35F7B935F600C04ECCF4FAE613E3921D6B34E86)

### fill

PhonePC/2in1TabletTVWearable

fill(): void

对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
7. ctx.fill(); // Draw it in default setting
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/xXzzeEWmQF2pxT8GNVW4eg/zh-cn_image_0000002589246557.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=ABBB28660E4565208F39FCD10EDF1868DB90138EFC4733D9DAB506B47CBB8AEC)

### clip

PhonePC/2in1TabletTVWearable

clip(): void

设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rect(100, 100, 200, 200);
7. ctx.stroke();
8. ctx.clip();
9. // Draw red rectangle after clip
10. ctx.fillStyle = "rgb(255,0,0)";
11. ctx.fillRect(100, 100, 150, 150);
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/bnQpRb5kTtiqvK7j4xmJtw/zh-cn_image_0000002558766750.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=263F14467365EAEDB46417AA6C69B180E2855AEC5B6499083F9A44623F706FF5)

### rotate

PhonePC/2in1TabletTVWearable

rotate(rotate: number): void

针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotate | number | 是 | 设置顺时针旋转的弧度值，可以通过Math.PI / 180将角度转换为弧度值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.rotate(45 * Math.PI / 180); // Rotate the rectangle 45 degrees
7. ctx.fillRect(70, 20, 50, 50);
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/6-NsHgQfQe6uQ41qbAkzzg/zh-cn_image_0000002558607090.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=0C8487FEA35401109DE2FE7A1E21B7B334549242C4610E1477674C92BDD3B554)

### scale

PhonePC/2in1TabletTVWearable

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平方向的缩放值。  单位：vp |
| y | number | 是 | 设置垂直方向的缩放值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.strokeRect(10, 10, 25, 25);
7. ctx.scale(2, 2);// Scale to 200%
8. ctx.strokeRect(10, 10, 25, 25);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/J0QAGeTLTnqodXoiC9E2bw/zh-cn_image_0000002589326617.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=4B432EC33DC9BF1475DCE32CAFA251049540B3572799D7EC4EF8DE7795580750)

### transform

PhonePC/2in1TabletTVWearable

transform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

说明

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

* x' = scaleX \* x + skewY \* y + translateX
* y' = skewX \* x + scaleY \* y + translateY

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。  单位：vp |
| skewX | number | 是 | 指定水平倾斜值。  单位：vp |
| skewY | number | 是 | 指定垂直倾斜值。  单位：vp |
| scaleY | number | 是 | 指定垂直缩放值。  单位：vp |
| translateX | number | 是 | 指定水平移动值。  单位：vp |
| translateY | number | 是 | 指定垂直移动值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(0,0,0)';
7. ctx.fillRect(0, 0, 100, 100);
8. ctx.transform(1, 0.5, -0.5, 1, 10, 10);
9. ctx.fillStyle = 'rgb(255,0,0)';
10. ctx.fillRect(0, 0, 100, 100);
11. ctx.transform(1, 0.5, -0.5, 1, 10, 10);
12. ctx.fillStyle = 'rgb(0,0,255)';
13. ctx.fillRect(0, 0, 100, 100);
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/AUbwT50YRQujcOg_p8t9sw/zh-cn_image_0000002589246559.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=E60B4F3277BA01151A24437A88BE2E018E08C3EFAD55E11BDA2B08E1F275B955)

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。  单位：vp |
| skewX | number | 是 | 指定水平倾斜值。  单位：vp |
| skewY | number | 是 | 指定垂直倾斜值。  单位：vp |
| scaleY | number | 是 | 指定垂直缩放值。  单位：vp |
| translateX | number | 是 | 指定水平移动值。  单位：vp |
| translateY | number | 是 | 指定垂直移动值。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillStyle = 'rgb(255,0,0)';
7. ctx.fillRect(0, 0, 100, 100);
8. ctx.setTransform(1,0.5, -0.5, 1, 10, 10);
9. ctx.fillStyle = 'rgb(0,0,255)';
10. ctx.fillRect(0, 0, 100, 100);
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/93XPBUTjRz6Plv1Jkvy5dQ/zh-cn_image_0000002558766752.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=3D58E98B2EC1556B610373350372D613B164E3B0B636D9A8309B947ABFB08EE6)

### translate

PhonePC/2in1TabletTVWearable

translate(x: number, y: number): void

移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平平移量。  单位：vp |
| y | number | 是 | 设置竖直平移量。  单位：vp |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.fillRect(10, 10, 50, 50);
7. ctx.translate(70, 70);
8. ctx.fillRect(10, 10, 50, 50);
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/tP-tZr3AQe-TnvJXl7IKFQ/zh-cn_image_0000002558607092.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=1C2C21340430033954173D31CD6A0EF6CD5B916BE8384AB690476D4F298067A7)

### createPath2D6+

PhonePC/2in1TabletTVWearable

createPath2D(path: Path2D, cmds: string): Path2D

创建一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | Path2D对象。 |
| cmds | string | 是 | SVG的Path描述字符串。 |

**返回值：**

[Path2D对象](js-components-canvas-path2d.md)

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var path1 = ctx.createPath2D();
7. path1.moveTo(100, 100);
8. path1.lineTo(200, 100);
9. path1.lineTo(100, 200);
10. path1.closePath();
11. ctx.stroke(path1);
12. var path2 = ctx.createPath2D("M150 150 L50 250 L250 250 Z");
13. ctx.stroke(path2);
14. var path3 = ctx.createPath2D(path2);
15. ctx.stroke(path3);
16. }
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/2Q_XTymeSdSaHRYwr1qxew/zh-cn_image_0000002589326619.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=B8D47A06E8C390CE6914B72E3CC2C107FFAC179C72CA45B91DAA63C76810A4C3)

### drawImage

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. var test = this.$refs.canvas;
5. var ctx = test.getContext('2d');
6. var img = new Image();
7. // 'common/image/test.jpg'需要替换为开发者所需的图像资源文件
8. img.src = 'common/image/test.jpg';
9. ctx.drawImage(img, 0, 0, 200, 200, 10, 10, 200, 200);
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/RnoJu0MfTOuchKsmS6LZvg/zh-cn_image_0000002589246561.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=7B6B9B799B1497C36A56A18D45A657F1991906428CBE81A8607157E088AAEBD3)

### restore

PhonePC/2in1TabletTVWearable

restore(): void

对保存的绘图上下文进行恢复。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.restore();
7. }
8. }
```

### save

PhonePC/2in1TabletTVWearable

save(): void

对当前的绘图上下文进行保存。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.save();
7. }
8. }
```

### createLinearGradient6+

PhonePC/2in1TabletTVWearable

createLinearGradient(x0: number, y0: number, x1: number, y1: number): Object

创建一个线性渐变色，返回CanvasGradient对象，请参考[CanvasGradient对象](js-components-canvas-canvasgradient.md)。

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
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
5. </div>
```

```
1. // xxx.js
2. export default {
3. handleClick() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. // Linear gradient: start(50,0) end(300,100)
7. var gradient = ctx.createLinearGradient(50,0, 300,100);
8. // Add three color stops
9. gradient.addColorStop(0.0, '#ff0000');
10. gradient.addColorStop(0.5, '#ffffff');
11. gradient.addColorStop(1.0, '#00ff00');
12. // Set the fill style and draw a rectangle
13. ctx.fillStyle = gradient;
14. ctx.fillRect(0, 0, 500, 500);
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/6ui0X1pfQsmZagthC9QHvQ/zh-cn_image_0000002558766754.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=DB8EBFAE06C4D6CAC30D7809855881BF754A493E50F1AFD4656CFD5F5D853126)

### createRadialGradient6+

PhonePC/2in1TabletTVWearable

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): Object

创建一个径向渐变色，返回CanvasGradient对象，请参考CanvasGradient。

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
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
5. </div>
```

```
1. // xxx.js
2. export default {
3. handleClick() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. // Radial gradient: inner circle(200,200,r:50) outer circle(200,200,r:200)
7. var gradient = ctx.createRadialGradient(200,200,50, 200,200,200);
8. // Add three color stops
9. gradient.addColorStop(0.0, '#ff0000');
10. gradient.addColorStop(0.5, '#ffffff');
11. gradient.addColorStop(1.0, '#00ff00');
12. // Set the fill style and draw a rectangle
13. ctx.fillStyle = gradient;
14. ctx.fillRect(0, 0, 500, 500);
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/OZfO98VvS1KstAC6fjp0ZA/zh-cn_image_0000002558607094.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=5CEA628A982473FAE0C75A91E59169B11171A9755FAFA40E262F25A46434FFEA)

### createImageData

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
7. }
8. }
```

### createImageData

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
7. var newImageData = ctx.createImageData(imageData);  // Create ImageData using the input imageData
8. }
9. }
```

### getImageData

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="getImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('getImageData')
5. const ctx = test.getContext('2d');
6. var imageData = ctx.getImageData(0, 0, 280, 300);
7. }
8. }
```

### putImageData

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #D5D5D5;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('putImageData')
5. const ctx = test.getContext('2d');
6. var imgData = ctx.createImageData(100, 100);
7. for (var i = 0; i < imgData.data.length; i += 4) {
8. imgData.data[i + 0] = 39;
9. imgData.data[i + 1] = 135;
10. imgData.data[i + 2] = 217;
11. imgData.data[i + 3] = 255;
12. }
13. ctx.putImageData(imgData, 10, 10, 0, 0, 100, 50);
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/NHCqRYeYTDe0sTl2Khrwug/zh-cn_image_0000002589326621.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=805FFE5F24C3F31B00B20CC5C9916B41879ABF38A77A39CE93AA05E1CB96F35B)

### putImageData

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('putImageData')
5. const ctx = test.getContext('2d');
6. var imgData = ctx.createImageData(100, 100);
7. for (var i = 0; i < imgData.data.length; i += 4) {
8. imgData.data[i + 0] = 255;
9. imgData.data[i + 1] = 0;
10. imgData.data[i + 2] = 0;
11. imgData.data[i + 3] = 255;
12. }
13. ctx.putImageData(imgData, 10, 10);
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/YlnFBVV3Tjy5c1_mJep6hQ/zh-cn_image_0000002589246563.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=947769BB27F5AA9E0DC896D489A1DDD19AFC428D8D401BF04D4910763A9A9269)

### getPixelMap9+

PhonePC/2in1TabletTVWearable

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

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas id="canvasId" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const test = this.$element('canvasId')
5. const ctx = test.getContext('2d');
6. var pixelMap = ctx.getPixelMap(0, 0, 280, 300);
7. }
8. }
```

### setLineDash

PhonePC/2in1TabletTVWearable

setLineDash(segments: Array): void

设置画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segments | Array | 是 | 作为数组用来描述线段如何交替和间距长度。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. ctx.arc(100, 75, 50, 0, 6.28);
7. ctx.setLineDash([10,20]);
8. ctx.stroke();
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/1jfSjcXoTk2m7_KROQPgvA/zh-cn_image_0000002558766756.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=EDB3FF5EED9F06B4873CFFEE1AD94B5F9B553CE452997C8030DC9080A878D339)

### getLineDash

PhonePC/2in1TabletTVWearable

getLineDash(): Array

获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array | 返回数组，该数组用来描述线段如何交替和间距长度。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var info = ctx.getLineDash();
7. }
8. }
```

### transferFromImageBitmap7+

PhonePC/2in1TabletTVWearable

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的[ImageBitmap对象](js-components-canvas-imagebitmap.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitmap | [ImageBitmap](js-components-canvas-imagebitmap.md) | 是 | 待显示的ImageBitmap对象。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. const ctx = el.getContext('2d');
6. var canvas = this.$refs.canvas.getContext('2d');
7. var offscreen = new OffscreenCanvas(500,500);
8. var offscreenCanvasCtx = offscreen.getContext("2d");
9. offscreenCanvasCtx.fillRect(0, 0, 200, 200);

11. var bitmap = offscreen.transferToImageBitmap();
12. canvas.transferFromImageBitmap(bitmap);
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/goEHs48EQoOc9AoGaTHovA/zh-cn_image_0000002558607096.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=94C577DC3A84A5B1C323D18B69242B0462851C405C52AD8B8C19F6C0583F9992)
