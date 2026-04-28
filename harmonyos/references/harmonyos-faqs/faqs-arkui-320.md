---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-320
title: 如何解决滚动类容器的滚动事件和手势之间的冲突
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决滚动类容器的滚动事件和手势之间的冲突
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a94322dd1774ea05746b9c4300c8a9d8e80359204b87de59ba64da7de2d7e7ba
---

可以通过添加并行手势绑定方法[parallelGesture](../harmonyos-guides/arkts-gesture-events-binding.md#parallelgesture并行手势绑定方法)来处理，参考代码如下：

```
1. @Entry
2. @Component
3. struct ScrollAndGesture {
4. scroller: Scroller = new Scroller();
5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
6. private panGestureOptions: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Up | PanDirection.Down });

9. build() {
10. Stack({ alignContent: Alignment.TopStart }) {
11. Scroll(this.scroller) {
12. Column() {
13. ForEach(this.arr, (item: number) => {
14. Text(item.toString())
15. .width('90%')
16. .height(150)
17. .backgroundColor(0xFFFFFF)
18. .borderRadius(15)
19. .fontSize(16)
20. .textAlign(TextAlign.Center)
21. .margin({ top: 10 })
22. }, (item: string) => item)
23. }.width('100%')
24. }
25. .scrollable(ScrollDirection.Vertical) // Rolling direction vertically
26. .scrollBar(BarState.On) // Scroll bar permanent display
27. .scrollBarColor(Color.Gray) // Scroll bar color
28. .scrollBarWidth(10) // Scroll bar width
29. .friction(0.6)
30. .edgeEffect(EdgeEffect.None)
31. .onWillScroll((xOffset: number, yOffset: number) => {
32. console.info(xOffset + ' ' + yOffset);
33. })
34. .onScrollEdge((side: Edge) => {
35. console.info('To the edge');
36. })
37. .onScrollStop(() => {
38. console.info('Scroll Stop');
39. })
40. }

43. .parallelGesture(
44. PanGesture(this.panGestureOptions)
45. .onActionStart((event?: GestureEvent) => {
46. console.info('start',event);
47. })
48. .onActionUpdate((event?: GestureEvent) => {
49. if (event) {
50. console.info('event',event);
51. }
52. })
53. .onActionEnd(() => {
54. console.info('end');
55. })
56. )
57. .width('100%')
58. .height('100%')
59. .backgroundColor(0xDCDCDC)
60. }
61. }
```

[ResolveConflictsBetweenGestures.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveConflictsBetweenGestures.ets#L21-L81)
