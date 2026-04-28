---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-latency-optimization-cases
title: 应用时延优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 应用启动与响应优化 > 应用时延优化
category: best-practices
scraped_at: 2026-04-28T08:22:32+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:2dc231992acc65eb9ca51c0fb3c92bea31b9570f38b9a72793cbe4b45462851f
---

## 应用时延概述

在移动终端应用开发中，完成时延是指用户操作移动终端时，从输入触控指令到界面完全刷新结束并达到可以阅读的稳定状态所用时间，点击时延依据界面转场类型可以分为界面内跳转和界面间跳转两种。完成时延作为用户体验关键指标，直接影响用户对响应速度和交互流畅性的感知，主要影响用户对触控交互及时性和愉悦性的体验评价。关于响应时延阶段的分析，请参考[《点击响应时延分析》](bpta-click-to-click-response-optimization.md)。关于完成时延阶段的分析，请参考[《点击完成时延分析》](bpta-click-to-complete-delay-analysis.md)。

在一定时延水平以上，时延越短越好，当时延小于一定水平后，用户的流畅体验不再继续提升。建议应用或元服务内点击操作响应时延应≤100ms，应用或元服务内点击操作完成时延≤900ms，更多体验建议，请参考指南[《应用性能体验建议》](../harmonyos-guides/performance-experience-suggestions.md)。本文将给出时延问题常见优化方案。

**图1** 点击完成起止点示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/MyUbz0pgT9uwC9jTY8x6OA/zh-cn_image_0000002229337521.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=F80CD9A6D2E8F51C5C0114DC965E818CAF331F91B9F4CDC42B80EF829834C5EC "点击放大")

**图2** 页面转场过程解析  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/B3Qsm1duQlKgK1eJiamEwg/zh-cn_image_0000002229452017.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=B1F48D8DCF4CD65335BF7E26606993D1621712B1E7E9AF1C9708DED370BA999A "点击放大")

## 常见时延问题优化方案

### UI优化

本节的示例是一个应用开发中常见的留言箱列表。

设计图稿显示，列表视图中的每个子项包含头像、消息红点、昵称、最新信息和时间等元素。

应用进入该页面时，根据每条消息的元素数据，呈现出不同的样式内容。

**图3** 留言箱列表界面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/4FJMjGtTRH6ByvsYGbXWhg/zh-cn_image_0000002229337533.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=4D2D76697ED27EC73C74F72220FE487250119E0C5E1E29A614E9B2A3C301D96A "点击放大")

分解关系结构后，单个子项界面由6个构成元素组成，元素排列以线性风格为主，使用的组件包括Image、Badge和Text。

**图4** 单个ListItem界面示意

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/MTCb4pEsQ7SqyiCk-WSizA/zh-cn_image_0000002193852136.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=72C58B56F077BB523D966880FF89247EE44121A36933E84784F08118CEA33558 "点击放大")

**具体实现**

* 熟悉弹性布局的开发者，得到需求后会第一时间使用Flex容器实现。界面主体呈线性结构，使用Flex作为包裹父容器，依次将横向纵向的元素添加进去，并设置其样式属性。通过DevEco Studio内置ArkUI Inspector工具，可以得到布局代码对应的视图树。实现结果从根节点到元素叶子节点最深处有6层，组件数目为15。这种实现方式，由于Flex容器默认情况下存在shrink等行为，绘制时会二次布局，造成页面渲染上的性能劣化。
* 接下来采用相对布局优化实现。先将左侧头像添加到容器中，然后锚定其位置，逐一在右侧添加其他元素。实现结果使用工具观察，发现层级相对减少，最终实现的层级是3层。同时，借助相对布局，子元素结构扁平化，容器也相对减少，进一步优化了页面的构建渲染时间。

**图5** Flex布局下的界面层级关系  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/9NlvKGUURF6XciSuuOBVLQ/zh-cn_image_0000002229452013.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=4E9A77DB8122BFE3E398DC04D02CAF5CF00D8DD40E9A464898067A25EE83F42A)

