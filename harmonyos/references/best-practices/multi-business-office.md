---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-business-office
title: 多设备商务办公界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备商务办公界面
category: best-practices
scraped_at: 2026-04-29T14:12:21+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:ac17b6af6b2e0875f01b51bd7778b740f032f8181ed67617193c51de0d34a7c2
---

## 概述

本文从目前流行的垂类市场中，选择商务办公类应用作为典型案例，详细介绍“一多”在实际开发中的应用。主要包含入口、备忘录、笔记汇总、笔记、日历等典型页面。

* 核心功能：

  [侧边栏显隐](multi-business-office.md#li46232105014)：监听断点变化，设置[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)组件的SideBarContainerType属性或改变showSideBar属性参数，实现侧边栏根据不同断点显示隐藏及显示类型的变化。

  [分栏](multi-financial-app.md#section1796912148314)布局：分栏布局通过[Navigation](../harmonyos-references/ts-basic-components-navigation.md)实现，监听断点变化，根据不同断点或状态改变Navigation的mode属性，实现单双栏切换的效果。

  宫格卡片：用网格布局[Grid](../harmonyos-references/ts-container-grid.md)组件，在不同断点下将父组件分为不同列数，来实现自适应布局的占比能力，可参考多设备长视频界面中[首页](multi-video-app.md#section109591922155720)的推荐视频实现方案。

* 关键场景：

  入口-多实例：监听断点变化，设置[List](../harmonyos-references/ts-container-list.md)组件的listDirection属性。在断点为sm时，设置为Vertical纵向展示；其余断点为Horizontal横向展示。实现入口组件根据不同断点切换横向/纵向排列的效果。使用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)实现点击子组件时拉起新实例的效果。

  备忘录-侧边栏显隐：监听断点变化，设置SideBarContainer组件的SideBarContainerType属性或改变showSideBar属性参数，实现侧边栏根据不同断点显示隐藏及显示类型的变化。

  日历-navigation的单双栏变化：监听断点变化，根据不同断点或状态改变[Navigation](../harmonyos-references/ts-basic-components-navigation.md)的mode属性，实现单双栏切换的效果。

下面的章节将分别从[UX设计](multi-business-office.md#section896911343456)、[架构设计](multi-business-office.md#section35961357151114)、[页面开发](multi-business-office.md#section183977201404)三个角度给出推荐的参考样例，介绍“一多”商务办公类应用在开发过程中的最佳实践。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

本示例中的商务办公应用包含入口、备忘录、笔记汇总、笔记、日历等页面。以平板端为例，应用的基本业务逻辑如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/-QJaTpWrRlSOIvo1GE4ARw/zh-cn_image_0000002229337365.png?HW-CC-KV=V1&HW-CC-Date=20260429T061210Z&HW-CC-Expire=86400&HW-CC-Sign=D84A6CE1E5EDA26AB5595798ECCA407C53BABCCF0369719F520A410F7D13A45A "点击放大")

## 架构设计

HarmonyOS的分层架构主要包括产品定制层、基础特性层和公共能力层，为开发者构建了清晰、高效、可扩展的设计架构。详细信息请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

## 页面开发

本章介绍商务办公类应用中如何使用“一多”布局能力，完成页面层级的单页面和多端适配。下文将从不同页面展开，介绍每个页面区域使用的具体布局能力，帮助开发者从零开始进行商务办公类应用的开发。

### 入口

* 将入口页划分为两部分，效果图如下：

  | 横向断点 | sm | md | lg | xl |
  | --- | --- | --- | --- | --- |
  | 效果图 |  |  |  |  |
* 对各个区域使用的一多能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 标题 | [Text](../harmonyos-references/ts-basic-components-text.md)组件实现。 |
  | 2 | 多实例入口 | 设置[List](../harmonyos-references/ts-container-list.md)组件的listDirection属性在断点为sm时为Vertical纵向展示，其余断点为Horizontal横向展示，同时点击子组件使用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)拉起新实例。 |

* 多实例入口的实现：

  监听断点变化，设置List组件的listDirection属性。当断点为sm时，设置为Vertical纵向展示；其余断点时，设置为Horizontal横向展示，实现入口组件根据不同断点横纵排列的效果。使用startAbility()实现点击子组件时拉起新实例的效果。

  ```
  1. Column() {
  2. // ...
  3. List() {
  4. ForEach(this.directory, (item: DirectoryItem, index: number) => {
  5. ListItem() {
  6. Column() {
  7. // ...
  8. }
  9. // ...
  10. .onClick(() => {
  11. if (index === CommonConstants.COMMON_ZERO) {
  12. let want: Want = {
  13. bundleName: this.bundleName,
  14. abilityName: 'SecondAbility'
  15. };
  16. let option: StartOptions = { displayId: CommonConstants.COMMON_ZERO };
  17. this.context.startAbility(want, option);
  18. } else {
  19. let want: Want = {
  20. bundleName: this.bundleName,
  21. abilityName: 'ThirdAbility'
  22. };
  23. let option: StartOptions = { displayId: CommonConstants.COMMON_ZERO };
  24. this.context.startAbility(want, option);
  25. }
  26. })
  27. }
  28. // ...
  29. })
  30. }, (item: DirectoryItem) => JSON.stringify(item))
  31. }
  32. // ...
  33. .listDirection(this.breakPoint === CommonConstants.BREAK_POINT_SM ? Axis.Vertical : Axis.Horizontal)
  34. }
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/MultiBusinessOffice/blob/master/entry/src/main/ets/pages/Index.ets#L70-L162)

### 备忘录

* 将备忘录页划分为6个部分，效果图如下：

  | 横向断点 | sm | md | lg | xl |
  | --- | --- | --- | --- | --- |
  | 效果图 |  |  |  |  |
* 对各个区域使用的适配能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 侧边栏 | 监听断点变化，设置[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)的SideBarContainerType属性在断点为lg时为Embed，其余断点为Overlay，实现侧边栏根据不同断点显示类型变化的效果，代码可参考[侧边栏显示类型变化](multi-business-office.md#li46232105014)。 |
  | 2 | 侧边栏显隐控件 | 监听断点变化，设置SideBarContainer组件的showSideBar属性，实现侧边栏根据不同断点显示隐藏的效果，代码可参考[侧边栏显隐变化](multi-business-office.md#li68811147079)。 |
  | 3 | navigation导航页 | 通过[Navigation](../harmonyos-references/ts-basic-components-navigation.md)路由栈[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)，将NavDestination页面信息入栈，实现NavDestination页面的展示。 |
  | 4 | navigation内容页 | NavDestination页面信息。 |
  | 5 | navigation内容页-控制按钮 | 给控制按钮添加onClick事件，通过自定义变量notesNavMode改变Navigation中mode属性的值，控制单双栏的变化，并通过自定义变量sideBarStatus改变SideBarContainer组件中showSideBar属性的值，控制侧边栏的显隐，实现内容页全屏展示或退出全屏的效果，代码可参考[navigation内容页-控制按钮](multi-business-office.md#li14995047141210)。 |
  | 6 | 按钮组件 | 监听断点变化，不同断点展示的位置不同。 |

* 侧边栏显示类型变化

  监听断点变化，同时设置SideBarContainer组件的SideBarContainerType属性在断点为lg时为Embed，其余断点为Overlay，实现侧边栏根据不同断点显示类型变化的效果。

  ```
  1. SideBarContainer(this.breakPoint === CommonConstants.BREAK_POINT_LG ? SideBarContainerType.Embed :
  2. SideBarContainerType.Overlay) {
  3. // ...
  4. }
  ```

  [NotesPage.ets](https://gitcode.com/harmonyos_samples/MultiBusinessOffice/blob/master/entry/src/main/ets/pages/NotesPage.ets#L172-L370)

* 侧边栏显隐变化

  监听断点变化，同时设置SideBarContainer组件的showSideBar属性，实现侧边栏根据不同断点显示隐藏的效果。

  ```
  1. .showSideBar(this.breakPoint === CommonConstants.BREAK_POINT_LG ? this.arrowStatus : false)
  ```

  [NotesPage.ets](https://gitcode.com/HarmonyOS_Samples/MultiBusinessOffice/blob/master/entry/src/main/ets/pages/NotesPage.ets#L390-L390)

* navigation内容页-控制按钮

  给控制按钮添加onClick事件，通过自定义变量notesNavMode改变Navigation中mode属性的值，控制单双栏的变化，并通过自定义变量sideBarStatus改变SideBarContainer组件中showSideBar属性的值，控制侧边栏的显隐，实现内容页全屏展示或退出全屏的效果。

  ```
  1. Row() {
  2. if (this.arrowStatus && this.breakPoint !== CommonConstants.BREAK_POINT_SM) {
  3. Column() {
  4. // ...
  5. }
  6. // ...
  7. .onClick(() => {
  8. this.notesNavMode = NavigationMode.Stack;
  9. this.arrowStatus = false;
  10. this.sideBarIsShown = false;
  11. })
  12. // ...
  13. } else {
  14. Column() {
  15. // ...
  16. }
  17. // ...
  18. .onClick(() => {
  19. if (this.breakPoint === CommonConstants.BREAK_POINT_SM) {
  20. this.notesPageInfos.pop();
  21. } else {
  22. this.notesNavMode = NavigationMode.Split;
  23. this.arrowStatus = true;
  24. }
  25. this.sideBarIsShown = true;
  26. if (this.breakPoint === CommonConstants.BREAK_POINT_LG) {
  27. this.sideBarStatus = true;
  28. }
  29. })
  30. // ...
  31. }
  32. // ...
  33. }
  ```

  [NotesPageC.ets](https://gitcode.com/harmonyos_samples/MultiBusinessOffice/blob/master/entry/src/main/ets/view/NotesPageC.ets#L33-L155)
* 整个页面使用的是[分栏](multi-financial-app.md#section1796912148314)布局，点击navigation导航页的某一备忘清单时，可分栏显示备忘内容，该功能在多设备银行理财界面中有详细介绍。

### 笔记汇总

* 笔记汇总页划分为4个部分，效果如下图所示：

  | 横向断点 | sm | md | lg | xl |
  | --- | --- | --- | --- | --- |
  | 效果图 |  |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 侧边栏 | 监听断点变化，设置[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)组件的SideBarContainerType属性在断点为lg时为Embed，其余断点为Overlay，实现侧边栏根据不同断点显示类型变化的效果。 |
  | 2 | 侧边栏显隐控件 | 监听断点变化，设置SideBarContainer组件的showSideBar属性，实现侧边栏根据不同断点显示隐藏的效果。 |
  | 3 | 标题栏 | 空白部分使用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充，实现拉伸能力。PC/2in1设备需设置setWindowDecorVisible()接口，隐藏标题栏后避让系统绘制的右上角三键区域。 |
  | 4 | 笔记汇总 | 使用网格布局[Grid](../harmonyos-references/ts-container-grid.md)组件，在不同断点下将父组件分为不同列数，来实现自适应布局的占比能力，可参考多设备长视频界面中[首页](multi-video-app.md#section109591922155720)的推荐视频实现方案。 |

* 整个页面使用的是宫格卡片，点击某一个笔记时，可打开笔记实例。

### 笔记

* 将笔记页划分为3个部分，具体效果见下图：

  | 横向断点 | sm | md | lg | xl |
  | --- | --- | --- | --- | --- |
  | 效果图 |  |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 标题栏 | 点击加号，增加[Tabs](../harmonyos-references/ts-container-tabs.md)标签及[TabContent](../harmonyos-references/ts-container-tabcontent.md)，实现多实例的效果，空白部分使用Blank组件填充，实现拉伸能力。 |
  | 2 | 编辑按钮 | 监听断点变化，改变[List](../harmonyos-references/ts-container-list.md)组件下子组件的间隔宽度，同时设置固定宽度，当List组件下的Tabs内容超过设定宽度时隐藏部分Tabs，延伸显示更多。 |
  | 3 | 笔记内容 | Tabs标签下的TabContent。 |

### 日历

* 将日历页划分为6个部分，效果图如下：

  | 横向断点 | sm | md | lg | xl |
  | --- | --- | --- | --- | --- |
  | 效果图 |  |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 侧边栏 | 设置[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)组件的SideBarContainerType属性在断点为lg时为Embed，其余断点为Overlay，实现侧边栏根据不同断点显示类型变化的效果。 |
  | 2 | 侧边栏显隐控件 | 设置SideBarContainer组件的showSideBar属性，实现侧边栏根据不同断点显示隐藏的效果。 |
  | 3 | 标题栏 | 空白部分使用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充，实现拉伸能力。PC/2in1设备需设置setWindowDecorVisible()接口，隐藏标题栏后避让系统绘制的右上角三键区域。 |
  | 4 | navigation导航页 | 使用[Grid](../harmonyos-references/ts-container-grid.md)组件设置columnsTemplate和rowsTemplate属性，实现五行七列的自适应布局。  通过[Navigation](../harmonyos-references/ts-basic-components-navigation.md)路由栈[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)，将NavDestination页面信息入栈，并监听断点变化，根据不同断点或状态改变Navigation的mode属性，实现单双栏切换及navigation内容页显隐的效果。 |
  | 5 | navigation内容页 | NavDestination页面信息。 |
  | 6 | navigation控制按钮 | 给控制按钮添加onClick事件，用来改变Navigation的mode属性，实现单双栏切换及控制navigation内容页显隐的效果，代码可参考[单双栏切换](multi-business-office.md#li12736428201)。 |

* 单双栏切换

  监听断点的变化，通过控制按钮的点击事件，用来改变Navigation的mode属性，实现单双栏切换及navigation内容页显隐。同时监听navigationMode变化，控制页面是否跳转。

  ```
  1. Row() {
  2. // ...

  4. if (this.breakPoint !== CommonConstants.BREAK_POINT_SM) {
  5. Column() {
  6. // ...
  7. }
  8. // ...
  9. .onClick(() => {
  10. if (this.navMode === NavigationMode.Split) {
  11. this.navMode = NavigationMode.Stack;
  12. } else if (this.navMode === NavigationMode.Stack && this.selectedItem.isTrip) {
  13. this.navMode = NavigationMode.Split;
  14. }
  15. })
  16. }
  17. // ...
  18. Navigation(this.calendarPageInfos) {
  19. CalendarView()
  20. }
  21. .navDestination(this.pageMap)
  22. .mode(this.breakPoint === CommonConstants.BREAK_POINT_SM ? NavigationMode.Stack : this.navMode)
  23. // ...
  24. .onNavigationModeChange((mode: NavigationMode) => {
  25. if (this.breakPoint === CommonConstants.BREAK_POINT_SM || mode === NavigationMode.Stack) {
  26. this.calendarPageInfos.clear();
  27. } else if (mode === NavigationMode.Split) {
  28. this.calendarPageInfos.pushPath({ name: this.selectedItem.date, param: this.selectedItem }, false);
  29. }
  30. })
  ```

  [CalendarPage.ets](https://gitcode.com/harmonyos_samples/MultiBusinessOffice/blob/master/entry/src/main/ets/pages/CalendarPage.ets#L97-L227)
* 整个页面使用的是[分栏](multi-financial-app.md#section1796912148314)布局，点击navigation导航页的某一日期时，可分栏显示行程内容，该功能在多设备银行理财界面中有详细介绍。

## 示例代码

* [多设备商务办公界面](https://gitcode.com/harmonyos_samples/MultiBusinessOffice)
