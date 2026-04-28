---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-469
title: Tabs组件，使用tab键循环走焦，会在最后一个页面和最后一个页签之间循环，怎么解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs组件，使用tab键循环走焦，会在最后一个页面和最后一个页签之间循环，怎么解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:662d7211b01135bb5297e985416e5b718bc9bf222130b959e6acc9d16043f8c4
---

**问题描述**

使用键盘tab按键切换焦点时，如何检测tabBar页签的焦点状态，或者设置页签不能获焦。现在如果在一个页签在底部的Tabs组件里使用tab键循环切换焦点，会在最后一个页面的最后一个组件和最后一个tabbar页签两个中循环。

示例如下：

```
1. @Entry
2. @Component
3. struct TabsExample {
4. @State fontColor: string = '#182431';
5. @State selectedFontColor: string = '#007DFF';
6. @State currentIndex: number = 0;
7. @State selectedIndex: number = 0;
8. private controller: TabsController = new TabsController();
9. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

11. @Builder
12. tabBuilder(index: number, name: string) {
13. Column() {
14. Text(name)
15. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
16. .fontSize(16)
17. .fontWeight(this.selectedIndex === index ? 500 : 400)
18. .lineHeight(22)
19. .margin({ top: 17, bottom: 7 })
20. Divider()
21. .strokeWidth(2)
22. .color('#007DFF')
23. .opacity(this.selectedIndex === index ? 1 : 0)
24. }.width('100%')
25. }

27. @Builder
28. tabContentBuilder() {
29. Column() {
30. List({ space: 20, initialIndex: 0 }) {
31. ForEach(this.arr, (item: number) => {
32. ListItem() {
33. Text('' + item)
34. .width('100%')
35. .height(100)
36. .fontSize(16)
37. .textAlign(TextAlign.Center)
38. .borderRadius(10)
39. .backgroundColor(0xFFFFFF)
40. .onClick(() => {
41. console.info('item: ' + item);
42. })
43. }
44. }, (item: string) => item)
45. }
46. .listDirection(Axis.Vertical) // 排列方向
47. .scrollBar(BarState.Off)
48. .friction(0.6)
49. .divider({
50. strokeWidth: 2,
51. color: 0xFFFFFF,
52. startMargin: 20,
53. endMargin: 20
54. }) // 每行之间的分界线
55. .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
56. }
57. .width('100%')
58. .height('100%')
59. }

61. build() {
62. Column() {
63. Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
64. TabContent() {
65. this.tabContentBuilder()
66. }.tabBar(this.tabBuilder(0, 'green'))

68. TabContent() {
69. this.tabContentBuilder()
70. }.tabBar(this.tabBuilder(1, 'blue'))

72. TabContent() {
73. this.tabContentBuilder()
74. }.tabBar(this.tabBuilder(3, 'pink'))
75. }
76. .barMode(BarMode.Fixed)
77. .barWidth('100%')
78. .barHeight(56)
79. .animationDuration(400)
80. .onChange((index: number) => {
81. // currentIndex控制TabContent显示页签
82. this.currentIndex = index;
83. this.selectedIndex = index;
84. })
85. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
86. if (index === targetIndex) {
87. return;
88. }
89. // selectedIndex控制自定义TabBar内Image和Text颜色切换
90. this.selectedIndex = targetIndex;
91. })
92. .width('100%')
93. .height('100%')
94. .backgroundColor('#F1F3F5')
95. }.width('100%')
96. }
97. }
```

**解决措施**

需要让tabbar不能获焦，可参考如下示例代码：

```
1. import { CommonModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TabsBarModifierExample {
6. @State selectedIndex: number = 2;
7. @State currentIndex: number = 2;
8. @State isClip: boolean = false;
9. @State tabBarModifier: CommonModifier = new CommonModifier();
10. private controller: TabsController = new TabsController();

12. aboutToAppear(): void {
13. this.tabBarModifier.focusable(false)
14. }

16. @Builder
17. tabBuilder(title: string, targetIndex: number) {
18. Column() {
19. Image($r('app.media.startIcon')).width(30).height(30)
20. Text(title).fontColor(this.selectedIndex === targetIndex ? '#1698CE' : '#6B6B6B')
21. }.width('100%')
22. .height(50)
23. .justifyContent(FlexAlign.Center)
24. .offset({ y: this.selectedIndex === targetIndex ? -15 : 0 })
25. }

27. build() {
28. Column() {
29. Tabs({
30. barPosition: BarPosition.End,
31. index: this.currentIndex,
32. controller: this.controller,
33. barModifier: this.tabBarModifier
34. }) {
35. TabContent() {
36. Column() {
37. Text('首页的内容')
38. }.width('100%').height('100%').backgroundColor('#00CB87').justifyContent(FlexAlign.Center)
39. }.tabBar(this.tabBuilder('首页', 0))

41. TabContent() {
42. Column() {
43. Text('发现的内容')
44. }.width('100%').height('100%').backgroundColor('#007DFF').justifyContent(FlexAlign.Center)
45. }.tabBar(this.tabBuilder('发现', 1))

47. TabContent() {
48. Column() {
49. Text('推荐的内容')
50. }.width('100%').height('100%').backgroundColor('#FFBF00').justifyContent(FlexAlign.Center)
51. }.tabBar(this.tabBuilder('推荐', 2))

53. TabContent() {
54. Column() {
55. Text('我的内容')
56. }.width('100%').height('100%').backgroundColor('#E67C92').justifyContent(FlexAlign.Center)
57. }.tabBar(this.tabBuilder('我的', 3))
58. }
59. .vertical(false)
60. .barMode(BarMode.Fixed)
61. .barWidth(340)
62. .barHeight(60)
63. .onChange((index: number) => {
64. this.currentIndex = index;
65. this.selectedIndex = index;
66. })
67. .width(340)
68. .height(400)
69. .backgroundColor('#F1F3F5')
70. .scrollable(true)
71. }
72. .width('100%')
73. }
74. }
```

[TabsBarModifierExample.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabsBarModifierExample.ets#L21-L94)
