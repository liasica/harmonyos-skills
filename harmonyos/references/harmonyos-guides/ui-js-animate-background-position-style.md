---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-background-position-style
title: background-position样式动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > CSS动画 > background-position样式动画
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a0f44992143b66acc5a1b26395f328805099da203b02973c10acc2de437873a6
---

通过改变background-position属性（第一个值为X轴的位置，第二个值为Y轴的位置）移动背景图片位置，若背景图位置超出组件则超出部分的背景图不显示。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="content"></div>
4. <div class="content1"></div>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. height: 100%;
4. background-color:#F1F3F5;
5. display: flex;
6. flex-direction: column;
7. justify-content: center;
8. align-items: center;
9. width: 100%;
10. }
11. .content{
12. width: 400px;
13. height: 400px;
14. /* 不建议图片长宽比为1:1 */
15. background-image: url('common/images/bg-tv.jpg');
16. background-size: 100%;
17. background-repeat: no-repeat;
18. animation: change 3s infinite;
19. border: 1px solid black;
20. }
21. .content1{
22. margin-top:50px;
23. width: 400px;
24. height: 400px;
25. background-image: url('common/images/bg-tv.jpg');
26. background-size: 50%;
27. background-repeat: no-repeat;
28. animation: change1 5s infinite;
29. border: 1px solid black;
30. }
31. /* 背景图片移动出组件 */
32. @keyframes change{
33. 0%{
34. background-position:0px top;
35. }
36. 25%{
37. background-position:400px top;
38. }
39. 50%{
40. background-position:0px top;
41. }
42. 75%{
43. background-position:0px bottom;
44. }
45. 100%{
46. background-position:0px top;
47. }
48. }
49. /* 背景图片在组件内移动 */
50. @keyframes change1{
51. 0%{
52. background-position:left top;
53. }
54. 25%{
55. background-position:50% 50%;
56. }
57. 50%{
58. background-position:right bottom;
59. }
60. 100%{
61. background-position:left top;
62. }
63. }
```

说明

background-position仅支持背景图片的移动，不支持背景颜色（background-color）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/NI2EHaC0RsmxxLHVrr63BA/zh-cn_image_0000002583438191.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234032Z&HW-CC-Expire=86400&HW-CC-Sign=ECA2BC28C0E539D8CED441D59540340B1FC8DB201AEF231C9650AFCD0DB6BB73)
