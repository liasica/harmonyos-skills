---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-volume-measurement
title: 高精几何重建（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 高精几何重建 > 高精几何重建（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:55+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8289ba398480a6720272a557ed58f5689172425946f08dd4af3b9fda89826122
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

高精几何重建能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AREngine高精几何重建相关接口，详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiresemanticdensedata) | 获取当前帧的高精几何重建对象数据。 |
| [HMS\_AREngine\_ARConfig\_GetSemanticDenseMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_getsemanticdensemode) | 获取已设置的高精几何重建模式。 |
| [HMS\_AREngine\_ARConfig\_SetSemanticDenseMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setsemanticdensemode) | 设置当前所需的高精几何重建模式。 |
| [HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedata) | 获取识别到的高精几何重建对象数据中的立方体数据。 |
| [HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedatasize) | 获取识别到的高精几何重建对象数据中的立方体数量。 |
| [HMS\_AREngine\_ARSemanticDense\_Release](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_release) | 释放高精几何重建对象。 |

## 开发步骤

## 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

首先创建一个UI界面ARSemanticDense.ets，用于选择高精几何重建相关模式。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARSemanticDense.ets。
2. import { display} from '@kit.ArkUI';

4. @Builder
5. export function ARSemanticDenseBuilder() {
6. ARSemanticDense();
7. }

9. @Component
10. struct ARSemanticDense {
11. pageInfo: NavPathStack = new NavPathStack();
12. @State context: Context = this.getUIContext().getHostContext() as Context;
13. @State showPage: boolean = true;
14. @State rotation: number = display.getDefaultDisplaySync().rotation;
15. @State volume: string = '';

17. build() {
18. NavDestination() {
19. Column() {
20. Button('开启稠密点云', { type: ButtonType.Normal, stateEffect: true })
21. .borderRadius(8)
22. .width('50%')
23. .height('5%')
24. .onClick(() => {
25. this.pageInfo.pushDestinationByName('ARSemanticDenseRender', 0).catch((error: BusinessError) => {
26. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
27. });
28. })

30. Button('打开体积测量', { type: ButtonType.Normal, stateEffect: true })
31. .borderRadius(8)
32. .width('50%')
33. .height('5%')
34. .onClick(() => {
35. this.pageInfo.pushDestinationByName('ARSemanticDenseRender', 1).catch((error: BusinessError) => {
36. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
37. });
38. })

40. Button('打开空间测量', { type: ButtonType.Normal, stateEffect: true })
41. .borderRadius(8)
42. .width('50%')
43. .height('5%')
44. .onClick(() => {
45. this.pageInfo.pushDestinationByName('ARSemanticDenseRender', 2).catch((error: BusinessError) => {
46. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
47. });
48. })
49. }
50. .justifyContent(FlexAlign.SpaceEvenly)
51. .width('100%')
52. .height('100%')
53. }
54. .onReady((context: NavDestinationContext) => {
55. this.pageInfo = context.pathStack;
56. })
57. .hideTitleBar(true)
58. .hideBackButton(true)
59. .hideToolBar(true)
60. }
61. }
```

最后创建一个ARSemanticDenseRender.ets，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件用于加载相机预览画面，并定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARSemanticDenseRender.ets。
2. import { display } from '@kit.ArkUI';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import arEngineDemo from 'libentry.so';

6. @Builder
7. export function ARSemanticDenseRenderBuilder() {
8. ARSemanticDenseRender();
9. }

11. @Component
12. struct ARSemanticDenseRender {
13. pageInfo: NavPathStack = new NavPathStack();
14. @State context: Context = this.getUIContext().getHostContext() as Context;
15. private xComponentId: string = 'ARSemanticDense';
16. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
17. private interval: number = -1;
18. private inputInterval: number = -1;
19. private getCubeInfoInterval: number = -1;
20. private isUpdate: boolean = false;
21. private semanticDenseMode: number = 0;
22. @State showPage: boolean = true;
23. @State rotation: number = display.getDefaultDisplaySync().rotation;
24. @State volume: string = '';

26. build(): void {
27. NavDestination() {
28. RelativeContainer() {

30. XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
31. .opacity(0.2)
32. .width('100%')
33. .height('100%')
34. .zIndex(0.1)
35. .visibility(this.showPage ? Visibility.Visible : Visibility.None)
36. .alignRules({
37. center: { anchor: '__container__', align: VerticalAlign.Center },
38. middle: { anchor: '__container__', align: HorizontalAlign.Center }
39. })
40. .onLoad(() => {
41. this.interval = setInterval(() => {
42. if (this.isUpdate) {
43. arEngineDemo.update(this.xComponentId);
44. if (this.semanticDenseMode != 0) {
45. this.volume = arEngineDemo.getVolume(this.xComponentId);
46. }
47. }
48. }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
49. })
50. .onDestroy(() => {
51. if (this.interval !== -1) {
52. clearInterval(this.interval);
53. this.interval = -1;
54. }

56. if (this.inputInterval !== -1) {
57. clearInterval(this.inputInterval);
58. this.inputInterval = -1;
59. }

61. if (this.getCubeInfoInterval !== -1) {
62. clearInterval(this.getCubeInfoInterval);
63. this.getCubeInfoInterval = -1;
64. }
65. })

67. Text(this.volume)
68. .fontColor(Color.Red)
69. .fontSize(14)
70. .textAlign(TextAlign.Center)
71. .alignRules({
72. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
73. middle: { anchor: '__container__', align: HorizontalAlign.Center }
74. })
75. }
76. }
77. .onAppear(() => {
78. arEngineDemo.init(this.resMgr);
79. let config: Int32Array = new Int32Array([1,this.rotation, 2, this.semanticDenseMode]);
80. arEngineDemo.start(this.xComponentId, config);
81. })
82. .onWillDisappear(async () => {
83. arEngineDemo.stop(this.xComponentId);
84. })
85. .onShown(() => {
86. this.isUpdate = true;
87. arEngineDemo.show(this.xComponentId);
88. })
89. .onHidden(() => {
90. this.isUpdate = false;
91. arEngineDemo.hide(this.xComponentId);
92. })
93. .onReady((context: NavDestinationContext) => {
94. this.pageInfo = context.pathStack;
95. this.semanticDenseMode = context.pathInfo.param as number;
96. })
97. .hideTitleBar(true)
98. .hideBackButton(true)
99. .hideToolBar(true)
100. }
101. }
```

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话并配置高精几何重建相关模式

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 配置高精几何重建模式中的体积识别模式。
8. HMS_AREngine_ARConfig_SetSemanticDenseMode(arSession, arConfig, ARENGINE_SEMANTIC_DENSE_MODE_CUBE_VOLUME);
9. // 配置器设置给AR会话。
10. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### 获取当前环境中的高精几何重建信息

