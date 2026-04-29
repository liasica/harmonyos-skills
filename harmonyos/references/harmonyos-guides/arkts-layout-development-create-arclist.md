---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist
title: 弧形列表 (ArcList)（圆形屏幕推荐使用）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > 弧形列表 (ArcList)（圆形屏幕推荐使用）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9f2a934c5b22961210c81d135f29fbbb53c76c51cf09b14e55a2d5a49166c8d
---

从API version 18开始支持弧形列表。弧形列表是一种专为圆形屏幕设备设计的特殊列表，它能够以结构化、可滚动的形式高效展示信息。具体用法可参考[ArcList](../harmonyos-references/ts-container-arclist.md)。

使用弧形列表可以通过在[ArcList](../harmonyos-references/ts-container-arclist.md)组件中按垂直方向线性排列子组件[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)，可以为弧形列表中的每一项提供独立视图。此外，可以使用[循环渲染](arkts-rendering-control-foreach.md)来迭代一组列表项，或结合任意数量的单个视图与[ForEach](arkts-rendering-control-foreach.md)结构，构建复杂的弧形列表。[ArcList](../harmonyos-references/ts-container-arclist.md)组件支持多种[渲染控制](arkts-rendering-control-overview.md)方式，包括条件渲染、循环渲染和懒加载，以生成子组件。

## 创建弧形列表

[ArcList](../harmonyos-references/ts-container-arclist.md)可通过调用以下接口来创建。

```
1. ArcList({
2. initialIndex: 2
3. }) {
4. ArcListItem() {
5. // ···
6. }
7. ArcListItem() {
8. // ···
9. }
10. // ···
11. }
```

