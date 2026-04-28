---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-waterflow
title: 创建瀑布流（WaterFlow）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > 创建瀑布流（WaterFlow）
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d92f8e522769b6f961d5951f1ec683830acdcfa753a1e9f19e6ab46383390c8f
---

[瀑布流](../harmonyos-references/ts-container-waterflow.md)常用于展示图片信息，尤其在购物和资讯类应用中。

ArkUI提供了WaterFlow容器组件，用于构建瀑布流布局。WaterFlow组件支持条件渲染、循环渲染和懒加载等方式生成子组件。

说明

本文仅展示关键代码片段，可运行的完整代码请参考[WaterFlow示例代码](../harmonyos-references/ts-container-waterflow.md#示例)。

## 布局与约束

瀑布流支持横向和纵向布局。在纵向布局中，可以通过[columnsTemplate](../harmonyos-references/ts-container-waterflow.md#columnstemplate)设置列数；在横向布局中，可以通过[rowsTemplate](../harmonyos-references/ts-container-waterflow.md#rowstemplate)设置行数。

在瀑布流的纵向布局中，第一行的子节点按从左到右顺序排列，从第二行开始，每个子节点将放置在当前总高度最小的列。如果多个列的总高度相同，则按照从左到右的顺序填充。如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/89oWSnGnSxKqXWZQZF5-Ug/zh-cn_image_0000002552957764.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=E0892036C3E714C4C0234AA0CB44F108373E2F178D81FFE69A29F269FA1F710A)

在瀑布流的横向布局中，每个子节点都会放置在当前总宽度最小的行。若多行总宽度相同，则按照从上到下的顺序进行填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/hQTtE_qYSdanr5cfD6hiTg/zh-cn_image_0000002552957788.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=EBF4A573B35FFCF3827F1F4DF88FE8E4FFCF14E42A80617B0F0C1BE71B2F286E)

## 无限滚动

### 到达末尾时新增数据

