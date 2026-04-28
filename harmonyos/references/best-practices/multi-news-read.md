---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-news-read
title: 多设备新闻阅读界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备新闻阅读界面
category: best-practices
scraped_at: 2026-04-28T08:21:29+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:aaf2a9f29b19c9a363b833fb5fb3f3468a8fef28c5f7fb73748f075e2f885976
---

## 概述

本文以新闻阅读应用作为典型案例详细介绍“一多”在实际开发中的应用。新闻阅读应用在大屏幕设备的使用过程中，不仅要保障用户在界面浏览中的正常使用，也要尽可能提升屏幕的交互效率。该示例主要界面包含首页推荐、热门新闻、新闻详情、刷新闻、精选发现等。

新闻阅读一多开发过程中涉及的相关能力包括：

* 挪移布局
* 延伸布局
* 重复布局
* 列表变瀑布流
* 列表变宫格
* 全屏新闻变瀑布流
* 边看边评
* 沉浸浏览
* 文字大小调节

下面的章节将分别从[UX设计](multi-news-read.md#section1719610101057)、[架构设计](multi-news-read.md#section119741723356)、[页面开发](multi-news-read.md#section1180220717819)三个角度给出推荐的参考样例，介绍“一多”新闻阅读应用在开发过程中的最佳实践。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

新闻阅读类的多设备响应式设计指南，[点击访问](../design-guides/responsive-design-examples4-0000001746657290.md)。

## 架构设计

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供了一个清晰、高效、可扩展的设计架构。更多详细信息，请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

## 页面开发

本章介绍新闻阅读应用中如何使用“一多”布局能力，完成页面层级的多端适配。下文将从不同页面介绍具体布局能力，帮助开发者从零开始开发新闻阅读应用。

### 首页推荐

新闻阅读应用首页主要推荐精选新闻，解决用户看新闻的需求。首页内容围绕这一功能设计。观察首页在多设备上的UX设计图，可以进行如下设计：

* 将首页划分为9个部分，效果图如下：

|  | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

实现方案如下表：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 底部/侧边页签 | 借助[栅格布局](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化改变位置。同[多设备长视频界面 底部/侧边页签](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)。 |
| 2 | 顶部页签及搜索框 | 使用[栅格布局](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化实现折行显示，[List](../harmonyos-references/ts-container-list.md)实现延伸布局，layoutWeight实现拉伸能力。同[多设备长视频界面 顶部页签及搜索框](multi-video-app.md#zh-cn_topic_0000001744653537_li1346175796)。 |
| 3 | [顶部文字要闻](multi-news-read.md#li42441859453) | 使用[List](../harmonyos-references/ts-container-list.md)的lanes属性，在不同断点下呈1、2、3列显示。同[多设备长视频界面 搜索发现](multi-video-app.md#zh-cn_topic_0000001744653537_li311217374149)。 |
| 4 | [新闻大图卡片](multi-news-read.md#li1441844512434) | 使用[Swiper](../harmonyos-references/ts-container-swiper.md)，指定displayCount属性实现延伸布局，设置aspectRatio属性实现缩放能力。同[多设备长视频界面 Banner图](multi-video-app.md#zh-cn_topic_0000001744653537_li139671645597)。 |
| 5 | [上文下图](multi-news-read.md#li894391114417) | 采用[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，在手机、折叠屏上保持原有布局，在PC/2in1及更宽的设备上重复布局。 |
| 6 | [左文右图](multi-news-read.md#li431911954516) | 采用[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，手机上的单列信息，在折叠屏和PC/2in1上重复布局。 |
| 7 | [竖向视频卡片](multi-news-read.md#li651243310458) | 采用[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，手机上的左图右文卡片，在折叠屏和PC/2in1上显示更多列该卡片内容。同[多设备社区评论界面 列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。 |
| 8 | [大视频类新闻](multi-news-read.md#li917373419216) | 采用[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，手机上单列展示，在折叠屏和PC/2in1上重复布局。同[多设备社区评论界面 列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。 |
| 9 | [横向滑动小视频](multi-news-read.md#li1924317507257) | 采用[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)，使得设备尺寸变宽时，更多的小视频卡片被展示到界面。同[多设备长视频界面 视频详情页](multi-video-app.md#section9259381113)。 |

* 顶部文字要闻

使用List组件，设置不同断点下的lanes属性来实现。在sm断点下设置为1，在md断点下设置为2，在lg断点下设置为3。实现不同屏幕尺寸显示更多列数。具体代码可参考：[多设备长视频界面 搜索发现](multi-video-app.md#zh-cn_topic_0000001744653537_li311217374149)。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

* 新闻大图卡片

使用Swiper组件，设置在不同断点下的displayCount属性来实现自适应布局延伸布局，新闻大图卡片在sm断点下设置为1，在md断点下设置为2，在lg断点下设置为3。实现在不同屏幕尺寸显示更多内容。具体代码可参考：[多设备长视频界面 Banner图](multi-video-app.md#zh-cn_topic_0000001744653537_li139671645597)。

| 示意图 | sm | md | l |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

* 上文下图

使用重复布局配合栅格布局控制不同设备上的内容列数。在sm和md断点下，设置GridCol的span属性为12；在lg断点下，设置GridCol的span属性为6。同时，使用onBreakpointChange函数控制不同设备尺寸上的显示数据数量。在sm和md断点下，渲染数据源包含一条数据；在lg断点下，渲染数据源包含两条数据。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. // src/main/ets/pages/MediaNews.ets
2. build() {
3. Column() {
4. Header()
5. GridRow({
6. gutter: $r("app.float.grid_gutter_bigger")
7. }) {
8. ForEach(this.newsList, (news: News) => {
9. GridCol({
10. span: {
11. sm: Constants.GRID_COL_SPAN[5],
12. lg: Constants.GRID_COL_SPAN[4]
13. }
14. }) {
15. NewsWithThreeImages({ news })
16. }
17. }, (news: News) => news.getNewsID())
18. }
19. .onBreakpointChange((breakPoints: string) => {
20. // Return the number of rendered data records based on the breakpoint situation
21. this.newsList = this.multiImageViewModel.getNewsListByBreakpoint(breakPoints);
22. })
23. .width(Constants.CONTENT_WIDTH)
24. }
25. .width(Constants.FULL_WIDTH)
26. .justifyContent(FlexAlign.Center)
27. }
```

[MediaNews.ets](https://gitcode.com/harmonyos_samples/multi-news-read/blob/master/entry/src/main/ets/pages/MediaNews.ets#L29-L55)

* 左文右图

使用栅格布局，配合断点控制列数：在sm尺寸下设置GridCol的span属性为12，在md及以上尺寸设置为6。同时，使用Text组件的visibility属性配合断点控制摘要部分的显隐：在sm和md断点下设置摘要部分Text组件的visibility为Visibility.Hidden，在lg及以上断点设置为Visibility.Visible。

示意图如下：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. build() {
2. Column() {
3. Header()
4. GridRow({
5. columns: 12,
6. gutter: {
7. x: { md: Constants.GRID_HORIZONTAL_GUTTER[0], lg: Constants.GRID_HORIZONTAL_GUTTER[1] },
8. y: { sm: Constants.GRID_VERTICAL_GUTTER[0], md: Constants.GRID_VERTICAL_GUTTER[1] }
9. }
10. }) {
11. ForEach(this.newsList, (news: News) => {
12. GridCol({
13. span: {
14. sm: Constants.GRID_COL_SPAN[5],
15. md: Constants.GRID_COL_SPAN[4]
16. }
17. }) {
18. LeftTextRightImageBgWhite({ news })
19. }
20. }, (news: News) => news.getNewsID())
21. }
22. .onBreakpointChange((breakPoints: string) => {
23. this.newsList = this.imageAndTextViewModel.getNewsListByBreakpoint(breakPoints);
24. })
25. .width(Constants.CONTENT_WIDTH)
26. }
27. .width(Constants.FULL_WIDTH)
28. .justifyContent(FlexAlign.Center)
29. }
```

[NewsChannel.ets](https://gitcode.com/harmonyos_samples/multi-news-read/blob/master/entry/src/main/ets/pages/NewsChannel.ets#L29-L57)

* 竖向视频卡片

采用重复布局，在sm断点下设置GridCol内容占用span为12。在md断点下设置GridCol内容占用span为6。在lg断点下设置GridCol内容占用span为4。同时使用GridRow的onBreakpointChange回调函数控制渲染的数据条数，使其在sm、md、lg断点下分别渲染1、2、3条数据。具体代码可参考：[多设备社区评论界面 列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

* 大视频类新闻

使用栅格布局配合断点控制显示列数与数据源数量。在sm断点下设置GridCol的span属性为12，返回渲染数据源个数为1个，在md断点下设置span为6，渲染数据源为2个，在lg断点下设置span为4，渲染数据源为3个。具体代码可参考：[多设备社区评论界面 列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

* 横向滑动小视频

使用Scroll与Row组件实现延伸布局，随着屏幕尺寸的增加，展示更多的小视频数量，延伸布局可参考：[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)，具体代码可参考：[多设备长视频界面 视频详情页](multi-video-app.md#section9259381113)。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

### 热门新闻

热门页提供不同设备的浏览体验。观察UX设计图，进行如下设计：

* 将热门新闻页划分为3个部分，如图所示：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

实现方案如下表：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 底部/侧边页签 | 借助[栅格布局](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化改变位置。同[多设备长视频界面 底部/侧边页签](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)。 |
| 2 | 顶部页签及搜索框 | [栅格布局](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化实现折行显示，[List](../harmonyos-references/ts-container-list.md)实现延伸布局，layoutWeight实现拉伸能力。同[多设备长视频界面 顶部页签及搜索框](multi-video-app.md#zh-cn_topic_0000001744653537_li1346175796)。 |
| 3 | [新闻列表](multi-news-read.md#li814217391355) | 借助断点监听改变不同断点下的布局方式，在sm断点及sm以下使用[List](../harmonyos-references/ts-container-list.md)，在sm断点以上使用[栅格布局](bpta-multi-device-responsive-layout.md#section1061332817545)。 |

* 新闻列表

为了实现列表与宫格的灵活切换，可以使用List组件在sm及以下断点时展示内容，而使用栅格布局在sm断点以上展示。在md断点下设置GridRow的columns属性为2，在lg断点下设置columns属性为4。对于需要更大空间的组件内容，设置GridCol的span属性以占用更多份数。

```
1. Column() {
2. if (this.curBp === 'sm') {
3. List({
4. space: Constants.LIST_GUTTER
5. }) {
6. // ...
7. }
8. .width(Constants.CONTENT_WIDTH)
9. } else {
10. GridRow({
11. columns: {
12. md: Constants.GRID_ROW_COLUMNS[1],
13. lg: Constants.GRID_ROW_COLUMNS[2]
14. },
15. gutter: $r("app.float.news_list_common_space")
16. }) {
17. // ...
18. }
19. // ...
20. }
21. }
```

[NewsListPage.ets](https://gitcode.com/harmonyos_samples/multi-news-read/blob/master/entry/src/main/ets/pages/NewsListPage.ets#L48-L208)

### 新闻详情

新闻详情页提供详细新闻信息。观察不同设备上的UX设计图，进行如下设计：

* 提供边看边评功能

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

如下表所示，实现方案：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部栏 | 使用自适应布局中的[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)，可使用Blank组件实现屏幕宽度变化时，中间空白内容随设备尺寸变化。具体可参考：[多设备长视频界面 搜索发现](multi-video-app.md#zh-cn_topic_0000001744653537_li311217374149)。 |
| 2 | 新闻标题及发布信息 | 使用[占比能力](bpta-multi-device-adaptive-layout.md#占比能力)保证多设备尺寸下的界面一致。具体可参考：[多设备社区评论界面 边看边评](multi-community-app.md#zh-cn_topic_0000001758831130_li11692132514198)。 |
| 3 | 新闻内容 | 使用[占比能力](bpta-multi-device-adaptive-layout.md#占比能力)保证多设备尺寸下的界面一致。具体可参考：[多设备社区评论界面 边看边评](multi-community-app.md#zh-cn_topic_0000001758831130_li11692132514198)。 |
| 4 | 评论区 | 采用[挪移布局](bpta-multi-device-responsive-layout.md#section1153210192360)，当设备尺寸变宽时将新闻内容区域和评论区左右布局。具体可参考：[多设备社区评论界面 边看边评](multi-community-app.md#zh-cn_topic_0000001758831130_li11692132514198)。 |
| 5 | 底部工具栏 | 使用[自适应布局](bpta-multi-device-adaptive-layout.md)中的均分能力，实现设备尺寸变化时图标尺寸不变，图标间距及左右边缘间距均等改变。具体可参考：[多设备社区评论界面 动态卡片](multi-community-app.md#zh-cn_topic_0000001758831130_li1420045031813)。 |

边看边评实现上可以利用[栅格布局](bpta-multi-device-responsive-layout.md#section1061332817545)实现[挪移布局](bpta-multi-device-responsive-layout.md#section1153210192360)，在sm断点下设置GridCol对应内容span为12，而在sm以上断点设置对应内容占用span为6，自动实现从新闻内容和评论区的上下布局切换到左右布局。具体可参考[多设备社区评论界面 边看边评](multi-community-app.md#zh-cn_topic_0000001758831130_li11692132514198)。

### 刷新闻

刷新闻界面向用户提供新闻流列表。观察不同设备上的UX设计图，进行如下设计：

* 全屏新闻变瀑布流

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

在刷新闻界面中，开发者可以使用[WaterFlow](../harmonyos-references/ts-container-waterflow.md)容器，实现一列到多列的切换。在sm断点下依赖断点控制设置WaterFlow的columnsTemplate属性为1，在md断点下设置columnsTemplate为2，在lg断点下设置columnsTemplate为3。具体实现开发者可以参考：[多设备社区评论界面 动态卡片](multi-community-app.md#zh-cn_topic_0000001758831130_li1420045031813)。

### 精选发现

* 瀑布流一列变多列

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

精选发现界面使用瀑布流一列变多列，主要使用[WaterFlow](../harmonyos-references/ts-container-waterflow.md)容器实现不同设备的差异化显示。在sm断点下一列显示，在md断点下依赖断点控制设置WaterFlow的columnsTemplate为两列，在lg断点下设置columnsTemplate为三列。具体实现开发者可以参考：[多设备社区评论界面 动态卡片](multi-community-app.md#zh-cn_topic_0000001758831130_li1420045031813)。

## 示例代码

* [多设备新闻阅读界面](https://gitcode.com/harmonyos_samples/multi-news-read)
