---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-attribute-style
title: 属性样式动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > CSS动画 > 属性样式动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0c8611f9c8ccd220dd74a5bb1c951c45e0391657641b98608f3095eed6bb40af
---

在关键帧（Keyframes）中动态设置父组件的width和height，实现组件变大缩小。子组件设置scale属性使父子组件同时缩放，再设置opacity实现父子组件的显示与隐藏。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="fade">
4. <text>fading away</text>
5. </div>
6. <div class="bigger">
7. <text>getting bigger</text>
8. </div>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. background-color:#F1F3F5;
4. display: flex;
5. justify-content: center;
6. align-items: center;
7. flex-direction: column;
8. width: 100%;
9. height: 100%;
10. }
11. .fade {
12. width: 30%;
13. height: 200px;
14. left: 35%;
15. top: 25%;
16. position: absolute;
17. animation: 2s change infinite friction;
18. }
19. .bigger {
20. width: 20%;
21. height: 100px;
22. background-color: blue;
23. animation: 2s change1 infinite linear-out-slow-in;
24. }
25. text {
26. width: 100%;
27. height: 100%;
28. text-align: center;
29. color: white;
30. font-size: 35px;
31. animation: 2s change2 infinite linear-out-slow-in;
32. }
33. /* 颜色变化 */
34. @keyframes change{
35. from {
36. background-color: #f76160;
37. opacity: 1;
38. }
39. to {
40. background-color: #09ba07;
41. opacity: 0;
42. }
43. }
44. /* 父组件大小变化 */
45. @keyframes change1 {
46. 0% {
47. width: 20%;
48. height: 100px;
49. }
50. 100% {
51. width: 80%;
52. height: 200px;
53. }
54. }
55. /* 子组件文字缩放 */
56. @keyframes change2 {
57. 0% {
58. transform: scale(0);
59. }
60. 100% {
61. transform: scale(1.5);
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/ItAwCy9OTUKUqvB3V53xaQ/zh-cn_image_0000002589324503.gif)

说明

* animation取值不区分先后，duration （动画执行时间）/ delay （动画延迟执行时间）按照出现的先后顺序解析。
* 必须设置animation-duration样式，否则时长为0则不会有动画效果。当设置animation-fill-mode属性为forwards时，组件直接展示最后一帧的样式。
