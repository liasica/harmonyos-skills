---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-235
title: 如何实现下拉刷新和上滑加载的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现下拉刷新和上滑加载的效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:910063160ba1cee8b74dded2c4cd6ad69f8144e7bbc18b7a5ffc1e0772d35330
---

使用[onTouch事件](../harmonyos-references/ts-universal-events-touch.md#ontouch)，在putDownPullUpRefresh方法里判断触摸事件是否满足下拉刷新和上滑加载的条件，同时使用条件渲染判断是否显示刷新和加载的布局。

参考代码如下：

```
1. @Entry
2. @Component
3. struct PageToRefresh {
4. private currentOffsetY: number = 0;
5. @State refreshStatus: boolean = false;
6. @State refreshText: string = 'Refreshing';
7. @State pullUpText: string = 'loading';
8. private timer: number = 0;
9. @State isRefreshing: boolean = false;
10. @State isCanLoadMore: boolean = false;
11. @State ArrData: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
12. @State newArr: string [] = ['10', '11']

14. putDownPullUpRefresh(event?: TouchEvent): void {
15. if (event === undefined) {
16. return;
17. }
18. switch (event.type) {
19. case TouchType.Down:
20. this.currentOffsetY = event.touches[0].y;
21. break;
22. case TouchType.Move:
23. let isDownPull = event.touches[0].y - this.currentOffsetY > 50;
24. if (isDownPull && this.isCanLoadMore === false) {
25. this.refreshStatus = true;
26. }

28. if (this.ArrData.length <= 11) {
29. this.isCanLoadMore = true;
30. }
31. break;
32. case TouchType.Cancel:
33. break;
34. case TouchType.Up:
35. if (this.refreshStatus) {
36. this.timer = setTimeout(() => {
37. this.refreshStatus = false;
38. this.ArrData = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
39. }, 1500)
40. }

42. if (this.isCanLoadMore) {
43. this.timer = setTimeout(() => {
44. this.isCanLoadMore = false;
45. this.newArr.forEach((item) => {
46. this.ArrData.push(item)
47. })
48. }, 1000)
49. }

51. break;
52. default:
53. break;
54. }
55. }

57. @Builder
58. putDown() {
59. Row() {
60. Image($r('app.media.refreshing'))
61. .width(40)
62. .height(20)
63. Text(this.refreshText).fontSize(16)
64. }
65. .justifyContent(FlexAlign.Center)
66. .width('94%')
67. .height('10%')
68. }

70. @Builder
71. PullUp() {
72. Row() {
73. Image($r('app.media.refreshing'))
74. .width(40)
75. .height(40)
76. Text(this.pullUpText).fontSize(16)
77. }
78. .justifyContent(FlexAlign.Center)
79. .width('94%')
80. .height('5%')
81. }

83. build() {
84. Column() {
85. Scroll() {
86. Column() {
87. Text('goods')
88. if (this.refreshStatus) {
89. this.putDown()
90. }
91. ForEach(this.ArrData, (item: string) => {
92. ListItem() {
93. Text(item)
94. .height(100)
95. }
96. }, (item: string) => JSON.stringify(item))
97. if (this.isCanLoadMore) {
98. this.PullUp()
99. }
100. if (!this.isCanLoadMore) {
101. Text('No more data available at the moment')
102. }
103. }
104. }
105. .width('100%')
106. .onTouch((event?: TouchEvent) => {
107. this.putDownPullUpRefresh(event);
108. })
109. }
110. }
111. }
```

[ImplementPullDownAndUpwardSliding.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementPullDownAndUpwardSliding.ets#L21-L131)
