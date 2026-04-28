---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-face
title: 人脸跟踪（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人脸识别与跟踪 > 人脸跟踪（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f08132daf8cebd507ea4cfbb19f0c71d1d8e0e2024a47d6e55bb1bab39b0509d
---

## 约束与限制

人脸识别与跟踪能力支持部分Phone、部分Tablet设备、TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_FACE](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR Engine人脸跟踪相关接口，详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARConfig\_GetCameraLensFacing](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_getcameralensfacing) | 获取相机镜头朝向。 |
| [HMS\_AREngine\_ARConfig\_GetMultiFaceMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_getmultifacemode) | 获取多人脸检测模式。 |
| [HMS\_AREngine\_ARConfig\_SetCameraLensFacing](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setcameralensfacing) | 设置相机镜头朝向。 |
| [HMS\_AREngine\_ARConfig\_SetMultiFaceMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setmultifacemode) | 设置多人脸检测模式。 |
| [HMS\_AREngine\_ARFace\_AcquireBlendShapes](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_acquireblendshapes) | 获取人脸表情信息。 |
| [HMS\_AREngine\_ARFace\_AcquireGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_acquiregeometry) | 获取人脸几何信息。 |
| [HMS\_AREngine\_ARFace\_AcquireViewMatrix](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_acquireviewmatrix) | 获取当前人脸的面视图矩阵。 |
| [HMS\_AREngine\_ARFace\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_getcenterpose) | 获取从人脸中心点位姿信息。 |
| [HMS\_AREngine\_ARFaceBlendShapes\_AcquireData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_acquiredata) | 获取微表情数据的集合。 |
| [HMS\_AREngine\_ARFaceBlendShapes\_AcquireTypes](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_acquiretypes) | 获取所有微表情参数类型数组。 |
| [HMS\_AREngine\_ARFaceBlendShapes\_GetCount](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_getcount) | 获取人脸微表情数据的个数。 |
| [HMS\_AREngine\_ARFaceBlendShapes\_Release](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfaceblendshapes_release) | 释放当前人脸的blendShapes对象，即由[HMS\_AREngine\_ARFace\_AcquireBlendShapes](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_acquireblendshapes)创建的对象。 |
| [HMS\_AREngine\_ARFaceGeometry\_AcquireIndices](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquireindices) | 获取人脸Mesh中的三角形索引集合。 |
| [HMS\_AREngine\_ARFaceGeometry\_AcquireTexCoord](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquiretexcoord) | 获取人脸Mesh中的纹理坐标集。 |
| [HMS\_AREngine\_ARFaceGeometry\_AcquireTriangleLabels](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquiretrianglelabels) | 获取人脸Mesh中的三角形标签集合。 |
| [HMS\_AREngine\_ARFaceGeometry\_AcquireVertices](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_acquirevertices) | 获取人脸Mesh中的顶点集合。 |
| [HMS\_AREngine\_ARFaceGeometry\_GetIndicesSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_getindicessize) | 获取人脸Mesh中三角形索引的大小。 |
| [HMS\_AREngine\_ARFaceGeometry\_GetTexCoordSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_gettexcoordsize) | 获取人脸Mesh中纹理坐标的大小。 |
| [HMS\_AREngine\_ARFaceGeometry\_GetTriangleCount](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_gettrianglecount) | 获取人脸Mesh中三角形的大小。 |
| [HMS\_AREngine\_ARFaceGeometry\_GetTriangleLabelsSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_gettrianglelabelssize) | 获取人脸Mesh中三角形标签的大小。 |
| [HMS\_AREngine\_ARFaceGeometry\_GetVerticesSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_getverticessize) | 获取人脸Mesh中顶点的大小。 |
| [HMS\_AREngine\_ARFaceGeometry\_Release](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arfacegeometry_release) | 释放当前人脸Mesh对象，即由[HMS\_AREngine\_ARFace\_AcquireBlendShapes](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_acquireblendshapes)创建的对象。 |

## 开发步骤

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

### 创建UI界面

创建一个UI界面，使用XComponent组件用于显示相机预览画面，并定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARFace.ets
2. import { display } from '@kit.ArkUI';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import { systemDateTime } from '@kit.BasicServicesKit';
5. import arEngineDemo from 'libentry.so';

7. @Builder
8. export function ARFaceBuilder() {
9. ARFace();
10. }