**图6** 相对布局下的界面层级关系

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/sWna8zPpQF2ZWuZCicr47w/zh-cn_image_0000002229452029.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=83B5BECE21AAD97D920EF8143D166A2BDDB9E883D15C109ECCCA61AD742E2448)

**统计分析**

在不同布局下，相同界面效果所需的组件数和嵌套层数不同。对本案例场景下的留言箱进行拆分，可以得到以下数目对比：

**表1** **不同布局下的数目对比**

|  | 组件数目 | 嵌套数目 |
| --- | --- | --- |
| Flex实现方式 | 15 | 6 |
| 相对布局实现方式 | 9 | 3 |

使用相同数据测试，记录从上一页面点击启动到留言箱列表渲染的响应时延，对比结果如下表：

**表2** **不同布局下的列表界面响应时长**

|  | 256条数据 | 512条数据 | 1024条数据 |
| --- | --- | --- | --- |
| Flex实现方式 | 308ms | 570ms | 1096ms |
| 相对布局实现方式 | 249ms | 499ms | 986ms |
| 优化百分比 | 19.2% | 12.5% | 10.0% |

从最后统计的数据来看：

* 形态单一的案例中，响应时长降低50ms以上，优化比提升10%以上。减少组件渲染数目和布局嵌套层级，有助于提升应用UI的绘制性能，减少响应时延。
* 随着加载数据量的提升，优化时长占比下降。列表在加载大量数据时，存在其他性能瓶颈，需要结合更多优化方法提升性能表现。

在实际开发中，简化布局结构和精简相关元素（包括绘制的子元素及其父容器）可以提升UI的响应速度。

### 并发优化

该示例是添加地址功能。点击“选择”按钮后，应用切换到选择城市地区的目标页。切换时，加载全国城市数据，按首字符排序，刷新列表。

在实际场景中，可以使用同步串行方式实现这一功能：点击按钮后，初始化页面，加载数据到内存，然后渲染界面视图。

当目标页选择范围到“市”这一行政级别时，数据量为1000条，新页面响应速度良好，没有明显异常。

如果功能需求调整，当目标页选择范围到“区”这一级别，数据量达到2000，页面响应速度仍然可以接受。

如果功能调整后，当目标页选择范围达到“乡镇/街道”这一级别时，数据量超过4000，页面响应将出现明显延迟。

地区数据的加载和排序都会消耗性能，可以使用并发机制来优化。

**代码实现**

在目标页面的aboutToAppear()中，使用TaskPool启动子线程加载城市数据，实现并发：

```
1. @Concurrent
2. function computeTask(): string[] {
3. let array: string[] = []
4. // AppConstant.CITYS is the data to be loaded.
5. for (let t of AppConstant.CITYS) {
6. array.push(t.trim())
7. }
8. let collator = new Intl.Collator("zh-CN", { localeMatcher: "lookup", usage: "sort" });
9. array.sort((a, b) => collator.compare(a, b))
10. return array;
11. }

13. @Entry
14. @Component
15. struct CityList {
16. isAsync: boolean = (this.getUIContext().getRouter().getParams() as Record<string, boolean>)['isAsync'];
17. // Interface data
18. @State citys: string[] = []
19. private listScroller: Scroller = new Scroller();

21. aboutToAppear() {
22. this.computeTaskAsync(); // Call asynchronous operation function
23. }

25. // Asynchronous thread
26. computeTaskAsync() {
27. let task: taskpool.Task = new taskpool.Task(computeTask);
28. taskpool.execute(task).then((res) => {
29. this.citys = res as string[]
30. })
31. }

33. // ...
34. }
```

[CityListPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/CityListPage.ets#L28-L137)

**统计分析**

使用Profiler Time工具，分别测试不同数量级别下的响应时长，得到结果如下：

**表3** **不同数据量的响应时长**

|  | 500条数据 | 1000条数据 | 2000条数据 | 4000条数据 |
| --- | --- | --- | --- | --- |
| 串行 | 49ms | 94ms | 296ms | 780ms |
| 并发 | 48ms | 86ms | 140ms | 172ms |

在该场景下，如果数据量小于1000，串行加载的用户体验可以保持良好。但随着城市数据量的增加，当数据量超过1000条时，响应时间显著增加，用户体验开始恶化。从手指抬起到页面转场进入列表页的第一帧画面，会出现明显的响应迟滞。

采用并发异步加载的优势在于，UI主线程可以快速拉起目标列表页面，同时触发异步加载和排序的逻辑线程。待结果返回后，再刷新列表，从而提升整体响应速度。

### 减少调用数据库API次数

本节示例是一个记账工具应用，其基于关系型数据库管理相关账目。

在查询用户数据时，会依次读取account表中每一行的数据，其中每一列column的值，需要借助getColumnIndex("列名")得到column索引，然后再取得对应值。

修改前代码：

```
1. for (let i = 0; i < count; i++) {
2. let tmp: AccountData = {
3. id: 0,
4. accountType: 0,
5. typeText: '',
6. amount: 0
7. };
8. tmp.id = resultSet.getDouble(resultSet.getColumnIndex('id'));
9. tmp.accountType = resultSet.getDouble(resultSet.getColumnIndex('accountType'));
10. tmp.typeText = resultSet.getString(resultSet.getColumnIndex('typeText'));
11. tmp.amount = resultSet.getDouble(resultSet.getColumnIndex('amount'));
12. result[i] = tmp;
13. resultSet.goToNextRow();
14. }
```

[AccountTable.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/common/db/AccountTable.ets#L42-L55)

在数据表结构固定的情况下，可以将getColumnIndex的调用提前，以减少总的调用次数，从而优化指令耗时。随着数据行数count的增加，for循环内的getColumnIndex调用次数也会增加，但索引不会变化。

修改后代码：

```
1. const idIndex = resultSet.getColumnIndex("id");
2. const accountTypeIndex = resultSet.getColumnIndex("accountType");
3. const typeTextIndex = resultSet.getColumnIndex("typeText");
4. const amountIndex = resultSet.getColumnIndex("amount");
5. for (let i = 0; i < count; i++) {
6. let tmp: AccountData = {
7. id: 0,
8. accountType: 0,
9. typeText: '',
10. amount: 0
11. };
12. tmp.id = resultSet.getDouble(idIndex);
13. tmp.accountType = resultSet.getDouble(accountTypeIndex);
14. tmp.typeText = resultSet.getString(typeTextIndex);
15. tmp.amount = resultSet.getDouble(amountIndex);
16. result[i] = tmp;
17. resultSet.goToNextRow();
18. }
```

[AccountTable.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/common/db/AccountTable.ets#L58-L75)

**统计分析**

使用Profiler Time工具，分别测试不同数量下的响应时长，得到结果如下：

**表4** **不同数据量的响应时长**

|  | 50条数据 | 500条数据 | 5000条数据 |
| --- | --- | --- | --- |
| 修改前 | 72ms | 97ms | 157ms |
| 修改后 | 72ms | 92ms | 110ms |

由此可以看出，在使用数据库时，需要关注相关API调用的潜在频率。

在数据条目数量较少时，API调用对应用响应的影响很小。随着使用时间的增加，数据量逐渐增大，API的高频调用将直接影响程序的性能。

### 延迟执行资源释放操作

该场景是相机正常使用后，执行释放相机资源的相关操作。通过“停止拍摄进程>暂停并释放相机会话>关闭和释放预览及拍照的输入输出对象>清空相机管理对象”的过程，确保应用程序在不再使用相机时能够有效管理并回收所有相机资源。但是，直接调用的release方法中，captureSession、cameraInput、previewOutput、cameraOutput都使用了await，导致相机关闭和释放操作顺序执行，可能会降低应用程序的响应性，引起用户界面卡顿。

下列代码将资源释放操作放在相机页面隐藏时触发的函数：

```
1. let cameraOutput: camera.PreviewOutput;
2. let cameraInput: camera.CameraInput;
3. let captureSession: camera.PhotoSession;
4. let previewOutput: camera.PhotoOutput;

6. // The camera page is triggered once every time it is hidden.
7. onPageHide() {
8. this.releaseCamera();
9. }

11. // Release resources
12. public async releaseCamera() {
13. try {
14. // Photo mode session class pause
15. await captureSession?.stop();
16. // Photo mode conversation class release
17. await captureSession?.release();
18. // The photo input object class is closed.
19. await cameraInput?.close();
20. // Preview output object class release
21. await previewOutput?.release();
22. // Photo output object class release
23. await cameraOutput?.release();
24. } catch (e) {
25. hilog.error(0x00, 'release input output error:', JSON.stringify(e));
26. }
27. }
```

[CameraPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/CameraPage.ets#L23-L58)

启动setTimeout异步延迟操作，在200毫秒后调用release释放并关闭相机。通过“停止拍摄进程>并发执行：暂停并释放相机会话>关闭和释放预览及拍照的输入输出对象>清空相机管理对象”的过程，确保应用程序在不再使用相机时能够有效管理并回收所有相机资源。移除await关键字应用于相机资源释放操作，允许异步并发执行，减少主线程阻塞，提升应用性能和响应速度。

```
1. let cameraOutput: camera.PreviewOutput;
2. let cameraInput: camera.CameraInput;
3. let captureSession: camera.PhotoSession;
4. let previewOutput: camera.PhotoOutput;

6. // The camera page is triggered once every time it is hidden.
7. onPageHide() {
8. setTimeout(this.releaseCamera, 200);
9. }

11. // Release resources
12. public async releaseCamera() {
13. try {
14. // Photo mode session class pause
15. await captureSession?.stop();
16. // Photo mode conversation class release
17. await captureSession?.release();
18. // The photo input object class is closed.
19. await cameraInput?.close();
20. // Preview output object class release
21. await previewOutput?.release();
22. // Photo output object class release
23. await cameraOutput?.release();
24. } catch (e) {
25. hilog.error(0x00, 'release input output error:', JSON.stringify(e));
26. }
27. }
```

[CameraOptPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/CameraOptPage.ets#L23-L58)

**性能比对**

**表5** 不同释放逻辑下的耗时

| 操作逻辑 | trace图识别耗时 | 备注 |
| --- | --- | --- |
| 直接关闭与释放（修改前） | 457.5ms | 在onPageHide中直接执行相机关闭与释放操作 |
| 延时关闭与释放（修改后） | 85.6ms | 在onPageHide中使用setTimeout延迟200ms后执行关闭与释放操作 |

两组数据显示，合理运用延时策略能够显著提高函数执行效率，是优化相机资源管理和关闭操作性能的有效方法，有助于提升整体用户体验。

### 减小拖动识别距离

该场景涉及为组件添加手势事件。优化前，设置触发拖动手势事件的最小拖动距离为100vp。代码如下：

```
1. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit'

3. @Entry
4. @Component
5. struct PanGestureExample {
6. @State offsetX: number = 0
7. @State offsetY: number = 0
8. @State positionX: number = 0
9. @State positionY: number = 0
10. private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right })

12. build() {
13. Column() {
14. Column() {
15. Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
16. }
17. .height(200)
18. .width(300)
19. .padding(20)
20. .border({ width: 3 })
21. .margin(50)
22. .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // Move with the upper left corner of the component as the coordinate origin.
23. // Drag left and right to trigger the gesture event.
24. .gesture(
25. PanGesture(this.panOption)
26. .onActionStart((event: GestureEvent) => {
27. console.info('Pan start')
28. hiTraceMeter.startTrace("PanGesture", 1)
29. })
30. .onActionUpdate((event: GestureEvent) => {
31. if (event) {
32. this.offsetX = this.positionX + event.offsetX
33. this.offsetY = this.positionY + event.offsetY
34. }
35. })
36. .onActionEnd(() => {
37. this.positionX = this.offsetX
38. this.positionY = this.offsetY
39. console.info('Pan end')
40. hiTraceMeter.finishTrace("PanGesture", 1)
41. })
42. )

44. Button('修改PanGesture触发条件')
45. .onClick(() => {
46. this.panOption.setDistance(100)
47. })
48. }
49. }
50. }
```

[PanGestureDistancePage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/PanGestureDistancePage.ets#L19-L69)

利用Profiler工具分析得到的trace图，重点关注两个trace标签：DispatchTouchEvent表示点击事件，PanGesture表示事件响应。追踪流程从应用侧的DispatchTouchEvent（type=0，表示手指接触屏幕）标签开始，到PanGesture（事件响应）的变化，整个过程耗时145.1毫秒。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/Yq5LcTEqQYaNIQ2iqO9SwA/zh-cn_image_0000002229337529.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=CEE9396ECC5862DF77437BAB3DF71D516E031817BD2C401239F0C77E25F2ECE3 "点击放大")

日志关注从应用接收TouchDown事件到pan识别的耗时，该过程耗时127ms。注：日志信息和trace图非同一时间获取，性能数据存在差异，提供的数值仅供参考。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/uvMs2RYeTPmQu1xvsTnuMg/zh-cn_image_0000002229452021.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=6980E112651712083028FDA1DFFCF77C1E87E81B983F7301683E6779D4B5D713 "点击放大")

针对该组件，其拖动手势识别距离可以调整到更合适的数值，这里优化后，指定触发拖动手势事件的最小拖动距离为4vp，代码如下：

```
1. Button('修改PanGesture触发条件')
2. .onClick(() => {
3. this.panOption.setDistance(4)
4. })
```

[PanGestureDistanceOptPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/PanGestureDistanceOptPage.ets#L62-L65)

同样采用Profiler工具分析trace图，得到对应耗时38.4ms

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/ADZHi8f7S1-zdV0gi9WxAg/zh-cn_image_0000002194011720.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=927D6350DBE513422854FF425D381DC1B22193E6E047A08ED4C553AF571B27F7 "点击放大")

对应日志过程耗时42ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/R3euGxlDQ5C8BlQoHfW3LA/zh-cn_image_0000002229452025.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=BAD8F5A12D0F573EB35CF7902691D48FC9F6C93122681DE6BBC44724AB10043E "点击放大")

**性能比对**

**表6** 不同拖动识别距离下的耗时

| 拖动距离设置 | trace图识别耗时 | 日志识别耗时 | 备注 |
| --- | --- | --- | --- |
| 最小拖动距离100vp（修改前） | 145.1ms | 127ms | 最小拖动距离过大可能导致滑动脱手和响应时延慢等问题，从而导致性能劣化 |
| 最小拖动距离4vp（修改后） | 38.4ms | 42ms | 设置合理的拖动距离可以优化性能 |

两组数据对比显示，适当减小拖动距离可显著提升执行效率，有效优化响应时延，从而显著改善整体用户体验。本案例通过设置较大和较小的拖动距离进行对比得出结论。设置过小的拖动距离容易导致误触等问题，建议开发者根据具体应用场景进行合理设置。

### 转场动画场景案例

下面的示例通过不同的连贯动画，使应用使用者在操作过程中感受到程序的快速响应。

该示例场景：从留言箱的列表项点击后，执行切换进入个人页。在这一过程中，使用了三个动画组成其完整过程：

* 在整体界面的切换过程，使用系统平台的转场动画，两个界面通过横向滑动完成切换。
* 转场动画中添加头像移动缩放的共享元素动画，体现响应元素的切换。
* 在个人页列表加载前，添加了列表轮廓的骨架图闪烁动画，让用户感知新页面的加载动态。

**图7** 场景实例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/6zxtixVDR9mSBUNttkqlxQ/zh-cn_image_0000002193852132.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=5DD0E4BDAE70761300989E997EC4743B92FBEEBFA09E2DC1E0F4B5A788A47D2C "点击放大")

**具体实现**

用router+sharedTransition+animateTo()的组合实现，具体操作思路如下：

1. 在两个页面中设置pageTransition()转场动画参数，然后在列表页头像的点击事件中添加router跳转，实现列表页到个人页的转场动画效果。
2. 在两个页面的头像组件Image中添加属性sharedTransition，并赋予相同的id以进行唯一匹配。同时，添加共享元素动画的时间等相关参数，实现头像从列表页向个人页移动的动画效果。
3. 根据个人页内容的版面样式，实现一个骨架图组件，并使用animateTo()添加反复渐显渐隐的动画行为。在个人页组件onAppear()时呈现该动画，具体内容刷新后隐藏动画元素。

**关键代码**

转场动画设置：

```
1. // page A Transition animation settings
2. pageTransition() {
3. PageTransitionEnter({ type: RouteType.None, duration: 400 })
4. .slide(SlideEffect.Left)
5. PageTransitionExit({ type: RouteType.None, duration: 400 })
6. .slide(SlideEffect.Left)
7. }
```

[VisionOptPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/VisionOptPage.ets#L30-L37)

列表页中共享元素动画设置：

```
1. // Use the avatar as a shared element in the list and specify the id as sharedImage+this.itemData.id
2. Image(this.itemData.avatar)
3. .height('40vp')
4. .width('40vp')
5. .borderRadius(8)
6. .sharedTransition('sharedImage' + this.itemData.id, { duration: 500, curve: Curve.FastOutSlowIn, delay: 0 })
```

[OptChatItemView.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/view/OptChatItemView.ets#L30-L35)

个人页中共享元素动画设置：

```
1. // The personal page sharing element needs to be the same as the previous page id.
2. Image(this.itemData.avatar)
3. .size({
4. width: $r('app.float.user_image_size'),
5. height: $r('app.float.user_image_size')
6. })// .borderRadius($r('app.float.user_image_border_radius'))
7. .borderRadius(8)
8. .margin({ bottom: $r('app.float.user_image_padding'), top: $r('app.float.user_image_padding') })
9. .sharedTransition('sharedImage' + this.itemData.id,
10. { duration: 500, curve: Curve.FastOutSlowIn, delay: 0 })
```

[ProfilePage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/ProfilePage.ets#L57-L66)

骨架图实现：

```
1. // Skeleton diagram, presenting skeleton animation in a fading way.
2. startAnimation(): void {
3. this.getUIContext().animateTo(CommonConstants.SKELETON_ANIMATION, () => {
4. this.listOpacity = CommonConstants.HALF_OPACITY;
5. });
6. }

8. // Skeletal diagram layout
9. build() {
10. Row() {
11. List({ space: Constants.RESOURCE_LIST_SPACE }) {
12. ForEach(SkeletonData, (item: SkeType) => {
13. ListItem() {
14. ArticleSkeletonView({ isMine: item.isMine, isFeed: item.isFeed })
15. }
16. })
17. }
18. .padding({
19. left: '12vp',
20. right: '12vp'
21. })
22. .lanes(1)
23. .layoutWeight(1)
24. .scrollBar(BarState.Off)

26. Row()
27. .layoutWeight(0)
28. .backgroundColor($r('app.color.skeleton_color_medium'))
29. }
30. .width('100%')
31. .opacity(this.listOpacity)
32. .onAppear(() => {
33. this.startAnimation();
34. })
35. }
```

[LoadingView.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/view/LoadingView.ets#L30-L65)

### 动画时延场景案例

页面转场动画对提升用户体验至关重要。动画时延过长会显著影响用户的点击完成时延，因为动画完成时间直接影响用户何时能开始与应用交互。动画时延的主要原因是动画时长设置过长。

常见的页面转场动画时长参数有：

1. [Tabs](../harmonyos-references/ts-container-tabs.md)组件设置TabContent切换动画时长，即[animationDuration](../harmonyos-references/ts-container-tabs.md#animationduration)属性。
2. [Swiper](../harmonyos-references/ts-container-swiper.md)组件设置子组件切换动画时长，即[duration](../harmonyos-references/ts-container-swiper.md#duration)属性。
3. 页面间转场（[pageTransition](../harmonyos-references/ts-page-transition-animation.md)）设置转场动画时长，即[PageTransitionOptions](../harmonyos-references/ts-page-transition-animation.md#pagetransitionoptions对象说明)对象中的duration字段。

使用Tabs组件进行页面切换时，当不设置BottomTabBarStyle时默认[animationDuration](../harmonyos-references/ts-container-tabs.md#animationduration)属性有300ms的动画时长，当该属性值设置过长时会导致完成时延变大。接下来将该属性值分别设置为100ms与1000ms来探究animationDuration属性对完成时延的影响。

实验一：设置animationDuration为100ms

```
1. @Entry
2. @Component
3. struct TabsPositiveExample {
4. @State currentIndex: number = 0;
5. private controller: TabsController = new TabsController();
6. private list: string[] = ['green', 'blue', 'yellow', 'pink'];

8. @Builder
9. customContent(color: Color) {
10. Column()
11. .width('100%')
12. .height('100%')
13. .backgroundColor(color)
14. }

16. build() {
17. Column() {
18. Row({ space: 10 }) {
19. ForEach(this.list, (item: string, index: number) => {
20. Text(item)
21. .textAlign(TextAlign.Center)
22. .fontSize(16)
23. .height(32)
24. .layoutWeight(1)
25. .fontColor(this.currentIndex === index ? Color.White : Color.Black)
26. .backgroundColor(this.currentIndex === index ? Color.Blue : '#f2f2f2')
27. .borderRadius(16)
28. .onClick(() => {
29. this.currentIndex = index;
30. this.controller.changeIndex(index);
31. })
32. }, (item: string, index: number) => JSON.stringify(item) + index)
33. }
34. .margin(10)

36. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
37. TabContent() {
38. this.customContent(Color.Green)
39. }

41. TabContent() {
42. this.customContent(Color.Blue)
43. }

45. TabContent() {
46. this.customContent(Color.Yellow)
47. }

49. TabContent() {
50. this.customContent(Color.Pink)
51. }
52. }
53. .animationDuration(100)
54. .layoutWeight(1)
55. .barHeight(0)
56. .scrollable(false)
57. }
58. .width('100%')
59. }
60. }
```

[TabsPositiveExample.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/TabsPositiveExample.ets#L22-L82)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/oBaKOjP5TLiF7MM05M6_nQ/zh-cn_image_0000002229337537.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=2C16D8E55564B609BC4EE1556F03C1F35428FB2E20C8278E1F88BB5E35ABF24A "点击放大")

实验二：设置animationDuration为1000ms

```
1. @Entry
2. @Component
3. struct TabsNegativeExample {
4. // ...
5. private controller: TabsController = new TabsController();

7. // ...

9. build() {
10. Column() {
11. // ...

13. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
14. // ...

16. }
17. .barHeight(0)
18. .layoutWeight(1)
19. .animationDuration(1000)
20. .scrollable(false)
21. }
22. .width('100%')
23. }
24. }
```

[TabsNegativeExample.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/OptimizationAppDelay/entry/src/main/ets/pages/TabsNegativeExample.ets#L22-L94)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/1I-zXkK3TT25GA9foRua1w/zh-cn_image_0000002229337525.png?HW-CC-KV=V1&HW-CC-Date=20260428T002230Z&HW-CC-Expire=86400&HW-CC-Sign=698F0EB3E8539CF40F02523059D14875638400AECC179EC5C0AAE06EA7AEB6C2 "点击放大")

**表7** 运行效果图

| 设置animationDuration为100ms | 设置animationDuration为1000ms |
| --- | --- |
|  |  |

**表8** animationDuration属性值对比

| animationDuration属性值 | 完成时延 |
| --- | --- |
| 100ms | 99ms39μs |
| 1000ms | 1s7ms693μs |

通过减少animationDuration属性的数值，可以减小Tabs组件切换动画的完成时延。如果不设置BottomTabBarStyle样式，动画时长默认为300毫秒。开发者可以根据实际业务场景，适当降低该动画时长，以提高应用性能。
