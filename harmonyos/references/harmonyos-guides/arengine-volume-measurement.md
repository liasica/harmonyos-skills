---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-volume-measurement
title: 高精几何重建（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 高精几何重建 > 高精几何重建（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:55+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e252863f7ecf28119c078f5ea69b76b895e55cb1b5b220394ca58ae030b9c0ae
---

## 约束与限制

高精几何重建能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

高精几何重建主要依赖[ARSemanticDenseData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedata)，以下接口为高精几何重建的相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe) | 获取AR Engine处理后的一帧数据。 |
| [ARFrame.acquireSemanticDense](../harmonyos-references/arengine-api-arengine.md#arframeacquiresemanticdense) | 返回当前帧的高精几何重建对象数据。 |
| [ARSemanticDenseData.acquireCubeData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedataacquirecubedata) | 返回一个高精几何重建对象的立方体数据信息的列表。 |
| [ARSemanticDenseData.release](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedatarelease) | 释放高精几何重建对象数据。 |

## 开发步骤

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

高精几何重建能力所需要导入的模块如下：

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node, Scene } from '@kit.ArkGraphics3D';
3. import { BusinessError } from '@kit.BasicServicesKit';
```

### 定义变量

定义变量cubeVertexData接收立方体顶点数据，定义变量cubeConfidence接收识别出立方体的置信度数据，定义变量cubeLabel接收立方体的语义信息。

```
1. let cubeVertexData: Array<number>;
2. let cubeConfidence: number;
3. let cubeLabel: arEngine.ARSemanticPlaneLabel;
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

更改semanticDenseMode为[ARSemanticDenseMode](../harmonyos-references/arengine-api-arengine.md#arsemanticdensemode).CUBE\_VOLUME，启用体积测量识别能力。

在设备界面上显示识别到的几何数据信息，使用重复调用函数方法在设备界面上实时更新识别到的几何数据信息。

```
1. @Builder
2. export function ARSemanticDenseBuilder(): void {
3. ARSemanticDense();
4. }

6. @Component
7. struct ARSemanticDense {
8. @State arContext?: arViewController.ARViewContext = undefined;

10. build(): void {
11. NavDestination() {
12. RelativeContainer() {
13. if (this.arContext) {
14. ARView({ context: this.arContext })
15. .height('100%')
16. .width('100%')
17. .alignRules({
18. center: { anchor: '__container__', align: VerticalAlign.Center },
19. middle: { anchor: '__container__', align: HorizontalAlign.Center }
20. })
21. }
22. }
23. }
24. .onAppear(() => {
25. this.initARView();
26. })
27. .onWillDisappear(() => {
28. this.stopARView();
29. })
30. .onShown(() => {
31. this.resumeARView();
32. })
33. .onHidden(() => {
34. this.pauseARView();
35. })
36. .hideTitleBar(true)
37. .hideBackButton(true)
38. .hideToolBar(true)
39. }

41. private initARView(): void {
42. Scene.load().then((scene: Scene) => {
43. let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
44. viewContext.scene = scene;
45. viewContext.callback = new ARViewCallbackImpl();
46. viewContext.config = {
47. type: arEngine.ARType.WORLD,
48. planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
49. powerMode: arEngine.ARPowerMode.NORMAL,
50. semanticDenseMode: arEngine.ARSemanticDenseMode.CUBE_VOLUME, // 开启体积测量
51. poseMode: arEngine.ARPoseMode.GRAVITY,
52. depthMode: arEngine.ARDepthMode.DISABLED,
53. meshMode: arEngine.ARMeshMode.DISABLED,
54. focusMode: arEngine.ARFocusMode.AUTO
55. }
56. viewContext.init().then(() => {
57. this.arContext = viewContext;
58. console.info('Succeeded in initializing ARView.');
59. }).catch((err: BusinessError) => {
60. console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
61. })
62. })
63. }

65. private stopARView(): void {
66. // ...
67. }
68. private resumeARView(): void {
69. // ...
70. }
71. private pauseARView(): void {
72. // ...
73. }
74. }
```

### 获取立方体体积数据

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，通过[ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe)方法获取当前帧，通过[ARFrame.acquireSemanticDense](../harmonyos-references/arengine-api-arengine.md#arframeacquiresemanticdense)获得当前帧的高精几何重建对象数据，通过[ARSemanticDenseData.acquireCubeData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedataacquirecubedata)从高精几何重建对象数据中获取识别到的立方体体积数据，相关变量定义参考[定义变量](arengine-volume-measurement.md#定义变量)。

```
1. class ARViewCallbackImpl extends arViewController.ARViewCallback {
2. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
3. // ...
4. }

6. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
7. // ...
8. }

10. async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
11. if (!ctx.session) {
12. return;
13. }

15. let arSession: arEngine.ARSession = ctx.session;

17. try {
18. let frame: arEngine.ARFrame = arSession.getFrame();
19. if (frame) {
20. let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
21. if(semanticData){
22. if(semanticData.cubeDataSize>0){
23. // 获取第一个Cube的体积数据
24. let semanticCubeData: arEngine.ARSemanticDenseCubeData = semanticData.acquireCubeData()[0];
25. cubeVertexData = semanticCubeData.vertexData;
26. cubeConfidence = semanticCubeData.confidence;
27. cubeLabel = semanticCubeData.label;
28. }
29. await semanticData.release();
30. }
31. }
32. } catch (error) {
33. const err: BusinessError = error as BusinessError;
34. console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
35. }
36. }
37. }
```
