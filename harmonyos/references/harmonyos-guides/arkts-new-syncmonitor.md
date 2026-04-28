---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-syncmonitor
title: @SyncMonitor装饰器：状态变量修改同步监听
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理数据对象的状态 > @SyncMonitor装饰器：状态变量修改同步监听
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8945d5b94323c939e02b42498f60a967ba6fa4725fce6e4adb547f70b85a9231
---

为了增强状态管理框架对状态变量变化的监听能力，开发者可以使用@SyncMonitor装饰器对状态变量进行监听。

@SyncMonitor提供了对V2状态变量的同步监听。在阅读本文档前，建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)，[@ObservedV2和@Trace](arkts-new-observedv2-and-trace.md)，[@Local](arkts-new-local.md)，[@Monitor](arkts-new-monitor.md)。

说明

@SyncMonitor装饰器从API version 23开始支持。

从API version 23开始，该装饰器支持在元服务中使用。

## 概述

@SyncMonitor装饰器用于同步监听状态变量修改，使得状态变量具有深度监听的能力：

* @SyncMonitor装饰器支持在@ComponentV2装饰的自定义组件中使用，未被状态变量装饰器[@Local](arkts-new-local.md)、[@Param](arkts-new-param.md)、[@Provider](arkts-new-provider-and-consumer.md)、[@Consumer](arkts-new-provider-and-consumer.md)、[@Computed](arkts-new-computed.md)装饰的变量无法被@SyncMonitor监听到变化。

## 装饰器使用规则说明

