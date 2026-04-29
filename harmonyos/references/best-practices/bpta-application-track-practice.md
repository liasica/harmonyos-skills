---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-track-practice
title: 应用埋点
breadcrumb: 最佳实践 > 应用框架 > ArkTS语言 > 应用埋点
category: best-practices
scraped_at: 2026-04-29T14:10:47+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:2098144c310ed003f23d008694cba69dd304fe062389d4255faf503ea641ed12
---

## 概述

埋点是指将信息采集程序和原本的功能代码结合起来，针对特定用户行为收集、处理和发送一些信息，用来跟踪应用使用情况。包括访问数、访客数、停留时长、页面浏览数和跳出率。以下是几种常见业务场景：

* 页面中可视区域或者组件的点击量，统计点击频率，分析用户的偏好行为。
* 监听页面中组件滑动的开始与结束，计算滑动偏移量以及曝光比例。
* 监听页面切换，统计页面的停留时间以及切换的来源页和目标页，分析页面浏览数和跳出率。
* 分析页面加载性能，计算加载过程各个节点的耗时，可针对某个关键点进行优化。

## 埋点分类

按照用户行为不同，埋点可以分为点击埋点、曝光埋点以及页面埋点等。

* 点击埋点：用户在任意区域的一次单击，比如一个icon或一张图片。区别于被动的用户曝光行为，单击属于主动行为。
* 曝光埋点：统计页面局部区域是否被用户有效浏览，例如瀑布流中的每个卡片的曝光比例和曝光时长，这是被动行为。
* 页面埋点：统计用户在固定页面的停留时间，页面加载性能以及页面跳转时的来源页和去向页信息。

## 方案介绍

