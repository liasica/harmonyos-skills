---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage
title: 状态管理V1和V2混用指导（API version 19及之后）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1和V2混用场景 > 状态管理V1和V2混用指导（API version 19及之后）
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2bc14b420cdb4a81e9b988189a7474fc009dbca178abdf5c4d6847ee3dc3f25f
---

## 概述

为了帮助开发者顺利地向状态管理V2迁移，从API version 19开始，减少了对状态管理V1和V2混用场景的约束。具体变更可参考[限制条件](arkts-v1-v2-mixusage.md#限制条件)。同时提供新的方法[enableV2Compatibility](../harmonyos-references/js-apis-statemanagement.md#enablev2compatibility19)和[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)来帮助开发者解决在迁移过程中遇到的混用问题。

说明

本文档中使用“->”表示变量的传递，比如“V1->V2”，表示V1状态变量向V2状态变量传递。

## 限制条件

1. V1装饰器不能和[@ObservedV2](arkts-new-observedv2-and-trace.md)一起使用。因为@ObservedV2/@Trace有自己独立的观察能力，不仅可以在[@ComponentV2](arkts-create-custom-components.md#componentv2)中使用，也可以独立在[@Component](arkts-create-custom-components.md#component)中使用，状态管理框架不希望其观察能力和V1的观察能力混合使用，所以依旧维持禁止现状。
2. V2->V1，V1不支持用装饰器接收@ObservedV2装饰的class，否则编译报错。
3. V1中[@Link](arkts-link.md)遵循其原本初始化规则，只能被V1状态变量初始化，详情见[@Link初始化规则示意图](arkts-link.md#变量的传递访问规则说明)。因为V1中[@Link](arkts-link.md)仅能和V1状态变量建立双向同步关系，而V2中如果想实现双向同步，可以使用@Param、@Event，具体例子见[@Link -> @Param/@Event迁移场景](arkts-v1-v2-migration-inner-component.md#link---paramevent)。

## 新增接口

### makeV1Observed

[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)将不可观察的对象包装成状态管理V1可观察的对象，能力等同于@Observed，其返回值可初始化@ObjectLink。

说明

从API version 19开始，开发者可以使用UIUtils中的makeV1Observed接口将不可观察的对象包装成状态管理V1可观察的对象。

**接口说明**

* makeV1Observed主要和enableV2Compatibility搭配使用，实现V2->V1的传递。
* makeV1Observed可将普通class、Array、Map、Set、Date类型转换为V1的状态变量，其能力等同于@Observed，所以其返回值可以初始化@ObjectLink。
* 如果makeV1Observed接受的数据已经是V1的状态变量，则返回自身，不做任何改变。
* makeV1Observed不会递归执行，仅会将第一层包装成V1的状态变量。

**限制条件**

* 不支持[collections类型](../harmonyos-references/arkts-apis-arkts-collections.md)和[@Sendable](arkts-sendable.md)装饰的class。
* 不支持非object类型。
* 不支持undefined、null。
* 不支持@ObservedV2、[makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)的返回值和V2装饰器装饰的built-in类型的变量（Array、Map、Set和Date）。

### enableV2Compatibility

[enableV2Compatibility](../harmonyos-references/js-apis-statemanagement.md#enablev2compatibility19)将V1的状态变量使能V2的观察能力，即让V1状态变量可以在@ComponentV2中观察到变化。

说明

从API version 19开始，开发者可以使用UIUtils中的enableV2Compatibility接口将V1的状态变量兼容V2中使用。

**接口说明**

* 该接口主要应用于V1->V2的场景，V1的状态变量调用该接口后，传递到@ComponentV2中，则可以在V2中观察到变化，从而实现数据的联动刷新。
* enableV2Compatibility只能作用于V1的状态变量。V1状态变量为V1装饰器装饰的变量，即@Observed装饰的变量，或[@State](arkts-state.md)、[@Prop](arkts-prop.md)、[@Link](arkts-link.md)、[@Provide](arkts-provide-and-consume.md)、[@Consume](arkts-provide-and-consume.md)和[@ObjectLink](arkts-observed-and-objectlink.md)（@ObjectLink需是@Observed装饰的实例或者makeV1Observed的返回值）装饰的变量。否则，将返回入参自身。
* enableV2Compatibility会递归遍历class的所有属性，Array/Set/Map的所有子项，直到遇到非V1状态变量的数据，则停止当前分支的遍历。

**限制条件**

* 不支持非object类型。
* 不支持undefined、null。
* 不支持非V1的状态变量数据。
* 不支持@ObservedV2、[makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)的返回值和V2装饰器装饰的built-in类型的变量（Array、Map、Set和Date）。

## 混用规则

* V1->V2传递复杂类型数据，需要调用enableV2Compatibility，否则无法实现V1和V2的数据联动，建议在V2组件的构造处调用，否则当变量被整体赋值时，需要再次手动调用enableV2Compatibility。

  ```
  1. // 建议用法，this.state = new ObservedClass()时无需再调用UIUtils.enableV2Compatibility，减少代码量
  2. SubComponentV2({param: UIUtils.enableV2Compatibility(this.state)})

  4. // 不建议用法，state做整体赋值时，需要再次调用UIUtils.enableV2Compatibility
  5. // 否则传递给SubComponentV2的V1变量是无法在V2中观察的
  6. // @State state: ObservedClass = UIUtils.enableV2Compatibility(new ObservedClass());
  7. // this.state = UIUtils.enableV2Compatibility(new ObservedClass());
  8. SubComponentV2({param: this.state})
  ```
* V2->V1传递复杂类型数据，在V2中优先声明成V1的状态变量数据，并调用UIUtils.enableV2Compatibility。因为在状态管理V1中，状态变量默认有观察第一层的能力，而状态管理V2仅有观察自身的能力，如果希望双方数据联动，则需要调用UIUtils.enableV2Compatibility(UIUtils.makeV1Observed())拉齐双方的观察能力。

  ```
  1. // 建议用法
  2. @Local unObservedClass: UnObservedClass = UIUtils.enableV2Compatibility(UIUtils.makeV1Observed(new UnObservedClass()));

  4. // 建议用法，ObservedClass是@Observed装饰的class
  5. @Local observedClass: ObservedClass = UIUtils.enableV2Compatibility(new ObservedClass());
  ```
* UIUtils.enableV2Compatibility(UIUtils.makeV1Observed())不会改变V1和V2本身观察能力。

  + 在V1中，UIUtils.enableV2Compatibility(UIUtils.makeV1Observed())等于V1的观察能力，观察数据本身的赋值和第一层属性的赋值，无法深度观察，如果需要深度观察，则需要配合@ObjectLink。
  + 在V2中，UIUtils.enableV2Compatibility(UIUtils.makeV1Observed())可以深度观察，但是需要每一层都是@Observed装饰的class，或者是makeV1Observed的返回值。
  + 不使用enableV2Compatibility和makeV1Observed会导致双重代理问题，使同一状态对象被V1和V2两套状态管理体系同时生成代理对象，从而引起监听逻辑冲突。
* 当数据已使用V2观察能力，即调用UIUtils.enableV2Compatibility后，会将新的数据默认使用V2观察能力，但需要开发者确保新增数据是@Observed装饰的class，或者是makeV1Observed的返回值。完整例子可见[传递嵌套类型（V1->V2）](arkts-v1-v2-mixusage.md#传递嵌套类型v1-v2)、[传递嵌套类型（V2->V1）](arkts-v1-v2-mixusage.md#传递嵌套类型v2-v1)。

  ```
  1. let arr: Array<ArrayItem> = UIUtils.enableV2Compatibility(UIUtils.makeV1Observed(new ArrayItem()));

  3. arr.push(new ArrayItem()); // 新增数据不是V1状态变量，所以不会具有V2观察能力
  4. arr.push(UIUtils.makeV1Observed(new ArrayItem())); // 新增数据是V1的状态变量，默认在V2中可观察
  ```
* 对于built-in类型，如Array、Map、Set和Date，V1和V2都可以观察自身赋值和其API的调用所带来的变化。虽然开发者在不调用UIUtils.enableV2Compatibility时，也可以在一些简单场景下实现数据刷新，但是会带来双重代理导致性能较差的问题，所以建议开发者使用UIUtils.enableV2Compatibility(UIUtils.makeV1Observed())，具体例子见[传递内置类型（V1->V2）](arkts-v1-v2-mixusage.md#传递内置类型v1-v2)、[传递内置类型（V2->V1）](arkts-v1-v2-mixusage.md#传递内置类型v2-v1)。
* 对于有[@Track](arkts-track.md)装饰属性的类，非@Track装饰的属性在@ComponentV2中使用不会崩溃，在@Component中使用仍会崩溃。具体例子见[传递class类型（V1->V2）](arkts-v1-v2-mixusage.md#传递class类型v1-v2)、[传递class类型（V2->V1）](arkts-v1-v2-mixusage.md#传递class类型v2-v1)。

开发者在使用这两个接口混用V1V2时，可遵循下图逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/JM1v2WX5SVmLxlgJG9Kosw/zh-cn_image_0000002583477633.png?HW-CC-KV=V1&HW-CC-Date=20260427T233916Z&HW-CC-Expire=86400&HW-CC-Sign=4E09E20319980672F51B3AD036DF5E6328E1C3C91396217982456CA0F45C5ACA)

## V1中使用V2的自定义组件

### 传递class类型（V1->V2）

**普通class**

以下代码中，V1的状态变量在传递给V2时，调用enableV2Compatibility接口，使V1的变量observedClass在V2组件中有观察能力。

```
1. import { UIUtils } from '@kit.ArkUI';

3. class ObservedClass {
4. public name: string = 'Tom';
5. }

7. @Entry
8. @Component
9. struct CompV1 {
10. @State observedClass: ObservedClass = new ObservedClass();

12. build() {
13. Column() {
14. Text(`@State observedClass: ${this.observedClass.name}`)
15. .onClick(() => {
16. this.observedClass.name += '!'; // 刷新
17. })
18. // 调用UIUtils.enableV2Compatibility使V1的状态变量可在@ComponentV2中有观察能力。
19. CompV2({ observedClass: UIUtils.enableV2Compatibility(this.observedClass) })
20. }
21. }
22. }

24. @ComponentV2
25. struct CompV2 {
26. @Param observedClass: ObservedClass = new ObservedClass();

28. build() {
29. // V1状态变量在使能V2观察能力后，可以在V2观察第一层的变化
30. Text(`@Param observedClass: ${this.observedClass.name}`)
31. .onClick(() => {
32. this.observedClass.name += '!'; // 刷新
33. })
34. }
35. }
```

[StateMixedSceneJsV1V2Recommend.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneJsV1V2Recommend.ets#L15-L52)

**@Observed+@Track装饰的class**

class类被@Observed修饰，从V1向V2传递使用enableV2Compatibility接口装饰的变量。该变量@Track装饰的属性在V1和V2中均可观察，但非@Track装饰的属性，在V1的UI中使用会导致运行时错误，而在V2中虽不会报错，但UI不会响应更新。

下面的例子中：

* name是@Track装饰的属性，其在V1和V2均是可观察的。
* count是非@Track装饰的属性，其在V1和V2的UI中使用均是非法的。

  + 在V1中，如果将非@Track装饰的属性使用在UI中，是非法行为，会有运行时报错。
  + 在V2中，非@Track装饰的属性使用在UI不会有运行时报错，但不会响应更新。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Observed
4. class ObservedClass {
5. @Track public name: string = 'a';
6. public count: number = 0;
7. }

9. @Entry
10. @Component
11. struct CompV1 {
12. @State observedClass: ObservedClass = new ObservedClass();

14. build() {
15. Column() {
16. Text(`@State observedClass: ${this.observedClass.name}`)
17. .onClick(() => {
18. this.observedClass.name += 'a'; // 触发刷新
19. })
20. // 调用UIUtils.enableV2Compatibility使V1的状态变量可在@ComponentV2中有观察能力。
21. CompV2({ observedClass: UIUtils.enableV2Compatibility(this.observedClass) })
22. }
23. }
24. }

26. @ComponentV2
27. struct CompV2 {
28. @Param observedClass: ObservedClass = new ObservedClass();

30. build() {
31. Column() {
32. // V1状态变量在使能V2观察能力后，可以在V2观察第一层的变化
33. Text(`@Param observedClass: ${this.observedClass.name}`)
34. .onClick(() => {
35. this.observedClass.name += '!'; // 刷新
36. })

38. // 使用非@Track的变量在V2中不会崩溃，但不会响应更新
39. Text(`count: ${this.observedClass.count}`).onClick(() => {
40. this.observedClass.count++; // 不触发刷新
41. })
42. }
43. }
44. }
```

[StateMixedSceneObservedClassV1V2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneObservedClassV1V2.ets#L15-L53)

### 传递内置类型（V1->V2）

以Array为例。建议调用enableV2Compatibility和makeV1Observed，避免造成V1和V2双重代理的问题。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ArrayCompV1 {
6. @State arr: Array<number> = UIUtils.makeV1Observed([1, 2, 3]);

8. build() {
9. Column() {
10. Text(`V1 ${this.arr[0]}`).onClick(() => {
11. // 点击触发ArrayCompV1和ArrayCompV2变化
12. this.arr[0]++;
13. })
14. // 传递给V2时，发现当前代理是makeV1Observed包装的，且使能V2观察能力
15. // 在ArrayCompV2中Param不会再次包装代理，避免双重代理的问题
16. ArrayCompV2({ arr: UIUtils.enableV2Compatibility(this.arr) })
17. }
18. .height('100%')
19. .width('100%')
20. }
21. }

23. @ComponentV2
24. struct ArrayCompV2 {
25. @Param arr: Array<number> = [1, 2, 3];

27. build() {
28. Column() {
29. Text(`V2 ${this.arr[0]}`).onClick(() => {
30. // 点击触发ArrayCompV1和ArrayCompV2变化
31. this.arr[0]++;
32. })
33. }
34. }
35. }
```

[StateMixedSceneBuiltTypeV1V2Recommend.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneBuiltTypeV1V2Recommend.ets#L15-L51)

### 传递二维数组（V1->V2）

下面的例子中：

* 使用makeV1Observed将二维数组的内层数组变成V1的状态变量。
* 在传递给V2子组件时，调用enableV2Compatibility，使其具有V2的观察能力，也避免V1V2的双重代理。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ComponentV2
4. struct Item {
5. @Require @Param itemArr: Array<string>;

7. build() {
8. Row() {
9. ForEach(this.itemArr, (item: string, index: number) => {
10. Text(`${index}: ${item}`)
11. }, (item: string) => item + Math.random())
12. // 新增数组元素
13. Button('@Param push')
14. .onClick(() => {
15. this.itemArr.push('Param');
16. })
17. }
18. }
19. }

21. @Entry
22. @Component
23. struct IndexPage {
24. @State arr: Array<Array<string>> =
25. [UIUtils.makeV1Observed(['apple']), UIUtils.makeV1Observed(['banana']), UIUtils.makeV1Observed(['orange'])];

27. build() {
28. Column() {
29. ForEach(this.arr, (itemArr: Array<string>) => {
30. Item({ itemArr: UIUtils.enableV2Compatibility(itemArr) })
31. }, (itemArr: Array<string>) => JSON.stringify(itemArr) + Math.random())
32. Divider()
33. // 数组arr[0]新增元素
34. Button('@State push two-dimensional array item')
35. .onClick(() => {
36. this.arr[0].push('strawberry');
37. })
38. // 数组arr新增元素
39. Button('@State push array item')
40. .onClick(() => {
41. this.arr.push(UIUtils.makeV1Observed(['pear']));
42. })
43. // 修改数组项arr[0][0]的值
44. Button('@State change two-dimensional array first item')
45. .onClick(() => {
46. this.arr[0][0] = 'APPLE';
47. })
48. // 修改数组arr的第一个元素
49. Button('@State change array first item')
50. .onClick(() => {
51. this.arr[0] = UIUtils.makeV1Observed(['watermelon']);
52. })
53. }
54. }
55. }
```

[StateMixedSceneTwoBitArrayV1V2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneTwoBitArrayV1V2.ets#L15-L70)

### 传递嵌套类型（V1->V2）

开发者在状态管理V1中基于@Observed和@ObjectLink实现深度观测，以下代码示例是嵌套场景：

普通outer类在传递给V2子组件NestedClassV2时，调用enableV2Compatibility，使其具有V2的观察能力。如果开发者在传递给V2时没有调用enableV2Compatibility，则@Param无法观察对象的属性。

```
1. import { UIUtils } from '@kit.ArkUI';

3. class ArrayItem {
4. public value: number = 0;

6. constructor(value: number) {
7. this.value = value;
8. }
9. }

11. class Inner {
12. public innerValue: string = 'inner';
13. public arr: Array<ArrayItem>;

15. constructor(arr: Array<ArrayItem>) {
16. this.arr = arr;
17. }
18. }

20. class Outer {
21. @Track public outerValue: string = 'outer';
22. @Track public inner: Inner;

24. constructor(inner: Inner) {
25. this.inner = inner;
26. }
27. }

29. @Entry
30. @Component
31. struct NestedClassV1 {
32. // 需保证每一层都是V1的状态变量
33. @State outer: Outer =
34. UIUtils.makeV1Observed(new Outer(
35. UIUtils.makeV1Observed(new Inner(UIUtils.makeV1Observed([
36. UIUtils.makeV1Observed(new ArrayItem(1)),
37. UIUtils.makeV1Observed(new ArrayItem(2))
38. ])))
39. ));

41. build() {
42. Column() {
43. Text(`@State outer.outerValue can update ${this.outer.outerValue}`)
44. .fontSize(20)
45. .onClick(() => {
46. // @State可以观察第一层的变化
47. // 变化会通知@ObjectLink和@Param刷新
48. this.outer.outerValue += '!';
49. })

51. Text(`@State outer.inner.innerValue cannot update ${this.outer.inner.innerValue}`)
52. .fontSize(20)
53. .onClick(() => {
54. // @State无法观察第二层的变化
55. // 但该变化会被@ObjectLink和@Param观察
56. this.outer.inner.innerValue += '!';
57. })
58. // 将inner传递给@ObjectLink可观察inner属性的变化
59. NestedClassV1ObjectLink({ inner: this.outer.inner })
60. // 将开启enableV2Compatibility的数据传给V2
61. NestedClassV2({ outer: UIUtils.enableV2Compatibility(this.outer) })
62. }
63. .height('100%')
64. .width('100%')
65. }
66. }

68. @Component
69. struct NestedClassV1ObjectLink {
70. @ObjectLink inner: Inner;

72. build() {
73. Text(`@ObjectLink inner.innerValue can update ${this.inner.innerValue}`)
74. .fontSize(20)
75. .onClick(() => {
76. // 可以触发刷新，和@Param是同一个对象的引用，@Param也会进行刷新
77. this.inner.innerValue += '!';
78. })
79. }
80. }

82. @ComponentV2
83. struct NestedClassV2 {
84. @Require @Param outer: Outer;

86. build() {
87. Column() {
88. Text(`@Param outer.outerValue can update ${this.outer.outerValue}`)
89. .fontSize(20)
90. .onClick(() => {
91. // 可以观察第一层的变化
92. this.outer.outerValue += '!';
93. })
94. Text(`@Param outer.inner.innerValue can update ${this.outer.inner.innerValue}`)
95. .fontSize(20)
96. .onClick(() => {
97. // 可以观察第二层的变化，和@ObjectLink是同一个对象的引用，也会触发刷新
98. this.outer.inner.innerValue += '!';
99. })

101. Repeat(this.outer.inner.arr)
102. .each((item: RepeatItem<ArrayItem>) => {
103. Text(`@Param outer.inner.arr index: ${item.index} item: ${item.item.value}`)
104. })

106. Button('@Param push').onClick(() => {
107. // outer已经使能了V2观察能力，对于新增加的数据，则默认开启V2观察能力
108. this.outer.inner.arr.push(UIUtils.makeV1Observed(new ArrayItem(20)));
109. })

111. Button('@Param change the last Item').onClick(() => {
112. // 可以观察最后一个数组项的属性变化
113. this.outer.inner.arr[this.outer.inner.arr.length - 1].value++;
114. })
115. }
116. }
117. }
```

[StateMixedSceneNestedTypeV1V2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneNestedTypeV1V2.ets#L15-L133)

以上例子刷新行为可总结为：

* @State仅能观察第一层的变化，如果要深度观察，需要传递给@ObjectLink。
* @State的第二层的改变，虽然不能带来本层的刷新，但会被@ObjectLink和@Param观察到，并触发它们关联组件的刷新。
* @ObjectLink和@Param是同一个对象的引用，其属性改变也会带来其他引用的刷新。

## V2中使用V1的自定义组件

### 传递class类型（V2->V1）

**普通class**

因为V1和V2观察能力不同，如果不调用UIUtils.enableV2Compatibility(UIUtils.makeV1Observed())直接进行数据传递，则会造成不刷新或者刷新行为不一致的问题。

```
1. import { UIUtils } from '@kit.ArkUI';

3. class ObservedClass {
4. public name: string = 'Tom';
5. }

7. @Entry
8. @ComponentV2
9. struct CompV2 {
10. @Local observedClass: ObservedClass = UIUtils.enableV2Compatibility(UIUtils.makeV1Observed(new ObservedClass()));

12. build() {
13. Column() {
14. // @Local原本能力仅可观察自身
15. // 但是调用了UIUtils.makeV1Observed使其变成V1的状态变量，V1状态变量可观察第一层变化
16. // 又调用UIUtils.enableV2Compatibility使其在V2中可观察
17. // 所以当前可观察第一层属性的变化
18. Text(`@Local observedClass: ${this.observedClass.name}`)
19. .onClick(() => {
20. this.observedClass.name += '!'; // 刷新
21. })
22. // @ObjectLink可接收@Observed装饰class的实例或者makeV1Observed的返回值
23. CompV1({ observedClass: this.observedClass })
24. }
25. }
26. }

28. @Component
29. struct CompV1 {
30. @ObjectLink observedClass: ObservedClass;

32. build() {
33. // 在CompV1中可观察第一层的变化
34. Text(`@ObjectLink observedClass: ${this.observedClass.name}`)
35. .onClick(() => {
36. this.observedClass.name += '!'; // 刷新
37. })
38. }
39. }
```

[StateMixedSceneJsV2V1Recommend.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneJsV2V1Recommend.ets#L15-L55)

**@Observed+@Track装饰的class**

下面例子中：

* ObservedClass是@Observed装饰的class，所以传递给V1调用UIUtils.enableV2Compatibility时，无需再调用UIUtils.makeV1Observed。
* 只有@Track装饰的变量在V1和V2中可观察。非@Track的变量在V1中使用在UI上会有运行时报错，在V2中不会报错，但不会响应刷新。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Observed
4. class ObservedClass {
5. @Track public name: string = 'a';
6. public count: number = 0;
7. }

9. @Entry
10. @ComponentV2
11. struct CompV1 {
12. @Local observedClass: ObservedClass = UIUtils.enableV2Compatibility(new ObservedClass());

14. build() {
15. Column() {
16. Text(`name: ${this.observedClass.name}`).onClick(() => {
17. // 触发刷新
18. this.observedClass.name += 'a';
19. })
20. // 使用非@Track的变量在V2中不会崩溃，但不响应更新
21. Text(`count: ${this.observedClass.count}`).onClick(() => {
22. this.observedClass.count++;
23. })

25. CompV2({ observedClass: this.observedClass })
26. }
27. }
28. }

30. @Component
31. struct CompV2 {
32. @ObjectLink observedClass: ObservedClass;

34. build() {
35. Column() {
36. Text(`count: ${this.observedClass.name}`).onClick(() => {
37. // 触发刷新
38. this.observedClass.name += 'a';
39. })
40. }
41. }
42. }
```

[StateMixedSceneObservedClassV2V1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneObservedClassV2V1.ets#L15-L58)

### 传递内置类型（V2->V1）

如果在V2中定义@Local arr: Array<number> = UIUtils.enableV2Compatibility(UIUtils.makeV1Observed([1, 2, 3]))，由于用了@Local装饰器V2可以观察属性的变化。但是没有调用enableV2Compatibility和makeV1Observed，V1无法观察属性的变化。所以正确做法调用UIUtils.enableV2Compatibility(UIUtils.makeV1Observed())，使V1中可以观察属性的变化。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct ArrayCompV2 {
6. @Local arr: Array<number> = UIUtils.enableV2Compatibility(UIUtils.makeV1Observed([1, 2, 3]));

8. build() {
9. Column() {
10. Text(`V2 ${this.arr[0]}`).fontSize(20).onClick(() => {
11. // 点击触发V2变化，且同步给V1 @ObjectLink
12. this.arr[0]++;
13. })
14. ArrayCompV1({ arr: this.arr })
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }

21. @Component
22. struct ArrayCompV1 {
23. @ObjectLink arr: Array<number>;

25. build() {
26. Column() {
27. Text(`V1 ${this.arr[0]}`).fontSize(20).onClick(() => {
28. // 点击触发V1变化，且双向同步回给V2
29. this.arr[0]++;
30. })
31. }
32. }
33. }
```

[StateMixedSceneBuiltTypeV2V1Recommend.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneBuiltTypeV2V1Recommend.ets#L15-L49)

### 传递二维数组（V2->V1）

下面的例子中：

* 使用makeV1Observed将二维数组的内层数组变成V1的状态变量。调用enableV2Compatibility，使其具有V2的观察能力，也避免V1和V2的双重代理。
* 在V1中，使用@ObjectLink接收二维数组的内层数组，因为其为makeV1Observed的返回值，所以点击Button('@ObjectLink push')，会正常响应刷新。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Component
4. struct Item {
5. @ObjectLink itemArr: Array<string>;

7. build() {
8. Row() {
9. ForEach(this.itemArr, (item: string, index: number) => {
10. Text(`${index}: ${item}`)
11. }, (item: string) => item + Math.random())
12. // 新增数组元素
13. Button('@ObjectLink push')
14. .onClick(() => {
15. this.itemArr.push('ObjectLink');
16. })
17. }
18. }
19. }

21. @Entry
22. @ComponentV2
23. struct IndexPage {
24. @Local arr: Array<Array<string>> =
25. UIUtils.enableV2Compatibility(UIUtils.makeV1Observed([UIUtils.makeV1Observed(['apple']),
26. UIUtils.makeV1Observed(['banana']), UIUtils.makeV1Observed(['orange'])]));

28. build() {
29. Column() {
30. ForEach(this.arr, (itemArr: Array<string>) => {
31. Item({ itemArr: itemArr })
32. }, (itemArr: Array<string>) => JSON.stringify(itemArr) + Math.random())
33. Divider()
34. // 数组arr[0]新增元素
35. Button('@Local push two-dimensional array item')
36. .onClick(() => {
37. this.arr[0].push('strawberry');
38. })
39. // 数组arr新增元素
40. Button('@Local push array item')
41. .onClick(() => {
42. this.arr.push(UIUtils.makeV1Observed(['pear']));
43. })
44. // 修改数组项arr[0][0]的值
45. Button('@Local change two-dimensional array first item')
46. .onClick(() => {
47. this.arr[0][0] = 'APPLE';
48. })
49. // 修改数组arr的第一个元素
50. Button('@Local change array first item')
51. .onClick(() => {
52. this.arr[0] = UIUtils.makeV1Observed(['watermelon']);
53. })
54. }
55. }
56. }
```

[StateMixedSceneTwoBitArrayV2V1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneTwoBitArrayV2V1.ets#L15-L71)

### 传递嵌套类型（V2->V1）

下面例子中：

* NestedClassV2中outer调用了UIUtils.enableV2Compatibility，且每一层都是UIUtils.makeV1Observed的返回值，所以outer在V2中有了深度观察的能力。
* V1中仅能观察第一层的变化，所以需要多层自定义组件，且每层都配合使用@ObjectLink来接收，从而实现深度观察能力。

```
1. import { UIUtils } from '@kit.ArkUI';

3. class ArrayItem {
4. public value: number = 0;

6. constructor(value: number) {
7. this.value = value;
8. }
9. }

11. class Inner {
12. public innerValue: string = 'inner';
13. public arr: Array<ArrayItem>;

15. constructor(arr: Array<ArrayItem>) {
16. this.arr = arr;
17. }
18. }

20. class Outer {
21. @Track public outerValue: string = 'out';
22. @Track public inner: Inner;

24. constructor(inner: Inner) {
25. this.inner = inner;
26. }
27. }

29. @Entry
30. @ComponentV2
31. struct NestedClassV2 {
32. // 需保证每一层都是V1的状态变量
33. @Local outer: Outer = UIUtils.enableV2Compatibility(
34. UIUtils.makeV1Observed(new Outer(
35. UIUtils.makeV1Observed(new Inner(UIUtils.makeV1Observed([
36. UIUtils.makeV1Observed(new ArrayItem(1)),
37. UIUtils.makeV1Observed(new ArrayItem(2))
38. ])))
39. )));

41. build() {
42. Column() {
43. Text(`@Local outer.outerValue can update ${this.outer.outerValue}`)
44. .fontSize(20)
45. .onClick(() => {
46. // 可观察第一层的变化
47. this.outer.outerValue += '!';
48. })

50. Text(`@Local outer.inner.innerValue can update ${this.outer.inner.innerValue}`)
51. .fontSize(20)
52. .onClick(() => {
53. // 可观察第二层的变化
54. this.outer.inner.innerValue += '!';
55. })
56. // 将inner传递给@ObjectLink可观察inner属性的变化
57. NestedClassV1ObjectLink({ inner: this.outer.inner })
58. }
59. .height('100%')
60. .width('100%')
61. }
62. }

64. @Component
65. struct NestedClassV1ObjectLink {
66. @ObjectLink inner: Inner;

68. build() {
69. Column() {
70. Text(`@ObjectLink inner.innerValue can update ${this.inner.innerValue}`)
71. .fontSize(20)
72. .onClick(() => {
73. // 可以触发刷新
74. this.inner.innerValue += '!';
75. })
76. NestedClassV1ObjectLinkArray({ arr: this.inner.arr })
77. }
78. }
79. }

81. @Component
82. struct NestedClassV1ObjectLinkArray {
83. @ObjectLink arr: Array<ArrayItem>;

85. build() {
86. Column() {
87. ForEach(this.arr, (item: ArrayItem) => {
88. NestedClassV1ObjectLinkArrayItem({ item: item })
89. }, (item: ArrayItem, index: number) => {
90. return item.value.toString() + index.toString();
91. })

93. Button('@ObjectLink push').onClick(() => {
94. this.arr.push(UIUtils.makeV1Observed(new ArrayItem(20)));
95. })

97. Button('@ObjectLink change the last Item').onClick(() => {
98. // 在NestedClassV1ObjectLinkArrayItem中可以观察最后一个数组项的属性变化
99. this.arr[this.arr.length - 1].value++;
100. })
101. }
102. }
103. }

105. @Component
106. struct NestedClassV1ObjectLinkArrayItem {
107. @ObjectLink item: ArrayItem;

109. build() {
110. Text(`@ObjectLink outer.inner.arr item: ${this.item.value}`)
111. }
112. }
```

[StateMixedSceneNestedTypeV2V1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateRestock/entry/src/main/ets/pages/mixedStateManageV1V2/StateMixedSceneNestedTypeV2V1.ets#L15-L128)
