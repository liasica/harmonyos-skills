---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvasrenderingcontext2d
title: CanvasRenderingContext2D对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > CanvasRenderingContext2D对象
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b56db47946184401d31b1ebeed59f828bef2f9e979ccf92e3c979ecdb647cf25
---

使用CanvasRenderingContext2D在Canvas画布组件上进行绘制，绘制对象可以是图形、文本、线段、图片等。具体请参考[CanvasRenderingContext2D对象](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md)。

## 画线段

使用moveTo和lineTo画出一条线段，当使用closePath方法时会结束当前路径形成一个封闭图形。设置quadraticCurveTo（二次贝塞尔曲线）或bezierCurveTo（三次贝塞尔曲线）的值组成图形。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1"></canvas>
4. <select @change="change">
5. <option value="value1"> line </option>
6. <option value="value2"> quadratic </option>
7. <option value="value3"> bezier </option>
8. <option value="value4"> arc/ellipse </option>
9. <option value="value5"> lineJoin/miterLimit </option>
10. </select>
11. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }

11. canvas {
12. width: 600px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. }

18. select {
19. margin-top: 50px;
20. width: 250px;
21. height: 100px;
22. background-color: white;
23. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. el: null,
5. ctx: null,
6. },
7. onShow() {
8. this.el = this.$refs.canvas1;
9. this.ctx = this.el.getContext("2d", { antialias: true });
10. // 清除画布上的内容
11. this.ctx.clearRect(0, 0, 600, 500);
12. // 创建一个新的绘制路径
13. this.ctx.beginPath();
14. // 线端点以方形结束
15. this.ctx.lineCap = 'butt';
16. // 描边的宽度
17. this.ctx.lineWidth = 15;
18. // 创建一个新的绘制路径
19. this.ctx.beginPath();
20. // 路径从当前点移动到指定点
21. this.ctx.moveTo(200, 100);
22. // 从当前点到指定点进行路径连接
23. this.ctx.lineTo(400, 100);
24. // 边框绘制
25. this.ctx.stroke();
26. this.ctx.beginPath();
27. // 线端点以圆形结束
28. this.ctx.lineCap = 'round';
29. this.ctx.moveTo(200, 200);
30. this.ctx.lineTo(400, 200);
31. this.ctx.stroke();
32. // 线端点以方形结束
33. this.ctx.beginPath();
34. this.ctx.lineCap = 'square';
35. this.ctx.moveTo(200, 300);
36. this.ctx.lineTo(400, 300);
37. this.ctx.stroke();
38. },
39. change(e) {
40. if (e.newValue == 'value1') {
41. this.el = this.$refs.canvas1;
42. this.ctx = this.el.getContext("2d", { antialias: true });
43. this.ctx.clearRect(0, 0, 600, 500);
44. // 上
45. this.ctx.beginPath();
46. this.ctx.lineCap = 'butt';
47. this.ctx.moveTo(200, 100);
48. this.ctx.lineTo(400, 100);
49. this.ctx.stroke();
50. // 中
51. this.ctx.beginPath();
52. this.ctx.lineCap = 'round';
53. this.ctx.moveTo(200, 200);
54. this.ctx.lineTo(400, 200);
55. this.ctx.stroke();
56. // 下
57. this.ctx.beginPath();
58. this.ctx.lineCap = 'square';
59. this.ctx.moveTo(200, 300);
60. this.ctx.lineTo(400, 300);
61. this.ctx.stroke();
62. } else if (e.newValue == 'value2') {
63. this.ctx.clearRect(0, 0, 600, 500);
64. // 上
65. this.ctx.beginPath();
66. this.ctx.moveTo(100, 150);
67. // 二次贝塞尔曲线的路径
68. this.ctx.quadraticCurveTo(300, 50, 500, 150);
69. this.ctx.stroke();
70. // 左
71. this.ctx.beginPath();
72. this.ctx.moveTo(200, 150);
73. this.ctx.quadraticCurveTo(250, 250, 250, 400);
74. this.ctx.stroke();
75. // 右
76. this.ctx.beginPath();
77. this.ctx.moveTo(400, 150);
78. this.ctx.quadraticCurveTo(350, 250, 350, 400);
79. this.ctx.stroke();
80. } else if (e.newValue == 'value3') {
81. this.ctx.clearRect(0, 0, 600, 500);
82. // 下
83. this.ctx.beginPath();
84. this.ctx.moveTo(100, 200);
85. // 三次贝塞尔曲线的路径
86. this.ctx.bezierCurveTo(150, 100, 200, 100, 250, 200);
87. this.ctx.stroke();
88. // 左
89. this.ctx.beginPath();
90. this.ctx.moveTo(350, 200);
91. this.ctx.bezierCurveTo(400, 100, 450, 100, 500, 200);
92. this.ctx.stroke();
93. // 右
94. this.ctx.beginPath();
95. this.ctx.moveTo(200, 350);
96. this.ctx.bezierCurveTo(250, 500, 350, 500, 400, 350);
97. this.ctx.stroke();
98. } else if (e.newValue == 'value4') {
99. this.ctx.clearRect(0, 0, 600, 500);
100. this.ctx.beginPath();
101. this.ctx.moveTo(100, 200);
102. // 弧线
103. this.ctx.arcTo(150, 300, 350, 300, 150);
104. this.ctx.stroke();
105. this.ctx.beginPath();
106. // 椭圆
107. this.ctx.ellipse(400, 250, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
108. this.ctx.stroke();
109. } else if (e.newValue == 'value5') {
110. this.ctx.clearRect(0, 0, 600, 500);
111. // 左上
112. this.ctx.beginPath();
113. // 在线段相连处绘制一个扇形
114. this.ctx.lineJoin = 'round';
115. this.ctx.moveTo(100, 100);
116. this.ctx.lineTo(200, 200);
117. this.ctx.lineTo(100, 250);
118. this.ctx.stroke();
119. // 左下
120. this.ctx.beginPath();
121. // 在线段相连处使用三角形为底填充
122. this.ctx.lineJoin = 'bevel';
123. this.ctx.moveTo(100, 300);
124. this.ctx.lineTo(200, 400);
125. this.ctx.lineTo(100, 450);
126. this.ctx.stroke();
127. // 右上
128. this.ctx.beginPath();
129. //线条相交处内角和外角的距离
130. this.ctx.lineJoin = 'miter';
131. this.ctx.miterLimit = 3;
132. this.ctx.moveTo(400, 100);
133. this.ctx.lineTo(450, 200);
134. this.ctx.lineTo(400, 250);
135. // 结束当前路径形成一个封闭路径
136. this.ctx.closePath();
137. this.ctx.stroke();
138. // 右下
139. this.ctx.beginPath();
140. this.ctx.lineJoin = 'miter';
141. this.ctx.miterLimit = 10;
142. this.ctx.moveTo(400, 300);
143. this.ctx.lineTo(450, 400);
144. this.ctx.lineTo(400, 450);
145. this.ctx.closePath();
146. this.ctx.stroke();
147. }
148. },
149. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/G0Ba2lgHQfm0yIEf_6dKAA/zh-cn_image_0000002589324493.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=B8568EFA6E1F4944631E354B0C1A8FEAD9A2575480EDADD842D40573F29EB090)

