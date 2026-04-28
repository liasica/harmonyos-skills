---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-337
title: 双层嵌套list，如何使用LazyForEach起作用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 双层嵌套list，如何使用LazyForEach起作用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:178603966aaa29c73993748cbe075e3eeff23feed1807845f9fa6ba61cb9bb08
---

**问题场景**

在外层ListA中，每个ListItem包含一个内层List，内层List使用LazyForEach实现懒加载效果。设置外层ListItem高度会导致内层LazyForEach失效（所有项一次性加载），而不设置高度时虽可正常懒加载，但可能导致内层列表数据显示不全。

**解决措施**

固定内层List高度。参考如下代码：

```
1. const bgColors: ResourceColor[] = [Color.Blue, Color.Gray];
2. const rowHeight = 60;

4. export class BaseDataSource<T> implements IDataSource {
5. private readonly listeners: DataChangeListener[] = [];
6. protected dataset: T[];

8. constructor(dataset?: T[]) {
9. this.dataset = dataset ?? [];
10. }

12. public resetDataset(dataset: T[]) {
13. this.dataset = dataset;
14. this.notifyDataReload();
15. }

17. public updateDataAt(index: number, data: T) {
18. if (index >= 0 && index < this.dataset.length) {
19. this.dataset[index] = data;
20. this.notifyDataChange(index);
21. } else {
22. console.error(`Index ${index} out of bounds`);
23. }
24. }

26. public getDataset() {
27. return this.dataset;
28. }

30. public totalCount(): number {
31. return this.dataset.length;
32. }

34. public getData(index: number): T {
35. return this.dataset[index];
36. }

38. /**
39. * Notify LazyForEach component to reload all child components
40. */
41. notifyDataReload(): void {
42. this.listeners.forEach(listener => {
43. listener.onDataReloaded();
44. })
45. }

47. /**
48. * Notify LazyForEach component to add a sub component at the index corresponding to the index
49. * @param index
50. */
51. notifyDataAdd(index: number): void {
52. this.listeners.forEach(listener => {
53. listener.onDataAdd(index);
54. })
55. }

57. /**
58. * Notify LazyForEach component that there is a change in data at the index corresponding to the index, and that the sub component needs to be rebuilt
59. * @param index
60. */
61. notifyDataChange(index: number): void {
62. this.listeners.forEach(listener => {
63. listener.onDataChange(index);
64. })
65. }

67. /**
68. * Notify LazyForEach component to remove the sub component at the index corresponding to the index
69. * @param index
70. */
71. notifyDataDelete(index: number): void {
72. this.listeners.forEach(listener => {
73. listener.onDataDelete(index);
74. })
75. }

77. /**
78. * Notify LazyForEach component to swap the subcomponents at the from index and to index
79. * @param from
80. * @param to
81. */
82. notifyDataMove(from: number, to: number): void {
83. this.listeners.forEach(listener => {
84. listener.onDataMove(from, to);
85. })
86. }

88. //----------------------------------------------------------------------------------------------------
89. // This method is called on the framework side to add listener listening to the LazyForEach component at its data source
90. registerDataChangeListener(listener: DataChangeListener): void {
91. if (this.listeners.indexOf(listener) < 0) {
92. this.listeners.push(listener);
93. }
94. }

96. // This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source
97. unregisterDataChangeListener(listener: DataChangeListener): void {
98. const pos = this.listeners.indexOf(listener);
99. if (pos >= 0) {
100. this.listeners.splice(pos, 1);
101. }
102. }
103. }

105. class NestedListItemDataSource extends BaseDataSource<string> {
106. private dataArray: string[] = [];

108. public totalCount(): number {
109. return this.dataArray.length;
110. }

112. public getData(index: number): string {
113. return this.dataArray[index];
114. }

116. public addData(index: number, data: string): void {
117. this.dataArray.splice(index, 0, data);
118. this.notifyDataAdd(index);
119. }

121. public pushData(data: string): void {
122. this.dataArray.push(data);
123. this.notifyDataAdd(this.dataArray.length - 1);
124. }
125. }

127. /*
128. * Header component for nested list items
129. * @param title - Display text for header
130. */
131. @Component
132. struct header {
133. title: string = '';

135. build() {
136. Column() {
137. Text(this.title)
138. .width('100%')
139. .height(40)
140. .fontSize(14)
141. .backgroundColor(Color.Yellow)
142. .fontColor(Color.Blue)
143. .textAlign(TextAlign.Center)
144. }
145. }
146. }

148. @Component
149. struct ItemComponent {
150. title: string = '';
151. @Prop datas: string[];

153. generateDataSource() {
154. let datasource: NestedListItemDataSource = new NestedListItemDataSource();
155. for (let index = 0; index < this.datas.length; index++) {
156. const element = this.datas[index];
157. datasource.pushData(element);
158. }
159. return datasource;
160. }

162. build() {
163. Column() {
164. header({ title: this.title })
165. List() {
166. LazyForEach(this.generateDataSource(), (data: string, index) => {
167. ListItem() {
168. Text(data)
169. .width('100%')
170. .fontSize(14)
171. .backgroundColor(Color.White)
172. .fontColor(bgColors[index % bgColors.length])
173. .textAlign(TextAlign.Center)
174. }
175. .height(rowHeight)
176. }, (data: string, index) => {
177. console.info(`------- ${data + ' - ' + index.toString()}`);
178. return data + ' - ' + index.toString();
179. })
180. }
181. .layoutWeight(1)
182. .scrollBar(BarState.Off)
183. .cachedCount(10)
184. .friction(1.25)
185. .edgeEffect(EdgeEffect.None)
186. }
187. }
188. }

190. function generateData(pre: string, count: number) {
191. let datas: string[] = [];
192. for (let index = 0; index < count; index++) {
193. const element = pre + '-' + index.toString();
194. datas.push(element);
195. }
196. return datas;
197. }

199. @Entry
200. @Component
201. struct Index {
202. private scroll: Scroller = new Scroller();

204. @Builder
205. private mainListView() {
206. List({ scroller: this.scroll }) {
207. ListItem() {
208. ItemComponent({ title: 'A', datas: generateData('A', 200) })
209. }

211. ListItem() {
212. ItemComponent({ title: 'B', datas: generateData('B', 20) })
213. }
214. }
215. .divider({ strokeWidth: 10, color: Color.Gray })
216. .height("100%")
217. .width("100%")
218. .scrollBar(BarState.Off)
219. .edgeEffect(EdgeEffect.None)
220. }

222. build() {
223. Column() {
224. this.mainListView()
225. }.width('100%')
226. .height('100%')
227. .backgroundColor(Color.White)
228. }
229. }
```

[DoubleNestedListsWork.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DoubleNestedListsWork.ets#L21-L250)
