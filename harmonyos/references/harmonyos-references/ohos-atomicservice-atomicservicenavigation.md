---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation
title: AtomicServiceNavigation
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > AtomicServiceNavigation
category: harmonyos-references
scraped_at: 2026-04-29T13:52:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:402ea4147ca60e5991e9ee5da68844f7132e2297c0b5d29c453149882b393ec4
---

作为Page页面的根容器使用，其内部默认包含了标题栏、内容区，其中内容区默认首页显示导航内容或非首页显示（[NavDestination](ts-basic-components-navdestination.md)的子组件），首页和非首页通过路由进行切换。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AtomicServiceNavigation } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

从API version 10开始，推荐使用[NavPathStack](ts-basic-components-navigation.md#navpathstack10)进行页面路由。

## AtomicServiceNavigation

PhonePC/2in1TabletTVWearable

```
1. AtomicServiceNavigation({
2. navPathStack?: NavPathStack,
3. navigationContent: Callback<void>,
4. title?: ResourceStr,
5. titleOptions?: TitleOptions,
6. gradientBackground?: GradientBackground,
7. hideTitleBar?: boolean,
8. navBarWidth?: Length,
9. mode?: NavigationMode,
10. navDestinationBuilder?: NavDestinationBuilder,
11. navBarWidthRange?: [Dimension, Dimension],
12. minContentWidth?: Dimension,
13. sideBarOptions?: SideBarOptions,
14. sideBarContent?: Callback<void>,
15. menus?: CustomBuilder | Array<NavigationMenuItem>,
16. stateChangeCallback?: Callback<boolean>,
17. modeChangeCallback?: Callback<NavigationMode>
18. })
```

**装饰器类型：** @Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| navPathStack | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 否 | @State | 路由栈信息。默认值为new NavPathStack()。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navigationContent | Callback<void> | 否 | @BuilderParam | Navigation容器内容。默认值为空，无内容展示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 设置页面标题。默认值为空字符串。当titleOptions的titleBarType字段设置为[TitleBarType](ohos-atomicservice-atomicservicenavigation.md#titlebartype18).ROUND\_ICON或者[TitleBarType](ohos-atomicservice-atomicservicenavigation.md#titlebartype18).SQUARED\_ICON，且设置了titleIcon时，title标题内容将不会显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| titleOptions | [TitleOptions](ohos-atomicservice-atomicservicenavigation.md#titleoptions) | 否 | @Prop | 标题栏选项。默认值为{ isBlurEnabled: true }。当titleBarType字段设置为[TitleBarType](ohos-atomicservice-atomicservicenavigation.md#titlebartype18).ROUND\_ICON或者[TitleBarType](ohos-atomicservice-atomicservicenavigation.md#titlebartype18).SQUARED\_ICON，且设置了titleIcon时，title标题内容将不会显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| gradientBackground18+ | [GradientBackground](ohos-atomicservice-atomicservicenavigation.md#gradientbackground18) | 否 | @Prop | 背景色选项。默认值见[GradientBackground](ohos-atomicservice-atomicservicenavigation.md#gradientbackground18)。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| hideTitleBar | boolean | 否 | @Prop | 设置是否隐藏标题栏。默认为false。  false表示显示标题栏，true表示隐藏标题栏。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navBarWidth | [Length](ts-types.md#length) | 否 | @Prop | 设置导航栏宽度。默认值为240vp。  仅在Navigation组件分栏时生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mode | [NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明) | 否 | @Prop | 设置导航栏的显示模式。默认值为Auto。  支持Stack、Split与Auto模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navDestinationBuilder | [NavDestinationBuilder](ohos-atomicservice-atomicservicenavigation.md#navdestinationbuilder) | 否 | @BuilderParam | 创建[NavDestination](ts-basic-components-navdestination.md)组件所需要的Builder数据。默认值为空，即无内容展示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navBarWidthRange | [[Dimension](ts-types.md#dimension10), [Dimension](ts-types.md#dimension10)] | 否 | @Prop | 设置导航栏最小和最大宽度（双栏模式下生效）。默认值：最小默认值为240vp，最大默认值为组件宽度的40%，且不大于432vp，如果只设置一个值，则未设置的值按照默认值计算。单位：vp。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| minContentWidth | [Dimension](ts-types.md#dimension10) | 否 | @Prop | 设置导航栏内容区最小宽度（双栏模式下生效）。默认值为360vp。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sideBarOptions18+ | [SideBarOptions](ohos-atomicservice-atomicservicenavigation.md#sidebaroptions18) | 否 | @Prop | 侧边栏的功能选项。默认值为{ sideBarBackground: $r('sys.color.ohos\_id\_color\_sub\_background'), sideBarIcon: $r('sys.symbol.open\_sidebar') }。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| sideBarContent18+ | Callback<void> | 否 | @BuilderParam | 侧边栏的内容。默认值为空。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| menus18+ | [CustomBuilder](ts-types.md#custombuilder8) | Array<[NavigationMenuItem](ts-basic-components-navigation.md#navigationmenuitem)> | 否 | @BuilderParam | 宽屏场景下用户自定义插入的布局样式。默认值为空，不显示任何样式。屏幕宽度低于600vp为非宽屏场景，大于等于600vp为宽屏场景。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| stateChangeCallback | Callback<boolean> | 否 | - | 导航栏显示状态切换时触发该回调。true表示导航栏显示状态发生了切换。默认值为空。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| modeChangeCallback | Callback<[NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明)> | 否 | - | 当Navigation首次显示或者单双栏状态发生变化时触发该回调。默认值为空。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## TitleOptions

PhonePC/2in1TabletTVWearable

标题栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏背景颜色。默认值为系统默认颜色。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isBlurEnabled | boolean | 否 | 是 | 标题栏是否模糊，默认值：true，表示标题栏模糊。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| barStyle | [BarStyle](ts-basic-components-navigation.md#barstyle12枚举说明) | 否 | 是 | 标题栏样式属性设置。默认值为BarStyle.STANDARD。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| titleBarType18+ | [TitleBarType](ohos-atomicservice-atomicservicenavigation.md#titlebartype18) | 否 | 是 | 设置标题栏类型。默认值为TitleBarType.ROUND\_ICON。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| titleIcon18+ | [Resource](ts-types.md#resource) | [SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置标题栏的图标。默认值为$r('sys.color.ohos\_id\_color\_titlebar\_icon')。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## GradientBackground18+

PhonePC/2in1TabletTVWearable

供开发者设置品牌渐变色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 单色渐变色彩值和双色渐变第一色彩值。默认值为空，即无颜色设置。 |
| secondaryColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 双色渐变色第二色彩值。默认值为空，即无颜色设置。 |
| backgroundTheme | [BackgroundTheme](ohos-atomicservice-atomicservicenavigation.md#backgroundtheme18) | 否 | 是 | 导航栏背景底色。默认值为DEFAULT。 |
| mixMode | [MixMode](ohos-atomicservice-atomicservicenavigation.md#mixmode18) | 否 | 是 | 同时设置primaryColor和secondaryColor时此参数生效。代表双色渐变下两种颜色的融合方式。默认值为TOWARDS。 |
| alpha | [GradientAlpha](ohos-atomicservice-atomicservicenavigation.md#gradientalpha18) | 否 | 是 | 设置渐变色显示区域的透明度。默认值为OPACITY\_20。 |

## NavDestinationBuilder

PhonePC/2in1TabletTVWearable

type NavDestinationBuilder = (name: string, param?: Object) => void

NavDestination组件内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | [NavDestination](ts-basic-components-navdestination.md)页面名称。 |
| param | Object | 否 | [NavDestination](ts-basic-components-navdestination.md)页面详细参数。默认值为空。 |

## MixMode18+

PhonePC/2in1TabletTVWearable

背景色颜色混合模式的可选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AVERAGE | 1 | 两种颜色各占一半。 |
| CROSS | 2 | 一种颜色从另一种颜色中穿过。 |
| TOWARDS | 3 | 一种颜色渐变为另一种颜色。 |

## TitleBarType18+

PhonePC/2in1TabletTVWearable

标题栏类型的可选项，默认值为ROUND\_ICON。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SQUARED\_ICON | 1 | 方形图标样式。 |
| ROUND\_ICON | 2 | 圆形图标样式。 |
| DRAWER | 3 | 抽屉样式。 |

## GradientAlpha18+

PhonePC/2in1TabletTVWearable

导航栏背景底色的可选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OPACITY\_20 | 1 | 不透明度为0.2。 |
| OPACITY\_60 | 2 | 不透明度为0.6。 |
| OPACITY\_80 | 3 | 不透明度为0.8。 |
| OPACITY\_100 | 4 | 不透明度为1.0。 |

## BackgroundTheme18+

PhonePC/2in1TabletTVWearable

导航栏背景色底色的可选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DARK | 1 | 背景底色为黑色。 |
| LIGHT | 2 | 背景底色为白色。 |
| DEFAULT | 3 | 背景底色为灰白色。颜色值#F1F3F5 。 |

## SideBarOptions18+

PhonePC/2in1TabletTVWearable

侧边栏的功能选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sideBarBackground | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置侧边栏的背景颜色。默认值为$r('sys.color.ohos\_id\_color\_sub\_background')。 |
| onChange | Callback<boolean> | 否 | 是 | 侧边栏显示隐藏回调。true表示显示，false表示隐藏。默认值为空，即无事件。 |
| sideBarIcon | [Resource](ts-types.md#resource) | [SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 侧边栏里的返回图标。默认值为$r('sys.symbol.open\_sidebar')。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（AtomicServiceNavigation页面布局与渐变色背景）

AtomicServiceNavigation的基础样式，并展示渐变色背景。

```
1. import { AtomicServiceNavigation, MixMode, GradientAlpha, BackgroundTheme } from '@kit.ArkUI';
2. import { AtomicServiceTabs, TabBarOptions, TabBarPosition } from '@kit.ArkUI';
3. @Entry
4. @Component
5. struct Index {
6. @State message: string = '主题';
7. childNavStack: NavPathStack = new NavPathStack();
8. @Builder
9. tabContent1() {
10. Text('first page')
11. .onClick(() => {
12. this.childNavStack.pushPath({ name: 'page one' })
13. })
14. }

16. @Builder
17. tabContent2() {
18. Text('second page')
19. }

21. @Builder
22. tabContent3() {
23. Text('third page')
24. }

26. @Builder
27. navigationContent() {
28. AtomicServiceTabs({
29. tabContents: [
30. () => {
31. this.tabContent1()
32. },
33. () => {
34. this.tabContent2()
35. },
36. () => {
37. this.tabContent3()
38. }
39. ],
40. tabBarOptionsArray: [
41. new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '功能1'),
42. new TabBarOptions($r('sys.media.ohos_ic_public_location'), '功能2', Color.Green, Color.Red),
43. new TabBarOptions($r('sys.media.ohos_ic_public_more'), '功能3')
44. ],
45. tabBarPosition: TabBarPosition.BOTTOM,
46. barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
47. onTabBarClick: (index: Number) => {
48. if (index == 0) {
49. this.message = '功能1';
50. } else if (index == 1) {
51. this.message = '功能2';
52. } else {
53. this.message = '功能3';
54. }
55. }
56. })
57. }

59. @Builder
60. pageMap(name: string) {
61. if (name === 'page one') {
62. PageOne()
63. } else if (name === 'page two') {
64. PageTwo()
65. }
66. }

68. build() {
69. Row() {
70. Column() {
71. AtomicServiceNavigation({
72. navigationContent: () => {
73. this.navigationContent()
74. },
75. title: this.message,
76. titleOptions: {
77. isBlurEnabled: false
78. },
79. gradientBackground: {
80. primaryColor: '#FF0000',
81. secondaryColor: '#00FF00',
82. backgroundTheme: BackgroundTheme.LIGHT,
83. mixMode: MixMode.AVERAGE,
84. alpha: GradientAlpha.OPACITY_100
85. },
86. navDestinationBuilder: this.pageMap,
87. navPathStack: this.childNavStack,
88. mode: NavigationMode.Stack
89. })
90. }
91. .width('100%')
92. }
93. .height('100%')
94. }
95. }

97. @Component
98. export struct PageOne {
99. pageInfo: NavPathStack = new NavPathStack();

101. build() {
102. NavDestination() {
103. Button('Next')
104. .onClick(() => {
105. this.pageInfo.pushPath({ name: 'page two'})
106. })
107. }
108. .title('PageOne')
109. .onReady((context: NavDestinationContext) => {
110. this.pageInfo = context.pathStack;
111. })
112. }
113. }

115. @Component
116. export struct PageTwo {
117. pageInfo: NavPathStack = new NavPathStack();

119. build() {
120. NavDestination() {
121. Button('End')
122. }
123. .title('PageTwo')
124. .onReady((context: NavDestinationContext) => {
125. this.pageInfo = context.pathStack;
126. })
127. }
128. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/JKq1iXAwSUi-IBMkGVo9XA/zh-cn_image_0000002558606944.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055249Z&HW-CC-Expire=86400&HW-CC-Sign=7B60F14D0E63B04F6613A3B51324B6FAF6EB0AC3C5F22607B090A19B8B187797)

### 示例2（抽屉模式，宽屏场景下插入自定义布局）

设备宽屏场景（宽度大于600vp）下设置抽屉模式，用户在标题栏插入自定义布局。

```
1. import { AtomicServiceNavigation, TitleBarType } from '@kit.ArkUI';
2. import { AtomicServiceTabs, TabBarOptions, TabBarPosition } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';
8. childNavStack: NavPathStack = new NavPathStack();

10. @Builder
11. tabContent1() {
12. Text('first page')
13. .onClick(() => {
14. this.childNavStack.pushPath({ name: 'page one' })
15. })
16. }

18. @Builder
19. tabContent2() {
20. Text('second page')
21. }

23. @Builder
24. tabContent3() {
25. Text('third page')
26. }

28. @Builder
29. navigationContent() {
30. AtomicServiceTabs({
31. tabContents: [
32. () => {
33. this.tabContent1()
34. },
35. () => {
36. this.tabContent2()
37. },
38. () => {
39. this.tabContent3()
40. }
41. ],
42. tabBarOptionsArray: [
43. new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '功能1'),
44. new TabBarOptions($r('sys.media.ohos_ic_public_location'), '功能2', Color.Green, Color.Red),
45. new TabBarOptions($r('sys.media.ohos_ic_public_more'), '功能3')
46. ],
47. tabBarPosition: TabBarPosition.BOTTOM,
48. barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
49. onTabBarClick: (index: Number) => {
50. if (index == 0) {
51. this.message = '功能1';
52. } else if (index == 1) {
53. this.message = '功能2';
54. } else {
55. this.message = '功能3';
56. }
57. }
58. })
59. }

61. @Builder
62. pageMap(name: string) {
63. if (name === 'page one') {
64. PageOne()
65. } else if (name === 'page two') {
66. PageTwo()
67. }
68. }

70. @State showText: string = 'time: ';
71. @State time: number = 0;

73. @Builder
74. insertComp() {
75. Text('This is menus area')
76. .fontColor(Color.Red)
77. .width(200)
78. .height('100%')
79. }

81. build() {
82. Column() {
83. AtomicServiceNavigation({
84. navigationContent: () => {
85. this.navigationContent()
86. },
87. navDestinationBuilder: this.pageMap,
88. navPathStack: this.childNavStack,
89. title: this.message,
90. titleOptions: {
91. titleIcon: $r('app.media.startIcon'),
92. backgroundColor: 'rgb(61, 157, 180)',
93. titleBarType: TitleBarType.DRAWER
94. },
95. menus: () => { this.insertComp() },
96. mode: NavigationMode.Stack
97. })
98. }
99. .width('100%')
100. }
101. }

103. @Component
104. export struct PageOne {
105. pageInfo: NavPathStack = new NavPathStack();

107. build() {
108. NavDestination() {
109. Button('Next')
110. .onClick(() => {
111. this.pageInfo.pushPath({ name: 'page two'})
112. })
113. }
114. .title('PageOne')
115. .onReady((context: NavDestinationContext) => {
116. this.pageInfo = context.pathStack;
117. })
118. }
119. }

121. @Component
122. export struct PageTwo {
123. pageInfo: NavPathStack = new NavPathStack();

125. build() {
126. NavDestination() {
127. Button('End')
128. }
129. .title('PageTwo')
130. .onReady((context: NavDestinationContext) => {
131. this.pageInfo = context.pathStack;
132. })
133. }
134. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/n2nguYySRyS002SeoDhxdA/zh-cn_image_0000002589326471.png?HW-CC-KV=V1&HW-CC-Date=20260429T055249Z&HW-CC-Expire=86400&HW-CC-Sign=8235AB5A3FD540F3088FF10DEB2B5411EEA82E0C8420C2FA54369820E0C1BF63)

### 示例3（边栏使用场景）

设置边栏：背景色与内容样式。

```
1. import { AtomicServiceNavigation, TitleBarType } from '@kit.ArkUI';
2. import { AtomicServiceTabs, TabBarOptions, TabBarPosition } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';
8. childNavStack: NavPathStack = new NavPathStack();

10. @Builder
11. tabContent1() {
12. Text('first page')
13. .onClick(() => {
14. this.childNavStack.pushPath({ name: 'page one' })
15. })
16. }

18. @Builder
19. tabContent2() {
20. Text('second page')
21. }

23. @Builder
24. tabContent3() {
25. Text('third page')
26. }

28. @Builder
29. navigationContent() {
30. AtomicServiceTabs({
31. tabContents: [
32. () => {
33. this.tabContent1()
34. },
35. () => {
36. this.tabContent2()
37. },
38. () => {
39. this.tabContent3()
40. }
41. ],
42. tabBarOptionsArray: [
43. new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '功能1'),
44. new TabBarOptions($r('sys.media.ohos_ic_public_location'), '功能2', Color.Green, Color.Red),
45. new TabBarOptions($r('sys.media.ohos_ic_public_more'), '功能3')
46. ],
47. tabBarPosition: TabBarPosition.BOTTOM,
48. barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
49. onTabBarClick: (index: Number) => {
50. if (index == 0) {
51. this.message = '功能1';
52. } else if (index == 1) {
53. this.message = '功能2';
54. } else {
55. this.message = '功能3';
56. }
57. }
58. })
59. }

61. @Builder
62. pageMap(name: string) {
63. if (name === 'page one') {
64. PageOne()
65. } else if (name === 'page two') {
66. PageTwo()
67. }
68. }

70. @State showText: string = 'time: ';
71. @State time: number = 0;

73. @Builder
74. insertComp() {
75. Text('This is menus area')
76. .fontColor(Color.Red)
77. .width(200)
78. .height('100%')
79. }

81. @Builder
82. sideBarContentBuilder() {
83. Text('This is sideBar content area')
84. .fontSize(20)
85. }

87. build() {
88. Column() {
89. AtomicServiceNavigation({
90. navigationContent: () => {
91. this.navigationContent()
92. },
93. navDestinationBuilder: this.pageMap,
94. navPathStack: this.childNavStack,
95. title: this.message,
96. titleOptions: {
97. titleIcon: $r('app.media.startIcon'),
98. backgroundColor: 'rgb(61, 157, 180)',
99. titleBarType: TitleBarType.DRAWER
100. },
101. sideBarOptions: {
102. sideBarBackground: '#409EFF'
103. },
104. sideBarContent: () => { this.sideBarContentBuilder() },
105. mode: NavigationMode.Stack
106. })
107. }
108. .width('100%')
109. }
110. }

112. @Component
113. export struct PageOne {
114. pageInfo: NavPathStack = new NavPathStack();

116. build() {
117. NavDestination() {
118. Button('Next')
119. .onClick(() => {
120. this.pageInfo.pushPath({ name: 'page two'})
121. })
122. }
123. .title('PageOne')
124. .onReady((context: NavDestinationContext) => {
125. this.pageInfo = context.pathStack;
126. })
127. }
128. }

130. @Component
131. export struct PageTwo {
132. pageInfo: NavPathStack = new NavPathStack();

134. build() {
135. NavDestination() {
136. Button('End')
137. }
138. .title('PageTwo')
139. .onReady((context: NavDestinationContext) => {
140. this.pageInfo = context.pathStack;
141. })
142. }
143. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ffEbuGqmSouh0RcxBylGLw/zh-cn_image_0000002589246413.png?HW-CC-KV=V1&HW-CC-Date=20260429T055249Z&HW-CC-Expire=86400&HW-CC-Sign=86DBED0ADCE18B8DE8A5BEB20B6FC809AD8E8704B04DC1F1DB2F2FF80825DBDF)
