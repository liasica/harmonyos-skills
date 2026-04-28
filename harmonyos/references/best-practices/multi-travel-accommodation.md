---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation
title: 多设备旅行订票界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备旅行订票界面
category: best-practices
scraped_at: 2026-04-28T08:21:16+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:905a21ad199bb5b2c52baf523e092d34362701cc173c48b461531b81168dfb74
---

## 概述

本文从目前流行的垂类市场中，选择旅行订票垂类作为典型案例详细介绍“一多”在实际开发中的应用。本文选择首页、时间选择页、查询车票页、填写购票信息页、提交订单页等11个典型页面进行开发，遵从多设备的“差异性”、“一致性”、“灵活性”和“兼容性”，能够让开发者快速高效地掌握“一多”能力并实现旅行订票应用的相关功能。

旅行订票应用在垂类核心功能上进行了独特设计：

* [首页](multi-travel-accommodation.md#section1576042964012)支持沉浸式浏览，将整个页面设置背景图，同时设置全屏显示，使用户阅读时有更加沉浸的体验。
* [时间选择页](multi-travel-accommodation.md#section147288193403)及[低价日历页](multi-travel-accommodation.md#section8503123314815)根据设备不同有更好的体验效果，手机支持页面跳转，其他大屏设备支持日历弹窗。
* [查询车票页](multi-travel-accommodation.md#section1359152704212)支持车票筛选功能，方便用户快速定位目标车票。
* [查询车票上滑](multi-travel-accommodation.md#section052546194213)支持沉浸式浏览，隐藏日期筛选等信息，方便用户获取更多信息。
* [酒店详情页](multi-travel-accommodation.md#section185431244812)支持顶部banner根据设备不同有不同的展示效果，使用户在不同设备上有更好的体验。

当前系统的产品形态包括直板机、双折叠（Mate X系列）、平板三种。下文的具体实践将围绕这些产品形态展开，并从UX设计、架构设计和页面开发三个角度提供符合“一多”原则的参考样例，介绍“一多”旅行订票应用在开发过程中的最佳实践。

* [UX设计](multi-travel-accommodation.md#section896911343456)章节介绍旅行订票应用的交互逻辑和通用的设计要点，对于类似的设计要点，开发者可以直接拿来使用。
* [架构设计](multi-travel-accommodation.md#section35961357151114)章节推荐“一多”应用使用目录结构更清晰的三层架构，具体包括：数据层、逻辑层和展示层。
* [页面开发](multi-travel-accommodation.md#section183977201404)章节会将页面划分为不同区域，按照区域的开发顺序，介绍如何使用自适应布局和响应式布局实现不同的UI效果，具体区域包括：头部、内容区和底部。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

[旅游住宿类](../design-guides/tourist-accommodation-0000001957241545.md)的多设备响应式设计指南可参考如上链接。

## 架构设计

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供了一个清晰、高效、可扩展的设计架构。详细信息请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

## 页面开发

本章介绍旅行订票应用中如何使用“一套代码、多端适配”的布局能力，完成页面层级的开发。下文将从不同页面展开，详细介绍每个页面区域使用的具体布局能力，帮助开发者从零开始进行旅行订票应用的开发。

### 首页

旅行订票应用首页提供买票窗口，解决用户订票和预约酒店需求。首页内容围绕这一功能设计。

* 将首页划分为以下6个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 分析各个区域的一多能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 底部/侧边栏 | 借助[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化改变位置，代码可参考多设备长视频界面[底部/侧边页签](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)小节。 |
  | 2 | 顶部控件 | [Select](../harmonyos-references/ts-basic-components-select.md)和[TextInput](../harmonyos-references/ts-basic-components-textinput.md)中间增加[Blank](../harmonyos-references/ts-basic-components-blank.md)，实现拉伸能力。 |
  | 3 | 火车票选择 | 使用Tabs组件实现拉伸能力。 |
  | 4 | 功能入口 | 使用[Swiper](../harmonyos-references/ts-container-swiper.md)，设置在不同断点下的displayCount属性来实现自适应布局的延伸能力，代码可参考多设备长视频界面[Banner图](multi-video-app.md#zh-cn_topic_0000001744653537_li139671645597)小节。 |
  | 5 | 热门资讯 | 利用响应式布局的[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)，结合[Stack](../harmonyos-references/ts-container-stack.md)和[Grid](../harmonyos-references/ts-container-grid.md)，设置aspectRatio属性实现缩放能力，代码可参考多设备长视频界面[每日佳片](multi-video-app.md#zh-cn_topic_0000001744653537_li1938820294129)小节。 |
  | 6 | 酒店预订 | 利用响应式布局的栅格布局，结合Stack组件和Grid组件，设置aspectRatio属性实现缩放能力。 |

### 时间选择页

旅行订票时间选择页的主要功能是提供出行时间的选择，帮助用户快速确定出行日期，并筛选出相应日期的车票。

* 将时间选择页划分为两个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 日期 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |

### 查询车票页

旅行订票查询车票页面主要用于筛选车票，帮助用户根据日期、始发站筛选车票，并支持按出发时间、价格和总时长对车票进行排序。

* 将查询车票划分为四个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 日期选择 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |
  | 3 | 车票列表 | List组件实现延伸能力，layoutWeight实现拉伸能力。 |
  | 4 | 功能入口 | List组件实现延伸能力。 |

### 查询车票上滑

旅行订票查询车票时，上滑动效的主要功能是隐藏筛选信息，以便用户更专注地浏览，获取更多信息。

* 将查询车票上滑动效划分为两个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 车票列表 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |

### 填写购票信息页

旅行订票的填写购票信息页提供订单确认和选择乘车人的功能，方便购票。

* 将填写购票信息页划分为六个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对其中的各个区域分析使用的能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 日期栏 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)实现日期与按钮的拉伸自适应。 |
  | 3 | 火车票信息 | 使用栅格断点能力，设置在不同断点下实现拉伸能力。 |
  | 4 | 选择乘车人 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)实现选择乘车人卡片拉伸自适应。 |
  | 5 | 协议条款 | 使用栅格断点能力，设置在不同断点下顶部控件实现挪移布局。代码可参考多设备长视频界面[顶部页签及搜索框](multi-video-app.md#zh-cn_topic_0000001744653537_li1346175796)小节。 |
  | 6 | 提交按钮 | 使用栅格断点能力，设置在不同断点下顶部控件实现挪移布局。代码可参考多设备长视频界面[顶部页签及搜索框](multi-video-app.md#zh-cn_topic_0000001744653537_li1346175796)小节。 |

### 提交订单页

旅行订票提交订单页主要展示车票和乘车人信息，方便用户确认订单的正确性。

* 将提交订单划分为五个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 日期栏 | 使用拉伸能力实现日期与按钮的拉伸自适应。 |
  | 3 | 车票信息及乘车人信息 | 使用拉伸能力实现模块内部的拉伸自适应。 |
  | 4 | 协议条款 | 使用栅格断点能力，设置在不同断点下实现挪移布局。 |
  | 5 | 提交按钮 | 使用栅格断点能力，设置在不同断点下实现挪移布局。 |

### 订单信息页

旅行订票订单信息页面展示订单服务详情和车票卡片信息，便于用户查看。

* 将订单信息页面划分为五个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 火车票订单信息 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |
  | 3 | 订单信息卡片 | Tabs组件实现延伸能力。 |
  | 4 | 服务列表 | Grid组件配合Swiper组件，实现延伸能力与均分能力。 |
  | 5 | 底部/侧边导航 | 使用栅格断点能力，设置在不同断点下Tabs组件的BarPosition属性。 |

### 已支付订单信息页

旅行订票应用的已支付订单信息页主要用于查看和确认订单信息。

* 将已支付订单页划分为三个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对其中各个区域的分析使用的能力及实现方案如下表所示：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 订单类型选择 | Tabs组件实现延伸能力。 |
  | 3 | 订单信息列表 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |

### 酒店首页

旅行订票酒店首页主要提供酒店预订服务，满足用户预约酒店的需求。

* 将酒店首页划分为四个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各个区域使用的多项能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 卡片banner | Swiper组件实现，设置displayCount属性为auto。 |
  | 3 | 酒店推荐 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |
  | 4 | 底部/侧边导航 | 使用栅格断点能力，设置在不同断点下Tabs组件的BarPosition属性。 |

### 酒店排行榜页面

酒店排行榜页展示酒店排名，方便用户选择。

* 将酒店排行榜页划分为三个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 酒店类型选择 | Tabs组件实现延伸能力。 |
  | 3 | 酒店排行 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |

### 酒店详情页

旅行订票酒店详情页提供酒店的详细信息，包括预览图、房间类型和价格，方便用户选择和预订酒店房间。

* 将酒店详情页划分为四个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 酒店卡片 | 使用[GridRow](../harmonyos-references/ts-container-gridrow.md)实现挪移布局。 |
  | 3 | 订房优惠 | 使用拉伸能力实现文字与按钮的拉伸自适应。 |
  | 4 | 房间详情 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |
* 顶部banner的具体实现

顶部横幅会根据不同的设备类型展示不同的效果。手机支持顶部横幅上滑，图片展开的动画效果。折叠屏设备支持使用Scroll组件展示小图，点击后更换为大图展示的效果。平板设备支持使用Swiper组件滑动切换视图的效果。

手机上滑展开、下滑收起，主要使用了Scroll组件的onReachStart属性和onWillScroll属性。

```
1. Scroll(this.scroller) {
2. HotelDetailsPictureView({ topLength: this.topLength })
3. }
4. .scrollBar(BarState.Off)
5. .width('100%')
6. .height('100%')
7. .onReachStart(() => {
8. if (!this.isInitialization) {
9. this.topLength = 225;
10. this.isInitialization = true;
11. } else {
12. this.topLength = 460;
13. }
14. })
15. .onWillScroll((xOffset: number, yOffset: number)=>{
16. if (yOffset > 0) {
17. this.topLength = 225;
18. }
19. })
```

[HotelDetailsPage.ets](https://gitcode.com/HarmonyOS_Samples/multi-travel-accommodation/blob/master/entry/src/main/ets/pages/HotelDetailsPage.ets#L48-L66)

折叠屏的实现使用Scroll组件支持滚动。小图的点击效果会改变大图内容，点击后将索引值作为参数传递，以修改大图。

```
1. Scroll() {
2. Row() {
3. ForEach(CommonConstants.HOTEL_PICTURE_MESSAGE, (item: Resource, index: number) => {
4. Column() {
5. Image(item)
6. .width(CommonConstants.THIRTY_PERCENT)
7. .borderRadius($r('app.float.hotel_grade_border'))
8. .margin(index === CommonConstants.NUMBER_FOUR ? {} : { right: CommonConstants.FIVE_PERCENT })
9. .onClick(() => {
10. this.getMainPicture(index);
11. })
12. }
13. }, (item: Resource) => JSON.stringify(item))
14. }
15. }
16. .scrollBar(BarState.Off)
17. .margin({ top: $r('app.float.calendar_column_margin') })
18. .width(CommonConstants.NINETY_PERCENT)
19. .scrollable(ScrollDirection.Horizontal)
```

[HotelDetailsPictureView.ets](https://gitcode.com/HarmonyOS_Samples/multi-travel-accommodation/blob/master/entry/src/main/ets/view/HotelDetailsPictureView.ets#L133-L151)

```
1. getMainPicture(index: number) {
2. this.mainPictureResource = CommonConstants.HOTEL_PICTURE_MESSAGE[index];
3. }
```

[HotelDetailsPictureView.ets](https://gitcode.com/HarmonyOS_Samples/multi-travel-accommodation/blob/master/entry/src/main/ets/view/HotelDetailsPictureView.ets#L29-L31)

平板则使用Swiper组件，完成滚动切换视图的功能。

```
1. Swiper() {
2. ForEach(CommonConstants.HOTEL_PICTURE_MESSAGE, (item: Resource) => {
3. Image(item)
4. .width('100')
5. }, (item: Resource) => JSON.stringify(item))
6. }
7. .width('40%')
8. .height('100%')
```

[HotelDetailsPictureView.ets](https://gitcode.com/HarmonyOS_Samples/multi-travel-accommodation/blob/master/entry/src/main/ets/view/HotelDetailsPictureView.ets#L208-L215)

### 低价日历页

旅行订票低价日历页提供预订房间的功能，帮助用户找到低价时段。

* 将低价日历划分为两个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对其中的各个区域分析使用的一多能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部控件 | 使用栅格断点能力，设置在不同断点下顶部控件实现拉伸能力。 |
  | 2 | 日期 | [List](../harmonyos-references/ts-container-list.md)实现延伸能力，layoutWeight实现拉伸能力。 |
* 低价日历

  根据栅格布局监听断点变化，根据断点不同实现不同的响应效果。

  ```
  1. getFoldStatus() {
  2. if (this.isShowingCalendar) {
  3. this.dialogController.open();
  4. } else {
  5. this.dialogController.close()
  6. }
  7. }
  ```

  [HotelDetailsRoomView.ets](https://gitcode.com/HarmonyOS_Samples/multi-travel-accommodation/blob/master/entry/src/main/ets/view/HotelDetailsRoomView.ets#L38-L44)

  ```
  1. Column() {
  2. Image($r("app.media.cheap_day"))
  3. .width('15vp')
  4. Text(CommonConstants.ROOM_BUTTON_MESSAGES[5])
  5. .font({ size: '8fp', weight: 500 })
  6. .opacity(0.4)
  7. }
  8. .onClick(() => {
  9. if (this.breakPoint === 'sm') {
  10. this.pageInfos.pushPath(new NavPathInfo('LowPriceCalendarPage',[]));
  11. } else {
  12. this.isShowingCalendar = true;
  13. }
  14. })
  ```

  [HotelDetailsRoomView.ets](https://gitcode.com/HarmonyOS_Samples/multi-travel-accommodation/blob/master/entry/src/main/ets/view/HotelDetailsRoomView.ets#L86-L99)

## 示例代码

* [多设备旅行订票界面](https://gitcode.com/harmonyos_samples/multi-travel-accommodation)
