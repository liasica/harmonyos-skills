---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline
title: UIAbility备份恢复
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用模型 > 应用组件 > UIAbility组件 > UIAbility备份恢复
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:75436116b2d9cee02e92dd6c06a725a7bca63daf9b65827284395a8d35eb3c55
---

## 场景介绍

当应用后台运行时，可能由于系统资源管控等原因导致应用关闭、进程退出，应用直接退出可能会导致用户数据丢失。如果应用在[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)中启用了[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)备份恢复功能，并对临时数据进行保存，则可以在应用退出后的下一次启动时恢复先前的状态和数据（包括应用的页面栈以及[onSaveState()](../harmonyos-references/js-apis-app-ability-uiability.md#onsavestate)接口中保存的数据），从而保证用户体验的连贯性。

**说明** 

应用正常关闭时，不会触发[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)备份流程。应用正常启动（例如通过startAbility接口启动或点击图标启动）时，不触发[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)恢复流程。

## 运行机制

* [UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)数据备份：当应用后台运行时，如果因系统资源管控、进程被kill、异常崩溃等非正常原因退出时，系统自动调用[onSaveState()](../harmonyos-references/js-apis-app-ability-uiability.md#onsavestate)进行备份。
* [UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)数据恢复：恢复的[Want](../harmonyos-references/js-apis-app-ability-want.md)数据可以在应用的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中获取，页面栈数据在应用的[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期中恢复。

## 约束限制

* [UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)备份恢复支持多实例，备份数据保存7天，以文件的形式存储在应用的沙箱路径中。
* 备份数据存储在[Want](../harmonyos-references/js-apis-app-ability-want.md#want)中的parameter字段中，由于序列化大小限制，支持的最大数据量为200KB。
* 重启设备不支持还原备份。
* 备份恢复机制依赖任务保留机制，如果应用设置[removeMissionAfterTerminate](module-configuration-file.md#abilities标签)为true，或者设备不支持任务保留（比如PC/2in1设备），则备份恢复机制不生效。
* [UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)不支持备份恢复。

## 接口说明

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)备份恢复接口由[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)模块提供，开发者可以通过在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)中通过this.context直接调用，详见[开发步骤](ability-recover-guideline.md#开发步骤)。

| 接口名称 | 说明 |
| --- | --- |
| setRestoreEnabled(enabled: boolean): void | 设置[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)是否启用备份恢复。 |

[setRestoreEnabled()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setrestoreenabled14)接口需要在应用初始化阶段调用（[onForeground()](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)前），比如[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)调用。

## 开发步骤

开发者需要在应用模块初始化时启用[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的备份恢复功能。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ···

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'EntryAbility', '[Demo] EntryAbility onCreate');
    this.context.setRestoreEnabled(true);
    // ···
  }

// ···
}
```

开发者主动保存数据，在UIAbility启动时恢复。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ···

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'EntryAbility', '[Demo] EntryAbility onCreate');
    this.context.setRestoreEnabled(true);
    if (want && want.parameters) {
      let recoveryMyData = want.parameters['myData'];
    }
  }

  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>): AbilityConstant.OnSaveResult {
    // 保存应用数据。
    hilog.info(DOMAIN, 'EntryAbility', '[Demo] EntryAbility onSaveState');
    wantParam['myData'] = 'my1234567';
    return AbilityConstant.OnSaveResult.ALL_AGREE;
  }

// ···
}
```
