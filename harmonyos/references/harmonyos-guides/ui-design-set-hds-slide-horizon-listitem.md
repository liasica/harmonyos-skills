---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-set-hds-slide-horizon-listitem
title: 设置附带横滑的列表样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 列表 > 设置附带横滑的列表样式
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:02ab459a2d98b17bb2d3c5bf8f1722bbb42a446c677e21cbcb377690faf64655
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持设置附带横滑的列表样式。

应用使用[HdsListItem](../harmonyos-references/ui-design-hdslistitem.md)组件实现多设备上的系统列表的横滑动效按钮的内容和样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/A2bcB-zuSmOoTxkbPNz1Zw/zh-cn_image_0000002583478349.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234156Z&HW-CC-Expire=86400&HW-CC-Sign=B5BF44B4F714BEA0B94AA9998FD7BFC235176113D15B130741B72E9415B9872B)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { promptAction, SymbolGlyphModifier, TextModifier } from '@kit.ArkUI';
   2. import { HdsListItem } from '@kit.UIDesignKit';
   ```
2. 简单配置页面的布局，调用HdsListItem的接口绘制列表的横滑动效按钮的内容和样式。

   ```
   1. @Entry
   2. @Component
   3. struct HdsListItemExample {
   4. @State dataSource: LazyDataSource<Item> = new LazyDataSource();
   5. @State dataArr: Array<Item> = [];
   6. @State EndOffset: number = 0;
   7. private scroller: Scroller = new Scroller();

   9. build() {
   10. Column() {
   11. List({ space: 10, scroller: this.scroller }) {
   12. LazyForEach(this.dataSource, (item: Item) => {
   13. HdsListItem({
   14. hdsListItemCard: {
   15. textItem: {
   16. primaryText: {
   17. text: 'Primary Text',
   18. modifier: new TextModifier().fontColor(Color.Orange).fontSize(16),
   19. }
   20. }
   21. },
   22. swipeActionOptions: {
   23. icons: [
   24. {
   25. icon: new SymbolGlyphModifier($r('sys.symbol.share')).fontColor([Color.Red]).fontSize(16),
   26. backgroundColor: Color.Green,
   27. onAction: () => {
   28. promptAction.openToast({ message: '点击share按钮', duration: 100 });
   29. },
   30. },
   31. {
   32. icon: new SymbolGlyphModifier($r('sys.symbol.plus_square_on_square')),
   33. backgroundColor: Color.Orange,
   34. onAction: () => {
   35. promptAction.openToast({ message: '点击copy按钮', duration: 100 });
   36. },
   37. },
   38. {
   39. icon: new SymbolGlyphModifier($r('sys.symbol.plus_square_dashed_on_square'))
   40. .symbolEffect(new BounceSymbolEffect(), true),
   41. onAction: () => {
   42. promptAction.openToast({ message: '点击paste按钮', duration: 100 });
   43. },
   44. },
   45. ],
   46. deleteIconOptions: {
   47. backgroundColor: Color.Red, //  ---修改背景色
   48. iconColor: Color.Gray, //  ---- 修改垃圾桶的颜色
   49. onAction: () => {
   50. promptAction.openToast({ message: '点击删除按钮', duration: 100 });
   51. }, //   --点击回调
   52. },
   53. fullDeleteOptions: {
   54. isFullDelete: true, // --- 划动距离超过划出组件大小后自动触发删除，默认是false
   55. onFullDeleteAction: () => {
   56. promptAction.openToast({ message: '触发自动删除', duration: 100 });
   57. this.getUIContext()?.animateTo({
   58. duration: 350,
   59. }, () => {
   60. this.dataSource.deleteItem(item)
   61. });
   62. }, //   -- 触发删除时的回调
   63. },
   64. }
   65. })
   66. }, (item: Item) => item.data)
   67. }
   68. .scrollBar(BarState.Off)
   69. .onDidScroll((scrollOffset: number) => {
   70. this.EndOffset = scrollOffset
   71. })
   72. .margin(10)
   73. .width('100%')
   74. .height('100%')
   75. }
   76. .backgroundColor('#0D182431')
   77. .width('100%')
   78. .height('100%')
   79. }

   81. aboutToAppear() {
   82. for (let i = 0; i < 2; i++) {
   83. this.dataSource.pushItem(new Item(i + ''));
   84. this.dataArr.push(new Item(i + ''));
   85. }
   86. }
   87. }

   89. class Item {
   90. constructor(data: string) {
   91. this.data = data;
   92. }

   94. public data: string = '';
   95. }

   97. export class LazyDataSource<T> implements IDataSource {
   98. private elements: T[];
   99. private listeners: Set<DataChangeListener>;

   101. constructor(elements: T[] = []) {
   102. this.elements = elements;
   103. this.listeners = new Set();
   104. }

   106. public totalCount(): number {
   107. return this.elements.length;
   108. }

   110. public getData(index: number): T {
   111. return this.elements[index];
   112. }

   114. public indexOf(item: T): number {
   115. return this.elements.indexOf(item);
   116. }

   118. public pinItem(item: T, index: number): void {
   119. this.elements.splice(index, 1);
   120. this.elements.unshift(item);
   121. this.listeners.forEach(listener => listener.onDataReloaded());
   122. }

   124. public pushItem(item: T) {
   125. this.elements.push(item);
   126. this.listeners.forEach(listener => listener.onDataAdd(this.elements.length - 1));
   127. }

   129. public deleteItem(item: T): void {
   130. const index = this.elements.indexOf(item);
   131. if (index < 0) {
   132. return;
   133. }
   134. this.elements.splice(index, 1);
   135. this.listeners.forEach(listener => listener.onDataDelete(index));
   136. }

   138. public deleteItemByIndex(index: number): void {
   139. this.elements.splice(index, 1);
   140. this.listeners.forEach(listener => listener.onDataDelete(index));
   141. }

   143. public registerDataChangeListener(listener: DataChangeListener): void {
   144. this.listeners.add(listener);
   145. }

   147. public unregisterDataChangeListener(listener: DataChangeListener): void {
   148. this.listeners.delete(listener);
   149. }
   150. }
   ```
