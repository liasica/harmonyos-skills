---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-rendering-control-repeat
title: 循环渲染迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > 循环渲染迁移
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:57e819c1a8528f6a8056467a6df262d7d6ce189fbfd5171197162f2df2400f41
---

本文档主要介绍组件循环渲染从V1向V2的迁移，涉及如下渲染控制组件。

| 迁移前渲染控制组件名称 | 迁移后渲染控制组件名称 |
| --- | --- |
| [ForEach](arkts-rendering-control-foreach.md) | [Repeat](arkts-new-rendering-control-repeat.md) |
| [LazyForEach](arkts-rendering-control-lazyforeach.md) | [Repeat](arkts-new-rendering-control-repeat.md) |

## ForEach迁移Repeat

状态管理V2推荐使用Repeat替代ForEach。

ForEach使用示例请参考[数据源数组项子属性变化](arkts-rendering-control-foreach.md#数据源数组项子属性变化)。对应在V2中，ForEach迁移Repeat示例代码参考如下。

Repeat需要和状态管理V2一起使用，状态管理V2提供了@ObservedV2和@Trace装饰器对子属性进行深度观测。

* V1的@Observed替换成@ObservedV2+@Trace进行深度观测。
* 其余V1装饰器遵循迁移规则，替换成V2相关装饰器。
* 直接把ForEach的循环结构替换成Repeat结构。

```
1. @ObservedV2
2. class ArticleChangeChild {
3. public id: string;
4. public title: string;
5. public brief: string;
6. @Trace public isLiked: boolean;
7. @Trace public likesCount: number;

9. constructor(id: string, title: string, brief: string, isLiked: boolean, likesCount: number) {
10. this.id = id;
11. this.title = title;
12. this.brief = brief;
13. this.isLiked = isLiked;
14. this.likesCount = likesCount;
15. }
16. }

18. @Entry
19. @ComponentV2
20. struct ArticleListChangeView {
21. @Local articleList: Array<ArticleChangeChild> = [
22. new ArticleChangeChild('001', 'Article 0', 'Abstract', false, 100),
23. new ArticleChangeChild('002', 'Article 1', 'Abstract', false, 100),
24. new ArticleChangeChild('003', 'Article 2', 'Abstract', false, 100),
25. new ArticleChangeChild('004', 'Article 4', 'Abstract', false, 100),
26. new ArticleChangeChild('005', 'Article 5', 'Abstract', false, 100),
27. new ArticleChangeChild('006', 'Article 6', 'Abstract', false, 100),
28. ];

30. build() {
31. List() {
32. // Repeat结构体
33. Repeat(this.articleList)
34. .each((obj: RepeatItem<ArticleChangeChild>) => {
35. ListItem() {
36. ArticleCardChangeChild({ article: obj.item })
37. .margin({ top: 20 })
38. }
39. })
40. .key(item => item.id)
41. }
42. .padding(20)
43. .scrollBar(BarState.Off)
44. .backgroundColor(0xF1F3F5)
45. }
46. }

48. @ComponentV2
49. struct ArticleCardChangeChild {
50. @Require @Param article: ArticleChangeChild;

52. handleLiked() {
53. this.article.isLiked = !this.article.isLiked;
54. this.article.likesCount = this.article.isLiked ? this.article.likesCount + 1 : this.article.likesCount - 1;
55. }

57. build() {
58. Row() {
59. // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
60. Image($r('app.media.startIcon'))
61. .width(80)
62. .height(80)
63. .margin({ right: 20 })

65. Column() {
66. Text(this.article.title)
67. .fontSize(20)
68. .margin({ bottom: 8 })
69. Text(this.article.brief)
70. .fontSize(16)
71. .fontColor(Color.Gray)
72. .margin({ bottom: 8 })

74. Row() {
75. // 此处app.media.iconLiked'，'app.media.iconUnLiked'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
76. Image(this.article.isLiked ? $r('app.media.iconLiked') : $r('app.media.iconUnLiked'))
77. .width(24)
78. .height(24)
79. .margin({ right: 8 })
80. Text(this.article.likesCount.toString())
81. .fontSize(16)
82. }
83. .onClick(() => this.handleLiked())
84. .justifyContent(FlexAlign.Center)
85. }
86. .alignItems(HorizontalAlign.Start)
87. .width('80%')
88. .height('100%')
89. }
90. .padding(20)
91. .borderRadius(12)
92. .backgroundColor('#FFECECEC')
93. .height(120)
94. .width('100%')
95. .justifyContent(FlexAlign.SpaceBetween)
96. }
97. }
```

## LazyForEach迁移Repeat

### 数据首次渲染

**LazyForEach示例**

LazyForEach根据数据源循环渲染子组件。

示例1中，在容器组件[List](arkts-layout-development-create-list.md)中使用LazyForEach，并基于数据源循环渲染出了一系列[Text](arkts-common-components-text-display.md)子组件。

**示例1 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: string[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): string {
11. return this.dataArray[index];
12. }

14. public pushData(data: string): void {
15. this.dataArray.push(data);
16. this.notifyDataAdd(this.dataArray.length - 1);
17. }
18. }

