---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-waterflow-operations
title: 常见瀑布流操作
breadcrumb: 最佳实践 > 布局与弹窗 > 常见瀑布流操作
category: best-practices
scraped_at: 2026-04-29T14:10:30+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:46507332a3c28c258842255d003c5d33c719024de73dbf0e59f4315f17efa371
---

## 概述

在应用开发中，开发者常会遇到希望某些页面的内容呈现出“瀑布流”效果，如图片资讯页面、商品列表页面等。通过将元素自上而下排列，形成参差不齐的界面。本文介绍瀑布流常见操作，帮助开发者高效构建自己想要的瀑布流效果。

## 瀑布流排版

### **分组参差布局**

在瀑布流常见开发场景中，主要实现方式类似下图布局效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/o8PGd5LrRziy2S1z91GTwg/zh-cn_image_0000002387038021.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=EDBD4D3732C1A6552DAF5F5D176108A3951082538F48C2E9FCA7B18A12B248C7 "点击放大")

为了实现上图中分组参差不齐的效果，首先需要创建多个SectionOptions，并重写其中的[onGetItemMainSizeByIndex()](../harmonyos-references/ts-container-waterflow.md#getitemmainsizebyindex12)方法的返回值。完整代码如下：

```
1. import { CommonConstants } from "../common/constants/CommonConstants";
2. import { SectionsWaterFlowDataSource } from "../model/SectionsWaterFlowDataSource";

4. // ...
5. @Entry
6. @Component
7. struct SectionOptionsUsePage {
8. // ...
9. dataSource: SectionsWaterFlowDataSource = new SectionsWaterFlowDataSource();
10. private itemHeightArray: number[] = [];
11. sectionMargin: Margin = {
12. top: 8,
13. left: 16,
14. bottom: 0,
15. right: 16
16. }
17. // 1、Create group information.
18. @State sections: WaterFlowSections = new WaterFlowSections();
19. @StorageProp(CommonConstants.AS_KEY_STATUS_BAR_HEIGHT) statusBarHeight: number = 0;
20. // 2、Create the first group.
21. oneColumnSection: SectionOptions = {
22. itemsCount: 3,
23. crossCount: 1,
24. margin: this.sectionMargin,
25. onGetItemMainSizeByIndex: (index: number) => {
26. return 120;
27. }
28. }
29. // 3、Create the second group.
30. twoColumnSection: SectionOptions = {
31. itemsCount: 2,
32. crossCount: 2,
33. margin: this.sectionMargin,
34. onGetItemMainSizeByIndex: (index: number) => {
35. return 160;
36. }
37. }
38. // 4、Create the third group.
39. dataSection: SectionOptions = {
40. itemsCount: 20,
41. crossCount: 2,
42. margin: this.sectionMargin,
43. onGetItemMainSizeByIndex: (index: number) => {
44. return this.itemHeightArray[index % 100];
45. }
46. }

48. // ...

50. aboutToAppear(): void {
51. this.setItemSizeArray();
52. this.initSections();
53. }

55. // 5、Initialise group data.
56. initSections(): void {
57. let sectionOptions: SectionOptions[] = [];
58. let count: number = 0;
59. let oneOrTwo: number = 0;
60. let dataCount: number = this.dataSource.totalCount();
61. while (count < dataCount) {
62. if (dataCount - count < 96) {
63. this.dataSection.itemsCount = dataCount - count;
64. sectionOptions.push(this.dataSection);
65. break;
66. }
67. if (oneOrTwo++ % 2 === 0) {
68. sectionOptions.push(this.oneColumnSection);
69. count += this.oneColumnSection.itemsCount;
70. } else {
71. sectionOptions.push(this.twoColumnSection);
72. count += this.twoColumnSection.itemsCount;
73. }
74. }
75. this.sections.splice(0, 0, sectionOptions);
76. }

78. build() {
79. Column({ space: 0 }) {
80. Row() {
81. Text($r('app.string.section_sort'))
82. .width('100%')
83. .fontSize(24)
84. .fontWeight(FontWeight.Bold)
85. .margin({ top: '18vp', left: '16vp', bottom: '8vp' })
86. }

88. // 6、Link the grouping information to WaterFlow.
89. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
90. // ...
91. }
92. .cachedCount(12)
93. .columnsGap(8)
94. .rowsGap(8)
95. .width('100%')
96. .height('100%')
97. .layoutWeight(1)
98. }
99. .padding({
100. top: this.statusBarHeight
101. })
102. }
103. }
```

[SectionOptionsUsePage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/SectionOptionsUsePage.ets#L17-L203)

说明

1. 使用分组混合布局时，会忽略columnsTemplate和rowsTemplate属性。
2. 使用分组混合布局时，不支持单独设置footer，如果需要footer组件，可使用最后一个分组作为尾部组件。
3. 使用section分组后，必须确保WaterFlow中数据总数与section分组所有itemCount之和相等，否则界面可能显示为空白。

### **自定义高度**

WaterFlow中FlowItem的高度通过SectionOptions的[onGetItemMainSizeByIndex()](../harmonyos-references/ts-container-waterflow.md#getitemmainsizebyindex12)方法返回值来控制，其中参数index表示FlowItem的索引位置。

```
1. import { SectionsWaterFlowDataSource } from "../model/SectionsWaterFlowDataSource";

3. // ...
4. @Entry
5. @Component
6. export struct CustomItemHeightPage {
7. // ...
8. // 1、Create group information.
9. @State sections: WaterFlowSections = new WaterFlowSections();
10. sectionMargin: Margin = {
11. top: 8,
12. left: 0,
13. bottom: 0,
14. right: 0
15. };
16. oneColumnSection: SectionOptions = {
17. itemsCount: 3,
18. crossCount: 1,
19. columnsGap: 5,
20. rowsGap: 10,
21. margin: this.sectionMargin,
22. onGetItemMainSizeByIndex: (index: number) => {
23. // 1、Return item height.
24. return 120;
25. }
26. };
27. // ...
28. }
```

[CustomItemHeightPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/CustomItemHeightPage.ets#L17-L189)

### **瀑布流吸顶**

在某些开发场景中，开发者可能希望WaterFlow向上滑动时，部分内容先跟随滑动，随后吸附于顶部。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/xzSpSkQuSpyMMspVh74Mjg/zh-cn_image_0000002386957729.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=D64CDFBB4DDEAFF94EC132531DD478D2895C7A3AF6EC621FE92A95DD9D2C51C4 "点击放大")

为了实现上图效果，需在WaterFlow分组中需为吸顶的部分预留位置，并监听瀑布流滚动事件。吸顶部分依据瀑布流滑动后的偏移量设置位置，实现与瀑布流同步滚动；吸顶部分达到顶部后固定不动。完整代码如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { CommonConstants } from '../common/constants/CommonConstants';
3. import MediaItem, { ItemType } from '../model/MediaItem';
4. import { StickyWaterFlowDataSource } from '../model/StickyWaterFlowDataSource';

6. const TAG: string = 'StickOnTopPage';

8. // ...
9. @Component
10. export struct StickyPage {
11. // ...
12. // 1、Define the height of the ceiling layout.
13. @State scrollOffset: number = 0;
14. private stickItemHeight: number = 90;
15. sectionMargin: Margin = {
16. top: 8,
17. left: 16,
18. bottom: 0,
19. right: 16
20. };
21. oneColumnSection: SectionOptions = {
22. itemsCount: 3,
23. crossCount: 1,
24. margin: this.sectionMargin,
25. onGetItemMainSizeByIndex: (index: number) => {
26. if (index === 1) {
27. // 2、Set the ceiling layout height in the group.
28. return this.stickItemHeight;
29. } else {
30. return 200;
31. }
32. }
33. };
34. twoColumnSection: SectionOptions = {
35. itemsCount: 2,
36. crossCount: 2,
37. margin: this.sectionMargin,
38. onGetItemMainSizeByIndex: (index: number) => {
39. return 250;
40. }
41. };

43. // ...
44. build() {
45. Stack({ alignContent: Alignment.TopStart }) {
46. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
47. LazyForEach(this.dataSource, (item: MediaItem) => {
48. FlowItem() {
49. // 3、A location is reserved for the ceiling part, and the ceiling position is at the second element location, so the id is 1.
50. FlowVideoItem({ item: item })
51. }
52. .width('100%')
53. .backgroundColor(Color.White)
54. }, (item: MediaItem) => item.id.toString())
55. }
56. .cachedCount(12)
57. .columnsTemplate('1fr 1fr')
58. .columnsGap(8)
59. .rowsGap(8)
60. .width('100%')
61. .height('100%')
62. .layoutWeight(1)
63. .onWillScroll((offset: number) => {
64. // 4、Listen to the waterfall scrolling event.
65. this.scrollOffset = this.scroller.currentOffset().yOffset + offset;
66. })

68. Stack() {
69. // ...
70. }
71. .width('100%')
72. .height(100)
73. .backgroundColor(Color.White)
74. .hitTestBehavior(HitTestMode.Transparent)
75. // 5、Dynamically adjust the sticky position according to the waterfall flow sliding offset.
76. .position({ x: 0, y: this.scrollOffset >= 210 ? 0 : 210 - this.scrollOffset })
77. }
78. }
79. }

81. // ...
```

[StickOnTopPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/StickOnTopPage.ets#L17-L462)

### **动态切换列数**

在应用开发中，开发者需要在列表模式与瀑布流模式间进行切换，或适应屏幕宽度的变化。为解决此类需求，通常通过动态调整瀑布流的列数来实现。建议采用瀑布流的移动窗口布局模式，以实现更快速的列数转换。参考：[动态切换列数](../harmonyos-guides/arkts-layout-development-create-waterflow.md#动态切换列数)。

## 瀑布流滑动

### 滑动性能优化

瀑布流上下滑动时，因其具有无限加载数据的特性，能够展示大量数据。不同大小的子元素将会带来测量和绘制的性能消耗过大。例如，在实际开发中，当瀑布流中的数据量过大时，可能会遇到渲染速度慢、滑动丢帧、内存占用高等问题，这些问题直接影响用户操作体验。为了解决这些开发中可能遇到的性能问题，建议参考[瀑布流优化](bpta-waterflow-performance-optimization.md#section088318458314)。

### 停止滑动时自动播放

在某些开发场景中，开发者可能想要在瀑布流停止滑动时播放其中的视频，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/94n0TXqPQ5eoohcEUULRRg/zh-cn_image_0000002353157698.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=640587993AE7CB1CCC4FEDFACBE3580D31888A1037D01C22273A21B69FC71213 "点击放大")

若要实现上述效果，可利用组件的[onVisibleAreaChange()](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)方法监听组件显示状态，以控制视频播放或暂停。完整代码如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { CommonConstants } from '../common/constants/CommonConstants';
3. import MediaItem, { ItemType } from '../model/MediaItem';
4. import { StickyWaterFlowDataSource } from '../model/StickyWaterFlowDataSource';

6. const TAG: string = 'FlowItemAutoPlayPage';

8. @Component
9. struct FlowVideoItem {
10. @Prop item: MediaItem;
11. controller: VideoController = new VideoController();

13. aboutToReuse(params: Record<string, MediaItem>): void {
14. this.item = params.item as MediaItem;
15. }

17. build() {
18. if (this.item.type === ItemType.VIDEO) {
19. Stack({ alignContent: Alignment.BottomStart }) {
20. Video({ src: this.item.videoUri, previewUri: this.item.videoCover, controller: this.controller })
21. .controls(false)
22. .muted(true)
23. .loop(true)
24. .borderRadius(8)
25. .onVisibleAreaChange([0.0, 1.0], (isVisible: boolean, currentRatio: number) => {
26. // 1、Slide to play the video when visible.
27. if (isVisible && currentRatio >= 1.0) {
28. this.controller.start();
29. }
30. // 2、Slide to pause the video when hidden.
31. if (!isVisible || currentRatio < 1.0) {
32. this.controller.pause();
33. }
34. })
35. Text('NO. ' + (this.item.id + 1))
36. .fontSize(12)
37. .fontColor(Color.White)
38. .margin({
39. left: 8,
40. bottom: 4
41. })
42. }
43. } else {
44. // ...
45. }
46. }
47. }

49. // ...
```

[FlowItemAutoPlayPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/FlowItemAutoPlayPage.ets#L17-L230)

说明

示例代码构建的数据屏幕中仅有一个视频。若屏幕中包含多个视频，滑动停止时需要播放首个完全显示的视频，则需借助WaterFlow的[onScrollIndex()](../harmonyos-references/ts-container-waterflow.md#onscrollindex11)方法，实现相关逻辑。

## 瀑布流数据更新

### **下拉刷新**

在某些应用场景中，开发者可能实现如下图所示的刷新效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/22UGmQPSSBm9YaUlf1a6VA/zh-cn_image_0000002353317494.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=699422856E971673C4813DE991E51B0FAED0EBEAF6E6EFF6B1F4912D054F8AD6 "点击放大")

为了实现上述效果，开发者可通过Refresh组件实现瀑布流下拉刷新。通过Refresh组件进行页面下拉操作，并绑定显示刷新Loading动效的容器组件，以实现下拉刷新效果。随后，在[onRefreshing()](../harmonyos-references/ts-container-refresh.md#onrefreshing)事件中更新数据。完整代码如下：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { CommonConstants } from "../common/constants/CommonConstants";
3. import { SectionsWaterFlowDataSource } from "../model/SectionsWaterFlowDataSource";

5. const TAG: string = 'DataUpdateAndAnimationPage';

7. // ...
8. @Entry
9. @Component
10. struct DataUpdateAndAnimationPage {
11. @State isRefreshing: boolean = false;
12. @State currentItem: number = -1;
13. // ...
14. // 1、Refresh Loading Animation Component.
15. @Builder
16. headerRefresh(): void {
17. Column() {
18. LoadingProgress()
19. .color(Color.Black)
20. .opacity(0.6)
21. .width(36)
22. .height(36)
23. }
24. .justifyContent(FlexAlign.Center)
25. }

27. // 5、Pull down to refresh the data update logic.
28. refresh(): void {
29. this.currentItem = -1;
30. setTimeout(() => {
31. // Add new data.
32. this.dataSource.dataArray = [];
33. let value: number = Math.floor(Math.random() * 100);
34. for (let i: number = 0; i < 100; i++) {
35. this.dataSource.dataArray.push(i + value);
36. this.dataSource.notifyDataAdd(i);
37. }
38. // Update sections itemsCount.
39. this.oneColumnSection.itemsCount = 3;
40. this.oneColumnSection.crossCount = 1;
41. this.twoColumnSection.itemsCount = 2;
42. this.twoColumnSection.crossCount = 2;
43. this.dataSection.itemsCount = 95;
44. this.dataSection.crossCount = 2;
45. this.sections.update(0, this.oneColumnSection);
46. this.sections.update(1, this.twoColumnSection);
47. this.sections.update(2, this.dataSection);
48. this.isRefreshing = false;
49. }, 2000);
50. }

52. loadMore(last: number): void {
53. setTimeout(() => {
54. let totalCount: number = this.dataSource.totalCount();
55. if (last + 20 >= totalCount) {
56. for (let i: number = 0; i < 20; i++) {
57. this.dataSource.addLastItem();
58. }
59. // Update sections itemsCount.
60. this.dataSection.itemsCount += 20;
61. this.sections.update(2, this.dataSection);
62. }
63. }, 1000);
64. }

66. // ...
67. build() {
68. Column({ space: 0 }) {
69. Row() {
70. Text($r('app.string.pull_down_refresh'))
71. .width('100%')
72. .fontSize(24)
73. .fontWeight(FontWeight.Bold)
74. .margin({ top: '18vp', left: '16vp', bottom: '8vp' })
75. }

77. // 2、Pull-to-refresh control.
78. Refresh({ refreshing: $$this.isRefreshing, builder: this.headerRefresh() }) {
79. // ...
80. // For better experience, pre load data.
81. .onScrollIndex((first: number, last: number) => {
82. this.loadMore(last);
83. })
84. }
85. // 3、Pull down to refresh offset.
86. .refreshOffset(56)
87. .onRefreshing(() => {
88. // 4、Pull down to refresh, triggering the refresh callback function.
89. this.refresh();
90. })
91. }
92. .padding({
93. top: this.statusBarHeight
94. })
95. }
96. }
```

[DataUpdateAndAnimationPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/DataUpdateAndAnimationPage.ets#L17-L319)

### **上拉加载**

WaterFlow实现加载更多功能，通常采用onReachEnd回调（[onReachEnd](../harmonyos-references/ts-container-waterflow.md#onreachend)）或onScrollIndex回调（[onScrollIndex](../harmonyos-references/ts-container-waterflow.md#onscrollindex11)）来实现。

1. 在onReachEnd加载数据时，应用会在数据源中的所有数据渲染完成后加载新数据，这会导致明显的加载动画出现，用户需等待新数据加载完毕后才能继续浏览瀑布流。
2. 相比onReachEnd方式，onScrollIndex回调可以在用户滑动到接近底部时预加载数据，实现无缝浏览体验。例如，当前可视区最后一个组件的索引加上20等于数据源总量时，才开始加载数据，这能避免每次索引变化时均加载数据。建议在[onScrollIndex](../harmonyos-references/ts-container-waterflow.md#onscrollindex11)回调中执行此操作，使瀑布流在未触底前即开始加载数据，进而提高用户体验，确保用户几乎不察觉数据加载过程。

   ```
   1. import { hilog } from "@kit.PerformanceAnalysisKit";
   2. import { CommonConstants } from "../common/constants/CommonConstants";
   3. import { SectionsWaterFlowDataSource } from "../model/SectionsWaterFlowDataSource";

   5. const TAG: string = 'DataLoadMorePage';

   7. // ...
   8. @Entry
   9. @Component
   10. struct DataLoadMorePage {
   11. @State sections: WaterFlowSections = new WaterFlowSections();
   12. dataSource: SectionsWaterFlowDataSource = new SectionsWaterFlowDataSource();
   13. // ...
   14. build() {
   15. Column({ space: 0 }) {
   16. Refresh({ refreshing: $$this.isRefreshing, builder: this.headerRefresh() }) {
   17. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
   18. // ...
   19. }
   20. .cachedCount(12)
   21. .columnsGap(8)
   22. .rowsGap(8)
   23. .width('100%')
   24. .height('100%')
   25. .layoutWeight(1)
   26. // For better experience, pre load data.
   27. .onScrollIndex((first: number, last: number) => {
   28. // 1、Obtain the total amount of data in the waterfall flow.
   29. let totalCount: number = this.dataSource.totalCount();
   30. // 2、If the index of the last visible area is greater than the total amount of data, it triggers loading more.
   31. if (last + 20 >= totalCount) {
   32. // 3、Re-add 20 data entries to the waterfall.
   33. for (let i: number = 0; i < 20; i++) {
   34. this.dataSource.addLastItem();
   35. }
   36. // 4、Update the itemsCount in the group and refresh the group information.
   37. this.dataSection.itemsCount += 20;
   38. this.sections.update(2, this.dataSection);
   39. }
   40. })
   41. }
   42. // ...
   43. }
   44. .padding({
   45. top: this.statusBarHeight
   46. })
   47. }
   48. }
   ```

   [DataLoadMorePage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/DataLoadMorePage.ets#L17-L307)

### **增删数据项**

在使用[WaterFlowSections](../harmonyos-references/ts-container-waterflow.md#waterflowsections12)对WaterFlow中的子元素进行分组的场景下，若需删除WaterFlow中的数据，不仅需从数据源中删除数据，还需更新对应section的itemsCount数量，并执行sections.[update()](../harmonyos-references/ts-container-waterflow.md#update12)操作。完整代码如下：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { SectionsWaterFlowDataSource } from "../model/SectionsWaterFlowDataSource";

4. const TAG: string = 'FlowItemRemovePage';

6. // ...
7. @Entry
8. @Component
9. struct FlowItemRemovePage {
10. // 1、Select the index of the FlowItem.
11. @State currentItem: number = -1;
12. // ...
13. removeItem(item: number): void {
14. // 5、Delete source data.
15. let index: number = this.dataSource.indexOf(item);
16. this.dataSource.deleteItem(index);
17. // 6、Update the itemsCount quantity in the group and refresh.
18. const sections: Array<SectionOptions> = this.sections.values();
19. let newSection: SectionOptions;
20. let tmpIndex: number = 0;
21. let sectionIndex: number = 0;
22. for (let i: number = 0; i < sections.length; i++) {
23. tmpIndex += sections[i].itemsCount;
24. if (index < tmpIndex) {
25. sectionIndex = i;
26. break;
27. }
28. }
29. newSection = sections[sectionIndex];
30. newSection.itemsCount -= 1;
31. if (newSection.crossCount && newSection.crossCount > newSection.itemsCount) {
32. newSection.crossCount = newSection.itemsCount;
33. }
34. this.sections.update(sectionIndex, newSection);
35. }

37. build() {
38. Column({ space: 0 }) {
39. Refresh({ refreshing: $$this.isRefreshing, builder: this.headerRefresh() }) {
40. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
41. LazyForEach(this.dataSource, (item: number) => {
42. FlowItem() {
43. Stack() {
44. // 3、Delete button.
45. Row() {
46. Button('Delete')
47. .fontColor(Color.Red)
48. .backgroundColor(Color.White)
49. .onClick(() => {
50. try {
51. this.getUIContext().animateTo({ duration: 300 }, () => {
52. // 4、Trigger delete operation.
53. this.removeItem(item);
54. });
55. } catch (err) {
56. hilog.error(0x0000, TAG, `animateTo get exception, error:${JSON.stringify(err)}.`);
57. }
58. })
59. }
60. .width('100%')
61. .height('100%')
62. .borderRadius(8)
63. .justifyContent(FlexAlign.Center)
64. .zIndex(1)
65. .visibility(this.currentItem === item ? Visibility.Visible : Visibility.Hidden)
66. .backgroundColor('#33000000')

68. ReusableFlowItem({ item: item })
69. }
70. }
71. .transition({ type: TransitionType.Delete, opacity: 0 })
72. // 2、FlowItem's long press event
73. .priorityGesture(LongPressGesture()
74. .onAction(() => {
75. this.currentItem = item;
76. }))
77. .width('100%')
78. .borderRadius(8)
79. .backgroundColor(Color.Gray)
80. }, (item: string) => item)
81. }
82. // ...
83. }
84. }
85. }
```

[FlowItemRemovePage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/FlowItemRemovePage.ets#L17-L302)

## 瀑布流动效

### 删除滑动错位

在某些场景，开发者可能想要删除WaterFlow中的数据后，并且界面还需要显示动画效果，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/9gsPcCGBTj-OWTgYriXO3A/zh-cn_image_0000002387038025.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=ECAE247B2B8EFBE187A010EF80E8C4C173BC2C1ED50AD8E26F82E8F6FFB74C50 "点击放大")

为了实现上图的效果，可通过配置FlowItem的[transition()](../harmonyos-references/ts-transition-animation-component.md)属性并添加转场参数，使组件在插入和删除时显示过渡动画。同时，在删除时添加[animateTo](../harmonyos-references/ts-explicit-animation.md)动画效果即可。完整代码如下：

```
1. import { hilog } from "@kit.PerformanceAnalysisKit";
2. import { CommonConstants } from "../common/constants/CommonConstants";
3. import { SectionsWaterFlowDataSource } from "../model/SectionsWaterFlowDataSource";

5. const TAG: string = 'FlowItemRemoveAnimationPage';

7. // ...
8. @Entry
9. @Component
10. struct FlowItemRemoveAnimationPage {
11. // ...
12. build() {
13. Column({ space: 0 }) {
14. Refresh({ refreshing: $$this.isRefreshing, builder: this.headerRefresh() }) {
15. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
16. LazyForEach(this.dataSource, (item: number) => {
17. FlowItem() {
18. Stack() {
19. Row() {
20. Button($r('app.string.delete'))
21. .fontColor(Color.Red)
22. .backgroundColor(Color.White)
23. .onClick(() => {
24. // 2、Execute the animateTo animation when triggering the delete operation.
25. try {
26. this.getUIContext().animateTo({ duration: 300 }, () => {
27. this.removeItem(item);
28. });
29. } catch (err) {
30. hilog.error(0x0000, TAG, `animateTo get exception, error:${JSON.stringify(err)}.`);
31. }
32. })
33. }
34. // ...
35. }
36. }
37. // 1、Add a transition property to FlowItem and configure the transition parameters.
38. .transition({ type: TransitionType.Delete, opacity: 0 })
39. .priorityGesture(LongPressGesture()
40. .onAction(() => {
41. this.currentItem = item;
42. }))
43. .width('100%')
44. .borderRadius(8)
45. .backgroundColor(Color.Gray)
46. }, (item: string) => item)
47. }
48. // ...
49. }
50. // ...
51. }
52. .padding({
53. top: this.statusBarHeight
54. })
55. }
56. }
```

[FlowItemRemoveAnimationPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/FlowItemRemoveAnimationPage.ets#L17-L308)

### 边缘渐隐

在某些开发场景中，开发者可能需要瀑布流边缘具有渐隐效果，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/j9srD5YNT7-2grt3kG9ahQ/zh-cn_image_0000002386957733.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=5B6EF7D6844B9B519B9FF91DFD35FF88B2FDEA4AB8311CD4E8F6085220E0B35D "点击放大")

该效果可通过WaterFlow组件的[fadingEdge](../harmonyos-references/ts-container-scrollable-common.md#fadingedge14)实现，并通过fadingEdgeLength参数设置边缘渐隐长度。具体代码参考：[设置边缘渐隐效果](../harmonyos-references/ts-container-waterflow.md#示例5设置边缘渐隐效果)。

## 场景案例

### **场景描述**

本案例集成了下拉刷新、预加载、删除错位滑动、滑动吸顶、自动播放等功能，应用于分组混排场景与滑动吸顶场景中。通过上述两场景的开发，可以使开发者更深入地理解WaterFlow在实际应用中的使用方式。

### **关键技术**

1. 实现瀑布流分组混排

   通过创建多个SectionOptions，不同SectionOptions设置不同的宽度和高度，以实现分组混排效果。具体实现参考[瀑布流排版](bpta-waterflow-operations.md#section154611537122218)。
2. 实现下拉刷新/上拉加载更多

   通过Refresh组件和[onScrollIndex()](../harmonyos-references/ts-container-waterflow.md#onscrollindex11)方法实现下拉刷新与上拉加载更多功能。具体实现参考[瀑布流数据更新](bpta-waterflow-operations.md#section193081340162215)。
3. 实现长按删除FlowItem

   通过长按显示删除按钮，执行删除操作时，不仅需删除源数据，还须更新section对应的itemsCount数量，确保分组数据与数据源数据同步。具体实现参考[瀑布流动效](bpta-waterflow-operations.md#section8332244132210)。
4. 实现瀑布流吸顶效果

   通过WaterFlow的[onWillScroll()](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)方法和position属性设置最大滑动偏移量，以实现滑动吸顶效果。具体参考[瀑布流排版](bpta-waterflow-operations.md#section154611537122218)。
5. 实现FlowItem自动播放效果

   通过[onVisibleAreaChange()](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)方法检测组件显示状态，控制FlowItem中视频的播放或暂停。具体参考[瀑布流滑动](bpta-waterflow-operations.md#section119347413579)。

### **实现效果**

最终效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/fF5hu5UuQpqHOF5sAyRUeA/zh-cn_image_0000002353157702.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=F44807A786BE3A82A11F753851D631AD68BE78F82F94A792A3D3CDB9DB1BA726 "点击放大")

## 常见问题

### **如何将多个FlowItem强制显示到左上角位置，如下图所示**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/4rnmuPhsS-OrN6Xb0B8YJg/zh-cn_image_0000002353317498.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=2C4E5FD9A2A775E173D975A2C071164B8FE6B186522337C2EECB60B3566B8D36 "点击放大")

通过在WaterFlow根节点添加FlowItem，将需要显示在左上角的元素放在此FlowItem内部即可，完整代码如下：

```
1. import { CommonConstants } from '../common/constants/CommonConstants';
2. import { MyDataSource } from '../model/MyDataSource'

4. @Entry
5. @Component
6. struct ForceShowOnTopLeftPage {
7. // ...
8. build() {
9. Column({ space: 0 }) {
10. Row() {
11. Text($r('app.string.force_left_show'))
12. .width('100%')
13. .fontSize(24)
14. .fontWeight(FontWeight.Bold)
15. .margin({ top: '18vp', left: '16vp', bottom: '16vp' })
16. }

18. WaterFlow() {
19. // 1、Add the layout content in the top left corner of WaterFlow.
20. FlowItem() {
21. Column() {
22. ForEach(this.data.getTopMastData(5), (item: number) => {
23. Text(`Top Hello ${item}`).fontSize(22)
24. })
25. }
26. .margin({
27. top: 4,
28. bottom: 4
29. })
30. }
31. .width('100%')
32. .alignSelf(ItemAlign.End)
33. .backgroundColor(Color.White)
34. .borderRadius(8)

36. // 2、Add WaterFlow data.
37. LazyForEach(this.data, (item: number, index: number) => {
38. FlowItem() {
39. Row() {
40. Text(`Hello ${item}`).fontSize(20)
41. }
42. }
43. .width('100%')
44. .height(30 + Math.random() * 30)
45. .backgroundColor(Color.White)
46. .borderRadius(8)
47. }, (item: number) => item.toString())
48. }
49. .cachedCount(5)
50. .columnsTemplate('1fr 1fr')
51. .backgroundColor('#efefef')
52. .columnsGap(10)
53. .rowsGap(5)
54. .margin({
55. left: '16vp',
56. right: '16vp'
57. })
58. }
59. .backgroundColor('#efefef')
60. .padding({
61. top: this.statusBarHeight
62. })
63. }
64. }
```

[ForceShowOnTopLeftPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/ForceShowOnTopLeftPage.ets#L17-L91)

### **如何实现双瀑布流衔接效果，如下图所示**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ou458Y25SViYtVEwIlZ-RQ/zh-cn_image_0000002387038029.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=92319B8629989A3F294ECABCAE2555C1B440BE94DACDF941276BEF9908DF76DB "点击放大")

通过WaterFlow的分组能力(SectionOptions)实现。在中间的FlowItem中预留位置显示 "分类信息" ，随后继续填充瀑布流数据。完整代码如下：

```
1. import { CommonConstants } from '../common/constants/CommonConstants';
2. import { MyDataSource } from '../model/MyDataSource'

4. @Entry
5. @Component
6. struct MergeDoubleWaterFlowPage {
7. // ...
8. build() {
9. Column({ space: 2 }) {
10. Row() {
11. Text($r('app.string.merge_double_waterflow'))
12. .width('100%')
13. .fontSize(24)
14. .fontWeight(FontWeight.Bold)
15. .margin({ top: '18vp', left: '16vp', bottom: '12vp' })
16. }

18. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
19. LazyForEach(this.data, (item: number) => {
20. FlowItem() {
21. if (item === 21) {
22. // 1、This is the content for stitching the item.
23. Column() {
24. Text($r('app.string.recommend_goods'))
25. .align(Alignment.Center)
26. .width('100%')
27. .margin({ left: 16, top: 24, bottom: 24 })
28. .fontSize(24)
29. .fontWeight(FontWeight.Bold)
30. }
31. } else {
32. // 2、Other data within WaterFlow.
33. Column() {
34. Text('N ' + item)
35. .fontSize(12)
36. .height('16vp')
37. Image($rawfile(`sections/${item % 4}.jpg`))
38. .objectFit(ImageFit.Cover)
39. .width('100%')
40. .layoutWeight(1)
41. }
42. }
43. }
44. .width('100%')
45. }, (item: number) => item.toString())
46. }
47. .cachedCount(10)
48. .rowsGap(5)
49. .backgroundColor('#efefef')
50. .width('100%')
51. .height('100%')
52. }
53. .padding({
54. top: this.statusBarHeight
55. })
56. .backgroundColor('#efefef')
57. }
58. }
```

[MergeDoubleWaterFlowPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/MergeDoubleWaterFlowPage.ets#L17-L141)

### **如何实现双指缩放动态改变瀑布流列数**，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/R7cz_KvXRESGNO1H1p2aJg/zh-cn_image_0000002386957737.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=20F6CD7D098B52659E0068CC61BFC11A5DA9D4FFEBB8E01EDE3FE70BB7F58DEC "点击放大")

通过监听用户捏合手势并配合缩放比例进行动态控制瀑布流列数。完整代码如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { image } from '@kit.ImageKit';
3. import { CommonConstants } from '../common/constants/CommonConstants';
4. import { MyDataSource } from '../model/MyDataSource'

6. const TAG: string = 'StickOnTopPage';

8. // ...
9. @Entry
10. @Component
11. struct ZoomChangeColumnPage {
12. // ...
13. // 1、Variables required for scaling operations.
14. @State itemScale: number = 1;
15. @State imageScale: number = 1;
16. @State itemOpacity: number = 1;
17. @State gestureEnd: boolean = false;
18. @State pixelMap: image.PixelMap | undefined = undefined;
19. @State columns: number = 4;
20. @StorageProp(CommonConstants.AS_KEY_STATUS_BAR_HEIGHT) statusBarHeight: number = 0;
21. private pinchTime: number = 0;
22. private columnChanged: boolean = false;
23. private oldColumn: number = this.columns;

25. // ...
26. // 7、Adjust the number of columns according to the zoom ratio.
27. changeColumns(scale: number): void {
28. this.oldColumn = this.columns;
29. if (scale > (this.columns / (this.columns - 0.5))) {
30. this.columns--;
31. this.columnChanged = true;
32. } else if (scale < 1 && this.columns < 4) {
33. this.columns++;
34. this.columnChanged = true;
35. }
36. this.columns = Math.min(4, Math.max(1, this.columns));
37. }

39. build() {
40. Column({ space: 2 }) {
41. // ...
42. Stack() {
43. // 2、Display the current screen's snapshot when zooming.
44. Image(this.pixelMap)
45. .width('100%')
46. .height('100%')
47. .scale({
48. x: this.imageScale,
49. y: this.imageScale,
50. centerX: 0,
51. centerY: 0
52. })
53. WaterFlow() {
54. // ...
55. }
56. .id('waterflow')
57. // 3、Dynamic adjustment of column numbers.
58. .columnsTemplate('1fr '.repeat(this.columns))
59. .backgroundColor(0xFAEEE0)
60. .width('100%')
61. .height('100%')
62. .layoutWeight(1)
63. // 4、WaterFlow's scaling information.
64. .opacity(this.itemOpacity)
65. .scale({
66. x: this.itemScale,
67. y: this.itemScale,
68. centerX: 0,
69. centerY: 0
70. })
71. .priorityGesture(
72. PinchGesture()
73. .onActionStart((event: GestureEvent) => {
74. // 5、Initialise scaling parameters.
75. this.gestureEnd = false;
76. this.pinchTime = event.timestamp;
77. this.columnChanged = false;
78. this.getUIContext().getComponentSnapshot().get('waterflow', (error: Error, pixelMap: image.PixelMap) => {
79. if (error) {
80. console.info('error: ' + error.message);
81. return;
82. }
83. this.pixelMap = pixelMap;
84. })
85. })
86. .onActionUpdate((event: GestureEvent) => {
87. // 6、Calculate the zoom ratio based on the finger swipe event and dynamically change the number of columns.
88. // 6.1、Intercept duplicate gestures.
89. if (event.timestamp - this.pinchTime < 10000000) {
90. return;
91. }
92. this.pinchTime = event.timestamp;
93. // 6.2、Calculate the scaling ratio.
94. let maxScale: number = this.oldColumn / (this.oldColumn - 1);
95. this.itemScale = event.scale > maxScale ? maxScale : event.scale;
96. this.imageScale = event.scale > maxScale ? maxScale : event.scale;
97. this.itemOpacity = (this.itemScale > 1) ? (this.itemScale - 1) : (1 - this.itemScale);
98. this.itemOpacity *= 3;
99. // 6.3、Dynamically adjust the number of columns.
100. if (!this.columnChanged) {
101. this.changeColumns(event.scale);
102. }
103. if (this.columnChanged) {
104. this.itemScale = this.imageScale * this.columns / this.oldColumn;
105. if (event.scale < 1) {
106. this.itemScale = this.itemScale > 1 ? this.itemScale : 1;
107. } else {
108. this.itemScale = this.itemScale < 1 ? this.itemScale : 1;
109. }
110. }
111. })
112. .onActionEnd((event: GestureEvent) => {
113. // 8、Reset the relevant scaling parameters and execute the scaling animation.
114. this.gestureEnd = true;
115. try {
116. this.getUIContext().animateTo({ duration: 300 }, () => {
117. this.itemScale = 1;
118. this.itemOpacity = 1;
119. });
120. } catch (err) {
121. hilog.error(0x0000, TAG, `animateTo get exception, error:${JSON.stringify(err)}.`);
122. }
123. AppStorage.setOrCreate<number>('columnsCount', this.columns);
124. })
125. )
126. }
127. .width('100%')
128. .height('100%')
129. }
130. .padding({
131. top: this.statusBarHeight
132. })
133. }
134. }
```

[ZoomChangeColumnPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/WaterFlowSample/entry/src/main/ets/pages/ZoomChangeColumnPage.ets#L17-L226)

## 示例代码

* [实现WaterFlow瀑布流布局功能](https://gitcode.com/harmonyos_samples/water-flow)
