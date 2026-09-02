---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-lifecycle
title: UIAbility组件生命周期
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用模型 > 应用组件 > UIAbility组件 > UIAbility组件生命周期
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea38ffed6b17ce8da000a95d29af3bd801d7de9f6c771156ace665c82b280c0d
---

## 概述

当用户在执行应用启动、应用前后台切换、应用退出等操作时，系统会触发相关应用组件的生命周期回调。其中，UIAbility组件的核心生命周期回调包括[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)、[onForeground](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)、[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)、[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。作为一种包含UI的应用组件，UIAbility的生命周期不可避免地与WindowStage的生命周期（可见[窗口生命周期](window-lifecycle.md)）存在关联关系。

UIAbility的生命周期示意图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/EdGFY0zlSc2rT5rwLmmCYg/zh-cn_image_0000002736432163.png)

以下是UIAbility启动到前台和后台两种场景说明，以及生命周期回调流程讲解。

* UIAbility启动到前台，对应流程图参见上图。

  1. 当用户启动一个UIAbility时，系统会依次触发onCreate()、onWindowStageCreate()、onForeground()生命周期回调。
  2. 当用户跳转到其他应用（当前UIAbility切换到后台）时，系统会触发onBackground()生命周期回调。
  3. 当用户再次将UIAbility切换到前台时，系统会依次触发onNewWant()、onForeground()生命周期回调。
* UIAbility启动到后台，对应流程图参见下图。

  1. 当用户通过[UIAbilityContext.startAbilityByCall()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口启动一个UIAbility到后台时，系统会依次触发onCreate()、onBackground()（不会执行onWindowStageCreate()生命周期回调）生命周期回调。
  2. 当用户将UIAbility拉到前台，系统会依次触发onNewWant()、onWindowStageCreate()、onForeground()生命周期回调。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/N5Nm8QaJTkSVbKeXuiBKPQ/zh-cn_image_0000002706833008.png)

## 生命周期回调

**说明** 

* 生命周期回调是在应用主线程执行，为了确保应用性能，建议在生命周期回调中，仅执行必要的轻量级操作。对于耗时任务，推荐采用异步处理或交由子线程执行，避免阻塞主线程。
* 如果需要感知UIAbility生命周期变化，开发者可以使用[ApplicationContext.on('abilityLifecycle')](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)接口监听UIAbility生命周期变化。详见[监听UIAbility生命周期变化](application-context-stage.md#监听uiability生命周期变化)。

### onCreate()

在首次创建UIAbility实例时，系统触发[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)回调。开发者可以在该回调中执行UIAbility整个生命周期中仅发生一次的启动逻辑。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
// ···

export default class EntryAbility extends UIAbility {
  // ···
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 执行UIAbility整个生命周期中仅发生一次的业务逻辑
  }
  // ···
}
```

### onWindowStageCreate()

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例创建完成之后，在进入前台之前，系统会创建一个WindowStage。WindowStage创建完成后会进入[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)回调，开发者可以在该回调中进行UI加载、WindowStage的事件订阅。

在onWindowStageCreate()回调中通过[loadContent()](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)方法设置应用要加载的页面，并根据需要调用[on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)方法订阅WindowStage生命周期状态（[WindowStageEventType](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)）变化事件（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）。

**说明** 

* 不同开发场景下WindowStage生命周期状态（[WindowStageEventType](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)）变化事件的时序可能存在差异，具体请见[窗口生命周期](window-lifecycle.md)。
* 对于不同类型的产品，当应用主窗口从前台进入后台时，UIAbility生命周期的变化也会存在差异。详见[不同设备UIAbility生命周期的差异化行为](window-lifecycle.md#不同设备uiability生命周期的差异化行为)。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // ...

    // ...
    // 设置WindowStage的事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
    try {
      windowStage.on('windowStageEvent', (data) => {
        let stageEventType: window.WindowStageEventType = data;
        switch (stageEventType) {
          case window.WindowStageEventType.SHOWN: // 切到前台
            hilog.info(DOMAIN, 'testTag', `windowStage foreground.`);
            break;
          case window.WindowStageEventType.ACTIVE: // 获焦状态
            hilog.info(DOMAIN, 'testTag', `windowStage active.`);
            break;
          case window.WindowStageEventType.INACTIVE: // 失焦状态
            hilog.info(DOMAIN, 'testTag', `windowStage inactive.`);
            break;
          case window.WindowStageEventType.HIDDEN: // 切到后台
            hilog.info(DOMAIN, 'testTag', `windowStage background.`);
            break;
          case window.WindowStageEventType.RESUMED: // 前台可交互状态
            hilog.info(DOMAIN, 'testTag', `windowStage resumed.`);
            break;
          case window.WindowStageEventType.PAUSED: // 前台不可交互状态
            hilog.info(DOMAIN, 'testTag', `windowStage paused.`);
            break;
          default:
            break;
        }
      });
    } catch (exception) {
      hilog.error(DOMAIN, 'testTag',
        `Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
    }
    hilog.info(DOMAIN, 'testTag', `%{public}s`, `Ability onWindowStageCreate`);
    // 设置UI加载
    windowStage.loadContent('pages/Index', (err) => {
      // ...
    });
  }

  // ...
}
```

### onForeground()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)切换至前台时且UIAbility的UI可见之前，系统触发[onForeground](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)回调。开发者可以在该回调中申请系统需要的资源，或者重新申请在onBackground()中释放的资源。系统回调该方法后，UIAbility实例进入前台状态，即UIAbility实例可以与用户交互的状态。UIAbility实例会一直处于这个状态，直到被某些动作打断（例如屏幕关闭、用户跳转到其他UIAbility）。

例如，应用已获得地理位置权限。在UI显示之前，开发者可以在onForeground()回调中开启定位功能，从而获取到当前的位置信息。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
// ···

export default class EntryAbility extends UIAbility {
// ···

  onForeground(): void {
    // 申请系统需要的资源，或者重新申请在onBackground()中释放的资源
  }

// ···
}
```

