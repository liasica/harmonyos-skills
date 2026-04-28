---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-plane
title: 检测环境中的平面（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 平面识别 > 检测环境中的平面（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9ccc1c05c58ed7d7bea9e7e4a0c0144d06723703368a70e9454ab0e008e1e156
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

检测环境平面能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

检测平面通过[ARPlane](../harmonyos-references/arengine-api-arengine.md#arplane)平面对象进行，以下接口为平面相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARTrackable.getPose](../harmonyos-references/arengine-api-arengine.md#artrackablegetpose) | 获取追踪目标的位姿信息。 |
| [ARTrackable.getAnchors](../harmonyos-references/arengine-api-arengine.md#artrackablegetanchors) | 获取绑定到输入可跟踪对象的锚点对象。 |
| [ARPose.getMatrix](../harmonyos-references/arengine-api-arengine.md#arposegetmatrix) | 将位姿数据转换为一个4x4的矩阵。 |
| [ARPlane.getPolygonXZ](../harmonyos-references/arengine-api-arengine.md#arplanegetpolygonxz) | 获取检测到的平面2D顶点数组。 |
| [ARPlane.getSubsumedBy](../harmonyos-references/arengine-api-arengine.md#arplanegetsubsumedby) | 获取平面的父平面（当平面与另一个平面合并时会生成父平面）。 |
| [ARPlane.isPoseInExtents](../harmonyos-references/arengine-api-arengine.md#arplaneisposeinextents) | 检查给定位姿是否在平面的边界矩形内。 |
| [ARPlane.isPoseInPolygon](../harmonyos-references/arengine-api-arengine.md#arplaneisposeinpolygon) | 检查给定位姿是否在平面的边界多边形内。 |

## 开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)绘制识别的平面。关于AGP的介绍可以查看[ArkGraphics 3D简介](arkgraphics3d-overview.md)和[AGP引擎](https://gitcode.com/openharmony/graphic_graphic_3d)。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

平面检测能力所需的模块导入如下：

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { Matrix4 } from '@kit.ArkUI';
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

```
1. @Builder
2. export function ARPlaneBuilder(): void {
3. ARPlane();
4. }

6. @Component
7. struct ARPlane {
8. @State arContext?: arViewController.ARViewContext = undefined;

10. build(): void {
11. // ...
12. }

14. private initARView(): void {
15. // ...
16. }
17. private stopARView(): void {
18. // ...
19. }
20. private resumeARView(): void {
21. // ...
22. }
23. private pauseARView(): void {
24. // ...
25. }
26. }
```

### 检测环境平面

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，通过[ARSession.getAllTrackables](../harmonyos-references/arengine-api-arengine.md#arsessiongetalltrackables)方法获取所有识别到的平面。

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
19. let camera: arEngine.ARCamera = frame.getCamera();
20. let trackable: arEngine.ARTrackable[] = [];

22. if (camera.state === arEngine.ARTrackingState.TRACKING) {
23. trackable = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
24. console.info(`Succeeded in getting tracking plane, length is: ${trackable.length}`);  // 打印当前识别到的平面数量
25. }

27. } catch (error) {
28. const err: BusinessError = error as BusinessError;
29. console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
30. }
31. }
32. }
```

### 检测平面的自定义方法

自定义方法获取顶点数据getVertices、创建索引generateMeshIndex、创建mesh数据generateMeshInput。

```
1. // 获取三维空间顶点坐标，第一个入参的位姿矩阵按垂直列排列，第二个坐标点为(x, 0, z, 1)，对应x-z平面。
2. export function getVertices(mat: Matrix4, point: number[]): Vec3[] {
3. let result: Vec3[] = [];
4. for (let i = 0; i < point.length; i += 2) {
5. let single: Vec3 = {
6. x: (mat[2] * point[i] + mat[6] * 0
7. + mat[10] * point[i + 1] + mat[14] * 1.0),
8. y: mat[1] * point[i] + mat[5] * 0
9. + mat[9] * point[i + 1] + mat[13] * 1.0,
10. z: -(mat[0] * point[i] + mat[4] * 0
11. + mat[8] * point[i + 1] + mat[12] * 1.0),
12. }
13. result.push(single);
14. }
15. return result;
16. }
17. // 创建 ARWorld 的 mesh索引。由于平面是由三角形拼接而成的，因此每个平面上的每个三角形的首个顶点索引都是相同的。
18. export function generateMeshIndex(input: Vec3[][]): number[] {
19. let result: number[] = [];
20. let start: number = 0;

22. for (let i = 0; i < input.length; i++) {
23. let length: number = input[i].length;

25. for (let j = start + 1; j < start + length - 1; j++) {
26. result.push(start);
27. result.push(j);
28. result.push(j + 1);
29. }
30. start += length;
31. }
32. return result;
33. }

35. export function generateMeshInput(vex: Vec3[][]): Vec3[] {
36. let result: Vec3[] = [];
37. for (let i = 0; i < vex.length; i++) {
38. let tmp: Vec3[] = vex[i];
39. for (let j = 0; j < tmp.length; j++) {
40. result.push(tmp[j]);
41. }
42. }
43. return result;
44. }
```
