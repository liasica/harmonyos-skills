---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-397
title: 如何实现swiper根据内容高度随滑动距离变动的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现swiper根据内容高度随滑动距离变动的效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e5cf6d7b010f904fe8a7ddf75703681e0c404464d66d5052fb970579317fd3fa
---

可通过[onContentDidScroll()](../harmonyos-references/ts-container-swiper.md#oncontentdidscroll12)监听Swiper页面滑动事件来实现，示例代码如下：

```
1. let COLUMN_NUMBER = 5;
2. let COLUMN_GAP = 20;
3. let ROWS_GAP = 20;

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Column() {
10. Text('Head area')
11. .textAlign(TextAlign.Center)
12. .backgroundColor(Color.Yellow)
13. .width('100%')
14. .height(40)
15. GridDemo()
16. .width('90%')
17. Text('Tail area')
18. .textAlign(TextAlign.Center)
19. .backgroundColor(Color.Green)
20. .width('100%')
21. .height('30%')
22. }
23. }
24. }

26. @Component
27. struct GridDemo {
28. @State gridHeights: number[] = [];
29. @State swiperHeight: number = 0;
30. @State tipList: string[] = ['Mathematics', 'Chinese Language', 'English', 'Biology'];
31. @State tipImageX: string = '0%';
32. @State tipIndex: number = 0;
33. @State numberList: number[][] = [
34. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
35. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
36. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
37. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
38. ];
39. private swiperController: SwiperController = new SwiperController();

41. aboutToAppear(): void {
42. this.getHeights();
43. }

45. getHeights() {
46. for (let index = 0; index < this.numberList.length; index++) {
47. let rowNumer = Math.ceil(this.numberList[index].length / COLUMN_NUMBER);
48. let gridHeight = px2vp(122) * rowNumer + COLUMN_GAP * (rowNumer - 1);
49. this.gridHeights.push(gridHeight);
50. }
51. this.swiperHeight = this.gridHeights[0];
52. }

54. build() {
55. Column() {
56. Stack() {
57. Image($r('app.media.background'))
58. .objectFit(ImageFit.Contain)
59. .width((100 / this.tipList.length) + '%')
60. .offset({ x: this.tipImageX })
61. Row() {
62. ForEach(this.tipList, (item: string, index: number) => {
63. ListItem() {
64. Text(item)
65. .backgroundImage(this.tipIndex == index ? $r('app.media.background') : null, ImageRepeat.NoRepeat)
66. .backgroundImageSize({
67. width: '100%',
68. height: '100%'
69. })
70. }
71. }, (item: string) => item)
72. }
73. .justifyContent(FlexAlign.SpaceAround)
74. .height(20)
75. .width('100%')
76. .margin({
77. top: 5,
78. bottom: 5
79. })
80. }
81. .alignContent(Alignment.Start)
82. .height(30)
83. .backgroundColor(Color.Pink)

85. Column() {
86. Swiper(this.swiperController) {
87. ForEach(this.numberList, (item: number, index: number) => {
88. Child({ numberList: this.numberList[index] })
89. })
90. }
91. .effectMode(EdgeEffect.None)
92. .indicator(false)
93. .loop(false)
94. .onContentDidScroll((selectedIndex: number, index: number, position: number, mainAxisLength: number) => {
95. // The direct scrolling positions of the two indices change the height of the parent control
96. if (selectedIndex != index && Math.abs(selectedIndex - index) == 1) {
97. let curHeight = this.gridHeights[selectedIndex];
98. let targetHeight = this.gridHeights[index];
99. this.swiperHeight = targetHeight +
100. (selectedIndex < index ? (curHeight - targetHeight) : (targetHeight - curHeight)) * position;
101. }
102. // Switch the subscript of the selected status
103. if (selectedIndex == index) {
104. let curIndex = -1 / this.tipList.length * position + selectedIndex / this.tipList.length;
105. this.tipImageX = (curIndex * 100).toFixed(2) + '%';
106. this.tipIndex = Math.ceil(curIndex / 0.25 + 0.5) - 1;
107. }
108. })
109. }
110. .height(this.swiperHeight)
111. }
112. .width('100%')
113. }
114. }

116. @Component
117. struct Child {
118. @Prop numberList: number[];

120. build() {
121. Grid() {
122. ForEach(this.numberList, (item: number) => {
123. GridItem() {
124. Column() {
125. Image($r('app.media.startIcon'))
126. .width(20)
127. .height(20)
128. Text('Menu' + item)
129. .fontSize(15)
130. }
131. }
132. })
133. }
134. .columnsGap(COLUMN_GAP)
135. .rowsGap(ROWS_GAP)
136. .scrollBar(BarState.Off)
137. .columnsTemplate('1fr '.repeat(COLUMN_NUMBER))
138. .animation({
139. duration: 1000
140. })
141. }
142. }
```

[HeightFollowsSlidingChanges.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/HeightFollowsSlidingChanges.ets#L21-L162)
