---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-multicomponent
title: 组合场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 组合场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:671f09fa05185c3405812f9fc182212b6d5970e5cc934cf00adf0f1127eba379
---

## 设计场景

在一些场景中，一个功能上完整的UI对象可能是由若干个更小的UI组件组合而成的。若每一个小的UI组件都可以获焦并朗读，则会造成信息冗余和效率降低。同时由于可聚焦的组件过多过细，也会影响触摸浏览时走焦的性能体验。在这种情况下，将它们在功能或语义上聚合成一个自然组并作为一个独立可获焦的UI元素来向视障用户表达内容更加合理，且更加高效。总体原则是：对于表示同一个对象信息的多个组件，需要进行组合标注，对外只暴露一个无障碍焦点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/yp2vYTiMS3etstNjwqp5iQ/zh-cn_image_0000002589323875.png?HW-CC-KV=V1&HW-CC-Date=20260429T052608Z&HW-CC-Expire=86400&HW-CC-Sign=2AB467AD44B786FBF5CB02013DCB531743F74C9C785E62E6900E621831EB9B8D)

## 开发实例

如下，可以将多个控件设置为一个组，通过对组设置朗读标签，达到整组播报的效果，组内的子控件设置不可获取焦点。

```
1. @Entry
2. @Component
3. export struct Rule_2_1_4 {
4. title: string = 'Rule 2.1.4'

6. build() {
7. NavDestination() {
8. Column() {

10. Row() {
11. //默认只有子组件才能获取焦点
12. //日期、天气、温度等信息在每个组件独立获取焦点时分别朗读
13. //在组合式组件规范里是不正确的。
14. Text("23 Dec 2023") // 日期信息。组件可独立对焦和朗读
15. .fontSize(32)
16. .fontColor(Color.Red)
17. .fontWeight(FontWeight.Bold)
18. .textAlign(TextAlign.Center)
19. .margin({ right: 20 })

21. Column() // 天气信息。组件可独立对焦和朗读
22. .backgroundColor(Color.Blue)
23. .width(50)
24. .height(50)
25. .accessibilityText("Snow") // 当该组件被屏幕阅读器选中时，该组件不包含文本信息，因此将读取此文本
26. .margin({ right: 20 })

28. Text("-1") // 温度信息。组件可独立对焦和朗读
29. .fontSize(20)
30. .fontColor(Color.Green)
31. .fontWeight(FontWeight.Bold)
32. .textAlign(TextAlign.Center)
33. }
34. .height(50)
35. .margin({ bottom: 20 })

37. Row() {
38. //因为accessibilityGroup属性设置为true，子组件无法获取焦点。
39. //获取焦点时，日期、天气、温度信息一起朗读
40. //此时只有Row可以获取焦点，这是符合组合式组件规范的。
41. Text("24 Dec 2023") //日期信息。组件无法聚焦，无法朗读，因为父组件的accessibilityGroup属性设置为true
42. .fontSize(32)
43. .fontColor(Color.Red)
44. .fontWeight(FontWeight.Bold)
45. .textAlign(TextAlign.Center)
46. .margin({ right: 20 })

48. Column() //天气信息组件无法聚焦，无法朗读，因为父组件的accessibilityGroup为true
49. .backgroundColor(Color.Yellow)
50. .width(50)
51. .height(50)
52. .accessibilityText("Sunny") // 组件不包含文本信息，当组件被屏幕阅读器选中时，因此将读取此文本
53. .margin({ right: 20 })

55. Text("-7") // //温度信息。组件无法聚焦，无法朗读因为父组件的accessibilityGroup为true
56. .fontSize(20)
57. .fontColor(Color.Green)
58. .fontWeight(FontWeight.Bold)
59. .textAlign(TextAlign.Center)
60. }
61. .height(50)
62. .margin({ bottom: 20 })
63. .accessibilityGroup(true) // 将accessibilityGroup属性设置为true
64. }
65. .alignItems(HorizontalAlign.Start)
66. .padding(10)
67. }
68. .title(this.title)
69. }
70. }
```
