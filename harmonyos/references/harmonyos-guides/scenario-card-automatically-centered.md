---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-card-automatically-centered
title: 卡片自动居中的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 卡片自动居中的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:10+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a20ac0b69f7872c9830c37a4d316faa0ba4789e71d10938615ec1a3965d7ad7f
---

## 设计场景

在横向滚动容器中，通过居中限位来突出中心卡片的详细信息和操作选项。为了确保屏幕朗读场景下聚焦卡片的可访问性，需要将获得焦点的卡片自动居中显示，以凸显其重要性。为此，需要应用通过[ForEach](../harmonyos-references/ts-rendering-control-foreach.md)或[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)获取卡片索引，在可聚焦的卡片控件上注册无障碍聚焦回调函数[onAccessibilityFocus](../harmonyos-references/ts-universal-accessibility-event.md#onaccessibilityfocus)，在回调函数中调用滚动容器的[scrollToIndex](../harmonyos-references-V5/ts-container-scroll-V5.md#scrolltoindex)接口并指定卡片索引，将聚焦的卡片控件居中显示。

## 开发实例

如下示例实现一个横向滚动容器，卡片被聚焦时自动居中显示：

```
1. class ListDataSource implements IDataSource {
2. private list: number[] = [];

4. constructor(list: number[]) {
5. this.list = list;
6. }

8. totalCount(): number {
9. return this.list.length;
10. }

12. getData(index: number): number {
13. return this.list[index];
14. }

16. registerDataChangeListener(listener: DataChangeListener): void {
17. }

19. unregisterDataChangeListener(listener: DataChangeListener): void {
20. }
21. }

23. @Entry
24. @Component
25. struct Rule_2_1_18 {
26. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
27. private scrollerForList: Scroller = new Scroller();
28. build() {
29. Column() {
30. List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
31. LazyForEach(this.arr, (index: number) => {
32. ListItem() {
33. Text('' + index)
34. .width('100%')
35. .height(100)
36. .fontSize(16)
37. .textAlign(TextAlign.Center)
38. .borderRadius(10)
39. .backgroundColor(0xFFFFFF)
40. }
41. .width('60%') // 设置高占比item
42. .onClick( () => {
43. // 设置点击事件，使组件可被无障碍聚焦
44. })
45. // 设置无障碍聚焦回调
46. .onAccessibilityFocus((isFocus: boolean) => {
47. if (isFocus) {
48. // 如果聚焦则滚动List，使当前的ListItem居中
49. this.scrollerForList.scrollToIndex(index, false, ScrollAlign.CENTER)
50. }
51. })
52. }, (item: string) => item)
53. }.width('90%')
54. .scrollBar(BarState.Off)
55. .scrollSnapAlign(ScrollSnapAlign.CENTER) // 设置居中对齐
56. .listDirection(Axis.Horizontal) // 设置横向list
57. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
58. }
59. }
```