* @SyncMonitor装饰器支持在类中与[@ObservedV2、@Trace](arkts-new-observedv2-and-trace.md)配合使用，不允许在未被@ObservedV2装饰的类中使用@SyncMonitor装饰器。未被@Trace装饰的属性无法被@SyncMonitor监听到变化。当观测的属性变化时，@SyncMonitor装饰器定义的回调方法将被调用。判断属性是否变化使用的是严格相等（===），当严格相等判断的结果是false（即不相等）的情况下，就会立即触发@SyncMonitor的回调。同一事件内，当被观察的属性多次改变时，回调函数将在每次属性改变时被调用。
* 单个@SyncMonitor装饰器能够同时监听多个属性的变化，当这些属性在一次事件中共同变化时，只会触发一次@SyncMonitor的回调方法。 当@SyncMonitor监听整个数组时，更改数组的某一项不会被监听到。
* 在继承类场景中，可以在父子类中对同一个属性分别定义@SyncMonitor进行监听，当属性变化时，父子组件中定义的@SyncMonitor回调均会被调用。
* @SyncMonitor装饰器具有深度监听的能力，能够监听嵌套类、多维数组、对象数组中指定项的变化。对于嵌套类、对象数组中成员属性变化的监听要求该类被@ObservedV2装饰且该属性被@Trace装饰。
* @SyncMonitor可以观察内置类型Map, Set, DateAPI调用引用的数据变化。
* @SyncMonitor可以观察Array类型API调用引起的数据变化，即使Array的长度为0，调用Array类型的API，比如copyWithin, fill, sort, push，@SyncMonitor装饰的回调函数也会执行。
* @SyncMonitor装饰器新增[通配符('\*')](arkts-new-syncmonitor.md#监听路径中通配符的说明)支持一层模糊监听，便于@Watch装饰器向@SyncMonitor装饰器迁移。

### 比较@Monitor，@SyncMonitor和@Watch

与[@Watch](arkts-watch.md)装饰器类似，开发者必须自己定义回调函数。不同之处在于，@Watch使用函数名作为参数，而@SyncMonitor直接装饰回调函数。带有通配符监听路径的@SyncMonitor监听与@Watch具有相同的状态变化。@Watch和@SyncMonitor装饰的函数都同步执行。下表比较@Monitor、@SyncMonitor和@Watch的用法和功能。

| 类别 | @Watch | @Monitor | @SyncMonitor |
| --- | --- | --- | --- |
| 参数 | 回调方法名称 | 监听到的状态变量名称和属性名称 | 监听到的状态变量名称和属性名称 |
| 监听目标数量 | 单个状态变量 | 多个状态变量 | 多个状态变量 |
| 监听类型 | 模糊监听 | 精准深度监听 | 支持模糊监听和精准监听 |
| 获取变更前的值 | 否 | 是 | 是 |
| 观察条件 | 被观察对象是状态变量 | 被观察对象是状态变量或用@Trace装饰的类成员属性 | 被观察对象是状态变量或用@Trace装饰的类成员属性 |
| 约束条件 | 仅在@Component装饰的自定义组件中 | 在@ComponentV2装饰的自定义组件和@ObservedV2装饰的类中 | 在@ComponentV2装饰的自定义组件和@ObservedV2装饰的类中 |
| 通配符支持 | 否 | 否 | 是 |
| 回调调用时机 | 立即（同步） | 状态变更函数结束后（异步），多次变更， 只触发一次。 | 立即（同步） |

[addMonitor和clearMonitor](arkts-new-addmonitor-clearmonitor.md)API允许在应用程序执行期间动态添加和清除监听器。当isSynchronous设置为true，addMonitor类似于@SyncMonitor, 当设置为false，addMonitor类似于@Monitor功能。

@Monitor和@SyncMonitor分别是@ComponentV2和@ObservedV2类的成员函数装饰器，属于V2状态管理的一部分。@Watch是[@Component](arkts-create-custom-components.md#component)中使用的变量装饰器，属于V1状态管理的一部分。

@Monitor装饰的函数会异步执行，在事件处理程序执行结束后执行。@SyncMonitor和@Watch函数在观察到的状态变量改变后，回调函数会立即同步执行。

@Monitor函数的执行可以由一个或多个特定跟踪对象属性的值变化而触发。@Watch函数会在任何被观察的对象属性或数组项发生变化时执行，它无法监听一个或多个特定属性。

路径中带有通配符的@SyncMonitor的行为与@Watch相同。这使得应用程序从V1状态管理迁移到V2状态管理更加容易。下面是一个例子：

V1状态管理@Watch示例代码:

```
1. @Component
2. struct CompV1 {
3. @State @Watch('watchFuncName') varName: ClassA = initialValue; // ClassA是Class类型
4. watchFuncName(propertyStr: string) {
5. // ....
6. }
7. }
```

迁移成V2状态管理@SyncMonitor示例代码:

```
1. @ComponentV2
2. struct CompV2 {
3. @Local varName: ClassA = initialValue;
4. @SyncMonitor('varName.*') monitorFuncName(m: IMonitor) {
5. // ....
6. }
7. }
```

其中，ClassA是指复杂对象类型。下面的例子使用@SyncMonitor和@Monitor来跟踪sum属性的变化。

代码计算数组元素的和，在循环中计算sum时，sum的值依次变为0, 1, 3, 6。

@Monitor只调用一次，before值为0，now值为6。

@SyncMonitor将调用其回调3次，分别对应从0到1、1到3和3到6的变化。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @ComponentV2
5. struct DocSampleArraySum {
6. @Local sum: number = 0;
7. arr: Array<number> = [1, 2, 3];
8. @SyncMonitor('sum')
9. syncSumMonitor(info: IMonitor) {
10. let path = info.dirty[0];
11. hilog.info(0xFF00, 'SyncMonitor', '%{public}s', `${path} changed from ${info.value(path)?.before} to ${info.value(path)?.now}`);
12. }
13. @Monitor('sum')
14. asyncSumMonitor(info: IMonitor) {
15. let path = info.dirty[0];
16. hilog.info(0xFF00, 'Monitor', '%{public}s', `${path} changed from ${info.value(path)?.before} to ${info.value(path)?.now}`);
17. }

19. build() {
20. Column() {
21. Button('Calculate a sum')
22. .onClick(() => {  // 修改sum时，syncSumMonitor会回调3次，asyncSumMonitor只回调1次。
23. this.sum = 0;
24. this.arr.forEach((element) => this.sum += element);
25. })
26. }
27. }
28. }
```

日志输出:

```
1. SyncMonitor - sum changed from 0 to 1
2. SyncMonitor - sum changed from 1 to 3
3. SyncMonitor - sum changed from 3 to 6
4. Monitor - sum changed from 0 to 6
```

## 装饰器说明

| @SyncMonitor属性装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 字符串类型的对象属性名称。可同时监听多个对象属性，每个属性以逗号隔开，例如： @SyncMonitor('prop1', 'prop2'). 此外，可监听深层的属性变化：多维数组中的元素、嵌套对象中的属性、对象数组中的属性。支持在路径末尾添加通配符'\*'来监听任意被观察属性的变化。详情参见 [监听变化](arkts-new-syncmonitor.md#监听变化)。 |
| 装饰内容 | 成员方法。在被观察属性变化时，该回调会被触发。该回调方法以[IMonitor类型](../harmonyos-references/ts-state-management-watch-monitor.md#imonitor12)的变量作为参数，开发者可以从该参数中获取变化前后的相关信息。 |

## 监听路径中通配符的说明

当@SyncMonitor装饰器监听路径中使用了通配符('\*')时：

* 对象赋值或对象任意属性变化都会触发；
* 数组赋值或数组任意项变化都会触发；
* 即可监听任意属性变化或任意数组项变化;
* 使用通配符时，before和after返回的值均是undefined;

通配符(\*)的路径语法规则：

* 通配符只能出现在路径末尾；
* 通配符不能出现在路径开头，也不能出现在路径中间；

如下给出合法路径示例：

* obj.\*（观察含@Trace的对象）
  + 当给obj赋新值时触发;
  + 当obj的任何被@Trace装饰的属性变化时触发；
* arr.\*观察数组
  + 当给arr赋新值时触发；
  + 当数组中任意项或数组长度变化时触发；
  + 调用Array类型的API，比如copyWithin, fill, sort, push，@SyncMonitor装饰的回调函数也会执行；
* obj.ObjA.objB.\*（观察嵌套对象中的对象）
  + 当obj、ObjA被重新赋值且objB变化时触发；
  + 当objB被重新赋值时触发；
  + 当objB内任意被@Trace装饰属性变化时触发；
* arr.1.\*（多维观察数组）
  + 给arr赋新值，且第1项的值发生变化时触发；
  + 当嵌套数组项的任何项或长度更改时触发；

## 接口说明

IMonitor类型和IMonitorValue<T>类型的接口说明参考API文档：[状态变量变化监听](../harmonyos-references/ts-state-management-watch-monitor.md)。

## 监听变化

### 在@ComponentV2装饰的自定义组件中使用@SyncMonitor

使用@SyncMonitor监听的状态变量发生变化时，会触发@SyncMonitor的回调方法。

* @SyncMonitor监听的变量需要被@Local、@Param、@Provider、@Consumer、@Computed装饰，未被状态变量装饰器装饰的变量在变化时无法被监听。@SyncMonitor可以同时监听多个状态变量，这些变量名之间用','隔开。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @Entry
  4. @ComponentV2
  5. struct Index {
  6. @Local message: string = 'Hello World';
  7. @Local name: string = 'Tom';
  8. @Local age: number = 24;

  10. @SyncMonitor('message', 'name')
  11. onStrChange(monitor: IMonitor) {
  12. monitor.dirty.forEach((path: string) => {
  13. hilog.info(0xFF00, 'testTag', '%{public}s',
  14. `${path} changed from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  15. });
  16. }

  18. build() {
  19. Column() {
  20. Button('change string')
  21. .onClick(() => {
  22. this.message += '!';
  23. this.name = 'Jack';
  24. })
  25. }
  26. }
  27. }
  ```
* @SyncMonitor监听的状态变量为类对象时，仅能监听对象整体的变化。监听类属性的变化需要类属性被@Trace装饰，无法监听非状态变量的变化。

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

  18. @SyncMonitor('info')
  19. infoChange(monitor: IMonitor) {
  20. hilog.info(0xFF00, 'testTag', '%{public}s', `info change`);
  21. }

  23. build() {
  24. Column() {
  25. Text(`name: ${this.info.name}, age: ${this.info.age}`)
  26. Button('change info')
  27. .onClick(() => {
  28. this.info = new Info('Lucy', 18); // 能够监听到
  29. })
  30. }
  31. }
  32. }
  ```

### 在@ObservedV2装饰的类中使用@SyncMonitor

使用@SyncMonitor监听的属性发生变化时，会触发@SyncMonitor的回调方法。

