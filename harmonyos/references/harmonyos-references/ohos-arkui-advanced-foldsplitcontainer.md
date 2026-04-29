---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-foldsplitcontainer
title: FoldSplitContainer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > FoldSplitContainer
category: harmonyos-references
scraped_at: 2026-04-29T13:53:00+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c524a58e69f293fdeb61f5bcd5de8639be11e529cf8290c28828d7a9e7dd9bbc
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

**装饰器类型：**[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| primary | Callback<void> | 是 | [@BuilderParam](../harmonyos-guides/arkts-builderparam.md) | 主要区域回调函数。 |
| secondary | Callback<void> | 是 | [@BuilderParam](../harmonyos-guides/arkts-builderparam.md) | 次要区域回调函数。 |
| extra | Callback<void> | 否 | [@BuilderParam](../harmonyos-guides/arkts-builderparam.md) | 扩展区域回调函数，不传入的情况，没有对应区域。 |
| expandedLayoutOptions | [ExpandedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#expandedregionlayoutoptions) | 是 | [@Prop](../harmonyos-guides/arkts-prop.md) | 展开态布局信息。 |
| hoverModeLayoutOptions | [HoverModeRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#hovermoderegionlayoutoptions) | 是 | [@Prop](../harmonyos-guides/arkts-prop.md) | 悬停态布局信息。 |
| foldedLayoutOptions | [FoldedRegionLayoutOptions](ohos-arkui-advanced-foldsplitcontainer.md#foldedregionlayoutoptions) | 是 | [@Prop](../harmonyos-guides/arkts-prop.md) | 折叠态布局信息。 |
| animationOptions | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | null | 否 | [@Prop](../harmonyos-guides/arkts-prop.md) | 设置动画效果相关的参数，null表示关闭动效。 |
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
29. // 主要区域回调函数
30. primary: () => {
31. this.privateRegion()
32. },
33. // 次要区域回调函数
34. secondary: () => {
35. this.secondaryRegion()
36. }
37. })
38. }
39. .height('100%')
40. .width('100%')
41. }
42. }
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
39. // 主要区域回调函数
40. primary: () => {
41. this.privateRegion()
42. },
43. // 次要区域回调函数
44. secondary: () => {
45. this.secondaryRegion()
46. },
47. // 扩展区域回调函数
48. extra: () => {
49. this.extraRegion()
50. }
51. })
52. }
53. .height('100%')
54. .width('100%')
55. }
56. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |

### 示例3 （FoldSplitContainer折叠态、悬停态、展开态各项配置行为展示）

该示例通过配置ExpandedRegionLayoutOptions实现折叠屏折叠态、悬停态、展开态布局信息的配置。示例代码中this.MajorRegion()，this.MinorRegion()，this.ExtraRegion()组件划分出来的主要区域，次要区域和扩展区域。这些区域使用Region为封装的区域组件（Region）实现， 其中RadioOptions为封装的切换单选框组件，SwitchOption为封装的切换开关组件。

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
106. // 展开态布局配置
107. @State expandedRegionLayoutOptions: ExpandedRegionLayoutOptions = {
108. horizontalSplitRatio: PresetSplitRatio.LAYOUT_3V2,
109. verticalSplitRatio: PresetSplitRatio.LAYOUT_1V1,
110. isExtraRegionPerpendicular: true,
111. extraRegionPosition: ExtraRegionPosition.TOP
112. };
113. // 悬停态布局配置
114. @State foldingRegionLayoutOptions: HoverModeRegionLayoutOptions = {
115. horizontalSplitRatio: PresetSplitRatio.LAYOUT_3V2,
116. showExtraRegion: false,
117. extraRegionPosition: ExtraRegionPosition.TOP
118. };
119. // 折叠态布局配置
120. @State foldedRegionLayoutOptions: FoldedRegionLayoutOptions = {
121. verticalSplitRatio: PresetSplitRatio.LAYOUT_1V1
122. };

124. @Builder
125. // 主要区域自定义组件
126. MajorRegion() {
127. Region({
128. title: "折叠态配置",
129. compBackgroundColor: "rgba(255, 0, 0, 0.1)",
130. }) {
131. Column({ space: 4 }) {
132. RadioOption({
133. label: "折叠态垂直高度比",
134. value: this.foldedRegionLayoutOptions.verticalSplitRatio,
135. options: [
136. {
137. label: "1:1",
138. value: PresetSplitRatio.LAYOUT_1V1,
139. onChecked: () => {
140. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_1V1
141. }
142. },
143. {
144. label: "2:3",
145. value: PresetSplitRatio.LAYOUT_2V3,
146. onChecked: () => {
147. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_2V3
148. }
149. },
150. {
151. label: "3:2",
152. value: PresetSplitRatio.LAYOUT_3V2,
153. onChecked: () => {
154. this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_3V2
155. }
156. },
157. {
158. label: "未定义",
159. value: undefined,
160. onChecked: () => {
161. this.foldedRegionLayoutOptions.verticalSplitRatio = undefined
162. }
163. }
164. ]
165. })
166. }
167. .constraintSize({ minHeight: "100%" })
168. }
169. }