20. @Entry
21. @Component
22. struct MyComponent {
23. private data: MyDataSource = new MyDataSource();

25. aboutToAppear() {
26. for (let i = 0; i <= 20; i++) {
27. this.data.pushData(`Hello ${i}`);
28. }
29. }

31. build() {
32. List({ space: 3 }) {
33. LazyForEach(this.data, (item: string) => {
34. ListItem() {
35. Row() {
36. Text(item).fontSize(50)
37. .onAppear(() => {
38. console.info(`appear: ${item}`);
39. })
40. }.margin({ left: 10, right: 10 })
41. }
42. }, (item: string) => item)
43. }.cachedCount(5)
44. }
45. }
```

以上是一个典型的使用LazyForEach循环渲染子组件的场景，下面将介绍如何将此示例迁移至Repeat。

**迁移步骤**

1. 使用状态管理V2装饰器。

   Repeat推荐和状态管理V2装饰器配合使用（[懒加载](arkts-new-rendering-control-repeat.md#懒加载能力说明)模式下只支持和状态管理V2装饰器配合使用）。如果之前使用的是状态管理V1装饰器，需要修改为状态管理V2装饰器。

   ```
   1. // 迁移前 - LazyForEach
   2. @Component // 状态管理V1
   3. struct MyComponent {
   4. build() {
   5. // ...
   6. LazyForEach(...)
   7. // ...
   8. }
   9. // ...其他属性、方法
   10. }

   12. // 迁移后 - Repeat
   13. @ComponentV2 // 状态管理V2
   14. struct MyComponent {
   15. build() {
   16. // ...
   17. Repeat(...)
   18. // ...
   19. }
   20. // ...其他属性、方法
   21. }
   ```
2. 迁移数据源。

   LazyForEach使用专用的数据结构[IDataSource](../harmonyos-references/ts-rendering-control-lazyforeach.md#idatasource)作为数据源。迁移至Repeat后，不再使用IDataSource作为数据源，而是使用状态管理V2装饰的数组作为数据源。

   ```
   1. // 迁移前 - LazyForEach
   2. class MyDataSource implements IDataSource {
   3. private dataArray: string[] = [];

   5. public totalCount(): number {
   6. return this.dataArray.length;
   7. }

   9. public getData(index: number): string {
   10. return this.dataArray[index];
   11. }

   13. // ...其他方法
   14. }

   16. // 迁移后 - Repeat
   17. @Local data: Array<string> = [];
   ```
3. 迁移组件生成函数和键值生成函数。

   LazyForEach与Repeat均通过组件生成函数，为每一项数据创建一个子组件；通过键值生成函数，为每一项数据生成一个唯一的键值。

   从LazyForEach迁移至Repeat时，两者的语法存在差异。Repeat需要在[.each()](../harmonyos-references/ts-rendering-control-repeat.md#each)或[.template()](../harmonyos-references/ts-rendering-control-repeat.md#template)中设置组件生成函数，在[.key()](../harmonyos-references/ts-rendering-control-repeat.md#key)中设置键值生成函数。

   ```
   1. // 迁移前 - LazyForEach
   2. List() {
   3. LazyForEach(
   4. this.data, // 数据源
   5. (item: string, index: number) => { // 组件生成函数
   6. ListItem() {
   7. Text(item)
   8. }
   9. },
   10. (item: string, index: number) => item // 键值生成函数
   11. )
   12. }

   14. // 迁移后 - Repeat
   15. List() {
   16. Repeat<string>(this.data) // 数据源
   17. .each((repeatItem: RepeatItem<string>) => { // 组件生成函数
   18. ListItem() {
   19. Text(repeatItem.item)
   20. }
   21. })
   22. .key((item: string, index: number) => item) // 键值生成函数
   23. }
   ```
4. 配置懒加载功能。

   Repeat具有[懒加载和全量加载](arkts-new-rendering-control-repeat.md#懒加载能力说明)两种模式。

   * 全量加载模式渲染所有子节点（对标[ForEach](arkts-rendering-control-foreach.md)）。
   * 懒加载模式动态渲染屏幕区域和预加载区域内的子节点（需要与容器组件配合使用，对标LazyForEach）。

   从LazyForEach迁移至Repeat时，需要调用[virtualScroll](../harmonyos-references/ts-rendering-control-repeat.md#virtualscroll)属性，使能懒加载。

   ```
   1. // 迁移前 - LazyForEach
   2. LazyForEach(data, (item) => {...}, (item) => item)

   4. // 迁移后 - Repeat
   5. Repeat(data)
   6. .virtualScroll() // 使能懒加载
   ```

**迁移后代码**

通过以上步骤，可以将示例1从LazyForEach迁移至Repeat，迁移后的完整示例如下所示。

**示例1 - 迁移后**

```
1. @Entry
2. @ComponentV2 // 使用状态管理V2
3. struct MyComponent {
4. @Local data: Array<string> = []; // 数据源为状态管理V2装饰的数组

6. aboutToAppear() {
7. for (let i = 0; i <= 20; i++) {
8. this.data.push(`Hello ${i}`);
9. }
10. }

12. build() {
13. List({ space: 3 }) {
14. Repeat(this.data) // 使用Repeat
15. .each((repeatItem: RepeatItem<string>) => { // 组件生成函数
16. ListItem() {
17. Row() {
18. Text(repeatItem.item).fontSize(50)
19. .onAppear(() => {
20. console.info(`appear: ${repeatItem.item}`);
21. })
22. }.margin({ left: 10, right: 10 })
23. }
24. })
25. .key((item: string) => item) // 键值生成函数
26. .virtualScroll() // 使能懒加载
27. }.cachedCount(5)
28. }
29. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ucwc6mbLR0y7NgbBjXTjwg/zh-cn_image_0000002552957628.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=EE53FF6732ADA44887EAAC02B56B9DC6E31DDEFC7CAAC422619BE8F8AD34F1F3)

### 数据更新操作

**LazyForEach示例**

当LazyForEach的数据源发生变化时，开发者需要根据数据源的变化情况调用[DataChangeListener](../harmonyos-references/ts-rendering-control-lazyforeach.md#datachangelistener)对应的接口，通知LazyForEach做相应的更新。主要的数据操作包括：添加数据、删除数据、交换数据、修改单个数据、修改多个数据、精准批量修改数据。

示例2演示了主要的数据操作。

**示例2 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: string[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): string {
11. return this.dataArray[index];
12. }

14. // 添加数据
15. public pushData(data: string): void {
16. this.dataArray.push(data);
17. this.notifyDataAdd(this.dataArray.length - 1);
18. }

20. // 删除数据
21. public deleteData(index: number): void {
22. this.dataArray.splice(index, 1);
23. this.notifyDataDelete(index);
24. }

26. // 交换数据
27. public moveData(from: number, to: number): void {
28. let temp: string = this.dataArray[from];
29. this.dataArray[from] = this.dataArray[to];
30. this.dataArray[to] = temp;
31. this.notifyDataMove(from, to);
32. }

34. // 修改单个数据
35. public changeData(index: number, data: string): void {
36. this.dataArray.splice(index, 1, data);
37. this.notifyDataChange(index);
38. }

40. // 修改多个数据
41. public modifyAllData(): void {
42. this.dataArray = this.dataArray.map((item: string) => {
43. return 'Changed ' + item;
44. });
45. this.notifyDataReload();
46. }
47. }