[ArcListCreate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListCreate.ets#L31-L57)

说明

[ArcList](../harmonyos-references/ts-container-arclist.md)的子组件必须是[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)，[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)必须配合[ArcList](../harmonyos-references/ts-container-arclist.md)来使用。

## 在弧形列表中显示数据

弧形列表视图垂直展示项目集合，当列表项超出屏幕范围时，提供滚动功能，这使得它非常适合展示大型数据集合。在最简单的弧形列表形式中，[ArcList](../harmonyos-references/ts-container-arclist.md)静态创建其列表项[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)的内容。

```
1. import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. export struct ArcListShow {
6. build() {
7. NavDestination() {
8. Column({ space: 12 }) {
9. // ...
10. ArcList({ initialIndex: 2 }) {
11. ArcListItem() {
12. Row() {
13. Image($r('app.media.wlan')).width('99px').height('99px')
14. .borderRadius('50px').margin({ left: 7 })
15. Column() {
16. Text($r('app.string.ArcListStyles_waln')).fontSize('38px').fontColor('#FFFFFFFF')
17. Text($r('app.string.ArcListStyles_open')).fontSize('20px').fontColor('#FFFFFFFF')
18. }.width('190px')

20. Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
21. .borderRadius('50px')
22. }
23. }
24. .borderRadius('65px')
25. .width('414px')
26. .height('129px')
27. .backgroundColor('#26FFFFFF')

29. ArcListItem() {
30. Row() {
31. Image($r('app.media.blueTooth')).width('99px').height('99px')
32. .borderRadius('50px').margin({ left: 7 })
33. Column() {
34. Text($r('app.string.ArcListStyles_blue')).fontSize('38px').fontColor('#FFFFFFFF')
35. Text($r('app.string.ArcListStyles_open')).fontSize('20px').fontColor('#FFFFFFFF')
36. }.width('190px')

38. Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
39. .borderRadius('50px')
40. }
41. }
42. .borderRadius('65px')
43. .width('414px')
44. .height('129px')
45. .backgroundColor('#26FFFFFF')

47. ArcListItem() {
48. Row() {
49. Image($r('app.media.mobileData')).width('99px').height('99px')
50. .borderRadius('50px').margin({ left: 7 })
51. Column() {
52. Text($r('app.string.ArcListStyles_net')).fontSize('38px').fontColor('#FFFFFFFF')
53. }.width('190px')

55. Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
56. .borderRadius('50px')
57. }
58. }
59. .borderRadius('65px')
60. .width('414px')
61. .height('129px')
62. .backgroundColor('#26FFFFFF')

64. ArcListItem() {
65. Row() {
66. Image($r('app.media.ic_settings_more_connections')).width('99px').height('99px')
67. .borderRadius('50px').margin({ left: 7 })
68. Column() {
69. Text($r('app.string.ArcListStyles_connect')).fontSize('38px').fontColor('#FFFFFFFF')
70. }.width('190px')

72. Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
73. .borderRadius('50px')
74. }
75. }
76. .borderRadius('65px')
77. .width('414px')
78. .height('129px')
79. .backgroundColor('#26FFFFFF')

81. ArcListItem() {
82. Row() {
83. Image($r('app.media.displayAndBrightness')).width('99px').height('99px')
84. .borderRadius('50px').margin({ left: 7 })
85. Column() {
86. Text($r('app.string.ArcListStyles_light')).fontSize('38px').fontColor('#FFFFFFFF')
87. }.width('190px')

89. Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
90. .borderRadius('50px')
91. }
92. }
93. .borderRadius('65px')
94. .width('414px')
95. .height('129px')
96. .backgroundColor('#26FFFFFF')
97. }
98. .width('466px')
99. .height('466px')
100. .space(LengthMetrics.px(10))
101. .borderRadius('233px')
102. .backgroundColor(Color.Black)
103. }
104. // ...
105. }
106. .backgroundColor('#f1f2f3')
107. // 请将$r('app.string.ArcListShow_title')替换为实际资源文件，在本示例中该资源文件的value值为"在弧形列表中显示数据"
108. .title($r('app.string.ArcListShow_title'))
109. }
110. }
```

[ArcListShow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListShow.ets#L16-L131)

**图1** 显示弧形列表数据

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/pWtCgDIpTH2oDqgFFOVs3w/zh-cn_image_0000002589244063.png?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=3A54561AD249D92FC4A97497DA0C5E1C3E1841E6374A7189EB84C150C679B442)

## 迭代弧形列表内容

通常，应用会通过数据集合动态创建列表。采用[循环渲染](arkts-rendering-control-foreach.md)的方式，可以从数据源中迭代获取数据，在每次迭代过程中创建相应的组件，从而降低代码的复杂度。

ArkTS通过[ForEach](arkts-rendering-control-foreach.md)提供了组件的循环渲染能力。以简单的联系人列表为例，将联系人名称和头像数据以Contact类结构存储到contacts数组中，使用[ForEach](arkts-rendering-control-foreach.md)中嵌套的[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)来代替多个平铺的、内容相似的[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)，从而减少重复代码，使代码更加简洁高效。

```
1. import { ArcList, ArcListAttribute, ArcListItemAttribute, ArcListItem, LengthMetrics } from '@kit.ArkUI';
2. import { util } from '@kit.ArkTS';
3. import { common } from '@kit.AbilityKit';

5. class Contact {
6. key: string = util.generateRandomUUID(true);
7. name: ResourceStr;
8. icon: Resource;

10. constructor(name: ResourceStr, icon: Resource) {
11. this.name = name;
12. this.icon = icon;
13. }
14. }

16. @Entry
17. @Component
18. export struct ArcListContents {
19. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
20. @State private contacts: Array<object> = [
21. // 请将$r('app.string.xxx')替换为实际资源文件
22. new Contact($r('app.string.name_xiaohong'), $r('app.media.ic_contact')),
23. new Contact($r('app.string.name_xiaolan'), $r('app.media.ic_contact')),
24. new Contact($r('app.string.name_xiaowang'), $r('app.media.ic_contact')),
25. new Contact($r('app.string.name_xiaoli'), $r('app.media.ic_contact')),
26. new Contact($r('app.string.name_xiaoming'), $r('app.media.ic_contact'))
27. ];

29. build() {
30. NavDestination() {
31. Column({ space: 12 }) {
32. // ...
33. ArcList({ initialIndex: 2 }) {
34. ForEach(this.contacts, (item: Contact) => {
35. ArcListItem() {
36. Row() {
37. Image(item.icon)
38. .width(40)
39. .height(40)
40. .margin(10)
41. .backgroundColor('#FF9CC998')
42. .borderRadius(20)
43. Text(item.name).fontSize('38px').fontColor('#FFFFFFFF')
44. }
45. .width('100%')
46. .justifyContent(FlexAlign.Start)
47. }
48. .borderRadius('65px')
49. .width('410px')
50. .height('130px')
51. .backgroundColor('#26FFFFFF')
52. }, (item: Contact) => JSON.stringify(item))
53. }
54. .space(LengthMetrics.px(10))
55. .width('466px')
56. .height('466px')
57. .borderRadius('233px')
58. .backgroundColor(Color.Black)
59. }
60. // ...
61. }
62. .backgroundColor('#f1f2f3')
63. // 请将$r('app.string.ArcListContents_title')替换为实际资源文件，在本示例中该资源文件的value值为"迭代弧形列表内容"
64. .title($r('app.string.ArcListContents_title'))
65. }
66. }
```

[ArcListContents.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListContents.ets#L15-L87)

**图2** 迭代弧形列表内容

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/8boJV1TFQHSD11zzK79cIg/zh-cn_image_0000002558764270.png?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=FE848CC0052A76887E4344457C2F043A7FD31A3695049669B84EA18DDD8A67D7)

## 自定义弧形列表样式

### 自定义弧形列表标题

可以通过[header](../harmonyos-references/ts-container-arclist.md#arklistoptions)参数为弧形列表添加自定义标题。

1. 首先，需要构造自定义标题组件customHeader。

   ```
   1. @Builder
   2. function customHeader() {
   3. Column() {
   4. Text($r('app.string.ArcListCrown_set'))
   5. .fontColor('#FFFFFFFF')
   6. .fontSize('19fp')
   7. }
   8. }
   ```

   [ArcListStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListStyles.ets#L26-L35)
2. 由于[header](../harmonyos-references/ts-container-arclist.md#arklistoptions)参数的类型是[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)，所以需要对自定义标题组件进行封装。

   ```
   1. context: UIContext = this.getUIContext();
   2. arcListHeader: ComponentContent<Object> = new ComponentContent(this.context, wrapBuilder(customHeader));
   ```

   [ArcListStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListStyles.ets#L40-L43)
3. 最后，通过[header](../harmonyos-references/ts-container-arclist.md#arklistoptions)参数将arcListHeader设置到弧形列表中。

   ```
   1. ArcList({ header: this.arcListHeader }) {
   2. ArcListItem() {
   3. // ···
   4. }
   5. // ···

   7. ArcListItem() {
   8. // ···
   9. }
   10. // ···
   11. }
   ```

   [ArcListStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListStyles.ets#L51-L148)

**图3** 自定义弧形列表标题

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/8RcGELrNQUeuUJHBR0iyYQ/zh-cn_image_0000002558604614.png?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=BA127C588B458C85D533989D6E0E1A5EA40FEB0BB6F07ADF35F41C31A9C2F900)

### 设置弧形列表项间距

在初始化列表时，若需在列表项之间添加间距，可以通过[space](../harmonyos-references/ts-container-arclist.md#space)属性实现。例如，为在每个列表项的垂直方向上增加30px的间距。

```
1. ArcList({ initialIndex: 2 }) {
2. // ···
3. }
4. .space(LengthMetrics.px(30))
```

[ArcListStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListStyles.ets#L159-L251)

**图4** 设置弧形列表项间距

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/TUt9BuNvT1G9lYGHJmLb2A/zh-cn_image_0000002589324139.png?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=522FD159970A71539E14A82BD11E2822370DD64D80700E192F3EA32BF936097C)

### 列表项关闭自动缩放

在弧形列表中，列表项默认具有在接近上下两端时自动缩放的效果。然而，在某些情况下，可能不希望有这种缩放效果。此时，可以通过设置[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)的[autoScale](../harmonyos-references/ts-container-arclistitem.md#autoscale)属性为false来禁用该效果。例如，如图5所示，“网络”和“显示”两个列表项，在关闭了自动缩放属性后，无论它们所处的位置如何，都不会出现缩放效果。

```
1. ArcListItem() {
2. // ...
3. }
4. .autoScale(false)
```

[ArcListStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListStyles.ets#L297-L313)

**图5** 列表项关闭自动缩放

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/aurjQE0xQfeOY6Axk15VXQ/zh-cn_image_0000002589244079.png?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=5ADFBFF7B97BDAA8BAC61C549D671ED5A86948539EBF1718CF53E11FC2BE007D)

### 添加内置滚动条

当列表项的高度超过屏幕高度时，弧形列表能够沿垂直方向滚动。若用户需要快速定位，可拖动滚动条以迅速滑动列表，如图6所示。

在使用[ArcList](../harmonyos-references/ts-container-arclist.md)组件时，可以通过[scrollBar](../harmonyos-references/ts-container-arclist.md#scrollbar)属性来控制弧形列表滚动条的显示。scrollBar的取值类型为[BarState](../harmonyos-references/ts-appendix-enums.md#barstate)，当设置为BarState.Auto时，表示滚动条将按需显示。在这种模式下，当用户触摸到滚动条区域时，滚动条会显示出来，支持上下拖拽以快速浏览内容，且在拖拽过程中滚动条会变粗。若用户不进行任何操作，滚动条将在2秒后自动消失。此外，还可以通过[scrollBarWidth](../harmonyos-references/ts-container-arclist.md#scrollbarwidth)属性来设置滚动条在按压状态下的宽度，以及通过[scrollBarColor](../harmonyos-references/ts-container-arclist.md#scrollbarcolor)属性来设置滚动条的颜色。

```
1. ArcList({ header: this.arcListHeader }) {
2. // ···
3. }
4. .scrollBar(BarState.Auto)
5. .scrollBarWidth(LengthMetrics.px(10))
6. .scrollBarColor(ColorMetrics.resourceColor(Color.White))
```

[arcListBuiltInScrollerBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/arcListBuiltInScrollerBar.ets#L47-L141)

**图6** 弧形列表的内置滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/7oadTvswS7q4ka0-Z6GDPQ/zh-cn_image_0000002558764272.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=2D8C21ACF17F1FD63B3EE8692C8C3D5890B0CD3534A64A08ACAFEF83B01A4FB0)

## 添加外置滚动条ArcScrollBar

弧形列表[ArcList](../harmonyos-references/ts-container-arclist.md)可与[ArcScrollBar](../harmonyos-references/ts-basic-components-arcscrollbar.md)组件配合使用，为弧形列表添加外置滚动条。两者通过绑定同一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)滚动控制器对象实现联动。

1. 首先，需要创建一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)类型的对象arcListScroller。

   ```
   1. private arcListScroller: Scroller = new Scroller();
   ```

   [ArcListAcrScrollBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListAcrScrollBar.ets#L39-L41)
2. 然后，弧形列表通过[scroller](../harmonyos-references/ts-container-arclist.md#arklistoptions)参数绑定滚动控制器。

   ```
   1. // 将arcListScroller用于初始化ArcList组件的scroller参数，完成arcListScroller与弧形列表的绑定。
   2. ArcList({ scroller: this.arcListScroller, header: this.arcListHeader }) {
   3. // ···
   4. }
   ```

   [ArcListAcrScrollBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListAcrScrollBar.ets#L52-L145)
3. 最后，弧形滚动条通过[scroller](../harmonyos-references/ts-basic-components-arcscrollbar.md#arcscrollbaroptions)参数绑定滚动控制器。

   ```
   1. // 将arcListScroller用于初始化ArcScrollBar组件的scroller参数，完成arcListScroller与滚动条的绑定。
   2. ArcScrollBar({ scroller: this.arcListScroller })
   ```

   [ArcListAcrScrollBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListAcrScrollBar.ets#L152-L155)

**图7** 弧形列表的外置滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/WGzQHVl7S0iQQMhZG1hxjg/zh-cn_image_0000002558604616.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=23D3B25CF9F75CE746D69F3A5B5B687AD11ED421C5B6C018A77EE850EC953463)

说明

弧形滚动条组件[ArcScrollBar](../harmonyos-references/ts-basic-components-arcscrollbar.md)，还可配合其他可滚动组件使用，如[List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)。

## 与弧形索引条ArcAlphabetIndexer联动

许多应用需要监测列表的滚动位置变动并作出响应，或通过调整滚动位置实现列表的快速定位。例如，在联系人列表滚动时，当列表滚动至不同首字母开头的联系人，外部索引条应更新至相应的字母位置。当用户选择外部索引条上的索引项时，列表应跳转至对应位置。为此，需使用弧形索引条组件[ArcAlphabetIndexer](../harmonyos-references/ts-container-arc-alphabet-indexer.md)。

如图8所示，当列表从联系人A滚动到联系人B时，外侧索引条也需要同步从选中A状态变成选中B状态，此场景可以通过监听[ArcList](../harmonyos-references/ts-container-arclist.md)组件的[onScrollIndex](../harmonyos-references/ts-container-arclist.md#onscrollindex)事件来实现；当点击索引项C时，列表也需要跳转到联系人C，此场景可以通过监听[ArcAlphabetIndexer](../harmonyos-references/ts-container-arc-alphabet-indexer.md)的[onSelect](../harmonyos-references/ts-container-arc-alphabet-indexer.md#onselect)事件来实现。

在列表滚动时，根据列表此时所在的索引值位置firstIndex，重新计算字母索引条对应字母的位置selectedIndex。由于[ArcAlphabetIndexer](../harmonyos-references/ts-container-arc-alphabet-indexer.md)组件通过[selected](../harmonyos-references/ts-container-arc-alphabet-indexer.md#selected)属性设置了选中项索引值，当selectedIndex变化时会触发[ArcAlphabetIndexer](../harmonyos-references/ts-container-arc-alphabet-indexer.md)组件重新渲染，从而显示为选中对应字母的状态。

在选中索引项时，根据此时选中项的索引值index，重新计算列表联系人对应的位置，然后通过列表绑定的滚动控制器arcListScroller的[scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)方法控制列表跳转到对应的联系人位置。弧形列表[ArcList](../harmonyos-references/ts-container-arclist.md)可通过[scroller](../harmonyos-references/ts-container-arclist.md#arklistoptions)参数绑定[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)（滚动控制器）。

```
1. import { ArcList, ArcListAttribute, ArcListItemAttribute, ArcListItem, LengthMetrics } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. // ...
5. const alphabets: string[] = [
6. '#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
7. 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
8. ];

10. @Entry
11. @Component
12. export struct ArcListArcIndexerBar {

14. // ...
15. // 索引条选中项索引
16. @State indexerIndex: number = 0;
17. // 列表绑定的滚动控制器
18. private arcListScroller: Scroller = new Scroller();

20. // ...

22. build() {
23. // ...
24. Stack({alignContent: Alignment.End}) {
25. ArcList({ initialIndex: 0, header:this.tabBar1, scroller:this.arcListScroller }) {
26. // ...
27. }
28. // ...
29. .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
30. // 根据列表滚动到的索引值，重新计算对应索引条的位置this.selectedIndex
31. this.indexerIndex = centerIndex + 1;
32. })
33. // ...
34. // 弧形索引条组件
35. ArcAlphabetIndexer({ arrayValue: alphabets, selected: this.indexerIndex})
36. .selected(this.indexerIndex!!)
37. .onSelect((index: number) => {
38. // 选中索引项后，列表跳转到相应位置
39. this.indexerIndex = index
40. this.arcListScroller.scrollToIndex(this.indexerIndex - 1)
41. })
42. // ...
43. }
44. // ...
45. }
46. }
```

[ArcListArcIndexerBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListArcIndexerBar.ets#L20-L186)

**图8** 弧形列表与弧形索引条联动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/f700f8acTQ-sUjxqNBjP2w/zh-cn_image_0000002589324141.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=DBFC71C6669A85212671FED93F360652A00379072DA115A44F6257FF90D45717)

## 响应列表项侧滑

[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)的[swipeAction](../harmonyos-references/ts-container-arclistitem.md#swipeaction)属性可用于实现列表项的左右滑动功能。[swipeAction](../harmonyos-references/ts-container-arclistitem.md#swipeaction)属性方法初始化时存在必填[SwipeActionOptions](../harmonyos-references/ts-container-listitem.md#swipeactionoptions9对象说明)参数start和end。其中，start表示设置列表项右滑时起始端滑出的组件，end表示设置列表项左滑时尾端滑出的组件。

在联系人列表中，end参数表示设置[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)左滑时尾端划出自定义组件，即删除按钮。在初始化end方法时，将滑动列表项的索引传入删除按钮组件，当用户点击删除按钮时，可以根据数据索引来删除列表项对应的数据，从而实现侧滑删除功能。

1. 首先，实现尾端滑出组件的构建。

   ```
   1. @Builder
   2. itemEnd(item: Contact) {
   3. // 构建尾端滑出组件
   4. Button({ type: ButtonType.Circle }) {
   5. Image($r('app.media.ic_public_delete_filled'))
   6. .width(20)
   7. .height(20)
   8. }
   9. .width(20)
   10. .height(20)
   11. .backgroundColor(Color.Black)
   12. .onClick(() => {
   13. this.getUIContext()?.animateTo({
   14. duration: 1000,
   15. curve: Curve.Smooth,
   16. iterations: 1,
   17. playMode: PlayMode.Normal,
   18. }, () => {
   19. // this.contacts为列表数据源，可根据实际场景构造，indexOf方法可获取将被删除数据在数据源中的索引
   20. let index = this.contacts.indexOf(item);
   21. // 从数据源删除指定数据项
   22. this.contacts.splice(index, 1);
   23. })
   24. })
   25. }
   ```

   [ArcListSideSlip.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListSideSlip.ets#L79-L105)
2. 然后，绑定[swipeAction](../harmonyos-references/ts-container-arclistitem.md#swipeaction)属性到可左滑的ArcListItem上。

   ```
   1. // 构建ArcList时，通过ForEach基于数据源this.contacts循环渲染ArcListItem
   2. ArcListItem() {
   3. // ···
   4. }
   5. .swipeAction({
   6. end: {
   7. // index为该ArcListItem在ArcList中的索引值。
   8. builder: () => {
   9. this.itemEnd(item);
   10. },
   11. }
   12. }) // 设置侧滑属性.
   ```

   [ArcListSideSlip.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListSideSlip.ets#L115-L143)

**图9** 侧滑删除列表项

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/blyhEpGgQBeDiniQLr2eKw/zh-cn_image_0000002589244081.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052740Z&HW-CC-Expire=86400&HW-CC-Sign=6DF409837F1A181265E010BF822DEC792A601BF6F4C68B69386E2ECCC6CBF452)

## 处理长列表

[循环渲染](arkts-rendering-control-foreach.md)适用于短列表，当构建具有大量列表项的长列表时，如果直接采用循环渲染方式，会一次性加载所有的列表元素，会导致页面启动时间过长，影响用户体验。因此，推荐使用[数据懒加载](arkts-rendering-control-lazyforeach.md)（LazyForEach）方式实现按需迭代加载数据，从而提升列表性能。关于长列表按需加载优化的具体实现可参考[数据懒加载](arkts-rendering-control-lazyforeach.md)章节中的示例。

当使用懒加载方式渲染列表时，为了减少列表滑动时出现白块，[ArcList](../harmonyos-references/ts-container-arclist.md)组件提供了[cachedCount](../harmonyos-references/ts-container-arclist.md#cachedcount)属性，该属性用于设置列表项缓存数，只在懒加载[LazyForEach](arkts-rendering-control-lazyforeach.md)中生效。

```
1. ArcList() {
2. // ···
3. }.cachedCount(3)
```

[ArcLongList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcLongList.ets#L126-L139)

说明

* cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。
* 列表使用数据懒加载时，除了显示区域的列表项和前后缓存的列表项，其他列表项会被销毁。

## 响应旋转表冠

手表设备上弧形列表在获焦的情况下可对旋转表冠做出响应，用户可通过旋转表冠的操作滑动列表，浏览列表项数据。弧形列表可通过下列[焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)相关属性成为所在页面的默认焦点。

```
1. ArcList({
2. initialIndex: 2,
3. }) {
4. // ···
5. }
6. // 设置弧形列表支持获焦
7. .focusable(true)
8. // 设置弧形列表支持点击获焦
9. .focusOnTouch(true)
10. // 设置弧形列表为所在页面上的默认焦点
11. .defaultFocus(true)
```

[ArcListCrown.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListCrown.ets#L41-L127)

还可以通过[digitalCrownSensitivity](../harmonyos-references/ts-container-arclist.md#digitalcrownsensitivity)属性设置表冠响应事件的灵敏度，以应对不同量级的列表项数据。列表项数据较多时可以设置更高的响应事件灵敏度，数据较少时可以设置较低的响应事件灵敏度。

```
1. ArcList({
2. initialIndex: 2,
3. }) {
4. // ···
5. }
6. // ···
7. .digitalCrownSensitivity(CrownSensitivity.MEDIUM)
```

[ArcListCrown.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcList/ArcListCrown.ets#L42-L130)
