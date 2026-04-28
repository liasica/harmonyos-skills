---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose
title: 获取设备位姿（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 获取设备位姿（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:51+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5f6128c251c61b8f52908da75b081afb3da208bc911253e3c87ef2bae7e6ee32
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

获取设备位姿支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

获取设备位姿可以通过[ARCamera](../harmonyos-references/arengine-api-arengine.md#arcamera)相机对象获取，以下接口为获取设备位姿接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARCamera.getPose](../harmonyos-references/arengine-api-arengine.md#arcameragetpose) | 获取摄像机在世界空间中的位姿信息。 |

## 开发步骤

### 导入模块

获取设备位姿能力需要依赖以下模块。

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
3. import { BusinessError } from '@kit.BasicServicesKit';
```

Vec3是一个三维向量，用于存储设备的位姿信息。

### 定义变量

定义两个变量pose和stateReason，用于接收pose位姿信息和追踪失败原因。

```
1. let pose: arEngine.ARPose;
2. let stateReason: arEngine.ARTrackingStateReason;
```

### 显示预览流及设备位姿信息

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

在设备界面上显示设备位姿信息及追踪失败原因，使用重复调用函数方法在设备界面上实时更新位姿和追踪失败原因的信息。

```
1. @Builder
2. export function ARPoseBuilder(): void {
3. ARPose();
4. }

6. @Component
7. struct ARPose {
8. @State arContext?: arViewController.ARViewContext = undefined;
9. private intervalId: number = -1;
10. // 重复调用函数时间间隔为33ms，即设定为30fps
11. private delayInterval: number = 33;
12. // 位姿的信息参数
13. @State translation: Vec3 = {
14. x: 0,
15. y: 0,
16. z: 0
17. }
18. // 追踪失败的原因
19. @State reason: arEngine.ARTrackingStateReason = stateReason;

21. build(): void {
22. NavDestination() {
23. RelativeContainer() {
24. if (this.arContext) {
25. ARView({ context: this.arContext })
26. .height('100%')
27. .width('100%')
28. .alignRules({
29. center: { anchor: "__container__", align: VerticalAlign.Center },
30. middle: { anchor: "__container__", align: HorizontalAlign.Center }
31. })

33. // 在屏幕上显示设备位姿信息
34. Column() {
35. Text(`x: ${this.translation.x.toFixed(4)}`)
36. .infoStyles()
37. Text(`y: ${this.translation.y.toFixed(4)}`)
38. .infoStyles()
39. Text(`z: ${this.translation.z.toFixed(4)}`)
40. .infoStyles()
41. Text(`reason: ${this.reason}`)
42. .infoStyles()
43. }
44. .alignItems(HorizontalAlign.Start)
45. .margin({ left: 28, top: 28 })
46. .alignRules({
47. top: { anchor: "__container__", align: VerticalAlign.Top },
48. left: { anchor: "__container__", align: HorizontalAlign.Start }
49. })
50. }
51. }
52. }
53. .onAppear(() => {
54. this.initARView();
55. // 设定在30fps下更新位姿和追踪失败原因的信息
56. this.intervalId = setInterval(() => {
57. if (pose !== undefined) {
58. this.translation = pose.translation;
59. this.reason = stateReason;
60. }
61. }, this.delayInterval);
62. })
63. .onWillDisappear(() => {
64. // 退出setInterval函数
65. clearInterval(this.intervalId);
66. this.stopARView();
67. })
68. .onShown(() => {
69. this.resumeARView();
70. })
71. .onHidden(() => {
72. this.pauseARView();
73. })
74. .hideTitleBar(true)
75. .hideBackButton(true)
76. .hideToolBar(true)
77. }

79. private initARView(): void {
80. // ...
81. }
82. private stopARView(): void {
83. // ...
84. }
85. private resumeARView(): void {
86. // ...
87. }
88. private pauseARView(): void {
89. // ...
90. }
91. }

93. // 界面显示文本样式
94. @Extend(Text)
95. function infoStyles() {
96. .fontColor(Color.Yellow)
97. .fontSize(24)
98. .textShadow({
99. radius: 10,
100. color: Color.Black,
101. offsetX: 0,
102. offsetY: 0
103. })
104. .textAlign(TextAlign.Start)
105. }
```

### 获取设备位姿信息

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法获取AR会话对象arSession，之后通过AR会话对象arSession获取每一帧对应的设备位姿信息。

```
1. class ARViewCallbackImpl extends arViewController.ARViewCallback {
2. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
3. // ...
4. }

6. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
7. // ...
8. }

10. onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
11. if (!ctx.session) {
12. return;
13. }

15. let arSession: arEngine.ARSession = ctx.session; // 获取AR会话

17. try {
18. // 获取每一帧的设备位姿信息及追踪失败的原因
19. let frame: arEngine.ARFrame = arSession.getFrame();
20. pose = frame.getCamera().getPose();
21. stateReason = frame.getCamera().stateReason;
22. } catch (error) {
23. const err: BusinessError = error as BusinessError;
24. console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}`);
25. }
26. }
27. }
```
