---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-start
title: 从一个例子开始
breadcrumb: 最佳实践 > 一次开发，多端部署 > 从一个例子开始
category: best-practices
scraped_at: 2026-04-29T14:11:53+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:d263c43ca9149bc71918d0ea1679c929cd5b70464031e5094843be857ae696ef
---

本章通过一个天气应用，介绍一多应用的整体开发过程，包括UX设计、工程管理及调试、页面开发等。

## UX设计

本示例中的天气应用包含主页、管理城市和添加城市三个页面，其中主页中又包含菜单和更新间隔两个弹窗，基本业务逻辑如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/IFgY6LudQ3my6tXgSnTLXg/zh-cn_image_0000002417910860.png?HW-CC-KV=V1&HW-CC-Date=20260429T061149Z&HW-CC-Expire=86400&HW-CC-Sign=8B0D34ABCFCA3C7291D67DB14E0143594402E695E883C96270151E93BAE177F0 "点击放大")

“一多”建议从最初的设计阶段开始就拉通多设备综合考虑。考虑实际智能终端设备种类繁多，设计师无法针对每种具体设备各自出一份UX设计图。“一多”建议从设备应用窗口宽度和窗口高宽比两个维度，将设备划分类别。

以应用窗口宽度为判断条件，建议划分为5个区间：

| 设备类型 | 窗口宽度（vp） |
| --- | --- |
| 超小设备 | (0, 320） |
| 小设备 | [320, 600) |
| 中设备 | [600, 840) |
| 大设备 | [840, 1440) |
| 超大设备 | [1440, +∞) |

根据应用窗口的高宽比进行判断，建议划分为3个区间：

| 设备类型 | 高宽比 |
| --- | --- |
| 小设备 | (0, 0.8) |
| 中设备 | [0.8, 1.2) |
| 大设备 | [1.2, +∞) |

说明

* vp是virtual pixel（虚拟像素）的缩写，是常用的长度单位。

直板机、双折叠、平板对应于小设备、中设备及大设备，本示例以这三种设备场景为例，介绍不同设备上的UX设计。天气主页在不同设备上的设计图如下所示。

|  | 小设备 | 中设备 | 大设备 |
| --- | --- | --- | --- |
| 主页 |  |  |  |

另外，大设备中天气主页还允许用户开启或者隐藏侧边栏。

| 开启侧边栏 | 隐藏侧边栏 |
| --- | --- |
|  |  |

从天气应用在各设备上的UX设计图中，可以观察到如下UX的一些“规律”：

* 在不同的屏幕宽度下，应用的整体风格基本保持一致。
* 在相近的屏幕宽度范围内，应用的布局基本不变；在不同的屏幕宽度范围内，应用的布局有较大差异。
* 应用在小屏幕下显示的元素，是大屏幕中显示元素的子集。

  + 考虑到屏幕尺寸及显示效果，大屏幕中可以显示的元素数量一定不少于小屏幕。
  + 为充分利用屏幕尺寸优势，大屏幕可以有其独有的元素或设计（如本示例中的侧边栏）。

如此，既在各设备上体现了UX的一致性，也在各设备上体现了UX的差异性，从而既可以保障各设备上应用界面的体验，也可以最大程度复用界面代码。

## 工程管理及调试

完成UX设计后，接下来需要考虑如何将设计转化为实际可运行的工程，在本文[多设备工程部署](bpta-multi-device-ide.md)中，将详细介绍一多的工程创建及管理等，本小节仅介绍最基础的工程创建及多设备预览调试。

### 工程创建

一多应用的工程创建过程，与传统应用并无较大差异。只需在工程创建过程中，注意在“Device Type”选项中勾选所有该应用期望运行的目标设备类型，保证后续该应用可以在所有目标设备上正确安装即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/5VCBPiSXQ0mlK1CZ9rw0zQ/zh-cn_image_0000002552894591.png?HW-CC-KV=V1&HW-CC-Date=20260429T061149Z&HW-CC-Expire=86400&HW-CC-Sign=D6A1F6F128AF4E852EA86F39A38CA49DE33D35DF93D0E317FC658C0925EBBB97 "点击放大")

### 预览调试

在代码开发过程中，可以开启预览器，并打开“Multi-profile preview”开关，实时观察应用在不同设备下的表现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Bie-rgQzR6C86ZMpFikGQw/zh-cn_image_0000002355145441.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061149Z&HW-CC-Expire=86400&HW-CC-Sign=A878FEFD36746F55C8B1C7289F6020EB30D84DF47EE272191C5BCCA4C7EDF5F0 "点击放大")

