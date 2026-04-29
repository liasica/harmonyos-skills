---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-attribute-animation
title: 自定义属性动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 属性动画 > 自定义属性动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:488bb6f34f072d04da9115558040a8a244ddd4bc3f0c2b51a8885ff8badf9d30
---

属性动画是指当可动画属性的参数值发生变化时，在UI上产生的连续视觉效果。当参数值连续变化，且设置到可以引起UI发生变化的属性接口上时，即可实现属性动画。

ArkUI提供[@AnimatableExtend装饰器](arkts-animatable-extend.md)，用于自定义可动画属性接口。由于参数的数据类型必须具备一定程度的连续性，自定义可动画属性接口的参数类型仅支持number类型和实现[AnimatableArithmetic<T>接口](arkts-animatable-extend.md#animatablearithmetict接口说明)的自定义类型。通过自定义可动画属性接口和可动画数据类型，在使用animateTo或animation执行动画时，通过逐帧回调函数修改不可动画属性接口的值，能够让不可动画属性接口实现动画效果。也可通过逐帧回调函数每帧修改可动画属性的值，实现逐帧布局的效果。

## 使用number数据类型和@AnimatableExtend装饰器改变Text组件宽度实现逐帧布局的效果

```
1. // 第一步：使用@AnimatableExtend装饰器，自定义可动画属性接口
2. @AnimatableExtend(Text)
3. function animatableWidth(width: number) {
4. .width(width) // 调用系统属性接口，逐帧回调函数每帧修改可动画属性的值，实现逐帧布局的效果。
5. }

7. @Entry
8. @Component
9. struct AnimatablePropertyExample {
10. @State textWidth: number = 80; // 80: 初始文本宽度

12. build() {
13. Column() {
14. Text('AnimatableProperty')
15. .animatableWidth(this.textWidth) // 第二步：将自定义可动画属性接口设置到组件上
16. .animation({ duration: 2000, curve: Curve.Ease }) // 第三步:为自定义可动画属性接口绑定动画。
17. Button('Play')
18. .onClick(() => {
19. this.textWidth = this.textWidth == 80 ? 160 : 80; // 第四步：改变自定义可动画属性的参数，产生动画。
20. })
21. }
22. .width('100%')
23. .padding(10) // 10: 内边距
24. }
25. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animatableProperty/template1/Index.ets#L16-L43)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/6scz3Um1R3iBU5fIxubTjQ/zh-cn_image_0000002558604816.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052807Z&HW-CC-Expire=86400&HW-CC-Sign=F4C9D5623DE2C1B151F0C4AED81A91806644CAF90CEAFEDD90B04217B5F81B44)

## 使用自定义数据类型和@AnimatableExtend装饰器改变图形形状

```
1. declare type Point = number[];

3. // 定义可动画属性接口的参数类型，实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数
4. class PointClass extends Array<number> {
5. constructor(value: Point) {
6. super(value[0], value[1]);
7. }

9. add(rhs: PointClass): PointClass {
10. let result: Point = new Array<number>() as Point;
11. for (let i = 0; i < 2; i++) { // 2: 二维坐标点
12. result.push(rhs[i] + this[i]);
13. }
14. return new PointClass(result);
15. }

17. subtract(rhs: PointClass): PointClass {
18. let result: Point = new Array<number>() as Point;
19. for (let i = 0; i < 2; i++) { // 2: 二维坐标点
20. result.push(this[i] - rhs[i]);
21. }
22. return new PointClass(result);
23. }

25. multiply(scale: number): PointClass {
26. let result: Point = new Array<number>() as Point;
27. for (let i = 0; i < 2; i++) { // 2: 二维坐标点
28. result.push(this[i] * scale);
29. }
30. return new PointClass(result);
31. }
32. }

34. // 定义可动画属性接口的参数类型，实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数
35. // 模板T支持嵌套实现AnimatableArithmetic<T>的类型
36. class PointVector extends Array<PointClass> implements AnimatableArithmetic<Array<Point>> {
37. constructor(initialValue: Array<Point>) {
38. super();
39. if (initialValue.length) {
40. initialValue.forEach((p: Point) => this.push(new PointClass(p)));
41. }
42. }

44. // implement the IAnimatableArithmetic interface
45. plus(rhs: PointVector): PointVector {
46. let result = new PointVector([]);
47. const len = Math.min(this.length, rhs.length);
48. for (let i = 0; i < len; i++) {
49. result.push(this[i].add(rhs[i]));
50. }
51. return result;
52. }

54. subtract(rhs: PointVector): PointVector {
55. let result = new PointVector([]);
56. const len = Math.min(this.length, rhs.length);
57. for (let i = 0; i < len; i++) {
58. result.push(this[i].subtract(rhs[i]));
59. }
60. return result;
61. }

63. multiply(scale: number): PointVector {
64. let result = new PointVector([]);
65. for (let i = 0; i < this.length; i++) {
66. result.push(this[i].multiply(scale));
67. }
68. return result;
69. }

71. equals(rhs: PointVector): boolean {
72. if (this.length !== rhs.length) {
73. return false;
74. }
75. for (let index = 0, size = this.length; index < size; ++index) {
76. if (this[index][0] !== rhs[index][0] || this[index][1] !== rhs[index][1]) {
77. return false;
78. }
79. }
80. return true;
81. }
82. }

84. // 自定义可动画属性接口
85. @AnimatableExtend(Polyline)
86. function animatablePoints(points: PointVector) {
87. .points(points);
88. }

90. @Entry
91. @Component
92. struct AnimatedShape {
93. squareStartPointX: number = 75; // 75: 正方形起始点X坐标
94. squareStartPointY: number = 25; // 25: 正方形起始点Y坐标
95. squareWidth: number = 150; // 150: 正方形宽度
96. squareEndTranslateX: number = 50; // 50: 正方形结束位置X轴平移量
97. squareEndTranslateY: number = 50; // 50: 正方形结束位置Y轴平移量
98. @State pointVec1: PointVector = new PointVector([
99. [this.squareStartPointX, this.squareStartPointY],
100. [this.squareStartPointX + this.squareWidth, this.squareStartPointY],
101. [this.squareStartPointX + this.squareWidth, this.squareStartPointY + this.squareWidth],
102. [this.squareStartPointX, this.squareStartPointY + this.squareWidth]
103. ]);
104. @State pointVec2: PointVector = new PointVector([
105. [this.squareStartPointX + this.squareEndTranslateX, this.squareStartPointY + this.squareStartPointY],
106. [this.squareStartPointX + this.squareWidth + this.squareEndTranslateX,
107. this.squareStartPointY + this.squareStartPointY],
108. [this.squareStartPointX + this.squareWidth, this.squareStartPointY + this.squareWidth],
109. [this.squareStartPointX, this.squareStartPointY + this.squareWidth]
110. ]);
111. @State color: Color = Color.Green;
112. @State fontSize: number = 20.0; // 20.0: 字体大小
113. @State polyline1Vec: PointVector = this.pointVec1;
114. @State polyline2Vec: PointVector = this.pointVec2;

116. build() {
117. Row() {
118. Polyline()
119. .width(300) // 300: 折线宽度
120. .height(200) // 200: 折线高度
121. .backgroundColor('#0C000000') // 0C000000: 背景颜色（黑色带透明度）
122. .fill('#317AF7') // 317AF7: 填充颜色（蓝色）
123. .animatablePoints(this.polyline1Vec)
124. .animation({ duration: 2000, delay: 0, curve: Curve.Ease }) // 2000: 动画持续时间（毫秒），0: 动画延迟时间
125. .onClick(() => {
126. if (this.polyline1Vec.equals(this.pointVec1)) {
127. this.polyline1Vec = this.pointVec2;
128. } else {
129. this.polyline1Vec = this.pointVec1;
130. }
131. })
132. }
133. .width('100%').height('100%').justifyContent(FlexAlign.Center)
134. }
135. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animatableProperty/template2/Index.ets#L16-L153)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/eixtg6gISBWtoA8fC3ulfg/zh-cn_image_0000002589324341.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052807Z&HW-CC-Expire=86400&HW-CC-Sign=2139526FA70426D60A763AAFD9908E1076B276EAAA7E31354B06E2D0F65EABEB)