### onBackground()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的UI完全不可见之后，系统触发[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)回调，将UIAbility实例切换至后台状态。开发者可以在该回调中释放UI不可见时的无用资源，例如停止定位功能，以节省系统的资源消耗。

onBackground()执行时间较短，无法提供足够的时间做一些耗时动作。请勿在该方法中执行保存用户数据或执行数据库事务等耗时操作。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
// ···

export default class EntryAbility extends UIAbility {
// ···

  onBackground(): void {
    // 释放UI不可见时无用的资源
  }

// ···
}
```

### onWindowStageWillDestroy()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例销毁之前，系统触发[onWindowStageWillDestroy()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagewilldestroy12)回调。该回调在WindowStage销毁前执行，此时WindowStage可以使用。开发者可以在该回调中释放通过WindowStage获取的资源、注销WindowStage事件订阅等。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  public windowStage: window.WindowStage | undefined = undefined;

// ···

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // 加载UI资源
    this.windowStage = windowStage;
    // ···
  }

  onWindowStageWillDestroy(windowStage: window.WindowStage): void {
    // 释放通过windowStage对象获取的资源
    // 在onWindowStageWillDestroy()中注销WindowStage事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
    try {
      if (this.windowStage) {
        this.windowStage.off('windowStageEvent');
      }
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(DOMAIN, 'testTag', `Failed to disable the listener for windowStageEvent. Code is ${code}, message is ${message}`);
    }
  }

// ···
}
```

### onWindowStageDestroy()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例销毁之前，系统触发[onWindowStageDestroy()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagedestroy)回调，开发者可以在该回调中释放UI资源。该回调在WindowStage销毁后执行，此时WindowStage不可以使用。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
// ···

export default class EntryAbility extends UIAbility {
// ···

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // 加载UI资源
    // ···
  }

