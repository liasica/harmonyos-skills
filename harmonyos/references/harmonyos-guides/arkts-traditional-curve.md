---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-traditional-curve
title: 传统曲线
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画曲线 > 传统曲线
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4712cf9604aa53a31d2c8e648e6388d9c218179f328ee85320fa9e712b8f2a5a
---

传统曲线基于数学公式，创造形状符合开发者预期的动画曲线。以三阶贝塞尔曲线为代表，通过调整曲线控制点，可以改变曲线形状，从而带来缓入、缓出等动画效果。对于同一条传统曲线，由于不具备物理含义，其形状不会因为用户行为发生任何改变，缺少物理动画的自然感和生动感。建议优先采用物理曲线创建动画，将传统曲线作为辅助用于极少数必要场景中。

ArkUI提供了贝塞尔曲线、阶梯曲线等传统曲线接口，开发者可参照[插值计算](../harmonyos-references/js-apis-curve.md)进行查阅。

传统曲线的示例和效果如下：

```
1. class TraditionalCurve {
2. public title: string;
3. public curve: Curve;
4. public color: Color | string;

6. constructor(title: string, curve: Curve, color: Color | string = '') {
7. this.title = title;
8. this.curve = curve;
9. this.color = color;
10. }
11. }

13. const traditionalCurves: TraditionalCurve[] = [
14. new TraditionalCurve(' Linear', Curve.Linear, '#317AF7'),
15. new TraditionalCurve(' Ease', Curve.Ease, '#D94838'),
16. new TraditionalCurve(' EaseIn', Curve.EaseIn, '#DB6B42'),
17. new TraditionalCurve(' EaseOut', Curve.EaseOut, '#5BA854'),
18. new TraditionalCurve(' EaseInOut', Curve.EaseInOut, '#317AF7'),
19. new TraditionalCurve(' FastOutSlowIn', Curve.FastOutSlowIn, '#D94838')
20. ]

22. @Entry
23. @Component
24. struct CurveDemo {
25. @State dRotate: number = 0; // 旋转角度

27. build() {
28. Column() {
29. // 曲线图例
30. Grid() {
31. ForEach(traditionalCurves, (item: TraditionalCurve) => {
32. GridItem() {
33. Column() {
34. Row()
35. .width(30)
36. .height(30)
37. .borderRadius(15)
38. .backgroundColor(item.color)
39. Text(item.title)
40. .fontSize(15)
41. .fontColor(0x909399)
42. }
43. .width('100%')
44. }
45. })
46. }
47. .columnsTemplate('1fr 1fr 1fr')
48. .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
49. .padding(10)
50. .width('100%')
51. .height(300)
52. .margin({ top: 50 })

54. Stack() {
55. // 摆动管道
56. Row()
57. .width(290)
58. .height(290)
59. .border({
60. width: 15,
61. color: 0xE6E8EB,
62. radius: 145
63. })

65. ForEach(traditionalCurves, (item: TraditionalCurve) => {
66. // 小球
67. Column() {
68. Row()
69. .width(30)
70. .height(30)
71. .borderRadius(15)
72. .backgroundColor(item.color)
73. }
74. .width(20)
75. .height(300)
76. .rotate({ angle: this.dRotate })
77. .animation({
78. duration: 2000,
79. iterations: -1,
80. curve: item.curve,
81. delay: 100
82. })
83. })
84. }
85. .width('100%')
86. .height(200)
87. .onClick(() => {
88. this.dRotate ? null : this.dRotate = 360;
89. })
90. }
91. .width('100%')
92. }
93. }
```

[CurveDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/traditionalCurve/template1/CurveDemo.ets#L16-L111)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/JOqruktyToCIMmY8uYZ7iA/zh-cn_image_0000002589244295.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052812Z&HW-CC-Expire=86400&HW-CC-Sign=F2656939DC6484EBD316A0EA7AD57EA4DC7735935E088F77705635621347E2BE)