特别的，还可以点击“+ New Profile”按钮，新增自定义预览器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/bRpT0agqTkGPAOEgoqaNzQ/zh-cn_image_0000002321146750.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061149Z&HW-CC-Expire=86400&HW-CC-Sign=C9A7262AF5416D26F00045862F18A6D979B3E8B0AA03D518ADD8F6E3A644D5D5 "点击放大")

## 页面开发

天气应用中涉及较多的页面和弹窗，本小节以天气主页为例，简单介绍不同设备下的页面实现思路。

观察天气主页在不同设备上的UX设计图，可以进行如下设计：

* 将天气主页划分为9个基础区域，如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/zLSo6eQcSVu_OHmPUk_AJg/zh-cn_image_0000002355265301.png?HW-CC-KV=V1&HW-CC-Date=20260429T061149Z&HW-CC-Expire=86400&HW-CC-Sign=C13887A88FA80F1DAAC6B17D601E4C9696D13B9572E73E02EDC0B713D08456B7 "点击放大")
* 基础区域9仅在大设备上显示（需要在大设备上展开侧边导航栏），基础区域1-8虽然在各设备上始终展示但其尺寸及区域内的布局基本保持不变（区域8需要向下滑动设备至底部，下方示例图不做展示），可以结合[自适应布局](bpta-multi-device-adaptive-layout.md)能力以[自定义组件](../harmonyos-guides/arkts-create-custom-components.md)的形式分别实现这9个基础区域。

  |  | 小设备 | 中设备 | 大设备 |
  | --- | --- | --- | --- |
  | 主页 |  |  |  |
