---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dispose-highly-loaded-component-render
title: 高负载场景分帧渲染
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 界面渲染性能优化 > 高负载场景分帧渲染
category: best-practices
scraped_at: 2026-04-28T08:22:31+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:d107b3d56e814f6418e3c97811f6861955ebecc471399a773dc439e08aa36001
---

## 概述

在应用开发中，页面内列表结构复杂，每个列表项包含的组件较多，就会导致嵌套层级较深，从而引起组件负载加重，绘制耗时增加。

在这种情况下，转场或者列表滑动的时候列表项就会一次性加载大量的数据，此时可以采用分帧渲染，将本来一帧内加载的数据分成多帧加载，但是分帧渲染需要开发者计算每帧中加载多少数据，操作复杂，因此在必要的情况下才推荐使用。

## 实现原理

### 原理说明

单帧内绘制多个特点各不相同的组件时，会同时创建数量较多的Graphics Pipelines，引发后续整个Flush阶段的耗时延长，从而导致单帧耗时超长。对于这种单帧内组件负载重、加载数据多和绘制耗时长的问题场景，开发者可以根据实际的业务逻辑、应用页面布局和数据量，提前计算规划出需要通过多少帧完成加载以及每帧具体加载的数据。应用页面实际加载绘制的时候，结合页面的布局，使用帧回调监听修改状态变量或补充数据到数据结构等方式，对每一帧需要处理的渲染数据进行计算和设置，保证每一帧内只处理提前设置好的数据。通过预先设置的帧回调监听，组件加载时可直接基于状态变量或数据结构实现分帧加载。这样就达到了原本在一帧中加载的数据分到多帧加载的目的，有效减少了首帧的耗时，避免首帧卡顿现象的出现。如下图所示，将一帧数据拆分到三帧示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Ft-Tsa_-TGGg2ZEoj1H5Mw/zh-cn_image_0000002229450329.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=A5F89A6DA061A9E591D837E1CB29F7313570AADEB9BDF93A255AFB290302129D)

### 具体实现

在高负载场景下使用分帧渲染的关键操作是把数据拆分到每一帧中加载，但这个过程中加载新的数据时可能会将已有数据再次绘制，因此需要搭配合理的页面布局来避免重绘。可以通过if或ForEach两种方法来实现布局，两种方法的更新机制如下：

* [if更新机制](../harmonyos-guides/arkts-rendering-control-ifelse.md#更新机制)是根据状态判断条件，如果分支没有变化，不会对条件渲染语句进行更新。
* [ForEach非首次渲染](../harmonyos-guides/arkts-rendering-control-foreach.md#非首次渲染)会检查新生成的键值是否在上次渲染中已经存在。如果键值不存在，则会创建一个新的组件；如果键值存在，则不会创建新的组件，而是直接渲染该键值所对应的组件。

因此在分帧逐步加载数据时使用上述两种方法不会引起重绘。并且在页面布局时可以给分帧渲染的外部容器组件设置宽高，这样组件本身不会触发重新进行Measure的过程，对组件的宽高不会重新测算，避免因外部容器大小改变引起重绘，详情可参考[合理使用布局](bpta-improve-layout-performance.md)。

保证页面不会重绘后，在实际开发过程中为了逐步增加页面数据，可以使用ArkTS中提供的[displaySync（可变帧率）](../harmonyos-references/js-apis-graphics-displaysync.md)API接口，通过Vsync信号控制数据刷新的时机，来实现绘制内容帧率的控制。先通过页面UI中aboutToAppear()添加帧回调监听并开启监听，Vsync信号变化时触发帧回调执行应用逻辑，计算每帧加载的数据，改变ViewModel数据。ViewModel数据改变后驱动页面或组件执行build()，使用if或ForEach分帧迭代渲染绘制UI并控制刷新范围。最后可以在aboutToDisappear()里停止帧回调监听。

具体操作流程如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/08PNIUQmQSScXMw6g8gB8w/zh-cn_image_0000002229450317.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=E79D220DA5123E10EC4E9312459C3296BBDEDBEC417C9878A4E279843F00F4BE)

## 转场场景

由于业务需求，从当前页面进入一个新页面时，会有转场动画播放，并且在动画首帧中加载新页面所需要的数据。如果数据量较多，那么动画首帧的响应时延就会变长，导致后面动画帧延迟播放的情况。从一个页面到新页面转场流程图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/y9mteT2aTtirPi3-badvTw/zh-cn_image_0000002229450337.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=6E7832B68F2089EC09D822FCF67197839D131C70B70AE9BDF3EE1E5616D97F9E "点击放大")

