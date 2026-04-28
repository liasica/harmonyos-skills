---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-280
title: 禁用Tab组件边缘滑动回弹效果的方法
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 禁用Tab组件边缘滑动回弹效果的方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3b9d35ba61b09881badc449a13cf8734075dffe570b38afc0cde429ad5dcf220
---

为边缘的 tabContent 添加 PanGesture 手势，最左侧的 tabContent 添加向右滑动手势，最右侧的 tabContent 添加向左滑动手势。示例代码如下：

```
1. @Component
2. export struct TabsNoRebound {
3. @State currentIndex: number = 0;
4. private fontColor: string = '#182431';
5. private selectedFontColor: string = '#007DFF';
6. private controller: TabsController = new TabsController();
7. private panOptionR: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Right });
8. private panOptionL: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left });

10. @Builder
11. tabBuilder(index: number, name: string) {
12. Column() {
13. Text(name)
14. .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
15. .fontSize(16)
16. .fontWeight(this.currentIndex === index ? 500 : 400)
17. .lineHeight(22)
18. .margin({
19. top: 17,
20. bottom: 7
21. })
22. Divider()
23. .strokeWidth(2)
24. .color('#007DFF')
25. .opacity(this.currentIndex === index ? 1 : 0)
26. }
27. .width('100%')
28. }

30. build() {
31. Column() {
32. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
33. TabContent() {
34. Column()
35. .width('100%')
36. .height('100%')
37. .backgroundColor('#00CB87')
38. }
39. .tabBar(this.tabBuilder(0, 'green'))
40. .gesture(
41. // Dragging to the right triggers this gesture event
42. PanGesture(this.panOptionR)
43. .onActionStart((event?: GestureEvent) => {
44. console.info('Pan start');
45. })
46. .onActionUpdate((event?: GestureEvent) => {
47. console.info('Pan onActionUpdate');
48. })
49. .onActionEnd(() => {
50. console.info('Pan end');
51. })
52. )

54. TabContent() {
55. Column()
56. .width('100%')
57. .height('100%')
58. .backgroundColor('#007DFF')
59. }
60. .tabBar(this.tabBuilder(1, 'blue'))

62. TabContent() {
63. Column()
64. .width('100%')
65. .height('100%')
66. .backgroundColor('#FFBF00')
67. }
68. .tabBar(this.tabBuilder(2, 'yellow'))

70. TabContent() {
71. Column()
72. .width('100%')
73. .height('100%')
74. .backgroundColor('#E67C92')
75. }
76. .tabBar(this.tabBuilder(3, 'pink'))
77. .gesture(
78. // Dragging to the left triggers this gesture event
79. PanGesture(this.panOptionL)
80. .onActionStart((event?: GestureEvent) => {
81. console.info('Pan start');
82. })
83. .onActionUpdate((event?: GestureEvent) => {
84. console.info('Pan onActionUpdate');
85. })
86. .onActionEnd(() => {
87. console.info('Pan end');
88. })
89. )
90. }
91. .barMode(BarMode.Fixed)
92. .barWidth(360)
93. .barHeight(56)
94. .onChange((index: number) => {
95. this.currentIndex = index;
96. })
97. .width(360)
98. .height(296)
99. .margin({ top: 52 })
100. .backgroundColor('#F1F3F5')
101. }
102. .width('100%')
103. }
104. }
```

[TabEdgeSlidingEffectTurnedOff.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabEdgeSlidingEffectTurnedOff.ets#L21-L124)
