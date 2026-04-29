---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-animation
title: 动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2a4d81e1109a97305ec6583bcaa3760fb6a574e987c2a848439fbc95d67b712a
---

动画分为[静态动画](ui-js-building-ui-animation.md#静态动画)和[连续动画](ui-js-building-ui-animation.md#连续动画)。

## 静态动画

静态动画的核心是transform样式，主要可以实现以下三种变换类型，一次样式设置只能实现一种类型变换。

* **translate**：沿水平或垂直方向将指定组件移动所需距离。
* **scale**：横向或纵向将指定组件缩小或放大到所需比例。
* **rotate**：将指定组件沿横轴或纵轴或中心点旋转指定的角度。

具体的使用示例如下，更多信息请参考[动画样式](../harmonyos-references/js-components-common-animation.md)。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="translate">hello</text>
4. <text class="rotate">hello</text>
5. <text class="scale">hello</text>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. flex-direction: column;
5. align-items: center;
6. }
7. .translate {
8. height: 150px;
9. width: 300px;
10. margin: 50px;
11. font-size: 50px;
12. background-color: #008000;
13. transform: translate(200px);
14. }
15. .rotate {
16. height: 150px;
17. width: 300px;
18. margin: 50px;
19. font-size: 50px;
20. background-color: #008000;
21. transform-origin: 200px 100px;
22. transform: rotate(45deg);
23. }
24. .scale {
25. height: 150px;
26. width: 300px;
27. margin: 50px;
28. font-size: 50px;
29. background-color: #008000;
30. transform: scaleX(1.5);
31. }
```

**图1** 静态动画效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/cqFWoNrjRz6AGqir5Z3Haw/zh-cn_image_0000002558764574.png?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=298ED5A422FBDE6648B1B9E7472EBE7D3428F0BC2CA4F0BC67F3D579856B1B3B)

## 连续动画

静态动画只有开始状态和结束状态，没有中间状态，如果需要设置中间的过渡状态和转换效果，需要使用连续动画实现。

连续动画的核心是animation样式，它定义了动画的开始状态、结束状态以及时间和速度的变化曲线。通过animation样式可以实现的效果有：

* **animation-name**：设置动画执行后应用到组件上的背景颜色、透明度、宽高和变换类型。
* **animation-delay**和**animation-duration**：分别设置动画执行后元素延迟和持续的时间。
* **animation-timing-function**：描述动画执行的速度曲线，使动画更加平滑。
* **animation-iteration-count**：定义动画播放的次数。
* **animation-fill-mode**：指定动画执行结束后是否恢复初始状态。

animation样式需要在css文件中先定义keyframe，在keyframe中设置动画的过渡效果，并通过一个样式类型在hml文件中调用。animation-name的使用示例如下：

```
1. <!-- xxx.hml -->
2. <div class="item-container">
3. <div class="item {{colorParam}}">
4. <text class="txt">color</text>
5. </div>
6. <div class="item {{opacityParam}}">
7. <text class="txt">opacity</text>
8. </div>
9. <input class="button" type="button" name="" value="show" onclick="showAnimation"/>
10. </div>
```

```
1. /* xxx.css */
2. .item-container {
3. margin: 60px;
4. flex-direction: column;
5. }
6. .item {
7. width: 80%;
8. background-color: #f76160;
9. }
10. .txt {
11. text-align: center;
12. width: 200px;
13. height: 100px;
14. }
15. .button {
16. width: 200px;
17. margin: 10px;
18. font-size: 30px;
19. background-color: #09ba07;
20. }
21. .color {
22. animation-name: Color;
23. animation-duration: 8000ms;
24. }
25. .opacity {
26. animation-name: Opacity;
27. animation-duration: 8000ms;
28. }
29. @keyframes Color {
30. from {
31. background-color: #f76160;
32. }
33. to {
34. background-color: #09ba07;
35. }
36. }
37. @keyframes Opacity {
38. from {
39. opacity: 0.9;
40. }
41. to {
42. opacity: 0.1;
43. }
44. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. colorParam: '',
5. opacityParam: '',
6. },
7. showAnimation: function () {
8. this.colorParam = '';
9. this.opacityParam = '';
10. this.colorParam = 'color';
11. this.opacityParam = 'opacity';
12. }
13. }
```

**图2** 连续动画效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/gcfragmpQR6xvGZK31Ot0g/zh-cn_image_0000002558604918.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=25166135C27B5E71126DF48D8B37B31DE6D1F3E702C1BECEAE355F3426AB9784)
