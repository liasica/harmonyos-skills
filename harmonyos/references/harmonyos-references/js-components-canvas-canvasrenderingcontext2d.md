---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > CanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-04-28T08:03:12+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:13dfecbadaf906c448bf77003c3c5d9eee283d3edb5be01000090bad7c7b23b1
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/GG9A_NFeR6ODFBVxQPgFQA/zh-cn_image_0000002583480205.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=EA597BCA3433AF9497E0E860FB25A34CC2969E2B73508FA73CCE400F9222D13C)
* 示意图（开启抗锯齿）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/blnAN7vwRUG8k_xjjpAcAw/zh-cn_image_0000002552800556.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=D0192E5533021D883D2877391968D02C7250A733597AAD2C7A1560835827A88B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/VxWWoucWRqyysm20GiIanw/zh-cn_image_0000002583440251.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=8FB092893EF5F1AA4AA801195A9F6304079E808E16A2208F44E36EEE4124AB5F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/SF_ojUlhSRmwx5dLvfcq1A/zh-cn_image_0000002552960206.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=38EAABDC13848922E4E5D1452DACF8391727387DDBC84575A2837C858F6C4541)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/W9I43yIpQjiZaTsioBidcA/zh-cn_image_0000002583480207.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=F2057CD4A10581479C2B84F1E1AB46B2FEE62844F64079E449B13F1253A1E784)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/nu52L6EnTnWMdxrNM1Phvw/zh-cn_image_0000002552800558.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=BB92F28BD4EA10544F9E2DFFD810080FCFA9CB0DA92FCDDFD11E8158D7ED9BEC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/xK060G1gSfWzoFYVT3XB4g/zh-cn_image_0000002583440253.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=E07712F6304DD21F304DB6B2419F7941F0A0A4A2A626EF33AA942928883CFEE2)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/-kzulmndTGWLTLM5B5JDXw/zh-cn_image_0000002552960208.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=D2B4AF5B4DE1CAEA7406A983C9028AFF605337C37086794DD468D37EF4851ED6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/jGQtObALTM-md7h8oCp51g/zh-cn_image_0000002583480209.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=4AD33E18749F8D89F1CFE095DB0BAE57FF938750CE62EC0F35108E14E9393451)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/6URu9oCgS8CixYJNSAwLKw/zh-cn_image_0000002552800560.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=EE27052627461ADF3F97E3A604AB5BAFAC84CD122AACA483D7642B08EFBF5ED8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/HKQ7931QQHuTR6g2KfTvjg/zh-cn_image_0000002583440255.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=4DE42F8F0E454FE8345F5748E5FCF873997CCDF260D2298403441FA83E7492D0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/usTTESd3T0iYcTf4Q3plnA/zh-cn_image_0000002552960210.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=2F6B0787E7993686D04C07A714C768A23C39280E2D2D6724C5DFE3B58A66B188)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/lBdJOKKfQR2ZKEkVgNG3ug/zh-cn_image_0000002583480211.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=3221A18F87978327466D08775A9472929052912B26E02367A1D28022F2D6241C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/cG6AZo65TRGQ7nC9yidHnQ/zh-cn_image_0000002552800562.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=285871460803E9DA7C045D7D1635D84B2D741146BAF6FABFC89EC78C0E2FC386)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/QnG293x6Rgyq0_9MnMjThQ/zh-cn_image_0000002583440257.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=8AA455E2EFE5C72D0BA6CE38103BE1658B57BDCD685B9838C612521E24AD2882)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/JFDSxRW7TmSzU_OiZGfZHA/zh-cn_image_0000002552960212.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=4C4ECD3A523B9FBB095B7145833515F26AD4BB30D75DD01E6FB446EAE578BB66)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/1d8u6l56S6yP3kJXtXK23g/zh-cn_image_0000002583480213.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=2F87CA557F18508981B21DAADE4FA8ACB9ACF773606B4E903A3CFE81E7F25A8F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/TwICeRqATEaJxPiSikE6Ng/zh-cn_image_0000002552800564.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=E162E1B087AF8DA30B8430B027FB465D6257E6AF0DFD09A743C9489DE5961228)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/dCMY8krXTwa5tW4idlOkeg/zh-cn_image_0000002583440259.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=13E6E44E9308099D4E20AF24387680069EA086B30C586F6514E60E1B1AC94901)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/o71sn9gYRqGrX7PEGX1zuw/zh-cn_image_0000002552960214.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=A519DBFA3090BC22145BE5520DAA0EFB221BA45D052FCAC2EC614841EC370853)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/9TOti7BSTC6VnG95gZF-cA/zh-cn_image_0000002583480215.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=E265DF4FC2BB0479BE3BD25847931FCCBE0DC3EC2571391D4A1E2933A8359037)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Dtzt7AcnTZCBMRxgddBAnQ/zh-cn_image_0000002552800566.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=4A8CB7BC6AC81369001E4099E905DD42DCC022B5BC4BA57AC54E35A159DE7436)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/h4xE0n1JRxGeyNYbhBnSGg/zh-cn_image_0000002583440261.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=8A3B7297E37803D9140ABF07A2F96BCC6749F863EBF0D168A6E277869797F886)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/1HPrkd3pReqgpmSWMPa_ug/zh-cn_image_0000002552960216.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=8DDE42343A8DF20E80BC3C251D2B8D87DD2AEB1AEBEAF2076889E9EB95E81262)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/0okRNSMlS3uBbCf5mxh16g/zh-cn_image_0000002583480217.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=23C57FCB3D7CDEBB3C7E9E5A50D6E34747E3AA40DF5B3EA9CBA66B4729DFFA50)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/uY5tromgQVmw6GclRWSIGw/zh-cn_image_0000002552800568.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=F5B2240B76CAD7C80F214787EE75EDB577462B97C7F88CD33DEF81CECF9C3439)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/TqJh8j5eSHOnYgpsqvy0Pw/zh-cn_image_0000002583440263.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=9FF38802E585B9AC0346AA9C2104E8C91886A583E0155EE47A6578CD447AD0B8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/CGp_s5Q6RJard5oJko5Zyg/zh-cn_image_0000002552960218.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=84218E68F011D7BCCEC1840005DCCD350D12699659345CEE31366D448F593095)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/xsi2s9WITuSwJgBMc3sWhA/zh-cn_image_0000002583480219.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=52854C9CBAC5602F0428FCD9690DF236E0194A36CB7528014BBE4A222A010B73)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/c6JsKe7wSKiPYB4BRjpYHw/zh-cn_image_0000002552800570.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=B36E92AD204C76F6C5710AF60D50F2FD54AA85DAA32CD23C8E80CEC67EB2B982)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qo0RljyvRYWM0XGcc1KPdA/zh-cn_image_0000002583440265.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=E39B05D36D0BF474B83C2B7CFD6185280785ABCD1B0562FC1E5436398DBEF61E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/sKuJZyDbQ1u5d3VMQTqCsA/zh-cn_image_0000002552960220.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=4CA72482BD53068CF0A61718939C91ED2F19C8DC0262A6D40E6ECFD3DE1888F0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/IGFm83JURW6IvC2anJVEzg/zh-cn_image_0000002583480221.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=BDAF5F238312682983C419ACE2A137366C3923B44F191F7DF49087F4D1344F3C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/7__QmP-vRAeaGponT2FfFA/zh-cn_image_0000002552800572.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=C26DBCD41CFA3928D337A976FC168281B5F99017E0BAA94440ADB0D000E860A2)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/aM3hTZBnRuO-nLHlKHbB3A/zh-cn_image_0000002583440267.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=E1D36517F973DED3B5743F2F21EA06E8F873BDF896558D9B99135C84A1F39959)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/V-tCWhBARjCl7i1ciQvHSA/zh-cn_image_0000002552960222.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=807D806D66DBC00479F6F4901B8EB03F9096B2643A4B62821C4FD12E061C80CD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/fUhnLXZuTOugIIpZfJx3sA/zh-cn_image_0000002583480223.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=65EA44894269D0C0433669EA13F8FE57D1AF15AF0DE744C59EF0ADB13BF652B6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/0WP0z0brRJqG_l593GbS8w/zh-cn_image_0000002552800574.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=C68CDD16D92D7B04A623915C76FB353C075F8D7EF0231297B6E48C8C9BBDCC66)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/pGSucGMWT5iPZ9IDOR_XKg/zh-cn_image_0000002583440269.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=C5C1D78ECD40EE8DAB695506765E60AC776ED68E57AD50C8999A838E1CA2758E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/o1v58vm8Tpi7OpYFpDHYTA/zh-cn_image_0000002552960224.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=E0455418DBF6BB936815209F3528235CCCC4569801B3B2B03818573AB9FC391F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/gkf_12N9SryNGtJQhj6GNA/zh-cn_image_0000002583480225.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=12F0B00F490A84DD081C44B7C96A5A478AB0E6C17FFDBB628D20C8B5004BCF4D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/dVB0rSeLTcK8z4eTGsP8oQ/zh-cn_image_0000002552800576.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=52F3885C2AEB0F9DE643603762D4F213E7879F71BB4A51DCD5BB5196CDC1AD2E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/ZK1NvlXXSeSxwL9SaFNKlg/zh-cn_image_0000002583440271.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=32A9D6AC19B87922E6883E4ADBF3F9F519E2B3E3C165F5175ED0460B4F97CB91)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/zhpeIX3BQtWqfTrIx_d-Dw/zh-cn_image_0000002552960226.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=0D627281FF5D849707E925AEB2011498768297D04D96F96D1281D1EB654C4BE0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/4Up95qMUQ5qrYR2MvF-CBw/zh-cn_image_0000002583480227.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=5867D4730235B33A7C181FE57E75A240BE0778C80AE14125C2E458C137BD7DCF)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uD49vXSVRLiL2uzGzkYbwQ/zh-cn_image_0000002552800578.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=D7D6C8FE8016CE291ABEBD558D0B76F03079A63A74695C2C46AD587488089278)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/5MtYa_EjSKSUOa5GNhP_vA/zh-cn_image_0000002583440273.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=618B9B964A99AAE872C239EAB6582C69A880A2786C7DFB3257936DD03422EAA7)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/JcCJWZ1kTIep9gyK0_4vKA/zh-cn_image_0000002552960228.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=B8AB085C202E24DE209D52EBBC6EE3893B49E9D012EBABEB3F48FCBBE5C90600)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Qk7g-iIUR9WkYMqXYEIOiA/zh-cn_image_0000002583480229.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=1A096C4D7A230D8E614F8A4AF2FDBC9D48EAC42032F05FE62F91ED5EBB49CA7E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/wHFzDsZIRHeTHRD7qOXgWQ/zh-cn_image_0000002552800580.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=D96C3CCD8EF339A1F5E74FB1D27A9181276451EF0BBC0323E640C955C1BE5B91)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/5bB4o0I9QEma-oD76d0GGw/zh-cn_image_0000002583440275.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=7450C87243D93E41B8D21BC3DEDE0D2ED3E5111B1C7EA5361C07F8265E58D413)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/ZEXmwmB7SWGBDO7unlN7_g/zh-cn_image_0000002552960230.png?HW-CC-KV=V1&HW-CC-Date=20260428T000310Z&HW-CC-Expire=86400&HW-CC-Sign=F1455BB86C101635DCE22AEF3FC083CD56ED01F976602712290DE6CCF2B0BFF5)
