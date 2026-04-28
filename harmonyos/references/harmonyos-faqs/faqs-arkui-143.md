---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-143
title: 如何实现拖拽时列表项占位动画的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现拖拽时列表项占位动画的效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:73f4b3b0fad9e0677abdfe6c50a9ffedbc266c6f3b258d89c062c143b462e4ac
---

拖拽Grid时，列表项显示占位动画效果。实现步骤如下：

1. 在Grid组件下设置属性editMode(true)，使Grid进入编辑模式。进入编辑模式后，可以拖拽Grid组件内部的GridItem。
2. 在onItemDragStart回调中设置拖拽时显示的组件。
3. 在onItemDrop中获取拖拽起始位置和拖拽插入位置，并完成数组位置交换逻辑。

   ```
   1. @Entry
   2. @Component
   3. struct GridExample {
   4. @State numbers: string[] = [];
   5. scroller: Scroller = new Scroller();
   6. @State text: string = 'drag';

   8. @Builder
   9. pixelMapBuilder() {
   10. Column() {
   11. Text(this.text)
   12. .fontSize(16)
   13. .backgroundColor(0xF9CF93)
   14. .width(80)
   15. .height(80)
   16. .textAlign(TextAlign.Center)
   17. }
   18. }

   20. aboutToAppear() {
   21. for (let i = 1; i <= 15; i++) {
   22. this.numbers.push(i + '');
   23. }
   24. }

   26. changeIndex(index1: number, index2: number) {
   27. // Swap array positions
   28. let temp = this.numbers[index1];
   29. this.numbers[index1] = this.numbers[index2];
   30. this.numbers[index2] = temp;
   31. }

   33. build() {
   34. Column({ space: 5 }) {
   35. Grid(this.scroller) {
   36. ForEach(this.numbers, (day: string) => {
   37. GridItem() {
   38. Text(day)
   39. .fontSize(16)
   40. .backgroundColor(0xF9CF93)
   41. .width(80)
   42. .height(80)
   43. .textAlign(TextAlign.Center)
   44. .onTouch((event: TouchEvent) => {
   45. if (event.type === TouchType.Up) {
   46. this.text = day;
   47. }
   48. })
   49. }
   50. })
   51. }
   52. .columnsTemplate('1fr 1fr 1fr')
   53. .columnsGap(10)
   54. .rowsGap(10)
   55. .onScrollIndex((first: number) => {
   56. console.info(first.toString());
   57. })
   58. .width('90%')
   59. .backgroundColor(0xFAEEE0)
   60. .height(300)
   61. .editMode(true) // Set whether the Grid enters editing mode. When entering editing mode, you can drag and drop the GridItem inside the Grid component
   62. .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // When dragging the component bound to this event for the first time, a callback is triggered.
   63. return this.pixelMapBuilder(); //Set the image displayed during the drag and drop process.
   64. })
   65. // The component bound to this event can be used as a drag and drop release target. When the drag behavior stops within the scope of this component, a callback is triggered.
   66. .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
   67. // Drag the starting position of itemIndex, drag the insertion position of insertIndex
   68. this.changeIndex(itemIndex, insertIndex)
   69. })
   70. }.width('100%').margin({ top: 5 })
   71. }
   72. }
   ```

   [ListItemPlaceholderAnimation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListItemPlaceholderAnimation.ets#L21-L92)