## 画边框

全局定义画布（el）及画笔（ctx），初始化创建一个边框宽度为5的长方形。对边框的宽度（lineWidth）、颜色（strokeStyle）、虚化程度（setLineDash）进行改变，选用select组件添加change事件，下拉选择时触发change事件后画出改变后的图形。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1"></canvas>
4. <select @change="change">
5. <option value="value1">strokeRect</option>
6. <option value="value2">arc</option>
7. <option value="value3">lineDashRect</option>
8. <option value="value4">fillRect</option>
9. </select>
10. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. display: flex;
10. }

12. canvas {
13. width: 600px;
14. height: 500px;
15. background-color: #fdfdfd;
16. border: 5px solid red;
17. }

19. select {
20. margin-top: 50px;
21. width: 250px;
22. height: 100px;
23. background-color: white;
24. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. el: null,
5. ctx: null,
6. },
7. onShow() {
8. this.el = this.$refs.canvas1;
9. this.ctx = this.el.getContext("2d", { antialias: true });
10. this.ctx.lineWidth = 5;
11. this.ctx.strokeRect(200, 150, 200, 200);
12. },
13. change(e) {
14. if (e.newValue == 'value1') {
15. // 清除画布上的内容
16. this.ctx.clearRect(0, 0, 600, 500);
17. // 边框宽度
18. this.ctx.lineWidth = 5;
19. // 边框颜色
20. this.ctx.strokeStyle = '#110000';
21. // 边框的虚化程度
22. this.ctx.setLineDash([0, 0]);
23. // 画具有边框的矩形
24. this.ctx.strokeRect(200, 150, 200, 200);
25. } else if (e.newValue == 'value2') {
26. this.ctx.clearRect(0, 0, 600, 500);
27. this.ctx.lineWidth = 30;
28. this.ctx.strokeStyle = '#0000ff';
29. this.ctx.setLineDash([0, 0]);
30. // 画圆
31. this.ctx.arc(300, 250, 150, 0, 6.28);
32. //进行边框绘制
33. this.ctx.stroke();
34. } else if (e.newValue == 'value3') {
35. this.ctx.clearRect(0, 0, 600, 500);
36. this.ctx.lineWidth = 5;
37. this.ctx.setLineDash([5, 5]);
38. this.ctx.strokeRect(200, 150, 200, 200);
39. } else if (e.newValue == 'value4') {
40. this.ctx.clearRect(0, 0, 600, 500);
41. // 画一个有填充颜色的矩形
42. this.ctx.fillStyle = '#0000ff';
43. this.ctx.fillRect(200, 150, 200, 200);
44. }
45. },
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/T7OyVEArQiyh0EClQVPAAg/zh-cn_image_0000002589244431.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=773B126CAF37EDFEA4D3700EB51BCE3389120852983D1BC021CF944607773BD1)

