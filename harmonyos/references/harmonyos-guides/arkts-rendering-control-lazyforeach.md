---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach
title: LazyForEach：数据懒加载
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式渲染控制 > LazyForEach：数据懒加载
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:34+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:4240481beab2583b44bcc55d3e37136c9a4a054940b4fcc4765da457d6c24694
---

## 概述

从API version 7开始，LazyForEach为开发者提供了基于数据源渲染出一系列子组件的能力。具体而言，LazyForEach从数据源中按需迭代数据，并在每次迭代时创建相应组件。当LazyForEach用于滚动容器时，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。

本文档依次介绍了LazyForEach的[基础特性](arkts-rendering-control-lazyforeach.md#基础特性)、[高级特性](arkts-rendering-control-lazyforeach.md#高级特性)和[常见问题](arkts-rendering-control-lazyforeach.md#常见问题)，开发者可以按需阅读。在[首次渲染](arkts-rendering-control-lazyforeach.md#首次渲染)小节中，给出了简单的示例，可以帮助开发者快速上手LazyForEach的使用。

本文档对应的API接口说明参见[LazyForEach API参数说明](../harmonyos-references/ts-rendering-control-lazyforeach.md)。

说明

在大量子组件的场景下，LazyForEach与缓存列表项、动态预加载、组件复用等方法配合使用，可以进一步提升滑动帧率并降低应用内存占用。最佳实践请参考[长列表加载丢帧优化](../best-practices/bpta-best-practices-long-list.md)。

[Repeat](arkts-new-rendering-control-repeat.md)组件也提供了循环渲染能力。相较于LazyForEach，Repeat基于状态管理监听数据源变化，使用更加便利。同时，Repeat具有子组件复用能力，UI渲染效率更高。建议开发者优先使用Repeat。开发者也可参考[循环渲染迁移](arkts-v1-v2-migration-rendering-control-repeat.md)，将现有的LazyForEach组件迁移至Repeat组件。

## 使用限制

* LazyForEach必须在容器组件内使用，仅有[List](../harmonyos-references/ts-container-list.md)、[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[Swiper](../harmonyos-references/ts-container-swiper.md)以及[WaterFlow](../harmonyos-references/ts-container-waterflow.md)组件支持数据懒加载（可配置cachedCount属性，即只加载可视部分以及其前后少量数据用于缓冲），其他组件仍然是一次性加载所有的数据。支持数据懒加载的父组件根据自身及子组件的高度或宽度计算可视区域内需布局的子节点数量，高度或宽度的缺失会导致部分场景[懒加载失效](arkts-rendering-control-lazyforeach.md#子组件尺寸缺失导致懒加载失效)。
* LazyForEach依赖生成的键值判断是否刷新子组件，键值不变则不触发刷新。
* 容器组件内只能包含一个LazyForEach。以List为例，不建议同时包含[ListItem](../harmonyos-references/ts-container-listitem.md)、[ForEach](arkts-rendering-control-foreach.md)、LazyForEach，不建议同时包含多个LazyForEach。
* LazyForEach在每次迭代中，必须创建且只允许创建一个子组件；即LazyForEach的子组件生成函数有且只有一个根组件。
* 生成的子组件必须是允许包含在LazyForEach父容器组件中的子组件。
* 允许LazyForEach包含在[if/else](arkts-rendering-control-ifelse.md)条件渲染语句中，也允许LazyForEach中出现if/else条件渲染语句。
* 键值生成器必须针对每个数据生成唯一的值，如果键值相同，将导致键值相同的UI组件渲染出现问题。
* LazyForEach必须使用一个数据变化监听器DataChangeListener对象进行更新（具体参数使用参考[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)），重新赋值第一个参数dataSource会导致异常；dataSource使用状态变量时，状态变量改变不会触发LazyForEach的UI刷新。
* 为了高性能渲染，使用DataChangeListener对象的onDataChange方法更新UI时，需要生成不同于原来的键值来触发组件刷新。
* LazyForEach和[@Reusable装饰器](arkts-reusable.md)一起使用能触发节点复用。使用方法：将@Reusable装饰在LazyForEach列表的组件上，见[列表滚动配合LazyForEach使用](arkts-reusable.md#列表滚动配合lazyforeach使用)。
* LazyForEach和[@ReusableV2装饰器](arkts-new-reusablev2.md)一起使用能触发节点复用。详见@ReusableV2装饰器指南文档中的[在LazyForEach组件中使用](arkts-new-reusablev2.md#在lazyforeach组件中使用)。
* LazyForEach的子节点在离开可视区域和预加载区域时，不会立即被析构或回收，LazyForEach会在空闲时析构或回收这些节点。

## 基础特性

### 设置数据源

为了管理[DataChangeListener](../harmonyos-references/ts-rendering-control-lazyforeach.md#datachangelistener)监听器和通知LazyForEach更新数据，开发者需要使用如下方法：首先实现LazyForEach提供的[IDataSource](../harmonyos-references/ts-rendering-control-lazyforeach.md#idatasource)接口，将其作为LazyForEach的数据源，然后管理监听器和更新数据。

为实现基本的数据管理和监听能力，开发者需要实现IDataSource的[totalCount](../harmonyos-references/ts-rendering-control-lazyforeach.md#totalcount)、[getData](../harmonyos-references/ts-rendering-control-lazyforeach.md#getdata)、[registerDataChangeListener](../harmonyos-references/ts-rendering-control-lazyforeach.md#registerdatachangelistener)和[unregisterDataChangeListener](../harmonyos-references/ts-rendering-control-lazyforeach.md#unregisterdatachangelistener)方法，具体请参考[BasicDataSource示例代码](arkts-rendering-control-lazyforeach.md#basicdatasource示例代码)。当数据源变化时，通过调用监听器的接口通知LazyForEach更新，具体请参考[数据更新](arkts-rendering-control-lazyforeach.md#数据更新)。

### 键值生成规则

在LazyForEach循环渲染过程中，系统为每个item生成一个唯一且持久的键值，用于标识对应的组件。键值变化时，ArkUI框架将视为该数组元素已被替换或修改，并基于新的键值创建新的组件。

LazyForEach提供了参数keyGenerator，开发者可以使用该函数生成自定义键值。如果未定义keyGenerator函数，ArkUI框架将使用默认的键值生成函数：(item: Object, index: number) => { return viewId + '-' + index.toString(); }。viewId在编译器转换过程中生成，同一个LazyForEach组件内的viewId一致。

键值应满足以下条件。

1. 键值具有唯一性，每个数据项对应的键值互不相同。
2. 键值具有一致性，数据项不变时对应的键值也不变。

上述条件保证LazyForEach正确、高效地更新子组件，否则可能存在渲染结果异常、渲染效率降低等问题。

### 组件创建规则

在确定键值生成规则后，LazyForEach的第二个参数itemGenerator函数会根据组件创建规则为数据源的每个数组项创建组件。组件的创建包括两种情况：LazyForEach[首次渲染](arkts-rendering-control-lazyforeach.md#首次渲染)和LazyForEach非首次渲染的[数据更新](arkts-rendering-control-lazyforeach.md#数据更新)。

### 首次渲染

使用LazyForEach时，开发者需要提供数据源、键值生成函数和组件创建函数。**开发者需保证键值生成函数为每项数据生成不同的键值。**

在LazyForEach首次渲染时，会根据上述键值生成规则为数据源的每个数组项生成唯一键值并创建相应的组件。

对于预加载区域内的节点，若创建耗时较长，框架会分帧执行创建任务。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class InitialDataSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public pushData(data: string): void {
19. this.dataArray.push(data);
20. this.notifyDataAdd(this.dataArray.length - 1);
21. }
22. }

24. @Entry
25. @Component
26. struct InitialRendering {
27. private data: InitialDataSource = new InitialDataSource();

29. aboutToAppear() {
30. for (let i = 0; i <= 20; i++) {
31. this.data.pushData(`Hello ${i}`);
32. }
33. }

35. build() {
36. List({ space: 3 }) {
37. LazyForEach(this.data, (item: string) => {
38. ListItem() {
39. Row() {
40. Text(item).fontSize(50)
41. .onAppear(() => {
42. hilog.info(DOMAIN, TAG, `appear: ${item}`);
43. })
44. }.margin({ left: 10, right: 10 })
45. }
46. }, (item: string) => item)
47. }
48. .cachedCount(5)
49. }
50. }
```

[InitialRendering.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/InitialRendering.ets#L16-L67)

在上述代码中，keyGenerator函数的返回值是item。LazyForEach循环渲染时，为数据源数组项依次生成键值Hello 0、Hello 1 ... Hello 20，并创建对应的ListItem子组件渲染到界面上。

运行效果如下图所示。

**LazyForEach正常首次渲染**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/jXutxDTdTLWE6sntsqtEXg/zh-cn_image_0000002589324011.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=B189CB8D563D4A5B605F1446FCFA5C453637A2B5A0946D8BB1C4949973D278B1)

**错误案例：键值相同导致渲染异常**

当不同数据项生成的键值相同时，框架的行为是不可预测的。例如，在以下代码中，LazyForEach渲染的数据项键值均相同，在滑动过程中，LazyForEach会预加载划入划出当前页面的子组件，而新建的子组件和销毁的旧子组件具有相同的键值，框架可能取用错误的缓存，导致子组件渲染出现问题。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. // BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码。
2. import { BasicDataSource } from './BasicDataSource';

4. class MyDataSource extends BasicDataSource {
5. private dataArray: string[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): string {
12. return this.dataArray[index];
13. }

15. public pushData(data: string): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @Entry
22. @Component
23. struct MyComponent {
24. private data: MyDataSource = new MyDataSource();

26. aboutToAppear() {
27. for (let i = 0; i <= 20; i++) {
28. this.data.pushData(`Hello ${i}`);
29. }
30. }

32. build() {
33. List({ space: 3 }) {
34. LazyForEach(this.data, (item: string) => {
35. ListItem() {
36. Row() {
37. Text(item).fontSize(50)
38. .onAppear(() => {
39. console.info(`appear: ${item}`);
40. })
41. }.margin({ left: 10, right: 10 })
42. }
43. }, (item: string) => `same key`) // 自定义键值生成函数，返回相同键值
44. }.cachedCount(5)
45. }
46. }
```

运行效果如下图所示。

**LazyForEach存在相同键值**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/rZsF0WDSQfq-P1EIAY59zQ/zh-cn_image_0000002589243951.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=769A486BD5486F24EB549D810C64B1662DDE14C9D7C2300281E1715BDF03C988)

修改上述示例中LazyForEach的键值生成函数，使每个数据项生成唯一的键值，保证渲染效果符合预期。

```
1. LazyForEach(this.data, (item: string) => {
2. ListItem() {
3. Row() {
4. Text(item).fontSize(50)
5. .onAppear(() => {
6. hilog.info(DOMAIN, TAG, `appear: ${item}`);
7. })
8. }.margin({ left: 10, right: 10 })
9. }
10. }, (item: string, index: number) => `${item}-${index}`) // 自定义键值生成函数，返回唯一键值
```

[InitialRendering2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/InitialRendering2.ets#L53-L64)

修改后运行效果如下图所示。

**LazyForEach生成唯一键值**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/AlOcCK0hSSuZfDubZJYNiA/zh-cn_image_0000002558764144.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=D01D31AB1F3BF741F0C9A9ADB62689DB8C927935D6450BFE02D5770A1EEF76FB)

### 数据更新

当LazyForEach数据源发生变化，需要再次渲染时，开发者应根据数据源的变化情况调用listener对应的接口，通知LazyForEach做相应的更新。LazyForEach的更新操作包括：添加数据、删除数据、交换数据、改变单个数据、改变多个数据以及精准批量修改数据，各使用场景示例如下。

**添加数据**

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
2. import { BasicDataSource } from './BasicDataSource';

4. class MyDataSource extends BasicDataSource {
5. private dataArray: string[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): string {
12. return this.dataArray[index];
13. }

15. public pushData(data: string): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @Entry
22. @Component
23. struct AddingData {
24. private data: MyDataSource = new MyDataSource();

26. aboutToAppear() {
27. for (let i = 0; i <= 20; i++) {
28. this.data.pushData(`Hello ${i}`);
29. }
30. }

32. build() {
33. Scroll(){
34. List({ space: 3 }) {
35. LazyForEach(this.data, (item: string) => {
36. ListItem() {
37. Row() {
38. Text(item).fontSize(50)
39. .onAppear(() => {
40. })
41. }.margin({ left: 10, right: 10 })
42. }
43. .onClick(() => {
44. // 点击追加子组件
45. this.data.pushData(`Hello ${this.data.totalCount()}`);
46. })
47. }, (item: string) => item)
48. }
49. .cachedCount(5)
50. }
51. }
52. }
```

[AddingData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/AddingData.ets#L17-L70)

点击LazyForEach的子组件时，首先调用数据源data的pushData方法。此方法会在数据源末尾添加数据，并调用notifyDataAdd方法。notifyDataAdd方法内部会调用listener.onDataAdd方法，通知LazyForEach有数据添加。LazyForEach接收到通知后，在该索引处新建子组件。

运行效果如下图所示。

**LazyForEach添加数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/cc-yOZOdR8uFjIwhe9QRvw/zh-cn_image_0000002558604488.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=53F619885C70946070AD58CDCCC02BA4D34EF2129072AA68844E63631BAF3B9E)

**删除数据**

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class DataDeletionSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public getAllData(): string[] {
19. return this.dataArray;
20. }

22. public pushData(data: string): void {
23. this.dataArray.push(data);
24. }

26. public deleteData(index: number): void {
27. this.dataArray.splice(index, 1);
28. this.notifyDataDelete(index);
29. }
30. }

32. @Entry
33. @Component
34. struct DataDeletion {
35. private data: DataDeletionSource = new DataDeletionSource();

37. aboutToAppear() {
38. for (let i = 0; i <= 20; i++) {
39. this.data.pushData(`Hello ${i}`);
40. }
41. }

43. build() {
44. List({ space: 3 }) {
45. LazyForEach(this.data, (item: string, index: number) => {
46. ListItem() {
47. Row() {
48. Text(item).fontSize(50)
49. .onAppear(() => {
50. hilog.info(DOMAIN, TAG, `appear: ${item}`);
51. })
52. }.margin({ left: 10, right: 10 })
53. }
54. .onClick(() => {
55. // 点击删除子组件
56. this.data.deleteData(this.data.getAllData().indexOf(item));
57. })
58. }, (item: string) => item)
59. }
60. .cachedCount(5)
61. }
62. }
```

[DataDeletion.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/DataDeletion.ets#L16-L79)

点击LazyForEach的子组件时，调用数据源data的deleteData方法。此方法删除数据源中对应索引的数据，并调用notifyDataDelete方法。notifyDataDelete方法内调用listener.onDataDelete方法，通知 LazyForEach删除该索引处的子组件。

运行效果如下图所示。

**LazyForEach删除数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/LitzQ-zgQrmFwK6ymLSYww/zh-cn_image_0000002589324013.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=9B608AFF722FC23D32A6BB1C228C71D80C813764D7FED79F38FD89D6BDD950CA)

**交换数据**

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class SwappingDataSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public getAllData(): string[] {
19. return this.dataArray;
20. }

22. public pushData(data: string): void {
23. this.dataArray.push(data);
24. }

26. public moveData(from: number, to: number): void {
27. let temp: string = this.dataArray[from];
28. this.dataArray[from] = this.dataArray[to];
29. this.dataArray[to] = temp;
30. this.notifyDataMove(from, to);
31. }
32. }

34. @Entry
35. @Component
36. struct SwappingData {
37. private moved: number[] = [];
38. private data: SwappingDataSource = new SwappingDataSource();

40. aboutToAppear() {
41. for (let i = 0; i <= 20; i++) {
42. this.data.pushData(`Hello ${i}`);
43. }
44. }

46. build() {
47. List({ space: 3 }) {
48. LazyForEach(this.data, (item: string, index: number) => {
49. ListItem() {
50. Row() {
51. Text(item).fontSize(50)
52. .onAppear(() => {
53. hilog.info(DOMAIN, TAG, `appear: ${item}`);
54. })
55. }.margin({ left: 10, right: 10 })
56. }
57. .onClick(() => {
58. this.moved.push(this.data.getAllData().indexOf(item));
59. if (this.moved.length === 2) {
60. // 点击交换子组件
61. this.data.moveData(this.moved[0], this.moved[1]);
62. this.moved = [];
63. }
64. })
65. }, (item: string) => item)
66. }
67. .cachedCount(5)
68. }
69. }
```

[SwappingData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/SwappingData.ets#L16-L86)

首次点击LazyForEach的子组件时，将要移动的数据索引存储在moved成员变量中。再次点击LazyForEach的另一个子组件时，将首次点击的子组件移到此处。调用数据源data的moveData方法，该方法将数据源中的数据移动到预期位置，并调用notifyDataMove方法。notifyDataMove方法会调用listener.onDataMove方法，通知LazyForEach在该处有数据需要移动。LazyForEach将from和to索引处的子组件进行位置调换。

运行效果如下图所示。

**LazyForEach交换数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/JXINDT8xRtGi3G7QF1lpyA/zh-cn_image_0000002589243953.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=6237DAAD104FEE81ED0C04D49FF99B3C932FAFECC2657BC8413F1ECA4780B1D7)

**改变单个数据**

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class ModifyingDataSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public pushData(data: string): void {
19. this.dataArray.push(data);
20. }

22. public changeData(index: number, data: string): void {
23. this.dataArray.splice(index, 1, data);
24. this.notifyDataChange(index);
25. }
26. }

28. @Entry
29. @Component
30. struct ModifyingIndividualDataItems {
31. private data: ModifyingDataSource = new ModifyingDataSource();

33. aboutToAppear() {
34. for (let i = 0; i <= 20; i++) {
35. this.data.pushData(`Hello ${i}`);
36. }
37. }

39. build() {
40. List({ space: 3 }) {
41. LazyForEach(this.data, (item: string, index: number) => {
42. ListItem() {
43. Row() {
44. Text(item).fontSize(50)
45. .onAppear(() => {
46. hilog.info(DOMAIN, TAG, `appear: ${item}`);
47. })
48. }.margin({ left: 10, right: 10 })
49. }
50. .onClick(() => {
51. this.data.changeData(index, item + '00');
52. })
53. }, (item: string) => item)
54. }
55. .cachedCount(5)
56. }
57. }
```

[ModifyingIndividualDataItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ModifyingIndividualDataItems.ets#L16-L74)

点击LazyForEach的子组件时，首先改变当前数据，然后调用数据源data的changeData方法。changeData 方法会调用notifyDataChange方法，该方法又会调用listener.onDataChange方法，通知LazyForEach组件数据发生变化。LazyForEach会在对应索引处重建子组件。

运行效果如下图所示。

**LazyForEach改变单个数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/gu1WvTmGQyC3FlgfNGZwTg/zh-cn_image_0000002558764146.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=325B8952D3CD243200450EB3E0CE50E32A0DBB7BA23919BC313BCE18A6CE563B)

**改变多个数据**

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class ModifyingMultiSourceEleven extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public pushData(data: string): void {
19. this.dataArray.push(data);
20. }

22. public reloadData(): void {
23. this.notifyDataReload();
24. }

26. public modifyAllData(): void {
27. this.dataArray = this.dataArray.map((item: string) => {
28. return item + '0';
29. });
30. }
31. }

33. @Entry
34. @Component
35. struct ModifyingMultipleDataItems {
36. private data: ModifyingMultiSourceEleven = new ModifyingMultiSourceEleven();

38. aboutToAppear() {
39. for (let i = 0; i <= 20; i++) {
40. this.data.pushData(`Hello ${i}`);
41. }
42. }

44. build() {
45. List({ space: 3 }) {
46. LazyForEach(this.data, (item: string, index: number) => {
47. ListItem() {
48. Row() {
49. Text(item).fontSize(50)
50. .onAppear(() => {
51. hilog.info(DOMAIN, TAG, `appear: ${item}`);
52. })
53. }.margin({ left: 10, right: 10 })
54. }
55. .onClick(() => {
56. this.data.modifyAllData();
57. this.data.reloadData();
58. })
59. }, (item: string) => item)
60. }
61. .cachedCount(5)
62. }
63. }
```

[ModifyingMultipleDataItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ModifyingMultipleDataItems.ets#L16-L80)

点击LazyForEach的子组件时，首先调用data的modifyAllData方法修改数据源中的所有数据，然后调用数据源的reloadData方法。该方法内会调用notifyDataReload方法，notifyDataReload方法内会调用listener.onDataReloaded方法，通知LazyForEach重建所有子节点。LazyForEach会将原数据项和新数据项进行键值比对，若键值相同则使用缓存，若键值不同则重新构建。

运行效果如下图所示。

**LazyForEach改变多个数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/rsnyUvF5QUGEHwRBzlNuIg/zh-cn_image_0000002558604490.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=BAD5F2645170CD51A3F8DFF176CB4869469901D8012BA654CD386B1F13681096)

**精准批量修改数据**

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class PreciseModifyingDataSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public operateData(): void {
19. this.dataArray.splice(4, 0, this.dataArray[1]);
20. this.dataArray.splice(1, 1);
21. let temp = this.dataArray[4];
22. this.dataArray[4] = this.dataArray[6];
23. this.dataArray[6] = temp;
24. this.dataArray.splice(8, 0, 'Hello 1', 'Hello 2');
25. this.dataArray.splice(12, 2);
26. this.notifyDatasetChange([
27. { type: DataOperationType.MOVE, index: { from: 1, to: 3 } },
28. { type: DataOperationType.EXCHANGE, index: { start: 4, end: 6 } },
29. { type: DataOperationType.ADD, index: 8, count: 2 },
30. { type: DataOperationType.DELETE, index: 10, count: 2 }]);
31. }

33. public init(): void {
34. this.dataArray.splice(0, 0, 'Hello a', 'Hello b', 'Hello c', 'Hello d', 'Hello e', 'Hello f', 'Hello g', 'Hello h',
35. 'Hello i', 'Hello j', 'Hello k', 'Hello l', 'Hello m', 'Hello n', 'Hello o', 'Hello p', 'Hello q', 'Hello r');
36. }
37. }

39. @Entry
40. @Component
41. struct PreciselyModifyingData {
42. private data: PreciseModifyingDataSource = new PreciseModifyingDataSource();

44. aboutToAppear() {
45. this.data.init();
46. }

48. build() {
49. Column() {
50. Text('change data')
51. .fontSize(10)
52. .backgroundColor(Color.Blue)
53. .fontColor(Color.White)
54. .borderRadius(50)
55. .padding(5)
56. .onClick(() => {
57. this.data.operateData();
58. })
59. List({ space: 3 }) {
60. LazyForEach(this.data, (item: string, index: number) => {
61. ListItem() {
62. Row() {
63. Text(item).fontSize(35)
64. .onAppear(() => {
65. hilog.info(DOMAIN, TAG, `appear: ${item}`);
66. })
67. }.margin({ left: 10, right: 10 })
68. }

70. }, (item: string) => item + new Date().getTime())
71. }
72. .cachedCount(5)
73. }
74. }
75. }
```

[PreciselyModifyingData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/PreciselyModifyingData.ets#L16-L92)

onDatasetChange接口允许开发者一次性通知LazyForEach进行数据添加、删除、移动和交换等操作。在上述例子中，点击“change data”文本后，第二项数据被移动到第四项位置，第五项与第七项数据交换位置，并且从第九项开始添加了数据"Hello 1"和"Hello 2"，同时从第十一项开始删除了两项数据。

**LazyForEach改变多个数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/GazpbhUHSLWId8tme06qkg/zh-cn_image_0000002589324015.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=4927F88D5614B1646642ECD77F1BDE7EDF9DE431E4899520FFD9CC3956B21151)

第二个例子，直接给数组赋值，不涉及 splice 操作。operations直接从比较原数组和新数组得到。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class PreciselyModifyingSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public operateData(): void {
19. this.dataArray =
20. ['Hello x', 'Hello 1', 'Hello 2', 'Hello b', 'Hello c', 'Hello e', 'Hello d', 'Hello f', 'Hello g', 'Hello h'];
21. this.notifyDatasetChange([
22. { type: DataOperationType.CHANGE, index: 0 },
23. { type: DataOperationType.ADD, index: 1, count: 2 },
24. { type: DataOperationType.EXCHANGE, index: { start: 3, end: 4 } },
25. ]);
26. }

28. public init(): void {
29. this.dataArray = ['Hello a', 'Hello b', 'Hello c', 'Hello d', 'Hello e', 'Hello f', 'Hello g', 'Hello h'];
30. }
31. }

33. @Entry
34. @Component
35. struct PreciselyModifyingDataTwo {
36. private data: PreciselyModifyingSource = new PreciselyModifyingSource();

38. aboutToAppear() {
39. this.data.init();
40. }

42. build() {
43. Column() {
44. Text('Multi-Data Change')
45. .fontSize(10)
46. .backgroundColor(Color.Blue)
47. .fontColor(Color.White)
48. .borderRadius(50)
49. .padding(5)
50. .onClick(() => {
51. this.data.operateData();
52. })
53. List({ space: 3 }) {
54. LazyForEach(this.data, (item: string, index: number) => {
55. ListItem() {
56. Row() {
57. Text(item).fontSize(35)
58. .onAppear(() => {
59. hilog.info(DOMAIN, TAG, `appear: ${item}`);
60. })
61. }.margin({ left: 10, right: 10 })
62. }
63. }, (item: string) => item + new Date().getTime())
64. }
65. .cachedCount(5)
66. }
67. }
68. }
```

[PreciselyModifyingData2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/PreciselyModifyingData2.ets#L16-L85)

**LazyForEach改变多个数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/7mEr2KsES_iaoo0GkimIpA/zh-cn_image_0000002589243955.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=0BBC12E1F43BA43D30755A74DDF0FB68800596B4ECBE11732A747AD92B75F3B0)

使用该接口时请注意以下事项。

1. 不要将onDatasetChange与其他操作数据的接口混用。
2. 传入onDatasetChange的operations中，每一项operation的index均从修改前的原数组中查找。因此，operations中的index不总是与Datasource中的index一一对应，并且不能为负数。

   第一个例子清楚地显示了这一点:

   ```
   1. // 修改之前的数组
   2. ['Hello a','Hello b','Hello c','Hello d','Hello e','Hello f','Hello g','Hello h','Hello i','Hello j','Hello k','Hello l','Hello m','Hello n','Hello o','Hello p','Hello q','Hello r']
   3. // 修改之后的数组
   4. ['Hello a','Hello c','Hello d','Hello b','Hello g','Hello f','Hello e','Hello h','Hello 1','Hello 2','Hello i','Hello j','Hello m','Hello n','Hello o','Hello p','Hello q','Hello r']
   ```

   "Hello b" 从第2项变成第4项，因此第一个 operation 为 { type: DataOperationType.MOVE, index: { from: 1, to: 3 } }。

   "Hello e" 跟 "Hello g" 对调了，而 "Hello e" 在修改前的原数组中的 index=4，"Hello g" 在修改前的原数组中的 index=6, 因此第二个 operation 为 { type: DataOperationType.EXCHANGE, index: { start: 4, end: 6 } }。

   "Hello 1","Hello 2" 在 "Hello h" 之后插入，而 "Hello h" 在修改前的原数组中的 index=7，因此第三个 operation 为 { type: DataOperationType.ADD, index: 8, count: 2 }。

   "Hello k","Hello l" 被删除了，而 "Hello k" 在原数组中的 index=10，因此第四个 operation 为 { type: DataOperationType.DELETE, index: 10, count: 2 }。
3. 在同一个onDatasetChange批量处理数据时，如果多个DataOperation操作同一个index，只有第一个DataOperation生效。
4. 部分操作由开发者传入键值，LazyForEach不再重复调用keygenerator获取键值，开发者需保证传入键值的正确性。
5. 若操作集合中包含RELOAD操作，则其他操作均不生效。

## 高级特性

### 使用状态管理V1修改数据子属性

若仅靠LazyForEach的刷新机制，当item变化时若想更新子组件，需要将原来的子组件全部销毁再重新构建，在子组件结构较为复杂的情况下，靠改变键值去刷新渲染性能较低。因此状态管理V1提供了[@Observed装饰器和@ObjectLink装饰器](arkts-observed-and-objectlink.md)机制进行深度观测，可以做到仅刷新使用了该属性的组件，提高渲染性能。开发者可根据其自身业务特点选择使用哪种刷新方式。

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class MySubDataSource extends GenericBasicDataSource<StringData> {
5. private dataArray: StringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): StringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: StringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @Observed
22. class StringData {
23. public message: string;

25. constructor(message: string) {
26. this.message = message;
27. }
28. }

30. @Entry
31. @Component
32. struct ChangingDataSubproperties {
33. private data: MySubDataSource = new MySubDataSource();

35. aboutToAppear() {
36. for (let i = 0; i <= 20; i++) {
37. this.data.pushData(new StringData(`Hello ${i}`));
38. }
39. }

41. build() {
42. List({ space: 3 }) {
43. LazyForEach(this.data, (item: StringData, index: number) => {
44. ListItem() {
45. ChangingDataSubpropertiesChildComponent({ data: item })
46. }
47. .onClick(() => {
48. item.message += '0';
49. })
50. }, (item: StringData, index: number) => index.toString())
51. }
52. .cachedCount(5)
53. }
54. }

56. @Component
57. struct ChangingDataSubpropertiesChildComponent {
58. @ObjectLink data: StringData;

60. build() {
61. Row() {
62. Text(this.data.message).fontSize(50)
63. .onAppear(() => {
64. })
65. }.margin({ left: 10, right: 10 })
66. }
67. }
```

[ChangingDataSubproperties.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ChangingDataSubproperties.ets#L16-L84)

点击LazyForEach子组件改变item.message时，重渲染依赖ChangingDataSubpropertiesChildComponent的@ObjectLink成员变量对子属性的监听。框架仅刷新Text(this.data.message)，不会重建整个ListItem子组件。

**LazyForEach改变数据子属性**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Sqyj7gYVSdKyqTrMJd9Lrw/zh-cn_image_0000002558764148.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=30F8422714B9E49D4BB0EEC1E77365F6CA369644DACBAAD0CD5728AC44F237F4)

### 使用状态管理V2修改数据子属性

状态管理V2提供[@ObservedV2装饰器和@Trace装饰器](arkts-new-observedv2-and-trace.md)，用于实现属性的深度观测。使用[@Local装饰器](arkts-new-local.md)和[@Param装饰器](arkts-new-param.md)，可以管理子组件的刷新，仅刷新使用了对应属性的组件。

**嵌套类属性变化观测**

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class PropertiesDataSource extends GenericBasicDataSource<ClassPropertiesStringData> {
5. private dataArray: ClassPropertiesStringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): ClassPropertiesStringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: ClassPropertiesStringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. class ClassPropertiesStringData {
22. public firstLayer: FirstLayer;

24. constructor(firstLayer: FirstLayer) {
25. this.firstLayer = firstLayer;
26. }
27. }

29. class FirstLayer {
30. public secondLayer: SecondLayer;

32. constructor(secondLayer: SecondLayer) {
33. this.secondLayer = secondLayer;
34. }
35. }

37. class SecondLayer {
38. public thirdLayer: ThirdLayer;

40. constructor(thirdLayer: ThirdLayer) {
41. this.thirdLayer = thirdLayer;
42. }
43. }

45. @ObservedV2
46. class ThirdLayer {
47. @Trace public fourthLayer: string;

49. constructor(fourthLayer: string) {
50. this.fourthLayer = fourthLayer;
51. }
52. }

54. @Entry
55. @ComponentV2
56. struct ObservingNestedClassProperties {
57. private data: PropertiesDataSource = new PropertiesDataSource();

59. aboutToAppear() {
60. for (let i = 0; i <= 20; i++) {
61. this.data.pushData(new ClassPropertiesStringData(new FirstLayer(new SecondLayer(new ThirdLayer(`Hello ${i}`)))));
62. }
63. }

65. build() {
66. List({ space: 3 }) {
67. LazyForEach(this.data, (item: ClassPropertiesStringData, index: number) => {
68. ListItem() {
69. Text(item.firstLayer.secondLayer.thirdLayer.fourthLayer).fontSize(50)
70. .onClick(() => {
71. item.firstLayer.secondLayer.thirdLayer.fourthLayer += '!';
72. })
73. }
74. }, (item: ClassPropertiesStringData, index: number) => index.toString())
75. }
76. .cachedCount(5)
77. }
78. }
```

[ObservingNestedClassProperties.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ObservingNestedClassProperties.ets#L16-L95)

@ObservedV2与@Trace用于装饰类以及类中的属性，配合使用能深度观测被装饰的类和属性。示例中，展示了深度嵌套类结构下，通过@ObservedV2和@Trace实现对多层嵌套属性变化的观测和子组件刷新。当点击子组件Text修改被@Trace修饰的嵌套类最内层的类成员属性时，仅重新渲染依赖了该属性的组件。

**组件内部状态**

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class MyStateDataSource extends GenericBasicDataSource<StateStringData> {
5. private dataArray: StateStringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): StateStringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: StateStringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @ObservedV2
22. class StateStringData {
23. @Trace public message: string;

25. constructor(message: string) {
26. this.message = message;
27. }
28. }

30. @Entry
31. @ComponentV2
32. struct ObservingComponentInternalState {
33. data: MyStateDataSource = new MyStateDataSource();

35. aboutToAppear() {
36. for (let i = 0; i <= 20; i++) {
37. this.data.pushData(new StateStringData(`Hello ${i}`));
38. }
39. }

41. build() {
42. List({ space: 3 }) {
43. LazyForEach(this.data, (item: StateStringData, index: number) => {
44. ListItem() {
45. Row() {
46. Text(item.message).fontSize(50)
47. .onClick(() => {
48. // 修改@ObservedV2装饰类中@Trace装饰的变量，触发刷新此处Text组件
49. item.message += '!';
50. })
51. ObservingComponentChildComponent()
52. }
53. }
54. }, (item: StateStringData, index: number) => index.toString())
55. }
56. .cachedCount(5)
57. }
58. }

60. @ComponentV2
61. struct ObservingComponentChildComponent {
62. @Local message: string = '?';

64. build() {
65. Row() {
66. Text(this.message).fontSize(50)
67. .onClick(() => {
68. // 修改@Local装饰的变量，触发刷新此处Text组件
69. this.message += '?';
70. })
71. }
72. }
73. }
```

[ObservingComponentInternalState.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ObservingComponentInternalState.ets#L16-L90)

@Local使得自定义组件内被修饰的变量具有观测其变化的能力，该变量必须在组件内部进行初始化。示例中，点击Text组件修改item.message触发变量更新并刷新使用该变量的组件，ObservingComponentChildComponent中@Local装饰的变量message变化时也能刷新子组件。

**组件外部输入**

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class MyInputDataSource extends GenericBasicDataSource<InputStringData> {
5. private dataArray: InputStringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): InputStringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: InputStringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @ObservedV2
22. class InputStringData {
23. @Trace public message: string;

25. constructor(message: string) {
26. this.message = message;
27. }
28. }

30. @Entry
31. @ComponentV2
32. struct ReceivingExternalInput {
33. data: MyInputDataSource = new MyInputDataSource();

35. aboutToAppear() {
36. for (let i = 0; i <= 20; i++) {
37. this.data.pushData(new InputStringData(`Hello ${i}`));
38. }
39. }

41. build() {
42. List({ space: 3 }) {
43. LazyForEach(this.data, (item: InputStringData, index: number) => {
44. ListItem() {
45. ReceivingExternalInputChildComponent({ data: item.message })
46. .onClick(() => {
47. item.message += '!';
48. })
49. }
50. }, (item: InputStringData, index: number) => index.toString())
51. }
52. .cachedCount(5)
53. }
54. }

56. @ComponentV2
57. struct ReceivingExternalInputChildComponent {
58. @Param @Require data: string = '';

60. build() {
61. Row() {
62. Text(this.data).fontSize(50)
63. }
64. }
65. }
```

[ReceivingExternalInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ReceivingExternalInput.ets#L16-L82)

使用@Param装饰器，子组件可以接受外部输入参数，实现父子组件间的数据同步。在ReceivingExternalInput中创建子组件时，传递item.message，并用@Param修饰的变量data与其关联。点击ListItem中的组件修改item.message，数据变化会从父组件传递到子组件，触发子组件刷新。

### 拖拽排序

当LazyForEach在List组件下使用，并且设置了[onMove](../harmonyos-references/ts-universal-attributes-drag-sorting.md#onmove)事件，可以使能拖拽排序。拖拽排序释放后，如果数据位置发生变化，将触发onMove事件，上报原始索引号和目标索引号。在onMove事件中，根据上报的索引号修改数据源。修改数据源时，无需调用DataChangeListener接口通知数据源变化。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
2. import { BasicDataSource } from './BasicDataSource';

4. class DragAndDropDataSource extends BasicDataSource {
5. private dataArray: string[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): string {
12. return this.dataArray[index];
13. }

15. public moveDataWithoutNotify(from: number, to: number): void {
16. let tmp = this.dataArray.splice(from, 1);
17. this.dataArray.splice(to, 0, tmp[0]);
18. }

20. public pushData(data: string): void {
21. this.dataArray.push(data);
22. this.notifyDataAdd(this.dataArray.length - 1);
23. }
24. }

26. @Entry
27. @Component
28. struct DragandDropSorting {
29. private data: DragAndDropDataSource = new DragAndDropDataSource();

31. aboutToAppear(): void {
32. for (let i = 0; i < 100; i++) {
33. this.data.pushData(i.toString());
34. }
35. }

37. build() {
38. Row() {
39. List() {
40. LazyForEach(this.data, (item: string) => {
41. ListItem() {
42. Text(item.toString())
43. .fontSize(16)
44. .textAlign(TextAlign.Center)
45. .size({ height: 100, width: '100%' })
46. }.margin(10)
47. .borderRadius(10)
48. .backgroundColor('#FFFFFFFF')
49. }, (item: string) => item)
50. .onMove((from: number, to: number) => {
51. this.data.moveDataWithoutNotify(from, to);
52. })
53. }
54. .width('100%')
55. .height('100%')
56. .backgroundColor('#FFDCDCDC')
57. }
58. }
59. }
```

[DragandDropSorting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/DragandDropSorting.ets#L16-L76)

**LazyForEach拖拽排序效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ltEz4OInSACIy55Mmmh8aQ/zh-cn_image_0000002558604492.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=E240396B8BC79FE5108690D321B778C471E132665989E99FCAC7E4D4A213A6E7)

## 常见问题

### 删除节点后渲染结果非预期

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. // BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码。
2. import { BasicDataSource } from './BasicDataSource';

4. class MyDataSource extends BasicDataSource {
5. private dataArray: string[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): string {
12. return this.dataArray[index];
13. }

15. public pushData(data: string): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }

20. public deleteData(index: number): void {
21. this.dataArray.splice(index, 1);
22. this.notifyDataDelete(index);
23. }
24. }

26. @Entry
27. @Component
28. struct MyComponent {
29. private data: MyDataSource = new MyDataSource();

31. aboutToAppear() {
32. for (let i = 0; i <= 20; i++) {
33. this.data.pushData(`Hello ${i}`);
34. }
35. }

37. build() {
38. List({ space: 3 }) {
39. LazyForEach(this.data, (item: string, index: number) => {
40. ListItem() {
41. Row() {
42. Text(item).fontSize(50)
43. .onAppear(() => {
44. console.info(`appear: ${item}`);
45. })
46. }.margin({ left: 10, right: 10 })
47. }
48. .onClick(() => {
49. // 点击删除子组件
50. this.data.deleteData(index);
51. })
52. }, (item: string) => item)
53. }.cachedCount(5)
54. }
55. }
```

**LazyForEach删除数据非预期**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/iMtGnhs6TMSJK42kX2gs6w/zh-cn_image_0000002589324017.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=CF047EEFE3244B3C174CBA53B8668F63AE4FB0F7F11E22F77582F96C352D9DC4)

多次点击子组件时，发现删除的不一定是点击的那个子组件。原因在于删除某个子组件后，该子组件之后的数据项的index应减1，但实际后续数据项对应的子组件仍使用最初分配的index，itemGenerator中的index未更新，导致删除结果与预期不符。

修复代码如下。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class UnexpectedDataSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public pushData(data: string): void {
19. this.dataArray.push(data);
20. this.notifyDataAdd(this.dataArray.length - 1);
21. }

23. public deleteData(index: number): void {
24. this.dataArray.splice(index, 1);
25. this.notifyDataDelete(index);
26. }

28. public reloadData(): void {
29. this.notifyDataReload();
30. }
31. }

33. @Entry
34. @Component
35. struct UnexpectedRenderingResults {
36. private data: UnexpectedDataSource = new UnexpectedDataSource();

38. aboutToAppear() {
39. for (let i = 0; i <= 20; i++) {
40. this.data.pushData(`Hello ${i}`);
41. }
42. }

44. build() {
45. List({ space: 3 }) {
46. LazyForEach(this.data, (item: string, index: number) => {
47. ListItem() {
48. Row() {
49. Text(item).fontSize(50)
50. .onAppear(() => {
51. hilog.info(DOMAIN, TAG, `appear: ${item}`);
52. })
53. }.margin({ left: 10, right: 10 })
54. }
55. .onClick(() => {
56. // 点击删除子组件
57. this.data.deleteData(index);
58. // 重置所有子组件的index索引
59. this.data.reloadData();
60. })
61. }, (item: string, index: number) => item + index.toString())
62. }
63. .cachedCount(5)
64. }
65. }
```

[UnexpectedRenderingResults.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/UnexpectedRenderingResults.ets#L16-L82)

在删除一个数据项后调用reloadData方法，重建后面的数据项，以达到更新index索引的目的。要保证reloadData方法重建数据项，必须保证数据项能生成新的key。这里用了item + index.toString()保证被删除数据项后面的数据项都被重建。如果用item + Date.now().toString()替代，那么所有数据项都生成新的key，导致所有数据项都被重建。这种方法，效果是一样的，只是性能略差。

**修复LazyForEach删除数据非预期**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/0Oq2lzldRm2yYOdohFjuYw/zh-cn_image_0000002589243957.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=4491999058494F9AAA92928F52A36E9B67528D831727A15C03BC274E17992D6E)

### 重渲染时图片闪烁

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class MyDataSource extends GenericBasicDataSource<StringData> {
5. private dataArray: StringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): StringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: StringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }

20. public reloadData(): void {
21. this.notifyDataReload();
22. }
23. }

25. class StringData {
26. message: string;
27. imgSrc: Resource;

29. constructor(message: string, imgSrc: Resource) {
30. this.message = message;
31. this.imgSrc = imgSrc;
32. }
33. }

35. @Entry
36. @Component
37. struct MyComponent {
38. private moved: number[] = [];
39. private data: MyDataSource = new MyDataSource();

41. aboutToAppear() {
42. for (let i = 0; i <= 20; i++) {
43. // 此处'app.media.img'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
44. this.data.pushData(new StringData(`Hello ${i}`, $r('app.media.img')));
45. }
46. }

48. build() {
49. List({ space: 3 }) {
50. LazyForEach(this.data, (item: StringData, index: number) => {
51. ListItem() {
52. Column() {
53. Text(item.message).fontSize(50)
54. .onAppear(() => {
55. console.info(`appear: ${item.message}`);
56. })
57. Image(item.imgSrc)
58. .width(500)
59. .height(200)
60. }.margin({ left: 10, right: 10 })
61. }
62. .onClick(() => {
63. item.message += '00';
64. this.data.reloadData();
65. })
66. }, (item: StringData, index: number) => item.message) // 修改message属性会导致键值变化
67. }.cachedCount(5)
68. }
69. }
```

**LazyForEach仅改变文字但是图片闪烁问题**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/YpEk7gfNTbyLHKWFgGlJVA/zh-cn_image_0000002558764150.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=5BA96719FCE97F405AC9F222EC9E8EF1DEC490B64B70D93E5EC6C8791B8E513B)

单击ListItem子组件时，只改变了数据项的message属性，但因为键值发生变化，导致整个ListItem被重建。由于Image组件异步刷新，视觉上图片会闪烁。解决方法是保持键值不变，并使用@ObjectLink和@Observed单独刷新子组件Text。

修复代码如下。

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
3. import { GenericBasicDataSource } from './GenericBasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class FliceringDataSource extends GenericBasicDataSource<ImageFliceringStringData> {
8. private dataArray: ImageFliceringStringData[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): ImageFliceringStringData {
15. return this.dataArray[index];
16. }

18. public pushData(data: ImageFliceringStringData): void {
19. this.dataArray.push(data);
20. this.notifyDataAdd(this.dataArray.length - 1);
21. }
22. }

24. // @Observed类装饰器 和 @ObjectLink 用于在涉及嵌套对象或数组的场景中进行双向数据同步
25. @Observed
26. class ImageFliceringStringData {
27. public message: string;
28. public imgSrc: Resource;

30. constructor(message: string, imgSrc: Resource) {
31. this.message = message;
32. this.imgSrc = imgSrc;
33. }
34. }

36. @Entry
37. @Component
38. struct ImageFlickeringDuringRerenders {
39. private data: FliceringDataSource = new FliceringDataSource();

41. aboutToAppear() {
42. for (let i = 0; i <= 20; i++) {
43. // 此处'app.media.img'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
44. this.data.pushData(new ImageFliceringStringData(`Hello ${i}`, $r('app.media.img')));
45. }
46. }

48. build() {
49. List({ space: 3 }) {
50. LazyForEach(this.data, (item: ImageFliceringStringData, index: number) => {
51. ListItem() {
52. ImageFlickeringChildComponent({ data: item })
53. }
54. .onClick(() => {
55. item.message += '0';
56. })
57. }, (item: ImageFliceringStringData, index: number) => index.toString()) // 键值不受message属性影响
58. }
59. .cachedCount(5)
60. }
61. }

63. @Component
64. struct ImageFlickeringChildComponent {
65. // 用状态变量来驱动UI刷新，而不是通过Lazyforeach的api来驱动UI刷新
66. @ObjectLink data: ImageFliceringStringData;

68. build() {
69. Column() {
70. Text(this.data.message).fontSize(50)
71. .onAppear(() => {
72. hilog.info(DOMAIN, TAG, `appear: ${this.data.message}`);
73. })
74. Image(this.data.imgSrc)
75. .width(500)
76. .height(200)
77. }.margin({ left: 10, right: 10 })
78. }
79. }
```

[ImageFlickeringDuringRerenders.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ImageFlickeringDuringRerenders.ets#L16-L96)

**修复LazyForEach仅改变文字但是图片闪烁问题**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/u9Jxu9sdR8ytAuE6pL4vnA/zh-cn_image_0000002558604494.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=28130C4B938DB1C9F0D629E26ED1E7638ACB380BB1D1EEF35B0EA7C1B1041106)

### @ObjectLink属性变化UI未更新

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class MyDataSource extends GenericBasicDataSource<StringData> {
5. private dataArray: StringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): StringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: StringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @Observed
22. class StringData {
23. message: NestedString;

25. constructor(message: NestedString) {
26. this.message = message;
27. }
28. }

30. @Observed
31. class NestedString {
32. message: string;

34. constructor(message: string) {
35. this.message = message;
36. }
37. }

39. @Entry
40. @Component
41. struct MyComponent {
42. private moved: number[] = [];
43. private data: MyDataSource = new MyDataSource();

45. aboutToAppear() {
46. for (let i = 0; i <= 20; i++) {
47. this.data.pushData(new StringData(new NestedString(`Hello ${i}`)));
48. }
49. }

51. build() {
52. List({ space: 3 }) {
53. LazyForEach(this.data, (item: StringData, index: number) => {
54. ListItem() {
55. ChildComponent({ data: item })
56. }
57. .onClick(() => {
58. item.message.message += '0';
59. })
60. }, (item: StringData, index: number) => item.message.message + index.toString())
61. }.cachedCount(5)
62. }
63. }

65. @Component
66. struct ChildComponent {
67. @ObjectLink data: StringData;

69. build() {
70. Row() {
71. Text(this.data.message.message).fontSize(50)
72. .onAppear(() => {
73. console.info(`appear: ${this.data.message.message}`);
74. })
75. }.margin({ left: 10, right: 10 })
76. }
77. }
```

**ObjectLink属性变化后UI未更新**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/l6si38ZXTYKUQ2AUBOkvwA/zh-cn_image_0000002589324019.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=8CAC0FFF6EBDCF1EBC11F4F802A5DC7FAF675D42D635A47BF78963983DB0ED7B)

@ObjectLink装饰的成员变量仅能监听到其子属性的变化，无法监听深层嵌套属性，因此，只能通过修改子属性来通知组件重新渲染。具体请查看[@ObjectLink装饰器与@Observed装饰器的详细使用方法和限制条件](arkts-observed-and-objectlink.md)。

修复代码如下。

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class UINoteRenderingSource extends GenericBasicDataSource<UINoteRenderingStringData> {
5. private dataArray: UINoteRenderingStringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): UINoteRenderingStringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: UINoteRenderingStringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @Observed
22. class UINoteRenderingStringData {
23. public message: NestedString;

25. constructor(message: NestedString) {
26. this.message = message;
27. }
28. }

30. @Observed
31. class NestedString {
32. public message: string;

34. constructor(message: string) {
35. this.message = message;
36. }
37. }

39. @Entry
40. @Component
41. struct UINotRerenderedWhenObjectLinkIsChanged {
42. private moved: number[] = [];
43. private data: UINoteRenderingSource = new UINoteRenderingSource();

45. aboutToAppear() {
46. for (let i = 0; i <= 20; i++) {
47. this.data.pushData(new UINoteRenderingStringData(new NestedString(`Hello ${i}`)));
48. }
49. }

51. build() {
52. List({ space: 3 }) {
53. LazyForEach(this.data, (item: UINoteRenderingStringData, index: number) => {
54. ListItem() {
55. UINotRerenderedChildComponent({ data: item })
56. }
57. .onClick(() => {
58. // @ObjectLink装饰的成员变量仅能监听到其子属性的变化，再深入嵌套的属性便无法观测到
59. item.message = new NestedString(item.message.message + '0');
60. })
61. }, (item: UINoteRenderingStringData, index: number) => item.message.message + index.toString())
62. }
63. .cachedCount(5)
64. }
65. }

67. @Component
68. struct UINotRerenderedChildComponent {
69. @ObjectLink data: UINoteRenderingStringData;

71. build() {
72. Row() {
73. Text(this.data.message.message).fontSize(50)
74. }.margin({ left: 10, right: 10 })
75. }
76. }
```

[UINotRerenderedWhenObjectLinkIsChanged.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/UINotRerenderedWhenObjectLinkIsChanged.ets#L16-L93)

**修复ObjectLink属性变化后UI更新**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/uCjjyQh6QUqkrDq0SecAlA/zh-cn_image_0000002589243959.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=5896A236755CD8A776C50997D75DD197F30A5D504F23C324AA518FE0823700BA)

### 在List内使用屏幕闪烁

在[List](../harmonyos-references/ts-container-list.md)的[onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)方法中调用onDataReloaded可能会导致屏幕闪烁。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. // BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码。
2. import { BasicDataSource } from './BasicDataSource';

4. class MyDataSource extends BasicDataSource {
5. private dataArray: string[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): string {
12. return this.dataArray[index];
13. }

15. public pushData(data: string): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }

20. operateData(): void {
21. const totalCount = this.dataArray.length;
22. const batch = 5;
23. for (let i = totalCount; i < totalCount + batch; i++) {
24. this.dataArray.push(`Hello ${i}`);
25. }
26. this.notifyDataReload();
27. }
28. }

30. @Entry
31. @Component
32. struct MyComponent {
33. private moved: number[] = [];
34. private data: MyDataSource = new MyDataSource();

36. aboutToAppear() {
37. for (let i = 0; i <= 10; i++) {
38. this.data.pushData(`Hello ${i}`);
39. }
40. }

42. build() {
43. List({ space: 3 }) {
44. LazyForEach(this.data, (item: string, index: number) => {
45. ListItem() {
46. Row() {
47. Text(item)
48. .width('100%')
49. .height(80)
50. .backgroundColor(Color.Gray)
51. .onAppear(() => {
52. console.info(`appear: ${item}`);
53. })
54. }.margin({ left: 10, right: 10 })
55. }
56. }, (item: string) => item)
57. }.cachedCount(10)
58. .onScrollIndex((start, end, center) => {
59. if (end === this.data.totalCount() - 1) {
60. console.info('scroll to end');
61. this.data.operateData();
62. }
63. })
64. }
65. }
```

**当List下拉到底时，屏幕闪烁**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/TX7iln8rRTKzlIW1erqzzA/zh-cn_image_0000002558764152.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=3DB91FDAE06195CD630257DD2A48C6134909B814CF12D531BB7631F7ADDC4029)

使用onDatasetChange代替onDataReloaded，不仅可以修复闪屏问题，还能提升加载性能。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. // BasicDataSource代码见文档末尾BasicDataSource示例代码: String类型数组的BasicDataSource代码。
3. import { BasicDataSource } from './BasicDataSource';
4. const TAG = '[Sample_RenderingControl]';
5. const DOMAIN = 0xF811;

7. class ScreenFliceringDataSource extends BasicDataSource {
8. private dataArray: string[] = [];

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number): string {
15. return this.dataArray[index];
16. }

18. public pushData(data: string): void {
19. this.dataArray.push(data);
20. this.notifyDataAdd(this.dataArray.length - 1);
21. }

23. operateData(): void {
24. const totalCount = this.dataArray.length;
25. const batch = 5;
26. for (let i = totalCount; i < totalCount + batch; i++) {
27. this.dataArray.push(`Hello ${i}`);
28. }
29. // 替换 notifyDataReload
30. this.notifyDatasetChange([{ type: DataOperationType.ADD, index: totalCount, count: batch }]);
31. }
32. }

34. @Entry
35. @Component
36. struct ScreenFlickeringInList {
37. private moved: number[] = [];
38. private data: ScreenFliceringDataSource = new ScreenFliceringDataSource();

40. aboutToAppear() {
41. for (let i = 0; i <= 10; i++) {
42. this.data.pushData(`Hello ${i}`);
43. }
44. }

46. build() {
47. List({ space: 3 }) {
48. LazyForEach(this.data, (item: string, index: number) => {
49. ListItem() {
50. Row() {
51. Text(item)
52. .width('100%')
53. .height(80)
54. .backgroundColor(Color.Gray)
55. .onAppear(() => {
56. hilog.info(DOMAIN, TAG, `appear: ${item}`);
57. })
58. }.margin({ left: 10, right: 10 })
59. }
60. }, (item: string) => item)
61. }
62. .cachedCount(10)
63. .onScrollIndex((start, end, center) => {
64. if (end === this.data.totalCount() - 1) {
65. this.data.operateData();
66. }
67. })
68. }
69. }
```

[ScreenFlickeringInList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ScreenFlickeringInList.ets#L16-L86)

**修复后，当List下拉到底时，屏幕不闪烁**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/xIgHseX5RUC1dqFvq7g5Vw/zh-cn_image_0000002558604496.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=84E1E8BF7841597889F335D03D634BDB96EB2CAA11E9BAF3DA9D7015C558EE23)

### 组件复用渲染异常

[@Reusable装饰器](arkts-reusable.md)与[@ComponentV2装饰器](arkts-create-custom-components.md#componentv2)混用会导致组件渲染异常。

GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: [泛型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#泛型数组的basicdatasource代码)。

```
1. // GenericBasicDataSource代码见文档末尾BasicDataSource示例代码: 泛型数组的BasicDataSource代码。
2. import { GenericBasicDataSource } from './GenericBasicDataSource';

4. class MyDataSource extends GenericBasicDataSource<StringData> {
5. private dataArray: StringData[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): StringData {
12. return this.dataArray[index];
13. }

15. public pushData(data: StringData): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

22. class StringData {
23. message: string;

25. constructor(message: string) {
26. this.message = message;
27. }
28. }

30. @Entry
31. @ComponentV2
32. struct MyComponent {
33. data: MyDataSource = new MyDataSource();

35. aboutToAppear() {
36. for (let i = 0; i <= 30; i++) {
37. this.data.pushData(new StringData(`Hello${i}`));
38. }
39. }

41. build() {
42. List({ space: 3 }) {
43. LazyForEach(this.data, (item: StringData, index: number) => {
44. ListItem() {
45. ChildComponent({ data: item })
46. .onAppear(() => {
47. console.info(`onAppear: ${item.message}`);
48. })
49. }
50. }, (item: StringData, index: number) => index.toString())
51. }.cachedCount(5)
52. }
53. }

55. @Reusable
56. @Component
57. struct ChildComponent {
58. @State data: StringData = new StringData('');

60. aboutToAppear(): void {
61. console.info(`aboutToAppear: ${this.data.message}`);
62. }

64. aboutToRecycle(): void {
65. console.info(`aboutToRecycle: ${this.data.message}`);
66. }

68. // 对复用的组件进行数据更新
69. aboutToReuse(params: Record<string, ESObject>): void {
70. this.data = params.data as StringData;
71. console.info(`aboutToReuse: ${this.data.message}`);
72. }

74. build() {
75. Row() {
76. Text(this.data.message).fontSize(50)
77. }
78. }
79. }
```

反例中，在@ComponentV2装饰的组件MyComponent中，LazyForEach列表使用了@Reusable装饰的组件ChildComponent，导致组件渲染失败。从日志中可以看到，组件触发了onAppear，但没有触发aboutToAppear。

将@ComponentV2修改为[@Component](arkts-create-custom-components.md#component)可以修复渲染异常。修复后，当滑动事件触发组件节点下树时，对应的可复用组件ChildComponent会被加入复用缓存，而非被销毁，并触发aboutToRecycle事件，打印日志信息。当列表滑动，出现新节点时，会将可复用的组件从复用缓存中重新加入到节点树，触发aboutToReuse刷新组件数据，并打印日志信息。

### 键值不合理导致组件不刷新

开发者需要定义合适的键值生成函数，返回与目标数据相关联的键值。目标数据发生改变时，LazyForEach识别到键值改变才会刷新对应组件。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. // BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码。
2. import { BasicDataSource } from './BasicDataSource';

4. class MyDataSource extends BasicDataSource {
5. private dataArray: string[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): string {
12. return this.dataArray[index];
13. }

15. public pushData(data: string): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }

20. public updateAllData(): void {
21. this.dataArray = this.dataArray.map((item: string) => item + `!`);
22. this.notifyDataReload();
23. }
24. }

26. @Entry
27. @Component
28. struct MyComponent {
29. private data: MyDataSource = new MyDataSource();

31. aboutToAppear() {
32. for (let i = 0; i <= 20; i++) {
33. this.data.pushData(`Hello ${i}`);
34. }
35. }

37. build() {
38. Column() {
39. Button(`update all`)
40. .onClick(() => {
41. this.data.updateAllData();
42. })
43. List({ space: 3 }) {
44. LazyForEach(this.data, (item: string) => {
45. ListItem() {
46. Text(item).fontSize(50)
47. }
48. })
49. }.cachedCount(5)
50. }
51. }
52. }
```

**点击按钮更新数据，组件不会刷新**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Num8Ij5tR-qBnj_zQkCxDg/zh-cn_image_0000002589324021.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=5A3051DE66F78FAE1390A2934252B4060D7BF1DD34797AE6B25AE4A6BD52B848)

LazyForEach依赖生成的键值判断是否刷新子组件，如果更新的数据没有改变键值（如示例中开发者没有定义键值生成函数，此时键值仅与组件索引index有关，更新数据时键值不变），则LazyForEach不会刷新对应组件。

```
1. LazyForEach(this.data, (item: string) => {
2. ListItem() {
3. Text(item).fontSize(50)
4. }
5. }, (item: string) => item) // 定义键值生成函数
```

[ComponentRerenderingFailure.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/ComponentRerenderingFailure.ets#L58-L64)

**定义键值生成函数后，点击按钮更新数据，组件刷新**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/0uR5XSBURG-DgbtNynHRiA/zh-cn_image_0000002589243961.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=A53D1FE7FFBCBEC023B5FD9B7E1184B42B9B78CDFD93670E33015FC9C697FA84)

### 子组件尺寸缺失导致懒加载失效

支持数据懒加载的父组件基于自身和子组件的高度或宽度计算可视范围内应布局的子节点数量，高度或宽度的缺失会导致部分场景懒加载失效。如下示例，在纵向布局中，首次渲染时子组件的高度缺失，所有数据项对应组件都会被创建。

BasicDataSource代码见文档末尾BasicDataSource示例代码: [string类型数组的BasicDataSource代码](arkts-rendering-control-lazyforeach.md#string类型数组的basicdatasource代码)。

```
1. // BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码。
2. import { BasicDataSource } from './BasicDataSource';

4. class MyDataSource extends BasicDataSource {
5. public dataArray: string[] = [];

7. public totalCount(): number {
8. return this.dataArray.length;
9. }

11. public getData(index: number): string {
12. return this.dataArray[index];
13. }

15. public pushData(data: string): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }
19. }

21. @Entry
22. @Component
23. struct MyComponent {
24. private data: MyDataSource = new MyDataSource();

26. aboutToAppear() {
27. for (let i = 0; i <= 100; i++) {
28. this.data.pushData(``);
29. }
30. }

32. build() {
33. List() {
34. LazyForEach(this.data, (item: string, index: number) => {
35. ChildComponent({ message: item, index: index })
36. // 子组件未设置默认高度，首次渲染时所有数据项对应组件都被创建
37. // .height(60)
38. }, (item: string, index: number) => item + index)
39. }
40. .cachedCount(2)
41. }
42. }

44. @Component
45. struct ChildComponent {
46. message: string = ``;
47. index: number = -1;

49. aboutToAppear(): void {
50. console.info(`about to appear ${this.index}`);
51. }

53. build() {
54. Text(this.message).fontSize(50)
55. }
56. }
```

上述示例由于子组件ChildComponent的变量message初始值为空字符串，导致其内部的Text组件高度为 0，同时子组件未显式设置默认高度（如.height(60)），因此在首次渲染时所有子组件的高度均被计算为0。父组件List在基于高度计算可视范围时，判断所有子组件均位于可视区域内，导致懒加载机制失效，最终触发了全部数据项对应组件的创建（此示例无实际显示内容，可通过日志观察到所有about to appear打印）。

为子组件设置默认高度，确保父组件能正确计算可视范围，从而恢复此场景下懒加载功能（此示例无实际显示内容，可通过日志观察到仅显示区域和预加载区域内的节点打印了about to appear日志）。

```
1. LazyForEach(this.data, (item: string, index: number) => {
2. ChildComponent({ message: item, index: index })
3. // 设置子组件默认高度，首次渲染懒加载生效
4. .height(60)
5. }, (item: string, index: number) => item + index)
```

[LazyLoadingFailure.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/LazyLoadingFailure.ets#L48-L54)

## BasicDataSource示例代码

### string类型数组的BasicDataSource代码

```
1. // BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
2. export class BasicDataSource implements IDataSource {
3. private listeners: DataChangeListener[] = [];
4. private originDataArray: string[] = [];

6. public totalCount(): number {
7. return this.originDataArray.length;
8. }

10. public getData(index: number): string {
11. return this.originDataArray[index];
12. }

14. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
15. registerDataChangeListener(listener: DataChangeListener): void {
16. if (this.listeners.indexOf(listener) < 0) {
17. this.listeners.push(listener);
18. }
19. }

21. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
22. unregisterDataChangeListener(listener: DataChangeListener): void {
23. const pos = this.listeners.indexOf(listener);
24. if (pos >= 0) {
25. this.listeners.splice(pos, 1);
26. }
27. }

29. // 通知LazyForEach组件需要重载所有子组件
30. notifyDataReload(): void {
31. this.listeners.forEach(listener => {
32. listener.onDataReloaded();
33. });
34. }

36. // 通知LazyForEach组件需要在index对应索引处添加子组件
37. notifyDataAdd(index: number): void {
38. this.listeners.forEach(listener => {
39. listener.onDataAdd(index);
40. // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
41. });
42. }

44. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
45. notifyDataChange(index: number): void {
46. this.listeners.forEach(listener => {
47. listener.onDataChange(index);
48. // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
49. });
50. }

52. // 通知LazyForEach组件需要在index对应索引处删除该子组件
53. notifyDataDelete(index: number): void {
54. this.listeners.forEach(listener => {
55. listener.onDataDelete(index);
56. // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
57. });
58. }

60. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
61. notifyDataMove(from: number, to: number): void {
62. this.listeners.forEach(listener => {
63. listener.onDataMove(from, to);
64. // 写法2：listener.onDatasetChange(
65. // [{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
66. });
67. }

69. notifyDatasetChange(operations: DataOperation[]): void {
70. this.listeners.forEach(listener => {
71. listener.onDatasetChange(operations);
72. });
73. }
74. }
```

[BasicDataSource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/BasicDataSource.ets#L16-L91)

### 泛型数组的BasicDataSource代码

```
1. // GenericBasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
2. export class GenericBasicDataSource<T> implements IDataSource {
3. private listeners: DataChangeListener[] = [];
4. private originDataArray: T[] = [];

6. public totalCount(): number {
7. return this.originDataArray.length;
8. }

10. public getData(index: number): T {
11. return this.originDataArray[index];
12. }

14. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
15. registerDataChangeListener(listener: DataChangeListener): void {
16. if (this.listeners.indexOf(listener) < 0) {
17. this.listeners.push(listener);
18. }
19. }

21. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
22. unregisterDataChangeListener(listener: DataChangeListener): void {
23. const pos = this.listeners.indexOf(listener);
24. if (pos >= 0) {
25. this.listeners.splice(pos, 1);
26. }
27. }

29. // 通知LazyForEach组件需要重载所有子组件
30. notifyDataReload(): void {
31. this.listeners.forEach(listener => {
32. listener.onDataReloaded();
33. });
34. }

36. // 通知LazyForEach组件需要在index对应索引处添加子组件
37. notifyDataAdd(index: number): void {
38. this.listeners.forEach(listener => {
39. listener.onDataAdd(index);
40. });
41. }

43. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
44. notifyDataChange(index: number): void {
45. this.listeners.forEach(listener => {
46. listener.onDataChange(index);
47. });
48. }

50. // 通知LazyForEach组件需要在index对应索引处删除该子组件
51. notifyDataDelete(index: number): void {
52. this.listeners.forEach(listener => {
53. listener.onDataDelete(index);
54. });
55. }

57. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
58. notifyDataMove(from: number, to: number): void {
59. this.listeners.forEach(listener => {
60. listener.onDataMove(from, to);
61. });
62. }

64. notifyDatasetChange(operations: DataOperation[]): void {
65. this.listeners.forEach(listener => {
66. listener.onDatasetChange(operations);
67. });
68. }
69. }
```

[GenericBasicDataSource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingLazyForeach/GenericBasicDataSource.ets#L16-L86)
