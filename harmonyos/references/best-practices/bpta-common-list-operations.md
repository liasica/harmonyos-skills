---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-common-list-operations
title: 常见列表操作
breadcrumb: 最佳实践 > 布局与弹窗 > 常见列表操作
category: best-practices
scraped_at: 2026-04-29T14:10:34+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:dc15574f0a348377a0f0feb81136f091c84c6798ccc558f1c1f5b9fd48e43aa8
---

## 概述

在应用开发中，列表通常用于展示结构化数据，例如联系人列表、通讯录等。为了提升用户体验和交互效果，开发者需要实现一系列常见的列表操作功能，本文主要介绍列表滚动、列表排版、列表数据更新、列表拖拽等常见功能，通过实现一个简单聊天列表的案例，来介绍常见列表操作以及对应的代码实现。

## 列表滚动

列表滚动是指用户通过上下或左右滚动屏幕来浏览超出当前视口范围的内容，它是最常见的交互方式之一，适用于展示联系人列表、商品目录、新闻文章等多种场景。

### 滚动到指定位置

列表滚动主要通过List组件的scroller参数绑定一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)对象，进行列表的滚动控制。

```
1. private scroller: Scroller = new Scroller();
2. @StorageProp('topRectHeight') topRectHeight: number = 0;

4. // ...
5. List({ space: 20, initialIndex: this.arr.length - 1, scroller: this.scroller }) {
6. // ...
7. }
```

