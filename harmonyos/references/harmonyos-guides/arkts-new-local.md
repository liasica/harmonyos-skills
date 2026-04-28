---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-local
title: @Local装饰器：组件内部状态
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理组件拥有的状态 > @Local装饰器：组件内部状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:19220cc129b94b252f0c1f6465320107ffd514e13b3b1d5487d00a7f15efd127
---

为了实现对@ComponentV2装饰的自定义组件中变量变化的观测，开发者可以使用@Local装饰器装饰变量。

在阅读本文档前，建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)。常见问题请参考[组件内状态变量常见问题](arkts-state-management-faq-inner-component.md)。

说明

从API version 12开始，在@ComponentV2装饰的自定义组件中支持使用@Local装饰器。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Local表示组件内部的状态，使得自定义组件内部的变量具有观察变化的能力：

* 被@Local装饰的变量无法从外部初始化，因此必须在组件内部进行初始化。
* 当被@Local装饰的变量变化时，会刷新使用该变量的组件。
* @Local支持观测number、boolean、string、Object、class等基本类型以及[Array](arkts-new-local.md#装饰array类型变量)、[Set](arkts-new-local.md#装饰set类型变量)、[Map](arkts-new-local.md#装饰map类型变量)、[Date](arkts-new-local.md#装饰date类型变量)等内置类型。
* @Local的观测能力仅限于被装饰的变量本身。当装饰简单类型时，能够观测到对变量的赋值；当装饰对象类型时，仅能观测到对对象整体的赋值；当装饰数组类型时，能观测到数组整体以及数组元素项的变化；当装饰Array、Set、Map、Date等内置类型时，可以观测到通过API调用带来的变化。详见[观察变化](arkts-new-local.md#观察变化)。
* @Local支持null、undefined以及[联合类型](arkts-new-local.md#联合类型)。

## 状态管理V1版本@State装饰器的局限性

状态管理V1使用[@State装饰器](arkts-state.md)定义组件中的基础状态变量，该状态变量常用来作为组件内部状态，在组件内使用。但由于@State装饰器又能够从外部初始化，因此无法确保@State装饰变量的初始值一定为组件内部定义的值。

```
1. class ComponentInfo {
2. public name: string;
3. public count: number;
4. public message: string;

6. constructor(name: string, count: number, message: string) {
7. this.name = name;
8. this.count = count;
9. this.message = message;
10. }
11. }

13. @Component
14. struct Child {
15. @State componentInfo: ComponentInfo = new ComponentInfo('Child', 1, 'Hello World'); // 父组件传递的componentInfo会覆盖初始值

17. build() {
18. Column() {
19. Text(`componentInfo.message is ${this.componentInfo.message}`)
20. }
21. }
22. }

24. @Entry
25. @Component
26. struct Index {
27. build() {
28. Column() {
29. Child({ componentInfo: new ComponentInfo('Unknown', 0, 'Error') })
30. }
31. }
32. }
```

[LocalV1StateDecorator.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalV1StateDecorator.ets#L29-L62)

上述代码中，可以通过在初始化Child自定义组件时传入新的值来覆盖作为内部状态变量使用的componentInfo。但Child自定义组件并不能感知到componentInfo从外部进行了初始化，这不利于自定义组件内部状态的管理。因此推出@Local装饰器表示组件的内部状态。

## 装饰器说明

| @Local变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 可装饰的变量类型 | Object、class、string、number、boolean、enum等基本类型以及Array、Date、Map、Set等内置类型。支持null、undefined以及联合类型。 |
| 装饰变量的初始值 | 必须本地初始化，不允许外部传入初始化。 |

## 变量传递

| 传递规则 | 说明 |
| --- | --- |
| 从父组件初始化 | @Local装饰的变量仅允许本地初始化，无法从外部传入初始化。 |
| 初始化子组件 | @Local装饰的变量可以初始化子组件中[@Param](arkts-new-param.md)装饰的变量。 |

## 观察变化

使用@Local装饰的变量具有观察变化的能力。当装饰的变量发生变化时，会触发该变量绑定的UI组件刷新。

* 当装饰的变量类型为boolean、string、number时，可以观察到对变量赋值的变化。

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
  11. Text(`${this.count}`)
  12. Text(`${this.message}`)
  13. Text(`${this.flag}`)
  14. Button('change Local')
  15. .onClick(() => {
  16. // 当@Local装饰简单类型时，能够观测到对变量的赋值
  17. this.count++;
  18. this.message += ' World';
  19. this.flag = !this.flag;
  20. })
  21. }
  22. }
  23. }
  ```

  [LocalObserveChangesType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalObserveChangesType.ets#L30-L54)
* 当装饰的变量类型为类对象时，仅可以观察到对类对象整体赋值的变化，无法直接观察到对类成员属性赋值的变化，对类成员属性的观察依赖[@ObservedV2](arkts-new-observedv2-and-trace.md)和[@Trace](arkts-new-observedv2-and-trace.md)装饰器，也可以使用[makeObserved](arkts-new-makeobserved.md)将该对象变为可观察对象。注意，API version 19之前，@Local无法和[@Observed](arkts-observed-and-objectlink.md)装饰的类实例对象混用。API version 19及以后，支持部分状态管理V1V2混用能力，允许@Local和@Observed同时使用，详情见[状态管理V1和V2混用指导（API version 19及之后）](arkts-v1-v2-mixusage.md)。

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
  36. // @Local不具备观察类对象属性的能力，因此对rawObject.name的修改无法观察到
  37. this.rawObject.name = 'new rawObject name';
  38. // 由于ObservedObject的name属性被@Trace装饰，因此对observedObject.name的修改能被观察到
  39. this.observedObject.name = 'new observedObject name';
  40. })
  41. }
  42. }
  43. }
  ```

  [LocalObserveChangesDecorator.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalObserveChangesDecorator.ets#L30-L74)
* 当装饰简单类型数组时，可以观察到数组整体或数组项的变化。

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Index {
  4. @Local numArr: number[] = [1, 2, 3, 4, 5]; // 使用@Local装饰一维数组变量
  5. @Local dimensionTwo: number[][] = [[1, 2, 3], [4, 5, 6]]; // 使用@Local装饰二维数组变量

  7. build() {
  8. Column() {
  9. Text(`${this.numArr[0]}`)
  10. Text(`${this.numArr[1]}`)
  11. Text(`${this.numArr[2]}`)
  12. Text(`${this.dimensionTwo[0][0]}`)
  13. Text(`${this.dimensionTwo[1][1]}`)
  14. Button('change array item') // 按钮1：修改数组中的特定元素
  15. .onClick(() => {
  16. this.numArr[0]++;
  17. this.numArr[1] += 2;
  18. this.dimensionTwo[0][0] = 0;
  19. this.dimensionTwo[1][1] = 0;
  20. })
  21. Button('change whole array') // 按钮2：替换整个数组
  22. .onClick(() => {
  23. this.numArr = [5, 4, 3, 2, 1];
  24. this.dimensionTwo = [[7, 8, 9], [0, 1, 2]];
  25. })
  26. }
  27. }
  28. }
  ```

  [LocalObserveChangesArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalObserveChangesArray.ets#L29-L58)
* 当装饰的变量是嵌套类或对象数组时，@Local无法观察深层对象属性的变化。对深层对象属性的观测依赖@ObservedV2与@Trace装饰器。

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
  58. }
  59. }
  60. }
  ```

  [LocalObserveChangesDeepObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalObserveChangesDeepObject.ets#L30-L91)
* 当装饰内置类型时，可以观察到变量整体赋值及API调用带来的变化。

  | 类型 | 可观察变化的API |
  | --- | --- |
  | Array | push, pop, shift, unshift, splice, copyWithin, fill, reverse, sort |
  | Date | setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds |
  | Map | set, clear, delete |
  | Set | add, clear, delete |

## 限制条件

@Local装饰器存在以下使用限制：

* @Local装饰器只能在[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件中使用。

  ```
  1. @ComponentV2
  2. struct MyComponent {
  3. @Local message: string = 'Hello World'; // 正确用法
  4. build() {
  5. }
  6. }
  7. @Component
  8. struct TestComponent {
  9. @Local message: string = 'Hello World'; // 错误用法，编译时报错
  10. build() {
  11. }
  12. }
  ```
* @Local装饰的变量表示组件内部状态，不允许从外部传入初始化。

  ```
  1. @ComponentV2
  2. struct ChildComponent {
  3. @Local message: string = 'Hello World';
  4. build() {
  5. }
  6. }
  7. @ComponentV2
  8. struct MyComponent {
  9. build() {
  10. ChildComponent({ message: 'Hello' }) // 错误用法，编译时报错
  11. }
  12. }
  ```

## @Local与@State对比

@Local与@State的用法、功能对比如下：

| 用法 | @State | @Local |
| --- | --- | --- |
| 参数 | 无。 | 无。 |
| 从父组件初始化 | 可选。 | 不允许外部初始化。 |
| 观察能力 | 能观测变量本身以及一层的成员属性，无法深度观测。 | 能观测变量本身，深度观测依赖@Trace装饰器。 |
| 数据传递 | 可以作为数据源和子组件中状态变量同步。 | 可以作为数据源和子组件中状态变量同步。 |

## 使用场景

### 观测对象整体变化

被@ObservedV2与@Trace装饰的类对象实例，具有深度观测对象属性的能力。但当对对象整体赋值时，UI却无法刷新。使用@Local装饰对象，可以达到观测对象本身变化的效果。

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

12. @Entry
13. @ComponentV2
14. struct Index {
15. info: Info = new Info('Tom', 25);
16. @Local localInfo: Info = new Info('Tom', 25);

18. build() {
19. Row() {
20. Column() {
21. Text(`info: ${this.info.name}-${this.info.age}`) // Text1
22. .margin(10)
23. Text(`localInfo: ${this.localInfo.name}-${this.localInfo.age}`) // Text2
24. .margin(10)
25. Button('change info&localInfo')
26. .onClick(() => {
27. this.info = new Info('Lucy', 18); // Text1不会刷新
28. this.localInfo = new Info('Lucy', 18); // Text2会刷新
29. })
30. .margin(10)
31. }
32. .width('100%')
33. }
34. .height('100%')
35. }
36. }
```

[LocalUseCaseObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalUseCaseObject.ets#L29-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/yYLVJrH7SGK7hxLSuAQkbw/zh-cn_image_0000002552797964.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=71047AC26B373B618C239452E9C44142D6C35FFD324A8D9617E2FE67CA7826DF)

### 装饰Array类型变量

当装饰的对象是Array时，可以观察到Array整体的赋值，同时可以通过调用Array的接口push, pop, shift, unshift, splice, copyWithin, fill, reverse, sort更新Array中的数据。

```
1. class Fruit {
2. public name: string;

4. constructor(name: string) {
5. this.name = name;
6. }
7. }

9. @Entry
10. @ComponentV2
11. struct Index {
12. @Local fruits: Fruit[] = [new Fruit('apple'), new Fruit('banana')]; // 使用@Local装饰Array类型变量

14. build() {
15. Row() {
16. Column() {
17. ForEach(this.fruits, (item: Fruit) => {
18. Text(`${item.name}`)
19. .fontSize(20)
20. .margin(10)
21. })
22. // 对数组整体重新赋值，触发UI刷新
23. Button('Reset array')
24. .onClick(() => {
25. this.fruits = [new Fruit('strawberry'), new Fruit('blueberry')];
26. })
27. .width(300)
28. .margin(10)
29. // 新增数组元素，触发UI刷新
30. Button('Push element')
31. .onClick(() => {
32. this.fruits.push(new Fruit('cherry'));
33. })
34. .width(300)
35. .margin(10)
36. // 翻转数组元素，触发UI刷新
37. Button('Reverse array')
38. .onClick(() => {
39. this.fruits.reverse();
40. })
41. .width(300)
42. .margin(10)
43. // 使用同一元素填充数组，触发UI刷新
44. Button('Fill array')
45. .onClick(() => {
46. this.fruits.fill(new Fruit('apple'));
47. })
48. .width(300)
49. .margin(10)
50. }
51. .width('100%')
52. }
53. .height('100%')
54. }
55. }
```

[LocalUseCaseArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalUseCaseArray.ets#L29-L85)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/kDzi0X_aSSqAk1TZOvH4ew/zh-cn_image_0000002583437659.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=38373F6A0391AA735E062BC71326FEFEFBF4FA4C78ABF06AF4F6685892185111)

### 装饰Date类型变量

当装饰的对象是Date时，可以观察到Date整体的赋值，同时可通过调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds更新Date的属性。

```
1. @Entry
2. @ComponentV2
3. struct DatePickerExample {
4. @Local selectedDate: Date = new Date('2021-08-08'); // 使用@Local装饰Date类型变量

6. build() {
7. Row() {
8. Column() {
9. // 通过给selectedDate重新赋值新的Date实例，触发UI刷新
10. Button('set selectedDate to 2023-07-08')
11. .onClick(() => {
12. this.selectedDate = new Date('2023-07-08');
13. })
14. .margin(10)
15. .width(300)
16. // 调用Date的setFullYear接口修改年份，触发UI刷新
17. Button('increase the year by 1')
18. .onClick(() => {
19. this.selectedDate.setFullYear(this.selectedDate.getFullYear() + 1);
20. })
21. .margin(10)
22. .width(300)
23. // 调用Date的setMonth接口修改月份，触发UI刷新
24. Button('increase the month by 1')
25. .onClick(() => {
26. this.selectedDate.setMonth(this.selectedDate.getMonth() + 1);
27. })
28. .margin(10)
29. .width(300)
30. // 调用Date的setDate接口修改日期，触发UI刷新
31. Button('increase the day by 1')
32. .onClick(() => {
33. this.selectedDate.setDate(this.selectedDate.getDate() + 1);
34. })
35. .margin(10)
36. .width(300)
37. DatePicker({
38. start: new Date('1970-1-1'),
39. end: new Date('2100-1-1'),
40. selected: this.selectedDate
41. }).margin(20)
42. }
43. .width('100%')
44. }
45. .height('100%')
46. }
47. }
```

[LocalUseCaseDate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalUseCaseDate.ets#L30-L78)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/iuxX5jwXTwSRj-cssq648A/zh-cn_image_0000002552957614.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=B1565331788E4ECA0F2DBE1AF1B21A641195A469967F17E65266E66F3023B53F)

### 装饰Map类型变量

当装饰的对象是Map时，可以观察到对Map整体的赋值，同时可以通过调用Map的接口set, clear, delete更新Map中的数据。

```
1. @Entry
2. @ComponentV2
3. struct MapSample {
4. @Local fruits: Map<string, number> = new Map([['apple', 1], ['banana', 2]]); // 使用@Local装饰Map类型变量

6. build() {
7. Row() {
8. Column() {
9. ForEach(Array.from(this.fruits.entries()), (item: [string, number]) => {
10. Text(`key: ${item[0]}, value: ${item[1]}`)
11. .fontSize(20)
12. .margin(10)
13. })
14. // 新增键值对，触发UI刷新
15. Button('Set entry cherry')
16. .onClick(() => {
17. this.fruits.set('cherry', 3);
18. })
19. .width(300)
20. .margin(10)
21. // 更新键值对，触发UI刷新
22. Button('Update entry apple')
23. .onClick(() => {
24. this.fruits.set('apple', 4);
25. })
26. .width(300)
27. .margin(10)
28. // 删除键值对，触发UI刷新
29. Button('Delete entry apple')
30. .onClick(() => {
31. this.fruits.delete('apple');
32. })
33. .width(300)
34. .margin(10)
35. // 对Map整体重新赋值，触发UI刷新
36. Button('Reset map')
37. .onClick(() => {
38. this.fruits = new Map([['strawberry', 9], ['blueberry', 8]]);
39. })
40. .width(300)
41. .margin(10)
42. // 清空Map，触发UI刷新
43. Button('Clear map')
44. .onClick(() => {
45. this.fruits.clear();
46. })
47. .width(300)
48. .margin(10)
49. }
50. .width('100%')
51. }
52. .height('100%')
53. }
54. }
```

[LocalUseCaseMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalUseCaseMap.ets#L29-L84)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/2cQmKnQ-Ti6Qr6mw7muZ-Q/zh-cn_image_0000002583477615.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=4C8F02657106B897108EB6DC18EEF1333A02A1948422D23E59D892C6429EEAB3)

### 装饰Set类型变量

当装饰的对象是Set时，可以观察到对Set整体的赋值，同时可以通过调用Set的接口add, clear, delete更新Set中的数据。

```
1. @Entry
2. @ComponentV2
3. struct SetSample {
4. @Local fruits: Set<string> = new Set(['apple', 'banana']); // 使用@Local装饰Set类型变量

6. build() {
7. Row() {
8. Column() {
9. ForEach(Array.from(this.fruits.entries()), (item: [number, number]) => {
10. Text(`${item[0]}`)
11. .fontSize(20)
12. .margin(10)
13. })
14. // 新增元素，触发UI刷新
15. Button('Add element')
16. .onClick(() => {
17. this.fruits.add('cherry');
18. })
19. .width(300)
20. .margin(10)
21. // 删除元素，触发UI刷新
22. Button('Delete element apple')
23. .onClick(() => {
24. this.fruits.delete('apple');
25. })
26. .width(300)
27. .margin(10)
28. // 对Set整体重新赋值，触发UI刷新
29. Button('Reset set')
30. .onClick(() => {
31. this.fruits = new Set(['strawberry', 'blueberry']);
32. })
33. .width(300)
34. .margin(10)
35. // 清空Set，触发UI刷新
36. Button('Clear set')
37. .onClick(() => {
38. this.fruits.clear();
39. })
40. .width(300)
41. .margin(10)
42. }
43. .width('100%')
44. }
45. .height('100%')
46. }
47. }
```

[LocalUseCaseSet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalUseCaseSet.ets#L29-L77)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hYANhWt8TNa4-6_AnZX_wg/zh-cn_image_0000002552797966.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=C2AEBB8FEE2CBABA950EA070E31C23D47AD0AC0735E8DC0854758ED3762744E1)

### 联合类型

@Local支持null、undefined以及联合类型。在下面的示例中，count类型为number | undefined，点击改变count的类型，UI会随之刷新。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Local count: number | undefined = 10; // 使用@Local装饰联合类型变量

6. build() {
7. Row() {
8. Column() {
9. Text(`count: ${this.count}`)
10. // 将联合类型变量从number切换为undefined，触发UI刷新
11. Button('change to undefined')
12. .onClick(() => {
13. this.count = undefined;
14. })
15. .width(300)
16. .margin(10)
17. // 将联合类型变量从undefined切换为number，触发UI刷新
18. Button('change to number')
19. .onClick(() => {
20. this.count = 10;
21. })
22. .width(300)
23. .margin(10)
24. }
25. .width('100%')
26. }
27. .height('100%')
28. }
29. }
```

[LocalUseCaseJoin.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalUseCaseJoin.ets#L30-L60)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/paPwa8YMTVmdqGIHz-bJrQ/zh-cn_image_0000002583437661.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=EE3030CDAEEB390200E6AC4D977334BC9C69CC1CDE67F64FBAA0F88B0A0243B2)

## 常见问题

### 在状态管理V2中使用animateTo动画效果异常

在下面的场景中，[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)暂不支持直接在状态管理V2中使用。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Local w: number = 50; // 宽度
5. @Local h: number = 50; // 高度
6. @Local message: string = 'Hello';

8. build() {
9. Column() {
10. Button('change size')
11. .margin(20)
12. .onClick(() => {
13. // 在执行动画前，存在额外的修改
14. this.w = 100;
15. this.h = 100;
16. this.message = 'Hello World';
17. this.getUIContext().animateTo({
18. duration: 1000
19. }, () => {
20. this.w = 200;
21. this.h = 200;
22. this.message = 'Hello ArkUI';
23. })
24. })
25. Column() {
26. Text(`${this.message}`)
27. }
28. .backgroundColor('#ff17a98d')
29. .width(this.w)
30. .height(this.h)
31. }
32. }
33. }
```

[LocalQuestionV2animateTo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalQuestionV2animateTo.ets#L29-L63)

上述代码中，开发者预期的动画效果是：绿色矩形从长宽100变为200，字符串从Hello World变为Hello ArkUI。但由于当前animateTo与V2的刷新机制不兼容，执行动画前的额外修改未生效，实际显示的动画效果是：绿色矩形从长宽50变为200，字符串从Hello变为Hello ArkUI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/f3bEN-FfT7mQCqLlkiclqA/zh-cn_image_0000002552957616.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=C5AEDD9459210077F20267D41EB7FC1A26C5D0E6F5C1B9FA371968EC92CD7ACE)

从API version 22开始，可以使用[applySync接口](arkts-new-applysync-flushupdates-flushuiupdates.md)实现预期的显示效果。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local w: number = 50; // 宽度
7. @Local h: number = 50; // 高度
8. @Local message: string = 'Hello';

10. build() {
11. Column() {
12. Button('change size')
13. .margin(20)
14. .onClick(() => {
15. // 在执行动画前，存在额外的修改
16. UIUtils.applySync(() => {
17. this.w = 100;
18. this.h = 100;
19. this.message = 'Hello World';
20. })
21. this.getUIContext().animateTo({
22. duration: 1000
23. }, () => {
24. this.w = 200;
25. this.h = 200;
26. this.message = 'Hello ArkUI';
27. })
28. })
29. Column() {
30. Text(`${this.message}`)
31. }
32. .backgroundColor('#ff17a98d')
33. .width(this.w)
34. .height(this.h)
35. }
36. }
37. }
```

[LocalQuestionExpectedEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalQuestionExpectedEffect.ets#L15-L53)

原理为使用applySync接口同步刷新闭包函数内的状态变量变化，再执行原来的动画达成预期的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/I0N98K9KRw60-PBJ9STE6A/zh-cn_image_0000002583477617.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=F13A6A2271CE0FCBDEF96085798D7480701ACA0B4FD2D8A35295FA84A21E5EB2)
