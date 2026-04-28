---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-5
title: 如何自定义Tabs页签导航栏及其对齐方式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何自定义Tabs页签导航栏及其对齐方式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c2c6dd7575862af2ee4f108ed286f9ad59d2ffd641fd241bab2d026429eada26
---

可以自定义页签，并设置页签的对齐方式。具体操作可参考代码：

```
1. @Entry
2. @Component
3. struct CustomizeTheTabsBarAndItsAlignment {
4. @State focusIndex: number = 0;
5. private controller: TabsController = new TabsController();
6. tabArray = [0, 1];

9. // Custom tab
10. @Builder
11. tabBuilder(tabName: string, tabItem: number, tabIndex: number) {
12. Column({ space: 20 }) {
13. Text(tabName).fontSize(18)
14. Image($r('app.media.startIcon')).width(20).height(20)
15. }
16. .width(100)
17. .height(60)
18. .borderRadius({ topLeft: 10, topRight: 10 })
19. .onClick(() => {
20. this.controller.changeIndex(tabIndex);
21. this.focusIndex = tabIndex;
22. })
23. .backgroundColor(tabIndex === this.focusIndex ? '#ffffffff' : '#ffb7b7b7')
24. }

27. build() {
28. Column() {
29. Column() {
30. // tab
31. Row({ space: 6 }) {
32. Scroll() {
33. Row() {
34. ForEach(this.tabArray, (item: number, index: number) => {
35. this.tabBuilder('page' + item, item, index);
36. })
37. }
38. .justifyContent(FlexAlign.Start)
39. }
40. // Set left alignment
41. .align(Alignment.Start)
42. .scrollable(ScrollDirection.Horizontal)
43. .scrollBar(BarState.Off)
44. .width('80%')
45. .backgroundColor('#ffb7b7b7')
46. }
47. .width('100%')
48. .backgroundColor('#ffb7b7b7')

51. // tabs
52. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
53. ForEach(this.tabArray, (item: number, index: number) => {
54. TabContent() {
55. Text('I am the page ' + item + ' The content')
56. .height(300)
57. .width('100%')
58. .fontSize(30)
59. }
60. .backgroundColor(Color.Pink)
61. })
62. }
63. .barHeight(0)
64. .animationDuration(100)
65. .onContentWillChange((currentIndex, comingIndex) => {
66. this.focusIndex = comingIndex;
67. console.info('foo change' + this.focusIndex);
68. return true;
69. })
70. }
71. .alignItems(HorizontalAlign.Start)
72. .width('100%')
73. }
74. .height('100%')
75. }
76. }
```

[CustomizeTabs.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CustomizeTabs.ets#L21-L96)

**参考链接**

[Tabs](../harmonyos-references/ts-container-tabs.md)
