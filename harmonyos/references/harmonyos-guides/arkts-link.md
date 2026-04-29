---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-link
title: @Link装饰器：父子双向同步
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理组件拥有的状态 > @Link装饰器：父子双向同步
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:15+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:de29897ba0cdc3dfb5309927c0aa270791bcc22df00b83e3f080b25ff36b3b83
---

子组件中被@Link装饰的变量与其父组件中对应的数据源建立双向数据绑定。

在阅读@Link文档前，建议先熟悉[@State](arkts-state.md)的基本用法。最佳实践请参考[状态管理最佳实践](../best-practices/bpta-status-management.md)。常见问题请参考[状态管理常见问题](arkts-state-management-faq.md)。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 概述

@Link装饰的变量与其父组件中的数据源共享相同的值。

## 装饰器使用规则说明

| @Link变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 同步类型 | 双向同步。  父组件状态变量与子组件@Link建立双向同步，当其中一方改变时，另一方也会同步更新。 |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum类型，以及这些类型的数组。  API version 10开始支持[Date类型](arkts-link.md#装饰date类型变量)。  API version 11及以上支持[Map](arkts-link.md#装饰map类型变量)、[Set](arkts-link.md#装饰set类型变量)类型、undefined和null类型、ArkUI框架定义的联合类型[Length](../harmonyos-references/ts-types.md#length)、[ResourceStr](../harmonyos-references/ts-types.md#resourcestr)、[ResourceColor](../harmonyos-references/ts-types.md#resourcecolor)类型以及这些类型的联合类型，示例见[Link支持联合类型实例](arkts-link.md#link支持联合类型实例)。  支持类型的场景请参考[观察变化](arkts-link.md#观察变化)。 |
| 不允许装饰的变量类型 | 不支持装饰Function类型。 |
| 被装饰变量的初始值 | 禁止本地初始化。 |

## 变量的传递/访问规则说明

| 传递/访问 | 说明 |
| --- | --- |
| 从父组件初始化和更新 | 必选。  允许父组件中[@State](arkts-state.md)、@Link、[@Prop](arkts-prop.md)、[@Provide](arkts-provide-and-consume.md)、[@Consume](arkts-provide-and-consume.md)、[@ObjectLink](arkts-observed-and-objectlink.md)、[@StorageLink](arkts-appstorage.md#storagelink)、[@StorageProp](arkts-appstorage.md#storageprop)、[@LocalStorageLink](arkts-localstorage.md#localstoragelink)和[@LocalStorageProp](arkts-localstorage.md#localstorageprop)装饰变量初始化子组件@Link，并建立双向绑定。  - 从API version 9开始，@Link子组件从父组件初始化@State的语法为Comp({ aLink: this.aState })，同样支持Comp({aLink: $aState})。 |
| 用于初始化子组件 | 允许，可用于初始化常规变量、@State、@Link、@Prop、@Provide。 |
| 是否支持组件外访问 | 私有，只能在所属组件内访问。 |

**图1** 初始化规则示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/1BTv6K7TT06OYAza9a_xXg/zh-cn_image_0000002558764092.png?HW-CC-KV=V1&HW-CC-Date=20260429T052713Z&HW-CC-Expire=86400&HW-CC-Sign=CF91EB83665877FD37D23E5128C859008D870CFFDD9CD891D5B48C1B6F181713)

## 观察变化和行为表现

### 观察变化

* 当装饰的数据类型为boolean、string、number类型时，可以同步观察到数值的变化，示例请参考[简单类型和类对象类型的@Link](arkts-link.md#简单类型和类对象类型的link)。
* 当装饰的数据类型为class或者Object时，可以观察到赋值和属性赋值的变化，即Object.keys(observedObject)返回的所有属性，示例请参考[简单类型和类对象类型的@Link](arkts-link.md#简单类型和类对象类型的link)。@Link仅能观察对象本身及其一层属性的变化，无法观察嵌套场景（如嵌套对象、对象数组）内层数据的变化，该场景请参考[@Observed装饰器与@ObjectLink装饰器的使用场景](arkts-observed-and-objectlink.md#使用场景)。
* 当装饰的对象是Array时，可以观察到数组添加、删除、更新数组单元的变化，示例请参考[数组类型的@Link](arkts-link.md#数组类型的link)。
* 当装饰的对象是Date时，可以观察到Date的整体赋值，以及通过调用setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds方法更新其属性，示例请参考[装饰Date类型变量](arkts-link.md#装饰date类型变量)。
* 当装饰的变量是Map时，可以观察到Map整体的赋值，以及可通过调用Map的set、clear、delete接口更新Map的值，示例请参考[装饰Map类型变量](arkts-link.md#装饰map类型变量)。
* 当装饰的变量是Set时，可以观察Set整体的赋值，以及通过调用Set的add、clear、delete接口更新其值，示例请参考[装饰Set类型变量](arkts-link.md#装饰set类型变量)。

### 框架行为

@Link装饰的变量和所属的自定义组件共享生命周期。

为了了解@Link变量的初始化和更新机制，有必要先了解父组件和拥有@Link变量的子组件的关系，以及初始渲染和双向更新的流程（以父组件为@State为例）。

1. 初始渲染：执行父组件的 build() 函数，创建子组件的新实例。初始化过程如下：

   1. 指定父组件中的@State变量用于初始化子组件的@Link变量。子组件的@Link变量值与其父组件的数据源变量保持双向数据同步。
   2. 父组件的@State状态变量包装类通过构造函数传给子组件，子组件的@Link包装类拿到父组件的@State的状态变量后，将当前@Link包装类实例注册给父组件的@State变量。
2. @Link的数据源的更新：即父组件中状态变量更新，引起相关子组件的@Link的更新。处理步骤：

   1. 通过初始渲染的步骤可知，子组件@Link包装类把当前this指针注册给父组件。父组件@State变量变更后，会遍历更新所有依赖它的系统组件和状态变量（例如：@Link包装类）。
   2. 通知@Link包装类更新后，子组件中所有依赖@Link状态变量的系统组件都会被通知更新。以此实现父组件对子组件的状态数据同步。
3. @Link的更新：当子组件中@Link更新后，处理步骤如下（以父组件为@State为例）：

   1. @Link更新后，调用父组件的@State包装类的set方法，将数值同步回父组件。
   2. 子组件@Link和父组件@State分别遍历依赖的系统组件，更新对应的UI。从而实现子组件@Link与父组件@State的同步。

## 限制条件

1. @Link装饰器不建议在[@Entry](arkts-create-custom-components.md#entry)装饰的自定义组件中使用，否则编译时会抛出警告；若该自定义组件作为页面根节点使用，则会抛出运行时错误。
2. @Link装饰的变量禁止本地初始化，否则编译期会报错。

   ```
   1. // 错误写法，编译报错
   2. @Link count: number = 10;

   4. // 正确写法
   5. @Link count: number;
   ```
3. @Link装饰的变量的类型要和数据源类型保持一致，否则编译期会报错。同时，数据源必须是状态变量，否则框架会抛出运行时错误。

   说明

   从API version 23开始，添加对@Link数据源错误的校验，运行时错误变为编译期报错。详情参见[UI相关应用崩溃常见问题](arkts-stability-crash-issues.md)。

   【反例】

   ```
   1. class Info {
   2. value: string = 'Hello';
   3. }

   5. class Cousin {
   6. name: string = 'Hello';
   7. }

   9. @Component
   10. struct Child {
   11. // 错误写法1：@Link装饰的变量与@State装饰的变量类型不一致
   12. @Link test: Cousin;
   13. // 错误写法2：数据源非状态变量
   14. @Link testStr: string;

   16. build() {
   17. Column() {
   18. Text(this.test.name)
   19. Text(this.testStr)
   20. }
   21. }
   22. }

   24. @Entry
   25. @Component
   26. struct LinkExample {
   27. @State info: Info = new Info();

   29. build() {
   30. Column() {
   31. Child({
   32. // 错误写法1：@Link装饰的变量与@State装饰的变量类型不一致
   33. test: this.info,
   34. // 错误写法2：数据源非状态变量
   35. testStr: this.info.value
   36. })
   37. }
   38. }
   39. }
   ```

   【正例】

   ```
   1. class LinkInfo {
   2. public value: string = 'Hello';
   3. }

   5. @Component
   6. struct LinkChild {
   7. // 在子组件中，使用@Link装饰LinkInfo类型的test变量
   8. @Link test: LinkInfo;

   10. build() {
   11. Text(this.test.value)
   12. }
   13. }

   15. @Entry
   16. @Component
   17. struct LinkExample {
   18. @State info: LinkInfo = new LinkInfo();

   20. build() {
   21. Column() {
   22. // 在父组件中，使用@State装饰的info变量初始化LinkChild组件的test变量
   23. LinkChild({test: this.info})
   24. }
   25. }
   26. }
   ```

   [LinkUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/LinkUsage.ets#L16-L43)
4. @Link装饰的变量仅能被状态变量初始化，不能使用常规变量初始化，否则编译期会给出告警，并在运行时崩溃。

   【反例】

   ```
   1. class Info {
   2. info: string = 'Hello';
   3. }

   5. @Component
   6. struct Child {
   7. @Link msg: string;
   8. @Link info: string;

   10. build() {
   11. Text(this.msg + this.info)
   12. }
   13. }

   15. @Entry
   16. @Component
   17. struct LinkExample {
   18. @State message: string = 'Hello';
   19. @State info: Info = new Info();

   21. build() {
   22. Column() {
   23. // 错误写法，常规变量不能初始化@Link
   24. Child({msg: 'World', info: this.info.info})
   25. }
   26. }
   27. }
   ```

   【正例】

   ```
   1. class LinkInfo2 {
   2. public info: string = 'Hello';
   3. }

   5. @Component
   6. struct LinkChild2 {
   7. @Link msg: string;
   8. @Link info: LinkInfo2;

   10. build() {
   11. Text(this.msg + this.info.info)
   12. }
   13. }

   15. @Entry
   16. @Component
   17. struct LinkExample2 {
   18. @State message: string = 'Hello';
   19. @State info: LinkInfo2 = new LinkInfo2();

   21. build() {
   22. Column() {
   23. // 正确写法
   24. LinkChild2({msg: this.message, info: this.info})
   25. }
   26. }
   27. }
   ```

   [LinkUsage2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/LinkUsage2.ets#L16-L44)
5. @Link不支持装饰Function类型的变量，API version 23之前，框架会抛出运行时错误。

   从API version 23开始，添加对@Link装饰Function类型变量的校验，编译期会报错。

## 使用场景

### 简单类型和类对象类型的@Link

以下示例中，点击父组件ShufflingContainer中的“Parent View: Set yellowButton”和“Parent View: Set GreenButton”，可以从父组件将变化同步给子组件。

1.点击子组件GreenButton和YellowButton中的Button，子组件会发生相应变化，将变化同步给父组件。因为@Link是双向同步，会将变化同步给@State。

2.当点击父组件ShufflingContainer中的Button时，@State会发生变化，并同步给@Link，子组件也会进行对应的刷新。

```
1. class GreenButtonState {
2. public width: number = 0;

4. constructor(width: number) {
5. this.width = width;
6. }
7. }

9. @Component
10. struct GreenButton {
11. @Link greenButtonState: GreenButtonState;

13. build() {
14. Button('Green Button')
15. .width(this.greenButtonState.width)
16. .height(40)
17. .backgroundColor('#64bb5c')
18. .fontColor('#FFFFFF')
19. .onClick(() => {
20. if (this.greenButtonState.width < 700) {
21. // 更新class的属性，变化可以被观察到同步回父组件
22. this.greenButtonState.width += 60;
23. } else {
24. // 更新class，变化可以被观察到同步回父组件
25. this.greenButtonState = new GreenButtonState(180);
26. }
27. })
28. }
29. }

31. @Component
32. struct YellowButton {
33. @Link yellowButtonState: number;

35. build() {
36. Button('Yellow Button')
37. .width(this.yellowButtonState)
38. .height(40)
39. .backgroundColor('#f7ce00')
40. .fontColor('#FFFFFF')
41. .onClick(() => {
42. // 子组件的简单类型可以同步回父组件
43. this.yellowButtonState += 40.0;
44. })
45. }
46. }

48. @Entry
49. @Component
50. struct ShufflingContainer {
51. @State greenButtonState: GreenButtonState = new GreenButtonState(180);
52. @State yellowButtonProp: number = 180;

54. build() {
55. Column() {
56. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
57. // 简单类型从父组件@State向子组件@Link数据同步
58. Button('Parent View: Set yellowButton')
59. .width(this.yellowButtonProp)
60. .height(40)
61. .margin(12)
62. .fontColor('#FFFFFF')
63. .onClick(() => {
64. this.yellowButtonProp = (this.yellowButtonProp < 700) ? this.yellowButtonProp + 40 : 100;
65. })
66. // class类型从父组件@State向子组件@Link数据同步
67. Button('Parent View: Set GreenButton')
68. .width(this.greenButtonState.width)
69. .height(40)
70. .margin(12)
71. .fontColor('#FFFFFF')
72. .onClick(() => {
73. this.greenButtonState.width = (this.greenButtonState.width < 700) ? this.greenButtonState.width + 100 : 100;
74. })
75. // class类型初始化@Link
76. GreenButton({ greenButtonState: this.greenButtonState }).margin(12)
77. // 简单类型初始化@Link
78. YellowButton({ yellowButtonState: this.yellowButtonProp }).margin(12)
79. }
80. }
81. }
82. }
```

[UsingLinkwithPrimitiveandClassTypes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/UsingLinkwithPrimitiveandClassTypes.ets#L16-L99)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/1NYfFlWISnadhXSLTKcUiA/zh-cn_image_0000002558604436.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052713Z&HW-CC-Expire=86400&HW-CC-Sign=BE411DC394F66C9462A28682E86CEEA44D25FF858C424891A16278DBD4C53BB8)

### 数组类型的@Link

```
1. @Component
2. struct ArrayTypesChild {
3. @Link items: number[];

5. build() {
6. Column() {
7. Button(`Button1: push`)
8. .margin(12)
9. .width(312)
10. .height(40)
11. .fontColor('#FFFFFF')
12. .onClick(() => {
13. this.items.push(this.items.length + 1);
14. })
15. // 子组件的数组类型可以同步回父组件
16. Button(`Button2: replace whole item`)
17. .margin(12)
18. .width(312)
19. .height(40)
20. .fontColor('#FFFFFF')
21. .onClick(() => {
22. this.items = [100, 200, 300];
23. })
24. }
25. }
26. }

28. @Entry
29. @Component
30. struct ArrayTypes {
31. @State arr: number[] = [1, 2, 3];

33. build() {
34. Column() {
35. ArrayTypesChild({ items: $arr })
36. .margin(12)
37. ForEach(this.arr,
38. (item: number) => {
39. Button(`${item}`)
40. .margin(12)
41. .width(312)
42. .height(40)
43. .backgroundColor('#11a2a2a2')
44. .fontColor('#e6000000')
45. },
46. (item: ForEachInterface) => item.toString()
47. )
48. }
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/OmM9dKRbT_Kol3K8jSTDUA/zh-cn_image_0000002589323961.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052713Z&HW-CC-Expire=86400&HW-CC-Sign=574C766D0F860DF810FE32C02662163840A34CEA6858259A5511538FE3714447)

状态管理框架可以观察到数组元素的添加、删除和替换。在该示例中，@State和@Link的类型均为number[]，不支持将@Link定义成number类型（@Link item : number），并用@State数组中的每个数据项在父组件中创建子组件。如需使用这种场景，可以参考[@Prop](arkts-prop.md)和[@Observed](arkts-observed-and-objectlink.md)。

### 装饰Map类型变量

说明

从API version 11开始，@Link支持Map类型。

在下面的示例中，value类型为Map<number, string>，点击Button改变message的值，视图会随之刷新。

```
1. @Component
2. struct MapSampleChild {
3. @Link value: Map<number, string>;

5. build() {
6. Column() {
7. ForEach(Array.from(this.value.entries()), (item: [number, string]) => {
8. Text(`${item[0]}`).fontSize(30)
9. Text(`${item[1]}`).fontSize(30)
10. Divider()
11. })
12. // 子组件的Map类型可以同步回父组件
13. Button('child init map').onClick(() => {
14. this.value = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
15. })
16. Button('child set new one').onClick(() => {
17. this.value.set(4, 'd');
18. })
19. Button('child clear').onClick(() => {
20. this.value.clear();
21. })
22. Button('child replace the first one').onClick(() => {
23. this.value.set(0, 'aa');
24. })
25. Button('child delete the first one').onClick(() => {
26. this.value.delete(0);
27. })
28. }
29. }
30. }

33. @Entry
34. @Component
35. struct MapSample {
36. @State message: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);

38. build() {
39. Row() {
40. Column() {
41. MapSampleChild({ value: this.message })
42. }
43. .width('100%')
44. }
45. .height('100%')
46. }
47. }
```

[DecoratingVariablesMapType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/DecoratingVariablesMapType.ets#L16-L63)

### 装饰Set类型变量

说明

从API version 11开始，@Link支持Set类型。

在下面的示例中，message类型为Set<number>，点击Button改变message的值，视图会随之刷新。

```
1. @Component
2. struct SetSampleChild {
3. @Link message: Set<number>;

5. build() {
6. Column() {
7. ForEach(Array.from(this.message.entries()), (item: [number, number]) => {
8. Text(`${item[0]}`).fontSize(30)
9. Divider()
10. })
11. // 子组件的Set类型可以同步回父组件
12. Button('init set').onClick(() => {
13. this.message = new Set([0, 1, 2, 3, 4]);
14. })
15. Button('set new one').onClick(() => {
16. this.message.add(5);
17. })
18. Button('clear').onClick(() => {
19. this.message.clear();
20. })
21. Button('delete the first one').onClick(() => {
22. this.message.delete(0);
23. })
24. }
25. .width('100%')
26. }
27. }

30. @Entry
31. @Component
32. struct SetSample {
33. @State message: Set<number> = new Set([0, 1, 2, 3, 4]);

35. build() {
36. Row() {
37. Column() {
38. SetSampleChild({ message: this.message })
39. }
40. .width('100%')
41. }
42. .height('100%')
43. }
44. }
```

[DecoratingVariablesSetType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/DecoratingVariablesSetType.ets#L16-L60)

### 装饰Date类型变量

在下面的示例中，selectedDate类型为Date，点击Button改变selectedDate的值，视图会随之刷新。

```
1. @Component
2. struct DateComponent {
3. @Link selectedDate: Date;

5. build() {
6. Column() {
7. // 子组件的Date类型可以同步回父组件
8. Button(`child increase the year by 1`)
9. .onClick(() => {
10. this.selectedDate.setFullYear(this.selectedDate.getFullYear() + 1);
11. })
12. Button('child update the new date')
13. .margin(10)
14. .onClick(() => {
15. this.selectedDate = new Date('2023-09-09');
16. })
17. DatePicker({
18. start: new Date('1970-1-1'),
19. end: new Date('2100-1-1'),
20. selected: this.selectedDate
21. })
22. }
23. }
24. }

26. @Entry
27. @Component
28. struct ParentComponent {
29. @State parentSelectedDate: Date = new Date('2021-08-08');

31. build() {
32. Column() {
33. Button('parent increase the month by 1')
34. .margin(10)
35. .onClick(() => {
36. this.parentSelectedDate.setMonth(this.parentSelectedDate.getMonth() + 1);
37. })
38. Button('parent update the new date')
39. .margin(10)
40. .onClick(() => {
41. this.parentSelectedDate = new Date('2023-07-07');
42. })
43. DatePicker({
44. start: new Date('1970-1-1'),
45. end: new Date('2100-1-1'),
46. selected: this.parentSelectedDate
47. })

49. DateComponent({ selectedDate:this.parentSelectedDate })
50. }
51. }
52. }
```

[DecoratingVariablesDateType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/DecoratingVariablesDateType.ets#L16-L68)

### 使用双向同步机制更改本地其他变量

通过[@Watch](arkts-watch.md)可以在双向同步时更改本地变量。

以下示例中，在@Link的@Watch里面修改了一个@State装饰的变量memberMessage，实现父子组件间的变量同步。但是@State装饰的变量memberMessage在本地修改不会影响到父组件中的变量改变。

```
1. @Entry
2. @Component
3. struct ChangeVariables {
4. @State sourceNumber: number = 0;

6. build() {
7. Column() {
8. Text(`sourceNumber of the parent component:` + this.sourceNumber)
9. ChangeVariablesChild({ sourceNumber: this.sourceNumber })
10. // sourceNumber的修改不会影响到父组件中的变量改变
11. Button('Change sourceNumber in Parent Component')
12. .onClick(() => {
13. this.sourceNumber++;
14. })
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }

21. @Component
22. struct ChangeVariablesChild {
23. @State memberMessage: string = 'Hello World';
24. @Link @Watch('onSourceChange') sourceNumber: number;

26. onSourceChange() {
27. this.memberMessage = this.sourceNumber.toString();
28. }

30. build() {
31. Column() {
32. Text(this.memberMessage)
33. Text(`sourceNumber of the child component:` + this.sourceNumber.toString())
34. Button('Change memberMessage in Child Component')
35. .onClick(() => {
36. this.memberMessage = 'Hello memberMessage';
37. })
38. }
39. }
40. }
```

[UseWatchToChangeLocalVariables.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/UseWatchToChangeLocalVariables.ets#L16-L56)

### Link支持联合类型实例

@Link支持联合类型、undefined和null。在以下示例中，name类型为string | undefined。点击父组件UnionTypes中的按钮可以改变name的属性或类型，UnionChild组件也会相应刷新。

```
1. @Component
2. struct UnionChild {
3. // @Link支持联合类型
4. @Link name: string | undefined;

6. build() {
7. Column() {

9. Button('Child change name to Bob')
10. .onClick(() => {
11. this.name = 'Bob';
12. })

14. Button('Child change name to undefined')
15. .onClick(() => {
16. this.name = undefined;
17. })

19. }.width('100%')
20. }
21. }

23. @Entry
24. @Component
25. struct UnionTypes {
26. @State name: string | undefined = 'mary';

28. build() {
29. Column() {
30. Text(`The name is  ${this.name}`).fontSize(30)

32. UnionChild({ name: this.name })

34. Button('Parents change name to Peter')
35. .onClick(() => {
36. this.name = 'Peter';
37. })

39. Button('Parents change name to undefined')
40. .onClick(() => {
41. this.name = undefined;
42. })
43. }
44. }
45. }
```

[UsingUnionTypes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentStateManagement/entry/src/main/ets/pages/LinkDecorator/UsingUnionTypes.ets#L16-L61)
