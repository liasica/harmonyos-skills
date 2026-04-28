---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-442
title: Tabs如何设置页面margin，使得边距空白跟随页面滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs如何设置页面margin，使得边距空白跟随页面滑动
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a28c4ea1962d54dab9e143c70c543049372ffc3985ea76fa04ec26cbdef03cad
---

**问题背景**

为Tabs设置了外边距，但在页签滑动时边距没有跟随页面滑动。

**解决措施**

设置页面边距的参数下沉到每个子页面中，参考代码如下：

```
1. @Entry
2. @Component
3. struct SetTabsMarginDemo {
4. private tabsController: TabsController = new TabsController()
5. @State currentIndex: number = 0;

7. @Builder
8. TabBarBuilder(title: string, targetIndex: number) {
9. Column(){
10. Text(title)
11. .fontWeight(targetIndex === this.currentIndex ? FontWeight.Bold : FontWeight.Normal).margin({ left: 10, right: 10 })
12. .fontColor(targetIndex === this.currentIndex ? Color.Orange : Color.Gray)
13. .onClick(() => {
14. this.tabsController.changeIndex(targetIndex)
15. })
16. }
17. }

19. build() {
20. Row() {
21. Column() {
22. Flex({ direction: FlexDirection.Row }) {
23. this.TabBarBuilder('页签1', 0)
24. this.TabBarBuilder('页签2', 1)
25. this.TabBarBuilder('页签3', 2)
26. }

28. Tabs({ barPosition: BarPosition.Start, controller: this.tabsController }) {
29. TabContent() {
30. Column() {
31. Text("页签1页面")
32. }
33. .height('100%')
34. .width('100%')
35. .backgroundColor(Color.Yellow)
36. }
37. // The place where the margins are correctly set.
38. .margin({left : 10, right :10})

40. TabContent() {
41. Column() {
42. Text("页签2页面")
43. }
44. .height('100%')
45. .width('100%')
46. .backgroundColor(Color.Green)
47. }
48. // The place where the margins are correctly set.
49. .margin({left : 10, right :10})

51. TabContent() {
52. Column() {
53. Text("页签3页面")
54. }
55. .height('100%')
56. .width('100%')
57. .backgroundColor(Color.Pink)
58. }
59. // The place where the margins are correctly set.
60. .margin({left : 10, right :10})
61. }
62. // The parameter for adjusting the margins should not be added here, as it may affect the user experience.
63. // .margin({left : 10, right :10})
64. .onChange((index: number) => {
65. this.currentIndex = index;
66. })
67. }
68. }
69. }
70. }
```

[SetTabsMarginDemo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/22947c04ee32f5f2adb0be40f025f476660ecc7a/ArkUI/entry/src/main/ets/pages/SetTabsMarginDemo.ets#L21-L90)
