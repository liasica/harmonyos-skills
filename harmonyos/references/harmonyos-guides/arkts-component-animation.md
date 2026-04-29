---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-component-animation
title: 组件动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 组件动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e1a46bfd3a458f52f60c5058d32be5661b5a1dc9308d726f802cd868ef6d8bce
---

ArkUI为组件提供了通用的属性动画和转场动画能力的同时，还为一些组件提供了默认的动画效果。例如，[List](../harmonyos-references/ts-container-list.md)的滑动动效、[Button](../harmonyos-references/ts-basic-components-button.md)的点击动效，是组件自带的默认动画效果。在组件默认动画效果的基础上，开发者还可以通过属性动画和转场动画对容器组件内的子组件动效进行定制。

## 使用组件默认动画

组件默认动效具备以下功能：

* 提示用户当前状态，例如用户点击Button组件时，Button组件默认变灰，用户即确定完成选中操作。
* 提升界面精致程度和生动性。
* 减少开发者工作量，例如列表滑动组件自带滑动动效，开发者直接调用即可。

更多效果，可以参考[组件说明](../harmonyos-references/ts-container-flex.md)。

示例代码和效果如下。

```
1. @Entry
2. @Component
3. struct ComponentDemo {
4. build() {
5. Row() {
6. Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
7. .select(true)
8. .shape(CheckBoxShape.CIRCLE)
9. .size({ width: 50, height: 50 })
10. }
11. .width('100%')
12. .height('100%')
13. .justifyContent(FlexAlign.Center)
14. }
15. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/component/template1/Index.ets#L16-L33)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/yVmwauXmQOSthXT3gXlAPA/zh-cn_image_0000002558764486.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=F82C143C172FEC0F47B4BF89129D2890DECB27FD0DED51EF84DE9BFF1E23262E)

## 打造组件定制化动效

部分组件支持通过[属性动画](arkts-attribute-animation-overview.md)和[转场动画](arkts-transition-overview.md)自定义组件子Item的动效，实现定制化动画效果。例如，[Scroll](../harmonyos-references/ts-container-scroll.md)组件中可对各个子组件在滑动时的动画效果进行定制。

* 在滑动或者点击操作时通过改变各个Scroll子组件的仿射属性来实现各种效果。
* 如果要在滑动过程中定制动效，可在滑动回调[onScroll](../harmonyos-references/ts-container-grid.md#onscrolldeprecated)中监控滑动距离，并计算每个组件的仿射属性。也可以自己定义手势，通过手势监控位置，手动调用ScrollTo改变滑动位置。
* 在滑动回调[onScrollStop](../harmonyos-references/ts-basic-components-textpicker.md#onscrollstop14)或手势结束回调中对滑动的最终位置进行微调。

定制Scroll组件滑动动效示例代码和效果如下。

```
1. import { curves, window, display, mediaquery, UIContext } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';

4. export default class GlobalContext extends AppStorage {
5. static mainWin: window.Window | undefined = undefined;
6. static mainWindowSize: window.Size | undefined = undefined;
7. }

9. /**
10. * 窗口、屏幕相关信息管理类
11. */
12. export class WindowManager {
13. private static instance: WindowManager | null = null;
14. private displayInfo: display.Display | null = null;
15. private uiContext: UIContext;
16. private orientationListener: mediaquery.MediaQueryListener;

18. constructor(uiContext: UIContext) {
19. this.uiContext = uiContext;
20. this.orientationListener = this.uiContext.getMediaQuery().matchMediaSync('(orientation: landscape)');
21. this.orientationListener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
22. this.onPortrait(mediaQueryResult);
23. });
24. this.loadDisplayInfo();
25. }

27. /**
28. * 设置主window窗口
29. * @param win 当前app窗口
30. */
31. setMainWin(win: window.Window) {
32. if (win == null) {
33. return;
34. }
35. GlobalContext.mainWin = win;
36. win.on('windowSizeChange', (data: window.Size) => {
37. if (GlobalContext.mainWindowSize == undefined || GlobalContext.mainWindowSize == null) {
38. GlobalContext.mainWindowSize = data;
39. } else {
40. if (GlobalContext.mainWindowSize.width == data.width && GlobalContext.mainWindowSize.height == data.height) {
41. return;
42. }
43. GlobalContext.mainWindowSize = data;
44. }

46. let winWidth = this.getMainWindowWidth();
47. AppStorage.setOrCreate<number>('mainWinWidth', winWidth);
48. let winHeight = this.getMainWindowHeight();
49. AppStorage.setOrCreate<number>('mainWinHeight', winHeight);
50. let context: UIAbility = new UIAbility();
51. context.context.eventHub.emit('windowSizeChange', winWidth, winHeight);
52. });
53. }

