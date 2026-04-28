---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-navigation
title: 多设备地图导航界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备地图导航界面
category: best-practices
scraped_at: 2026-04-28T08:21:15+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:8af6b346b646674d4e21551472a5bf670778862f91e9d2aaaa3abe89f3cc13df
---

## 概述

本文从目前流行的垂类市场中，选择地图行业应用作为典型案例详细介绍“一多”在实际开发中的应用。地图行业核心功能为定位、导航和打车等。根据这些核心功能，本文选择[首页](multi-travel-navigation.md#section39845311410)、[路线规划页](multi-travel-navigation.md#section19991633183514)、[服务卡片页](multi-travel-navigation.md#section167117194016)、[实况窗页](multi-travel-navigation.md#section168841418408)等作为典型页面进行开发，遵循多设备的差异性、一致性、灵活性和兼容性原则，帮助开发者快速高效地掌握“一多”能力，实现地图导航应用的相关功能。

地图类应用为了提升用户的使用体验，对垂类内的核心功能进行了独特设计：

* [首页](multi-travel-navigation.md#section39845311410)为了减少面板对地图的遮挡，采用手机端使用底部面板，而折叠屏展开态使用侧边面板的方式展示功能入口。
* 面板高度支持多档位调节以满足不同用户需求，其中手机端和折叠屏默认设置为中档位高度以方便查看地图时使用常用功能，而宽屏设备因屏幕空间充足支持面板拖拽至右侧。
* 用户查看[地点详情页](multi-travel-navigation.md#section122261042123411)时，选择地点后，地点详情信息展示在面板上。
* 在[搜索结果页](multi-travel-navigation.md#section535342543519)中，搜索框始终展示在面板上，避免遮挡地图。
* 在[路线规划页](multi-travel-navigation.md#section19991633183514)中，用户上滑或下滑面板时，路线推荐方案布局自适应变化，展示相同路线信息。
* 在宽屏设备上，[导航页](multi-travel-navigation.md#section5892174743917)通过侧边小弹窗和侧边底部面板展示路线信息，避免遮挡地图。
* 应用提供[服务卡片页](multi-travel-navigation.md#section167117194016)，展示常用功能、常用地点或路况信息等用户关注的内容，用户可以通过卡片进入应用。
* [实况窗页](multi-travel-navigation.md#section168841418408)可以在屏幕左上角实时更新定位、导航或打车的关键信息，并在通知中心中实时更新更多关键信息。

当前系统的产品形态包括直板机和双折叠（Mate X系列）。下文将围绕这两种产品形态，从UX设计、架构设计、页面开发三个角度，给出符合“一多”地图导航应用的最佳实践参考样例。

* [UX设计](multi-travel-navigation.md#section054881618315)章节介绍地图导航应用的交互逻辑和通用的设计要点，对于类似的设计要点，开发者可以直接拿来使用。
* [架构设计](multi-travel-navigation.md#section18115172420311)章节推荐“一多”应用使用目录结构更清晰的三层架构。
* [页面开发](multi-travel-navigation.md#section684313418314)章节会将页面划分为不同区域，介绍如何使用自适应布局和响应式布局实现不同的UI效果。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

[出行导航类](../design-guides/travel-and-navigation-0000001957391017.md)的多设备响应式设计指南可参考如上链接。

## 架构设计

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，构建了清晰、高效、可扩展的设计架构。更多详情请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

## 页面开发

本章介绍地图导航应用中如何使用“一多”的布局能力，完成页面层级的多端适配。下文将介绍每个页面区域的具体布局能力，帮助开发者从0到1进行开发。

说明

阅读本章节前，读者需熟悉[Map Kit简介](../harmonyos-guides/map-introduction.md)，并参考[应用开发准备](../harmonyos-guides/application-dev-overview.md)及[开发准备](../harmonyos-guides/map-config-agc.md)开通相关服务。下文将详细介绍地图导航的“一多”开发实践。

### 首页

首页展示当前位置信息，提供搜索地点、查看地点详情等入口，便于操作。观察不同设备上的UX设计图，进行如下设计：

* 将首页分为6个区域，效果图如下：

  |  | sm | md |
  | --- | --- | --- |
  | 效果图 |  |  |
* 对其中的各个区域分析使用的能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 地图 | 使用[MapComponent](../harmonyos-references/map-mapcomponent.md)组件实现地图的展示，默认占满窗口，并设置窗口的沉浸式。 |
  | 2 | 面板 | 使用[Stack](../harmonyos-references/ts-container-stack.md)组件，在地图上层嵌套[Column](../harmonyos-references/ts-container-column.md)组件实现面板，并借助[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化，设置在不同断点下面板的不同形态。在sm断点下面板底部展示，在md断点下悬浮展示。并通过绑定[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)实现在宽屏设备上的居左或居右变换。 |
  | 3 | 拖动区域 | 通过绑定[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)实现面板高度变换，当前支持三个档位变换调节。 |
  | 4 | 搜索框 | 使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件实现搜索框效果，通过[onSubmit()](../harmonyos-references/ts-basic-components-textinput.md#onsubmit)事件实现搜索功能。 |
  | 5 | 功能选择 | 使用[Grid](../harmonyos-references/ts-container-grid.md)组件实现均分能力，并在面板高度切换时，展示不同行数的功能。 |
  | 6 | 页签 | [Tabs](../harmonyos-references/ts-container-tabs.md)组件实现延伸能力，代码可参考多设备长视频界面的[底部/侧边页签](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)。 |
* 通过Stack组件在MapComponent上嵌套Column实现面板，并通过手势判定实现面板的多档位调节和位置改变。

  ```
  1. build() {
  2. Stack({ alignContent: Alignment.BottomStart }) {
  3. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })

  5. Column() {
  6. Row() {
  7. // ...
  8. }
  9. .height('26vp')
  10. .width('100%')
  11. .justifyContent(FlexAlign.Center)
  12. .gesture(
  13. PanGesture(this.panOptionHeight)
  14. .onActionUpdate((event?: GestureEvent) => {
  15. if (event) {
  16. let height = this.columnHeight - event.offsetY;
  17. this.tempColumnHeight = height;
  18. if (this.tempColumnHeight < 150) {
  19. this.tempColumnHeight = 150;
  20. }
  21. if (this.tempColumnHeight > this.columnMaxHeight) {
  22. this.tempColumnHeight = this.columnMaxHeight;
  23. }
  24. }
  25. })
  26. .onActionEnd(() => {
  27. if (this.tempColumnHeight > (this.columnMaxHeight - 269) / 2 + 269) {
  28. this.columnHeight = this.columnMaxHeight;
  29. this.isShowBack = false;
  30. } else if (this.tempColumnHeight < (269 - 150) / 2 + 150) {
  31. this.columnHeight = 150;
  32. this.isShowBack = true;
  33. } else {
  34. this.columnHeight = 269;
  35. this.isShowBack = true;
  36. }
  37. this.tempColumnHeight = this.columnHeight;
  38. })
  39. )

  41. // ...
  42. }
  43. // ...
  44. .gesture(
  45. PanGesture(this.panOptionPosition)
  46. .onActionUpdate((event?: GestureEvent) => {
  47. if (event) {
  48. let position = this.left + event.offsetX;
  49. this.tempLeft = position;
  50. if (this.tempLeft < 24) {
  51. this.tempLeft = 24;
  52. }
  53. if (this.tempLeft > 350) {
  54. this.tempLeft = 350;
  55. }
  56. }
  57. })
  58. .onActionEnd(() => {
  59. if (this.tempLeft < 200) {
  60. this.left = 24;
  61. } else {
  62. this.left = 350;
  63. }
  64. this.tempLeft = this.left;
  65. })
  66. )
  67. // ...
  68. }
  69. .height('100%')
  70. .width('100%')
  71. }
  ```

  [MapView.ets](https://gitcode.com/harmonyos_samples/multi-travel-navigation/blob/master/features/map/src/main/ets/view/MapView.ets#L129-L266)

### 地点详情页

地点详情页展示用户所选地点的详细信息，并提供导航和路线规划入口。观察地点详情页在不同设备上的UX设计图，可以进行以下设计：

* 将地点详情页划分为2个区域，效果图如下：

  |  | sm | md |
  | --- | --- | --- |
  | 效果图 |  |  |
* 对各区域使用的能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 图片轮播区 | [Swiper](../harmonyos-references/ts-container-swiper.md)实现图片轮播切换。 |
  | 2 | 景点信息 | [List](../harmonyos-references/ts-container-list.md)实现[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)。 |

### 搜索结果页

搜索结果页展示附近相关地点列表，根据用户输入内容生成。观察搜索结果页在不同设备上的UX设计图，可以进行以下设计：

* 将搜索结果页划分为2个区域。效果图如下：

  |  | sm | md |
  | --- | --- | --- |
  | 搜索结果列表-中档位面板效果 |  |  |
  | 搜索结果列表-高档位面板效果 |  |  |
* 对其中的各个区域分析使用的能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 搜索框 | 搜索内容后，右侧按钮变为取消。代码参考多设备长视频界面的[顶部页签及搜索框](multi-video-app.md#zh-cn_topic_0000001744653537_li1346175796)。 |
  | 2 | 搜索结果列表 | 面板处于中档位时采用[Swiper](../harmonyos-references/ts-container-swiper.md)实现延伸能力，高档位时采用[List](../harmonyos-references/ts-container-list.md)实现延伸能力。 |

### 路线规划页

路线规划页默认展示最多三条驾车路线及其相关信息。观察路线规划页在不同设备上的UX设计图，可以进行以下设计：

* 将路线规划页划分为4个区域，效果图如下：

  |  | sm | md |
  | --- | --- | --- |
  | 路线搜索效果 |  |  |
  | 路径规划结果 |  |  |
* 对其中的各个区域分析使用的能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 输入区域 | 通过判断当前面板高度更换按钮及输入区域布局，[Row](../harmonyos-references/ts-container-row.md)组件配合layoutWeight实现拉伸能力，代码可参考多设备长视频界面的[视频简介](multi-video-app.md#zh-cn_topic_0000001744653537_li1134192618160)。 |
  | 2 | 方案页签 | [Tabs](../harmonyos-references/ts-container-tabs.md)组件实现延伸能力，代码可参考多设备长视频界面的[顶部页签及搜索框](multi-video-app.md#zh-cn_topic_0000001744653537_li1346175796)。 |
  | 3 | 常去地点信息 | [Column](../harmonyos-references/ts-container-column.md)组件实现[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)。 |
  | 4 | 路线规划结果 | [List](../harmonyos-references/ts-container-list.md)组件实现[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)，并在不同面板高度时设置List的不同方向。 |

### 导航页

导航页提供实时导航和路况、剩余路线信息展示。观察不同设备上的导航页UX设计图，可以进行如下设计：

* 将导航页划分为两个区域，效果图如下：

  |  | sm | md |
  | --- | --- | --- |
  | 效果图 |  |  |
* 分析各区域使用的能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 当前路径信息 | [栅格](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化实现[挪移布局](bpta-multi-device-responsive-layout.md#section1153210192360)。 |
  | 2 | 剩余路线信息 | [Row](../harmonyos-references/ts-container-row.md)组件设置justifyContent属性为SpaceBetween实现自适应占满。 |

### 打车页

打车页展示可选择的车辆类型及价格，并提供打车功能。观察打车页在不同设备上的UX设计图，进行如下设计：

* 将打车页划分为两个区域，效果图如下：

  |  | sm | md |
  | --- | --- | --- |
  | 效果图 |  |  |
* 对各区域的分析能力及实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 车辆信息 | [List](../harmonyos-references/ts-container-list.md)组件实现[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)。 |
  | 2 | 打车 | [Row](../harmonyos-references/ts-container-row.md)组件实现拉伸效果。 |

### 服务卡片页

说明

阅读本章节前，读者需熟悉[Form Kit（卡片开发服务）](../harmonyos-guides/form-kit.md)以及[ArkTS卡片开发（推荐）](../harmonyos-guides/arkts-ui.md)。下面将详细介绍ArkTS卡片在“一多”开发中的实践。

服务卡片页展示应用常用功能、地点及路况等信息。观察不同设备上的UX设计图，可以进行如下设计：

* 服务卡片效果图如下：

  |  | sm | md |
  | --- | --- | --- |
  | 效果图 |  |  |
* 对其中的各个区域分析使用的能力，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 静态卡片 | 在多端均采用2\*4的八宫格静态卡片。可参考[创建ArkTS卡片](../harmonyos-guides/arkts-ui-widget-creation.md)在入口模块创建一个静态卡片，并[配置ArkTS卡片的配置文件](../harmonyos-guides/arkts-ui-widget-configuration.md)。 |

* 静态卡片的实现

  在入口模块创建静态卡片，添加显示内容，通过FormLink实现静态卡片与提供方应用的交互。

  ```
  1. Column() {
  2. FormLink({
  3. action: 'router',
  4. abilityName: 'EntryAbility',
  5. params: {
  6. message: 'add detail'
  7. }
  8. }) {
  9. Column() {
  10. Row() {
  11. Image($r('app.media.ic_public_input_search'))
  12. .width('15vp')
  13. .margin({
  14. left: '10vp',
  15. right: '10vp'
  16. })

  18. Text($r('app.string.textInput_holder'))
  19. .fontColor('#99000000')
  20. .width('80%')
  21. .maxLines(1)
  22. .textOverflow({ overflow: TextOverflow.Ellipsis })
  23. }
  24. .borderRadius('22vp')
  25. .width('100%')
  26. .height('44vp')
  27. .backgroundColor('#0d000000')
  28. .margin({ top: '20vp' })

  30. Row() {
  31. ForEach(FormViewData.FUNCTIONS, (item: FunctionType) => {
  32. Column() {
  33. Image(item.icon)
  34. .width('40vp')
  35. .height('40vp')

  37. Text(item.desc)
  38. .fontSize('12vp')
  39. .padding({ top: '4vp' })
  40. }
  41. }, (item: FunctionType) => item.id.toString())
  42. }
  43. .justifyContent(FlexAlign.SpaceBetween)
  44. .height('60%')
  45. .width('100%')
  46. }
  47. .width('90%')
  48. }
  49. }
  50. .width('100%')
  ```

  [FormCard.ets](https://gitcode.com/harmonyos_samples/multi-travel-navigation/blob/master/products/phone/src/main/ets/form/pages/FormCard.ets#L38-L87)

### 实况窗页

说明

阅读本章节前，读者需熟悉[Live View Kit简介](../harmonyos-guides/liveview-introduction.md)及[实况窗支持对接的场景](../harmonyos-guides/liveview-introduction.md#section4266105713209)，并根据读者的开发场景进行[开发准备](../harmonyos-guides/liveview-preparations.md)。下面将详细介绍实况窗在“一多”开发中的实践。

实况窗页支持卡片和胶囊两种形态，分别展示在锁屏、通知中心和状态栏。查看不同设备上的UX设计图，可以进行以下设计：

* 实况窗及服务胶囊效果图如下：

  |  | 通知中心 | 状态栏 | 实况胶囊 |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |
* 对各个区域进行能力分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 卡片形态 | 实况窗默认支持多端效果，本应用实现效果为[强调文本模板](../harmonyos-guides/liveview-create-locally.md#section113626521804)，实况窗拉起时展示在通知中心、和锁屏界面，点击实况胶囊后展示在状态栏。 |
  | 2 | 胶囊形态 | 实况胶囊默认支持多端效果，本应用实现效果为文本胶囊[TextCapsule](../harmonyos-references/liveview-liveviewmanager.md#section1440294811375)。 |
* 应用在后台运行时，拉起实况窗和实况胶囊，并配置相应参数。

  ```
  1. private static async buildDefaultView(): Promise<liveViewManager.LiveView> {
  2. return {
  3. id: 0,
  4. event: 'PICK_UP',
  5. liveViewData: {
  6. primary: {
  7. title: 'The driver has taken the order',
  8. content: [
  9. {
  10. text: 'distance from you',
  11. },
  12. {
  13. text: '1 km',
  14. textColor: '#FF0A59F7'
  15. }
  16. ],
  17. keepTime: 15,
  18. clickAction: await LiveViewController.buildWantAgent(),
  19. layoutData: {
  20. layoutType: 4,
  21. underlineColor: '#00ffffff',
  22. title: 'Deep Space Gray · Question M7',
  23. content: 'Pard 123456',
  24. descPic: 'taxi.png'
  25. }
  26. },
  27. capsule: {
  28. type: 1,
  29. status: 1,
  30. icon: 'navigate.png',
  31. backgroundColor: '#FF0A59F7',
  32. title: '1 km'
  33. }
  34. }
  35. };
  36. }
  ```

  [LiveViewController.ets](https://gitcode.com/harmonyos_samples/multi-travel-navigation/blob/master/features/live/src/main/ets/viewmodel/LiveViewController.ets#L48-L84)

## 示例代码

* [多设备地图导航界面](https://gitcode.com/harmonyos_samples/multi-travel-navigation)
