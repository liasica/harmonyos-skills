---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-339
title: 如何解决Web页上下滑动时会误触发tab页翻页手势及tab页切换时Web组件还可以上下滚动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决Web页上下滑动时会误触发tab页翻页手势及tab页切换时Web组件还可以上下滚动问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c427974a0a873f18e199aa5e97715def45cc659d2ae1e22076a1cb71e9fcd0c3
---

**问题现象**

Tabs组件嵌套Web组件在滚动场景中可能出现以下问题：

1. 在Web页面上下滑动时，可能会误触发标签页的翻页手势。
2. 切换tab页时，Web组件仍可上下滚动。

**解决措施**

1. 可以通过给**Web组件**设置嵌套滚动[nestedScroll](../harmonyos-references/arkts-basic-components-web-attributes.md#nestedscroll11)属性解决。
2. 可以通过给**Web组件**设置网页是否允许滚动[setScrollable](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setscrollable12)属性解决。

示例代码如下：

```
1. import { webview } from '@kit.ArkWeb';

4. @Component
5. @Entry
6. struct TabWebScroll {
7. @State isScrollEnabled: boolean = true; // Control the sliding page for page switching
8. private tabsController = new TabsController();
9. private currentIndex: number = 0;// Track currently active tab index
10. private webviewController: webview.WebviewController = new webview.WebviewController();

13. build() {
14. Tabs({ barPosition: BarPosition.End, controller: this.tabsController }) {
15. TabContent() {
16. Web({ src: 'https://developer.huawei.com/consumer/cn/', controller: this.webviewController })
17. .nestedScroll({
18. // Set nested scrolling
19. scrollForward: NestedScrollMode.PARENT_FIRST,
20. scrollBackward: NestedScrollMode.SELF_FIRST
21. })
22. }
23. .tabBar(this.tabBuilder('home page', 0))

26. TabContent() {
27. Column() {
28. Text('find')
29. }
30. .width('100%')
31. .height('100%')
32. }
33. .tabBar(this.tabBuilder('find', 1))

36. TabContent() {
37. Column() {
38. Text('recommend')
39. }
40. .width('100%')
41. .height('100%')
42. }
43. .tabBar(this.tabBuilder('recommend', 2))

46. TabContent() {
47. Column() {
48. Text('my')
49. }
50. .width('100%')
51. .height('100%')
52. }
53. .tabBar(this.tabBuilder('my', 3))
54. }
55. .onChange((index: number) => {
56. this.currentIndex = index;
57. })
58. .scrollable(this.isScrollEnabled)
59. .onAnimationEnd(() => {
60. // Trigger this callback when the animation ends, and set the web component to slide
61. this.webviewController?.setScrollable(true);
62. })
63. .onGestureSwipe(() => {
64. // During the sliding process on the page, this callback is triggered frame by frame. When switching between tab pages, the web page cannot slide up or down
65. this.webviewController?.setScrollable(false);
66. })
67. }

70. @Builder
71. tabBuilder(title: string, targetIndex: number) {
72. Column() {
73. Text(title)
74. .fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B')
75. }
76. .width('100%')
77. .height(50)
78. .justifyContent(FlexAlign.Center)
79. }
80. }
```

[ResolveWebPageAccidentalTouches.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveWebPageAccidentalTouches.ets#L21-L100)
