---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arworld
title: 物体摆放（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 命中检测 > 物体摆放（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:fcb617b4e416f2cd47c62348cd16430315980d74ff9c62032f4f7289ac423ffa
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

物体摆放能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

AR物体摆放主要依赖[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，以下接口为AR物体摆放相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARViewContext.init](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextinit) | 初始化[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，初始化AR会话和设置AR渲染场景等。 |
| [ARViewContext.pause](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextpause) | 暂停相机跟踪与AR场景渲染。 |
| [ARViewContext.destroy](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextdestroy) | 销毁[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，释放ARView使用资源，包括AR会话与呈现场景销毁，在退出ARView场景时使用。 |
| [ARViewContext.resume](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextresume) | 用于恢复暂停的相机跟踪与AR场景渲染。 |
| [ARViewContext.scene](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextscene) | 设置ARView的AR场景。 |
| [ARViewContext.scene](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextscene-1) | 获得的AR呈现场景，用于管理空间节点。 |
| [ARViewContext.session](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextsession) | 获取AR会话，用于获取相关AR环境跟踪、相机跟踪、命中检测等能力，如相机位姿、平面信息、创建锚点等。 |
| [ARViewContext.config](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextconfig) | 设置AR会话的配置文件，如北向坐标、性能模式等。 |
| [ARViewContext.callback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextcallback) | 设置回调函数，以根据回调功能实现对应业务逻辑。 |
| [ARFrame.getCamera](../harmonyos-references/arengine-api-arengine.md#arframegetcamera) | 获取当前帧的摄像机参数对象。 |
| [ARFrame.getUpdatedTrackables](../harmonyos-references/arengine-api-arengine.md#arframegetupdatedtrackables) | 获取更新后的指定类型的可追踪对象。 |
| [ARFrame.hitTest](../harmonyos-references/arengine-api-arengine.md#arframehittest) | 根据相机投射光线，获取预览区域中的像素坐标（pixelX和pixelY）来确定射线方向，然后检测这个射线在平面或点云中是否有交点。 |
| [ARAnchor.getPose](../harmonyos-references/arengine-api-arengine.md#aranchorgetpose) | 获取锚点在世界坐标系中的位姿信息。 |
| [ARHitResult.getHitPose](../harmonyos-references/arengine-api-arengine.md#arhitresultgethitpose) | 获取交点位姿。 |
| [ARHitResult.getTrackable](../harmonyos-references/arengine-api-arengine.md#arhitresultgettrackable) | 获取被命中的可追踪对象。 |
| [ARPose.getMatrix](../harmonyos-references/arengine-api-arengine.md#arposegetmatrix) | 将位姿数据转换为一个4x4的矩阵。 |

## 开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)绘制识别的平面。关于AGP的介绍可以查看[ArkGraphics 3D简介](arkgraphics3d-overview.md)和[AGP引擎](https://gitcode.com/openharmony/graphic_graphic_3d)。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

AR物体摆放所需要导入的模块如下。

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';
```

### 定义变量

定义变量hitAnchorList存储放置物体处的锚点信息、hitPoseList存储放置物体处的位姿信息和statusBarHeight设备状态栏高度。

用户点击设备的坐标和显示预览流的坐标不一致，预览流的窗口略小于设备屏幕，因此需要减去设备状态栏高度以获取准确的点击坐标。

```
1. let frame: arEngine.ARFrame;
2. let hitAnchorList: arEngine.ARAnchor[] = [];
3. let hitPoseList: Vec3[] = [];
4. let statusBarHeight: number = 0;
```

### 显示预览流

在ARView中加入点击事件，进行碰撞检测，获取锚点位姿数据加入列表。

```
1. @Builder
2. export function ARWorldBuilder(): void {
3. ARWorld();
4. }

6. @Component
7. struct ARWorld {
8. @State arContext?: arViewController.ARViewContext = undefined;
9. @State context: Context = this.getUIContext().getHostContext() as Context;

11. build(): void {
12. NavDestination() {
13. RelativeContainer() {
14. if (this.arContext) {
15. ARView({ context: this.arContext })
16. .height('100%')
17. .width('100%')
18. .alignRules({
19. center: { anchor: '__container__', align: VerticalAlign.Center },
20. middle: { anchor: '__container__', align: HorizontalAlign.Center }
21. })
22. .onClick((event: ClickEvent) => {
23. this.objectCollisionDetection(event);
24. })
25. }
26. }
27. }
28. .onAppear(() => {
29. this.initARView();
30. this.getAvoidArea();
31. })
32. .onWillDisappear(() => {
33. this.stopARView();
34. })
35. .onShown(() => {
36. this.resumeARView();
37. })
38. .onHidden(() => {
39. this.pauseARView();
40. })
41. .hideTitleBar(true)
42. .hideBackButton(true)
43. .hideToolBar(true)
44. }

46. // 获取用户点击坐标，获取碰撞检测结果
47. private objectCollisionDetection(event: ClickEvent): void {
48. let x: number = this.getUIContext().vp2px(event.windowX);
49. let y: number = this.getUIContext().vp2px(event.windowY) - statusBarHeight;
50. console.info(`Get onclick position, x: ${x} y: ${y}.`);

52. try {
53. let result: arEngine.ARHitResult[] = frame.hitTest(x, y);
54. console.info(`The hitResult size is: ${result.length}.`);
55. if (!result) {
56. return;
57. }

59. for (let i = 0; i < result.length; i++) {
60. let hitResult: arEngine.ARHitResult = result[i];
61. let trackable: arEngine.ARTrackable = hitResult.getTrackable();

63. if (trackable.type !== arEngine.ARTrackableType.PLANE) {
64. continue;
65. }

67. let hitPlane: arEngine.ARPlane = trackable as arEngine.ARPlane;
68. let hitPose: arEngine.ARPose = hitResult.getHitPose();
69. let inPolygon: boolean = hitPlane.isPoseInPolygon(hitPose);
70. let distance: number = hitResult.distance;
71. console.info(`The hitResult inPolygon is: ${inPolygon}, distance is: ${distance}.`);

73. if (!inPolygon || distance <= 0) {
74. continue;
75. }

77. let hitAnchor: arEngine.ARAnchor = hitResult.createAnchor();
78. let pos: Vec3 = hitAnchor.getPose().translation;

80. hitPoseList.push(pos);
81. hitAnchorList.push(hitAnchor);

83. }
84. console.info('Succeeded in getting hit result.');
85. } catch (error) {
86. const err: BusinessError = error as BusinessError;
87. console.error(`Failed to get hitResults. Code is ${err.code}, message is ${err.message}.`);
88. }
89. }

91. private initARView(): void {
92. Scene.load().then((scene: Scene) => {
93. let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
94. viewContext.scene = scene;
95. viewContext.callback = new ARViewCallbackImpl();
96. viewContext.config = {
97. type: arEngine.ARType.WORLD,
98. planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
99. powerMode: arEngine.ARPowerMode.NORMAL,
100. semanticMode: arEngine.ARSemanticMode.NONE,
101. poseMode: arEngine.ARPoseMode.GRAVITY,
102. depthMode: arEngine.ARDepthMode.AUTOMATIC,
103. meshMode: arEngine.ARMeshMode.DISABLED,
104. focusMode: arEngine.ARFocusMode.AUTO
105. }
106. viewContext.init().then(() => {
107. this.arContext = viewContext;
108. console.info('Succeeded in initializing ARView.');
109. }).catch((err: BusinessError) => {
110. console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
111. })
112. })
113. }

115. // 获取屏幕上减去状态栏的真实高度（预览流高度）
116. private getAvoidArea(): void {
117. let avoidAreaType: window.AvoidAreaType = window.AvoidAreaType.TYPE_SYSTEM;
118. window.getLastWindow(this.context).then((data) => {
119. // 获取顶部状态栏高度
120. let avoidArea: window.AvoidArea = data.getWindowAvoidArea(avoidAreaType);
121. statusBarHeight = avoidArea.topRect.height;
122. console.info(`The statusBarHeight is ${statusBarHeight}.`);
123. }).catch((err: BusinessError) => {
124. console.error(`Failed to obtain the window. Code is ${err.code}, message is ${err.message}.`);
125. })
126. }

128. private stopARView(): void {
129. // ...
130. }
131. private resumeARView(): void {
132. // ...
133. }
134. private pauseARView(): void {
135. // ...
136. }
137. }
```

### 渲染识别的平面和放置的物体

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，获取平面信息。

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

15. let arSession: arEngine.ARSession = ctx.session;

17. try {
18. frame = arSession.getFrame();
19. let camera: arEngine.ARCamera = frame.getCamera();
20. let trackable: arEngine.ARTrackable[] = [];

22. if (camera.state === arEngine.ARTrackingState.TRACKING) {
23. trackable = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
24. console.info(`Succeeded in getting tracking plane，length is: ${trackable.length}.`);  // 输出识别到的平面数量
25. }

27. } catch (error) {
28. const err: BusinessError = error as BusinessError;
29. console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
30. }
31. }
32. }
```