## 填充渐变色

添加[createLinearGradient](../harmonyos-references/ts-canvasrenderingcontext2d.md#createlineargradient)和[createRadialGradient](../harmonyos-references/ts-canvasrenderingcontext2d.md#createradialgradient)属性创建渐变容器，接着用addColorStop方法添加多个色块组成渐变色，再设置fillStyle为gradient将渐变色填充到矩形中，最后设置阴影的模糊级别（shadowBlur）、阴影颜色（shadowColor）及阴影偏移量（shadowOffset）。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1"></canvas>
4. <select @change="change">
5. <option value="value1">LinearGradient</option>
6. <option value="value2">RadialGradient</option>
7. <option value="value3">shadowBlur</option>
8. <option value="value4">shadowOffset</option>
9. </select>
10. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. display: flex;
10. }

12. canvas {
13. width: 600px;
14. height: 500px;
15. background-color: #fdfdfd;
16. border: 5px solid red;
17. }

19. select {
20. margin-top: 50px;
21. width: 250px;
22. height: 100px;
23. background-color: white;
24. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. el: null,
5. ctx: null,
6. },
7. onShow() {
8. this.el = this.$refs.canvas1;
9. this.ctx = this.el.getContext("2d", { antialias: true });
10. // 创建一个线性渐变色
11. let gradient = this.ctx.createLinearGradient(100, 100, 400, 300);
12. // 添加渐变颜色
13. gradient.addColorStop(0.0, 'red');
14. gradient.addColorStop(0.7, 'white');
15. gradient.addColorStop(1.0, 'green');
16. // 填充颜色为渐变色
17. this.ctx.fillStyle = gradient;
18. this.ctx.fillRect(100, 100, 400, 300);
19. },
20. change(e) {
21. if (e.newValue == 'value1') {
22. // 清除画布上的内容
23. this.ctx.clearRect(0, 0, 600, 500);
24. let gradient = this.ctx.createLinearGradient(100, 100, 400, 300);
25. gradient.addColorStop(0.0, 'red');
26. gradient.addColorStop(0.7, 'white');
27. gradient.addColorStop(1.0, 'green');
28. this.ctx.fillStyle = gradient;
29. // 设置绘制阴影时的模糊级别
30. this.ctx.shadowBlur = 0;
31. // 绘制阴影时和原有对象的垂直偏移值
32. this.ctx.shadowOffsetY = 0;
33. // 绘制阴影时和原有对象的水平偏移值
34. this.ctx.shadowOffsetX = 0;
35. this.ctx.fillRect(100, 100, 400, 300);
36. } else if (e.newValue == 'value2') {
37. this.ctx.clearRect(0, 0, 600, 500);
38. // 创建一个径向渐变色
39. let gradient = this.ctx.createRadialGradient(300, 250, 20, 300, 250, 100);
40. gradient.addColorStop(0.0, 'red');
41. gradient.addColorStop(0.7, 'white');
42. gradient.addColorStop(1.0, 'green');
43. this.ctx.shadowBlur = 0;
44. this.ctx.shadowOffsetY = 0;
45. this.ctx.shadowOffsetX = 0;
46. this.ctx.fillStyle = gradient;
47. this.ctx.fillRect(100, 100, 400, 300);
48. } else if (e.newValue == 'value3') {
49. this.ctx.clearRect(0, 0, 600, 500);
50. let gradient = this.ctx.createLinearGradient(100, 100, 400, 400);
51. gradient.addColorStop(0.0, 'red');
52. gradient.addColorStop(0.5, 'white');
53. gradient.addColorStop(1, '#17ea35');
54. // 设置绘制阴影时的模糊级别
55. this.ctx.shadowBlur = 30;
56. // 绘制阴影时的阴影颜色
57. this.ctx.shadowColor = 'rgb(229, 16, 16)';
58. this.ctx.fillStyle = gradient;
59. this.ctx.fillRect(100, 100, 400, 300);
60. } else if (e.newValue == 'value4') {
61. this.ctx.clearRect(0, 0, 600, 500);
62. this.ctx.clearRect(0, 0, 600, 500);
63. let gradient = this.ctx.createRadialGradient(300, 250, 20, 300, 250, 200);
64. gradient.addColorStop(0.0, 'red');
65. gradient.addColorStop(0.5, 'white');
66. gradient.addColorStop(1, '#17ea35');
67. // 设置绘制阴影时的模糊级别
68. this.ctx.shadowBlur = 30;
69. this.ctx.shadowOffsetY = 30;
70. // 绘制阴影时的阴影颜色
71. this.ctx.shadowColor = 'rgb(23, 1, 1)';
72. this.ctx.fillStyle = gradient;
73. this.ctx.fillRect(100, 100, 400, 300);
74. }
75. },
76. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/02sJtSGaTaeDvestfwwGNw/zh-cn_image_0000002558764624.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=04F6B4901E7F9D8E891083D1D7AA5E3F32877E72B98FD98DAF297750560CAC80)

