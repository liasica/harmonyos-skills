---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-path2d
title: Path2D对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > Path2D对象
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:63db31773812008350de709b7a76fc9078b855daf4d9c19f74fe4316ce592406
---

路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的[stroke](../harmonyos-references/ts-canvasrenderingcontext2d.md#stroke-1)接口进行绘制。具体请参考[Path2D对象](../harmonyos-references/js-components-canvas-path2d.md)。

## 画线段

创建Path2D对象，使用多条线段组合图形。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas"></canvas>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. align-items: center;
6. justify-content: center;
7. width: 100%;
8. height: 100%;
9. }

11. canvas {
12. width: 600px;
13. height: 600px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. }
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. let ctx = this.$refs.canvas.getContext('2d', {
5. antialias: true
6. });
7. let path = ctx.createPath2D();
8. // 房顶
9. path.moveTo(10, 300);
10. path.lineTo(210, 100);
11. path.lineTo(410, 300);
12. // 屋子
13. path.moveTo(10, 300);
14. path.lineTo(410, 300);
15. path.lineTo(410, 600);
16. path.lineTo(10, 600);
17. path.closePath();
18. // 窗子
19. path.moveTo(50, 450);
20. path.bezierCurveTo(70, 350, 130, 350, 150, 450);
21. path.closePath();
22. // 门
23. path.moveTo(250, 450);
24. path.rect(250, 450, 100, 600);
25. path.closePath();
26. // 烟囱
27. path.moveTo(365, 250);
28. path.ellipse(310, 215, 30, 130, 0, Math.PI * 0.04, Math.PI * 1.1, 1);
29. // 树
30. path.moveTo(485, 450);
31. path.quadraticCurveTo(510, 500, 485, 600);
32. path.moveTo(550, 450);
33. path.quadraticCurveTo(525, 500, 550, 600);
34. path.moveTo(600, 535);
35. path.arc(520, 450, 85, 0, 6);
36. ctx.stroke(path);
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/z6jutU-eQ4u8DojDVqhPUg/zh-cn_image_0000002558764626.png?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=9388458E3F3860529C4176BD14B38211EAA85BC1807A1DC18FC1645CE702F369)

## 画图形

先使用createPath2D创建出路径对象，只对path1路径进行描边，所以画布上就只会出现path1的路径图形。点击text组件触发addPath方法会把path2路径对象当参数传入path1中，再对path1对象进行描边（stroke）操作后画布出现path1和path2两个图形。点击change文本改变setTransform属性值为setTransform(2, 0.1, 0.1, 2, 0,0)，图形变大并向左倾斜。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas"></canvas>
4. <div class="content">
5. <text onclick="addPath">{{ isAdd }}</text>
6. <text onclick="setTransform">{{ textName }}</text>
7. </div>
8. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. align-items: center;
6. justify-content: center;
7. width: 100%;
8. height: 100%;
9. }

11. canvas {
12. width: 600px;
13. height: 600px;
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
2. export default {
3. data: {
4. ctx: null,
5. path1: null,
6. path2: null,
7. path3: null,
8. isAdd: 'addPath2',
9. isChange: true,
10. textName: 'change'
11. },
12. onShow() {
13. this.ctx = this.$refs.canvas.getContext('2d', {
14. antialias: true
15. });
16. this.path1 = this.ctx.createPath2D();
17. // 正方形
18. this.path1.moveTo(200, 200);
19. this.path1.lineTo(400, 200);
20. this.path1.lineTo(400, 400);
21. this.path1.lineTo(200, 400);
22. this.path1.closePath();
23. this.path2 = this.ctx.createPath2D();
24. // 圆形
25. this.path2.arc(300, 300, 75, 0, 6.28);
26. this.ctx.stroke(this.path1);
27. },
28. addPath() {
29. if (this.isAdd == 'addPath2') {
30. // 删除指定区域的绘制内容
31. this.ctx.clearRect(0, 0, 600, 600);
32. this.ctx.beginPath();
33. // 将另一个的路径添加到当前路径对象中
34. this.path2.addPath(this.path1);
35. this.ctx.stroke(this.path2);
36. this.isAdd = 'clearPath2';
37. } else {
38. this.ctx.clearRect(0, 0, 600, 600);
39. this.ctx.stroke(this.path1);
40. this.isAdd = 'addPath2';
41. }
42. },
43. setTransform() {
44. if (this.isChange) {
45. this.ctx.clearRect(0, 0, 600, 600);
46. this.path3 = this.ctx.createPath2D();
47. this.path3.arc(150, 150, 100, 0, 6.28);
48. // 重置现有的变换矩阵并创建新的变换矩阵
49. this.path3.setTransform(2, 0.1, 0.1, 2, 0, 0);
50. this.ctx.stroke(this.path3);
51. this.isChange = !this.isChange;
52. this.textName = 'back';
53. } else {
54. this.ctx.clearRect(0, 0, 600, 600);
55. this.path3.setTransform(0.5, -0.1, -0.1, 0.5, 0, 0);
56. this.ctx.stroke(this.path3);
57. this.isChange = !this.isChange;
58. this.textName = 'change';
59. }
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/8jB3Gu0fTaG72H2psS3cIA/zh-cn_image_0000002558604970.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=AD3930157FF5C481D0EDC78CE046CF77DD1E24B2049A691192A365E8914D4C88)
