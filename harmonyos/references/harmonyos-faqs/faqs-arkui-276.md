---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-276
title: 如何实现List内拖拽交换子组件位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现List内拖拽交换子组件位置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:12+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:e8023d83c839e4bda7a32576d9dd3a8ed0309cad6f626af7ccc3d49b123aed16
---

1. 在onItemDragStart回调中设置拖拽过程中显示的内容。
2. 在onItemDrop中通过itemIndex获取拖拽起始位置，insertIndex获取目标位置，并在onItemDrop中调用changeListItemIndex函数交换数组中的元素位置。

参考如下示例：

```
1. @Entry
2. @Component
3. struct Index {
4. @State listArr: string[] = [];

6. @Builder
7. textItemBuilder(text: string) {
8. Column() {
9. Text(text)
10. .fontSize(16)
11. .backgroundColor(0xDCDCDC)
12. .width(80)
13. .height(80)
14. .textAlign(TextAlign.Center)
15. }
16. }

18. aboutToAppear() {
19. for (let i = 0; i < 16; i++) {
20. this.listArr.push(i + '');
21. }
22. }

24. // Swap the position of listItem in the listArr array
25. changeListItemIndex(index1: number, index2: number) {
26. let tempItem = this.listArr[index1];
27. this.listArr[index1] = this.listArr[index2];
28. this.listArr[index2] = tempItem;
29. }

31. build() {
32. Column() {
33. List() {
34. ForEach(this.listArr, (item: string) => {
35. ListItem() {
36. Text(item)
37. }
38. .width(80)
39. .height(80)
40. .backgroundColor(Color.White)
41. .borderRadius(4)
42. .margin({ top: 10 })
43. }, (item: string) => item)
44. }
45. .width('100%')
46. .height(500)
47. .lanes({ minLength: 80, maxLength: 80 })
48. .alignListItem(ListItemAlign.Center)
49. .onItemDragStart((event: ItemDragInfo, index: number) => {
50. return this.textItemBuilder(this.listArr[index]);
51. })
52. .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
53. if (!isSuccess || insertIndex < 0 || insertIndex >= this.listArr.length) {
54. return;
55. }
56. this.changeListItemIndex(itemIndex, insertIndex);
57. })
58. }
59. .width('100%')
60. .height('100%')
61. .backgroundColor(0xDCDCDC)
62. }
63. }
```

[ListExchangeSubcomponentPositions.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListExchangeSubcomponentPositions.ets#L21-L84)
