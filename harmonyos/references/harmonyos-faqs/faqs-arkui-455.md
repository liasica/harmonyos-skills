---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-455
title: 如何控制Tabs内容页单向滑动切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何控制Tabs内容页单向滑动切换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fc71c9348524b921504e106020b8f977b2a27f441d2e1ac48f6422f985c1f52d
---

**背景知识**

[scrollable](../harmonyos-references/ts-container-tabs.md#scrollable)：设置是否可以通过滑动页面进行Tab页面切换，默认支持向左向右两个方向滑动。

gesture：通用属性手势绑定，可绑定[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)、[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)、[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)、[PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)、[RotationGesture](../harmonyos-references/ts-basic-gestures-rotationgesture.md)、[SwipeGesture](../harmonyos-references/ts-basic-gestures-swipegesture.md)等手势。

**解决方案**

1. 创建活动手势的[PanGestureOptions](../harmonyos-references/ts-basic-gestures-pangesture.md#pangestureoptions)，指定滑动方向为向右滑动。

   panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Right })
2. 给除第一个tab外，其他每个tab的内容父组件绑定gesture滑动手势，指定为第一步创建的panOption。

   .gesture(PanGesture(this.panOption))

示例代码如下：

```
1. @Component
2. struct TabsPageSwitching {
3. @State currentIndex: number = 0;
4. private controller: TabsController = new TabsController();
5. private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Right });

7. @Builder
8. tabBuilder(index: number, name: string) {
9. Column() {
10. Text(name)
11. .fontSize(16)
12. .lineHeight(22)
13. .margin({ top: 16, bottom: 16 })
14. .fontColor(this.currentIndex === index ? Color.Blue : Color.Black)

16. Divider()
17. .strokeWidth(2)
18. .color(Color.Blue)
19. .opacity(this.currentIndex === index ? 1 : 0)
20. }
21. .width('100%')
22. }

24. build() {
25. Column() {
26. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
27. TabContent() {
28. Column()
29. .width('100%')
30. .height('100%')
31. .backgroundColor(Color.Green)
32. }
33. .tabBar(this.tabBuilder(0, 'Tab1'))

35. TabContent() {
36. Column()
37. .width('100%')
38. .height('100%')
39. .backgroundColor(Color.Pink)
40. .gesture(PanGesture(this.panOption))
41. }
42. .tabBar(this.tabBuilder(1, 'Tab2'))

44. TabContent() {
45. Column()
46. .width('100%')
47. .height('100%')
48. .backgroundColor(Color.Orange)
49. .gesture(PanGesture(this.panOption))
50. }
51. .tabBar(this.tabBuilder(2, 'Tab3'))
52. }
53. .vertical(false)
54. .barMode(BarMode.Fixed)
55. .barWidth(360)
56. .barHeight(56)
57. .animationDuration(200)
58. .onChange((index: number) => {
59. this.currentIndex = index;
60. })
61. .width('100%')
62. .height(296)
63. .margin({ top: 52 })
64. }
65. .width('100%')
66. }
67. }
```

[TabsPageSwitching.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/b9d6551b75b078dfbf00850327a0896f97877d23/ArkUI/entry/src/main/ets/pages/TabsPageSwitching.ets#L21-L87)
