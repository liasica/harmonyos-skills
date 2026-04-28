---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-prop
title: @Prop装饰器：父子单向同步
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理组件拥有的状态 > @Prop装饰器：父子单向同步
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:794542b249b1ffbd0a78bf48850a5f646c44124d0da8ba72ae88471c84311b55
---

@Prop装饰的变量可以和父组件建立单向同步关系。

在阅读@Prop文档前，建议开发者首先了解[@State](arkts-state.md)的基本用法。最佳实践请参考[状态管理最佳实践](../best-practices/bpta-status-management.md)。常见问题请参考[状态管理常见问题](arkts-state-management-faq.md)。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 概述

@Prop装饰的变量具有以下特性：

* @Prop装饰的变量允许本地修改，但修改不会同步回父组件。
* 当数据源更改时，@Prop装饰的变量都会更新，并且会覆盖本地所有更改。

## 装饰器使用规则说明

| @Prop变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 同步类型 | 单向同步。对父组件状态变量值的修改，将同步给子组件@Prop装饰的变量，子组件@Prop装饰的变量的修改不会同步到父组件的状态变量上。  嵌套类型的场景请参考[观察变化](arkts-prop.md#观察变化)。 |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum类型，以及这些类型的数组。  API version 10开始支持[Date类型](arkts-prop.md#装饰date类型变量)。  API version 11及以上支持[Map](arkts-prop.md#装饰map类型变量)、[Set](arkts-prop.md#装饰set类型变量)类型、undefined和null类型、ArkUI框架定义的联合类型[Length](../harmonyos-references/ts-types.md#length)、[ResourceStr](../harmonyos-references/ts-types.md#resourcestr)、[ResourceColor](../harmonyos-references/ts-types.md#resourcecolor)类型以及这些类型的联合类型，示例见[Prop支持联合类型实例](arkts-prop.md#prop支持联合类型实例)。  支持类型的场景请参考[观察变化](arkts-prop.md#观察变化)。 |
| 不允许装饰的变量类型 | 不支持装饰Function类型。 |
| 嵌套传递层数 | 在组件复用场景，建议@Prop深度嵌套数据不要超过5层，嵌套太多会导致深拷贝占用的空间过大以及GarbageCollection(垃圾回收)，引起性能问题，此时更建议使用[@ObjectLink](arkts-observed-and-objectlink.md)。 |
| 被装饰变量的初始值 | 允许本地初始化。API version 11及以上，如果和[@Require](arkts-require.md)结合使用，则必须父组件构造传参。 |

## 变量的传递/访问规则说明

| 装饰器使用规则 | 说明 |
| --- | --- |
| 从父组件初始化 | 如果本地有初始化，则是可选的，初始化行为和[@State](arkts-state.md#变量的传递访问规则说明)保持一致。没有的话，则必选，支持父组件中的常规变量（常规变量对@Prop赋值，只是数值的初始化，常规变量的变化不会触发UI刷新。只有状态变量才能触发UI刷新）、[@State](arkts-state.md)、[@Link](arkts-link.md)、@Prop、[@Provide](arkts-provide-and-consume.md)、[@Consume](arkts-provide-and-consume.md)、[@ObjectLink](arkts-observed-and-objectlink.md)、[@StorageLink](arkts-appstorage.md#storagelink)、[@StorageProp](arkts-appstorage.md#storageprop)、[@LocalStorageLink](arkts-localstorage.md#localstoragelink)和[@LocalStorageProp](arkts-localstorage.md#localstorageprop)去初始化子组件中的@Prop装饰的变量。 |
| 用于初始化子组件 | @Prop支持初始化子组件中的常规变量、@State、@Link、@Prop、@Provide。 |
| 是否支持组件外访问 | @Prop装饰的变量是私有的，只能在组件内访问。 |

初始化规则图示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/oz-cDnXQSqeb8bo4kZ_BOQ/zh-cn_image_0000002552797950.png?HW-CC-KV=V1&HW-CC-Date=20260427T233902Z&HW-CC-Expire=86400&HW-CC-Sign=16E6358F9387A378B13656D33ED6D46736A49DF8E309C28573DBAB8D7898DDFC)

## 观察变化和行为表现

### 观察变化

@Prop装饰的数据可以观察到以下变化。

* 当装饰支持类型，可以观察到赋值的变化。简单类型完整示例请参考[父组件@State到子组件@Prop简单数据类型同步](arkts-prop.md#父组件state到子组件prop简单数据类型同步)。

  ```
  1. // 简单类型
  2. @Prop count: number;
  3. // 赋值的变化可以被观察到
  4. this.count = 1;
  5. // 复杂类型
  6. @Prop title: Model;
  7. // 可以观察到赋值的变化
  8. this.title = new Model('Hi');
  ```
* 当装饰的类型是Object或者class复杂类型时，可以观察到自身的赋值和第一层的属性的变化，属性即object.keys(observedObject)返回的所有属性。复杂类型完整示例请参考[从父组件中的@State类对象属性到@Prop简单类型的同步](arkts-prop.md#从父组件中的state类对象属性到prop简单类型的同步)。

  ```
  1. // 定义嵌套类
  2. class Info {
  3. public value: string;

  5. constructor(value: string) {
  6. this.value = value;
  7. }
  8. }

  10. class Model {
  11. public value: string;
  12. public info: Info;

  14. constructor(value: string, info: Info) {
  15. this.value = value;
  16. this.info = info;
  17. }
  18. }
  ```

  [PageSeventeen.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageSeventeen.ets#L16-L36)

  ```
  1. @Prop title: Model;
  ```

  [PageSeventeen.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageSeventeen.ets#L42-L45)

  ```
  1. // 可以观察到第一层的变化
  2. this.title.value = 'Hi';
  ```

  [PageSeventeen.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageSeventeen.ets#L68-L71)

  ```
  1. // 观察不到第二层的变化
  2. this.title.info.value = 'ArkUI';
  ```

  [PageSeventeen.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageSeventeen.ets#L77-L80)

对于嵌套场景，如果class是被@Observed装饰的，可以观察到class属性的变化，示例请参考[@Prop嵌套场景](arkts-prop.md#prop嵌套场景)。

* 当装饰的类型是数组的时候，可以观察到数组本身的赋值和数组项的添加、删除和更新。数组类型完整示例请参考[父组件@State数组项到子组件@Prop简单数据类型同步](arkts-prop.md#父组件state数组项到子组件prop简单数据类型同步)。

  ```
  1. // @Prop装饰的对象为数组时
  2. @Prop title: string[];
  3. // 数组自身的赋值可以观察到
  4. this.title = ['1'];
  5. // 数组项的赋值可以观察到
  6. this.title[0] = '2';
  7. // 删除数组项可以观察到
  8. this.title.pop();
  9. // 新增数组项可以观察到
  10. this.title.push('3');
  ```

对于@State和@Prop的同步场景：

* 使用父组件中@State变量的值初始化子组件中的@Prop装饰的变量。当@State变量变化时，该变量值也会同步更新至@Prop装饰的变量。
* @Prop装饰的变量的修改不会影响其数据源@State装饰变量的值。
* 除了@State，数据源也可以用@Link或@Prop装饰，对@Prop的同步机制是相同的。
* 数据源和@Prop装饰的变量的类型需要相同。
* 当装饰的对象是Date时，可以观察到Date整体的赋值，同时可通过调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds 更新Date的属性，详见[装饰Date类型变量](arkts-prop.md#装饰date类型变量)。
* 当装饰的变量是Map时，可以观察到Map整体的赋值，同时可通过调用Map的接口set, clear, delete 更新Map的值。详见[装饰Map类型变量](arkts-prop.md#装饰map类型变量)。
* 当装饰的变量是Set时，可以观察到Set整体的赋值，同时可通过调用Set的接口add, clear, delete 更新Set的值。详见[装饰Set类型变量](arkts-prop.md#装饰set类型变量)。

### 框架行为

理解@Prop装饰的变量值初始化和更新机制，需要了解父组件和子组件的渲染和更新流程。

1. 初始渲染：

   1. 执行父组件的build()函数，创建子组件的新实例并传递数据源。
   2. 初始化子组件@Prop装饰的变量。
2. 更新：

   1. 子组件@Prop更新时，更新仅停留在当前子组件，不会同步回父组件。
   2. 当父组件的数据源更新时，子组件的@Prop装饰的变量将被来自父组件的数据源重置，所有@Prop装饰变量的本地修改将被父组件的更新覆盖。

说明

@Prop同步数据源依赖于数据源所在组件的刷新，而应用进入后台后无法触发刷新，因此应用进入后台后，@Prop无法从数据源更新。在此场景下，若需即时数据同步，推荐使用@Link代替。

以下示例中，当@State装饰的变量message改变时，Father组件会刷新。由于Son组件使用@Prop接收了该变量，因此Father组件刷新的过程中会使用message的最新值去更新@Prop的值。@Prop更新后，会触发Son组件的刷新。

```
1. @Component
2. struct Son {
3. @Prop message: string = 'Hi';

5. build() {
6. Column() {
7. Text(this.message)
8. }
9. }
10. }

12. @Entry
13. @Component
14. struct Father {
15. @State message: string = 'Hello';

17. build() {
18. Column() {
19. Text(this.message)
20. Button(`father click`).onClick(() => {
21. this.message += '*';
22. })
23. Son({ message: this.message })
24. }
25. }
26. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageOne.ets#L16-L44)

## 限制条件

* @Prop装饰变量时会进行深拷贝，在拷贝的过程中除了基本类型、Map、Set、Date、Array外，都会丢失类型。例如，对于通过NAPI提供的复杂类型（如[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)），由于其部分实现在Native侧，因此无法在ArkTS侧通过深拷贝获得完整的数据；同样，RegExp类型在拷贝过程中会丢失原类型，导致被@Prop装饰后无法调用正则相关函数。
* @Prop不支持装饰Function类型的变量，API version 23之前，框架会抛出运行时错误。

  从API version 23开始，添加对@Prop装饰Function类型变量的校验，编译期会报错。
* 父组件传入undefined时，@Prop装饰的变量仍使用本地默认值进行初始化。

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
  18. @Prop count: number | undefined = 0;

  20. build() {
  21. Column() {
  22. Text(`Child count value: ${this.count}`)
  23. .fontSize(20)
  24. .margin(10)
  25. }
  26. }
  27. }
  ```

## 使用场景

### 父组件@State到子组件@Prop简单数据类型同步

以下示例是@State到子组件@Prop简单数据同步，父组件ParentComponent的状态变量countDownStartValue初始化子组件CountDownComponent中@Prop装饰的count，点击“Try again”，count的修改仅保留在CountDownComponent，不会同步给父组件ParentComponent。

ParentComponent的状态变量countDownStartValue的变化将重置CountDownComponent的count。

```
1. @Component
2. struct CountDownComponent {
3. @Prop count: number = 0;
4. costOfOneAttempt: number = 1;

6. build() {
7. Column() {
8. if (this.count > 0) {
9. Text(`You have ${this.count} Nuggets left`)
10. } else {
11. Text('Game over!')
12. }
13. // @Prop装饰的变量不会同步给父组件
14. Button(`Try again`).onClick(() => {
15. this.count -= this.costOfOneAttempt;
16. })
17. }
18. }
19. }

21. @Entry
22. @Component
23. struct ParentComponent {
24. @State countDownStartValue: number = 10;

26. build() {
27. Column() {
28. Text(`Grant ${this.countDownStartValue} nuggets to play.`)
29. // 父组件的数据源的修改会同步给子组件
30. Button(`+1 - Nuggets in New Game`).onClick(() => {
31. this.countDownStartValue += 1;
32. })
33. // 父组件的修改会同步给子组件
34. Button(`-1  - Nuggets in New Game`).onClick(() => {
35. this.countDownStartValue -= 1;
36. })
37. CountDownComponent({ count: this.countDownStartValue, costOfOneAttempt: 2 })
38. }
39. }
40. }
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageTwo.ets#L15-L57)

在上面的示例中：

1. CountDownComponent子组件首次创建时其@Prop装饰的count变量将从父组件@State装饰的countDownStartValue变量初始化。
2. 按“+1”或“-1”按钮时，父组件的@State装饰的countDownStartValue值会变化，这将触发父组件重新渲染，在父组件重新渲染过程中会刷新使用countDownStartValue状态变量的UI组件，并单向同步更新CountDownComponent子组件中的count值。
3. 更新count状态变量值也会触发CountDownComponent的重新渲染，在重新渲染过程中，评估使用count状态变量的if语句条件（this.count > 0），并执行true分支中的使用count状态变量的UI组件相关描述来更新Text组件的UI显示。
4. 当按下子组件CountDownComponent的“Try again”按钮时，其@Prop装饰的变量count将被更改，但是count值的更改不会影响父组件的countDownStartValue值。
5. 父组件的countDownStartValue值变化时，父组件的修改将覆盖掉子组件CountDownComponent中count本地的修改。

### 父组件@State数组项到子组件@Prop简单数据类型同步

父组件中@State如果装饰数组类型的变量，其数组项也可以初始化@Prop。以下示例中，父组件Index中@State装饰数组arr，将其数组项初始化子组件Child中@Prop装饰的value。

```
1. @Component
2. struct Child {
3. @Prop value: number = 0;

5. build() {
6. Text(`${this.value}`)
7. .fontSize(50)
8. .onClick(() => {
9. this.value++;
10. })
11. }
12. }

14. @Entry
15. @Component
16. struct Index {
17. @State arr: number[] = [1, 2, 3];

19. build() {
20. Row() {
21. Column() {
22. Child({ value: this.arr[0] })
23. Child({ value: this.arr[1] })
24. Child({ value: this.arr[2] })

26. Divider().height(5)

28. ForEach(this.arr,
29. (item: number) => {
30. Child({ value: item })
31. },
32. (item: number) => item.toString()
33. )
34. Text('replace entire arr')
35. .fontSize(50)
36. .onClick(() => {
37. // 两个数组都包含项“3”。
38. this.arr = this.arr[0] == 1 ? [3, 4, 5] : [1, 2, 3];
39. })
40. }
41. }
42. }
43. }
```

[PageFour.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageFour.ets#L16-L61)

初始渲染创建6个子组件实例，每个@Prop装饰的变量初始化都在本地拷贝了一份数组项。子组件onClick事件处理程序会更改局部变量值。

如果点击界面上的“1”六次，“2”五次、“3”四次，将所有变量的本地取值都变为“7”。

```
1. 7
2. 7
3. 7
4. ——————
5. 7
6. 7
7. 7
```

点击replace entire arr后，屏幕将显示以下信息。

```
1. 3
2. 4
3. 5
4. ——————
5. 7
6. 4
7. 5
```

* 在子组件Child中做的所有的修改都不会同步回父组件Index组件，所以即使6个组件显示都为7，但在父组件Index中，this.arr保存的值依旧是[1,2,3]。
* 点击replace entire arr，this.arr[0] == 1成立，将this.arr赋值为[3, 4, 5]。
* 因为this.arr[0]已更改，Child({value: this.arr[0]})组件将this.arr[0]更新同步到实例@Prop装饰的变量。Child({value: this.arr[1]})和Child({value: this.arr[2]})的情况也类似。
* this.arr的更改触发ForEach更新，this.arr更新的前后都有数值为3的数组项：[3, 4, 5] 和[1, 2, 3]。根据diff算法，数组项“3”将被保留，删除“1”和“2”的数组项，添加为“4”和“5”的数组项。这就意味着，数组项“3”的组件不会重新生成，而是将其移动到第一位。所以“3”对应的组件不会更新，此时“3”对应的组件数值为“7”，ForEach最终的渲染结果是“7”，“4”，“5”。

### 从父组件中的@State类对象属性到@Prop简单类型的同步

如果图书馆有一本图书和两位用户，每位用户都可以将图书标记为已读，此标记行为不会影响其他用户。从代码角度讲，对@Prop图书对象的本地更改不会同步给图书馆组件中的@State图书对象。

在此示例中，图书类可以使用@Observed装饰器，但不是必须的，只有在嵌套结构时需要此装饰器。这一点会在[从父组件中的@State数组项到@Prop class类型的同步](arkts-prop.md#从父组件中的state数组项到prop-class类型的同步)说明。

```
1. class Book {
2. public title: string;
3. public pages: number;
4. public readIt: boolean = false;

6. constructor(title: string, pages: number) {
7. this.title = title;
8. this.pages = pages;
9. }
10. }

12. @Component
13. struct ReaderComp {
14. @Prop book: Book = new Book('', 0);

16. build() {
17. Row() {
18. Text(this.book.title)
19. Text(`...has${this.book.pages} pages!`)
20. Text(`...${this.book.readIt ? 'I have read' : 'I have not read it'}`)
21. .onClick(() => this.book.readIt = true)
22. }
23. }
24. }

26. @Entry
27. @Component
28. struct Library {
29. @State book: Book = new Book('100 secrets of C++', 765);

31. build() {
32. Column() {
33. ReaderComp({ book: this.book })
34. ReaderComp({ book: this.book })
35. }
36. }
37. }
```

[PageFive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageFive.ets#L16-L55)

### 从父组件中的@State数组项到@Prop class类型的同步

以下示例中，更改了@State装饰的allBooks数组中Book对象的属性，但点击“Mark read for everyone”时，没有触发UI更新。这是因为该属性是第二层的嵌套属性，@State装饰器只能观察到第一层属性，不会观察到此属性更改，所以框架不会更新ReaderComp。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG: string = '[SampleProp]';
5. let nextId: number = 1;

7. // @Observed
8. class Book {
9. public id: number;
10. public title: string;
11. public pages: number;
12. public readIt: boolean = false;

14. constructor(title: string, pages: number) {
15. this.id = nextId++;
16. this.title = title;
17. this.pages = pages;
18. }
19. }

21. @Component
22. struct ReaderComp {
23. @Prop book: Book = new Book('', 1);

25. build() {
26. Row() {
27. Text(` ${this.book ? this.book.title : 'Book is undefined'}`).fontColor('#e6000000')
28. Text(` has ${this.book ? this.book.pages : 'Book is undefined'} pages!`).fontColor('#e6000000')
29. Text(` ${this.book ? this.book.readIt ? 'I have read' : 'I have not read it' : 'Book is undefined'}`)
30. .fontColor('#e6000000')
31. .onClick(() => this.book.readIt = true)
32. }
33. }
34. }

36. @Entry
37. @Component
38. struct Library {
39. @State allBooks: Book[] = [new Book('C#', 765), new Book('JS', 652), new Book('TS', 765)];

41. build() {
42. Column() {
43. Text('library`s all time favorite')
44. .width(312)
45. .height(40)
46. .backgroundColor('#0d000000')
47. .borderRadius(20)
48. .margin(12)
49. .padding({ left: 20 })
50. .fontColor('#e6000000')
51. ReaderComp({ book: this.allBooks[2] })
52. .backgroundColor('#0d000000')
53. .width(312)
54. .height(40)
55. .padding({ left: 20, top: 10 })
56. .borderRadius(20)
57. .colorBlend('#e6000000')
58. Text('Books on loan to a reader')
59. .width(312)
60. .height(40)
61. .backgroundColor('#0d000000')
62. .borderRadius(20)
63. .margin(12)
64. .padding({ left: 20 })
65. .fontColor('#e6000000')
66. ForEach(this.allBooks, (book: Book) => {
67. ReaderComp({ book: book })
68. .margin(12)
69. .width(312)
70. .height(40)
71. .padding({ left: 20, top: 10 })
72. .backgroundColor('#0d000000')
73. .borderRadius(20)
74. },
75. (book: Book) => book.id.toString())
76. Button('Add new')
77. .width(312)
78. .height(40)
79. .margin(12)
80. .fontColor('#FFFFFF')
81. .onClick(() => {
82. this.allBooks.push(new Book('JA', 512));
83. })
84. Button('Remove first book')
85. .width(312)
86. .height(40)
87. .margin(12)
88. .fontColor('#FFFFFF')
89. .onClick(() => {
90. if (this.allBooks.length > 0) {
91. this.allBooks.shift();
92. } else {
93. hilog.info(DOMAIN, TAG, 'length <= 0');
94. }
95. })
96. Button('Mark read for everyone')
97. .width(312)
98. .height(40)
99. .margin(12)
100. .fontColor('#FFFFFF')
101. .onClick(() => {
102. this.allBooks.forEach((book) => book.readIt = true)
103. })
104. }
105. }
106. }
```

[PageSix.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageSix.ets#L16-L124)

使用@Observed装饰class Book，Book的属性变化将被观察。需要注意的是，@Prop在子组件装饰的状态变量和父组件的数据源是单向同步关系，即ReaderComp中的@Prop book的修改不会同步给父组件Library。而父组件只会在状态变量发生变化的时候，才会触发UI的重新渲染。

```
1. @Observed
2. class Book {
3. public id: number;
4. public title: string;
5. public pages: number;
6. public readIt: boolean = false;

8. constructor(title: string, pages: number) {
9. this.id = nextId++;
10. this.title = title;
11. this.pages = pages;
12. }
13. }
```

@Observed装饰的类的实例会被不透明的代理对象包装，此代理可以检测到包装对象内的所有属性更改。如果发生这种情况，此时，代理通知@Prop，@Prop对象值被更新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/HtizzWTgRzOHtVZjTmZqZw/zh-cn_image_0000002583437645.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233902Z&HW-CC-Expire=86400&HW-CC-Sign=EF4C25F2DB063FF0F07BF7E74A8F5B3D162F533F80FBAD3703A0EE9567F8413C)

### @Prop本地初始化不和父组件同步

为了支持@Component装饰的组件复用场景，@Prop支持本地初始化，这样可以让@Prop是否与父组件建立同步关系变得可选。当且仅当@Prop有本地初始化时，从父组件向子组件传递@Prop的数据源才是可选的。

下面的示例中，子组件包含两个@Prop装饰的变量：

* @Prop customCounter没有本地初始化，所以需要父组件提供数据源去初始化@Prop，并当父组件的数据源变化时，@Prop也将被更新。
* @Prop customCounter2有本地初始化，在这种情况下，@Prop依旧允许但非强制父组件同步数据源给@Prop。

```
1. @Component
2. struct MyComponent {
3. @Prop customCounter: number;
4. @Prop customCounter2: number = 5;

6. build() {
7. Column() {
8. Row() {
9. Text(`From Main: ${this.customCounter}`).fontColor('#ff6b6565').margin({ left: -110, top: 12 })
10. }

12. Row() {
13. Button('Click to change locally!')
14. .width(288)
15. .height(40)
16. .margin({ left: 30, top: 12 })
17. .fontColor('#FFFFFF')
18. .onClick(() => {
19. this.customCounter2++;
20. })
21. }

23. Row() {
24. Text(`Custom Local: ${this.customCounter2}`).fontColor('#ff6b6565').margin({ left: -110, top: 12 })
25. }
26. }
27. }
28. }

30. @Entry
31. @Component
32. struct MainProgram {
33. @State mainCounter: number = 10;

35. build() {
36. Column() {
37. Row() {
38. Column() {
39. // customCounter必须从父组件初始化，因为MyComponent的customCounter成员变量缺少本地初始化；此处，customCounter2可以不做初始化
40. MyComponent({ customCounter: this.mainCounter })
41. // customCounter2也可以从父组件初始化，父组件初始化的值会覆盖子组件customCounter2的本地初始化的值
42. MyComponent({ customCounter: this.mainCounter, customCounter2: this.mainCounter })
43. }
44. }

46. Row() {
47. Column() {
48. Button('Click to change number')
49. .width(288)
50. .height(40)
51. .margin({ left: 30, top: 12 })
52. .fontColor('#FFFFFF')
53. .onClick(() => {
54. this.mainCounter++;
55. })
56. }
57. }
58. }
59. }
60. }
```

[PageSeven.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageSeven.ets#L16-L78)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ysq3D80ATqGFePM20II4fA/zh-cn_image_0000002552957600.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233902Z&HW-CC-Expire=86400&HW-CC-Sign=C26E5C743A30EB372E9A5BB2B31661D4059F26E250C62B64EC89EC431EC02A66)

### @Prop嵌套场景

在嵌套场景下，每一层都要用@Observed装饰，且每一层都要被@Prop接收，这样才能观察到嵌套场景。

```
1. // 以下是嵌套类对象的数据结构。
2. @Observed
3. class Son {
4. public title: string;

6. constructor(title: string) {
7. this.title = title;
8. }
9. }

11. @Observed
12. class Father {
13. public name: string;
14. public son: Son;

16. constructor(name: string, son: Son) {
17. this.name = name;
18. this.son = son;
19. }
20. }
```

[PageEight.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageEight.ets#L15-L37)

以下组件层次结构展示了@Prop嵌套场景的数据结构。

```
1. @Entry
2. @Component
3. struct Person {
4. @State person: Father = new Father('Hello', new Son('world'));

6. build() {
7. Column() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
9. Button('change Father name')
10. .width(312)
11. .height(40)
12. .margin(12)
13. .fontColor('#FFFFFF')
14. .onClick(() => {
15. this.person.name = 'Hi';
16. })
17. Button('change Son title')
18. .width(312)
19. .height(40)
20. .margin(12)
21. .fontColor('#FFFFFF')
22. .onClick(() => {
23. // person被@State装饰，@State无法观测到嵌套类型的变化，直接点击该按钮，此时title已经发生变化，但是无法被观测到。
24. this.person.son.title = 'ArkUI';
25. })
26. Text(this.person.name)
27. .fontSize(16)
28. .margin(12)
29. .width(312)
30. .height(40)
31. .backgroundColor('#ededed')
32. .borderRadius(20)
33. .textAlign(TextAlign.Center)
34. .fontColor('#e6000000')
35. .onClick(() => {
36. // 点击该按钮，此次变化会被观测到，同时能够观察到Button('change Son title')点击后的效果。
37. this.person.name = 'Bye';
38. })
39. Text(this.person.son.title)
40. .fontSize(16)
41. .margin(12)
42. .width(312)
43. .height(40)
44. .backgroundColor('#ededed')
45. .borderRadius(20)
46. .textAlign(TextAlign.Center)
47. .onClick(() => {
48. this.person.son.title = 'openHarmony';
49. })
50. Child({ child: this.person.son })
51. }
52. }
53. }
54. }

57. @Component
58. struct Child {
59. @Prop child: Son = new Son('');

61. build() {
62. Column() {
63. Text(this.child.title)
64. .fontSize(16)
65. .margin(12)
66. .width(312)
67. .height(40)
68. .backgroundColor('#ededed')
69. .borderRadius(20)
70. .textAlign(TextAlign.Center)
71. .onClick(() => {
72. this.child.title = 'Bye Bye';
73. })
74. }
75. }
76. }
```

[PageNine.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageNine.ets#L36-L114)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/zAKZ67JuQwePNrXhR7jBKQ/zh-cn_image_0000002583477601.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233902Z&HW-CC-Expire=86400&HW-CC-Sign=8FE73C8C85C6ED781CCB406AE880D37E9A2B038A26CD41AFA800F51596042413)

### 装饰Array类型变量

在下面的示例中，message类型为number[]，点击Button改变message的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: number[] = [0, 1, 2, 3];

6. build() {
7. Column() {
8. Child({ message: this.message })
9. }
10. }
11. }

13. @Component
14. struct Child {
15. @Prop message: number[] = [0, 1, 2, 3];

17. build() {
18. Row() {
19. Column() {
20. ForEach(this.message, (item: number) => {
21. Text(`${item}`)
22. .fontSize(20)
23. .margin(10)
24. })
25. // 新增数组元素，触发UI刷新
26. Button('Push element')
27. .onClick(() => {
28. this.message.push(4);
29. })
30. .width(300)
31. .margin(10)
32. // 删除数组元素，触发UI刷新
33. Button('Pop element')
34. .onClick(() => {
35. this.message.pop();
36. })
37. .width(300)
38. .margin(10)
39. // 对数组整体重新赋值，触发UI刷新
40. Button('Reset array')
41. .onClick(() => {
42. this.message = [9, 8, 7, 6];
43. })
44. .width(300)
45. .margin(10)
46. // 更新数组元素，触发UI刷新
47. Button('Modify element[0]')
48. .onClick(() => {
49. this.message[0] = 10;
50. })
51. .width(300)
52. .margin(10)
53. }
54. .width('100%')
55. }
56. .height('100%')
57. }
58. }
```

### 装饰Map类型变量

说明

从API version 11开始，@Prop支持Map类型。

在下面的示例中，value类型为Map<number, string>，点击Button改变value的值，视图会随之刷新。

```
1. @Component
2. struct Child {
3. @Prop value: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);

5. build() {
6. Column() {
7. ForEach(Array.from(this.value.entries()), (item: [number, string]) => {
8. Text(`${item[0]}`).fontSize(30)
9. Text(`${item[1]}`).fontSize(30)
10. Divider()
11. })
12. Button('child init map').onClick(() => {
13. this.value = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
14. })
15. Button('child set new one').onClick(() => {
16. this.value.set(4, 'd');
17. })
18. Button('child clear').onClick(() => {
19. this.value.clear();
20. })
21. Button('child replace the first one').onClick(() => {
22. this.value.set(0, 'aa');
23. })
24. Button('child delete the first one').onClick(() => {
25. this.value.delete(0);
26. })
27. }
28. }
29. }

32. @Entry
33. @Component
34. struct MapSample {
35. @State message: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);

37. build() {
38. Row() {
39. Column() {
40. Child({ value: this.message })
41. }
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```

[PageTen.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageTen.ets#L16-L64)

### 装饰Set类型变量

说明

从API version 11开始，@Prop支持Set类型。

在下面的示例中，message类型为Set<number>，点击Button改变message的值，视图会随之刷新。

```
1. @Component
2. struct Child {
3. @Prop message: Set<number> = new Set([0, 1, 2, 3, 4]);

5. build() {
6. Column() {
7. ForEach(Array.from(this.message.entries()), (item: [number, number]) => {
8. Text(`${item[0]}`).fontSize(30)
9. Divider()
10. })
11. Button('init set').onClick(() => {
12. this.message = new Set([0, 1, 2, 3, 4]);
13. })
14. Button('set new one').onClick(() => {
15. this.message.add(5);
16. })
17. Button('clear').onClick(() => {
18. this.message.clear();
19. })
20. Button('delete the first one').onClick(() => {
21. this.message.delete(0);
22. })
23. }
24. .width('100%')
25. }
26. }

29. @Entry
30. @Component
31. struct SetSample {
32. @State message: Set<number> = new Set([0, 1, 2, 3, 4]);

34. build() {
35. Row() {
36. Column() {
37. Child({ message: this.message })
38. }
39. .width('100%')
40. }
41. .height('100%')
42. }
43. }
```

[PageEleven.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageEleven.ets#L16-L61)

### 装饰Date类型变量

在下面的示例中，selectedDate类型为Date，点击Button改变Date的值，视图会随之刷新。

```
1. @Component
2. struct DateComponent {
3. @Prop selectedDate: Date = new Date('');

5. build() {
6. Column() {
7. Button('child update the new date')
8. .margin(10)
9. .onClick(() => {
10. this.selectedDate = new Date('2023-09-09');
11. })
12. Button(`child increase the year by 1`).onClick(() => {
13. this.selectedDate.setFullYear(this.selectedDate.getFullYear() + 1);
14. })
15. DatePicker({
16. start: new Date('1970-1-1'),
17. end: new Date('2100-1-1'),
18. selected: this.selectedDate
19. })
20. }
21. }
22. }

24. @Entry
25. @Component
26. struct ParentComponent {
27. @State parentSelectedDate: Date = new Date('2021-08-08');

29. build() {
30. Column() {
31. Button('parent update the new date')
32. .margin(10)
33. .onClick(() => {
34. this.parentSelectedDate = new Date('2023-07-07');
35. })
36. Button('parent increase the day by 1')
37. .margin(10)
38. .onClick(() => {
39. this.parentSelectedDate.setDate(this.parentSelectedDate.getDate() + 1);
40. })
41. DatePicker({
42. start: new Date('1970-1-1'),
43. end: new Date('2100-1-1'),
44. selected: this.parentSelectedDate
45. })

47. DateComponent({ selectedDate: this.parentSelectedDate })
48. }
49. }
50. }
```

[PageTwelve.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageTwelve.ets#L16-L68)

### Prop支持联合类型实例

@Prop支持联合类型和undefined和null，在下面的示例中，animal类型为Animals | undefined，点击父组件Zoo中的Button改变animal的属性或者类型，Child中也会对应刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG: string = '[SampleProp]';

6. class Animals {
7. public name: string;

9. constructor(name: string) {
10. this.name = name;
11. }
12. }

14. @Component
15. struct Child {
16. @Prop animal: Animals | undefined;

18. build() {
19. Column() {
20. Text(`Child's animal is  ${this.animal instanceof Animals ? this.animal.name : 'undefined'}`).fontSize(30)

22. Button('Child change animals into tigers')
23. .onClick(() => {
24. // 赋值为Animals的实例
25. this.animal = new Animals('Tiger');
26. })

28. Button('Child change animal to undefined')
29. .onClick(() => {
30. // 赋值为undefined
31. this.animal = undefined;
32. })

34. }.width('100%')
35. }
36. }

38. @Entry
39. @Component
40. struct Zoo {
41. @State animal: Animals | undefined = new Animals('lion');

43. build() {
44. Column() {
45. Text(`Parents' animals are  ${this.animal instanceof Animals ? this.animal.name : 'undefined'}`).fontSize(30)

47. Child({ animal: this.animal })

49. Button('Parents change animals into dogs')
50. .onClick(() => {
51. // 判断animal的类型，做属性的更新
52. if (this.animal instanceof Animals) {
53. this.animal.name = 'Dog';
54. } else {
55. hilog.info(DOMAIN, TAG, 'num is undefined, cannot change property');
56. }
57. })

59. Button('Parents change animal to undefined')
60. .onClick(() => {
61. // 赋值为undefined
62. this.animal = undefined;
63. })
64. }
65. }
66. }
```

[PageThirteen.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Prop/entry/src/main/ets/pages/PageThirteen.ets#L16-L84)
