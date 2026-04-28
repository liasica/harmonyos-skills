---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-316
title: 如何实现Scroll、List单边回弹效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现Scroll、List单边回弹效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d3e1b169c1bebc03daf5adf113bab932d81e2ab82dfba76e85b22ba29c7687fe
---

1. [Scroll组件](../harmonyos-references/ts-container-scroll.md)：在onDidScroll里获取currentOffset().yOffset来控制单边回弹效果；

2. [List组件](../harmonyos-references/ts-container-list.md)：在onDidScroll里获取currentOffset().yOffset来控制，还可以通过onScrollIndex实现单边回弹效果。

参考代码如下：

```
1. // Single side rebound effect of Scroll component
2. @Entry
3. @Component
4. struct ScrollSideRebound {
5. @State yOffset: number = 0;
6. scroller: Scroller = new Scroller();
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

10. build() {
11. Stack({ alignContent: Alignment.TopStart }) {
12. Scroll(this.scroller) {
13. Column() {
14. ForEach(this.arr, (item: number) => {
15. Text(item.toString())
16. .width('90%')
17. .height(150)
18. .backgroundColor(0xFFFFFF)
19. .borderRadius(15)
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .margin({ top: 10 })
23. }, (item: string) => item)
24. }
25. .width('100%')
26. }
27. .scrollable(ScrollDirection.Vertical) // Rolling direction vertically
28. .scrollBar(BarState.On) // Scroll bar permanent display
29. .scrollBarColor(Color.Gray) // Scroll bar color
30. .scrollBarWidth(2) // Scroll bar width
31. .friction(0.6)
32. .edgeEffect(this.yOffset <= 0 ? EdgeEffect.Spring : EdgeEffect.None) // Rebound after rolling to the edge
33. .onDidScroll(() => {
34. this.yOffset = this.scroller.currentOffset().yOffset;
35. })
36. }
37. .width('100%')
38. .height('100%')
39. .backgroundColor(0xDCDCDC)
40. }
41. }
```

[ScrollListUnilateralReboundEffect.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ScrollListUnilateralReboundEffect.ets#L21-L61)

```
1. // Single side rebound effect of List component
2. @Entry
3. @Component
4. struct ListSideRebound {
5. @State isTop: boolean = true;
6. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

8. build() {
9. Column() {
10. List({ space: 20, initialIndex: 0 }) {
11. ForEach(this.arr, (item: number) => {
12. ListItem() {
13. Text('' + item)
14. .width('100%')
15. .height(100)
16. .fontSize(16)
17. .textAlign(TextAlign.Center)
18. .borderRadius(10)
19. .backgroundColor(0xFFFFFF)
20. }
21. }, (item: string) => item)
22. }
23. .listDirection(Axis.Vertical) // Arrangement direction
24. .scrollBar(BarState.Off)
25. .friction(0.6)
26. .edgeEffect(this.isTop ? EdgeEffect.Spring : EdgeEffect.None) // Enable the flex effect only on the top boundary
27. .onScrollIndex((firstIndex: number) => {
28. if (this.arr.length === 0 || firstIndex === 0) {
29. this.isTop = true;
30. } else {
31. this.isTop = false;
32. }
33. })
34. .width('90%')
35. }
36. .width('100%')
37. .height('100%')
38. .backgroundColor(0xDCDCDC)
39. .padding({ top: 5 })
40. }
41. }
```

[ListSideRebound.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListSideRebound.ets#L21-L62)
