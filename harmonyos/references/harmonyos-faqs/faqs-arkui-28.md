---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-28
title: 如何设置分组列表的圆角和间距
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置分组列表的圆角和间距
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a871967d64ab301409096338d322b1d5c01a60cf4514d2ee630e9ecc8c230101
---

通过[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)中的ListItemGroupStyle设置分组列表的圆角，List的[space](../harmonyos-references/ts-container-list.md#接口)设置间距。可参考如下代码：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListItemGroupExample {
5. private timeTable: TimeTable[] = [
6. { projects: ['language'] },
7. { projects: ['mathematics', 'English'] },
8. { projects: ['physics', 'chemistry', 'biology'] },
9. { projects: ['the fine arts', 'music', 'sport'] }
10. ]

12. build() {
13. Column() {
14. List({ space: 20 }) { // Set the spacing of the grouping list
15. ForEach(this.timeTable, (item: TimeTable) => {
16. ListItemGroup({ style: ListItemGroupStyle.CARD }) { // Set the rounded corners of the grouping list
17. ForEach(item.projects, (project: string) => {
18. ListItem() {
19. Text(project)
20. .width("100%")
21. .height(100)
22. .fontSize(20)
23. .textAlign(TextAlign.Center)
24. .backgroundColor(0xFFFFFF)
25. }
26. }, (item: string) => item)
27. }
28. })
29. }
30. .width('90%')
31. .sticky(StickyStyle.Header | StickyStyle.Footer)
32. .scrollBar(BarState.Off)
33. }
34. .width('100%')
35. .height('100%')
36. .backgroundColor(0xDCDCDC)
37. .padding({ top: 5, bottom: 5 })
38. }
39. }

41. interface TimeTable {
42. projects: string[];
43. }
```

[SetRoundedCornersAndSpacing.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SetRoundedCornersAndSpacing.ets#L21-L63)
