---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage
title: AppStorage：应用全局的UI状态存储
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理应用拥有的状态 > AppStorage：应用全局的UI状态存储
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:16+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e7d3f14186c3a44797ee3edf01be7b3586a80d7499c8ed38c68debdc9f3f98a8
---

在阅读本文档前，建议提前阅读：[状态管理概述](arkts-state-management-overview.md)，从而对状态管理框架中AppStorage的定位有一个宏观了解。

AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。

作为应用的“中枢”，AppStorage是[持久化数据PersistentStorage](arkts-persiststorage.md)和[环境变量Environment](arkts-environment.md)与UI交互的中转桥梁。其核心价值在于为开发者提供跨ability的大范围UI状态数据共享能力。

AppStorage提供了API接口，允许开发者在自定义组件外手动触发AppStorage对应属性的增、删、改、查操作。建议配合[AppStorage API文档](../harmonyos-references/ts-state-management.md#appstorage)阅读。最佳实践请参考[状态管理最佳实践](../best-practices/bpta-status-management.md)。

说明

多组件间状态共享和同步、状态管理和UI解耦，可以参考解决方案[基于StateStore的全局状态管理开发实践](../best-practices/bpta-global-state-management-state-store.md)。

不涉及UI组件同步的数据处理工作，建议[通过用户首选项实现数据持久化](data-persistence-by-preferences.md)。

## 概述

AppStorage是在应用启动时创建的单例，用于提供应用状态数据的中心存储。这些状态数据在应用级别可访问。AppStorage在应用运行过程中保留其属性。

AppStorage中的属性通过唯一的字符串类型属性名（key）访问，支持与UI组件同步，并可在应用业务逻辑中被访问。其支持应用的[主线程](thread-model-stage.md)内多个[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例间的UI状态数据共享。

AppStorage中的属性可以被双向同步，并具有不同的功能，比如数据持久化（详见[PersistentStorage](arkts-persiststorage.md)）。这些UI状态是通过业务逻辑实现，与UI解耦，如果希望这些UI状态在UI中使用，需要用到[@StorageProp](arkts-appstorage.md#storageprop)和[@StorageLink](arkts-appstorage.md#storagelink)。

## @StorageProp

@StorageProp与AppStorage中对应的属性建立单向数据同步。

说明

从API version 11开始，该装饰器支持在元服务中使用。

### 装饰器使用规则说明

| @StorageProp变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 常量字符串，必填（字符串需要有引号）。  **说明：**  使用null和undefined作为key时，会隐式转换为对应的字符串，不建议该用法。 |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum类型，以及这些类型的数组。  API Version 12及以上支持[Map](arkts-appstorage.md#装饰map类型变量)、[Set](arkts-appstorage.md#装饰set类型变量)、[Date](arkts-appstorage.md#装饰date类型变量)、undefined和null类型以及这些类型的联合类型，示例见[AppStorage支持联合类型](arkts-appstorage.md#appstorage支持联合类型)。  嵌套类型的场景请参考[观察变化和行为表现](arkts-appstorage.md#观察变化和行为表现)。  **说明：**  变量类型必须被指定，建议和AppStorage中对应属性类型相同，否则会发生类型隐式转换，从而导致应用行为异常。 |
| 不允许装饰的变量类型 | 不支持装饰Function类型。 |
| 同步类型 | 单向同步：从AppStorage的对应属性到组件的状态变量。  组件本地的修改是允许的，但是AppStorage中给定的属性一旦发生变化，将覆盖本地的修改。 |
| 被装饰变量的初始值 | 必须本地初始化，如果AppStorage实例中不存在属性，则用该初始值初始化该属性，并存入AppStorage中。 |

### 变量的传递/访问规则说明

| 传递/访问 | 说明 |
| --- | --- |
| 从父节点初始化和更新 | 禁止从父节点初始化和更新@StorageProp。仅支持使用AppStorage中对应key的属性进行初始化，如果不存在对应key，则使用本地默认值进行初始化。 |
| 初始化子节点 | 支持，可用于初始化[@State](arkts-state.md)、[@Link](arkts-link.md)、[@Prop](arkts-prop.md)、[@Provide](arkts-provide-and-consume.md)。 |
| 是否支持组件外访问 | 否。 |

**图1** @StorageProp初始化规则图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/n6u_e_dPSH2_3-duDNv63A/zh-cn_image_0000002558604446.png?HW-CC-KV=V1&HW-CC-Date=20260429T052715Z&HW-CC-Expire=86400&HW-CC-Sign=51C393C4D748D022EB9A133CBF64E21B24D576E099C9DB662D793DEF05B84D7E)

### 观察变化和行为表现

**观察变化**

* 当装饰的类型为boolean、string、number时，可以观察到数值的变化。
* 当装饰的数据类型为class或者Object时，可以观察到对象整体赋值和属性变化（详见[从UI内部使用AppStorage](arkts-appstorage.md#从ui内部使用appstorage)）。
* 当装饰的对象是数组时，可以观察到数组添加、删除、更新数组单元的变化。
* 当装饰的对象是Date时，可以观察到Date整体的赋值，以及通过调用Date的接口setFullYear、setMonth、setDate、setHours、setMinutes、setSeconds、setMilliseconds、setTime、setUTCFullYear、setUTCMonth、setUTCDate、setUTCHours、setUTCMinutes、setUTCSeconds、setUTCMilliseconds更新Date的属性。详见[装饰Date类型变量](arkts-appstorage.md#装饰date类型变量)。
* 当装饰的变量是Map时，可以观察到Map整体的赋值，以及通过调用Map的接口set、clear、delete更新Map的值。详见[装饰Map类型变量](arkts-appstorage.md#装饰map类型变量)。
* 当装饰的变量是Set时，可以观察到Set整体的赋值，以及通过调用Set的接口add、clear、delete更新Set的值。详见[装饰Set类型变量](arkts-appstorage.md#装饰set类型变量)。

**框架行为**

1. @StorageProp(key)装饰的数值发生变化，不会同步写回AppStorage对应的属性；变化会触发自定义组件重新渲染，并且该变动仅作用于当前组件的私有成员变量，其他绑定该key的数据不会同步改变。
2. 当AppStorage中对应key的属性发生改变时，所有@StorageProp(key)装饰的变量都会同步更新，本地的修改将被覆盖。

## @StorageLink

@StorageLink与AppStorage中对应的属性建立双向数据同步。

说明

从API version 11开始，该装饰器支持在元服务中使用。

### 装饰器使用规则说明

| @StorageLink变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | key：常量字符串，必填（字符串需要有引号）。  **注意：**  使用null和undefined作为key时，会隐式转换为对应的字符串，不建议该用法。 |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum类型，以及这些类型的数组。  API Version 12及以上支持Map、Set、Date、undefined和null类型以及这些类型的联合类型，示例见[AppStorage支持联合类型](arkts-appstorage.md#appstorage支持联合类型)。  嵌套类型的场景请参考[观察变化和行为表现](arkts-appstorage.md#观察变化和行为表现-1)。  **注意：**  变量类型必须被指定，建议和AppStorage中对应属性类型相同，否则会发生类型隐式转换，从而导致应用行为异常。 |
| 不允许装饰的变量类型 | 不支持装饰Function类型。 |
| 同步类型 | 双向同步：从AppStorage的对应属性到自定义组件，从自定义组件到AppStorage对应属性。 |
| 被装饰变量的初始值 | 必须本地初始化，如果AppStorage实例中不存在属性，则用该初始值初始化该属性，并存入AppStorage中。 |

### 变量的传递/访问规则说明

| 传递/访问 | 说明 |
| --- | --- |
| 从父节点初始化和更新 | 禁止。 |
| 初始化子节点 | 支持，可用于初始化常规变量、@State、@Link、@Prop、@Provide。 |
| 是否支持组件外访问 | 否。 |

**图2** @StorageLink初始化规则图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/XK9gNBcXQTu7MXUxrsosdw/zh-cn_image_0000002589323971.png?HW-CC-KV=V1&HW-CC-Date=20260429T052715Z&HW-CC-Expire=86400&HW-CC-Sign=94A09092C9DDEF0CDF2CC2A5385DD2CFCAE4AD4A5804A0F63F9E811F29CDE934)

### 观察变化和行为表现

**观察变化**

* 装饰的数据类型为boolean、string、number时，可以观察到数值变化。
* 装饰的数据类型为class或Object时，可以观察到对象整体赋值和属性变化。（详见[从UI内部使用AppStorage](arkts-appstorage.md#从ui内部使用appstorage)）。
* 当装饰的对象是数组时，可以观察到数组添加、删除、更新数组单元的变化。详见[装饰Array类型变量](arkts-appstorage.md#装饰array类型变量)。
* 当装饰的对象是Date时，可以观察到Date整体的赋值，以及通过调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds 更新Date的属性。详见[装饰Date类型变量](arkts-appstorage.md#装饰date类型变量)。
* 当装饰的变量是Map时，可以观察到Map整体的赋值，以及通过调用Map的接口set、clear、delete更新Map的值。详见[装饰Map类型变量](arkts-appstorage.md#装饰map类型变量)。
* 当装饰的变量是Set时，可以观察到Set的整体赋值，以及通过调用Set的接口add、clear、delete更新Set的值。详见[装饰Set类型变量](arkts-appstorage.md#装饰set类型变量)。

**框架行为**

1. 当@StorageLink(key)装饰的数值发生变化时，修改将被同步回AppStorage对应key的属性中。
2. AppStorage中key对应的数据一旦改变，其绑定的所有的数据（包括双向@StorageLink和单向@StorageProp）都将被同步修改。
3. @StorageLink(key)装饰的数据是状态变量，其变化不仅会同步到AppStorage，还会触发自定义组件的重新渲染。

## 限制条件

1. @StorageProp/@StorageLink的参数必须为string类型，否则编译期会报错。

   ```
   1. AppStorage.setOrCreate('propA', 47);

   3. // 错误写法，编译报错
   4. @StorageProp() storageProp: number = 1;
   5. @StorageLink() storageLink: number = 2;

   7. // 正确写法
   8. @StorageProp('propA') storageProp: number = 1;
   9. @StorageLink('propA') storageLink: number = 2;
   ```
2. @StorageProp与@StorageLink不支持装饰Function类型的变量，API version 23之前，框架会抛出运行时错误。

   从API version 23开始，添加对@StorageProp与@StorageLink装饰Function类型变量的校验，编译期会报错。
3. AppStorage与[PersistentStorage](arkts-persiststorage.md)以及[Environment](arkts-environment.md)配合使用时，需要注意以下几点：

   (1) 在AppStorage中创建属性后，调用PersistentStorage.[persistProp](../harmonyos-references/ts-state-management.md#persistprop10)接口时，会使用AppStorage中已存在的值，并覆盖PersistentStorage中的同名属性。因此，建议使用相反的调用顺序。反例可见[在PersistentStorage之前访问AppStorage中的属性](arkts-persiststorage.md#在persistentstorage之前访问appstorage中的属性)。

   (2) 如果在AppStorage中已创建属性，再调用Environment.[envProp](../harmonyos-references/ts-state-management.md#envprop10)创建同名属性，会调用失败。因为AppStorage已有同名属性，Environment环境变量不会再写入AppStorage中，所以建议不要在AppStorage中使用Environment预置环境变量名。

   ```
   1. AppStorage.setOrCreate('languageCode', 'en');
   2. // result结果为false
   3. let result = Environment.envProp('languageCode','en');
   ```
4. 状态装饰器装饰的变量，改变会引起UI的渲染更新。如果改变的变量仅用于消息传递，不用于UI更新，推荐使用[emitter](../harmonyos-references/js-apis-emitter.md)方式。具体示例可见[不建议借助@StorageLink的双向同步机制实现事件通知](arkts-appstorage.md#不建议借助storagelink的双向同步机制实现事件通知)。
5. AppStorage同一进程内共享，UIAbility和UIExtensionAbility是两个进程，所以在UIExtensionAbility中不共享主进程的AppStorage。

## 使用场景

### 从应用逻辑使用AppStorage和LocalStorage

AppStorage是单例，其所有API均为静态方法，使用方法类似于[LocalStorage](arkts-localstorage.md)中对应的非静态方法。

```
1. AppStorage.setOrCreate('propA', 47);

3. let storage: LocalStorage = new LocalStorage();
4. storage.setOrCreate('propA',17);
5. let propA: number | undefined = AppStorage.get('propA'); // propA in AppStorage == 47, propA in LocalStorage == 17
6. let link1: SubscribedAbstractProperty<number> = AppStorage.link('propA'); // link1.get() == 47
7. let link2: SubscribedAbstractProperty<number> = AppStorage.link('propA'); // link2.get() == 47
8. let prop: SubscribedAbstractProperty<number> = AppStorage.prop('propA'); // prop.get() == 47

10. link1.set(48); // 双向同步: link1.get() == link2.get() == prop.get() == 48
11. prop.set(1); // 单向同步: prop.get() == 1; 但 link1.get() == link2.get() == 48
12. link1.set(49); // 双向同步: link1.get() == link2.get() == prop.get() == 49

14. storage.get<number>('propA') // == 17
15. storage.set('propA', 101);
16. storage.get<number>('propA') // == 101

18. AppStorage.get<number>('propA') // == 49
19. link1.get() // == 49
20. link2.get() // == 49
21. prop.get() // == 49
```

### 从UI内部使用AppStorage

@StorageLink与AppStorage配合使用，通过AppStorage中的属性创建双向数据同步。

@StorageProp与AppStorage配合使用，通过AppStorage中的属性创建单向数据同步。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG: string = '[SampleAppStorage]';

6. class Data {
7. public code: number;

9. constructor(code: number) {
10. this.code = code;
11. }
12. }

14. AppStorage.setOrCreate('propA', 47);
15. AppStorage.setOrCreate('propB', new Data(50));
16. let storage = new LocalStorage();
17. storage.setOrCreate('linkA', 48);
18. storage.setOrCreate('linkB', new Data(100));

20. @Entry(storage)
21. @Component
22. struct TestStorageProp {
23. @StorageLink('propA') storageLink: number = 1;
24. @StorageProp('propA') storageProp: number = 1;
25. @StorageLink('propB') storageLinkObject: Data = new Data(1);
26. @StorageProp('propB') storagePropObject: Data = new Data(1);

28. build() {
29. Column({ space: 20 }) {
30. // @StorageLink与AppStorage建立双向联系，更改数据会同步回AppStorage中key为'propA'的值
31. Text(`storageLink ${this.storageLink}`)
32. .onClick(() => {
33. this.storageLink += 1;
34. })

36. // @StorageProp与AppStorage建立单向联系，更改数据不会同步回AppStorage中key为'propA'的值
37. // 但能被AppStorage的set/setorCreate更新值
38. Text(`storageProp ${this.storageProp}`)
39. .onClick(() => {
40. this.storageProp += 1;
41. })

43. // AppStorage的API虽然能获取值，但是不具有刷新UI的能力，日志能看到数值更改
44. // 依赖@StorageLink/@StorageProp才能建立起与自定义组件的联系，刷新UI
45. Text(`change by AppStorage: ${AppStorage.get<number>('propA')}`)
46. .onClick(() => {
47. hilog.info(DOMAIN, TAG, `Appstorage.get: ${AppStorage.get<number>('propA')}`);
48. AppStorage.set<number>('propA', 100);
49. })

51. Text(`storageLinkObject ${this.storageLinkObject.code}`)
52. .onClick(() => {
53. this.storageLinkObject.code += 1;
54. })

56. Text(`storagePropObject ${this.storagePropObject.code}`)
57. .onClick(() => {
58. this.storagePropObject.code += 1;
59. })
60. }
61. }
62. }
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageTwo.ets#L15-L79)

### AppStorage支持联合类型

在下面的示例中，变量linkA的类型为number | null，变量linkB的类型为number | undefined。[Text](arkts-common-components-text-display.md)组件初始化分别显示为null和undefined，点击切换为数字，再次点击切换回null和undefined。

```
1. @Component
2. struct StorageLinkComponent {
3. @StorageLink('linkA') linkA: number | null = null;
4. @StorageLink('linkB') linkB: number | undefined = undefined;

6. build() {
7. Column() {
8. Text('@StorageLink接口初始化，@StorageLink取值')
9. // linkA为null时，点击后会切换为1；linkA为1时，点击后会切换为null
10. Text(`${this.linkA}`).fontSize(20).onClick(() => {
11. this.linkA ? this.linkA = null : this.linkA = 1;
12. })
13. Text(`${this.linkB}`).fontSize(20).onClick(() => {
14. this.linkB ? this.linkB = undefined : this.linkB = 1;
15. })
16. }
17. .borderWidth(3).borderColor(Color.Red)
18. }
19. }

21. @Component
22. struct StoragePropComponent {
23. @StorageProp('propA') propA: number | null = null;
24. @StorageProp('propB') propB: number | undefined = undefined;

26. build() {
27. Column() {
28. Text('@StorageProp接口初始化，@StorageProp取值')
29. Text(`${this.propA}`).fontSize(20).onClick(() => {
30. this.propA ? this.propA = null : this.propA = 1;
31. })
32. Text(`${this.propB}`).fontSize(20).onClick(() => {
33. this.propB ? this.propB = undefined : this.propB = 1;
34. })
35. }
36. .borderWidth(3).borderColor(Color.Blue)
37. }
38. }

40. @Entry
41. @Component
42. struct TestPageStorageLink {
43. build() {
44. Row() {
45. Column() {
46. StorageLinkComponent()
47. StoragePropComponent()
48. }
49. .width('100%')
50. }
51. .height('100%')
52. }
53. }
```

[PageThree.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageThree.ets#L15-L69)

### 装饰Array类型变量

在下面的示例中，@StorageLink装饰的message类型为number[]，点击Button改变message的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct ArraySample {
4. @StorageLink('array') message: number[] = [0, 1, 2, 3];

6. build() {
7. Column() {
8. ForEach(this.message, (item: number) => {
9. Text(`${item}`)
10. .fontSize(20)
11. .margin(10)
12. })
13. // 新增数组元素，触发UI刷新
14. Button('Push element')
15. .onClick(() => {
16. this.message.push(4);
17. })
18. .width(300)
19. .margin(10)
20. // 删除数组元素，触发UI刷新
21. Button('Pop element')
22. .onClick(() => {
23. this.message.pop();
24. })
25. .width(300)
26. .margin(10)
27. // 对数组整体重新赋值，触发UI刷新
28. Button('Reset array')
29. .onClick(() => {
30. this.message = [9, 8, 7, 6];
31. })
32. .width(300)
33. .margin(10)
34. // 更新数组元素，触发UI刷新
35. Button('Modify element[0]')
36. .onClick(() => {
37. this.message[0] = 10;
38. })
39. .width(300)
40. .margin(10)
41. }
42. }
43. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageOne.ets#L15-L163)

### 装饰Date类型变量

说明

从API version 12开始，AppStorage支持Date类型。

在下面的示例中，@StorageLink装饰的selectedDate类型为Date。点击Button改变selectedDate的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct DateSample {
4. @StorageLink('date') selectedDate: Date = new Date('2021-08-08');

6. build() {
7. Column() {
8. Button('set selectedDate to 2023-07-08')
9. .margin(10)
10. .onClick(() => {
11. AppStorage.setOrCreate('date', new Date('2023-07-08'));
12. })
13. // 点击Button更新selectedDate年份数据，触发视图刷新
14. Button('increase the year by 1')
15. .margin(10)
16. .onClick(() => {
17. this.selectedDate.setFullYear(this.selectedDate.getFullYear() + 1);
18. })
19. Button('increase the month by 1')
20. .margin(10)
21. .onClick(() => {
22. this.selectedDate.setMonth(this.selectedDate.getMonth() + 1);
23. })
24. Button('increase the day by 1')
25. .margin(10)
26. .onClick(() => {
27. this.selectedDate.setDate(this.selectedDate.getDate() + 1);
28. })
29. DatePicker({
30. start: new Date('1970-1-1'),
31. end: new Date('2100-1-1'),
32. selected: $$this.selectedDate
33. })
34. }.width('100%')
35. }
36. }
```

[PageFour.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageFour.ets#L15-L52)

### 装饰Map类型变量

说明

从API version 12开始，AppStorage支持Map类型。

在下面的示例中，@StorageLink装饰的message类型为Map<number, string>，点击Button改变message的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct MapSample {
4. @StorageLink('map') message: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);

6. build() {
7. Row() {
8. Column() {
9. ForEach(Array.from(this.message.entries()), (item: [number, string]) => {
10. Text(`${item[0]}`).fontSize(30)
11. Text(`${item[1]}`).fontSize(30)
12. Divider()
13. })
14. // 点击Button初始化message
15. Button('init map').onClick(() => {
16. this.message = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
17. })
18. Button('set new one').onClick(() => {
19. this.message.set(4, 'd');
20. })
21. Button('clear').onClick(() => {
22. this.message.clear();
23. })
24. Button('replace the existing one').onClick(() => {
25. this.message.set(0, 'aa');
26. })
27. Button('delete the existing one').onClick(() => {
28. AppStorage.get<Map<number, string>>('map')?.delete(0);
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

[PageFive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageFive.ets#L15-L51)

### 装饰Set类型变量

说明

从API version 12开始，AppStorage支持Set类型。

在下面的示例中，@StorageLink装饰的memberSet类型为Set<number>，点击Button改变memberSet的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct SetSample {
4. @StorageLink('set') memberSet: Set<number> = new Set([0, 1, 2, 3, 4]);

6. build() {
7. Row() {
8. Column() {
9. ForEach(Array.from(this.memberSet.entries()), (item: [number, number]) => {
10. Text(`${item[0]}`)
11. .fontSize(30)
12. Divider()
13. })
14. // 点击Button初始化memberSet
15. Button('init set')
16. .onClick(() => {
17. this.memberSet = new Set([0, 1, 2, 3, 4]);
18. })
19. Button('set new one')
20. .onClick(() => {
21. AppStorage.get<Set<number>>('set')?.add(5);
22. })
23. Button('clear')
24. .onClick(() => {
25. this.memberSet.clear();
26. })
27. Button('delete the first one')
28. .onClick(() => {
29. this.memberSet.delete(0);
30. })
31. }
32. .width('100%')
33. }
34. .height('100%')
35. }
36. }
```

[PageSix.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageSix.ets#L15-L52)

### AppStorage在多页面中共享使用

在下面示例中，Index和Page页面通过同一个全局AppStorage对象共享linkA数据。在一处修改其值，另一处也能获取到更新后的值。

```
1. AppStorage.setOrCreate('linkA', 47)
2. AppStorage.setOrCreate('propB', 48)

4. @Entry
5. @Component
6. struct Index {
7. @StorageLink('linkA') linkA: number = 1; // 与AppStorage进行双向数据同步
8. @StorageProp('propB') propB: number = 1; // 与AppStorage进行单向数据同步
9. pageStack: NavPathStack = new NavPathStack();

11. build() {
12. Navigation(this.pageStack) {
13. Row() {
14. Column({ space: 5 }) {
15. Text(`${this.linkA}`)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. Text(`${this.propB}`)
19. .fontSize(50)
20. .fontWeight(FontWeight.Bold)
21. Button('Change linkA')
22. .onClick(() => {
23. // 刷新UI，修改将会被同步回AppStorage
24. this.linkA++;
25. })
26. Button('Change propB')
27. .onClick(() => {
28. // 刷新UI，修改不会被同步回AppStorage
29. this.propB++;
30. })
31. Button('To Page')
32. .onClick(() => {
33. this.pageStack.pushPathByName('Page', null);
34. })
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
41. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/Index.ets#L16-L59)

```
1. @Builder
2. export function PageBuilder() {
3. Page()
4. }

6. // 应用全局共享一个AppStorage
7. @Component
8. struct Page {
9. @StorageLink('linkA') linkA: number = 2; // 与AppStorage进行双向数据同步
10. @StorageProp('propB') propB: number = 2; // 与AppStorage进行单向数据同步
11. pageStack: NavPathStack = new NavPathStack();

13. build() {
14. NavDestination() {
15. Row() {
16. Column({ space: 5 }) {
17. Text(`${this.linkA}`)
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. Text(`${this.propB}`)
21. .fontSize(50)
22. .fontWeight(FontWeight.Bold)
23. Button('Change linkA')
24. .onClick(() => {
25. // 刷新UI，修改将会被同步回AppStorage
26. this.linkA++;
27. })
28. Button('Change propB')
29. .onClick(() => {
30. // 刷新UI，修改不会被同步回AppStorage
31. this.propB++;
32. })
33. Button('Back Index')
34. .onClick(() => {
35. this.pageStack.pop();
36. })
37. }
38. .width('100%')
39. }
40. }
41. .onReady((context: NavDestinationContext) => {
42. this.pageStack = context.pathStack;
43. })
44. }
45. }
```

[Page.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/Page.ets#L16-L63)

使用Navigation时，需要手动添加系统路由表文件src/main/resources/base/profile/router\_map.json，并在module.json5中添加:"routerMap": "$profile:router\_map"。

```
1. {
2. "routerMap": [
3. {
4. "name": "Page",
5. "pageSourceFile": "src/main/ets/pages/Page.ets",
6. "buildFunction": "PageBuilder",
7. "data": {
8. "description": "AppStorage example"
9. }
10. }
11. ]
12. }
```

## AppStorage使用建议

### 不建议借助@StorageLink的双向同步机制实现事件通知

不建议使用@StorageLink和AppStorage的双向同步机制来实现事件通知。AppStorage中的变量可能绑定在多个页面的组件中，但事件通知不一定需要通知到所有这些组件。此外，当这些@StorageLink装饰的变量在UI中使用时，会触发UI刷新，造成不必要的性能影响。

示例代码中，TapImage中的点击事件会触发AppStorage中tapIndex对应属性的改变。由于@StorageLink是双向同步的，修改会同步回AppStorage中，因此所有绑定AppStorage的tapIndex自定义组件都能感知到tapIndex的变化。使用[@Watch](arkts-watch.md)监听到tapIndex的变化后，修改状态变量tapColor，从而触发UI刷新（此处tapIndex未直接绑定在UI上，因此tapIndex的变化不会直接触发UI刷新）。

使用该机制实现事件通知时，应确保AppStorage中的变量不直接被绑定到UI上，同时控制@Watch函数的复杂度。如果@Watch函数执行时间过长，会影响UI刷新效率。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG: string = '[SampleAppStorage]';

6. class ViewData {
7. public title: string;
8. public uri: Resource;
9. public color: Color = Color.Black;

11. constructor(title: string, uri: Resource) {
12. this.title = title;
13. this.uri = uri;
14. }
15. }

17. @Entry
18. @Component
19. struct Gallery {
20. // 请将$r('app.media.startIcon')替换为实际资源文件
21. dataList: Array<ViewData> =
22. [new ViewData('flower', $r('app.media.startIcon')), new ViewData('OMG', $r('app.media.startIcon')),
23. new ViewData('OMG', $r('app.media.startIcon'))];
24. scroller: Scroller = new Scroller();

26. build() {
27. Column() {
28. Grid(this.scroller) {
29. ForEach(this.dataList, (item: ViewData, index?: number) => {
30. GridItem() {
31. TapImage({
32. uri: item.uri,
33. index: index
34. })
35. }.aspectRatio(1)

37. }, (item: ViewData, index?: number) => {
38. return JSON.stringify(item) + index;
39. })
40. }.columnsTemplate('1fr 1fr')
41. }

43. }
44. }

46. @Component
47. export struct TapImage {
48. @StorageLink('tapIndex') @Watch('onTapIndexChange') tapIndex: number = -1;
49. @State tapColor: Color = Color.Black;
50. index: number = 0;
51. uri: Resource = {
52. id: 0,
53. type: 0,
54. moduleName: '',
55. bundleName: ''
56. };

58. // 判断是否被选中
59. onTapIndexChange() {
60. if (this.tapIndex >= 0 && this.index === this.tapIndex) {
61. hilog.info(DOMAIN, TAG, `tapindex: ${this.tapIndex}, index: ${this.index}, red`);
62. this.tapColor = Color.Red;
63. } else {
64. hilog.info(DOMAIN, TAG, `tapindex: ${this.tapIndex}, index: ${this.index}, black`);
65. this.tapColor = Color.Black;
66. }
67. }

69. build() {
70. Column() {
71. Image(this.uri)
72. .objectFit(ImageFit.Cover)
73. .onClick(() => {
74. this.tapIndex = this.index;
75. })
76. .border({ width: 5, style: BorderStyle.Dotted, color: this.tapColor })
77. }

79. }
80. }
```

[ViewData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/ViewData.ets#L15-L97)

相比借助@StorageLink的双向同步机制实现事件通知，开发者可以使用[emit](../harmonyos-references/js-apis-emitter.md#emitteremit)订阅某个事件并接收事件回调的方式来减少开销，增强代码的可读性。

说明

emit接口不支持在Previewer预览器中使用。

```
1. import { emitter } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0001;
5. const TAG: string = '[SampleAppStorage]';

7. let nextId: number = 0;

9. class ViewData {
10. public title: string;
11. public uri: Resource;
12. public color: Color = Color.Black;
13. public id: number;

15. constructor(title: string, uri: Resource) {
16. this.title = title;
17. this.uri = uri;
18. this.id = nextId++;
19. }
20. }

22. @Entry
23. @Component
24. struct Gallery {
25. // 请将$r('app.media.startIcon')替换为实际资源文件
26. dataList: Array<ViewData> =
27. [new ViewData('flower', $r('app.media.startIcon')), new ViewData('OMG', $r('app.media.startIcon')),
28. new ViewData('OMG', $r('app.media.startIcon'))];
29. scroller: Scroller = new Scroller();
30. private preIndex: number = -1;

32. build() {
33. Column() {
34. Grid(this.scroller) {
35. ForEach(this.dataList, (item: ViewData) => {
36. GridItem() {
37. TapImage({
38. uri: item.uri,
39. index: item.id
40. })
41. }.aspectRatio(1)
42. .onClick(() => {
43. if (this.preIndex === item.id) {
44. return;
45. }
46. let innerEvent: emitter.InnerEvent = { eventId: item.id };
47. // 选中态：黑变红
48. let eventData: emitter.EventData = {
49. data: {
50. 'colorTag': 1
51. }
52. };
53. emitter.emit(innerEvent, eventData);

55. if (this.preIndex != -1) {
56. hilog.info(DOMAIN, TAG, `preIndex: ${this.preIndex}, index: ${item.id}, black`);
57. let innerEvent: emitter.InnerEvent = { eventId: this.preIndex };
58. // 取消选中态：红变黑
59. let eventData: emitter.EventData = {
60. data: {
61. 'colorTag': 0
62. }
63. };
64. emitter.emit(innerEvent, eventData);
65. }
66. this.preIndex = item.id;
67. })
68. }, (item: ViewData) => JSON.stringify(item))
69. }.columnsTemplate('1fr 1fr')
70. }

72. }
73. }

75. @Component
76. export struct TapImage {
77. @State tapColor: Color = Color.Black;
78. index: number = 0;
79. uri: Resource = {
80. id: 0,
81. type: 0,
82. moduleName: '',
83. bundleName: ''
84. };

86. onTapIndexChange(colorTag: emitter.EventData) {
87. if (colorTag.data != null) {
88. this.tapColor = colorTag.data.colorTag ? Color.Red : Color.Black;
89. }
90. }

92. aboutToAppear() {
93. // 定义事件ID
94. let innerEvent: emitter.InnerEvent = { eventId: this.index };
95. emitter.on(innerEvent, data => {
96. this.onTapIndexChange(data);
97. });
98. }

100. build() {
101. Column() {
102. Image(this.uri)
103. .objectFit(ImageFit.Cover)
104. .border({ width: 5, style: BorderStyle.Dotted, color: this.tapColor })
105. }
106. }
107. }
```

[PageEight.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageEight.ets#L15-L124)

以上通知事件逻辑简单，也可以简化成三元表达式。

```
1. class ViewData {
2. public title: string;
3. public uri: Resource;
4. public color: Color = Color.Black;

6. constructor(title: string, uri: Resource) {
7. this.title = title;
8. this.uri = uri;
9. }
10. }

12. @Entry
13. @Component
14. struct Gallery {
15. // 请将$r('app.media.startIcon')替换为实际资源文件
16. dataList: Array<ViewData> =
17. [new ViewData('flower', $r('app.media.startIcon')), new ViewData('OMG', $r('app.media.startIcon')),
18. new ViewData('OMG', $r('app.media.startIcon'))];
19. scroller: Scroller = new Scroller();

21. build() {
22. Column() {
23. Grid(this.scroller) {
24. ForEach(this.dataList, (item: ViewData, index?: number) => {
25. GridItem() {
26. TapImage({
27. uri: item.uri,
28. index: index
29. })
30. }.aspectRatio(1)

32. }, (item: ViewData, index?: number) => {
33. return JSON.stringify(item) + index;
34. })
35. }.columnsTemplate('1fr 1fr')
36. }

38. }
39. }

41. @Component
42. export struct TapImage {
43. @StorageLink('tapIndex') tapIndex: number = -1;
44. index: number = 0;
45. uri: Resource = {
46. id: 0,
47. type: 0,
48. moduleName: '',
49. bundleName: ''
50. };

52. build() {
53. Column() {
54. Image(this.uri)
55. .objectFit(ImageFit.Cover)
56. .onClick(() => {
57. this.tapIndex = this.index;
58. })
59. .border({
60. width: 5,
61. style: BorderStyle.Dotted,
62. color: (this.tapIndex >= 0 && this.index === this.tapIndex) ? Color.Red : Color.Black
63. })
64. }
65. }
66. }
```

[Gallery.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/Gallery.ets#L15-L84)

### @StorageProp和AppStorage接口配合使用时，需要注意更新规则

使用setOrCreate/set接口更新key的值时，如果值相同，setOrCreate不会通知@StorageLink/@StorageProp更新，但因为@StorageProp本身有数据副本，更改值不会同步给AppStorage，这会导致开发者误认已通过AppStorage改了值，但实际上未通知@StorageProp更新值的情况。示例如下。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG: string = '[SampleAppStorage]';
5. AppStorage.setOrCreate('propA', false);

7. @Entry
8. @Component
9. struct PageStorageProp {
10. @StorageProp('propA') @Watch('onChange') propA: boolean = false;

12. onChange() {
13. hilog.info(DOMAIN, TAG, `propA change`);
14. }

16. aboutToAppear(): void {
17. this.propA = true;
18. }

20. build() {
21. Column() {
22. Text(`${this.propA}`)
23. Button('change')
24. .onClick(() => {
25. AppStorage.setOrCreate('propA', false);
26. // 输出当前this.propA的值
27. hilog.info(DOMAIN, TAG, `propA: ${this.propA}`);
28. })
29. }
30. }
31. }
```

[PageTen.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorage/entry/src/main/ets/pages/PageTen.ets#L15-L47)

上述示例，在点击事件之前，propA的值已经在本地被更改为true，而AppStorage中存的值仍为false。当点击事件通过setOrCreate接口尝试更新propA的值为false时，由于AppStorage中的值为false，两者相等，不会触发更新同步，因此@StorageProp的值仍为true。

实现二者同步有以下两种方式：

1. 将@StorageProp更改为@StorageLink。
2. 本地更改值的方式变为使用AppStorage.setOrCreate('propA', true)的方式。
