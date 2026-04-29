---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state
title: @State装饰器：组件内状态
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理组件拥有的状态 > @State装饰器：组件内状态
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:11+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b7733780cc768457237d0b6cba4a983a9b859d7e7218b780e03c0ea896506057
---

被状态变量装饰器装饰的变量称为状态变量，使普通变量具备状态属性。当状态变量改变时，会触发其直接绑定的UI组件渲染更新。

在状态变量相关装饰器中，@State是最基础的装饰器，也是大部分状态变量的数据源。

在阅读@State文档前，建议开发者对状态管理框架有基本的了解。建议提前阅读：[状态管理概述](arkts-state-management-overview.md)。最佳实践请参考[状态管理最佳实践](../best-practices/bpta-status-management.md)。常见问题请参考[状态管理常见问题](arkts-state-management-faq.md)。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 概述

@State装饰的变量与声明式范式中的其他被装饰变量一样，是私有的，只能从组件内部访问，在声明时必须指定其类型并完成本地初始化；若需从父组件初始化，也可选择使用命名参数机制完成赋值。

@State装饰的变量拥有以下特性：

* @State装饰的变量生命周期与其所属自定义组件的生命周期相同。

## 装饰器使用规则说明

| @State变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无 |
| 同步类型 | 不与父组件中任何类型的变量同步。 |
| 允许装饰的变量类型 | object、class、string、number、boolean、enum类型，以及这些类型的数组。  API version 10开始支持[Date类型](arkts-state.md#装饰date类型变量)。  API version 11及以上支持[Map](arkts-state.md#装饰map类型变量)、[Set](arkts-state.md#装饰set类型变量)类型、undefined和null类型、ArkUI框架定义的联合类型[Length](../harmonyos-references/ts-types.md#length)、[ResourceStr](../harmonyos-references/ts-types.md#resourcestr)、[ResourceColor](../harmonyos-references/ts-types.md#resourcecolor)类型以及这些类型的联合类型，示例见[@State支持联合类型实例](arkts-state.md#state支持联合类型实例)。  支持类型的场景见[观察变化](arkts-state.md#观察变化)。 |
| 不允许装饰的变量类型 | 不支持装饰Function类型。 |
| 被装饰变量的初始值 | 必须本地初始化。 |

## 变量的传递/访问规则说明

| 传递/访问 | 说明 |
| --- | --- |
| 从父组件初始化 | 可以从父组件或本地初始化。  父组件传入非undefined值时覆盖本地初始值，否则使用@State的本地初始值。  支持父组件中的常规变量以及装饰器装饰的状态变量：@State、[@Link](arkts-link.md)、[@Prop](arkts-prop.md)、[@Provide](arkts-provide-and-consume.md)、[@Consume](arkts-provide-and-consume.md)、[@ObjectLink](arkts-observed-and-objectlink.md)、[@StorageLink](arkts-appstorage.md#storagelink)、[@StorageProp](arkts-appstorage.md#storageprop)、[@LocalStorageLink](arkts-localstorage.md#localstoragelink)和[@LocalStorageProp](arkts-localstorage.md#localstorageprop)，初始化@State。需要注意：父组件传入的外部变量对@State初始化时，仅作为初始值，后续变量的变化不会同步至@State。 |
| 用于初始化子组件 | @State装饰的变量支持初始化子组件的常规变量、@State、@Link、@Prop、@Provide。 |
| 是否支持组件外访问 | 不支持，只能在组件内访问。 |

**图1** 初始化规则图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/saTn3lD1Q0unPAvkI3xtnQ/zh-cn_image_0000002558764086.png?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=FFB8FDE34A2C6CFFE7541B4F1D0DF6433A21D41EAE9B21BB620483905B7E68CB)

## 观察变化和行为表现

并不是状态变量的所有更改都会引起UI的刷新，只有可以被框架观察到的修改才会引起UI刷新。本小节将介绍什么样的修改才能被观察到，以及观察到变化后，框架是怎么引起UI刷新的，即框架的行为表现是什么。

### 观察变化

* 当装饰的数据类型为boolean、string、number类型时，可以观察到数值的变化。

  ```
  1. // 简单类型
  2. @State count: number = 0;
  3. // 可以观察到值的变化
  4. this.count = 1;
  ```
* 当装饰的数据类型为class或Object时，可以观察到自身的赋值和属性赋值的变化，即Object.keys(observedObject)返回的所有属性。示例如下：

  声明Person和Model类。

  ```
  1. // 声明Person类
  2. class Person {
  3. public value: string;

  5. constructor(value: string) {
  6. this.value = value;
  7. }
  8. }

  10. // 声明Model类
  11. class Model {
  12. public value: string;
  13. public name: Person;

  15. constructor(value: string, person: Person) {
  16. this.value = value;
  17. this.name = person;
  18. }
  19. }
  ```

  [StateChangeObservationObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateChangeObservationObject.ets#L15-L33)

  @State装饰的类型是Model。

  ```
  1. // class类型
  2. @State title: Model = new Model('Hello', new Person('World'));
  ```

  [StateChangeObservationObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateChangeObservationObject.ets#L38-L42)

  对@State装饰变量的赋值。

  ```
  1. // class类型赋值
  2. this.title = new Model('Hi', new Person('ArkUI'));
  ```

  [StateChangeObservationObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateChangeObservationObject.ets#L55-L59)

  对@State装饰变量的属性赋值。

  ```
  1. // class属性的赋值
  2. this.title.value = 'Hi';
  ```

  [StateChangeObservationObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateChangeObservationObject.ets#L62-L66)

  对嵌套对象的属性直接赋值无法被框架观察到，因此不会触发UI刷新。

  ```
  1. // 嵌套的属性赋值观察不到
  2. this.title.name.value = 'ArkUI';
  ```

  [StateChangeObservationObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateChangeObservationObject.ets#L69-L73)
* 当装饰的对象是Array时，可以观察到Array整体的赋值及数组元素的赋值，同时可以通过调用Array的接口push, pop, shift, unshift, splice, copyWithin, fill, reverse, sort更新Array中的数据。数组项中嵌套的属性赋值无法观察。详见[装饰Array类型变量](arkts-state.md#装饰array类型变量)。
* 当装饰的对象是Date时，可以观察到Date的赋值，以及通过调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds更新Date的属性，详见[装饰Date类型变量](arkts-state.md#装饰date类型变量)。
* 当装饰的变量是Map时，可以观察到Map整体的赋值，以及通过调用Map的接口set, clear, delete更新Map的值。详见[装饰Map类型变量](arkts-state.md#装饰map类型变量)。
* 当装饰的变量是Set时，可以观察到Set整体的赋值，以及通过调用Set的接口add, clear, delete更新Set的值。详见[装饰Set类型变量](arkts-state.md#装饰set类型变量)。

### 框架行为

* 当状态变量改变时，查询依赖该状态变量的组件。
* 执行依赖该状态变量的组件更新方法，实现组件更新渲染。

## 限制条件

1. @State装饰的变量必须初始化，否则编译期会报错。

   ```
   1. // 错误写法，编译报错
   2. @State count: number;

   4. // 正确写法
   5. @State count: number = 10;
   ```
2. @State不支持装饰Function类型的变量，API version 23之前，框架会抛出运行时错误。

   从API version 23开始，添加对@State装饰Function类型变量的校验，编译期会报错。
3. 父组件传入undefined时，@State装饰的变量仍使用本地默认值进行初始化。

   ```
   1. @Entry
   2. @Component
   3. struct Parent {
   4. @State count: number | undefined = undefined;

   6. build() {
   7. Column() {
   8. Text(`Parent count value: ${this.count}`)
   9. .fontSize(20)
   10. .margin(10)
   11. Child({ count: this.count })
   12. }
   13. }
   14. }

   16. @Component
   17. struct Child {
   18. // 子组件count本地默认值为0；父组件传入undefined时，框架会保留该本地默认值
   19. @State count: number | undefined = 0;

   21. build() {
   22. Column() {
   23. Text(`Child count value: ${this.count}`)
   24. .fontSize(20)
   25. .margin(10)
   26. }
   27. }
   28. }
   ```

## 使用场景

### 装饰简单类型的变量

以下示例为@State装饰的简单类型，count被@State装饰成为状态变量，count的改变引起Button组件的刷新：

* 当状态变量count改变时，只能查询到Button组件与之关联。
* 执行Button组件的更新方法，实现按需刷新。

  ```
  1. @Entry
  2. @Component
  3. struct MyComponent {
  4. @State count: number = 0; // 使用@State装饰简单类型变量

  6. build() {
  7. Row() {
  8. Column() {
  9. Button(`click times: ${this.count}`)
  10. .onClick(() => {
  11. this.count += 1;
  12. })
  13. .width(300)
  14. }
  15. .width('100%')
  16. }
  17. .height('100%')
  18. }
  19. }
  ```

  [StateSceneSimpleType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneSimpleType.ets#L16-L36)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/SNiuSOGARRGC5yRYVis-Kg/zh-cn_image_0000002558604430.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=9B53FE97249541D6C02152F02479285FD340066A3F35224FC883B29210CE92B2)

### 装饰class对象类型的变量

* 自定义组件MyComponent定义了被@State装饰的状态变量count和title，其中title的类型为自定义类Model。如果count或title的值发生变化，则查询MyComponent中使用该状态变量的UI组件，并进行重新渲染。
* EntryComponent中有多个MyComponent组件实例，第一个MyComponent内部状态的更改不会影响第二个MyComponent。

  ```
  1. class Model {
  2. public value: string;

  4. constructor(value: string) {
  5. this.value = value;
  6. }
  7. }

  9. @Entry
  10. @Component
  11. struct EntryComponent {
  12. build() {
  13. Column() {
  14. // 此处指定的参数都将在初始渲染时覆盖本地定义的默认值，并不是所有的参数都需要从父组件初始化
  15. MyComponent({ count: 1, increaseBy: 2 })
  16. .width(300)
  17. MyComponent({ title: new Model('Hello World 2'), count: 7 })
  18. }
  19. }
  20. }

  22. @Component
  23. struct MyComponent {
  24. @State title: Model = new Model('Hello World');
  25. @State count: number = 0;
  26. increaseBy: number = 1;

  28. build() {
  29. Column() {
  30. Text(`${this.title.value}`)
  31. .margin(10)
  32. Button(`Click to change title`)
  33. .onClick(() => {
  34. // @State变量的更新将触发上面的Text组件内容更新
  35. this.title.value = this.title.value === 'Hello ArkUI' ? 'Hello World' : 'Hello ArkUI';
  36. })
  37. .width(300)
  38. .margin(10)

  40. Button(`Click to increase count = ${this.count}`)
  41. .onClick(() => {
  42. // @State变量的更新将触发该Button组件的内容更新
  43. this.count += this.increaseBy;
  44. })
  45. .width(300)
  46. .margin(10)
  47. }
  48. }
  49. }
  ```

  [StateSceneTypeClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneTypeClass.ets#L16-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/pOJnI4l9RfyQvEpKhDGMaA/zh-cn_image_0000002589323955.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=2B89D1B9D6620984314DA830046F496EB73E84906C32F8C9ABAF01AF2FC96BCE)

从上述示例中，我们可以了解到@State变量的初始化机制：

1. 上述示例中，在没有外部传入的情况下，使用默认的值进行本地初始化：

   ```
   1. // title没有外部传入，使用本地的值new Model('Hello World')进行初始化
   2. MyComponent({ count: 1, increaseBy: 2 })
   3. // increaseBy没有外部传入，使用本地的值1进行初始化
   4. MyComponent({ title: new Model('Hello World 2'), count: 7 })
   ```

   [StateSceneTypeClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneTypeClass.ets#L76-L81)
2. 上述示例中，在有外部传入的情况下，使用外部传入的值进行初始化：

   ```
   1. // count和increaseBy均有外部传入，分别使用传入的1和2进行初始化
   2. MyComponent({ count: 1, increaseBy: 2 })
   3. // title和count均有外部传入，分别使用传入的new Model('Hello World 2')和7进行初始化
   4. MyComponent({ title: new Model('Hello World 2'), count: 7 })
   ```

   [StateSceneTypeClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneTypeClass.ets#L83-L88)

### 装饰Array类型变量

在下面的示例中，@State装饰的变量fruits的类型为Array<Fruit>，点击Button改变fruits的值，视图会随之刷新。

```
1. class Fruit {
2. public name: string;

4. constructor(name: string) {
5. this.name = name;
6. }
7. }

9. @Entry
10. @Component
11. struct ArraySample {
12. @State fruits: Fruit[] = [new Fruit('apple'), new Fruit('banana')]; // 使用@State装饰Array类型变量

14. build() {
15. Row() {
16. Column() {
17. ForEach(this.fruits, (item: Fruit) => {
18. Text(`${item.name}`)
19. .fontSize(20)
20. .margin(10)
21. })
22. // 对数组元素重新赋值，触发UI刷新
23. Button('Set element at index 0')
24. .onClick(() => {
25. this.fruits[0] = new Fruit('orange');
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
36. // 删除数组元素，触发UI刷新
37. Button('Pop element')
38. .onClick(() => {
39. this.fruits.pop();
40. })
41. .width(300)
42. .margin(10)
43. // 对数组整体重新赋值，触发UI刷新
44. Button('Reset array')
45. .onClick(() => {
46. this.fruits = [new Fruit('strawberry'), new Fruit('blueberry')];
47. })
48. .width(300)
49. .margin(10)
50. // 修改嵌套的属性，无法触发UI刷新
51. Button('Modify element[0] property')
52. .onClick(() => {
53. this.fruits[0].name = 'pineapple';
54. })
55. .width(300)
56. .margin(10)
57. }
58. .width('100%')
59. }
60. .height('100%')
61. }
62. }
```

[StateSceneTypeArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneTypeArray.ets#L16-L79)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/BvtcZaH7QiSaigebCN4jQA/zh-cn_image_0000002589243895.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=D89D96CDB83B2F15B3F9688E76AFBF8F40FD53A5C1C86903501D0C5DFACBFC7E)

### 装饰Map类型变量

说明

从API version 11开始，@State支持Map类型。

在下面的示例中，@State装饰的变量fruits的类型为Map<string, number>，点击Button改变fruits的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct MapSample {
4. @State fruits: Map<string, number> = new Map([['apple', 1], ['banana', 2]]); // 使用@State装饰Map类型变量

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

[StateSceneTypeMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneTypeMap.ets#L16-L71)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/smVSWgtFQfK83G4YJTRuDQ/zh-cn_image_0000002558764088.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=14B4514F4DFECD8C6D9165B22E4A7A12DEA36D10E02BB6E50DDCA8BBE5B4F0AC)

### 装饰Set类型变量

说明

从API version 11开始，@State支持Set类型。

在下面的示例中，@State装饰的变量fruits的类型为Set<string>，点击Button改变fruits的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct SetSample {
4. @State fruits: Set<string> = new Set(['apple', 'banana']); // 使用@State装饰Set类型变量

6. build() {
7. Row() {
8. Column() {
9. ForEach(Array.from(this.fruits.entries()), (item: [string, string]) => {
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

[StateSceneTypeSet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneTypeSet.ets#L16-L64)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/vfeS3_heTOWFNL15QkFlTg/zh-cn_image_0000002558604432.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=DD6A94D5F80345A2BC8F90FAEBEB06E2F9F42BA85FA7AC63D1F4C015B4FEEEB8)

### 装饰Date类型变量

在下面的示例中，@State装饰的变量selectedDate的类型为Date，点击Button改变selectedDate的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct DatePickerExample {
4. @State selectedDate: Date = new Date('2021-08-08'); // 使用@State装饰Date类型变量

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

[StateSceneTypeDate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneTypeDate.ets#L16-L64)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/6vcmpkQ4QgG8Wuc0VR0U5g/zh-cn_image_0000002589323957.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=4D4DCEE41B5E770F1A7A85CE1E0983BA18505B40BFD1427314CD51C03C2B685E)

### State支持联合类型实例

@State支持联合类型和undefined和null，在下面的示例中，count类型为number | undefined，点击Button改变count的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct UnionTypeSample {
4. @State count: number | undefined = 0; // 使用@State装饰联合类型变量

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

[StateSceneJointTypeInstance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateSceneJointTypeInstance.ets#L16-L46)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/nl3N4MlmRFS6x94DED6Tiw/zh-cn_image_0000002589243897.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052710Z&HW-CC-Expire=86400&HW-CC-Sign=D4D43E921C4B3C0C9F8B97C01718DF58E184252119EB903D881BA2BF14FDE63F)
