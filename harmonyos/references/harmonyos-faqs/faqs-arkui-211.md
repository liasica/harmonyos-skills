---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-211
title: Grid如何实现拖拽功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Grid如何实现拖拽功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:55+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:1ec9482d64c0e8b1acea185a77ace323cbec3fb27cd5cfcbc9b78229df538fc8
---

1. 通过editMode(true)属性设置Grid进入编辑模式，该模式下可拖拽内部GridItem。
2. 在onItemDragStart回调中设置拖拽过程中显示的图片。
3. 在onItemDrop中获取拖拽起始位置和拖拽插入位置，并在onItemDrop中完成交换数组位置动作。

可以参考如下示例代码：

```
1. @Component
2. export struct GridExample {
3. @State numbers: string[] = [];
4. scroller: Scroller = new Scroller();

6. // Drag and drop process style
7. @Builder
8. pixelMapBuilder(text: string) {
9. Column() {
10. Text(text)
11. .fontSize(16)
12. .backgroundColor(0xF9CF93)
13. .width(80)
14. .height(80)
15. .textAlign(TextAlign.Center)
16. }
17. }

19. aboutToAppear() {
20. for (let i = 1; i <= 15; i++) {
21. this.numbers.push(i + '');
22. }
23. }

25. // Swap array positions
26. changeIndex(index1: number, index2: number) {
27. let temp: string;
28. temp = this.numbers[index1];
29. this.numbers[index1] = this.numbers[index2];
30. this.numbers[index2] = temp;
31. }

33. build() {
34. Column({ space: 5 }) {
35. Grid(this.scroller) {
36. ForEach(this.numbers, (day: string) => {
37. GridItem() {
38. this.pixelMapBuilder(day)
39. }
40. })
41. }
42. .columnsTemplate('1fr 1fr 1fr')
43. .columnsGap(10)
44. .rowsGap(10)
45. .width('90%')
46. .backgroundColor(0xFAEEE0)
47. .height(500)
48. .editMode(true) // Set whether the Grid enters editing mode. When entering editing mode, you can drag and drop the GridItem inside the Grid component
49. .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // 第一次拖拽此事件绑定的组件时，触发回调。
50. // Set the image displayed during the drag and drop process
51. return this.pixelMapBuilder(this.numbers[itemIndex]);
52. })
53. .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
54. // The component bound to this event can be used as a drag and drop release target. When the drag behavior stops within the scope of this component, a callback is triggered.
55. // When isSuccess=false, it indicates that the drop is located outside the grid; When insertIndex>length, it indicates that an event of adding new elements has occurred
56. if (!isSuccess || insertIndex >= this.numbers.length) {
57. return;
58. }
59. this.changeIndex(itemIndex, insertIndex);
60. })
61. }
62. .width('100%')
63. .margin({ top: 5 })
64. }
65. }
```

[GridImplementationDragAndDrop.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GridImplementationDragAndDrop.ets#L21-L85)

**参考链接**

[Grid](../harmonyos-references/ts-container-grid.md)
