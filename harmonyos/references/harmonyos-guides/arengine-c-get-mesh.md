---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-mesh
title: 获取网格扫描信息（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 环境Mesh识别 > 获取网格扫描信息（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:54+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5bc0a6495a8c252f09bf34bdfaf124f34750f366ab4f8d3453edd4b10d98853c
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

获取网格扫描信息能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_MESH](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR网格扫描相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create) | 创建一个新的[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update) | 更新AR Engine的计算结果。 |
| [HMS\_AREngine\_ARSession\_Configure](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_configure) | 配置[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARFrame\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_create) | 创建一个新的[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到\*outFrame中。 |
| [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry) | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture) | 设置可用于存储相机预览流数据的openGL纹理。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem) | 从可跟踪列表中获取指定index的对象。 |
| [HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [HMS\_AREngine\_ARFrame\_AcquireCamera](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera) | 获取当前帧的相机参数对象。 |
| [HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create) | 分配并初始化一个新的位姿对象。 |
| [HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose) | 获取当前相机对象在AR世界空间中的位姿。 |
| [HMS\_AREngine\_ARFrame\_AcquireSceneMesh](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirescenemesh) | 获取当前帧的mesh信息。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireverticessize) | 获取mesh的顶点个数。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquirevertexlist) | 获取mesh顶点集合。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlistsize) | 获取mesh面片的索引个数。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlist) | 获取mesh面片的索引集合。 |
| [HMS\_AREngine\_ARSceneMesh\_Release](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_release) | 释放当前帧的mesh信息。 |

## 开发步骤

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

创建一个UI界面，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件用于显示相机预览画面，并定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARMesh.ets。
2. import { deviceInfo } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import arEngineDemo from 'libentry.so';

6. @Builder
7. export function ARMeshBuilder() {
8. ARMesh();
9. }

11. @Component
12. struct ARMesh {
13. pageInfo: NavPathStack = new NavPathStack();
14. private interval: number = -1;
15. private xComponentId: string = 'ARMesh';
16. @State context: Context = this.getUIContext().getHostContext() as Context;
17. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
18. @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

20. build(): void {
21. NavDestination() {
22. RelativeContainer() {
23. XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
24. .width('100%')
25. .height('100%')
26. .alignRules({
27. center: { anchor: '__container__', align: VerticalAlign.Center },
28. middle: { anchor: '__container__', align: HorizontalAlign.Center }
29. })
30. .onLoad(() => {
31. console.info(`XComponent onLoad ${this.xComponentId}.`);
32. this.interval = setInterval(() => {
33. // 调用更新Native API来更新AR Engine每帧的计算结果
34. arEngineDemo.update(this.xComponentId);
35. }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
36. })
37. .onDestroy(() => {
38. console.info(`XComponent onDestroy ${this.xComponentId}.`);
39. clearInterval(this.interval);
40. })
41. }
42. }
43. .onAppear(() => {
44. arEngineDemo.init(this.resMgr);
45. let config: Int32Array = new Int32Array([1, this.rotation]);
46. arEngineDemo.start(this.xComponentId, config);
47. })
48. .onWillDisappear(() => {
49. arEngineDemo.stop(this.xComponentId);
50. })
51. .onShown(() => {
52. arEngineDemo.show(this.xComponentId);
53. })
54. .onHidden(() => {
55. arEngineDemo.hide(this.xComponentId);
56. })
57. .onReady((context: NavDestinationContext) => {
58. this.pageInfo = context.pathStack;
59. })
60. .hideTitleBar(true)
61. .hideBackButton(true)
62. .hideToolBar(true)
63. }
64. }
```

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话

创建AR会话并配置为开启mesh模式。

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 设置mesh模式为开启状态。
8. HMS_AREngine_ARConfig_SetMeshMode(arSession, arConfig, ARENGINE_MESH_MODE_ENABLED);
9. // 配置器设置给AR会话。
10. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### 获取当前环境中的mesh信息

调用[HMS\_AREngine\_ARFrame\_AcquireSceneMesh](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirescenemesh)函数，获取当前环境中的mesh信息，并将结果存放在sceneMesh中。

```
1. AREngine_ARFrame *arFrame = nullptr;
2. // 创建AR单帧对象
3. HMS_AREngine_ARFrame_Create(arSession, &arFrame);
4. AREngine_ARSceneMesh *sceneMesh = nullptr;
5. // 获取当前帧的mesh信息
6. HMS_AREngine_ARFrame_AcquireSceneMesh(arSession, arFrame, &sceneMesh);
```

### 获取当前mesh信息对应的mesh顶点信息

1. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireverticessize)函数，获取mesh顶点信息包含的浮点数数量，每三个浮点数组成一个mesh顶点，将结果存放在meshVerticesSize 中。

   ```
   1. int32_t meshVerticesSize = 0;
   2. // 获取mesh顶点信息包含的浮点数数量
   3. HMS_AREngine_ARSceneMesh_AcquireVerticesSize(arSession, sceneMesh, &meshVerticesSize);
   ```
2. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquirevertexlist)函数，获取mesh顶点信息，并将结果保存在meshVertices中。

   ```
   1. float *meshVertices = new float[meshVerticesSize];
   2. // 获取mesh顶点信息
   3. HMS_AREngine_ARSceneMesh_AcquireVertexList(arSession, sceneMesh, meshVertices, meshVerticesSize);
   4. // 获取mesh顶点个数
   5. int32_t mPointsNum = meshVerticesSize / 3;
   ```

### 获取当前mesh信息对应的mesh面片信息

1. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlistsize)函数，获取mesh面片信息对应顶点的索引个数，每三个顶点索引表示一个mesh面片，将结果存放在triangleIndicesSize 中。

   ```
   1. int32_t triangleIndicesSize = 0;
   2. // 获取mesh面片信息对应顶点的索引个数
   3. HMS_AREngine_ARSceneMesh_AcquireIndexListSize(arSession, sceneMesh, &triangleIndicesSize);
   ```
2. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlist)函数，获取mesh面片信息对应顶点的索引列表，并将结果保存在meshTriangleIndices中。

   ```
   1. int32_t *meshTriangleIndices = new int32_t[triangleIndicesSize];
   2. // 获取mesh面片信息对应顶点的索引列表
   3. HMS_AREngine_ARSceneMesh_AcquireIndexList(arSession, sceneMesh, meshTriangleIndices, triangleIndicesSize);
   4. // 获取mesh面片个数
   5. int32_t mTrianglesNum = triangleIndicesSize / 3;
   ```

### 使用完毕后，销毁mesh信息

```
1. void HMS_AREngine_ARSceneMesh_Release(AREngine_ARSceneMesh *sceneMesh);
```
