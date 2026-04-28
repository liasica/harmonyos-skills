---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-292
title: 如何实现二维数组的懒加载
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现二维数组的懒加载
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6a739853b112f5d179c7e65d2c64f8a50e17a588c05e222c3fc2e004ec946d5d
---

通过HashMap存储二维数组数据，并利用ListGroup组件实现分组懒加载，其中HashMap的键为分组标题，值为对应分组的数据源。示例代码如下：

```
1. import { HashMap } from '@kit.ArkTS';

3. class BasicDataSource implements IDataSource {
4. private listeners: DataChangeListener[] = [];
5. private originDataArray: Array<TimeTable> | Array<string> = [];

7. public totalCount(): number {
8. return 0;
9. }

11. public getData(index: number): TimeTable | string {
12. if (index < 0 || index >= this.originDataArray.length) {
13. return '';
14. }
15. return this.originDataArray[index];
16. }

18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. console.info('add listener');
21. this.listeners.push(listener);
22. }
23. }

25. unregisterDataChangeListener(listener: DataChangeListener): void {
26. const pos = this.listeners.indexOf(listener);
27. if (pos >= 0) {
28. console.info('remove listener');
29. this.listeners.splice(pos, 1);
30. }
31. }

33. notifyDataReload(): void {
34. this.listeners.forEach(listener => {
35. listener.onDataReloaded();
36. })
37. }

39. notifyDataAdd(index: number): void {
40. this.listeners.forEach(listener => {
41. listener.onDataAdd(index);
42. })
43. }

45. notifyDataChange(index: number): void {
46. this.listeners.forEach(listener => {
47. listener.onDataChange(index);
48. })
49. }

51. notifyDataDelete(index: number): void {
52. this.listeners.forEach(listener => {
53. listener.onDataDelete(index);
54. })
55. }

57. notifyDataMove(from: number, to: number): void {
58. this.listeners.forEach(listener => {
59. listener.onDataMove(from, to);
60. })
61. }
62. }

64. class MyDataSource extends BasicDataSource {
65. private dataArray: TimeTable[] | Array<string> = [];

67. constructor(data: Array<TimeTable> | Array<string>) {
68. super();
69. this.dataArray = data;
70. }

72. public totalCount(): number {
73. return this.dataArray.length;
74. }

76. public getData(index: number): TimeTable | string {
77. return this.dataArray[index];
78. }

80. public addDataTimeTable(index: number, data: TimeTable): void {
81. this.dataArray.splice(index, 0, data);
82. this.notifyDataAdd(index);
83. }

85. public addDataString(index: number, data: string): void {
86. this.dataArray.splice(index, 0, data);
87. this.notifyDataAdd(index);
88. }

90. public pushDataTimeTable(data: TimeTable): void {
91. (this.dataArray as Array<TimeTable>).push(data);
92. this.notifyDataAdd(this.dataArray.length - 1);
93. }

95. public pushDataString(data: string): void {
96. (this.dataArray as Array<string>).push(data);
97. this.notifyDataAdd(this.dataArray.length - 1);
98. }
99. }

101. /*
102. * The course schedule data structure, title represents the day of the week, and projects represents the list of courses for that day
103. */
104. interface TimeTable {
105. title: string;
106. projects: string[];
107. }

109. @Component
110. export struct TwoNestingArrayLazy {
111. @State timeTable: TimeTable[] = [
112. {
113. title: 'Monday',
114. projects: ['language', 'mathematics', 'English']
115. },
116. {
117. title: 'Tuesday',
118. projects: ['physics', 'chemistry', 'biology']
119. },
120. {
121. title: 'Wednesday',
122. projects: ['history', 'geography', 'politics']
123. },
124. {
125. title: 'Thursday',
126. projects: ['the fine arts', 'music', 'sport']
127. }
128. ];
129. private data1: MyDataSource = new MyDataSource(this.timeTable);
130. private hashMap: HashMap<string, MyDataSource> = new HashMap<string, MyDataSource>();

132. aboutToAppear(): void {
133. for (let index = 0; index < this.timeTable.length; index++) {
134. this.hashMap.set(this.timeTable[index].title, new MyDataSource(this.timeTable[index].projects));
135. }
136. }

138. @Builder
139. itemHead(text: string) {
140. Text(text)
141. .fontSize(20)
142. .backgroundColor(0xAABBCC)
143. .width('100%')
144. .padding(10)
145. }

147. @Builder
148. itemFoot(itemCount: number) {
149. Text('common' + itemCount + 'period')
150. .fontSize(16)
151. .backgroundColor(0xAABBCC)
152. .width("100%")
153. .padding(5)
154. }

156. build() {
157. List({ space: 3 }) {
158. LazyForEach(this.data1, (item: TimeTable) => {
159. ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
160. LazyForEach(this.hashMap.get(item.title), (project: string) => {
161. ListItem() {
162. Text(project)
163. .width('100%')
164. .height(100)
165. .fontSize(20)
166. .textAlign(TextAlign.Center)
167. .backgroundColor(0xFFFFFF)
168. }
169. }, (item: string) => item)
170. }
171. .divider({ strokeWidth: 1, color: Color.Blue }) // The boundary line between each row
172. }, (item: string) => item)
173. }
174. .width('100%')
175. .height('100%')
176. }
177. }
```

[ImplementLazyLoadingOfTwoDimensionalArrays.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementLazyLoadingOfTwoDimensionalArrays.ets#L21-L197)
