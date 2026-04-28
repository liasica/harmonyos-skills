---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ltpo-description
title: 基于LTPO的低功耗设计
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 基于LTPO的低功耗设计
category: best-practices
scraped_at: 2026-04-28T08:22:39+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:4f6eb6e4a3b5a823a8386871597bd0d50e0049850f061c463aeaee0e1547a275
---

## 概述

### LTPO技术简介

LTPO的全称是“Low Temperature Polycrystalline Oxide”，中文译为“低温多晶氧化物”。这是OLED屏背板的一种驱动技术。通过将OLED驱动电路中的TFT换成IGZO TFT，降低显示功耗。LTPO屏支持1~120Hz的自适应刷新率，使应用在需要高刷新率的场景下提升流畅性，而在视频、静止等场景中使用低刷新率降低显示功耗，延长电池续航。通常，用“LTPO”指代自适应刷新率技术。

### 特性介绍

LTPO是自适应刷新率技术，按需调整显示刷新率，优化性能和功耗。

说明

适配LTPO的好处包括：精细化场景帧率控制，降低场景负载，减少偶发卡顿，降低场景功耗。

### 场景策略建议

实现控件级帧率控制，降低系统因突发负载增加导致的卡顿，同时在高刷新率场景下主动适配，确保流畅体验。

**不建议锁定最高帧率运行**

不建议将ExpectedFrameRateRange中的expected、min、max都设置为120，这会干扰系统可变帧率机制，增加负载，影响整机性能和功耗。

主要原因有以下三点：

1. ExpectedFrameRateRange中的关键参数是expected（期望帧率）。系统优先按照expected设置的帧率执行。如果系统难以满足expected帧率，会在min和max之间选择一个更合适的帧率提供给应用。
2. 如果应用锁定120Hz，系统会优先满足应用的设置，以120帧运行。这将显著增加手机功耗，长时间运行会导致手机过热，严重影响用户体验。此外，不必要的高帧率会额外占据更多算力，可能导致其他场景的响应延迟。
3. 如果系统持续以120Hz运行，此时系统的可变帧率能力已失效，这与可变帧率的设计原则不符。

**策略建议**

|  |  |  |
| --- | --- | --- |
| **类型** | **类型描述** | **帧率建议（案例）** |
| 高帧率场景 | 基本全屏的非持续动效 | 应用启动，退出，窗口转场动效，拖动窗口移动动效：90~120Hz |
| 中等帧率场景 | 变化区域大的持续型动效，非全屏的手势动效与转场动效 | 视频内弹幕，小说自动翻页动效：60Hz  QQ首页左滑某一行消息动效:60Hz  微信右上角点击“+”号弹出应用内子窗口动效:60~120Hz  抖音内滑动切换视频，图库滑动切换图片动效：60Hz |
| 低帧率场景 | 小区域动效，微动效 | 小视频右下角转盘动效：15~30Hz  页面刷新加载转圈动效:20~30Hz  滑动列表右侧拖动条消失动效:15~30Hz  复杂微动效，根据实际效果调整帧率 |
| 跟随源帧率场景 | 插画动效，固定源帧率动效 | 帧率跟随内容源，不建议长时间保持高帧率  购物应用首页图标帧动效  聊天表情包动效  导航主界面 |

## 功耗测试工具

### 显示手机实时刷新率

打开开发者模式中的"显示刷新频率"开关。具体操作：设置中搜索"开发者" -> "显示刷新频率"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/eaF5fa5FRvOExc2Nt0x7MA/zh-cn_image_0000002194009772.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=5672250AB3DF71A703A565D22F22CBD4EBF79674442AB40E24075A66007AFBE9) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/xnt2rBk0RsidsQaKH3AP_g/zh-cn_image_0000002229335585.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=38B1484AC4F17F242A9676C561934CFC73745BAF87208DE35E695D4846C2F24C)

### Profiler工具测试手机功耗

1. 启动程序，并将其部署安装到真实手机上。

2. 打开工具Profiler，并按图示选择需要监控的设备、app、进程。未启动app会出现设备、app等选项为空的情况，此时不能进行Profiler性能分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Fi9wosYcS6Cqvk0mnHIZcw/zh-cn_image_0000002229335569.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=8EED37721DB5F9B9A5BEBAC219D9D14D34BF8188C7D2CEB2E6A5679B240FCA34 "点击放大")

图中的黄色折线展示整机的电量消耗，斜率为正表示设备耗电，斜率为负表示设备充电。

3. 点击会话区“Realtime Monitor”页签上的启动按钮，控制实时监控界面的录制状态。

4. 将鼠标悬浮在关注的泳道数据上时，界面上会显示当前时间点的时间标线和详细数据的Tooltips。当鼠标悬浮在时间轴上时，实时监控页面内的所有泳道均会以Tooltips显示该时刻的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/mHZdNNmORRWqT06Rw1iw-g/zh-cn_image_0000002194009788.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=21B8FEAA3DDCC8793DFDCB038FBCA4DFC4AD333F5775630102FE8A1F6B9E4DEF "点击放大")