55. static getInstance(uiContext: UIContext): WindowManager {
56. if (WindowManager.instance == null) {
57. WindowManager.instance = new WindowManager(uiContext);
58. }
59. return WindowManager.instance;
60. }

62. private onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
63. if (mediaQueryResult.matches == AppStorage.get<boolean>('isLandscape')) {
64. return;
65. }
66. AppStorage.setOrCreate<boolean>('isLandscape', mediaQueryResult.matches);
67. this.loadDisplayInfo();
68. }

70. /**
71. * 切换屏幕方向
72. * @param ori 常量枚举值：window.Orientation
73. */
74. changeOrientation(ori: window.Orientation) {
75. if (GlobalContext.mainWin != null) {
76. GlobalContext.mainWin.setPreferredOrientation(ori);
77. }
78. }

80. private loadDisplayInfo() {
81. this.displayInfo = display.getDefaultDisplaySync();
82. AppStorage.setOrCreate<number>('displayWidth', this.getDisplayWidth());
83. AppStorage.setOrCreate<number>('displayHeight', this.getDisplayHeight());
84. }

86. /**
87. * 获取main窗口宽度，单位vp
88. */
89. getMainWindowWidth(): number {
90. return GlobalContext.mainWindowSize != null ? this.uiContext.px2vp(GlobalContext.mainWindowSize.width) : 0;
91. }

93. /**
94. * 获取main窗口高度，单位vp
95. */
96. getMainWindowHeight(): number {
97. return GlobalContext.mainWindowSize != null ? this.uiContext.px2vp(GlobalContext.mainWindowSize.height) : 0;
98. }

100. /**
101. * 获取屏幕宽度，单位vp
102. */
103. getDisplayWidth(): number {
104. return this.displayInfo != null ? this.uiContext.px2vp(this.displayInfo.width) : 0;
105. }

107. /**
108. * 获取屏幕高度，单位vp
109. */
110. getDisplayHeight(): number {
111. return this.displayInfo != null ? this.uiContext.px2vp(this.displayInfo.height) : 0;
112. }

114. /**
115. * 释放资源
116. */
117. release() {
118. if (this.orientationListener) {
119. this.orientationListener.off('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
120. this.onPortrait(mediaQueryResult);
121. });
122. }
123. if (GlobalContext.mainWin != null) {
124. GlobalContext.mainWin.off('windowSizeChange');
125. }
126. WindowManager.instance = null;
127. }
128. }

130. /**
131. * 封装任务卡片信息数据类
132. */
133. export class TaskData {
134. bgColor: Color | string | Resource = Color.White;
135. index: number = 0;
136. taskInfo: string = 'music';

138. constructor(bgColor: Color | string | Resource, index: number, taskInfo: string) {
139. this.bgColor = bgColor;
140. this.index = index;
141. this.taskInfo = taskInfo;
142. }
143. }

145. export const taskDataArr: Array<TaskData> =
146. [
147. new TaskData('#317AF7', 0, 'music'),
148. new TaskData('#D94838', 1, 'mall'),
149. new TaskData('#DB6B42', 2, 'photos'),
150. new TaskData('#5BA854', 3, 'setting'),
151. new TaskData('#317AF7', 4, 'call'),
152. new TaskData('#D94838', 5, 'music'),
153. new TaskData('#DB6B42', 6, 'mall'),
154. new TaskData('#5BA854', 7, 'photos'),
155. new TaskData('#D94838', 8, 'setting'),
156. new TaskData('#DB6B42', 9, 'call'),
157. new TaskData('#5BA854', 10, 'music')

159. ];

