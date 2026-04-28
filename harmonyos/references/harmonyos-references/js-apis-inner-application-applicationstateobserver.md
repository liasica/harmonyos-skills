---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver
title: ApplicationStateObserver
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ApplicationStateObserver
category: harmonyos-references
scraped_at: 2026-04-28T07:58:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:553d01c89d3574f7c7ec69f33ed3474faf372ee179b62ff1a63205aa2c96ae91
---

应用状态监听器，可以作为入参传入[on('applicationState')](js-apis-app-ability-appmanager.md#appmanageronapplicationstate14)方法，监听应用的生命周期变化。

说明

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { appManager } from '@kit.AbilityKit';
```

## ApplicationStateObserver.onForegroundApplicationChanged

PhonePC/2in1TabletTVWearable

onForegroundApplicationChanged(appStateData: AppStateData): void

应用前后台状态发生变化时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appStateData | [AppStateData](js-apis-inner-application-appstatedata.md) | 是 | 应用状态信息。 |

## ApplicationStateObserver.onAbilityStateChanged

PhonePC/2in1TabletTVWearable

onAbilityStateChanged(abilityStateData: AbilityStateData): void

Ability状态发生变化时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityStateData | [AbilityStateData](js-apis-inner-application-abilitystatedata.md) | 是 | Ability状态信息。 |

## ApplicationStateObserver.onProcessCreated

PhonePC/2in1TabletTVWearable

onProcessCreated(processData: ProcessData): void

进程创建时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processData | [ProcessData](js-apis-inner-application-processdata.md) | 是 | 进程数据信息。 |

## ApplicationStateObserver.onProcessDied

PhonePC/2in1TabletTVWearable

onProcessDied(processData: ProcessData): void

进程销毁时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processData | [ProcessData](js-apis-inner-application-processdata.md) | 是 | 进程数据信息。 |

## ApplicationStateObserver.onProcessStateChanged

PhonePC/2in1TabletTVWearable

onProcessStateChanged(processData: ProcessData): void

进程状态更新时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processData | [ProcessData](js-apis-inner-application-processdata.md) | 是 | 进程数据信息。 |

## ApplicationStateObserver.onAppStarted

PhonePC/2in1TabletTVWearable

onAppStarted(appStateData: AppStateData): void

应用第一个进程创建时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appStateData | [AppStateData](js-apis-inner-application-appstatedata.md) | 是 | 应用状态信息。 |

## ApplicationStateObserver.onAppStopped

PhonePC/2in1TabletTVWearable

onAppStopped(appStateData: AppStateData): void

应用最后一个进程销毁时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appStateData | [AppStateData](js-apis-inner-application-appstatedata.md) | 是 | 应用状态信息。 |

## ProcessData

PhonePC/2in1TabletTVWearable

type ProcessData = \_ProcessData.default

进程数据信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ProcessData.default](js-apis-inner-application-processdata.md) | 进程数据信息。 |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';

3. let applicationStateObserver: appManager.ApplicationStateObserver = {
4. onForegroundApplicationChanged(appStateData) {
5. console.info(`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.`);
6. },
7. onAbilityStateChanged(abilityStateData) {
8. console.info(`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.`);
9. },
10. onProcessCreated(processData) {
11. console.info(`onProcessCreated, processData: ${JSON.stringify(processData)}.`);
12. },
13. onProcessDied(processData) {
14. console.info(`onProcessDied, processData: ${JSON.stringify(processData)}.`);
15. },
16. onProcessStateChanged(processData) {
17. console.info(`onProcessStateChanged, processData: ${JSON.stringify(processData)}.`);
18. },
19. onAppStarted(appStateData) {
20. console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.`);
21. },
22. onAppStopped(appStateData) {
23. console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.`);
24. }
25. };
26. let observerCode = appManager.on('applicationState', applicationStateObserver);
```