// ···

  onWindowStageDestroy(): void {
    // 释放UI资源
  }
  // ···
}
```

### onDestroy()

在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例销毁之前，系统触发[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)回调。该回调是UIAbility接收到的最后一个生命周期回调，开发者可以在onDestroy()回调中进行系统资源的释放、数据的保存等操作。

例如，开发者调用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)方法通知系统停止当前UIAbility实例时，系统会触发onDestroy()回调。

**说明** 

* 从API version 13开始，用户在最近任务列表中使用一键清理来关闭应用，对于无实况窗的应用将不会触发onDestroy()回调，而是会直接终止进程；对于有实况窗的应用会继续触发onDestroy()回调。如果最近任务列表中的最后一个应用在前台运行，无论是否显示实况窗，都会触发onDestroy()回调。
* 当在开发者模式下调试某个应用时，如果用户从最近任务列表中移除了该调试应用的一个任务，则该调试应用的进程会被强制销毁，不会触发onDestroy()回调。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
// ···

export default class EntryAbility extends UIAbility {
// ···

  onDestroy(): void {
    // 系统资源的释放、数据的保存等
  }

// ···
}
```

### onNewWant()

当应用的UIAbility实例已创建，再次调用方法启动该UIAbility实例时，系统触发该UIAbility的[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调。开发者可以在该回调中更新要加载的资源和数据等，用于后续的UI展示。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
// ···

export default class EntryAbility extends UIAbility {
// ···

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 更新资源、数据
  }
}
```

## 常见问题

### onNewWant回调非预期触发导致页面变化

**问题现象**

在[Scenarios](../harmonyos-references/js-apis-app-ability-contextconstant.md#scenarios20)相关的场景下启动UIAbility时，若该UIAbility实例已存在，系统会非预期触发[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调，导致回调中传入的want参数也为非预期。若应用使用了该非预期want参数，可能引起非预期的页面变化。

**解决措施**

建议在[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期回调中调用[setOnNewWantSkipScenarios()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setonnewwantskipscenarios20)接口，通过位运算将上述三种场景的标志位组合后作为参数传入，设置在这些场景下不触发onNewWant()回调，使应用再次启动时直接切至前台。

**说明** 

* 设置setOnNewWantSkipScenarios()后，在上述三种场景下系统不会触发onNewWant()回调。
* 建议同时跳过上述三种场景。若仅跳过部分场景，则未跳过的场景仍会非预期触发onNewWant()回调。
* 该方案仅影响上述三种场景下onNewWant()回调的触发与否，不影响其他功能。设置跳过后，应用将直接切至前台，不影响正常的UI显示与用户交互。

**实现步骤**

1. 在onCreate()生命周期回调中，通过按位或运算符（|）组合三种场景的标志位。

   标志位定义在[contextConstant.Scenarios](../harmonyos-references/js-apis-app-ability-contextconstant.md#scenarios20)中：

   * SCENARIO\_MOVE\_MISSION\_TO\_FRONT（0x00000001）
   * SCENARIO\_SHOW\_ABILITY（0x00000002）
   * SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT（0x00000004）
2. 调用setOnNewWantSkipScenarios()接口，将组合后的场景值作为参数传入，设置跳过场景。

**代码示例**

```typescript
// EntryAbility.ts
import { UIAbility, Want, AbilityConstant, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 设置不触发onNewWant的场景，组合多个场景标志位
    let scenarios: number = contextConstant.Scenarios.SCENARIO_MOVE_MISSION_TO_FRONT |
      contextConstant.Scenarios.SCENARIO_SHOW_ABILITY |
      contextConstant.Scenarios.SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT;

    try {
      // 设置特定场景下启动UIAbility时不触发onNewWant生命周期回调
      this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
        console.info('setOnNewWantSkipScenarios succeed');
      }).catch((err: BusinessError) => {
        console.error('setOnNewWantSkipScenarios failed, code is ' + err.code + ', message is ' + err.message);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error('setOnNewWantSkipScenarios failed, code is ' + code + ', message is ' + message);
    }
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 在设置跳过场景后，三种场景下都不会触发此回调
    console.info('onNewWant called with want:' + JSON.stringify(want));
  }
}
```
