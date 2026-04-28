---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-foldsplitcontainer
title: FoldSplitContainer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > FoldSplitContainer
category: harmonyos-references
scraped_at: 2026-04-28T08:02:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b63a44df81f938f25eb096e0b6ccca58c5fdfff59f64ad7bfe88010e0cdf1d4a
---

FoldSplitContainer分栏布局，实现折叠屏二分栏、三分栏在展开态、悬停态以及折叠态的区域控制。

说明

* 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 窗口宽度小于等于600vp时默认使用二分栏，窗口宽度大于600vp时在上下分栏的同时可支持扩展区域，窗口宽度大于600vp且在横屏半折状态下可触发悬停态布局。悬停态布局时会增加折痕区的避让并且扩展区域不可以贯穿折痕区，悬停态可设置不展示扩展区域，详情请参考[示例](ohos-arkui-advanced-foldsplitcontainer.md#示例)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FoldSplitContainer } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## FoldSplitContainer

PhonePC/2in1TabletTVWearable

FoldSplitContainer({primary: Callback<void>, secondary: Callback<void>, extra?: Callback<void>, expandedLayoutOptions: ExpandedRegionLayoutOptions, hoverModeLayoutOptions: HoverModeRegionLayoutOptions, foldedLayoutOptions: FoldedRegionLayoutOptions, animationOptions?: AnimateParam | null, onHoverStatusChange?: OnHoverStatusChangeHandler})

实现折叠屏二分栏、三分栏在展开态、悬停态以及折叠态的区域控制的分栏布局。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| primary | Callback<void> | 是 | @BuilderParam | 主要区域回调函数。 |
| secondary | Callback<void> | 是 | @BuilderParam | 次要区域回调函数。 |
| extra | Callback<void> | 否 | @BuilderParam | 扩展区域回调函数，不传入的情况，没有对应区域。 |
| expandedLayoutOptions | [ExpandedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#expandedregionlayoutoptions) | 是 | @Prop | 展开态布局信息。 |
| hoverModeLayoutOptions | [HoverModeRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#hovermoderegionlayoutoptions) | 是 | @Prop | 悬停态布局信息。 |
| foldedLayoutOptions | [FoldedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#foldedregionlayoutoptions) | 是 | @Prop | 折叠态布局信息。 |
| animationOptions | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | null | 否 | @Prop | 设置动画效果相关的参数，null表示关闭动效。 |
| onHoverStatusChange | [OnHoverStatusChangeHandler](ohos-arkui-advanced-foldsplitcontainer.md#onhoverstatuschangehandler) | 否 | - | 折叠屏进入或退出悬停模式时触发的回调函数。 |

## ExpandedRegionLayoutOptions

PhonePC/2in1TabletTVWearable

展开态布局信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isExtraRegionPerpendicular | boolean | 否 | 是 | 设置为true时，扩展区域从上到下贯穿整个组件；设置为false时，扩展区域不贯穿整个组件。此字段仅在extra有效时生效。  默认值：true |
| verticalSplitRatio | number | 否 | 是 | 主要区域与次要区域之间的高度比例。  默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_1V1 |
| horizontalSplitRatio | number | 否 | 是 | 主要区域与扩展区域之间的宽度比例。此字段在extra有效时生效。  默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_3V2 |
| extraRegionPosition | [ExtraRegionPosition](ohos-arkui-advanced-foldsplitcontainer.md#extraregionposition) | 否 | 是 | 扩展区域的位置信息。当isExtraRegionPerpendicular设置为false时，此字段生效。  默认值：ExtraRegionPosition.top |

## HoverModeRegionLayoutOptions

PhonePC/2in1TabletTVWearable

悬停态布局信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showExtraRegion | boolean | 否 | 是 | 可折叠屏幕在半折叠状态下是否显示扩展区域。设置为true时表示显示扩展区域，设置为false时表示不显示扩展区域。  默认值：false |
| horizontalSplitRatio | number | 否 | 是 | 主要区域与扩展区域之间的宽度比例，当且仅当extra有效时此字段才生效。  默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_3V2 |
| extraRegionPosition | [ExtraRegionPosition](ohos-arkui-advanced-foldsplitcontainer.md#extraregionposition) | 否 | 是 | 扩展区域的位置信息，当且仅当showExtraRegion设置为true时此字段才生效。  默认值：ExtraRegionPosition.top |

说明

1.在悬停状态下，设备存在避让区域，布局计算时需考虑该区域的影响。

2.在悬停模式下，屏幕上半部分为显示区域，下半部分为操作区域。

## FoldedRegionLayoutOptions

PhonePC/2in1TabletTVWearable

折叠态布局信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| verticalSplitRatio | number | 否 | 是 | 主要区域与次要区域之间的高度比例。默认值：[PresetSplitRatio](ohos-arkui-advanced-foldsplitcontainer.md#presetsplitratio).LAYOUT\_1V1 |

## OnHoverStatusChangeHandler

PhonePC/2in1TabletTVWearable

type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void

onHoverStatusChange事件处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | [HoverModeStatus](ohos-arkui-advanced-foldsplitcontainer.md#hovermodestatus) | 是 | 折叠屏进入或退出悬停模式时触发的回调函数。 |

## HoverModeStatus

PhonePC/2in1TabletTVWearable

设备或应用的折叠、旋转、窗口状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| foldStatus | [display.FoldStatus](js-apis-display.md#foldstatus10) | 否 | 否 | 设备的折叠状态。 |
| isHoverMode | boolean | 否 | 否 | app当前是否处于悬停态。设置为true时表示当前为悬停态，设置为false时表示当前为非悬停态。 |
| appRotation | number | 否 | 否 | 应用旋转角度。 |
| windowStatusType | [window.WindowStatusType](arkts-apis-window-e.md#windowstatustype11) | 否 | 否 | 窗口模式。 |

## ExtraRegionPosition

PhonePC/2in1TabletTVWearable

扩展区域位置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 1 | 扩展区域在组件上半区域。 |
| BOTTOM | 2 | 扩展区域在组件下半区域。 |

## PresetSplitRatio

PhonePC/2in1TabletTVWearable

区域比例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LAYOUT\_1V1 | 1 | 1:1比例。 |
| LAYOUT\_3V2 | 1.5 | 3:2比例。 |
| LAYOUT\_2V3 | 0.6666666666666666 | 2:3比例。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置二分栏）

该示例实现了折叠屏二分栏在展开态、悬停态以及折叠态的区域控制。

```
1. import { FoldSplitContainer } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TwoColumns {
6. @Builder
7. privateRegion() {
8. Text("Primary")
9. .backgroundColor('rgba(255, 0, 0, 0.1)')
10. .fontSize(28)
11. .textAlign(TextAlign.Center)
12. .height('100%')
13. .width('100%')
14. }

16. @Builder
17. secondaryRegion() {
18. Text("Secondary")
19. .backgroundColor('rgba(0, 255, 0, 0.1)')
20. .fontSize(28)
21. .textAlign(TextAlign.Center)
22. .height('100%')
23. .width('100%')
24. }

26. build() {
27. RelativeContainer() {
28. FoldSplitContainer({
29. primary: () => {
30. this.privateRegion()
31. },
32. secondary: () => {
33. this.secondaryRegion()
34. }
35. })
36. }
37. .height('100%')
38. .width('100%')
39. }
40. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |

### 示例2（设置三分栏）

该示例实现了折叠屏三分栏在展开态、悬停态以及折叠态的区域控制。

```
1. import { FoldSplitContainer } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ThreeColumns {
6. @Builder
7. privateRegion() {
8. Text("Primary")
9. .backgroundColor('rgba(255, 0, 0, 0.1)')
10. .fontSize(28)
11. .textAlign(TextAlign.Center)
12. .height('100%')
13. .width('100%')
14. }

16. @Builder
17. secondaryRegion() {
18. Text("Secondary")
19. .backgroundColor('rgba(0, 255, 0, 0.1)')
20. .fontSize(28)
21. .textAlign(TextAlign.Center)
22. .height('100%')
23. .width('100%')
24. }

26. @Builder
27. extraRegion() {
28. Text("Extra")
29. .backgroundColor('rgba(0, 0, 255, 0.1)')
30. .fontSize(28)
31. .textAlign(TextAlign.Center)
32. .height('100%')
33. .width('100%')
34. }

36. build() {
37. RelativeContainer() {
38. FoldSplitContainer({
39. primary: () => {
40. this.privateRegion()
41. },
42. secondary: () => {
43. this.secondaryRegion()
44. },
45. extra: () => {
46. this.extraRegion()
47. }
48. })
49. }
50. .height('100%')
51. .width('100%')
52. }
53. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |

### 示例3（展开态布局信息）

该示例通过配置ExpandedRegionLayoutOptions实现折叠屏展开态的布局信息。

```
1. import {
2. FoldSplitContainer,
3. PresetSplitRatio,
4. ExtraRegionPosition,
5. ExpandedRegionLayoutOptions,
6. HoverModeRegionLayoutOptions,
7. FoldedRegionLayoutOptions
8. } from '@kit.ArkUI';

10. @Component
11. struct Region {
12. @Prop title: string;
13. @BuilderParam content: () => void;
14. @Prop compBackgroundColor: string;

16. build() {
17. Column({ space: 8 }) {
18. Text(this.title)
19. .fontSize("24fp")
20. .fontWeight(600)

22. Scroll() {
23. this.content()
24. }
25. .layoutWeight(1)
26. .width("100%")
27. }
28. .backgroundColor(this.compBackgroundColor)
29. .width("100%")
30. .height("100%")
31. .padding(12)
32. }
33. }

35. const noop = () => {
36. };

38. @Component
39. struct SwitchOption {
40. @Prop label: string = ""
41. @Prop value: boolean = false
42. public onChange: (checked: boolean) => void = noop;

44. build() {
45. Row() {
46. Text(this.label)
47. Blank()
48. Toggle({ type: ToggleType.Switch, isOn: this.value })
49. .onChange((isOn) => {
50. this.onChange(isOn);
51. })
52. }
53. .backgroundColor(Color.White)
54. .borderRadius(8)
55. .padding(8)
56. .width("100%")
57. }
58. }

60. interface RadioOptions {
61. label: string;
62. value: Object | undefined | null;
63. onChecked: () => void;
64. }

66. @Component
67. struct RadioOption {
68. @Prop label: string;
69. @Prop value: Object | undefined | null;
70. @Prop options: Array<RadioOptions>;

72. build() {
73. Row() {
74. Text(this.label)
75. Blank()
76. Column({ space: 4 }) {
77. ForEach(this.options, (option: RadioOptions) => {
78. Row() {
79. Radio({
80. group: this.label,
81. value: JSON.stringify(option.value),
82. })
83. .checked(this.value === option.value)
84. .onChange((checked) => {
85. if (checked) {
86. option.onChecked();
87. }
88. })
89. Text(option.label)
90. }
91. })
92. }
93. .alignItems(HorizontalAlign.Start)
94. }
95. .alignItems(VerticalAlign.Top)
96. .backgroundColor(Color.White)
97. .borderRadius(8)
98. .padding(8)
99. .width("100%")
100. }
101. }

103. @Entry
104. @Component
105. struct Index {
106. @State expandedRegionLayoutOptions: ExpandedRegionLayoutOptions = {
107. horizontalSplitRatio: PresetSplitRatio.LAYOUT_3V2,
108. verticalSplitRatio: PresetSplitRatio.LAYOUT_1V1,
109. isExtraRegionPerpendicular: true,
110. extraRegionPosition: ExtraRegionPosition.TOP
111. };
112. @State foldingRegionLayoutOptions: HoverModeRegionLayoutOptions = {
113. horizontalSplitRatio: PresetSplitRatio.LAYOUT_3V2,
114. showExtraRegion: false,
115. extraRegionPosition: ExtraRegionPosition.TOP
116. };
117. @State foldedRegionLayoutOptions: FoldedRegionLayoutOptions = {
118. verticalSplitRatio: PresetSplitRatio.LAYOUT_1V1
119. };

121. @Builder
122. MajorRegion() {
123. Region({
124. title: "折叠态配置",
125. compBackgroundColor: "rgba(255, 0, 0, 0.1)",
126. }) {
127. Column({ space: 4 }) {
128. RadioOption({
129. label: "折叠态垂直高度比",
130. value: this.foldedRegionLayoutOptions.verticalSplitRatio,
131. options: [
132. {
133. label: "1:1",
134. value: PresetSplitRatio.LAYOUT_1V1,
135. onChecked: () => {
136. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_1V1
137. }
138. },
139. {
140. label: "2:3",
141. value: PresetSplitRatio.LAYOUT_2V3,
142. onChecked: () => {
143. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_2V3
144. }
145. },
146. {
147. label: "3:2",
148. value: PresetSplitRatio.LAYOUT_3V2,
149. onChecked: () => {
150. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_3V2
151. }
152. },
153. {
154. label: "未定义",
155. value: undefined,
156. onChecked: () => {
157. this.foldedRegionLayoutOptions.verticalSplitRatio = undefined
158. }
159. }
160. ]
161. })
162. }
163. .constraintSize({ minHeight: "100%" })
164. }
165. }

167. @Builder
168. MinorRegion() {
169. Region({
170. title: "悬停态配置",
171. compBackgroundColor: "rgba(0, 255, 0, 0.1)"
172. }) {
173. Column({ space: 4 }) {
174. RadioOption({
175. label: "悬停态水平宽度比",
176. value: this.foldingRegionLayoutOptions.horizontalSplitRatio,
177. options: [
178. {
179. label: "1:1",
180. value: PresetSplitRatio.LAYOUT_1V1,
181. onChecked: () => {
182. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_1V1
183. }
184. },
185. {
186. label: "2:3",
187. value: PresetSplitRatio.LAYOUT_2V3,
188. onChecked: () => {
189. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_2V3
190. }
191. },
192. {
193. label: "3:2",
194. value: PresetSplitRatio.LAYOUT_3V2,
195. onChecked: () => {
196. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_3V2
197. }
198. },
199. {
200. label: "未定义",
201. value: undefined,
202. onChecked: () => {
203. this.foldingRegionLayoutOptions.horizontalSplitRatio = undefined
204. }
205. },
206. ]
207. })

209. SwitchOption({
210. label: "悬停态是否显示扩展区",
211. value: this.foldingRegionLayoutOptions.showExtraRegion,
212. onChange: (checked) => {
213. this.foldingRegionLayoutOptions.showExtraRegion = checked;
214. }
215. })

217. if (this.foldingRegionLayoutOptions.showExtraRegion) {
218. RadioOption({
219. label: "悬停态扩展区位置",
220. value: this.foldingRegionLayoutOptions.extraRegionPosition,
221. options: [
222. {
223. label: "顶部",
224. value: ExtraRegionPosition.TOP,
225. onChecked: () => {
226. this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
227. }
228. },
229. {
230. label: "底部",
231. value: ExtraRegionPosition.BOTTOM,
232. onChecked: () => {
233. this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
234. }
235. },
236. {
237. label: "未定义",
238. value: undefined,
239. onChecked: () => {
240. this.foldingRegionLayoutOptions.extraRegionPosition = undefined
241. }
242. },
243. ]
244. })
245. }
246. }
247. .constraintSize({ minHeight: "100%" })
248. }
249. }

251. @Builder
252. ExtraRegion() {
253. Region({
254. title: "展开态配置",
255. compBackgroundColor: "rgba(0, 0, 255, 0.1)"
256. }) {
257. Column({ space: 4 }) {
258. RadioOption({
259. label: "展开态水平宽度比",
260. value: this.expandedRegionLayoutOptions.horizontalSplitRatio,
261. options: [
262. {
263. label: "1:1",
264. value: PresetSplitRatio.LAYOUT_1V1,
265. onChecked: () => {
266. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_1V1
267. }
268. },
269. {
270. label: "2:3",
271. value: PresetSplitRatio.LAYOUT_2V3,
272. onChecked: () => {
273. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_2V3
274. }
275. },
276. {
277. label: "3:2",
278. value: PresetSplitRatio.LAYOUT_3V2,
279. onChecked: () => {
280. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_3V2
281. }
282. },
283. {
284. label: "未定义",
285. value: undefined,
286. onChecked: () => {
287. this.expandedRegionLayoutOptions.horizontalSplitRatio = undefined
288. }
289. },
290. ]
291. })

293. RadioOption({
294. label: "展开态垂直高度比",
295. value: this.expandedRegionLayoutOptions.verticalSplitRatio,
296. options: [
297. {
298. label: "1:1",
299. value: PresetSplitRatio.LAYOUT_1V1,
300. onChecked: () => {
301. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_1V1
302. }
303. },
304. {
305. label: "2:3",
306. value: PresetSplitRatio.LAYOUT_2V3,
307. onChecked: () => {
308. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_2V3
309. }
310. },
311. {
312. label: "3:2",
313. value: PresetSplitRatio.LAYOUT_3V2,
314. onChecked: () => {
315. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_3V2
316. }
317. },
318. {
319. label: "未定义",
320. value: undefined,
321. onChecked: () => {
322. this.expandedRegionLayoutOptions.verticalSplitRatio = undefined
323. }
324. }
325. ]
326. })

328. SwitchOption({
329. label: "展开态扩展区是否上下贯穿",
330. value: this.expandedRegionLayoutOptions.isExtraRegionPerpendicular,
331. onChange: (checked) => {
332. this.expandedRegionLayoutOptions.isExtraRegionPerpendicular = checked;
333. }
334. })

336. if (!this.expandedRegionLayoutOptions.isExtraRegionPerpendicular) {
337. RadioOption({
338. label: "展开态扩展区位置",
339. value: this.expandedRegionLayoutOptions.extraRegionPosition,
340. options: [
341. {
342. label: "顶部",
343. value: ExtraRegionPosition.TOP,
344. onChecked: () => {
345. this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
346. }
347. },
348. {
349. label: "底部",
350. value: ExtraRegionPosition.BOTTOM,
351. onChecked: () => {
352. this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
353. }
354. },
355. {
356. label: "未定义",
357. value: undefined,
358. onChecked: () => {
359. this.expandedRegionLayoutOptions.extraRegionPosition = undefined
360. }
361. },
362. ]
363. })
364. }
365. }
366. .constraintSize({ minHeight: "100%" })
367. }
368. }

370. build() {
371. Column() {
372. FoldSplitContainer({
373. primary: () => {
374. this.MajorRegion()
375. },
376. secondary: () => {
377. this.MinorRegion()
378. },
379. extra: () => {
380. this.ExtraRegion()
381. },
382. expandedLayoutOptions: this.expandedRegionLayoutOptions,
383. hoverModeLayoutOptions: this.foldingRegionLayoutOptions,
384. foldedLayoutOptions: this.foldedRegionLayoutOptions,
385. })
386. }
387. .width("100%")
388. .height("100%")
389. }
390. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |
| - |  |  |
| - |  |  |
