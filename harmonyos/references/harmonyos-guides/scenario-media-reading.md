---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-media-reading
title: 插画/视频/动画的播报场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 插画/视频/动画的播报场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7befb50b3527d58fa48cf8b4a409fc5889649cf983ace82d98b6300d54fe1051
---

## 开发实例1

如下图，插画信息有一定提示作用，插画和对应的功能介绍应该组合在一起，当焦点落到插画或者包含插画的符合控件时，需要朗读出对应的功能描述。建议插画和功能介绍作为一个组合使用一个焦点朗读。它可以借助“accessibilityGroup(true)”属性来实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/O2N2xNIuTlOVG5p0tadZOg/zh-cn_image_0000002583477517.png?HW-CC-KV=V1&HW-CC-Date=20260427T233806Z&HW-CC-Expire=86400&HW-CC-Sign=214EA877A6BAD361F2513DD39A3F26E2F27F8A8CAF262B6CC7CAF49E5907BC99)

```
1. @Entry
2. @Component
3. export struct Rule_2_1_6_1 {
4. title: string = 'Rule 2.1.6.1'
5. private description: string = 'gesture swipe left then up'

7. build() {
8. NavDestination() {
9. Column() {
10. Flex({
11. direction: FlexDirection.Column,
12. alignItems: ItemAlign.Center,
13. justifyContent: FlexAlign.Center,
14. }) {
15. Column() {
16. Image($r("app.media.gesture_swipe_left_then_up"))
17. .width(220)
18. .height(220)
19. Text(this.description)
20. .fontSize(22)
21. .fontColor(Color.Red)
22. .fontWeight(FontWeight.Bold)
23. .textAlign(TextAlign.Center)
24. }.accessibilityGroup(true) // 将图像和文本合并为一个辅助功能对象
25. }
26. .width('100%')
27. .height('100%')
28. .backgroundColor(Color.White)
29. }
30. }
31. .title(this.title)
32. }
33. }
```

## 开发实例2

以下List的每个Item，应该进行组合标注，从而给用户一个完整的提示信息：

* 对于列表/网格控件，控件中的每个项目默认需要一起标记。
* 列表/网格控件，每个item应提供item包含的元素的所有信息。
* 建议朗读列表每一项的所有嵌套元素的组合信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/UpEUjOcGQgKa8zownYcqcg/zh-cn_image_0000002552797868.png?HW-CC-KV=V1&HW-CC-Date=20260427T233806Z&HW-CC-Expire=86400&HW-CC-Sign=D85DB4FBDE782532C212069A14D07F7A9ACEF415B510F55AB73EEFDDC7C2516B)

  它可以借助“accessibilityGroup(true)”属性来实现：

  ```
  1. @Entry
  2. @Preview
  3. @Component
  4. export struct Rule_2_1_6_2 {
  5. title: string = 'Rule 2.1.6.2'

  7. build() {
  8. NavDestination() {
  9. Flex({
  10. direction: FlexDirection.Column,
  11. alignItems: ItemAlign.Center,
  12. justifyContent: FlexAlign.Center,
  13. }) {
  14. Column() {
  15. Item_2_1_6_3({
  16. title: 'Video card',
  17. subtitle: 'provided with options',
  18. time: '1:23 hrs',
  19. color: '#ffdee5ff'
  20. })
  21. Item_2_1_6_3({
  22. title: 'Music card',
  23. subtitle: 'sound feedback available',
  24. time: '2:75 min',
  25. color: '#92e1ffd8'
  26. })
  27. Item_2_1_6_3({
  28. title: 'Live card',
  29. subtitle: 'health support on request',
  30. time: '10:55',
  31. color: '#fff3deff'
  32. })
  33. Item_2_1_6_3({
  34. title: 'Play card',
  35. subtitle: 'play station tournament',
  36. time: '5:12 hrs',
  37. color: '#92e1ffd8'
  38. })
  39. Item_2_1_6_3({
  40. title: 'Theater card',
  41. subtitle: 'ticket on concert',
  42. time: '2:75 min',
  43. color: '#ffdee5ff'
  44. })
  45. }
  46. }
  47. }.title(this.title)
  48. }
  49. }

  51. @Component
  52. export struct Item_2_1_6_3 {
  53. title: string = 'Video card'
  54. subtitle: string = 'provided with additional options'
  55. time: string = '1:23 hr'
  56. color: ResourceColor = "#80FAFAFA"

  58. build() {
  59. Flex({
  60. direction: FlexDirection.Row,
  61. alignItems: ItemAlign.Center,
  62. justifyContent: FlexAlign.SpaceBetween,
  63. }) {
  64. Column() {
  65. Text(this.title)
  66. .fontSize(22)
  67. .fontWeight(FontWeight.Bold)
  68. .textAlign(TextAlign.Center)
  69. .padding({ left: 20, right: 0 })
  70. Text(this.subtitle)
  71. .fontSize(14)
  72. .fontColor(Color.Gray)
  73. .fontWeight(FontWeight.Normal)
  74. .textAlign(TextAlign.Center)
  75. .padding({ left: 20, right: 0 })
  76. }

  78. Column() {
  79. Text(this.time)
  80. .fontSize(20)
  81. .fontWeight(FontWeight.Normal)
  82. .textAlign(TextAlign.Center)
  83. .padding({ left: 10, right: 10 })
  84. }

  86. Column() {
  87. Image($r("app.media.ic_arrow")) // 此处为图片资源，请替换为本地图片
  88. .width(28)
  89. .height(28)
  90. .fillColor(Color.Gray)
  91. }.align(Alignment.End)

  93. }
  94. .width('90%')
  95. .height(75)
  96. .border({
  97. width: 1,
  98. color: '#FFC0C0C0',
  99. radius: 8,
  100. style: {
  101. top: BorderStyle.Solid,
  102. }
  103. })
  104. .backgroundColor(this.color)
  105. .accessibilityGroup(true) // combines text and image into single object
  106. .margin({ top: 10 })
  107. }
  108. }
  ```
