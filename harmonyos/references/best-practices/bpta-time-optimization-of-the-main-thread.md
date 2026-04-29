---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread
title: 主线程耗时操作优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 界面渲染性能优化 > 主线程耗时操作优化
category: best-practices
scraped_at: 2026-04-29T14:13:33+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5bbbfaddb0bfe235cc6af2c30be994a889cf27b07d599382bd1b76058870f5dd
---

## 概述

在应用开发实践中，有效避免主线程执行冗余与易耗时操作是至关重要的策略。此举能有效降低主线程负载，提升UI的响应速度。面对高频回调接口在短时间内密集触发的场景，需要避免接口内的耗时操作，尽量保证主线程不被长时间占用，从而防止阻塞UI渲染，引发界面卡顿。本文介绍开发过程中常见的冗余操作，常见的高频回调场景以及其他主线程优化思路。

## 常见冗余操作

在软件开发中，冗余操作指的是那些不必要、重复执行且对程序功能无实质性贡献的操作。这些操作不仅会浪费计算资源，还可能降低程序的运行效率，特别是在高频调用的场景下，其负面影响更为显著。下面列举一些release版本中常见的冗余操作：

* debug日志打印
* Trace打点
* 冗余空回调

  说明

  建议开发者优先使用[Code Linter扫描工具](../harmonyos-guides/ide-code-linter.md)进行代码检查，重点关注[@performance/hp-arkui-avoid-empty-callback](../harmonyos-guides/ide_hp-arkui-avoid-empty-callback.md)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

【反例】：release版本中冗余日志打印，Trace打点，以及无业务代码的空回调

```
1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';

3. // Redundant operations are counterexamples
4. @Entry
5. @Component
6. struct RedundantOperation {
7. private arr: number[] = [];

9. aboutToAppear(): void {
10. for (let i = 0; i < 500; i++) {
11. this.arr[i] = i;
12. }
13. }

15. build() {
16. Column() {
17. Row({ space: 5 }) {
18. Column() {
19. Image($r('app.media.chevron_left'))
20. .width(16)
21. .height(16)
22. }
23. .width(40)
24. .height(40)
25. .justifyContent(FlexAlign.Center)
26. .backgroundColor('#E8E8E8')
27. .borderRadius(40)
28. .onClick(() => {
29. this.getUIContext().getRouter().back({
30. url: 'pages/Index'
31. });
32. })

34. Text('Redundant operations')
35. .fontSize(20)
36. .fontWeight(700)
37. .height(26)
38. }
39. .width('100%')
40. .height(56)
41. .margin({ top: 36 })

43. Scroll() {
44. List() {
45. ForEach(this.arr, (item: number) => {
46. ListItem() {
47. Text('TextItem' + item)
48. .width('100%')
49. .padding({ left: 12 })
50. }
51. .onAreaChange(() => {
52. // No business operations
53. // Negative example.
54. })
55. .width('100%')
56. .height(48)
57. }, (item: number) => item.toString())
58. }
59. .divider({ strokeWidth: 1, color: '#F5F5F5' })
60. .width('100%')
61. .height('100%')
62. }
63. .width('100%')
64. .height('86%')
65. .margin({ top: 8 })
66. .backgroundColor(Color.White)
67. .borderRadius(20)
68. .onWillScroll(() => {
69. hiTraceMeter.startTrace('ScrollSlide', 1001);

71. hilog.debug(0x0000, 'Sample', 'Debug %{public}s', 'contents: logs');
72. // Business logic
73. // ...
74. hiTraceMeter.finishTrace('ScrollSlide', 1001);
75. })
76. }
77. .backgroundColor('#F5F5F5')
78. .height('100%')
79. .padding({ left: 16, right: 16, bottom: 16 })
80. }
81. }
```

