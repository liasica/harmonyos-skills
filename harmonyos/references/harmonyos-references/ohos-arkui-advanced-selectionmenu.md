---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu
title: SelectionMenu
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SelectionMenu
category: harmonyos-references
scraped_at: 2026-04-29T13:53:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7c0973921f407af94fea69b19b0664d12fb78eb219edb0b1969366069e1d0def
---

文本选择菜单，适用于[RichEditor](ts-basic-components-richeditor.md)组件通过[bindSelectionMenu](ts-basic-components-richeditor.md#bindselectionmenu)或[Text](ts-basic-components-text.md)组件通过[bindSelectionMenu](ts-basic-components-text.md#bindselectionmenu11)绑定自定义文本选择菜单，建议绑定鼠标右键或者鼠标选中方式弹出，不支持作为普通组件单独使用。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SelectionMenu, EditorMenuOptions, ExpandedMenuOptions, EditorEventInfo, SelectionMenuOptions } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无。

## SelectionMenu

PhonePC/2in1TabletTVWearable

SelectionMenu(options: SelectionMenuOptions): void

入参为空时，文本选择菜单组件SelectionMenu内容区大小及组件大小为零。表现例如，富文本组件[RichEditor](ts-basic-components-richeditor.md)使用[bindSelectionMenu](ts-basic-components-richeditor.md#bindselectionmenu)接口绑定一个SelectionMenu的右键菜单，则右键富文本组件区域时无任何菜单弹出。

**装饰器类型：**@Builder

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常， 异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SelectionMenuOptions](ohos-arkui-advanced-selectionmenu.md#selectionmenuoptions) | 是 | 文本选择菜单可选项。 |

## SelectionMenuOptions

PhonePC/2in1TabletTVWearable

SelectionMenuOptions定义SelectionMenu的可选菜单类型项及其具体配置参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| editorMenuOptions | Array<[EditorMenuOptions](ohos-arkui-advanced-selectionmenu.md#editormenuoptions)> | 否 | 是 | 编辑菜单。  editorMenuOptions未配置时，不显示编辑菜单。  同时配置EditorMenuOptions中action和builder时，点击图标会同时响应。  点击编辑菜单图标默认不关闭整个菜单，应用可以通过action接口配置RichEditorController的closeSelectionMenu主动关闭菜单。 |
| expandedMenuOptions | Array<[ExpandedMenuOptions](ohos-arkui-advanced-selectionmenu.md#expandedmenuoptions)> | 否 | 是 | 扩展下拉菜单。  expandedMenuOptions参数为空时无更多按钮，不显示扩展下拉菜单。  expandedMenuOptions参数不为空时显示更多按钮，配置菜单项收起在更多按钮中，点击更多按钮展示。 |
| controller | [RichEditorController](ts-basic-components-richeditor.md#richeditorcontroller) | 否 | 是 | 富文本控制器不为空时显示默认系统菜单（包含剪切复制粘贴等部分）且默认菜单功能内置。  controller为空时不显示更多按钮，expandedMenuOptions参数不为空则显示下拉菜单中。  系统默认只支持复制粘贴富文本文本内容，图文混排需要应用自定义onCopy、onPaste接口。应用自行配置onCopy | onPaste接口时，系统菜单默认复制粘贴失效，调用应用自定义函数。  **说明：**  点击自定义文本选择菜单内置复制功能选项后，自定义菜单消失选中文本高亮保留。  点击自定义文本选择菜单内置全选功能选项后，自定义菜单消失文本全选高亮。  点击自定义文本选择菜单内置粘贴功能选项后，空白处粘贴或者选中文本替换粘贴均是保留被复制文本的样式。  当富文本组件[RichEditor](ts-basic-components-richeditor.md)的copyOptions属性设置为CopyOptions.None时，内置的复制剪切功能不会被限制。 |
| onCopy | (event?: [EditorEventInfo](ohos-arkui-advanced-selectionmenu.md#editoreventinfo)) => void | 否 | 是 | 替代内置系统菜单复制项的事件回调。  生效前提是一定要有controller参数，有系统默认菜单才能替换内置复制功能。  **说明：**  event为返回信息。 |
| onPaste | (event?: [EditorEventInfo](ohos-arkui-advanced-selectionmenu.md#editoreventinfo)) => void | 否 | 是 | 替代内置系统菜单粘贴项的事件回调。  生效前提是一定要有controller参数，有系统默认菜单才能替换内置粘贴功能。  **说明：**  event为返回信息。 |
| onCut | (event?: [EditorEventInfo](ohos-arkui-advanced-selectionmenu.md#editoreventinfo)) => void | 否 | 是 | 替代内置系统菜单剪切项的事件回调。  生效前提是一定要有controller参数，有系统默认菜单才能替换内置剪切功能。  **说明：**  event为返回信息。 |
| onSelectAll | (event?: [EditorEventInfo](ohos-arkui-advanced-selectionmenu.md#editoreventinfo)) => void | 否 | 是 | 替代内置系统菜单全选项的事件回调。  生效前提是一定要有controller参数，有系统默认菜单才能替换内置全选功能。  **说明：**  event为返回信息。 |

## EditorMenuOptions

PhonePC/2in1TabletTVWearable

编辑菜单选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图标资源。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| builder | () => void | 否 | 是 | 点击时显示用户自定义组件，自定义组件在构造时结合@Builder使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 点击菜单项的事件回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](ts-universal-attributes-text-style.md#symbolglyphmodifier12) | 否 | 是 | Symbol图标资源，优先级大于icon。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## ExpandedMenuOptions

PhonePC/2in1TabletTVWearable

扩展下拉菜单。

继承于[MenuItemOptions](ts-basic-components-menuitem.md#menuitemoptions对象说明)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | () => void | 否 | 是 | 点击菜单项的事件回调。 |

## EditorEventInfo

PhonePC/2in1TabletTVWearable

选中内容信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [RichEditorSelection](ts-basic-components-richeditor.md#richeditorselection) | 否 | 是 | 选中内容信息。 |

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)，宽度默认224vp， 高度自适应内容。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（绑定不同触发方式的自定义文本选择菜单）

该示例展示了文本绑定不同触发方式的自定义文本选择菜单的效果。

```
1. import {
2. SelectionMenu,
3. EditorMenuOptions,
4. ExpandedMenuOptions,
5. EditorEventInfo,
6. SelectionMenuOptions
7. } from '@kit.ArkUI';

9. @Entry
10. @Component
11. struct Index {
12. @State select: boolean = true;
13. controller: RichEditorController = new RichEditorController();
14. options: RichEditorOptions = { controller: this.controller };
15. @State message: string = 'Hello world';
16. @State textSize: number = 30;
17. @State fontWeight: FontWeight = FontWeight.Normal;
18. @State start: number = -1;
19. @State end: number = -1;
20. @State visibleValue: Visibility = Visibility.Visible;
21. @State colorTransparent: Color = Color.Transparent;
22. @State textStyle: RichEditorTextStyle = {};
23. private editorMenuOptions: Array<EditorMenuOptions> =
24. [
25. {
26. // $r('app.media.ic_notepad_textbold')需要替换为开发者所需的图像资源文件。
27. icon: $r("app.media.ic_notepad_textbold"), action: () => {
28. if (this.controller) {
29. let selection = this.controller.getSelection();
30. let spans = selection.spans;
31. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
32. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
33. let span = item as RichEditorTextSpanResult;
34. this.textStyle = span.textStyle;
35. let start = span.offsetInSpan[0];
36. let end = span.offsetInSpan[1];
37. let offset = span.spanPosition.spanRange[0];
38. if (this.textStyle.fontWeight != 11) {
39. this.textStyle.fontWeight = FontWeight.Bolder;
40. } else {
41. this.textStyle.fontWeight = FontWeight.Normal;
42. }
43. this.controller.updateSpanStyle({
44. start: offset + start,
45. end: offset + end,
46. textStyle: this.textStyle
47. })
48. }
49. })
50. }
51. }
52. },
53. {
54. // $r('app.media.ic_notepad_texttilt')需要替换为开发者所需的图像资源文件。
55. icon: $r("app.media.ic_notepad_texttilt"), action: () => {
56. if (this.controller) {
57. let selection = this.controller.getSelection();
58. let spans = selection.spans;
59. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
60. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
61. let span = item as RichEditorTextSpanResult;
62. this.textStyle = span.textStyle;
63. let start = span.offsetInSpan[0];
64. let end = span.offsetInSpan[1];
65. let offset = span.spanPosition.spanRange[0];
66. if (this.textStyle.fontStyle == FontStyle.Italic) {
67. this.textStyle.fontStyle = FontStyle.Normal;
68. } else {
69. this.textStyle.fontStyle = FontStyle.Italic;
70. }
71. this.controller.updateSpanStyle({
72. start: offset + start,
73. end: offset + end,
74. textStyle: this.textStyle
75. })
76. }
77. })
78. }
79. }
80. },
81. {
82. // $r('app.media.ic_notepad_underline')需要替换为开发者所需的图像资源文件。
83. icon: $r("app.media.ic_notepad_underline"),
84. action: () => {
85. if (this.controller) {
86. let selection = this.controller.getSelection();
87. let spans = selection.spans;
88. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
89. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
90. let span = item as RichEditorTextSpanResult;
91. this.textStyle = span.textStyle;
92. let start = span.offsetInSpan[0];
93. let end = span.offsetInSpan[1];
94. let offset = span.spanPosition.spanRange[0];
95. if (this.textStyle.decoration) {
96. if (this.textStyle.decoration.type == TextDecorationType.Underline) {
97. this.textStyle.decoration.type = TextDecorationType.None;
98. } else {
99. this.textStyle.decoration.type = TextDecorationType.Underline;
100. }
101. } else {
102. this.textStyle.decoration = { type: TextDecorationType.Underline, color: Color.Black }
103. }
104. this.controller.updateSpanStyle({
105. start: offset + start,
106. end: offset + end,
107. textStyle: this.textStyle
108. })
109. }
110. })
111. }
112. }
113. },
114. {
115. // $r('app.media.ic_notepad_fontsize')需要替换为开发者所需的图像资源文件。
116. icon: $r("app.media.ic_notepad_fontsize"), action: () => {
117. }, builder: (): void => this.sliderPanel()
118. },
119. {
120. // $r('app.media.ic_notepad_textcolor')需要替换为开发者所需的图像资源文件。
121. icon: $r("app.media.ic_notepad_textcolor"), action: () => {
122. if (this.controller) {
123. let selection = this.controller.getSelection();
124. let spans = selection.spans;
125. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
126. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
127. let span = item as RichEditorTextSpanResult;
128. this.textStyle = span.textStyle;
129. let start = span.offsetInSpan[0];
130. let end = span.offsetInSpan[1];
131. let offset = span.spanPosition.spanRange[0];
132. if (this.textStyle.fontColor == Color.Orange || this.textStyle.fontColor == '#FFFFA500') {
133. this.textStyle.fontColor = Color.Black;
134. } else {
135. this.textStyle.fontColor = Color.Orange;
136. }
137. this.controller.updateSpanStyle({
138. start: offset + start,
139. end: offset + end,
140. textStyle: this.textStyle
141. })
142. }
143. })
144. }
145. }
146. }]
147. private expandedMenuOptions: Array<ExpandedMenuOptions> =
148. [{
149. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
150. startIcon: $r("app.media.startIcon"), content: '词典', action: () => {
151. }
152. }, {
153. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
154. startIcon: $r("app.media.startIcon"), content: '翻译', action: () => {
155. }
156. }, {
157. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
158. startIcon: $r("app.media.startIcon"), content: '搜索', action: () => {
159. }
160. }]
161. private expandedMenuOptions1: Array<ExpandedMenuOptions> = [];
162. private selectionMenuOptions: SelectionMenuOptions = {
163. editorMenuOptions: this.editorMenuOptions,
164. expandedMenuOptions: this.expandedMenuOptions,
165. controller: this.controller,
166. onCut: (event?: EditorEventInfo) => {
167. if (event && event.content) {
168. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
169. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
170. let span = item as RichEditorTextSpanResult;
171. console.info('test cut' + span.value);
172. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
173. }
174. })
175. }
176. },
177. onPaste: (event?: EditorEventInfo) => {
178. if (event && event.content) {
179. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
180. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
181. let span = item as RichEditorTextSpanResult;
182. console.info('test onPaste' + span.value);
183. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
184. }
185. })
186. }
187. },
188. onCopy: (event?: EditorEventInfo) => {
189. if (event && event.content) {
190. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
191. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
192. let span = item as RichEditorTextSpanResult;
193. console.info('test cut' + span.value);
194. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
195. }
196. })
197. }
198. },
199. onSelectAll: (event?: EditorEventInfo) => {
200. if (event && event.content) {
201. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
202. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
203. let span = item as RichEditorTextSpanResult;
204. console.info('test onPaste' + span.value);
205. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
206. }
207. })
208. }
209. }
210. };

212. @Builder
213. sliderPanel() {
214. Column() {
215. Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
216. Text('A').fontSize(15)
217. Slider({ value: this.textSize, step: 10, style: SliderStyle.InSet })
218. .width(210)
219. .onChange((value: number, mode: SliderChangeMode) => {
220. if (this.controller) {
221. let selection = this.controller.getSelection();
222. if (mode == SliderChangeMode.End) {
223. if (this.textSize == undefined) {
224. this.textSize = 0;
225. }
226. let spans = selection.spans;
227. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
228. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
229. this.textSize = Math.max(this.textSize, (item as RichEditorTextSpanResult).textStyle.fontSize);
230. }
231. })
232. }
233. if (mode == SliderChangeMode.Moving || mode == SliderChangeMode.Click) {
234. this.start = selection.selection[0];
235. this.end = selection.selection[1];
236. this.textSize = value;
237. this.controller.updateSpanStyle({
238. start: this.start,
239. end: this.end,
240. textStyle: { fontSize: this.textSize }
241. })
242. }
243. }
244. })
245. Text('A').fontSize(20).fontWeight(FontWeight.Medium)
246. }.borderRadius($r('sys.float.ohos_id_corner_radius_card'))
247. }
248. .shadow(ShadowStyle.OUTER_DEFAULT_MD)
249. .backgroundColor(Color.White)
250. .borderRadius($r('sys.float.ohos_id_corner_radius_card'))
251. .padding(15)
252. .height(48)
253. }

255. @Builder
256. MyMenu() {
257. Column() {
258. SelectionMenu(this.selectionMenuOptions)
259. }
260. .width(256)
261. .backgroundColor(Color.Transparent)
262. }

264. @Builder
265. MyMenu2() {
266. Column() {
267. SelectionMenu({
268. editorMenuOptions: this.editorMenuOptions,
269. expandedMenuOptions: this.expandedMenuOptions1,
270. controller: this.controller,
271. })
272. }
273. .width(256)
274. .backgroundColor(Color.Transparent)
275. }

277. @Builder
278. MyMenu3() {
279. Column() {
280. SelectionMenu({
281. editorMenuOptions: this.editorMenuOptions,
282. expandedMenuOptions: this.expandedMenuOptions,
283. controller: this.controller,
284. })
285. }
286. .width(256)
287. .backgroundColor(Color.Transparent)
288. }

290. build() {
291. Column() {
292. Button("SetSelection")
293. .onClick((event: ClickEvent) => {
294. if (this.controller) {
295. this.controller.setSelection(0, 2);
296. }
297. })

299. RichEditor(this.options)
300. .onReady(() => {
301. this.controller.addTextSpan(this.message, { style: { fontColor: Color.Orange, fontSize: 30 } });
302. this.controller.addTextSpan(this.message, { style: { fontColor: Color.Black, fontSize: 25 } });
303. })
304. .onSelect((value: RichEditorSelection) => {
305. if (value.selection[0] == -1 && value.selection[1] == -1) {
306. return;
307. }
308. this.start = value.selection[0];
309. this.end = value.selection[1];
310. })
311. .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu3(), RichEditorResponseType.RIGHT_CLICK)
312. .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu2(), RichEditorResponseType.SELECT)
313. .borderWidth(1)
314. .borderColor(Color.Red)
315. .width(200)
316. .height(200)
317. .margin(10)
318. }
319. }
320. }
```

说明

系统暂未预置加粗、斜体等图标，示例代码使用本地资源图标，开发者使用时需自行替换editorMenuOptions中icon项的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/zqbthCjpR3u85_kX8hNMng/zh-cn_image_0000002558606994.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=9AF8F9175DCB18D08B62491CC79ACEEB3F4053F41EBD6A58B0648FD5A4545BB7)

### 示例2（设置Symbol类型图标）

从API version 11开始，该示例通过设置[EditorMenuOptions](ohos-arkui-advanced-selectionmenu.md#editormenuoptions)的属性symbolStyle，展示了自定义Symbol类型图标。

```
1. import {
2. SelectionMenu,
3. EditorMenuOptions,
4. ExpandedMenuOptions,
5. EditorEventInfo,
6. SelectionMenuOptions,
7. SymbolGlyphModifier
8. } from '@kit.ArkUI'

10. @Entry
11. @Component
12. struct Index {
13. @State select: boolean = true;
14. controller: RichEditorController = new RichEditorController();
15. options: RichEditorOptions = { controller: this.controller };
16. @State message: string = 'Hello world';
17. @State textSize: number = 30;
18. @State fontWeight: FontWeight = FontWeight.Normal;
19. @State start: number = -1;
20. @State end: number = -1;
21. @State visibleValue: Visibility = Visibility.Visible;
22. @State colorTransparent: Color = Color.Transparent;
23. @State textStyle: RichEditorTextStyle = {};
24. private editorMenuOptions: Array<EditorMenuOptions> =
25. [
26. {
27. icon: $r("sys.media.wifi_router_fill"),
28. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.save')),
29. action: () => {
30. if (this.controller) {
31. let selection = this.controller.getSelection();
32. let spans = selection.spans;
33. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
34. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
35. let span = item as RichEditorTextSpanResult;
36. this.textStyle = span.textStyle;
37. let start = span.offsetInSpan[0];
38. let end = span.offsetInSpan[1];
39. let offset = span.spanPosition.spanRange[0];
40. if (this.textStyle.fontWeight != 11) {
41. this.textStyle.fontWeight = FontWeight.Bolder;
42. } else {
43. this.textStyle.fontWeight = FontWeight.Normal;
44. }
45. this.controller.updateSpanStyle({
46. start: offset + start,
47. end: offset + end,
48. textStyle: this.textStyle
49. })
50. }
51. })
52. }
53. }
54. },
55. {
56. icon: $r("sys.media.save_button_picture"),
57. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.camera')),
58. action: () => {
59. if (this.controller) {
60. let selection = this.controller.getSelection();
61. let spans = selection.spans;
62. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
63. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
64. let span = item as RichEditorTextSpanResult;
65. this.textStyle = span.textStyle;
66. let start = span.offsetInSpan[0];
67. let end = span.offsetInSpan[1];
68. let offset = span.spanPosition.spanRange[0];
69. if (this.textStyle.fontStyle == FontStyle.Italic) {
70. this.textStyle.fontStyle = FontStyle.Normal;
71. } else {
72. this.textStyle.fontStyle = FontStyle.Italic;
73. }
74. this.controller.updateSpanStyle({
75. start: offset + start,
76. end: offset + end,
77. textStyle: this.textStyle
78. })
79. }
80. })
81. }
82. }
83. },
84. {
85. icon: $r("sys.media.waveform_folder_fill"),
86. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.car')),
87. action: () => {
88. if (this.controller) {
89. let selection = this.controller.getSelection();
90. let spans = selection.spans;
91. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
92. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
93. let span = item as RichEditorTextSpanResult;
94. this.textStyle = span.textStyle;
95. let start = span.offsetInSpan[0];
96. let end = span.offsetInSpan[1];
97. let offset = span.spanPosition.spanRange[0];
98. if (this.textStyle.decoration) {
99. if (this.textStyle.decoration.type == TextDecorationType.Underline) {
100. this.textStyle.decoration.type = TextDecorationType.None;
101. } else {
102. this.textStyle.decoration.type = TextDecorationType.Underline;
103. }
104. } else {
105. this.textStyle.decoration = { type: TextDecorationType.Underline, color: Color.Black }
106. }
107. this.controller.updateSpanStyle({
108. start: offset + start,
109. end: offset + end,
110. textStyle: this.textStyle
111. })
112. }
113. })
114. }
115. }
116. },
117. {
118. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
119. icon: $r("app.media.app_icon"), action: () => {
120. }, builder: (): void => this.sliderPanel()
121. },
122. {
123. icon: $r("sys.media.thermometer_fill"), action: () => {
124. if (this.controller) {
125. let selection = this.controller.getSelection();
126. let spans = selection.spans;
127. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
128. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
129. let span = item as RichEditorTextSpanResult;
130. this.textStyle = span.textStyle;
131. let start = span.offsetInSpan[0];
132. let end = span.offsetInSpan[1];
133. let offset = span.spanPosition.spanRange[0];
134. if (this.textStyle.fontColor == Color.Orange || this.textStyle.fontColor == '#FFFFA500') {
135. this.textStyle.fontColor = Color.Black;
136. } else {
137. this.textStyle.fontColor = Color.Orange;
138. }
139. this.controller.updateSpanStyle({
140. start: offset + start,
141. end: offset + end,
142. textStyle: this.textStyle
143. })
144. }
145. })
146. }
147. }
148. }]
149. private expandedMenuOptions: Array<ExpandedMenuOptions> =
150. [{
151. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
152. startIcon: $r("app.media.startIcon"), content: '词典', action: () => {
153. }
154. }, {
155. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
156. startIcon: $r("app.media.startIcon"), content: '翻译', action: () => {
157. }
158. }, {
159. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
160. startIcon: $r("app.media.startIcon"), content: '搜索', action: () => {
161. }
162. }]
163. private expandedMenuOptions1: Array<ExpandedMenuOptions> = []
164. private editorMenuOptions1: Array<EditorMenuOptions> = []
165. private selectionMenuOptions: SelectionMenuOptions = {
166. editorMenuOptions: this.editorMenuOptions,
167. expandedMenuOptions: this.expandedMenuOptions,
168. controller: this.controller,
169. onCut: (event?: EditorEventInfo) => {
170. if (event && event.content) {
171. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
172. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
173. let span = item as RichEditorTextSpanResult;
174. console.info('test cut' + span.value);
175. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
176. }
177. })
178. }
179. },
180. onPaste: (event?: EditorEventInfo) => {
181. if (event && event.content) {
182. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
183. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
184. let span = item as RichEditorTextSpanResult;
185. console.info('test onPaste' + span.value);
186. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
187. }
188. })
189. }
190. },
191. onCopy: (event?: EditorEventInfo) => {
192. if (event && event.content) {
193. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
194. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
195. let span = item as RichEditorTextSpanResult;
196. console.info('test cut' + span.value);
197. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
198. }
199. })
200. }
201. },
202. onSelectAll: (event?: EditorEventInfo) => {
203. if (event && event.content) {
204. event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
205. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
206. let span = item as RichEditorTextSpanResult;
207. console.info('test onPaste' + span.value);
208. console.info('test start ' + span.offsetInSpan[0] + ' end: ' + span.offsetInSpan[1]);
209. }
210. })
211. }
212. }
213. }

215. @Builder
216. sliderPanel() {
217. Column() {
218. Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
219. Text('A').fontSize(15)
220. Slider({ value: this.textSize, step: 10, style: SliderStyle.InSet })
221. .width(210)
222. .onChange((value: number, mode: SliderChangeMode) => {
223. if (this.controller) {
224. let selection = this.controller.getSelection();
225. if (mode == SliderChangeMode.End) {
226. if (this.textSize == undefined) {
227. this.textSize = 0;
228. }
229. let spans = selection.spans;
230. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
231. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
232. this.textSize = Math.max(this.textSize, (item as RichEditorTextSpanResult).textStyle.fontSize);
233. }
234. })
235. }
236. if (mode == SliderChangeMode.Moving || mode == SliderChangeMode.Click) {
237. this.start = selection.selection[0];
238. this.end = selection.selection[1];
239. this.textSize = value;
240. this.controller.updateSpanStyle({
241. start: this.start,
242. end: this.end,
243. textStyle: { fontSize: this.textSize }
244. })
245. }
246. }
247. })
248. Text('A').fontSize(20).fontWeight(FontWeight.Medium)
249. }.borderRadius($r('sys.float.ohos_id_corner_radius_card'))
250. }
251. .shadow(ShadowStyle.OUTER_DEFAULT_MD)
252. .backgroundColor(Color.White)
253. .borderRadius($r('sys.float.ohos_id_corner_radius_card'))
254. .padding(15)
255. .height(48)
256. }

258. @Builder
259. MyMenu() {
260. Column() {
261. SelectionMenu(this.selectionMenuOptions)
262. }
263. .width(256)
264. .backgroundColor(Color.Transparent)
265. }

267. @Builder
268. MyMenu2() {
269. Column() {
270. SelectionMenu({
271. editorMenuOptions: this.editorMenuOptions,
272. expandedMenuOptions: this.expandedMenuOptions1,
273. controller: this.controller,
274. })
275. }
276. .width(256)
277. .backgroundColor(Color.Transparent)
278. }

280. @Builder
281. MyMenu3() {
282. Column() {
283. SelectionMenu({
284. editorMenuOptions: this.editorMenuOptions1,
285. expandedMenuOptions: this.expandedMenuOptions,
286. controller: this.controller,
287. })
288. }
289. .width(256)
290. .backgroundColor(Color.Transparent)
291. }

293. build() {
294. Column() {
295. Button("SetSelection")
296. .onClick((event: ClickEvent) => {
297. if (this.controller) {
298. this.controller.setSelection(0, 2);
299. }
300. })

302. RichEditor(this.options)
303. .onReady(() => {
304. this.controller.addTextSpan(this.message, { style: { fontColor: Color.Orange, fontSize: 30 } });
305. this.controller.addTextSpan(this.message, { style: { fontColor: Color.Black, fontSize: 25 } });
306. })
307. .onSelect((value: RichEditorSelection) => {
308. if (value.selection[0] == -1 && value.selection[1] == -1) {
309. return;
310. }
311. this.start = value.selection[0];
312. this.end = value.selection[1];
313. })
314. .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu3(), RichEditorResponseType.RIGHT_CLICK)
315. .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu2(), RichEditorResponseType.SELECT)
316. .borderWidth(1)
317. .borderColor(Color.Red)
318. .width(200)
319. .height(200)
320. }
321. }
322. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/1v9Z5sU-Sg6vPog4o4qzXg/zh-cn_image_0000002589326521.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=8764386DF032C7127FCFF2227EC5820D69A8A81EEEC659D73D758FDCFA7FE10C)
