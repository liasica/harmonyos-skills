---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-skip-analysis
title: 应用UI进程空跑问题分析
breadcrumb: 最佳实践 > 功耗 > 应用功耗分析 > 应用UI进程空跑问题分析
category: best-practices
scraped_at: 2026-04-29T14:13:47+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:362ca2a32d97e134aa868326d1947aeca772fe296b71793b7620bf2a8936656b
---

## 应用UI进程空跑介绍

应用UI进程空跑主要指在应用界面无实际变化、无用户交互、无可见动画播放等情况下，应用进程仍以固定帧率刷新。

如下图所示，为一个UI空跑的trace示例，图中应用主线程powerdemon以90Hz刷新，但在高亮框选区域，render\_service线程对应的帧未刷新，表明期间应用主线程powerdemon未递交有效绘制指令给render\_service进行绘制，产生空帧。这些空帧通常由应用注册帧回调但实际无节点脏区引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/LtQcKJOsR-qMfcd44x1pjA/zh-cn_image_0000002555774310.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=65895E804D8ECD57A586042653AB1F24A6C5DE98D85B336E44A34DE2C3AA8409 "点击放大")

开发者可进一步在空刷帧中搜索“FlushMessages”，如下图所示，当“FlushMessages”下方存在“UI skip”时，表示该帧未递交任何绘制指令，属于UI空跑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/-oL645ggTgmnoUBZKXlMng/zh-cn_image_0000002586294233.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=1C2A4E994565A31CFC081151240AF747977E6D9906E2CE645152CFCAAD9F2F5D "点击放大")

对比下图的非UI空跑场景，“FlushMessages”下方发现“H:MarshRSTransactionData cmdCount: 2, transactionFlag:[22766,879]”字样时，可确认该帧有绘制指令递交，将引起下一帧render\_service的RS树准备工作。其中22766表示下发绘制指令的线程ID，879表示帧数据的索引，“cmdCount:2”表示绘制指令数量为2，有两个arkui节点在该帧被标脏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/qZefOOAmSeW-5E5PlpWv5A/zh-cn_image_0000002555614690.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=210EDC7B7CB8FA20FD24FCAFBBC61BFFF90CF7A76C22777928EC37EF48D8D328 "点击放大")

## 分析思路

### 使用Trace分析

开发者可在Profiler中的Energy模板录制一段trace分析，以找到UI帧空帧的原因。关键Trace：H:DisplaySyncId[29] Type[0]... 其中Type的类型是导致刷帧的原因，包括：

Type[-1]：Other，三方自申请的回调接口

Type[0]：Animator

Type[1]：Xcomponent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/QCQGr3ZgTIO48E_LNTRBMA/zh-cn_image_0000002586174287.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=1E9595A79F0A3CF36270970BD1E48E80E02B4000334E89640FC9106E8C2A950C "点击放大")

### 使用Profiler的Energy工具分析（推荐）

在DevEco Studio 6.1版本（手机版本需配套HarmonyOS 6.1及以上版本），针对UI空刷问题，增加了自动检测与分析能力，可通过以下步骤辅助问题定位:

1. 抓取Trace信息

   点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，操作应用进行测试。
2. 查看异常信息

   点击Energy Anomaly泳道，在Detail栏展示异常信息，其中UI Empty Run表示存在UI空刷异常。

   图中① AnomalyType: 异常类型，② Anomaly Reason: 异常原因，③ Anomaly Count: 异常的帧数，④ More: 异常帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Khtmk8zkRCWajfH0RzB8_A/zh-cn_image_0000002555774312.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=B97E264615FE6F0EF1B60AA938F3098616C901FA02BEBF0A365ABC171AEAF77A "点击放大")

3. 查看单帧详情信息

   在More栏，点击其中一帧，在应用的主线程泳道，查看H:DisplaySyncId关键字的Trace，依据Type确认根因类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/vFzBthykRG24zNbP3O8t-A/zh-cn_image_0000002586294237.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=F0BD3ADDDCA559E0F597857A2BF3FA1CCF40B83D60476303C331602C08F63FB8 "点击放大")

## 常见故障根因

### Animator动画

Animator是一种依赖DisplaySync机制产生UI刷新的动画机制。如下图“1”处所示，“jsAnimator onframe, duration: 5000, curve: ease, id:1”表明，该动效持续时间为5000ms，动效曲线为ease，Animator的ID为1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/g4CA_J66TSy2xcJagD58hg/zh-cn_image_0000002555614692.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=777FCB1AA04E3197CC4F504491E8DAC9480EB387EF7CA488CDD1A165867369D8 "点击放大")

开启hdc shell param set persist.ace.debug.enabled 1开关后，如果该Animator导致实际的组件属性更新，下方会有打印信息如下：

