---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-25
title: 如何实现分组列表的吸顶/吸底效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现分组列表的吸顶/吸底效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:eb3b3d8c4a717a603dc2197b6028309a1a1dd58d61ff93ccb1ae604c9d337719
---

可通过[List](../harmonyos-references/ts-container-list.md)组件的sticky属性配合ListItemGroup组件来实现。通过给List组件设置sticky属性为StickyStyle.Header/StickyStyle.Footer。可参考如下代码：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListItemGroupExample {
5. private timeTable: TimeTable[] = [
6. {
7. title: 'Monday',
8. projects: ['language', 'mathematics', 'English']
9. },
10. {
11. title: 'Tuesday',
12. projects: ['physics', 'chemistry', 'biology']
13. },
14. {
15. title: 'Wednesday',
16. projects: ['history', 'geography', 'politics']
17. },
18. {
19. title: 'Thursday',
20. projects: ['the fine arts', 'music', 'sport']
21. }
22. ]

24. @Builder
25. itemHead(text: string) {
26. Text(text)
27. .fontSize(20)
28. .backgroundColor(0xAABBCC)
29. .width("100%")
30. .padding(10)
31. }

33. @Builder
34. itemFoot(num: number) {
35. Text('common' + num + "period")
36. .fontSize(16)
37. .backgroundColor(0xAABBCC)
38. .width("100%")
39. .padding(5)
40. }

42. build() {
43. Column() {
44. List({ space: 20 }) {
45. ForEach(this.timeTable, (item: TimeTable) => {
46. ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
47. ForEach(item.projects, (project: string) => {
48. ListItem() {
49. Text(project)
50. .width("100%")
51. .height(100)
52. .fontSize(20)
53. .textAlign(TextAlign.Center)
54. .backgroundColor(0xFFFFFF)
55. }
56. }, (item: string) => item)
57. }
58. .divider({ strokeWidth: 1, color: Color.Blue }) // The boundary line between each row
59. })
60. }
61. .width('90%')
62. .sticky(StickyStyle.Header | StickyStyle.Footer)
63. .scrollBar(BarState.Off)
64. }
65. .width('100%')
66. .height('100%')
67. .backgroundColor(0xDCDCDC)
68. .padding({ top: 5 })
69. }
70. }

72. interface TimeTable {
73. title: string;
74. projects: string[];
75. }
```

[TopBottomSuctionOfGroupingList.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TopBottomSuctionOfGroupingList.ets#L21-L95)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/MnB8eI8xTz-6Q5YwVQ-z9g/zh-cn_image_0000002530800653.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002502Z&HW-CC-Expire=86400&HW-CC-Sign=66A088A21D5C595A65F4695D43DA48356694651805CF0229209AA925F5D53831)