* 基础区域1-8之间的布局在不同设备上有较大差异，可以使用响应式布局中的[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)能力实现组件间的布局效果。
* 展开和隐藏侧边栏的功能可以通过[侧边栏组件](../harmonyos-references/ts-container-sidebarcontainer.md)来实现。侧边栏是大设备上独有的，借助响应式布局中的[媒体查询](bpta-multi-device-responsive-layout.md#section1950102518311)能力，控制仅在大设备上展示侧边栏即可。

### 主页基础区域

天气主页中的9个基础区域介绍及实现方案如下表所示。

| 编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 标题栏 | 自适应布局拉伸能力。 |
| 2 | 天气概览 | Row和Column组件，并指定其子组件按照主轴起始方向对齐或居中对齐。 |
| 3 | 每小时天气 | 自适应布局延伸能力。 |
| 4 | 每日天气 | 自适应布局延伸能力。 |
| 5 | 空气质量 | Canvas画布组件绘制空气质量图，并使用Row组件和Column组件控制内部元素的布局。 |
| 6 | 生活指数 | 自适应布局均分能力。 |
| 7 | 日出日落 | Canvas画布组件绘制日出日落图。 |
| 8 | 应用信息 | Row和Column组件，并指定其子组件居中对齐。 |
| 9 | 侧边导航栏 | 综合运用自适应布局中的拉伸能力、占比能力和延伸能力。 |

天气主页涉及的内容较多，因篇幅限制，本小节仅介绍区域3（每小时天气）的实现。

延伸能力是指容器组件内的子组件，按照其在列表中的先后顺序，随容器组件尺寸变化显示或隐藏。随着可用显示区域的增加，用户可以看到的“每小时天气”信息也不断增加，故“每小时天气”可以通过延伸能力实现，其核心代码如下所示。

```
1. import { Forecast, getHoursData, MyDataSource, Style } from 'common';

3. @Preview
4. @Component
5. export default struct HoursWeather {
6. hoursData: Forecast[] = getHoursData(0);
7. @State hoursDataResource: MyDataSource<Forecast> = new MyDataSource(this.hoursData);
8. @StorageLink('curBp') curBp: string = 'lg';

10. // ...
11. build() {
12. // Implement extensibility capability through list component.
13. List() {
14. LazyForEach(this.hoursDataResource, (hoursItem: Forecast) => {
15. ListItem() {
16. this.HoursWeatherItem(hoursItem,
17. this.curBp === 'lg' ? Style.WEATHER_ITEM_WIDTH + 2 : Style.WEATHER_ITEM_WIDTH)
18. }
19. }, (hoursItem: Forecast, index: number) => JSON.stringify(hoursItem) + index)
20. }
21. .width('100%')
22. .height(Style.CARD_HEIGHT)
23. .borderRadius(Style.NORMAL_RADIUS)
24. .backgroundColor(Style.CARD_BACKGROUND_COLOR)
25. .listDirection(Axis.Horizontal)
26. }
27. }
```

[HoursWeather.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Weather/product/default/src/main/ets/pages/HoursWeather.ets#L17-L80)

### 城市天气详情

天气主页右侧的城市天气详情由区域1-8组成，区域1（标题栏）始终固定在页面顶部，区域2-8在不同设备下的布局不同且可以随页面上下滚动。本小节介绍如何实现城市天气详情中区域2~8的布局效果。

设备屏幕可能无法一次性显示区域2-8的所有内容，故需要在外层增加滚动组件（即Scroll组件）以支持上下滚动。不同设备下区域2-8的相对位置一共有三套不同的布局，可以借助响应式布局中的[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)实现这一效果。本示例中将栅格在不同场景下分别划分为4列、8列和12列，区域2-8在不同场景下的布局如下表所示。

| 小设备 | 中设备 或 大设备（侧边栏显示状态） | 大设备（侧边栏隐藏状态） |
| --- | --- | --- |
|  |  |  |

说明

为提升用户体验，大设备侧边栏隐藏状态下，每日天气与空气质量的相对顺序发生了改变。可以通过调整GridCol栅格子组件的order属性，实现目标效果。

```
1. import AirQuality from './AirQuality';
2. import HoursWeather from './HoursWeather';
3. import IndexHeader from './IndexHeader';
4. import IndexEnd from './IndexEnd';
5. import LifeIndex from './LifeIndex';
6. import MultidayWeather from './MultidayWeather';
7. import SunCanvas from './SunCanvas';
8. import { CityListData, Style } from 'common';

10. @Component
11. export default struct HomeContent {
12. @Prop showSideBar: boolean;
13. @StorageLink('titleText') titleText: string[] = [];
14. @StorageLink('swiperIndex') swiperIndex: number = 0;
15. @State headerOpacity: number = 1;
16. cityListData?: CityListData;
17. index: number = 1;
18. scroller: Scroller = new Scroller();

20. build() {
21. Scroll(this.scroller) {
22. GridRow({
23. columns: {
24. xs: 4,
25. sm: 4,
26. md: 8,
27. lg: this.showSideBar ? 8 : 12
28. },
29. gutter: { x: Style.GRID_GUTTER, y: Style.GRID_GUTTER },
30. breakpoints: { reference: BreakpointsReference.WindowSize }
31. }) {
32. // Weather overview.
33. GridCol({
34. span: {
35. xs: 4,
36. sm: 4,
37. md: 8,
38. lg: this.showSideBar ? 8 : 12
39. },
40. order: 0
41. }) {
42. IndexHeader({ headerDate: this.cityListData!.header, index: this.index })
43. .opacity(this.headerOpacity)
44. }

46. // Hourly weather.
47. GridCol({
48. span: {
49. xs: 4,
50. sm: 4,
51. md: 8,
52. lg: 8
53. },
54. order: 1
55. }) {
56. HoursWeather({ hoursData: this.cityListData!.hoursData })
57. }

59. // Daily weather.
60. GridCol({
61. span: 4,
62. order: {
63. xs: 2,
64. sm: 2,
65. md: 2,
66. lg: this.showSideBar ? 2 : 3
67. }
68. },) {
69. MultidayWeather({ weekData: this.cityListData!.weekData })
70. }

72. // Air quality.
73. GridCol({
74. span: 4,
75. order: {
76. xs: 3,
77. sm: 3,
78. md: 3,
79. lg: this.showSideBar ? 3 : 2
80. }
81. }) {
82. AirQuality({ airData: this.cityListData!.airData, airIndexData: this.cityListData!.airIndex })
83. }

85. // Living index.
86. GridCol({ span: 4, order: 4 }) {
87. LifeIndex({ lifeData: this.cityListData!.suitDate })
88. }

90. // Sun canvas.
91. GridCol({ span: 4, order: 5 }) {
92. SunCanvas()
93. }

95. // Index end.
96. GridCol({
97. span: {
98. xs: 4,
99. sm: 4,
100. md: 8,
101. lg: this.showSideBar ? 8 : 12
102. },
103. order: 6
104. }) {
105. IndexEnd()
106. }
107. }
108. }
109. // ...
110. }
111. }
```

[HomeContent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Weather/product/default/src/main/ets/pages/HomeContent.ets#L17-L142)

### 主页整体实现

综合考虑各设备下的效果，天气主页的根节点使用侧边栏组件：

* 小设备和中设备既不展示侧边栏，也不提供控制侧边栏显示和隐藏的按钮。
* 大设备默认展示侧边栏，同时提供控制侧边栏显示和隐藏的按钮。

另外主页右侧的城市天气详情，支持左右滑动切换城市，可以使用[Swiper组件](../harmonyos-references/ts-container-swiper.md)实现目标效果：

* 小设备和中设备开启Swiper组件的导航点，引导用户通过左右滑动切换不同城市。
* 大设备中用户通过点击侧边栏中的城市列表即可高效的切换不同城市，此时需要关闭Swiper组件的导航点。

```
1. import HomeContent from './HomeContent';
2. import IndexTitleBar from './IndexTitleBar';
3. import SideContent from './SideContent';
4. import { CityListData, Style, getBg, getCityListWeatherData, Logger } from 'common';
5. // ...

7. @Entry
8. @Component
9. struct Home {
10. // ...
11. @State curBp: string = 'md';
12. @State cityListWeatherData: CityListData[] = getCityListWeatherData();
13. @State showSideBar: boolean = false;
14. // ...

16. build() {
17. SideBarContainer(SideBarContainerType.Embed) {
18. // Left sidebar.
19. SideContent({ showSideBar: $showSideBar })
20. .height('100%')
21. // Right content area.
22. Column() {
23. // Title bar.
24. IndexTitleBar({ showSideBar: $showSideBar })
25. .height(56)
26. // Weather details.
27. Swiper() {
28. ForEach(this.cityListWeatherData, (item: CityListData, index: number) => {
29. HomeContent({ showSideBar: this.showSideBar, cityListData: item, index: index })
30. }, (item: CityListData, index: number) => JSON.stringify(item) + index)
31. }
32. .id('swiper')
33. .padding({ left: Style.NORMAL_PADDING, right: Style.NORMAL_PADDING })
34. .onChange(index => {
35. this.swiperIndex = index;
36. AppStorage.setOrCreate('swiperIndex', this.swiperIndex);
37. })
38. // Disable navigation dots on lg width breakpoint.
39. .indicator(this.curBp !== 'lg' ? new DotIndicator()
40. .selectedColor(Color.White) : false
41. )
42. .index(this.swiperIndex)
43. .loop(false)
44. .width('100%')
45. .layoutWeight(1)
46. }
47. .height('100%')
48. }
49. .height('100%')
50. .sideBarWidth('33.3%')
51. .minSideBarWidth('33.3%')
52. .maxSideBarWidth('33.3%')
53. .showControlButton(false)
54. .showSideBar(this.showSideBar)
55. .backgroundImageSize(ImageSize.Cover)
56. .backgroundImage(getBg(this.cityListWeatherData[this.swiperIndex].header.weatherType))
57. }
58. // ...
59. }
```

[Home.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Weather/product/default/src/main/ets/pages/Home.ets#L18-L138)

最终，天气首页的运行效果如下图所示。

| 小设备 | 中设备 | 大设备（隐藏侧边栏） | 大设备（显示侧边栏） |
| --- | --- | --- | --- |
|  |  |  |  |

## 功能开发

应用开发不仅包含应用页面开发，还包括应用后端功能开发以及服务器端开发等。服务器端开发不在本文的讨论范围内，本小节仅介绍多设备上应用功能开发的注意事项。

如前文所示，本示例的目标运行设备是小设备、中设备和大设备，对应实际的设备类型为默认设备和平板等。这些设备运行的都是标准系统，其系统能力一致，所以无需做特别考虑。但是在超小设备（对应的实际设备类型为智能穿戴设备等）上，考虑CPU、内存、硬盘等硬件限制，往往会对系统进行裁剪。如果在应用后端功能开发时调用当前系统没有的能力，就可能会引发异常。

通常有两种方式解决上述问题：

* 在应用安装包中描述其需要的系统能力，保证本应用仅被分发和安装到可以满足其诉求的系统中。
* 在使用特定系统能力前，通过canIUse接口判断系统能力是否存在，进而执行不同的逻辑。

在本文的[多设备功能开发](bpta-multi-device-function.md)章节中，将详细展开介绍。

## 示例代码

* [一多天气](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/Weather)
