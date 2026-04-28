---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-17
title: 如何实现Tabs页签导航栏切换时，下划线也随之滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现Tabs页签导航栏切换时，下划线也随之滑动
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d220a87458b88e79cbbe4956754e9c2c4add10c438cfc8277b217d289b9bd37c
---

可通过SubTabBarStyle子页签样式实现该效果，具体参考如下代码：

```
1. @Entry
2. @Component
3. struct TabsBarUnderlineSwitching {
4. private controller: TabsController = new TabsController();
5. @State indicatorColor: Color = Color.Blue;
6. @State indicatorWidth: number = 40;
7. @State indicatorHeight: number = 5;
8. @State indicatorBorderRadius: number = 5;
9. @State indicatorSpace: number = 10;
10. @State subTabBorderRadius: number = 20;
11. @State selectedMode: SelectedMode = SelectedMode.INDICATOR;

14. build() {
15. Column() {
16. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
17. TabContent() {
18. Column().width('100%').height('100%').backgroundColor(Color.Pink).borderRadius('12vp')
19. }.tabBar(SubTabBarStyle.of('pink')
20. .indicator({
21. color: this.indicatorColor, // Underline color
22. height: this.indicatorHeight, // Underline height
23. width: this.indicatorWidth, // Underline width
24. borderRadius: this.indicatorBorderRadius, // Underline corner radius
25. marginTop: this.indicatorSpace // The spacing between underline and text
26. })
27. .selectedMode(this.selectedMode)
28. .board({ borderRadius: this.subTabBorderRadius })
29. .labelStyle({})
30. )

33. TabContent() {
34. Column().width('100%').height('100%').backgroundColor(Color.Yellow).borderRadius('12vp')
35. }.tabBar(SubTabBarStyle.of('yellow')
36. .indicator({
37. color: this.indicatorColor, // Underline color
38. height: this.indicatorHeight, // Underline height
39. width: this.indicatorWidth, // Underline width
40. borderRadius: this.indicatorBorderRadius, // Underline corner radius
41. marginTop: this.indicatorSpace // The spacing between underline and text
42. })
43. .selectedMode(this.selectedMode)
44. .board({ borderRadius: this.subTabBorderRadius })
45. .labelStyle({})
46. )

49. TabContent() {
50. Column().width('100%').height('100%').backgroundColor(Color.Blue).borderRadius('12vp')
51. }.tabBar(SubTabBarStyle.of('blue')
52. .indicator({
53. color: this.indicatorColor, // Underline color
54. height: this.indicatorHeight, // Underline height
55. width: this.indicatorWidth, // Underline width
56. borderRadius: this.indicatorBorderRadius, // Underline corner radius
57. marginTop: this.indicatorSpace // The spacing between underline and text
58. })
59. .selectedMode(this.selectedMode)
60. .board({ borderRadius: this.subTabBorderRadius })
61. .labelStyle({})
62. )

65. TabContent() {
66. Column().width('100%').height('100%').backgroundColor(Color.Green).borderRadius('12vp')
67. }.tabBar(SubTabBarStyle.of('green')
68. .indicator({
69. color: this.indicatorColor, // Underline color
70. height: this.indicatorHeight, // Underline height
71. width: this.indicatorWidth, // Underline width
72. borderRadius: this.indicatorBorderRadius, // Underline corner radius
73. marginTop: this.indicatorSpace // The spacing between underline and text
74. })
75. .selectedMode(this.selectedMode)
76. .board({ borderRadius: this.subTabBorderRadius })
77. .labelStyle({})
78. )

81. TabContent() {
82. Column().width('100%').height('100%').backgroundColor(Color.Gray).borderRadius('12vp')
83. }.tabBar(SubTabBarStyle.of('gray')
84. .indicator({
85. color: this.indicatorColor, // Underline color
86. height: this.indicatorHeight, // Underline height
87. width: this.indicatorWidth, // Underline width
88. borderRadius: this.indicatorBorderRadius, // Underline corner radius
89. marginTop: this.indicatorSpace // The spacing between underline and text
90. })
91. .selectedMode(this.selectedMode)
92. .board({ borderRadius: this.subTabBorderRadius })
93. .labelStyle({})
94. )

97. TabContent() {
98. Column().width('100%').height('100%').backgroundColor(Color.Orange).borderRadius('12vp')
99. }.tabBar(SubTabBarStyle.of('orange')
100. .indicator({
101. color: this.indicatorColor, // Underline color
102. height: this.indicatorHeight, // Underline height
103. width: this.indicatorWidth, // Underline width
104. borderRadius: this.indicatorBorderRadius, // Underline corner radius
105. marginTop: this.indicatorSpace // The spacing between underline and text
106. })
107. .selectedMode(this.selectedMode)
108. .board({ borderRadius: this.subTabBorderRadius })
109. .labelStyle({})
110. )
111. }
112. .vertical(false)
113. .scrollable(true)
114. .fadingEdge(false)
115. .barMode(BarMode.Scrollable)
116. .barHeight(140)
117. .animationDuration(400)
118. .onChange((index: number) => {
119. console.info(index.toString())
120. })
121. .backgroundColor(0xF5F5F5)
122. .height(320)
123. }.width('100%').height(250).padding({ top: '24vp', left: '24vp', right: '24vp' })
124. }
125. }
```

[NavigationBarSwitching.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/NavigationBarSwitching.ets#L21-L145)

**参考链接**

[TabContent](../harmonyos-references/ts-container-tabcontent.md)中的子页签样式SubTabBarStyle
