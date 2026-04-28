---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arsession
title: 管理AR会话（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 管理AR会话 > 管理AR会话（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:48+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0f52bbde1a2ca495c5d00e91bef0063401eb9a89c87ab0db62088294f374fb53
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，管理AR会话支持部分Phone、部分Tablet设备。并且从6.1.0(23)版本开始，新增支持TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持。

## 接口说明

AR会话主要依赖[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，以下接口为AR会话相关接口。详细接口和说明，请参考[arViewController（AR场景管理能力）](../harmonyos-references/arengine-api-arviewcontroller.md)。

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

## 开发步骤

对于使用ArkTS的任何AR应用，从6.1.0(23)开始，AREngine对于任何AR特性，都可以通过[arViewController.isARTypeSupported](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口来查询当前设备是否支持该特性，当判断该设备支持特性后，进行之后的开发工作。

首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。

### 导入模块

导入AR Engine相关模块，导入方法如下。

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node, Scene } from '@kit.ArkGraphics3D';
3. import { BusinessError } from '@kit.BasicServicesKit';
```

### 初始化AR会话和AR场景

通过[ARViewContext.init](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextinit)方法初始化一个AR会话及场景。

在此之前请确保已获取相机权限，否则将不会加载AR场景，具体指导请参考[前置准备](arengine-preparations.md#前置准备)或者[申请权限](arengine-preparations.md#申请权限)。

AR会话及场景创建好后使用[组件导航（Navigation）](arkts-navigation-navigation.md)组件及[ARView](../harmonyos-references/arengine-api-component-arview.md#arview)组件在设备上显示AR场景，关于[组件导航（Navigation）](arkts-navigation-navigation.md)具体指导可参考[前置准备](arengine-preparations.md#前置准备)。

```
1. @Builder
2. export function ARWorldBuilder(): void {
3. ARWorld();
4. }

6. @Component
7. struct ARWorld {
8. @State arContext?: arViewController.ARViewContext = undefined;

10. // 创建UI窗口，显示AR场景
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
22. }
23. }
24. }
25. .onAppear(() => {
26. this.initARView();
27. })
28. .onWillDisappear(() => {
29. this.stopARView();
30. })
31. .onShown(() => {
32. this.resumeARView();
33. })
34. .onHidden(() => {
35. this.pauseARView();
36. })
37. .hideTitleBar(true)
38. .hideBackButton(true)
39. .hideToolBar(true)
40. }

42. private initARView(): void {
43. Scene.load().then((scene: Scene) => {
44. let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
45. viewContext.scene = scene;
46. viewContext.callback = new ARViewCallbackImpl();  // 通过回调实现业务场景
47. viewContext.config = {
48. type: arEngine.ARType.WORLD,
49. planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
50. powerMode: arEngine.ARPowerMode.NORMAL,
51. semanticMode: arEngine.ARSemanticMode.NONE,
52. poseMode: arEngine.ARPoseMode.GRAVITY,
53. depthMode: arEngine.ARDepthMode.AUTOMATIC,
54. meshMode: arEngine.ARMeshMode.DISABLED,
55. focusMode: arEngine.ARFocusMode.AUTO
56. }
57. viewContext.init().then(() => {
58. this.arContext = viewContext;
59. console.info('Succeeded in initializing ARView.');
60. }).catch((err: BusinessError) => {
61. console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
62. })
63. })
64. }
65. }
```

### 使用AR会话对象处理业务

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法获取AR会话对象，之后可根据开发者所需的具体业务编写处理逻辑。

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

15. let arSession: arEngine.ARSession = ctx.session; // 获取AR会话

17. try {
18. // 示例为一个帧对象的获取与销毁
19. let frame: arEngine.ARFrame = arSession.getFrame();
20. await frame.release();

22. } catch (error) {
23. const err: BusinessError = error as BusinessError;
24. console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
25. }
26. }
27. }
```

### 暂停AR会话

要暂停AR会话，开发者可以使用[ARViewContext.pause](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextpause)方法，在应用置为后台时可以暂停AR会话和暂停AR场景。

```
1. private pauseARView(): void {
2. if (!this.arContext) {
3. return;
4. }
5. try {
6. this.arContext.pause();
7. } catch (error) {
8. const err: BusinessError = error as BusinessError;
9. console.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}.`);
10. }
11. }
```

### 恢复AR会话

要恢复暂停的AR会话和AR场景，开发者可以使用[ARViewContext.resume](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextresume)方法。

```
1. private resumeARView(): void {
2. if (!this.arContext) {
3. return;
4. }
5. try {
6. this.arContext.resume();
7. } catch (error) {
8. const err: BusinessError = error as BusinessError;
9. console.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}.`);
10. }
11. }
```

### 销毁AR会话

退出AR会话和AR场景时，开发者可以使用[ARViewContext.destroy](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextdestroy)方法同时销毁AR会话及AR场景。

```
1. private stopARView(): void {
2. if (!this.arContext) {
3. return;
4. }
5. try {
6. this.arContext.destroy();
7. } catch (error) {
8. const err: BusinessError = error as BusinessError;
9. console.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
10. }
11. }
```

说明

组件生命周期的方法，除[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)、[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)、[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)、[onPageHide](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)外，还可以使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)的[页面生命周期](arkts-navigation-navigation.md#页面生命周期)所示方法，开发者可根据需要进行选择。