49. @Entry
50. @Component
51. struct MyComponent {
52. private data: MyDataSource = new MyDataSource();
53. private count: number = 0;

55. aboutToAppear() {
56. for (let i = 0; i <= 10; i++) {
57. this.data.pushData(`Hello ${i}`);
58. }
59. }

61. build() {
62. Column({ space: 3 }) {
63. // 点击追加子组件
64. Button('Add new item')
65. .onClick(() => {
66. this.data.pushData(`New item ${this.count++}`);
67. })
68. // 点击删除子组件
69. Button('Delete item 0')
70. .onClick(() => {
71. this.data.deleteData(0);
72. })
73. // 点击交换子组件
74. Button('Swap item 0 and item 1')
75. .onClick(() => {
76. this.data.moveData(0, 1);
77. })
78. // 点击修改单个子组件
79. Button('Change item 0')
80. .onClick(() => {
81. this.data.changeData(0, `Changed item ${this.count++}`);
82. })
83. // 点击修改多个子组件
84. Button('Change all items')
85. .onClick(() => {
86. this.data.modifyAllData();
87. })
88. List({ space: 3 }) {
89. LazyForEach(this.data, (item: string) => {
90. ListItem() {
91. Row() {
92. Text(item).fontSize(25)
93. }
94. }
95. }, (item: string) => item)
96. }.cachedCount(5)
97. }
98. }
99. }
```

以上是一个典型的更新数据后LazyForEach重新渲染子组件的场景，下面将介绍如何将此示例迁移至Repeat。

**迁移步骤**

1. 迁移准备。

   根据[数据首次渲染](arkts-v1-v2-migration-rendering-control-repeat.md#数据首次渲染)小节中的步骤，将LazyForEach替换为Repeat。

   1. 使用状态管理V2装饰器。
   2. 迁移数据源。
   3. 迁移组件生成函数与键值生成函数。
   4. 使能懒加载。
2. 迁移数据源修改方式。

   * 对于LazyForEach，在修改数据源后需要调用对应的接口通知其更新。
   * 对于Repeat，由状态管理V2监听其数据源变化，并触发更新。因此，开发者直接修改数据源即可，无需其他额外操作。

   ```
   1. // 以修改单个数据为例
   2. // 迁移前 - LazyForEach
   3. class MyDataSource implements IDataSource {
   4. private dataArray: string[] = [];

   6. public changeData(index: number, newData: string): void {
   7. this.dataArray.splice(index, 1, data);
   8. this.notifyDataChange(index);
   9. }

   11. // ...其他方法
   12. }

   14. // 迁移后 - Repeat
   15. this.data.splice(index, 1, data);
   ```

   其他数据更新操作，如添加数据、删除数据、交换数据等，与以上方法类似，可通过直接修改数据源数组实现。

**迁移后代码**

迁移后的完整示例如下。

**示例2 - 迁移后**

```
1. @Entry
2. @ComponentV2
3. struct MyComponent {
4. @Local data: Array<string> = [];
5. private count: number = 0;

7. aboutToAppear() {
8. for (let i = 0; i <= 10; i++) {
9. this.data.push(`Hello ${i}`);
10. }
11. }

13. build() {
14. Column({ space: 3 }) {
15. // 点击追加子组件
16. Button('Add new item')
17. .onClick(() => { this.data.push(`New item ${this.count++}`); })
18. // 点击删除子组件
19. Button('Delete item 0')
20. .onClick(() => { this.data.splice(0, 1); })
21. // 点击交换子组件
22. Button('Swap item 0 and item 1')
23. .onClick(() => { let temp: string = this.data[0];
24. this.data[0] = this.data[1];
25. this.data[1] = temp; })
26. // 点击修改单个子组件
27. Button('Change item 0')
28. .onClick(() => { this.data.splice(0, 1, `Changed item ${this.count++}`); })
29. // 点击修改多个子组件
30. Button('Change all items')
31. .onClick(() => { this.data = this.data.map((item: string) => { return 'Changed ' + item; }); })
32. List({ space: 3 }) {
33. Repeat(this.data)
34. .each((repeatItem: RepeatItem<string>) => {
35. ListItem() {
36. Row() {
37. Text(repeatItem.item).fontSize(25)
38. }
39. }
40. })
41. .key((item: string) => item)
42. .virtualScroll()
43. }.cachedCount(5)
44. }
45. }
46. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/aj_LiLQ7TlGVY0xVO5hzvg/zh-cn_image_0000002583477629.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=4E38765B40CBA1E641987CBDE0741D6268ACF2691546EA3E0E8A2FBED3DB1BA3)

### 修改数据子属性

**LazyForEach示例**

LazyForEach可以使用[@Observed与@ObjectLink](arkts-observed-and-objectlink.md)装饰器实现对数据子属性的观测。当有数据子属性发生变化时，仅更新使用了该子属性的组件，从而提高性能。

示例3演示了对子属性的观测。

**示例3 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: StringData类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: StringData[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): StringData {
11. return this.dataArray[index];
12. }

14. public pushData(data: StringData): void {
15. this.dataArray.push(data);
16. this.notifyDataAdd(this.dataArray.length - 1);
17. }
18. }

20. @Observed
21. class StringData {
22. message: string;

24. constructor(message: string) {
25. this.message = message;
26. }
27. }

29. @Entry
30. @Component
31. struct MyComponent {
32. private data: MyDataSource = new MyDataSource();

34. aboutToAppear() {
35. for (let i = 0; i <= 20; i++) {
36. this.data.pushData(new StringData(`Hello ${i}`));
37. }
38. }

40. build() {
41. List({ space: 3 }) {
42. LazyForEach(this.data, (item: StringData, index: number) => {
43. ListItem() {
44. ChildComponent({ data: item })
45. }
46. .onClick(() => {
47. item.message += '0';
48. })
49. }, (item: StringData, index: number) => index.toString())
50. }.cachedCount(5)
51. }
52. }

