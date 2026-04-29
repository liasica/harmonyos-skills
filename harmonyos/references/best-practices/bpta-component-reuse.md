---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-reuse
title: 组件复用
breadcrumb: 最佳实践 > 组件封装与复用 > 组件复用
category: best-practices
scraped_at: 2026-04-29T14:10:18+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:0831f7764936514d92944107dc8cd1da7bfc9143ef7f4d71bd0adf5fa49cd207
---

## 概述

组件复用是指自定义组件从组件树上移除后被放入缓存池，后续在创建相同类型的组件节点时，直接复用缓存池中的组件对象。

在应用开发时，组件复用是优化UI性能，确保应用流畅的重要手段。合理使用可复用组件，一方面，可以避免频繁创建和销毁对象的过程，减少内存回收的频率；另一方面，复用缓存中的组件可以直接绑定数据进行显示，与创建新视图相比，降低了计算开销，提升了显示效率。

常见的组件复用开发场景是长列表滑动：在应用展示大量数据的列表界面中，当用户快速地进行滑动操作，列表项反复创建销毁可能导致卡顿等性能问题。这种情况下，使用组件复用机制可以重用已经创建过的列表项视图，提高滑动的流畅度。

本文介绍以下组件复用开发场景，帮助开发者更好地理解复用机制，进而优化应用性能。