### 解决思路

既然转场时一次性加载大量的数据会导致卡顿情况，那么采用分帧渲染将数据拆分成多份并分批次进行加载就是一种解决思路。

转场场景分帧：转场时会在动画首帧加载新页面的数据，采用分帧策略就是将首帧加载的数据拆分，将数据拆分到后面的帧加载，新页面打开后List列表只展示两个列表项，因此在首帧加载显示两条数据，其余缓存数据可以在第二帧加载。该方法的优点是减少动画首帧的响应时间，缺点是转场动画完成时延变长。

转场场景效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/2RSGtTTJQZSOV4Mz-iVc8Q/zh-cn_image_0000002194010024.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=7DC7815FE7433928D2EB9B2FDB974B4C1C1CD167353E6DB4EF6522A613273A66 "点击放大")

在分帧前会在转场动画的首帧将层叠组件和列表可见区域与缓存区域的数据全部加载，而分帧后在首帧加载层叠组件和列表前两项的数据，在第二帧加载缓存区域的列表数据。分帧前后示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/5Dgob0XjQiKWs5z9oAkH6g/zh-cn_image_0000002229450333.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=416455869CFC1C4A3F200BF83B04239D3C8FF29D216B4C053CACD3D984AD13AD)

### 常规代码

通常情况下，在自定义列表组件中一次性加载全部数据，更新所有的列表项。

```
1. @Component
2. export struct TransitionScene {
3. private productData: ProductDetailSource = new ProductDetailSource();

5. aboutToAppear(): void {
6. this.productData.getProductData();
7. }

9. build() {
10. WaterFlow() {
11. LazyForEach(this.productData, (item: ProductDetailModel) => {
12. FlowItem() {
13. // ...
14. }
15. }, (item: ProductDetailModel) => item.id.toString())
16. }
17. // ...
18. }
19. }
```

[TestCode.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/FramedRendering/entry/src/main/ets/view/TestCode.ets#L5-L23)

这段代码里，在组件即将出现时回调aboutToAppear()接口，将数据放入productData中，并通过瀑布流加载。编译运行后，可以通过Trace图看到，转场动画的首帧耗时21ms左右，这是因为在点击进入页面时将数据全部放入瀑布流，在235970帧中需要计算每个子组件的尺寸，导致了响应时间增长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/c5ag98FYStOs26ZAwqKFnw/zh-cn_image_0000002229450305.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=1F7FC32869AACD520C30A9D0D18E73CF020482F1A49F55EA9D0064AF488FA146 "点击放大")

说明

* 上图是运行DevEco Studio中的Profiler工具结果Trace图，针对Frame运行的性能分析泳道。
* Actual TimeLane：橙色块235970为页面渲染第一帧的过程，橙色块235972为渲染第二帧的过程。
* Slice Details：应用渲染每帧的情况，Duration代表渲染此帧的耗时。如上图所示，第一帧耗时21ms，第二帧耗时4ms。
* Trace图帧分析详情请参考：[Frame分析](../harmonyos-guides/ide-insight-session-frame.md)。

### 优化代码

在aboutToAppear()接口中添加displaySync的帧回调，并将数据拆分进行加载。