* @SyncMonitor监听的对象属性需要被@Trace装饰，未被@Trace装饰的属性的变化无法被监听。@SyncMonitor可以同时监听多个属性，这些属性之间用','隔开。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public name: string = 'Tom';
  6. @Trace public region: string = 'North';
  7. @Trace public job: string = 'Teacher';
  8. public age: number = 25;

  10. // name被@Trace装饰，能够监听变化
  11. @SyncMonitor('name')
  12. onNameChange(monitor: IMonitor) {
  13. hilog.info(0xFF00, 'testTag', '%{public}s',
  14. `name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  15. }

  17. // age未被@Trace装饰，不能监听变化
  18. @SyncMonitor('age')
  19. onAgeChange(monitor: IMonitor) {
  20. hilog.info(0xFF00, 'testTag', '%{public}s',
  21. `age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  22. }

  24. // region与job均被@Trace装饰，能够监听变化
  25. @SyncMonitor('region', 'job')
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
* @SyncMonitor可以监听深层属性的变化，该深层属性需要被@Trace装饰。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Inner {
  5. @Trace public num: number = 0;
  6. }

  8. @ObservedV2
  9. class Outer {
  10. public inner: Inner = new Inner();

  12. @SyncMonitor('inner.num')
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
* 在继承类场景下，可以在继承链中对同一个属性进行多次监听，父子类中定义的@SyncMonitor回调均会被调用。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Base {
  5. @Trace public name: string;

  7. // 基类监听name属性
  8. @SyncMonitor('name')
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
  21. @SyncMonitor('name')
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
  40. this.derived.name = 'BBB'; // onDerivedNameChange方法会调用，父类的onBaseNameChange也会回调
  41. })
  42. }
  43. }
  44. }
  ```

### 通用监听能力

@SyncMonitor还有一些通用的监听能力。

* @SyncMonitor支持对数组项进行监听，包括多维数组，对象数组。@SyncMonitor支持使用通配符监听由调用Array的API引起的变化，比如copyWithin, fill, sort, push。
* @SyncMonitor可以观察由调用内置类型Map，Date和Set的API引起的变化，例如，如果调用set、add、delete修改数据集合，则将执行监听函数。Map和Set中对应key的变化，不会执行监听函数，框架会打印错误日志。

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
  21. @SyncMonitor('dimensionTwo.0.0', 'dimensionTwo.1.1')
  22. onDimensionTwoChange(monitor: IMonitor) {
  23. monitor.dirty.forEach((path: string) => {
  24. hilog.info(0xFF00, 'testTag', '%{public}s',
  25. `dimensionTwo path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  26. })
  27. }

  29. // dimensionThree为三维简单类型数组，且被@Trace装饰，能够观测里面的元素变化
  30. @SyncMonitor('dimensionThree.0.0.0', 'dimensionThree.1.1.0')
  31. onDimensionThreeChange(monitor: IMonitor) {
  32. monitor.dirty.forEach((path: string) => {
  33. hilog.info(0xFF00, 'testTag', '%{public}s',
  34. `dimensionThree path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  35. })
  36. }

  38. // Info类中属性name、age均被@Trace装饰，能够监听到变化
  39. @SyncMonitor('infoArr.0.name', 'infoArr.1.age')
  40. onInfoArrPropertyChange(monitor: IMonitor) {
  41. monitor.dirty.forEach((path: string) => {
  42. hilog.info(0xFF00, 'testTag', '%{public}s',
  43. `infoArr path:${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  44. })
  45. }

  47. // infoArr被@Trace装饰，能够监听到infoArr整体赋值的变化
  48. @SyncMonitor('infoArr')
  49. onInfoArrChange(monitor: IMonitor) {
  50. hilog.info(0xFF00, 'testTag', '%{public}s', `infoArr whole change`);
  51. }

  53. // 能够监听到infoArr的长度变化
  54. @SyncMonitor('infoArr.length')
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
* 对象整体改变，但监听的属性不变时，不触发@SyncMonitor回调。

  下面的示例按照Step1-Step2-Step3的顺序点击，表现为代码注释中的行为。

  如果只点击Step2或Step3，改变name、age的值，此时会触发onNameChange和onAgeChange方法。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public person: Person;

  7. @SyncMonitor('person.name')
  8. onNameChange(monitor: IMonitor) {
  9. hilog.info(0xFF00, 'testTag', '%{public}s',
  10. `name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  11. }

  13. @SyncMonitor('person.age')
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
* 在一次事件中多次改变被@SyncMonitor监听的属性，@SyncMonitor回调将在该属性每次改变时被调用。

  @SyncMonitor与@Monitor行为不一样，@Monitor只被调用一次并以最后一次修改为准。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Frequency {
  5. @Trace public count: number = 0;

  7. @SyncMonitor('count')
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
  32. this.frequency.count = 1000; // 最终会触发onCountChange方法
  33. })
  34. }
  35. }
  36. }
  ```

  点击change count to 1000后，onCountChange方法被触发1000次，日志输出：

  ```
  1. count change from 0 to 1
  2. count change from 1 to 2
  3. count change from 2 to 3
  4. ...
  5. count change from 999 to 1000
  ```

  只点击change count to 0 then to 1000后，onCountChange 被触发1001次，日志输出：

  ```
  1. count change from 0 to 999
  2. count change from 999 to 998
  3. ...
  4. count change from 1 to 0
  5. count change from 0 to 1000
  ```

  与@Monitor的区别：在上面的例子中将@SyncMonitor('count')替换为@Monitor('count')。按下任一按钮，@Monitor装饰的监听函数仅执行一次。
* 如果@SyncMonitor观察的多个属性在不同的赋值操作中发生改变，则每次赋值操作后都会立即调用@SyncMonitor回调函数。这与@Monitor的行为相反，后者只调用一次并使用最后一次更改的值。调用Array的API可能会一次改变多个数组元素，但每次只会触发一次@SyncMonitor装饰的回调函数。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';
  2. @Entry
  3. @ComponentV2
  4. struct DocSampleArrayMultiPath {
  5. @Local arr: Array<number> = [0, 1, 2, 3, 4, 5]

  7. @SyncMonitor('arr','arr.0','arr.1','arr.2','arr.3','arr.4','arr.length')
  8. onArrChangedSync(m: IMonitor) {
  9. hilog.info(0xFF00, 'testTag', '%{public}s', `@SyncMonitor: arr: [${this.arr}], m.dirty: [${m.dirty}]`);
  10. }

  12. build() {
  13. Column() {
  14. Button('Change array by making separate assignments')
  15. .onClick(() => {
  16. hilog.info(0xFF00, 'testTag', 'arr[1] assign  ...');
  17. this.arr[1] = 100;
  18. hilog.info(0xFF00, 'testTag', 'arr[2] assign  ...');
  19. this.arr[2] = 200;
  20. hilog.info(0xFF00, 'testTag', '.. done');
  21. })

  23. Button('Change array with array functions')
  24. .onClick(() => {
  25. hilog.info(0xFF00, 'testTag', 'splice execute ...');
  26. // changes arr from [ 0, 1, 2, 3, 4, 5 ] to [ 0, 100, 101, 102, 5]
  27. this.arr.splice(1, 4, 100, 101, 102);
  28. hilog.info(0xFF00, 'testTag', 'shift execute ...');
  29. // changes arr from [ 1, 100, 101, 102, 5] to [ 100, 101, 102, 5]
  30. this.arr.shift()
  31. hilog.info(0xFF00, 'testTag', '.. done');
  32. })
  33. }
  34. }
  35. }
  ```

  启动应用。按下Change array by making separate assignments按钮，代码执行流程如下:

  1. 执行onClick；
  2. 打印arr[1] assign ...；
  3. 执行onArrChangedSync，打印日志: '@SyncMonitor: arr: [0,100,2,3,4,5], m.dirty [arr.1]'；
  4. 打印日志arr[2] assign ...；
  5. 执行onArrChangedSync, 打印日志: '@SyncMonitor: arr: [0,100,200,3,4,5], m.dirty: [arr.2]'；
  6. onClick执行完毕，打印日志.. done。

  启动应用。按下Change array with array functions按钮，代码执行流程如下:

  1. 执行onClick；
  2. 打印splice execute ...；
  3. 执行onArrChangedSync, 打印日志'@SyncMonitor: arr: [0,100,101,102,5], m.dirty: [arr.1,arr.2,arr.3,arr.4,arr.length]'；
  4. 打印日志shift execute ...；
  5. 执行onArrChangedSync， 打印日志'@SyncMonitor: arr: [100,101,102,5], m.dirty: [arr.0,arr.1,arr.2,arr.3,arr.4,arr.length]'；
  6. 打印.. done日志。

## 观察路径中的通配符

@SyncMonitor路径中的通配符(\*)可用于在任何对象属性或任何数组项更改时触发回调。

### 被观察属性变更或对象赋值时，监听函数自动执行

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. @ObservedV2
3. class ClassA {
4. @Trace public propA : number = 8;
5. @Trace public propB : number = 99;

7. constructor(a : number, b: number) {
8. this.propA = a;
9. this.propB = b;
10. }
11. }

13. @Entry
14. @ComponentV2 struct DocSampleClass {
15. @Local cls : ClassA = new ClassA(100, 100);

17. @SyncMonitor('cls.*')
18. onClsChanged(m: IMonitor) {
19. hilog.info(0xFF00, 'testTag', '%{public}s', `### onClsChanged, dirty: ${m.dirty.toString()}`);
20. }

22. build() {
23. Column() {
24. Divider()
25. Button(`#1 Change propA ${this.cls.propA}: +=1;`)
26. .onClick(() => {
27. this.cls.propA += 1;
28. })
29. Button(`#2 Change propB ${this.cls.propB}: +=1`)
30. .onClick(() => {
31. this.cls.propB += 1;
32. })
33. Button(`#3 Assign class object`)
34. .onClick(() => {
35. this.cls = new ClassA(-200, -200);
36. })
37. }
38. .border({ style: BorderStyle.Solid, width: 2, color: Color.Green })
39. }
40. }
```

点击按钮#1或#2（更新被监听对象cls的属性）时，m.dirty的值将相同，包含m.dirty==['cls.\*']。框架无法准确告知是哪个属性触发了监听函数的执行。

对于按钮#3（给cls属性赋予新对象），框架会将cls传递给脏属性数组，即m.dirty==['cls.\*']。

```
1. 点击Button #1, 输出日志：
2. ### onClsChanged, dirty: cls.*

4. 点击Button #2 输出日志：
5. ### onClsChanged, dirty: cls.*

7. 点击Button #3 输出日志：
8. ### onClsChanged, dirty: cls.*
```

### 数组项更改及数组赋值时，监听函数会自动执行

同步监听的观察路径：@SyncMonitor('arrayOrPerson.\*')

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. @ObservedV2
3. class Person {
4. @Trace public firstName: string;
5. @Trace public lastName: string;
6. constructor(first: string = 'no first', last: string = 'no last') {
7. this.firstName = first;
8. this.lastName = last;
9. }
10. }

12. @ObservedV2
13. class ArrayOfPerson extends Array<Person> {}

15. @Entry
16. @ComponentV2
17. struct DocSampleArray {
18. @Local arrayOrPerson: ArrayOfPerson =
19. [new Person('Adrian'), new Person('Andrew'), new Person('Aaliyah'), new Person('Amir'), new Person('Angel')];

21. @SyncMonitor('arrayOrPerson.*')
22. arrayOfPersonMonitor(monitor: IMonitor) {
23. hilog.info(0xFF00, 'testTag', '%{public}s', `### SyncMonitor dirty: ${monitor.dirty.toString()}`);
24. }

26. build() {
27. Column() {
28. Button('#1 arrayOfPerson.push')
29. .onClick(() => {
30. this.arrayOrPerson.push(new Person('Austin'));
31. })
32. Button('#2 arrayOfPerson.splice(0,1,P)')
33. .onClick(() => {
34. this.arrayOrPerson.splice(0, 1, new Person('Addison'));
35. })
36. Button('#3 arrayOfPerson.assign new [1]')
37. .onClick(() => {
38. this.arrayOrPerson[1] = new Person('Amari');
39. })
40. Button('#4 arrayOfPerson shift')
41. .onClick(() => {
42. this.arrayOrPerson.shift();
43. })
44. Button('#5 arrayOfPerson length change')
45. .onClick(() => {
46. this.arrayOrPerson.length = this.arrayOrPerson.length +1;
47. })
48. Button('#6 arrayOfPerson  = new Array')
49. .onClick(() => {
50. this.arrayOrPerson = new ArrayOfPerson(new Person('Adrian'), new Person('Andrew'))
51. })
52. Button('#7 arrayOfPerson [1] last name')
53. .onClick(() => {
54. this.arrayOrPerson[1].lastName += '~'
55. })
56. }
57. }
58. }
```

当按下按钮1-6时，监听函数会被触发:

```
1. ### SyncMonitor dirty: arrayOrPerson.*
```

按下按钮7，监听函数不会被调用，因为没有数组项被更改。

### 嵌套被观察对象属性更改时，监听函数会执行

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. @ObservedV2
3. class Person {
4. @Trace public firstName: string = 'first';
5. @Trace public lastName: string = 'last';
6. }
7. @ObservedV2
8. class Class1 {
9. @Trace public person: Person = new Person();
10. }
11. @ObservedV2
12. class Class0 {
13. @Trace public class1: Class1 = new Class1();
14. }

16. @Entry
17. @ComponentV2
18. export struct DocSampleNestedClass {
19. @Local class0 : Class0 | number = new Class0();

21. @SyncMonitor('class0.class1.person.*')
22. onPersonChange(info: IMonitor) {
23. hilog.info(0xFF00, 'testTag', '%{public}s', '### onPersonChange, dirty: ' + info.dirty.toString());
24. }

26. build() {
27. Column() {
28. Button('#1 Class0 = new Class')
29. .onClick(() => {
30. this.class0 = new Class0();
31. })
32. Button('#2 Class0 = new Class, keep Class1')
33. .onClick(() => {
34. let newClass0 = new Class0();
35. newClass0.class1.person = (this.class0 as Class0).class1.person;
36. this.class0 = newClass0;
37. })
38. Button('#3 Class0.class1 = new Class1')
39. .onClick(() => {
40. (this.class0 as Class0).class1 = new Class1();
41. })
42. Button('#4 Class0.class1.person = new Person')
43. .onClick(() => {
44. (this.class0 as Class0).class1.person = new Person();
45. })
46. Button('#5 Class0....person.last update')
47. .onClick(() => {
48. if (typeof (this.class0) === 'object') {
49. (this.class0 as Class0).class1.person.lastName += '+';
50. } else {
51. }
52. })
53. Button('#6 Class0 toggle number <=> new Class0')
54. .onClick(() => {
55. this.class0 = (typeof (this.class0) === 'object') ? 500 : new Class0();
56. })
57. }
58. }
59. }
```

