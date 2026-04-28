---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-reusable
title: 组件复用迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > 组件复用迁移
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91eaa9baf308f09a90365d3e9855977e744677ddd2cb8235f5eaa5e927477ac8
---

本文档主要介绍组件复用从V1向V2的迁移，涉及如下装饰器。

| V1装饰器名称 | V2装饰器名称 |
| --- | --- |
| [@Reusable](arkts-reusable.md) | [@ReusableV2](arkts-new-reusablev2.md) |

## @Reusable->@ReusableV2迁移规则

### V1->V2组件迁移

**迁移规则**

* 将@Component装饰的父自定义组件迁移至@ComponentV2装饰。
* 将@Reusable装饰的子自定义组件迁移为@ReusableV2装饰。
* 涉及组件内状态变量的迁移可参考[组件内状态变量迁移指导](arkts-v1-v2-migration-inner-component.md)。

### aboutToRecycle与aboutToReuse迁移

**迁移规则**

* [aboutToRecycle](../harmonyos-references/ts-custom-component-lifecycle.md#abouttorecycle10)生命周期无需改动，可保留原实现。
* [aboutToReuse](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoreuse18)生命周期在组件复用V2中进行了优化，去除了参数的同时，在复用前会自动重置各状态变量（详情参考[复用前的组件内状态变量重置](arkts-new-reusablev2.md#复用前的组件内状态变量重置)），无需开发者在aboutToReuse中手动赋值回初始值。

```
1. // V1原组件
2. @Reusable
3. @Component
4. struct ReusableComponent {
5. // 存在外部传值的可能性，可迁移为@Local或@Param @Once
6. @State val: string = 'Hello World';
7. aboutToRecycle(): void {
8. // 这里可以释放比较占内存的内容或其他非必要资源引用，避免一直占用内存
9. console.info('ReusableComponent aboutToRecycle called');
10. }
11. aboutToReuse(params: ESObject): void {
12. console.info('ReusableComponent aboutToReuse called');
13. this.val = params.val ?? 'Hello World'; // 对@State变量重新赋值
14. }
15. build() {
16. Column() {
17. Text(`val: ${this.val}`)
18. }
19. }
20. }

22. // V2迁移后组件
23. @ReusableV2
24. @ComponentV2
25. struct ReusableV2Component {
26. // 当不存在外部传入值时，可迁移为@Local
27. @Local val: string = 'Hello World';
28. // 当存在外部传入值时，可迁移为@Param @Once
29. @Require @Param @Once param: string;
30. aboutToRecycle(): void {
31. // aboutToRecycle无需改动
32. console.info('ReusableComponent aboutToRecycle called');
33. }
34. aboutToReuse(): void { // aboutToReuse不再有参数
35. // aboutToReuse执行时@Local已重置回'Hello World'，@Param @Once已经重置回外部传入值
36. console.info('ReusableComponent aboutToReuse called');
37. this.val = 'Hello ArkUI'; // 可以在复用阶段修改为其他值
38. this.param = 'Hello ArkUI'; // @Param @Once可本地修改
39. }
40. build() {
41. Column() {
42. Text(`val: ${this.val}`)
43. Text(`param: ${this.param}`)
44. }
45. }
46. }
```

### reuseId->reuse

**迁移规则**

在组件复用V1中，使用[reuseId](../harmonyos-references/ts-universal-attributes-reuse-id.md#reuseid)属性标记组件的复用组。迁移到组件复用V2后，需更换使用[reuse](../harmonyos-references/ts-universal-attributes-reuse.md#reuse)属性。

```
1. // V1原写法
2. ReusableComponent().reuseId('groupA')
3. // V2迁移后写法
4. ReusableV2Component().reuse({reuseId: () => 'groupA'})
```

### 组件冻结

**迁移规则**

组件复用V1中，当开发者打开复用组件的冻结开关freezeWhenInactive时，才会冻结复用池中的组件，详细规则参考[自定义组件冻结功能](arkts-custom-components-freeze.md)。而在组件复用V2中，会自动开启冻结，详细规则参考[复用阶段的冻结](arkts-new-reusablev2.md#复用阶段的冻结)。

### LazyForEach->Repeat

**迁移规则**

组件复用V1中，经常使用LazyForEach配合组件复用实现高性能懒加载。在组件复用V2中，推荐使用[Repeat](arkts-new-rendering-control-repeat.md)替代[LazyForEach](arkts-rendering-control-lazyforeach.md)。Repeat自身能够对组件进行复用，相比LazyForEach具有更简洁的API以及更好的性能。由LazyForEach迁移至Repeat可参考[LazyForEach迁移Repeat](arkts-v1-v2-migration-rendering-control-repeat.md#lazyforeach迁移repeat)。

## @Reusable->@ReusableV2迁移示例

### if使用场景

@Reusable使用示例请参考[动态布局更新](arkts-reusable.md#动态布局更新)。

@ReusableV2的if使用场景示例代码如下：

```
1. @ObservedV2
2. class Message {
3. @Trace value: string | undefined;

5. constructor(value: string) {
6. this.value = value;
7. }
8. }

10. @Entry
11. @ComponentV2
12. struct Index {
13. @Local switch: boolean = true;

15. build() {
16. Column() {
17. Button('Hello')
18. .fontSize(24)
19. .fontWeight(FontWeight.Bold)
20. .onClick(() => {
21. this.switch = !this.switch;
22. })
23. if (this.switch) {
24. // 如果只有一个复用的组件，可以不用设置reuse
25. Child({ message: new Message('Child') })
26. .reuse({ reuseId: () => 'Child' })
27. }
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }

34. @ReusableV2
35. @ComponentV2
36. struct Child {
37. @Require @Param @Once message: Message = new Message('AboutToReuse');

39. aboutToReuse() {
40. // 如无需对状态变量做额外修改，aboutToReuse回调可移除
41. console.info('Recycle====Child==');
42. }

44. build() {
45. Column() {
46. Text(this.message.value)
47. .fontSize(30)
48. .margin(20)
49. }
50. .borderWidth(1)
51. .margin({ top: 10 })
52. .height(100)
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/AeYAEXDbSD6r74_IpN3AMg/zh-cn_image_0000002552797974.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=8F6FEE5084EA97DB730FD8D1A50786B9CAC9F8CB04E12815E43B076D7FBC20EB)

### 列表滚动-Repeat使用场景

@Reusable使用示例请参考[列表滚动配合LazyForEach使用](arkts-reusable.md#列表滚动配合lazyforeach使用)。

@ReusableV2的列表滚动-Repeat使用场景示例代码如下：

```
1. @Entry
2. @ComponentV2
3. struct ReuseV2Demo {
4. private data: string[] = [];

6. aboutToAppear() {
7. for (let i = 1; i < 1000; i++) {
8. this.data.push(i + '');
9. }
10. }

12. build() {
13. Column() {
14. List() {
15. Repeat(this.data)
16. .virtualScroll()
17. .each((ri) => {
18. ListItem() {
19. CardViewV2({ item: ri.item })
20. }
21. })
22. }
23. }
24. }
25. }

27. // 复用组件
28. @ReusableV2
29. @ComponentV2
30. export struct CardViewV2 {
31. // 使用@Param @Once接收外部传入变量并观察变化
32. @Param @Once item: string = '';

34. aboutToReuse(): void {
35. // Repeat自身能够进行复用，不会走到自定义组件复用的生命周期
36. }

38. build() {
39. Column() {
40. Text(this.item)
41. .fontSize(30)
42. }
43. .borderWidth(1)
44. .height(100)
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/N8WvhCEfR827NGDNcOLr-g/zh-cn_image_0000002583437669.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=F2F28626851A089B9336C6622E00DF27808B3015F2DBE241337BB1D5CB9F89E0)

### 列表滚动-if使用场景

@Reusable使用示例请参考[列表滚动-if使用场景](arkts-reusable.md#列表滚动-if使用场景)。

@ReusableV2的列表滚动-if使用场景示例代码如下：

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. private dataSource: FriendMoment[] = new Array<FriendMoment>();

6. aboutToAppear(): void {
7. for (let i = 0; i < 20; i++) {
8. let title = i + 1 + 'test_if';
9. // 开发者可自行替换显示图片的内容，此处以app.media.startIcon为例
10. this.dataSource.push(new FriendMoment(i.toString(), title, 'app.media.startIcon'));
11. }

13. for (let i = 0; i < 50; i++) {
14. let title = i + 1 + 'test_if';
15. this.dataSource.push(new FriendMoment(i.toString(), title, ''));
16. }
17. }

19. build() {
20. Column() {
21. List({ space: 3 }) {
22. Repeat(this.dataSource)
23. .virtualScroll()
24. .each((ri) => {
25. ListItem() {
26. if (ri.item.image) {
27. OneMoment({ moment: ri.item })
28. .reuse({ reuseId: () => 'withImage' })
29. } else {
30. OneMoment({ moment: ri.item })
31. .reuse({ reuseId: () => 'noImage' })
32. }
33. }
34. })
35. }
36. .cachedCount(0)
37. }
38. }
39. }

41. @ObservedV2
42. class FriendMoment {
43. @Trace id: string = '';
44. @Trace text: string = '';
45. @Trace title: string = '';
46. @Trace image: string = '';
47. @Trace answers: Array<ResourceStr> = [];

49. constructor(id: string, title: string, image: string) {
50. this.text = id;
51. this.title = title;
52. this.image = image;
53. }
54. }

56. @ReusableV2
57. @ComponentV2
58. export struct OneMoment {
59. @Require @Param moment: FriendMoment;

61. // 复用id相同的组件才能触发复用
62. aboutToReuse(): void {
63. // 如无需对状态变量做额外修改，aboutToReuse回调可移除
64. console.info(`=====aboutToReuse====OneMoment==复用了==${this.moment.text}`);
65. }

67. build() {
68. Column() {
69. Text(this.moment.text)
70. // if分支判断。
71. if (this.moment.image !== '') {
72. Flex({ wrap: FlexWrap.Wrap }) {
73. Image($r(this.moment.image)).height(50).width(50)
74. Image($r(this.moment.image)).height(50).width(50)
75. Image($r(this.moment.image)).height(50).width(50)
76. Image($r(this.moment.image)).height(50).width(50)
77. }
78. }
79. }
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/SErYjBPXRzmh1yMiP8iQ0Q/zh-cn_image_0000002552957624.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=191C276AC746AA189FB33BD123D7EC0C32E9B0C423CEEC613F4AF41433AF4785)

### 列表滚动-Repeat全量加载使用场景

状态管理V2推荐使用[Repeat全量加载模式](arkts-new-rendering-control-repeat.md#懒加载能力说明)替代[ForEach](arkts-rendering-control-foreach.md)实现循环渲染。

@Reusable使用示例请参考[列表滚动-ForEach使用场景](arkts-reusable.md#列表滚动-foreach使用场景)。

@ReusableV2的列表滚动-Repeat全量加载使用场景示例代码如下：

```
1. // xxx.ets
2. @Entry
3. @ComponentV2
4. struct Index {
5. @Local isShow: boolean = true;
6. @Local dataSource: ListItemObject[] = [];

8. build() {
9. Column() {
10. Row() {
11. Button('clear').onClick(() => {
12. for (let i = 1; i < 50; i++) {
13. this.dataSource.pop();
14. }
15. }).height(40)

17. Button('update').onClick(() => {
18. for (let i = 1; i < 50; i++) {
19. let obj = new ListItemObject();
20. obj.id = i;
21. obj.uuid = Math.random().toString();
22. obj.isExpand = false;
23. this.dataSource.push(obj);
24. }
25. }).height(40)
26. }

28. List({ space: 10 }) {
29. Repeat(this.dataSource)
30. .each((ri) => {
31. ListItem() {
32. ListItemView({
33. obj: ri.item
34. })
35. }
36. })
37. }.cachedCount(0)
38. .width('100%')
39. .height('100%')
40. }
41. }
42. }

44. @ReusableV2
45. @ComponentV2
46. struct ListItemView {
47. @Require @Param obj: ListItemObject;

49. aboutToAppear(): void {
50. // 点击 update，首次进入，上下滑动，由于ForEach全展开属性，无法复用
51. console.info('=====aboutToAppear=====ListItemView==创建了==');
52. }

54. aboutToReuse() {
55. // 点击clear，再次update，复用成功
56. // 符合一帧内重复创建多个已被销毁的自定义组件
57. // 如无需对状态变量做额外修改，aboutToReuse回调可移除
58. console.info('=====aboutToReuse====ListItemView==复用了==');
59. }

61. build() {
62. Column({ space: 10 }) {
63. Text(`${this.obj.id}.标题`)
64. .fontSize(16)
65. .fontColor('#000000')
66. .padding({
67. top: 20,
68. bottom: 20,
69. })

71. if (this.obj.isExpand) {
72. Text('expand')
73. .fontSize(14)
74. .fontColor('#999999')
75. }
76. }
77. .width('100%')
78. .borderRadius(10)
79. .backgroundColor(Color.White)
80. .padding(15)
81. .onClick(() => {
82. this.obj.isExpand = !this.obj.isExpand;
83. })
84. }
85. }

87. @ObservedV2
88. class ListItemObject {
89. @Trace uuid: string = '';
90. @Trace id: number = 0;
91. @Trace isExpand: boolean = false;
92. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/hPEjcYclR3WFbZwG_vMPSg/zh-cn_image_0000002583477625.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=13D73D9006EA88B898F009624CE007A598D70D19A44F7180E8D945A663A7ADDB)

### Grid使用场景

@Reusable使用示例请参考[Grid使用场景](arkts-reusable.md#grid使用场景)。

@ReusableV2的Grid使用场景示例代码如下：

```
1. @Entry
2. @ComponentV2
3. struct MyComponent {
4. // 数据源。
5. @Local data: number[] = [];

7. aboutToAppear() {
8. for (let i = 1; i < 1000; i++) {
9. this.data.push(i);
10. }
11. }

13. build() {
14. Column({ space: 5 }) {
15. Grid() {
16. Repeat(this.data)
17. .virtualScroll()
18. .each((ri) => {
19. GridItem() {
20. ReusableV2ChildComponent({ item: ri.item })
21. }
22. })
23. }
24. .cachedCount(2) // 设置GridItem的缓存数量。
25. .columnsTemplate('1fr 1fr 1fr')
26. .columnsGap(10)
27. .rowsGap(10)
28. .margin(10)
29. .height(500)
30. .backgroundColor(0xFAEEE0)
31. }
32. }
33. }

35. @ReusableV2
36. @ComponentV2
37. struct ReusableV2ChildComponent {
38. @Param item: number = 0;

40. aboutToAppear() {
41. }

43. build() {
44. Column() {
45. // 开发者可自行替换显示图片的内容，此处以app.media.startIcon为例
46. Image($r('app.media.startIcon'))
47. .objectFit(ImageFit.Fill)
48. .layoutWeight(1)
49. Text(`图片${this.item}`)
50. .fontSize(16)
51. .textAlign(TextAlign.Center)
52. }
53. .width('100%')
54. .height(120)
55. .backgroundColor(0xF9CF93)
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/NXOnK4X8RzqM4_EtPqgRLg/zh-cn_image_0000002552797976.png?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=163FC1A8F02169E80CF647B0735527B725B4BC74308DA3164125F3B52819B589)

### WaterFlow使用场景

@Reusable使用示例请参考[WaterFlow使用场景](arkts-reusable.md#waterflow使用场景)。

@ReusableV2的WaterFlow使用场景示例代码如下：

```
1. @ReusableV2
2. @ComponentV2
3. struct ReusableV2FlowItem {
4. @Param item: number = 0;

6. build() {
7. Column() {
8. Text('N' + this.item).fontSize(24).height(26).margin(10)
9. // 开发者可自行替换显示图片的内容，此处以app.media.startIcon为例
10. Image($r('app.media.startIcon'))
11. .objectFit(ImageFit.Cover)
12. .width(50)
13. .height(50)
14. }
15. }
16. }

18. @Entry
19. @ComponentV2
20. struct Index {
21. @Local minSize: number = 50;
22. @Local maxSize: number = 80;
23. @Local fontSize: number = 24;
24. @Local colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
25. scroller: Scroller = new Scroller();
26. @Local dataSource: number[] = [];
27. private itemWidthArray: number[] = [];
28. private itemHeightArray: number[] = [];

30. // 计算flow item宽/高。
31. getSize() {
32. let ret = Math.floor(Math.random() * this.maxSize);
33. return (ret > this.minSize ? ret : this.minSize);
34. }

36. // 保存flow item宽/高。
37. getItemSizeArray() {
38. for (let i = 0; i < 100; i++) {
39. this.itemWidthArray.push(this.getSize());
40. this.itemHeightArray.push(this.getSize());
41. }
42. }

44. aboutToAppear() {
45. for (let i = 0; i <= 60; i++) {
46. this.dataSource.push(i);
47. }
48. this.getItemSizeArray();
49. }

51. build() {
52. Stack({ alignContent: Alignment.TopStart }) {
53. Column({ space: 2 }) {
54. Button('back top')
55. .height('5%')
56. .onClick(() => {
57. // 点击后回到顶部。
58. this.scroller.scrollEdge(Edge.Top);
59. })
60. WaterFlow({ scroller: this.scroller }) {
61. Repeat(this.dataSource)
62. .virtualScroll()
63. .each((ri) => {
64. FlowItem() {
65. ReusableV2FlowItem({ item: ri.item })
66. }.onAppear(() => {
67. if (ri.item + 20 == this.dataSource.length) {
68. for (let i = 0; i < 50; i++) {
69. this.dataSource.splice(this.dataSource.length, 0, this.dataSource.length);
70. }
71. }
72. })
73. })
74. }.margin({ left: 160, top: 10 })
75. }
76. }
77. }
78. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/DBsjRxjBQXyBloDXJUhSsA/zh-cn_image_0000002583437671.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=08BC5215532F0E411903680679D2586CBF37925F77E2FCD409ABAA10A3A28217)

### Swiper使用场景

@Reusable使用示例请参考[Swiper使用场景](arkts-reusable.md#swiper使用场景)。

@ReusableV2的Swiper使用场景示例代码如下：

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. private dataSource: Question[] = new Array<Question>();

6. aboutToAppear(): void {
7. for (let i = 0; i < 1000; i++) {
8. let title = i + 1 + 'test_swiper';
9. let answers = ['test1', 'test2', 'test3', 'test4'];
10. // 开发者可自行替换显示图片的内容，此处以app.media.startIcon为例
11. this.dataSource.push(new Question(i.toString(), title, $r('app.media.startIcon'), answers));
12. }
13. }

15. build() {
16. Column({ space: 5 }) {
17. Swiper() {
18. Repeat(this.dataSource)
19. .virtualScroll()
20. .each((ri) => {
21. QuestionSwiperItem({ itemData: ri.item })
22. })
23. }
24. }
25. .width('100%')
26. .margin({ top: 5 })
27. }
28. }

30. @ObservedV2
31. class Question {
32. @Trace id: string = '';
33. @Trace title: ResourceStr = '';
34. @Trace image: ResourceStr = '';
35. @Trace answers: Array<ResourceStr> = [];

37. constructor(id: string, title: ResourceStr, image: ResourceStr, answers: Array<ResourceStr>) {
38. this.id = id;
39. this.title = title;
40. this.image = image;
41. this.answers = answers;
42. }
43. }

45. @ReusableV2
46. @ComponentV2
47. struct QuestionSwiperItem {
48. @Param itemData: Question | null = null;

50. build() {
51. Column() {
52. Text(this.itemData?.title)
53. .fontSize(18)
54. .fontColor($r('sys.color.ohos_id_color_primary'))
55. .alignSelf(ItemAlign.Start)
56. .margin({
57. top: 10,
58. bottom: 16
59. })
60. Image(this.itemData?.image)
61. .width('100%')
62. .borderRadius(12)
63. .objectFit(ImageFit.Contain)
64. .margin({
65. bottom: 16
66. })
67. .height(80)
68. .width(80)

70. Column({ space: 16 }) {
71. Repeat(this.itemData?.answers)
72. .each((ri) => {
73. Text(ri.item)
74. .fontSize(16)
75. .fontColor($r('sys.color.ohos_id_color_primary'))
76. })
77. }
78. .width('100%')
79. .alignItems(HorizontalAlign.Start)
80. }
81. .width('100%')
82. .padding({
83. left: 16,
84. right: 16
85. })
86. }
87. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/hKrmugSuQROtkMkYeVZeVg/zh-cn_image_0000002552957626.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=BF6245CE067AFB0C2CAB15B02FEB4CD78B3FFDA78366A56B07AD17C4809860C8)

### 列表滚动-ListItemGroup使用场景

@Reusable使用示例请参考[列表滚动-ListItemGroup使用场景](arkts-reusable.md#列表滚动-listitemgroup使用场景)。

@ReusableV2的列表滚动-ListItemGroup使用场景示例代码如下：

```
1. @Entry
2. @ComponentV2
3. struct ListItemGroupAndReusable {
4. dataSource: DataSrc[] = new Array<DataSrc>();

6. @Builder
7. itemHead(text: string) {
8. Text(text)
9. .fontSize(20)
10. .backgroundColor(0xff519db4)
11. .width('100%')
12. .padding(10)
13. }

15. aboutToAppear() {
16. for (let i = 0; i < 10000; i++) {
17. let data = new DataSrc();
18. for (let j = 0; j < 12; j++) {
19. data.dataScr1.push(`测试条目数据: ${i} - ${j}`);
20. }
21. this.dataSource.push(data);
22. }
23. }

25. build() {
26. Stack() {
27. List() {
28. Repeat(this.dataSource)
29. .virtualScroll()
30. .each((ri) => {
31. ListItemGroup({ header: this.itemHead(ri.index.toString()) }) {
32. Repeat(ri.item.dataScr1)
33. .virtualScroll()
34. .each((ri) => {
35. ListItem() {
36. Inner({ str: ri.item })
37. }
38. })
39. }
40. })
41. }
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }

48. @ReusableV2
49. @ComponentV2
50. struct Inner {
51. @Param str: string = '';

53. build() {
54. Text(this.str)
55. }
56. }

58. @ObservedV2
59. class DataSrc {
60. @Trace dataScr1: string[] = [];
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/2A0zXGOBRly9ekGWsTqsIA/zh-cn_image_0000002583477627.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=C8469A564B92FA3006A1DA2FD7EFBBFF42CAAEB50A95DEC1C1253FED2292BC1B)

### 多种条目类型使用场景

@Reusable使用示例请参考[多种条目类型使用场景](arkts-reusable.md#多种条目类型使用场景)。

@ReusableV2的多种条目类型使用场景示例代码如下：

**标准型**

复用组件的布局相同，示例参见本文列表滚动部分用例。

**有限变化型**

复用组件间存在差异，但类型有限。例如，可以通过显式设置两个reuse选项或使用两个自定义组件来实现复用。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. private data: number[] = [];

6. aboutToAppear() {
7. for (let i = 0; i < 1000; i++) {
8. this.data.push(i);
9. }
10. }

12. build() {
13. Column() {
14. List({ space: 10 }) {
15. Repeat(this.data)
16. .virtualScroll()
17. .each((ri) => {
18. ListItem() {
19. if (ri.item % 2 === 0 ) {
20. ReusableV2Component({ item: ri.item }).reuse({reuseId: () => 'ReusableV2ComponentOne'})
21. } else {
22. ReusableV2Component({ item: ri.item }).reuse({reuseId: () => 'ReusableV2ComponentTwo'})
23. }
24. }
25. })
26. }
27. .cachedCount(2)
28. }
29. }
30. }

32. @ReusableV2
33. @ComponentV2
34. struct ReusableV2Component {
35. @Param item: number = 0;

37. aboutToReuse() {
38. // 如无需对状态变量做额外修改，aboutToReuse回调可移除
39. console.info(`ReusableComponent aboutToReuse called${this.item}`)
40. }

42. build() {
43. Column() {
44. // 组件内部根据类型差异渲染
45. if (this.item % 2 === 0) {
46. Text(`Item ${this.item} ReusableComponentOne`)
47. .fontSize(20)
48. .margin({ left: 10 })
49. } else {
50. Text(`Item ${this.item} ReusableComponentTwo`)
51. .fontSize(20)
52. .margin({ left: 10 })
53. }
54. }.margin({ left: 10, right: 10 })
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/6tjfYZP6SriRUNriGAW5CQ/zh-cn_image_0000002552797978.png?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=28C61BC159D31B302C666833DD0E0AD59ACF7E9B9EAB493872F2D28E04F7B788)

**组合型**

复用组件间存在多种差异，但通常具备共同的子组件。将三种复用组件以组合型方式转换为[@Builder](arkts-builder.md)函数后，内部的共享子组件将统一置于父组件MyComponentV2之下。复用这些子组件时，缓存池在父组件层面实现共享，减少组件创建过程中的资源消耗。

```
1. @Entry
2. @ComponentV2
3. struct MyComponentV2 {
4. private data: string[] = [];

6. aboutToAppear() {
7. for (let i = 0; i < 1000; i++) {
8. this.data.push(i.toString());
9. }
10. }

12. // itemBuilderOne作为复用组件的写法未展示，以下为转为Builder之后的写法。
13. @Builder
14. itemBuilderOne(item: string) {
15. Column() {
16. ChildComponentA({ item: item })
17. ChildComponentB({ item: item })
18. ChildComponentC({ item: item })
19. }
20. }

22. // itemBuilderTwo转为Builder之后的写法。
23. @Builder
24. itemBuilderTwo(item: string) {
25. Column() {
26. ChildComponentA({ item: item })
27. ChildComponentC({ item: item })
28. ChildComponentD({ item: item })
29. }
30. }

32. // itemBuilderThree转为Builder之后的写法。
33. @Builder
34. itemBuilderThree(item: string) {
35. Column() {
36. ChildComponentA({ item: item })
37. ChildComponentB({ item: item })
38. ChildComponentD({ item: item })
39. }
40. }

42. build() {
43. List({ space: 40 }) {
44. Repeat(this.data)
45. .virtualScroll()
46. .each((ri) => {
47. ListItem() {
48. if (ri.index % 3 === 0) {
49. this.itemBuilderOne(ri.item)
50. } else if (ri.index % 5 === 0) {
51. this.itemBuilderTwo(ri.item)
52. } else {
53. this.itemBuilderThree(ri.item)
54. }
55. }
56. })
57. }
58. .width('100%')
59. .height('100%')
60. .cachedCount(0)
61. }
62. }

64. @ReusableV2
65. @ComponentV2
66. struct ChildComponentA {
67. @Param item: string = '';

69. aboutToReuse() {
70. // 如无需对状态变量做额外修改，aboutToReuse回调可移除
71. console.info(`ChildComponentA Reuse ${this.item}`);
72. }

74. aboutToRecycle(): void {
75. console.info(`ChildComponentA ${this.item} Recycle`);
76. }

78. build() {
79. Column() {
80. Text(`Item ${this.item} Child Component A`)
81. .fontSize(20)
82. .margin({ left: 10 })
83. .fontColor(Color.Blue)
84. Grid() {
85. ForEach((new Array(20)).fill(''), (item: string, index: number) => {
86. GridItem() {
87. // 开发者可自行替换显示图片的内容，此处以app.media.startIcon为例
88. Image($r('app.media.startIcon'))
89. .height(20)
90. }
91. })
92. }
93. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
94. .rowsTemplate('1fr 1fr 1fr 1fr')
95. .columnsGap(10)
96. .width('90%')
97. .height(160)
98. }
99. .margin({ left: 10, right: 10 })
100. .backgroundColor(0xFAEEE0)
101. }
102. }

104. @ReusableV2
105. @ComponentV2
106. struct ChildComponentB {
107. @Param item: string = '';

109. build() {
110. Row() {
111. Text(`Item ${this.item} Child Component B`)
112. .fontSize(20)
113. .margin({ left: 10 })
114. .fontColor(Color.Red)
115. }.margin({ left: 10, right: 10 })
116. }
117. }

119. @ReusableV2
120. @ComponentV2
121. struct ChildComponentC {
122. @Param item: string = '';

124. build() {
125. Row() {
126. Text(`Item ${this.item} Child Component C`)
127. .fontSize(20)
128. .margin({ left: 10 })
129. .fontColor(Color.Green)
130. }.margin({ left: 10, right: 10 })
131. }
132. }

134. @ReusableV2
135. @ComponentV2
136. struct ChildComponentD {
137. @Param item: string = '';

139. build() {
140. Row() {
141. Text(`Item ${this.item} Child Component D`)
142. .fontSize(20)
143. .margin({ left: 10 })
144. .fontColor(Color.Orange)
145. }.margin({ left: 10, right: 10 })
146. }
147. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/BDZHwTScS4GSeBr-pp3tOQ/zh-cn_image_0000002583437673.png?HW-CC-KV=V1&HW-CC-Date=20260427T233915Z&HW-CC-Expire=86400&HW-CC-Sign=EAE689A525B1D5B7F45195FAFAF445FFA9C739D1917C80A6DF46DE3C0175CAF5)
