---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver
title: ApplicationStateObserver
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ApplicationStateObserver
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b2a3c6d220ad4cb50c606e49f38e86074e8c252c642f04e9841441cc3c7391b4
---

应用状态监听器，可以作为入参传入[on('applicationState')](js-apis-app-ability-appmanager.md#appmanageronapplicationstate14)方法，监听应用的生命周期变化。

**说明** 

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { appManager } from '@kit.AbilityKit';
```

## ApplicationStateObserver.onForegroundApplicationChanged

onForegroundApplicationChanged(appStateData: AppStateData): void

应用前后台状态发生变化时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appStateData | [AppStateData](js-apis-inner-application-appstatedata.md) | 是 | 应用状态信息。 |

## ApplicationStateObserver.onAbilityStateChanged

onAbilityStateChanged(abilityStateData: AbilityStateData): void

Ability状态发生变化时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityStateData | [AbilityStateData](js-apis-inner-application-abilitystatedata.md) | 是 | Ability状态信息。 |

## ApplicationStateObserver.onProcessCreated

onProcessCreated(processData: ProcessData): void

进程创建时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processData | [ProcessData](js-apis-inner-application-processdata.md) | 是 | 进程数据信息。 |

## ApplicationStateObserver.onProcessDied

onProcessDied(processData: ProcessData): void

进程销毁时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processData | [ProcessData](js-apis-inner-application-processdata.md) | 是 | 进程数据信息。 |

## ApplicationStateObserver.onProcessStateChanged

onProcessStateChanged(processData: ProcessData): void

进程状态发生变化时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processData | [ProcessData](js-apis-inner-application-processdata.md) | 是 | 进程数据信息。 |

## ApplicationStateObserver.onAppStarted

onAppStarted(appStateData: AppStateData): void

应用第一个进程创建时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appStateData | [AppStateData](js-apis-inner-application-appstatedata.md) | 是 | 应用状态信息。 |

## ApplicationStateObserver.onAppStopped

onAppStopped(appStateData: AppStateData): void

应用最后一个进程销毁时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appStateData | [AppStateData](js-apis-inner-application-appstatedata.md) | 是 | 应用状态信息。 |

## ProcessData

type ProcessData = \_ProcessData.default

进程数据信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| \_[ProcessData](js-apis-inner-application-processdata.md).default | 进程数据信息。 |

**示例：**

```ts
import { appManager } from '@kit.AbilityKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.`);
  },
  onProcessCreated(processData) {
    console.info(`onProcessCreated, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessDied(processData) {
    console.info(`onProcessDied, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessStateChanged(processData) {
    console.info(`onProcessStateChanged, processData: ${JSON.stringify(processData)}.`);
  },
  onAppStarted(appStateData) {
    console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAppStopped(appStateData) {
    console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.`);
  }
};
let observerCode = appManager.on('applicationState', applicationStateObserver);
```
