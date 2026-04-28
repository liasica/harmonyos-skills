---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-param
title: @Param：组件外部输入
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理组件拥有的状态 > @Param：组件外部输入
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:84d1d3fedced4e6c30a2f89a7657178de9b4184ffe817256721813ea29e1ed75
---

为了增强子组件接受外部参数输入的能力，开发者可以使用@Param装饰器。

@Param不仅可以接受组件外部输入，还可以接受@Local的同步变化。在阅读本文档前，建议提前阅读：[@Local](arkts-new-local.md)。

说明

从API version 12开始，在@ComponentV2装饰的自定义组件中支持使用@Param装饰器。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Param表示组件从外部传入的状态，使得父子组件之间的数据能够进行同步：

* @Param装饰的变量支持本地初始化，但不允许在组件内部直接修改。
* 被@Param装饰的变量能够在初始化自定义组件时从外部传入，当数据源也是状态变量时，数据源的修改会同步给@Param。
* @Param可以接受任意类型的数据源，包括普通变量、状态变量、常量、函数返回值等。
* @Param装饰的变量变化时，会刷新该变量关联的组件。
* @Param支持对基本类型（如number、boolean、string、Object、class）、内嵌类型（如[Array](arkts-new-param.md#装饰array类型变量)、[Set](arkts-new-param.md#装饰set类型变量)、[Map](arkts-new-param.md#装饰map类型变量)、[Date](arkts-new-param.md#装饰date类型变量)），以及null、undefined和[联合类型](arkts-new-param.md#联合类型)进行观测。
* 对于复杂类型如类对象，@Param会接受数据源的引用。在组件内可以修改类对象中的属性，该修改会同步到数据源。
* @Param的观测能力仅限于被装饰的变量本身。详见[观察变化](arkts-new-param.md#观察变化)。

## 状态管理V1版本接受外部传入的装饰器的局限性

状态管理V1存在多种可接受外部传入的装饰器，常用的有[@State](arkts-state.md)、[@Prop](arkts-prop.md)、[@Link](arkts-link.md)、[@ObjectLink](arkts-observed-and-objectlink.md)。这些装饰器使用有限制且不易区分，不当使用会导致性能问题。

```
1. @Observed
2. class Region {
3. public x: number;
4. public y: number;

6. constructor(x: number, y: number) {
7. this.x = x;
8. this.y = y;
9. }
10. }

12. @Observed
13. class Info {
14. public region: Region;

16. constructor(x: number, y: number) {
17. this.region = new Region(x, y);
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State info: Info = new Info(0, 0);

26. build() {
27. Column() {
28. Button('change Info')
29. .onClick(() => {
30. this.info = new Info(100, 100);
31. })
32. Child({
33. region: this.info.region,
34. regionProp: this.info.region,
35. infoProp: this.info,
36. infoLink: this.info,
37. infoState: this.info
38. })
39. }
40. }
41. }

43. @Component
44. struct Child {
45. @ObjectLink region: Region;
46. @Prop regionProp: Region;
47. @Prop infoProp: Info;
48. @Link infoLink: Info;
49. @State infoState: Info = new Info(1, 1);

51. build() {
52. Column() {
53. Text(`ObjectLink region: ${this.region.x}-${this.region.y}`)
54. Text(`Prop regionProp: ${this.regionProp.x}-${this.regionProp.y}`)
55. }
56. }
57. }
```

[ParamDecoratorLimitations.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamDecoratorLimitations.ets#L30-L88)

在上面的示例中，@State仅能在初始化时接收info的引用，改变info之后无法同步。@Prop虽然能够进行单向同步，但是对于较复杂的类型来说，深拷贝性能较差。@Link能够接受传入的引用进行双向同步，但它必须要求数据源也是状态变量，因此无法接受info中的成员属性region。@ObjectLink能够接受类成员属性，但是要求该属性类型必须为@Observed装饰的类。装饰器的不同限制使得父子组件之间的传值规则复杂、不易使用。因此推出@Param装饰器，表示组件从外部传入的状态。

## 装饰器说明

| @Param变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 能否本地修改 | 否。若需要修改值，可使用@Param搭配[@Once](arkts-new-once.md)修改子组件的本地值。或通过[@Event](arkts-new-event.md)装饰器，修改@Param数据源的值。 |
| 同步类型 | 由父到子单向同步。 |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum等基本类型以及Array、Date、Map、Set等内嵌类型。支持null、undefined以及联合类型。 |
| 被装饰变量的初始值 | 允许本地初始化，若不在本地初始化，则需要和[@Require](arkts-require.md)装饰器一起使用，要求必须从外部传入初始化。 |

## 变量传递

| 传递规则 | 说明 |
| --- | --- |
| 从父组件初始化 | @Param装饰的变量允许本地初始化，若无本地初始化则必须从外部传入初始化。当同时存在本地初始值与外部传入值时，优先使用外部传入值进行初始化。 |
| 初始化子组件 | @Param装饰的变量可以初始化子组件中@Param装饰的变量。 |
| 同步 | @Param可以和父组件传入的状态变量数据源（即@Local或@Param装饰的变量）进行同步，当数据源发生变化时，会将修改同步给子组件的@Param。 |

## 观察变化

使用@Param装饰的变量具有被观测变化的能力。当装饰的变量发生变化时，会触发该变量绑定的UI组件刷新。

* 当装饰的变量类型为boolean、string、number类型时，可观察数据源同步变化。

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Index {
  4. // 点击的次数
  5. @Local count: number = 0;
  6. @Local message: string = 'Hello';
  7. @Local flag: boolean = false;

  9. build() {
  10. Column() {
  11. Text(`Local ${this.count}`)
  12. Text(`Local ${this.message}`)
  13. Text(`Local ${this.flag}`)
  14. Button('change Local')
  15. .onClick(() => {
  16. // 对数据源的更改会同步给子组件
  17. this.count++;
  18. this.message += ' World';
  19. this.flag = !this.flag;
  20. })
  21. Child({
  22. count: this.count,
  23. message: this.message,
  24. flag: this.flag
  25. })
  26. }
  27. }
  28. }

  30. @ComponentV2
  31. struct Child {
  32. @Require @Param count: number;
  33. @Require @Param message: string;
  34. @Require @Param flag: boolean;

  36. build() {
  37. Column() {
  38. Text(`Param ${this.count}`)
  39. Text(`Param ${this.message}`)
  40. Text(`Param ${this.flag}`)
  41. }
  42. }
  43. }
  ```

  [ParamObserveChangeVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamObserveChangeVariable.ets#L30-L74)
* 当装饰的变量类型为类对象时，仅可以观察到对类对象整体赋值的变化，无法直接观察到对类成员属性赋值的变化，对类成员属性的观察依赖[@ObservedV2](arkts-new-observedv2-and-trace.md)和[@Trace](arkts-new-observedv2-and-trace.md)装饰器，也可以使用[makeObserved](arkts-new-makeobserved.md)将该对象变为可观察对象。

  ```
  1. class RawObject {
  2. public name: string;

  4. constructor(name: string) {
  5. this.name = name;
  6. }
  7. }

  9. @ObservedV2
  10. class ObservedObject {
  11. @Trace public name: string;

  13. constructor(name: string) {
  14. this.name = name;
  15. }
  16. }

  18. @Entry
  19. @ComponentV2
  20. struct Index {
  21. @Local rawObject: RawObject = new RawObject('rawObject');
  22. @Local observedObject: ObservedObject = new ObservedObject('observedObject');

  24. build() {
  25. Column() {
  26. Text(`${this.rawObject.name}`)
  27. Text(`${this.observedObject.name}`)
  28. Button('change object')
  29. .onClick(() => {
  30. // 对类对象整体的修改均能观察到
  31. this.rawObject = new RawObject('new rawObject');
  32. this.observedObject = new ObservedObject('new observedObject');
  33. })
  34. Button('change name')
  35. .onClick(() => {
  36. // @Local与@Param均不具备观察类对象属性的能力，因此对rawObject.name的修改无法观察到
  37. this.rawObject.name = 'new rawObject name';
  38. // 由于ObservedObject的name属性被@Trace装饰，因此对observedObject.name的修改能被观察到
  39. this.observedObject.name = 'new observedObject name';
  40. })
  41. Child({
  42. rawObject: this.rawObject,
  43. observedObject: this.observedObject
  44. })
  45. }
  46. }
  47. }

  49. @ComponentV2
  50. struct Child {
  51. @Require @Param rawObject: RawObject;
  52. @Require @Param observedObject: ObservedObject;

  54. build() {
  55. Column() {
  56. Text(`${this.rawObject.name}`)
  57. Text(`${this.observedObject.name}`)
  58. }
  59. }
  60. }
  ```

  [ParamObserveChangeClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamObserveChangeClass.ets#L30-L91)
* 装饰的变量为简单类型数组时，可观察数组整体或数组项变化。

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Index {
  4. @Local numArr: number[] = [1, 2, 3, 4, 5];
  5. @Local dimensionTwo: number[][] = [[1, 2, 3], [4, 5, 6]];

  7. build() {
  8. Column() {
  9. Text(`${this.numArr[0]}`)
  10. Text(`${this.numArr[1]}`)
  11. Text(`${this.numArr[2]}`)
  12. Text(`${this.dimensionTwo[0][0]}`)
  13. Text(`${this.dimensionTwo[1][1]}`)
  14. Button('change array item')
  15. .onClick(() => {
  16. this.numArr[0]++;
  17. this.numArr[1] += 2;
  18. this.dimensionTwo[0][0] = 0;
  19. this.dimensionTwo[1][1] = 0;
  20. })
  21. Button('change whole array')
  22. .onClick(() => {
  23. this.numArr = [5, 4, 3, 2, 1];
  24. this.dimensionTwo = [[7, 8, 9], [0, 1, 2]];
  25. })
  26. Child({
  27. numArr: this.numArr,
  28. dimensionTwo: this.dimensionTwo
  29. })
  30. }
  31. }
  32. }

  34. @ComponentV2
  35. struct Child {
  36. @Require @Param numArr: number[];
  37. @Require @Param dimensionTwo: number[][];

  39. build() {
  40. Column() {
  41. Text(`${this.numArr[0]}`)
  42. Text(`${this.numArr[1]}`)
  43. Text(`${this.numArr[2]}`)
  44. Text(`${this.dimensionTwo[0][0]}`)
  45. Text(`${this.dimensionTwo[1][1]}`)
  46. }
  47. }
  48. }
  ```

  [ParamObserveChangeArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamObserveChangeArray.ets#L30-L79)
* 当装饰的变量是嵌套类或对象数组时，@Param无法观察深层对象属性的变化。对深层对象属性的观测依赖@ObservedV2与@Trace装饰器。

  ```
  1. @ObservedV2
  2. class Region {
  3. @Trace public x: number;
  4. @Trace public y: number;

  6. constructor(x: number, y: number) {
  7. this.x = x;
  8. this.y = y;
  9. }
  10. }

  12. @ObservedV2
  13. class Info {
  14. @Trace public region: Region;
  15. @Trace public name: string;

  17. constructor(name: string, x: number, y: number) {
  18. this.name = name;
  19. this.region = new Region(x, y);
  20. }
  21. }

  23. @Entry
  24. @ComponentV2
  25. struct Index {
  26. @Local infoArr: Info[] = [new Info('Ocean', 28, 120), new Info('Mountain', 26, 20)];
  27. @Local originInfo: Info = new Info('Origin', 0, 0);

  29. build() {
  30. Column() {
  31. ForEach(this.infoArr, (info: Info) => {
  32. Row() {
  33. Text(`name: ${info.name}`)
  34. Text(`region: ${info.region.x}-${info.region.y}`)
  35. }
  36. })
  37. Row() {
  38. Text(`Origin name: ${this.originInfo.name}`)
  39. Text(`Origin region: ${this.originInfo.region.x}-${this.originInfo.region.y}`)
  40. }

  42. Button('change infoArr item')
  43. .onClick(() => {
  44. // 由于属性name被@Trace装饰，所以能够观察到
  45. this.infoArr[0].name = 'Win';
  46. })
  47. Button('change originInfo')
  48. .onClick(() => {
  49. // 由于变量originInfo被@Local装饰，所以能够观察到
  50. this.originInfo = new Info('Origin', 100, 100);
  51. })
  52. Button('change originInfo region')
  53. .onClick(() => {
  54. // 由于属性x、y被@Trace装饰，所以能够观察到
  55. this.originInfo.region.x = 25;
  56. this.originInfo.region.y = 25;
  57. })
  58. Child({
  59. infoArr: this.infoArr,
  60. originInfo: this.originInfo
  61. })
  62. }
  63. }
  64. }

  66. @ComponentV2
  67. struct Child {
  68. @Param infoArr: Info[] = [];
  69. @Param originInfo: Info = new Info('O', 0, 0);

  71. build() {
  72. Column() {
  73. ForEach(this.infoArr, (info: Info) => {
  74. Row() {
  75. Text(`name: ${info.name}`)
  76. Text(`region: ${info.region.x}-${info.region.y}`)
  77. }
  78. })
  79. Row() {
  80. Text(`Origin name: ${this.originInfo.name}`)
  81. Text(`Origin region: ${this.originInfo.region.x}-${this.originInfo.region.y}`)
  82. }
  83. }
  84. }
  85. }
  ```

  [ParamObserveChangeNestedClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamObserveChangeNestedClass.ets#L30-L116)
* 装饰的变量为内置类型时，可观察变量整体赋值和API调用的变化。

  | 类型 | 可观测变化的API |
  | --- | --- |
  | Array | push, pop, shift, unshift, splice, copyWithin, fill, reverse, sort |
  | Date | setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds |
  | Map | set, clear, delete |
  | Set | add, clear, delete |

## 限制条件

@Param装饰器存在以下使用限制：

* @Param装饰器只能在[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰器的自定义组件中使用。

  ```
  1. @ComponentV2
  2. struct MyComponent {
  3. @Param message: string = 'Hello World'; // 正确用法
  4. build() {
  5. }
  6. }
  7. @Component
  8. struct TestComponent {
  9. @Param message: string = 'Hello World'; // 错误用法，编译时报错
  10. build() {
  11. }
  12. }
  ```
* @Param装饰的变量表示组件外部输入，需要初始化。支持使用本地初始值或外部传入值进行初始化。当存在外部传入值时，优先使用外部传入值。不允许既不使用本地初始值，也不使用外部传入值。

  ```
  1. @ComponentV2
  2. struct ChildComponent {
  3. @Param param1: string = 'Initialize local';
  4. @Param param2: string = 'Initialize local and put in';
  5. @Require @Param param3: string;
  6. @Param param4: string; // 错误用法，外部未传入初始化且本地也无初始值，编译报错
  7. build() {
  8. Column() {
  9. Text(`${this.param1}`) // 本地初始化，显示Initialize local
  10. Text(`${this.param2}`) // 外部传入初始化，显示Put in
  11. Text(`${this.param3}`) // 外部传入初始化，显示Put in
  12. }
  13. }
  14. }
  15. @Entry
  16. @ComponentV2
  17. struct MyComponent {
  18. @Local message: string = 'Put in';
  19. build() {
  20. Column() {
  21. ChildComponent({
  22. param2: this.message,
  23. param3: this.message
  24. })
  25. }
  26. }
  27. }
  ```
* 使用@Param装饰的变量在子组件中无法被直接修改。但是，如果装饰的变量是对象类型，在子组件中可以修改对象的属性。

  ```
  1. @ObservedV2
  2. class Info {
  3. @Trace name: string;
  4. constructor(name: string) {
  5. this.name = name;
  6. }
  7. }
  8. @Entry
  9. @ComponentV2
  10. struct Index {
  11. @Local info: Info = new Info('Tom');
  12. build() {
  13. Column() {
  14. Text(`Parent info.name ${this.info.name}`)
  15. Button('Parent change info')
  16. .onClick(() => {
  17. // 父组件更改@Local变量，会同步子组件对应@Param变量
  18. this.info = new Info('Lucy');
  19. })
  20. Child({ info: this.info })
  21. }
  22. }
  23. }
  24. @ComponentV2
  25. struct Child {
  26. @Require @Param info: Info;
  27. build() {
  28. Column() {
  29. Text(`info.name: ${this.info.name}`)
  30. Button('change info')
  31. .onClick(() => {
  32. // 错误用法，不允许在子组件中更改@Param变量，编译时会报错
  33. this.info = new Info('Jack');
  34. })
  35. Button('Child change info.name')
  36. .onClick(() => {
  37. // 允许在子组件中更改对象中属性，该修改会同步到父组件数据源上，当属性被@Trace装饰时，可观测到对应UI刷新
  38. this.info.name = 'Jack';
  39. })
  40. }
  41. }
  42. }
  ```

## 使用场景

### 从父组件到子组件变量传递与同步

@Param能够接受父组件@Local或@Param传递的数据并与之变化同步。

```
1. @ObservedV2
2. class Region {
3. @Trace public x: number;
4. @Trace public y: number;

6. constructor(x: number, y: number) {
7. this.x = x;
8. this.y = y;
9. }
10. }

12. @ObservedV2
13. class Info {
14. @Trace public name: string;
15. @Trace public age: number;
16. @Trace public region: Region;

18. constructor(name: string, age: number, x: number, y: number) {
19. this.name = name;
20. this.age = age;
21. this.region = new Region(x, y);
22. }
23. }

25. @Entry
26. @ComponentV2
27. struct Index {
28. // 使用@Local装饰infoList数组，作为数据源传递给子组件的@Param。
29. @Local infoList: Info[] = [new Info('Alice', 8, 0, 0), new Info('Barry', 10, 1, 20), new Info('Cindy', 18, 24, 40)];

31. build() {
32. Column() {
33. ForEach(this.infoList, (info: Info) => {
34. MiddleComponent({ info: info })
35. })
36. // 修改数组元素及对象属性，触发MiddleComponent和SubComponent更新。
37. Button('change')
38. .onClick(() => {
39. this.infoList[0] = new Info('Atom', 40, 27, 90);
40. this.infoList[1].name = 'Bob';
41. this.infoList[2].region = new Region(7, 9);
42. })
43. }
44. }
45. }

47. @ComponentV2
48. struct MiddleComponent {
49. // 使用@Param接收父组件传入的Info对象，数据源变化时触发子组件更新。
50. @Require @Param info: Info;

52. build() {
53. Column() {
54. Text(`name: ${this.info.name}`)
55. Text(`age: ${this.info.age}`)
56. // 将Region对象继续传递给子组件的@Param。
57. SubComponent({ region: this.info.region })
58. }
59. }
60. }

62. @ComponentV2
63. struct SubComponent {
64. // @Param接收父组件传入的Region对象，数据源变化时触发子组件更新。
65. @Require @Param region: Region;

67. build() {
68. Column() {
69. Text(`region: ${this.region.x}-${this.region.y}`)
70. }
71. }
72. }
```

[ParamUseSceneParentToChild.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamUseSceneParentToChild.ets#L30-L103)

### 装饰Array类型变量

@Param装饰Array类型变量，可以观察到数据源对Array整体的赋值，以及调用Array的接口push, pop, shift, unshift, splice, copyWithin, fill, reverse, sort带来的变化。

```
1. @ComponentV2
2. struct Child {
3. // 使用@Param接收父组件传入的Array类型变量。
4. @Require @Param count: number[];

6. build() {
7. Column() {
8. ForEach(this.count, (item: number) => {
9. Text(`${item}`).fontSize(30)
10. Divider()
11. })
12. }
13. .width('100%')
14. }
15. }

17. @Entry
18. @ComponentV2
19. struct Index {
20. // 使用@Local装饰Array类型变量，作为数据源传递给子组件的@Param。
21. @Local count: number[] = [1, 2, 3];

23. build() {
24. Row() {
25. Column() {
26. Child({ count: this.count })
27. // 对数组整体重新赋值，触发子组件更新。
28. Button('init array').onClick(() => {
29. this.count = [9, 8, 7];
30. })
31. // 新增数组元素，触发子组件更新。
32. Button('push').onClick(() => {
33. this.count.push(0);
34. })
35. // 翻转数组元素，触发子组件更新。
36. Button('reverse').onClick(() => {
37. this.count.reverse();
38. })
39. // 使用同一元素填充数组，触发子组件更新。
40. Button('fill').onClick(() => {
41. this.count.fill(6);
42. })
43. }
44. .width('100%')
45. }
46. .height('100%')
47. }
48. }
```

[ParamUseSceneArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamUseSceneArray.ets#L30-L79)

### 装饰Date类型变量

@Param装饰Date类型变量，可以观察到数据源对Date整体的赋值，以及调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds带来的变化。

```
1. @ComponentV2
2. struct DateComponent {
3. // 使用@Param接收父组件传入的Date类型变量。
4. @Param selectedDate: Date = new Date('2024-01-01');

6. build() {
7. Column() {
8. DatePicker({
9. start: new Date('1970-1-1'),
10. end: new Date('2100-1-1'),
11. selected: this.selectedDate
12. })
13. }
14. }
15. }

17. @Entry
18. @ComponentV2
19. struct Index {
20. // 使用@Local装饰Date类型变量，作为数据源传递给子组件的@Param。
21. @Local parentSelectedDate: Date = new Date('2021-08-08');

23. build() {
24. Column() {
25. // 对Date类型变量整体重新赋值，触发子组件更新。
26. Button('parent update the new date')
27. .margin(10)
28. .onClick(() => {
29. this.parentSelectedDate = new Date('2023-07-07');
30. })
31. // 调用Date的setFullYear方法修改年份，触发子组件更新。
32. Button('increase the year by 1')
33. .margin(10)
34. .onClick(() => {
35. this.parentSelectedDate.setFullYear(this.parentSelectedDate.getFullYear() + 1);
36. })
37. // 调用Date的setMonth方法修改月份，触发子组件更新。
38. Button('increase the month by 1')
39. .margin(10)
40. .onClick(() => {
41. this.parentSelectedDate.setMonth(this.parentSelectedDate.getMonth() + 1);
42. })
43. // 调用Date的setDate方法修改日期，触发子组件更新。
44. Button('parent increase the day by 1')
45. .margin(10)
46. .onClick(() => {
47. this.parentSelectedDate.setDate(this.parentSelectedDate.getDate() + 1);
48. })
49. DateComponent({ selectedDate: this.parentSelectedDate })
50. }
51. }
52. }
```

[ParamUseSceneDate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamUseSceneDate.ets#L30-L83)

### 装饰Map类型变量

@Param装饰Map类型变量，可以观察到数据源对Map整体的赋值，以及调用Map的接口set, clear, delete带来的变化。

```
1. @ComponentV2
2. struct Child {
3. // 使用@Param接收父组件传入的Map类型变量。
4. @Param value: Map<number, string> = new Map();

6. build() {
7. Column() {
8. ForEach(Array.from(this.value.entries()), (item: [number, string]) => {
9. Text(`${item[0]}`).fontSize(30)
10. Text(`${item[1]}`).fontSize(30)
11. Divider()
12. })
13. }
14. }
15. }

17. @Entry
18. @ComponentV2
19. struct Index {
20. // 使用@Local装饰Map类型变量，作为数据源传递给子组件的@Param。
21. @Local message: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);

23. build() {
24. Row() {
25. Column() {
26. Child({ value: this.message })
27. // 对Map整体重新赋值，触发子组件更新。
28. Button('init map').onClick(() => {
29. this.message = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
30. })
31. // 新增键值对，触发子组件更新。
32. Button('set new one').onClick(() => {
33. this.message.set(4, 'd');
34. })
35. // 清空Map，触发子组件更新。
36. Button('clear').onClick(() => {
37. this.message.clear();
38. })
39. // 更新键值对，触发子组件更新。
40. Button('replace the first one').onClick(() => {
41. this.message.set(0, 'aa');
42. })
43. // 删除键值对，触发子组件更新。
44. Button('delete the first one').onClick(() => {
45. this.message.delete(0);
46. })
47. }
48. .width('100%')
49. }
50. .height('100%')
51. }
52. }
```

[ParamUseSceneMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamUseSceneMap.ets#L30-L83)

### 装饰Set类型变量

@Param装饰Set类型变量，可以观察到数据源对Set整体的赋值，以及调用Set的接口add, clear, delete带来的变化。

```
1. @ComponentV2
2. struct Child {
3. // 使用@Param接收父组件传入的Set类型变量。
4. @Param message: Set<number> = new Set();

6. build() {
7. Column() {
8. ForEach(Array.from(this.message.entries()), (item: [number, number]) => {
9. Text(`${item[0]}`).fontSize(30)
10. Divider()
11. })
12. }
13. .width('100%')
14. }
15. }

17. @Entry
18. @ComponentV2
19. struct Index {
20. // 使用@Local装饰Set类型变量，作为数据源传递给子组件的@Param。
21. @Local message: Set<number> = new Set([0, 1, 2, 3, 4]);

23. build() {
24. Row() {
25. Column() {
26. Child({ message: this.message })
27. // 对Set整体重新赋值，触发子组件更新。
28. Button('init set').onClick(() => {
29. this.message = new Set([0, 1, 2, 3, 4]);
30. })
31. // 新增元素，触发子组件更新。
32. Button('set new one').onClick(() => {
33. this.message.add(5);
34. })
35. // 清空Set，触发子组件更新。
36. Button('clear').onClick(() => {
37. this.message.clear();
38. })
39. // 删除元素，触发子组件更新。
40. Button('delete the first one').onClick(() => {
41. this.message.delete(0);
42. })
43. }
44. .width('100%')
45. }
46. .height('100%')
47. }
48. }
```

[ParamUseSceneSet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamUseSceneSet.ets#L30-L79)

### 联合类型

@Param支持null、undefined以及联合类型。以下示例中，count类型为number | undefined，点击改变count的类型时，UI会自动刷新。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. // 使用@Local装饰联合类型变量，作为数据源传递给子组件的@Param。
5. @Local count: number | undefined = 0;

7. build() {
8. Column() {
9. MyComponent({ count: this.count })
10. // 修改联合类型值，触发子组件更新。
11. Button('change')
12. .onClick(() => {
13. this.count = undefined;
14. })
15. }
16. }
17. }

19. @ComponentV2
20. struct MyComponent {
21. // 使用@Param接收父组件传入的联合类型变量。
22. @Param count: number | undefined = 0;

24. build() {
25. Column() {
26. Text(`count(${this.count})`)
27. }
28. }
29. }
```

[ParamUseSceneUnite.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/param/ParamUseSceneUnite.ets#L30-L60)
