---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-offscreencanvasrenderingcontext2d
title: OffscreenCanvasRenderingContext2D对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > OffscreenCanvasRenderingContext2D对象
category: harmonyos-references
scraped_at: 2026-04-28T08:03:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a07898928ae52351d3500ca7fad2ef2971c3096ba0291cc3c78c5f8d45f05c1c
---

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用OffscreenCanvasRenderingContext2D在[OffscreenCanvas对象](js-components-canvas-offscreencanvas.md)上进行绘制，绘制对象可以是矩形、文本、图片等。

## 属性

PhonePC/2in1TabletTVWearable

除支持与[CanvasRenderingContext2D对象](js-components-canvas-canvasrenderingcontext2d.md)相同的属性外，还支持如下属性：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| filter | string | 设置图像的滤镜。  支持的滤镜效果如下：  - blur：给图像设置高斯模糊。  - brightness：给图片应用一种线性乘法，使其看起来更亮或更暗。  - contrast：调整图像的对比度。  - drop-shadow：给图像设置一个阴影效果。  - grayscale：将图像转换为灰度图像。  - hue-rotate：给图像应用色相旋转。  - invert：反转输入图像。  - opacity：调整图像的透明程度。  - saturate：转换图像饱和度。  - sepia：将图像转换为深褐色。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div style="width: 500px; height: 500px;">
3. <canvas ref="canvasId" style="width: 500px; height: 500px; padding: 80px; background-color: rgb(213, 213, 213);"></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow(){
4. var ctx = this.$refs.canvasId.getContext('2d');
5. var offscreen = new OffscreenCanvas(360, 500);
6. var offCanvas2 = offscreen.getContext("2d");
7. var img = new Image();
8. // 'common/images/flower.jpg'需要替换为开发者所需的图像资源文件
9. img.src = 'common/images/flower.jpg';
10. offCanvas2.drawImage(img, 0, 0, 100, 100);
11. offCanvas2.filter = 'blur(5px)';
12. offCanvas2.drawImage(img, 100, 0, 100, 100);

14. offCanvas2.filter = 'grayscale(50%)';
15. offCanvas2.drawImage(img, 200, 0, 100, 100);

17. offCanvas2.filter = 'hue-rotate(90deg)';
18. offCanvas2.drawImage(img, 0, 100, 100, 100);

20. offCanvas2.filter = 'invert(100%)';
21. offCanvas2.drawImage(img, 100, 100, 100, 100);

23. offCanvas2.filter = 'drop-shadow(8px 8px 10px green)';
24. offCanvas2.drawImage(img, 200, 100, 100, 100);

26. offCanvas2.filter = 'brightness(0.4)';
27. offCanvas2.drawImage(img, 0, 200, 100, 100);

29. offCanvas2.filter = 'opacity(25%)';
30. offCanvas2.drawImage(img, 100, 200, 100, 100);

32. offCanvas2.filter = 'saturate(30%)';
33. offCanvas2.drawImage(img, 200, 200, 100, 100);

35. offCanvas2.filter = 'sepia(60%)';
36. offCanvas2.drawImage(img, 0, 300, 100, 100);

38. offCanvas2.filter = 'contrast(200%)';
39. offCanvas2.drawImage(img, 100, 300, 100, 100);
40. var bitmap = offscreen.transferToImageBitmap();
41. ctx.transferFromImageBitmap(bitmap);
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/_XIvdzcfSJq2WgO02Hrz6g/zh-cn_image_0000002552800588.png?HW-CC-KV=V1&HW-CC-Date=20260428T000312Z&HW-CC-Expire=86400&HW-CC-Sign=65E6CB6A36A446B830CD38A401508CB6E1B8719F59C31E9D55EC3D2E032E1415)

## 方法

PhonePC/2in1TabletTVWearable

除支持与CanvasRenderingContext2D对象相同的方法外，还支持如下方法：

### isPointInPath

PhonePC/2in1TabletTVWearable

isPointInPath(path?: Path2D, x: number, y: number): boolean

判断指定点是否在路径的区域内。

**参数：**

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| path | Path2D | 否 | 可选对象，指定用来判断的路径。若没有设置，则使用当前路径。 |
| x | number | 是 | 待判断点的x轴坐标。 |
| y | number | 是 | 待判断点的y轴坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 指定点是否在路径的区域内。返回true时，指定点在路径区域内。返回false时，指定点不在路径区域内。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div class="container" style="width: 500px; height: 500px;">
3. <text class="textsize">In path:{{textValue}}</text>
4. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. background-color: #F1F3F5;
6. align-items: center;
7. justify-content: center;
8. width: 100%;
9. height: 100%;
10. }

12. canvas {
13. width: 600px;
14. height: 600px;
15. background-color: #fdfdfd;
16. border: none;
17. }

