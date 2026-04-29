---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-relative-layout
title: 相对布局 (RelativeContainer)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 相对布局 (RelativeContainer)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:7bf89d759be54fa44639193a8e75282635bfc3672eb4b2d8a567f04d400f0eff
---

## 概述

在应用的开发过程中，经常需要设计复杂界面，此时涉及到多个相同或不同组件之间的嵌套。如果布局组件嵌套深度过深，或者嵌套组件数过多，会带来额外的开销。如果在布局的方式上进行优化，就可以有效的提升性能，减少时间开销。

RelativeContainer是一种采用相对布局的容器，支持容器内部的子元素设置相对位置关系，适用于处理界面复杂的场景，对多个子元素进行对齐和排列。子元素可以指定兄弟元素或父容器作为锚点，基于锚点进行相对位置布局。在使用锚点时，需注意子元素的相对位置关系，以避免出现错位或遮挡的情况。下图展示了一个 RelativeContainer的概念图，图中的虚线表示位置的依赖关系。

**图1** 相对布局示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ZhDhy2HIQyeErO51eMLsBQ/zh-cn_image_0000002558764222.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=BA6C5EBBC3B8E1C746896202FFA12A6AA759EAF06EF24AC6A7FE68958216378B)

子元素并不完全是上图中的依赖关系。比如，Item4可以以Item2为依赖锚点，也可以以RelativeContainer父容器为依赖锚点。

## 基本概念

* 参考边界：设置当前组件的哪个边界对齐到锚点。
* 锚点：通过锚点设置当前元素基于哪个元素确定位置。
* 对齐方式：通过对齐方式，设置当前元素是基于锚点的上中下对齐，还是基于锚点的左中右对齐。
* 链：将一系列组件以首尾相连的方式对齐，可以形成一条链。通过设置链的模式，可以指定链上元素的排列方式。
* 辅助线：辅助线是在容器内虚拟出的额外水平或垂直锚点，便于统一对齐至某个偏移位置。
* 屏障：屏障是指容器内一组指定组件在特定方向上的共同最远边界，例如，一组组件下方的屏障，是指这些组件底部边缘中最底部的那个边界。

## 设置依赖关系

### 设置参考边界

设置当前组件的哪个边界对齐到锚点。容器内子组件的参考边界区分水平方向和垂直方向。

* 在水平方向上，可以按照起始（left）、居中（middle）或尾端（right）的组件边界与锚点对齐。当设置三个边界时，仅起始（left）和居中（middle）的边界设置生效。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/2MZRZBIKSOi284wZUW68ag/zh-cn_image_0000002558604566.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=139E9F29D8795680125455619CD6D3B1FBD75A5C4A232F632C1386DDB7B87C92)
* 在垂直方向上，可以设置组件边界与锚点对齐，具体包括顶部（top）、居中（center）和底部（bottom）。当设置三个边界时，仅顶部（top）和居中（center）生效。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/j9bUZJ2yRiawTmuJM3FrjA/zh-cn_image_0000002589324091.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=D21FF6DCFB5B029C108F8889AC6480AB3B591335771610809915E5EBB81ED36E)

### 设置锚点

锚点设置涉及子元素相对于其父元素或兄弟元素的位置依赖关系。具体而言，子元素可以将其位置锚定到相对布局容器（RelativeContainer）、辅助线（guideline）、屏障（barrier）或其他子元素上。

为了准确定义锚点，RelativeContainer的子元素必须拥有唯一的组件标识（id），用于指定锚点信息。父元素RelativeContainer的标识默认为“\_\_container\_\_”，其他子元素的组件标识（id）则通过[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)属性设置。

说明

* 未设置组件标识（id）的组件虽可显示，但无法被其他组件引用为锚点。相对布局容器会为其拼接组件标识，但组件标识（id）的规律无法被应用感知。辅助线（guideline）与屏障（barrier）的组件标识（id）需确保唯一，避免与任何组件冲突。若有重复，遵循组件 > guideline > barrier 的优先级。
* 组件间设置锚点时应避免形成依赖循环（组件之间设置链除外），依赖循环将导致子组件缺乏定位基准，最终无法绘制。