54. @Component
55. struct ChildComponent {
56. @ObjectLink data: StringData;

58. build() {
59. Row() {
60. Text(this.data.message).fontSize(50)
61. .onAppear(() => {
62. console.info(`appear: ${this.data.message}`);
63. })
64. }.margin({ left: 10, right: 10 })
65. }
66. }
```

**迁移Repeat**

Repeat需要和状态管理V2一起使用，状态管理V2提供了[@ObservedV2和@Trace](arkts-new-observedv2-and-trace.md)装饰器对子属性进行深度观测。迁移时，需要将@Observe和@ObjectLink装饰器迁移至@ObserveV2和@Trace装饰器。

迁移后的示例如下所示。

**示例3 - 迁移后**

```
1. @ObservedV2
2. class StringData {
3. @Trace message: string; // 观测子属性

5. constructor(message: string) {
6. this.message = message;
7. }
8. }

10. @Entry
11. @ComponentV2
12. struct MyComponent {
13. @Local data: StringData[] = [];

15. aboutToAppear() {
16. for (let i = 0; i <= 20; i++) {
17. this.data.push(new StringData(`Hello ${i}`));
18. }
19. }

21. build() {
22. List({ space: 3 }) {
23. Repeat(this.data)
24. .each((repeatItem) => {
25. ListItem() {
26. Text(repeatItem.item.message).fontSize(50)
27. .onAppear(() => {
28. console.info(`appear: ${repeatItem.item.message}`);
29. })
30. }
31. .onClick(() => {
32. repeatItem.item.message += '0';
33. })
34. })
35. .key((item: StringData, index: number) => index.toString())
36. .virtualScroll()
37. }.cachedCount(5)
38. }
39. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/3maKpWpzSQG5_TLQhTBp4g/zh-cn_image_0000002552797980.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=FDFAF5B46293B285CF530FA65440AF4E69DF30DB29F8B58F7359DDBDDD9ADB50)

### 状态管理V2观测组件内部状态

**LazyForEach示例**

状态管理V2的[@Local](arkts-new-local.md)装饰器提供了观测自定义组件内部变量的能力。被@Local装饰的变量发生变化时，会通知LazyForEach更新对应的组件。

示例4演示了在LazyForEach中使用@Local装饰器观测数据变化，触发组件更新。

**示例4 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: StringData类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: StringData[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): StringData {
11. return this.dataArray[index];
12. }

14. public pushData(data: StringData): void {
15. this.dataArray.push(data);
16. this.notifyDataAdd(this.dataArray.length - 1);
17. }
18. }

20. @ObservedV2
21. class StringData {
22. @Trace message: string;

24. constructor(message: string) {
25. this.message = message;
26. }
27. }

29. @Entry
30. @ComponentV2
31. struct MyComponent {
32. data: MyDataSource = new MyDataSource();

34. aboutToAppear() {
35. for (let i = 0; i <= 20; i++) {
36. this.data.pushData(new StringData(`Hello ${i}`));
37. }
38. }

40. build() {
41. List({ space: 3 }) {
42. LazyForEach(this.data, (item: StringData, index: number) => {
43. ListItem() {
44. Row() {
45. Text(item.message).fontSize(50)
46. .onClick(() => {
47. // 修改@ObservedV2装饰类中@Trace装饰的变量，触发刷新此处Text组件
48. item.message += '!';
49. })
50. ChildComponent()
51. }
52. }
53. }, (item: StringData, index: number) => index.toString())
54. }.cachedCount(5)
55. }
56. }

58. @ComponentV2
59. struct ChildComponent {
60. @Local message: string = '?';

62. build() {
63. Row() {
64. Text(this.message).fontSize(50)
65. .onClick(() => {
66. // 修改@Local装饰的变量，触发刷新此处Text组件
67. this.message += '?';
68. })
69. }
70. }
71. }
```

**迁移Repeat**

Repeat本身支持与状态管理V2联合使用，将LazyForEach相关代码修改为Repeat后，即可实现对组件内部状态变量的观测。

迁移后的示例如下所示。

**示例4 - 迁移后**

```
1. @ObservedV2
2. class StringData {
3. @Trace message: string;

5. constructor(message: string) {
6. this.message = message;
7. }
8. }

10. @Entry
11. @ComponentV2
12. struct MyComponent {
13. @Local data: StringData[] = [];

15. aboutToAppear() {
16. for (let i = 0; i <= 20; i++) {
17. this.data.push(new StringData(`Hello ${i}`));
18. }
19. }

21. build() {
22. List({ space: 3 }) {
23. Repeat(this.data)
24. .each((repeatItem) => {
25. ListItem() {
26. Row() {
27. Text(repeatItem.item.message).fontSize(50)
28. .onClick(() => {
29. // 修改@ObservedV2装饰类中@Trace装饰的变量，触发刷新此处Text组件
30. repeatItem.item.message += '!';
31. })
32. ChildComponent()
33. }
34. }
35. })
36. .key((item: StringData, index: number) => index.toString())
37. .virtualScroll()
38. }.cachedCount(5)
39. }
40. }

42. @ComponentV2
43. struct ChildComponent {
44. @Local message: string = '?';

46. build() {
47. Row() {
48. Text(this.message).fontSize(50)
49. .onClick(() => {
50. // 修改@Local装饰的变量，触发刷新此处Text组件
51. this.message += '?';
52. })
53. }
54. }
55. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/nvuKIg_KQfuZavjk9yWKmA/zh-cn_image_0000002583437675.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=91067909ADA6F4A00909FECE162C339C3242303ECB1DE664AF2AFF62445ECCD2)

### 状态管理V2观测组件外部输入

**LazyForEach示例**

状态管理V2的[@Param](arkts-new-param.md)装饰器提供了观测自定义组件外部输入变量的能力，可以实现父子组件间的数据同步。将父组件的变量传递给子组件，并用@Param装饰，当父组件变量发生变化时，会通知对应的组件更新。