启动应用程序。当按下按钮#1 Class0 = new Class时，由于Person对象已更改，监听函数将被触发。

```
1. ### onPersonChange, dirty: class0.class1.person.*
```

启动应用程序。当按下按钮#2 Class0 = new Class, keep Class1时，由于被监听的Person对象保持不变，监听函数不会执行。

启动应用程序。当按下按钮#3 Class0.class1 = new Class1时，由于Person对象已更改，监听函数将被触发。

```
1. ### onPersonChange, dirty: class0.class1.person.*
```

启动应用程序。当按下按钮#4 Class0.class1.person = new Person时，由于Person对象已更改，监听函数将被触发：

```
1. ### onPersonChange, dirty: class0.class1.person.*
```

启动应用程序。当按下按钮#5 Class0....person.last update时，由于Person对象属性已更改，监听函数将被触发：

```
1. ### onPersonChange, dirty: class0.class1.person.*
```

启动应用程序。当按下按钮#6 Class0 toggle number <=> new Class0时，由于路径值从Person类引用更改为undefined，监听函数将被触发：

```
1. ### onPersonChange, dirty: class0.class1.person.*
```

第二次按下同一个按钮#6 Class0 toggle number <=> new Class0时，框架将再次调用监听函数并通知它对象已从undefined更改为Person类的实例。