接下来会从（1）组件动态绑定埋点数据；（2）点击埋点方案；（3）曝光埋点方案；（4）页面埋点方案四部分介绍。整体方案使用全局无感监听能力[UIObserver](../harmonyos-references/arkts-apis-uicontext-uiobserver.md)和[setOnVisibleAreaApproximateChange](../harmonyos-references/ts-uicommonevent.md#setonvisibleareaapproximatechange)属性实现埋点功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/PZ6XLdRxRcK5C2ntOJ8EoA/zh-cn_image_0000002194010920.png?HW-CC-KV=V1&HW-CC-Date=20260429T061045Z&HW-CC-Expire=86400&HW-CC-Sign=D7C38E62F2CCDD4E8F65E8753BFD39EE65829FB848FBDD815E630F5226ADD809 "点击放大")

### 绑定埋点数据

首先，为需要埋点的组件指定对应的ID值和埋点数据。例如，Button组件的ID可以设为“button-1”，并通过customProperty属性设置key和value，其中key为组件ID，value为埋点数据。为了方便获取，可以将埋点数据统一定义在DataResource中。

```
1. // entry\src\main\ets\pages\ClickPage.ets
2. Button('Click Tracing Point - Single Component')
3. .width('100%')
4. .id('button-1')
5. .fontWeight(FontWeight.Bold)
6. .customProperty('button-1', DataResource['Index']['button-1'])
7. .onClick(() => {
8. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'btn');
9. })
```

[ClickPage.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/pages/ClickPage.ets#L82-L90)

DataResource根据Page名、组件名和索引封装，Page名为最外层key，组件名+索引为里层key。value值根据实际业务配置。

```
1. // entry\src\main\ets\viewModel\DataResource.ets
2. export const DataResource: Record<string, Record<string, DataResourceType>> = {
3. 'Index': {
4. 'button-1': { id: 'button-1' },
5. 'button-2': { id: 'button-2' }
6. },
7. 'Page2': {
8. 'component-1': { id: 'text-2' }
9. }
10. }

12. export interface DataResourceType {
13. id: string
14. }
```

[DataResource.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/viewModel/DataResource.ets#L21-L35)

### 点击埋点

配置完埋点数据并绑定组件后，在EntryAbility中注册点击事件监听，在事件回调中获取触发节点。[UIObserver](../harmonyos-references/arkts-apis-uicontext-uiobserver.md)一共提供了两种监听事件：

* [on('willClick')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onwillclick12)：用于监听点击事件指令下发情况，所注册回调将于点击事件触发前触发。

* [on('didClick')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#ondidclick12)：用于监听点击事件指令下发情况，所注册回调将于点击事件触发后触发。

这两种方法都能在用户点击组件时触发回调。本示例使用 `willClick` 监听方式，下面介绍具体实现方案。

**实现步骤**

1. 首先实现一个简单页面，在组件上绑定ID和埋点数据。ID可以根据组件名-索引命名，例如代码示例中的两个组件，ID值分别为“button-1”和“button-2”。

   ```
   1. // entry\src\main\ets\pages\ClickPage.ets
   2. Row() {
   3. Text('Click Tracing Point - Composite Component')
   4. // ...
   5. Image($r('app.media.ic_public_arrow_right'))
   6. // ...
   7. }
   8. // ...
   9. .id('button-2')
   10. .margin({ top: 12 })
   11. .customProperty('button-2', DataResource['Index']['button-2'])
   12. .onClick(() => {
   13. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'row');
   14. })

   16. Row() {
   17. // entry\src\main\ets\pages\ClickPage.ets
   18. Button('Click Tracing Point - Single Component')
   19. .width('100%')
   20. .id('button-1')
   21. .fontWeight(FontWeight.Bold)
   22. .customProperty('button-1', DataResource['Index']['button-1'])
   23. .onClick(() => {
   24. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'btn');
   25. })
   26. }
   ```

   [ClickPage.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/pages/ClickPage.ets#L47-L92)
2. 在EntryAbility中注册UIObserver的willClick事件监听，并在事件回调中获取触发的组件节点FrameNode。

   ```
   1. // entry\src\main\ets\entryability\EntryAbility.ets
   2. uiContext.getUIObserver()?.on('willClick', (_event: ClickEvent, node?: FrameNode) => {
   3. const clickCallback = CallbackManager.getInstance().getClickCallback();
   4. clickCallback(node, uiContext);
   5. })
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L49-L53)
3. 接着可以根据FrameNode获取当前组件所在的Page和ID值，并且通过[getCustomProperty](../harmonyos-references/js-apis-arkui-framenode.md#getcustomproperty12)获取当前组件绑定的埋点数据。此外FrameNode还提供一些方法获取组件的基础属性，比如组件大小、组件位置以及是否可见等一些信息。具体可以参考[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md#framenode-1)官方文档。

   ```
   1. // entry\src\main\ets\viewModel\CallBackManager.ets
   2. /**
   3. * Obtains the ClickCallback callback.
   4. *
   5. */
   6. public getClickCallback() {
   7. return (node: FrameNode | undefined, uiContext: UIContext) => {
   8. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `FrameNode: ${node}`);
   9. const uniqueId = node?.getUniqueId();
   10. const ID = node?.getId();
   11. const pageInfo = uiContext.getPageInfoByUniqueId(uniqueId);
   12. const trackData = node?.getCustomProperty(ID);
   13. let eventParams: Record<string, string | number> = {
   14. 'component_id': ID ?? '',
   15. 'pageInfo': JSON.stringify(pageInfo ?? {}),
   16. 'trackData': JSON.stringify(trackData ?? {})
   17. };
   18. hiAppEvent.write({
   19. domain: 'test_domain',
   20. name: 'test_event',
   21. eventType: hiAppEvent.EventType.FAULT,
   22. params: eventParams
   23. }, (err: BusinessError) => {
   24. if (err) {
   25. hilog.error(0x0000, 'CallBackManager', '%{public}s', `code: ${err.code}, message: ${err.message}`);
   26. return;
   27. }
   28. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `getClickCallback, success to write event`);
   29. });
   30. };
   31. }
   ```

   [CallBackManager.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/viewModel/CallBackManager.ets#L54-L86)
4. 然后通过@kit.PerformanceAnalysisKit的[write()](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventwrite)方法将需要的数据写入当天的事件文件中。需要注意的是eventParams的参数值只能是number、string、boolean以及数组类型。

   ```
   1. hiAppEvent.write({
   2. domain: 'test_domain',
   3. name: 'test_event',
   4. eventType: hiAppEvent.EventType.FAULT,
   5. params: eventParams
   6. }, (err: BusinessError) => {
   7. if (err) {
   8. hilog.error(0x0000, 'CallBackManager', '%{public}s', `code: ${err.code}, message: ${err.message}`);
   9. return;
   10. }
   11. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `getClickCallback, success to write event`);
   12. });
   ```

   [CallBackManager.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/viewModel/CallBackManager.ets#L72-L83)
5. 最后在onWindowStageDestroy()调用UIObserver的[off()](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#offwillclick12)接口取消监听事件。

   ```
   1. // entry\src\main\ets\entryability\EntryAbility.ets
   2. onWindowStageDestroy(): void {
   3. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
   4. uiContext?.getUIObserver().off('willClick');
   5. uiContext?.getUIObserver().off('scrollEvent');
   6. uiContext?.getUIObserver().off('navDestinationSwitch');
   7. uiContext?.getUIObserver().off('routerPageUpdate');
   8. // Main window is destroyed, release UI related resources
   9. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'Ability onWindowStageDestroy');
   10. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L104-L113)

除了点击事件外，UIObserver还可以通过[on('scrollEvent')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onscrollevent12)监听组件滑动。在滑动开始与结束触发回调并得到滑动偏移量。以[瀑布流](../harmonyos-references/ts-container-waterflow.md#子组件)为例，对WaterFlow和FlowItem设置组件ID。

```
1. // entry\src\main\ets\pages\WaterFlowPage.ets
2. TrackNode({ track: new Track().id('WaterFlow-1') }) {
3. WaterFlow() {
4. LazyForEach(this.dataSource, (item: number, index: number) => {
5. FlowItem() {
6. TrackNode({ track: new Track().id(`flowItem_${index}`) }) {
7. WaterFlowCard({ item: item, index: index }).id(`flowItem_${index}`)
8. }
9. }
10. // ...
11. }, (item: number) => item.toString())
12. }
13. .id('WaterFlow-1')
14. // ...
15. .onReachStart(() => {
16. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'waterFlow reach start');
17. })
18. .onScrollStart(() => {
19. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'waterFlow scroll start');
20. })
21. .onScrollStop(() => {
22. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'waterFlow scroll stop');
23. })
24. .onScrollFrameBegin((offset: number, state: ScrollState) => {
25. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `waterFlow scrollFrameBegin offset: ${offset}`);
26. hilog.info(0x0000, 'ApplicationTrack', '%{public}s',
27. `waterFlow scrollFrameBegin state: ${state.toString()}`);
28. return { offsetRemain: offset };
29. })
30. }
```

[WaterFlowPage.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/pages/WaterFlowPage.ets#L80-L121)

接着在EntryAbility里统一注册scrollEvent的事件监听，在回调中获取[ScrollEventInfo](../harmonyos-references/js-apis-arkui-observer.md#scrolleventinfo12)信息，包括id、uniqueId、scrollEvent以及offset。

```
1. // entry\src\main\ets\entryability\EntryAbility.ets
2. uiContext.getUIObserver()
3. .on('scrollEvent', (info) => CallbackManager.getInstance().getScrollEvent(info))
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L56-L58)

说明

在scrollEvent监听事件中，回调参数的id值仅能精确到外层组件WaterFlow，无法精确到内层FlowItem。 若要在滑动过程中获取各Item组件的曝光比例，请参考第三小节的曝光埋点。

### 曝光埋点

曝光埋点需要监测页面中每个组件的出现与消失。例如，当用户滑动瀑布流时，如果某个项目出现的时长超过500毫秒，则记录为一次有效曝光。为避免在每个页面注入冗长代码，建议使用自定义的“埋点钩子”组件进行封装。以下是具体实现步骤。

**实现步骤**

1. 首先自定义一个TrackNode“钩子”组件，该组件需支持嵌套子组件、组件ID值注入以及注册监听事件。因此，TrackNode中的build()方法需由外部调用方决定，并且在onDidBuild()生命周期中将组件信息注入。onDidBuild()主要完成以下三件事：

   （1）调用TrackManager的addTrack()方法，将当前组件与TrackShadow对象绑定。

   （2）通过[setOnVisibleAreaApproximateChange()](../harmonyos-references/ts-uicommonevent.md#setonvisibleareaapproximatechange)监听埋点组件的可视区域的变化；其中ratio值可以自定义设置，比如本示例设置了0.0、0.5、1.0。

   （3）根据当前组件获取其父节点，判断父节点是否有埋点钩子。如果没有，继续往上追溯，直到父节点为null。如果有，则在父节点的子组件集合中添加当前节点。

   在aboutToDisappear()生命周期中，调用TrackManager的removeTrack()方法删除当前组件信息。

   ```
   1. // entry\src\main\ets\viewModel\TrackNode.ets
   2. // onDidBuild Life Cycle.
   3. onDidBuild(): void {
   4. // Construct the virtual tree of the tracing point.
   5. // The obtained node is the root node of the current page (row in the test case).
   6. let uid = this.getUniqueId();
   7. let node: FrameNode | null = this.getUIContext().getFrameNodeByUniqueId(uid);
   8. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `Track onDidBuild node:${node?.getNodeType()}`);
   9. if (node === null) {
   10. return;
   11. }
   12. this.trackShadow.node = node;
   13. this.trackShadow.id = node?.getId();
   14. this.trackShadow.track = this.track;
   15. TrackManager.get().addTrack(this.trackShadow.id, this.trackShadow);
   16. // The setOnVisibleAreaApproximateChange monitors and records the visible area of the tracing point component.
   17. node?.commonEvent.setOnVisibleAreaApproximateChange(
   18. { ratios: [0, 0.5, 1], expectedUpdateInterval: 500 },
   19. (ratioInc: boolean, ratio: number) => {
   20. const areaChangeCb = CallbackManager.getInstance().getAreaChangeCallback();
   21. areaChangeCb(node, ratio);
   22. this.trackShadow.visibleRatio = ratio;
   23. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `ratioInc: ${ratioInc}`);
   24. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `ratio: ${ratio}`);
   25. });

   27. let parent: FrameNode | null = node?.getParent();
   28. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `Parent getId: ${parent?.getId()}`);

   30. let attachTrackToParent: (parent: FrameNode | null) => boolean =
   31. (parent: FrameNode | null) => {
   32. while (parent !== null) {
   33. let parentTrack = TrackManager.get().getTrackById(parent?.getId());
   34. if (parentTrack !== undefined) {
   35. parentTrack.childIds.add(this.trackShadow.id);
   36. this.trackShadow.parentId = parentTrack.id;
   37. return true;
   38. }
   39. parent = parent.getParent();
   40. }
   41. return false;
   42. };
   43. let attached = attachTrackToParent(parent);

   45. if (!attached) {
   46. node?.commonEvent.setOnAppear(() => {
   47. let attached = attachTrackToParent(parent);
   48. if (attached) {
   49. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `Track lazy attached: ${this.trackShadow.id}`);
   50. }
   51. });
   52. }
   53. }
   ```

   [TrackNode.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/viewModel/TrackNode.ets#L41-L93)
2. TrackManager封装了埋点钩子的操作方法，包括绑定、删除和导出。绑定是将当前组件ID与TrackShadow对象存入全局Map中。导出是以根节点为起点，递归输出所有子组件的曝光比例。删除是根据具体ID值从Map中移除对应数据。

   ```
   1. // entry\src\main\ets\viewModel\TrackNode.ets
   2. /**
   3. * Tracing point data operation class
   4. */
   5. export class TrackManager {
   6. static instance: TrackManager;
   7. private trackMap: Map<string, TrackShadow> = new Map();
   8. private rootTrack: TrackShadow | null = null;

   10. static get(): TrackManager {
   11. if (TrackManager.instance !== undefined) {
   12. return TrackManager.instance;
   13. }
   14. TrackManager.instance = new TrackManager();
   15. return TrackManager.instance;
   16. }

   18. addTrack(id: string, track: TrackShadow): void {
   19. if (this.trackMap.size === 0) {
   20. this.rootTrack = track;
   21. }
   22. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `Track add id: ${id}`);
   23. this.trackMap.set(id, track);
   24. }

   26. removeTrack(id: string): void {
   27. let current = this.getTrackById(id);
   28. if (current !== undefined) {
   29. this.trackMap.delete(id);
   30. let parent = this.getTrackById(current?.parentId);
   31. parent?.childIds.delete(id);
   32. }
   33. }

   35. getTrackById(id: string): TrackShadow | undefined {
   36. return this.trackMap.get(id);
   37. }

   39. dump(): void {
   40. this.rootTrack?.dump(0);
   41. }
   42. }
   ```

   [TrackNode.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/viewModel/TrackNode.ets#L142-L183)
3. TrackShadow对象包含FrameNode、track、childIds和parentId。FrameNode表示组件节点，track包含ID值，childIds表示子组件列表，parentId表示父组件的ID值。

   ```
   1. // entry\src\main\ets\viewModel\TrackNode.ets
   2. export class Track {
   3. public areaPercent: number = 0;
   4. public trackId: string = '';

   6. constructor() {
   7. }

   9. id(newId: string): Track {
   10. this.trackId = newId;
   11. return this;
   12. }
   13. }

   15. /**
   16. * Tracing point data.
   17. */
   18. export class TrackShadow {
   19. public node: FrameNode | null = null;
   20. public id: string = '';
   21. public track: Track | null = null;
   22. public childIds: Set<string> = new Set();
   23. public parentId: string = '';
   24. public visibleRect: common2D.Rect = {
   25. left: 0,
   26. top: 0,
   27. right: 0,
   28. bottom: 0
   29. };
   30. public visibleRatio: number = 0;

   32. // Output the information about the tracing point tree through global dump.
   33. dump(depth: number = 0): void {
   34. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `Track Dp: ${depth}`);
   35. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `AreaPer: ${this.track?.areaPercent}`);
   36. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `VisibleRatio: ${this.visibleRatio}`);
   37. this.childIds.forEach((value: string) => {
   38. TrackManager.get().getTrackById(value)?.dump(depth + 1);
   39. });
   40. }
   41. }
   ```

   [TrackNode.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/viewModel/TrackNode.ets#L98-L138)
4. 根据上述TrackNode组件改造瀑布流代码：使用TrackNode钩子将WaterFlow和FlowItem组件包裹起来，并传递一个包含id的track对象，id作为组件的唯一标识。

   ```
   1. // entry\src\main\ets\pages\WaterFlowPage.ets
   2. TrackNode({ track: new Track().id('WaterFlow-1') }) {
   3. WaterFlow() {
   4. LazyForEach(this.dataSource, (item: number, index: number) => {
   5. FlowItem() {
   6. TrackNode({ track: new Track().id(`flowItem_${index}`) }) {
   7. WaterFlowCard({ item: item, index: index }).id(`flowItem_${index}`)
   8. }
   9. }
   10. // ...
   11. }, (item: number) => item.toString())
   12. }
   13. .id('WaterFlow-1')
   14. // ...
   15. .onReachStart(() => {
   16. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'waterFlow reach start');
   17. })
   18. .onScrollStart(() => {
   19. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'waterFlow scroll start');
   20. })
   21. .onScrollStop(() => {
   22. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'waterFlow scroll stop');
   23. })
   24. .onScrollFrameBegin((offset: number, state: ScrollState) => {
   25. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', `waterFlow scrollFrameBegin offset: ${offset}`);
   26. hilog.info(0x0000, 'ApplicationTrack', '%{public}s',
   27. `waterFlow scrollFrameBegin state: ${state.toString()}`);
   28. return { offsetRemain: offset };
   29. })
   30. }
   ```

   [WaterFlowPage.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/pages/WaterFlowPage.ets#L80-L121)

滚动瀑布流时，不仅可以监听每个Item的曝光比例，还可以追溯到根节点，统计根节点中每个子组件的曝光比例。

说明

* 滑动容器中的子组件曝光，例如List、Grid、Swiper、WaterFlow，可以参考本章节进行实现。
* 当该曝光埋点在组件未发生变化时，不会触发回调记录一次有效曝光。例如：在瀑布流场景下，如果某个Item已经达到设定的500ms，但用户后续不再滑动或直接退出应用，则此次曝光将不会被记录。

### 页面埋点

页面埋点在本示例中分为两类：监听页面切换和采集页面加载性能。以下将从Navigation和Router两种路由方案进行讲解。

**Navigation路由**：

针对Navigation方案，UIObserver提供`navDestinationSwitch`事件，用于监听页面切换，并支持在回调中获取当前页面的切换信息。在`EntryAbility`中统一注册`UIObserver`的`navDestinationSwitch`事件监听。

```
1. // entry\src\main\ets\entryability\EntryAbility.ets
2. uiContext.getUIObserver().on('navDestinationSwitch', (info) => {
3. const switchCallback = CallbackManager.getInstance().getSwitchCallback();
4. switchCallback(info);
5. })
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L61-L65)

