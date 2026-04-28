---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-56
title: 如何去除Tabs组件两侧的蒙层
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何去除Tabs组件两侧的蒙层
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:18e0d857ac353de4566f8d8a959e31c4b5dddb2395bd9fa11f1807f93df075c0
---

Tabs组件的fadingEdge属性表示页签超过容器宽度时是否渐隐消失，默认值为true，设置为false时则直接截断显示，不产生任何渐变效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsOpaque {
5. @State message: string = 'Hello World';
6. private controller: TabsController = new TabsController();
7. @State selfFadingFade: boolean = false; // Does the tab gradually disappear when it exceeds the width of the container? The default value is true.

10. build() {
11. Column() {
12. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
13. TabContent() {
14. Column().width('100%').height('100%').backgroundColor(Color.Pink)
15. }.tabBar('pink')

18. TabContent() {
19. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
20. }.tabBar('yellow')

23. TabContent() {
24. Column().width('100%').height('100%').backgroundColor(Color.Blue)
25. }.tabBar('blue')

28. TabContent() {
29. Column().width('100%').height('100%').backgroundColor(Color.Green)
30. }.tabBar('green')

33. TabContent() {
34. Column().width('100%').height('100%').backgroundColor(Color.Green)
35. }.tabBar('green')

38. TabContent() {
39. Column().width('100%').height('100%').backgroundColor(Color.Green)
40. }.tabBar('green')

43. TabContent() {
44. Column().width('100%').height('100%').backgroundColor(Color.Green)
45. }.tabBar('green')

48. TabContent() {
49. Column().width('100%').height('100%').backgroundColor(Color.Green)
50. }.tabBar('green')
51. }
52. .vertical(false)
53. .scrollable(true)
54. .barMode(BarMode.Scrollable)
55. .barHeight(80)
56. .animationDuration(400)
57. .onChange((index: number) => {
58. console.info(index.toString());
59. })
60. .fadingEdge(this.selfFadingFade)
61. .height('30%')
62. .width('100%')
63. }
64. .padding({ top: '24vp', left: '24vp', right: '24vp' })
65. }
66. }
```

[RemoveTabsComponentMask.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/RemoveTabsComponentMask.ets#L21-L86)

**参考链接**

[属性](../harmonyos-references/ts-container-tabs.md#属性)

[示例5（设置TabBar渐隐）](../harmonyos-references/ts-container-tabs.md#示例5设置tabbar渐隐)
