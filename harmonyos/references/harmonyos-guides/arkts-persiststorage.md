---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-persiststorage
title: PersistentStorage：持久化存储UI状态
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理应用拥有的状态 > PersistentStorage：持久化存储UI状态
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:16+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:4ab83467d81e9b8724ed5b33b8d4a1e0f17a3b4a5e9096e1fb2cedeb397b8e2b
---

PersistentStorage是应用程序中的可选单例对象。此对象的作用是持久化存储选定的AppStorage属性，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。

PersistentStorage提供状态变量持久化的能力，但是需要注意，其持久化和读回UI的能力都需要依赖AppStorage。在阅读本文档前，建议提前阅读：[AppStorage](arkts-appstorage.md)，[PersistentStorage API文档](../harmonyos-references/ts-state-management.md#persistentstorage)。

## 概述

PersistentStorage将选定的AppStorage属性保留在设备磁盘上。应用程序通过API，以决定哪些属性应借助PersistentStorage持久化。PersistentStorage和AppStorage中的属性建立了双向同步，UI和业务逻辑不直接访问PersistentStorage中的属性，所有属性访问都是对AppStorage的访问，AppStorage中的更改会自动同步到PersistentStorage。

PersistentStorage的存储路径为module级别，即哪个module调用了PersistentStorage，数据副本存入对应module的持久化文件中。如果多个module使用相同的key，则数据归属到最先使用PersistentStorage的module里。

PersistentStorage的存储路径在应用第一个ability启动时就已确定，为该ability所属的module。如果一个ability调用了PersistentStorage，并且该ability能被不同的module拉起，那么ability存在多少种启动方式，就会有多少份数据副本。

PersistentStorage功能上耦合了AppStorage，并且数据在不同module中使用也会有问题，因此推荐开发者使用[PersistenceV2](arkts-new-persistencev2.md)的globalConnect接口替换掉PersistentStorage的persistProp接口。PersistentStorage向PersistenceV2迁移的方案见[PersistentStorage->PersistenceV2](arkts-v1-v2-migration-application.md#persistentstorage-persistencev2)。

## 限制条件

PersistentStorage允许的类型和值有：

* number，string，boolean，enum 等简单类型。
* 可以被JSON.stringify()和JSON.parse()重构的对象（但是对象中的成员方法不支持持久化）。
* API version 12及以上支持Map类型，可以观察到Map整体的赋值，同时可通过调用Map的接口set、clear、delete 更新Map的值，且更新的值被持久化存储。详见[持久化Map类型变量](arkts-persiststorage.md#持久化map类型变量)。
* API version 12及以上支持Set类型，可以观察到Set整体的赋值，同时可通过调用Set的接口add、clear、delete 更新Set的值，且更新的值被持久化存储。详见[持久化Set类型变量](arkts-persiststorage.md#持久化set类型变量)。
* API version 12及以上支持Date类型，可以观察到Date整体的赋值，同时可通过调用Date的接口setFullYear、setMonth、setDate、setHours、setMinutes、setSeconds、setMilliseconds、setTime、setUTCFullYear、setUTCMonth、setUTCDate、setUTCHours、setUTCMinutes、setUTCSeconds、setUTCMilliseconds 更新Date的属性，且更新的值被持久化存储。详见[持久化Date类型变量](arkts-persiststorage.md#持久化date类型变量)。
* API version 12及以上支持undefined 和 null。
* API version 12及以上[支持联合类型](arkts-persiststorage.md#持久化联合类型变量)。

PersistentStorage不允许的类型和值有：

* 嵌套对象（对象数组，对象的属性是对象等）。因为目前框架无法检测AppStorage中嵌套对象（包括数组）值的变化，所以无法写回到PersistentStorage中。

持久化数据是一个相对缓慢的操作，应用程序应避免以下情况：

* 持久化大型数据集。
* 持久化经常变化的变量。

PersistentStorage的持久化变量最好是小于2kb的数据，不要大量的数据持久化，因为PersistentStorage写入磁盘是在UI线程同步执行的，大量数据本地读写会影响UI渲染性能。如果开发者需要存储大量的数据，建议使用[@ohos.data.relationalStore (关系型数据库)](../harmonyos-references/arkts-apis-data-relationalstore.md)相关接口。

PersistentStorage和UI实例相关联，持久化操作需要在UI实例初始化成功后（即[loadContent](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)传入的回调被调用时）才可以被调用，早于该时机调用会导致持久化失败。

```
1. // EntryAbility.ets
2. onWindowStageCreate(windowStage: window.WindowStage): void {
3. windowStage.loadContent('pages/PageOneMessageStorage', (err) => {
4. if (err.code) {
5. return;
6. }
7. PersistentStorage.persistProp('aProp', 47);
8. });
9. }
```

## 使用场景

### 从AppStorage中访问PersistentStorage初始化的属性

1. 初始化PersistentStorage：

   ```
   1. PersistentStorage.persistProp('aProp', 47);
   ```
2. 在AppStorage获取对应属性：

   ```
   1. AppStorage.get<number>('aProp'); // returns 47
   ```

   或在组件内部定义：

   ```
   1. @StorageLink('aProp') aProp: number = 48;
   ```

   完整代码如下：

   ```
   1. PersistentStorage.persistProp('aProp', 47);

   3. @Entry
   4. @Component
   5. struct TestPageOne {
   6. @State message: string = 'Hello World';
   7. @StorageLink('aProp') aProp: number = 48;

   9. build() {
   10. Row() {
   11. Column() {
   12. Text(this.message)
   13. // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
   14. // 未修改时默认值为47
   15. Text(`${this.aProp}`)
   16. .onClick(() => {
   17. this.aProp += 1;
   18. })
   19. }
   20. }
   21. }
   22. }
   ```

   [PageOneMessageStorage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/PersistentStorage/entry/src/main/ets/pages/PageOneMessageStorage.ets#L15-L39)

* 新应用安装后首次启动运行：

  1. 调用persistProp初始化PersistentStorage，首先查询在PersistentStorage本地文件中是否存在“aProp”，查询结果为不存在，因为应用是第一次安装。
  2. 接着查询属性“aProp”在AppStorage中是否存在，依旧不存在。
  3. 在AppStorage中创建名为“aProp”的number类型属性，属性初始值是定义的默认值47。
  4. PersistentStorage将属性“aProp”和值47写入磁盘，AppStorage中“aProp”对应的值和其后续的更改将被持久化。
  5. 在TestPageOne组件中创建状态变量@StorageLink('aProp') aProp，和AppStorage中“aProp”双向绑定，在创建的过程中会在AppStorage中查找，成功找到“aProp”，所以使用其在AppStorage找到的值47。

  **图1** PersistProp初始化流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/AfGy7U7-QgmC0CFzsE9yGQ/zh-cn_image_0000002589243911.png?HW-CC-KV=V1&HW-CC-Date=20260429T052715Z&HW-CC-Expire=86400&HW-CC-Sign=E796E3EB098FBD3D030E2FD0AB65445E4A81D6D5BF8276BA64F86A95DF14CB71)
* 触发点击事件后：

  1. 状态变量@StorageLink('aProp') aProp改变，触发Text组件重新刷新。
  2. @StorageLink装饰的变量是和AppStorage中建立双向同步的，所以@StorageLink('aProp') aProp的变化会被同步回AppStorage中。
  3. AppStorage中“aProp”属性的改变会同步到所有绑定该“aProp”的单向或者双向变量，在本示例中没有其他的绑定“aProp”的变量。
  4. 因为“aProp”对应的属性已经被持久化，所以在AppStorage中“aProp”的改变会触发PersistentStorage，将新的改变写入本地磁盘。
* 后续启动应用：

  1. 执行PersistentStorage.persistProp('aProp', 47)，首先在PersistentStorage本地文件查询“aProp”属性，成功查询到。
  2. 将在PersistentStorage查询到的值写入AppStorage中。
  3. 在TestPageOne组件里，@StorageLink绑定的“aProp”为PersistentStorage写入AppStorage中的值，即为上一次退出应用存入的值。

### 在PersistentStorage之前访问AppStorage中的属性

该示例为反例。在调用PersistentStorage.persistProp或者persistProps之前使用接口访问AppStorage中的属性是错误的，因为这样的调用顺序会丢失上一次应用程序运行中的属性值：

```
1. let aProp = AppStorage.setOrCreate('aProp', 47);
2. PersistentStorage.persistProp('aProp', 48);
```

应用在非首次运行时，先执行AppStorage.setOrCreate('aProp', 47)：属性“aProp”在AppStorage中创建，其类型为number，其值设置为指定的默认值47。“aProp”是持久化的属性，所以会被写回PersistentStorage磁盘中，PersistentStorage存储的上次退出应用的值被覆盖。

PersistentStorage.persistProp('aProp', 48)：在PersistentStorage中查找到“aProp”，值为刚刚使用AppStorage接口写入的47。

### 在PersistentStorage之后访问AppStorage中的属性

开发者可以先判断是否需要覆盖上一次保存在PersistentStorage中的值，如果需要覆盖，再调用AppStorage的接口进行修改，如果不需要覆盖，则不调用AppStorage的接口。

```
1. const MAX_NUM: number = 50;
```

[PageThreeAppStorage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/PersistentStorage/entry/src/main/ets/pages/PageThreeAppStorage.ets#L15-L18)

```
1. PersistentStorage.persistProp('aProp', 48);
2. if ((AppStorage.get<number>('aProp') ?? 0) > MAX_NUM) {
3. // 如果PersistentStorage存储的值超过50，设置为47
4. AppStorage.setOrCreate('aProp', 47);
5. }
```

[PageThreeAppStorage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/PersistentStorage/entry/src/main/ets/pages/PageThreeAppStorage.ets#L27-L33)

示例代码在读取PersistentStorage存储的数据后，判断“aProp”的值是否大于50，如果大于50，则使用AppStorage的接口将其设置为47。

### 持久化联合类型变量

PersistentStorage支持联合类型和undefined和null，在下面的示例中，使用persistProp方法初始化“P”为undefined。通过@StorageLink('P')绑定变量p，类型为number | undefined | null，点击Button改变P的值，视图会随之刷新。且P的值被持久化存储。

```
1. // 定义常量替代魔法值，明确数值含义
2. const DEFAULT_NUMBER: number = 10; // 默认数字值
3. const FONT_SIZE_LARGE: number = 50; // 大字体尺寸

5. // 初始化持久化属性，键名使用常量定义（若有多处使用可提取）
6. const STORAGE_KEY_P: string = 'P';
7. PersistentStorage.persistProp(STORAGE_KEY_P, undefined);

9. @Entry
10. @Component
11. struct TestCase6 {
12. // 使用常量作为默认值，类型明确
13. @StorageLink(STORAGE_KEY_P) p: number | undefined | null = DEFAULT_NUMBER;

15. build() {
16. Row() {
17. Column() {
18. Text(this.p + '')
19. .fontSize(FONT_SIZE_LARGE)
20. .fontWeight(FontWeight.Bold)
21. Button('changeToNumber').onClick(() => {
22. this.p = DEFAULT_NUMBER;
23. })
24. Button('changeTo undefined').onClick(() => {
25. this.p = undefined;
26. })
27. Button('changeTo null').onClick(() => {
28. this.p = null;
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

[PageFourMessageChange.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/PersistentStorage/entry/src/main/ets/pages/PageFourMessageChange.ets#L15-L52)

### 持久化Date类型变量

在下面的示例中，@StorageLink装饰的persistedDate类型为Date，点击Button改变persistedDate的值，视图会随之刷新。且persistedDate的值被持久化存储。

```
1. PersistentStorage.persistProp('persistedDate', new Date());

3. @Entry
4. @Component
5. struct PersistedDate {
6. @StorageLink('persistedDate') persistedDate: Date = new Date();

8. updateDate() {
9. this.persistedDate = new Date();
10. }

12. build() {
13. List() {
14. ListItem() {
15. Column() {
16. Text(`Persisted Date is ${this.persistedDate.toString()}`)
17. .margin(20)

19. Text(`Persisted Date year is ${this.persistedDate.getFullYear()}`)
20. .margin(20)

22. Text(`Persisted Date hours is ${this.persistedDate.getHours()}`)
23. .margin(20)

25. Text(`Persisted Date minutes is ${this.persistedDate.getMinutes()}`)
26. .margin(20)

28. Text(`Persisted Date time is ${this.persistedDate.toLocaleTimeString()}`)
29. .margin(20)

31. Button() {
32. Text('Update Date')
33. .fontSize(25)
34. .fontWeight(FontWeight.Bold)
35. .fontColor(Color.White)
36. }
37. .type(ButtonType.Capsule)
38. .margin({
39. top: 20
40. })
41. .backgroundColor('#0D9FFB')
42. .width('60%')
43. .height('5%')
44. .onClick(() => {
45. // 改变persistedDate的值，视图会随之刷新
46. this.updateDate();
47. })

49. }.width('100%')
50. }
51. }
52. }
53. }
```

[PageFivePersistedDate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/PersistentStorage/entry/src/main/ets/pages/PageFivePersistedDate.ets#L15-L69)

### 持久化Map类型变量

在下面的示例中，@StorageLink装饰的persistedMapString类型为Map<number, string>，点击Button改变persistedMapString的值，视图会随之刷新。且persistedMapString的值被持久化存储。

```
1. PersistentStorage.persistProp('persistedMapString', new Map<number, string>([]));

3. @Entry
4. @Component
5. struct PersistedMap {
6. @StorageLink('persistedMapString') persistedMapString: Map<number, string> = new Map<number, string>([]);

8. persistMapString() {
9. this.persistedMapString = new Map<number, string>([[3, 'one'], [6, 'two'], [9, 'three']]);
10. }

12. build() {
13. List() {
14. ListItem() {
15. Column() {
16. Text(`Persisted Map String is `)
17. .margin(20)
18. ForEach(Array.from(this.persistedMapString.entries()), (item: [number, string]) => {
19. Text(`${item[0]} ${item[1]}`)
20. })

22. Button() {
23. Text('Persist Map String')
24. .fontSize(20)
25. .fontWeight(FontWeight.Bold)
26. .fontColor(Color.White)
27. }
28. .type(ButtonType.Capsule)
29. .margin({
30. top: 20
31. })
32. .backgroundColor('#0D9FFB')
33. .width('60%')
34. .height('5%')
35. .onClick(() => {
36. // 点击Button改变persistedMapString的值，视图会随之刷新
37. this.persistMapString();
38. })

40. }.width('100%')
41. }
42. }
43. }
44. }
```

[PageSixPersistedMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/PersistentStorage/entry/src/main/ets/pages/PageSixPersistedMap.ets#L15-L60)

### 持久化Set类型变量

在下面的示例中，@StorageLink装饰的persistedSet类型为Set<number>，点击Button改变persistedSet的值，视图会随之刷新。且persistedSet的值被持久化存储。

```
1. PersistentStorage.persistProp('persistedSet', new Set<number>([]));

3. @Entry
4. @Component
5. struct PersistedSet {
6. @StorageLink('persistedSet') persistedSet: Set<number> = new Set<number>([]);

8. persistSet() {
9. this.persistedSet = new Set<number>([33, 1, 3]);
10. }

12. clearSet() {
13. this.persistedSet.clear();
14. }

16. build() {
17. List() {
18. ListItem() {
19. Column() {
20. Text(`Persisted Set is `)
21. .margin(20)
22. ForEach(Array.from(this.persistedSet.entries()), (item: [number, number]) => {
23. Text(`${item[1]}`)
24. })

26. Button() {
27. Text('Persist Set')
28. .fontSize(25)
29. .fontWeight(FontWeight.Bold)
30. .fontColor(Color.White)
31. }
32. .type(ButtonType.Capsule)
33. .margin({
34. top: 20
35. })
36. .backgroundColor('#0D9FFB')
37. .width('60%')
38. .height('5%')
39. .onClick(() => {
40. this.persistSet();
41. })

43. Button() {
44. Text('Persist Clear')
45. .fontSize(25)
46. .fontWeight(FontWeight.Bold)
47. .fontColor(Color.White)
48. }
49. .type(ButtonType.Capsule)
50. .margin({
51. top: 20
52. })
53. .backgroundColor('#0D9FFB')
54. .width('60%')
55. .height('5%')
56. .onClick(() => {
57. // 点击Button改变persistedSet的值，视图会随之刷新
58. this.clearSet();
59. })

61. }
62. .width('100%')
63. }
64. }
65. }
66. }
```

[PageSevenPersistedSet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/PersistentStorage/entry/src/main/ets/pages/PageSevenPersistedSet.ets#L15-L82)
