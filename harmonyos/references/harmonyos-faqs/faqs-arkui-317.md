---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-317
title: 如何合并两个列表并支持懒加载
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何合并两个列表并支持懒加载
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:699dcedbfc0be3c3dce78503b7558d4cbe8e6b2243acae2b2cca17d5e2f66ee2
---

外层布局使用Scroll，内层布局包含两个List：ListA和ListB。ListA位于上方，ListB位于下方。两者均采用LazyForEach方式加载数据，并绑定nestedScroll属性。

参考代码如下：

```
1. import { MyDataSource } from './DataUtil';

3. @Entry
4. @Component
5. struct DoubleLazyForEach {
6. private scrollerForScroll: Scroller = new Scroller();

8. build() {
9. Flex() {
10. Scroll(this.scrollerForScroll) {
11. Column() {
12. Text('Scroll Area')
13. .width('100%')
14. .height('40%')
15. .backgroundColor(0X330000FF)
16. .fontSize(16)
17. .textAlign(TextAlign.Center)
18. ListA().height('80%')
19. ListB().height('80%')
20. }
21. }
22. .width('100%')
23. .height('100%')
24. }
25. .width('100%')
26. .height('100%')
27. .backgroundColor(0xDCDCDC)
28. .padding(20)
29. }
30. }

32. @Component
33. struct ListA {
34. private scrollerForListA: Scroller = new Scroller();
35. private dataOne: MyDataSource = new MyDataSource();

37. aboutToAppear() {
38. for (let i = 0; i <= 20; i++) {
39. this.dataOne.pushData(`Hello One ${i}`);
40. }
41. }

43. build() {
44. Column() {
45. List({ space: 20, scroller: this.scrollerForListA }) {
46. LazyForEach(this.dataOne, (item: string) => {
47. ListItem() {
48. Text('ListItem' + item)
49. .width('100%')
50. .height('100%')
51. .borderRadius(15)
52. .fontSize(16)
53. .textAlign(TextAlign.Center)
54. .backgroundColor(Color.White)
55. }
56. .width('100%')
57. .height(100)
58. }, (item: string) => item)
59. }
60. .width('100%')
61. .height('100%')
62. .edgeEffect(EdgeEffect.None)
63. .friction(0.6)
64. .nestedScroll({
65. scrollForward: NestedScrollMode.SELF_FIRST,
66. scrollBackward: NestedScrollMode.PARENT_FIRST
67. })
68. }
69. .height('100%')
70. .width('100%')
71. }
72. }

74. @Component
75. struct ListB {
76. private dataTwo: MyDataSource = new MyDataSource();
77. private scrollerForListB: Scroller = new Scroller();

79. aboutToAppear() {
80. for (let i = 0; i <= 20; i++) {
81. this.dataTwo.pushData(`Hello Two ${i}`);
82. }
83. }

85. build() {
86. Column() {
87. List({ space: 20, scroller: this.scrollerForListB }) {
88. LazyForEach(this.dataTwo, (item: string) => {
89. ListItem() {
90. MyText({ state_value: item })
91. }
92. .width('100%')
93. .height(100)
94. }, (item: string) => item)
95. }
96. .width('100%')
97. .height('100%')
98. .edgeEffect(EdgeEffect.None)
99. .friction(0.6)
100. .nestedScroll({
101. scrollForward: NestedScrollMode.PARENT_FIRST,
102. scrollBackward: NestedScrollMode.SELF_FIRST
103. })
104. }
105. }
106. }

108. @Component
109. struct MyText {
110. @State private state_value: string = 'Hello';

112. build() {
113. Text('ListItem' + this.state_value)
114. .width('100%')
115. .height('100%')
116. .borderRadius(15)
117. .fontSize(16)
118. .textAlign(TextAlign.Center)
119. .backgroundColor(Color.Pink)
120. }
121. }
```

[MergeTwoListsAndSupportLazyLoading.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MergeTwoListsAndSupportLazyLoading.ets#L21-L142)

```
1. // DataUtil.ets
2. export class BasicDataSource implements IDataSource {
3. private listeners: DataChangeListener[] = [];
4. private originDataArray: string[] = [];

7. public totalCount(): number {
8. return 0;
9. }

12. public getData(index: number): string {
13. return this.originDataArray[index];
14. }

17. // This method is called on the framework side to add listener listening to the LazyForEach component at its data source
18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. console.info('add listener');
21. this.listeners.push(listener);
22. }
23. }

26. // This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source
27. unregisterDataChangeListener(listener: DataChangeListener): void {
28. const pos = this.listeners.indexOf(listener);
29. if (pos >= 0) {
30. console.info('remove listener');
31. this.listeners.splice(pos, 1);
32. }
33. }

36. // Notify LazyForEach component to reload all child components
37. notifyDataReload(): void {
38. this.listeners.forEach(listener => {
39. listener.onDataReloaded();
40. })
41. }

44. // Notify LazyForEach component to add a sub component at the index corresponding to the index
45. notifyDataAdd(index: number): void {
46. this.listeners.forEach(listener => {
47. listener.onDataAdd(index);
48. })
49. }

52. // Notify LazyForEach component that there is a change in data at the index corresponding to the index, and that the sub component needs to be rebuilt
53. notifyDataChange(index: number): void {
54. this.listeners.forEach(listener => {
55. listener.onDataChange(index);
56. })
57. }

60. // Notify LazyForEach component to remove the sub component at the index corresponding to the index
61. notifyDataDelete(index: number): void {
62. this.listeners.forEach(listener => {
63. listener.onDataDelete(index);
64. })
65. }

68. // Notify LazyForEach component to swap the subcomponents at the from index and to index
69. notifyDataMove(from: number, to: number): void {
70. this.listeners.forEach(listener => {
71. listener.onDataMove(from, to);
72. })
73. }
74. }

77. export class MyDataSource extends BasicDataSource {
78. private dataArray: string[] = [];

81. public totalCount(): number {
82. return this.dataArray.length;
83. }

86. public getData(index: number): string {
87. return this.dataArray[index];
88. }

91. public addData(index: number, data: string): void {
92. this.dataArray.splice(index, 0, data);
93. this.notifyDataAdd(index);
94. }

97. public pushData(data: string): void {
98. this.dataArray.push(data);
99. this.notifyDataAdd(this.dataArray.length - 1);
100. }
101. }
```

[DataUtil.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DataUtil.ets#L21-L121)
