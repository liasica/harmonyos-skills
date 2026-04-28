---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-247
title: ListItemGroup和LazyForEach如何结合使用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ListItemGroup和LazyForEach如何结合使用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:85599ead7c47bd351ee74a6fbbfb59c48f808cdac9d9a4a0555bc4bed09c99bb
---

在List容器组件内可以将ListItemGroup和LazyForEach结合使用。参考代码如下：

```
1. @Entry
2. @Component
3. struct LazyForEachDemo {
4. private list: MyDataSource2 = new MyDataSource2();

6. @Builder
7. itemHead(text: string) {
8. Text(text)
9. .fontSize(20)
10. .backgroundColor(0xAABBCC)
11. .width('100%')
12. .padding(10)
13. }

15. @Builder
16. itemFoot(num: number) {
17. Text('common' + num + 'period')
18. .fontSize(16)
19. .backgroundColor(0xAABBCC)
20. .width('100%')
21. .padding(5)
22. }

24. aboutToAppear() {
25. for (let date = 1; date < ~~(Math.random() * 30) + 3; date++) {
26. let dayData = new DateListItem(date + '');
27. for (let index = 1; index < ~~(Math.random() * 100) + 30; index++) {
28. dayData.orderList.pushData(`hello${index}`);
29. }
30. this.list.pushData(dayData);
31. }
32. }

34. build() {
35. Column() {
36. List({ space: 20 }) {
37. LazyForEach(this.list, (item: DateListItem) => {
38. ListItemGroup({ header: this.itemHead(item.date + ''), footer: this.itemFoot(item.orderList.totalCount()) }) {
39. LazyForEach(item.orderList, (order: string) => {
40. ListItem() {
41. Text(order)
42. .width('100%')
43. .height(60)
44. .fontSize(20)
45. .textAlign(TextAlign.Center)
46. .backgroundColor(0xFFFFFF)
47. }
48. }, (item: string) => JSON.stringify(item))
49. }
50. .divider({ strokeWidth: 1, color: Color.Blue })
51. })
52. }
53. .height('100%')
54. .cachedCount(1)
55. .width('90%')
56. .sticky(StickyStyle.Header | StickyStyle.Footer)
57. .scrollBar(BarState.Off)
58. }
59. .width('100%')
60. .height('100%')
61. .backgroundColor(0xDCDCDC)
62. .padding({ top: 5 })
63. }
64. }

66. class BasicDataSource implements IDataSource {
67. private listeners: DataChangeListener[] = [];
68. private originDataArray: string[] = [];

70. public totalCount(): number {
71. return 0;
72. }

74. public getData(index: number): string | DateListItem {
75. return this.originDataArray[index];
76. }

78. registerDataChangeListener(listener: DataChangeListener): void {
79. if (this.listeners.indexOf(listener) < 0) {
80. this.listeners.push(listener);
81. }
82. }

84. unregisterDataChangeListener(listener: DataChangeListener): void {
85. const pos = this.listeners.indexOf(listener);
86. if (pos >= 0) {
87. this.listeners.splice(pos, 1);
88. }
89. }

91. notifyDataReload(): void {
92. this.listeners.forEach(listener => {
93. listener.onDataReloaded();
94. })
95. }

97. notifyDataAdd(index: number): void {
98. this.listeners.forEach(listener => {
99. listener.onDataAdd(index);
100. })
101. }

103. notifyDataChange(index: number): void {
104. this.listeners.forEach(listener => {
105. listener.onDataChange(index);
106. })
107. }

109. notifyDataDelete(index: number): void {
110. this.listeners.forEach(listener => {
111. listener.onDataDelete(index);
112. })
113. }
114. }

116. class MyDataSource1 extends BasicDataSource {
117. private dataArray: string[] = [];

119. public totalCount(): number {
120. return this.dataArray.length;
121. }

123. public getData(index: number): string {
124. return this.dataArray[index];
125. }

127. public addData(index: number, data: string): void {
128. this.dataArray.splice(index, 0, data);
129. this.notifyDataAdd(index);
130. }

132. public pushData(data: string): void {
133. this.dataArray.push(data);
134. this.notifyDataAdd(this.dataArray.length - 1);
135. }
136. }

139. class MyDataSource2 extends BasicDataSource {
140. private dataArray: DateListItem[] = [];

142. public totalCount(): number {
143. return this.dataArray.length;
144. }

146. public getData(index: number): DateListItem {
147. return this.dataArray[index];
148. }

150. public addData(index: number, data: DateListItem): void {
151. this.dataArray.splice(index, 0, data);
152. this.notifyDataAdd(index);
153. }

155. public pushData(data: DateListItem): void {
156. this.dataArray.push(data);
157. this.notifyDataAdd(this.dataArray.length - 1);
158. }
159. }

161. class DateListItem {
162. date: string;
163. orderList: MyDataSource1;

165. constructor(date: string) {
166. this.date = date;
167. this.orderList = new MyDataSource1();
168. }
169. }
```

[CombiningListItemGroupAndLazyForEach.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CombiningListItemGroupAndLazyForEach.ets#L21-L190)
