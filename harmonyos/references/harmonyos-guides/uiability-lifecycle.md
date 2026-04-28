---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-lifecycle
title: UIAbility组件生命周期
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > UIAbility组件 > UIAbility组件生命周期
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0b7ebea1eba8bcc51076dfedf560397adbfa3ed6de0ca4d5f1f1c82fbede38e7
---

## 概述

当用户在执行应用启动、应用前后台切换、应用退出等操作时，系统会触发相关应用组件的生命周期回调。其中，UIAbility组件的核心生命周期回调包括[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)、[onForeground](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)、[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)、[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。作为一种包含UI的应用组件，UIAbility的生命周期不可避免地与[WindowStage](application-window-stage.md)的生命周期存在关联关系。

UIAbility的生命周期示意图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/i5PQJl2ySa2LZa04cZGlOQ/zh-cn_image_0000002552957488.png?HW-CC-KV=V1&HW-CC-Date=20260427T233739Z&HW-CC-Expire=86400&HW-CC-Sign=123825A21E867160528956B86A3D97E85A54E71B55298F026F3B72BFDF84CA12)

以下是UIAbility启动到前台和后台两种场景说明，以及生命周期回调流程讲解。

* UIAbility启动到前台，对应流程图参见上图。

  1. 当用户启动一个UIAbility时，系统会依次触发onCreate()、onWindowStageCreate()、onForeground()生命周期回调。
  2. 当用户跳转到其他应用（当前UIAbility切换到后台）时，系统会触发onBackground()生命周期回调。
  3. 当用户再次将UIAbility切换到前台时，系统会依次触发onNewWant()、onForeground()生命周期回调。
* UIAbility启动到后台，对应流程图参见下图。

  1. 当用户通过[UIAbilityContext.startAbilityByCall()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口启动一个UIAbility到后台时，系统会依次触发onCreate()、onBackground()（不会执行onWindowStageCreate()生命周期回调）生命周期回调。
  2. 当用户将UIAbility拉到前台，系统会依次触发onNewWant()、onWindowStageCreate()、onForeground()生命周期回调。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/yUa1-xF1QJyCoLbcImws3w/zh-cn_image_0000002583477489.png?HW-CC-KV=V1&HW-CC-Date=20260427T233739Z&HW-CC-Expire=86400&HW-CC-Sign=A47CEB8E2EE44870C6AA7AB6D0C0AD14555BEB240C401AA445BC83D6AE6732E6)

## 生命周期回调

说明

* 生命周期回调是在应用主线程执行，为了确保应用性能，建议在生命周期回调中，仅执行必要的轻量级操作。对于耗时任务，推荐采用异步处理或交由子线程执行，避免阻塞主线程。
* 如果需要感知UIAbility生命周期变化，开发者可以使用[ApplicationContext注册接口](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)监听UIAbility生命周期变化。详见[监听UIAbility生命周期变化](application-context-stage.md#监听uiability生命周期变化)。

### onCreate()

在首次创建UIAbility实例时，系统触发[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)回调。开发者可以在该回调中执行UIAbility整个生命周期中仅发生一次的启动逻辑。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. // ···

4. export default class EntryAbility extends UIAbility {
5. // ···
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. // 执行UIAbility整个生命周期中仅发生一次的业务逻辑
8. }
9. // ···
10. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L16-L181)

### onWindowStageCreate()

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例创建完成之后，在进入前台之前，系统会创建一个[WindowStage](application-window-stage.md)。WindowStage创建完成后会进入[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)回调，开发者可以在该回调中进行UI加载、WindowStage的事件订阅。