@Monitor和@SyncMonitor对路径变为不可用的处理方式存在差异。

@SyncMonitor在两种情况下都会触发执行 - 当路径变为不可用时和当路径再次变为可用时。

@Monitor只触发一种情况的执行 - 仅当路径再次变为可用时。当路径上的对象被赋值为undefined时，@Monitor装饰的回调函数将不会触发执行。

如果在示例应用程序中有@Monitor('class0.class1.person')，那么当路径变为不可用时，@Monitor将无法监听这个变化。当以this.class0 = 500的方式更改值时，@Monitor装饰的回调函数不会被触发。当再次为Class0赋值时，即执行this.class0 = new Class0，@Monitor装饰的回调函数将被触发。

### 模糊监听数组项的变化

嵌套的被观察对象的属性更改时，会执行监听函数。

观察数组及数组项更改时，也会执行监听函数。

在以下例子中，有两个@SyncMonitor监听的路径分别为：topArray.1.\*和topArray.\*。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Person {
5. @Trace firstName: string = 'first';
6. @Trace lastName: string = 'last';
7. constructor(first: string = 'no first', last: string = 'no last') {
8. this.firstName = first;
9. this.lastName = last;
10. }
11. }

13. @ObservedV2
14. class ArrayOfPerson extends Array<Person> {}

16. @ObservedV2
17. class TopArray extends Array<ArrayOfPerson> {}