161. @Entry
162. @Component
163. export struct TaskSwitchMainPage {
164. displayWidth: number = WindowManager.getInstance(this.getUIContext()).getDisplayWidth();
165. scroller: Scroller = new Scroller();
166. cardSpace: number = 0; // 卡片间距
167. cardWidth: number = this.displayWidth / 2 - this.cardSpace / 2; // 卡片宽度
168. cardHeight: number = 400; // 卡片高度
169. cardPosition: Array<number> = []; // 卡片初始位置
170. clickIndex: boolean = false;
171. @State taskViewOffsetX: number = 0;
172. @State cardOffset: number = this.displayWidth / 4;
173. lastCardOffset: number = this.cardOffset;
174. startTime: number | undefined = undefined;

176. // 每个卡片初始位置
177. aboutToAppear() {
178. for (let i = 0; i < taskDataArr.length; i++) {
179. this.cardPosition[i] = i * (this.cardWidth + this.cardSpace);
180. }
181. }

183. // 每个卡片位置
184. getProgress(index: number): number {
185. let progress = (this.cardOffset + this.cardPosition[index] - this.taskViewOffsetX +
186. this.cardWidth / 2) / this.displayWidth;
187. return progress;
188. }

190. build() {
191. Stack({ alignContent: Alignment.Bottom }) {
192. // 背景
193. Column()
194. .width('100%')
195. .height('100%')
196. .backgroundColor(0xF0F0F0)

198. // 滑动组件
199. Scroll(this.scroller) {
200. Row({ space: this.cardSpace }) {
201. ForEach(taskDataArr, (item: TaskData, index) => {
202. Column()
203. .width(this.cardWidth)
204. .height(this.cardHeight)
205. .backgroundColor(item.bgColor)
206. .borderStyle(BorderStyle.Solid)
207. .borderWidth(1)
208. .borderColor(0xAFEEEE)
209. .borderRadius(15)
210. // 计算子组件的仿射属性
211. .scale((this.getProgress(index) >= 0.4 && this.getProgress(index) <= 0.6) ?
212. {
213. x: 1.1 - Math.abs(0.5 - this.getProgress(index)),
214. y: 1.1 - Math.abs(0.5 - this.getProgress(index))
215. } :
216. { x: 1, y: 1 })
217. .animation({ curve: Curve.Smooth })
218. // 滑动动画
219. .translate({ x: this.cardOffset })
220. .animation({ curve: curves.springMotion() })
221. .zIndex((this.getProgress(index) >= 0.4 && this.getProgress(index) <= 0.6) ? 2 : 1)
222. }, (item: TaskData) => item.toString())
223. }
224. .width((this.cardWidth + this.cardSpace) * (taskDataArr.length + 1))
225. .height('100%')
226. }
227. .gesture(
228. GestureGroup(GestureMode.Parallel,
229. PanGesture({ direction: PanDirection.Horizontal, distance: 5 })
230. .onActionStart((event: GestureEvent | undefined) => {
231. if (event) {
232. this.startTime = event.timestamp;
233. }
234. })
235. .onActionUpdate((event: GestureEvent | undefined) => {
236. if (event) {
237. this.cardOffset = this.lastCardOffset + event.offsetX;
238. }
239. })
240. .onActionEnd((event: GestureEvent | undefined) => {
241. if (event) {
242. let time = 0;
243. if (this.startTime) {
244. time = event.timestamp - this.startTime;
245. }
246. let speed = event.offsetX / (time / 1000000000);
247. let moveX = Math.pow(speed, 2) / 7000 * (speed > 0 ? 1 : -1);

249. this.cardOffset += moveX;
250. // 左滑大于最右侧位置
251. let cardOffsetMax = -(taskDataArr.length - 1) * (this.displayWidth / 2);
252. if (this.cardOffset < cardOffsetMax) {
253. this.cardOffset = cardOffsetMax;
254. }
255. // 右滑大于最左侧位置
256. if (this.cardOffset > this.displayWidth / 4) {
257. this.cardOffset = this.displayWidth / 4;
258. }

260. // 左右滑动距离不满足/满足切换关系时，补位/退回
261. let remainMargin = this.cardOffset % (this.displayWidth / 2);
262. if (remainMargin < 0) {
263. remainMargin = this.cardOffset % (this.displayWidth / 2) + this.displayWidth / 2;
264. }
265. if (remainMargin <= this.displayWidth / 4) {
266. this.cardOffset += this.displayWidth / 4 - remainMargin;
267. } else {
268. this.cardOffset -= this.displayWidth / 4 - (this.displayWidth / 2 - remainMargin);
269. }

271. // 记录本次滑动偏移量
272. this.lastCardOffset = this.cardOffset;
273. }
274. })
275. ), GestureMask.IgnoreInternal)
276. .scrollable(ScrollDirection.Horizontal)
277. .scrollBar(BarState.Off)

279. // 滑动到首尾位置
280. Button('Move to first/last')
281. .backgroundColor(0x888888)
282. .margin({ bottom: 30 })
283. .onClick(() => {
284. this.clickIndex = !this.clickIndex;

286. if (this.clickIndex) {
287. this.cardOffset = this.displayWidth / 4;
288. } else {
289. this.cardOffset = this.displayWidth / 4 - (taskDataArr.length - 1) * this.displayWidth / 2;
290. }
291. this.lastCardOffset = this.cardOffset;
292. })
293. }
294. .width('100%')
295. .height('100%')
296. }
297. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/component/template2/Index.ets#L16-L314)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/2jijB7zaQ5-VZuHlP6__0Q/zh-cn_image_0000002558604830.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=B4E3C83541CDC0103961FCA7400AB05461C4ABFEB99188A1077431C21E4ADBC2)

通过animateTo可以实现将List中指定的Item替换到首位，List中其余Item依次向下排列。定制List组件动态替换动效的示例代码和效果如下。

```
1. import { curves, AnimatorResult } from '@kit.ArkUI';

3. // 该接口控制列表项视觉属性
4. class ListItemModify implements AttributeModifier<ListItemAttribute> {
5. public offsetY: number = 0; // Y轴偏移量

7. applyNormalAttribute(instance: ListItemAttribute): void {
8. instance.translate({ y: this.offsetY }); // Y轴位移
9. }
10. }

12. @Observed
13. class DragSortCtrl<T> {
14. private arr: Array<T>; // 数据数组
15. private modify: Array<ListItemModify>; // 属性修改器数组
16. private uiContext: UIContext; // 新增UIContext成员
17. private dragRefOffset: number = 0; // 拖拽参考偏移量
18. offsetY: number = 0; // 当前Y轴偏移量
19. private ITEM_INTV: number = 0; // 列表项间隔

21. constructor(arr: Array<T>, intv: number, uiContext: UIContext) {
22. this.arr = arr;
23. this.uiContext = uiContext;
24. this.modify = [];
25. this.ITEM_INTV = intv;
26. arr.forEach(() => {
27. this.modify.push(new ListItemModify());
28. });
29. }

31. itemMove(index: number, newIndex: number): void {
32. let tmp = this.arr.splice(index, 1); // 移除当前传入的index
33. this.arr.splice(newIndex, 0, tmp[0]); // 将当前移除的index插入到数组前一个位置
34. let tmp2 = this.modify.splice(index, 1);
35. this.modify.splice(newIndex, 0, tmp2[0]);
36. }

38. setDragRef(item: T): void {
39. this.dragRefOffset = 0;
40. }

42. onMove(item: T, offset: number) {
43. this.offsetY = offset - this.dragRefOffset; // 逐帧计算传入的offect，每满足一个item高度时，进入下方if逻辑，更新dragRefOffset的值
44. let index = this.arr.indexOf(item); // 在数组中查找传入的item
45. this.modify[index].offsetY = this.offsetY;
46. if (this.offsetY < -this.ITEM_INTV / 2) { // 通过判断使指定的item逐一移动到首位
47. // 使用interpolatingSpring曲线生成弹簧动画
48. this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => { // 400: 弹簧刚度，38: 弹簧阻尼
49. this.offsetY += this.ITEM_INTV; // 调整偏移量实现平滑移动
50. this.dragRefOffset -= this.ITEM_INTV; // 移动的总偏移量
51. console.info(`item offsetY ${this.offsetY} dragRefOffset ${this.dragRefOffset}`);
52. this.itemMove(index, index - 1); // 执行列表项位置交换
53. });
54. }
55. }

57. getModify(item: T): ListItemModify {
58. let index = this.arr.indexOf(item);
59. return this.modify[index];
60. }
61. }

63. @Entry
64. @Component
65. struct ListAutoSortExample {
66. @State private arr: Array<number> = [0, 1, 2, 3, 4, 5]; // 列表数据数组
67. @State dragSortCtrl: DragSortCtrl<number> =
68. new DragSortCtrl<number>(this.arr, 120, this.getUIContext()); // 120: 列表项高度间隔
69. @State firstListItemGroupCount: number = 3; // 第一个列表项组包含的项目数量
70. private listScroll: ListScroller = new ListScroller(); // 列表滚动控制器
71. private backAnimator: AnimatorResult | null = null; // 动画控制器

73. @Builder
74. itemEnd(item: number, index: number) {
75. Row() {
76. Button('To TOP').margin('4vp').onClick(() => { // 4vp: 按钮边距
77. console.info(`item number item ${item} index ${index}`);
78. this.listScroll.closeAllSwipeActions({
79. onFinish: () => {
80. this.dragSortCtrl.setDragRef(item);
81. let length = 120 * (this.arr.indexOf(item)); // 120: 列表项高度间隔
82. this.backAnimator = this.getUIContext()?.createAnimator({
83. // 创建弹簧动画
84. duration: 1000, // 动画持续时间，单位毫秒
85. easing: 'interpolating-spring(0, 1, 150, 24)', // 150: 弹簧刚度，24: 弹簧阻尼
86. delay: 0, // 动画延迟时间
87. fill: 'none',
88. direction: 'normal',
89. iterations: 1, // 动画迭代次数
90. begin: 0, // 动画起始值
91. end: -length
92. });
93. this.backAnimator.onFrame = (value) => { // 逐帧回调更新位置
94. this.dragSortCtrl.onMove(item, value); // 处理list的移动替换动效
95. };
96. this.backAnimator.onFinish = () => {
97. };
98. this.backAnimator.play(); // 启动动画
99. }
100. });
101. })
102. }
103. .padding('4vp').justifyContent(FlexAlign.SpaceEvenly) // 4vp: 内边距
104. }

106. @Builder
107. header(title: string) {
108. Row() {
109. Text(title)
110. }
111. }

113. build() {
114. Row() {
115. Column() {
116. List({ space: 20, scroller: this.listScroll }) { // 20: 列表项间距
117. ListItemGroup({ header: this.header('first ListItemGroup'), space: 20 }) { // 20: 列表项组内间距
118. ForEach(this.arr, (item: number, index) => {
119. if (index < this.firstListItemGroupCount) {
120. ListItem() {
121. Text('' + item)
122. .width('100%')
123. .height(100) // 100: 列表项高度
124. .fontSize(16) // 16: 字体大小
125. .borderRadius(10) // 10: 边框圆角半径
126. .textAlign(TextAlign.Center)
127. .backgroundColor(0xFFFFFF) // 0xFFFFFF: 白色背景
128. }
129. .swipeAction({
130. end: this.itemEnd(item, index)
131. })
132. .clip(true)
133. .attributeModifier(this.dragSortCtrl.getModify(item)) // 动态设置属性修改
134. .borderRadius(10) // 10: 边框圆角半径
135. .margin({ left: 20, right: 20 }) // 20: 左右外边距
136. }
137. })
138. }

140. ListItemGroup({ header: this.header('second ListItemGroup'), space: 20 }) { // 20: 列表项组内间距
141. ForEach(this.arr, (item: number, index) => {
142. if (index > this.firstListItemGroupCount - 1) { // 1: 索引偏移量
143. ListItem() {
144. Text('' + item)
145. .width('100%')
146. .height(100) // 100: 列表项高度
147. .fontSize(16) // 16: 字体大小
148. .borderRadius(10) // 10: 边框圆角半径
149. .textAlign(TextAlign.Center)
150. .backgroundColor(0xFFFFFF) // 0xFFFFFF: 白色背景
151. }
152. .swipeAction({
153. end: this.itemEnd(item, index)
154. })
155. .clip(true)
156. .attributeModifier(this.dragSortCtrl.getModify(item))
157. .borderRadius(10) // 10: 边框圆角半径
158. .margin({ left: 20, right: 20 }) // 20: 左右外边距
159. }
160. })
161. }
162. }
163. .padding({ top: 20 }) // 20: 顶部内边距
164. .height('100%')
165. }
166. }
167. .backgroundColor(0xDCDCDC) // 0xDCDCDC: 浅灰色背景
168. }
169. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/component/template3/Index.ets#L16-L186)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/QaiUHDm8T_-h6qWneBtJCA/zh-cn_image_0000002589324355.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=D6AD29FA18C48FAFC993EBE8B26883381DDDCBFF236F9AF5A526838E05FA89D0)

## 示例代码

* [实现动效功能合集](https://gitcode.com/HarmonyOS_Samples/animation-collection)