* H:ViewPU.viewPropertyHasChanged MyAnimatorTest wid 1 6 0 false
* H:ViewPU.viewPropertyHasChanged MyAnimatorTest hei 1 6 1 false

重点关注其中提到的MyAnimatorTest、wid、hei三处信息，这表明该Animator的执行在MyAnimatorTest组件上进行，受影响的状态变量为wid与hei。此外，下图标志“2”“3”“4”处会打印组件脏区刷新、FlushTask以及SendCommand的信息，证实了该Animator的效果在递交绘制指令时，是通过组件变量wid、hei更新来完成的。

注意

Animator发生空跑的主要根因是，组件被析构或进入不可见状态时，Animator未主动设置停止或取消。由于Animator本身是独立的回调对象，不会与组件一对一关联，系统无法代为回收这些持续产生空跑的对象。

开发者在使用Animator时，可遵循以下两个要点：

1. 确保组件析构时，Animator执行finish，并置空，可有效规避空跑问题与内存泄漏风险。
2. 组件添加可见性回调，Animator默认不播放，当且仅当组件位于可见状态时，执行play。

```
1. let expectedFrameRate: ExpectedFrameRateRange = {
2. min: 0,
3. max: 120,
4. expected: 30
5. }

7. @Component
8. export struct MyAnimatorTest {
9. private TAG: string = '[AnimatorTest]'
10. private backAnimator: AnimatorResult | undefined = undefined
11. private flag: boolean = false
12. @State wid: number = 100
13. @State hei: number = 100

15. create() {
16. this.backAnimator = this.getUIContext()?.createAnimator({
17. // 建议使用 this.getUIContext().createAnimator()接口
18. duration: 5000,
19. easing: "ease",
20. delay: 0,
21. fill: "forwards",
22. direction: "normal",
23. iterations: 1,
24. begin: 100, //动画插值起点
25. end: 200, //动画插值终点
26. })
27. this.backAnimator.setExpectedFrameRateRange(expectedFrameRate)
28. this.backAnimator.onFinish = () => {
29. this.flag = true
30. console.info(this.TAG, 'backAnimator onFinish')
31. }
32. this.backAnimator.onRepeat = () => {
33. console.info(this.TAG, 'backAnimator repeat')
34. }
35. this.backAnimator.onCancel = () => {
36. console.info(this.TAG, 'backAnimator cancel')
37. }
38. this.backAnimator.onFrame = (value: number) => {
39. this.wid = value
40. this.hei = value
41. }
42. }

44. aboutToDisappear() {
45. // 由于backAnimator在onframe中引用了this, this中保存了backAnimator，
46. // 在自定义组件消失时应该将保存在组件中的backAnimator置空，避免内存泄漏
47. this.backAnimator?.finish();
48. this.backAnimator = undefined;
49. }

51. build() {
52. Column() {
53. Column() {
54. Column()
55. .width(this.wid)
56. .height(this.hei)
57. .backgroundColor(Color.Red)
58. .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
59. if (!isExpanding && currentRatio <= 0.0) {
60. console.info('Component is completely invisible.')
61. this.backAnimator?.pause()
62. }
63. })
64. }
65. .width('100%')
66. .height(300)

68. Column() {
69. Row() {
70. Button('create')
71. .fontSize(30)
72. .fontColor(Color.Black)
73. .onClick(() => {
74. this.create()
75. })
76. }
77. .padding(10)

79. Row() {
80. Button('play')
81. .fontSize(30)
82. .fontColor(Color.Black)
83. .onClick(() => {
84. this.flag = false
85. if (this.backAnimator) {
86. this.backAnimator.play()
87. }
88. })
89. }
90. .padding(10)
91. }
92. }
93. }
94. }
```

### DisplaySync

DisplaySync支持开发者以[指定帧率运行UI业务](../harmonyos-guides/displaysync-ui.md)，主要用于精细控制绘制帧率的场景，如动态帧率动画、为特定UI组件设置独立于系统刷新率的绘制帧率等。

推荐的优化措施：

1. 若开发者希望注册监听窗口帧率变化用于分析UI卡顿、丢帧、FPS监控等场景，建议通过接入ohos.window提供的[frameMetricsMeasured](../harmonyos-references/arkts-apis-window-window.md#onframemetricsmeasured22)接口，该接口仅在客户端UI内容发生重绘时（如页面切换、与可响应组件交互、设置背景色和透明度等）触发注册的回调。

2. 在使用DisplaySync实现自定义动画、独立的UI绘制控制等场景时，需做好生命周期管理，具体优化方案参照[displaySync优化案例](bpta-vsync-power-optimization.md)。