## 填充文字

先创建文本，再用[fillText](../harmonyos-references/ts-canvasrenderingcontext2d.md#filltext)方法把文字写在画布上。通过[globalAlpha](../harmonyos-references/ts-canvasrenderingcontext2d.md#globalalpha)属性改变基线透明度，使基线不会挡住文字，再设置[textAlign](../harmonyos-references/ts-canvasrenderingcontext2d.md#textalign)和[textBaseline](../harmonyos-references/ts-canvasrenderingcontext2d.md#textbaseline)属性确定文字基于基线的位置。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1"></canvas>
4. <select @change="change">
5. <option value="value1">text</option>
6. <option value="value2">textBaseline</option>
7. <option value="value3">textAlign</option>
8. </select>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }

11. canvas {
12. width: 600px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. }

18. select {
19. margin-top: 50px;
20. width: 250px;
21. height: 100px;
22. background-color: white;
23. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. el: null,
5. ctx: null,
6. },
7. onShow() {
8. this.el = this.$refs.canvas1;
9. this.ctx = this.el.getContext("2d", { antialias: true });
10. // 创建文本
11. let text = "Hello World";
12. // 设置字体
13. this.ctx.font = '30px';
14. this.ctx.fillText("with:" + this.ctx.measureText(text).width, 200, 300);
15. // 填充字体文本
16. this.ctx.fillText(text, 200, 250);
17. },
18. change(e) {
19. if (e.newValue == 'value1') {
20. // 清除画布上的内容
21. this.ctx.clearRect(0, 0, 600, 500);
22. // 开始新的路径
23. this.ctx.beginPath();
24. // 初始化textAlign值
25. this.ctx.textAlign = 'left';
26. // 初始化textBaseline
27. this.ctx.textBaseline = 'alphabetic';
28. // 设置字体
29. this.ctx.font = '30px Arial';
30. let text = "Hello World";
31. // 获取字体width
32. this.ctx.fillText("with:" + this.ctx.measureText(text).width, 200, 300);
33. // 填充字体文本
34. this.ctx.fillText(text, 200, 250);
35. } else if (e.newValue == 'value2') {
36. this.ctx.clearRect(0, 0, 600, 500);
37. this.ctx.beginPath();
38. // 设置透明度
39. this.ctx.globalAlpha = 0.1;
40. // 设置线宽度
41. this.ctx.lineWidth = 10;
42. // 设置线段颜色
43. this.ctx.strokeStyle = '#0000ff';
44. // 从当前点移动到指定点
45. this.ctx.moveTo(0, 240);
46. // 当前点到指定点进行路径连接
47. this.ctx.lineTo(600, 240);
48. this.ctx.stroke();
49. this.ctx.font = '35px';
50. this.ctx.globalAlpha = 1;
51. // 初始化textAlign值
52. this.ctx.textAlign = 'left';
53. // 设置textBaseline
54. this.ctx.textBaseline = 'top';
55. this.ctx.fillText('Top', 50, 240);
56. this.ctx.textBaseline = 'bottom';
57. this.ctx.fillText('Bottom', 200, 240);
58. this.ctx.textBaseline = 'middle';
59. this.ctx.fillText('Middle', 400, 240);
60. } else if (e.newValue == 'value3') {
61. // 清除画布上的内容
62. this.ctx.clearRect(0, 0, 600, 500);
63. this.ctx.beginPath();
64. this.ctx.globalAlpha = 0.1;
65. this.ctx.lineWidth = 10;
66. this.ctx.strokeStyle = '#0000ff';
67. this.ctx.moveTo(300, 0);
68. this.ctx.lineTo(300, 500);
69. this.ctx.stroke();
70. this.ctx.font = '35px';
71. this.ctx.globalAlpha = 1;
72. // 初始化 textBaseline
73. this.ctx.textBaseline = 'alphabetic';
74. // 设置textAlign
75. this.ctx.textAlign = 'left';
76. this.ctx.fillText('textAlign=left', 300, 100);
77. this.ctx.textAlign = 'center';
78. this.ctx.fillText('textAlign=center', 300, 250);
79. this.ctx.textAlign = 'right';
80. this.ctx.fillText('textAlign=right', 300, 400);
81. }
82. }
83. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/SG4-68F6TviSj0hGfH-AOA/zh-cn_image_0000002558604968.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=D5C5C46DBFE5730515423F99DF1DF9AF847E4B76078B263086D8208679664386)