本文采用的测试方式是让应用运行30秒，每3秒记录一次功耗数据，取设备从第6秒到第21秒的5个节点的平均功耗。此时设备已平稳运行，功耗也趋于稳定。

## 使用场景

### 场景说明

在具备LTPO屏幕的设备上，基于显示内容的可变帧率能力，可以达到性能体验和功耗间的平衡。HarmonyOS支持可变帧率能力，开发者通过使用可变帧率接口，进行相关业务开发，可以享受可变帧率特性带来的功耗收益。

可变帧率能力支持开发者自定义应用业务的帧率，其常见的使用场景：

* 通过配置属性动画/显示动画的帧率属性参数，用于动画的绘制，具体可见[请求动画绘制帧率](../harmonyos-guides/displaysync-animation.md)。
* 通过申请一个独立的绘制帧率，用于UI的绘制，具体可见[请求UI绘制帧率](../harmonyos-guides/displaysync-ui.md)。
* 通过XComponent在Native侧申请独立的绘制帧率，用于游戏等自绘制内容的绘制，具体可见[请求自绘制内容绘制帧率](../harmonyos-guides/displaysync-xcomponent.md)。

基于以上使用场景，结合众多实际开发案例，本文选取两个有代表性的案例展开介绍。

说明

设置的期望帧率值可能无法完全实现，因为会受到系统能力和屏幕刷新率的限制。

### 基于LTPO实现循环动画

针对无限循环的动画效果，如转盘动画，需要特别注意设置动画的可变帧率。长时间保持高帧率可能导致手机发热。

**效果展示**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/jFwFQkZQT82h69PKrKKJbQ/zh-cn_image_0000002229335581.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=5BADE3D1F3BB8D395687966F4983B2D1A19776E367771132C14FB1E4E57D292D)

**功耗对比**

说明

使用DisplaySync去实现转盘动画，通过主动设置可变帧率，可以获取功耗的差异。

功耗测试方法参考章节2。

打开手机屏幕刷新率设置，可以查看刷新率变化。使用Profiler工具，可以查看功耗变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/L_cFGz2pSem2rOPgHskZyg/zh-cn_image_0000002229450069.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=2CF35003FE5AF672319D2D36EC0098F7F20E9020A4290B352A2DEE04DB1CA2C9 "点击放大")

从图中可以发现，当屏幕刷新率降低时，功耗也会降低。

传入可变帧率（ExpectedFrameRateRange），屏幕感知并利用LTPO技术降低功耗。屏幕帧率不始终保持最高，功耗较低。

**实现说明**

首先，导入模块。

```
1. import { displaySync } from '@kit.ArkGraphics2D';
```

