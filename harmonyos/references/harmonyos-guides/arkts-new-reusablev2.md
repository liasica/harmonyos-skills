---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-reusablev2
title: @ReusableV2装饰器：V2组件复用
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件复用 > @ReusableV2装饰器：V2组件复用
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:04+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:fb9ff1c395eb8bbf9444e58ed651fdd9bf125c0b7f1d0c15e871d7d8f374ac25
---

为了降低反复创建销毁自定义组件带来的性能开销，开发者可以使用@ReusableV2装饰[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件，达成组件复用的效果。

在阅读本文前，建议提前阅读：[@Reusable装饰器：V1组件复用](arkts-reusable.md)。

说明

从API version 18开始，可以使用@ReusableV2装饰@ComponentV2装饰的自定义组件。

从API version 18开始，该装饰器支持在元服务中使用。

## 概述

@ReusableV2用于装饰V2的自定义组件，表明该自定义组件具有被复用的能力：

* @ReusableV2仅能装饰V2的自定义组件，即@ComponentV2装饰的自定义组件。并且仅能将@ReusableV2装饰的自定义组件作为V2自定义组件的子组件使用。
* @ReusableV2同样提供了[aboutToRecycle](../harmonyos-references/ts-custom-component-lifecycle.md#abouttorecycle10)和[aboutToReuse](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoreuse18)的生命周期，在组件被回收时调用aboutToRecycle，在组件被复用时调用aboutToReuse，但与@Reusable不同的是，aboutToReuse没有入参。
* 在回收阶段，会递归地调用所有子组件的aboutToRecycle回调（即使子组件未被标记可复用）；在复用阶段，会递归地调用所有子组件的aboutToReuse回调（即使子组件未被标记可复用）。
* @ReusableV2装饰的自定义组件会在被回收期间保持冻结状态，即无法触发UI刷新、无法触发[@Monitor](arkts-new-monitor.md)回调，与[freezeWhenInactive](arkts-custom-components-freezev2.md)标记位不同的是，在解除冻结状态后，不会触发延后的刷新。
* @ReusableV2装饰的自定义组件会在复用时自动重置组件内状态变量的值、重新计算组件内[@Computed](arkts-new-computed.md)以及与之相关的@Monitor。不建议开发者在aboutToRecycle中更改组件内状态变量，详见[复用前的组件内状态变量重置](arkts-new-reusablev2.md#复用前的组件内状态变量重置)。
* V1和V2的复用组件可在一定规则下混用，详见[使用限制](arkts-new-reusablev2.md#使用限制)第二点。
* 不建议开发者嵌套滥用@ReusableV2装饰器，这可能会导致复用效率降低以及内存开销变大。

## 装饰器说明

| @ReusableV2装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无 |
| 可装饰的组件 | @ComponentV2装饰的自定义组件 |
| 装饰器作用 | 表明该组件可被复用 |

```
1. @ReusableV2 // 装饰ComponentV2的自定义组件
2. @ComponentV2
3. struct ReusableV2Component {
4. @Local message: string = 'Hello World';
5. build () {
6. Column() {
7. Text(this.message)
8. }
9. }
10. }
```

[ReusableV2Component1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/common/ReusableV2Component1.ets#L15-L26)

## 接口说明

reuse、ReuseOptions、ReuseIdCallback的接口说明参考API文档：[复用选项](../harmonyos-references/ts-universal-attributes-reuse.md)。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. build() {
5. Column() {
6. ReusableV2Component()
7. .reuse({ reuseId: () => 'reuseComponent' }) // 使用'reuseComponent'作为reuseId
8. ReusableV2Component()
9. .reuse({ reuseId: () => '' }) // 使用空字符串将默认使用组件名'ReusableV2Component'作为reuseId
10. ReusableV2Component() // 未指定reuseId将默认使用组件名'ReusableV2Component'作为reuseId
11. }
12. }
13. }

15. @ReusableV2
16. @ComponentV2
17. struct ReusableV2Component {
18. build() {
19. }
20. }
```

[ExamplePage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/ExamplePage.ets#L16-L36)

## 使用限制

* 仅能将@ReusableV2装饰的自定义组件作为V2自定义组件的子组件使用。如果在V1的自定义组件中使用V2的复用组件将导致编译期报错，编译期无法校验到的复杂场景下将会有运行时报错。

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Index {
  4. build() {
  5. Column() {
  6. ReusableV2Component() // 正确用法
  7. }
  8. }
  9. }

  11. @ReusableV2
  12. @ComponentV2
  13. struct ReusableV2Component {
  14. build() {
  15. }
  16. }

  18. @Builder
  19. function V2ReusableBuilder() {
  20. ReusableV2Component()
  21. }
  ```

  [UsageRestrictionsPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/UsageRestrictionsPage.ets#L15-L35)
* V1和V2支持部分混用场景。

  下文提到的描述对应关系如下表：

  | 描述 | 对应组件类型 |
  | --- | --- |
  | V1普通组件 | [@Component](arkts-create-custom-components.md#component)装饰的struct。 |
  | V2普通组件 | @ComponentV2装饰的struct。 |
  | V1复用组件 | @Reusable@Component装饰的struct。 |
  | V2复用组件 | @ReusableV2@ComponentV2装饰的struct。 |

  下面的表展示了V1和V2的混用支持关系，每行的含义为第一列作为父组件，能否将后面列的组件作为子组件。

  以第一行V1普通组件为例，可以将V1普通组件、V2普通组件以及V1复用组件作为子组件，但无法将V2复用组件作为子组件。

  | 混用支持关系 | V1普通组件 | V2普通组件 | V1复用组件 | V2复用组件 |
  | --- | --- | --- | --- | --- |
  | V1普通组件 | 支持 | 支持 | 支持 | 不支持，编译报错 |
  | V2普通组件 | 支持 | 支持 | 不支持，编译告警，实际使用子组件不创建 | 支持 |
  | V1复用组件 | 支持 | 支持，需要使用API version 18及以上的SDK，否则会有运行时报错，从API version 23开始，将返回错误码[140113](../harmonyos-references/errorcode-statemanagement.md#section140113-复用componentv2自定义组件但工具链版本过低) | 支持 | 不支持，编译报错 |
  | V2复用组件 | 支持 | 支持 | 不支持，编译报错 | 支持 |

  根据上表，仅支持12种可能的父子关系，不推荐开发者高度嵌套可复用组件，这会造成复用效率降低。
* V2的复用组件当前不支持直接用于[Repeat](../harmonyos-references/ts-rendering-control-repeat.md)的template中，但是可以用在template中的V2自定义组件中。

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Index {
  4. @Local arr: number[] = [1, 2, 3, 4, 5];

  6. build() {
  7. Column() {
  8. List() {
  9. Repeat(this.arr)
  10. .each(() => {
  11. })
  12. .virtualScroll()
  13. .templateId(() => 'a')
  14. .template('a', (ri) => {
  15. ListItem() {
  16. Column() {
  17. NormalV2Component({ val: ri.item }) // 支持普通V2自定义组件下面包含V2复用组件
  18. }
  19. }
  20. })
  21. }
  22. }
  23. }
  24. }

  26. @ComponentV2
  27. struct NormalV2Component {
  28. @Require @Param val: number;

  30. build() {
  31. ReusableV2Component({ val: this.val })
  32. }
  33. }

  35. @Builder
  36. function ReusableV2Builder(param: number) {
  37. ReusableV2Component({ val: param })
  38. }

  40. @ReusableV2
  41. @ComponentV2
  42. struct ReusableV2Component {
  43. @Require @Param val: number;

  45. build() {
  46. Column() {
  47. Text(`val: ${this.val}`)
  48. }
  49. }
  50. }
  ```

  [RepeatTemplatePage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/RepeatTemplatePage.ets#L15-L59)

## 回收与复用的生命周期

@ReusableV2提供了aboutToRecycle以及aboutToReuse的生命周期，当组件被回收时触发aboutToRecycle，当组件被复用时触发aboutToReuse。

以if的使用场景为例：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @Entry
7. @ComponentV2
8. struct Index {
9. @Local condition1: boolean = false;
10. @Local condition2: boolean = true;

12. build() {
13. Column({ space: 10 }) {
14. Button('step1. appear')
15. .width('60%')
16. .onClick(() => {
17. this.condition1 = true;
18. })
19. Button('step2. recycle')
20. .width('60%')
21. .onClick(() => {
22. this.condition2 = false;
23. })
24. Button('step3. reuse')
25. .width('60%')
26. .onClick(() => {
27. this.condition2 = true;
28. })
29. Button('step4. disappear')
30. .width('60%')
31. .onClick(() => {
32. this.condition1 = false;
33. })
34. if (this.condition1) {
35. NormalV2Component({ condition: this.condition2 })
36. }
37. }
38. .width('100%')
39. }
40. }

42. @ComponentV2
43. struct NormalV2Component {
44. @Require @Param condition: boolean;

46. build() {
47. if (this.condition) {
48. ReusableV2Component()
49. }
50. }
51. }

53. @ReusableV2
54. @ComponentV2
55. struct ReusableV2Component {
56. aboutToAppear() {
57. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToAppear called'); // 组件创建时调用
58. }

60. aboutToDisappear() {
61. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToDisappear called'); // 组件销毁时调用
62. }

64. aboutToRecycle() {
65. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToRecycle called'); // 组件回收时调用
66. }

68. aboutToReuse() {
69. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToReuse called'); // 组件复用时调用
70. }

72. build() {
73. Column() {
74. Text('ReusableV2Component')
75. }
76. }
77. }
```

[AboutToRecyclePage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/AboutToRecyclePage.ets#L15-L80)

建议按下面顺序进行操作：

1. 点击step1. appear，此时condition1变为true，Index中的if组件切换分支，创建出NormalV2Component，由于condition2初始值为true，所以NormalV2Component中的if条件满足，尝试创建ReusableV2Component。此时复用池中无元素，因此会创建ReusableV2Component，并回调aboutToAppear的方法，输出ReusableV2Component aboutToAppear called的日志。
2. 点击step2. recycle，此时condition2变为false，通过@Param同步给NormalV2Component，if条件切换，由于ReusableV2Component使用了@ReusableV2，因此会将该组件回收至复用池而不是销毁，回调aboutToRecycle的方法并输出ReusableV2Component aboutToRecycle called的日志。
3. 点击step3. reuse，此时condition2变为true，通过@Param传递给NormalV2Component，if条件切换，由于ReusableV2Component使用了@ReusableV2，因此在创建该组件时尝试去复用池中寻找。此时复用池中有第二步放入的组件实例，因此从复用池中取出复用，回调aboutToReuse方法并输出ReusableV2Component aboutToReuse called的日志。
4. 点击step4. disappear，此时condition1变为false，Index组件中的if组件切换分支，销毁NormalV2Component，此时ReusableV2Component因为父组件销毁，所以会被一起销毁，回调aboutToDisappear的方法并输出ReusableV2Component aboutToDisappear called的日志。

倘若该复用组件下有子组件时，会在回收和复用时递归调用子组件的aboutToRecycle和aboutToReuse（与子组件是否被标记复用无关），直到遍历完所有的孩子组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/B35wy1WWTI6lwF7kcoUuXQ/zh-cn_image_0000002558604390.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=9BB17743B1601ACEC496ACA41AF1D1497EAAEC56972E391115844B0AA7E6FE2B)

## 复用阶段的冻结

在之前的复用中，V1组件在复用池中仍能响应更新，这会对性能带来一定的负面影响，需要开发者使用组件冻结能力，才能够使V1组件在复用池中时不响应更新。针对这一点，V2组件在复用时将会被自动冻结，不会响应在回收期间发生的变化。这一个期间包括aboutToRecycle，即aboutToRecycle中的修改不会刷新到UI上，也不会触发@Computed以及@Monitor。冻结状态将持续到aboutToReuse前，即aboutToReuse及之后的变量更改，才会正常触发UI刷新、@Computed重新计算以及@Monitor的调用。

以if的使用场景为例：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @ObservedV2
7. class Info {
8. @Trace public age: number = 25;
9. }

11. const info: Info = new Info();

13. @Entry
14. @ComponentV2
15. struct Index {
16. @Local condition: boolean = true;

18. build() {
19. Column({ space: 10 }) {
20. Button('Reuse/Recycle')
21. .width('60%')
22. .onClick(() => {
23. this.condition = !this.condition;
24. })
25. Button('Change value')
26. .width('60%')
27. .onClick(() => {
28. info.age++;
29. })
30. if (this.condition) {
31. ReusableV2Component()
32. }
33. }
34. .width('100%')
35. }
36. }

38. @ReusableV2
39. @ComponentV2
40. struct ReusableV2Component {
41. @Local info: Info = info; // 仅做演示使用，并不建议@Local赋值全局变量

43. @Monitor('info.age')
44. onValChange() {
45. hilog.info(DOMAIN, TAG, 'info.age change');
46. }

48. aboutToRecycle() {
49. hilog.info(DOMAIN, TAG, 'aboutToRecycle');
50. this.info.age++;
51. }

53. aboutToReuse() {
54. hilog.info(DOMAIN, TAG, 'aboutToReuse');
55. this.info.age++;
56. }

58. onRender(): string {
59. hilog.info(DOMAIN, TAG, 'info.age onRender');
60. return this.info.age.toString();
61. }

63. build() {
64. Column() {
65. Text(this.onRender())
66. }
67. }
68. }
```

[ConditionPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/ConditionPage.ets#L15-L72)

建议按如下步骤进行操作：

1. 点击Change value按钮，可以观察到UI变化，@Monitor触发并输出日志info.age change以及info.age onRender，说明此时能够正常监听到变化以及触发UI刷新。
2. 点击Reuse/Recycle按钮，此时调用aboutToRecycle回调并输出aboutToRecycle的日志，但@Monitor不被触发，且onRender方法不被回调。
3. 点击Change value按钮，UI无变化，@Monitor不触发且onRender方法不被回调。
4. 点击Reuse/Recycle按钮，此时调用aboutToReuse回调并输出aboutToReuse的日志，@Monitor触发并输出日志info.age change且onRender方法回调输出info.age onRender，UI发生变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/YYIJzmClT4C4mjtRkOCQ2g/zh-cn_image_0000002589323915.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=68F27217B9AA1F74C5F8551757B5532454CEF52A46A8659BFFB377C688808FE9)

如果去掉aboutToReuse方法中的自增操作，则上述第四步不会触发@Monitor回调。

在复杂的混用场景中，是否冻结的规则可以总结为以下两点：

1. V1的组件根据是否开启组件冻结freezeWhenInactive决定。
2. V2的组件自动被冻结。

## 复用前的组件内状态变量重置

与@Reusable不同的是，@ReusableV2在复用前会重置组件中的状态变量以及相关的@Computed、@Monitor的内容。在复用的过程当中，所有的V2自定义组件，无论是否被标记了@ReusableV2，都会经历这一个重置过程。

重置会按照变量在组件中定义的顺序按照下面的规则依次进行：

| 装饰器 | 重置方法 |
| --- | --- |
| [@Local](arkts-new-local.md) | 直接使用定义时的初始值重新赋值。 |
| [@Param](arkts-new-param.md) | 如果有外部传入则使用外部传入值重新赋值，否则用本地初始值重新赋值。注意：@Once装饰的变量同样会被重置初始化一次。 |
| [@Event](arkts-new-event.md) | 如果有外部传入则使用外部传入值重新赋值，否则用本地初始值重新赋值。如果本地没有初始值，则生成默认的空实现。 |
| [@Provider](arkts-new-provider-and-consumer.md) | 直接使用定义时的初始值重新赋值。 |
| [@Consumer](arkts-new-provider-and-consumer.md) | 如果有对应的@Provider则直接使用@Provider对应的值，否则使用本地初始值重新赋值。 |
| @Computed | 使用当前最新的值重新计算一次，如果使用到的变量还未被重置，将会使用重置前的值，因此推荐开发者将@Computed定义在所使用的变量之后。 |
| @Monitor | 在上述所有变量重置完成之后触发。重置过程中产生的变量变化不会触发@Monitor回调，仅更新IMonitorValue中的before值。重置过程中不产生变化的赋值不会触发@Monitor的重置。 |
| 常量 | 包括readonly的常量，不重置。 |

下面的例子展示了重置的一些效果：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @ObservedV2
7. class Info {
8. @Trace public age: number;

10. constructor(age: number) {
11. this.age = age;
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct Index {
18. @Local local: number = 0;
19. @Provider('inherit') inheritProvider: number = 100;
20. @Local condition: boolean = true;

22. build() {
23. Column({ space: 10 }) {
24. Button('Recycle/Reuse')
25. .onClick(() => {
26. this.condition = !this.condition;
27. })
28. Column({ space: 10 }) {
29. Text('Variables of parent component')
30. Text(`local: ${this.local}`)
31. .onClick(() => {
32. this.local++;
33. })
34. Text(`inheritProvider: ${this.inheritProvider}`)
35. .onClick(() => {
36. this.inheritProvider++;
37. })
38. }
39. .width('80%')
40. .borderWidth(2)

42. if (this.condition) {
43. ReusableV2Component({
44. paramOut: this.local,
45. paramOnce: this.local,
46. changeParam: () => {
47. this.local++;
48. }
49. })
50. }
51. }
52. .width('100%')
53. }
54. }

56. @ReusableV2
57. @ComponentV2
58. struct ReusableV2Component {
59. @Local val: number = 0;
60. @Local info: Info = new Info(25);
61. @Param paramLocal: number = 1;
62. @Require @Param paramOut: number;
63. @Require @Param @Once paramOnce: number;
64. @Event changeParam: () => void;
65. @Provider('selfProvider') selfProvider: number = 0;
66. @Consumer('inherit') inheritConsumer: number = 0;
67. @Consumer('selfConsumer') selfConsumer: number = 0;
68. noDecoVariable: number = 0; // 未加装饰器，被视作常量
69. noDecoInfo: Info = new Info(30); // 未加装饰器，被视作常量
70. readonly readOnlyVariable: number = 0; // readonly常量

72. @Computed
73. get plusParam() {
74. return this.paramLocal + this.paramOut + this.paramOnce;
75. }

77. @Monitor('val')
78. onValChange(monitor: IMonitor) {
79. hilog.info(DOMAIN, TAG, `val change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
80. }

82. @Monitor('plusParam')
83. onPlusParamChange(monitor: IMonitor) {
84. hilog.info(DOMAIN, TAG, `plusParam change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
85. }

87. build() {
88. Column({ space: 10 }) {
89. Column({ space: 10 }) {
90. Text('Variables reset to local initial values')
91. Text(`val: ${this.val}`)
92. .onClick(() => {
93. this.val++;
94. })
95. Text(`info.age: ${this.info.age}`)
96. .onClick(() => {
97. this.info.age++;
98. })
99. Text(`paramLocal: ${this.paramLocal}`)
100. .onClick(() => {
101. /* 无外部传入的Local无法本地修改 */
102. })
103. Text(`selfProvider: ${this.selfProvider}`)
104. .onClick(() => {
105. this.selfProvider++;
106. })
107. Text(`selfConsumer: ${this.selfConsumer}`)
108. .onClick(() => {
109. this.selfConsumer++;
110. })
111. }
112. .width('80%')
113. .borderWidth(2)

115. Column({ space: 10 }) {
116. Text('Reset to an external variable')
117. Text(`paramOut: ${this.paramOut}`)
118. .onClick(() => {
119. this.changeParam();
120. })
121. Text(`paramOnce: ${this.paramOnce}`)
122. .onClick(() => {
123. this.paramOnce++;
124. })
125. }
126. .width('80%')
127. .borderWidth(2)

129. Column({ space: 10 }) {
130. Text('Depending on the parent component')
131. Text(`inheritConsumer: ${this.inheritConsumer}`)
132. .onClick(() => {
133. this.inheritConsumer++;
134. })
135. Text(`plusParam: ${this.plusParam}`)
136. }
137. .width('80%')
138. .borderWidth(2)

140. Column({ space: 10 }) {
141. Text('Not reset')
142. Text(`noDecoVariable: ${this.noDecoVariable}`)
143. Text(`noDecoInfo.age: ${this.noDecoInfo.age}`)
144. .onClick(() => {
145. this.noDecoInfo.age++;
146. }) // 能够触发刷新但是复用时不会被重置
147. Text(`readOnlyVariable: ${this.readOnlyVariable}`)
148. }
149. .width('80%')
150. .borderWidth(2)
151. }
152. .width('100%')
153. }
154. }
```

[ComputedPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/ComputedPage.ets#L15-L147)

开发者可以尝试点击各个变量，并点击Recycle/Reuse按钮查看复用后的重置情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/IgOblbwiRpeorActmCPuIg/zh-cn_image_0000002589243855.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=663604B8892E650FDD6C95BB5ACEB44FB5500323BFBA99F5F85396EDCABDA65B)

需要注意的是，上面的例子中noDecoInfo未被重置，如果存在监听noDecoInfo.age的@Monitor，因为noDecoInfo本身未产生变化，所以该@Monitor也不会被重置，因此在后续第一次更改noDecoInfo.age时，IMonitorValue的before值将不会被重置，仍是复用前的值。

将上面的例子简化可得下面的例子：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @ObservedV2
7. class Info {
8. @Trace public age: number;

10. constructor(age: number) {
11. this.age = age;
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct Index {
18. @Local condition: boolean = true;

20. build() {
21. Column({ space: 10 }) {
22. Button('Recycle/Reuse')
23. .width('60%')
24. .onClick(() => {
25. this.condition = !this.condition;
26. })
27. if (this.condition) {
28. ReusableV2Component()
29. }
30. }
31. .width('100%')
32. }
33. }

35. @ReusableV2
36. @ComponentV2
37. struct ReusableV2Component {
38. noDecoInfo: Info = new Info(30); // 未加装饰器，被视作常量

40. @Monitor('noDecoInfo.age')
41. onAgeChange(monitor: IMonitor) {
42. hilog.info(DOMAIN, TAG, `age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
43. }

45. aboutToRecycle() {
46. this.noDecoInfo.age = 25;
47. }

49. aboutToReuse() {
50. this.noDecoInfo.age = 35;
51. }

53. build() {
54. Column() {
55. Column() {
56. Text(`noDecoInfo.age: ${this.noDecoInfo.age}`)
57. .onClick(() => {
58. this.noDecoInfo.age++;
59. }) // 能够触发刷新但是不会被重置
60. }
61. }
62. }
63. }
```

[IMonitorValuePage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/IMonitorValuePage.ets#L15-L69)

建议按照下列步骤进行操作：

1. 点击noDecoInfo.age: 30，UI刷新为noDecoInfo.age: 31，@Monitor触发并输出日志age change from 30 to 31。
2. 点击Recycle/Reuse两次，UI刷新为noDecoInfo.age: 35，@Monitor触发并输出日志age change from 31 to 35。
3. 点击noDecoInfo.age: 35，UI刷新为noDecoInfo.age: 36，@Monitor触发并输出日志age change from 35 to 36。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/IMYJosT8Ty6z1iYmgHAb1g/zh-cn_image_0000002558764048.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=C678D2F85122014F980BCFD98843318C6B79AA0F8B3019C42400071EBB25DA16)

由于冻结机制的存在，在aboutToRecycle中赋值不会被@Monitor观察到。而在经历完变量重置后，变量又会被赋予新的值，因此对于组件内状态变量来说，在aboutToRecycle中赋值不会有明显的效果；而常量（例如上面的noDecoInfo）由于冻结机制的存在，在aboutToRecycle中更改age也不会被观察到，并且因为不会被重置，所以相关的@Monitor也不会被重置，即这里的age值本身未被重置，也就不会重置与之绑定的@Monitor。最终表现出来的现象即：第二步回调的@Monitor中，monitor.value()?.before得到的值为31，而非age的初始值30。

针对这一现象，推荐开发者在复用的场景减少使用类似的常量对象包含[@Trace](arkts-new-observedv2-and-trace.md)属性的写法，以确保复用场景的功能符合预期。

## 使用场景

### 在if组件中使用

通过改变if组件的条件可以控制组件回收/复用。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @Entry
7. @ComponentV2
8. struct Index {
9. @Local condition: boolean = true;

11. build() {
12. Column({ space: 10 }) {
13. Button('Recycle/Reuse')
14. .width('60%')
15. .onClick(() => {
16. this.condition = !this.condition;
17. }) // 点击切换回收/复用状态
18. if (this.condition) {
19. ReusableV2Component()
20. }
21. }
22. .width('100%')
23. }
24. }

26. @ReusableV2
27. @ComponentV2
28. struct ReusableV2Component {
29. @Local message: string = 'Hello World';

31. aboutToRecycle() {
32. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToRecycle'); // 回收时被调用
33. }

35. aboutToReuse() {
36. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToReuse'); // 复用时被调用
37. }

39. build() {
40. Column() {
41. Text(this.message)
42. }
43. }
44. }
```

[ComponentIfPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/ComponentIfPage.ets#L15-L53)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/vJPyblU8RgC9JcNia8rkUw/zh-cn_image_0000002558604392.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=BF8AB3FC973372462352D5182A59C9EFFA1AF407D11110DB492B233A06025BE7)

### 在Repeat组件中使用

Repeat组件懒加载场景中，将会优先使用Repeat组件的缓存池，正常滑动场景、更新场景不涉及组件的回收与复用。当Repeat的缓存池需要扩充时将会向自定义组件要求新的子组件，此时如果复用池中有可复用的节点，将会进行复用。

下面的例子中，先点击Change condition会让3个节点进入复用池，而后向下滑动List组件时，可以观察到日志输出ReusableV2Component aboutToReuse，表明Repeat可以使用自定义组件的复用池填充自己的缓存池。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @Entry
7. @ComponentV2
8. struct Index {
9. @Local condition: boolean = true;
10. @Local simpleList: number[] = [];

12. aboutToAppear(): void {
13. for (let i = 0; i < 100; i++) {
14. this.simpleList.push(i);
15. }
16. }

18. build() {
19. Column() {
20. Button('Change condition')
21. .onClick(() => {
22. this.condition = !this.condition;
23. })
24. if (this.condition) {
25. // 此处仅做演示使用，让复用池中填充3个组件
26. ReusableV2Component({ num: 0 })
27. ReusableV2Component({ num: 0 })
28. ReusableV2Component({ num: 0 })
29. }
30. List({ space: 10 }) {
31. Repeat(this.simpleList)
32. .virtualScroll()
33. .each((obj: RepeatItem<number>) => {
34. ListItem() {
35. Column() {
36. ReusableV2Component({ num: obj.item })
37. }
38. }
39. .width('100%')
40. })
41. }.height('50%')
42. .cachedCount(2)
43. }
44. }
45. }

47. @ReusableV2
48. @ComponentV2
49. struct ReusableV2Component {
50. @Require @Param num: number;

52. aboutToAppear() {
53. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToAppear');
54. }

56. aboutToRecycle() {
57. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToRecycle');
58. }

60. aboutToReuse() {
61. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToReuse');
62. }

64. build() {
65. Column() {
66. Text(`${this.num}`).fontSize(50)
67. }
68. }
69. }
```

[RepeatPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/RepeatPage.ets#L15-L77)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/FbqS0JnRSwC39ekDxyZulQ/zh-cn_image_0000002589323917.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=A412CB29DB8BA2F6C718451AB0B671BBA164B9026DA0FDB8E231C19A93F9EB9D)

### 在Repeat组件非懒加载场景的each属性中使用

Repeat组件非懒加载场景中，会在删除/创建子树时触发回收/复用。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @Entry
7. @ComponentV2
8. struct Index {
9. @Local simpleList: number[] = [1, 2, 3, 4, 5];
10. @Local condition: boolean = true;

12. build() {
13. Column({ space: 10 }) {
14. // 点击Button切换condition，删除/创建ReusableV2Component
15. Button('Delete/Create Repeat')
16. .width('60%')
17. .onClick(() => {
18. this.condition = !this.condition;
19. })
20. Button('Add element')
21. .width('60%')
22. .onClick(() => {
23. this.simpleList.push(this.simpleList.length + 1);
24. })
25. Button('Delete element')
26. .width('60%')
27. .onClick(() => {
28. this.simpleList.pop();
29. })
30. Button('Change element')
31. .width('60%')
32. .onClick(() => {
33. this.simpleList[0]++;
34. })
35. if (this.condition) {
36. List({ space: 10 }) {
37. Repeat(this.simpleList)
38. .each((obj: RepeatItem<number>) => {
39. ListItem() {
40. Column() {
41. ReusableV2Component({ num: obj.item })
42. }
43. .width('100%')
44. }
45. })
46. }
47. }
48. }
49. .width('100%')
50. }
51. }

53. @ReusableV2
54. @ComponentV2
55. struct ReusableV2Component {
56. @Require @Param num: number;

58. aboutToAppear() {
59. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToAppear');
60. }

62. aboutToRecycle() {
63. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToRecycle');
64. }

66. aboutToReuse() {
67. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToReuse');
68. }

70. build() {
71. Column() {
72. Text(`${this.num}`)
73. }
74. }
75. }
```

[ComponentEachPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/ComponentEachPage.ets#L15-L78)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/De_HRjFVRdWI6xBgR03bjg/zh-cn_image_0000002589243857.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=B5F02635E0F15EABB9168E17700A70EB602F52F41A434A4AAE8B2303283E9CAA)

### 在ForEach组件中使用

说明

推荐开发者使用Repeat组件的非懒加载场景代替[ForEach](../harmonyos-references/ts-rendering-control-foreach.md)组件。

下面的例子中使用了ForEach组件渲染了数个可复用组件，由于每次点击Click to change按钮时key值都会发生变化，因此从第二次点击开始都会触发回收与复用（由于ForEach先判断有无可复用节点时复用池仍未初始化，因此第一次点击会创建新的节点，而后初始化复用池同时回收节点）。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. @Entry
7. @ComponentV2
8. struct Index {
9. @Local simpleList: number[] = [0, 1, 2, 3, 4, 5];

11. build() {
12. Column() {
13. ForEach(this.simpleList, (num: number, index) => {
14. Row() {
15. Button('Click to change')
16. .margin({ right: 10 })
17. .onClick(() => {
18. this.simpleList[index]++;
19. })
20. ReusableV2Component({ num: num })
21. }
22. .margin({ bottom: 10 })
23. }) // 每次修改完key发生变化
24. }
25. }
26. }

28. @ReusableV2
29. @ComponentV2
30. struct ReusableV2Component {
31. @Require @Param num: number;

33. aboutToAppear() {
34. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToAppear', this.num); // 创建时触发
35. }

37. aboutToRecycle() {
38. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToRecycle', this.num); // 回收时触发
39. }

41. aboutToReuse() {
42. hilog.info(DOMAIN, TAG, 'ReusableV2Component aboutToReuse', this.num); // 复用时触发
43. }

45. build() {
46. Column() {
47. Text(`child: ${this.num}`)
48. }
49. }
50. }
```

[ComponentForEachPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/ComponentForEachPage.ets#L15-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/VhiNOr68RrWE_u71su6T-w/zh-cn_image_0000002558764050.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=80172BEE5C6A259485EB986C0088BB8B3AAD517AD5A43BE6074A47ABE922AA18)

### 在LazyForEach组件中使用

说明

推荐开发者使用Repeat组件的懒加载场景代替[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)组件。

下面的例子中使用了LazyForEach渲染了数个可复用组件，在滑动时可以先观察到组件创建，直到预加载节点全部创建完成之后，再滑动则触发复用和回收。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Reusablev2]';
4. const DOMAIN = 0xF811;

6. class BasicDataSource implements IDataSource {
7. private listeners: DataChangeListener[] = [];
8. private originDataArray: StringData[] = [];

10. public totalCount(): number {
11. return 0;
12. }

14. public getData(index: number): StringData {
15. return this.originDataArray[index];
16. }

18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. hilog.info(DOMAIN, TAG, 'add listener');
21. this.listeners.push(listener);
22. }
23. }

25. unregisterDataChangeListener(listener: DataChangeListener): void {
26. const pos = this.listeners.indexOf(listener);
27. if (pos >= 0) {
28. hilog.info(DOMAIN, TAG, 'remove listener');
29. this.listeners.splice(pos, 1);
30. }
31. }

33. notifyDataReload(): void {
34. this.listeners.forEach(listener => {
35. listener.onDataReloaded();
36. });
37. }

39. notifyDataAdd(index: number): void {
40. this.listeners.forEach(listener => {
41. listener.onDataAdd(index);
42. });
43. }

45. notifyDataChange(index: number): void {
46. this.listeners.forEach(listener => {
47. listener.onDataChange(index);
48. });
49. }

51. notifyDataDelete(index: number): void {
52. this.listeners.forEach(listener => {
53. listener.onDataDelete(index);
54. });
55. }

57. notifyDataMove(from: number, to: number): void {
58. this.listeners.forEach(listener => {
59. listener.onDataMove(from, to);
60. });
61. }

63. notifyDatasetChange(operations: DataOperation[]): void {
64. this.listeners.forEach(listener => {
65. listener.onDatasetChange(operations);
66. });
67. }
68. }

70. class MyDataSource extends BasicDataSource {
71. private dataArray: StringData[] = [];

73. public totalCount(): number {
74. return this.dataArray.length;
75. }

77. public getData(index: number): StringData {
78. return this.dataArray[index];
79. }

81. public addData(index: number, data: StringData): void {
82. this.dataArray.splice(index, 0, data);
83. this.notifyDataAdd(index);
84. }

86. public pushData(data: StringData): void {
87. this.dataArray.push(data);
88. this.notifyDataAdd(this.dataArray.length - 1);
89. }
90. }

92. @ObservedV2
93. class StringData {
94. @Trace message: string;

96. constructor(message: string) {
97. this.message = message;
98. }
99. }

101. @Entry
102. @ComponentV2
103. struct Index {
104. data: MyDataSource = new MyDataSource(); // 数据源

106. aboutToAppear() {
107. for (let i = 0; i <= 200; i++) {
108. this.data.pushData(new StringData('Hello' + i));
109. }
110. }

112. build() {
113. List({ space: 3 }) {
114. LazyForEach(this.data, (item: StringData, index: number) => {
115. ListItem() {
116. Column() {
117. Text(item.message)
118. ChildComponent({ data: item.message })
119. .onClick(() => {
120. item.message += '!'; // message为@Trace装饰的变量，可观察变化
121. })
122. }
123. }
124. })
125. }.cachedCount(5)
126. }
127. }

129. @ReusableV2
130. @ComponentV2
131. struct ChildComponent {
132. @Param @Require data: string;

134. aboutToAppear(): void {
135. hilog.info(DOMAIN, TAG, 'ChildComponent aboutToAppear', this.data);
136. }

138. aboutToDisappear(): void {
139. hilog.info(DOMAIN, TAG, 'ChildComponent aboutToDisappear', this.data);
140. }

142. aboutToReuse(): void {
143. hilog.info(DOMAIN, TAG, 'ChildComponent aboutToReuse', this.data); // 复用时触发
144. }

146. aboutToRecycle(): void {
147. hilog.info(DOMAIN, TAG, 'ChildComponent aboutToRecycle', this.data); // 回收时触发
148. }

150. build() {
151. Row() {
152. Text(this.data).fontSize(50)
153. }
154. }
155. }
```

[LazyForEachPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableV2/entry/src/main/ets/view/LazyForEachPage.ets#L15-L164)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/8_-tdgj6RB214UcZnXjo7A/zh-cn_image_0000002558604394.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=18D273732060155F73EE12BC8416CE90EF0B5B0F33E57A78CBA33930C861EBC7)