```
1. @Entry
2. @Component
3. struct TransitionScene {
4. @State currentIndex: number = 0;
5. private readonly LIST_SPACE: number = 10;
6. private readonly FRAME_60: number = 60;
7. private readonly FRAME_120: number = 120;
8. private readonly SWIPER_CACHE: number = 2;
9. private readonly HORIZONTAL_LIST_CACHE: number = 2;
10. private swiperDataSource: SwiperDataSource = new SwiperDataSource();
11. private midListDataSource: MidListDataSource = new MidListDataSource();
12. private productDetailSource: ProductDetailSource = new ProductDetailSource();
13. private displaySync: displaySync.DisplaySync | undefined = undefined;
14. private frame: number = 1;

16. aboutToAppear(): void {
17. this.swiperDataSource.getProductData();
18. this.midListDataSource.getProductData();

20. // Creating a DisplaySync Object
21. this.displaySync = displaySync.create();

23. // Set the expected frame rate
24. let range: ExpectedFrameRateRange = {
25. expected: this.FRAME_120,
26. min: this.FRAME_60,
27. max: this.FRAME_120
28. };
29. this.displaySync.setExpectedFrameRateRange(range);

31. // Add Frame Callback
32. this.displaySync.on('frame', () => {
33. if (this.frame === 1) {
34. hiTraceMeter.startTrace('firstFrame', 1);
35. this.productDetailSource.getProductData(0, 2);
36. this.frame += 1;
37. hiTraceMeter.finishTrace('firstFrame', 1);
38. } else if (this.frame === 2) {
39. hiTraceMeter.startTrace('secondFrame', 2);
40. this.productDetailSource.getProductData(2, 10);
41. hiTraceMeter.finishTrace('secondFrame', 2);
42. this.frame += 1;
43. this.displaySync?.stop();
44. }
45. });

47. // Enable frame callback listening
48. this.displaySync.start();
49. }

51. aboutToDisappear(): void {
52. if (this.displaySync) {
53. this.displaySync.stop();
54. this.displaySync.off('frame');
55. this.displaySync = undefined;
56. }
57. }

59. build() {
60. Column() {
61. Search({ placeholder: $r('app.string.search_title') })
62. this.typeSwiper();
63. this.typeList();
64. this.typeWaterFlow();
65. }
66. .padding({
67. left: 16,
68. right: 16
69. })
70. }
```

[TransitionScene.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/FramedRendering/entry/src/main/ets/view/TransitionScene.ets#L24-L93)

在这段代码中，aboutToAppear()接口中并没有一次性加载全部数据，而是将数据拆分，在帧回调中分成2次进行加载，编译运行后，通过Trace图可以看到，动画首帧的耗时是12ms。相较于优化前的代码，不再是首帧占据大量的时间，而是将耗时分摊到了后面的动画帧中。当数据量更大时，可以将数据进行更多次拆分，将不会直接出现在屏幕上的数据放到第二帧或者第三帧中进行加载，降低首帧的响应时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/AlfZ72ocTheb1BGzMNtbtQ/zh-cn_image_0000002229450341.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=03BADD9DAFD6DFE7ED7E9F83F64D35C8A3BD6C72C3F60AF064DDC68CAD93EB1E "点击放大")

对使用分帧前后进行分析，得到的数据如下表所示：

**表1** 使用分帧前后耗时对比

| 使用分帧 | 使用分帧前 | 使用分帧后 |
| --- | --- | --- |
| 首帧耗时 | 21ms | 12ms |
| 第二帧耗时 | 4ms | 13ms |

在使用分帧后动画首帧与第二帧分别是12ms和13ms，如果依然没有达到期望的帧率，可以继续将数据拆分。

## 滑动场景

在日历应用中，需要在一个List里面加载每个月的全部天数，包括公历和农历日期，这样在一个ItemView复用组件中就会有很多数据加载，当列表滑动的时候，通过组件复用的aboutToReuse()接口设置新的数据，就会导致ItemView内所有组件一起刷新，可能会引起掉帧卡顿现象。

### 解决思路

由于一次性加载大量数据、刷新大量组件会导致卡顿丢帧，那么减少一次性加载的数据量就是一种解决方法。但是由于业务需求，需要加载的数据总量和绘制的组件数量是不能减少的，那么就可以考虑采用分帧渲染。

滑动场景分帧：滑动日历列表，复用ItemView组件，更新每月天数包含阴历和阳历，一次更新所有天数，数据量大，可以使用分帧策略，将每月日期数据进行拆分，一帧只更新5天数据，在使用ForEach循环每月的天数时，因为一次只更新5天数据，ForEach会根据key值更新对应的天数，从而避免在一帧中更新所有数据。该方法优点是可以将数据拆分在多帧中加载；缺点是操作比较麻烦，需要开发者根据实际情况计算一帧中加载的数据量，维护较为复杂。

滑动场景效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/bZ-aybS_RZqBjoT61eOW5A/zh-cn_image_0000002229450321.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=59842614CA1660F0F939EF9286E7C2A5C0E0A646B3BE5014A8AF15D11B3198F8 "点击放大")

分帧前后示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Ownvu3N5Qg20Af7hFa2Eaw/zh-cn_image_0000002229450313.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=52381138AF1699EF4CB2EED76C8752A22AE9B22F1F3D6DAE331290B12B3C5785 "点击放大")

### 常规代码