回调函数中的info包含context、from、to和operation，用于标识页面的来源和去向。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| context | UIContext | 页面上下文信息 |
| from | NavDestinationInfo | NavBar | 来源页 |
| to | NavDestinationInfo | NavBar | 去向页 |
| operation | [NavigationOperation](../harmonyos-references/ts-basic-components-navigation.md#navigationoperation11枚举说明) | 页面操作 |

此外还可以通过UIObserver的[on("navDestinationUpdate")](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onnavdestinationupdate11)事件监听页面的显示与隐藏，回调传参中包含页面名称、状态信息以及页面的唯一标识ID。

**Router路由**：

针对Router路由方案，UIObserver提供了[on('routerPageUpdate')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onrouterpageupdate11)监听事件，在页面切换过程中触发相应回调。

```
1. // entry\src\main\ets\entryability\EntryAbility.ets
2. uiContext.getUIObserver().on('routerPageUpdate', (info) => {
3. const switchCallback = CallbackManager.getInstance().getSwitchCallback();
4. switchCallback(info);
5. })
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L68-L72)

比如调用pushPath()从A页面跳转到B页面时，该回调会被触发三次：第一次触发的页面名称为PageB，页面状态为[ABOUT\_TO\_APPEAR](../harmonyos-references/js-apis-arkui-observer.md#routerpagestate)即将显示；第二次触发的页面名称为PageA，页面状态为ON\_PAGE\_HIDE页面隐藏；第三次触发的页面名称为PageB，页面状态为ON\_PAGE\_SHOW页面显示。回调传参同样包含页面上下文、触发事件的页面名称等等。

| 字段名 | 类型 | 含义 |
| --- | --- | --- |
| context | UIContext | 页面上下文信息 |
| index | number | 触发页面在路由栈中的位置 |
| name | String | 触发页面名称 |
| path | String | 触发页面路径 |
| state | [RouterPageState](../harmonyos-references/js-apis-arkui-observer.md#routerpagestate) | 页面状态 |
| pageId | String | 页面唯一标识 |

**页面加载性能：**

页面加载性能可以通过计算首帧绘制与绘制结束的时间差来判断。UIObserver同样提供了on("willDraw")事件和on("didLayout")事件，可以在首帧监听中记录初始时间，在完成绘制时记录结束时间。此事件监听需要在页面中注册，Navigation与Router路由相同，本示例以Navigation为例。在aboutToAppear注册on("willDraw")和on("didLayout")事件。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { router } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct NavigationPage {
7. // ...

9. aboutToAppear(): void {
10. const uiContext = this.getUIContext();
11. // Registering a Listening Event
12. uiContext.getUIObserver().on('willDraw', () => {
13. this.startTime = Date.now();
14. })
15. uiContext.getUIObserver().on('didLayout', () => {
16. this.endTime = Date.now();
17. })
18. }

20. // ...
21. getResourceString(resource: Resource): string {
22. let resourceString: string = '';
23. try {
24. resourceString = this.getUIContext().getHostContext()!.resourceManager.getStringSync(resource.id);
25. } catch (error) {
26. hilog.error(0x0000, '[getResourceString]', `getResourceString err: ${JSON.stringify(error)}`);
27. }
28. return resourceString;
29. }
30. // ...
31. build() {
32. Navigation(this.pageInfos) {
33. Column() {
34. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
35. .width('100%')
36. .onClick(() => {
37. // Put the NavDestination page information specified by name into the stack.
38. this.pageInfos.pushPath({ name: 'pageOne' });
39. })
40. Button('Use interception', { stateEffect: true, type: ButtonType.Capsule })
41. // ...
42. .onClick(() => {
43. this.isUseInterception = !this.isUseInterception;
44. if (this.isUseInterception) {
45. // Register Interceptor.
46. this.registerInterception();
47. } else {
48. // Do not use interceptors.
49. this.pageInfos.setInterception(undefined);
50. }
51. })
52. Button($r('app.string.back'), { stateEffect: true, type: ButtonType.Capsule })
53. // ...
54. .onClick(() => {
55. this.getUIContext().getRouter().back();
56. })
57. }
58. // ...
59. }
60. // ...
61. }
62. }
```

[NavigationPage.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/pages/NavigationPage.ets#L17-L164)

## 埋点数据上传

如果需要将埋点数据上传至服务器，可以通过[@kit.PerformanceAnalysisKit](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)的[addWatcher()](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)方法添加订阅事件观察者、onTrigger()回调以及回调触发条件。可以自定义设置回调触发条件，比如在示例代码中当事件size大于等于1000字节时才会触发，然后在onTrigger()回调中调用http的request方法发起网络请求，将示例中的EXAMPLE\_URL替换为服务器的IP地址即可。

```
1. // entry\src\main\ets\entryability\EntryAbility.ets
2. const onTrigger = CallbackManager.getInstance().getOnTrigger();
3. hiAppEvent.addWatcher({
4. name: 'watcher1',
5. appEventFilters: [
6. {
7. domain: 'test_domain',
8. eventTypes: [hiAppEvent.EventType.FAULT, hiAppEvent.EventType.BEHAVIOR]
9. }
10. ],
11. triggerCondition: {
12. row: 10,
13. size: 1000,
14. timeOut: 1
15. },
16. onTrigger: onTrigger
17. })
18. hilog.info(0x0000, 'ApplicationTrack', '%{public}s', 'Succeeded in loading the content.');
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/application-track/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L80-L97)

## 总结

本文从绑定埋点数据入手，介绍三种埋点的开发实现：点击、曝光和页面埋点。最后调用hiAppEvent的addWatcher()方法添加订阅对象和onTrigger()回调，在回调中实现数据上报逻辑。

* 点击埋点：使用UIObserver的on("willClick")跟hiAppEvent的write()方法共同实现埋点操作，将埋点数据写入本地设备文件。
* 曝光埋点：使用setOnVisibleAreaApproximateChange跟hiAppEvent的write()方法共同实现埋点操作，将埋点数据写入本地设备文件。
* 页面埋点：使用UIObserver的on("navDestinationSwitch")跟hiAppEvent的write()方法共同实现埋点操作，将埋点数据写入本地设备文件。

## 示例代码

* [基于UIObserver能力的应用埋点](https://gitcode.com/harmonyos_samples/application-track)