[RedundantOperation.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/RedundantOperation.ets#L17-L99)

【正例】：release版本中删除冗余的debug日志，Trace打点以及无业务代码的空回调

```
1. // Redundancy operation example
2. @Entry
3. @Component
4. struct NoRedundantOperation {
5. private arr: number[] = [];

7. aboutToAppear(): void {
8. for (let i = 0; i < 500; i++) {
9. this.arr[i] = i;
10. }
11. }

13. build() {
14. Column() {
15. Row({ space: 5 }) {
16. Column() {
17. Image($r('app.media.chevron_left'))
18. .width(16)
19. .height(16)
20. }
21. .width(40)
22. .height(40)
23. .justifyContent(FlexAlign.Center)
24. .backgroundColor('#E8E8E8')
25. .borderRadius(40)
26. .onClick(() => {
27. this.getUIContext().getRouter().back({
28. url: 'pages/Index'
29. });
30. })

32. Text('No redundant operations')
33. .fontSize(20)
34. .fontWeight(700)
35. .height(26)
36. }
37. .width('100%')
38. .height(56)
39. .margin({ top: 36 })

41. Scroll() {
42. List() {
43. ForEach(this.arr, (item: number) => {
44. ListItem() {
45. Text('TextItem' + item)
46. .width('100%')
47. .padding({ left: 12 })
48. }
49. .width('100%')
50. .height(48)
51. }, (item: number) => item.toString())
52. }
53. .divider({ strokeWidth: 1, color: '#F5F5F5' })
54. .width('100%')
55. .height('100%')
56. }
57. .margin({ top: 8 })
58. .width('100%')
59. .height('86%')
60. .backgroundColor(Color.White)
61. .borderRadius(20)
62. .onWillScroll(() => {
63. // Business logic
64. // ...
65. }
66. }
```

[NoRedundantOperation.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/NoRedundantOperation.ets#L19-L92)

**图1** 反例标签"H:ScrollSlide"Trace图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/mN8eFKeNQdCvocrYk1cjlg/zh-cn_image_0000002193850140.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=FE3E67B59D76D77E4755E733D7A0E70C5BFC47F67E9C67F0C08A9B84B0BF29EC "点击放大")

通过上图可知，在3.5s的滑动过程中，总计触发了424次日志打印以及Trace追踪，打印一次日志的平均耗时为84μs，由此可以计算出冗余的debug日志浪费了35.616ms。release版本建议删除无效日志的打印。

对于回调函数体内不包含任何业务逻辑代码的冗余回调而言，即使开发者在回调函数内部未进行任何实质性的操作，只要注册了回调接口，如onAreaChange，系统底层仍会耗费资源去监测对应事件的发生，例如计算组件的位置或大小变化，并将这些数据传递给ArkTS侧。即使这些数据最终在ArkTS层没有被有效利用，底层的计算和通信开销已然存在。所以，为了避免不必要的资源消耗，提升应用性能，应当仔细审查并移除这类无实际用途的回调函数注册。开发过程中，除了需要避免冗余操作，还需要注意避免在高频回调场景执行耗时操作，接下来介绍一下高频回调场景以及需要避免的耗时操作。

## 高频回调场景

高频回调接口通常是指在应用程序运行过程中会被频繁触发的事件或回调函数，以下常见高频回调场景中需要避免执行耗时操作:

* [高频事件回调](bpta-time-optimization-of-the-main-thread.md#section204221336134312)
* [组件复用回调](bpta-time-optimization-of-the-main-thread.md#section20815336174316)
* [组件生命周期回调](bpta-time-optimization-of-the-main-thread.md#section418843713435)
* [循环渲染](bpta-time-optimization-of-the-main-thread.md#section4551193714439)
* [组件属性](bpta-time-optimization-of-the-main-thread.md#section166841738154316)

### 高频事件回调

例如，触摸事件、拖拽事件、移动事件、组件区域变化事件、滑动事件等系统事件在应用程序运行过程中会被频繁触发，如果在这些回调接口中执行耗时操作，将导致应用出现卡顿丢帧的问题。下方是基于Scroll组件滑动时会高频调用onWillScroll的场景，分析性能差异。

**场景案例**

【案例一】在onWillScroll回调中执行耗时操作

```
1. // onWillScroll high-frequency event callback counterexample
2. @Entry
3. @Component
4. struct NegativeOfOnScroll {
5. private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

7. count(): number {
8. let temp: number = 0;
9. for (let i = 0; i < 1000000; i++) {
10. temp += 1;
11. }
12. return temp;
13. }

15. build() {
16. Column() {
17. Row({ space: 5 }) {
18. Column() {
19. Image($r('app.media.chevron_left'))
20. .width(16)
21. .height(16)
22. }
23. .width(40)
24. .height(40)
25. .justifyContent(FlexAlign.Center)
26. .backgroundColor('#E8E8E8')
27. .borderRadius(40)
28. .onClick(() => {
29. this.getUIContext().getRouter().back({
30. url: 'pages/Index'
31. });
32. })

34. Text($r('app.string.negative_of_onScroll'))
35. .fontSize(20)
36. .fontWeight(700)
37. .height(26)
38. }
39. .width('100%')
40. .height(56)
41. .margin({ top: 20 })

43. Scroll() {
44. List() {
45. ForEach(this.arr, (item: number) => {
46. ListItem() {
47. Text('TextItem' + item)
48. .width('100%')
49. .padding({ left: 12 })
50. }
51. .width('100%')
52. .height(48)
53. }, (item: number) => item.toString())
54. }
55. .divider({ strokeWidth: 1, color: '#F5F5F5' })
56. .width('100%')
57. .height('100%')
58. }
59. .width('100%')
60. .height(492)
61. .margin({ top: 8 })
62. .backgroundColor(Color.White)
63. .borderRadius(20)
64. .onWillScroll(() => {
65. hiTraceMeter.startTrace('ScrollSlide', 1001);
66. hilog.info(0x0000, 'Sample', '%{public}s', 'Scroll TextItem');
67. // Time-consuming operation
68. this.count();
69. // Business logic
70. // ...
71. hiTraceMeter.finishTrace('ScrollSlide', 1001);
72. })
73. }
74. .padding(16)
75. .height('100%')
76. .backgroundColor('#F5F5F5')
77. }
78. }
```

[NegativeOfOnScroll.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/NegativeOfOnScroll.ets#L19-L97)

【案例二】onWillScroll回调中不执行耗时操作

```
1. // onWillScroll high-frequency event callback positive example
2. @Entry
3. @Component
4. struct PositiveOfOnScroll {
5. private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

7. build() {
8. Column() {
9. Row({ space: 5 }) {
10. Column() {
11. Image($r('app.media.chevron_left'))
12. .width(16)
13. .height(16)
14. }
15. .width(40)
16. .height(40)
17. .justifyContent(FlexAlign.Center)
18. .backgroundColor('#E8E8E8')
19. .borderRadius(40)
20. .onClick(() => {
21. this.getUIContext().getRouter().back({
22. url: 'pages/Index'
23. });
24. })

26. Text($r('app.string.positive_of_onScroll'))
27. .fontSize(20)
28. .fontWeight(700)
29. .height(26)
30. }
31. .width('100%')
32. .height(56)
33. .margin({ top: 20 })

35. Scroll() {
36. List() {
37. ForEach(this.arr, (item: number) => {
38. ListItem() {
39. Text('TextItem' + item)
40. .width('100%')
41. .padding({ left: 12 })
42. }
43. .width('100%')
44. .height(48)
45. }, (item: number) => item.toString())
46. }
47. .divider({ strokeWidth: 1, color: '#F5F5F5' })
48. .width('100%')
49. .height('100%')
50. }
51. .width('100%')
52. .height(492)
53. .margin({ top: 8 })
54. .backgroundColor(Color.White)
55. .borderRadius(20)
56. .onWillScroll(() => {
57. hiTraceMeter.startTrace('ScrollSlide', 1001);
58. hilog.info(0x0000, 'Sample', '%{public}s', 'Scroll TextItem');
59. // Business logic
60. // ...
61. hiTraceMeter.finishTrace('ScrollSlide', 1001);
62. })
63. }
64. .padding(16)
65. .height('100%')
66. .backgroundColor('#F5F5F5')
67. }
68. }
```

[PositiveOfOnScroll.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/PositiveOfOnScroll.ets#L19-L87)

**结果对比**

下面将通过自定义Trace打点，统计不同案例场景下，单次onWillScroll事件回调的耗时差异，帧率差异以及分析。

* 耗时对比

**图2** 案例一onWillScroll事件回调耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/F7Dz9OdHQm6SwDJlwmI5eg/zh-cn_image_0000002194009712.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=7D2BE87649C83969AAD4998BD89E26F69DE71E1638E39AEBEF0484CE48B82A83 "点击放大")

**图3** 案例二onWillScroll事件回调耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/FDJbZQYkRweumRuSa_EE1Q/zh-cn_image_0000002194009728.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=6C2753D8D1AE129C0B1AB00E91BDED94F61B91ED1D4FE1C42D95548C3A328FFD "点击放大")

* 帧率对比

**图4** onWillScroll执行耗时操作的丢帧率  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/9hVHUx1bTHW5ARGJqmOqyA/zh-cn_image_0000002194009704.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=BBAF2CA7F2A86C85CC3052C58AE9F6A9C2E7B89533BC7C7AB5E3DFA233E11D7F "点击放大")

**图5** onWillScroll不执行耗时操作的丢帧率  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Kh07ZLbfTLuQbhnSnldbeA/zh-cn_image_0000002193850112.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=AB3E39F6AD8500316288C537AF77021CDBED0F5AFDA316371161141388731D65 "点击放大")

**图6** 首帧Trace详细信息  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/m8u4g4awR1CRRtN0uIuncA/zh-cn_image_0000002231669457.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=C55187FD711186A38B62A267E876F25B5886E92613339FA2C1B78E9C7AD09839 "点击放大")

通过图2、图3可知，onWillScroll事件回调中带有耗时操作，会占用主线程20ms左右的时间。由图4可知在具有耗时操作的滑动过程中，丢帧率高达87.5%。观察图6卡顿首帧Trace的详细信息发现，原本期望完成时间为8.3ms。因为onWillScroll中耗时操作的影响，使得实际处理时间为25ms，远超期望时间，短时间内连续触发该回调就会导致发生连续丢帧现象。因此在开发过程中，开发者应该尽量避免在高频事件回调中处理耗时操作，否则将导致应用性能大幅下降。

说明

本案例在onWillScroll事件回调的开始开启打点追踪，在事件回调结束前停止性能打点追踪，用以测试有无耗时操作的性能差异。关于本例中使用性能打点的介绍，请参考[@ohos.hiTraceMeter (性能打点)](../harmonyos-references/js-apis-hitracemeter.md)。案例中关于帧率检测，丢帧分析，请参考[帧率问题分析](bpta-zhenlv.md)。

由于本章节各场景的帧率数据统计以及分析步骤与方式大体一致，下文将不再对各场景的帧率进行重复统计分析。

### 组件复用回调

在滑动场景中，使用组件复用通常需要用生命周期回调aboutToReuse去更新组件的状态变量。在滑动时，aboutToReuse会被频繁调用。如果在aboutToReuse中进行了耗时操作，将导致应用出现卡顿丢帧的问题。下面的案例将基于Grid懒加载组件复用场景进行分析。

**场景案例**

【反例】：在aboutToReuse中进行耗时操作

```
1. // ...
2. // Simulate time-consuming operations with loop functions
3. count(): number {
4. let temp: number = 0;
5. for (let index = 0; index < 1000000; index++) {
6. temp += 1;
7. }
8. return temp;
9. }

11. aboutToReuse(params: Record<string, number>): void {
12. hiTraceMeter.startTrace('ReuseOfGrid', 1001);
13. this.item = params.item;
14. // Simulate time-consuming operations
15. this.count();
16. hiTraceMeter.finishTrace('ReuseOfGrid', 1001);
17. }

19. // ...
```

[NegativeOfGrid.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/NegativeOfGrid.ets#L110-L130)

【正例】：在aboutToReuse中不进行耗时操作

```
1. // ...
2. aboutToReuse(params: Record<string, number>): void {
3. hiTraceMeter.startTrace('ReuseOfGrid', 1001);
4. this.item = params.item;
5. hiTraceMeter.finishTrace('ReuseOfGrid', 1001)
6. }

8. // ...
```

[PositiveOfGrid.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/PositiveOfGrid.ets#L110-L117)

**结果对比**

**图7** 反例滑动时单个aboutToReuse耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/_0fbSFjrQZSg760_H2ADaw/zh-cn_image_0000002194009716.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=2689F83163E7DCCAFFAE932F812B3D5A0412122C8EB92922DACCF0A4B0B81DDA "点击放大")

**图8** 正例滑动时单个aboutToReuse耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/wJ6f2rGdTqCYCN2Crd_OAQ/zh-cn_image_0000002231555137.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=2543AF5FF56CEEFB80FBBB0F2556D87AD4F77FE52E749ACA3A36D8A803BF95EC "点击放大")

如图7所示，从反例Trace中“H:ReuseOfGrid”标签可以看出，单个aboutToReuse执行耗时20ms。而从图8正例Trace中“H:ReuseOfGrid”标签看，单个aboutToReuse执行耗时仅56μs。带有耗时操作的单个aboutToReuse执行耗时远超期望时间8.3ms，在Grid滑动高频调用aboutToReuse的场景中，将会导致应用连续丢帧卡顿，性能大幅下降。因此，组件复用时应避免在aboutToReuse中执行耗时操作。

### 组件生命周期回调

在需要频繁创建和销毁组件的场景中，将会频繁调用组件生命周期回调aboutToAppear，aboutToDisappear。下面是一个使用条件渲染，通过点击按钮切换自定义组件A和B来模拟频繁创建和销毁组件的场景示例。

在自定义组件A，B的生命周期回调函数aboutToAppear和aboutToDisappear中加入耗时操作。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct MyComponent {
6. // Toggles the custom component flag
7. @State flag: boolean = false;

9. build() {
10. Column({ space: 10 }) {
11. Row({ space: 5 }) {
12. Column() {
13. // $r('app.media.chevron_left') It needs to be replaced with the resources required by the developers
14. Image($r('app.media.chevron_left'))
15. .width(16)
16. .height(16)
17. }
18. .width(40)
19. .height(40)
20. .justifyContent(FlexAlign.Center)
21. .backgroundColor('#E8E8E8')
22. .borderRadius(40)
23. .onClick(() => {
24. this.getUIContext().getRouter().back({
25. url: 'pages/Index'
26. });
27. })

29. Text('Conditional rendering')
30. .fontSize(20)
31. .fontWeight(700)
32. .height(26)
33. }
34. .width('100%')
35. .height(56)
36. .margin({ top: 36 })

38. // Use conditional rendering to simulate a scene where components are frequently created and destroyed with the click of a button
39. if (this.flag) {
40. // Custom component A
41. CustomComponentA()
42. } else {
43. // Custom component B
44. CustomComponentB()
45. }
46. Button('switch custom component')
47. .width('100%')
48. .backgroundColor('#0A59F7')
49. .onClick(() => {
50. // Click the button to switch to the custom component
51. this.flag = !this.flag;
52. })
53. }
54. .width('100%')
55. .height('100%')
56. .justifyContent(FlexAlign.SpaceBetween)
57. .padding({ left: 16, right: 16, bottom: 44 })
58. .backgroundColor('#F5F5F5')
59. }
60. }

62. @Component
63. struct CustomComponentA {
64. aboutToAppear(): void {
65. let temp: number = 0;
66. for (let i = 0; i < 1000000; i++) {
67. temp += 1;
68. }
69. hilog.info(0x0001, 'Sample', `%{public}s', 'CustomComponentA aboutToAppear ${temp}`);
70. }

72. aboutToDisappear(): void {
73. let temp: number = 0;
74. for (let i = 0; i < 1000000; i++) {
75. temp += 1;
76. }
77. hilog.info(0x0001, 'Sample', '%{public}s', `CustomComponentA aboutToDisappear ${temp}`);
78. }

80. build() {
81. Column()
82. .backgroundColor(Color.Blue)
83. .width(200)
84. .height(200)
85. }
86. }

88. @Component
89. struct CustomComponentB {
90. aboutToAppear(): void {
91. let temp: number = 0;
92. for (let i = 0; i < 1000000; i++) {
93. temp += 1;
94. }
95. hilog.info(0x0001, 'Sample', '%{public}s', `CustomComponentB aboutToAppear ${temp}`);
96. }

98. aboutToDisappear(): void {
99. let temp: number = 0;
100. for (let i = 0; i < 1000000; i++) {
101. temp += 1;
102. }
103. hilog.info(0x0001, 'Sample', '%{public}s', `CustomComponentB aboutToDisappear ${temp}`);
104. }

106. build() {
107. Column()
108. .backgroundColor(Color.Gray)
109. .width(200)
110. .height(200)
111. }
112. }
```

[ConditionalRendering.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/ConditionalRendering.ets#L17-L129)

因为示例中使用了条件渲染，每次销毁前一个自定义组件都会调用一次aboutToDisappear函数，然后创建新的自定义组件时，又会调用一次aboutToAppear，所以调用较为频繁。因此，在频繁创建和销毁组件的场景中，应尽量避免在aboutToAppear，aboutToDisappear中执行耗时操作。

### 循环渲染

在懒加载滑动场景中，框架会根据滚动容器可视区域按需创建组件，关于懒加载接口的描述如下

```
1. LazyForEach(
2. dataSource: IDataSource,  // Data sources requiring iterative data processing
3. itemGenerator: (item: Object, index: number) => void,  // Subcomponent build function
4. keyGenerator?: (item: Object, index: number) => string // Key-value generation function
5. ): void
```

所以在滑动时框架会频繁调用子组件生成函数itemGenerator，键值生成函数keyGenerator以及dataSource获取索引数据函数的getData函数。如果在itemGenerator，keyGenerator，getData中执行了耗时操作（比如传入耗时的函数作为入参），就会导致应用出现卡顿丢帧的问题。

三种函数的正反例效果类似，故本次只针对itemGenerator进行测试，下面依然基于Grid懒加载组件复用场景进行分析。

说明

本案例中子组件生成函数itemGenerator以及键值生成函数keyGenerator详细信息，请参考[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)。获取索引数据函数getData的说明，请参考[IDataSource说明](../harmonyos-references/ts-rendering-control-lazyforeach.md#idatasource)。

本案例中懒加载的子组件生成函数即GridItem组件的生成函数。

【反例】：在itemGenerator中执行itemGeneratorFunc()耗时函数

```
1. // ...
2. aboutToAppear(): void {
3. // ...
4. }

6. // Simulate time-consuming operations
7. itemGeneratorFunc(item: number): number {
8. let temp: number = 0;
9. for (let index = 0; index < 1000000; index++) {
10. temp += 1;
11. }
12. item += temp;
13. return item;
14. }

16. build() {
17. Column() {
18. Row({ space: 5 }) {
19. Column() {
20. Image($r('app.media.chevron_left'))
21. .width(16)
22. .height(16)
23. }
24. .width(40)
25. .height(40)
26. .justifyContent(FlexAlign.Center)
27. .backgroundColor('#E8E8E8')
28. .borderRadius(40)
29. .onClick(() => {
30. this.getUIContext().getRouter().back({
31. url: 'pages/Index'
32. });
33. })

35. Text('Loop rendering counterexamples')
36. .fontSize(20)
37. .fontWeight(700)
38. .height(26)
39. }
40. .padding({ left: 16, right: 16 })
41. .width('100%')
42. .height(56)
43. .margin({ top: 36 })

45. Column({ space: 5 }) {
46. Grid() {
47. LazyForEach(this.data, (item: number) => {
48. GridItem() {
49. // Use reusable custom components
50. ReusableChildComponent({ item: item })
51. }
52. }, (item: number) => item.toString())
53. }
54. // ...
55. }
56. .margin({ top: 12 })
57. }
58. .backgroundColor('#F5F5F5')
59. }
```

[NegativeOfLazyForEach.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/NegativeOfLazyForEach.ets#L50-L122)

【正例】：itemGenerator不执行耗时操作

**结果对比**

**图9** itemGenerator中执行耗时操作的滑动效果  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/d4gOztsQRyOVxJO_asmEZQ/zh-cn_image_0000002229335521.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=FF5565DEF5D1AE158593627E83F0292309BDD8337BF316E91C2F4F4C868E419B)

**图10** itemGenerator中不执行耗时操作的滑动效果  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/dKU6A3dlQES3DLlnnNFMCg/zh-cn_image_0000002194009708.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=34C105B10CB8F6AB1169B95F67323B1CAA516657C299D637A78744A375054D6C)

图9是在itemGenerator入参函数中执行耗时操作的滑动效果，可以明显看出滑动时存在卡顿，item节点刷新慢等问题。图10是在aboutToAppear中执行耗时操作，把耗时操作计算的值timeConsumingValue传入itemGenerator的滑动效果，可以看出滑动效果流畅，无卡顿问题。

因此，在懒加载滑动场景中，应避免在LazyForEach的itemGenerator，keyGenerator，getData中执行耗时操作，可以有效减少应用卡顿丢帧的问题，提升用户体验。

### 组件属性

组件单一属性刷新时，组件的其他属性也会同时进行刷新。在需要频繁刷新组件属性的场景中，如果组件中其他不需要刷新的属性使用了耗时的函数作为入参。那么在刷新组件某个属性时，组件中那些实际上不需要去刷新的属性将会去调用耗时函数，导致不必要的性能损耗，同时也会引起应用卡顿丢帧的问题。

下面是一个点击按钮改变Row组件宽度的示例

【反例】：Row组件的高度以耗时函数作为入参

```
1. @Entry
2. @Component
3. struct NegativeOfProperty {
4. // Row Width
5. @State rowWidth: number = 200;

7. getHeight(): number {
8. let height: number = 0;
9. // Simulate time-consuming operations with loop functions
10. for (let index = 0; index < 1000000; index++) {
11. height += 0.0001;
12. }
13. return height;
14. }

16. build() {
17. Column() {
18. Row({ space: 5 }) {
19. Column() {
20. Image($r('app.media.chevron_left'))
21. .width(16)
22. .height(16)
23. }
24. .width(40)
25. .height(40)
26. .justifyContent(FlexAlign.Center)
27. .backgroundColor('#E8E8E8')
28. .borderRadius(40)
29. .onClick(() => {
30. this.getUIContext().getRouter().back({
31. url: 'pages/Index'
32. });
33. })

35. Text('Component property counterexamples')
36. .fontSize(20)
37. .fontWeight(700)
38. .height(26)
39. }
40. .width('100%')
41. .height(56)
42. .margin({ top: 36 })

44. Row()
45. .width(this.rowWidth)
46. .height(this.getHeight())
47. .backgroundColor(Color.Blue)

49. Button('change row width')
50. .onClick(() => {
51. this.rowWidth = this.rowWidth + 20;
52. if (this.rowWidth > 300) {
53. this.rowWidth = 200;
54. }
55. })
56. .width('100%')
57. .backgroundColor('#0A59F7')
58. }
59. .justifyContent(FlexAlign.SpaceBetween)
60. .width('100%')
61. .height('100%')
62. .padding({ left: 16, right: 16, bottom: 44 })
63. .backgroundColor('#F5F5F5')
64. }
65. }
```

[NegativeOfProperty.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/NegativeOfProperty.ets#L18-L83)

【正例】：使用任务池taskpool处理耗时操作后返回结果给Row的高度rowHeight

```
1. import { taskpool } from '@kit.ArkTS'; // Task pools
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Concurrent
6. function getHeight(): number {
7. let height: number = 0;
8. // Simulate time-consuming operations with loop functions
9. for (let index = 0; index < 1000000; index++) {
10. height += 0.0001;
11. }
12. hilog.info(0x0000, 'Sample', '%{public}s', 'Scenario 4 call getHeight');
13. return height;
14. }

16. // Execute getHeight
17. taskpool.execute(getHeight).then((value: Object) => {
18. AppStorage.setOrCreate('height', value);
19. }).catch((error: BusinessError)=>{
20. hilog.error(0x0000,'',`execute failed. code=${error.code}, message=${error.message}`);
21. });

23. @Entry
24. @Component
25. struct PositiveOfProperty {
26. // Row width
27. @State rowWidth: number = 200;
28. // Row height
29. @StorageLink('height') rowHeight: number = 0;
30. // The number of times you click the button to change the width of the row
31. private count: number = 0;

33. build() {
34. Column({ space: 10 }) {
35. Row({ space: 5 }) {
36. Column() {
37. Image($r('app.media.chevron_left'))
38. .width(16)
39. .height(16)
40. }
41. .width(40)
42. .height(40)
43. .justifyContent(FlexAlign.Center)
44. .backgroundColor('#E8E8E8')
45. .borderRadius(40)
46. .onClick(() => {
47. this.getUIContext().getRouter().back({
48. url: 'pages/Index'
49. });
50. })

52. Text('Component property examples')
53. .fontSize(20)
54. .fontWeight(700)
55. .height(26)
56. }
57. .width('100%')
58. .height(56)
59. .margin({ top: 36 })

61. Row()
62. .width(this.rowWidth)
63. .height(this.rowHeight)
64. .backgroundColor(Color.Blue)

66. Button('change row width')
67. .width('100%')
68. .backgroundColor('#0A59F7')
69. .onClick(() => {
70. this.rowWidth = this.rowWidth + 20;
71. this.count++;
72. hilog.info(0x0000, 'Sample', 'Scenario 4 call getHeight: %{public}s', this.count);
73. if (this.rowWidth > 300) {
74. this.rowWidth = 200;
75. }
76. })
77. }
78. .justifyContent(FlexAlign.SpaceBetween)
79. .width('100%')
80. .height('100%')
81. .padding({ left: 16, right: 16, bottom: 44 })
82. .backgroundColor('#F5F5F5')
83. }
84. }
```

[PositiveOfProperty.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/PositiveOfProperty.ets#L17-L101)

在组件单一属性刷新时，组件的其他属性也会同时进行刷新。每次点击按钮改变Row组件宽度时，Row的高度也会同时刷新。反例每次改变Row组件宽度rowWidth，都会调用一次耗时的Row高度入参函数getHeight()。正例在页面加载时通过taskpool方式仅执行一次耗时的getHeight()。然后返回结果直接赋值给Row高度变量rowHeight。后续每次改变Row组件宽度rowWidth时,不需要重复调用耗时的getHeight()，有效减少了不必要的性能开销。

因此，在高频刷新组件属性的场景中，应避免在组件的属性中执行耗时操作（如属性使用耗时的函数入参），能有效减少应用卡顿丢帧的情况，提升用户体验。

## 其他主线程优化思路

当主线程中遇到一些难以避免的耗时操作时，可以从以下角度进行性能优化：

* [避免使用耗时接口](bpta-time-optimization-of-the-main-thread.md#section193673511440)
* [使用多线程能力](bpta-time-optimization-of-the-main-thread.md#section32971936174416)
* [@Sendable装饰器](bpta-time-optimization-of-the-main-thread.md#section7359185917239)

### 避免使用耗时接口

在应用开发中，经常会调用系统提供的接口，比如读取本地文件、处理服务端数据等等。若对接口使用不合理，可能引起延迟、卡顿、丢帧等性能问题。以如下系统提供的接口为例，总结了使用中的注意事项。下面以ResourceManager同步获取资源的接口为例进行分析。

说明

建议开发者优先使用[Code Linter扫描工具](../harmonyos-guides/ide-code-linter.md)进行代码检查，重点关注[@performance/hp-arkui-use-taskpool-for-web-request](../harmonyos-guides/ide-hp-arkui-use-taskpool-for-web-request.md)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

**ResourceManager**

ResourceManager通过getXXXSync接口同步获取资源的方式有两种，1、通过resource对象获取resourceManager.getStringSync($r('app.string.test'))；2、通过id获取resourceManager.getStringSync($r('app.string.test').id)。 下面以[getStringSync](../harmonyos-references/js-apis-resource-manager.md#getstringsync9)为例，测试一下这两种参数在方法中的使用是否会有耗时区别。

* 通过resource对象获取

  ```
  1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';

  4. @Entry
  5. @Component
  6. struct GetStrOfResource {
  7. @State message: string = 'getStringSync';

  9. aboutToAppear(): void {
  10. hiTraceMeter.startTrace('getStringSync', 1);
  11. // The input parameter of the getStringSync operation directly uses the resource and does not use the resource ID
  12. try {
  13. this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.test').id)
  14. } catch (error) {
  15. hilog.error(0x0000,'',`getStringSync failed. code=${error.code}, message=${error.message}`);
  16. }
  17. hiTraceMeter.finishTrace('getStringSync', 1)
  18. }

  20. build() {
  21. Column() {
  22. Row({ space: 5 }) {
  23. Column() {
  24. Image($r('app.media.chevron_left'))
  25. .width(16)
  26. .height(16)
  27. }
  28. .width(40)
  29. .height(40)
  30. .justifyContent(FlexAlign.Center)
  31. .backgroundColor('#E8E8E8')
  32. .borderRadius(40)
  33. .onClick(() => {
  34. this.getUIContext().getRouter().back({
  35. url: 'pages/Index'
  36. });
  37. })

  39. Text('Through resource objects')
  40. .fontSize(20)
  41. .fontWeight(700)
  42. .height(26)
  43. }
  44. .width('100%')
  45. .height(56)
  46. .margin({ top: 20 })

  48. TextArea({text: this.message})
  49. .height('40%')
  50. }
  51. .height('100%')
  52. .width('100%')
  53. .padding(16)
  54. .backgroundColor('#F5F5F5')
  55. }
  56. }
  ```

  [GetStrOfResource.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/GetStrOfResource.ets#L17-L73)

* 通过id获取

  ```
  1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';

  3. @Entry
  4. @Component
  5. struct GetStrOfId {
  6. @State message: string = 'getStringSyncAfter';

  8. aboutToAppear(): void {
  9. hiTraceMeter.startTrace('getStringSyncAfter', 1);
  10. // The input parameter of the getStringSync operation directly uses the resource and resource ID
  11. try {
  12. this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.test').id)
  13. } catch (error) {
  14. hilog.error(0x0000,'',`getStringSync failed. code=${error.code}, message=${error.message}`);
  15. }
  16. hiTraceMeter.finishTrace('getStringSyncAfter', 1)
  17. }

  19. build() {
  20. Column() {
  21. Row({ space: 5 }) {
  22. Column() {
  23. Image($r('app.media.chevron_left'))
  24. .width(16)
  25. .height(16)
  26. }
  27. .width(40)
  28. .height(40)
  29. .justifyContent(FlexAlign.Center)
  30. .backgroundColor('#E8E8E8')
  31. .borderRadius(40)
  32. .onClick(() => {
  33. this.getUIContext().getRouter().back({
  34. url: 'pages/Index'
  35. });
  36. })

  38. Text($r('app.string.get_str_of_id'))
  39. .fontSize(20)
  40. .fontWeight(700)
  41. .height(26)
  42. }
  43. .width('100%')
  44. .height(56)
  45. .margin({ top: 20 })

  47. TextArea({ text: this.message })
  48. .height('40%')
  49. }
  50. .height('100%')
  51. .width('100%')
  52. .padding(16)
  53. .backgroundColor('#F5F5F5')
  54. }
  55. }
  ```

  [GetStrOfId.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/GetStrOfId.ets#L17-L72)

**结果对比**

**图11** 通过资源对象获取数据的耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/3XAUEdzATuKqxTSlsI2RvQ/zh-cn_image_0000002229335497.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=3B463C3670A59B02229D6D598C6D3EB2BCAB503DA2D9BE3F3E6B4084ACFBE233 "点击放大")

**图12** 通过资源id获取数据的耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/WLLbVABJRpiTcITg4_T-fQ/zh-cn_image_0000002193850108.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=14A4C0F82FC6DE2A8F27458271CB8AA30AFDF7B715FDEC782D985763901FE522 "点击放大")

getStringSync参数为资源信息时（1.956ms）比参数为资源ID值时（0.071ms）耗时更多，因为通过resource对象获取资源时，获取的是拷贝对象，获取过程中发生了一次深拷贝，而通过资源ID获取子元素，直接获取原对象的引用。所以当需要使用类似方法时，使用资源ID值作为参数更优。

通过本案例可以发现，同一接口的不同使用方式存在着性能差异，在开发过程中应该选择耗时更少、性能更优的接口，避免因此引起的延迟卡顿丢帧等性能问题。

**wordBreak****属性**

说明

建议开发者优先使用[Code Linter扫描工具](../harmonyos-guides/ide-code-linter.md)进行代码检查，重点关注[@performance/hp-arkui-use-word-break-to-replace-zero-width-space](../harmonyos-guides/ide_hp-arkui-use-word-break-in-space.md)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

零宽空格（Zero Width Space, ZWSP）是一个特殊的Unicode字符。它是一个不可见的字符，其宽度为零，不占用任何可见空间。在文本处理系统中，尽管它在视觉上是不可见的，但它在文本中确实存在，并可以作为潜在的断点，即允许在此位置断开行。这意味着如果一行文本过长需要自动换行时，文本可以在零宽空格的位置进行折行，而不影响单词的完整性。

虽然零宽空格在许多情况下都是有用的，但它也可能引起问题，特别是在文本处理和数据清洗中。不注意这些看不见的字符可能导致数据的意外错误、搜索失败、数据不一致等问题。因此，在处理来自不同源的文本数据时，了解和考虑这些不可见字符是非常重要的。

避免在文本组件内使用零宽空格(\u200b)的形式来设置断行规则，推荐使用[wordBreak](../harmonyos-references/ts-basic-components-text.md#wordbreak11)，wordBreak在使用性能方面优于零宽空格。例如推荐用法为：Text(this.diskName).wordBreak(WordBreak.BREAK\_ALL)。

说明

常见高耗时接口有：[getInspectorByKey](../harmonyos-references/ts-universal-attributes-component-id.md#getinspectorbykey9)、[getInspectorTree](../harmonyos-references/ts-universal-attributes-component-id.md#getinspectortree9)、[sendEventByKey](../harmonyos-references/ts-universal-attributes-component-id.md#sendeventbykey9)、[sendTouchEvent](../harmonyos-references/ts-universal-attributes-component-id.md#sendtouchevent9)、[sendKeyEvent](../harmonyos-references/ts-universal-attributes-component-id.md#sendkeyevent9)、[sendMouseEvent](../harmonyos-references/ts-universal-attributes-component-id.md#sendmouseevent9)。

以上接口由于耗时长，建议仅用于应用测试阶段。

### 使用多线程能力

在主线程面临耗时操作时，采用多线程能力是一种高效的优化手段。通过将耗时任务分配给后台线程并行执行，主线程可以继续处理其他任务，保持应用的流畅性和响应性。这种方式能够充分利用多核处理器的计算能力，提高程序的执行效率，减少用户等待时间，从而提升整体的用户体验。

**场景案例**

列表无限滑动的场景，在即将触底的时候需要进行数据请求，如果在主线程中直接处理请求数据，可能会导致滑动动画被中断。如果回调函数处理的耗时较长，会直接阻塞主线程，卡顿就会非常明显。使用异步执行的方式进行异步调用，回调函数的执行还是会在主线程，一样会阻塞UI绘制和渲染。

以[瀑布流使用案例](../harmonyos-references/ts-container-waterflow.md#示例1使用基本瀑布流)为基础进行代码改造,得到如下代码,瀑布流在即将触底时调用异步函数mockRequestData获取新数据，并将新数据写入数据源。异步函数mockRequestData用于模拟耗时的网络请求，从rawfile目录下读取数据，将数据处理后返回。

```
1. build() {
2. Column({ space: 2 }) {
3. Row({ space: 5 }) {
4. Column() {
5. Image($r('app.media.chevron_left'))
6. .width(16)
7. .height(16)
8. }
9. .width(40)
10. .height(40)
11. .justifyContent(FlexAlign.Center)
12. .backgroundColor('#E8E8E8')
13. .borderRadius(40)
14. .onClick(() => {
15. this.getUIContext().getRouter().back({
16. url: 'pages/Index'
17. });
18. })

20. Text('Use asynchronous')
21. .fontSize(20)
22. .fontWeight(700)
23. .height(26)
24. }
25. .width('100%')
26. .height(56)
27. .margin({ top: 20 })

30. WaterFlow() {
31. LazyForEach(this.dataSource, (item: number) => {
32. FlowItem() {
33. // ...
34. }
35. .onAppear(() => {
36. // Add data in advance when you are about to hit the bottom
37. if (item + 20 === this.dataSource.totalCount()) {
38. // Simulate the time it takes for the network to acquire data
39. this.mockRequestData().then((data: Item[]) => {
40. for (let i = 0; i < data.length; i++) {
41. this.dataSource.addLastItem();
42. }
43. })
44. }
45. })
46. // ...
47. }, (item: number) => item.toString())
48. }
49. // ...
50. }
51. .padding(16)
52. .height('100%')
53. .backgroundColor('#F5F5F5')
54. }

56. async mockRequestData(): Promise<Item[]> {
57. let res: ResponseData = new ResponseData();
58. // data.json is the local json data, which is about 20 MB in size, and simulates getting data from the network
59. await this.getUIContext().getHostContext()!.resourceManager.getRawFileContent('data.json').then((data: Uint8Array) => {
60. // parse json
61. try {
62. let str: string = buffer.from(data).toString();
63. res = JSON.parse(str);
64. } catch (error) {
65. hilog.error(0x0000,'',`buffer.from failed. code=${error.code}, message=${error.message}`);
66. }
67. }).catch((error: BusinessError)=>{
68. hilog.error(0x0000,'',`getRawFileContent failed. code=${error.code}, message=${error.message}`);
69. });
70. return dataToItem(res.data)
71. }
```

[UseAsync.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/UseAsync.ets#L49-L137)

```
1. export class Item {
2. url: string = '';
3. id: number = 0;
4. name: string = '';
5. // ...
6. }
```

[Item.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/common/Item.ets#L18-L29)

使用profiler工具抓取Trace：

**图13** 不使用多线程的Trace信息  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/TGfWtxT9RFi9-XzjOnlZDg/zh-cn_image_0000002229450001.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=EAFBCFEF3B281643B79A9B5CB29C071C2EC116289A67D4FF4CC572672305868C "点击放大")

从图中可以看到，在主线程中出现了大块的耗时，直接导致用户在滑动的时候能感受到明显的卡顿。异步回调函数最后也由主线程执行，所以应该尽量避免在回调函数中执行耗时操作。可以使用系统自带的[@ohos.taskpool（启动任务池）](../harmonyos-references/js-apis-taskpool.md)多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞，以下为使用TaskPool优化后的代码：

```
1. build() {
2. Column({ space: 2 }) {
3. Row({ space: 5 }) {
4. Column() {
5. Image($r('app.media.chevron_left'))
6. .width(16)
7. .height(16)
8. }
9. .width(40)
10. .height(40)
11. .justifyContent(FlexAlign.Center)
12. .backgroundColor('#E8E8E8')
13. .borderRadius(40)
14. .onClick(() => {
15. this.getUIContext().getRouter().back({
16. url: 'pages/Index'
17. });
18. })

20. Text($r('app.string.use_async'))
21. .fontSize(20)
22. .fontWeight(700)
23. .height(26)
24. }
25. .width('100%')
26. .height(56)
27. .margin({ top: 20 })

29. WaterFlow() {
30. LazyForEach(this.dataSource, (item: number) => {
31. FlowItem() {
32. // ...
33. }
34. .onAppear(() => {
35. // Add data in advance when you are about to hit the bottom
36. if (item + 20 === this.dataSource.totalCount()) {
37. // Simulate the time it takes for the network to acquire data
38. taskPoolExecute(this.UIContext).then((data: Item[]) => {
39. for (let i = 0; i < data.length; i++) {
40. this.dataSource.addLastItem();
41. }
42. })
43. }
44. })
45. // ...
46. }, (item: number) => item.toString())
47. }
48. // ...
49. }
50. .padding(16)
51. .height('100%')
52. .backgroundColor('#F5F5F5')
53. }
```

[UseTaskPool.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/UseTaskPool.ets#L50-L120)

```
1. // The following methods are defined outside of the component
2. async function taskPoolExecute(UIContext: UIContext): Promise<Item[]> {
3. let task: taskpool.Task = new taskpool.Task(mockRequestData, UIContext);
4. let result: Item[] = [];
5. try {
6. result = await taskpool.execute(task) as Item[]
7. } catch (error) {
8. hilog.error(0x0000,'',`execute failed. code=${error.code}, message=${error.message}`);
9. }
10. return result;
11. }

13. @Concurrent
14. async function mockRequestData(context: Context): Promise<Item[]> {
15. let res: ResponseData = new ResponseData();
16. // data.json is the local json data, which is about 20 MB in size, and simulates getting data from the network
17. await context.resourceManager.getRawFileContent('data.json').then((data: Uint8Array) => {
18. // parse json
19. try {
20. let str: string = buffer.from(data).toString();
21. res = JSON.parse(str);
22. } catch (error) {
23. hilog.error(0x0000,'',`buffer.from failed. code=${error.code}, message=${error.message}`);
24. }
25. }).catch((error: BusinessError)=>{
26. hilog.error(0x0000,'',`getRawFileContent failed. code=${error.code}, message=${error.message}`);
27. });
28. let arr: Item[] = dataToItem(res.data);
29. return arr;
30. }
```

[UseTaskPool.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/views/UseTaskPool.ets#L125-L155)

**图14** 使用多线程的Trace信息  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/SHY3XmhSRFueYs7UX7unsQ/zh-cn_image_0000002229335505.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=108ABCDF0D31999E97C80FF486E28059425CDD906A5120FD6A6C28EB07350730 "点击放大")

通过上图可以看出，使用多线程能力TaskPool后，将原先在主线程中的获取资源的任务getRawFileContent转移到了TaskWorker线程，避免了获取资源导致的主线程长时间阻塞，但是TaskWorker将结果返回给主线程，主线程反序列化数据的过程中依然会消耗一定时间，接下来在泳道图中搜索"H:Deserialize"标签查看主线程反序列化耗时。

**图15** 主线程反序列化耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/DjW2kFSVSoydD90vXq9z0A/zh-cn_image_0000002229335525.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=4E8D9E144D39B8FDB18ACAECB90B9D42236026BEFDF1560E35BF20093D1CF72D "点击放大")

从图中可以看出主线程在反序列化TaskWorker线程返回的数据依然存在12ms的耗时，超过当前测试设备的Vsync周期（8.3ms），应用可能会因此引起卡顿。针对跨线程的序列化耗时问题，系统提供了@Sendable装饰器来实现内存共享，可以在返回的Item类上使用@Sendable装饰器，继续优化性能。

### @Sendable装饰器

@Sendable装饰器可以实现数据在多线程间的传递行为是引用传递，使用方式如下：

```
1. export class Item {
2. url: string = '';
3. id: number = 0;
4. name: string = '';
5. // ...
6. }
```

[Item.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AvoidTimeComsume/entry/src/main/ets/common/Item.ets#L18-L29)

关于@Sendable装饰器的详细介绍以及使用限制，请参考[Sendable对象简介](../harmonyos-guides/arkts-sendable.md)。

上述示例代码中在TaskWorker线程返回的Item对象上使用了@Sendable，系统会使用共享内存的方式处理使用了@Sendable的类，从而降低反序列化的开销，抓取Trace图如下：

**图16** 使用@Sendable装饰器后主线程反序列化耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/v9ycVhUgTf-FueOq-oAcoQ/zh-cn_image_0000002229449973.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=23F9C9D18717E8DFA7474E43175CBDC73E4A55CCC3CF6F5BC8E14F51DDC880AF "点击放大")

从图中可以看出反序列化的耗时由12ms减少到1.6ms，明显减少了主线程的阻塞时间，所以当主线程需要反序列化其他线程返回的大量数据时，可以使用@Sendable装饰器减少主线程的时间消耗。

开发过程中，在主线程执行一些耗时任务，可能会阻塞UI渲染导致卡顿、掉帧等性能问题。具有如下优化思路

* 正式发布版本避免冗余日志，Trace打点以及没有业务操作的系统回调；
* 在高频回调的场景中，避免执行耗时操作；
* 避免使用耗时接口，同一接口的不同使用方式存在性能差异，开发者应该选择耗时更少，性能更优的接口；
* 使用多线程能力，将一些必要的耗时操作交由子线程执行，减小主线程的阻塞耗时；
* 主线程与其他线程存在大量数据交互时，使用@Sendable装饰器，可以提升线程间数据的传输与同步效率。

## 示例代码

[主线程耗时操作优化指导](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/AvoidTimeComsume)
