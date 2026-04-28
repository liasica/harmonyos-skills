---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-109
title: List组件如何设置多列
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > List组件如何设置多列
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:455ef6da02065f8477587300726203ee0a81604f87e0b539c69bf0432b20f295
---

以列模式为例(listDirection为Axis.Vertical):lanes用于决定List组件在交叉轴方向上的列数。参考代码如下：

```
1. @Entry
2. @Component
3. struct ListLanesExample {
4. @State arr: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'];
5. @State alignListItem: ListItemAlign = ListItemAlign.Start;

7. build() {
8. Column() {
9. List({ space: 20, initialIndex: 0 }) {
10. ForEach(this.arr, (item: string) => {
11. ListItem() {
12. Text('' + item)
13. .width('100%')
14. .height(100)
15. .fontSize(16)
16. .textAlign(TextAlign.Center)
17. .borderRadius(10)
18. .backgroundColor(0xFFFFFF)
19. }
20. .border({ width: 2, color: Color.Green })
21. }, (item: string) => item)
22. }
23. .height(300)
24. .width('90%')
25. .border({ width: 3, color: Color.Red })
26. .lanes({ minLength: 40, maxLength: 40 })
27. .alignListItem(this.alignListItem)

29. Button('Click to change alignListItem:' + this.alignListItem).onClick(() => {
30. if (this.alignListItem == ListItemAlign.Start) {
31. this.alignListItem = ListItemAlign.Center;
32. } else if (this.alignListItem == ListItemAlign.Center) {
33. this.alignListItem = ListItemAlign.End;
34. } else {
35. this.alignListItem = ListItemAlign.Start;
36. }
37. })
38. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
39. }
40. }
```

[ListSettingMultipleColumns.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListSettingMultipleColumns.ets#L21-L62)
