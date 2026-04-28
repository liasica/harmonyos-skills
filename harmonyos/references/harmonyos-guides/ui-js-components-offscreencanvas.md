---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-offscreencanvas
title: OffscreenCanvasRenderingContext2D对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > OffscreenCanvasRenderingContext2D对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1961222ecb6e6b777454e45e3058feb3a35f1023b7757c20baa85a282562cb9e
---

使用OffscreenCanvas在离屏Canvas画布组件上进行绘制，绘制对象可以是矩形、文本、图片等。 离屏，即GPU在当前缓冲区以外新开辟的一个缓冲区。具体请参考[OffscreenCanvasRenderingContext2D对象](../harmonyos-references/js-offscreencanvasrenderingcontext2d.md)。

以下示例创建了一个OffscreenCanvas画布，再在画布上创建一个getContext2d对象，并设置filter属性改变图片样式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1"></canvas>
4. <select @change="change()">
5. <option value="blur(5px)">blur</option>
6. <option value="grayscale(50%)">grayscale</option>
7. <option value="hue-rotate(45deg)">hue-rotate</option>
8. <option value="invert(100%)">invert</option>
9. <option value="drop-shadow(8px 8px 10px green)">drop-shadow</option>
10. <option value="brightness(0.4)">brightness</option>
11. <option value="opacity(0.25)">opacity</option>
12. <option value="saturate(30%)">saturate</option>
13. <option value="sepia(60%)">sepia</option>
14. <option value="contrast(200%)">contrast</option>
15. </select>
16. </div>
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
2. import promptAction from '@ohos.promptAction';

4. export default {
5. data: {
6. el: null,
7. ctx: null,
8. offscreen: null,
9. offCanvas: null,
10. img: null,
11. },
12. onShow() {
13. this.ctx = this.$refs.canvas1.getContext('2d');
14. this.offscreen = new OffscreenCanvas(600, 500);
15. this.offCanvas = this.offscreen.getContext('2d');
16. this.img = new Image();
17. // "common/images/2.png"需要替换为开发者所需的图像资源文件
18. this.img.src = 'common/images/2.png';
19. // 图片成功获取触发方法
20. let _this = this;
21. this.img.onload = function () {
22. _this.offCanvas.drawImage(_this.img, 100, 100, 400, 300);
23. };
24. this.img.onerror = function () {
25. promptAction.showToast({ message: 'error', duration: 2000 })
26. };
27. var bitmap = this.offscreen.transferToImageBitmap();
28. this.ctx.transferFromImageBitmap(bitmap);
29. },
30. change(e) {
31. this.offCanvas.filter = e.newValue;
32. this.offCanvas.drawImage(this.img, 100, 100, 400, 300);
33. var bitmap = this.offscreen.transferToImageBitmap();
34. this.ctx.transferFromImageBitmap(bitmap);
35. },
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/NGhKziU_R42RQ-TnDBJJ4A/zh-cn_image_0000002552958136.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234029Z&HW-CC-Expire=86400&HW-CC-Sign=157540E2AD859521497CCAD6CFAA3FA3A893E2F15E36E0B5488B9F8ADB55EA2B)

## 判断位置

使用isPointInPath判断坐标点是否在路径的区域内，使用isPointInStroke判断坐标点是否在路径的边缘线上，并在页面上显示返回结果。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="content">
4. <text>坐标：{{X}}, {{Y}}</text>
5. <text>In path:{{textValue}}</text>
6. <text>In stroke:{{textValue1}}</text>
7. </div>
8. <canvas ref="canvas"></canvas>
9. <button onclick="change">Add(50)</button>
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

19. .content {
20. flex-direction: column;
21. justify-content: center;
22. align-items: center;
23. }

25. text {
26. font-size: 30px;
27. width: 300px;
28. height: 80px;
29. text-align: center;
30. }

32. button {
33. width: 180px;
34. height: 75px;
35. margin-top: 50px;
36. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. textValue: 0,
5. textValue1: 0,
6. X: 0,
7. Y: 250,
8. },
9. onShow() {
10. let canvas = this.$refs.canvas.getContext('2d');
11. let offscreen = new OffscreenCanvas(500, 500);
12. let offscreenCanvasCtx = offscreen.getContext('2d');
13. let offscreenCanvasCtx1 = offscreen.getContext('2d');
14. offscreenCanvasCtx1.arc(this.X, this.Y, 2, 0, 6.28);
15. offscreenCanvasCtx.lineWidth = 20;
16. offscreenCanvasCtx.rect(200, 150, 200, 200);
17. offscreenCanvasCtx.stroke();
18. this.textValue1 = offscreenCanvasCtx.isPointInStroke(this.X, this.Y) ? 'true' : 'false';
19. this.textValue = offscreenCanvasCtx.isPointInPath(this.X, this.Y) ? 'true' : 'false';
20. let bitmap = offscreen.transferToImageBitmap();
21. canvas.transferFromImageBitmap(bitmap);
22. },
23. change() {
24. if (this.X < 500) {
25. this.X = this.X + 50;
26. } else {
27. this.X = 0;
28. }
29. let canvas = this.$refs.canvas.getContext('2d');
30. let offscreen = new OffscreenCanvas(500, 500);
31. let offscreenCanvasCtx = offscreen.getContext('2d');
32. let offscreenCanvasCtx1 = offscreen.getContext('2d');
33. offscreenCanvasCtx1.arc(this.X, this.Y, 1, 0, 6.28)
34. offscreenCanvasCtx.lineWidth = 20
35. offscreenCanvasCtx.rect(200, 150, 200, 200);
36. offscreenCanvasCtx.stroke();
37. this.textValue1 = offscreenCanvasCtx.isPointInStroke(this.X, this.Y) ? 'true' : 'false';
38. this.textValue = offscreenCanvasCtx.isPointInPath(this.X, this.Y) ? 'true' : 'false';
39. let bitmap = offscreen.transferToImageBitmap();
40. canvas.transferFromImageBitmap(bitmap);
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Nex9NwVGRi-t1n7pk8Qc7A/zh-cn_image_0000002583478137.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234029Z&HW-CC-Expire=86400&HW-CC-Sign=9D97A859196B310BD9EE39AC959ADE698696EB03201A4187D157B11DCDB38783)
