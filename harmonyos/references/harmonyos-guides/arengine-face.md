---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-face
title: 人脸跟踪（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人脸识别与跟踪 > 人脸跟踪（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d67e9c39a19bef3d0d78752b5b6d271997cb46d9745452d268b76c801fbf3518
---

## 约束与限制

人脸跟踪能力支持部分Phone、部分Tablet、TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_FACE](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

人脸跟踪主要依赖ARFace，以下接口为人脸跟踪的相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe) | 获取AR Engine处理后的一帧数据。 |
| [ARSession.getAllTrackables](../harmonyos-references/arengine-api-arengine.md#arsessiongetalltrackables) | 获取当前session中包含的人脸对象。 |
| [ARFace.getGeometry](../harmonyos-references/arengine-api-arengine.md#arfacegetgeometry) | 返回一个人脸几何对象。 |
| [ARFace.getBlendShapes](../harmonyos-references/arengine-api-arengine.md#arfacegetblendshapes) | 返回一个人脸微表情对象。 |

## 开发步骤

对于使用ArkTS的任何AR应用，首先需要参考[AR特性检查](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口检查当前设备是否支持该特性。若设备支持，创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

人脸跟踪能力所需要导入的模块如下：

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node, Scene } from '@kit.ArkGraphics3D';
3. import { BusinessError } from '@kit.BasicServicesKit';
```

### 定义变量

定义变量face接收人脸对象，定义变量faceGeometry接收人脸几何对象，定义变量faceBlendShapes接收人脸微表情对象。

```
1. let face: arEngine.ARFace;
2. let faceGeometry: arEngine.ARGeometry;
3. let faceBlendShapes: arEngine.ARBlendShapes;
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

更改type为[ARType](../harmonyos-references/arengine-api-arengine.md#artype).FACE，更改cameraLensFacing为[ARCameraLensFacing](../harmonyos-references/arengine-api-arengine.md#arcameralensfacing).FRONT，更改multiFaceMode为[ARMultiFaceMode](../harmonyos-references/arengine-api-arengine.md#armultifacemode).MULTIFACE\_DISABLE，启用前置相机的人脸跟踪能力。

```
1. @Builder
2. export function ARFaceBuilder(): void {
3. ARFace();
4. }

6. @Component
7. struct ARFace {
8. @State arContext?: arViewController.ARViewContext = undefined;
9. // 平面类型
10. private intervalId: number = -1;
11. // 重复调用函数时间间隔为33ms，即设定为30fps
12. private delayInterval: number = 33;

14. build(): void {
15. NavDestination() {
16. RelativeContainer() {
17. if (this.arContext) {
18. ARView({ context: this.arContext })
19. .height('100%')
20. .width('100%')
21. .alignRules({
22. center: { anchor: '__container__', align: VerticalAlign.Center },
23. middle: { anchor: '__container__', align: HorizontalAlign.Center }
24. })
25. }
26. }
27. }
28. .onAppear(() => {
29. this.initARView();
30. // 设定在30fps下更新获取物体体积信息
31. this.intervalId = setInterval(async () => {
32. }, this.delayInterval);
33. })
34. .onWillDisappear(() => {
35. // 退出setInterval函数
36. clearInterval(this.intervalId);
37. this.stopARView();
38. })
39. .onShown(() => {
40. this.resumeARView();
41. })
42. .onHidden(() => {
43. this.pauseARView();
44. })
45. .hideTitleBar(true)
46. .hideBackButton(true)
47. .hideToolBar(true)
48. }

50. private initARView(): void {
51. Scene.load().then((scene: Scene) => {
52. let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
53. viewContext.scene = scene;
54. viewContext.callback = new ARViewCallbackImpl();
55. viewContext.config = {
56. type: arEngine.ARType.FACE,
57. planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
58. semanticMode: arEngine.ARSemanticMode.NONE,
59. meshMode: arEngine.ARMeshMode.DISABLED,
60. focusMode: arEngine.ARFocusMode.AUTO,
61. cameraLensFacing: arEngine.ARCameraLensFacing.FRONT,
62. multiFaceMode: arEngine.ARMultiFaceMode.MULTIFACE_DISABLE,
63. }
64. viewContext.init().then(() => {
65. this.arContext = viewContext;
66. console.info('Succeeded in initializing ARView.');
67. }).catch((err: BusinessError) => {
68. console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
69. })
70. })
71. }

73. private stopARView(): void {
74. // ...
75. }
76. private resumeARView(): void {
77. // ...
78. }
79. private pauseARView(): void {
80. // ...
81. }
82. }
```

### 获取人脸几何数据和微表情数据

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，通过[ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe)方法获取当前帧，通过[ARSession.getAllTrackables](../harmonyos-references/arengine-api-arengine.md#arsessiongetalltrackables)获得当前会话包含的人脸对象数据，通过[ARFace.getGeometry](../harmonyos-references/arengine-api-arengine.md#arfacegetgeometry)和[ARFace.getBlendShapes](../harmonyos-references/arengine-api-arengine.md#arfacegetblendshapes)从人脸对象数据中获取识别到的几何信息和微表情信息，相关变量定义参考[定义变量](arengine-face.md#定义变量)。

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
18. let frame: arEngine.ARFrame = arSession.getFrame();
19. if (frame) {
20. // 获取face信息
21. let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.FACE);
22. for (let i = 0; i < trackables.length; ++i) {
23. if (trackables[i].state !== arEngine.ARTrackingState.TRACKING) {
24. console.error('Face not in tracking state');
25. continue;
26. }
27. face = trackables[i] as arEngine.ARFace;
28. faceGeometry = face.getGeometry();
29. faceBlendShapes = face.getBlendShapes();
30. if(faceGeometry){
31. let tmpVert = faceGeometry.getVertices();
32. let tmpIndices = faceGeometry.getIndices();
33. }
34. if(faceBlendShapes){
35. let tmpData = faceBlendShapes.getData();
36. let tmpTypes = faceBlendShapes.getTypes();
37. }
38. faceGeometry.release();
39. faceBlendShapes.release();
40. }
41. }
42. } catch (error) {
43. const err: BusinessError = error as BusinessError;
44. console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
45. }
46. }
47. }
```
