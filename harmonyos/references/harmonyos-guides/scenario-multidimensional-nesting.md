---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-multidimensional-nesting
title: 多维嵌套场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 多维嵌套场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ab3d170e18c31dd94d939b1b7acf7cd80c608ced8d20ebdcbf2a78118825018d
---

## 设计场景

如果应用展示的是多维信息，还可能出现“嵌套组”的情况。在嵌套组中，应避免两个可获焦对象的功能或朗读内容产生重复。比如下图的天气卡片，时间和地点信息获取到焦点时，都是朗读的时间信息；不同焦点的重复朗读会额外增加用户的操作步骤，焦点控制杂乱，这些对同一个信息结构的完整描述应该统一标注在这几个子控件的父控件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/epePecDOTo2YH4j0UDgFew/zh-cn_image_0000002558604350.png?HW-CC-KV=V1&HW-CC-Date=20260429T052608Z&HW-CC-Expire=86400&HW-CC-Sign=0A92A4C88D1E2F61B5D33E6D6F2C11202898D08BE334306CAEEAF7728DBADAEF)

## 开发实例

```
1. @Entry
2. @Component
3. export struct Rule_2_1_3 {
4. title: string = 'Rule 2.1.3'

6. build() {
7. NavDestination() {
8. Column() {
9. Text('Incorrect behavior:') // 播报 "Time Group 12:05 Beijing" + "12:05" + "Beijing".
10. //继续下滑焦点可聚焦至子控件文本重复了两次。这是不正确的。
11. .width('100%')
12. .fontSize(12)
13. .fontColor(Color.Black)
14. .margin({bottom: 12})
15. Row(){
16. Text("12:05") // time information
17. .fontSize(32)
18. .fontColor(Color.Red)
19. .fontWeight(FontWeight.Bold)
20. .textAlign(TextAlign.Center)
21. .margin({right: 20})

23. Text("Beijing") // location information
24. .fontSize(20)
25. .fontColor(Color.Green)
26. .fontWeight(FontWeight.Bold)
27. .textAlign(TextAlign.Center)
28. }
29. .accessibilityText("Time Group") // 时间信息、位置信息和此可访问性文本在获得焦点时被朗读。
30. // 带有时间信息的文本组件可聚焦并朗读
31. // 具有位置信息的文本组件可聚焦并朗读
32. .height(50)
33. .margin({bottom: 150})

35. Text('Correct behavior:') // 只朗读 "07:05 Moscow" ，不重复文本。是正确的。
36. .width('100%')
37. .fontSize(12)
38. .fontColor(Color.Black)
39. .margin({bottom: 12})
40. Row(){
41. Text("07:05") // time information
42. .fontSize(32)
43. .fontColor(Color.Red)
44. .fontWeight(FontWeight.Bold)
45. .textAlign(TextAlign.Center)
46. .margin({right: 20})

48. Text("Moscow") // location information
49. .fontSize(20)
50. .fontColor(Color.Green)
51. .fontWeight(FontWeight.Bold)
52. .textAlign(TextAlign.Center)
53. }
54. .height(50)
55. .accessibilityGroup(true) // 获取焦点时朗读时间和位置信息。
56. // 带有时间信息的文本组件无法聚焦和朗读
57. //具有位置信息的文本组件无法获得焦点并朗读
58. }
59. .alignItems(HorizontalAlign.Start)
60. .padding(10)
61. }
62. .title(this.title)
63. }
64. }
```