瀑布流常用于无限滚动的信息流。可以在瀑布流组件到达末尾位置时触发的[onReachEnd](../harmonyos-references/ts-container-waterflow.md#onreachend)事件回调中对[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)增加新数据，并将footer做成正在加载新数据的样式（使用[LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md)组件）。

```
1. @Builder
2. itemFoot() {
3. Row() {
4. LoadingProgress()
5. .color(Color.Blue).height(50).aspectRatio(1).width('20%')
6. // 请将$r('app.string.waterFlow_text1')替换为实际资源文件，在本示例中该资源文件的value值为"正在加载 "
7. Text($r('app.string.waterFlow_text1'))
8. .fontSize(20)
9. .width('30%')
10. .height(50)
11. .align(Alignment.Center)
12. .margin({ top: 2 })
13. }.width('100%').justifyContent(FlexAlign.Center)
14. }

16. build() {
17. NavDestination() {
18. Column({ space: 12 }) {
19. // ...
20. WaterFlow({ footer: this.itemFoot(), layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW }) {
21. LazyForEach(this.dataSource, (item: number) => {
22. FlowItem() {
23. ReusableFlowItem({ item: item })
24. }
25. .width('100%')
26. .aspectRatio(this.itemHeightArray[item % 100] / this.itemWidthArray[item%100])
27. .backgroundColor(this.colors[item % 5])
28. }, (item: string) => item)
29. }
30. .columnsTemplate('1fr '.repeat(this.columns))
31. .backgroundColor(0xFAEEE0)
32. .width('100%')
33. .height('100%')
34. .layoutWeight(1)
35. // 触底加载数据
36. .onReachEnd(() => {
37. setTimeout(() => {
38. this.dataSource.addNewItems(100);
39. }, 1000)
40. })
41. }
42. // ...
43. }
44. .backgroundColor('#f1f2f3')
45. // 请将$r('app.string.WaterFlowInfiniteScrolling_title')替换为实际资源文件，在本示例中该资源文件的value值为"无限滚动（到达末尾时新增数据）"
46. .title($r('app.string.WaterFlowInfiniteScrolling_title'))
47. }
```

[WaterFlowInfiniteScrolling.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowInfiniteScrolling.ets#L96-L148)

在此处应通过在数据末尾添加元素的方式来新增数据，不可直接修改dataArray后通过LazyForEach的[onDataReloaded](../harmonyos-references/ts-rendering-control-lazyforeach.md#ondatareloaded)方法通知瀑布流重新加载数据。

由于在瀑布流布局中，各子节点的高度不一致，下面的节点位置依赖于上面的节点，所以重新加载所有数据会触发整个瀑布流重新计算布局，可能会导致卡顿。在数据末尾增加数据后，应使用[onDataAdd](../harmonyos-references/ts-rendering-control-lazyforeach.md#ondataadd8)通知，以使瀑布流能够识别新增数据并继续加载，同时避免对已有数据进行重复处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/dUOv75bKTMyHjBmb0cyqmQ/zh-cn_image_0000002583477789.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=21F5125AE507F477A0B789DB70B25EF0691E0C8836BAF1862EA98E8CC54F7E66)

### 提前新增数据

虽然在onReachEnd()触发时加载数据可以实现无限加载，但在滑动到底部会出现明显的停顿。

为了实现更加流畅的无限滑动，需要调整增加新数据的时机。比如可以在LazyForEach还剩余若干个数据未遍历的情况下提前加载新数据。以下代码通过在WaterFlow的[onScrollIndex](../harmonyos-references/ts-container-waterflow.md#onscrollindex11)中判断当前显示的最后一个子节点相对数据集终点的距离，并在合适时机提前加载新数据，实现了无停顿的无限滚动。

```
1. build() {
2. NavDestination() {
3. Column({ space: 12 }) {
4. // ...
5. WaterFlow({ layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW }) {
6. LazyForEach(this.dataSource, (item: number) => {
7. FlowItem() {
8. ReusableFlowItem({ item: item })
9. }
10. .width('100%')
11. .aspectRatio(this.itemHeightArray[item % 100] / this.itemWidthArray[item%100])
12. .backgroundColor(this.colors[item % 5])
13. }, (item: string) => item)
14. }
15. .columnsTemplate('1fr '.repeat(this.columns))
16. .backgroundColor(0xFAEEE0)
17. .width('100%')
18. .height('100%')
19. .layoutWeight(1)
20. // 即将触底时提前增加数据
21. .onScrollIndex((first: number, last: number) => {
22. if (last + 20 >= this.dataSource.totalCount()) {
23. setTimeout(() => {
24. this.dataSource.addNewItems(100);
25. }, 1000);
26. }
27. })
28. }
29. // ...
30. }
31. .backgroundColor('#f1f2f3')
32. // 请将$r('app.string.WaterFlowInfiniteScrollingEarly_title')替换为实际资源文件，在本示例中该资源文件的value值为"无限滚动（提前新增数据）"
33. .title($r('app.string.WaterFlowInfiniteScrollingEarly_title'))
34. }
```

[WaterFlowInfiniteScrollingEarly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowInfiniteScrollingEarly.ets#L111-L150)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/2q19y0yzSxKCtlz8g5P5Ug/zh-cn_image_0000002552798140.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=B033E3FE7C4C56BB659A46C50096776889CBE9BE1A89A58C7531BF9420F9E8B8)

## 动态切换列数

通过动态调整瀑布流的列数，应用能够实现在列表模式与瀑布流模式间的切换，或适应屏幕宽度的变化。 若要动态设置列数，建议采用瀑布流的移动窗口布局模式，即取值为[WaterFlowLayoutMode枚举说明](../harmonyos-references/ts-container-waterflow.md#waterflowlayoutmode12枚举说明)中的SLIDING\_WINDOW，这可以实现更快速的列数转换。

```
1. @Reusable
2. @Component
3. struct ReusableListItem {
4. @State item: number = 0;

6. aboutToReuse(params: Record<string, number>) {
7. this.item = params.item;
8. }

10. build() {
11. Row() {
12. Image('res/waterFlow(' + this.item % 5 + ').JPG')
13. .objectFit(ImageFit.Fill)
14. .height(100)
15. .aspectRatio(1)
16. Text('N' + this.item).fontSize(12).height('16').layoutWeight(1).textAlign(TextAlign.Center)
17. }
18. }
19. }

21. @Entry
22. @Component
23. export struct WaterFlowDynamicSwitchover {
24. // 通过状态变量设置列数，可以按需修改触发布局更新
25. @State columns: number = 2;

27. // ...
28. build() {
29. NavDestination() {
30. Column({ space: 12 }) {
31. // ...
32. Column({ space: 2 }) {
33. // 请将$r('app.string.waterFlow_text2')替换为实际资源文件，在本示例中该资源文件的value值为"切换列数 "
34. Button($r('app.string.waterFlow_text2')).fontSize(20).onClick(() => {
35. if (this.columns === 2) {
36. this.columns = 1;
37. } else {
38. this.columns = 2;
39. }
40. })
41. WaterFlow({ layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW }) {
42. LazyForEach(this.dataSource, (item: number) => {
43. FlowItem() {
44. if (this.columns === 1) {
45. ReusableListItem({ item: item })
46. } else {
47. ReusableFlowItem({ item: item })
48. }
49. }
50. .width('100%')
51. .aspectRatio(this.columns === 2 ? this.itemHeightArray[item % 100] / this.itemWidthArray[item % 100] : 0)
52. .backgroundColor(this.colors[item % 5])
53. }, (item: string) => item)
54. }
55. .columnsTemplate('1fr '.repeat(this.columns))
56. .backgroundColor(0xFAEEE0)
57. .width('100%')
58. .height('100%')
59. .layoutWeight(1)
60. // 即将触底时提前增加数据
61. .onScrollIndex((first: number, last: number) => {
62. if (last + 20 >= this.dataSource.totalCount()) {
63. setTimeout(() => {
64. this.dataSource.addNewItems(100);
65. }, 1000);
66. }
67. })
68. // ...
69. }
70. }
71. // ...
72. }
73. .backgroundColor('#f1f2f3')
74. // 请将$r('app.string.WaterFlowDynamicSwitchover_title')替换为实际资源文件，在本示例中该资源文件的value值为"动态切换列数"
75. .title($r('app.string.WaterFlowDynamicSwitchover_title'))
76. }
77. }
```

[WaterFlowDynamicSwitchover.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowDynamicSwitchover.ets#L40-L190)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/qnhYSpKXTyuqEncm8oqe8A/zh-cn_image_0000002583437835.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=3F3785167296D70B4E86FF3209C3F4B94456CF5AC501F5576A957B9E705C3E4F)

## 分组混合布局

许多应用界面在瀑布流上方包含其他内容，这类场景可通过在Scroll或List内部嵌套WaterFlow来实现。类似下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/pwb0n0bPSNmv-7oW9UL2Vg/zh-cn_image_0000002552957790.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=D3EA6293A4142C18D922EAD47BE00ED25ABC32130F386B5569D64A699C367366)

如果能够将不同部分的子节点整合到一个数据源中，那么通过设置[WaterFlowSections](../harmonyos-references/ts-container-waterflow.md#waterflowsections12)，可以在一个 WaterFlow 容器内实现混合布局。与嵌套滚动相比，这种方法可以简化滚动事件处理等应用逻辑。

每个瀑布流分组可以分别设置自己的列数、行间距、列间距、margin和子节点总数，如下代码可以实现上述效果：

```
1. @Entry
2. @Component
3. export struct WaterFlowGroupingMixing {
4. minSize: number = 80;
5. maxSize: number = 180;
6. colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
7. dataSource: WaterFlowDataSource = new WaterFlowDataSource(100);
8. private itemWidthArray: number[] = [];
9. private itemHeightArray: number[] = [];
10. private gridItems: number[] = [];
11. @State sections: WaterFlowSections = new WaterFlowSections();
12. sectionMargin: Margin = {
13. top: 10,
14. left: 5,
15. bottom: 10,
16. right: 5
17. };
18. oneColumnSection: SectionOptions = {
19. itemsCount: 1,
20. crossCount: 1,
21. columnsGap: 5,
22. rowsGap: 10,
23. margin: this.sectionMargin,
24. };
25. twoColumnSection: SectionOptions = {
26. itemsCount: 98,
27. crossCount: 2,
28. };
29. // 使用分组瀑布流时无法通过footer设置尾部组件，可以保留一个固定的分组作为footer
30. lastSection: SectionOptions = {
31. itemsCount: 1,
32. crossCount: 1,
33. };

35. // 计算FlowItem宽/高
36. getSize() {
37. let ret = Math.floor(Math.random() * this.maxSize);
38. return (ret > this.minSize ? ret : this.minSize);
39. }

41. // 设置FlowItem的宽/高数组
42. setItemSizeArray() {
43. for (let i = 0; i < 100; i++) {
44. this.itemWidthArray.push(this.getSize());
45. this.itemHeightArray.push(this.getSize());
46. }
47. }

49. aboutToAppear() {
50. this.setItemSizeArray();
51. for (let i = 0; i < 15; ++i) {
52. this.gridItems.push(i);
53. }
54. // 所有分组的itemCount之和需要和WaterFlow下数据源的子节点总数相等，否则无法正常布局
55. let sectionOptions: SectionOptions[] = [this.oneColumnSection, this.twoColumnSection, this.lastSection];
56. this.sections.splice(0, 0, sectionOptions);
57. }

59. build() {
60. NavDestination() {
61. // ...
62. WaterFlow({ layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW, sections: this.sections }) {
63. LazyForEach(this.dataSource, (item: number) => {
64. FlowItem() {
65. if (item === 0) {
66. Grid() {
67. ForEach(this.gridItems, (day: number) => {
68. GridItem() {
69. Text('GridItem').fontSize(14).height(16)
70. }.backgroundColor(0xFFC0CB)
71. }, (day: number) => day.toString())
72. }
73. .height('30%')
74. .rowsGap(5)
75. .columnsGap(5)
76. .columnsTemplate('1fr '.repeat(5))
77. .rowsTemplate('1fr '.repeat(3))
78. } else {
79. ReusableFlowItem({ item: item })
80. }
81. }
82. .width('100%')
83. .aspectRatio(item != 0 ? this.itemHeightArray[item % 100] / this.itemWidthArray[item % 100] : 0)
84. .backgroundColor(item != 0 ? this.colors[item % 5] : Color.White)
85. }, (item: string) => item)
86. }
87. .backgroundColor(0xFAEEE0)
88. .height('100%')
89. // 即将触底时提前增加数据
90. .onScrollIndex((first: number, last: number) => {
91. if (last + 20 >= this.dataSource.totalCount()) {
92. setTimeout(() => {
93. this.dataSource.addNewItems(100);
94. // 增加数据后同步调整对应分组的itemCount
95. this.twoColumnSection.itemsCount += 100;
96. this.sections.update(1, this.twoColumnSection);
97. }, 1000);
98. }
99. })
100. .margin(10)
101. }
102. // ...
103. }
104. }
```

[WaterFlowGroupingMixing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowGroupingMixing.ets#L40-L148)

说明

使用分组混合布局时不支持单独设置footer，可以使用最后一个分组作为尾部组件。

增加或删除数据后需要同步修改对应分组的itemCount。

## 示例代码

* [实现WaterFlow瀑布流布局功能](https://gitcode.com/HarmonyOS_Samples/water-flow)
* [主页瀑布流实现](https://gitcode.com/HarmonyOS-Cases/cases/blob/master/CommonAppDevelopment/feature/functionalscenes/README.md)