示例5演示了在LazyForEach中使用@Param装饰器观测数据变化，触发组件更新。

**示例5 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: StringData类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: StringData[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): StringData {
11. return this.dataArray[index];
12. }

14. public pushData(data: StringData): void {
15. this.dataArray.push(data);
16. this.notifyDataAdd(this.dataArray.length - 1);
17. }
18. }

20. @ObservedV2
21. class StringData {
22. @Trace message: string;

24. constructor(message: string) {
25. this.message = message;
26. }
27. }

29. @Entry
30. @ComponentV2
31. struct MyComponent {
32. data: MyDataSource = new MyDataSource();

34. aboutToAppear() {
35. for (let i = 0; i <= 20; i++) {
36. this.data.pushData(new StringData(`Hello ${i}`));
37. }
38. }

40. build() {
41. List({ space: 3 }) {
42. LazyForEach(this.data, (item: StringData, index: number) => {
43. ListItem() {
44. ChildComponent({ data: item.message }) // 向自定义组件内传入变量
45. .onClick(() => {
46. item.message += '!';
47. })
48. }
49. }, (item: StringData, index: number) => index.toString())
50. }.cachedCount(5)
51. }
52. }

54. @ComponentV2
55. struct ChildComponent {
56. @Param @Require data: string = ''; // 接收来自外部的变量

58. build() {
59. Row() {
60. Text(this.data).fontSize(50)
61. }
62. }
63. }
```

**迁移Repeat**

Repeat本身支持与状态管理V2联合使用，将LazyForEach相关代码修改为Repeat后，即可实现对组件外部输入状态变量的观测。

迁移后的示例如下所示。

**示例5 - 迁移后**

```
1. @ObservedV2
2. class StringData {
3. @Trace message: string;

5. constructor(message: string) {
6. this.message = message;
7. }
8. }

10. @Entry
11. @ComponentV2
12. struct MyComponent {
13. @Local data: StringData[] = [];

15. aboutToAppear() {
16. for (let i = 0; i <= 20; i++) {
17. this.data.push(new StringData(`Hello ${i}`));
18. }
19. }

21. build() {
22. List({ space: 3 }) {
23. Repeat(this.data)
24. .each((repeatItem) => {
25. ListItem() {
26. ChildComponent({ data: repeatItem.item.message }) // 向自定义组件内传入变量
27. .onClick(() => {
28. repeatItem.item.message += '!';
29. })
30. }
31. })
32. .key((item: StringData, index: number) => index.toString())
33. .virtualScroll()
34. }.cachedCount(5)
35. }
36. }

38. @ComponentV2
39. struct ChildComponent {
40. @Param @Require data: string = ''; // 接收来自外部的变量

42. build() {
43. Row() {
44. Text(this.data).fontSize(50)
45. }
46. }
47. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/1hhT0J0fTESihdEIkkWrgg/zh-cn_image_0000002552957630.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=6B087B24EEDC0E57FFE8CDBEB1D7231A9D4510D0D46F852231036D53B9B5DBD7)

### 拖拽排序

**LazyForEach示例**

LazyForEach的[onMove](../harmonyos-references/ts-universal-attributes-drag-sorting.md#onmove)属性提供了拖拽排序能力。

示例6为典型用例。

**示例6 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: string类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: string[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): string {
11. return this.dataArray[index];
12. }

14. public moveDataWithoutNotify(from: number, to: number): void {
15. let tmp = this.dataArray.splice(from, 1);
16. this.dataArray.splice(to, 0, tmp[0]);
17. }

19. public pushData(data: string): void {
20. this.dataArray.push(data);
21. this.notifyDataAdd(this.dataArray.length - 1);
22. }
23. }

25. @Entry
26. @Component
27. struct Parent {
28. private data: MyDataSource = new MyDataSource();

30. aboutToAppear(): void {
31. for (let i = 0; i < 100; i++) {
32. this.data.pushData(i.toString());
33. }
34. }

36. build() {
37. Row() {
38. List() {
39. LazyForEach(this.data, (item: string) => {
40. ListItem() {
41. Text(item.toString())
42. .fontSize(16)
43. .textAlign(TextAlign.Center)
44. .size({ height: 100, width: '100%' })
45. }.margin(10)
46. .borderRadius(10)
47. .backgroundColor('#FFFFFFFF')
48. }, (item: string) => item)
49. .onMove((from: number, to: number) => { // 实现拖拽排序
50. this.data.moveDataWithoutNotify(from, to);
51. })
52. }
53. .width('100%')
54. .height('100%')
55. .backgroundColor('#FFDCDCDC')
56. }
57. }
58. }
```

**迁移Repeat**

Repeat具有与LazyForEach相同的onMove属性。将LazyForEach相关代码修改为Repeat后，即可实现拖拽排序。

迁移后的示例如下所示。

**示例6 - 迁移后**

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Local data: string[] = [];

6. aboutToAppear(): void {
7. for (let i = 0; i < 100; i++) {
8. this.data.push(i.toString());
9. }
10. }

12. moveData(from: number, to: number) {
13. let tmp = this.data.splice(from, 1);
14. this.data.splice(to, 0, tmp[0]);
15. }

17. build() {
18. Row() {
19. List() {
20. Repeat(this.data)
21. .each((repeatItem) => {
22. ListItem() {
23. Text(repeatItem.item.toString())
24. .fontSize(16)
25. .textAlign(TextAlign.Center)
26. .size({ height: 100, width: '100%' })
27. }.margin(10)
28. .borderRadius(10)
29. .backgroundColor('#FFFFFFFF')
30. })
31. .key((item: string) => item)
32. .virtualScroll()
33. .onMove((from: number, to: number) => { // 实现拖拽排序
34. this.moveData(from, to);
35. })
36. }
37. .width('100%')
38. .height('100%')
39. .backgroundColor('#FFDCDCDC')
40. }
41. }
42. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/7JHf6KXkR0q7-vzviS0KIA/zh-cn_image_0000002583477631.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=CF5787276F709AFCD22CB9FA9C332185A652E743CBE2912590FCB734C5EE8DA1)

### 组件复用

**LazyForEach示例**

LazyForEach自身并不具备组件复用能力，为实现组件复用，需要与[@Reusable](arkts-reusable.md)装饰器配合使用（被@Reusable装饰的自定义组件具有复用能力）。

示例7演示了组件复用的典型场景。

**示例7 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: StringData类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: StringData[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): StringData {
11. return this.dataArray[index];
12. }

14. public pushData(data: StringData): void {
15. this.dataArray.push(data);
16. this.notifyDataAdd(this.dataArray.length - 1);
17. }
18. }

20. class StringData {
21. message: string;

23. constructor(message: string) {
24. this.message = message;
25. }
26. }

28. @Entry
29. @Component
30. struct MyComponent {
31. data: MyDataSource = new MyDataSource();

33. aboutToAppear() {
34. for (let i = 0; i <= 30; i++) {
35. this.data.pushData(new StringData(`Hello${i}`));
36. }
37. }

39. build() {
40. List({ space: 3 }) {
41. LazyForEach(this.data, (item: StringData, index: number) => {
42. ListItem() {
43. ChildComponent({ data: item })
44. .onAppear(() => {
45. console.info(`onAppear: ${item.message}`);
46. })
47. }
48. }, (item: StringData, index: number) => index.toString())
49. }.cachedCount(5)
50. }
51. }

53. @Reusable
54. @Component
55. struct ChildComponent {
56. @State data: StringData = new StringData('');

58. aboutToAppear(): void {
59. console.info(`aboutToAppear: ${this.data.message}`);
60. }

62. aboutToRecycle(): void {
63. console.info(`aboutToRecycle: ${this.data.message}`);
64. }

66. // 对复用的组件进行数据更新
67. aboutToReuse(params: Record<string, ESObject>): void {
68. this.data = params.data as StringData;
69. console.info(`aboutToReuse: ${this.data.message}`);
70. }

72. build() {
73. Row() {
74. Text(this.data.message).fontSize(50)
75. }
76. }
77. }
```

