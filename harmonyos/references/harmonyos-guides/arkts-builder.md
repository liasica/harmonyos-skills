---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder
title: @Builder装饰器：自定义构建函数
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > @Builder装饰器：自定义构建函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:06+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:61fef45267b305ca285ed5e1b2f91d63afae499a0ef03b55832b43aada1e460c
---

ArkUI提供轻量的UI元素复用机制@Builder，其内部UI结构固定，仅与使用方进行数据传递。开发者可将重复使用的UI元素抽象成函数，在build函数中调用。

@Builder装饰的函数也称为“自定义构建函数”。

在阅读本文档前，建议提前阅读：[基本语法概述](arkts-basic-syntax-overview.md)、[声明式UI描述](arkts-declarative-ui-description.md)、[自定义组件-创建自定义组件](arkts-create-custom-components.md)。

@Builder装饰器和[@Component装饰器](arkts-create-custom-components.md#component)在功能和使用方式上的主要差异：

1. @Builder装饰器用于封装可复用的UI结构，通过提取重复的布局代码提高开发效率。该装饰器严格禁止在其内部定义[状态变量](arkts-state-management-glossary.md#状态变量state-variables)或使用[生命周期函数](../harmonyos-references/ts-custom-component-lifecycle.md)，必须通过参数传递或者访问所属组件的状态变量完成数据交互。
2. 在ArkUI框架中，@Component装饰器作为封装复杂UI组件的核心机制，允许开发者通过组合多个基础组件来构建可复用的复合界面。该装饰器不仅支持内部状态变量的定义，还能完整管理组件的生命周期。

说明

从API version 7开始支持。

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

@Builder装饰器有两种使用方式，分别是定义在自定义组件内部的[私有自定义构建函数](arkts-builder.md#私有自定义构建函数)和定义在全局的[全局自定义构建函数](arkts-builder.md#全局自定义构建函数)。

### 私有自定义构建函数

示例：

```
1. @Entry
2. @Component
3. struct BuilderDemo {
4. @Builder
5. showTextBuilder() {
6. // @Builder装饰此函数，使其能以链式调用的方式配置并构建Text组件
7. Text('Hello World')
8. .fontSize(30)
9. .fontWeight(FontWeight.Bold)
10. }

12. @Builder
13. showTextValueBuilder(param: string) {
14. Text(param)
15. .fontSize(30)
16. .fontWeight(FontWeight.Bold)
17. }

19. build() {
20. Column() {
21. // 无参数
22. this.showTextBuilder()
23. // 有参数
24. this.showTextValueBuilder('Hello @Builder')
25. }
26. }
27. }
```

[PrivateCustomConstructor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/PrivateCustomConstructor.ets#L15-L43)

使用方法：

* 允许在自定义组件内定义一个或多个@Builder函数，该函数被认为是该组件的私有、特殊类型的成员函数。
* 私有自定义构建函数允许在自定义组件内、build函数和其他自定义构建函数中调用。
* 在自定义组件中，this指代当前所属组件，组件的状态变量可在自定义构建函数内访问。建议通过this访问组件的状态变量，而不是通过参数传递。

### 全局自定义构建函数

示例：

```
1. // 全局自定义构建函数showTextBuilder
2. @Builder
3. function showTextBuilder() {
4. Text('Hello World')
5. .fontSize(30)
6. .fontWeight(FontWeight.Bold)
7. }

9. @Entry
10. @Component
11. struct BuilderSample {
12. build() {
13. Column() {
14. showTextBuilder()
15. }
16. }
17. }
```

[GlobalCustomConstructor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/GlobalCustomConstructor.ets#L15-L31)

* 如果不涉及组件状态变量变化，建议使用全局的自定义构建函数。
* 全局自定义构建函数允许在build函数和其他自定义构建函数中调用。

## 参数传递规则

自定义构建函数的参数传递有[按回调传递](arkts-builder.md#按回调传递参数)，[按引用传递](arkts-builder.md#按引用传递参数)和[按值传递](arkts-builder.md#按值传递参数)，均需遵守以下规则：

* @Builder装饰的函数参数类型不允许为undefined、null和返回undefined、null的表达式。
* 在@Builder装饰的函数内部，不允许改变参数值。
* @Builder内UI语法遵循[UI语法规则](arkts-create-custom-components.md#build函数实现规则)。
* 按回调传递和按引用传递时，支持@Builder函数内UI组件刷新。按引用传递只在传入一个参数且该参数直接传入对象字面量时生效，有多个参数时不支持@Builder函数内UI组件刷新。
* 使用引用传递时，在@Builder函数中不能修改参数的属性，但使用UIUtils.makeBinding并传入写回调时，我们可以在@Builder函数内修改属性，并同步到调用@Builder的组件中。

### 按回调传递参数

从API version 20开始，开发者可以通过使用UIUtils.makeBinding()函数、Binding类和MutableBinding类实现@Builder函数中状态变量的刷新。详细用例见[@Builder支持状态变量刷新](arkts-builder.md#builder支持状态变量刷新)。

使用UIUtils.makeBinding()包装读取状态变量的回调函数作为参数传入@Builder函数，可以支持@Builder函数中UI组件刷新；UIUtils.makeBinding()中额外传入写状态变量的回调函数可以将@Builder函数内对参数的修改，传递到调用@Builder函数的组件中。

```
1. import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function customButton(num1: Binding<number>, num2: MutableBinding<number>) {
5. Row() {
6. Column() {
7. Text(`number1: ${num1.value}, number2: ${num2.value}`)
8. Button(`only change number2`)
9. .onClick(() => {
10. // 赋值MutableBinding类型传递该修改到父组件中。
11. num2.value += 1;
12. })
13. }
14. }
15. }

17. @Entry
18. @ComponentV2
19. struct ParameterMakeBinding {
20. @Local number1: number = 5;
21. @Local number2: number = 12;

23. build() {
24. Column() {
25. customButton(
26. // 使用makeBinding传入参数，需要传入读回调，返回Binding类型，支持@Builder内组件UI刷新。
27. UIUtils.makeBinding<number>(() => this.number1),
28. // makeBinding额外传入写回调时返回MutableBinding类型，支持@Builder内组件UI刷新并且同步属性修改。
29. UIUtils.makeBinding<number>(
30. () => this.number2,
31. (val: number) => {
32. this.number2 = val;
33. })
34. )
35. }
36. }
37. }
```

[ParameterMakeBinding.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/ParameterMakeBinding.ets#L15-L53)

### 按引用传递参数

按引用传递参数时，传递的参数可为状态变量，且状态变量的改变会引起@Builder函数内的UI刷新。

```
1. class Tmp {
2. public paramA1: string = '';
3. }

5. @Builder
6. function overBuilderByReference(params: Tmp) {
7. Row() {
8. Text(`UseStateVarByReference: ${params.paramA1} `)
9. }
10. }

12. @Entry
13. @Component
14. struct ParameterReference {
15. @State label: string = 'Hello';

17. build() {
18. Column() {
19. // 在父组件中调用overBuilderByReference组件时，
20. // 把this.label通过引用传递的方式传给overBuilderByReference组件。
21. overBuilderByReference({ paramA1: this.label })
22. Button('Click me').onClick(() => {
23. // 单击Click me后，UI文本从Hello更改为ArkUI。
24. this.label = 'ArkUI';
25. })
26. }
27. }
28. }
```

[ParameterReference.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/ParameterReference.ets#L15-L44)

### 按值传递参数

调用@Builder装饰的函数默认按值传递。当传递的参数为状态变量时，状态变量的改变不会引起@Builder函数内的UI刷新。所以当使用状态变量的时候，推荐使用[按回调传递](arkts-builder.md#按回调传递参数)或[按引用传递](arkts-builder.md#按引用传递参数)。

```
1. @Builder
2. function overBuilderByValue(paramA1: string) {
3. Row() {
4. Text(`UseStateVarByValue: ${paramA1} `)
5. }
6. }

8. @Entry
9. @Component
10. struct ParameterValue {
11. @State label: string = 'Hello';

13. build() {
14. Column() {
15. // 按值传递参数，状态变量的改变不会引起overBuilderByValue内的UI刷新
16. overBuilderByValue(this.label)
17. }
18. }
19. }
```

[ParameterValue.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/ParameterValue.ets#L15-L34)

## 限制条件

1. @Builder装饰的函数内部在没有使用[MutableBinding](../harmonyos-references/js-apis-statemanagement.md#mutablebindingt20)时不允许修改参数值，修改不会触发UI刷新。若[按引用传递参数](arkts-builder.md#按引用传递参数)且仅传入一个参数时，修改参数内部的属性会抛出运行时错误。使用MutableBinding可以帮助开发者在@Builder装饰的函数内部修改参数值，请参考[在@Builder装饰的函数内部修改入参内容](arkts-builder.md#在builder装饰的函数内部修改入参内容)。
2. @Builder按引用传递传入一个参数时，可以触发动态渲染UI，请参考[按引用传递参数](arkts-builder.md#按引用传递参数)。
3. 如果@Builder传入的参数是两个或两个以上，且未使用[按回调传递参数](arkts-builder.md#按回调传递参数)，不会触发动态渲染UI，请参考[@Builder存在两个或两个以上参数](arkts-builder.md#builder存在两个或两个以上参数)。
4. @Builder传入的参数中同时包含按值传递和按引用传递，不会触发动态渲染UI，请参考[@Builder存在两个或两个以上参数](arkts-builder.md#builder存在两个或两个以上参数)。
5. 不允许在@Builder函数里修改参数的属性，否则会抛出运行时错误，从API version 23开始，将返回错误码[140109](../harmonyos-references/errorcode-statemanagement.md#section140109-builder非法触发参数属性赋值)，示例请参考[在@Builder装饰的函数内部修改入参内容](arkts-builder.md#在builder装饰的函数内部修改入参内容)。

## 使用场景

### 自定义组件内使用自定义构建函数

创建私有的@Builder函数，在Column中使用this.builder()调用。通过[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)生命周期函数和按钮的点击事件更新builderValue，实现UI的动态渲染。

```
1. @Entry
2. @Component
3. struct PrivateBuilder {
4. @State builderValue: string = 'Hello';

6. @Builder
7. builder() {
8. Column() {
9. Text(this.builderValue)
10. .width(230)
11. .height(40)
12. .backgroundColor('#ffeae5e5')
13. .borderRadius(20)
14. .margin(12)
15. .textAlign(TextAlign.Center)
16. }
17. }

19. aboutToAppear(): void {
20. setTimeout(() => {
21. this.builderValue = 'Hello World';
22. }, 2000);
23. }

25. build() {
26. Row() {
27. Column() {
28. Text(this.builderValue)
29. .width(230)
30. .height(40)
31. .backgroundColor('#ffeae5e5')
32. .borderRadius(20)
33. .textAlign(TextAlign.Center)
34. this.builder()
35. // 点击Button更新builderValue，用于更新文本显示
36. Button('Click to change the builderValue')
37. .onClick(() => {
38. this.builderValue = 'builderValue was clicked';
39. })
40. }
41. .height('100%')
42. .width('100%')
43. }
44. }
45. }
```

[InCustomComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/InCustomComponent.ets#L15-L60)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/C5YXH3UgTXSal12zdMT9Xg/zh-cn_image_0000002558604406.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=F75DC873850D3226728017BB5C386192B498F880A66898C35ADF89F743C684B2)

### 全局自定义构建函数

创建全局的@Builder函数，并在Column中通过overBuilder()方式调用。传递参数时，可以使用对象字面量形式，无论是简单类型还是复杂类型，值的任何变化都会触发UI界面的刷新。

```
1. class ChildTmp {
2. public val: number = 1;
3. }

5. class ParamTmp {
6. public strValue: string = 'Hello';
7. public numValue: number = 0;
8. public tmpValue: ChildTmp = new ChildTmp();
9. public arrayTmpValue: Array<ChildTmp> = [];
10. }

12. @Builder
13. function overBuilder(param: ParamTmp) {
14. Column() {
15. Text(`strValue: ${param.strValue}`)
16. .width(230)
17. .height(40)
18. .margin(12)
19. .backgroundColor('#0d000000')
20. .fontColor('#e6000000')
21. .borderRadius(20)
22. .textAlign(TextAlign.Center)
23. Text(`numValue: ${param.numValue}`)
24. .width(230)
25. .height(40)
26. .margin(12)
27. .backgroundColor('#0d000000')
28. .fontColor('#e6000000')
29. .borderRadius(20)
30. .textAlign(TextAlign.Center)
31. Text(`tmpValue: ${param.tmpValue.val}`)
32. .width(230)
33. .height(40)
34. .margin(12)
35. .backgroundColor('#0d000000')
36. .fontColor('#e6000000')
37. .borderRadius(20)
38. .textAlign(TextAlign.Center)
39. ForEach(param.arrayTmpValue, (item: ChildTmp) => {
40. ListItem() {
41. Text(`arrayTmpValue: ${item.val}`)
42. .width(230)
43. .height(40)
44. .margin(12)
45. .backgroundColor('#0d000000')
46. .fontColor('#e6000000')
47. .borderRadius(20)
48. .textAlign(TextAlign.Center)
49. }
50. }, (item: ChildTmp) => JSON.stringify(item))
51. }
52. }

54. @Entry
55. @Component
56. struct ParentDemo {
57. @State objParam: ParamTmp = new ParamTmp();

59. build() {
60. Column() {
61. Text('UI Rendered via @Builder')
62. .fontSize(20)
63. .margin(12)
64. // 调用全局@Builder函数overBuilder
65. overBuilder({
66. strValue: this.objParam.strValue,
67. numValue: this.objParam.numValue,
68. tmpValue: this.objParam.tmpValue,
69. arrayTmpValue: this.objParam.arrayTmpValue
70. })
71. // 点击Button更新objParam，触发overBuilder内组件的刷新
72. Button('Update Values').onClick(() => {
73. this.objParam.strValue = 'Hello World';
74. this.objParam.numValue = 1;
75. this.objParam.tmpValue.val = 8;
76. const childValue: ChildTmp = {
77. val: 2
78. }
79. this.objParam.arrayTmpValue.push(childValue);
80. })
81. }
82. .height('100%')
83. .width('100%')
84. }
85. }
```

[GlobalCustomBuilder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/GlobalCustomBuilder.ets#L15-L99)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qxAHiABeSa2xaOpWbZZQlw/zh-cn_image_0000002589323931.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=C78DD02052EC1D0B2F6831DD04DDA80098EC1C871374B337E1F53A6BA230456A)

### 修改装饰器修饰的变量触发UI刷新

在该场景中，@Builder被用来展示Text组件，不会参与动态UI刷新。Text组件中值的变化是通过使用装饰器的特性，监听到值的改变触发的UI刷新，而不是通过@Builder的能力触发的。

```
1. class ChildrenTmp {
2. public strValue: string = 'Hello';
3. }

5. @Entry
6. @Component
7. struct ParentSample {
8. @State objParam: ChildrenTmp = new ChildrenTmp();
9. @State label: string = 'World';

11. @Builder
12. privateBuilder() {
13. Column() {
14. Text(`wrapBuilder strValue: ${this.objParam.strValue}`)
15. .width(350)
16. .height(40)
17. .margin(12)
18. .backgroundColor('#0d000000')
19. .fontColor('#e6000000')
20. .borderRadius(20)
21. .textAlign(TextAlign.Center)
22. Text(`wrapBuilder num: ${this.label}`)
23. .width(350)
24. .height(40)
25. .margin(12)
26. .backgroundColor('#0d000000')
27. .fontColor('#e6000000')
28. .borderRadius(20)
29. .textAlign(TextAlign.Center)
30. }
31. }

33. build() {
34. Column() {
35. Text('UI Rendered via @Builder')
36. .fontSize(20)
37. this.privateBuilder()
38. // 点击Button更新label，触发Text组件的刷新
39. Button('Update Values').onClick(() => {
40. this.objParam.strValue = 'strValue Hello World';
41. this.label = 'label Hello World';
42. })
43. }
44. .height('100%')
45. .width('100%')
46. }
47. }
```

[ChangingByDecorator.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/ChangingByDecorator.ets#L15-L62)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/6NFUM0-_T8Gl7DRT4cZabA/zh-cn_image_0000002589243871.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=B32422AF5AFE8A68E2EB21D454F44F3C59C9964CF8E0D30A11F4F395B329FCC7)

### 将@Builder装饰的函数当作CustomBuilder类型使用

当参数类型为[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)时，可以传入定义的@Builder函数。因为CustomBuilder实际上是Function(() => any)或void类型，而@Builder也是Function类型。所以通过传入@Builder可以实现特定效果。

全局@Builder函数当作CustomBuilder类型传递时需要绑定this上下文，开发者可以直接调用全局@Builder函数，编译工具链会自动生成绑定this上下文的代码。

```
1. @Builder
2. function overBuilderDemo() {
3. Row() {
4. Text('Global Builder')
5. .fontSize(30)
6. .fontWeight(FontWeight.Bold)
7. }
8. }

10. @Entry
11. @Component
12. struct customBuilderDemo {
13. @State arr: number[] = [0, 1, 2, 3, 4];

15. @Builder
16. privateBuilder() {
17. Row() {
18. Text('Private Builder')
19. .fontSize(30)
20. .fontWeight(FontWeight.Bold)
21. }
22. }

24. build() {
25. Column() {
26. List({ space: 10 }) {
27. ForEach(this.arr, (item: number) => {
28. ListItem() {
29. Text(`${item}`)
30. .width('100%')
31. .height(100)
32. .fontSize(16)
33. .textAlign(TextAlign.Center)
34. .borderRadius(10)
35. .backgroundColor(0xFFFFFF)
36. }
37. .swipeAction({
38. start: {
39. builder: overBuilderDemo() // 编译工具链会自动绑定this上下文
40. },
41. end: {
42. builder: () => {
43. // 在箭头函数中调用局部@Builder会自动绑定this上下文，无需编译工具链处理
44. this.privateBuilder()
45. }
46. }
47. })
48. }, (item: number) => JSON.stringify(item))
49. }
50. }
51. }
52. }
```

[AsCustomBuilder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/AsCustomBuilder.ets#L15-L68)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/vU4gNtejTZCk2P1nDshEgw/zh-cn_image_0000002558764064.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=0F631445BA04494559FAAD7439FFBFF570F975543D8CFAA57FC51860F931B502)

### 多层@Builder函数嵌套

在@Builder函数内调用自定义组件或其他@Builder函数，实现多个@Builder嵌套使用。若要实现最内层的@Builder动态UI刷新功能，每层调用@Builder的地方必须使用按引用传递的方式。这里$$不是必须的参数形式，可以换成其他名称。

```
1. class ThisTmp {
2. public paramA1: string = '';
3. }

5. @Builder
6. function parentBuilder($$: ThisTmp) {
7. Row() {
8. Column() {
9. Text(`parentBuilder===${$$.paramA1}`)
10. .width(300)
11. .height(40)
12. .margin(10)
13. .backgroundColor('#0d000000')
14. .fontColor('#e6000000')
15. .borderRadius(20)
16. .textAlign(TextAlign.Center)
17. // 调用自定义组件HelloComponent
18. HelloComponent({ message: $$.paramA1 })
19. // 调用全局@Builder函数childBuilder
20. childBuilder({ paramA1: $$.paramA1 })
21. }
22. }
23. }

25. @Component
26. struct HelloComponent {
27. @Prop message: string = '';

29. build() {
30. Row() {
31. Text(`HelloComponent===${this.message}`)
32. .width(300)
33. .height(40)
34. .margin(10)
35. .backgroundColor('#0d000000')
36. .fontColor('#e6000000')
37. .borderRadius(20)
38. .textAlign(TextAlign.Center)
39. }
40. }
41. }

43. @Builder
44. function childBuilder($$: ThisTmp) {
45. Row() {
46. Column() {
47. Text(`childBuilder===${$$.paramA1}`)
48. .width(300)
49. .height(40)
50. .margin(10)
51. .backgroundColor('#0d000000')
52. .fontColor('#e6000000')
53. .borderRadius(20)
54. .textAlign(TextAlign.Center)
55. // 调用自定义组件HelloChildComponent
56. HelloChildComponent({ message: $$.paramA1 })
57. // 调用全局@Builder函数grandsonBuilder
58. grandsonBuilder({ paramA1: $$.paramA1 })
59. }
60. }
61. }

63. @Component
64. struct HelloChildComponent {
65. @Prop message: string = '';

67. build() {
68. Row() {
69. Text(`HelloChildComponent===${this.message}`)
70. .width(300)
71. .height(40)
72. .margin(10)
73. .backgroundColor('#0d000000')
74. .fontColor('#e6000000')
75. .borderRadius(20)
76. .textAlign(TextAlign.Center)
77. }
78. }
79. }

81. @Builder
82. function grandsonBuilder($$: ThisTmp) {
83. Row() {
84. Column() {
85. Text(`grandsonBuilder===${$$.paramA1}`)
86. .width(300)
87. .height(40)
88. .margin(10)
89. .backgroundColor('#0d000000')
90. .fontColor('#e6000000')
91. .borderRadius(20)
92. .textAlign(TextAlign.Center)
93. // 调用自定义组件HelloGrandsonComponent
94. HelloGrandsonComponent({ message: $$.paramA1 })
95. }
96. }
97. }

99. @Component
100. struct HelloGrandsonComponent {
101. @Prop message: string;

103. build() {
104. Row() {
105. Text(`HelloGrandsonComponent===${this.message}`)
106. .width(300)
107. .height(40)
108. .margin(10)
109. .backgroundColor('#0d000000')
110. .fontColor('#e6000000')
111. .borderRadius(20)
112. .textAlign(TextAlign.Center)
113. }
114. }
115. }

117. @Entry
118. @Component
119. struct ParentExample {
120. @State label: string = 'Hello';

122. build() {
123. Column() {
124. // 调用全局@Builder函数parentBuilder
125. parentBuilder({ paramA1: this.label })
126. Button('Click me').onClick(() => {
127. this.label = 'ArkUI';
128. })
129. }
130. .height('100%')
131. .width('100%')
132. }
133. }
```

[NestedBuilderFunctions.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/NestedBuilderFunctions.ets#L15-L143)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yr__zmDNRdK0VOzsltvnyg/zh-cn_image_0000002558604408.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=6EE26AB8747819B65FB07B639D4854C20285B63183EBD91D42623AED1EF72C2C)

### @Builder函数联合V2装饰器

由[@ObservedV2](arkts-new-observedv2-and-trace.md)和[@Trace](arkts-new-observedv2-and-trace.md)装饰的类对象实例具备深度观测属性变化的能力。在@ComponentV2装饰的自定义组件中，当调用全局Builder或局部Builder且使用值传递的方式传递参数时，修改@Trace装饰的对象属性可以触发UI刷新。

```
1. @ObservedV2
2. class Info {
3. @Trace public name: string;
4. @Trace public age: number;

6. constructor(name: string, age: number) {
7. this.name = name;
8. this.age = age;
9. }
10. }

12. @Builder
13. function overBuilderTest(param: Info) {
14. Column() {
15. Text(`Global@Builder name: ${param.name}`)
16. Text(`Global@Builder age: ${param.age}`)
17. }
18. .width(230)
19. .height(40)
20. .margin(10)
21. .padding({ left: 20 })
22. .backgroundColor('#0d000000')
23. .borderRadius(20)
24. }

26. @ComponentV2
27. struct ChildPage {
28. @Require @Param childInfo: Info;

30. build() {
31. Column() {
32. // 此处必须为值传递方式，如果使用引用传递的方式会被ArkTS语法拦截
33. overBuilderTest(this.childInfo)
34. }
35. }
36. }

38. @Entry
39. @ComponentV2
40. struct ParentPage {
41. info1: Info = new Info('Tom', 25);
42. info2: Info = new Info('Tom', 25);

44. @Builder
45. privateBuilder() {
46. Column() {
47. Text(`Private@Builder name: ${this.info1.name}`)
48. Text(`Private@Builder age: ${this.info1.age}`)
49. }
50. .width(230)
51. .height(40)
52. .margin(10)
53. .backgroundColor('#0d000000')
54. .borderRadius(20)
55. }

57. build() {
58. Column() {
59. Flex() {
60. Column() {
61. Text(`info1: ${this.info1.name}  ${this.info1.age}`) // Text1
62. Text(`info2: ${this.info2.name}  ${this.info2.age}`) // Text2
63. }
64. }
65. .width(230)
66. .height(40)
67. .margin(10)
68. .padding({ left: 60 })
69. .backgroundColor('#0d000000')
70. .borderRadius(20)

72. // 调用局部@Builder
73. this.privateBuilder()
74. // 调用全局@Builder, 此处必须为值传递方式，如果使用引用传递的方式会被ArkTS语法拦截
75. overBuilderTest(this.info2)
76. ChildPage({ childInfo: this.info1 }) // 调用自定义组件
77. ChildPage({ childInfo: this.info2 }) // 调用自定义组件
78. Button('change info1&info2')
79. .onClick(() => {
80. this.info1.name = 'Cat'; // 修改Text1显示的info1的name值
81. this.info1.age = 18; // 修改Text1显示的info1的age值
82. this.info2.name = 'Cat'; // 修改Text2显示的info2的name值
83. this.info2.age = 18; // 修改Text2显示的info2的age值
84. })
85. }
86. .height('100%')
87. .width('100%')
88. }
89. }
```

[BuilderCombined.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/BuilderCombined.ets#L15-L105)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/-a0LYWWHTq-q5J9hzJefuw/zh-cn_image_0000002589323933.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=83D24AB7417023511F13FAD6F26F0C1E604E765F787270D0E1053FBCB6F52034)

当通过引用传递方式向@Builder传递参数时，若参数为[@Local](arkts-new-local.md)装饰的对象，对该对象进行整体赋值会触发@Builder中UI刷新。

```
1. class LocalInfo {
2. public name: string = 'Tom';
3. public age: number = 25;
4. }

6. @Builder
7. function overBuilderLocal(param: LocalInfo) {
8. Column() {
9. Text(`Global@Builder name: ${param.name}`)
10. Text(`Global@Builder age: ${param.age}`)
11. }
12. .width(230)
13. .height(40)
14. .margin(10)
15. .padding({ left: 20 })
16. .backgroundColor('#0d000000')
17. .borderRadius(20)
18. }

20. @ComponentV2
21. struct ChildLocalPage {
22. @Require @Param childLocalInfo: LocalInfo;

24. build() {
25. Column() {
26. // 此处为引用传递方式
27. overBuilderLocal({ name: this.childLocalInfo.name, age: this.childLocalInfo.age })
28. }
29. }
30. }

32. @Entry
33. @ComponentV2
34. struct ParentLocalPage {
35. LocalInfo1: LocalInfo = { name: 'Tom', age: 25 };
36. @Local LocalInfo2: LocalInfo = { name: 'Tom', age: 25 };

38. @Builder
39. privateBuilder() {
40. Column() {
41. Text(`Private@Builder name: ${this.LocalInfo1.name}`)
42. Text(`Private@Builder age: ${this.LocalInfo1.age}`)
43. }
44. .width(230)
45. .height(40)
46. .margin(10)
47. .backgroundColor('#0d000000')
48. .borderRadius(20)
49. }

51. build() {
52. Column() {
53. Flex() {
54. Column() {
55. Text(`LocalInfo1: ${this.LocalInfo1.name}  ${this.LocalInfo1.age}`) // Text1
56. Text(`LocalInfo2: ${this.LocalInfo2.name}  ${this.LocalInfo2.age}`) // Text2
57. }
58. }
59. .width(230)
60. .height(40)
61. .margin(10)
62. .padding({ left: 60 })
63. .backgroundColor('#0d000000')
64. .borderRadius(20)

66. // 调用局部@Builder
67. this.privateBuilder()
68. // 调用全局@Builder, 此处为引用传递方式
69. overBuilderLocal({ name: this.LocalInfo2.name, age: this.LocalInfo2.age })
70. ChildLocalPage({ childLocalInfo: this.LocalInfo1 }) // 调用自定义组件
71. ChildLocalPage({ childLocalInfo: this.LocalInfo2 }) // 调用自定义组件
72. Button('change LocalInfo1&LocalInfo2')
73. .onClick(() => {
74. this.LocalInfo1 = { name: 'Cat', age: 18 }; // Text1不会刷新，原因是没有装饰器修饰监听不到值的改变
75. this.LocalInfo2 = { name: 'Cat', age: 18 }; // Text2会刷新，原因是有装饰器修饰，可以监听到值的改变
76. })
77. }
78. .height('100%')
79. .width('100%')
80. }
81. }
```

[BuilderCombinedLocal.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/BuilderCombinedLocal.ets#L15-L97)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Gn5gAfw-Q72fXZg5RkEcUA/zh-cn_image_0000002589243873.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=93A0B797486AF1CA54F0509F1858D58BBC80BD27D28E160F26A9A2481988B669)

### 跨组件复用的全局@Builder

在跨组件的场景中调用全局@Builder，通过按引用传递的方式传递参数，可以实现UI的动态刷新功能。

```
1. class ReusableTmp {
2. public componentName: string = 'Child';
3. }

5. @Builder
6. function itemBuilder(params: ReusableTmp) {
7. Column() {
8. Text(`Builder ===${params.componentName}`)
9. .width(300)
10. .height(40)
11. .margin(10)
12. .backgroundColor('#0d000000')
13. .fontColor('#e6000000')
14. .borderRadius(20)
15. .textAlign(TextAlign.Center)
16. }
17. }

19. @Entry
20. @Component
21. struct ReusablePage {
22. @State switchFlag: boolean = true;

24. build() {
25. Column() {
26. if (this.switchFlag) {
27. // 调用自定义组件ReusableChildPage
28. ReusableChildPage({ message: 'Child' })
29. } else {
30. // 调用自定义组件ReusableChildTwoPage
31. ReusableChildTwoPage({ message: 'ChildTwo' })
32. }
33. Button('Click me')
34. .onClick(() => {
35. this.switchFlag = !this.switchFlag;
36. })
37. }
38. .height('100%')
39. .width('100%')
40. }
41. }

43. @Reusable
44. @Component
45. struct ReusableChildPage {
46. @State message: string = 'Child';

48. aboutToReuse(params: Record<string, ESObject>): void {
49. console.info('Recycle ====Child');
50. this.message = params.message;
51. }

53. build() {
54. Column() {
55. Text(`ReusableChildPage ===${this.message}`)
56. .width(300)
57. .height(40)
58. .margin(10)
59. .backgroundColor('#0d000000')
60. .fontColor('#e6000000')
61. .borderRadius(20)
62. .textAlign(TextAlign.Center)
63. // 调用全局@Builder函数itemBuilder
64. itemBuilder({ componentName: this.message })
65. }
66. }
67. }

69. @Reusable
70. @Component
71. struct ReusableChildTwoPage {
72. @State message: string = 'ChildTwo';

74. aboutToReuse(params: Record<string, ESObject>): void {
75. console.info('Recycle ====ChildTwo');
76. this.message = params.message;
77. }

79. build() {
80. Column() {
81. Text(`ReusableChildTwoPage ===${this.message}`)
82. .width(300)
83. .height(40)
84. .margin(10)
85. .backgroundColor('#0d000000')
86. .fontColor('#e6000000')
87. .borderRadius(20)
88. .textAlign(TextAlign.Center)
89. // 调用全局@Builder函数itemBuilder
90. itemBuilder({ componentName: this.message })
91. }
92. }
93. }
```

[AcrossComponents.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/AcrossComponents.ets#L15-L105)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/FFnGFCH1T06K-MZSMaQ6Dg/zh-cn_image_0000002558764066.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=D8E2C08F0A990C3743647DB106E28B3AB2059781FEF6122C913DC14F6B271899)

### @Builder支持状态变量刷新

从API version 20开始，开发者可以通过使用UIUtils.makeBinding()函数、Binding类和MutableBinding类实现@Builder函数中状态变量的刷新。详情请参考[状态管理API文档](../harmonyos-references/js-apis-statemanagement.md#makebinding20)。

```
1. import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class ClassA {
5. @Trace public props: string = 'Hello';
6. }

8. @Builder
9. function customButton(num1: Binding<number>, num2: MutableBinding<number>) {
10. Row() {
11. Column() {
12. Text(`number1 === ${num1.value},  number2 === ${num2.value}`)
13. .width(300)
14. .height(40)
15. .margin(10)
16. .backgroundColor('#0d000000')
17. .fontColor('#e6000000')
18. .borderRadius(20)
19. .textAlign(TextAlign.Center)

21. Button(`only change number2`)
22. .onClick(() => {
23. num2.value += 1;
24. })
25. }
26. }
27. }

29. @Builder
30. function customButtonObj(obj1: MutableBinding<ClassA>) {
31. Row() {
32. Column() {
33. Text(`props === ${obj1.value.props}`)
34. .width(300)
35. .height(40)
36. .margin(10)
37. .backgroundColor('#0d000000')
38. .fontColor('#e6000000')
39. .borderRadius(20)
40. .textAlign(TextAlign.Center)

42. Button(`change props`)
43. .onClick(() => {
44. obj1.value.props += 'Hi';
45. })
46. }
47. }
48. }

50. @Entry
51. @ComponentV2
52. struct Single {
53. @Local number1: number = 5;
54. @Local number2: number = 12;
55. @Local classA: ClassA = new ClassA();

57. build() {
58. Column() {
59. Button(`change both number1 and number2`)
60. .onClick(() => {
61. this.number1 += 1;
62. this.number2 += 2;
63. })
64. Text(`number1 === ${this.number1}`)
65. .width(300)
66. .height(40)
67. .margin(10)
68. .backgroundColor('#0d000000')
69. .fontColor('#e6000000')
70. .borderRadius(20)
71. .textAlign(TextAlign.Center)
72. Text(`number2 === ${this.number2}`)
73. .width(300)
74. .height(40)
75. .margin(10)
76. .backgroundColor('#0d000000')
77. .fontColor('#e6000000')
78. .borderRadius(20)
79. .textAlign(TextAlign.Center)
80. // 调用全局@Builder函数customButton
81. customButton(
82. UIUtils.makeBinding<number>(() => this.number1), // 使用UIUtils.makeBinding()函数实现@Builder函数中状态变量的刷新
83. UIUtils.makeBinding<number>(
84. () => this.number2,
85. (val: number) => {
86. this.number2 = val;
87. })
88. )
89. Text(`classA.props === ${this.classA.props}`)
90. .width(300)
91. .height(40)
92. .margin(10)
93. .backgroundColor('#0d000000')
94. .fontColor('#e6000000')
95. .borderRadius(20)
96. .textAlign(TextAlign.Center)
97. // 调用全局@Builder函数customButtonObj
98. customButtonObj(
99. UIUtils.makeBinding<ClassA>( // 使用UIUtils.makeBinding()函数实现@Builder函数中状态变量的刷新
100. () => this.classA,
101. (val: ClassA) => {
102. this.classA = val;
103. })
104. )
105. }
106. .width('100%')
107. .height('100%')
108. .alignItems(HorizontalAlign.Center)
109. .justifyContent(FlexAlign.Center)
110. }
111. }
```

[BuilderSupports.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/BuilderSupports.ets#L15-L125)

示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/cvCSDMc1S2W-CBN-jYChvw/zh-cn_image_0000002558604410.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=FBF07F1D3CBE5E38275464F04E9E68F74E72C334F08CCA645EA45861C9CEB914)

## 常见问题

### @Builder存在两个或两个以上参数

当存在两个或两个以上的参数时，即使通过对象字面量形式传递，值的改变也不会触发UI刷新。

【反例】

```
1. class GlobalTmp1 {
2. public strValue: string = 'Hello';
3. }

5. @Builder
6. function overBuilder1(param: GlobalTmp1, num: number) {
7. Column() {
8. Text(`strValue: ${param.strValue}`)
9. Text(`num: ${num}`)
10. }
11. }

13. @Entry
14. @Component
15. struct Parent1 {
16. @State objParam: GlobalTmp1 = new GlobalTmp1();
17. @State num: number = 0;

19. build() {
20. Column() {
21. Text('UI Rendered via @Builder')
22. .fontSize(20)
23. // 使用了两个参数，用法错误。
24. overBuilder1({ strValue: this.objParam.strValue }, this.num)
25. Line()
26. .width('100%')
27. .height(10)
28. .backgroundColor('#000000').margin(10)
29. Button('Update Values').onClick(() => {
30. this.objParam.strValue = 'Hello World';
31. this.num = 1;
32. })
33. }
34. }
35. }
```

[MultipleIncorrectUsage1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/MultipleIncorrectUsage1.ets#L15-L49)

【反例】

```
1. class GlobalTmp2 {
2. public strValue: string = 'Hello';
3. }

5. class SecondTmp {
6. public numValue: number = 0;
7. }

9. @Builder
10. function overBuilder2(param: GlobalTmp2, num: SecondTmp) {
11. Column() {
12. Text(`strValue: ${param.strValue}`)
13. Text(`num: ${num.numValue}`)
14. }
15. }

17. @Entry
18. @Component
19. struct Parent2 {
20. @State strParam: GlobalTmp2 = new GlobalTmp2();
21. @State numParam: SecondTmp = new SecondTmp();

23. build() {
24. Column() {
25. Text('UI Rendered via @Builder')
26. .fontSize(20)
27. // 使用了两个参数，用法错误。
28. overBuilder2({ strValue: this.strParam.strValue }, { numValue: this.numParam.numValue })
29. Line()
30. .width('100%')
31. .height(10)
32. .backgroundColor('#000000').margin(10)
33. Button('Update Values').onClick(() => {
34. this.strParam.strValue = 'Hello World';
35. this.numParam.numValue = 1;
36. })
37. }
38. }
39. }
```

[MultipleIncorrectUsage2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/MultipleIncorrectUsage2.ets#L15-L51)

@Builder只接受一个参数。当传入一个参数的时候，通过对象字面量的形式传递，值的改变会引起UI的刷新。

【正例】

```
1. class GlobalTmp3 {
2. public strValue: string = 'Hello';
3. public numValue: number = 0;
4. }

6. @Builder
7. function overBuilder3(param: GlobalTmp3) {
8. Column() {
9. Text(`strValue: ${param.strValue}`)
10. Text(`num: ${param.numValue}`)
11. }
12. }

14. @Entry
15. @Component
16. struct Parent3 {
17. @State objParam: GlobalTmp3 = new GlobalTmp3();

19. build() {
20. Column() {
21. Text('UI Rendered via @Builder')
22. .fontSize(20)
23. // 传入一个参数，正确用法
24. overBuilder3({ strValue: this.objParam.strValue, numValue: this.objParam.numValue })
25. Line()
26. .width('100%')
27. .height(10)
28. .backgroundColor('#000000').margin(10)
29. Button('Update Values').onClick(() => {
30. this.objParam.strValue = 'Hello World';
31. this.objParam.numValue = 1;
32. })
33. }
34. }
35. }
```

[MultipleCorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/MultipleCorrectUsage.ets#L15-L47)

### 使用@ComponentV2装饰器触发动态刷新

在@ComponentV2装饰的组件中，配合@ObservedV2和@Trace装饰器，通过按值传递实现UI刷新功能。

【反例】

在[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件中，使用简单数据类型不可以触发UI的刷新。

```
1. @ObservedV2
2. class ParamTemp {
3. @Trace public count : number = 0;
4. }

6. @Builder
7. function renderNumber(paramNum: number) {
8. Text(`paramNum : ${paramNum}`)
9. .fontSize(30)
10. .fontWeight(FontWeight.Bold)
11. }

13. @Entry
14. @ComponentV2
15. struct PageBuilderIncorrectUsage {
16. @Local classValue: ParamTemp = new ParamTemp();
17. // 此处使用简单数据类型不支持刷新UI的能力。
18. @Local numValue: number = 0;
19. private progressTimer: number = -1;

21. aboutToAppear(): void {
22. this.progressTimer = setInterval(() => {
23. if (this.classValue.count < 100) {
24. this.classValue.count += 5;
25. this.numValue += 5;
26. } else {
27. clearInterval(this.progressTimer);
28. }
29. }, 500);
30. }

32. build() {
33. Column() {
34. renderNumber(this.numValue)
35. }
36. .width('100%')
37. .height('100%')
38. .padding(50)
39. }
40. }
```

[DynamicIncorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/DynamicIncorrectUsage.ets#L15-L56)

【正例】

在@ComponentV2装饰器装饰的自定义组件中，只有使用@ObservedV2装饰的ParamTmpClass类和使用@Trace装饰的count属性才能触发UI刷新。

```
1. @ObservedV2
2. class ParamTmpClass {
3. @Trace public count: number = 0;
4. }

6. @Builder
7. function renderText(param: ParamTmpClass) {
8. Column() {
9. Text(`param : ${param.count}`)
10. .fontSize(20)
11. .fontWeight(FontWeight.Bold)
12. }
13. }

15. @Builder
16. function renderMap(paramMap: Map<string, number>) {
17. Text(`paramMap : ${paramMap.get('name')}`)
18. .fontSize(20)
19. .fontWeight(FontWeight.Bold)
20. }

22. @Builder
23. function renderSet(paramSet: Set<number>) {
24. Text(`paramSet : ${paramSet.size}`)
25. .fontSize(20)
26. .fontWeight(FontWeight.Bold)
27. }

29. @Builder
30. function renderNumberArr(paramNumArr: number[]) {
31. Text(`paramNumArr : ${paramNumArr[0]}`)
32. .fontSize(20)
33. .fontWeight(FontWeight.Bold)
34. }

36. @Entry
37. @ComponentV2
38. struct PageBuilderCorrectUsage {
39. @Local builderParams: ParamTmpClass = new ParamTmpClass();
40. @Local mapValue: Map<string, number> = new Map();
41. @Local setValue: Set<number> = new Set([0]);
42. @Local numArrValue: number[] = [0];
43. private progressTimer: number = -1;

45. aboutToAppear(): void {
46. this.progressTimer = setInterval(() => {
47. if (this.builderParams.count < 100) {
48. // builderParams是被@ObservedV2装饰的ParamTmpClass类
49. // count属性被@Trace装饰
50. // count变化会引起UI刷新
51. this.builderParams.count += 5;
52. this.mapValue.set('name', this.builderParams.count);
53. this.setValue.add(this.builderParams.count);
54. this.numArrValue[0] = this.builderParams.count;
55. } else {
56. clearInterval(this.progressTimer);
57. }
58. }, 500);
59. }

61. @Builder
62. localBuilder() {
63. Column() {
64. Text(`localBuilder : ${this.builderParams.count}`)
65. .fontSize(20)
66. .fontWeight(FontWeight.Bold)
67. }
68. }

70. build() {
71. Column() {
72. this.localBuilder()
73. Text(`builderParams :${this.builderParams.count}`)
74. .fontSize(20)
75. .fontWeight(FontWeight.Bold)
76. renderText(this.builderParams)
77. renderText({ count: this.builderParams.count })
78. renderMap(this.mapValue)
79. renderSet(this.setValue)
80. renderNumberArr(this.numArrValue)
81. }
82. .width('100%')
83. .height('100%')
84. }
85. }
```

[DynamicCorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/DynamicCorrectUsage.ets#L15-L98)

### 在@Builder内创建自定义组件传递参数不刷新问题

在parentBuilder1函数中创建自定义组件HelloComponent1，传递参数为class对象并修改对象内的值时，UI不会触发刷新功能。

【反例】

```
1. class Tmp4 {
2. public name: string = 'Hello';
3. public age: number = 16;
4. }

6. @Builder
7. function parentBuilder1(params: Tmp4) {
8. Row() {
9. Column() {
10. Text(`parentBuilder1===${params.name}===${params.age}`)
11. .fontSize(20)
12. .fontWeight(FontWeight.Bold)
13. // 此写法不属于按引用传递方式，用法错误导致UI不刷新。
14. HelloComponent1({ info: params })
15. }
16. }
17. }

19. @Component
20. struct HelloComponent1 {
21. @Prop info: Tmp4 = new Tmp4();

23. build() {
24. Row() {
25. Text(`HelloComponent1===${this.info.name}===${this.info.age}`)
26. .fontSize(20)
27. .fontWeight(FontWeight.Bold)
28. }
29. }
30. }

32. @Entry
33. @Component
34. struct ParentPage1 {
35. @State nameValue: string = 'Zhang San';
36. @State ageValue: number = 18;

38. build() {
39. Column() {
40. parentBuilder1({ name: this.nameValue, age: this.ageValue })
41. Button('Click me')
42. .onClick(() => {
43. // 此处修改内容时，不会引起HelloComponent1处的变化
44. this.nameValue = 'Li Si';
45. this.ageValue = 20;
46. })
47. }
48. .height('100%')
49. .width('100%')
50. }
51. }
```

[BuilderIncorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/BuilderIncorrectUsage.ets#L15-L67)

在parentBuilder2函数中创建自定义组件HelloComponent2，传递参数为对象字面量形式并修改对象内的值时，UI触发刷新功能。

【正例】

```
1. class Tmp5 {
2. public name: string = 'Hello';
3. public age: number = 16;
4. }

6. @Builder
7. function parentBuilder2(params: Tmp5) {
8. Row() {
9. Column() {
10. Text(`parentBuilder2===${params.name}===${params.age}`)
11. .fontSize(20)
12. .fontWeight(FontWeight.Bold)
13. // 将整个对象拆分开变成简单类型，属于按引用传递方式，更改属性能够触发UI刷新。
14. HelloComponent2({ childName: params.name, childAge: params.age })
15. }
16. }
17. }

19. @Component
20. struct HelloComponent2 {
21. @Prop childName: string = '';
22. @Prop childAge: number = 0;

24. build() {
25. Row() {
26. Text(`HelloComponent2===${this.childName}===${this.childAge}`)
27. .fontSize(20)
28. .fontWeight(FontWeight.Bold)
29. }
30. }
31. }

33. @Entry
34. @Component
35. struct ParentPage2 {
36. @State nameValue: string = 'Zhang San';
37. @State ageValue: number = 18;

39. build() {
40. Column() {
41. parentBuilder2({ name: this.nameValue, age: this.ageValue })
42. Button('Click me')
43. .onClick(() => {
44. // 此处修改内容时，会引起HelloComponent2处的变化
45. this.nameValue = 'Li Si';
46. this.ageValue = 20;
47. })
48. }
49. .height('100%')
50. .width('100%')
51. }
52. }
```

[BuilderCorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/BuilderCorrectUsage.ets#L15-L68)

### 在UI语句外调用@Builder函数或方法影响节点正常刷新

当@Builder方法赋值给变量或者数组后，在UI方法中无法使用，且会造成刷新时节点显示异常。

【反例】

```
1. @Entry
2. @Component
3. struct BackGround1 {
4. @Builder
5. myImages() {
6. Column() {
7. // 从应用media目录加载名为startIcon的图像资源。此处'app.media.startIcon'仅作示例，请开发者自行替换。
8. Image($r('app.media.startIcon')).width('100%').height('100%')
9. }
10. };

12. @Builder
13. myImages2() {
14. Column() {
15. // 从应用media目录加载名为startIcon的图像资源。此处'app.media.startIcon'仅作示例，请开发者自行替换。
16. Image($r('app.media.startIcon')).width('100%').height('100%')
17. }
18. };

20. private bgList: Array<CustomBuilder> = [this.myImages(), this.myImages2()]; // 错误用法，应避免在UI方法外调用@Builder方法
21. @State bgBuilder: CustomBuilder = this.myImages(); // 错误用法，应避免在UI方法外调用@Builder方法
22. @State bgColor: ResourceColor = Color.Orange;
23. @State bgColor2: ResourceColor = Color.Orange;
24. @State index: number = 0;

26. build() {
27. Column({ space: 10 }) {
28. Text('1').width(100).height(50)
29. Text('2').width(100).height(50)
30. Text('3').width(100).height(50)

32. Text('4-1').width(100).height(50).fontColor(this.bgColor)
33. Text('5-1').width(100).height(50)
34. Text('4-2').width(100).height(50)
35. Text('5-2').width(100).height(50)
36. Stack() {
37. Column() {
38. Text('Vsync2')
39. }
40. .size({ width: '100%', height: '100%' })
41. .border({ width: 1, color: Color.Black })
42. }
43. .size({ width: 100, height: 80 })
44. .backgroundColor('#ffbbd4bb')

46. Button('change').onClick((event: ClickEvent) => {
47. this.index = 1;
48. this.bgColor = Color.Red;
49. this.bgColor2 = Color.Red;
50. })
51. }
52. .margin(10)
53. }
54. }
```

[OutsideIncorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/OutsideIncorrectUsage.ets#L15-L71)

@Builder方法赋值给变量或数组后在UI方法中无法使用，开发者应避免将@Builder赋值给变量或数组后再使用。

【正例】

```
1. @Entry
2. @Component
3. struct BackGround2 {
4. @Builder
5. myImages() {
6. Column() {
7. // 从应用media目录加载名为startIcon的图像资源。此处'app.media.startIcon'仅作示例，请开发者自行替换。
8. Image($r('app.media.startIcon')).width('100%').height('100%')
9. }
10. }

12. @Builder
13. myImages2() {
14. Column() {
15. // 从应用media目录加载名为startIcon的图像资源。此处'app.media.startIcon'仅作示例，请开发者自行替换。
16. Image($r('app.media.startIcon')).width('100%').height('100%')
17. }
18. }

20. @State bgColor: ResourceColor = Color.Orange;
21. @State bgColor2: ResourceColor = Color.Orange;
22. @State index: number = 0;

24. build() {
25. Column({ space: 10 }) {
26. Text('1').width(100).height(50)
27. Text('2').width(100).height(50).background(this.myImages) // 直接传递@Builder方法
28. Text('3').width(100).height(50).background(this.myImages()) // 直接调用@Builder方法

30. Text('4-1').width(100).height(50).fontColor(this.bgColor)
31. Text('5-1').width(100).height(50)
32. Text('4-2').width(100).height(50)
33. Text('5-2').width(100).height(50)
34. Stack() {
35. Column() {
36. Text('Vsync2')
37. }
38. .size({ width: '100%', height: '100%' })
39. .border({ width: 1, color: Color.Black })
40. }
41. .size({ width: 100, height: 80 })
42. .backgroundColor('#ffbbd4bb')

44. Button('change').onClick((event: ClickEvent) => {
45. this.index = 1;
46. this.bgColor = Color.Red;
47. this.bgColor2 = Color.Red;
48. })
49. }
50. .margin(10)
51. }
52. }
```

[OutsideCorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/OutsideCorrectUsage.ets#L15-L68)

### 在@Builder方法中使用MutableBinding未传递set访问器

@Builder方法定义时使用MutableBinding，构造时没有给MutableBinding类型参数传递set访问器，触发set访问器会造成运行时错误。

【反例】

```
1. import { UIUtils, Binding, MutableBinding } from '@kit.ArkUI';

3. @ObservedV2
4. class GlobalTmp1 {
5. @Trace public strValue: string = 'Hello';
6. }

8. @Builder
9. function builderWithTwoParams1(param1: Binding<GlobalTmp1>, param2: MutableBinding<number>) {
10. Column() {
11. Text(`strValue: ${param1.value.strValue}`)
12. Button(`num: ${param2.value}`)
13. .onClick(() => {
14. param2.value += 1; // 点击Button触发set访问器会造成运行时错误
15. })
16. }.borderWidth(1)
17. }

19. @Entry
20. @ComponentV2
21. struct MakeBindingTest1 {
22. @Local GlobalTmp1: GlobalTmp1 = new GlobalTmp1();
23. @Local num: number = 0;

25. build() {
26. Column() {
27. Text(`${this.GlobalTmp1.strValue}`)
28. builderWithTwoParams1(UIUtils.makeBinding(() => this.GlobalTmp1),
29. UIUtils.makeBinding<number>(() => this.num)) // 构造MutableBinding类型参数时没有传SetterCallback
30. Button('Update Values').onClick(() => {
31. this.GlobalTmp1.strValue = 'Hello World 2025';
32. this.num = 1;
33. })
34. }
35. }
36. }
```

[AccessorIncorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/AccessorIncorrectUsage.ets#L15-L51)

使用规格详见状态管理API文档中的[MutableBinding](../harmonyos-references/js-apis-statemanagement.md#mutablebindingt20)。

【正例】

```
1. import { UIUtils, Binding, MutableBinding } from '@kit.ArkUI';

3. @ObservedV2
4. class GlobalTmp2 {
5. @Trace public strValue: string = 'Hello';
6. }

8. @Builder
9. function builderWithTwoParams2(param1: Binding<GlobalTmp2>, param2: MutableBinding<number>) {
10. Column() {
11. Text(`strValue: ${param1.value.strValue}`)
12. Button(`num: ${param2.value}`)
13. .onClick(() => {
14. param2.value += 1; // 修改了MutableBinding类型参数的value属性
15. })
16. }.borderWidth(1)
17. }

19. @Entry
20. @ComponentV2
21. struct MakeBindingTest2 {
22. @Local GlobalTmp2: GlobalTmp2 = new GlobalTmp2();
23. @Local num: number = 0;

25. build() {
26. Column() {
27. Text(`${this.GlobalTmp2.strValue}`)
28. builderWithTwoParams2(UIUtils.makeBinding(() => this.GlobalTmp2),
29. UIUtils.makeBinding<number>(() => this.num,
30. val => {
31. this.num = val;
32. }))
33. Button('Update Values').onClick(() => {
34. this.GlobalTmp2.strValue = 'Hello World 2025';
35. this.num = 1;
36. })
37. }
38. }
39. }
```

[AccessorCorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/AccessorCorrectUsage.ets#L15-L55)

### 在@Builder装饰的函数内部修改入参内容

不使用[MutableBinding](../harmonyos-references/js-apis-statemanagement.md#mutablebindingt20)的情况下，在@Builder装饰的函数内部修改参数值，修改不会生效且可能造成运行时错误。从API version 23开始，将返回错误码[140109](../harmonyos-references/errorcode-statemanagement.md#section140109-builder非法触发参数属性赋值)。

【反例】

```
1. @Builder
2. function myGlobalBuilder(value: string) {
3. Column() {
4. Text(`myGlobalBuilder: ${value} `)
5. .fontSize(16)
6. .onClick(() => {
7. // 简单类型按值传递的@Builder函数中修改参数，不闪退但UI不刷新
8. value = 'value change';
9. })
10. }.borderWidth(1)
11. }

13. interface TempMod1 {
14. paramA: string;
15. }

17. @Builder
18. function overBuilderMod1(param: TempMod1) {
19. Row() {
20. Column() {
21. Button(`overBuilderMod1 === ${param.paramA}`)
22. .onClick(() => {
23. // 错误写法，不允许在@Builder装饰的函数内部修改对象类型参数的属性，闪退且UI不刷新
24. param.paramA = 'Yes';
25. })
26. Button('change')
27. .onClick(() => {
28. // 错误写法，不允许在@Builder装饰的函数内部修改对象类型参数的引用，不闪退但UI不刷新
29. param = { paramA: 'change trial' };
30. })
31. }
32. }
33. }

35. @Entry
36. @Component
37. struct ParentMod1 {
38. @State label: string = 'Hello';
39. @State message1: string = 'Value Passing';

41. @Builder
42. extendBlank() {
43. Row() {
44. Blank()
45. }
46. .height(20)
47. }

49. build() {
50. Column() {
51. // 按引用传递能实现参数变化时的UI刷新，但不能在@Builder函数内部修改参数
52. overBuilderMod1({ paramA: this.label });
53. this.extendBlank();
54. Button('click me')
55. .onClick(() => {
56. this.label = 'ArkUI';
57. })
58. this.extendBlank();
59. myGlobalBuilder(this.message1);
60. }
61. }
62. }
```

[ChangingIncorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/ChangingIncorrectUsage.ets#L15-L78)

正确使用[MutableBinding](../harmonyos-references/js-apis-statemanagement.md#mutablebindingt20)可以帮助开发者在@Builder装饰的函数内部修改参数值。

【正例】

```
1. import { UIUtils, MutableBinding } from '@kit.ArkUI';

3. // 使用MutableBinding在@Builder装饰的函数中修改参数值
4. @Builder
5. function myGlobalBuilderMod(str: MutableBinding<string>) {
6. Column() {
7. Text(`Mod--MyGlobalBuilder: ${str.value}`)
8. .fontSize(16)
9. .onClick(() => {
10. str.value = 'value change mod';
11. })
12. }
13. }

15. interface TempMod2 {
16. paramA: string;
17. }

19. // 使用MutableBinding在@Builder装饰的函数内部修改参数值
20. @Builder
21. function overBuilderMod2(param: MutableBinding<TempMod2>) {
22. Column() {
23. Button(`Mod--overBuilder === ${param.value.paramA}`)
24. .onClick(() => {
25. param.value.paramA = 'Yes';
26. })
27. Button(`change`)
28. .onClick(() => {
29. param.value = { paramA: 'trialOne' };
30. })
31. }
32. }

34. @Entry
35. @Component
36. struct ParentMod2 {
37. @State label: string = 'Hello';
38. @State message1: string = 'Value Passing';
39. @State objectOne: TempMod2 = {
40. paramA: this.label
41. };

43. @Builder
44. extendBlank() {
45. Row() {
46. Blank()
47. }
48. .height(20)
49. }

51. build() {
52. Column() {
53. // 使用MutableBinding时无法传对象字面量，需要先将字面量对象抽出为状态变量
54. overBuilderMod2(
55. UIUtils.makeBinding<TempMod2>(
56. () => this.objectOne,
57. value => {
58. this.objectOne = value; // 必须要传SetterCallback，否则触发时会造成运行时错误
59. }
60. )
61. )
62. this.extendBlank();
63. Button('click me')
64. .onClick(() => {
65. this.objectOne.paramA = 'ArkUI';
66. })
67. this.extendBlank();
68. myGlobalBuilderMod(
69. UIUtils.makeBinding<string>(
70. () => this.message1,
71. value => {
72. this.message1 = value; // 必须要传SetterCallback，否则触发时会造成运行时错误
73. }
74. )
75. );
76. }
77. }
78. }
```

[ChangingCorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/ChangingCorrectUsage.ets#L15-L94)

### 在@Watch函数中执行@Builder函数

在[@Watch](arkts-watch.md)函数中执行@Builder函数，会导致UI刷新异常。

【反例】

```
1. @Entry
2. @Component
3. struct Child1 {
4. @Provide @Watch('provideWatch') content: string = 'Index: hello world';

6. @Builder
7. watchBuilder(content: string) {
8. Row() {
9. Text(`${content}`)
10. }
11. }

13. provideWatch() {
14. this.watchBuilder(this.content); // 错误写法，在@Watch函数中使用@Builder函数
15. }

17. build() {
18. Column() {
19. Button(`content value: ${this.content}`)
20. .onClick(() => {
21. this.content += '_world';
22. })
23. this.watchBuilder(this.content);
24. }
25. }
26. }
```

[WatchIncorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/WatchIncorrectUsage.ets#L15-L42)

Button按钮会出现UI异常的情况，开发者需要避免在@Watch函数中使用@Builder函数。

【正例】

```
1. @Entry
2. @Component
3. struct Child2 {
4. @Provide @Watch('provideWatch') content: string = 'Index: hello world';

6. @Builder
7. watchBuilder(content: string) {
8. Row() {
9. Text(`${content}`)
10. }
11. }

13. provideWatch() {
14. // 正确写法，不在@Watch函数中使用@Builder函数
15. console.info(`content value has changed.`);
16. }

18. build() {
19. Column() {
20. Button(`content value: ${this.content}`)
21. .onClick(() => {
22. this.content += '_world';
23. })
24. this.watchBuilder(this.content);
25. }
26. }
27. }
```

[WatchCorrectUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderComponent/entry/src/main/ets/pages/WatchCorrectUsage.ets#L15-L42)
