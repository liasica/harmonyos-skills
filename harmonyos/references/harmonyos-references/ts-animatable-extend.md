---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatable-extend
title: 定义可动画属性 (@AnimatableExtend)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > 定义可动画属性 (@AnimatableExtend)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1105ffa76e91ade0ff6c74be772302714136ee882d02160a589361a9972f0578
---

@AnimatableExtend装饰器用于自定义可动画的属性方法，该装饰器内定义的函数在动画过程中会被逐帧调用，直到动画结束。该装饰器的常见用途有：

1. 使不可动画属性变为可动画属性，自定义数据运算规则使得属性能进行插值运算得到中间结果，再由动画驱动属性从起点值逐渐过渡到终点值。
2. 使属性逐帧变化，实现逐帧布局的效果。

* 可动画属性：如果一个属性方法在animation属性前调用，改变这个属性的值可以使animation属性的动画效果生效，属性有动画过渡效果，这个属性称为可动画属性。比如height、width、backgroundColor、translate属性，和Text组件的fontSize属性等。
* 不可动画属性：如果一个属性方法在animation属性前调用，改变这个属性的值不能使animation属性的动画效果生效，属性突变无动画效果，这个属性称为不可动画属性。比如Polyline组件的points属性等。

说明

该装饰器从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 语法

PhonePC/2in1TabletTVWearable

```
1. @AnimatableExtend(UIComponentName) function functionName(value: typeName) {
2. .propertyName(value)
3. }
```

* @AnimatableExtend仅支持定义在全局，不支持在组件内部定义。
* @AnimatableExtend定义的函数参数类型必须为number类型或者实现 AnimatableArithmetic<T>接口的自定义类型。
* @AnimatableExtend定义的函数体内只能调用@AnimatableExtend括号内组件的属性方法。

## AnimatableArithmetic<T>

PhonePC/2in1TabletTVWearable

该接口定义非number数据类型的动画运算规则。对非number类型的数据（如数组、结构体、颜色等）做动画，需要实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数，使得该数据能参与动画的插值运算和识别该数据是否发生改变。即定义它们为实现了AnimatableArithmetic<T>接口的类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### plus

PhonePC/2in1TabletTVWearable

plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>

定义数据类型的加法运算规则。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic<T>](ts-animatable-extend.md#animatablearithmetict) | 是 | 加法运算的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatableArithmetic<T>](ts-animatable-extend.md#animatablearithmetict) | 加法运算的结果。 |

### subtract

PhonePC/2in1TabletTVWearable

subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>

定义该数据类型的减法运算规则。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic<T>](ts-animatable-extend.md#animatablearithmetict) | 是 | 减法运算的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatableArithmetic<T>](ts-animatable-extend.md#animatablearithmetict) | 减法运算的结果。 |

### multiply

PhonePC/2in1TabletTVWearable

multiply(scale: number): AnimatableArithmetic<T>

定义该数据类型的乘法运算规则。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 乘法运算的系数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatableArithmetic<T>](ts-animatable-extend.md#animatablearithmetict) | 乘法运算的结果。 |

### equals

PhonePC/2in1TabletTVWearable

equals(rhs: AnimatableArithmetic<T>): boolean

定义该数据类型的相等判断规则。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic<T>](ts-animatable-extend.md#animatablearithmetict) | 是 | 和自身比较相等的另一个数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否相等。返回true表示相等，返回false表示不相等。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（逐帧布局的效果）

以下示例通过改变Text组件宽度实现逐帧布局的效果。

```
1. @AnimatableExtend(Text)
2. function animatableWidth(width: number) {
3. .width(width)
4. }

6. @Entry
7. @Component
8. struct AnimatablePropertyExample {
9. @State textWidth: number = 80;

11. build() {
12. Column() {
13. Text("AnimatableProperty")
14. .animatableWidth(this.textWidth)
15. .animation({ duration: 2000, curve: Curve.Ease })
16. Button("Play")
17. .onClick(() => {
18. this.textWidth = this.textWidth == 80 ? 160 : 80;
19. })
20. }.width("100%")
21. .padding(10)
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/U3bXTbBlQgylsjV0rBYAFQ/zh-cn_image_0000002589326485.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055254Z&HW-CC-Expire=86400&HW-CC-Sign=EB42A70B5B688A7F94082127CF584D731D7F642FB216E555F12EAEADB67F8D7D)

### 示例2（折线的动画效果）

以下示例实现折线的动画效果。

```
1. class Point {
2. x: number
3. y: number

5. constructor(x: number, y: number) {
6. this.x = x
7. this.y = y
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
86. struct AnimatablePropertyExample {
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
104. Button("Play")
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
115. }.width("100%")
116. .padding(10)
117. }
118. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/NnfvSUkkR7GZTPfUUlbQ0w/zh-cn_image_0000002589246427.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055254Z&HW-CC-Expire=86400&HW-CC-Sign=78551A73CA78D2BD43AAAB4973B835096BB7A7DF5A20EC7C6A6486E6E17AA38F)
