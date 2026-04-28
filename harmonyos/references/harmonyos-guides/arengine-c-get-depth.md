---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-depth
title: 获取深度图（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 深度估计 > 获取深度图（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:55+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0000265258c95f293ec531b9cc6c4993abf46eff591a362af962063e18d0ef0d
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

获取深度估计信息能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_DEPTH](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR深度估计相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create) | 创建一个新的[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update) | 更新AR Engine的计算结果。 |
| [HMS\_AREngine\_ARSession\_Configure](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_configure) | 配置[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARFrame\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_create) | 创建一个新的[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到\*outFrame中。 |
| [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry) | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture) | 设置可用于存储相机预览流数据的OpenGL纹理。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem) | 从可跟踪列表中获取指定index的对象。 |
| [HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [HMS\_AREngine\_ARFrame\_AcquireCamera](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera) | 获取当前帧的相机参数对象。 |
| [HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create) | 分配并初始化一个新的位姿对象。 |
| [HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose) | 获取当前相机对象在AR世界空间中的位姿。 |
| [HMS\_AREngine\_ARConfig\_SetDepthMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setdepthmode) | 设置深度模式。 |
| [HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthimage16bits) | 获取当前帧的深度图像。 |
| [HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthconfidenceimage) | 获取当前帧的深度图像对应的置信度信息。 |
| [HMS\_AREngine\_ARImage\_GetNativeBuffer](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arimage_getnativebuffer) | 获取当前帧图像对象的NativeBuffer数据。 |

## 开发步骤

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

首先创建一个UI界面ARDepth.ets，用于选择是否开启深度图渲染模式。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARDepth.ets。
2. @Builder
3. export function ARDepthBuilder() {
4. ARDepth();
5. }

7. @Component
8. struct ARDepth {
9. pageInfo: NavPathStack = new NavPathStack();

11. build(): void {
12. NavDestination() {
13. Column() {
14. Button('关闭深度图渲染模式', { type: ButtonType.Normal, stateEffect: true })
15. .borderRadius(8)
16. .width('50%')
17. .height('5%')
18. .onClick(() => {
19. this.pageInfo.pushPathByName('ARDepthRender', 0); // 0表示关闭渲染
20. })

22. Button('开启深度图渲染模式', { type: ButtonType.Normal, stateEffect: true })
23. .borderRadius(8)
24. .width('50%')
25. .height('5%')
26. .onClick(() => {
27. this.pageInfo.pushPathByName('ARDepthRender', 1); // 1表示打开渲染
28. })
29. }
30. .justifyContent(FlexAlign.SpaceEvenly)
31. .width('100%')
32. .height('100%')
33. }
34. .onReady((context: NavDestinationContext) => {
35. this.pageInfo = context.pathStack;
36. })
37. .hideTitleBar(true)
38. .hideBackButton(true)
39. .hideToolBar(true)
40. }
41. }
```

最后创建一个ARDepthRender.ets，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件用于加载相机预览画面，并定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARDepthRender.ets。
2. import { deviceInfo } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import arEngineDemo from 'libentry.so';

6. @Builder
7. export function ARDepthRenderBuilder() {
8. ARDepthRender();
9. }

11. @Component
12. struct ARDepthRender {
13. pageInfo: NavPathStack = new NavPathStack();
14. private interval: number = -1;
15. private isUpdate: boolean = true;
16. private params: number = 0;
17. private xComponentId = 'ARDepth';
18. @State context: Context = this.getUIContext().getHostContext() as Context;
19. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
20. @State distance: string = '';
21. @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

23. build(): void {
24. NavDestination() {
25. RelativeContainer() {
26. XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
27. .width('100%')
28. .height('100%')
29. .alignRules({
30. center: { anchor: '__container__', align: VerticalAlign.Center },
31. middle: { anchor: '__container__', align: HorizontalAlign.Center }
32. })
33. .onLoad(() => {
34. this.interval = setInterval(() => {
35. if (this.isUpdate) {
36. // 每一帧通过调用AR Engine的Native API update来更新计算结果
37. arEngineDemo.update(this.xComponentId);
38. this.distance = arEngineDemo.getDistance(this.xComponentId);
39. }
40. }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
41. })
42. .onDestroy(() => {
43. clearInterval(this.interval);
44. })

46. Text(this.distance)
47. .fontColor(Color.Yellow)
48. .fontSize(24)
49. .textShadow({
50. radius: 10,
51. color: Color.Black,
52. offsetX: 0,
53. offsetY: 0
54. })
55. .textAlign(TextAlign.Center)
56. .alignRules({
57. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
58. middle: { anchor: '__container__', align: HorizontalAlign.Center }
59. })
60. }
61. }
62. .onAppear(() => {
63. arEngineDemo.init(this.resMgr);
64. let config: Int32Array = new Int32Array([0, this.params, 1, this.rotation]);
65. arEngineDemo.start(this.xComponentId, config);
66. })
67. .onWillDisappear(() => {
68. arEngineDemo.stop(this.xComponentId);
69. })
70. .onShown(() => {
71. this.isUpdate = true;
72. arEngineDemo.show(this.xComponentId);
73. })
74. .onHidden(() => {
75. this.isUpdate = false;
76. arEngineDemo.hide(this.xComponentId);
77. })
78. .onReady((context: NavDestinationContext) => {
79. this.pageInfo = context.pathStack;
80. this.params = context.pathInfo.param as number;
81. })
82. .hideTitleBar(true)
83. .hideBackButton(true)
84. .hideToolBar(true)
85. }

87. }
```

配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话

创建AR会话并配置为开启深度模式。

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 设置深度模式为开启状态。
8. HMS_AREngine_ARConfig_SetDepthMode(arSession, arConfig, ARENGINE_DEPTH_MODE_AUTOMATIC);
9. // 配置器设置给AR会话。
10. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### 获取当前环境中的深度图

调用[HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthimage16bits)函数，获取当前环境中的深度信息，并将结果存放在depthImage中。

```
1. AREngine_ARFrame *arFrame = nullptr;
2. // 创建AR单帧对象
3. HMS_AREngine_ARFrame_Create(arSession, &arFrame);
4. AREngine_ARImage *depthImage = nullptr;
5. // 获取深度图
6. HMS_AREngine_ARFrame_AcquireDepthImage16Bits(arSession, arFrame, &depthImage);
7. // 获取深度图的nativeBuffer
8. OH_NativeBuffer* depthBuffer;
9. HMS_AREngine_ARImage_GetNativeBuffer(arSession, depthImage, &depthBuffer);
```

### 获取当前深度图对应的深度置信度图

调用[HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthconfidenceimage)函数，获取当前深度图对应的置信度图。

```
1. AREngine_ARFrame *arFrame = nullptr;
2. // 创建AR单帧对象
3. HMS_AREngine_ARFrame_Create(arSession, &arFrame);
4. AREngine_ARImage *depthConfidenceImage = nullptr;
5. // 获取深度置信度图
6. HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(arSession, arFrame, &depthConfidenceImage);
7. // 获取深度置信图的nativeBuffer
8. OH_NativeBuffer* depthConfidenceBuffer;
9. HMS_AREngine_ARImage_GetNativeBuffer(arSession, depthConfidenceImage, &depthConfidenceBuffer);
```

### 获取深度图和深度置信度图中的值

深度图和深度置信度图包装为[AREngine\_ARImage](../harmonyos-references/arengine-capi-arengine.md#arengine_arimage)对象，可以通过此对象获取对应的深度图和深度置信度图。

```
1. AREngine_ARImageFormat format;
2. // 获取当前帧图像的数据格式
3. HMS_AREngine_ARImage_GetFormat(arSession, depthImage, &format);
4. int32_t depthWidth;
5. // 获取深度图的宽度
6. HMS_AREngine_ARImage_GetWidth(arSession, depthImage, &depthWidth);
7. int32_t depthHeight;
8. // 获取深度图的高度
9. HMS_AREngine_ARImage_GetHeight(arSession, depthImage, &depthHeight);
10. uint8_t *depthData = nullptr;
11. int32_t depthLength = 0;
12. // 获取深度图的数据
13. HMS_AREngine_ARImage_GetPlaneData(arSession, depthImage, 0, (const uint8_t **)&depthData, &depthLength);
```

### 使用完毕后，销毁深度图和深度置信度图

```
1. HMS_AREngine_ARImage_Release(depthImage);
2. HMS_AREngine_ARImage_Release(depthConfidenceImage);
```