[ScrollToTheBottom.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/ScrollToTheBottom.ets#L20-L48)

根据滚动位置的不同，本文介绍列表滚动常见的三种形式：滚动到底部、滚动到指定索引、指定偏移量滚动，其实现方式如下：

**滚动到底部：**通过initialIndex或者[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)接口实现。

* 使用List组件的[ListOptions对象](../harmonyos-references/ts-container-list.md#listoptions18对象说明)-initialIndex设置列表初始化显示到最后一个ListItem的位置。

  ```
  1. List({ space: 20, initialIndex: this.arr.length - 1, scroller: this.scroller }) {

  3. ForEach(this.arr, (item: number) => {
  4. ListItem() {
  5. // ...
  6. }
  7. .borderRadius(16)
  8. .backgroundColor(0xDCDCDC)
  9. }, (item: string) => item)
  10. }
  ```

  [ScrollToTheBottom.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/ScrollToTheBottom.ets#L29-L49)
* 使用[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)接口实现滚动到最后一个ListItem的索引位置。

  ```
  1. this.scroller.scrollToIndex(this.arr.length - 1);
  ```

  [ScrollToTheBottom.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/ScrollToTheBottom.ets#L56-L56)

  需要注意的是，scrollToIndex与initialIndex都能实现滚动到底部（最后一个ListItem），若ListItem高度过高则不能展示到最底部，可以搭配使用[scrollEdge()](../harmonyos-references/ts-container-scroll.md#scrolledge)滚动到列表底部。

  ```
  1. this.scroller.scrollEdge(Edge.Bottom);
  ```

  [ScrollToTheBottom.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/ScrollToTheBottom.ets#L59-L59)

**滚动到指定索引：**通过[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)接口滚动到列表数组的指定索引Index。

说明

在使用scrollToIndex()等场景时，若滚动过程中ListItem大小动态变化，将会导致获取到的currentOffset不准确，无法准确的跳转到指定位置。可以使用[childrenMainSize()](../harmonyos-references/ts-container-list.md#childrenmainsize12)给ListItem固定高度，该属性通过向List组件提供所有子组件在主轴方向的大小信息，确保List组件能够维护其滚动位置准确性。

**指定偏移量滚动：**通过[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)接口实现，可以配置上下偏移量、左右偏移量以及动画方式。

```
1. Button('scroll 200')
2. .height('5%')
3. .onClick(() => {
4. let curve = curves.interpolatingSpring(10, 1, 228, 30);
5. const yOffset: number = this.scroller.currentOffset().yOffset;
6. this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 200, animation: { duration: 1000, curve: curve } })
7. })
```

[RollingMonitoring.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/RollingMonitoring.ets#L27-L33)

说明

需要注意的是，这里的偏移量是相对于组件最顶端的偏移量，并非相对于当前显示Item的偏移量。

### 滚动监听

当列表项过多时，通常需要监听列表的滚动偏移量，基于此来展示额外信息或辅助功能。例如，在选择商品时，滚动至一定距离后，用户希望能返回顶部，就需要进行滚动监听。通过在List组件的[onWillScroll()](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)或者[onDidScroll()](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)方法里面执行scroller.currentOffset()实时监听位移偏移量。

```
1. .onWillScroll(() => {
2. // Trigger before scrolling component scrolling.
3. console.info('currentOffset:' + this.scroller.currentOffset().yOffset)
4. })
5. .onDidScroll(() => {
6. // Triggered when scrolling components scroll.
7. console.info('currentOffset:' + this.scroller.currentOffset().yOffset)
8. })
```

[RollingMonitoring.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/RollingMonitoring.ets#L64-L71)

说明

scroller.currentOffset()偏移量是相对于组件最顶端的偏移量，并非相对于当前显示Item的偏移量。如果想要获取此次滚动偏移量，可以通过onWillScroll()或者onDidScroll()接口的回调参数获取。onwillscroll()中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。具体可参考：[设置scroller控制器](../harmonyos-references/ts-container-scroll.md#示例1设置scroller控制器)。

### 嵌套滚动

嵌套滚动是指多个滚动容器相互嵌套，并能协同工作的滚动机制。例如：在移动端应用中，一个页面整体可以垂直滚动，而其中某个子组件（如Tab内容、评论区、图片列表）也只支持独立滚动。根据滚动对象的不同，嵌套滚动主要分为Scroll组件嵌套List组件、Web组件嵌套List组件、List组件嵌套List组件等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/KLZAyN83QXiA2wPtNU5lpw/zh-cn_image_0000002361711474.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=88B8FE6E38C7211C7F73903872CE5C89B7308D682B10ACF234877918B61BCE00 "点击放大")

* [List组件与Scroll组件的嵌套滚动](../harmonyos-references/ts-container-scroll.md#示例2嵌套滚动实现方式一)
* [Web组件与List组件嵌套](../harmonyos-guides/web-nested-scrolling.md#滚动偏移量由滚动父组件统一派发)
* [List组件与List组件嵌套滚动](../harmonyos-faqs/faqs-arkui-337.md)

说明

若通过[onScrollFrameBegin()](../harmonyos-references/ts-container-scroll.md#onscrollframebegin9)事件和[scrollBy()](../harmonyos-references/ts-container-scroll.md#scrollby9)方法实现容器嵌套滚动，需设置子滚动节点的[EdgeEffect()](../harmonyos-references/ts-container-scrollable-common.md#edgeeffect11)为None。如Scroll嵌套List滚动时，List组件的edgeEffect属性需设置为EdgeEffect.None。

### 滚动效果

列表滚动效果指的是当用户通过上下或左右滚动屏幕来浏览超出当前视口范围的内容时，列表项如何平滑地进入和离开视口，以及在此过程中可能伴随的视觉效果，例如单边回弹、滚动过程中禁用滚动、列表项左滑等**。**

**单边回弹效果：**

单边回弹是指当用户滚动到可滚动区域的一端时，如果继续施加力，该端会出现一种视觉上的“回弹”效果，例如实现顶部回弹效果，可以有2种方式实现：

* 在[onDidScroll()](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)里获取currentOffset().yOffset，然后拿获取的值与0比较，当其值小于等于0时，说明已到达或超越顶部，此时设置[EdgeEffect](../harmonyos-references/ts-container-scrollable-common.md#edgeeffect11)属性设置边缘滚动效果。

  ```
  1. List({ space: 20, initialIndex: 0, scroller: this.scroller }) {
  2. // ...
  3. }
  4. .width('90%')
  5. .scrollBar(BarState.Off)
  6. .onDidScroll(() => {
  7. const y = this.scroller.currentOffset().yOffset;
  8. this.isTop = y <= 0;
  9. })
  10. .edgeEffect(this.isTop ? EdgeEffect.Spring : EdgeEffect.None)
  ```

  [UnilateralRebound.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/UnilateralRebound.ets#L26-L50)
* 通过[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)实现单边回弹效果，List显示区域内第一个子组件的索引值为0时，说明已到达顶部，此时设置[EdgeEffect](../harmonyos-references/ts-container-scrollable-common.md#edgeeffect11)属性设置边缘滚动效果。

  ```
  1. .edgeEffect(this.isTop ? EdgeEffect.Spring : EdgeEffect.None)
  2. .onScrollIndex((firstIndex: number) => {
  3. this.isTop = firstIndex === 0;
  4. console.info('firstIndex:' + firstIndex + ',' + this.isTop)
  5. })
  ```

  [UnilateralRebound.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/UnilateralRebound.ets#L50-L56)

当List组件内容大小小于组件自身时，默认不开启滚动效果，可以设置[edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })](../harmonyos-references/ts-container-scrollable-common.md#edgeeffect11)开启滚动效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/CUgR73IKTIOEPNq3bA3Qrg/zh-cn_image_0000002395231413.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=04C722B05AE215A89261859A289328008B9670D9F3298A0AFC37FA08E6FC33F1 "点击放大")

**滚动过程中禁用滚动：**可以通过enabled(false)关闭滚动使能，但是如果是惯性滚动触发的，List仍然能依靠惯性滚动一段距离。如果想要实现禁用滚动及惯性滚动，可使用以下2种方式：

* 设置[enableScrollInteraction(false)](../harmonyos-references/ts-container-list.md#enablescrollinteraction10)来禁用List滚动。
* 在列表开始滚动时触发[onScrollFrameBegin](../harmonyos-references/ts-container-list.md#onscrollframebegin9)事件，事件参数传入即将发生的滚动量，在事件处理函数中根据应用场景计算实际需要的滚动量，并将其作为事件处理函数的返回值返回，列表将按照返回值的实际滚动量进行滚动，例如，可以将返回值设置为0，则表示不滚动。

  ```
  1. .onScrollFrameBegin((offset: number, state: ScrollState) => {
  2. return { offsetRemain: 0 } // If the return value is set to 0, it means that there will be no scrolling.
  3. })
  ```

  [EdgeBlur.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/EdgeBlur.ets#L55-L57)

**列表项左滑：**通过给列表项ListItem添加SwiperAction组件实现，可以实现左滑删除、置顶等功能。具体实现方案和示例代码请参见下一章节[案例一：实现简单聊天列表](bpta-common-list-operations.md#section312414023718)中的左滑删除/置顶。

**循环滚动：**当用户滚动到列表的末尾或开头时，列表会自动循环回到开头或结尾。例如，实现一个可左右滑动的循环滚动列表，可以通过[onScrollFrameBegin](../harmonyos-references/ts-container-list.md#onscrollframebegin9)事件计算当前的滚动偏移量和即将发生的滚动量之和，与ListItem的总宽度作比较，从而判断用户是左滑还是右滑，计算出列表滚动时实际需要的滚动量，示例代码如下：

```
1. .onScrollFrameBegin((offset: number, state: ScrollState) => {
2. let currentOffset = this.scroller.currentOffset().xOffset;
3. let newOffset = currentOffset + offset;
4. let totalWeight = 220 * 10; // The total width of LIST.
5. if (newOffset < totalWeight * 0.5) {
6. newOffset += totalWeight;
7. } else if (newOffset > totalWeight * 2.5) {
8. newOffset -= totalWeight;
9. }
10. return { offsetRemain: newOffset - currentOffset };
11. })
```

[LoopScrolling.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/LoopScrolling.ets#L142-L153)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/v7BfbPoSQKe66LhKsIKP6Q/zh-cn_image_0000002361871362.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=52EEA621B8FC2471394E7AB81B2D1D6FB023B7D8FF5DBB916722F199FA38D333 "点击放大")

## 列表排版

列表排版是指根据数据内容或使用场景，将一组相似或相关的列表项（如消息、商品等）按照一定的布局方式进行排列，以便用户能够快速识别并操作列表项。

### 列表内容显示

列表内容显示的方式决定了用户能否快速获取信息，直接影响整体的视觉体验和交互效率。主要包括边栏索引、列表底部留白、列表吸顶、边缘模糊效果等，具体说明和实现方式如下：

**边栏索引：**可以通过监听List组件的onScrollIndex事件来实现，右侧索引栏需要使用字母表索引组件[AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md)。具体请参见：[响应滚动位置](../harmonyos-guides/arkts-layout-development-create-list.md#响应滚动位置)

**列表底部留白：**可以通过[contentEndOffset](../harmonyos-references/ts-container-list.md#contentendoffset11)设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。

**列表吸顶：**List组件的sticky属性配合ListItemGroup组件使用，用于设置ListItemGroup中的头部组件是否呈现吸顶效果或者尾部组件是否呈现吸底效果。通过给List组件设置sticky属性为StickyStyle.Header，即可实现列表的粘性标题效果。如果需要支持吸底效果，可以通过footer参数初始化ListItemGroup的底部组件，并将sticky属性设置为StickyStyle.Footer。具体请参见：[添加粘性标题](../harmonyos-guides/arkts-layout-development-create-list.md#添加粘性标题)

**边缘模糊效果：**例如实现List上下渐隐效果，可以在List组件上添加overlay浮层，通过linearGradient属性给overlay叠加模糊渐变效果实现。

```
1. @Builder
2. overlayBuilder() {
3. Stack().width('100%').height('100%')
4. .linearGradient({
5. direction: GradientDirection.Bottom, // Gradient direction.
6. colors: [[0x00000000, 0.0], [0xB3000000, 1.0]]
7. })
8. .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN)
9. }

11. build() {
12. NavDestination() {
13. List({ space: 20, initialIndex: 0 }) {
14. ForEach(this.arr, (item: number) => {
15. ListItem() {
16. Text('' + item)
17. .width('100%')
18. .height(100)
19. .fontSize(16)
20. .textAlign(TextAlign.Center)
21. .borderRadius(16)
22. .backgroundColor(0xDCDCDC)
23. }
24. .borderRadius(16)
25. .backgroundColor(0xDCDCDC)
26. }, (item: string) => item)
27. }
28. .overlay(this.overlayBuilder())
```

[EdgeBlur.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/EdgeBlur.ets#L23-L50)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/HOp-8m-sSMa4o71d8pVULw/zh-cn_image_0000002395391277.png?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=D288E9272CEC56F5AFFD310012CF8E21C428B74E6FF8375D32198008B7C24B6D "点击放大")

**折叠展开：**列表项的折叠与展开用途广泛，常用于信息清单的展示、填写等应用场景。通过改变ListItem的状态，来控制每个列表项是否展开，并通过animation和animateTo来实现展开与折叠过程中的动效效果。具体请参见：**[折叠与展开](../harmonyos-guides/arkts-layout-development-create-list.md#折叠与展开)**

## 列表数据更新

列表数据更新操作通常包含列表刷新方式、增删列表项以及在数据刷新时，可能需要保持可见区域内容位置不变，其对应的具体说明和实现方式可参考如下。

### 列表刷新

列表刷新指的是在不重新加载整个页面或组件的前提下，根据新的数据源动态地对列表内容进行刷新、替换或局部更新，主要方式包括上拉加载、下拉刷新、左右滚动刷新、局部数据刷新。

**上拉加载：**在列表底部添加LoadingProgress()组件用于显示加载动画，并在onScrollIndex()回调中判断显示区域是否到底，当显示到底时加载更多数据。示例如下：

```
1. List({ space: 20 }) {
2. ForEach(this.arr, (item: number) => {
3. ListItem() {
4. Text('' + item)
5. .width('100%')
6. .height(100)
7. .fontSize(16)
8. .textAlign(TextAlign.Center)
9. .borderRadius(16)
10. .backgroundColor(0xDCDCDC)
11. }
12. }, (item: string) => item)
13. ListItem() {
14. Row() {
15. LoadingProgress().height(32).width(48)
16. Text('加载中')
17. }
18. }
19. .width('100%')
20. .height(64)
21. }
22. .width('90%')
23. .onScrollIndex((start: number, end: number) => {
24. if (end > this.arr.length) {
25. setTimeout(() => {
26. for (let i = 0; i < 5; i++) {
27. this.arr.push(this.arr.length);
28. }
29. })
30. }
31. })
```

[PullUpLoading.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/PullUpLoading.ets#L45-L75)

**下拉刷新：**可通过[Refresh](../harmonyos-references/ts-container-refresh.md)容器进行页面下拉操作并绑定显示刷新动效的容器组件，实现下拉刷新效果。具体实现方案和示例代码请参见下一章节[案例一：实现简单聊天列表](bpta-common-list-operations.md#section312414023718)中的下拉加载更多聊天记录。

**左右滚动刷新：**由于refresh没有横滑交互，可以使用Column容器包裹refresh，然后给Column容器设置rotate属性使其旋转90度。

```
1. Column() {
2. Refresh({ refreshing: $$this.isRefreshing }) {
3. List({ space: 10 }) {
4. ForEach(this.arr, (item: number) => {
5. ListItem() {
6. Text('' + item)
7. .width(300)
8. .height(80)
9. .fontSize(16)
10. .textAlign(TextAlign.Center)
11. .borderRadius(16)
12. .backgroundColor(0xFFFFFF)
13. .translate({ x: (80 - 300) / 2 })
14. .rotate({
15. x: 0,
16. y: 0,
17. z: 1,
18. centerX: '50%',
19. centerY: '50%',
20. angle: 90
21. })
22. }
23. .width(80)
24. .height(300)
25. }, (item: string) => item)
26. }
27. .width(300)
28. .height(300)
29. .alignListItem(ListItemAlign.Center)
30. .scrollBar(BarState.Off)
31. }
32. .onRefreshing(() => {
33. setTimeout(() => {
34. this.isRefreshing = false;
35. }, 2000)
36. })
37. .backgroundColor(0xDCDCDC)
38. .refreshOffset(64)
39. .pullToRefresh(true)
40. }
41. .justifyContent(FlexAlign.Center)
42. .width('100%')
43. .height('100%')
44. .rotate({
45. x: 0,
46. y: 0,
47. z: 1,
48. centerX: '50%',
49. centerY: '50%',
50. angle: -90
51. })
```

[ScrollLeftAndRightToRefresh.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/ScrollLeftAndRightToRefresh.ets#L25-L76)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/0-OIb0-QQ1W_waAazjkoZw/zh-cn_image_0000002361711486.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=F839DBB5F19C785B13B6F69F254A25D4839DF024D6284FE03124557E1474750C "点击放大")

**局部数据刷新：**通过直接修改单一ListItem的数据源即可实现。

```
1. Button('Partial_Refresh')
2. .height('5%')
3. .margin({ top: 8, bottom: 8 })
4. .onClick(() => {
5. this.arr[0] += 10;
6. })
```

[RollingMonitoring.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/RollingMonitoring.ets#L37-L42)

### 增删列表项

增删列表项是指用户可以动态地向列表中添加新项或从列表中删除已有项，通常伴随着数据更新与界面刷新。使用数组的Push()、Pop()或splice()等方法即可实现插入列表项、删除列表项、删除ListItem子元素等操作。

```
1. public addData(index: number, data: TextClass): void {
2. this.dataArray.splice(index, 0, data);
3. this.notifyDataAdd(index);
4. }

6. public pushData(data: TextClass): void {
7. this.dataArray.push(data);
8. this.notifyDataAdd(this.dataArray.length - 1);
9. }
```

[MaintainVisibleAreaContent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/MaintainVisibleAreaContent.ets#L86-L95)

### 保持可见区域内容

保持可见区域内容是指在用户滚动列表时，确保当前正在查看的内容不会因为数据更新、界面刷新或组件重新渲染而被替换或消失。例如在一些动态更新的列表中，如聊天消息、任务状态更新、股票行情等，如果每次更新都重新加载整个列表，可能会导致用户正在查看的内容被顶上去或消失，造成体验中断。针对此需求，主要有两种解决方案，参考如下：

**方案一：**使用[maintainVisibleContentPosition](../harmonyos-references/ts-container-list.md#maintainvisiblecontentposition12)设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。需要注意的是，此方案只有在[LazyForEach：数据懒加载](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)场景下才能生效。

```
1. List({ space: 3 }) {
2. LazyForEach(this.data, (item: TextClass) => {
3. ListItem() {
4. Row() {
5. Text(item.message).fontSize(20)
6. }
7. .height(50)
8. .margin({ left: 10, right: 10 })
9. }
10. }, (item: TextClass) => JSON.stringify(item))
11. }
12. .width('100%')
13. .height('100%')
14. .scrollBar(BarState.Off)
15. .maintainVisibleContentPosition(true)
```

[MaintainVisibleAreaContent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/SimpleChatList/entry/src/main/ets/pages/MaintainVisibleAreaContent.ets#L122-L137)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/dH0KzyDRTnKCIqo5SIvKjg/zh-cn_image_0000002395231433.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=7ED63BED86696736EA60F470DBFF94CD349D07A1F4CD0303936FBE2BCA0DDA18 "点击放大")

**方案二：**可以给List添加scroller控制器，将列表跳回至原先所在位置this.scroller.scrollToIndex，具体请参考示例：[List的下拉加载如何回滚到当前展示位置](../harmonyos-faqs/faqs-arkui-268.md)

## 列表拖拽

列表拖拽指的是用户通过长按或点击并拖动某个列表项ListItem，将其移动到另一个位置或区域的操作。这种交互通常用于列表项优先级调整、列表排序等。可以通过List组件的拖拽方法[onItemDragStart()](../harmonyos-references/ts-container-list.md#onitemdragstart8)和[onItemDragMove()](../harmonyos-references/ts-container-list.md#onitemdragmove8)方法，在列表开始拖拽时和拖拽状态的回调中处理被拖拽的ListItem，当结束拖拽时，在新的位置或区域插入ListItem。具体实现方案和示例代码请参见下一章节[案例一：实现简单聊天列表](bpta-common-list-operations.md#section312414023718)中的消息列表拖拽排序。

## 列表场景案例

本章节包含实现简单聊天列表和常见列表流这两个案例，主要通过实现简单聊天列表来介绍列表常见操作、实现方案以及代码实现。

### 案例一：实现简单聊天列表

**场景描述**

常见聊天界面主要包含联系人消息界面以及聊天窗口界面。其中，联系人列表界面主要支持以下交互场景：

* 左滑操作，用于删除或置顶联系人
* 滚动后点击“回到顶部”按钮快速跳转
* 拖拽调整联系人排序

聊天窗口界面则包含以下功能：

* 初始化时自动定位到底部消息
* 支持下拉加载历史聊天记录
* 实时新增并展示最新聊天内容

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/n9orVuUWTx2Qn59HAIERbw/zh-cn_image_0000002361871382.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=E2223A4D02CA777C312397916681CA9BA033B355382B870FFB3B61788EFBD51D "点击放大")

**消息气泡**

在ListItem中使用[Badge](../harmonyos-references/ts-container-badge.md)组件可实现给列表项添加标记功能。Badge是可以附加在单个组件上用于信息标记的容器组件。例如，在消息列表中，若希望在联系人头像右上角添加标记，可在实现消息列表项ListItem的联系人头像时，将头像Image组件作为Badge的子组件。在Badge组件中，count和position参数用于设置需要展示的消息数量和提示点显示位置，还可以通过style参数灵活设置标记的样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/GRANtCyHR-2mfY2zE766bA/zh-cn_image_0000002395391281.png?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=33E15AFFA1EFD8B8B400302C7F92D54AE62D058F3352256406D15BE391C76E93 "点击放大")

**实现方案**

定义一个变量isNewMessage来标识是否需要给列表项添加标记功能，然后使用[Badge](../harmonyos-references/ts-container-badge.md)组件给列表项添加标记功能。

**示例代码**

```
1. if (item.isNewMessage) {
2. // The Badge component can be used to add tags to list items.
3. Badge({
4. value: '',
5. position: BadgePosition.RightTop,
6. style: { badgeSize: 8, badgeColor: '#FA2A2D' }
7. }) {
8. Image(item.image)
9. .width(48)
10. .height(48)
11. }
12. } else {
13. Image(item.image)
14. .width(48)
15. .height(48)
16. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L154-L169)

**左滑删除/置顶**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/EA8fFsLfTRaWUoGqe7ULtQ/zh-cn_image_0000002361711502.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=A76BCC44BAF22F45E46F0DF51C2092BA1448DD0A5BA046B6D465948E27BFBE12 "点击放大")

**实现方案**

使用组件swipeAction实现ListItem左滑划出组件，然后实现一个左滑区域内容显示的组件itemEnd，将其绑定到swipeAction上。

* 实现ListItem置顶，为每个ListItem定义一个变量isTop用于标记是否置顶，然后设置一个排序方式实现置顶项优先显示。
* 实现ListItem删除，利用Item数组自带的splice方法删除指定index的ListItem。

**示例代码**

```
1. @Builder
2. itemEnd(item: Item, index: number) {
3. Row() {
4. Image($r(item.isTop ? 'app.media.up_off' : 'app.media.up_on'))
5. .width(24)
6. .height(24)
7. .margin({ right: 8 })
8. .onClick(() => {
9. this.toggleTop(item);
10. })
11. Image($r('app.media.delete'))
12. .width(24)
13. .height(24)
14. .onClick(() => {
15. this.sortedList.splice(index, 1);
16. })
17. }
18. .padding(4)
19. .height('100%')
20. .backgroundColor('#F1F3F5')
21. .justifyContent(FlexAlign.SpaceEvenly)
22. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L120-L142)

```
1. .swipeAction({
2. end: {
3. builder: () => {
4. this.itemEnd(item, index);
5. },
6. actionAreaDistance: 56,
7. onAction: () => {
8. this.getUIContext().animateTo({ duration: 1000 }, () => {
9. this.sortedList.splice(index, 1);
10. })
11. }
12. },
13. edgeEffect: SwipeEdgeEffect.Spring
14. })
```

[Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L218-L232)

**滚动后跳转到指定位置**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/MnoLSkC-Twu1rQ6NA5aNCA/zh-cn_image_0000002395231445.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=82A09008E9C220E6C0B52C87B63E8BD1F5B4EBFD6AA1EDEE12D97DC179C26EC9 "点击放大")

**实现方案**

以滚动后跳转到顶部为例，在回调.onWillScroll()中通过scroll组件自带的接口currentOffset()获取当前滚动偏移量，将偏移量与临界值进行对比，当超过临界值时显示按钮，点击后调用scrolltoindex(0)即可跳转到顶部。

**示例代码**

```
1. .onWillScroll(() => {
2. if (this.scroller.currentOffset().yOffset > 100) {
3. this.isFlag = true;
4. } else {
5. this.isFlag = false;
6. }
7. })
```

[Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L242-L248)

```
1. if (this.isFlag) {
2. Image($r('app.media.arrow_up_circle_fill'))
3. .width(36)
4. .height(36)
5. .margin({ right: 10, bottom: 10 })
6. .onClick(() => {
7. this.scroller.scrollToIndex(0, true);
8. this.isFlag = false;
9. })
10. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L287-L296)

**消息列表拖拽排序**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/igh4R5biSjWHfl8AnMYsYw/zh-cn_image_0000002361871390.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=63293E1521008D90ACCEC39DC58A6ED7096A1E118B4C37C4BF22F4C20E26CE48 "点击放大")

**实现方案**

通过List组件的拖拽方法onItemDragStart()和onItemDragMove()方法，主要步骤如下：

1. 开始拖拽列表元素时，[onItemDragStart()](../harmonyos-references/ts-container-list.md#onitemdragstart8)方法被触发，在回调里记录当前拖拽的ListItem并赋值给自定义对象dragItem，返回并展示拖拽时的UI函数dragFloatView()。

   ```
   1. .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
   2. // Triggered when starting to drag and drop list elements.
   3. this.dragItem = this.sortedList[itemIndex];
   4. return this.dragFloatView(this.sortedList[itemIndex]);
   5. })
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L254-L258)
2. 拖拽列表元素在列表范围内移动时触发[onItemDragMove()方法](../harmonyos-references/ts-container-list.md#onitemdragmove8)，在回调里分别记录被拖拽ListItem的索引deleteIndex和拖拽插入位置索引insertIndex，然后通过Item数组的splice方法删除被拖拽的ListItem，同时将被删除的ListItem添加至insertIndex所在的位置。

   ```
   1. .onItemDragMove((event: ItemDragInfo, itemIndex: number, insertIndex: number) => {
   2. // Triggered when dragging and moving within the range of a list element.
   3. this.getUIContext().animateTo({ duration: 200, curve: Curve.Linear }, () => {
   4. let deleteIndex = this.sortedList.indexOf(this.dragItem);
   5. this.sortedList.splice(deleteIndex, 1);
   6. this.sortedList.splice(insertIndex, 0, this.dragItem);
   7. })
   8. })
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L261-L268)
3. 定义一个dragFloatView[自定义构建函数](../harmonyos-guides/arkts-builder.md#私有自定义构建函数)作为拖拽时临时展示的UI元素，直至拖拽结束。

   ```
   1. @Builder
   2. dragFloatView(item: Item) {
   3. Row() {
   4. if (item.isNewMessage) {
   5. Badge({
   6. value: '',
   7. position: BadgePosition.RightTop,
   8. style: { badgeSize: 8, badgeColor: '#FA2A2D' }
   9. }) {
   10. Image(item.image)
   11. .width(48)
   12. .height(48)
   13. }
   14. } else {
   15. Image(item.image)
   16. .width(48)
   17. .height(48)
   18. }

   20. Row() {
   21. Column() {
   22. Text(item.name)
   23. .fontSize(16)
   24. .fontWeight(FontWeight.Bold)
   25. .margin({ bottom: 8 })
   26. .textAlign(TextAlign.Start)
   27. Text(item.message[item.message.length - 1].msg)
   28. .fontSize(16)
   29. .maxLines(1)
   30. .constraintSize({ maxWidth: '70%' })
   31. .textOverflow({ overflow: TextOverflow.Ellipsis })
   32. }
   33. .height('100%')
   34. .justifyContent(FlexAlign.Center)
   35. .alignItems(HorizontalAlign.Start)

   37. Text(item.time)
   38. .fontSize(12)
   39. .margin({ bottom: 20 })
   40. .fontColor(item.isTop ? Color.Black : Color.Gray)
   41. }
   42. .width('80%')
   43. .justifyContent(FlexAlign.SpaceBetween)
   44. }
   45. .width('100%')
   46. .height(72)
   47. .backgroundColor(item.isTop ? '#4497FF' : 'rgba(240,240,240,1)')
   48. .justifyContent(FlexAlign.SpaceAround)
   49. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L67-L116)
4. 在拖拽时，被拖拽的ListItem若与记录的dragItem相同，则对其隐藏，避免页面中同时出现相同的ListItem。

   ```
   1. .visibility(item == this.dragItem ? Visibility.Hidden : Visibility.Visible)
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/Index.ets#L210-L210)

**初始化显示到底部**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Wbg2DLcLTAWHq6mzr8_dLQ/zh-cn_image_0000002395391293.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=CB68BB985450074672D165FB6594B20325C55A9EC260488B5B6CBB6B2C246D03 "点击放大")

**实现方案**

通过设置参数initialIndex为消息列表的最大长度，此时只是实现了显示到最后一条，还不能达到预期效果。当遇到超长item时，会从最后一条的顶部开始显示，并不能直接显示到底部。还需要在List组件挂载显示后触发的[onAppear()](../harmonyos-references/ts-universal-events-show-hide.md#onappear)回调中通过ScrollEdge(Edge.Bottom)跳转至最底部。

**示例代码**

```
1. List({ space: 10, scroller: this.scroller, initialIndex: this.itemInfo.message.length - 1 }) {
2. ForEach(this.showItemMessage, (item: messageObj, index: number) => {
3. ListItem() {
4. if (item.sender === 'others') {
5. Row() {
6. Image(this.itemInfo.image)
7. .width(36)
8. .height(36)
9. .margin({ right: 8 })

11. Text(item.msg)
12. .fontSize(16)
13. .constraintSize({ maxWidth: '70%' })
14. .backgroundColor('#F1F3F5')
15. .borderRadius(12)
16. .padding({
17. top: 8,
18. bottom: 8,
19. left: 12,
20. right: 12
21. })
22. }
23. .width('100%')
24. .constraintSize({ minHeight: 48 })
25. .justifyContent(FlexAlign.Start)
26. } else {
27. Row() {
28. Text(item.msg)
29. .fontSize(16)
30. .backgroundColor('#F1F3F5')
31. .borderRadius(12)
32. .padding({
33. top: 8,
34. bottom: 8,
35. left: 12,
36. right: 12
37. })
38. Image($r('app.media.Public_avatar'))
39. .width(36)
40. .height(36)
41. .margin({ left: 8 })
42. }
43. .width('100%')
44. .height(48)
45. .justifyContent(FlexAlign.End)
46. }
47. }
48. })
49. }
50. .onAppear(() => {
51. // Initialize display to the bottom.
52. this.scroller.scrollEdge(Edge.Bottom);
53. })
```

[ChatPage.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/ChatPage.ets#L57-L109)

**下拉加载更多聊天记录**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/n_0TnpxQTp2WqmQJXI7AhA/zh-cn_image_0000002361711514.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=A79B81F10F84B715EE77A149DB2830CA9C72BF9DDF2EE91B9A0F2B9E7709488A "点击放大")

**实现方案**

可以使用[Refresh](../harmonyos-references/ts-container-refresh.md)容器组件包裹List组件进行页面下拉操作，进入刷新状态时触发[onRefreshing()](../harmonyos-references/ts-container-refresh.md#onrefreshing)回调，并在其中添加数据更新的操作，实现下拉刷新页面的功能。

**示例代码**

```
1. Refresh({ refreshing: $$this.isRefreshing }) {
2. List({ space: 10, scroller: this.scroller, initialIndex: this.itemInfo.message.length - 1 }) {
3. ForEach(this.showItemMessage, (item: messageObj, index: number) => {
4. ListItem() {
5. if (item.sender === 'others') {
6. Row() {
7. Image(this.itemInfo.image)
8. .width(36)
9. .height(36)
10. .margin({ right: 8 })

12. Text(item.msg)
13. .fontSize(16)
14. .constraintSize({ maxWidth: '70%' })
15. .backgroundColor('#F1F3F5')
16. .borderRadius(12)
17. .padding({
18. top: 8,
19. bottom: 8,
20. left: 12,
21. right: 12
22. })
23. }
24. .width('100%')
25. .constraintSize({ minHeight: 48 })
26. .justifyContent(FlexAlign.Start)
27. } else {
28. Row() {
29. Text(item.msg)
30. .fontSize(16)
31. .backgroundColor('#F1F3F5')
32. .borderRadius(12)
33. .padding({
34. top: 8,
35. bottom: 8,
36. left: 12,
37. right: 12
38. })
39. Image($r('app.media.Public_avatar'))
40. .width(36)
41. .height(36)
42. .margin({ left: 8 })
43. }
44. .width('100%')
45. .height(48)
46. .justifyContent(FlexAlign.End)
47. }
48. }
49. })
50. }
51. .onAppear(() => {
52. // Initialize display to the bottom.
53. this.scroller.scrollEdge(Edge.Bottom);
54. })
55. .scrollBar(BarState.Off)
56. .contentEndOffset(8)
57. .width('100%')
58. .height('100%')
59. }
60. .width('100%')
61. .height('100%')
62. .refreshOffset(64)
63. .pullToRefresh(true)
64. .onRefreshing(() => {
65. setTimeout(() => {
66. this.getLastTenElements(this.itemMessage);
67. this.isRefreshing = false;
68. }, 1500)
69. })
```

[ChatPage.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/ChatPage.ets#L55-L126)

**新增聊天记录**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/TBmxgaCYQt2HNaYRUF_Dkg/zh-cn_image_0000002395231449.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061026Z&HW-CC-Expire=86400&HW-CC-Sign=8E5B25B223243AC42F21189C81AC546E7B41F0C91279C04C7C35F5FD300C5C45 "点击放大")

**实现方案**

通过TextInput组件获取聊天键盘内容，使用新增列表项push()接口将消息添加到聊天记录中。

**示例代码**

```
1. TextInput({ placeholder: 'input your word...', text: this.inputMessage })
2. .height(40)
3. .width(200)
4. .margin({
5. left: 12,
6. right: 12
7. })
8. .onBlur(() => {
9. this.scroller.scrollEdge(Edge.Bottom);
10. })
11. .onChange((value) => {
12. this.inputMessage = value;
13. })
```

[ChatPage.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/ChatPage.ets#L151-L163)

点击图标发送消息，通过数组的push()方法将输入的内容添加至List数据源itemMessage数组中，然后调用scrollEdge(Edge.Bottom)使List滚动到底部，同时清空输入框的内容。

```
1. Image(this.inputMessage === '' ? $r('app.media.send_off') : $r('app.media.send_on'))
2. .width(28)
3. .height(28)
4. .onClick(() => {
5. if (this.inputMessage.trim() === '') {
6. return;
7. }
8. this.itemMessage.push({
9. sender: 'myself',
10. msg: this.inputMessage
11. });
12. this.showItemMessage = this.itemMessage.slice(-10);
13. this.scroller.scrollEdge(Edge.Bottom);
14. this.inputMessage = '';
15. })
```

[ChatPage.ets](https://gitcode.com/harmonyos_samples/simple-chat-list/blob/master/entry/src/main/ets/pages/ChatPage.ets#L172-L186)

### 案例二：常见列表流场景

列表流是采用以“行”为单位进行内容排列的布局形式，每“行”列表项通过文本、图片等不同形式的组合，高效地显示结构化的信息，当列表项内容超过屏幕大小时，可以提供滚动功能。具体场景介绍请参见：[常见列表流](bpta-common-list-flows.md)。

## 示例代码

* [实现简单聊天列表功能](https://gitcode.com/harmonyos_samples/simple-chat-list)