171. @Builder
172. // 次要区域自定义组件
173. MinorRegion() {
174. Region({
175. title: "悬停态配置",
176. compBackgroundColor: "rgba(0, 255, 0, 0.1)"
177. }) {
178. Column({ space: 4 }) {
179. RadioOption({
180. label: "悬停态水平宽度比",
181. value: this.foldingRegionLayoutOptions.horizontalSplitRatio,
182. options: [
183. {
184. label: "1:1",
185. value: PresetSplitRatio.LAYOUT_1V1,
186. onChecked: () => {
187. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_1V1
188. }
189. },
190. {
191. label: "2:3",
192. value: PresetSplitRatio.LAYOUT_2V3,
193. onChecked: () => {
194. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_2V3
195. }
196. },
197. {
198. label: "3:2",
199. value: PresetSplitRatio.LAYOUT_3V2,
200. onChecked: () => {
201. this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_3V2
202. }
203. },
204. {
205. label: "未定义",
206. value: undefined,
207. onChecked: () => {
208. this.foldingRegionLayoutOptions.horizontalSplitRatio = undefined
209. }
210. },
211. ]
212. })

214. SwitchOption({
215. label: "悬停态是否显示扩展区",
216. value: this.foldingRegionLayoutOptions.showExtraRegion,
217. onChange: (checked) => {
218. this.foldingRegionLayoutOptions.showExtraRegion = checked;
219. }
220. })

222. if (this.foldingRegionLayoutOptions.showExtraRegion) {
223. RadioOption({
224. label: "悬停态扩展区位置",
225. value: this.foldingRegionLayoutOptions.extraRegionPosition,
226. options: [
227. {
228. label: "顶部",
229. value: ExtraRegionPosition.TOP,
230. onChecked: () => {
231. this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
232. }
233. },
234. {
235. label: "底部",
236. value: ExtraRegionPosition.BOTTOM,
237. onChecked: () => {
238. this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
239. }
240. },
241. {
242. label: "未定义",
243. value: undefined,
244. onChecked: () => {
245. this.foldingRegionLayoutOptions.extraRegionPosition = undefined
246. }
247. },
248. ]
249. })
250. }
251. }
252. .constraintSize({ minHeight: "100%" })
253. }
254. }

256. @Builder
257. // 扩展区域自定义组件
258. ExtraRegion() {
259. Region({
260. title: "展开态配置",
261. compBackgroundColor: "rgba(0, 0, 255, 0.1)"
262. }) {
263. Column({ space: 4 }) {
264. RadioOption({
265. label: "展开态水平宽度比",
266. value: this.expandedRegionLayoutOptions.horizontalSplitRatio,
267. options: [
268. {
269. label: "1:1",
270. value: PresetSplitRatio.LAYOUT_1V1,
271. onChecked: () => {
272. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_1V1
273. }
274. },
275. {
276. label: "2:3",
277. value: PresetSplitRatio.LAYOUT_2V3,
278. onChecked: () => {
279. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_2V3
280. }
281. },
282. {
283. label: "3:2",
284. value: PresetSplitRatio.LAYOUT_3V2,
285. onChecked: () => {
286. this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT_3V2
287. }
288. },
289. {
290. label: "未定义",
291. value: undefined,
292. onChecked: () => {
293. this.expandedRegionLayoutOptions.horizontalSplitRatio = undefined
294. }
295. },
296. ]
297. })

299. RadioOption({
300. label: "展开态垂直高度比",
301. value: this.expandedRegionLayoutOptions.verticalSplitRatio,
302. options: [
303. {
304. label: "1:1",
305. value: PresetSplitRatio.LAYOUT_1V1,
306. onChecked: () => {
307. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_1V1
308. }
309. },
310. {
311. label: "2:3",
312. value: PresetSplitRatio.LAYOUT_2V3,
313. onChecked: () => {
314. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_2V3
315. }
316. },
317. {
318. label: "3:2",
319. value: PresetSplitRatio.LAYOUT_3V2,
320. onChecked: () => {
321. this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT_3V2
322. }
323. },
324. {
325. label: "未定义",
326. value: undefined,
327. onChecked: () => {
328. this.expandedRegionLayoutOptions.verticalSplitRatio = undefined
329. }
330. }
331. ]
332. })

334. SwitchOption({
335. label: "展开态扩展区是否上下贯穿",
336. value: this.expandedRegionLayoutOptions.isExtraRegionPerpendicular,
337. onChange: (checked) => {
338. this.expandedRegionLayoutOptions.isExtraRegionPerpendicular = checked;
339. }
340. })

342. if (!this.expandedRegionLayoutOptions.isExtraRegionPerpendicular) {
343. RadioOption({
344. label: "展开态扩展区位置",
345. value: this.expandedRegionLayoutOptions.extraRegionPosition,
346. options: [
347. {
348. label: "顶部",
349. value: ExtraRegionPosition.TOP,
350. onChecked: () => {
351. this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
352. }
353. },
354. {
355. label: "底部",
356. value: ExtraRegionPosition.BOTTOM,
357. onChecked: () => {
358. this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
359. }
360. },
361. {
362. label: "未定义",
363. value: undefined,
364. onChecked: () => {
365. this.expandedRegionLayoutOptions.extraRegionPosition = undefined
366. }
367. },
368. ]
369. })
370. }
371. }
372. .constraintSize({ minHeight: "100%" })
373. }
374. }

376. build() {
377. Column() {
378. FoldSplitContainer({
379. // 主要区域回调函数
380. primary: () => {
381. this.MajorRegion()
382. },
383. // 次要区域回调函数
384. secondary: () => {
385. this.MinorRegion()
386. },
387. // 扩展区域回调函数
388. extra: () => {
389. this.ExtraRegion()
390. },
391. expandedLayoutOptions: this.expandedRegionLayoutOptions,
392. hoverModeLayoutOptions: this.foldingRegionLayoutOptions,
393. foldedLayoutOptions: this.foldedRegionLayoutOptions,
394. })
395. }
396. .width("100%")
397. .height("100%")
398. }
399. }
```

| 折叠态 | 展开态 | 悬停态 |
| --- | --- | --- |
|  |  |  |
| - |  |  |
| - |  |  |
