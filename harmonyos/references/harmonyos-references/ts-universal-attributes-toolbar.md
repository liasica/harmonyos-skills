---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-toolbar
title: 工具栏设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 其他 > 工具栏设置
category: harmonyos-references
scraped_at: 2026-04-28T08:01:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4b2034d7ceedc2e999853ad7556f826fa5e4da43c208a9ab15c0379eacd71fe2
---

设置组件对应的工具栏。

说明

* 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该toolbar为组件通用属性，请注意与[Navigation](ts-basic-components-navigation.md)组件自身的toolbar属性进行区分。

## toolbar

PhonePC/2in1TabletTVWearable

toolbar(value: CustomBuilder): T

为绑定该属性的组件，在窗口顶部标题栏相应分栏创建与该组件绑定的由[ToolBarItem](ts-basic-components-toolbaritem.md)构成的工具栏，分栏位置依据绑定该属性的组件所在分栏位置确定。[CustomBuilder](ts-types.md#custombuilder8)必须由[ToolBarItem](ts-basic-components-toolbaritem.md)构成，该工具栏才能生效。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 为当前组件配置CustomBuilder类型的自定义工具栏。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

1. toolbar仅支持固定标题栏，不支持悬浮标题栏（仅限三键模式）。
2. toolbar支持自定义组件布局，可将其置于特定分栏位置（左侧或右侧）。但需注意，当元素数量超过可用空间时，将导致布局截断或焦点框遮挡等现象，从而使部分操作项不可见或引发交互冲突。此时，元素不会自动缩略，建议合理控制元素数量。
3. toolbar当前仅支持单行布局，不支持多行布局，因此应避免在一个toolbar中放置多行布局的元素。
4. toolbar仅支持在[NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明)为Split的场景中使用。当[NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明)设置为Stack或Auto时，无法应用toolbar。
5. 标题栏高度会根据toolbar内的[ToolBarItem](ts-basic-components-toolbaritem.md)组件在有限范围内浮动：

   * [ToolBarItem](ts-basic-components-toolbaritem.md)组件与标题栏默认存在4VP的margin（外边距）。
   * 当[ToolBarItem](ts-basic-components-toolbaritem.md)组件的最大高度小于等于48VP时，标题栏高度会调整为56VP，此设置适用于标题栏、工具栏、搜索栏等通用组件。
   * 当[ToolBarItem](ts-basic-components-toolbaritem.md)组件的最大高度介于48VP到56VP之间时，标题栏高度会调整为64VP，此设置适用于图标与文字同时呈现的工具栏。
   * 当[ToolBarItem](ts-basic-components-toolbaritem.md)组件的最大高度超过56VP时，标题栏高度会调整为72VP。如果[ToolBarItem](ts-basic-components-toolbaritem.md)组件的最大高度超过64VP，则标题栏的高度保持为72VP，超出的区域会发生裁剪。

## 示例

PhonePC/2in1TabletTVWearable

该示例通过为[Navigation](ts-basic-components-navigation.md)下的[Button](ts-basic-components-button.md)组件绑定toolbar通用属性，为标题栏Navbar分栏开头位置添加包含两个[Button](ts-basic-components-button.md)组件工具栏项。为[NavDestination](ts-basic-components-navdestination.md)下的[Text](ts-basic-components-text.md)组件绑定toolbar通用属性，为标题栏NavDestination分栏末尾位置添加包含一个滑动条组件和一个搜索栏组件工具栏项。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SideBarContainerExample {
5. normalIcon: Resource = $r("app.media.startIcon")
6. selectedIcon: Resource = $r("app.media.startIcon")
7. @State arr: number[] = [1, 2, 3]
8. @State current: number = 1
9. @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack()

11. @Builder
12. MyToolBar() {
13. ToolBarItem({ placement: ToolBarItemPlacement.TOP_BAR_LEADING }) {
14. Button("left").height("30vp")
15. }

17. ToolBarItem({ placement: ToolBarItemPlacement.TOP_BAR_LEADING }) {
18. Button("right").height("30vp")
19. }
20. }

22. @Builder
23. MyToolbarNavDest() {
24. ToolBarItem({ placement: ToolBarItemPlacement.TOP_BAR_TRAILING }) {
25. Slider().width("120vp")
26. }

28. ToolBarItem({ placement: ToolBarItemPlacement.TOP_BAR_TRAILING }) {
29. Search().width("120vp")
30. }
31. }

33. @Builder
34. PageNavDest(name: string) {
35. NavDestination() {
36. Column() {
37. Text("add toolbar")
38. .fontSize(30)
39. .toolbar(this.MyToolbarNavDest())
40. }
41. .backgroundColor(Color.Grey)
42. }
43. }

45. build() {
46. SideBarContainer(SideBarContainerType.Embed) {
47. Column() {
48. ForEach(this.arr, (item: number) => {
49. Column({ space: 5 }) {
50. Image(this.current === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
51. Text("Index0" + item)
52. .fontSize(25)
53. .fontColor(this.current === item ? '#0A59F7' : '#999')
54. .fontFamily('source-sans-pro,cursive,sans-serif')
55. }
56. .onClick(() => {
57. this.current = item
58. })
59. }, (item: number) => item.toString())
60. }.width('100%')
61. .justifyContent(FlexAlign.SpaceEvenly)
62. .backgroundColor('#19000000')

64. Navigation(this.navPathStack) {
65. Column() {
66. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
67. .width('20%')
68. .height(40)
69. .margin(20)
70. .toolbar(this.MyToolBar)
71. Button('showNavDest', { stateEffect: true, type: ButtonType.Capsule })
72. .width('20%')
73. .height(40)
74. .margin(20)
75. .onClick(() => {
76. this.navPathStack.pushPath({ name: "1" })
77. })
78. }
79. .width('100%')
80. .height('100%')
81. }
82. .navBarPosition(NavBarPosition.Start)
83. .navBarWidth("50%")
84. .navBarWidthRange(["25%", "70%"])
85. .hideBackButton(true)
86. .navDestination(this.PageNavDest)
87. .height('100%')
88. .title('Navigation')
89. }
90. .sideBarWidth(150)
91. .minSideBarWidth(50)
92. .maxSideBarWidth(300)
93. .minContentWidth(0)
94. .onChange((value: boolean) => {
95. console.info('status:' + value)
96. })
97. .divider({
98. strokeWidth: '1vp',
99. color: Color.Gray,
100. startMargin: '4vp',
101. endMargin: '4vp'
102. })
103. }
104. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/eFPPIeq6R8Wjwg3UiJ7WGA/zh-cn_image_0000002552799930.png?HW-CC-KV=V1&HW-CC-Date=20260428T000118Z&HW-CC-Expire=86400&HW-CC-Sign=F611A61CBCBC2778ADA11190EA62FE23D610EEDA11F07FDB8B22220DE8AF06EF)