12. @Component
13. struct ARFace {
14. pageInfos: NavPathStack = new NavPathStack();
15. @State context: Context = this.getUIContext().getHostContext() as Context;
16. private xComponentId = 'ARFace';
17. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
18. private interval: number = -1;
19. @State rotation: number = display.getDefaultDisplaySync().rotation;

21. build() {
22. NavDestination() {
23. RelativeContainer() {
24. XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
25. .width('100%')
26. .height('100%')
27. .alignRules({
28. center: { anchor: "__container__", align: VerticalAlign.Center },
29. middle: { anchor: "__container__", align: HorizontalAlign.Center }
30. })
31. .onLoad(() => {
32. this.interval = setInterval(() => {
33. // Call the update Native API to update the calculation result of each frame by AR Engine.
34. arEngineDemo.update(this.xComponentId);
35. }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
36. })
37. .onDestroy(() => {
38. clearInterval(this.interval);
39. })

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
58. this.pageInfos = context.pathStack;
59. })
60. .hideTitleBar(true)
61. .hideBackButton(true)
62. .hideToolBar(true)
63. }
64. }
```

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话并配置为开启人脸跟踪模式

使用人脸识别与跟踪能力时请使用[HMS\_AREngine\_ARSession\_Create\_Human\_Perception](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create_human_perception)创建AR会话。

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create_Human_Perception(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 设置ARType为FACE开启人脸跟踪模式。
8. HMS_AREngine_ARConfig_SetARType(arSession, arConfig, ARENGINE_TYPE_FACE)；
9. // （可选）设置为前置相机
10. HMS_AREngine_ARConfig_SetCameraLensFacing(arSession, arConfig, ARENGINE_CAMERA_FACING_FRONT);
11. // （可选）设置为多人脸模式
12. HMS_AREngine_ARConfig_SetMultiFaceMode(arSession, arConfig, ARENGINE_MULTIFACE_ENABLE);
13. // 配置器设置给AR会话。
14. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### 获取当前环境中的人脸信息

1. 创建一个可追踪对象列表trackableList，用于存放人脸跟踪模式下AR Engine运行过程中检测到的所有人脸。

   ```
   1. AREngine_ARTrackableList *trackableList = nullptr;
   2. HMS_AREngine_ARTrackableList_Create(arSession, &trackableList);
   3. // 调用HMS_AREngine_ARSession_GetAllTrackables函数，检测当前环境中的所有人脸，并将结果存放在trackableList中。
   4. HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList);
   ```
2. 获取平面数量调用[HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)函数获取可追踪对象数量，结果存放在trackableListSize中。

   ```
   1. int32_t trackableListSize = 0;
   2. HMS_AREngine_ARTrackableList_GetSize(arSession, trackableList, &trackableListSize);
   3. // 未设置多人脸模式时，最多同时跟踪1个人脸信息，设置后最多同时跟踪3个人脸信息
   ```
3. 转化为人脸信息对象[AREngine\_ARFace](../harmonyos-references/arengine-capi-arengine.md#arengine_arface)。

   ```
   1. for (int i = 0; i < trackableListSize; ++i) {
   2. // 遍历所有人脸信息对象，根据您的应用进行处理。
   3. AREngine_ARTrackable *arTrackable = nullptr;
   4. HMS_AREngine_ARTrackableList_AcquireItem(arSession, trackableList, i, &arTrackable);
   5. AREngine_ARFace *arFace = reinterpret_cast<AREngine_ARFace*>(arTrackable);
   6. }
   ```

## 获取当前人脸的位姿信息

1. 先通过[HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create)接口创建一个[ARPose](../harmonyos-references/arengine-capi-arengine.md#arengine_arpose)对象，然后调用[HMS\_AREngine\_ARFace\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_getcenterpose)，获取当前人脸的位姿信息。

   ```
   1. AREngine_ARPose *facePose = nullptr;
   2. HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &facePose);
   3. HMS_AREngine_ARFace_GetCenterPose(arSession, arFace, facePose);
   ```
2. 获取当前人脸的视图矩阵。

   调用[HMS\_AREngine\_ARFace\_AcquireViewMatrix](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_acquireviewmatrix)函数，获取当前人脸的视图矩阵，该矩阵用于后续生成MVP矩阵实现渲染。

   ```
   1. float *viewMatrix = new float[16];
   2. int size = 16;
   3. auto result = HMS_AREngine_ARFace_AcquireViewMatrix(arSession, arFace, viewMatrix, size);
   ```
3. 获取当前人脸的几何信息。

   调用[HMS\_AREngine\_ARFace\_AcquireGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arface_acquiregeometry)，获取当前人脸的几何信息，并将结果存放在arFaceGeometry中。

   ```
   1. AREngine_ARFaceGeometry* arFaceGeometry = nullptr;
   2. HMS_AREngine_ARFace_AcquireGeometry(arSession, arFace, &arFaceGeometry);
   ```
4. 获取人脸的几何信息中的三角形顶点。

   ```
   1. // 调用HMS_AREngine_ARFaceGeometry_GetTriangleCount函数，获取人脸几何信息中的三角形数量
   2. int triangleCount = 0;
   3. HMS_AREngine_ARFaceGeometry_GetTriangleCount(arSession, arFaceGeometry, &triangleCount);
   4. // 调用HMS_AREngine_ARFaceGeometry_GetVerticesSize函数，获取人脸几何信息中的三角形顶点数量
   5. int verticesSize = 0;
   6. HMS_AREngine_ARFaceGeometry_GetVerticesSize(arSession, arFaceGeometry, &verticesSize);
   7. // 调用HMS_AREngine_ARFaceGeometry_AcquireVertices函数，获取人脸几何信息中的三角形顶点集合
   8. const float *meshVertices = nullptr;
   9. HMS_AREngine_ARFaceGeometry_AcquireVertices(arSession, arFaceGeometry, &meshVertices);
   ```
5. 获取人脸的几何信息中的三角形面片。

   ```
   1. // 调用HMS_AREngine_ARFaceGeometry_GetIndicesSize函数，获取三角形面片对应顶点的索引个数，每三个顶点索引表示一个三角形面片
   2. int indicesSize = 0;
   3. HMS_AREngine_ARFaceGeometry_GetIndicesSize(arSession, arFaceGeometry, &indicesSize);
   4. // 调用HMS_AREngine_ARFaceGeometry_AcquireIndices函数，获取三角形面片对应顶点的索引列表
   5. int32_t *meshTriangleIndices = nullptr;
   6. HMS_AREngine_ARFaceGeometry_AcquireIndices(arSession, arFaceGeometry, &meshTriangleIndices);
   ```
6. 获取人脸的几何信息中的三角形面片的语义标签。

   ```
   1. // 调用HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize函数，获取三角形面片语义标签数量
   2. int triangleLabelsSize = 0;
   3. HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize(arSession, arFaceGeometry, &triangleLabelsSize);
   4. // 调用HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels函数，获取三角形面片语义标签集合
   5. const AREngine_ARAnimojiTriangleLabel* triangleLabels = nullptr;
   6. HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels(arSession, arFaceGeometry, &triangleLabels);
   ```
7. 获取人脸几何信息中的UV纹理坐标。

   ```
   1. // 调用HMS_AREngine_ARFaceGeometry_GetTexCoordSize函数，获取UV纹理坐标数量
   2. int texCoordSize = 0;
   3. HMS_AREngine_ARFaceGeometry_GetTexCoordSize(arSession, arFaceGeometry, &texCoordSize);
   4. // 调用HMS_AREngine_ARFaceGeometry_AcquireTexCoord函数，获取UV纹理坐标集合
   5. const float* texCoords = nullptr;
   6. HMS_AREngine_ARFaceGeometry_AcquireTexCoord(arSession, arFaceGeometry, &texCoords);
   ```
8. 获取当前人脸的微表情信息。

   ```
   1. // 调用HMS_AREngine_ARFace_AcquireBlendShapes，获取当前人脸的微表情信息，并将结果存放在arFaceBlendShapes中。
   2. AREngine_ARFaceBlendShapes* arFaceBlendShapes = nullptr;
   3. HMS_AREngine_ARFace_AcquireBlendShapes(arSession, arFace, &arFaceBlendShapes);
   4. // 调用HMS_AREngine_ARFace_AcquireBlendShapes，获取当前人脸的微表情的数量
   5. int count = 0;
   6. HMS_AREngine_ARFaceBlendShapes_GetCount(arSession, arFaceBlendShapes, &count);
   7. // 调用HMS_AREngine_ARFaceBlendShapes_AcquireTypes，获取当前人脸的微表情的标签集合
   8. const AREngine_ARAnimojiBlendShape* blendShapesTypes = nullptr;
   9. HMS_AREngine_ARFaceBlendShapes_AcquireTypes(arSession, arFaceBlendShapes, &blendShapesTypes);
   10. // 调用HMS_AREngine_ARFaceBlendShapes_AcquireData，获取当前人脸的微表情的数据集合，集合中的元素表示该位置在标签集合中表示的微表情的变化程度
   11. const float *blendShapesData = nullptr;
   12. HMS_AREngine_ARFaceBlendShapes_AcquireData(arSession, arFaceBlendShapes, &blendShapesData);
   ```
