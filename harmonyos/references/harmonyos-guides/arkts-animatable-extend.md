---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animatable-extend
title: @AnimatableExtend装饰器：定义可动画属性
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > @AnimatableExtend装饰器：定义可动画属性
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:262ad18585cafefe3dadcda8faa118bc02fd4171933bbd09695f6eee67368532
---

@AnimatableExtend装饰器用于自定义可动画的属性方法，在这个属性方法中修改组件不可动画的属性。在动画执行过程中，通过逐帧回调函数修改不可动画属性值，让不可动画属性也能实现动画效果。也可通过逐帧回调函数修改可动画属性的值，实现逐帧布局的效果。

* 可动画属性：如果一个属性方法在[animation](arkts-animation.md)属性前调用，改变这个属性的值可以使animation属性的动画效果生效，这个属性称为可动画属性。比如height、width、backgroundColor、translate属性，和Text组件的fontSize属性等。
* 不可动画属性：如果一个属性方法在animation属性前调用，改变这个属性的值不能使animation属性的动画效果生效，这个属性称为不可动画属性。比如Polyline组件的points属性等。

说明

该装饰器从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

### 语法

```
1. @AnimatableExtend(UIComponentName) function functionName(value: typeName) {
2. .propertyName(value)
3. }
```

* @AnimatableExtend仅支持定义在全局，不支持在组件内部定义。
* @AnimatableExtend定义的函数参数类型必须为number类型或者实现 AnimatableArithmetic<T>接口的自定义类型。
* @AnimatableExtend定义的函数体内只能调用@AnimatableExtend括号内组件的属性方法。

### AnimatableArithmetic<T>接口说明

该接口定义非number数据类型的动画运算规则。对非number类型的数据（如数组、结构体、颜色等）做动画，需要实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数，使得该数据能参与动画的插值运算和识别该数据是否发生改变。即定义它们为实现了AnimatableArithmetic<T>接口的类型。

| 名称 | 入参类型 | 返回值类型 | 说明 |
| --- | --- | --- | --- |
| plus | AnimatableArithmetic<T> | AnimatableArithmetic<T> | 定义该数据类型的加法运算规则 |
| subtract | AnimatableArithmetic<T> | AnimatableArithmetic<T> | 定义该数据类型的减法运算规则 |
| multiply | number | AnimatableArithmetic<T> | 定义该数据类型的乘法运算规则 |
| equals | AnimatableArithmetic<T> | boolean | 定义该数据类型的相等判断规则 |

## 使用场景

以下示例通过改变Text组件宽度实现逐帧布局的效果。

```
1. @AnimatableExtend(Text)
2. function animatableWidth(width: number) {
3. .width(width)
4. }

6. @Entry
7. @Component
8. struct AnimatablePropertyText {
9. @State textWidth: number = 80;

11. build() {
12. Column() {
13. Text('AnimatableProperty')
14. .animatableWidth(this.textWidth)
15. .animation({ duration: 2000, curve: Curve.Ease })
16. Button('Play')
17. .onClick(() => {
18. this.textWidth = this.textWidth == 80 ? 160 : 80;
19. })
20. }.width('100%')
21. .padding(10)
22. }
23. }
```

