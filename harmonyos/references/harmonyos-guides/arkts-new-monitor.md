---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor
title: @Monitor装饰器：状态变量修改异步监听
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理数据对象的状态 > @Monitor装饰器：状态变量修改异步监听
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:19+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2feb4739109d93b5f83ecfb1c4f9a3b1a64411800f47cdd1557890e194b00609
---

为了增强状态管理框架对状态变量变化的监听能力，开发者可以使用@Monitor装饰器对状态变量进行监听。

@Monitor提供了对V2状态变量的监听。在阅读本文档前，建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)，[@ObservedV2和@Trace](arkts-new-observedv2-and-trace.md)，[@Local](arkts-new-local.md)。

说明

@Monitor装饰器从API version 12开始支持。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Monitor装饰器用于监听状态变量修改，使得状态变量具有深度监听的能力：

* @Monitor装饰器支持在@ComponentV2装饰的自定义组件中使用，未被状态变量装饰器[@Local](arkts-new-local.md)、[@Param](arkts-new-param.md)、[@Provider](arkts-new-provider-and-consumer.md)、[@Consumer](arkts-new-provider-and-consumer.md)、[@Computed](arkts-new-computed.md)装饰的变量无法被@Monitor监听到变化。
* @Monitor装饰器支持在类中与[@ObservedV2、@Trace](arkts-new-observedv2-and-trace.md)配合使用，不允许在未被@ObservedV2装饰的类中使用@Monitor装饰器。未被@Trace装饰的属性无法被@Monitor监听到变化。
* 当观测的属性变化时，@Monitor装饰器定义的回调方法将被调用。判断属性是否变化使用的是严格相等（===），当严格相等判断的结果是false（即不相等）的情况下，就会触发@Monitor的回调。当在一次事件中多次改变同一个属性时，将会使用初始值和最终值进行比较以判断是否变化。
* 单个@Monitor装饰器能够同时监听多个属性的变化，当这些属性在一次事件中共同变化时，只会触发一次@Monitor的回调方法。
* @Monitor装饰器具有深度监听的能力，能够监听嵌套类、多维数组、对象数组中指定项的变化。对于嵌套类、对象数组中成员属性变化的监听要求该类被@ObservedV2装饰且该属性被@Trace装饰。
* 当@Monitor监听整个数组时，更改数组的某一项不会被监听到。无法监听内置类型（Array、Map、Date、Set）的API调用引起的变化。
* 在继承类场景中，可以在父子组件中对同一个属性分别定义@Monitor进行监听，当属性变化时，父子组件中定义的@Monitor回调均会被调用。
* 和[@Watch装饰器](arkts-watch.md)类似，开发者需要自己定义回调函数，区别在于@Watch装饰器将函数名作为参数，而@Monitor直接装饰回调函数。@Monitor与@Watch的对比可以查看[@Monitor与@Watch的对比](arkts-new-monitor.md#monitor与watch对比)。

## 状态管理V1版本@Watch装饰器的局限性

现有状态管理V1版本无法实现对对象、数组中某一单个属性或数组项变化的监听，且无法获取变化之前的值。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Observed
4. class Info {
5. public name: string = 'Tom';
6. public age: number = 25;
7. }

9. @Entry
10. @Component
11. struct Index {
12. @State @Watch('onInfoChange') info: Info = new Info();
13. @State @Watch('onNumArrChange') numArr: number[] = [1, 2, 3, 4, 5];

15. onInfoChange() {
16. hilog.info(0xFF00, 'testTag', '%{public}s', `info after change name: ${this.info.name}, age: ${this.info.age} `);
17. }

19. onNumArrChange() {
20. hilog.info(0xFF00, 'testTag', '%{public}s', `numArr after change ${this.numArr}`);
21. }

23. build() {
24. Row() {
25. Column() {
26. // 对象、数组中某一单个属性或数组项变化，不会触发UI刷新
27. Button('change info name')
28. .onClick(() => {
29. this.info.name = 'Jack';
30. })
31. Button('change info age')
32. .onClick(() => {
33. this.info.age = 30;
34. })
35. Button('change numArr[2]')
36. .onClick(() => {
37. this.numArr[2] = 5;
38. })
39. Button('change numArr[3]')
40. .onClick(() => {
41. this.numArr[3] = 6;
42. })
43. }
44. .width('100%')
45. }
46. .height('100%')
47. }
48. }
```

[WatchDecoratorLimitationsV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/WatchDecoratorLimitationsV1.ets#L15-L63)

上述代码中，点击"change info name"更改info中的name属性或点击"change info age"更改age时，均会触发info注册的@Watch回调。点击"change numArr[2]"更改numArr中的第3个元素或点击"change numArr[3]"更改第4个元素时，均会触发numArr注册的@Watch回调。在这两个回调中，由于无法获取数据更改前的值，在业务逻辑更加复杂的场景下，无法准确知道是哪一个属性或元素发生了改变从而触发了@Watch事件，这不便于开发者对变量的更改进行准确监听。因此推出@Monitor装饰器实现对对象、数组中某一单个属性或数组项变化的监听，并且能够获取到变化之前的值。

## 装饰器说明

| @Monitor属性装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 字符串类型的对象属性名。可同时监听多个对象属性，每个属性以逗号隔开，例如@Monitor('prop1', 'prop2')。可监听深层的属性变化，如多维数组中的某一个元素，嵌套对象或对象数组中的某一个属性。详见[监听变化](arkts-new-monitor.md#监听变化)。 |
| 装饰对象 | @Monitor装饰成员方法。当监听的属性发生变化时，会触发该回调方法。该回调方法以[IMonitor类型](../harmonyos-references/ts-state-management-watch-monitor.md#imonitor12)的变量作为参数，开发者可以从该参数中获取变化前后的相关信息。 |

## 接口说明

IMonitor类型和IMonitorValue<T>类型的接口说明参考API文档：[状态变量变化监听](../harmonyos-references/ts-state-management-watch-monitor.md)。

## 监听变化

### 在@ComponentV2装饰的自定义组件中使用@Monitor

使用@Monitor监听的状态变量发生变化时，会触发@Monitor的回调方法。

* @Monitor监听的变量需要被@Local、@Param、@Provider、@Consumer、@Computed装饰，未被状态变量装饰器装饰的变量在变化时无法被监听。@Monitor可以同时监听多个状态变量，这些变量名之间用","隔开。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @Entry
  4. @ComponentV2
  5. struct Index {
  6. @Local message: string = 'Hello World';
  7. @Local name: string = 'Tom';
  8. @Local age: number = 24;

  10. @Monitor('message', 'name')
  11. onStrChange(monitor: IMonitor) {
  12. monitor.dirty.forEach((path: string) => {
  13. hilog.info(0xFF00, 'testTag', '%{public}s',
  14. `${path} changed from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  15. });
  16. }

  18. build() {
  19. Column() {
  20. // 点击Button更新message和name，触发onStrChange回调
  21. Button('change string')
  22. .onClick(() => {
  23. this.message += '!';
  24. this.name = 'Jack';
  25. })
  26. }
  27. }
  28. }
  ```

  [MonitorDecoratorMultiWatchCompV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorMultiWatchCompV2.ets#L15-L43)
* @Monitor监听的状态变量为类对象时，仅能监听对象整体的变化。监听类属性的变化需要类属性被@Trace装饰。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. class Info {
  4. public name: string;
  5. public age: number;

  7. constructor(name: string, age: number) {
  8. this.name = name;
  9. this.age = age;
  10. }
  11. }

  13. @Entry
  14. @ComponentV2
  15. struct Index {
  16. @Local info: Info = new Info('Tom', 25);

  18. @Monitor('info')
  19. infoChange(monitor: IMonitor) {
  20. hilog.info(0xFF00, 'testTag', '%{public}s', `info change`);
  21. }

  23. @Monitor('info.name')
  24. infoPropertyChange(monitor: IMonitor) {
  25. hilog.info(0xFF00, 'testTag', '%{public}s', `info name change`);
  26. }

  28. build() {
  29. Column() {
  30. Text(`name: ${this.info.name}, age: ${this.info.age}`)
  31. Button('change info')
  32. .onClick(() => {
  33. this.info = new Info('Lucy', 18); // 能够监听到
  34. })
  35. Button('change info.name')
  36. .onClick(() => {
  37. this.info.name = 'Jack'; // 监听不到
  38. })
  39. }
  40. }
  41. }
  ```

  [MonitorDecoratorObjectTraceCompV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorObjectTraceCompV2.ets#L15-L57)

### 在@ObservedV2装饰的类中使用@Monitor

使用@Monitor监听的属性发生变化时，会触发@Monitor的回调方法。

* @Monitor监听的对象属性需要被@Trace装饰，未被@Trace装饰的属性的变化无法被监听。@Monitor可以同时监听多个属性，这些属性之间用","隔开。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public name: string = 'Tom';
  6. @Trace public region: string = 'North';
  7. @Trace public job: string = 'Teacher';
  8. public age: number = 25;

  10. // name被@Trace装饰，能够监听变化
  11. @Monitor('name')
  12. onNameChange(monitor: IMonitor) {
  13. hilog.info(0xFF00, 'testTag', '%{public}s',
  14. `name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  15. }

  17. // age未被@Trace装饰，不能监听变化
  18. @Monitor('age')
  19. onAgeChange(monitor: IMonitor) {
  20. hilog.info(0xFF00, 'testTag', '%{public}s',
  21. `age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  22. }

  24. // region与job均被@Trace装饰，能够监听变化
  25. @Monitor('region', 'job')
  26. onChange(monitor: IMonitor) {
  27. monitor.dirty.forEach((path: string) => {
  28. hilog.info(0xFF00, 'testTag', '%{public}s',
  29. `${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  30. })
  31. }
  32. }

  34. @Entry
  35. @ComponentV2
  36. struct Index {
  37. info: Info = new Info();

  39. build() {
  40. Column() {
  41. Button('change name')
  42. .onClick(() => {
  43. this.info.name = 'Jack'; // 能够触发onNameChange方法
  44. })
  45. Button('change age')
  46. .onClick(() => {
  47. this.info.age = 26; // 不能够触发onAgeChange方法
  48. })
  49. Button('change region')
  50. .onClick(() => {
  51. this.info.region = 'South'; // 能够触发onChange方法
  52. })
  53. Button('change job')
  54. .onClick(() => {
  55. this.info.job = 'Driver'; // 能够触发onChange方法
  56. })
  57. }
  58. }
  59. }
  ```

  [MonitorDecoratorMultiWatchObservedV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorMultiWatchObservedV2.ets#L15-L75)
* @Monitor可以监听深层属性的变化，该深层属性需要被@Trace装饰。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Inner {
  5. @Trace public num: number = 0;
  6. }

  8. @ObservedV2
  9. class Outer {
  10. public inner: Inner = new Inner();

  12. @Monitor('inner.num')
  13. onChange(monitor: IMonitor) {
  14. hilog.info(0xFF00, 'testTag', '%{public}s',
  15. `inner.num change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  16. }
  17. }

  19. @Entry
  20. @ComponentV2
  21. struct Index {
  22. outer: Outer = new Outer();

  24. build() {
  25. Column() {
  26. Button('change num')
  27. .onClick(() => {
  28. this.outer.inner.num = 100; // 能够触发onChange方法
  29. })
  30. }
  31. }
  32. }
  ```

  [MonitorDecoratorObjectTraceObservedV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorObjectTraceObservedV2.ets#L15-L48)
* 在继承类场景下，可以在继承链中对同一个属性进行多次监听。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Base {
  5. @Trace public name: string;

  7. // 基类监听name属性
  8. @Monitor('name')
  9. onBaseNameChange(monitor: IMonitor) {
  10. hilog.info(0xFF00, 'testTag', '%{public}s', `Base Class name change`);
  11. }

  13. constructor(name: string) {
  14. this.name = name;
  15. }
  16. }

  18. @ObservedV2
  19. class Derived extends Base {
  20. // 继承类监听name属性
  21. @Monitor('name')
  22. onDerivedNameChange(monitor: IMonitor) {
  23. hilog.info(0xFF00, 'testTag', '%{public}s', `Derived Class name change`);
  24. }

  26. constructor(name: string) {
  27. super(name);
  28. }
  29. }

  31. @Entry
  32. @ComponentV2
  33. struct Index {
  34. derived: Derived = new Derived('AAA');

  36. build() {
  37. Column() {
  38. Button('change name')
  39. .onClick(() => {
  40. this.derived.name = 'BBB'; // 能够先后触发onBaseNameChange、onDerivedNameChange方法
  41. })
  42. }
  43. }
  44. }
  ```

  [MonitorDecoratorInheritanceSupportObservedV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorInheritanceSupportObservedV2.ets#L15-L60)

### 通用监听能力

@Monitor还有一些通用的监听能力。

* @Monitor支持对数组中的项进行监听，包括多维数组，对象数组。@Monitor无法监听内置类型（Array、Map、Date、Set）的API调用引起的变化。当@Monitor监听数组整体时，只能观测到数组整体的赋值。可以通过监听数组的长度变化来判断数组是否有插入、删除等变化。当前仅支持使用"."的方式表达深层属性、数组项的监听。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public name: string;
  6. @Trace public age: number;

  8. constructor(name: string, age: number) {
  9. this.name = name;
  10. this.age = age;
  11. }
  12. }

  14. @ObservedV2
  15. class ArrMonitor {
  16. @Trace public dimensionTwo: number[][] = [[1, 1, 1], [2, 2, 2], [3, 3, 3]];
  17. @Trace public dimensionThree: number[][][] = [[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]];
  18. @Trace public infoArr: Info[] = [new Info('Jack', 24), new Info('Lucy', 18)];

  20. // dimensionTwo为二维简单类型数组，且被@Trace装饰，能够观测里面的元素变化
  21. @Monitor('dimensionTwo.0.0', 'dimensionTwo.1.1')
  22. onDimensionTwoChange(monitor: IMonitor) {
  23. monitor.dirty.forEach((path: string) => {
  24. hilog.info(0xFF00, 'testTag', '%{public}s',
  25. `dimensionTwo path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  26. })
  27. }

  29. // dimensionThree为三维简单类型数组，且被@Trace装饰，能够观测里面的元素变化
  30. @Monitor('dimensionThree.0.0.0', 'dimensionThree.1.1.0')
  31. onDimensionThreeChange(monitor: IMonitor) {
  32. monitor.dirty.forEach((path: string) => {
  33. hilog.info(0xFF00, 'testTag', '%{public}s',
  34. `dimensionThree path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  35. })
  36. }

  38. // Info类中属性name、age均被@Trace装饰，能够监听到变化
  39. @Monitor('infoArr.0.name', 'infoArr.1.age')
  40. onInfoArrPropertyChange(monitor: IMonitor) {
  41. monitor.dirty.forEach((path: string) => {
  42. hilog.info(0xFF00, 'testTag', '%{public}s',
  43. `infoArr path:${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  44. })
  45. }

  47. // infoArr被@Trace装饰，能够监听到infoArr整体赋值的变化
  48. @Monitor('infoArr')
  49. onInfoArrChange(monitor: IMonitor) {
  50. hilog.info(0xFF00, 'testTag', '%{public}s', `infoArr whole change`);
  51. }

  53. // 能够监听到infoArr的长度变化
  54. @Monitor('infoArr.length')
  55. onInfoArrLengthChange(monitor: IMonitor) {
  56. hilog.info(0xFF00, 'testTag', '%{public}s', `infoArr length change`);
  57. }
  58. }

  60. @Entry
  61. @ComponentV2
  62. struct Index {
  63. arrMonitor: ArrMonitor = new ArrMonitor();

  65. build() {
  66. Column() {
  67. Button('Change dimensionTwo')
  68. .onClick(() => {
  69. // 能够触发onDimensionTwoChange方法
  70. this.arrMonitor.dimensionTwo[0][0]++;
  71. this.arrMonitor.dimensionTwo[1][1]++;
  72. })
  73. Button('Change dimensionThree')
  74. .onClick(() => {
  75. // 能够触发onDimensionThreeChange方法
  76. this.arrMonitor.dimensionThree[0][0][0]++;
  77. this.arrMonitor.dimensionThree[1][1][0]++;
  78. })
  79. Button('Change info property')
  80. .onClick(() => {
  81. // 能够触发onInfoArrPropertyChange方法
  82. this.arrMonitor.infoArr[0].name = 'Tom';
  83. this.arrMonitor.infoArr[1].age = 19;
  84. })
  85. Button('Change whole infoArr')
  86. .onClick(() => {
  87. // 能够触发onInfoArrChange、onInfoArrPropertyChange、onInfoArrLengthChange方法
  88. this.arrMonitor.infoArr = [new Info('Cindy', 8)];
  89. })
  90. Button('Push new info to infoArr')
  91. .onClick(() => {
  92. // 能够触发onInfoArrPropertyChange、onInfoArrLengthChange方法
  93. this.arrMonitor.infoArr.push(new Info('David', 50));
  94. })
  95. }
  96. }
  97. }
  ```

  [MonitorDecoratorArraySupport.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorArraySupport.ets#L15-L113)
* 对象整体改变，但监听的属性不变时，不触发@Monitor回调。

  下面的示例按照Step1-Step2-Step3的顺序点击，表现为代码注释中的行为。

  如果只点击Step2或Step3，改变name、age的值，此时会触发onNameChange和onAgeChange方法。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public person: Person;

  7. @Monitor('person.name')
  8. onNameChange(monitor: IMonitor) {
  9. hilog.info(0xFF00, 'testTag', '%{public}s',
  10. `name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  11. }

  13. @Monitor('person.age')
  14. onAgeChange(monitor: IMonitor) {
  15. hilog.info(0xFF00, 'testTag', '%{public}s',
  16. `age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  17. }

  19. constructor(name: string, age: number) {
  20. this.person = new Person(name, age);
  21. }
  22. }

  24. @ObservedV2
  25. class Person {
  26. @Trace public name: string;
  27. @Trace public age: number;

  29. constructor(name: string, age: number) {
  30. this.name = name;
  31. this.age = age;
  32. }
  33. }

  35. @Entry
  36. @ComponentV2
  37. struct Index {
  38. info: Info = new Info('Tom', 25);

  40. build() {
  41. Column() {
  42. Button('Step1: Only change name')
  43. .onClick(() => {
  44. this.info.person = new Person('Jack', 25); // 能够触发onNameChange方法，不触发onAgeChange方法
  45. })
  46. Button('Step2: Only change age')
  47. .onClick(() => {
  48. this.info.person = new Person('Jack', 18); // 能够触发onAgeChange方法，不触发onNameChange方法
  49. })
  50. Button('Step3: Change name and age')
  51. .onClick(() => {
  52. this.info.person = new Person('Lucy', 19); // 能够触发onNameChange、onAgeChange方法
  53. })
  54. }
  55. }
  56. }
  ```

  [MonitorDecoratorObjectSupport.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorObjectSupport.ets#L15-L72)
* 在一次事件中多次改变被@Monitor监听的属性，以最后一次修改为准。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Frequency {
  5. @Trace public count: number = 0;

  7. @Monitor('count')
  8. onCountChange(monitor: IMonitor) {
  9. hilog.info(0xFF00, 'testTag', '%{public}s',
  10. `count change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  11. }
  12. }

  14. @Entry
  15. @ComponentV2
  16. struct Index {
  17. frequency: Frequency = new Frequency();

  19. build() {
  20. Column() {
  21. Button('change count to 1000')
  22. .onClick(() => {
  23. for (let i = 1; i <= 1000; i++) {
  24. this.frequency.count = i;
  25. }
  26. })
  27. Button('change count to 0 then to 1000')
  28. .onClick(() => {
  29. for (let i = 999; i >= 0; i--) {
  30. this.frequency.count = i;
  31. }
  32. this.frequency.count = 1000; // 最终不触发onCountChange方法
  33. })
  34. }
  35. }
  36. }
  ```

  [MonitorDecoratorLastWrite.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorDecoratorLastWrite.ets#L15-L52)

在点击按钮"change count to 1000"后，会触发一次onCountChange方法，并输出日志"count change from 0 to 1000"。在点击按钮"change count to 0 then to 1000"后，由于事件前后属性count的值并没有改变，都为1000，所以不触发onCountChange方法。

## 限制条件

使用@Monitor需要注意如下限制条件：

* 不建议在一个类中对同一个属性进行多次@Monitor的监听。当一个类中存在对一个属性的多次监听时，只有最后一个定义的监听方法会生效。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public name: string = 'Tom';

  7. @Monitor('name')
  8. onNameChange(monitor: IMonitor) {
  9. hilog.info(0xFF00, 'testTag', '%{public}s', `onNameChange`);
  10. }

  12. @Monitor('name')
  13. onNameChangeDuplicate(monitor: IMonitor) {
  14. hilog.info(0xFF00, 'testTag', '%{public}s', `onNameChangeDuplicate`);
  15. }
  16. }

  18. @Entry
  19. @ComponentV2
  20. struct Index {
  21. info: Info = new Info();

  23. build() {
  24. Column() {
  25. Button('change name')
  26. .onClick(() => {
  27. this.info.name = 'Jack'; // 仅会触发onNameChangeDuplicate方法
  28. })
  29. }
  30. }
  31. }
  ```

  [MonitorLimitationLastListenerWins.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorLimitationLastListenerWins.ets#L15-L47)
* 当@Monitor传入多个路径参数时，以参数的全拼接结果判断是否重复监听。全拼接时会在参数间加空格，以区分不同参数。例如，'ab', 'c'的全拼接结果为'ab c'，'a', 'bc'的全拼接结果为'a bc'，二者全拼接不相等。以下示例中，Monitor 1、Monitor 2与Monitor 3都监听了name属性的变化。由于Monitor 2与Monitor 3的入参全拼接相等（都为'name position'），因此Monitor 2不生效，仅Monitor 3生效。当name属性变化时，将同时触发onNameAgeChange与onNamePositionChangeDuplicate方法。但请注意，Monitor 2与Monitor 3的写法仍然被视作在一个类中对同一个属性进行多次@Monitor的监听，这是不建议的。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public name: string = 'Tom';
  6. @Trace public age: number = 25;
  7. @Trace public position: string = 'North';

  9. @Monitor('name', 'age') // Monitor 1
  10. onNameAgeChange(monitor: IMonitor) {
  11. monitor.dirty.forEach((path: string) => {
  12. hilog.info(0xFF00, 'testTag', '%{public}s',
  13. `onNameAgeChange path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  14. });
  15. }

  17. @Monitor('name', 'position') // Monitor 2
  18. onNamePositionChange(monitor: IMonitor) {
  19. monitor.dirty.forEach((path: string) => {
  20. hilog.info(0xFF00, 'testTag', '%{public}s',
  21. `onNamePositionChange path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  22. });
  23. }

  25. // 重复监听name、position，仅最后定义的生效
  26. @Monitor('name', 'position') // Monitor3
  27. onNamePositionChangeDuplicate(monitor: IMonitor) {
  28. monitor.dirty.forEach((path: string) => {
  29. hilog.info(0xFF00, 'testTag', '%{public}s',
  30. `onNamePositionChangeDuplicate path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  31. });
  32. }
  33. }

  35. @Entry
  36. @ComponentV2
  37. struct Index {
  38. info: Info = new Info();

  40. build() {
  41. Column() {
  42. Button('change name')
  43. .onClick(() => {
  44. this.info.name = 'Jack'; // 同时触发onNameAgeChange与onNamePositionChangeDuplicate方法
  45. })
  46. }
  47. }
  48. }
  ```

  [MonitorLimitationMultiplePathParams.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorLimitationMultiplePathParams.ets#L15-L64)
* @Monitor的参数需要为监听属性名的字符串，仅可以使用字符串字面量、const常量、enum枚举值作为参数。如果使用变量作为参数，仅会监听@Monitor初始化时，变量值所对应的属性。当更改变量时，@Monitor无法实时改变监听的属性，即@Monitor监听的目标属性从初始化时便已经确定，无法动态更改。不建议开发者使用变量作为@Monitor的参数进行初始化。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. const t2: string = 't2'; // const常量

  5. enum ENUM {
  6. T3 = 't3' // enum枚举值
  7. };
  8. let t4: string = 't4'; // 变量

  10. @ObservedV2
  11. class Info {
  12. @Trace public t1: number = 0;
  13. @Trace public t2: number = 0;
  14. @Trace public t3: number = 0;
  15. @Trace public t4: number = 0;
  16. @Trace public t5: number = 0;

  18. // 字符串字面量
  19. @Monitor('t1')
  20. onT1Change(monitor: IMonitor) {
  21. hilog.info(0xFF00, 'testTag', '%{public}s', `t1 change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  22. }

  24. @Monitor(t2)
  25. onT2Change(monitor: IMonitor) {
  26. hilog.info(0xFF00, 'testTag', '%{public}s', `t2 change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  27. }

  29. @Monitor(ENUM.T3)
  30. onT3Change(monitor: IMonitor) {
  31. hilog.info(0xFF00, 'testTag', '%{public}s', `t3 change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  32. }

  34. @Monitor(t4)
  35. onT4Change(monitor: IMonitor) {
  36. hilog.info(0xFF00, 'testTag', '%{public}s', `t4 change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  37. }
  38. }

  40. @Entry
  41. @ComponentV2
  42. struct Index {
  43. info: Info = new Info();

  45. build() {
  46. Column() {
  47. Button('Change t1')
  48. .onClick(() => {
  49. this.info.t1++; // 能够触发onT1Change方法
  50. })
  51. Button('Change t2')
  52. .onClick(() => {
  53. this.info.t2++; // 能够触发onT2Change方法
  54. })
  55. Button('Change t3')
  56. .onClick(() => {
  57. this.info.t3++; // 能够触发onT3Change方法
  58. })
  59. Button('Change t4')
  60. .onClick(() => {
  61. this.info.t4++; // 能够触发onT4Change方法
  62. })
  63. Button('Change var t4 to t5')
  64. .onClick(() => {
  65. t4 = 't5'; // 更改变量值为't5'
  66. })
  67. Button('Change t5')
  68. .onClick(() => {
  69. this.info.t5++; // onT4Change仍监听t4，不会触发
  70. })
  71. Button('Change t4 again')
  72. .onClick(() => {
  73. this.info.t4++; // 能够触发onT4Change方法
  74. })
  75. }
  76. }
  77. }
  ```

  [MonitorLimitationParameterStringConstraint.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorLimitationParameterStringConstraint.ets#L15-L93)
* 建议开发者避免在@Monitor中再次更改被监听的属性，这会导致无限循环。

  ```
  1. @ObservedV2
  2. class Info {
  3. @Trace count: number = 0;
  4. @Monitor('count')
  5. onCountChange(monitor: IMonitor) {
  6. this.count++; // 应避免这种写法，会导致无限循环
  7. }
  8. }
  ```

## @Monitor与@Watch对比

@Monitor与@Watch的用法、功能对比如下：

| 用法 | @Watch | @Monitor |
| --- | --- | --- |
| 参数 | 回调方法名。 | 监听状态变量名、属性名。 |
| 监听目标数 | 只能监听单个状态变量。 | 能同时监听多个状态变量。 |
| 监听能力 | 跟随状态变量观察能力（一层）。 | 跟随状态变量观察能力（深层）。 |
| 能否获取变化前的值 | 不能获取变化前的值。 | 能获取变化前的值。 |
| 监听条件 | 监听对象为状态变量。 | 监听对象为状态变量或为@Trace装饰的类成员属性。 |
| 使用限制 | 仅能在@Component装饰的自定义组件中使用。 | 能在@ComponentV2装饰的自定义组件中使用，也能在@ObservedV2装饰的类中使用。 |

## 使用场景

### 监听深层属性变化

@Monitor可以监听深层属性的变化，并能够根据更改前后的值做分类处理。

下面的示例中监听了属性value的变化，并根据变化的幅度改变Text组件显示的样式。

```
1. @ObservedV2
2. class Info {
3. @Trace public value: number = 50;
4. }

6. @ObservedV2
7. class UIStyle {
8. public info: Info = new Info();
9. @Trace public color: Color = Color.Black;
10. @Trace public fontSize: number = 45;

12. @Monitor('info.value')
13. onValueChange(monitor: IMonitor) {
14. let lastValue: number = monitor.value()?.before as number;
15. let curValue: number = monitor.value()?.now as number;
16. if (lastValue != 0) {
17. let diffPercent: number = (curValue - lastValue) / lastValue;
18. // 通过info.value变化的幅度，改变Text组件显示的样式
19. if (diffPercent > 0.1) {
20. this.color = Color.Red;
21. this.fontSize = 50;
22. } else if (diffPercent < -0.1) {
23. this.color = Color.Green;
24. this.fontSize = 40;
25. } else {
26. this.color = Color.Black;
27. this.fontSize = 45;
28. }
29. }
30. }
31. }

33. @Entry
34. @ComponentV2
35. struct Index {
36. textStyle: UIStyle = new UIStyle();

38. build() {
39. Column() {
40. Text(`Important Value: ${this.textStyle.info.value}`)
41. .fontColor(this.textStyle.color)
42. .fontSize(this.textStyle.fontSize)
43. Button('change!')
44. .onClick(() => {
45. this.textStyle.info.value = Math.floor(Math.random() * 100) + 1;
46. })
47. }
48. }
49. }
```

[MonitorSceneDeepAttributeChanges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorSceneDeepAttributeChanges.ets#L30-L79)

## 常见问题

### 自定义组件中@Monitor对变量监听的生效及失效时间

当@Monitor定义在@ComponentV2装饰的自定义组件中时，@Monitor会在状态变量初始化完成之后生效，并在组件销毁时失效。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. @Trace public message: string = 'not initialized';

7. constructor() {
8. hilog.info(0xFF00, 'testTag', '%{public}s', 'in constructor message change to initialized');
9. // 此时@Monitor还未初始化成功，因此不会监听到message的变化
10. this.message = 'initialized';
11. }
12. }

14. @ComponentV2
15. struct Child {
16. @Param info: Info = new Info();

18. @Monitor('info.message')
19. onMessageChange(monitor: IMonitor) {
20. hilog.info(0xFF00, 'testTag', '%{public}s',
21. `Child message change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
22. }

24. aboutToAppear(): void {
25. this.info.message = 'Child aboutToAppear';
26. }

28. aboutToDisappear(): void {
29. hilog.info(0xFF00, 'testTag', '%{public}s', 'Child aboutToDisappear');
30. this.info.message = 'Child aboutToDisappear';
31. }

33. build() {
34. Column() {
35. Text('Child')
36. Button('change message in Child')
37. .onClick(() => {
38. this.info.message = 'Child click to change Message';
39. })
40. }
41. .borderColor(Color.Red)
42. .borderWidth(2)

44. }
45. }

47. @Entry
48. @ComponentV2
49. struct Index {
50. @Local info: Info = new Info();
51. @Local flag: boolean = false;

53. @Monitor('info.message')
54. onMessageChange(monitor: IMonitor) {
55. hilog.info(0xFF00, 'testTag', '%{public}s',
56. `Index message change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
57. }

59. build() {
60. Column() {
61. Button('show/hide Child')
62. .onClick(() => {
63. this.flag = !this.flag
64. })
65. Button('change message in Index')
66. .onClick(() => {
67. this.info.message = 'Index click to change Message';
68. })
69. if (this.flag) {
70. Child({ info: this.info })
71. }
72. }
73. }
74. }
```

[MonitorProblemEffectTimeCompV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemEffectTimeCompV2.ets#L15-L89)

在上面的例子中，可以通过创建和销毁Child组件来观察定义在自定义组件中的@Monitor的生效和失效时机。推荐按如下顺序进行操作：

* 当Index组件创建Info类实例时，日志输出in constructor message change to initialized。此时Index组件的@Monitor还未初始化成功，因此不会监听到message的变化。
* 当Index组件创建完成，页面加载完成后，点击按钮“change message in Index”，此时Index组件中的@Monitor能够监听到变化，日志输出Index message change from initialized to Index click to change Message。
* 点击按钮“show/hide Child”，创建Child组件，在Child组件初始化@Param装饰的变量以及@Monitor之后，调用Child组件的aboutToAppear回调，改变message。此时Index组件与Child组件的@Monitor均能监听到变化，日志输出Index message change from Index click to change Message to Child aboutToAppear以及Child message change from Index click to change Message to Child aboutToAppear。
* 点击按钮“change message in Child”，改变message。此时Index组件与Child组件的@Monitor均能监听到变化，日志输出Index message change from Child aboutToAppear to Child click to change Message以及Child message change from Child aboutToAppear to Child click to change Message。
* 点击按钮”show/hide Child“，销毁Child组件，调用Child组件的aboutToDisappear回调，改变message。此时Index组件与Child组件的@Monitor均能监听到变化，日志输出Child aboutToDisappear，Index message change from Child click to change Message to Child aboutToDisappear以及Child message change from Child click to change Message to Child aboutToDisappear。
* 点击按钮“change message in Index”，改变message。此时Child组件已销毁，其注册的@Monitor监听也被解注册，仅有Index组件的@Monitor能够监听到变化，日志输出Index message change from Child aboutToDisappear to Index click to change Message。

这表明Child组件中定义的@Monitor监听随着Child组件的创建初始化生效，随着Child组件的销毁失效。

### 类中@Monitor对变量监听的生效及失效时间

当@Monitor定义在@ObservedV2装饰的类中时，@Monitor会在类的实例创建完成后生效，在类的实例销毁时失效。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. @Trace public message: string = 'not initialized';

7. constructor() {
8. // 此时@Monitor还未生效，因此不会监听到message的变化
9. this.message = 'initialized';
10. }

12. @Monitor('message')
13. onMessageChange(monitor: IMonitor) {
14. hilog.info(0xFF00, 'testTag', '%{public}s',
15. `message change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Index {
22. info: Info = new Info();

24. aboutToAppear(): void {
25. this.info.message = 'Index aboutToAppear';
26. }

28. build() {
29. Column() {
30. Button('change message')
31. .onClick(() => {
32. this.info.message = 'Index click to change message';
33. })
34. }
35. }
36. }
```

[MonitorProblemEffectTimeClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemEffectTimeClass.ets#L15-L51)

上面的例子中，@Monitor会在info创建完成后生效，这个时机晚于类的constructor，早于自定义组件的aboutToAppear。当界面加载完成后，点击“change message”，修改message变量。此时日志输出信息如下：

```
1. message change from initialized to Index aboutToAppear
2. message change from Index aboutToAppear to Index click to change message
```

类中定义的@Monitor随着类的销毁失效。而由于类的实际销毁释放依赖于垃圾回收机制，因此会出现即使所在自定义组件已经销毁，类却还未及时销毁，导致类中定义的@Monitor仍在监听变化的情况。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class InfoWrapper {
5. public info?: Info;

7. constructor(info: Info) {
8. this.info = info;
9. }

11. @Monitor('info.age')
12. onInfoAgeChange(monitor: IMonitor) {
13. hilog.info(0xFF00, 'testTag', '%{public}s',
14. `age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
15. }
16. }

18. @ObservedV2
19. class Info {
20. @Trace public age: number;

22. constructor(age: number) {
23. this.age = age;
24. }
25. }

27. @ComponentV2
28. struct Child {
29. @Param @Require infoWrapper: InfoWrapper;

31. aboutToDisappear(): void {
32. hilog.info(0xFF00, 'testTag', '%{public}s', 'Child aboutToDisappear', this.infoWrapper.info?.age);
33. }

35. build() {
36. Column() {
37. Text(`${this.infoWrapper.info?.age}`)
38. }
39. }
40. }

42. @Entry
43. @ComponentV2
44. struct Index {
45. dataArray: Info[] = [];
46. @Local showFlag: boolean = true;

48. aboutToAppear(): void {
49. for (let i = 0; i < 5; i++) {
50. this.dataArray.push(new Info(i));
51. }
52. }

54. build() {
55. Column() {
56. Button('change showFlag')
57. .onClick(() => {
58. this.showFlag = !this.showFlag;
59. })
60. Button('change number')
61. .onClick(() => {
62. hilog.info(0xFF00, 'testTag', '%{public}s', 'click to change age');
63. this.dataArray.forEach((info: Info) => {
64. info.age += 100;
65. });
66. })
67. if (this.showFlag) {
68. Column() {
69. Text('Children')
70. ForEach(this.dataArray, (info: Info) => {
71. Child({ infoWrapper: new InfoWrapper(info) })
72. })
73. }
74. .borderColor(Color.Red)
75. .borderWidth(2)
76. }
77. }
78. }
79. }
```

[MonitorProblemClassDelayed.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemClassDelayed.ets#L15-L95)

在上面的例子中，当点击“change showFlag”切换if组件的条件时，Child组件会被销毁。此时，点击“change number”修改age的值时，可以通过日志观察到InfoWrapper中定义的@Monitor回调仍然被触发了。这是因为此时自定义组件Child虽然执行了aboutToDisappear，但是其成员变量infoWrapper还没有被立刻回收，当变量发生变化时，依然能够调用到infoWrapper中定义的onInfoAgeChange方法，所以从现象上看@Monitor回调仍会被触发。

借助垃圾回收机制去取消@Monitor的监听是不稳定的，开发者可以采用以下两种方式去管理@Monitor的失效时间：

1、将@Monitor定义在自定义组件中。由于自定义组件在销毁时，状态管理框架会手动取消@Monitor的监听，因此在自定义组件调用完aboutToDisappear，尽管自定义组件的数据不一定已经被释放，但@Monitor回调已不会再被触发。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class InfoWrapper {
5. public info?: Info;

7. constructor(info: Info) {
8. this.info = info;
9. }
10. }

12. @ObservedV2
13. class Info {
14. @Trace public age: number;

16. constructor(age: number) {
17. this.age = age;
18. }
19. }

21. @ComponentV2
22. struct Child {
23. @Param @Require infoWrapper: InfoWrapper;

25. @Monitor('infoWrapper.info.age')
26. onInfoAgeChange(monitor: IMonitor) {
27. hilog.info(0xFF00, 'testTag', '%{public}s',
28. `age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
29. }

31. aboutToDisappear(): void {
32. hilog.info(0xFF00, 'testTag', '%{public}s', 'Child aboutToDisappear', this.infoWrapper.info?.age);
33. }

35. build() {
36. Column() {
37. Text(`${this.infoWrapper.info?.age}`)
38. }
39. }
40. }

42. @Entry
43. @ComponentV2
44. struct Index {
45. dataArray: Info[] = [];
46. @Local showFlag: boolean = true;

48. aboutToAppear(): void {
49. for (let i = 0; i < 5; i++) {
50. this.dataArray.push(new Info(i));
51. }
52. }

54. build() {
55. Column() {
56. // 点击Button切换showFlag，触发Child组件的创建/销毁
57. Button('change showFlag')
58. .onClick(() => {
59. this.showFlag = !this.showFlag;
60. })
61. Button('change number')
62. .onClick(() => {
63. hilog.info(0xFF00, 'testTag', '%{public}s', 'click to change age');
64. this.dataArray.forEach((info: Info) => {
65. info.age += 100;
66. })
67. })
68. if (this.showFlag) {
69. Column() {
70. Text('Children')
71. ForEach(this.dataArray, (info: Info) => {
72. Child({ infoWrapper: new InfoWrapper(info) })
73. })
74. }
75. .borderColor(Color.Red)
76. .borderWidth(2)
77. }
78. }
79. }
80. }
```

[MonitorProblemClassFailureTimeSetComp.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemClassFailureTimeSetComp.ets#L15-L95)

2、主动置空监听的对象。当自定义组件即将销毁时，主动置空@Monitor的监听目标，这样@Monitor无法再监听原监听目标的变化，达到取消@Monitor监听的效果。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class InfoWrapper {
5. public info?: Info;

7. constructor(info: Info) {
8. this.info = info;
9. }

11. @Monitor('info.age')
12. onInfoAgeChange(monitor: IMonitor) {
13. hilog.info(0xFF00, 'testTag', '%{public}s',
14. `age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
15. }
16. }

18. @ObservedV2
19. class Info {
20. @Trace public age: number;

22. constructor(age: number) {
23. this.age = age;
24. }
25. }

27. @ComponentV2
28. struct Child {
29. @Param @Require infoWrapper: InfoWrapper;

31. aboutToDisappear(): void {
32. hilog.info(0xFF00, 'testTag', '%{public}s', 'Child aboutToDisappear', this.infoWrapper.info?.age);
33. this.infoWrapper.info = undefined; // 使InfoWrapper对info.age的监听失效
34. }

36. build() {
37. Column() {
38. Text(`${this.infoWrapper.info?.age}`)
39. }
40. }
41. }

43. @Entry
44. @ComponentV2
45. struct Index {
46. dataArray: Info[] = [];
47. @Local showFlag: boolean = true;

49. aboutToAppear(): void {
50. for (let i = 0; i < 5; i++) {
51. this.dataArray.push(new Info(i));
52. }
53. }

55. build() {
56. Column() {
57. // 点击Button切换showFlag，触发Child组件的创建/销毁
58. Button('change showFlag')
59. .onClick(() => {
60. this.showFlag = !this.showFlag;
61. })
62. Button('change number')
63. .onClick(() => {
64. hilog.info(0xFF00, 'testTag', '%{public}s', 'click to change age');
65. this.dataArray.forEach((info: Info) => {
66. info.age += 100;
67. })
68. })
69. if (this.showFlag) {
70. Column() {
71. Text('Children')
72. ForEach(this.dataArray, (info: Info) => {
73. Child({ infoWrapper: new InfoWrapper(info) })
74. })
75. }
76. .borderColor(Color.Red)
77. .borderWidth(2)
78. }
79. }
80. }
81. }
```

[MonitorProblemClassFailureTimeEmptyObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemClassFailureTimeEmptyObject.ets#L15-L96)

### 正确设置@Monitor入参

从API version 23起，增加了对@Monitor入参的编译时校验。当@Monitor的入参不符合监听条件时（如传入非状态变量、不存在的变量等），将会有编辑、编译告警，但@Monitor回调仍会被触发。开发者应正确传入@Monitor入参，避免监听非状态变量，防止功能异常或行为与预期不符。

【反例1】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. @Trace public age: number = 24;

8. // 同时监听状态变量age和非状态变量name
9. // 此时会编辑、编译告警，提示`The '@Monitor' decorator needs to monitor the state variables that exist.`
10. @Monitor('age', 'name')
11. onPropertyChange(monitor: IMonitor) {
12. monitor.dirty.forEach((path: string) => {
13. hilog.info(0xFF00, 'testTag', '%{public}s',
14. `property path:${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
15. })
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Index {
22. info: Info = new Info();

24. build() {
25. Column() {
26. Button('change age&name')
27. .onClick(() => {
28. this.info.age = 25; // 同时改变状态变量age和非状态变量name
29. this.info.name = 'Johny';
30. })
31. }
32. }
33. }
```

[MonitorProblemParamCounterExample1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemParamCounterExample1.ets#L15-L48)

上面的代码中，当点击按钮同时更改状态变量age和非状态变量name时，会输出以下日志：

```
1. property path:age change from 24 to 25
2. property path:name change from John to Johny
```

实际上name属性本身并不是可被观测的变量，不应被加入到@Monitor的入参当中。建议开发者去除对name属性的监听或者给name加上@Trace装饰成为状态变量。

【正例1】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. @Trace public age: number = 24;

8. // 仅监听状态变量age
9. @Monitor('age')
10. onPropertyChange(monitor: IMonitor) {
11. monitor.dirty.forEach((path: string) => {
12. hilog.info(0xFF00, 'testTag', '%{public}s',
13. `property path:${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
14. })
15. }
16. }

18. @Entry
19. @ComponentV2
20. struct Index {
21. info: Info = new Info();

23. build() {
24. Column() {
25. Button('change age&name')
26. .onClick(() => {
27. this.info.age = 25; // 状态变量age改变
28. this.info.name = 'Johny';
29. })
30. }
31. }
32. }
```

[MonitorProblemParamPositiveExample1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemParamPositiveExample1.ets#L15-L48)

【反例2】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. @Trace public age: number = 24;

8. get myAge() {
9. return this.age; // age为状态变量
10. }

12. // 监听非@Computed装饰的getter访问器
13. @Monitor('myAge')
14. onPropertyChange() {
15. hilog.info(0xFF00, 'testTag', '%{public}s', 'age changed');
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Index {
22. info: Info = new Info();

24. build() {
25. Column() {
26. Button('change age')
27. .onClick(() => {
28. this.info.age = 25; // 状态变量age改变
29. })
30. }
31. }
32. }
```

[MonitorProblemParamCounterExample2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemParamCounterExample2.ets#L15-L48)

上面的代码中，@Monitor的入参为一个getter访问器的名字，但该getter访问器本身并未被@Computed装饰，不是一个可被监听的变量。但由于使用了状态变量参与了计算，在状态变量变化后，myAge也被认为发生了变化，因此触发了@Monitor回调。建议开发者给myAge添加@Computed装饰器或当getter访问器直接返回状态变量时，不监听getter访问器而是直接监听状态变量本身。

【正例2】

将myAge变为状态变量：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. @Trace public age: number = 24;

8. // 给myAge添加@Computed成为状态变量
9. @Computed
10. get myAge() {
11. return this.age;
12. }

14. // 监听@Computed装饰的getter访问器
15. @Monitor('myAge')
16. onPropertyChange() {
17. hilog.info(0xFF00, 'testTag', '%{public}s', 'age changed');
18. }
19. }

21. @Entry
22. @ComponentV2
23. struct Index {
24. info: Info = new Info();

26. build() {
27. Column() {
28. Button('change age')
29. .onClick(() => {
30. this.info.age = 25; // 状态变量age改变
31. })
32. }
33. }
34. }
```

[MonitorProblemParamPositiveExample2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemParamPositiveExample2.ets#L15-L50)

或直接监听状态变量本身：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. @Trace public age: number = 24;

8. // 监听状态变量age
9. @Monitor('age')
10. onPropertyChange() {
11. hilog.info(0xFF00, 'testTag', '%{public}s', 'age changed');
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct Index {
18. info: Info = new Info();

20. build() {
21. Column() {
22. Button('change age')
23. .onClick(() => {
24. this.info.age = 25; // 状态变量age改变
25. })
26. }
27. }
28. }
```

[MonitorProblemParamStateVariables.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemParamStateVariables.ets#L15-L44)

### 无法监听变量从可访问变为不可访问和从不可访问变为可访问

@Monitor仅会保存变量可访问时的值，当状态变量变为不可访问的状态时，并不会记录其值的变化。在下面的例子中，点击三个Button，均不会触发onChange的回调。

从API version 20开始，如果需要监听可访问到不可访问和不可访问到可访问的状态变化，可以使用[addMonitor](arkts-new-addmonitor-clearmonitor.md#监听变量从可访问到不访问和从不可访问到可访问)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class User {
5. @Trace public age: number = 10;
6. }

8. @Entry
9. @ComponentV2
10. struct Page {
11. @Local user: User | undefined | null = new User();

13. @Monitor('user.age')
14. onChange(mon: IMonitor) {
15. mon.dirty.forEach((path: string) => {
16. hilog.info(0xFF00, 'testTag', '%{public}s',
17. `onChange: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
18. });
19. }

21. build() {
22. Column() {
23. Text(`User age ${this.user?.age}`).fontSize(20)
24. Button('set user to undefined').onClick(() => {
25. // age：可访问 -> 不可访问
26. this.user = undefined;
27. })
28. Button('set user to User').onClick(() => {
29. // age：不可访问 ->可访问
30. this.user = new User();
31. })
32. Button('set user to null').onClick(() => {
33. // age：可访问->不可访问
34. this.user = null;
35. })
36. }
37. }
38. }
```

[MonitorProblemStateChangeUseAddMonitor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/monitor/MonitorProblemStateChangeUseAddMonitor.ets#L15-L54)