在onWindowStageCreate()回调中通过[loadContent()](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)方法设置应用要加载的页面，并根据需要调用[on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)方法订阅[WindowStage的事件](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）。

说明

* 不同开发场景下[WindowStage事件](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)的时序可能存在差异，WindowStage的相关使用请参见[窗口开发指导](application-window-stage.md)。
* 对于不同类型的产品，当应用主窗口从前台进入后台时，UIAbility生命周期的变化也会存在差异。详见[不同设备生命周期的差异化行为](window-overview.md#不同设备生命周期的差异化行为)。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. // ···

6. const DOMAIN = 0x0000;

8. export default class EntryAbility extends UIAbility {

10. // ···

12. onWindowStageCreate(windowStage: window.WindowStage): void {
13. // ···
14. // 设置WindowStage的事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
15. try {
16. windowStage.on('windowStageEvent', (data) => {
17. let stageEventType: window.WindowStageEventType = data;
18. switch (stageEventType) {
19. case window.WindowStageEventType.SHOWN: // 切到前台
20. hilog.info(DOMAIN, 'testTag', `windowStage foreground.`);
21. break;
22. case window.WindowStageEventType.ACTIVE: // 获焦状态
23. hilog.info(DOMAIN, 'testTag', `windowStage active.`);
24. break;
25. case window.WindowStageEventType.INACTIVE: // 失焦状态
26. hilog.info(DOMAIN, 'testTag', `windowStage inactive.`);
27. break;
28. case window.WindowStageEventType.HIDDEN: // 切到后台
29. hilog.info(DOMAIN, 'testTag', `windowStage background.`);
30. break;
31. case window.WindowStageEventType.RESUMED: // 前台可交互状态
32. hilog.info(DOMAIN, 'testTag', `windowStage resumed.`);
33. break;
34. case window.WindowStageEventType.PAUSED: // 前台不可交互状态
35. hilog.info(DOMAIN, 'testTag', `windowStage paused.`);
36. break;
37. default:
38. break;
39. }
40. });
41. } catch (exception) {
42. hilog.error(DOMAIN, 'testTag',
43. `Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
44. }
45. hilog.info(DOMAIN, 'testTag', `%{public}s`, `Ability onWindowStageCreate`);
46. // 设置UI加载
47. windowStage.loadContent('pages/Index', (err) => {
48. // ···
49. });
50. }

52. // ···
53. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L17-L180)

### onForeground()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)切换至前台时且UIAbility的UI可见之前，系统触发[onForeground](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)回调。开发者可以在该回调中申请系统需要的资源，或者重新申请在onBackground()中释放的资源。系统回调该方法后，UIAbility实例进入前台状态，即UIAbility实例可以与用户交互的状态。UIAbility实例会一直处于这个状态，直到被某些动作打断（例如屏幕关闭、用户跳转到其他UIAbility）。

例如，应用已获得地理位置权限。在UI显示之前，开发者可以在onForeground()回调中开启定位功能，从而获取到当前的位置信息。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. // ···

4. export default class EntryAbility extends UIAbility {
5. // ···

7. onForeground(): void {
8. // 申请系统需要的资源，或者重新申请在onBackground()中释放的资源
9. }

11. // ···
12. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L18-L179)

### onBackground()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的UI完全不可见之后，系统触发[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)回调，将UIAbility实例切换至后台状态。开发者可以在该回调中释放UI不可见时的无用资源，例如停止定位功能，以节省系统的资源消耗。

onBackground()执行时间较短，无法提供足够的时间做一些耗时动作。请勿在该方法中执行保存用户数据或执行数据库事务等耗时操作。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. // ···

4. export default class EntryAbility extends UIAbility {
5. // ···

7. onBackground(): void {
8. // 释放UI不可见时无用的资源
9. }

11. // ···
12. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L19-L178)

### onWindowStageWillDestroy()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例销毁之前，系统触发[onWindowStageWillDestroy()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagewilldestroy12)回调。该回调在WindowStage销毁前执行，此时WindowStage可以使用。开发者可以在该回调中释放通过WindowStage获取的资源、注销WindowStage事件订阅等。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. const DOMAIN = 0x0000;

8. export default class EntryAbility extends UIAbility {
9. public windowStage: window.WindowStage | undefined = undefined;

11. // ···

13. onWindowStageCreate(windowStage: window.WindowStage): void {
14. // 加载UI资源
15. this.windowStage = windowStage;
16. // ···
17. }

19. onWindowStageWillDestroy(windowStage: window.WindowStage): void {
20. // 释放通过windowStage对象获取的资源
21. // 在onWindowStageWillDestroy()中注销WindowStage事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
22. try {
23. if (this.windowStage) {
24. this.windowStage.off('windowStageEvent');
25. }
26. } catch (err) {
27. let code = (err as BusinessError).code;
28. let message = (err as BusinessError).message;
29. hilog.error(DOMAIN, 'testTag', `Failed to disable the listener for windowStageEvent. Code is ${code}, message is ${message}`);
30. }
31. }

33. // ···
34. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L20-L177)

### onWindowStageDestroy()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例销毁之前，系统触发[onWindowStageDestroy()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagedestroy)回调，开发者可以在该回调中释放UI资源。该回调在WindowStage销毁后执行，此时WindowStage不可以使用。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. // ···

5. export default class EntryAbility extends UIAbility {
6. // ···

8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. // 加载UI资源
10. // ···
11. }

13. // ···

15. onWindowStageDestroy(): void {
16. // 释放UI资源
17. }
18. // ···
19. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L21-L176)

### onDestroy()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例销毁之前，系统触发[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)回调。该回调是UIAbility接收到的最后一个生命周期回调，开发者可以在onDestroy()回调中进行系统资源的释放、数据的保存等操作。

例如，开发者调用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)方法通知系统停止当前UIAbility实例时，系统会触发onDestroy()回调。

说明

* 从API version 13开始，用户在最近任务列表中使用一键清理来关闭应用，对于无实况窗的应用将不会触发onDestroy()回调，而是会直接终止进程；对于有实况窗的应用会继续触发onDestroy()回调。
* 当在开发者模式下调试某个应用时，如果用户从最近任务列表中移除了该调试应用的一个任务，则该调试应用的进程会被强制销毁，不会触发onDestroy()回调。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. // ···

4. export default class EntryAbility extends UIAbility {
5. // ···

7. onDestroy(): void {
8. // 系统资源的释放、数据的保存等
9. }

11. // ···
12. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L22-L175)

### onNewWant()

当应用的UIAbility实例已创建，再次调用方法启动该UIAbility实例时，系统触发该UIAbility的[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调。开发者可以在该回调中更新要加载的资源和数据等，用于后续的UI展示。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. // ···

4. export default class EntryAbility extends UIAbility {
5. // ···

7. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. // 更新资源、数据
9. }
10. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLifecycle/entry/src/main/ets/entryability/EntryAbility.ets#L23-L174)
