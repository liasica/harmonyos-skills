---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-310
title: 在长按拖拽排序的场景下，如何实现自定义长按拖拽onItemDragStart的开始触发时长
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 在长按拖拽排序的场景下，如何实现自定义长按拖拽onItemDragStart的开始触发时长
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b9aa36feacae1fec5ed10ef804d0c65a8e22007b2aab0ef59cc778a28afb34ff
---

在Grid组件中，onItemDragStart事件的默认触发时长为170毫秒，但当前版本不支持直接修改该参数。可以通过自定义Grid，通过设置长按手势LongPressGesture中的duration参数，来实现自定义长按拖拽的开始触发时长，参考代码如下：

```
1. import { curves } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ReplaceDefaultTimeSetPage {
6. // Element array
7. @State numbers: number[] = [];
8. @State row: number = 4;
9. // Index of the last element in the array
10. @State lastIndex: number = 0;
11. @State dragItem: number = -1;
12. @State scaleItem: number = -1;
13. @State item: number = -1;
14. @State offsetX: number = 0;
15. @State offsetY: number = 0;
16. // Set grid column count
17. private str: string = '';
18. // Records the offset of the drag starting position
19. private dragRefOffsetx: number = 0;
20. private dragRefOffsety: number = 0;
21. private FIX_VP_X: number = 108;
22. private FIX_VP_Y: number = 120;

24. aboutToAppear() {
25. for (let i = 1; i <= 110; i++) {
26. this.numbers.push(i);
27. }
28. this.lastIndex = this.numbers.length - 1;

30. // Multiple columns
31. for (let i = 0; i < this.row; i++) {
32. this.str = this.str + '1fr ';
33. }
34. }

36. itemMove(index: number, newIndex: number): void {
37. if (!this.isDraggable(newIndex)) {
38. return;
39. }
40. let tmp = this.numbers.splice(index, 1);
41. this.numbers.splice(newIndex, 0, tmp[0]);
42. }

44. // Slide down
45. down(index: number): void {
46. // Specify fixed GridItem does not respond to events
47. if (!this.isDraggable(index + this.row)) {
48. return;
49. }
50. this.offsetY -= this.FIX_VP_Y;
51. this.dragRefOffsety += this.FIX_VP_Y;
52. // Multiple columns
53. this.itemMove(index, index + this.row);
54. }

56. // Slide down (bottom right is empty)
57. down2(index: number): void {
58. if (!this.isDraggable(index + 3)) {
59. return;
60. }
61. this.offsetY -= this.FIX_VP_Y;
62. this.dragRefOffsety += this.FIX_VP_Y;
63. this.itemMove(index, index + 3);
64. }

66. // Slide up
67. up(index: number): void {
68. if (!this.isDraggable(index - this.row)) {
69. return;
70. }
71. this.offsetY += this.FIX_VP_Y;
72. this.dragRefOffsety -= this.FIX_VP_Y;
73. this.itemMove(index, index - this.row);
74. }

76. // Slide left
77. left(index: number): void {
78. if (!this.isDraggable(index - 1)) {
79. return;
80. }
81. this.offsetX += this.FIX_VP_X;
82. this.dragRefOffsetx -= this.FIX_VP_X;
83. this.itemMove(index, index - 1);
84. }

86. // Slide right
87. right(index: number): void {
88. if (!this.isDraggable(index + 1)) {
89. return;
90. }
91. this.offsetX -= this.FIX_VP_X;
92. this.dragRefOffsetx += this.FIX_VP_X;
93. this.itemMove(index, index + 1);
94. }

96. // Slide bottom right
97. lowerRight(index: number): void {
98. if (!this.isDraggable(index + this.row + 1)) {
99. return;
100. }
101. this.offsetX -= this.FIX_VP_X;
102. this.dragRefOffsetx += this.FIX_VP_X;
103. this.offsetY -= this.FIX_VP_Y;
104. this.dragRefOffsety += this.FIX_VP_Y;
105. this.itemMove(index, index + this.row + 1);
106. }

108. // Slide top right
109. upperRight(index: number): void {
110. if (!this.isDraggable(index - (this.row - 1))) {
111. return;
112. }
113. this.offsetX -= this.FIX_VP_X;
114. this.dragRefOffsetx += this.FIX_VP_X;
115. this.offsetY += this.FIX_VP_Y;
116. this.dragRefOffsety -= this.FIX_VP_Y;
117. this.itemMove(index, index - (this.row - 1));
118. }

120. // Slide bottom left
121. lowerLeft(index: number): void {
122. if (!this.isDraggable(index + (this.row - 1))) {
123. return;
124. }
125. this.offsetX += this.FIX_VP_X;
126. this.dragRefOffsetx -= this.FIX_VP_X;
127. this.offsetY -= this.FIX_VP_Y;
128. this.dragRefOffsety += this.FIX_VP_Y;
129. this.itemMove(index, index + (this.row - 1));
130. }

132. // Slide top left
133. upperLeft(index: number): void {
134. if (!this.isDraggable(index - (this.row + 1))) {
135. return;
136. }
137. this.offsetX += this.FIX_VP_X;
138. this.dragRefOffsetx -= this.FIX_VP_X;
139. this.offsetY += this.FIX_VP_Y;
140. this.dragRefOffsety -= this.FIX_VP_Y;
141. this.itemMove(index, index - (this.row + 1));
142. }

144. // Control whether the element can be moved and sorted by its index
145. isDraggable(index: number): boolean {
146. return index >= 0 && index < this.numbers.length;
147. }

149. build() {
150. Column() {
151. Grid() {
152. ForEach(this.numbers, (item: number) => {
153. GridItem() {
154. Text(item + '')
155. .fontSize(16)
156. .width('100%')
157. .textAlign(TextAlign.Center)
158. .height(100)
159. .borderRadius(10)
160. .backgroundColor(0xFFFFFF)
161. .shadow(this.scaleItem == item ? {
162. radius: 70,
163. color: '#15000000',
164. offsetX: 0,
165. offsetY: 0
166. } :
167. {
168. radius: 0,
169. color: '#15000000',
170. offsetX: 0,
171. offsetY: 0
172. })
173. .animation({
174. curve: Curve.Sharp,
175. duration: 300
176. })
177. }
178. .onAreaChange((_oldVal, newVal) => {
179. // Multiple columns
180. this.FIX_VP_X = Math.round(newVal.width as number);
181. this.FIX_VP_Y = Math.round(newVal.height as number);
182. })
183. // Specify fixed GridItem does not respond to events
184. .hitTestBehavior(this.isDraggable(this.numbers.indexOf(item)) ? HitTestMode.Default : HitTestMode.None)
185. .scale({ x: this.scaleItem === item ? 1.05 : 1, y: this.scaleItem === item ? 1.05 : 1 })
186. .zIndex(this.dragItem === item ? 1 : 0)
187. .translate(this.dragItem === item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
188. .padding(10)
189. .gesture(
190. //The following combined gestures are recognized sequentially. If the long press gesture event is not triggered normally, the drag gesture event will not be triggered.
191. GestureGroup(GestureMode.Sequence,
192. LongPressGesture({
193. repeat: true,
194. duration: 50
195. })  // Control the duration of the long-press event that triggers dragging, defaulting to 500 milliseconds. Setting it to less than 0 reverts to the default value; here it is set to 50 milliseconds
196. .onAction((_event?: GestureEvent) => {
197. this.getUIContext().animateTo({
198. curve: Curve.Friction,
199. duration: 300
200. }, () => {
201. this.scaleItem = item;
202. });
203. })
204. .onActionEnd(() => {
205. this.getUIContext().animateTo({
206. curve: Curve.Friction,
207. duration: 300
208. }, () => {
209. this.scaleItem = -1;
210. });
211. }),
212. PanGesture({
213. fingers: 1,
214. direction: null,
215. distance: 0
216. })
217. .onActionStart(() => {
218. this.dragItem = item;
219. this.dragRefOffsetx = 0;
220. this.dragRefOffsety = 0;
221. })
222. .onActionUpdate((event: GestureEvent) => {
223. this.offsetY = event.offsetY - this.dragRefOffsety;
224. this.offsetX = event.offsetX - this.dragRefOffsetx;

226. this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
227. let index = this.numbers.indexOf(this.dragItem);
228. if (this.offsetY >= this.FIX_VP_Y / 2 &&
229. (this.offsetX <= this.FIX_VP_X / 2 && this.offsetX >= -this.FIX_VP_X / 2)
230. && (index + this.row <= this.lastIndex)) {
231. // Slide down
232. this.down(index);
233. } else if (this.offsetY <= -this.FIX_VP_Y / 2 &&
234. (this.offsetX <= this.FIX_VP_X / 2 && this.offsetX >= -this.FIX_VP_X / 2)
235. && index - this.row >= 0) {
236. // Slide up
237. this.up(index);
238. } else if (this.offsetX >= this.FIX_VP_X / 2 &&
239. (this.offsetY <= this.FIX_VP_Y / 2 && this.offsetY >= -this.FIX_VP_Y / 2)
240. && !(((index - (this.row - 1)) % this.row === 0) || index === this.lastIndex)) {
241. // ) {
242. // Slide right
243. this.right(index);
244. } else if (this.offsetX <= -this.FIX_VP_X / 2 &&
245. (this.offsetY <= this.FIX_VP_Y / 2 && this.offsetY >= -this.FIX_VP_Y / 2)
246. && !(index % this.row === 0)) {
247. // Slide left
248. this.left(index);
249. } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
250. && ((index + this.row + 1 <= this.lastIndex && !((index - (this.row - 1)) % this.row === 0)) ||
251. !((index - (this.row - 1)) % this.row === 0))) {
252. // Slide bottom right
253. this.lowerRight(index);
254. } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2
255. && !((index - this.row < 0) || ((index - (this.row - 1)) % this.row === 0))) {
256. // Slide top right
257. this.upperRight(index);
258. } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
259. && (!(index % this.row === 0) && (index + (this.row - 1) <= this.lastIndex))) {
260. // Slide bottom left
261. this.lowerLeft(index);
262. } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2
263. && !((index <= this.row - 1) || (index % this.row === 0))) {
264. // Slide top left
265. this.upperLeft(index);
266. } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
267. && (index === this.lastIndex)) {
268. // Slide right down (bottom right is empty)
269. this.down2(index);
270. }
271. });
272. })
273. .onActionEnd(() => {
274. this.getUIContext().animateTo({
275. curve: curves.interpolatingSpring(0, 1, 400, 38)
276. }, () => {
277. this.dragItem = -1;
278. });
279. this.getUIContext().animateTo({
280. curve: curves.interpolatingSpring(14, 1, 170, 17),
281. delay: 150
282. }, () => {
283. this.scaleItem = -1;
284. });
285. })
286. )
287. .onCancel(() => {
288. this.getUIContext().animateTo({
289. curve: curves.interpolatingSpring(0, 1, 400, 38)
290. }, () => {
291. this.dragItem = -1;
292. });
293. this.getUIContext().animateTo({
294. curve: curves.interpolatingSpring(14, 1, 170, 17)
295. }, () => {
296. this.scaleItem = -1;
297. });
298. })
299. )
300. }, (item: number) => item.toString())
301. }
302. .width('90%')
303. .editMode(true)
304. .scrollBar(BarState.Off)
305. // Multiple columns
306. .columnsTemplate(this.str)
307. }
308. .width('100%')
309. .height('100%')
310. .backgroundColor('#0D182431')
311. .padding({ top: 5 })
312. }
313. }
```

[ReplaceDefaultTimeSet.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ReplaceDefaultTimeSet.ets#L21-L333)

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/voLRAcmqSgCZ-E6yCDRTlQ/zh-cn_image_0000002194158820.png?HW-CC-KV=V1&HW-CC-Date=20260428T002617Z&HW-CC-Expire=86400&HW-CC-Sign=CC1B62CBAE34FA66A730227B4BB5E6A24AB827F58C9D31A4A8E797F1E5CF5D20 "点击放大")