通常情况下，会在aboutToReuse()中设置新的数据，并一次性绘制所有的组件。

```
1. @Reusable
2. @Component
3. export struct DateItemView {
4. @State monthItem: Month = {
5. month: '',
6. num: 0,
7. days: [],
8. lunarDays: [],
9. year: 0
10. };
11. // ...
12. aboutToReuse(params: Record<string, Object>): void {
13. hiTraceMeter.startTrace('reuse_' + (params.monthItem as Month).month, 1);
14. this.monthItem = params.monthItem as Month;
15. hiTraceMeter.finishTrace('reuse_' + (params.monthItem as Month).month, 1);
16. }

18. build() {
19. Flex({ wrap: FlexWrap.Wrap }) {
20. // ...
21. ForEach(this.monthItem.days, (day: number, index: number) => {
22. // ...
23. }, (index: number): string => index.toString())
24. }
25. // ...
26. }
27. }
```

[TestCode.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/FramedRendering/entry/src/main/ets/view/TestCode.ets#L29-L55)

在上面的代码中，通过组件复用，在ItemView的aboutToReuse()接口中，将一个月的数据直接设置到状态变量monthItem中，这样下面的Flex就会收到状态变量变更的消息通知，从而刷新组件中的数据。编译运行后，进入日历页面，然后滑动列表到最底端，分析下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/TuQSa353SfuAfSMnEtbZzA/zh-cn_image_0000002229450325.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=5370844A8029E5895BB2AECA4896B2D85B4D06FBB3CE9256EA50B640C6DE9296 "点击放大")

* 选中Actual Timeline（render\_service）标签中的146272后，可以通过箭头看到它所关联到的位置是Actual Timeline（example.display）标签中的209136和209137，即RenderService层出现的异常情况是由应用层中前面两帧里面的操作引起的。
* 通过箭头2的标签可以看到，在209135中调用了aboutToReuse接口，此时系统开始了组件复用的绘制操作，在aboutToReuse接口将一个月的所有数据全部放入了当前被复用的组件中，并更新了所有用于显示日期的Text组件中的数据（箭头3，diffIndexArray.length：35，表示有35个不同的元素），这就导致209136需要计算35个子组件的尺寸（箭头1），从而引起146272的绘制时间延长。
* 在列表数据量较少时，其实并不会引起掉帧现象，因为每次延长帧的时间都很短，对帧率的影响较小，但是在列表数据较多时，就会因为延长帧过多，发生掉帧现象。

### 优化代码

通过displaySync中的帧回调方法，将数据拆分到每一帧中进行加载和绘制，只需要在帧回调中修改自定义子组件ItemView中加载数据的方式。

首先，需要在ItemView中第一次使用时创建displaySync对象，设置期望帧率，添加帧回调的监听，然后进行启动。

```
1. @Reusable
2. @Component
3. export struct DateItemView {
4. // ...
5. aboutToAppear(): void {
6. hiTraceMeter.startTrace('appear_', 1);
7. this.displaySync = displaySync.create();
8. const range: ExpectedFrameRateRange = {
9. expected: 120,
10. min: 60,
11. max: 120
12. };
13. this.displaySync.setExpectedFrameRateRange(range);
14. this.displaySync.on('frame', () => {
15. // ...
16. });
17. this.displaySync.start();
18. allDisplaySyncArray.push(this.displaySync);
19. this.temp.push(this.monthItem);
20. hiTraceMeter.finishTrace('appear_', 1);
21. }
22. // ...
23. }
```