19. @Entry
20. @ComponentV2
21. struct DocSampleArrayOfArrays {
22. @Local topArray: TopArray = this.makeNewTopArray();

24. @SyncMonitor('topArray.1.*')
25. topArrayMonitor1Star(monitor: IMonitor) {
26. hilog.info(0xFF00, 'testTag', '%{public}s', `TopArray[1]: ${monitor.dirty.toString()}`);
27. }

29. @SyncMonitor('topArray.*')
30. topArrayMonitorStar(monitor: IMonitor) {
31. hilog.info(0xFF00, 'testTag', '%{public}s', `TopArray: ${monitor.dirty.toString()}`);
32. }

34. makeNewTopArray(): TopArray {
35. return new TopArray(
36. new ArrayOfPerson(new Person('Adrian'), new Person('Andrew'), new Person('Aaliyah'), new Person('Amir'), new Person('Angel')),
37. new ArrayOfPerson(new Person('Carter'), new Person('Charlie'), new Person('Cooper'), new Person('Cole'), new Person('Callie')),
38. new ArrayOfPerson(new Person('Danile'), new Person('Dasy'), new Person('Dawson'), new Person('Dana'), new Person('Dalton'))
39. );
40. }

42. build() {
43. Column() {
44. Text('Array of Arrays')
45. .fontSize(30)

47. // 因为脏的路径中包含'topArray.1'，会触发路径为'topArray.1.*'的@SyncMonitor的回调
48. // 因为脏的路径中包含'topArray'，会触发路径为'topArray.*'的@SyncMonitor的回调
49. Button('topArray = new TopArray')
50. .onClick(() => {
51. this.topArray = this.makeNewTopArray();
52. })

54. // 因为脏路径被包含在'topArray.1.*'中，会触发路径为'topArray.1.*'的@SyncMonitor的回调
55. // 因为脏路径没被包含在'topArray.*'中，不会触发路径为'topArray.*'的@SyncMonitor的回调
56. Button('topArray[1][0] = new Person')
57. .onClick(() => {
58. this.topArray[1][0] = new Person();
59. })

61. // 不会触发路径为 'topArray.1.*'的@SyncMonitor的回调
62. // 不会触发路径为'topArray.*'的@SyncMonitor的回调
63. Button('topArray[0][1] = new Person')
64. .onClick(() => {
65. this.topArray[0][1] = new Person();
66. })

68. // 因为脏路径被包含在'topArray.1.*'中，会触发路径为'topArray.1.*'的@SyncMonitor的回调
69. // 因为脏路径没被包含在'topArray.*'中，不会触发路径为'topArray.*'的@SyncMonitor的回调
70. Button('topArray[1].push')
71. .onClick(() => {
72. this.topArray[1].push(new Person());
73. })

75. // 因为脏的路径中包含'topArray.1'，会触发路径为'topArray.1.*'的@SyncMonitor的回调
76. // 因为脏的路径中包含'topArray.*'，会触发路径为'topArray.*'的@SyncMonitor的回调
77. Button('topArray.shift (size>2)')
78. .onClick(() => {
79. this.topArray.shift();
80. })

82. // 不会触发路径为'topArray.1.*'的@SyncMonitor的回调
83. // 因为脏的路径中包含'topArray.*'，会触发路径为'topArray.*'的@SyncMonitor的回调
84. Button('topArray[0] = new ArrayOfPerson')
85. .onClick(() => {
86. this.topArray[0] = new ArrayOfPerson(new Person(), new Person());
87. })

89. // 不会触发路径为'topArray.1.*'的@SyncMonitor的回调
90. // 不会触发路径为'topArray.*'的@SyncMonitor的回调
91. Button('topArray[1][0].last update')
92. .onClick(() => {
93. this.topArray[1][0].lastName += '~';
94. })

96. // 不会触发路径为'topArray.1.*'的@SyncMonitor的回调
97. // 因为脏的路径中包含'topArray'，会触发路径为'topArray.*'的@SyncMonitor的回调
98. Button('topArray = new TopArray, keep [1]')
99. .onClick(() => {
100. let newTop = this.makeNewTopArray();
101. newTop[1] = this.topArray[1];
102. this.topArray = newTop;
103. })

105. // 不会触发路径为'topArray.1.*'的@SyncMonitor的回调
106. // 因为脏的路径中包含'topArray.*'，会触发路径为'topArray.*'的@SyncMonitor的回调
107. Button('topArray.push, +0, +1')
108. .onClick(() => {
109. this.topArray.push(new ArrayOfPerson(new Person(), new Person()));
110. })
111. }
112. }
113. }
```

## 限制条件

使用@SyncMonitor需要注意如下限制条件：

* 不建议在一个类中对同一个属性进行多次@SyncMonitor的监听。当一个类中存在对一个属性的多次监听时，只有最后一个定义的监听方法会生效。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public name: string = 'Tom';

  7. @SyncMonitor('name')
  8. onNameChange(monitor: IMonitor) {
  9. hilog.info(0xFF00, 'testTag', '%{public}s', `onNameChange`);
  10. }

  12. @SyncMonitor('name')
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
* 当@SyncMonitor传入多个路径参数时，以参数的全拼接结果判断是否重复监听。全拼接时会在参数间加空格，以区分不同参数。例如，'ab', 'c'的全拼接结果为'ab c'，'a', 'bc'的全拼接结果为'a bc'，二者全拼接不相等。以下示例中，SyncMonitor 1、SyncMonitor 2与SyncMonitor 3都监听了name属性的变化。由于SyncMonitor 2与SyncMonitor 3的入参全拼接相等（都为'name position'），因此SyncMonitor 2不生效，仅SyncMonitor 3生效。当name属性变化时，将同时触发onNameAgeChange与onNamePositionChangeDuplicate方法。但请注意，SyncMonitor 2与SyncMonitor 3的写法仍然被视作在一个类中对同一个属性进行多次@SyncMonitor的监听，这是不建议的。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. @ObservedV2
  4. class Info {
  5. @Trace public name: string = 'Tom';
  6. @Trace public age: number = 25;
  7. @Trace public position: string = 'North';

  9. @SyncMonitor('name', 'age') // SyncMonitor 1
  10. onNameAgeChange(monitor: IMonitor) {
  11. monitor.dirty.forEach((path: string) => {
  12. hilog.info(0xFF00, 'testTag', '%{public}s',
  13. `onNameAgeChange path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  14. });
  15. }

  17. @SyncMonitor('name', 'position') // SyncMonitor 2
  18. onNamePositionChange(monitor: IMonitor) {
  19. monitor.dirty.forEach((path: string) => {
  20. hilog.info(0xFF00, 'testTag', '%{public}s',
  21. `onNamePositionChange path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
  22. });
  23. }

  25. // 重复监听name、position，仅最后定义的生效
  26. @SyncMonitor('name', 'position') // SyncMonitor 3
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
* @SyncMonitor的参数需要为监听属性名的字符串，仅可以使用字符串字面量，不支持const常量、enum枚举值及变量作为参数。如果使用const常量、enum枚举值及变量作为参数，会编译报错，如下提供用例展示@SyncMonitor正常使用场景。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. const propB: string = 'propB'; // const常量

  5. enum ENUM {
  6. propC = 'PropC' // enum枚举值
  7. };
  8. let propD: string = 'propD'; // 变量

  10. @ObservedV2
  11. class Info {
  12. @Trace public propA: number = 0;
  13. @Trace public propB: number = 0;
  14. @Trace public propC: number = 0;
  15. @Trace public propD: number = 0;

  17. // @SyncMonitor仅支持字符串字面量
  18. @SyncMonitor('propA')
  19. onPropAChange(monitor: IMonitor) {
  20. hilog.info(0xFF00, 'testTag', '%{public}s', `propA change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  21. }

  23. // @SyncMonitor入参类型为const常量，编译会报错，提示`Only constant expressions are supported as parameters in '@SyncMonitor'. Variables are not allowed.`
  24. @SyncMonitor(propB)
  25. onPropBChange(monitor: IMonitor) {
  26. hilog.info(0xFF00, 'testTag', '%{public}s', `propB change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  27. }

  29. // @SyncMonitor入参类型为enum枚举值，编译会报错，提示`Only constant expressions are supported as parameters in '@SyncMonitor'. Variables are not allowed.`
  30. @SyncMonitor(ENUM.propC)
  31. onPropCChange(monitor: IMonitor) {
  32. hilog.info(0xFF00, 'testTag', '%{public}s', `propC change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  33. }

  35. // @SyncMonitor入参类型为变量，编译会报错，提示`Only constant expressions are supported as parameters in '@SyncMonitor'. Variables are not allowed.`
  36. @SyncMonitor(propD)
  37. onPropDChange(monitor: IMonitor) {
  38. hilog.info(0xFF00, 'testTag', '%{public}s', `propD change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  39. }
  40. }

  42. @Entry
  43. @ComponentV2
  44. struct Index {
  45. info: Info = new Info();

  47. build() {
  48. Column() {
  49. Button('Change propA')
  50. .onClick(() => {
  51. this.info.propA++; // 能够触发onPropAChange方法
  52. })
  53. }
  54. }
  55. }
  ```
* 建议开发者避免在@SyncMonitor中再次更改被监听的属性，这会导致无限循环。

  ```
  1. @ObservedV2
  2. class Info {
  3. @Trace count: number = 0;
  4. @SyncMonitor('count')
  5. onCountChange(monitor: IMonitor) {
  6. this.count++; // 应避免这种写法，会导致无限循环
  7. }
  8. }
  ```

## 使用场景

### 监听深层属性变化

@SyncMonitor可以监听深层属性的变化，并能够根据更改前后的值做分类处理。

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

12. @SyncMonitor('info.value')
13. onValueChange(monitor: IMonitor) {
14. let lastValue: number = monitor.value()?.before as number;
15. let curValue: number = monitor.value()?.now as number;
16. if (lastValue != 0) {
17. let diffPercent: number = (curValue - lastValue) / lastValue;
18. if (diffPercent > 0.1) {
19. this.color = Color.Red;
20. this.fontSize = 50;
21. } else if (diffPercent < -0.1) {
22. this.color = Color.Green;
23. this.fontSize = 40;
24. } else {
25. this.color = Color.Black;
26. this.fontSize = 45;
27. }
28. }
29. }
30. }

32. @Entry
33. @ComponentV2
34. struct Index {
35. textStyle: UIStyle = new UIStyle();

37. build() {
38. Column() {
39. Text(`Important Value: ${this.textStyle.info.value}`)
40. .fontColor(this.textStyle.color)
41. .fontSize(this.textStyle.fontSize)
42. Button('change!')
43. .onClick(() => {
44. this.textStyle.info.value = Math.floor(Math.random() * 100) + 1;
45. })
46. }
47. }
48. }
```

## 常见问题

### 自定义组件中@SyncMonitor对变量监听的生效及失效时间

当@SyncMonitor定义在@ComponentV2装饰的自定义组件中时，@SyncMonitor会在状态变量初始化完成之后生效，并在组件销毁时失效。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. @Trace public message: string = 'not initialized';

7. constructor() {
8. hilog.info(0xFF00, 'testTag', '%{public}s', 'in constructor message change to initialized');
9. this.message = 'initialized';
10. }
11. }

13. @ComponentV2
14. struct Child {
15. @Param info: Info = new Info();

17. @SyncMonitor('info.message')
18. onMessageChange(monitor: IMonitor) {
19. hilog.info(0xFF00, 'testTag', '%{public}s',
20. `Child message change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
21. }

23. aboutToAppear(): void {
24. this.info.message = 'Child aboutToAppear';
25. }

27. aboutToDisappear(): void {
28. hilog.info(0xFF00, 'testTag', '%{public}s', 'Child aboutToDisappear');
29. this.info.message = 'Child aboutToDisappear';
30. }

32. build() {
33. Column() {
34. Text('Child')
35. Button('change message in Child')
36. .onClick(() => {
37. this.info.message = 'Child click to change Message';
38. })
39. }
40. .borderColor(Color.Red)
41. .borderWidth(2)

43. }
44. }

46. @Entry
47. @ComponentV2
48. struct Index {
49. @Local info: Info = new Info();
50. @Local flag: boolean = false;

52. @SyncMonitor('info.message')
53. onMessageChange(monitor: IMonitor) {
54. hilog.info(0xFF00, 'testTag', '%{public}s',
55. `Index message change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
56. }

58. build() {
59. Column() {
60. Button('show/hide Child')
61. .onClick(() => {
62. this.flag = !this.flag
63. })
64. Button('change message in Index')
65. .onClick(() => {
66. this.info.message = 'Index click to change Message';
67. })
68. if (this.flag) {
69. Child({ info: this.info })
70. }
71. }
72. }
73. }
```

在上面的例子中，可以通过创建和销毁Child组件来观察定义在自定义组件中的@SyncMonitor的生效和失效时机。推荐按如下顺序进行操作：

* 当Index组件创建Info类实例时，日志输出in constructor message change to initialized。此时Index组件的@SyncMonitor还未初始化成功，因此不会监听到message的变化。
* 当Index组件创建完成，页面加载完成后，点击按钮'change message in Index'，此时Index组件中的@SyncMonitor能够监听到变化，日志输出Index message change from initialized to Index click to change Message。
* 点击按钮'show/hide Child'，创建Child组件，在Child组件初始化@Param装饰的变量以及@SyncMonitor之后，调用Child组件的aboutToAppear回调，改变message。此时Index组件与Child组件的@SyncMonitor均能监听到变化，日志输出Index message change from Index click to change Message to Child aboutToAppear以及Child message change from Index click to change Message to Child aboutToAppear。
* 点击按钮'change message in Child'，改变message。此时Index组件与Child组件的@SyncMonitor均能监听到变化，日志输出Index message change from Child aboutToAppear to Child click to change Message以及Child message change from Child aboutToAppear to Child click to change Message。
* 点击按钮'show/hide Child'，销毁Child组件，调用Child组件的aboutToDisappear回调，改变message。此时Index组件与Child组件的@SyncMonitor均能监听到变化，日志输出Child aboutToDisappear，Index message change from Child click to change Message to Child aboutToDisappear以及Child message change from Child click to change Message to Child aboutToDisappear。
* 点击按钮'change message in Index'，改变message。此时Child组件已销毁，其注册的@SyncMonitor监听也被解注册，仅有Index组件的@SyncMonitor能够监听到变化，日志输出Index message change from Child aboutToDisappear to Index click to change Message。

这表明Child组件中定义的@SyncMonitor监听随着Child组件的创建初始化生效，随着Child组件的销毁失效。

### 类中@SyncMonitor对变量监听的生效及失效时间

当@SyncMonitor定义在@ObservedV2装饰的类中时，@SyncMonitor会在类的实例创建完成后生效，在类的实例销毁时失效。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. @Trace public message: string = 'not initialized';

7. constructor() {
8. this.message = 'initialized';
9. }

11. @SyncMonitor('message')
12. onMessageChange(monitor: IMonitor) {
13. hilog.info(0xFF00, 'testTag', '%{public}s',
14. `message change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
15. }
16. }

18. @Entry
19. @ComponentV2
20. struct Index {
21. info: Info = new Info();

23. aboutToAppear(): void {
24. this.info.message = 'Index aboutToAppear';
25. }

27. build() {
28. Column() {
29. Button('change message')
30. .onClick(() => {
31. this.info.message = 'Index click to change message';
32. })
33. }
34. }
35. }
```

上面的例子中，@SyncMonitor会在info创建完成后生效，这个时机晚于类的constructor，早于自定义组件的aboutToAppear。当界面加载完成后，点击'change message'，修改message变量。此时日志输出信息如下：

```
1. message change from initialized to Index aboutToAppear
2. message change from Index aboutToAppear to Index click to change message
```

类中定义的@SyncMonitor随着类的销毁失效。而由于类的实际销毁释放依赖于垃圾回收机制，因此会出现即使所在自定义组件已经销毁，类却还未及时销毁，导致类中定义的@SyncMonitor仍在监听变化的情况。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class InfoWrapper {
5. public info?: Info;

7. constructor(info: Info) {
8. this.info = info;
9. }

11. @SyncMonitor('info.age')
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

在上面的例子中，当点击'change showFlag'切换if组件的条件时，Child组件会被销毁。此时，点击'change number'修改age的值时，可以通过日志观察到InfoWrapper中定义的@SyncMonitor回调仍然被触发了。这是因为此时自定义组件Child虽然执行了aboutToDisappear，但是其成员变量infoWrapper还没有被立刻回收，当变量发生变化时，依然能够调用到infoWrapper中定义的onInfoAgeChange方法，所以从现象上看@SyncMonitor回调仍会被触发。

借助垃圾回收机制去取消@SyncMonitor的监听是不稳定的，开发者可以采用以下如下方式去管理@SyncMonitor的失效时间：

将@SyncMonitor定义在自定义组件中。由于自定义组件在销毁时，状态管理框架会手动取消@SyncMonitor的监听，因此在自定义组件调用完aboutToDisappear，尽管自定义组件的数据不一定已经被释放，但@SyncMonitor回调已不会再被触发。与@Monitor不同的时，当自定义组件即将销毁时，主动置空@SyncMonitor监听的对象，@SyncMonitor依然能监听原监听目标的变化。

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

25. @SyncMonitor('infoWrapper.info.age')
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

### 正确设置@SyncMonitor入参

由于@SyncMonitor无法对入参做编译时校验，当前存在以下写法不符合@SyncMonitor监听条件但@SyncMonitor仍会触发的情况。开发者应当正确传入@SyncMonitor入参，不传入非状态变量，避免造成功能异常或行为表现不符合预期。

【反例1】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. @Trace public age: number = 24;

8. // 只运行监听状态变量age，监听非状态变量name，会编译告警，提示`Cannot observe non-existent variables or non-state variables, except in wildcard-based monitoring scenarios.`
9. @SyncMonitor('age', 'name')
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
27. this.info.age = 25; // 同时改变状态变量age和非状态变量name
28. this.info.name = 'Johny';
29. })
30. }
31. }
32. }
```

上面的代码中，由于@SyncMonitor入参传入非状态变量'name'，编译会告警。建议开发者去除对name属性的监听或者给name加上@Trace装饰成为状态变量。

当点击按钮同时更改状态变量age和非状态变量name时，会输出以下日志：

```
1. property path:age change from 24 to 25
```

【正例1】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. @Trace public age: number = 24;

8. // 仅监听状态变量age
9. @SyncMonitor('age')
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

【反例2】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. public name: string = 'John';
6. public age: number = 24;

8. get myAge() {
9. return this.age; // age为非状态变量
10. }

12. // 监听非@Computed装饰的getter访问器，编译会告警
13. @SyncMonitor('myAge')
14. onPropertyChange(monitor: IMonitor) {
15. monitor.dirty.forEach((path: string) => {
16. hilog.info(0xFF00, 'testTag', '%{public}s',
17. `property path:${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
18. })
19. }
20. }

22. @Entry
23. @ComponentV2
24. struct Index {
25. info: Info = new Info();

27. build() {
28. Column() {
29. Button('change age')
30. .onClick(() => {
31. this.info.age = 25; // 状态变量age改变
32. })
33. }
34. }
35. }
```

上面的代码中，@SyncMonitor的入参为一个getter访问器的名字，但该getter访问器本身并未被@Computed装饰，不是一个可被监听的变量。建议开发者给myAge添加@Computed装饰器或当getter访问器直接返回状态变量时，不监听getter访问器而是直接监听状态变量本身。

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
15. @SyncMonitor('myAge')
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

### 使用通配符的无效路径

有效的监听路径规则如下：

* 路径只能以\*结尾；
* \*不能出现在路径开头或路径内部；

以下路径均使用了无效的通配符。编译会报错。

* @SyncMonitor('\*.propA') - 错误，通配符不能位于路径开头
* @SyncMonitor('arr.\*.propA') - 错误，通配符不能位于路径中间
* @SyncMonitor('obsArr.\*.\*') - 错误，不允许使用双重通配符。任何属性或数组项都只支持一级
* @SyncMonitor('obsArr.\*\*') - 错误，属性或数组项名称无效\*\*
* @SyncMonitor('obsObj\*') - 错误，属性名称obsObj\*无效
* @SyncMonitor('obsObj.objObj2\*') - 错误，属性名称无效obsObj2\*

### 监听变量从可访问变为不可访问和从不可访问变为可访问

@Monitor仅会保存变量可访问时的值，当状态变量变为不可访问的状态时，并不会记录其值的变化。从API version 20开始，如果需要监听可访问到不可访问和不可访问到可访问的状态变化，可以使用[addMonitor](arkts-new-addmonitor-clearmonitor.md#监听变量从可访问到不访问和从不可访问到可访问)。

@SyncMonitor可以监听变量从可访问变为不可访问或从不可访问变为可访问的变化。在下面的例子中，点击三个Button，均会触发onChange的回调。

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

13. @SyncMonitor('user.age')
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