说明

ltr布局模式下start和left一致，rtl布局模式下start和right一致。

## 添加图片

创建图片对象后使用[drawImage](../harmonyos-references/ts-canvasrenderingcontext2d.md#drawimage)方法画出图片，给图片设置一些动画样式如scale（缩放）、translate（平移）或rotate（旋转）。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="content">
4. <canvas ref="canvas0"></canvas>
5. <text onclick="change">change</text>
6. <canvas ref="canvas1"></canvas>
7. <text onclick="rotate">rotate</text>
8. <canvas ref="canvas2"></canvas>
9. <text onclick="scale">scale</text>
10. <canvas ref="canvas3"></canvas>
11. <text onclick="translate" style="width: 300px;">translate</text>
12. <canvas ref="canvas4"></canvas>
13. <text onclick="transform" style="width: 300px;">transform</text>
14. <canvas ref="canvas5"></canvas>
15. <text onclick="setTransform" style="width: 300px;">setTransform</text>
16. <canvas ref="canvas6"></canvas>
17. </div>
18. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. flex-direction: column;
5. background-color: #F1F3F5;
6. align-items: center;
7. }

9. canvas {
10. width: 600px;
11. height: 300px;
12. margin-bottom: 100px;
13. background-color: #fdfdfd;
14. border: 5px solid red;
15. }

