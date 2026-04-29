---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-color-effect
title: 色彩
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画效果 > 色彩
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df78a6fb73f0a000e1daa5aa85b62ea012a90ae548732ed0a88254815fb9cf9a
---

## 色彩

通过颜色渐变接口，可以设置组件的背景颜色渐变效果，实现在两个或多个指定的颜色之间进行平稳的过渡。

| 接口 | 说明 |
| --- | --- |
| [linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient) | 为当前组件添加线性渐变的颜色渐变效果。 |
| [sweepGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#sweepgradient) | 为当前组件添加角度渐变的颜色渐变效果。 |
| [radialGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#radialgradient) | 为当前组件添加径向渐变的颜色渐变效果。 |

## 为组件添加线性渐变效果

```
1. @Entry
2. @Component
3. struct LinearGradientDemo {
4. build() {
5. Grid() {
6. GridItem() {
7. Column() {
8. Text('angle: 180')
9. .fontSize(15)
10. }
11. .width(100)
12. .height(100)
13. .justifyContent(FlexAlign.Center)
14. .borderRadius(10)
15. .linearGradient({
16. // 0点方向顺时针旋转为正向角度，线性渐变起始角度的默认值为180°
17. colors: [
18. [0xf56c6c, 0.0], // 颜色断点1的颜色和比重，对应组件在180°方向上的起始位置
19. [0xffffff, 1.0],// 颜色断点2的颜色和比重，对应组件在180°方向上的终点位置
20. ]
21. })
22. }

24. GridItem() {
25. Column() {
26. Text('angle: 45')
27. .fontSize(15)
28. }
29. .width(100)
30. .height(100)
31. .justifyContent(FlexAlign.Center)
32. .borderRadius(10)
33. .linearGradient({
34. angle: 45, // 设置颜色渐变起始角度为顺时针方向45°
35. colors: [
36. [0xf56c6c, 0.0],
37. [0xffffff, 1.0],
38. ]
39. })
40. }

42. GridItem() {
43. Column() {
44. Text('repeat: true')
45. .fontSize(15)
46. }
47. .width(100)
48. .height(100)
49. .justifyContent(FlexAlign.Center)
50. .borderRadius(10)
51. .linearGradient({
52. repeating: true, // 在当前组件内0.3到1.0区域内重复0到0.3区域的颜色渐变效果
53. colors: [
54. [0xf56c6c, 0.0],
55. [0xE6A23C, 0.3],
56. ]
57. })
58. }

60. GridItem() {
61. Column() {
62. Text('repeat: false')
63. .fontSize(15)
64. }
65. .width(100)
66. .height(100)
67. .justifyContent(FlexAlign.Center)
68. .borderRadius(10)
69. .linearGradient({
70. colors: [
71. [0xf56c6c, 0.0], // repeating默认为false，此时组件内只有0到0.3区域内存在颜色渐变效果
72. [0xE6A23C, 0.3],
73. ]
74. })
75. }
76. }
77. .columnsGap(10)
78. .rowsGap(10)
79. .columnsTemplate('1fr 1fr')
80. .rowsTemplate('1fr 1fr 1fr')
81. .width('100%')
82. .height('100%')
83. }
84. }
```

[LinearGradientEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GradientEffect/entry/src/main/ets/homePage/LinearGradientEffect.ets#L16-L101)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/-5_KEWx_Q6eucHW3bFF-SQ/zh-cn_image_0000002558604836.png?HW-CC-KV=V1&HW-CC-Date=20260429T052815Z&HW-CC-Expire=86400&HW-CC-Sign=C800E6AE4BD99F613040D254D135F80C2450B2B77804FAB4953F58489B94B7B6)

## 为组件添加角度渐变效果

```
1. @Entry
2. @Component
3. struct SweepGradientDemo {
4. build() {
5. Grid() {
6. GridItem() {
7. Column() {
8. Text('center: 50')
9. .fontSize(15)
10. }
11. .width(100)
12. .height(100)
13. .justifyContent(FlexAlign.Center)
14. .borderRadius(10)
15. .sweepGradient({
16. center: [50, 50], // 角度渐变中心点
17. start: 0, // 角度渐变的起点
18. end: 360, // 角度渐变的终点。
19. repeating: true, // 渐变效果在重复
20. colors: [
21. // 当前组件中，按照中心点和渐变的起点和终点值,
22. // 角度区域为0-0.125的范围，从颜色断点1的颜色渐变到颜色断点2的颜色,
23. // 角度区域0.125到0.25的范围，从颜色断点2的颜色渐变到颜色断点3的颜色,
24. // 因为repeating设置为true，角度区域0.25到1的范围，重复区域0到0.25的颜色渐变效果
25. [0xf56c6c, 0], // 颜色断点1的颜色和比重，对应角度为0*360°=0°，角点为中心点
26. [0xffffff, 0.125], // 颜色断点2的颜色和比重
27. [0x409EFF, 0.25]// 颜色断点3的颜色和比重
28. ]
29. })
30. }

32. GridItem() {
33. Column() {
34. Text('center: 0')
35. .fontSize(15)
36. }
37. .width(100)
38. .height(100)
39. .justifyContent(FlexAlign.Center)
40. .borderRadius(10)
41. .sweepGradient({
42. center: [0, 0], // 角度渐变中心点，当前为组件的左上角坐标
43. start: 0,
44. end: 360,
45. repeating: true,
46. colors: [
47. // 当前组件中，因为角度渐变中心是组件的左上角，所以从颜色断点1到颜色断点3的角度范围，恰好可以覆盖整个组件
48. [0xf56c6c, 0], // 颜色断点1的颜色和比重，对应角度为0*360°=0°
49. [0xffffff, 0.125], // 颜色断点2的颜色和比重，对应角度为0.125*360°=45°
50. [0x409EFF, 0.25]// 颜色断点3的颜色和比重，对应角度为0.25*360°=90°
51. ]
52. })
53. }

55. GridItem() {
56. Column() {
57. Text('repeat: true')
58. .fontSize(15)
59. }
60. .width(100)
61. .height(100)
62. .justifyContent(FlexAlign.Center)
63. .borderRadius(10)
64. .sweepGradient({
65. center: [50, 50],
66. start: 0,
67. end: 360,
68. repeating: true,
69. colors: [
70. [0xf56c6c, 0],
71. [0xffffff, 0.125],
72. [0x409EFF, 0.25]
73. ]
74. })
75. }

77. GridItem() {
78. Column() {
79. Text('repeat: false')
80. .fontSize(15)
81. }
82. .width(100)
83. .height(100)
84. .justifyContent(FlexAlign.Center)
85. .borderRadius(10)
86. .sweepGradient({
87. center: [50, 50],
88. start: 0,
89. end: 360,
90. repeating: false, //只在颜色断点角度覆盖范围内产生颜色渐变效果，其余范围内不重复
91. colors: [
92. [0xf56c6c, 0],
93. [0xffffff, 0.125],
94. [0x409EFF, 0.25]
95. ]
96. })
97. }
98. }
99. .columnsGap(10)
100. .rowsGap(10)
101. .columnsTemplate('1fr 1fr')
102. .rowsTemplate('1fr 1fr 1fr')
103. .width('100%')
104. .height(437)
105. }
106. }
```

[DirectionGradientEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GradientEffect/entry/src/main/ets/homePage/DirectionGradientEffect.ets#L16-L123)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/_XFSWXyCQCm938KiQN1Kkg/zh-cn_image_0000002589324361.png?HW-CC-KV=V1&HW-CC-Date=20260429T052815Z&HW-CC-Expire=86400&HW-CC-Sign=B28F0E444BA2CAA23C45696B248814AEEC861E4FC910BA62BD41CAA03A4ED404)

## 为组件添加径向渐变效果

```
1. @Entry
2. @Component
3. struct RadialGradientDemo {
4. build() {
5. Grid() {
6. GridItem() {
7. Column() {
8. Text('center: 50')
9. .fontSize(15)
10. }
11. .width(100)
12. .height(100)
13. .justifyContent(FlexAlign.Center)
14. .borderRadius(10)
15. .radialGradient({
16. center: [50, 50], // 径向渐变中心点
17. radius: 100, // 径向渐变半径
18. repeating: true, // 允许在组件内渐变范围外重复按照渐变范围内效果着色
19. colors: [
20. // 组件内以[50，50]为中心点，在半径为0到12.5的范围内从颜色断点1的颜色渐变到颜色断点2的颜色,
21. // 在半径为12.5到25的范围内从颜色断点2的颜色渐变到颜色断点3的颜色,
22. // 组件外其他半径范围内按照半径为0到25的渐变效果重复着色
23. [0xf56c6c, 0], // 颜色断点1的颜色和比重，对应半径为0*100=0
24. [0xffffff, 0.125], // 颜色断点2的颜色和比重，对应半径为0.125*100=12.5
25. [0x409EFF, 0.25]// 颜色断点3的颜色和比重，对应半径为0.25*100=25
26. ]
27. })
28. }

30. GridItem() {
31. Column() {
32. Text('center: 0')
33. .fontSize(15)
34. }
35. .width(100)
36. .height(100)
37. .justifyContent(FlexAlign.Center)
38. .borderRadius(10)
39. .radialGradient({
40. center: [0, 0], // 径向渐变中心点，当前为组件左上角坐标
41. radius: 100,
42. repeating: true,
43. colors: [
44. [0xf56c6c, 0],
45. [0xffffff, 0.125],
46. [0x409EFF, 0.25]
47. ]
48. })
49. }

51. GridItem() {
52. Column() {
53. Text('repeat: true')
54. .fontSize(15)
55. }
56. .width(100)
57. .height(100)
58. .justifyContent(FlexAlign.Center)
59. .borderRadius(10)
60. .radialGradient({
61. center: [50, 50],
62. radius: 100,
63. repeating: true,
64. colors: [
65. [0xf56c6c, 0],
66. [0xffffff, 0.125],
67. [0x409EFF, 0.25]
68. ]
69. })
70. }

72. GridItem() {
73. Column() {
74. Text('repeat: false')
75. .fontSize(15)
76. }
77. .width(100)
78. .height(100)
79. .justifyContent(FlexAlign.Center)
80. .borderRadius(10)
81. .radialGradient({
82. center: [50, 50],
83. radius: 100,
84. repeating: false, // 在组件内渐变范围外不重复按照渐变范围内效果着色
85. colors: [
86. [0xf56c6c, 0],
87. [0xffffff, 0.125],
88. [0x409EFF, 0.25]
89. ]
90. })
91. }
92. }
93. .columnsGap(10)
94. .rowsGap(10)
95. .columnsTemplate('1fr 1fr')
96. .rowsTemplate('1fr 1fr 1fr')
97. .width('100%')
98. .height('100%')
99. }
100. }
```

[RadialGradientEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GradientEffect/entry/src/main/ets/homePage/RadialGradientEffect.ets#L16-L117)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/OWTMjlR9SMG09HNP-jTq3A/zh-cn_image_0000002589244301.png?HW-CC-KV=V1&HW-CC-Date=20260429T052815Z&HW-CC-Expire=86400&HW-CC-Sign=DDEBA547D5A8437AC2BA22C4BDFE6F8FEA23A6508F04D8F80682DA130FDFD9B2)
