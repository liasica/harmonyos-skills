---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-478
title: Tabs组件子组件包含if节点，if条件变更后, tabBar页签联动异常，有没有解决方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs组件子组件包含if节点，if条件变更后, tabBar页签联动异常，有没有解决方案
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8bd556198fdb360232cb92c85fa94a4c9b1f4b8bd8ee602998705457312c7b0d
---

**问题描述**

在Tabs刚启动的时候创建四个TabContent ，当this.isShowMessageTab为true会再加一个TabContent，

当前有遇到一个问题，当this.isShowMessageTab从false变到true后（即TabContent从4个变成5个后）。 点击最后一个tabBar后，再点击前面的tabBar就无法响应Tabs下的onChange，用左右滑动可以切换Tabs且触发onChange。

完整示例代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. private currentIndex: number = 0;
5. private controller: TabsController = new TabsController();
6. @State change: boolean = true;

8. @Builder
9. tabBuilder(index: number, name: string) {
10. RelativeContainer() {
11. Text(name)
12. .fontColor(this.currentIndex === index ? '#007DFF' : '#182431')
13. .fontSize(16)
14. .fontWeight(this.currentIndex === index ? 500 : 400)
15. .height('auto')
16. .padding({
17. left: 8,
18. right: 8,
19. top: 6,
20. bottom: 6
21. })
22. .id('textTitle')
23. .alignRules({
24. middle: { anchor: '__container__', align: HorizontalAlign.Center },
25. center: { anchor: '__container__', align: VerticalAlign.Center }
26. })
27. Divider()
28. .strokeWidth(1)
29. .color('#C3C3C3')
30. .width(100)
31. .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
32. Divider()
33. .strokeWidth(2)
34. .color('#007DFF')
35. .opacity(this.currentIndex === index ? 1 : 0)
36. .width(100)
37. .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
38. }
39. .width(100)
40. .backgroundColor('#F0F1F3')
41. }

43. build() {
44. RelativeContainer() {
45. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
46. TabContent() {
47. Text('Page One')
48. }
49. .tabBar(this.tabBuilder(0, 'Page One'))
50. .backgroundColor('#ffa2051d')

52. TabContent() {
53. Text('Page Two, Click on Page Three to show or hide')
54. .onClick(() => {
55. this.change = !this.change;
56. })
57. }
58. .tabBar(this.tabBuilder(1, 'Page Two'))
59. .backgroundColor('#ffefd005')

61. if (this.change) {
62. TabContent() {
63. Text('Page Three')
64. }
65. .tabBar(this.tabBuilder(2, 'Page Three'))
66. .backgroundColor('#ff061ef8')

68. TabContent() {
69. Text('Page Four')
70. }
71. .tabBar(this.tabBuilder(3, 'Page Four'))
72. .backgroundColor('#ff039105')

74. TabContent() {
75. Text('Page Five')
76. }
77. .tabBar(this.tabBuilder(4, 'Page Five'))
78. .backgroundColor('#ff02e7c4')
79. }
80. // When the page is hidden, it is necessary to ensure that the first parameter Index of the TabContent page is continuous
81. else {
82. TabContent() {
83. Text('Page Four')
84. }
85. .tabBar(this.tabBuilder(2, 'Page Four'))
86. .backgroundColor('#ff039105')

88. TabContent() {
89. Text('Page Five')
90. }
91. .tabBar(this.tabBuilder(3, 'Page Five'))
92. .backgroundColor('#ff02e7c4')
93. }
94. }
95. .barMode(BarMode.Scrollable)
96. .barBackgroundColor('#fff3f3f3')
97. .onChange((index) => {
98. this.currentIndex = index;
99. })
100. .animationDuration(400)
101. .scrollable(true)
102. .vertical(false)
103. .width('100%')
104. .fadingEdge(false)
105. }
106. }
107. }
```

[TabsLinkageAbnormal.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabsLinkageAbnormal.ets#L21-L128)
