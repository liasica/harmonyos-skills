---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-468
title: 如何实现Tabs切换页签，强制重新刷新页面数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现Tabs切换页签，强制重新刷新页面数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a39db2c8eeca980ca280144bba293df2d9c48ac716996a00c85bdcad561a5173
---

**问题描述**

在Tab切换数据没重新加载，如何保证每次点击Tab标签都能重新加载数据，包含一级Tab栏和二级Tab栏。

**解决措施**

可以通过在主页面通过emitter.emit('refreshTable')发送指定的事件refreshTable来强制重新刷新页面数据，即当Tab切换至index=0时触发事件，子组件通过计数器变化驱动视图更新。

请参考如下示例：

```
1. import { SubTabContent } from './SubTabContent'
2. import { emitter } from '@kit.BasicServicesKit'

4. @Entry
5. @Component
6. export struct TabContentExample {
7. @State fontColor: string = '#182431'
8. @State selectedFontColor: string = '#007DFF'
9. @State currentIndex: number = 0
10. @State selectedIndex: number = 0
11. @State refreshFlag: boolean = true
12. private controller: TabsController = new TabsController()

14. @Builder
15. tabBuilder(index: number) {
16. Column() {
17. Text(`Tab${index + 1}`)
18. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
19. .fontSize(20)
20. .fontWeight(500)
21. .lineHeight(14)
22. }.width('100%')
23. }

25. build() {
26. Column() {
27. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
28. TabContent() {
29. Column() {
30. SubTabContent()
31. }
32. .width('100%')
33. }.tabBar(this.tabBuilder(0))

35. TabContent() {
36. Column() {
37. Text('Tab2')
38. .fontSize(36)
39. .fontColor('#182431')
40. .fontWeight(500)
41. .opacity(0.4)
42. .margin({ top: 30, bottom: 56.5 })
43. Divider()
44. .strokeWidth(0.5)
45. .color('#182431')
46. .opacity(0.05)
47. }.width('100%')
48. }.tabBar(this.tabBuilder(1))
49. }
50. .vertical(false)
51. .barHeight(56)
52. .onChange((index: number) => {
53. this.currentIndex = index
54. this.selectedIndex = index
55. if (index === 0) {
56. // 事件携带的数据
57. let eventData: emitter.EventData = {
58. data: {}
59. };
60. // 通过emitter.emit('refreshTable')发送指定的事件
61. emitter.emit("refreshTable", eventData);
62. }
63. })
64. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
65. if (index === targetIndex) {
66. return
67. }
68. // selectedIndex控制自定义TabBar内Image和Text颜色切换
69. this.selectedIndex = targetIndex
70. })
71. .width('100%')
72. .height('100%')
73. .backgroundColor('#F1F3F5')
74. .margin({ top: 38 })
75. }
76. .width('100%')
77. .height('100%')
78. .padding({
79. bottom: 30
80. })
81. }
82. }
```

[TabContentExample.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabContentExample.ets#L21-L102)

在子页面通过emitter.on('refreshTable')持续订阅该事件去刷新数据。

请参考如下代码：

```
1. import { emitter } from '@kit.BasicServicesKit';

3. @Component
4. export struct SubTabContent {
5. @State counter: number = 0

7. aboutToAppear(): void {
8. // Tabs子组件通过emitter.on('refreshTable')持续订阅该事件去刷新数据
9. emitter.on("refreshTable", () => {
10. this.counter += 1
11. });
12. }

14. build() {
15. Text(`切换Tabs刷新数据${this.counter}`)
16. }
17. }
```

[TabContentExample.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabContentExample.ets#L106-L122)