[DateItemView.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/FramedRendering/entry/src/main/ets/view/DateItemView.ets#L29-L182)

然后，在监听中添加更新数据的代码。这里将每个月的数据更新拆分开来，第一步用来更新月份数据和计算总的执行步骤，最后一步将计数数据清空， 方便下一次数据的写入，其余需要执行步骤的多少根据每次加载数据量会有所改变。

```
1. if (this.temp.length > 0) {
2. if (this.step === 0) {
3. // Step 1: Add the monthly data and calculate the maximum number of frames required to complete the data operation.
4. hiTraceMeter.startTrace('reuse_' + this.step, 1);
5. this.month = this.temp[0].month;
6. this.monthNumber = this.temp[0].num;
7. this.maxStep = this.maxStep + Math.ceil(this.temp[0].days.length / this.MAX_EVERY_FRAME);
8. hiTraceMeter.finishTrace('reuse_' + this.step, 1);
9. this.step += 1;
10. } else if (this.step === this.maxStep - 1) {
11. // Final step: Initialize partial count data.
12. this.temp = [];
13. this.step = 0;
14. this.maxStep = 2;
15. } else {
16. hiTraceMeter.startTrace('reuse_' + this.step, 1);
17. const start: number = this.MAX_EVERY_FRAME * (this.step - 1);
18. const end: number = (this.MAX_EVERY_FRAME * this.step) > this.temp[0].days.length ?
19. this.temp[0].days.length : this.MAX_EVERY_FRAME * this.step;
20. for (let i = start; i < end; i++) {
21. this.days[i] = this.temp[0].days[i];
22. this.lunarDays[i] = this.temp[0].lunarDays[i];
23. }
24. hiTraceMeter.finishTrace('reuse_' + this.step, 1);
25. this.step += 1;
26. }
27. }
```

[DateItemView.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/FramedRendering/entry/src/main/ets/view/DateItemView.ets#L79-L105)

最后，在aboutToReuse接口中将数据放入数组中，用于帧回调中开始执行数据更新。

```
1. aboutToReuse(params: Record<string, Object>): void {
2. hiTraceMeter.startTrace('reuse_' + (params.monthItem as Month).month, 1);
3. this.temp.push(params.monthItem as Month);
4. hiTraceMeter.finishTrace('reuse_' + (params.monthItem as Month).month, 1);
5. }
```

[DateItemView.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/FramedRendering/entry/src/main/ets/view/DateItemView.ets#L52-L56)

分析下面trace图，在211618中，开始调用aboutToReuse接口，由于只是将数据放入一个temp数组中，并没有更新复用组件中的数据，所以这一帧并没有发生延长现象。

在211619中开始逐步更新复用组件中的数据，在第一帧中更新月份和周的数据，但是由于前一帧（211618）中并没有更新当前复用组件中的数据，所以在211619中并不需要绘制组件，所以此帧耗时依旧很短。

结合代码可以看到，在211620中放入了5天的日期数据，由于前一帧（211619）只是设置了2条数据，并且只有1条会更新，所以这一帧的绘制时间也不会超时。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/qekkWKBFTj6Sl0CUZV99hQ/zh-cn_image_0000002229450345.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=2FA3E43F2CAB20ACE56265D7BA1BCD0DEC0C5AB664DB4FC460DE697738A4B3B4 "点击放大")

和前一帧（211620）一样，此帧（211621）中更新了5天的日期数据，并且会重新测量上一帧中更新数据的5个Text组件尺寸（箭头1），而其余的组件由于数据并没有变动，所以测量被略过了（箭头2）。

后面的帧是类似的，每次只会放入5天的数据，并且更新上一帧中设置的数据所关联的Text组件。由于每次更新的组件数量较少，每帧基本上都能在规定的时间内（1秒120帧，即8ms一帧）绘制完成，所以延长帧就会较少。这样不论列表中数据多还是少，都不会引起掉帧现象的发生。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/brZ8M2cnS8ytNFpdkE-gTw/zh-cn_image_0000002229450309.png?HW-CC-KV=V1&HW-CC-Date=20260428T002228Z&HW-CC-Expire=86400&HW-CC-Sign=CDCAF5E3A9E0108D348B9A9126F52C960140B295AA8F475AB16E0111C1D54D59 "点击放大")

**表2** 使用分帧前后对比

| 使用分帧 | 使用分帧前 | 使用分帧后 |
| --- | --- | --- |
| 渲染帧率 | 113fps | 120fps |
| 丢帧率 | 5.8% | 0% |

在使用displaySync时不建议将ExpectedFrameRateRange中的expected、min、max都设置为120，否则会干扰系统的可变帧率机制运行，产生不必要的负载，进而影响到整机的性能和功耗，详情请参考[场景策略建议](bpta-ltpo-description.md#section12516101118180)。

## 总结

通过上面的示例代码和优化过程，可以看到在列表中使用组件复用时，一次性全部加载时可能会引起掉帧。虽然在数据量较少时，单帧绘制的延长并不会引起掉帧，但是数据量变多后，这种延长帧的影响就会比较明显。根据自己实际业务需求合理使用分帧策略进行数据拆分后，可以有效减少延长帧的发生，从而减少掉帧引起的性能问题。

## 示例代码

* [基于分帧渲染实现应用界面优化](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/FramedRendering)
