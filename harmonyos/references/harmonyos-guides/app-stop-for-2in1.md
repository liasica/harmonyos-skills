---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-stop-for-2in1
title: 应用退出（PC/2in1）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用生命周期 > 应用退出（PC/2in1）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ca04b2b977659e704ac523a99fa8069cf8c935eec39d6fc5e1610eb4ebae8c94
---

## 概述

在PC/2in1设备上，由于设备形态和交互方式更加丰富，应用或窗口的退出场景也更加多样。开发者需要了解不同退出场景下的行为差异，并据此处理资源释放、数据保存等逻辑，确保应用能够正常退出。

PC/2in1设备上常见的应用退出场景主要包括：

* **关闭按钮退出**：用户点击主窗口三键区中的关闭按钮，关闭当前应用窗口。这是最常见的窗口退出方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/RWsYt1wuSx2UkkaDJUtwOQ/zh-cn_image_0000002736432183.png)
* **快捷栏退出**：用户在快捷栏右键点击应用图标，并选择“退出”或“关闭所有窗口”，触发应用级别的关闭流程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/wG-yjfhhTsGSlETw4yYqLA/zh-cn_image_0000002706833028.png)
* **托盘退出**：用户在系统托盘区域右键点击应用图标，并选择“退出”，触发应用级别的关闭流程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/okdkmE_6R5iGdwHWrOWf9w/zh-cn_image_0000002736312137.png)
* **关机退出**：用户执行系统关机、重启等操作时，系统会依次关闭所有应用，并触发应用退出流程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/CT2tmDVsSSGtwe96TAyHvQ/zh-cn_image_0000002706673094.png)

