---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-manage-components-visibility
title: 感知组件可见性
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 感知组件可见性
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d72a0f2ceb7ff04be9648c82aa58b2872e2e8c041e10c957979bde4f70a5c341
---

## 概述

组件可见性是指组件在屏幕上的显示状态，通过感知可见性，应用能够实现以下典型场景：

* 组件曝光统计与分析（例如，统计广告组件在屏幕上的显示时长）；
* 资源按需加载与释放（例如，组件不可见时，释放组件使用的图片、视频等资源）；
* 感知复杂视图切换（例如，在多层视图嵌套情况下，依据组件的显示状态，处理相关逻辑）。

针对上述场景，建议按照以下策略进行选择：

| 场景描述 | 推荐接口 | 说明 |
| --- | --- | --- |
| [组件曝光统计与分析](arkts-manage-components-visibility.md#组件曝光统计与分析) | onVisibleAreaApproximateChange | 要监控的组件数量多，需要低频计算降低开销。 |
| [资源按需加载与释放](arkts-manage-components-visibility.md#资源按需加载与释放) | onVisibleAreaChange | 要监控的组件数量少，希望每帧检测确保状态及时更新。 |
| [感知复杂视图切换](arkts-manage-components-visibility.md#感知复杂视图切换) | nodeRenderState监听 | 适合感知页面或页切换导致的可见性变化。 |

应用也可自行遍历计算组件可见性，但由于组件存在复杂的层次关系，自行计算涉及大量运算，通常不被推荐。

## 组件曝光统计与分析

使用[onVisibleAreaApproximateChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareaapproximatechange17)监控关键组件（如广告、商品卡片）的曝光时长，用于用户行为分析和运营统计。

该接口比onVisibleAreaChange性能更优，支持通过设置计算周期减少检测频率，适用于组件数量多、层级深的场景，可显著降低性能消耗。

说明

该能力从API version 17开始支持。

```
1. class ListDataSource implements IDataSource {
2. private list: number[] = [];
3. private listeners: DataChangeListener[] = [];

5. constructor(list: number[]) {
6. this.list = list;
7. }

9. totalCount(): number {
10. return this.list.length;
11. }

13. getData(index: number): number {
14. return this.list[index];
15. }

17. registerDataChangeListener(listener: DataChangeListener): void {
18. if (this.listeners.indexOf(listener) < 0) {
19. this.listeners.push(listener);
20. }
21. }

23. unregisterDataChangeListener(listener: DataChangeListener): void {
24. const pos = this.listeners.indexOf(listener);
25. if (pos >= 0) {
26. this.listeners.splice(pos, 1);
27. }
28. }

30. notifyDataDelete(index: number): void {
31. this.listeners.forEach(listener => {
32. listener.onDataDelete(index);
33. });
34. }

36. notifyDataAdd(index: number): void {
37. this.listeners.forEach(listener => {
38. listener.onDataAdd(index);
39. });
40. }

42. public deleteItem(index: number): void {
43. this.list.splice(index, 1);
44. this.notifyDataDelete(index);
45. }

47. public insertItem(index: number, data: number): void {
48. this.list.splice(index, 0, data);
49. this.notifyDataAdd(index);
50. }
51. }

53. class ExposureTrackingData {
54. // 使用一个map记录当前正在展示的广告位，以及它开始被展示的时间戳，以便在它不可见时可以计算在屏幕上的展示时长
55. private visibleAdvertisingInfos = new Map<string, number>();
56. // 使用一个map记录每个广告位的展示总时长
57. private exposureData = new Map<string, number>();

59. constructor() {
60. }

62. notifyAdvertisingSlotIsAppearing(slot: string): void {
63. // 广告位开始展示，记录起始时间戳
64. let startTimestamp = Date.now()
65. this.visibleAdvertisingInfos.set(slot, startTimestamp)
66. }

68. notifyAdvertisingSlotIsDisappearing(slot: string): void {
69. // 广告位开始消失，计算本次展示时长，并累加到总时长数据中
70. let endTimestamp: number = Date.now()
71. let advertisingInfo = this.visibleAdvertisingInfos.get(slot)
72. let duration: number = 0
73. if (advertisingInfo) {
74. duration = endTimestamp - advertisingInfo.valueOf()
75. }
76. // 刷新展示总时长
77. this.updateExposureData(slot, duration)
78. // 从当前可见的map中删除这个广告位信息
79. this.visibleAdvertisingInfos.delete(slot)
80. }

82. notifyPageHiding(): void {
83. // 页面正在退出，上报统计数据
84. this.reportData()
85. }

87. updateExposureData(slot: string, duration: number) {
88. if (duration <= 0) {
89. return
90. }
91. let oldDuration = 0
92. let dataItem = this.exposureData.get(slot)
93. if (dataItem) {
94. oldDuration = dataItem.valueOf()
95. }
96. this.exposureData.set(slot, oldDuration + duration)
97. }

99. consumeAllCurrentVisibleSlots(): void {
100. this.visibleAdvertisingInfos.forEach((value: number, key: string) => {
101. this.notifyAdvertisingSlotIsDisappearing(key)
102. });
103. this.visibleAdvertisingInfos.clear()
104. }

106. reportData(): void {
107. // 上报之前先将当前正在展示的广告位统计信息刷新到总时长
108. this.consumeAllCurrentVisibleSlots()
109. // 发送数据到分析平台
110. console.info(`曝光数据上报: ` + Array.from(this.exposureData))
111. // 上报后清空
112. this.exposureData.clear()
113. }
114. }

116. @Entry
117. @ComponentV2
118. struct ExposureTrackingPage {
119. private data: ListDataSource =
120. new ListDataSource([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]);
121. private exposureData = new ExposureTrackingData()

123. onPageHide(): void {
124. // 在页面退出时，上报统计数据到分析平台
125. this.exposureData.notifyPageHiding()
126. }

128. build() {
129. Column() {
130. List({ space: 20, initialIndex: 0 }) {
131. LazyForEach(this.data, (item: number) => {
132. ListItem() {
133. Text(this.getAdvertisingSlotInfo(item))
134. .width('100%')
135. .height(100)
136. .fontSize(20)
137. .fontColor(Color.White)
138. .textAlign(TextAlign.Center)
139. .borderRadius(10)
140. .backgroundColor(this.calculateItemBackgroundColor(item))
141. }
142. // 为每一个列表条目都增加一个可见性监听回调，给定阈值0.5，即如果广告位在屏幕上显示超过自身一半，就认为已经曝光；
143. // 尽管这里代码只写了一行，但实际会为每个显示出来的列表项都绑定一个回调，因此这里我们使用可控制计算频率的回调接口。
144. .onVisibleAreaApproximateChange({ ratios: [0.5], expectedUpdateInterval: 500 },
145. (isExpanding: boolean, currentRatio: number) => {
146. this.handleExposureTracking(item, isExpanding, currentRatio)
147. })
148. }, (item: number) => item.toString())
149. }
150. .listDirection(Axis.Vertical)
151. .scrollBar(BarState.Off)
152. .edgeEffect(EdgeEffect.Spring)
153. .width('90%')
154. .margin(5)
155. }
156. .width('100%')
157. .height('100%')
158. .backgroundColor(0xDCDCDC)
159. .padding({ top: 5 })
160. }

162. private isAdvertisingSlot(index: number): boolean {
163. // 假设每隔5个组件就是一个广告位
164. return (index % 5 == 0)
165. }

167. private calculateAdvertisingSlot(index: number): number | null {
168. if (this.isAdvertisingSlot(index)) {
169. return (index / 5)
170. }
171. return null
172. }

174. private calculateItemBackgroundColor(index: number): Color {
175. if (this.isAdvertisingSlot(index)) {
176. return Color.Green
177. }

179. return Color.Gray
180. }

182. private getAdvertisingSlotInfo(index: number): string {
183. let advertisingSlot = this.calculateAdvertisingSlot(index)
184. if (advertisingSlot) {
185. return advertisingSlot + " 号广告位"
186. }
187. return '普通内容 ' + index
188. }

190. private handleExposureTracking(index: number, isExpanding: boolean, currentRatio: number): void {
191. if (!this.isAdvertisingSlot(index)) {
192. // 不处理非广告位
193. return
194. }
195. let slot = this.getAdvertisingSlotInfo(index)
196. if (isExpanding) {
197. // 可见比例正在增大，说明组件正在出现
198. this.exposureData.notifyAdvertisingSlotIsAppearing(slot)
199. return
200. }
201. // 可见比例正在减小，说明组件正在消失
202. this.exposureData.notifyAdvertisingSlotIsDisappearing(slot)
203. }
204. }
```

## 资源按需加载与释放

使用[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)监听组件可见面积占比的精细变化，当可见比例接近预设阈值时触发回调，根据可见比例的变化加载或释放资源。

说明

该能力从API version 9开始支持。

* 可见面积以父组件边界为限，超出父组件的部分不会被计入可见面积比值计算;
* 由于存在浮点数比较，系统会在计算结果接近所设置的阈值时触发回调；
* 为确保可见性变化通知的及时性，系统在每帧进行计算可见比例的变化检测，为了减小系统负载，应尽可能少的使用这个接口。

```
1. import { image } from '@kit.ImageKit';

3. class ListDataSource implements IDataSource {
4. private list: number[] = [];
5. private listeners: DataChangeListener[] = [];

7. constructor(list: number[]) {
8. this.list = list;
9. }

11. totalCount(): number {
12. return this.list.length;
13. }

15. getData(index: number): number {
16. return this.list[index];
17. }

19. registerDataChangeListener(listener: DataChangeListener): void {
20. if (this.listeners.indexOf(listener) < 0) {
21. this.listeners.push(listener);
22. }
23. }

25. unregisterDataChangeListener(listener: DataChangeListener): void {
26. const pos = this.listeners.indexOf(listener);
27. if (pos >= 0) {
28. this.listeners.splice(pos, 1);
29. }
30. }

32. notifyDataDelete(index: number): void {
33. this.listeners.forEach(listener => {
34. listener.onDataDelete(index);
35. });
36. }

38. notifyDataAdd(index: number): void {
39. this.listeners.forEach(listener => {
40. listener.onDataAdd(index);
41. });
42. }

44. public deleteItem(index: number): void {
45. this.list.splice(index, 1);
46. this.notifyDataDelete(index);
47. }

49. public insertItem(index: number, data: number): void {
50. this.list.splice(index, 0, data);
51. this.notifyDataAdd(index);
52. }
53. }

55. @Entry
56. @ComponentV2
57. struct Index {
58. @Local headerImage: PixelMap | null = null
59. private data: ListDataSource =
60. new ListDataSource([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]);

62. build() {
63. Column() {
64. List({ space: 20, initialIndex: 0 }) {
65. ListItem() {
66. Image(this.headerImage)
67. .width('100%')
68. .height(300)
69. // 整个页面上只有这一个组件需要监听可见性，并且需要及时感知状态进行资源的及时加载
70. .onVisibleAreaChange([0.1], (isExpanding: boolean, currentRatio: number) => {
71. this.loadOrReleaseHeaderImage(isExpanding)
72. })
73. }

75. LazyForEach(this.data, (item: number) => {
76. ListItem() {
77. Text('' + item)
78. .width('100%')
79. .height(50)
80. .fontSize(20)
81. .fontColor(Color.White)
82. .textAlign(TextAlign.Center)
83. .borderRadius(10)
84. .backgroundColor(Color.Grey)
85. }
86. }, (item: number) => item.toString())
87. }
88. .listDirection(Axis.Vertical)
89. .scrollBar(BarState.Off)
90. .edgeEffect(EdgeEffect.Spring)
91. .width('90%')
92. .margin(5)
93. }
94. .width('100%')
95. .height('100%')
96. .backgroundColor(0xDCDCDC)
97. .padding({ top: 5 })
98. }

100. private loadOrReleaseHeaderImage(isExpanding: boolean): void {
101. if (!isExpanding) {
102. // 马上就不可见了，释放掉图片
103. this.headerImage = null
104. console.info('图片释放完成')
105. return
106. }

108. try {
109. this.getUIContext().getHostContext()!.resourceManager.getMediaContent($r('app.media.startIcon').id,
110. (error, value: ArrayBuffer) => {
111. let opts: image.InitializationOptions = {
112. editable: true,
113. pixelFormat: 3,
114. size: { height: 4, width: 6 }
115. };
116. let uint8Array: Uint8Array = new Uint8Array(value);
117. let buffer: ArrayBuffer = uint8Array.buffer.slice(0);

119. image.createPixelMap(buffer, opts).then((pixelMap) => {
120. this.headerImage = pixelMap
121. console.info('图片加载完成')
122. })
123. });
124. } catch (error) {
125. console.error(`callback getMediaContent failed, error code: ${error.code}, message: ${error.message}.`)
126. }
127. }
128. }
```

## 感知复杂视图切换

通过UIObserver提供的[on('nodeRenderState')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onnoderenderstate20)方法，可以监听指定组件的渲染状态。此接口需要传入一个组件标识，以指定需要观察的组件，因此不适用于组件频繁创建和销毁的场景，适用于因页面变化导致的组件显隐变化，例如页面跳转、组件所在页面被压栈，如Swiper/Tabs组件当前显示页被划出的场景。

渲染状态有两种：

* ABOUT\_TO\_RENDER\_IN：组件已挂载到渲染树，下一帧将被渲染；
* ABOUT\_TO\_RENDER\_OUT：组件已从渲染树移除，下一帧不再渲染。

说明

该能力从API version 20开始支持。

需要注意的是，ABOUT\_TO\_RENDER\_IN仅表示组件进入渲染流程，下一帧将由系统送显到屏幕上，但组件可能因被其他组件遮挡而无法被看到，因此渲染状态并不完全等同于可见性。

以下示例将一个被观测的Column组件置于Tabs、Navigation和Swiper的嵌套布局中，无论切换Tab页、页面跳转或Swiper页，均能准确感知组件是否显示于屏幕上。

说明

鉴于on('nodeRenderState')接口的特点，不建议将其用于列表项这种划出屏幕区域外节点就会被回收下树的场景。

```
1. // Index.ets
2. import { NodeRenderState } from '@kit.ArkUI';

4. @Entry
5. @ComponentV2
6. struct Index {
7. private childNavStack: NavPathStack = new NavPathStack();
8. private tabController: TabsController = new TabsController();

10. build() {
11. Tabs({ barPosition: BarPosition.End, controller: this.tabController }) {
12. TabContent() {
13. Navigation() {
14. Stack({ alignContent: Alignment.Center }) {
15. Swiper() {
16. // swiper 第一页为一个子navigation
17. Navigation(this.childNavStack) {
18. Column() {
19. Text('被监听的组件')
20. .width('100%')
21. .height('100%')
22. .fontSize(26)
23. .fontColor(Color.White)
24. .textAlign(TextAlign.Center)
25. }
26. .width('90%')
27. .height(300)
28. .backgroundColor(Color.Blue)
29. .id('component_to_be_monitor')
30. .onAttach(() => {
31. // 10ms后再注册监听回调，避免挂载还未完全完成
32. setTimeout(()=>{
33. // 在被监听的组件挂载的时候开启对该组件的状态监听
34. this.getUIContext()
35. .getUIObserver()
36. .on('nodeRenderState', 'component_to_be_monitor', (state: NodeRenderState, node?: FrameNode) => {
37. if (state == NodeRenderState.ABOUT_TO_RENDER_IN) {
38. console.info('组件将显示')
39. } else {
40. console.info('组件将消失')
41. }
42. })
43. }, 10)
44. })
45. .onDetach(() => {
46. // 在被监听的组件从组件树上下树时取消监听
47. this.getUIContext().getUIObserver().off('nodeRenderState', 'component_to_be_monitor')
48. })

50. Button('跳转下一页', { stateEffect: true, type: ButtonType.Capsule })
51. .width('80%')
52. .height(40)
53. .margin(20)
54. .onClick(() => {
55. let parentStack = this.childNavStack.getParent();
56. parentStack?.pushPath({ name: "pageTwo" });
57. })
58. }
59. .clip(true)
60. .backgroundColor(Color.Orange)
61. .width('90%')
62. .height('90%')
63. .title('ChildNavigation')

65. // swiper 第二页
66. Text('swiper 第二页')
67. .width('90%')
68. .height('90%')
69. .fontSize(20)
70. .fontColor(Color.Black)
71. .backgroundColor(Color.Orange)
72. .textAlign(TextAlign.Center)
73. // swiper 第三页
74. Text('swiper 第三页')
75. .width('90%')
76. .height('90%')
77. .fontSize(20)
78. .fontColor(Color.Black)
79. .backgroundColor(Color.Orange)
80. .textAlign(TextAlign.Center)
81. }
82. .itemSpace(10)
83. }
84. .width('100%')
85. .height('100%')
86. }
87. .backgroundColor(Color.Green)
88. .width('100%')
89. .height('100%')
90. .title('ParentNavigation')
91. }.tabBar('首页')

93. TabContent() {
94. Text('推荐')
95. .width('100%')
96. .height('100%')
97. .fontSize(20)
98. .fontColor(Color.Black)
99. .backgroundColor(Color.Pink)
100. .textAlign(TextAlign.Center)
101. }.tabBar('推荐')

103. TabContent() {
104. Text('我的')
105. .width('100%')
106. .height('100%')
107. .fontSize(20)
108. .fontColor(Color.Black)
109. .backgroundColor(Color.Yellow)
110. .textAlign(TextAlign.Center)
111. }.tabBar('我的')
112. }
113. .backgroundColor(Color.Gray)
114. }
115. }
```

```
1. // PageTwo.ets
2. @Builder
3. export function PageTwoBuilder(name: string) {
4. NavDestination() {
5. Text("this is " + name)
6. .width('100%')
7. .height('100%')
8. .textAlign(TextAlign.Center)
9. .fontSize(20)
10. .fontColor(Color.White)
11. .backgroundColor(Color.Red)
12. }
13. .title(name)
14. }
```

在resources/base/profile中创建route\_map.json文件，并添加以下配置信息。

```
1. {
2. "routerMap": [
3. {
4. "name": "pageTwo",
5. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
6. "buildFunction": "PageTwoBuilder",
7. "data": {
8. "description": "this is pageTwo"
9. }
10. }
11. ]
12. }
```

在module.json5配置文件的module标签中定义routerMap字段，指向路由表配置文件route\_map.json。

```
1. "routerMap": "$profile:route_map"
```

## 常见问题

### 可见性计算与实际视觉不符

**问题现象**

组件已进入屏幕但回调未触发，或可见比例与视觉感知不一致。

**解决措施**

* 检查父组件是否设置clip属性，裁剪可能导致可见面积计算偏差。
* 考虑组件透明度影响，即使 opacity为0也会被计入可见面积。
* 结合nodeRenderState监听交叉验证。
* 尝试将[measureFromViewport](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange22)设置为true进行验证。

### 高频回调导致性能下降

**问题现象**

滚动时界面卡顿，日志显示可见性回调频繁执行。

**解决措施**

* 切换到onVisibleAreaApproximateChange并将expectedUpdateInterval设置为一个更大的值。
* 减少注册可见性回调的组件数量。

### RenderState监听数量超限

**问题现象**

nodeRenderState监听失败，日志提示超出最大监听数量。

**解决措施**

* 替换为使用局部监听接口onVisibleAreaApproximateChange。
* 替换为对显示范围较大的父容器组件进行监听。
* 及时移除不再需要的监听off方法。