创建一个帧对象，调用[HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiresemanticdensedata)函数，从当前帧中获取环境中的高精几何重建信息，其中包含了环境中的稠密点云信息和立方体信息。

```
1. AREngine_ARFrame *arFrame = nullptr;
2. // 创建AR单帧对象
3. HMS_AREngine_ARFrame_Create(arSession, &arFrame);
4. AREngine_ARSemanticDenseData *arSemanticDense = nullptr;
5. // 获取当前帧的稠密点云信息
6. HMS_AREngine_ARFrame_AcquireSemanticDenseData(arSession, arFrame, &arSemanticDense);
```

### 获取高精几何重建信息中的立方体数据

1. 调用[HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedata)函数，获取当前环境中的立方体数据，立方体的数据结构详情参考[AREngine\_ARSemanticDenseCubeData](../harmonyos-references/arengine-struct-arsemanticdensecubedata.md)。

   ```
   1. AREngine_ARSemanticDenseCubeData *semanticDenseCubeData = nullptr;
   2. HMS_AREngine_ARSemanticDense_AcquireCubeData(arSession, arSemanticDense, &semanticDenseCubeData);
   ```
2. 调用[HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedatasize)函数，获取当前环境中的立方体数量，如果立方体数量大于0，即可从中获取单个立方体的数据进行绘制和体积计算。

   ```
   1. int64_t cubeDataSize = 0;
   2. HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(arSession, arSemanticDense, &cubeDataSize);
   ```

### 绘制相关几何信息

1. 通过获取到的[AREngine\_ARSemanticDenseCubeData](../harmonyos-references/arengine-struct-arsemanticdensecubedata.md)对象来绘制立方体。

   ```
   1. // 判断获取的立方体数据及数量。
   2. if (semanticDenseCubeData != nullptr && cubeDataSize > 0) {
   3. // 绘制立方体。
   4. mCubeRenderer.Draw(projectionMat, viewMat, arSession, semanticDenseCubeData);
   5. }
   ```
