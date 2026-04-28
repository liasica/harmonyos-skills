---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localbuilder
title: @LocalBuilder装饰器： 维持组件关系
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > @LocalBuilder装饰器： 维持组件关系
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d87e6125a1264053ffefed1293fd927e8a73e1bc934d43e4542926ce2cda3ca3
---

当开发者使用局部@Builder进行引用数据传递时，需要考虑组件的父子关系。然而在使用.bind(this)的方式更改函数调用上下文后，会出现组件的父子关系与状态管理的父子关系不一致的问题。为了解决这一问题，引入@LocalBuilder装饰器。@LocalBuilder拥有和局部@Builder相同的功能，且比局部@Builder能够更好的确定组件的父子关系和状态管理的父子关系。

在阅读本文档前，建议提前阅读：[@Builder](arkts-builder.md)。

说明

从API version 12开始支持。

从API version 12开始，该装饰器支持在ArkTS卡片中使用。

从API version 12开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

### 自定义组件内自定义构建函数

定义的语法：

```
1. @LocalBuilder
2. myBuilderFunction() {
3. // ···
4. }
```

[CustomBuilderInComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/CustomBuilderInComponent.ets#L36-L47)

使用方法：

```
1. this.myBuilderFunction()
```

[CustomBuilderInComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/CustomBuilderInComponent.ets#L51-L53)

* 允许在自定义组件内定义一个或多个@LocalBuilder函数，该函数被视为是该组件的私有、特殊类型的成员函数。
* 自定义构建函数可以在所属组件的build函数和其他自定义构建函数中调用，但不允许在组件外调用。
* 在自定义函数体中，this指代当前所属组件，组件的状态变量可以在自定义构建函数内访问。建议通过this访问自定义组件的状态变量而不是参数传递。

## @LocalBuilder和局部@Builder使用区别

跨组件传递局部@Builder函数时，会使用.bind(this)更改函数上下文，但这可能会导致组件的父子关系与状态管理的父子关系不一致。而@LocalBuilder无论是否使用.bind(this)，都不会改变组件的父子关系，即@LocalBuilder中定义组件所属的父组件是确定的，无法被改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Z-K6YKkETkKXjVjWRsIhSg/zh-cn_image_0000002552957576.png?HW-CC-KV=V1&HW-CC-Date=20260427T233855Z&HW-CC-Expire=86400&HW-CC-Sign=2F0B337095EFB725FABD232125BCB7397061696570BC1B74BE8E84B0B118A19F)

说明

bind()方法创建一个新的函数，称为绑定函数，当调用者绑定bind()时，该绑定函数会以创建时传入的第一个this作为原函数的this。

下方用例中，当函数componentBuilder被@Builder修饰时，显示效果为“Child”；当函数componentBuilder被@LocalBuilder修饰时，显示效果是“Parent”。

```
1. @Component
2. struct Child {
3. label: string = 'Child';
4. @BuilderParam customBuilderParam: () => void;

6. build() {
7. Column() {
8. this.customBuilderParam()
9. }
10. }
11. }

13. @Entry
14. @Component
15. struct Parent {
16. label: string = 'Parent';

18. @Builder
19. componentBuilder() {
20. Text(`${this.label}`) // @Builder内的this指向实际调用点的组件，在这个用例中因为调用点在Child组件内，所以this实际指向Child组件
21. }

23. @LocalBuilder
24. componentLocalBuilder() {
25. Text(`${this.label}`) // @LocalBuilder内的this指向声明@LocalBuilder函数Parent组件
26. }

28. build() {
29. Column() {
30. Child({ customBuilderParam: this.componentBuilder }) // Child组件内调用customBuilderParam显示字符串Child。
31. Child({ customBuilderParam: this.componentLocalBuilder }) // Child组件内调用customBuilderParam显示字符串Parent，传递函数本身写法。
32. Child({
33. customBuilderParam: () => {
34. this.componentLocalBuilder()
35. }
36. }) // Child组件内调用customBuilderParam显示字符串Parent，() => { 函数调用 }写法。
37. }
38. }
39. }
```

[ComponentBuilderModify.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/ComponentBuilderModify.ets#L15-L48)

## 限制条件

* @LocalBuilder只能在所属组件内声明，不允许全局声明。
* @LocalBuilder不能与内置装饰器或自定义装饰器一起使用。
* 在自定义组件中，@LocalBuilder不能用来装饰静态函数。
* 关于@LocalBuilder函数的传递方式，建议优先传递函数本身，或使用 () => { 函数调用 } 的形式，避免直接传递函数的执行结果。

## 参数传递规则

@LocalBuilder函数的参数传递有[按回调传递](arkts-localbuilder.md#按回调传递参数)，[按引用传递](arkts-localbuilder.md#按引用传递参数)和[按值传递](arkts-localbuilder.md#按值传递参数)，均需遵守以下规则：

* 参数的类型必须与参数声明的类型一致，且不允许为undefined、null。
* 在@LocalBuilder修饰的函数内部，不允许改变参数值。
* @LocalBuilder内的UI语法遵循[UI语法规则](arkts-create-custom-components.md#build函数实现规则)。
* 按回调传递和按引用传递时，支持@Builder函数内UI组件刷新。按引用传递只在传入一个参数且该参数直接传入对象字面量时生效，有多个参数时不支持@Builder函数内UI组件刷新。

### 按回调传递参数

从API version 20开始，开发者可以通过使用UIUtils.makeBinding()函数、Binding类和MutableBinding类实现@Builder函数中状态变量的刷新。详情请参考[状态管理API文档](../harmonyos-references/js-apis-statemanagement.md#makebinding20)。

```
1. import { UIUtils, Binding } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Parent {
6. @State variableValue: string = 'Hello World';

8. @LocalBuilder
9. citeLocalBuilder(params: Binding<string>) {
10. Row() {
11. Text(`UseStateVarByReference: ${params.value}`)
12. }
13. }

15. build() {
16. Column() {
17. this.citeLocalBuilder(UIUtils.makeBinding<string>(() => this.variableValue))
18. Button('Click me')
19. .onClick(() => {
20. this.variableValue = 'Hi World';
21. })
22. }
23. }
24. }
```

[BuilderMakeBinding.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/BuilderMakeBinding.ets#L15-L40)

### 按引用传递参数

按引用传递参数时，传递的参数可为状态变量，且状态变量的改变会引起@LocalBuilder函数内的UI刷新。

说明

若@LocalBuilder函数和$$参数一起使用，子组件调用父组件的@LocalBuilder函数，子组件传入的参数发生变化，不会引起@LocalBuilder函数内的UI刷新。见常见错误[@LocalBuilder函数和$$参数一起使用UI不刷新](arkts-localbuilder.md#localbuilder函数和参数一起使用ui不刷新)。

组件Parent内的@LocalBuilder函数在build函数内调用，按键值对写法进行传值，当点击Click me时，@LocalBuilder内的Text文本内容会随着状态变量内容的改变而改变。

```
1. class ReferenceType {
2. paramString: string = '';
3. }

5. @Entry
6. @Component
7. struct Parent {
8. @State variableValue: string = 'Hello World';

10. @LocalBuilder
11. citeLocalBuilder(params: ReferenceType) {
12. Row() {
13. Text(`UseStateVarByReference: ${params.paramString}`)
14. }
15. };

17. build() {
18. Column() {
19. this.citeLocalBuilder({ paramString: this.variableValue })
20. Button('Click me').onClick(() => {
21. this.variableValue = 'Hi World';
22. })
23. }
24. }
25. }
```

[ReferencePassing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/ReferencePassing.ets#L30-L56)

按引用传递参数时，如果在@LocalBuilder函数内调用自定义组件，ArkUI提供$$作为按引用传递参数的范式。

组件Parent内的@LocalBuilder函数内调用自定义组件，且按照引用传递参数将值传递到自定义组件，当Parent组件内状态变量值发生变化时，@LocalBuilder函数内的自定义组件HelloComponent的message值也会随之更新。

```
1. class ReferenceType {
2. paramString: string = '';
3. }

5. @Component
6. struct HelloComponent {
7. @Prop message: string;

9. build() {
10. Row() {
11. Text(`HelloComponent===${this.message}`)
12. }
13. }
14. }

16. @Entry
17. @Component
18. struct Parent {
19. @State variableValue: string = 'Hello World';

21. @LocalBuilder
22. citeLocalBuilder($$: ReferenceType) {
23. Row() {
24. Column() {
25. Text(`citeLocalBuilder===${$$.paramString}`)
26. HelloComponent({ message: $$.paramString })
27. }
28. }
29. }

31. build() {
32. Column() {
33. this.citeLocalBuilder({ paramString: this.variableValue })
34. Button('Click me').onClick(() => {
35. this.variableValue = 'Hi World';
36. })
37. }
38. }
39. }
```

[ParentRefSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/ParentRefSync.ets#L30-L70)

当子组件引用父组件的@LocalBuilder函数并传入状态变量时，状态变量的改变不会触发@LocalBuilder函数内的UI刷新。这是因为调用@LocalBuilder装饰的函数创建出来的组件绑定于父组件，而状态变量的刷新机制仅作用于当前组件及其子组件，对父组件无效。而使用@Builder修饰函数可触发UI刷新，原因在于@Builder改变了函数的this指向，使创建出来的组件绑定到子组件上，从而在子组件修改变量能够实现@Builder中的UI刷新。

下面示例中，组件Child将状态变量传递到Parent的@Builder和@LocalBuilder函数内。在@Builder函数内，this指向Child，参数变化能触发UI刷新。在@LocalBuilder函数内，this指向Parent，参数变化不会触发UI刷新。若@LocalBuilder函数内引用Parent的状态变量发生变化，UI能正常刷新。

```
1. class Data {
2. public size: number = 0;
3. }

5. @Entry
6. @Component
7. struct Parent {
8. label: string = 'parent';
9. @State data: Data = new Data();

11. @Builder
12. componentBuilder($$: Data) {
13. // 点击Button 触发UI刷新
14. Text('builder + $$')
15. Text(`${'this -> ' + this.label}`)
16. Text(`${'size : ' + $$.size}`)
17. }

19. @LocalBuilder
20. componentLocalBuilder($$: Data) {
21. // 点击Button 不会触发UI刷新
22. Text('LocalBuilder + $$ data')
23. Text(`${'this -> ' + this.label}`)
24. Text(`${'size : ' + $$.size}`)
25. }

27. @LocalBuilder
28. contentLocalBuilderNoArgument() {
29. // 点击Button 触发UI刷新
30. Text('LocalBuilder + local data')
31. Text(`${'this -> ' + this.label}`)
32. Text(`${'size : ' + this.data.size}`)
33. }

35. build() {
36. Column() {
37. Child({
38. contentBuilder: this.componentBuilder,
39. contentLocalBuilder: this.componentLocalBuilder,
40. contentLocalBuilderNoArgument: this.contentLocalBuilderNoArgument,
41. data: this.data
42. })
43. }
44. }
45. }

47. @Component
48. struct Child {
49. label: string = 'child';

51. @Builder
52. customBuilder() {
53. };

55. @BuilderParam contentBuilder: ((data: Data) => void) = this.customBuilder;
56. @BuilderParam contentLocalBuilder: ((data: Data) => void) = this.customBuilder;
57. @BuilderParam contentLocalBuilderNoArgument: (() => void) = this.customBuilder;
58. @Link data: Data;

60. build() {
61. Column() {
62. this.contentBuilder({ size: this.data.size })
63. this.contentLocalBuilder({ size: this.data.size })
64. this.contentLocalBuilderNoArgument()
65. Button('add child size')
66. .onClick(() => {
67. this.data.size += 1;
68. })
69. }
70. }
71. }
```

[BuilderThisDiff.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/BuilderThisDiff.ets#L30-L98)

### 按值传递参数

调用@LocalBuilder装饰的函数默认按值传递。当传递的参数为状态变量时，状态变量的改变不会引起@LocalBuilder函数内的UI刷新。所以当使用状态变量的时候，推荐使用[按回调传递](arkts-localbuilder.md#按回调传递参数)或[按引用传递](arkts-localbuilder.md#按引用传递参数)。

组件Parent将@State修饰的label值按照函数传参方式传递到@LocalBuilder函数内，此时@LocalBuilder函数获取到的值为普通变量值，所以改变@State修饰的label值时，@LocalBuilder函数内的值不会发生改变。

```
1. @Entry
2. @Component
3. struct Parent {
4. @State label: string = 'Hello';

6. @LocalBuilder
7. citeLocalBuilder(paramA1: string) {
8. Row() {
9. Text(`UseStateVarByValue: ${paramA1}`)
10. }
11. }

13. build() {
14. Column() {
15. this.citeLocalBuilder(this.label)
16. }
17. }
18. }
```

[ValuePassing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/ValuePassing.ets#L30-L49)

## 使用场景

### @LocalBuilder在@ComponentV2修饰的自定义组件中使用

在[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件中使用局部的@LocalBuilder，修改变量时会触发UI刷新。

```
1. @ObservedV2
2. class Info {
3. @Trace name: string = '';
4. @Trace age: number = 0;
5. }

7. @ComponentV2
8. struct ChildPage {
9. @Require @Param childInfo: Info;

11. build() {
12. Column() {
13. Text(`Custom component name: ${this.childInfo.name}`)
14. .fontSize(20)
15. .fontWeight(FontWeight.Bold)
16. Text(`Custom component age: ${this.childInfo.age}`)
17. .fontSize(20)
18. .fontWeight(FontWeight.Bold)
19. }
20. }
21. }

23. @Entry
24. @ComponentV2
25. struct ParentPage {
26. info1: Info = { name: 'Tom', age: 25 };
27. @Local info2: Info = { name: 'Tom', age: 25 };

29. @LocalBuilder
30. privateBuilder() {
31. Column() {
32. Text(`Local @LocalBuilder name: ${this.info1.name}`)
33. .fontSize(20)
34. .fontWeight(FontWeight.Bold)
35. Text(`Local @LocalBuilder age: ${this.info1.age}`)
36. .fontSize(20)
37. .fontWeight(FontWeight.Bold)
38. }
39. }

41. @LocalBuilder
42. privateBuilderSecond() {
43. Column() {
44. Text(`Local @LocalBuilder name: ${this.info2.name}`)
45. .fontSize(20)
46. .fontWeight(FontWeight.Bold)
47. Text(`Local @LocalBuilder age: ${this.info2.age}`)
48. .fontSize(20)
49. .fontWeight(FontWeight.Bold)
50. }
51. }

53. build() {
54. Column() {
55. Text(`info1: ${this.info1.name}  ${this.info1.age}`) // Text1
56. .fontSize(30)
57. .fontWeight(FontWeight.Bold)
58. this.privateBuilder() // 调用局部@Builder
59. Line()
60. .width('100%')
61. .height(10)
62. .backgroundColor('#000000')
63. .margin(10)
64. Text(`info2: ${this.info2.name}  ${this.info2.age}`) // Text2
65. .fontSize(30)
66. .fontWeight(FontWeight.Bold)
67. this.privateBuilderSecond() // 调用局部@Builder
68. Line()
69. .width('100%')
70. .height(10)
71. .backgroundColor('#000000')
72. .margin(10)
73. Text(`info1: ${this.info1.name}  ${this.info1.age}`) // Text1
74. .fontSize(30)
75. .fontWeight(FontWeight.Bold)
76. ChildPage({ childInfo: this.info1 }) // 调用自定义组件
77. Line()
78. .width('100%')
79. .height(10)
80. .backgroundColor('#000000')
81. .margin(10)
82. Text(`info2: ${this.info2.name}  ${this.info2.age}`) // Text2
83. .fontSize(30)
84. .fontWeight(FontWeight.Bold)
85. ChildPage({ childInfo: this.info2 }) // 调用自定义组件
86. Line()
87. .width('100%')
88. .height(10)
89. .backgroundColor('#000000')
90. .margin(10)
91. Button('change info1&info2')
92. .onClick(() => {
93. this.info1 = { name: 'Cat', age: 18 }; // Text1不会刷新，原因是info1没被装饰器装饰，无法监听到值的改变。
94. this.info2 = { name: 'Cat', age: 18 }; // Text2会刷新，原因是info2有装饰器装饰，可以监听到值的改变。
95. })
96. }
97. }
98. }
```

[V2LocalBuilderUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/V2LocalBuilderUpdate.ets#L30-L125)

## 常见问题

### @LocalBuilder函数和$$参数一起使用UI不刷新

若@LocalBuilder函数和$$参数一起使用，子组件调用父组件的@LocalBuilder函数，子组件传入的参数发生变化，不会引起@LocalBuilder函数内的UI刷新。

【反例】

```
1. class LayoutSize {
2. public size: number = 0;
3. }

5. @Entry
6. @Component
7. struct Parent {
8. label: string = 'parent';
9. @State layoutSize: LayoutSize = { size: 0 };

11. @LocalBuilder
12. componentBuilder($$: LayoutSize) {
13. Text(`this: ${this.label}`)
14. Text(`size: ${$$.size}`)
15. }

17. build() {
18. Column() {
19. Child({
20. customBuilder: this.componentBuilder,
21. layoutSize: this.layoutSize
22. })
23. }
24. }
25. }

27. @Component
28. struct Child {
29. label: string = 'child';
30. @BuilderParam customBuilder: ((layoutSize: LayoutSize) => void);
31. @Link layoutSize: LayoutSize;

33. build() {
34. Column() {
35. this.customBuilder({ size: this.layoutSize.size }) // 子组件调用父组件的@LocalBuilder函数
36. Button('add child size')
37. .onClick(() => {
38. this.layoutSize.size += 1; // 子组件传入的参数发生变化，不会引起@LocalBuilder函数内的UI刷新
39. })
40. }
41. }
42. }
```

[ProblemUINotRefreshOpposite.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/ProblemUINotRefreshOpposite.ets#L15-L58)

【正例】

在声明@LocalBuilder的组件下创建状态变量并在@LocalBuilder函数内访问，可以在状态变量变化时更新@LocalBuilder内的UI组件。

```
1. class LayoutSize {
2. public size: number = 0;
3. }

5. @Entry
6. @Component
7. struct Parent {
8. label: string = 'parent';
9. @State layoutSize: LayoutSize = { size: 0 };

11. @LocalBuilder
12. componentBuilder() {
13. Text(`this: ${this.label}`)
14. Text(`size: ${this.layoutSize.size}`)
15. }

17. build() {
18. Column() {
19. Child({
20. customBuilder: this.componentBuilder,
21. layoutSize: this.layoutSize
22. })
23. }
24. }
25. }

27. @Component
28. struct Child {
29. label: string = 'child';
30. @BuilderParam customBuilder: () => void;
31. @Link layoutSize: LayoutSize;

33. build() {
34. Column() {
35. this.customBuilder()
36. Button('add child size')
37. .onClick(() => {
38. this.layoutSize.size += 1; // 子组件传入的参数发生变化，由@Link传入父组件@State，刷新父组件声明的@LocalBuilder函数的UI。
39. })
40. }
41. }
42. }
```

[ProblemUINotRefreshPositive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/localBuilder/ProblemUINotRefreshPositive.ets#L15-L58)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/esHBfleFQ2KrsejOf1gAKg/zh-cn_image_0000002583477577.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233855Z&HW-CC-Expire=86400&HW-CC-Sign=F9D3C549CF1D5125F7A42A91990607A9CD80B82FAF1283614266C1BB51545FFC)

### @LocalBuilder函数在参数处直接调用出现布局错乱

@LocalBuilder装饰的函数作为参数时，直接传递函数的执行结果，会导致布局和预期效果有偏差。

【反例】

```
1. @Entry
2. @Component
3. struct Page {
4. @State message: string[] = ['1', '2', '3'];

6. build() {
7. List() {
8. // 错误写法，直接传递itemFoot的执行结果。
9. ListItemGroup({ space: 10, footer: this.itemFoot() }) {
10. ForEach(this.message, (item: string, index: number) => {
11. ListItem() {
12. Stack() {
13. Text(item)
14. .fontSize(30)
15. }
16. }
17. })
18. }
19. }
20. }

22. @LocalBuilder
23. itemFoot() {
24. Column() {
25. Text('itemFoot')
26. .fontSize(30)
27. }
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/TcIfQTp4QCyYddFz9GS3hw/zh-cn_image_0000002552797928.png?HW-CC-KV=V1&HW-CC-Date=20260427T233855Z&HW-CC-Expire=86400&HW-CC-Sign=2D394786CD25FE1D3B60ABCC1559A866F2A267DC5B1C882AA03DB1475BB51ED7)

【正例】

@LocalBuilder装饰的函数作为参数时，使用 () => { 函数调用 } 的形式，布局能够符合预期效果。

```
1. @Entry
2. @Component
3. struct Page {
4. @State message: string[] = ['1', '2', '3'];

6. build() {
7. List() {
8. // 正确写法，使用() => { 函数调用 }的形式。
9. ListItemGroup({ space: 10, footer: () => { this.itemFoot() } }) {
10. ForEach(this.message, (item: string, index: number) => {
11. ListItem() {
12. Stack() {
13. Text(item)
14. .fontSize(30)
15. }
16. }
17. })
18. }
19. }
20. }

22. @LocalBuilder
23. itemFoot() {
24. Column() {
25. Text('itemFoot')
26. .fontSize(30)
27. }
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/gVDqcgGpQ_iOe5bmbds1GQ/zh-cn_image_0000002583437623.png?HW-CC-KV=V1&HW-CC-Date=20260427T233855Z&HW-CC-Expire=86400&HW-CC-Sign=99B028A44FE9623B813301AD19E35C88A189E5EDEE86F0C879FC2DBAC66AE112)