**迁移Repeat**

Repeat本身具备组件复用能力，同时也支持与状态管理V2的[@ReusableV2](arkts-new-reusablev2.md)装饰器联合使用。因此，迁移至Repeat后，其组件复用具有两种实现方案。

1. 直接使用Repeat自身的复用能力。
2. 使用@ReusableV2装饰器提供的复用能力。

需要注意的是，Repeat默认启用自身的复用能力，且优先级高于@ReusableV2装饰器。若要使用@ReusableV2装饰器，必须先手动关闭Repeat自身的复用能力，即Repeat中[VirtualScrollOptions](../harmonyos-references/ts-rendering-control-repeat.md#virtualscrolloptions)的reusable属性设置为false（@ReusableV2装饰器从API version 18开始支持，Repeat从API version 18开始支持关闭自身复用能力）。

**示例7 - 迁移方案1：使用Repeat自身的复用能力**

Repeat本身具备复用能力，且默认开启。将LazyForEach相关代码迁移至Repeat后，便已经具备了复用能力。

修改后的示例如下。

```
1. class StringData {
2. message: string;

4. constructor(message: string) {
5. this.message = message;
6. }
7. }

9. @Entry
10. @ComponentV2
11. struct MyComponent {
12. @Local data: StringData[] = [];

14. aboutToAppear() {
15. for (let i = 0; i <= 30; i++) {
16. this.data.push(new StringData(`Hello${i}`));
17. }
18. }

20. build() {
21. List({ space: 3 }) {
22. Repeat(this.data) // Repeat自身具备复用功能
23. .each((repeatItem) => {
24. ListItem() {
25. Text(repeatItem.item.message).fontSize(50)
26. }
27. })
28. .key((item: StringData, index: number) => index.toString())
29. .virtualScroll()
30. }.cachedCount(5)
31. }
32. }
```

**示例7 - 迁移方案2：使用@ReusableV2装饰器**

若要使用@ReusableV2装饰器，首先需要通过.virtualScroll({ reusable: false })关闭Repeat自身的复用功能，再用@ReusableV2装饰需要复用的自定义组件。

相较于Repeat自身的复用，@ReusableV2装饰的自定义组件在回收和复用时，会触发aboutToRecycle和aboutToReuse两个生命周期。

使用@ReusableV2装饰器的迁移示例如下所示。

```
1. class StringData {
2. message: string;

4. constructor(message: string) {
5. this.message = message;
6. }
7. }

9. @Entry
10. @ComponentV2
11. struct MyComponent {
12. @Local data: StringData[] = [];

14. aboutToAppear() {
15. for (let i = 0; i <= 30; i++) {
16. this.data.push(new StringData(`Hello${i}`));
17. }
18. }

20. build() {
21. List({ space: 3 }) {
22. Repeat(this.data)
23. .each((repeatItem) => {
24. ListItem() {
25. ChildComponent({ data: repeatItem.item })
26. .onAppear(() => {
27. console.info(`onAppear: ${repeatItem.item.message}`);
28. })
29. }
30. })
31. .key((item: StringData, index: number) => index.toString())
32. .virtualScroll({ reusable: false }) // 关闭Repeat自身的复用功能（API 19）
33. }.cachedCount(5)
34. }
35. }

37. // 使用@ReusableV2实现组件复用（API 18）
38. @ReusableV2
39. @ComponentV2
40. struct ChildComponent {
41. @Param data: StringData = new StringData('');

43. aboutToAppear(): void {
44. console.info(`aboutToAppear: ${this.data.message}`);
45. }

47. aboutToRecycle(): void {
48. console.info(`aboutToRecycle: ${this.data.message}`);
49. }

51. aboutToReuse(): void {
52. console.info(`aboutToReuse: ${this.data.message}`);
53. }

55. build() {
56. Row() {
57. Text(this.data.message).fontSize(50)
58. }
59. }
60. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/PkuhuktpT6yTb2TPuxAsBQ/zh-cn_image_0000002552797982.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=772ECC060274D1C76D822C1DA1C6B4798CEE4436B68A01163D48BDB39A1A85A2)

### 模板渲染

**LazyForEach示例**

LazyForEach自身并不具备模板渲染能力。为实现模板渲染能力，需要开发者自己实现逻辑判断，为不同的数据项选择不同的渲染模板。

示例8演示了模板渲染的典型场景。

**示例8 - 迁移前**

```
1. /* BasicDataSource代码见文档末尾BasicDataSource示例代码: StringData类型数组的BasicDataSource代码 */

3. class MyDataSource extends BasicDataSource {
4. private dataArray: StringData[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): StringData {
11. return this.dataArray[index];
12. }

14. public pushData(data: StringData): void {
15. this.dataArray.push(data);
16. this.notifyDataAdd(this.dataArray.length - 1);
17. }
18. }

20. class StringData {
21. message: string;
22. type: number;

24. constructor(message: string, type: number) {
25. this.message = message;
26. this.type = type;
27. }

29. getType(): number {
30. if (this.type >= 1) {
31. return 1;
32. } else {
33. return 0;
34. }
35. }
36. }

38. @Entry
39. @Component
40. struct MyComponent {
41. data: MyDataSource = new MyDataSource();

43. aboutToAppear() {
44. for (let i = 0; i <= 200; i++) {
45. this.data.pushData(new StringData(`Hello${i}`, i % 2));
46. }
47. }

49. build() {
50. List({ space: 3 }) {
51. LazyForEach(this.data, (item: StringData, index: number) => {
52. ListItem() {
53. // 开发者自己实现逻辑判断，为不同的数据项选择不同的渲染模板
54. if (item.getType() == 0) {
55. // 模板A
56. ChildComponentA({ data: item })
57. .onAppear(() => {
58. console.info(`type A onAppear: ${item.message}`);
59. })
60. } else {
61. // 模板B
62. ChildComponentB({ data: item })
63. .onAppear(() => {
64. console.info(`type B onAppear: ${item.message}`);
65. })
66. }
67. }
68. }, (item: StringData, index: number) => index.toString())
69. }.cachedCount(5)
70. }
71. }

73. // 使用@Reusable实现组件复用
74. @Reusable
75. @Component
76. struct ChildComponentA {
77. @State data: StringData = new StringData('', 0);

79. aboutToAppear(): void {
80. console.info(`type A aboutToAppear: ${this.data.message}`);
81. }

83. aboutToRecycle(): void {
84. console.info(`type A aboutToRecycle: ${this.data.message}`);
85. }

87. aboutToReuse(params: Record<string, ESObject>): void {
88. this.data = params.data as StringData;
89. console.info(`type A aboutToReuse: ${this.data.message}`);
90. }

92. build() {
93. Row() {
94. Text(this.data.message).fontSize(50)
95. Button('Type A')
96. }
97. }
98. }

100. @Reusable
101. @Component
102. struct ChildComponentB {
103. @State data: StringData = new StringData('', 0);

105. aboutToAppear(): void {
106. console.info(`type B aboutToAppear: ${this.data.message}`);
107. }

109. aboutToRecycle(): void {
110. console.info(`type B aboutToRecycle: ${this.data.message}`);
111. }

113. aboutToReuse(params: Record<string, ESObject>): void {
114. this.data = params.data as StringData;
115. console.info(`type B aboutToReuse: ${this.data.message}`);
116. }

118. build() {
119. Row() {
120. Text(this.data.message).fontSize(50).fontColor(Color.Gray)
121. Text('Type B')
122. }
123. }
124. }
```

**迁移Repeat**

Repeat本身具备模板渲染能力，开发者可以通过[templateId](../harmonyos-references/ts-rendering-control-repeat.md#templateid)方法为不同的数据项选择不同的模板，再通过[template](../harmonyos-references/ts-rendering-control-repeat.md#template)方法为不同的模板配置不同的组件生成函数。同时，开发者仍然可以选择自己实现逻辑判断，为不同的数据项分配不同的模板。

需要注意的是，如果开发者选择自己实现模板渲染，则需要关闭Repeat自身的复用功能。否则，Repeat在复用子组件时无法选择正确的模板，会导致渲染异常。

**示例8 - 迁移方案1：使用Repeat自身的模板渲染能力**

```
1. class StringData {
2. message: string;
3. type: number;

5. constructor(message: string, type: number) {
6. this.message = message;
7. this.type = type;
8. }

10. getType(): number {
11. if (this.type >= 1) {
12. return 1;
13. } else {
14. return 0;
15. }
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct MyComponent {
22. data: StringData[] = [];

24. aboutToAppear() {
25. for (let i = 0; i <= 200; i++) {
26. this.data.push(new StringData(`Hello${i}`, i % 2));
27. }
28. }

30. build() {
31. List({ space: 3 }) {
32. Repeat(this.data)
33. .each((repeatItem) => {
34. ListItem() {
35. Text('Default item')
36. }
37. })
38. .template('A', (repeatItem) => { // 模板A
39. ListItem() {
40. Row() {
41. Text(repeatItem.item.message).fontSize(50)
42. Button('Type A')
43. }
44. }
45. })
46. .template('B', (repeatItem) => { // 模板B
47. ListItem() {
48. Row() {
49. Text(repeatItem.item.message).fontSize(50).fontColor(Color.Gray)
50. Text('Type B')
51. }
52. }
53. })
54. .templateId((item: StringData) => { // 为不同的数据项选择不同的模板
55. if (item.getType() == 0) {
56. return 'A';
57. } else {
58. return 'B';
59. }
60. })
61. .key((item: StringData, index: number) => index.toString())
62. .virtualScroll()
63. }.cachedCount(5)
64. }
65. }
```

**示例8 - 迁移方案2：由开发者实现模板渲染能力**

```
1. class StringData {
2. message: string;
3. type: number;

5. constructor(message: string, type: number) {
6. this.message = message;
7. this.type = type;
8. }

10. getType(): number {
11. if (this.type >= 1) {
12. return 1;
13. } else {
14. return 0;
15. }
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct MyComponent {
22. data: StringData[] = [];

24. aboutToAppear() {
25. for (let i = 0; i <= 200; i++) {
26. this.data.push(new StringData(`Hello${i}`, i % 2));
27. }
28. }

30. build() {
31. List({ space: 3 }) {
32. Repeat(this.data)
33. .each((repeatItem) => {
34. ListItem() {
35. // 开发者自己实现逻辑判断，为不同的数据项选择不同的渲染模板
36. if (repeatItem.item.getType() == 0) {
37. ChildComponentA({ data: repeatItem.item }) // 模板A
38. .onAppear(() => {
39. console.info(`type A onAppear: ${repeatItem.item.message}`);
40. })
41. } else {
42. ChildComponentB({ data: repeatItem.item }) // 模板B
43. .onAppear(() => {
44. console.info(`type B onAppear: ${repeatItem.item.message}`);
45. })
46. }
47. }
48. })
49. .key((item: StringData, index: number) => index.toString())
50. .virtualScroll({ reusable: false }) // 关闭Repeat自身的复用功能（API 19），避免渲染异常
51. }.cachedCount(5)
52. }
53. }

55. // 使用@ReusableV2实现组件复用（API version 18开始支持使用）
56. @ReusableV2
57. @ComponentV2
58. struct ChildComponentA {
59. @Param data: StringData = new StringData('', 0);

61. aboutToAppear(): void {
62. console.info(`type A aboutToAppear: ${this.data.message}`);
63. }

65. aboutToRecycle(): void {
66. console.info(`type A aboutToRecycle: ${this.data.message}`);
67. }

69. aboutToReuse(): void {
70. console.info(`type A aboutToReuse: ${this.data.message}`);
71. }

73. build() {
74. Row() {
75. Text(this.data.message).fontSize(50)
76. Button('Type A')
77. }
78. }
79. }

81. @ReusableV2
82. @ComponentV2
83. struct ChildComponentB {
84. @Param data: StringData = new StringData('', 0);

86. aboutToAppear(): void {
87. console.info(`type B aboutToAppear: ${this.data.message}`);
88. }

90. aboutToRecycle(): void {
91. console.info(`type B aboutToRecycle: ${this.data.message}`);
92. }

94. aboutToReuse(): void {
95. console.info(`type B aboutToReuse: ${this.data.message}`);
96. }

98. build() {
99. Row() {
100. Text(this.data.message).fontSize(50).fontColor(Color.Gray)
101. Text('Type B')
102. }
103. }
104. }
```

运行后界面如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/60a0a9-BQ8SGA3jN8XVm9Q/zh-cn_image_0000002583437677.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=92CEDE11AF3B8E065502BE7648FD61B759398FBFDBE97609CE976C2E1BC61067)

## BasicDataSource示例代码

### string类型数组的BasicDataSource代码

```
1. // BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
2. class BasicDataSource implements IDataSource {
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
17. console.info('add listener');
18. this.listeners.push(listener);
19. }
20. }

22. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
23. unregisterDataChangeListener(listener: DataChangeListener): void {
24. const pos = this.listeners.indexOf(listener);
25. if (pos >= 0) {
26. console.info('remove listener');
27. this.listeners.splice(pos, 1);
28. }
29. }

31. // 通知LazyForEach组件需要重载所有子组件
32. notifyDataReload(): void {
33. this.listeners.forEach(listener => {
34. listener.onDataReloaded();
35. });
36. }

38. // 通知LazyForEach组件需要在index对应索引处添加子组件
39. notifyDataAdd(index: number): void {
40. this.listeners.forEach(listener => {
41. listener.onDataAdd(index);
42. // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
43. });
44. }

46. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
47. notifyDataChange(index: number): void {
48. this.listeners.forEach(listener => {
49. listener.onDataChange(index);
50. // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
51. });
52. }

54. // 通知LazyForEach组件需要在index对应索引处删除该子组件
55. notifyDataDelete(index: number): void {
56. this.listeners.forEach(listener => {
57. listener.onDataDelete(index);
58. // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
59. });
60. }

62. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
63. notifyDataMove(from: number, to: number): void {
64. this.listeners.forEach(listener => {
65. listener.onDataMove(from, to);
66. // 写法2：listener.onDatasetChange(
67. // [{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
68. });
69. }

71. notifyDatasetChange(operations: DataOperation[]): void {
72. this.listeners.forEach(listener => {
73. listener.onDatasetChange(operations);
74. });
75. }
76. }
```

### StringData类型数组的BasicDataSource代码

```
1. class BasicDataSource implements IDataSource {
2. private listeners: DataChangeListener[] = [];
3. private originDataArray: StringData[] = [];

5. public totalCount(): number {
6. return this.originDataArray.length;
7. }

9. public getData(index: number): StringData {
10. return this.originDataArray[index];
11. }

13. registerDataChangeListener(listener: DataChangeListener): void {
14. if (this.listeners.indexOf(listener) < 0) {
15. console.info('add listener');
16. this.listeners.push(listener);
17. }
18. }

20. unregisterDataChangeListener(listener: DataChangeListener): void {
21. const pos = this.listeners.indexOf(listener);
22. if (pos >= 0) {
23. console.info('remove listener');
24. this.listeners.splice(pos, 1);
25. }
26. }

28. notifyDataReload(): void {
29. this.listeners.forEach(listener => {
30. listener.onDataReloaded();
31. });
32. }

34. notifyDataAdd(index: number): void {
35. this.listeners.forEach(listener => {
36. listener.onDataAdd(index);
37. });
38. }

40. notifyDataChange(index: number): void {
41. this.listeners.forEach(listener => {
42. listener.onDataChange(index);
43. });
44. }

46. notifyDataDelete(index: number): void {
47. this.listeners.forEach(listener => {
48. listener.onDataDelete(index);
49. });
50. }

52. notifyDataMove(from: number, to: number): void {
53. this.listeners.forEach(listener => {
54. listener.onDataMove(from, to);
55. });
56. }

58. notifyDatasetChange(operations: DataOperation[]): void {
59. this.listeners.forEach(listener => {
60. listener.onDatasetChange(operations);
61. });
62. }
63. }
```
