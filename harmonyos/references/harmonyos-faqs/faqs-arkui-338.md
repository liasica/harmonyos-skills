---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-338
title: Marquee组件的文字滚动，第一次滚动出现大量空白，如何避免空白出现
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Marquee组件的文字滚动，第一次滚动出现大量空白，如何避免空白出现
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6e8cce6041aecff8df26fc92e9a0a8bd23a86b8a3d62700cf06964c7ef97ba96
---

**问题现象**

Marquee组件在文本滚动时，文本滚动到控件的开头，会造成大量空白，如何实现让文本末尾滚动到控件末尾时停止，避免空白出现。

**解决措施**

推荐使用Scroll代替跑马灯组件实现文字滚动。示例代码如下：

```
1. @Entry
2. @Component
3. struct MarqueeScroll {
4. @State textList: string[] = [
5. 'this is a test string1 this is a test string1',
6. 'this is a test string2 this is a test string2 this is a test string2',
7. 'this is a test string3 this is a test string3 this is a test string3 this is a test string3'
8. ];
9. @State count: number = 1;

11. build() {
12. Row() {
13. Column() {
14. myMarqueeCard({
15. textList: $textList,
16. updateList: () => {
17. this.textList = [
18. `This is test data${this.count++}This is test data${this.count++}`,
19. `This is test data${this.count++}This is test data${this.count++}This is test data${this.count++}`,
20. `This is test data${this.count++}This is test data${this.count++}This is test data${this.count++}This is test data${this.count++}`
21. ];
22. }
23. })
24. }
25. .width('100%')
26. .margin(20)
27. }
28. .height('100%')
29. }
30. }

32. @Component
33. struct myMarqueeCard {
34. @Link @Watch('handleNewList') textList: string[];
35. @State list: string[] = [];
36. scroller1: Scroller = new Scroller();
37. scroller2: Scroller = new Scroller();
38. scroller3: Scroller = new Scroller();
39. updateList?: () => void;
40. private intervalID?: number;

42. handleNewList() {
43. console.info(JSON.stringify(this.textList));
44. }

46. handleScroll(scroller: Scroller) {
47. this.intervalID = setInterval(() => {
48. const curOffset: OffsetResult = scroller.currentOffset();
49. scroller.scrollTo({
50. xOffset: curOffset.xOffset + 50, yOffset: curOffset.yOffset, animation: {
51. duration: 1000,
52. curve: Curve.Linear
53. }
54. });
55. if (scroller.isAtEnd() && this.scroller1.isAtEnd() && this.scroller2.isAtEnd() && this.scroller3.isAtEnd() &&
56. this.updateList) {
57. this.scroller1.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
58. this.scroller2.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
59. this.scroller3.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
60. this.updateList();
61. }
62. }, 500);
63. }

65. @Builder
66. SingleText($$: SingleTextParams) {
67. Scroll($$.scroller) {
68. Row() {
69. Text($$.text)
70. .fontSize(30)
71. .onAppear(() => {
72. this.handleScroll($$.scroller);
73. })
74. }
75. }
76. .width(300)
77. .scrollable(ScrollDirection.Horizontal)
78. .enableScrollInteraction(false)
79. .scrollBar(BarState.Off)
80. }

82. aboutToDisappear(): void {
83. clearInterval(this.intervalID);
84. }

86. build() {
87. Column() {
88. this.SingleText({ text: this.textList[0], scroller: this.scroller1 })
89. this.SingleText({ text: this.textList[1], scroller: this.scroller2 })
90. this.SingleText({ text: this.textList[2], scroller: this.scroller3 })
91. }
92. }
93. }

95. class SingleTextParams {
96. text: string = '';
97. scroller: Scroller = new Scroller();
98. }
```

[MarqueeAvoidsBlankSpacesFromAppearing.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MarqueeAvoidsBlankSpacesFromAppearing.ets#L21-L119)
