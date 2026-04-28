---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-page-layout
title: 页面布局场景
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 界面布局响应式变化 > 页面布局场景
category: best-practices
scraped_at: 2026-04-28T08:21:05+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:01a785887aec8b7c97d8766616e77393f3cb93cb7cdca7b393f73af5d8d24634
---

HarmonyOS基于“一次开发，多端部署”的理念设计了响应式布局，旨在帮助开发者高效构建适应不同设备的应用界面。系统通过统一的UI框架、响应式布局能力——断点和栅格，让应用页面能够根据代码的差异化实现自动适应从手机、折叠屏、平板到PC/2in1等各种终端形态。

响应式布局方式包含四种：[重复布局](bpta-multi-device-page-layout.md#section381193213517)、[分栏布局](bpta-multi-device-page-layout.md#section11897247142110)、[挪移布局](bpta-multi-device-page-layout.md#section454920411796)和[缩进布局](bpta-multi-device-page-layout.md#section74801750591)。

本文将从页面布局场景的角度，通过典型布局场景的示例，展示不同横向断点下界面的展示效果，并详细说明在多设备上的实现方案。本文主要覆盖手机、折叠屏、平板和电脑设备，旨在帮助开发者高效实现跨端布局开发。

| 响应式布局方式 | 布局示例 | 典型布局场景 | 实现方案 |
| --- | --- | --- | --- |
| [重复布局](../design-guides/design-responsive-layout-method-0000001795698449.md#section198611812185) |  | 列表布局 | List组件+断点 |
| 瀑布流布局 | WaterFlow组件+断点 |
| 轮播布局 | Swiper组件+断点 |
| 网格布局 | Grid组件+断点 |
| [分栏布局](../design-guides/design-responsive-layout-method-0000001795698449.md#section20649152191817) |  | 侧边栏 | SideBarContainer组件+断点 |
| 单/双栏 | Navigation组件+断点 |
| 三分栏 | SideBarContainer组件+Navigation组件+断点 |
| [挪移布局](../design-guides/design-responsive-layout-method-0000001795698449.md#section114691379188) |  | 插图和文字组合布局 | GridRow/GridCol组件+断点+栅格 |
| 底部/侧边导航 | Tabs组件+断点 |
| [缩进布局](../design-guides/design-responsive-layout-method-0000001795698449.md#section19655124713115) |  | 单列列表布局 | GridRow/GridCol组件+断点+栅格 |

说明

设计指南请参考[响应式布局方法](../design-guides/design-responsive-layout-method-0000001795698449.md)。

## 重复布局

重复布局是指在空间充足时，重复使用相同或相似的结构、组件或排列方式，用以展示更多内容、保持视觉一致性并提高用户体验。常用的重复布局包括列表布局、瀑布流布局、轮播布局和网格布局。

### 列表布局

列表布局基于横向断点，动态调整列数以实现重复布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 单列列表  行间距8vp | 双列列表  列间距12vp  行间距 12vp | 三列列表  列间距12vp  行间距16vp |
| 布局效果 |  |  |  |

**实现方案**

设置不同横向断点下，[List组件](../harmonyos-references/ts-container-list.md)的lanes、space属性实现目标效果。

**参考代码**

```
1. List({
2. space: new WidthBreakpointType(8, 12, 16, 16).getValue(this.mainWindowInfo.widthBp),
3. scroller: this.listScroller
4. }) {
5. // ...
6. }
7. .scrollBar(BarState.Off)
8. .lanes(new WidthBreakpointType(1, 2, 3, 3).getValue(this.mainWindowInfo.widthBp), 12)
```

[ListView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/ListView.ets#L43-L63)

### 瀑布流布局

瀑布流布局基于横向断点，动态控制列数以实现重复布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 双列布局 | 三列布局 | 四列布局 |
| 展示布局 |  |  |  |

**实现方案**

设置不同横向断点下，[WaterFlow组件](../harmonyos-references/ts-container-waterflow.md)的columnsTemplate属性实现目标效果。

**示例代码**

```
1. WaterFlow() {
2. LazyForEach(this.dataSource, (item: number, index: number) => {
3. FlowItem() {
4. Row() {}
5. .width('100%')
6. .height('100%')
7. .borderRadius(16)
8. .backgroundColor('#F1F3F5')
9. }
10. .width('100%')
11. .height(this.itemHeightArray[index])
12. }, (item: number, index: number) => JSON.stringify(item) + index)
13. }
14. .columnsTemplate(`repeat(${new WidthBreakpointType(2, 3, 4, 4).getValue(this.mainWindowInfo.widthBp)}, 1fr)`)
15. .columnsGap(12)
16. .rowsGap(12)
17. .width('100%')
```

[WaterFlowView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/WaterFlowView.ets#L60-L76)

### 轮播布局

轮播布局基于横向断点，动态控制视窗内显示元素的个数以实现重复布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 展示一个元素  无前后边距  显示圆点指示器 | 展示两个元素  前后边距12vp  不显示圆点指示器 | 展示三个元素  前后边距64vp  不显示圆点指示器 |
| 展示布局 |  |  |  |

**实现方案**

设置不同横向断点下，[Swiper组件](../harmonyos-references/ts-container-swiper.md)的displayCount、prevMargin、nextMargin和indicator属性实现目标效果。

**示例代码**

```
1. Swiper() {
2. // ...
3. }
4. .displayCount(new WidthBreakpointType(1, 2, 3, 3).getValue(this.mainWindowInfo.widthBp))
5. // Setting the navigation point Style of the swiper.
6. .indicator(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? Indicator.dot()
7. .itemWidth(6)
8. .itemHeight(6)
9. .selectedItemWidth(12)
10. .selectedItemHeight(6)
11. .color('#4DFFFFFF')
12. .selectedColor(Color.White) : false
13. )
14. // The sizes of the front and rear banners on the MD and LG devices are different.
15. .prevMargin(new WidthBreakpointType(0, 12, 64, 64).getValue(this.mainWindowInfo.widthBp))
16. .nextMargin(new WidthBreakpointType(0, 12, 64, 64).getValue(this.mainWindowInfo.widthBp))
```

[SwiperView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/SwiperView.ets#L74-L107)

### 网格布局

网格布局基于横向断点，动态控制列数/行数以实现重复布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 网格2行2列 | 网格2行3列 | 网格2行4列 |
| 展示布局 |  |  |  |

说明

网格布局将容器按行和列划分为规则的网格，每个子组件严格对齐，实现均分和占比能力，详情请参考[创建网格](../harmonyos-guides/arkts-layout-development-create-grid.md)；瀑布流布局子组件高度支持自定义，无需对齐，适合展示高度不一的内容，详情请参考[创建瀑布流](../harmonyos-guides/arkts-layout-development-create-waterflow.md)。

**实现方案**

设置不同横向断点下，[Grid组件](../harmonyos-references/ts-container-grid.md)的columnsTemplate属性实现目标效果。在不设置Grid组件行数的情况下，行数 = 展示元素数量 / 列数。Grid组件其他布局模式，请参考[rowsTemplate](../harmonyos-references/ts-container-grid.md#rowstemplate)。

**示例代码**

```
1. Grid() {
2. ForEach(this.infoArray.slice(new WidthBreakpointType(4, 2, 0, 0).getValue(this.mainWindowInfo.widthBp)),
3. (item: number) => {
4. // ...
5. }, (item: number, index: number) => JSON.stringify(item) + index)
6. }
7. .width('100%')
8. .columnsTemplate(`repeat(${new WidthBreakpointType(2, 3, 4, 4).getValue(this.mainWindowInfo.widthBp)}, 1fr)`)
9. .columnsGap(12)
10. .rowsGap(12)
```

[GridView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/GridView.ets#L52-L69)

## 分栏布局

分栏布局是指在空间充足时，将窗口划分为两栏或三栏，用于展示多类内容。常见的分栏布局包括侧边栏、单/双栏和三分栏。

### 侧边栏

侧边栏基于横向断点，动态控制侧边栏是否显示，实现二分栏布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 默认不显示侧边栏  侧边栏浮在内容区上  侧边栏宽度80% | 默认显示侧边栏  侧边栏和内容区并列展示  侧边栏宽度50% | 默认显示侧边栏  侧边栏和内容区并列展示  侧边栏宽度40% |
| 展示布局 |  |  |  |

**实现方案**

在不同横向断点下，动态控制[SideBarContainer组件](../harmonyos-references/ts-container-sidebarcontainer.md)的showSideBar和sideBarWidth属性实现目标效果。

**示例代码**

```
1. SideBarContainer(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? SideBarContainerType.Overlay :
2. SideBarContainerType.Embed) {
3. Column() {
4. // ...
5. }
6. .backgroundColor('#F1F3F5')

8. Column() {
9. // ...
10. }
11. .backgroundColor('#FDBFFC')
12. .padding({
13. top: this.getUIContext().px2vp(this.mainWindowInfo.AvoidSystem?.topRect.height) + 12,
14. bottom: this.getUIContext().px2vp(this.mainWindowInfo.AvoidNavigationIndicator?.bottomRect.height),
15. left: 16,
16. right: 16
17. })
18. }
19. .showSideBar(this.isShowingSidebar)
20. .sideBarWidth(new WidthBreakpointType('80%', '50%', '40%', '40%').getValue(this.mainWindowInfo.widthBp))
21. .controlButton({ top: this.getUIContext().px2vp(this.mainWindowInfo.AvoidSystem?.topRect.height) + 12 })
```

[SidebarView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/SidebarView.ets#L27-L112)

### 单/双栏

单/双栏基于横向断点，动态控制导航栏的显示模式，实现二分栏布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 导航栏和内容区单栏显示 | 导航栏和内容区分栏显示  导航栏宽度50% | 导航栏和内容区分栏显示  导航栏宽度50% |
| 展示布局 |  |  |  |

**实现方案**

设置不同横向断点下，[Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)的mode属性实现目标效果。

**示例代码**

```
1. Navigation(this.pathStack) {
2. // ...
3. }
4. .mode(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? NavigationMode.Stack : NavigationMode.Split)
```

[DoubleColumnView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/DoubleColumnView.ets#L38-L48)

说明

单/双栏与侧边栏的主要区别是单/双栏的导航栏能够控制内容区的路由跳转，例如商品列表与商品详情；侧边栏通常不控制内容区展示的内容，例如图文详情与评论区。

### 二分栏典型场景——聊天

某些应用在双栏布局下支持通过右侧内容区链接跳转至其扩展页面并单栏展示。以社交应用为例，在横向断点为md、lg和xl时，左侧导航栏为聊天列表，右侧内容区显示聊天框，包括文字信息和商品链接；当用户在右侧点击商品链接时，可进入单栏模式，全屏展示对应的商品扩展区页面，同时隐藏原聊天页，实现沉浸式浏览体验。

**布局效果**

| 横向断点 | sm | md | lg/xl |
| --- | --- | --- | --- |
| 属性 | 导航栏和内容区单栏显示 | 导航栏和内容区分栏显示，内容扩展区单独展示  导航栏宽度50% | 导航栏和内容区分栏显示，内容扩展区单独展示  导航栏宽度50% |
| 展示布局 |  |  |  |

**实现方案**

使用[Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)，动态控制其NavigationMode，在路由时切换单双栏显示。聊天列表作为Navigation导航栏，通过点击不同列表条目实现右侧Navigation内容区的路由控制，这种分栏路由模式为NavigationMode.Split。点击商品链接时，设置全屏变量isNavFullScreen为true，切换Navigation为单栏展示，此时路由模式为NavigationMode.Stack。路由返回时，isNavFullScreen变量改为false，路由重新切换为NavigationMode.Split。

对于聊天页面的双栏路由模式切换，开发者可以抽象为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/SjbQvD6lQ-K1uh25AYapnw/zh-cn_image_0000002509292755.png?HW-CC-KV=V1&HW-CC-Date=20260428T002058Z&HW-CC-Expire=86400&HW-CC-Sign=6980DC3993EECD3C3BE4DFD8FAF2041D5FA92C5591C987DA54508240694E7814 "点击放大")

**示例代码**

```
1. @Builder
2. PageMap(name: string) {
3. if (name === 'conversationDetail') {
4. ConversationDetail({
5. // ...
6. })
7. } else if (name === 'conversationDetailNone') {
8. ConversationDetailNone();
9. } else if (name === 'productPage') {
10. ProductPage({
11. // ...
12. })
13. }
14. }

16. build() {
17. Navigation(this.pathStack) {
18. ConversationNavBarView({
19. mainWindowInfo: this.mainWindowInfo,
20. pageInfos: this.pageInfos,
21. pathStack: this.pathStack,
22. })
23. }
24. .mode(this.getNavMode())
25. // ...
26. .navDestination(this.PageMap)
27. }

29. getNavMode(): NavigationMode {
30. if (!this.isNavFullScreen && this.mainWindowInfo.widthBp !== WidthBreakpoint.WIDTH_SM) {
31. return NavigationMode.Split;
32. }
33. return NavigationMode.Stack
34. }
```

[DoubleConversationView.ets](https://gitcode.com/HarmonyOS_Samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/DoubleConversationView/DoubleConversationView.ets#L31-L78)

### 三分栏

三分栏基于横向断点，动态控制导航栏的显示模式和侧边栏是否显示，实现三分栏布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 默认不显示侧边栏  侧边栏覆盖导航栏  侧边栏宽度80%  导航栏和内容区单栏显示 | 默认不显示侧边栏  侧边栏覆盖导航栏  侧边栏宽度50%  导航栏和内容区分栏显示  导航栏宽度50% | 默认显示侧边栏  侧边栏嵌入导航栏  侧边栏宽度20%  导航栏和内容区分栏显示  导航栏宽度30% |
| 展示布局 |  |  |  |

**实现方案**

在不同横向断点下，动态控制[SideBarContainer组件](../harmonyos-references/ts-container-sidebarcontainer.md)的showSideBar、sideBarWidth属性，和[Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)的mode、navBarWidth属性实现目标效果。

**示例代码**

```
1. SideBarContainer(new WidthBreakpointType(SideBarContainerType.Overlay, SideBarContainerType.Overlay,
2. SideBarContainerType.Embed, SideBarContainerType.Embed).getValue(this.mainWindowInfo.widthBp)) {
3. Column() {
4. // ...
5. }
6. // ...

8. Column() {
9. Navigation(this.pathStack) {
10. NavigationBarView({
11. mainWindowInfo: this.mainWindowInfo,
12. pageInfos: this.pageInfos,
13. pathStack: this.pathStack,
14. isShowingSidebar: this.isShowingSidebar,
15. isTriView: true
16. })
17. }
18. .width('100%')
19. .height('100%')
20. .mode(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? NavigationMode.Stack : NavigationMode.Split)
21. .navBarWidth(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_MD ? '50%' : '40%')
22. .navDestination(this.PageMap)
23. .backgroundColor('#B8EEB2')
24. }
25. // ...
26. }
27. .showSideBar(this.isShowingSidebar)
28. .sideBarWidth(new WidthBreakpointType('80%', '50%', '20%', '20%').getValue(this.mainWindowInfo.widthBp))
```

[TripleColumnView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/TripleColumnView.ets#L52-L110)

### 三分栏典型场景——邮箱

在邮箱场景中，单栏状态下，默认展示收件箱页，当选择邮件对象后，展示邮件详情页。双栏和三栏状态下，右侧默认不展示邮件详情页，当选择邮件对象后，右侧展示邮件详情页。

**布局效果**

| 横向断点 | sm | md | lg/xl |
| --- | --- | --- | --- |
| 效果图（默认） |  |  |  |
| 效果图（内容） |  |  |  |

邮箱分为三个层级目录：第一层为账户信息，第二层为收件箱（一个账户信息对应多条邮件信息），第三层为邮件详情。根据内容的重要性，开发者在单栏模式下显示邮件详情，在双栏模式下显示收件箱和邮件详情，在三栏模式下显示账户信息、收件箱和邮件详情。

对于邮箱页面的一多分栏变化，开发者可以抽象为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/T6ScMH7aSQyt90QbZc9mMw/zh-cn_image_0000002509132789.png?HW-CC-KV=V1&HW-CC-Date=20260428T002058Z&HW-CC-Expire=86400&HW-CC-Sign=A35E0E66478E82AD915CC13743EE6B9F712CB5CAD45E27B2730DB8AEFDC43B99 "点击放大")

**示例代码**

* 对SideBarContainer组件的showSideBar属性进行赋值，如果横向断点为lg或xl，则默认显示侧边栏，反之，则默认不显示。

  ```
  1. build() {
  2. GridRow() {
  3. GridCol({ span: { sm: 12, md: 12, lg: 12, xl: 12 } }) {
  4. SideBarContainer(new WidthBreakpointType(SideBarContainerType.Overlay, SideBarContainerType.Overlay,
  5. SideBarContainerType.Embed, SideBarContainerType.Embed).getValue(this.mainWindowInfo.widthBp)) {
  6. // Area A
  7. Column() {
  8. MailSideBar()
  9. }
  10. .width('100%')
  11. .height('100%')
  12. .backgroundColor($r('sys.color.gray_01'))

  14. // Area B+C
  15. Column() {
  16. Stack() {
  17. MailNavigation({
  18. mainWindowInfo: this.mainWindowInfo,
  19. pageInfos: this.pageInfos,
  20. pathStack: this.pathStack,
  21. })
  22. .margin({ top: 18 })
  23. .padding({ left: this.getUIContext().px2vp(this.mainWindowInfo.AvoidSystem?.topRect.left) })
  24. // ...
  25. }
  26. }
  27. .width('100%')
  28. .height('100%')
  29. }
  30. .showSideBar(this.isShowingSidebar)
  31. // ...
  32. }
  33. }
  34. .width('100%')
  35. .height('100%')
  36. }
  ```

  [TripleMailView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/TripleMailView/TripleMailView.ets#L41-L96)

* 在SideBarContainer组件内容区中使用Navigation组件，对Navigation组件的mode属性进行赋值，如果断点为sm或xs，则为单栏，反之则为双栏。

  ```
  1. build() {
  2. Navigation(this.pathStack) {
  3. // ...
  4. }
  5. .mode(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? NavigationMode.Stack : this.notesNavMode)
  6. .navDestination(this.myRouter)
  7. // ...
  8. }
  ```

  [MailNavView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/TripleMailView/MailNavView.ets#L99-L180)

### 三分栏典型场景——日历

在三分栏的单栏布局中，通常展示的重点是Navigation的内容区。但在某些场景下，内容区的优先级低于导航区，例如日历日程功能。在这种情况下，单栏布局会优先展示日历（即Navigation的导航区）。效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/QL3DQlPTRsylBj7Ne_aOrg/zh-cn_image_0000002509292759.png?HW-CC-KV=V1&HW-CC-Date=20260428T002058Z&HW-CC-Expire=86400&HW-CC-Sign=5C9281B7F6B9B4F33E58FDADE04313B24DDD515F26DA5315843970A96686072B "点击放大")

日历日程分为三个层级，账户信息->日历->日程，开发者通常在单栏显示日历，双栏显示日历、日程，三栏显示账户信息、日历、日程。日历日程页面与邮箱页面的主要区别在于，日历日程页面的单栏页面重点显示Navigation导航栏，邮箱页面的单栏重点显示Navigation内容区。

**布局效果**

| 横向断点 | sm | md | lg/xl |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

**示例代码**

在Navigation的onNavigationModeChange属性中进行判断，当Navigation首次显示或单双栏状态发生变化时。

* 如果是单栏，则清空PathInfo路由，Navigation的内容区不显示，即可实现单栏显示Navigation导航栏的目的。
* 如果为双栏，则重新向PathInfo路由中push内容区参数，即可实现Navigation内容区显示具体日程的目的。

  ```
  1. Row() {
  2. // ...

  4. if (this.mainWindowInfo.widthBp !== WidthBreakpoint.WIDTH_SM) {
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
  18. Navigation(this.pathStack) {
  19. CalendarView({
  20. mainWindowInfo: this.mainWindowInfo,
  21. pathStack: this.pathStack,
  22. })
  23. }
  24. .navDestination(this.pageMap)
  25. .mode(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? NavigationMode.Stack : this.navMode)
  26. // ...
  27. .onNavigationModeChange((mode: NavigationMode) => {
  28. if (this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM || mode === NavigationMode.Stack) {
  29. this.pathStack.clear();
  30. } else if (mode === NavigationMode.Split) {
  31. this.pathStack.pushPath({ name: this.selectedItem.date, param: this.selectedItem }, false);
  32. }
  33. })
  ```

  [TripleCalendarView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/TripleCanlendarView/TripleCalendarView.ets#L108-L240)

## 挪移布局

挪移布局是指在空间充足时，通过调整组件的位置与展示方式，在左右布局与上下布局之间切换，用以展示更多内容或提高用户体验。常用的挪移布局包括插图和文字组合布局、底部/侧边导航。

### 插图和文字组合布局

插图和文字组合布局基于横向断点，设置组件所占不同的栅格数，实现左右布局与上下布局的切换。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 整个窗口划分为4栅格，歌单封面区（蓝）占4栅格，歌曲列表区（粉）占4栅格 | 整个窗口划分为8栅格，歌单封面区（蓝）占4栅格，歌曲列表区（粉）占4栅格 | 整个窗口划分为12栅格，歌单封面区（蓝）占4栅格，歌曲列表区（粉）占8栅格 |
| 展示布局 |  |  |  |

**实现方案**

设置不同横向断点下，[GridRow组件](../harmonyos-references/ts-container-gridrow.md)的columns、breakpoints属性，和[GridCol组件](../harmonyos-references/ts-container-gridcol.md)的span属性实现目标效果。

**示例代码**

```
1. GridRow({
2. columns: { xs: 4, sm: 4, md: 8, lg: 12, xl: 12 },
3. gutter: 0,
4. breakpoints: { value: ['320vp', '600vp', '840vp', '1440vp']},
5. direction: GridRowDirection.Row
6. }) {
7. GridCol({
8. span: { xs: 4, sm: 4, md: 4, lg: 4, xl: 4 },
9. offset: 0
10. }) {
11. // ...
12. }
13. .height(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? this.getGridColHeight() : '100%')
14. .padding({ top: this.getUIContext().px2vp(this.mainWindowInfo.AvoidSystem?.topRect.height) + 12})
15. .backgroundColor('#AAD3F1')

17. GridCol({
18. span: { xs: 4, sm: 4, md: 4, lg: 8, xl: 8 },
19. offset: 0
20. }) {
21. // ...
22. }
23. .backgroundColor(Color.Pink)
24. .layoutWeight(1)
25. .padding({ top: this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_SM ? 0 :
26. this.getUIContext().px2vp(this.mainWindowInfo.AvoidSystem?.topRect.height) })
27. }
```

[MoveView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/MoveView.ets#L27-L136)

说明

此布局场景也常用于页面顶部页签与搜索框，具体可参考如下布局效果。

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 展示布局 |  |  |  |

### 底部/侧边导航

底部/侧边导航基于横向断点，设置导航栏的位置与方向，实现上下布局与左右布局的切换。

电脑设备上的商务办公、实用工具垂类应用开发中，常使用侧边分级导航展示多级目录。而在一多开发时，侧边分级导航并不一定适用于手机、平板等设备，若需要实现导航栏内的分级效果，比较复杂。

当前系统支持手机、折叠屏、平板和电脑四种产品形态，分别对应sm、md、lg和xl四个断点，下文将实现不同断点下的分级导航栏。

**布局效果**

| 横向断点 | sm | md | lg | xl |
| --- | --- | --- | --- | --- |
| 属性 | 分级导航由底部一级导航栏和顶部二级页签组成 | 分级导航由底部一级导航栏和顶部二级页签组成 | 分级导航由侧边一级导航栏和顶部二级页签组成 | 通过侧边栏显示一级和二级导航 |
| 展示布局 |  |  |  |  |

当断点为sm或md时，显示底部导航和顶部页签；当断点为lg时，显示左侧导航；当断点为xl或设备为PC/2in1时，侧边显示一级和二级导航。

**实现方案**

开发一多分级导航栏时，需要实现4种断点下的一多效果：

* 订阅窗口尺寸变化，更新断点，触发页面布局更新。
* 在sm和md断点下，分级导航由底部一级导航栏和顶部二级页签组成。
* 在lg断点下，分级导航由侧边一级导航栏和顶部二级页签组成。
* 使用电脑设备或xl断点下，通过侧边栏显示一级和二级导航。

设置不同横向断点下，[Tabs组件](../harmonyos-references/ts-container-tabs.md)的barPosition、vertical、barHeight、barWidth和barMode属性实现目标效果。

**示例代码**

在sm、md和lg断点下，在首页调用Tabs组件，渲染一级导航目录信息到页签，并在内容区域调用已实现的页面视图，实现页面效果

```
1. // entry/src/main/ets/view/TabsView/TabsView.ets
2. Tabs({
3. barPosition: this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_LG ? BarPosition.Start : BarPosition.End
4. }) {
5. TabContent() {
6. TopTabView({
7. pageInfos: this.pageInfos,
8. mainWindowInfo: this.mainWindowInfo,
9. firstLevelIndex: this.firstLevelIndex,
10. tabData: this.tabData
11. })
12. }
13. .tabBar(this.tabBuilder(this.firstTabList[0], 0))

15. TabContent()
16. .tabBar(this.tabBuilder(this.firstTabList[1], 1))

18. TabContent()
19. .tabBar(this.tabBuilder(this.firstTabList[2], 2))

21. TabContent()
22. .tabBar(this.tabBuilder(this.firstTabList[3], 3))
23. }
24. .barBackgroundColor('#CCF1F3F5')
25. .barWidth(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_LG ? 96 : '100%')
26. .barHeight(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_LG ? '100%' : 56 + this.getUIContext().px2vp(this.mainWindowInfo.AvoidNavigationIndicator?.bottomRect.height))
27. .barMode(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_LG ? BarMode.Scrollable : BarMode.Fixed,
28. { nonScrollableLayoutStyle: LayoutStyle.ALWAYS_CENTER })
29. .barBackgroundBlurStyle(BlurStyle.COMPONENT_THICK)
30. .vertical(this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_LG)
31. .onChange((index: number) => {
32. this.firstLevelIndex = index;
33. })
```

[TabsView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/TabsView/TabsView.ets#L115-L147)

在xl断点下或使用PC/2in1设备，首页调用SideBarContainer组件，传入侧边栏区域组件和内容区域组件。此时可以结合[@State](../harmonyos-guides/arkts-state.md)和[@Link](../harmonyos-guides/arkts-link.md)装饰器，同步所需要的参数信息，如当前选中的一级目录索引和二级目录索引，可以用于呈现与页签强相关的页面内容。

```
1. // entry/src/main/ets/view/TabsView/TabsView.ets
2. if ((this.mainWindowInfo.widthBp === WidthBreakpoint.WIDTH_LG || this.mainWindowInfo.widthBp
3. === WidthBreakpoint.WIDTH_XL)&& deviceInfo.deviceType == "2in1") {
4. // Use SideBarContainer at XL breakpoint.
5. SideBarContainer(SideBarContainerType.Embed) {
6. TabSideBarView({
7. firstLevelIndex: this.firstLevelIndex,
8. secondLevelIndex: this.secondLevelIndex,
9. tabData: this.tabData,
10. firstTabList: this.firstTabList
11. })
12. Column() {
13. Row() {
14. // ...
15. Text(this.tabViewModel.getTabNameOfSecondLevel(this.tabViewModel.getTabNameOfFirstLevel(this.firstLevelIndex),
16. this.secondLevelIndex))
17. .fontSize('20fp')
18. .fontWeight(700)
19. .margin({
20. left: 16,
21. })
22. }
23. .padding({
24. top: 60,
25. bottom: 14,
26. })

28. VideoInfoView({
29. mainWindowInfo: this.mainWindowInfo,
30. firstLevelIndex: this.firstLevelIndex,
31. secondLevelIndex: this.secondLevelIndex
32. })
33. }
34. .alignItems(HorizontalAlign.Start)
35. }
36. .autoHide(false)
37. .divider({ strokeWidth: 0.3 })
38. .showControlButton(false)
39. .sideBarWidth(240)
40. .minSideBarWidth(240)
41. .maxSideBarWidth(240)
42. } else {
43. // ...
44. }
```

[TabsView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/TabsView/TabsView.ets#L62-L153)

## 缩进布局

缩进布局是指在空间充足时，组件居中展示并在两侧留白，通过调整内容的缩进来建立视觉层次结构，提高可读性和美观性。常用的缩进布局包括单列列表布局。

### 单列列表布局

单列列表布局基于横向断点，设置栅格子组件所占的栅格列数和偏移列数，实现缩进布局。

**布局效果**

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 属性 | 整个窗口划分为4栅格，单列列表占4列，偏移0列 | 整个窗口划分为8栅格，单列列表占6列，  两侧各偏移1列 | 整个窗口划分为12栅格，单列列表占8列，两侧各偏移2列 |
| 展示布局 |  |  |  |

**实现方案**

设置不同横向断点下，[GridRow组件](../harmonyos-references/ts-container-gridrow.md)的columns、breakpoints属性和[GridCol组件](../harmonyos-references/ts-container-gridcol.md)的span、offset属性实现目标效果。

**示例代码**

```
1. GridRow({
2. columns: { xs: 4, sm: 4, md: 8, lg: 12, xl: 12 },
3. gutter: 0,
4. breakpoints: { value: ['320vp', '600vp', '840vp', '1440vp']},
5. direction: GridRowDirection.Row
6. }) {
7. GridCol({
8. span: { xs: 4, sm: 4, md: 6, lg: 8, xl: 8 },
9. offset: { xs: 0, sm: 0, md: 1, lg: 2, xl: 2 }
10. }) {
11. // ...
12. }
13. .width('100%')
14. .height('100%')
15. }
```

[IndentedView.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/IndentedView.ets#L42-L79)

## 示例代码

* [基于一多能力实现响应式布局](https://gitcode.com/harmonyos_samples/ResponsiveLayout)
