---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arworld
title: 物体摆放（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 命中检测 > 物体摆放（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:58e339e9a21bda12f87cd60faac322866f548663b802bb6faa5d6491958bfdd2
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

物体摆放能力支持部分Phone、Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR物体摆放相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create) | 创建一个新的[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update) | 更新AR Engine的计算结果。 |
| [HMS\_AREngine\_ARSession\_Configure](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_configure) | 配置[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARFrame\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_create) | 创建一个新的[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到中\*outFrame。 |
| [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry) | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture) | 设置可用于存储相机预览流数据的openGL纹理。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem) | 从可跟踪列表中获取指定index的对象。 |
| [HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [HMS\_AREngine\_ARFrame\_HitTest](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_hittest) | 根据屏幕上兴趣点位置获取命中检测结果。 |
| [HMS\_AREngine\_ARHitResultList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arhitresultlist_getsize) | 获取命中检测结果对象列表中包含的对象数。 |
| [HMS\_AREngine\_ARHitResultList\_GetItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arhitresultlist_getitem) | 在命中检测结果列表中获取指定索引的命中检测结果对象。 |
| [HMS\_AREngine\_ARHitResult\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arhitresult_create) | 创建一个空的命中检测结果对象。 |
| [HMS\_AREngine\_ARHitResult\_AcquireNewAnchor](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arhitresult_acquirenewanchor) | 在碰撞命中位置创建一个新的锚点。 |
| [HMS\_AREngine\_ARHitResult\_AcquireTrackable](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arhitresult_acquiretrackable) | 获取被命中的可追踪对象。 |
| [HMS\_AREngine\_ARFrame\_AcquireCamera](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera) | 获取当前帧的相机参数对象。 |
| [HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create) | 分配并初始化一个新的位姿对象。 |
| [HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose) | 获取当前相机对象在AR世界空间中的位姿。 |

## 开发步骤

### 声明Native接口

ArkTS接口声明。

```
1. import { resourceManager } from '@kit.LocalizationKit';

3. export const start: (id: string, params: Int32Array) => void;
4. export const show: (id: string) => void;
5. export const hide: (id: string) => void;
6. export const update: (id: string) => number;
7. export const stop: (id: string) => void;
8. export const init: (resmgr: resourceManager.ResourceManager) => void;
9. export const getDistance: (id: string) => string;
10. export const initImage: (id: string, width: number, height: number, buffer: ArrayBuffer) => number;
11. export const setPath: (id: string, path: string) => void;
12. export const saveImageDataBaseToLocal: (id: string, path: string) => void;
13. export const getImageCount: (id: string) => number;
14. export const getVolume: (id: string) => string;
```

建立ArkTS接口与C++接口之间的映射。

```
1. napi_property_descriptor desc[] = {
2. {"init", nullptr, Global::Init, nullptr, nullptr, nullptr, napi_default, nullptr},
3. {"start", nullptr, NapiManager::NapiOnPageAppear, nullptr, nullptr, nullptr, napi_default, nullptr},
4. {"show", nullptr, NapiManager::NapiOnPageShow, nullptr, nullptr, nullptr, napi_default, nullptr},
5. {"hide", nullptr, NapiManager::NapiOnPageHide, nullptr, nullptr, nullptr, napi_default, nullptr},
6. {"update", nullptr, NapiManager::NapiOnPageUpdate, nullptr, nullptr, nullptr, napi_default, nullptr},
7. {"stop", nullptr, NapiManager::NapiOnPageDisappear, nullptr, nullptr, nullptr, napi_default, nullptr},
8. {"getDistance", nullptr, NapiManager::NapiGetDistance, nullptr, nullptr, nullptr, napi_default, nullptr},
9. {"initImage", nullptr, NapiManager::NapiInitImage, nullptr, nullptr, nullptr, napi_default, nullptr},
10. {"setPath", nullptr, NapiManager::NapiSetPath, nullptr, nullptr, nullptr, napi_default, nullptr},
11. {"saveImageDataBaseToLocal", nullptr, NapiManager::NapiSaveImageDataBaseToLocal, nullptr, nullptr, nullptr,
12. napi_default, nullptr},
13. {"getImageCount", nullptr, NapiManager::NapiGetImageCount, nullptr, nullptr, nullptr, napi_default, nullptr},
14. {"getVolume", nullptr, NapiManager::NapiGetVolume, nullptr, nullptr, nullptr, napi_default, nullptr}
15. };
```

### 创建UI界面

创建一个UI界面，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件用于显示相机预览画面，并定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARWorld.ets。
2. import { PromptAction } from '@kit.ArkUI';
3. import { deviceInfo } from '@kit.BasicServicesKit';
4. import { resourceManager } from '@kit.LocalizationKit';
5. import arEngineDemo from 'libentry.so';

7. @Builder
8. export function ARWorldBuilder() {
9. ARWorld();
10. }

12. @Component
13. struct ARWorld {
14. pageInfo: NavPathStack = new NavPathStack();
15. private currentMillisecond: number = 0;
16. private interval: number = -1;
17. private isUpdate: boolean = true;
18. private xComponentId: string = 'ARWorld';
19. @State context: Context = this.getUIContext().getHostContext() as Context;
20. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
21. @State numberOfPlans: number = 0;
22. @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

24. build(): void {
25. NavDestination() {
26. RelativeContainer() {
27. XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
28. .width('100%')
29. .height('100%')
30. .alignRules({
31. center: { anchor: '__container__', align: VerticalAlign.Center },
32. middle: { anchor: '__container__', align: HorizontalAlign.Center }
33. })
34. .onLoad(() => {
35. this.interval = setInterval(() => {
36. if (this.isUpdate) {
37. // 每一帧通过调用AR Engine的Native API update来更新计算结果
38. this.numberOfPlans = arEngineDemo.update(this.xComponentId);
39. this.planeNum();
40. }
41. }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
42. })
43. .onDestroy(() => {
44. clearInterval(this.interval);
45. })
46. }
47. }
48. .onAppear(() => {
49. arEngineDemo.init(this.resMgr);
50. let config: Int32Array = new Int32Array([1, this.rotation]);
51. arEngineDemo.start(this.xComponentId, config);
52. })
53. .onWillDisappear(() => {
54. arEngineDemo.stop(this.xComponentId);
55. })
56. .onShown(() => {
57. this.isUpdate = true;
58. arEngineDemo.show(this.xComponentId);
59. })
60. .onHidden(() => {
61. this.isUpdate = false;
62. arEngineDemo.hide(this.xComponentId);
63. })
64. .onReady((context: NavDestinationContext) => {
65. this.pageInfo = context.pathStack;
66. })
67. .hideTitleBar(true)
68. .hideBackButton(true)
69. .hideToolBar(true)
70. }

72. private messageNotification(): void {
73. let promptAction: PromptAction = this.getUIContext().getPromptAction();
74. promptAction.showToast({
75. message: '当前特征点较少，无法识别平面，请移动相机。',
76. bottom: 300
77. })
78. }

80. private planeNum(): void {
81. if (this.numberOfPlans < 1) {
82. // 平面数量少于1
83. let tempMillisecond: number = new Date().getTime();
84. // 为首次启动的时间分配一个值
85. if (this.currentMillisecond === 0) {
86. this.currentMillisecond = tempMillisecond;
87. return;
88. }
89. // 当识别平面时间超过10s，则展示一个弹窗
90. if (tempMillisecond - this.currentMillisecond > 10000) {
91. this.messageNotification();
92. this.currentMillisecond = 0;
93. }
94. } else {
95. this.currentMillisecond = 0;
96. }
97. }
98. }
```

### 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

### 创建AR场景

1. 调用[HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create)函数创建[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。您可以参考[管理AR会话](arengine-c-arsession.md)创建ARSession。
2. 配置AR会话及预览尺寸。

   ```
   1. // 【可选】创建一个拥有合理默认配置的配置对象。
   2. AREngine_ARConfig *arConfig = nullptr;
   3. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
   4. // 【可选】配置AREngine_ARSession会话。
   5. HMS_AREngine_ARSession_Configure(arSession, arConfig);
   6. // 【可选】释放指定的配置对象的内存空间。
   7. HMS_AREngine_ARConfig_Destroy(arConfig);

   9. // 创建一个新的AREngine_ARFrame对象。
   10. AREngine_ARFrame *arFrame = nullptr;
   11. HMS_AREngine_ARFrame_Create(arSession, &arFrame);
   12. // 预览区域的实际宽高，如使用xComponent组件显示，则该宽和高是xComponent的宽和高，如果不一致，会导致显示相机预览出错。
   13. int32_t width = 1440;
   14. int32_t height = 1080;
   15. // 显示旋转常量，值为AREngine_ARPoseType中定义的枚举值。
   16. AREngine_ARPoseType displayRotation = ARENGINE_POSE_TYPE_IDENTITY;
   17. // 设置显示的宽和高（以Pixel为单位）。
   18. HMS_AREngine_ARSession_SetDisplayGeometry(arSession, displayRotation, width, height);
   ```
3. 通过OpenGL接口获取纹理ID。

   ```
   1. // 通过openGL接口获取纹理ID。
   2. GLuint textureId = 0;
   3. glGenTextures(1, &textureId);
   ```
4. 设置OpenGL纹理，存储相机预览流数据。

   ```
   1. // 设置可用于存储相机预览流数据的openGL纹理。
   2. HMS_AREngine_ARSession_SetCameraGLTexture(arSession, textureId );
   ```

### 获取平面

1. 调用[HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update)函数更新当前[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象。

   ```
   1. // 获取帧数据AREngine_ARFrame。
   2. HMS_AREngine_ARSession_Update(arSession, arFrame);
   ```
2. 获取相机的视图矩阵和相机的投影矩阵，用于后续渲染。

   ```
   1. // 根据AREngine_ARFrame对象可以获取相机对象AREngine_ARCamera。
   2. AREngine_ARCamera *arCamera = nullptr;
   3. HMS_AREngine_ARFrame_AcquireCamera(arSession, arFrame, &arCamera);
   4. // 获取最新帧中相机的视图矩阵。
   5. HMS_AREngine_ARCamera_GetViewMatrix(arSession, arCamera, glm::value_ptr(*viewMat), 16);
   6. // 获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。Near (0.1) Far (100)。
   7. HMS_AREngine_ARCamera_GetProjectionMatrix(arSession, arCamera, {0.1f, 100.f}, glm::value_ptr(*projectionMat), 16);
   ```

   说明

   这里直接获取相机的视图矩阵和相机的投影矩阵，是为了便于渲染。获取相机运动中的位姿变化，还可以调用[HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose)函数配合[HMS\_AREngine\_ARPose\_GetPoseRaw](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_getposeraw)函数进行获取。详细可参考[获取设备当前位姿](arengine-c-get-pose.md#获取设备当前位姿)。
3. 调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)函数获取平面列表。详细可参考[检测环境中的平面](arengine-c-get-plane.md)章节。

   ```
   1. // 获取当前检测到的平面列表。
   2. AREngine_ARTrackableList *planeList = nullptr;
   3. // 创建一个可跟踪对象列表。
   4. HMS_AREngine_ARTrackableList_Create(arSession, &planeList);
   5. // 获取所有指定类型为ARENGINE_TRACKABLE_PLANE的可跟踪对象集合。
   6. AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;
   7. HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList);
   8. int32_t planeListSize = 0;
   9. // 获取此列表中的可跟踪对象的数量。
   10. HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize);
   11. for (int i = 0; i < planeListSize; ++i) {
   12. AREngine_ARTrackable *arTrackable = nullptr;
   13. // 从可跟踪列表中获取指定index的对象。
   14. HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable);
   15. AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane*>(arTrackable);
   16. // 获取当前可跟踪对象的跟踪状态。如果状态为：ARENGINE_TRACKING_STATE_TRACKING（可跟踪状态）才进行绘制。
   17. AREngine_ARTrackingState outTrackingState;
   18. HMS_AREngine_ARTrackable_GetTrackingState(arSession, arTrackable, &outTrackingState);
   19. AREngine_ARPlane *subsumePlane = nullptr;
   20. // 获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。
   21. HMS_AREngine_ARPlane_AcquireSubsumedBy(arSession, arPlane, &subsumePlane);
   22. if (subsumePlane != nullptr) {
   23. HMS_AREngine_ARTrackable_Release(reinterpret_cast<AREngine_ARTrackable*>(subsumePlane));
   24. // 如果当前平面有父平面，则当前平面不进行展示。否则会出现双平面。
   25. continue;
   26. }
   27. // 跟踪状态为：ARENGINE_TRACKING_STATE_TRACKING时才进行绘制。
   28. if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
   29. continue;
   30. }
   31. // 进行平面绘制。
   32. }
   33. HMS_AREngine_ARTrackableList_Destroy(planeList);
   34. planeList = nullptr;
   ```
4. 调用[HMS\_AREngine\_ARPlane\_GetPolygon](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getpolygon)函数获取平面的二维顶点坐标数组，用于绘制平面边界。

   ```
   1. // 获取检测到平面的二维顶点数组大小。
   2. int32_t polygonLength = 0;
   3. HMS_AREngine_ARPlane_GetPolygonSize(arSession, arPlane, &polygonLength);

   5. // 获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。
   6. const int32_t verticesSize = polygonLength / 2;
   7. std::vector<glm::vec2> raw_vertices(verticesSize);
   8. HMS_AREngine_ARPlane_GetPolygon(arSession, arPlane, glm::value_ptr(raw_vertices.front()), polygonLength);

   10. // 局部坐标系顶点坐标。
   11. for (int32_t i = 0; i < verticesSize; ++i) {
   12. vertices.emplace_back(raw_vertices[i].x, raw_vertices[i].y, 0.75f);
   13. }
   ```

   说明

   调用[HMS\_AREngine\_ARPlane\_GetPolygon](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getpolygon)函数获取平面的二维顶点坐标数组格式为[x1，z1，x2，z2，...]。这些值均在平面局部坐标系的x-z平面中定义，须先调用[HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose)函数获取从平面的局部坐标系到世界坐标系转换的位姿数据，然后调用[HMS\_AREngine\_ARPose\_GetMatrix](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_getmatrix)函数将位姿数据转换成4X4的矩阵，该矩阵与局部坐标系的坐标点做乘法，可以得到局部坐标系到世界坐标系的转换。
5. 将平面的二维顶点坐标转换到世界坐标系，并绘制平面。

   ```
   1. // 获取从平面的局部坐标系到世界坐标系转换的位姿信息。
   2. AREngine_ARPose *scopedArPose = nullptr;
   3. HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &scopedArPose);
   4. HMS_AREngine_ARPlane_GetCenterPose(arSession, arPlane, scopedArPose);

   6. // 将位姿数据转换成4X4的矩阵，outMatrixColMajor4x4为存放数组，其中的数据按照列优先存储。
   7. // 该矩阵与局部坐标系的坐标点做乘法，可以得到局部坐标系到世界坐标系的转换。
   8. HMS_AREngine_ARPose_GetMatrix(arSession, scopedArPose, glm::value_ptr(modelMat), 16);
   9. HMS_AREngine_ARPose_Destroy(scopedArPose);

   11. // 构筑绘制渲染平面所需的数据。
   12. // 生成三角形。
   13. for (int i = 1; i < verticesSize - 1; ++i) {
   14. triangles.push_back(0);
   15. triangles.push_back(i);
   16. triangles.push_back(i + 1);
   17. }
   18. // 生成平面包围线。
   19. for (int i = 0; i < verticesSize; ++i) {
   20. lines.push_back(i);
   21. }
   ```

### 点击屏幕

1. 用户点击屏幕后，基于点击事件获取屏幕坐标。可参考[Native XComponent](../harmonyos-references/capi-oh-nativexcomponent-native-xcomponent.md)。

   添加头文件：native\_interface\_xcomponent.h。

   ```
   1. #include <ace/xcomponent/native_interface_xcomponent.h>
   ```

   通过点击事件获取屏幕点击坐标。

   ```
   1. float pixelX= 0.0f;
   2. float pixelY= 0.0f;
   3. int32_t ret = OH_NativeXComponent_GetTouchEvent(component, window, &mTouchEvent);

   5. if (ret == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
   6. if (mTouchEvent.type == OH_NATIVEXCOMPONENT_DOWN) {
   7. pixelX= mTouchEvent.touchPoints[0].x;
   8. pixelY= mTouchEvent.touchPoints[0].y;
   9. } else {
   10. return;
   11. }
   12. }
   ```
2. 调用[HMS\_AREngine\_ARFrame\_HitTest](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_hittest)函数进行碰撞检测，结果存放在碰撞检测结果列表中。

   ```
   1. // 创建一个命中检测结果对象列表，arSession为创建AR场景步骤中创建的会话对象。
   2. AREngine_ARHitResultList *hitResultList = nullptr;
   3. HMS_AREngine_ARHitResultList_Create(arSession, &hitResultList);

   5. // 获取命中检测结果对象列表，arFrame为创建AR场景步骤中创建的帧对象，pixelX/pixelY为屏幕点坐标。
   6. HMS_AREngine_ARFrame_HitTest(arSession, arFrame, pixelX, pixelY, hitResultList);
   ```

   说明

   碰撞结果按照交点与设备的距离从近到远进行排序，存放在碰撞结果列表中。

### 放置虚拟物体

1. 调用[HMS\_AREngine\_ARHitResultList\_GetItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arhitresultlist_getitem)函数遍历碰撞检测结果列表，获取命中的可跟踪对象。

   ```
   1. // 创建命中检测结果对象。
   2. AREngine_ARHitResult *arHit = nullptr;
   3. HMS_AREngine_ARHitResult_Create(arSession, &arHit);

   5. // 获取第一个命中检测结果对象。
   6. HMS_AREngine_ARHitResultList_GetItem(arSession, hitResultList, 0, arHit);

   8. // 获取被命中的可追踪对象。
   9. AREngine_ARTrackable *arHitTrackable = nullptr;
   10. HMS_AREngine_ARHitResult_AcquireTrackable(arSession, arHit, &arHitTrackable);
   ```
2. 判断碰撞结果是否存在于平面内部。

   ```
   1. AREngine_ARTrackableType ar_trackable_type = ARENGINE_TRACKABLE_INVALID;
   2. HMS_AREngine_ARTrackable_GetType(arSession, arTrackable, &ar_trackable_type);
   3. if (ARENGINE_TRACKABLE_PLANE == ar_trackable_type) {
   4. AREngine_ARPose *arPose = nullptr;
   5. HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &arPose);
   6. HMS_AREngine_ARHitResult_GetHitPose(arSession, arHit, arPose);
   7. // 判断位姿是否位于平面的多边形范围内。0表示不在范围内，非0表示在范围内。
   8. HMS_AREngine_ARPlane_IsPoseInPolygon(arSession, arPlane, arPose, &inPolygon);
   9. HMS_AREngine_ARPose_Destroy(arPose);
   10. if (!inPolygon) {
   11. // 不在平面内，就跳过当前平面。
   12. continue;
   13. }
   14. }
   ```
3. 在碰撞结果位置创建一个新的锚点，并基于此锚点放置虚拟模型。

   ```
   1. // 在碰撞命中位置创建一个新的锚点。
   2. AREngine_ARAnchor *anchor = nullptr;
   3. HMS_AREngine_ARHitResult_AcquireNewAnchor(arSession, arHitResult, &anchor);

   5. // 判断锚点的可跟踪状态
   6. AREngine_ARTrackingState trackingState = ARENGINE_TRACKING_STATE_STOPPED;
   7. HMS_AREngine_ARAnchor_GetTrackingState(arSession, anchor, &trackingState);
   8. if (trackingState != ARENGINE_TRACKING_STATE_TRACKING) {
   9. HMS_AREngine_ARAnchor_Release(anchor);
   10. return;
   11. }
   ```
4. 绘制模型。

   调用[HMS\_AREngine\_ARAnchor\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_aranchor_getpose)函数获取锚点位姿，并基于该位姿绘制虚拟模型。

   ```
   1. // 获取锚点的位姿。
   2. AREngine_ARPose *pose = nullptr;
   3. HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &pose);
   4. HMS_AREngine_ARAnchor_GetPose(arSession, anchor, pose);
   5. // 将位姿数据转换成4X4的矩阵modelMat。
   6. HMS_AREngine_ARPose_GetMatrix(arSession, pose, glm::value_ptr(modelMat), 16);
   7. HMS_AREngine_ARPose_Destroy(pose);
   8. // 绘制虚拟模型。
   9. // 开发者可以使用OpenGL进行模型绘制，可参考示例代码：world_render_manager.cpp及world_object_renderer.cpp。
   ```
