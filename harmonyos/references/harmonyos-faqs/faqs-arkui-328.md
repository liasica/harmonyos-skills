---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-328
title: Tab组件页面切换时，如何不显示中间过渡的tab页
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tab组件页面切换时，如何不显示中间过渡的tab页
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:437afb674c56372f582c40456bb3ed800b6ffd8e1e22ac8ccfe115b9753c8264
---

如果需要做动画，可以通过设置[.animationDuration(0)](../harmonyos-references/ts-container-tabs.md#animationduration)跳过中间过渡页显示，示例代码如下：

```
1. @Entry
2. @Component
3. struct TABTransitionAnimation {
4. @State fontColor: string = '#182431';
5. @State selectedFontColor: string = '#007DFF';
6. @State currentIndex: number = 0;
7. private tabController: TabsController = new TabsController();

9. @Builder
10. tabBuilder(index: number, name: string) {
11. Column() {
12. Text(name)
13. .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
14. .fontSize(16)
15. .fontWeight(this.currentIndex === index ? 500 : 400)
16. .lineHeight(22)
17. .margin({
18. top: 17,
19. bottom: 7
20. })
21. Divider()
22. .strokeWidth(2)
23. .color($r('sys.color.brand'))
24. .opacity(this.currentIndex === index ? 1 : 0)
25. }
26. .width('100%')
27. }

29. build() {
30. Column() {
31. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.tabController }) {
32. TabContent() {
33. Column()
34. .width('100%')
35. .height('100%')
36. .backgroundColor('#00CB87')
37. }.tabBar(this.tabBuilder(0, 'green'))

40. TabContent() {
41. Column()
42. .width('100%')
43. .height('100%')
44. .backgroundColor($r('sys.color.brand'))
45. }.tabBar(this.tabBuilder(1, 'blue'))

48. TabContent() {
49. Column()
50. .width('100%')
51. .height('100%')
52. .backgroundColor($r('sys.color.multi_color_11'))
53. }.tabBar(this.tabBuilder(2, 'yellow'))

56. TabContent() {
57. Column()
58. .width('100%')
59. .height('100%')
60. .backgroundColor('#E67C92')
61. }
62. .tabBar(this.tabBuilder(3, 'pink'))
63. }
64. .width(360)
65. .height(296)
66. .barWidth(360)
67. .barHeight(56)
68. .vertical(false)
69. .barMode(BarMode.Fixed)
70. .backgroundColor('#F1F3F5')
71. .margin({ top: 52 })
72. .animationDuration(0) // Setting the animation time to 0 can solve the problem of switching between pages and displaying intermediate transition pages
73. .onChange((index: number) => {
74. if (index >= 0 && index <= 3) {
75. this.currentIndex = index;
76. }
77. })
78. }
79. .width('100%')
80. }
81. }
```

[DoNotDisplayTransitionalTabs.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DoNotDisplayTransitionalTabs.ets#L21-L102)