17. .content {
18. width: 80%;
19. margin-top: 50px;
20. margin-bottom: 50px;
21. display: flex;
22. flex-wrap: wrap;
23. justify-content: space-around;
24. }

26. text {
27. font-size: 35px;
28. width: 200px;
29. height: 80px;
30. color: white;
31. border-radius: 20px;
32. text-align: center;
33. background-color: #6060e7;
34. margin-bottom: 30px;
35. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';

4. export default {
5. data: {
6. compositeOperation: 'source-over'
7. },
8. onShow() {
9. let ctx = this.$refs.canvas0.getContext('2d');
10. // 创建图片对象
11. let img = new Image();
12. // 设置图片路径
13. // "common/images/2.png"需要替换为开发者所需的图像资源文件
14. img.src = 'common/images/2.png';
15. // 设置图片宽度
16. img.width = 150;
17. // 设置图片高度
18. img.height = 150;
19. // 图片平铺容器
20. var pat = ctx.createPattern(img, 'repeat');
21. ctx.fillStyle = pat;
22. ctx.fillRect(0, 0, 600, 300);
23. },
24. change() {
25. // 创建画布后得到画笔
26. let ctx = this.$refs.canvas1.getContext('2d');
27. ctx.clearRect(0, 0, 600, 1000);
28. if (this.compositeOperation == 'source-over') {
29. this.compositeOperation = 'destination-over';
30. } else {
31. this.compositeOperation = 'source-over';
32. }
33. ctx.globalCompositeOperation = this.compositeOperation;
34. let img = new Image();
35. img.src = 'common/images/2.png';
36. // 图片成功获取触发方法
37. img.onload = function () {
38. ctx.drawImage(img, 150, 20, 200, 200);
39. };
40. let img1 = new Image();
41. // "common/images/3.png"需要替换为开发者所需的图像资源文件
42. img1.src = 'common/images/3.png';
43. img1.onload = function () {
44. // 画上图片
45. ctx.drawImage(img1, 250, 80, 200, 200);
46. };
47. // 图片获取失败触发方法
48. img1.onerror = function () {
49. promptAction.showToast({ message: 'error', duration: 2000 })
50. };
51. },
52. rotate() {
53. let ctx = this.$refs.canvas2.getContext('2d');
54. ctx.clearRect(0, 0, 600, 300);
55. // 旋转
56. ctx.rotate(10 * Math.PI / 180);
57. let img = new Image();
58. img.src = 'common/images/2.png';
59. img.onload = function () {
60. ctx.drawImage(img, 300, 0, 100, 100);
61. };
62. },
63. scale() {
64. let ctx = this.$refs.canvas3.getContext('2d');
65. ctx.clearRect(0, 0, 600, 200);
66. // 缩放
67. ctx.scale(1.3, 1.2);
68. let img = new Image();
69. img.src = 'common/images/2.png';
70. img.onload = function () {
71. ctx.drawImage(img, 0, 0, 50, 50);
72. };
73. },
74. translate() {
75. let ctx = this.$refs.canvas4.getContext('2d');
76. ctx.clearRect(0, 0, 600, 300);
77. ctx.translate(10, 0);
78. let img = new Image();
79. img.src = 'common/images/2.png';
80. img.onload = function () {
81. ctx.drawImage(img, 0, 50, 300, 200);
82. };
83. },
84. transform() {
85. let ctx = this.$refs.canvas5.getContext('2d');
86. ctx.clearRect(0, 0, 600, 300);
87. ctx.transform(1.1, 0.1, 0.1, 1, 10, 0);
88. let img = new Image();
89. img.src = 'common/images/2.png';
90. img.onload = function () {
91. ctx.drawImage(img, 0, 50, 100, 100);
92. };
93. },
94. setTransform() {
95. let ctx = this.$refs.canvas6.getContext('2d');
96. ctx.clearRect(0, 0, 600, 300);
97. ctx.setTransform(1.1, 0.1, 0.1, 1, 10, 0);
98. let img = new Image();
99. img.src = 'common/images/2.png';
100. img.onload = function () {
101. ctx.drawImage(img, 0, 50, 100, 100);
102. };
103. },
104. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/aVql2FcyQACVUj6GDjexJg/zh-cn_image_0000002589324495.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=52EC7C46D784AF32527B85702780FD8C0128D028F0D0A9B8FA0D549AF4E952CC)

说明

* setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。
* 变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

  x' = scaleX \* x + skewY \* y + translateX

  y' = skewX \* x + scaleY \* y + translateY

## 添加方法

save方法可对画笔样式进行存储，restore可对存储的画笔进行恢复。如下面的示例，先设置画笔为红色，在保存画笔后对画布进行清除并改变画笔为蓝色，当我们直接使用画笔时会画出一个蓝色矩形，对存储的画笔进行恢复后就可画出红色矩形。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="content">
4. <canvas ref="canvas"></canvas>
5. </div>
6. <div class="content">
7. <text onclick="save">save</text>
8. <text onclick="clear">clear</text>
9. <text onclick="restore">restore</text>
10. </div>
11. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. align-items: center;
8. }