[segment.ets](https://gitcode.com/harmonyos_samples/fluent-blog/blob/master/entry/src/main/ets/segment/segment.ets#L3-L3)

定义并构建DisplaySync对象。

```
1. private backDisplaySyncSlow: displaySync.DisplaySync | undefined = undefined;
2. private backDisplaySyncFast: displaySync.DisplaySync | undefined = undefined;
```

[segment.ets](https://gitcode.com/harmonyos_samples/fluent-blog/blob/master/entry/src/main/ets/segment/segment.ets#L13-L14)

定义图片组件，添加旋转方法。

```
1. Row() {
2. Image($r('app.media.avatar'))
3. .height(40)
4. .width(40)
5. }
6. .rotate({
7. x: 0,
8. y: 0,
9. z: 1,
10. centerX: '50%',
11. centerY: '50%',
12. angle: this.rotateAngle
13. })
```

[segment.ets](https://gitcode.com/harmonyos_samples/fluent-blog/blob/master/entry/src/main/ets/segment/segment.ets#L58-L70)

使用DisplaySync实例设置帧率并注册订阅函数。

```
1. let range: ExpectedFrameRateRange = {
2. expected: 30,
3. min: 0,
4. max: 120
5. };
6. this.backDisplaySyncSlow.setExpectedFrameRateRange(range); // Setting the frame rate
```

[segment.ets](https://gitcode.com/harmonyos_samples/fluent-blog/blob/master/entry/src/main/ets/segment/segment.ets#L33-L38)

全部代码实现如下

```
1. import { displaySync } from '@kit.ArkGraphics2D';

3. @Entry
4. @Component
5. struct Index {
6. @State drawFirstSize: number = 25;
7. @State rotateAngle: number = 1;
8. @State drawSecondSize: number = 25;
9. private backDisplaySyncSlow: displaySync.DisplaySync | undefined = undefined;
10. private backDisplaySyncFast: displaySync.DisplaySync | undefined = undefined;
11. private isBigger30: boolean = true;

13. aboutToDisappear() {
14. if (this.backDisplaySyncSlow) {
15. this.backDisplaySyncSlow.stop(); // DisplaySync enable off
16. this.backDisplaySyncSlow = undefined; // Empty the instance
17. }
18. if (this.backDisplaySyncFast) {
19. this.backDisplaySyncFast.stop(); // DisplaySync enable off
20. this.backDisplaySyncFast = undefined; // Empty the instance
21. }
22. }

24. CreateDisplaySyncSlow() {
25. // Defining the Desired Drawing Frame Rate
26. this.backDisplaySyncSlow = displaySync.create(); // Creating a DisplaySync Instance
27. let range: ExpectedFrameRateRange = {
28. expected: 30,
29. min: 0,
30. max: 120
31. };
32. this.backDisplaySyncSlow.setExpectedFrameRateRange(range); // Setting the frame rate

34. let draw30 = (intervalInfo: displaySync.IntervalInfo) => {
35. if (this.isBigger30) {
36. this.rotateAngle += 1;
37. } else {
38. this.rotateAngle -= 1;
39. if (this.rotateAngle < 25) {
40. this.isBigger30 = true;
41. }
42. }
43. };

45. this.backDisplaySyncSlow.on("frame", draw30); // Subscribing to frame events and registering subscription functions
46. }

48. build() {
49. Column() {
50. Row() {
51. Image($r('app.media.avatar'))
52. .height(40)
53. .width(40)
54. }
55. .rotate({
56. x: 0,
57. y: 0,
58. z: 1,
59. centerX: '50%',
60. centerY: '50%',
61. angle: this.rotateAngle
62. })

64. Row() {
65. Button('Start')
66. .onClick(() => {
67. if (this.backDisplaySyncSlow === undefined) {
68. this.CreateDisplaySyncSlow();
69. }
70. if (this.backDisplaySyncSlow) {
71. this.backDisplaySyncSlow.start(); // DisplaySync enable off
72. }
73. })
74. }
75. }
76. }
77. }
```

[segment.ets](https://gitcode.com/harmonyos_samples/fluent-blog/blob/master/entry/src/main/ets/segment/segment.ets#L2-L86)

上述代码中，设置DisplaySync的可变帧率ExpectedFrameRateRange可以让系统调整屏幕刷新率。若要取消设置可变帧率，可注释以下代码：

```
1. // Note the following lines
2. // let range : ExpectedFrameRateRange = {
3. //     expected: 30,
4. //     min: 0,
5. //     max: 120
6. // };
7. // this.backDisplaySyncSlow.setExpectedFrameRateRange(range);
```

[segment.ets](https://gitcode.com/harmonyos_samples/fluent-blog/blob/master/entry/src/main/ets/segment/segment.ets#L90-L96)

说明

不建议将ExpectedFrameRateRange中的expected、min、max都设置为120，这会干扰系统的可变帧率机制，增加负载，影响整机性能和功耗。

如setExpectedFrameRateRange({ expected: 120, min: 120, max: 120 })。

### 基于LTPO实现滑动条

**效果展示**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/_DilYC4CQxmVIOBbdMzZTQ/zh-cn_image_0000002193850184.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=E80E77D9BC837136E51BC2E67CD1E8A14D4D20BA7D282B5732EE81AC1044F02C)

**功耗对比**

说明

使用animateTo实现滑动动画，通过设置可变帧率，可以观察功耗差异。

功耗测试方法参考章节2。

开启手机帧率设置，查看帧率变化；使用Profiler工具，查看功耗变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/cf66-jliSfKm6WwrM7-JXg/zh-cn_image_0000002229450057.png?HW-CC-KV=V1&HW-CC-Date=20260428T002238Z&HW-CC-Expire=86400&HW-CC-Sign=4DA927793F38255353036F8F8DAA26758779FFE658E14BF0900AEF4CB62ACC53 "点击放大")

屏幕刷新率降低时，功耗也会降低。

传入可变帧率（ExpectedFrameRateRange），屏幕感知后充分利用LTPO技术降低功耗。屏幕帧率不始终处于最高，因此功耗较低。

**代码实现**

在滑动条中添加onVisibleAreaChange事件，并在回调函数中将滑块的当前值增加到100。

```
1. Slider({ value: this.curTime, min: 0, max: 100 })
2. .enabled(false)
3. .height(4)
4. .width(320)
5. .trackThickness(3)
6. .blockColor(Color.Red)
7. .blockSize({ width: 4, height: 4 })
8. .onVisibleAreaChange([0.0, 1.0], (isVisible: boolean, currentRatio: number) => {
9. if (isVisible) {
10. this.getUIContext().animateTo({
11. duration: DURATION,
12. iterations: -1,
13. expectedFrameRateRange: {
14. expected: 30,
15. min: 0,
16. max: 120,
17. },
18. }, () => {
19. if (this.curTime >= 100) {
20. this.curTime = 0;
21. }
22. for (let i = 0; i < 101; i++) {
23. this.curTime += 1;
24. }
25. })
26. }
27. })
```

[SampleUnitAVPlayView.ets](https://gitcode.com/harmonyos_samples/fluent-blog/blob/master/entry/src/main/ets/view/SampleUnitAVPlayView.ets#L101-L127)

## 总结

综上所述，使用LTPO技术可以控制动效刷新率，降低屏幕功耗，延长续航时间，提升使用体验。开发时推荐使用可变帧率接口，享受功耗优化。

## 示例代码

* [实现流畅刷文章功能](https://gitcode.com/harmonyos_samples/fluent-blog)