[AnimatablePropertyText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentExtension/entry/src/main/ets/pages/AnimatableExtendDecorator/AnimatablePropertyText.ets#L16-L40)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/nkV0ut89QQ6xW_rYuP9vmw/zh-cn_image_0000002589323945.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052707Z&HW-CC-Expire=86400&HW-CC-Sign=4E5BCA8A0F6965457E5975D10CFC391CC791CC02DF192DD4C1715558BF02E347)

以下示例实现折线的动画效果。

```
1. class Point {
2. x: number;
3. y: number;

5. constructor(x: number, y: number) {
6. this.x = x;
7. this.y = y;
8. }

10. plus(rhs: Point): Point {
11. return new Point(this.x + rhs.x, this.y + rhs.y);
12. }

14. subtract(rhs: Point): Point {
15. return new Point(this.x - rhs.x, this.y - rhs.y);
16. }

18. multiply(scale: number): Point {
19. return new Point(this.x * scale, this.y * scale);
20. }

22. equals(rhs: Point): boolean {
23. return this.x === rhs.x && this.y === rhs.y;
24. }
25. }

27. // PointVector实现了AnimatableArithmetic<T>接口
28. class PointVector extends Array<Point> implements AnimatableArithmetic<PointVector> {
29. constructor(value: Array<Point>) {
30. super();
31. value.forEach(p => this.push(p));
32. }

34. plus(rhs: PointVector): PointVector {
35. let result = new PointVector([]);
36. const len = Math.min(this.length, rhs.length);
37. for (let i = 0; i < len; i++) {
38. result.push((this as Array<Point>)[i].plus((rhs as Array<Point>)[i]));
39. }
40. return result;
41. }

43. subtract(rhs: PointVector): PointVector {
44. let result = new PointVector([]);
45. const len = Math.min(this.length, rhs.length);
46. for (let i = 0; i < len; i++) {
47. result.push((this as Array<Point>)[i].subtract((rhs as Array<Point>)[i]));
48. }
49. return result;
50. }

52. multiply(scale: number): PointVector {
53. let result = new PointVector([]);
54. for (let i = 0; i < this.length; i++) {
55. result.push((this as Array<Point>)[i].multiply(scale));
56. }
57. return result;
58. }

60. equals(rhs: PointVector): boolean {
61. if (this.length != rhs.length) {
62. return false;
63. }
64. for (let i = 0; i < this.length; i++) {
65. if (!(this as Array<Point>)[i].equals((rhs as Array<Point>)[i])) {
66. return false;
67. }
68. }
69. return true;
70. }

72. get(): Array<Object[]> {
73. let result: Array<Object[]> = [];
74. this.forEach(p => result.push([p.x, p.y]));
75. return result;
76. }
77. }

79. @AnimatableExtend(Polyline)
80. function animatablePoints(points: PointVector) {
81. .points(points.get())
82. }

84. @Entry
85. @Component
86. struct  AnimatablePropertyExample {
87. @State points: PointVector = new PointVector([
88. new Point(50, Math.random() * 200),
89. new Point(100, Math.random() * 200),
90. new Point(150, Math.random() * 200),
91. new Point(200, Math.random() * 200),
92. new Point(250, Math.random() * 200),
93. ])

95. build() {
96. Column() {
97. Polyline()
98. .animatablePoints(this.points)
99. .animation({ duration: 1000, curve: Curve.Ease })// 设置动画参数
100. .size({ height: 220, width: 300 })
101. .fill(Color.Green)
102. .stroke(Color.Red)
103. .backgroundColor('#eeaacc')
104. Button('Play')
105. .onClick(() => {
106. // points是实现了可动画协议的数据类型，points在动画过程中可按照定义的运算规则、动画参数从之前的PointVector变为新的PointVector数据，产生每一帧的PointVector数据，进而产生动画
107. this.points = new PointVector([
108. new Point(50, Math.random() * 200),
109. new Point(100, Math.random() * 200),
110. new Point(150, Math.random() * 200),
111. new Point(200, Math.random() * 200),
112. new Point(250, Math.random() * 200),
113. ]);
114. })
115. }.width('100%')
116. .padding(10)
117. }
118. }
```

[AnimatablePropertyExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentExtension/entry/src/main/ets/pages/AnimatableExtendDecorator/AnimatablePropertyExample.ets#L16-L135)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Qs7J_SXQRj6ZPtbXJ9g5Vw/zh-cn_image_0000002589243885.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052707Z&HW-CC-Expire=86400&HW-CC-Sign=D552E29B2524F41328508AA71743893080C0E337C1B629242535D7B462E1B36D)