10. canvas {
11. margin-top: 300px;
12. width: 600px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. }

18. .content {
19. width: 80%;
20. margin-top: 50px;
21. margin-bottom: 50px;
22. display: flex;
23. flex-wrap: wrap;
24. justify-content: space-around;
25. }

27. text {
28. width: 150px;
29. height: 80px;
30. color: white;
31. border-radius: 20px;
32. text-align: center;
33. background-color: #6060e7;
34. margin-bottom: 30px;
35. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';

4. export default {
5. data: {
6. ctx: '',
7. },
8. onShow() {
9. this.ctx = this.$refs.canvas.getContext('2d');
10. this.ctx.fillStyle = 'red';
11. this.ctx.fillRect(200, 150, 200, 200);
12. },
13. save() {
14. // 画笔储存
15. this.ctx.save();
16. promptAction.showToast({ message: 'save succeed' });
17. },
18. clear() {
19. this.ctx.clearRect(0, 0, 600, 500);
20. // 改变画笔颜色
21. this.ctx.fillStyle = '#2133d2';
22. },
23. restore() {
24. this.ctx.beginPath();
25. // 画笔恢复
26. this.ctx.restore();
27. this.ctx.fillRect(200, 150, 200, 200);
28. },
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/gibNXkElTpK9CixKgy6ZPA/zh-cn_image_0000002589244433.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=84E58C98B718A2EE65F6BA2DC035EEEDFA2CB5C67BA43B07E79D0792487C715D)