* [同一列表内的组件复用](bpta-component-reuse.md#section142674274329)
* [多个列表间的组件复用](bpta-component-reuse.md#section1032053073217)

说明

本文以列表相关场景为例介绍，但实际只要发生了自定义组件的销毁和再创建，都可以考虑使用组件复用。包括以下情形：

1. 滑动场景下对子组件进行频繁创建和销毁。例如List、Grid、WaterFlow、Swiper等布局容器中的滑动。
2. 界面中反复切换条件渲染的控制分支，且控制分支中的子组件树结构比较复杂。

## 场景：同一列表内的组件复用

### 场景描述

同一列表内的列表项组件复用是典型的应用开发场景。列表在滑动时，超出屏幕一定范围的列表项，被放入缓存池中，当新的列表项滑动进入屏幕范围内时，从缓存池中取出对象，绑定对应数据后呈现到列表界面中。

在实际业务中，同一列表内可能呈现一种或多种不同结构的列表项，可以进一步划分以下子场景：

* [列表项结构类型相同](bpta-component-reuse.md#section182174216314)
* [列表项结构类型不同](bpta-component-reuse.md#section43301824133220)
* [列表项内子组件可拆分组合](bpta-component-reuse.md#section11716134215321)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/FLFn1bwhRA-Af7GQLDK0QQ/zh-cn_image_0000002306983630.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=97C5C18E2F3F59265B113A7CFB5D375EBFEA0729DCC67538EDD6BBE1188EE78C "点击放大")

### 实现原理

ArkUI提供了[@Reusable装饰器](../harmonyos-guides/arkts-reusable.md)以实现自定义组件的复用，其原理如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/r09KAHqzRruqUWthfEF2dg/zh-cn_image_0000002341062601.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=6F9357E572130FCBFC9D5AA24EA73074E794EEF5AB9CAA8E50B6B71C8BADB98A "点击放大")

1. 标记了@Reusable的自定义组件listItem列表项，在滑动出屏幕一定范围后，从组件树上被移除，组件的对象实例被放入CustomNode虚拟结点（与自定义组件一一对应的自定义结点）。
2. 在不断滑动过程中，列表的RecycleManager将这些CustomNode虚拟结点回收，根据复用标识[reuseId](../harmonyos-references/ts-universal-attributes-reuse-id.md)分组，形成CachedRecycleNodes的集合，即视图对象的复用缓存池。
3. 继续滑动，新的listItem需要在列表上显示时，RecycleManager优先从复用缓存池（CachedRecycleNodes集合）中查找对应reuseId的视图对象，然后将新的数据绑定到该视图，重用该节点并添加到组件树上。

### 开发步骤

1. 定义可复用组件：使用@Reusable装饰器修饰可复用的自定义组件。
2. 实现复用回调：可复用组件需要实现aboutToReuse()生命周期回调。当组件从缓存中重新加入到节点树时，触发aboutToReuse()生命周期回调，组件的构造参数会传递进来，开发者根据需要在回调中处理数据刷新。
3. 布局中使用可复用组件：设置reuseId划分组件的复用组别，以区分缓存池。未设置reuseId时，组件名会默认作为reuseId。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // ...

   6. build() {
   7. Column() {
   8. // ...
   9. if (this.switch) {
   10. // 3.layout the component and set reuse id
   11. ReusableComponent({ text: this.typeStr })
   12. .reuseId(this.typeStr)
   13. }
   14. }
   15. // ...
   16. }

   18. // ...
   19. }

   21. // 1.add @Reusable to mark component
   22. @Reusable
   23. @Component
   24. struct ReusableComponent {
   25. @State text: string = ''

   27. // 2.update data in aboutToReuse
   28. aboutToReuse(params: Record<string, Object>): void {
   29. this.text = params.text as string;
   30. }

   32. build() {
   33. // ...
   34. }
   35. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentReuse/entry/src/main/ets/pages/Index.ets#L19-L126)

注意

* @Reusable修饰的组件需要布局在同一个父自定义组件（后文简称”父组件”）下才能实现缓存复用。
* 不建议在@Reusable修饰的组件中嵌套使用另一个@Reusable组件。

更多注意事项参考指南[限制条件](../harmonyos-guides/arkts-reusable.md#限制条件)。

### 列表项结构类型相同

这种场景下，列表中的每一项都是由相同类型的元素和布局构成，列表项组件可以作为复用逻辑的基本单位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/A0x8CRXXRN-Ib_YrKdMg6g/zh-cn_image_0000002321247750.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=F411498FA1CACF9DC667D4DD5CA5F9D4C9567E637F524A455644DE8565F9ECD3 "点击放大")

实现步骤：

1. 将列表项封装为自定义组件ItemView，添加@Reusable修饰。
2. 在ItemView组件内的aboutToReuse()方法中进行新数据绑定逻辑。
3. 在列表的LazyForEach()中使用ItemView组件，设置reuseId。

下面的示例中，ItemView组件添加了@Reusable和aboutToReuse()方法，然后在OneTypeItemPage页面中使用，对ItemView组件设置reuseId('item\_id')，表示此处以item\_id为复用分组id。

```
1. @Component
2. export struct OneTypeItemPage {
3. // ...
4. build() {
5. NavDestination() {
6. Column() {
7. List() {
8. LazyForEach(this.dataSource, (item: ItemData) => {
9. // layout the component, and set reuse id (or no set with using name as default id)
10. ItemView({ title: item.title, from: item.from, tail: item.tail })
11. .reuseId('item_id')
12. }, (item: ItemData) => item.id.toString())
13. }
14. // ...
15. }
16. // ...
17. }
18. // ...
19. }
20. }

22. // add @Reusable to mark component
23. @Reusable
24. @Component
25. struct ItemView {
26. @State title: string | Resource = '';
27. @State from: string | Resource = '';
28. @State tail: string | Resource = '';

30. // update data in aboutToReuse method
31. aboutToReuse(params: Record<string, Object>): void {
32. this.title = params.title as string;
33. this.from = params.from as string;
34. this.tail = params.tail as string;
35. }

37. build() {
38. // ...
39. }
40. }
```

[OneTypeItemPage.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/pages/OneTypeItemPage.ets#L21-L111)

### 列表项结构类型不同

这种场景下，列表中会有多种类型的列表项，如下图包含了文本、单图、多图等三种列表项，其布局、组成元素存在一定差异，可以将每种类型的列表项分别作为复用单位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/3-1DZ6Y-TKu5POnryUmxwg/zh-cn_image_0000002355045581.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=06BB7950BDB2DA0E07F75746D050D42618B04E34A1CDD639F9F6D45ABCC0A7D1 "点击放大")

在滑动的过程中，不同类型的列表项将分别回收进入各自的缓存池，当需要复用时，根据类型找到对应视图缓存进行显示。

实现步骤：

1. 将不同类型的列表项分别封装为自定义组件，添加@Reusable修饰。
2. 在组件内的aboutToReuse()方法中进行新的数据绑定逻辑。
3. 在列表的LazyForEach()中，根据业务逻辑进行if条件选择，布局相应类型的列表项组件，分别设置reuseId。

```
1. @Component
2. export struct MultiTypeItemPage {
3. // ...

5. build() {
6. NavDestination() {
7. Column() {
8. List() {
9. LazyForEach(this.dataSource, (item: ItemData) => {
10. if (item.type === 0) {
11. TextTypeItemView({ item: item })
12. .reuseId('text_item_id')
13. } else if (item.type === 1) {
14. ImageTypeItemView({ item: item })
15. .reuseId('image_item_id')
16. } else if (item.type === 2) {
17. ThreeImageTypeItemView({ item: item })
18. .reuseId('three_image_item_id')
19. }
20. }, (item: ItemData) => item.id.toString())
21. }
22. // ...
23. }
24. // ...
25. }
26. // ...
27. }
28. }

30. @Reusable
31. @Component
32. struct TextTypeItemView {
33. // ...
34. }

37. @Reusable
38. @Component
39. struct ImageTypeItemView {
40. // ...
41. }

43. @Reusable
44. @Component
45. struct ThreeImageTypeItemView {
46. // ...
47. }
```

[MultiTypeItemPage.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/pages/MultiTypeItemPage.ets#L21-L211)

### 列表项内子组件可拆分组合

这种情况下，列表项也具有多种结构类型。通过观察可知，列表项内部子组件都是纵向分布排列，相同之处是顶部的文本标题、底部的发布时间，而不同之处是中间的区域部分：有单图、多图、视频三种情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/ymFqdxQPTFG-ct1r5g8SPA/zh-cn_image_0000002306983638.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=E398642AF55E8C5D320D4512F07B633881F64728D5B711291E487040CE055217 "点击放大")

因此，可以创建五种复用子组件，通过子组件的选择组合，实现不同类型的列表项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/_nQWsI4SRr-eiUZIMRgXmQ/zh-cn_image_0000002341062605.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=FE6BAE8A8E5A2472D1CC3C9477AED7D1FE53C53848E1EEC8616309CA20CEFC03 "点击放大")

实现步骤：

1. 将单图、多图、视频、顶部标题、底部时间等分别封装为子组件，添加@Reusable修饰。
2. 在组件内的aboutToReuse()方法中进行新的数据绑定逻辑。
3. 通过组合子组件，实现三个不同的@Builder函数，与三种列表项一一对应。
4. 在列表的LazyForEach()中，根据业务逻辑进行条件选择，分别调用相应类型的@Builder函数。

说明

为什么使用@Builder实现，而不直接使用自定义组件嵌套子组件？

由于缓存池位于自定义组件上，嵌套子组件后会将缓存池分割，导致复用不生效。而使用@Builder可以使内部的自定义组件依然汇聚在同一个缓存池里，从而实现相互复用。

正例：

itemBuilderSingleImage()函数使用@Builder装饰器实现，ComposableItemPage中调用this.itemBuilderSingleImage(item)布局，itemBuilderSingleImage()内部的自定义组件就会汇聚在ComposableItemPage对应的缓存池里，即TopView、MiddleSingleImageView、BottomView等Reusable组件汇聚在同一缓存池里，当调用ComposableItemPage中其他@Builder函数时，也可复用内部@Reusable装饰的组件。

```
1. @Component
2. export struct ComposableItemPage {
3. // ...

5. @Builder
6. itemBuilderSingleImage(item: ItemData) {
7. TopView({ item: item }).reuseId('top_id')
8. MiddleSingleImageView({ item: item }).reuseId('middle_image_id')
9. BottomView({ item: item }).reuseId('bottom_id')
10. }

12. @Builder
13. itemBuilderThreeImage(item: ItemData) {
14. TopView({ item: item }).reuseId('top_id')
15. MiddleThreeImageView({ item: item }).reuseId('middle_three_image_id')
16. BottomView({ item: item }).reuseId('bottom_id')
17. }

19. @Builder
20. itemBuilderVideoImage(item: ItemData) {
21. TopView({ item: item }).reuseId('top_id')
22. MiddleVideoView({ item: item }).reuseId('middle_video_id')
23. BottomView({ item: item }).reuseId('bottom_id')
24. }

26. build() {
27. NavDestination() {
28. Column() {
29. List() {
30. LazyForEach(this.dataSource, (item: ItemData) => {
31. ListItem() {
32. Column() {
33. if (item.type === 0) {
34. this.itemBuilderSingleImage(item)
35. } else if (item.type === 1) {
36. this.itemBuilderThreeImage(item)
37. } else if (item.type === 2) {
38. this.itemBuilderVideoImage(item)
39. }
40. }
41. // ...
42. }
43. }, (item: ItemData) => item.id.toString())
44. }
45. // ...
46. }
47. // ...
48. }
49. // ...
50. }
51. }

53. @Reusable
54. @Component
55. struct TopView {
56. // ...
57. }

59. @Reusable
60. @Component
61. struct BottomView {
62. // ...
63. }

65. @Reusable
66. @Component
67. struct MiddleSingleImageView {
68. // ...
69. }

71. @Reusable
72. @Component
73. struct MiddleThreeImageView {
74. // ...
75. }

77. @Reusable
78. @Component
79. struct MiddleVideoView {
80. // ...
81. }
```

[ComposableItemPage.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/pages/ComposableItemPage.ets#L21-L207)

反例：

如果将itemBuilderSingleImage()、itemBuilderThreeImage()等@Builder函数改为@Component装饰器实现，比如分别命名为SingleImageComponent、ThreeImageComponent等，这会导致SingleImageComponent内部的TopView、MiddleSingleImageView、BottomView等组件仅汇聚在SingleImageComponent组件对应的缓存池中，ThreeImageComponent内部同理。这些@Reusable组件因处在不同@Component的缓存池中，ComposableItemPage在最后布局绘制时，复用将不生效。

```
1. @Component
2. export struct ComposableItemPage {
3. // ...
4. build() {
5. NavDestination() {
6. Column() {
7. List() {
8. LazyForEach(this.dataSource, (item: ItemData) => {
9. ListItem() {
10. Column() {
11. if (item.type === 0) {
12. SingleImageComponent({ item: item })
13. } else if (item.type === 1) {
14. ThreeImageComponent({ item: item })
15. } else if (item.type === 2) {
16. VideoComponent({ item: item })
17. }
18. }
19. // ...
20. }
21. }, (item: ItemData) => item.id.toString())
22. }
23. // ...
24. }
25. // ...
26. }
27. // ...
28. }
29. }

31. @Component
32. struct SingleImageComponent{
33. // ...
34. build() {
35. Column() {
36. TopView({ item: item }).reuseId('top_id')
37. MiddleSingleImageView({ item: item }).reuseId('middle_image_id')
38. BottomView({ item: item }).reuseId('bottom_id')
39. }
40. }
41. }

43. @Component
44. struct ThreeImageComponent{
45. // ...
46. build() {
47. Column() {
48. TopView({ item: item }).reuseId('top_id')
49. MiddleThreeImageView({ item: item }).reuseId('middle_three_image_id')
50. BottomView({ item: item }).reuseId('bottom_id')
51. }
52. }
53. }

55. @Component
56. struct VideoComponent{
57. // ...
58. build() {
59. Column() {
60. TopView({ item: item }).reuseId('top_id')
61. MiddleVideoView({ item: item }).reuseId('middle_video_id')
62. BottomView({ item: item }).reuseId('bottom_id')
63. }
64. }
65. }

67. @Reusable
68. @Component
69. struct TopView {
70. // ...
71. }

73. @Reusable
74. @Component
75. struct BottomView {
76. // ...
77. }

79. @Reusable
80. @Component
81. struct MiddleSingleImageView {
82. // ...
83. }

85. @Reusable
86. @Component
87. struct MiddleThreeImageView {
88. // ...
89. }

91. @Reusable
92. @Component
93. struct MiddleVideoView {
94. // ...
95. }
```

## 场景：多个列表间的组件复用

### 场景描述

应用开发有这种场景：在不同的标题页面中展示数据，每一页面下实现了一个列表，这样在页面切换时，列表与列表之间如果存在结构相同的列表项，就有组件复用的优化可能。例如下图，News、Hot等页签下，绘制了类型相同的列表项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/64X7k9j9Sn6toYwVWCwVcQ/zh-cn_image_0000002307143354.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=A8BB254075DD71EE7404ADF07C0C99F61E0110FBF289B11202E700D592A871C2 "点击放大")

### 实现原理

在ArkUI中，可以采用Swiper+List实现这种功能场景，其中Swiper中的每个页面都使用一个List列表呈现内容。从@Reusable的复用机制可知，复用缓存池需要在同一父组件中，而列表项Item的父组件是当前页面的列表List，当Swiper内的页面切换时，无法直接复用上一个页面的列表项。

此时可以自定义一个全局的复用缓存池NodePool，利用[BuilderNode](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md)的节点复用能力，根据页面状态创建、回收、复用子组件，实现这种跨页面多个列表间的组件复用。

说明

为什么不使用Tabs+List，而是用Swiper+List组件实现？

当前Tabs内容页不支持使用LazyForEach()，只能使用ForEach+TabContent。如果使用ForEach()，Tabs页面显示时会一次性将所有的TabContent创建，TabContent子页面切换时也不会执行aboutToDisappear()，无法回收组件，进而不存在复用优化的可能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/yg1_5cUTQOSJZkHFRuJb9w/zh-cn_image_0000002340902753.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=1109D7E31FE7FEF3D5716C7ED034FBAF2B1DD0BAF81F688FC466F0CE4AA54844 "点击放大")

在需要布局自定义组件的位置，使用[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)占位，然后继承[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)实现NodeItem结点类，其内部需要持有[BuilderNode](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md)实例以实现结点的创建和复用，同时需要持有视图相应的数据对象以更新界面显示。

1. 当NodeItem随着视图组件即将销毁时，在aboutToDisappear()中回收NodeItem到NodePool缓存池，存入type类型对应的集合中。
2. 每次需要创建自定义组件时，优先根据type类型查找对应的NodeItem对象，若未找到则新建一个NodeItem。
3. 视图组件随着NodeContainer的生命周期显示时，执行数据更新，完成组件的复用过程。

这种方式需要自行维护复用池，开发者也可以考虑使用同一原理实现的全局组件复用池三方库：[nodepool](https://ohpm.openharmony.cn/#/cn/detail/@hadss%2Fnodepool)。

### 开发步骤

1. 实现列表项占位结点类NodeItem，继承NodeController实现makeNode()方法，根据node是否存在，执行创建或刷新数据的逻辑，并在aboutToDisappear()时回收组件结点。

   ```
   1. export class NodeItem extends NodeController {
   2. public builder: WrappedBuilder<ESObject> | null = null;
   3. public node: BuilderNode<ESObject> | null = null;
   4. public data: ESObject = {};
   5. public type: string = '';
   6. public id: number = 0;

   8. aboutToDisappear(): void {
   9. // recycle node into cache pool when UI disappear
   10. NodePool.getInstance().recycleNode(this.type, this);
   11. }

   13. update(data: ESObject) {
   14. this.data = data;
   15. this.node?.reuse(data);
   16. }

   18. makeNode(uiContext: UIContext): FrameNode | null {
   19. // build new node or update node in the cache
   20. if (!this.node) {
   21. this.node = new BuilderNode(uiContext);
   22. this.node.build(this.builder, this.data);
   23. } else {
   24. this.update(this.data);
   25. }
   26. return this.node.getFrameNode();
   27. }

   29. // ...
   30. }
   ```

   [BuilderNodePool.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/utils/BuilderNodePool.ets#L25-L61)
2. 使用单例模式实现复用缓存池NodePool工具类，在应用内统一管理组件的复用逻辑：实现取缓存getNode()方法，根据传入的type类型，获取对应的NodeItem，如果未找到，则新创建后绑定数据；实现缓存回收recycleNode()方法，根据type类型存入相应的集合中。

   ```
   1. export class NodePool {
   2. private static instance: NodePool;
   3. private idGen: number;
   4. private nodePool: HashMap<string, LinkedList<NodeItem>>;

   6. private constructor() {
   7. this.nodePool = new HashMap();
   8. this.idGen = 0;
   9. }

   11. // single instance mode, managing the cache pool
   12. public static getInstance() {
   13. if (!NodePool.instance) {
   14. NodePool.instance = new NodePool();
   15. }
   16. return NodePool.instance;
   17. }

   19. public getNextId(): number {
   20. this.idGen += 1;
   21. return this.idGen;
   22. }

   24. public getNode(type: string, item: ESObject,
   25. builder: WrappedBuilder<ESObject>): NodeItem | undefined {
   26. let nodeItem: NodeItem | undefined = undefined;
   27. try {
   28. // get the cached node based on type
   29. if (this.nodePool.get(type)) {
   30. for (let i = 0; i < this.nodePool.get(type)?.length; i++) {
   31. let tmpItem: NodeItem | undefined = this.nodePool.get(type)?.get(i);
   32. // if the parent node is null, it means the node is reusable, so get it out
   33. if (!tmpItem.node?.getFrameNode()?.getParent()) {
   34. nodeItem = tmpItem;
   35. this.nodePool.get(type)?.removeByIndex(i);
   36. break;
   37. }
   38. }
   39. }
   40. } catch (e) {
   41. let err = e as BusinessError;
   42. hilog.error(DOMAIN, 'testTag', `failed code=${err.code}, message=${err.message}`);
   43. }

   45. if (!nodeItem) {
   46. // No valid reusable node found, so create new one
   47. nodeItem = new NodeItem();
   48. nodeItem.builder = builder;
   49. nodeItem.type = type;
   50. nodeItem.data.item = item;
   51. } else {
   52. // update cached node
   53. nodeItem.data.item = item;
   54. }
   55. return nodeItem;
   56. }

   58. // cache the node based on type
   59. public recycleNode(type: string, node: NodeItem) {
   60. try {
   61. let nodeArray: LinkedList<NodeItem> = this.nodePool.get(type);
   62. if (!nodeArray) {
   63. nodeArray = new LinkedList();
   64. this.nodePool.set(type, nodeArray);
   65. }
   66. // reset data
   67. node.data.item = {};
   68. nodeArray.add(node);
   69. } catch (e) {
   70. let err = e as BusinessError;
   71. hilog.error(DOMAIN, 'testTag', `failed code=${err.code}, message=${err.message}`);
   72. }
   73. }

   75. // ...
   76. }
   ```

   [BuilderNodePool.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/utils/BuilderNodePool.ets#L65-L153)

   注意

   * getNode()方法中，如果找到的NodeItem父结点不为空（说明未完全下树），需要继续遍历查找下一个有效的NodeItem对象。
   * recycleNode()方法中，需要对NodeItem对象属性重置，使节点内容还原，避免复用显示异常情况。
3. 将步骤1中的列表项占位结点包装成组件，在对应的生命周期中分别取缓存、回收、复用。

   ```
   1. // The list item placeholder component with NodeContainer
   2. @Component
   3. export struct DiffListItemNode {
   4. @State type: string = '';
   5. @State item: ItemData = new ItemData('', 0);
   6. @State itemHeight: number = 0;
   7. @State builder: WrappedBuilder<ESObject> | null = null;
   8. private nodeItem: NodeItem = new NodeItem();

   10. aboutToAppear(): void {
   11. this.nodeItem = NodePool.getInstance().getNode(this.type, this.item, this.builder!)!;
   12. }

   14. aboutToRecycle(): void {
   15. this.nodeItem?.node?.recycle();
   16. }

   18. aboutToReuse(params: ESObject): void {
   19. this.nodeItem?.node?.reuse(params);
   20. }

   22. build() {
   23. NodeContainer(this.nodeItem)
   24. }
   25. }
   ```

   [DiffListItemNode.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/view/DiffListItemNode.ets#L20-L44)
4. 封装列表项的界面视图组件，使用listItemBuilder函数对外export该组件。

   ```
   1. // export the list item component
   2. @Builder
   3. export function listItemBuilder(data: ESObject) {
   4. DiffListItemView({
   5. item: data.item
   6. })
   7. }

   9. // The list item view component
   10. @Component
   11. export struct DiffListItemView {
   12. // ...

   14. aboutToReuse(params: ESObject): void {
   15. this.item = params.item;
   16. }

   18. build() {
   19. Row() {
   20. // ...
   21. }
   22. // ...
   23. }
   24. }
   ```

   [DiffListItemView.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/view/DiffListItemView.ets#L19-L79)
5. 在列表的LazyForEach()中，将步骤4的实际列表项视图wrapBuilder后作为参数传递给步骤3封装的占位组件，实现复用组件的布局。

   ```
   1. // wrapBuilder the list item view component
   2. export const listItemWrapper: WrappedBuilder<ESObject> = wrapBuilder<ESObject>(listItemBuilder);

   4. // The list component in the swiper
   5. @Component
   6. export struct TabContentView {
   7. // ...

   9. build() {
   10. List() {
   11. LazyForEach(this.dataSource, (item: ItemData) => {
   12. DiffListItemNode({
   13. type: REUSE_VIEW_TYPE_ITEM,
   14. item: item,
   15. builder: listItemWrapper
   16. })
   17. }, (item: ItemData) => item.id.toString())
   18. }
   19. // ...
   20. }
   21. }
   ```

   [TabContentView.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/view/TabContentView.ets#L26-L67)

### 使用onIdle()预创建组件

在当前场景下，首次进入页面可能耗时较高，因为在第一次进入时，自定义组件复用池中没有缓存可以复用，列表项都需要新创建。优化这个问题，可以考虑预创建组件，将组件对象提前放入复用缓存池中。

当组件数量较多，集中预创建本身也耗时较长，容易导致主线程阻塞。ArkUI中提供了[onIdle()接口](../harmonyos-references/arkts-apis-uicontext-framecallback.md#onidle12)，会返回每一帧帧尾的空闲时间，可以将组件预创建分布到每一帧帧尾的空闲时间中执行，这样预创建过程就被平摊在多个周期里执行，避免集中运行的耗时影响，进而优化应用体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/m5jipT4eRCOStqMi0JnMYA/zh-cn_image_0000002306983642.png?HW-CC-KV=V1&HW-CC-Date=20260429T060728Z&HW-CC-Expire=86400&HW-CC-Sign=3B82ED33B8B84EA4635AD38A4E5F6A71590C1E6FF9E81D7E278C8E572478BA5D "点击放大")

注意

1. 需要根据业务准确预估组件预创建耗时，同时将业务逻辑颗粒度拆小，以便能够分到多个onIdle()时机中完成。例如，单个组件预创建耗时在2ms左右，帧尾空闲时间只有1ms，那么就不能在当前帧进行预创建，而是延迟到下一帧中执行。

2. 需要合理控制自定义组件复用池中预创建的数量，否则内存占用较多，可能会影响性能。

1. 在NodePool工具类中实现预创建preBuild()方法：新建NodeItem实例，设置builder等属性，执行recycleNode()提前放入缓存池中。

   ```
   1. export class NodeItem extends NodeController {
   2. // ...

   4. prebuild(uiContext: UIContext) {
   5. this.node = new BuilderNode(uiContext);
   6. this.node.build(this.builder, this.data);
   7. }
   8. }

   10. export class NodePool {
   11. // ...

   13. public preBuild(type: string, item: ESObject, builder: WrappedBuilder<ESObject>, uiContext: UIContext) {
   14. if (type) {
   15. let nodeItem: NodeItem | undefined = new NodeItem();
   16. nodeItem.builder = builder;
   17. nodeItem.data.item = item;
   18. nodeItem.type = type;
   19. nodeItem.prebuild(uiContext);
   20. this.recycleNode(type, nodeItem);
   21. }
   22. }
   23. }
   ```

   [BuilderNodePool.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/utils/BuilderNodePool.ets#L24-L154)
2. 继承FrameCallback实现帧回调类，在构造器中传入预创建的数据，并实现onIdle()接口。
   1. 系统会通过onIdle()回调，将帧尾空闲时间通过参数idleTimeInNano传递出来，可根据单个组件的预创建耗时，设置预创建的剩余空闲时间上限（示例代码假设单个组件预创建耗时最长1ms=1000000ns）。
   2. 当剩余空闲时间足够创建组件时，在这一帧中进行组件预创建，并不断更新当前帧的剩余空闲时间。
   3. 若当前帧剩余空闲时间不足以创建组件，通过postFrameCallback()方法，将回调传递到下一帧，继续进行剩余组件的预创建。

      ```
      1. export class IdleCallback extends FrameCallback {
      2. private uiContext: UIContext;
      3. // Pre build component index, start from 0
      4. private todoCount: number = 0;
      5. private dataArray: ItemData[] = [];

      7. constructor(context: UIContext, preBuildData: ItemData[]) {
      8. super();
      9. this.uiContext = context;
      10. this.dataArray = preBuildData;
      11. }

      13. onIdle(idleTimeInNano: number): void {
      14. if (this.todoCount >= this.dataArray.length) {
      15. // All pre build completed
      16. return;
      17. }
      18. let cur: number = systemDateTime.getTime(true);
      19. let timeLeft = idleTimeInNano;
      20. // if the build time for a single component is 1000000 ns
      21. while (timeLeft >= 1000000) {
      22. hiTraceMeter.startTrace('onIdle_prebuild', 1);
      23. // prebuild the component
      24. NodePool.getInstance().preBuild('reuse_type_', this.dataArray[this.todoCount], listItemWrapper, this.uiContext);
      25. hiTraceMeter.finishTrace('onIdle_prebuild', 1);
      26. // update the idle time
      27. let now = systemDateTime.getTime(true);
      28. timeLeft = timeLeft - (now - cur);
      29. cur = now;
      30. this.todoCount++;
      31. if (this.todoCount >= this.dataArray.length) {
      32. // All pre build completed
      33. return;
      34. }
      35. if (this.todoCount < this.dataArray.length) {
      36. // Pre build not completed, proceed to the next frame
      37. this.uiContext.postFrameCallback(this);
      38. }
      39. }
      40. }
      41. }
      ```

      [IdleCallback.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/utils/IdleCallback.ets#L24-L64)
3. 在进入Swiper+List的页面之前，选择合适的时机执行context.postFrameCallback()，开启IdleCallback帧回调逻辑。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // ...

   6. aboutToAppear(): void {
   7. let dataArray: ItemData[] = [];
   8. dataArray.push(...genMockItemData(100))
   9. let context = this.getUIContext();
   10. context.postFrameCallback(new IdleCallback(context, dataArray));
   11. }

   13. // ...
   14. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/component-reuse/blob/master/entry/src/main/ets/pages/Index.ets#L26-L86)

## 更多优化方法

### 使用attributeUpdater实现组件属性的部分刷新

在可复用组件中使用[attributeUpdater](../harmonyos-references/js-apis-arkui-attributeupdater.md)可以控制指定属性的刷新，避免不必要的重绘、减少渲染负载，从而提升应用性能。

默认情况下，直接使用状态变量在aboutToReuse()中进行数据赋值，会导致组件全部属性刷新。实际需求中，可能只需要更新组件的部分属性。例如，当组件复用显示时，只希望设置文本的字体颜色，那么可以使用attributeUpdater在aboutToReuse()修改fontColor属性。

反例：

这里通过aboutToReuse()对fontColor状态变量更新，导致组件全部属性进行刷新，造成不必要的耗时。

```
1. @Component
2. export struct LessEmbeddedComponent {
3. aboutToAppear(): void {
4. momentData.getFriendMomentFromRawfile();
5. }

7. build() {
8. Column() {
9. Text('use nothing')
10. List({ space: ListConstants.LIST_SPACE }) {
11. LazyForEach(momentData, (moment: FriendMoment) => {
12. ListItem() {
13. OneMomentNoModifier({ color: moment.color })
14. .onClick(() => {
15. console.log(`my id is ${moment.id}`)
16. })
17. }
18. }, (moment: FriendMoment) => moment.id)
19. }
20. .width("100%")
21. .height("100%")
22. .cachedCount(5)
23. }
24. }
25. }

27. @Reusable
28. @Component
29. export struct OneMomentNoModifier {
30. @State color: string | number | Resource = "";

32. aboutToReuse(params: Record<string, Object>): void {
33. this.color = params.color as number;
34. }

36. build() {
37. Column() {
38. Text('This is title')
39. Text('This is desc text')
40. .fontColor(this.color)
41. .textAlign(TextAlign.Center)
42. .fontStyle(FontStyle.Normal)
43. .fontSize(13)
44. .lineHeight(30)
45. .opacity(0.6)
46. .margin({ top: 10 })
47. .fontWeight(30)
48. .clip(false)
49. .backgroundBlurStyle(BlurStyle.NONE)
50. .foregroundBlurStyle(BlurStyle.NONE)
51. .borderWidth(1)
52. .borderColor(Color.Pink)
53. .borderStyle(BorderStyle.Solid)
54. .alignRules({
55. 'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
56. 'left': { 'anchor': 'image', 'align': HorizontalAlign.End }
57. })
58. }
59. }
60. }
```

正例：

通过attributeUpdater对Text组件中的fontColor属性进行精准刷新，避免重绘Text中不需要更改的属性。

```
1. export class MyTextUpdater extends AttributeUpdater<TextAttribute> {
2. private color: string | number | Resource | Color = '';

4. constructor(color: string | number | Resource | Color) {
5. super();
6. this.color = color;
7. }

9. initializeModifier(instance: TextAttribute): void {
10. instance.fontColor(this.color) // Differentiated update
11. }
12. }

14. // ...

16. @Reusable
17. @Component
18. export struct OneMomentNoModifier {
19. @State text: string = '';
20. color: string | number | Resource | Color = '';
21. textUpdater: MyTextUpdater | null = null;

23. aboutToAppear(): void {
24. this.textUpdater = new MyTextUpdater(this.color);
25. }

27. aboutToReuse(params: Record<string, Object>): void {
28. this.color = params.color as string;
29. this.text = params.text as string;
30. this.textUpdater?.attribute?.fontColor(this.color);
31. }

33. build() {
34. Column() {
35. Text(this.text)
36. .fontSize(18)
37. .textAlign(TextAlign.Center)
38. .fontWeight(500)
39. .lineHeight(24)
40. .fontColor(Color.Black)
41. .opacity(0.6)
42. Column() {
43. Text('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
44. .attributeModifier(this.textUpdater) // Precise refresh
45. .textAlign(TextAlign.Start)
46. .fontSize(16)
47. .fontWeight(400)
48. .lineHeight(21)
49. }
50. // ...
51. }
52. // ...
53. }
54. }
```

[UpdaterComponent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentReuse/entry/src/main/ets/view/UpdaterComponent.ets#L24-L125)

### 使用@Link/@ObjectLink替代@Prop以减少深拷贝

在可复用组件中，建议使用[@Link](../harmonyos-guides/arkts-link.md)/[@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)替代[@Prop](../harmonyos-guides/arkts-prop.md)。因为@Prop装饰变量时会进行深拷贝，增加了创建时间及内存消耗，而改用@Link/@ObjectLink，变量会共享同一地址。

反例：

```
1. @Entry
2. @Component
3. struct lessEmbeddedComponent {
4. aboutToAppear(): void {
5. getFriendMomentFromRawfile();
6. }

8. build() {
9. Column() {
10. TopBar()
11. List({ space: ListConstants.LIST_SPACE }) {
12. LazyForEach(momentData, (moment: FriendMoment) => {
13. ListItem() {
14. OneMoment({moment: moment})
15. }
16. }, (moment: FriendMoment) => moment.id)
17. }
18. .cachedCount(Constants.CACHED_COUNT)
19. }
20. }
21. }

23. @Reusable
24. @Component
25. export struct OneMoment {
26. @Prop moment: FriendMoment;

28. build() {
29. Column() {
30. ...
31. Text(`${this.moment.userName}`)
32. ...
33. }
34. }
35. }

37. export class FriendMoment {
38. id: string;
39. userName: string;
40. avatar: string;
41. text: string;
42. size: number;
43. image?: string;
44. }
```

正例：

将子组件moment变量@Prop改为@ObjectLink即可。

父子组件之间的数据同步用了@ObjectLink来进行，子组件@ObjectLink包装类把当前this指针注册给父组件，会直接将父组件的数据同步给子组件，实现父子组件数据的双向同步，降低子组件创建时间和内存消耗。

### 避免对@Link/@ObjectLink/@Prop等自动更新的状态变量，在aboutToReuse()中重复赋值

如果可复用组件中使用了[@Link](../harmonyos-guides/arkts-link.md)/[@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)/[@Prop](../harmonyos-guides/arkts-prop.md)等自动同步父子组件数据的状态变量，则不需要在aboutToReuse()中对这些数据重复赋值。如果重新赋值这些变量，会导致组件的内容重新触发状态刷新，造成额外的计算更新耗时。

反例：

```
1. @Reusable
2. @Component
3. export struct OneMoment {
4. @ObjectLink moment: FriendMoment;

6. aboutToReuse(params: Record<string, Object>): void {
7. this.moment.id = (params.moment as FriendMoment).id
8. this.moment.userName = (params.moment as FriendMoment).userName
9. this.moment.avatar = (params.moment as FriendMoment).avatar
10. this.moment.text = (params.moment as FriendMoment).text
11. this.moment.image = (params.moment as FriendMoment).image
12. }

14. build() {
15. Column() {
16. ...
17. Text(`${this.moment.userName}`)
18. ...
19. }
20. }
21. }
```

正例：

将aboutToReuse()中的赋值语句删除。

@ObjectLink修饰的moment状态变量已包含自动刷新功能，不需要再重复赋值刷新。

### 使用reuseId标记布局发生变化的组件

在同一段自定义组件代码中，如果使用if/else条件语句控制布局结构，会导致在不同逻辑分支中创建不同布局的组件，从而造成组件树结构的差异。此时可以使用reuseId来区分发生变化的分支逻辑，确保系统能够根据reuseId缓存各种结构的组件，提升复用性能。

反例：

组件通过if条件创建包含Image的Flex组件。不使用reuseId时，复用后根据if条件，可能会删除Flex或重新创建Flex，存在性能消耗。

```
1. @Entry
2. @Component
3. struct AboutReuseId {

5. build() {
6. Column() {
7. TopBar()
8. List({ space: ListConstants.LIST_SPACE }) {
9. LazyForEach(momentData, (moment: FriendMoment) => {
10. ListItem() {
11. OneMoment({
12. moment: moment,
13. fontSize: moment.size
14. })
15. }
16. }, (moment: FriendMoment) => moment.id)
17. }
18. .cachedCount(Constants.CACHED_COUNT)
19. }
20. }
21. }

23. @Reusable
24. @Component
25. export struct OneMoment {
26. @Prop moment: FriendMoment;

28. build() {
29. Column() {
30. ...
31. Text(this.moment.text)

33. if (this.moment.image !== '') {
34. Flex({ wrap: FlexWrap.Wrap }) {
35. Image($r(this.moment.image))
36. Image($r(this.moment.image))
37. Image($r(this.moment.image))
38. }
39. }
40. ...
41. }
42. }
43. }
```

正例：

根据分支逻辑设置不同的reuseId，缓存不同布局结构下的组件，省去重复执行if的删除或创建逻辑。

```
1. @Entry
2. @Component
3. struct WithReuseId {
4. // ...

6. build() {
7. Column() {
8. List({ space: this.LIST_SPACE }) {
9. LazyForEach(this.momentData, (moment: FriendMoment) => {
10. ListItem() {
11. OneMoment({ moment: moment })// ReusId is used to control component reuse
12. .reuseId((moment.image !== '') ? 'withImage_id' : 'noImage_id')
13. }
14. }, (moment: FriendMoment) => moment.id)
15. }
16. // ...
17. }
18. }
19. }

21. @Reusable
22. @Component
23. export struct OneMoment {
24. @ObjectLink moment: FriendMoment;

26. build() {
27. Column() {
28. // ...

30. if (this.moment.image !== '') {
31. Flex({ wrap: FlexWrap.Wrap }) {
32. Image($r(this.moment.image))
33. .width(Constants.LAYOUT_MAX)
34. .height('27.5%')
35. .borderRadius(16)
36. Image($r(this.moment.image))
37. .width(Constants.LAYOUT_MAX)
38. .height('27.5%')
39. .borderRadius(16)
40. .margin({ top: 10 })
41. }
42. .width(Constants.LAYOUT_MAX)
43. .margin({ top: 14 })
44. }
45. }
46. // ...
47. }
48. }
```

[WithReuseId.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentReuse/entry/src/main/ets/view/WithReuseId.ets#L20-L95)

### 避免使用函数方法作为复用组件的入参

如果可复用组件的入参使用了函数方法，因每次复用都需要重新创建组件关联的数据对象，该函数会在每次复用时执行，造成性能问题。建议改为通过状态变量传递参数，从而减少重复执行入参中的函数所带来的性能消耗。

反例：

复用的子组件参数sum是通过模拟耗时函数countAndReturn()生成。该函数在每次组件复用时都执行，会造成性能问题，甚至导致列表滑动过程中的卡顿丢帧。

```
1. @Entry
2. @Component
3. struct withFuncParam {
4. aboutToAppear(): void {
5. getFriendMomentFromRawfile();
6. }

8. countAndReturn(): number {
9. let temp: number = 0;
10. for (let index = 0; index < 100000; index++) {
11. temp += index;
12. }
13. return temp;
14. }

16. build() {
17. Column() {
18. TopBar()
19. List({ space: ListConstants.LIST_SPACE }) {
20. LazyForEach(momentData, (moment: FriendMoment) => {
21. ListItem() {
22. OneMoment({
23. moment: moment,
24. sum: this.countAndReturn()
25. })
26. }
27. }, (moment: FriendMoment) => moment.id)
28. }
29. .cachedCount(Constants.CACHED_COUNT)
30. }
31. }
32. }

34. @Reusable
35. @Component
36. export struct OneMoment {
37. @Prop moment: FriendMoment;
38. @State sum: number = 0;

40. aboutToReuse(params: Record<string, Object>): void {
41. this.sum = params.sum as number;
42. }

44. build() {
45. Column() {
46. ...
47. Text(`${this.moment.userName} （${this.moment.id} / ${this.sum}）`)
48. ...
49. }
50. }
51. }
```

正例：

可以先将countAndReturn()计算放到页面初始时执行，将结果赋值给this.sum变量。在复用组件的参数传递时，通过this.sum来进行。

```
1. @Entry
2. @Component
3. struct WithFuncParam {
4. @State sum: number = 0;
5. // ...
6. private readonly MOCK_ASYNC_DEFAULT_NUM: number = 1000000;
7. private readonly MOCK_ASYNC_TIME_OUT_NUM: number = 2000;

9. aboutToAppear(): void {
10. this.momentData.getFriendMomentFromRawFile();
11. // Execute the asynchronous function
12. this.countAndReturn();
13. }

15. async countAndReturn(): Promise<void> {
16. await this.sleep();
17. this.sum = this.MOCK_ASYNC_DEFAULT_NUM;
18. }

20. sleep(): Promise<string> {
21. return new Promise<string>((resolve) => {
22. setTimeout(() => {
23. resolve('ok');
24. }, this.MOCK_ASYNC_TIME_OUT_NUM)
25. });
26. }

28. build() {
29. Column() {
30. List({ space: this.LIST_SPACE }) {
31. LazyForEach(this.momentData, (moment: FriendMoment) => {
32. ListItem() {
33. // Parameters of subcomponents are transferred through status variables
34. OneMoment({
35. moment: moment,
36. sum: this.sum
37. })
38. }
39. }, (moment: FriendMoment) => moment.id)
40. }
41. // ...
42. }
43. }
44. }

46. @Reusable
47. @Component
48. export struct OneMoment {
49. @ObjectLink moment: FriendMoment;
50. @State sum: number = 0;
51. // ...

53. aboutToReuse(params: Record<string, Object>): void {
54. this.sum = params.sum as number;
55. }

57. // ...
58. }
```

[WithFuncParam.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentReuse/entry/src/main/ets/view/WithFuncParam.ets#L20-L157)

## 常见问题

### 如何检查组件复用是否生效

* 使用[Code Linter扫描工具](../harmonyos-guides/ide-code-linter.md)进行代码检查，重点关注[@performance/hp-arkui-use-reusable-component](../harmonyos-guides/ide_hp-arkui-use-reusable-component.md)规则。
* 通过Profiler工具抓取Trace，搜索组件名称，根据BuildRecycle字段识别是否触发复用渲染。具体可参考[通过Trace识别懒加载渲染流程](bpta-optimization-overview.md#section1588117331934)。
* 通过Profiler工具抓取Trace，识别是否发生丢帧，判断子组件创建的次数。具体分析过程可参考[优化长列表-组件复用性能分析](bpta-best-practices-long-list.md#section1069111015296)。

## 示例代码

* [实现组件复用](https://gitcode.com/harmonyos_samples/component-reuse/)