19. .textsize {
20. font-size: 40px;
21. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. textValue: false
5. },
6. onShow(){
7. var canvas = this.$refs.canvas.getContext('2d');
8. var offscreen = new OffscreenCanvas(500,500);
9. var offscreenCanvasCtx = offscreen.getContext("2d");

11. offscreenCanvasCtx.rect(10, 10, 100, 100);
12. offscreenCanvasCtx.fill();
13. this.textValue = offscreenCanvasCtx.isPointInPath(30, 70);

15. var bitmap = offscreen.transferToImageBitmap();
16. canvas.transferFromImageBitmap(bitmap);
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/g7l4x6UEQg6N_eMU6T5ddA/zh-cn_image_0000002583440283.png?HW-CC-KV=V1&HW-CC-Date=20260428T000312Z&HW-CC-Expire=86400&HW-CC-Sign=7204FF066EACE29AFB1093494615DB814999E1185493E59227635A022110A08A)

### isPointInStroke

PhonePC/2in1TabletTVWearable

isPointInStroke(path?: Path2D, x: number, y: number): boolean

判断指定点是否在路径的边缘线上。

**参数：**

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| path | Path2D | 否 | 可选对象，指定用来判断的路径。若没有设置，则使用当前路径。 |
| x | number | 是 | 待判断点的x轴坐标。 |
| y | number | 是 | 待判断点的y轴坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 指定点是否在路径的区域内。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div class="container" style="width: 500px; height: 500px;">
3. <text class="textsize">In stroke:{{textValue}}</text>
4. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. background-color: #F1F3F5;
6. align-items: center;
7. justify-content: center;
8. width: 100%;
9. height: 100%;
10. }

12. canvas {
13. width: 600px;
14. height: 600px;
15. background-color: #fdfdfd;
16. border: none;
17. }

19. .textsize {
20. font-size: 40px;
21. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. textValue: false
5. },
6. onShow(){
7. var canvas = this.$refs.canvas.getContext('2d');
8. var offscreen = new OffscreenCanvas(500,500);
9. var offscreenCanvasCtx = offscreen.getContext("2d");

11. offscreenCanvasCtx.rect(10, 10, 100, 100);
12. offscreenCanvasCtx.stroke();
13. this.textValue = offscreenCanvasCtx.isPointInStroke(50, 10);

15. var bitmap = offscreen.transferToImageBitmap();
16. canvas.transferFromImageBitmap(bitmap);
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/WUN7GcDrSlqqzePvnvJa3Q/zh-cn_image_0000002552960238.png?HW-CC-KV=V1&HW-CC-Date=20260428T000312Z&HW-CC-Expire=86400&HW-CC-Sign=4C3BD5082CF2EF16323FB835A18C8CBF137EEB80B70C35F6DA3718F51D8153F4)

### resetTransform

PhonePC/2in1TabletTVWearable

resetTransform(): void

**示例：**

```
1. <!-- xxx.hml -->
2. <div class="container" style="width: 500px; height: 500px;">
3. <text class="textsize">In path:{{textValue}}</text>
4. <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. background-color: #F1F3F5;
6. align-items: center;
7. justify-content: center;
8. width: 100%;
9. height: 100%;
10. }

12. canvas {
13. width: 600px;
14. height: 600px;
15. background-color: #fdfdfd;
16. border: none;
17. }

19. .textsize {
20. font-size: 40px;
21. }
```

```
1. // xxx.js
2. export default {
3. data:{
4. textValue:0
5. },
6. onShow(){
7. var canvas = this.$refs.canvas.getContext('2d');
8. var offscreen = new OffscreenCanvas(500,500);
9. var offscreenCanvasCtx = offscreen.getContext("2d");

11. offscreenCanvasCtx.transform(1, 0, 1.7, 1, 0, 0);
12. offscreenCanvasCtx.fillStyle = '#a9a9a9';
13. offscreenCanvasCtx.fillRect(40, 40, 50, 20);
14. offscreenCanvasCtx.fillRect(40, 90, 50, 20);

16. // Non-skewed rectangles
17. offscreenCanvasCtx.resetTransform();
18. offscreenCanvasCtx.fillStyle = '#ff0000';
19. offscreenCanvasCtx.fillRect(40, 40, 50, 20);
20. offscreenCanvasCtx.fillRect(40, 90, 50, 20);

22. var bitmap = offscreen.transferToImageBitmap();
23. canvas.transferFromImageBitmap(bitmap);
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/utCL3NBKRby8S-FSwr92Eg/zh-cn_image_0000002583480239.png?HW-CC-KV=V1&HW-CC-Date=20260428T000312Z&HW-CC-Expire=86400&HW-CC-Sign=48CA1125B54D07FD9F3F966A1F4BA86838AFB9DE6C07BE2B177C4523BA02565A)