* RelativeContainer父组件为锚点，\_\_container\_\_代表父容器的组件标识（id）。

  ```
  1. let alignRus: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {
  2. 'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
  3. 'left': { 'anchor': '__container__', 'align': HorizontalAlign.Start }
  4. }
  5. let alignRue: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {
  6. 'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
  7. 'right': { 'anchor': '__container__', 'align': HorizontalAlign.End }
  8. }
  9. let marginLeft: Record<string, number> = { 'left': 20 }
  10. let bwc: Record<string, number | string> = { 'width': 2, 'color': '#6699FF' }

  12. @Entry
  13. @Component
  14. struct ParentRefRelativeContainer {
  15. build() {
  16. RelativeContainer() {
  17. Row() {
  18. Text('row1')
  19. }
  20. .justifyContent(FlexAlign.Center)
  21. .width(100)
  22. .height(100)
  23. .backgroundColor('#a3cf62')
  24. .alignRules(alignRus)
  25. .id('row1')

  27. Row() {
  28. Text('row2')
  29. }
  30. .justifyContent(FlexAlign.Center)
  31. .width(100)
  32. .height(100)
  33. .backgroundColor('#00ae9d')
  34. .alignRules(alignRue)
  35. .id('row2')
  36. }.width(300).height(300)
  37. .margin(marginLeft)
  38. .border(bwc)
  39. }
  40. }
  ```

  [RelativeContainerParentComponentId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerParentComponentId.ets#L15-L56)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/OubAwYiRSSCpUOoXqF8ckA/zh-cn_image_0000002589244031.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=B7B6712BF81B505102DEEEA6ADF3EA48B711BED2AFADE49171E6EB02F41E06A3)
* 以兄弟元素为锚点。

  ```
  1. let alignRus001: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {
  2. 'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
  3. 'left': { 'anchor': '__container__', 'align': HorizontalAlign.Start }
  4. }
  5. let relConB: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {
  6. 'top': { 'anchor': 'row1', 'align': VerticalAlign.Bottom },
  7. 'left': { 'anchor': 'row1', 'align': HorizontalAlign.Start }
  8. }
  9. let marginLeft001: Record<string, number> = { 'left': 20 }
  10. let bwc001: Record<string, number | string> = { 'width': 2, 'color': '#6699FF' }

  12. @Entry
  13. @Component
  14. struct SiblingRefRelativeContainer {
  15. build() {
  16. RelativeContainer() {
  17. Row() {
  18. Text('row1')
  19. }
  20. .justifyContent(FlexAlign.Center)
  21. .width(100)
  22. .height(100)
  23. .backgroundColor('#00ae9d')
  24. .alignRules(alignRus001)
  25. .id('row1')

  27. Row() {
  28. Text('row2')
  29. }
  30. .justifyContent(FlexAlign.Center)
  31. .width(100)
  32. .height(100)
  33. .backgroundColor('#a3cf62')
  34. .alignRules(relConB)
  35. .id('row2')
  36. }.width(300).height(300)
  37. .margin(marginLeft001)
  38. .border(bwc001)
  39. }
  40. }
  ```

  [RelativeContainerSiblingComponentId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerSiblingComponentId.ets#L15-L56)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/YDLNfdq-TWKD6DSrBNnyQQ/zh-cn_image_0000002558764224.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=63FD09F85C8BB5B80EBFEA1112F9C283A83B70C574CC6CD804EB90AA76FDB0F9)
* 子组件锚点可以任意选择，但需注意不要相互依赖。

  ```
  1. @Entry
  2. @Component
  3. struct ChildRefRelativeContainer {
  4. build() {
  5. Row() {
  6. RelativeContainer() {
  7. Row() {
  8. Text('row1')
  9. }
  10. .justifyContent(FlexAlign.Center)
  11. .width(100)
  12. .height(100)
  13. .backgroundColor('#a3cf62')
  14. .alignRules({
  15. top: { anchor: '__container__', align: VerticalAlign.Top },
  16. left: { anchor: '__container__', align: HorizontalAlign.Start }
  17. })
  18. .id('row1')

  20. Row() {
  21. Text('row2')
  22. }
  23. .justifyContent(FlexAlign.Center)
  24. .width(100)
  25. .backgroundColor('#00ae9d')
  26. .alignRules({
  27. top: { anchor: '__container__', align: VerticalAlign.Top },
  28. right: { anchor: '__container__', align: HorizontalAlign.End },
  29. bottom: { anchor: 'row1', align: VerticalAlign.Center },
  30. })
  31. .id('row2')

  33. Row() {
  34. Text('row3')
  35. }
  36. .justifyContent(FlexAlign.Center)
  37. .height(100)
  38. .backgroundColor('#0a59f7')
  39. .alignRules({
  40. top: { anchor: 'row1', align: VerticalAlign.Bottom },
  41. left: { anchor: 'row1', align: HorizontalAlign.Start },
  42. right: { anchor: 'row2', align: HorizontalAlign.Start }
  43. })
  44. .id('row3')

  46. Row() {
  47. Text('row4')
  48. }.justifyContent(FlexAlign.Center)
  49. .backgroundColor('#2ca9e0')
  50. .alignRules({
  51. top: { anchor: 'row3', align: VerticalAlign.Bottom },
  52. left: { anchor: 'row1', align: HorizontalAlign.Center },
  53. right: { anchor: 'row2', align: HorizontalAlign.End },
  54. bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
  55. })
  56. .id('row4')
  57. }
  58. .width(300).height(300)
  59. .margin({ left: 50 })
  60. .border({ width: 2, color: '#6699FF' })
  61. }
  62. .height('100%')
  63. }
  64. }
  ```

  [RelativeContainerChildComponentId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerChildComponentId.ets#L15-L65)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/2tbQP7eWT0Wg2RYxQBTjAQ/zh-cn_image_0000002558604568.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=8B44CDB60CFF5276825E6DB50D0EBEE96685E0120027E21D00B0BDF65DA65384)

### 设置相对于锚点的对齐位置

设置了锚点之后，可以通过[alignRules](../harmonyos-references/ts-universal-attributes-location.md#alignrules9)属性的align设置相对于锚点的对齐位置。

在水平方向上，对齐位置可以设置为HorizontalAlign.Start、HorizontalAlign.Center、HorizontalAlign.End。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/CEKc_tU9QhuhJduwT8oG7w/zh-cn_image_0000002589324093.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=BB579C17DCB36C86CDAF73B161BE6B4716F9EFAC4A5B237C951C531E04957E9C)

在垂直方向上，对齐位置可以设置为VerticalAlign.Top、VerticalAlign.Center、VerticalAlign.Bottom。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/hHCZAIbOSiyltJQH6CYBqQ/zh-cn_image_0000002589244033.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=6100985B3ED93EA09BD1E895959D45EA31D5F8868C24412AD859246829D58E86)

### 子组件位置偏移

子组件经过相对位置对齐后，可能尚未达到目标位置。开发者可根据需要设置额外偏移（offset）。当使用offset调整位置的组件作为锚点时，对齐位置为设置offset之前的位置。从API Version 11开始，新增了[Bias](../harmonyos-references/ts-types.md#bias对象说明)对象，建议API Version 11及以后的版本使用bias来设置额外偏移。使用bias的示例可以参考[示例4（设置偏移）](../harmonyos-references/ts-container-relativecontainer.md#示例4设置偏移)。

```
1. @Entry
2. @Component
3. struct ChildComponentOffsetExample {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(100)
12. .height(100)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. top: { anchor: '__container__', align: VerticalAlign.Top },
16. left: { anchor: '__container__', align: HorizontalAlign.Start }
17. })
18. .id('row1')

20. Row() {
21. Text('row2')
22. }
23. .justifyContent(FlexAlign.Center)
24. .width(100)
25. .backgroundColor('#00ae9d')
26. .alignRules({
27. top: { anchor: '__container__', align: VerticalAlign.Top },
28. right: { anchor: '__container__', align: HorizontalAlign.End },
29. bottom: { anchor: 'row1', align: VerticalAlign.Center },
30. })
31. .offset({
32. x: -40,
33. y: -20
34. })
35. .id('row2')

37. Row() {
38. Text('row3')
39. }
40. .justifyContent(FlexAlign.Center)
41. .height(100)
42. .backgroundColor('#0a59f7')
43. .alignRules({
44. top: { anchor: 'row1', align: VerticalAlign.Bottom },
45. left: { anchor: 'row1', align: HorizontalAlign.End },
46. right: { anchor: 'row2', align: HorizontalAlign.Start }
47. })
48. .offset({
49. x: -10,
50. y: -20
51. })
52. .id('row3')

54. Row() {
55. Text('row4')
56. }
57. .justifyContent(FlexAlign.Center)
58. .backgroundColor('#2ca9e0')
59. .alignRules({
60. top: { anchor: 'row3', align: VerticalAlign.Bottom },
61. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
62. left: { anchor: '__container__', align: HorizontalAlign.Start },
63. right: { anchor: 'row1', align: HorizontalAlign.End }
64. })
65. .offset({
66. x: -10,
67. y: -30
68. })
69. .id('row4')

71. Row() {
72. Text('row5')
73. }
74. .justifyContent(FlexAlign.Center)
75. .backgroundColor('#30c9f7')
76. .alignRules({
77. top: { anchor: 'row3', align: VerticalAlign.Bottom },
78. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
79. left: { anchor: 'row2', align: HorizontalAlign.Start },
80. right: { anchor: 'row2', align: HorizontalAlign.End }
81. })
82. .offset({
83. x: 10,
84. y: 20
85. })
86. .id('row5')

88. Row() {
89. Text('row6')
90. }
91. .justifyContent(FlexAlign.Center)
92. .backgroundColor('#ff33ffb5')
93. .alignRules({
94. top: { anchor: 'row3', align: VerticalAlign.Bottom },
95. bottom: { anchor: 'row4', align: VerticalAlign.Bottom },
96. left: { anchor: 'row3', align: HorizontalAlign.Start },
97. right: { anchor: 'row3', align: HorizontalAlign.End }
98. })
99. .offset({
100. x: -15,
101. y: 10
102. })
103. .backgroundImagePosition(Alignment.Bottom)
104. .backgroundImageSize(ImageSize.Cover)
105. .id('row6')
106. }
107. .width(300).height(300)
108. .margin({ left: 50 })
109. .border({ width: 2, color: '#6699FF' })
110. }
111. .height('100%')
112. }
113. }
```

[RelativeContainerChildComponentOffset.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerChildComponentOffset.ets#L15-L129)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/1HU2mHzkS52ZieEVu4kWrw/zh-cn_image_0000002558764226.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=16F5A169AC55B6303931FA711BDDEEE445A037E0B3494F8E64CDB0AF5D27F4E3)

## 多种组件的对齐布局

[Row](../harmonyos-references/ts-container-row.md)、[Column](../harmonyos-references/ts-container-column.md)、[Flex](../harmonyos-references/ts-container-flex.md)、[Stack](../harmonyos-references/ts-container-stack.md)等多种布局组件，可按照RelativeContainer组件规则进行对齐排布。

```
1. @Entry
2. @Component
3. struct RelativeContainerExample {
4. build() {
5. Row() {

7. RelativeContainer() {
8. Row()
9. .width(100)
10. .height(100)
11. .backgroundColor('#a3cf62')
12. .alignRules({
13. top: { anchor: '__container__', align: VerticalAlign.Top },
14. left: { anchor: '__container__', align: HorizontalAlign.Start }
15. })
16. .id('row1')

18. Column()
19. .width('50%')
20. .height(30)
21. .backgroundColor('#00ae9d')
22. .alignRules({
23. top: { anchor: '__container__', align: VerticalAlign.Top },
24. left: { anchor: '__container__', align: HorizontalAlign.Center }
25. })
26. .id('row2')

28. Flex({ direction: FlexDirection.Row }) {
29. Text('1').width('20%').height(50).backgroundColor('#0a59f7')
30. Text('2').width('20%').height(50).backgroundColor('#2ca9e0')
31. Text('3').width('20%').height(50).backgroundColor('#0a59f7')
32. Text('4').width('20%').height(50).backgroundColor('#2ca9e0')
33. }
34. .padding(10)
35. .backgroundColor('#30c9f7')
36. .alignRules({
37. top: { anchor: 'row2', align: VerticalAlign.Bottom },
38. left: { anchor: '__container__', align: HorizontalAlign.Start },
39. bottom: { anchor: '__container__', align: VerticalAlign.Center },
40. right: { anchor: 'row2', align: HorizontalAlign.Center }
41. })
42. .id('row3')

44. Stack({ alignContent: Alignment.Bottom }) {
45. Text('First child, show in bottom')
46. .width('90%')
47. .height('100%')
48. .backgroundColor('#a3cf62')
49. .align(Alignment.Top)
50. Text('Second child, show in top').width('70%').height('60%').backgroundColor('#00ae9d').align(Alignment.Top)
51. }
52. .margin({ top: 5 })
53. .alignRules({
54. top: { anchor: 'row3', align: VerticalAlign.Bottom },
55. left: { anchor: '__container__', align: HorizontalAlign.Start },
56. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
57. right: { anchor: 'row3', align: HorizontalAlign.End }
58. })
59. .id('row4')

61. }
62. .width(300).height(300)
63. .margin({ left: 50 })
64. .border({ width: 2, color: '#6699FF' })
65. }
66. .height('100%')
67. }
68. }
```

[RelativeContainerDifferentComponentId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerDifferentComponentId.ets#L15-L82)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/rPW0Vrx3QNChL-wlAQTHpw/zh-cn_image_0000002558604570.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=BC706AC07A12CF859D11F3BEA4139922EE9FF8E630EE3ED9797AFD13E4691E91)

## 组件尺寸

当同时存在前端页面设置的子组件尺寸和相对布局规则时，子组件的绘制尺寸依据约束规则确定。从API Version 11开始，此规则有所变化，子组件自身设置的尺寸优先级高于相对布局规则中的对齐锚点尺寸。因此，若要使子组件与锚点严格对齐，应仅使用alignRules，避免使用[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)。

说明

* 根据约束条件和子组件自身的size属性无法确定子组件的大小，此时，不绘制该子组件。
* 在同一方向上设置两个或更多锚点时，若这些锚点的位置顺序有误，该子组件将被视为大小为0而不予绘制。

```
1. @Entry
2. @Component
3. struct RelativeAlignRulesExample {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(100)
12. .height(100)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. top: { anchor: '__container__', align: VerticalAlign.Top },
16. left: { anchor: '__container__', align: HorizontalAlign.Start }
17. })
18. .id('row1')

20. Row() {
21. Text('row2')
22. }
23. .justifyContent(FlexAlign.Center)
24. .width(100)
25. .backgroundColor('#00ae9d')
26. .alignRules({
27. top: { anchor: '__container__', align: VerticalAlign.Top },
28. right: { anchor: '__container__', align: HorizontalAlign.End },
29. bottom: { anchor: 'row1', align: VerticalAlign.Center },
30. })
31. .id('row2')

33. Row() {
34. Text('row3')
35. }
36. .justifyContent(FlexAlign.Center)
37. .height(100)
38. .backgroundColor('#0a59f7')
39. .alignRules({
40. top: { anchor: 'row1', align: VerticalAlign.Bottom },
41. left: { anchor: 'row1', align: HorizontalAlign.End },
42. right: { anchor: 'row2', align: HorizontalAlign.Start }
43. })
44. .id('row3')

46. Row() {
47. Text('row4')
48. }.justifyContent(FlexAlign.Center)
49. .backgroundColor('#2ca9e0')
50. .alignRules({
51. top: { anchor: 'row3', align: VerticalAlign.Bottom },
52. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
53. left: { anchor: '__container__', align: HorizontalAlign.Start },
54. right: { anchor: 'row1', align: HorizontalAlign.End }
55. })
56. .id('row4')

58. Row() {
59. Text('row5')
60. }.justifyContent(FlexAlign.Center)
61. .backgroundColor('#30c9f7')
62. .alignRules({
63. top: { anchor: 'row3', align: VerticalAlign.Bottom },
64. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
65. left: { anchor: 'row2', align: HorizontalAlign.Start },
66. right: { anchor: 'row2', align: HorizontalAlign.End }
67. })
68. .id('row5')

70. Row() {
71. Text('row6')
72. }
73. .justifyContent(FlexAlign.Center)
74. .backgroundColor('#ff33ffb5')
75. .alignRules({
76. top: { anchor: 'row3', align: VerticalAlign.Bottom },
77. bottom: { anchor: 'row4', align: VerticalAlign.Bottom },
78. left: { anchor: 'row3', align: HorizontalAlign.Start },
79. right: { anchor: 'row3', align: HorizontalAlign.End }
80. })
81. .id('row6')
82. .backgroundImagePosition(Alignment.Bottom)
83. .backgroundImageSize(ImageSize.Cover)
84. }
85. .width(300).height(300)
86. .margin({ left: 50 })
87. .border({ width: 2, color: '#6699FF' })
88. }
89. .height('100%')
90. }
91. }
```

[RelativeContainerComponentSize.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerComponentSize.ets#L15-L107)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/k1NMWJqXTV6R--_0CwhveA/zh-cn_image_0000002589324095.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=4FA9C87C43A86F63737FF82F89FB494663DCE52E454363D3CCA7530D55FF5A76)

## 多个组件形成链

链的形成依赖于组件之间的关联关系。以组件A和组件B构成的最简水平链为例，其依赖关系为：锚点1 <-- 组件A <---> 组件B --> 锚点2，即A具有left锚点，B具有right锚点，同时A的right锚点与B的[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign).Start对齐，B的left锚点与A的[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign).End对齐。

* 链的方向和格式在链头组件的[chainMode](../harmonyos-references/ts-universal-attributes-location.md#chainmode12)接口中声明；链内元素的bias属性全部失效，链头元素的bias属性作为整个链的bias生效。链头是指在满足成链规则时链的第一个组件（在水平方向上，从左边开始，镜像语言中从右边开始；在垂直方向上，从上边开始）。
* 如果链内所有元素的size超出链的锚点约束，超出部分将被均匀分配到链的两侧。在[PACKED](../harmonyos-references/ts-universal-attributes-location.md#chainstyle12)链中，可以通过[Bias](../harmonyos-references/ts-types.md#bias对象说明)设置超出部分的分布。

在以下示例代码中，通过alignRules和chainMode将九个在容器内的Row组件分为三组水平链式排列。组件row1、组件row2和组件row3顶部对齐，水平方向成SPREAD链，链内组件在锚点间均匀分布。组件row4、组件row5、组件row6垂直方向基于容器居中，水平方向成SPREAD\_INSIDE链，链内除首尾2个组件对齐锚点外，其他组件在链中均匀分布。组件row7、组件row8、组件row9底部对齐，水平方向组成PACKED链，链内组件无间隙。

```
1. @Entry
2. @Component
3. struct RelativeChainModeExample {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row() {
8. Text('row1')
9. }
10. .justifyContent(FlexAlign.Center)
11. .width(80)
12. .height(80)
13. .backgroundColor('#a3cf62')
14. .alignRules({
15. left: { anchor: '__container__', align: HorizontalAlign.Start },
16. right: { anchor: 'row2', align: HorizontalAlign.Start },
17. top: { anchor: '__container__', align: VerticalAlign.Top }
18. })
19. .id('row1')
20. .chainMode(Axis.Horizontal, ChainStyle.SPREAD)

22. Row() {
23. Text('row2')
24. }
25. .justifyContent(FlexAlign.Center)
26. .width(80)
27. .height(80)
28. .backgroundColor('#00ae9d')
29. .alignRules({
30. left: { anchor: 'row1', align: HorizontalAlign.End },
31. right: { anchor: 'row3', align: HorizontalAlign.Start },
32. top: { anchor: 'row1', align: VerticalAlign.Top }
33. })
34. .id('row2')

36. Row() {
37. Text('row3')
38. }
39. .justifyContent(FlexAlign.Center)
40. .width(80)
41. .height(80)
42. .backgroundColor('#0a59f7')
43. .alignRules({
44. left: { anchor: 'row2', align: HorizontalAlign.End },
45. right: { anchor: '__container__', align: HorizontalAlign.End },
46. top: { anchor: 'row1', align: VerticalAlign.Top }
47. })
48. .id('row3')

50. Row() {
51. Text('row4')
52. }
53. .justifyContent(FlexAlign.Center)
54. .width(80)
55. .height(80)
56. .backgroundColor('#a3cf62')
57. .alignRules({
58. left: { anchor: '__container__', align: HorizontalAlign.Start },
59. right: { anchor: 'row5', align: HorizontalAlign.Start },
60. center: { anchor: '__container__', align: VerticalAlign.Center }
61. })
62. .id('row4')
63. .chainMode(Axis.Horizontal, ChainStyle.SPREAD_INSIDE)

65. Row() {
66. Text('row5')
67. }
68. .justifyContent(FlexAlign.Center)
69. .width(80)
70. .height(80)
71. .backgroundColor('#00ae9d')
72. .alignRules({
73. left: { anchor: 'row4', align: HorizontalAlign.End },
74. right: { anchor: 'row6', align: HorizontalAlign.Start },
75. top: { anchor: 'row4', align: VerticalAlign.Top }
76. })
77. .id('row5')

79. Row() {
80. Text('row6')
81. }
82. .justifyContent(FlexAlign.Center)
83. .width(80)
84. .height(80)
85. .backgroundColor('#0a59f7')
86. .alignRules({
87. left: { anchor: 'row5', align: HorizontalAlign.End },
88. right: { anchor: '__container__', align: HorizontalAlign.End },
89. top: { anchor: 'row4', align: VerticalAlign.Top }
90. })
91. .id('row6')

93. Row() {
94. Text('row7')
95. }
96. .justifyContent(FlexAlign.Center)
97. .width(80)
98. .height(80)
99. .backgroundColor('#a3cf62')
100. .alignRules({
101. left: { anchor: '__container__', align: HorizontalAlign.Start },
102. right: { anchor: 'row8', align: HorizontalAlign.Start },
103. bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
104. })
105. .id('row7')
106. .chainMode(Axis.Horizontal, ChainStyle.PACKED)

108. Row() {
109. Text('row8')
110. }
111. .justifyContent(FlexAlign.Center)
112. .width(80)
113. .height(80)
114. .backgroundColor('#00ae9d')
115. .alignRules({
116. left: { anchor: 'row7', align: HorizontalAlign.End },
117. right: { anchor: 'row9', align: HorizontalAlign.Start },
118. top: { anchor: 'row7', align: VerticalAlign.Top }
119. })
120. .id('row8')

122. Row() {
123. Text('row9')
124. }
125. .justifyContent(FlexAlign.Center)
126. .width(80)
127. .height(80)
128. .backgroundColor('#0a59f7')
129. .alignRules({
130. left: { anchor: 'row8', align: HorizontalAlign.End },
131. right: { anchor: '__container__', align: HorizontalAlign.End },
132. top: { anchor: 'row7', align: VerticalAlign.Top }
133. })
134. .id('row9')
135. }
136. .width(300).height(300)
137. .margin({ left: 50 })
138. .border({ width: 2, color: '#6699FF' })
139. }
140. .height('100%')
141. }
142. }
```

[RelativeContainerMultipleComponentsChainMode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerMultipleComponentsChainMode.ets#L15-L158)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/VoHTiWzjSH6xYrEPllVBmA/zh-cn_image_0000002589244035.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=138CAF65A910002DAFD4ACBBDAF655207A73F38043144DEA006209172D87B6F5)

## 使用辅助线辅助定位子组件

辅助线（guideLine）是在容器内虚拟出的额外水平或垂直锚点，便于统一对齐到特定偏移位置，从而避免为每个组件单独编写重复的偏移设置。

辅助线分为垂直（Vertical）和水平（Horizontal）两种：垂直辅助线通过start和end属性指定其距离容器左侧和右侧的距离；水平辅助线通过start和end属性指定其距离容器顶部和底部的距离。

* 如果同时设置了start和end，当两者规则冲突时，仅start属性生效。
* 若容器在某个方向的尺寸被声明为"auto"，则该方向上的guideLine位置只能使用start属性声明（不允许使用百分比）。

在以下示例代码中，定义了一条垂直辅助线guideline1，距离容器左侧50vp，以及另一条水平辅助线guideline2，距离容器顶部50vp。组件row1通过这两条辅助线来定位自身位置，无需设置bias。

```
1. @Entry
2. @Component
3. struct RelativeGuideLineExample {
4. build() {
5. Row() {
6. RelativeContainer() {
7. Row()
8. .width(100)
9. .height(100)
10. .backgroundColor('#a3cf62')
11. .alignRules({
12. left: { anchor: 'guideline1', align: HorizontalAlign.End },
13. top: { anchor: 'guideline2', align: VerticalAlign.Top }
14. })
15. .id('row1')
16. }
17. .width(300)
18. .height(300)
19. .margin({ left: 50 })
20. .border({ width: 2, color: '#6699FF' })
21. .guideLine([{ id: 'guideline1', direction: Axis.Vertical, position: { start: 50 } },
22. { id: 'guideline2', direction: Axis.Horizontal, position: { start: 50 } }])
23. }
24. .height('100%')
25. }
26. }
```

[RelativeContainerComponentGuideLine.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerComponentGuideLine.ets#L15-L42)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/9Lc_J-C1StqsCCKy95FkEQ/zh-cn_image_0000002558764228.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=1DB943346E98AD5E61385B51F98DB441361851CD59122AC870B487CCF883B17D)

## 多个组件的屏障

屏障（barrier）是容器的一种动态参考边界，它基于一组指定组件的实际位置，计算出它们在特定方向上的公共最远边界。当需要让某个组件参照多个组件的集体边界时使用，例如实现“位于这些组件右侧”或“不与其他任何组件重叠”等效果。

屏障可以有上下左右四个方向。垂直方向（TOP，BOTTOM）的屏障仅能作为组件的水平方向锚点，用作垂直方向锚点时值为0；水平方向（LEFT，RIGHT）的屏障仅能作为组件的垂直方向锚点，用作水平方向锚点时值为0。

与静态的guideline不同，barrier会随参照组件位置变化而自动更新，只需定义实际需要的方向即可。

在下列示例代码中，item1，item2，item3三个组件可以视为由一个隐形的矩形区域包围着，outer1基于这个“隐形区域”的底部边界进行布局，位于该区域的下方；outer2基于这个“隐形区域”的右侧边界进行布局，位于该区域的右侧。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. RelativeContainer() {
6. Text('item 1')
7. .width(80)
8. .height(80)
9. .textAlign(TextAlign.Center)
10. .backgroundColor('#a3cf62')
11. .id('item1')
12. .alignRules({
13. top: {
14. anchor: '__container__',
15. align: VerticalAlign.Top
16. },
17. left: {
18. anchor: '__container__',
19. align: HorizontalAlign.Start
20. }
21. })
22. Text('item 2')
23. .width(80)
24. .height(80)
25. .textAlign(TextAlign.Center)
26. .backgroundColor('#a3cf62')
27. .id('item2')
28. .alignRules({
29. top: {
30. anchor: 'item1',
31. align: VerticalAlign.Bottom
32. },
33. left: {
34. anchor: 'item1',
35. align: HorizontalAlign.End
36. }
37. })
38. Text('item 3')
39. .width(80)
40. .height(80)
41. .textAlign(TextAlign.Center)
42. .backgroundColor('#a3cf62')
43. .id('item3')
44. .alignRules({
45. bottom: {
46. anchor: 'item2',
47. align: VerticalAlign.Top
48. },
49. left: {
50. anchor: 'item2',
51. align: HorizontalAlign.End
52. }
53. })
54. Text('outer 1')
55. .width(80)
56. .height(80)
57. .textAlign(TextAlign.Center)
58. .backgroundColor('#00ae9d')
59. // 定义其位置
60. .alignRules({
61. top: {
62. anchor: 'barrier_bottom',
63. align: VerticalAlign.Top
64. },
65. left: {
66. anchor: 'barrier_left',
67. align: HorizontalAlign.Start
68. }
69. })

71. Text('outer 2')
72. .width(80)
73. .height(80)
74. .textAlign(TextAlign.Center)
75. .backgroundColor('#00ae9d')
76. // 定义其位置
77. .alignRules({
78. top: {
79. anchor: 'barrier_top',
80. align: VerticalAlign.Top
81. },
82. left: {
83. anchor: 'barrier_right',
84. align: HorizontalAlign.Start
85. }
86. })
87. }
88. .width('100%')
89. .padding(10)
90. .barrier([
91. {
92. id: 'barrier_left',
93. direction: BarrierDirection.LEFT,
94. referencedId: ['item1', 'item2', 'item3']
95. },
96. {
97. id: 'barrier_right',
98. direction: BarrierDirection.RIGHT,
99. referencedId: ['item1', 'item2', 'item3']
100. },
101. {
102. id: 'barrier_top',
103. direction: BarrierDirection.TOP,
104. referencedId: ['item1', 'item2', 'item3']
105. },
106. {
107. id: 'barrier_bottom',
108. direction: BarrierDirection.BOTTOM,
109. referencedId: ['item1', 'item2', 'item3']
110. },
111. ])
112. }
113. }
```

[RelativeContainerComponentBarrier.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/relativecontainerlayout/RelativeContainerComponentBarrier.ets#L15-L80)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/jOAnFrL1SRWivEudwLBC0A/zh-cn_image_0000002558604572.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=68981DB98A0CB094E91D4491939479831D5384316E1F62C4680050CA9B6AB1E4)