不同退出场景触发的回调机制存在差异。开发者可根据应用需求选择合适的监听方式。本文将介绍单主窗退出、应用进程退出以及预关闭机制，帮助开发者了解PC/2in1设备上的应用退出开发方式。关于应用退出流程的通用机制，请参见[应用退出流程](app-stop.md#应用退出流程)。

## 单主窗退出

对于单个主窗口，当用户通过关闭按钮关闭窗口时，UIAbility实例和WindowStage会按照特定的生命周期顺序依次变化。理解这一流程有助于开发者在正确的时机执行资源释放、数据保存等操作。

**生命周期变化**

当用户点击窗口关闭按钮时，UIAbility从运行状态进入销毁状态，触发的生命周期回调顺序为：**onBackground() -> onDestroy()**。（其中onForeground()已在应用启动时回调，此处不再重复触发。）

对应的WindowStage生命周期状态变化顺序为：**获焦（ACTIVE） -> 失焦（INACTIVE） -> 隐藏（HIDDEN）**。

具体流程如下：

1. UIAbility处于前台运行状态（onForeground已回调），WindowStage处于获焦状态（ACTIVE）。
2. 用户点击关闭按钮，系统首先将WindowStage切换为失焦状态（INACTIVE），UIAbility仍在前台。
3. 随后，WindowStage切换为隐藏状态（HIDDEN），UIAbility进入后台状态，系统回调onBackground()。
4. 最后，系统销毁UIAbility实例，依次回调onWindowStageWillDestroy()、onWindowStageDestroy()、onDestroy()。

**说明** 

在PC/2in1设备上，当应用窗口由可见变为不可见（如点击最小化按钮）时，系统并不会驱动UIAbility进入后台状态。这一生命周期行为与Phone设备存在本质差异，详见[不同设备UIAbility生命周期的差异化行为](window-lifecycle.md#不同设备uiability生命周期的差异化行为)。

以下示例展示了如何监听WindowStage生命周期状态变化，以及如何在UIAbility生命周期回调中处理退出逻辑：

```ts
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  windowStage: window.WindowStage | undefined = undefined;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, TAG, 'onCreate');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(DOMAIN, TAG, 'onWindowStageCreate');
    this.windowStage = windowStage;

    try {
      windowStage.on('windowStageEvent', (data) => {
        let stageEventType: window.WindowStageEventType = data;
        switch (stageEventType) {
          case window.WindowStageEventType.ACTIVE:
            hilog.info(DOMAIN, TAG, 'WindowStage active.');
            break;
          case window.WindowStageEventType.INACTIVE:
            hilog.info(DOMAIN, TAG, 'WindowStage inactive.');
            break;
          case window.WindowStageEventType.HIDDEN:
            hilog.info(DOMAIN, TAG, 'WindowStage hidden.');
            break;
          default:
            break;
        }
      });
    } catch (exception) {
      hilog.error(DOMAIN, TAG,
        `Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
    }

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, TAG, `Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      hilog.info(DOMAIN, TAG, 'Succeeded in loading the content.');
    });
  }

  onForeground(): void {
    hilog.info(DOMAIN, TAG, 'onForeground');
  }

  onBackground(): void {
    hilog.info(DOMAIN, TAG, 'onBackground');
  }

  onWindowStageWillDestroy(windowStage: window.WindowStage): void {
    try {
      if (this.windowStage) {
        this.windowStage.off('windowStageEvent');
      }
    } catch (exception) {
      hilog.error(DOMAIN, TAG,
        `Failed to disable the listener for windowStageEvent. Cause: ${JSON.stringify(exception)}`);
    }
    hilog.info(DOMAIN, TAG, 'onWindowStageWillDestroy');
  }

  onWindowStageDestroy(): void {
    hilog.info(DOMAIN, TAG, 'onWindowStageDestroy');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, TAG, 'onDestroy');
  }
}
```

**说明** 

* on('windowStageEvent')接口无法保证生命周期状态切换间的顺序，对于关注状态间切换顺序的场景，建议从API版本20开始使用[on('windowStageLifecycleEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstagelifecycleevent20)接口。
* 对于WindowStage获焦/失焦状态，推荐使用[on('windowEvent')](../harmonyos-references/arkts-apis-window-window.md#onwindowevent10)进行监听。

## 应用进程退出

**单窗口应用的进程退出**

对于仅包含一个窗口的应用，当该窗口关闭后，对应的UIAbility实例会被销毁，随后AbilityStage销毁，应用进程退出。这是最简单的进程退出场景。

**多窗口应用的进程退出**

对于包含多个窗口的应用，不同窗口通常对应不同的UIAbility实例。当其中一个窗口关闭时，仅该窗口对应的UIAbility实例会被销毁，应用进程不会退出。只有当应用的所有窗口均被关闭，所有UIAbility实例及其对应的AbilityStage均被销毁后，应用进程才会退出。

**批量退出场景**

除关闭单个窗口外，PC/2in1设备还支持批量退出应用的场景。此类场景会依次关闭应用的所有窗口，并在窗口关闭完成后退出应用进程。

* **关机退出**：用户执行系统关机、重启操作时，系统会依次关闭所有应用的窗口，触发各UIAbility的退出流程，最终所有应用进程退出。
* **托盘退出**：用户在系统托盘区域右键点击应用图标选择退出时，系统会依次关闭该应用的所有窗口，窗口关闭完成后进程退出。
* **快捷栏右键退出**：用户在快捷栏上右键点击应用图标选择退出或关闭所有窗口时，系统会依次关闭该应用的所有窗口，窗口关闭完成后进程退出。

在批量退出场景中，系统会逐一关闭每个窗口，每个窗口的退出流程与单窗口退出流程一致，开发者无需做额外处理，只需确保在UIAbility的onDestroy()回调中正确释放资源即可。

## 预关闭机制

预关闭是指在应用窗口或应用关闭前，系统为应用提供一次拦截关闭流程的机会。应用可在该阶段执行必要的确认或处理逻辑。例如，文档编辑类应用在用户关闭窗口时，可以弹出提示框，提示用户存在未保存的文档，并由用户选择保存、放弃更改或取消关闭。该机制可用于降低误操作导致数据丢失的风险。

针对PC/2in1设备，系统提供了多个层次的预关闭接口，开发者可以根据实际场景选择合适的接口：

| 接口 | 作用层级 | 触发方式 | 同步/异步 | API版本 |
| --- | --- | --- | --- | --- |
| [on('windowStageClose')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageclose14) | 窗口 | 点击主窗口三键区关闭按钮 | 同步 | 14+ |
| [on('windowWillClose')](../harmonyos-references/arkts-apis-window-window.md#onwindowwillclose15) | 窗口 | 点击主窗口三键区关闭按钮 | 异步 | 15+ |
| [onPrepareToTerminate](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminate10) | UIAbility | 关闭按钮、快捷栏/托盘退出 | 同步 | 10+ |
| [onPrepareToTerminateAsync](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminateasync15) | UIAbility | 关闭按钮、快捷栏/托盘退出 | 异步 | 15+ |
| [onPrepareTermination](../harmonyos-references/js-apis-app-ability-abilitystage.md#onpreparetermination15) | AbilityStage | 快捷栏/托盘退出、关机 | 同步 | 15+ |
| [onPrepareTerminationAsync](../harmonyos-references/js-apis-app-ability-abilitystage.md#onprepareterminationasync15) | AbilityStage | 快捷栏/托盘退出、关机 | 异步 | 15+ |

**说明** 

onPrepareToTerminate、onPrepareToTerminateAsync、onPrepareTermination、onPrepareTerminationAsync需要申请ohos.permission.PREPARE\_APP\_TERMINATE权限。

### 单个窗口的预关闭

当用户通过关闭按钮关闭单个窗口时，应用可以通过监听窗口关闭事件来拦截关闭流程。根据业务需求，可以选择同步或异步的监听方式。

**同步监听Window的关闭：on('windowStageClose')**

通过[windowStage.on('windowStageClose')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageclose14)监听主窗口三键区的关闭按钮事件。

```ts
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.on('windowStageClose', () => {
      // 检查是否有未保存的数据
      if (this.hasUnsavedData()) {
        // 弹框提示用户保存
        this.showSaveDialog();
        return true; // 返回true，阻止关闭
      }
      return false; // 返回false，允许关闭
    });
    windowStage.loadContent('pages/Index');
  }

  private hasUnsavedData(): boolean {
    // 检查是否有未保存数据的逻辑
    return true;
  }

  private showSaveDialog(): void {
    // 弹框提示用户保存的逻辑
  }
}
```

**异步监听Window的退出：on('windowWillClose')**

通过[window.on('windowWillClose')](../harmonyos-references/arkts-apis-window-window.md#onwindowwillclose15)监听主窗口或子窗口的关闭事件。回调函数异步执行，适用于需要执行异步操作（如弹框等待用户确认）的场景。

```ts
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let mainWindow = windowStage.getMainWindowSync();
    mainWindow.on('windowWillClose', () => {
      return new Promise<boolean>((resolve) => {
        if (this.hasUnsavedData()) {
          // 弹框询问用户是否保存
          this.showSaveConfirmDialog((shouldClose: boolean) => {
            if (shouldClose) {
              this.saveData(); // 保存数据
              resolve(false); // 允许关闭
            } else {
              resolve(true); // 取消关闭
            }
          });
        } else {
          resolve(false); // 无未保存数据，允许关闭
        }
      });
    });
    windowStage.loadContent('pages/Index');
  }

  private hasUnsavedData(): boolean {
    return true;
  }

  private saveData(): void {
  }

  private showSaveConfirmDialog(callback: (shouldClose: boolean) => void): void {
    // 弹框提示用户，通过callback返回用户选择
    // 示例：用户选择"保存并关闭"时 callback(true)
    // 用户选择"取消"时 callback(false)
    callback(true);
  }
}
```

**UIAbility级别的预关闭**

除了监听窗口的关闭事件，还可以通过[onPrepareToTerminate()](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminate10)生命周期回调来感知UIAbility的退出，并在其正式关闭前执行必要的预关闭操作。

```ts
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onPrepareToTerminate(): boolean {
    // 拉起一个确认弹框的Ability
    let want: Want = {
      bundleName: 'com.example.myapplication',
      moduleName: 'entry',
      abilityName: 'SaveConfirmAbility'
    };
    this.context.startAbilityForResult(want)
      .then((result) => {
        if (result && result.resultCode === 0) {
          this.context.terminateSelf(); // 用户确认，关闭当前UIAbility
        }
      }).catch((err: BusinessError) => {
        this.context.terminateSelf(); // 异常时也关闭
      });
    return true; // 返回true，取消本次关闭，等待异步结果后再主动关闭
  }
}
```

可使用[onPrepareToTerminateAsync()](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminateasync15)异步响应预关闭：

```ts
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  async onPrepareToTerminateAsync(): Promise<boolean> {
    // 异步执行预关闭操作，如等待用户确认
    let shouldClose = await this.waitForUserConfirm();
    return !shouldClose; // 返回true取消关闭，返回false允许关闭
  }

  private waitForUserConfirm(): Promise<boolean> {
    return new Promise((resolve) => {
      // 弹框等待用户确认
      resolve(true); // 用户确认关闭
    });
  }
}
```

**说明** 

当用户通过关闭按钮关闭单个窗口时，应用可以监听窗口退出或UIAbility预关闭来拦截管理流程。系统回调遵循以下优先级：优先回调窗口的on('windowWillClose')，如果应用未注册该回调，则回调窗口的on('windowStageClose')；若以上两者应用都未注册，系统将回调UIAbility的onPrepareToTerminateAsync或onPrepareToTerminate，其中异步回调会优先执行。

### 应用级预关闭

当用户通过快捷栏右键退出、托盘退出或关机等操作触发应用整体退出时，系统会依次关闭应用的所有窗口。此时需要使用AbilityStage级别的预关闭接口来拦截整个应用的退出流程。

**AbilityStage级别的预关闭**

通过[AbilityStage.onPrepareTermination()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onpreparetermination15)在应用被用户关闭时执行预关闭操作。该回调仅在应用正常退出（如通过快捷栏/托盘关闭应用、应用随设备关机退出）时触发，应用被强制关闭时不会触发。

```ts
import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onPrepareTermination(): AbilityConstant.PrepareTermination {
    // 检查是否有未保存的数据
    if (this.hasUnsavedData()) {
      // 弹框提示用户保存
      this.showSaveDialog();
      return AbilityConstant.PrepareTermination.CANCEL; // 取消关闭
    }
    return AbilityConstant.PrepareTermination.TERMINATE_IMMEDIATELY; // 立即关闭
  }

  private hasUnsavedData(): boolean {
    return true;
  }

  private showSaveDialog(): void {
    // 弹框提示用户保存的逻辑
  }
}
```

可使用[onPrepareTerminationAsync()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onprepareterminationasync15)异步响应预关闭：

```ts
import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  async onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination> {
    let shouldClose = await this.waitForUserConfirm();
    if (shouldClose) {
      return AbilityConstant.PrepareTermination.TERMINATE_IMMEDIATELY;
    }
    return AbilityConstant.PrepareTermination.CANCEL;
  }

  private waitForUserConfirm(): Promise<boolean> {
    return new Promise((resolve) => {
      // 弹框等待用户确认
      resolve(true);
    });
  }
}
```

**说明** 

* 应用级预关闭时，预关闭回调遵循以下优先级：优先回调AbilityStage.onPrepareTerminationAsync，若未实现则回调AbilityStage.onPrepareTermination。若两者均未实现，则逐一回调该AbilityStage下各个正在运行的UIAbility的onPrepareToTerminate。
* onPrepareTerminationAsync若异步回调内发生Crash，按超时处理，若回调执行超过10秒未返回结果，应用将被强制关闭。
* 关机时，系统对应用响应时间有限制，应用应尽快完成预关闭处理，避免因超时导致系统强制关闭。
