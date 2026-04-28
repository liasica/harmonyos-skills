---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitydelegatorregistry
title: @ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > @ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1bf1bd80705ee30db7d94ab9b1360fb4f6c66fed8152019fb1c7fb1b2c5d2867
---

AbilityDelegatorRegistry是自动化测试框架使用指南模块，该模块用于获取[AbilityDelegator](js-apis-inner-application-abilitydelegator.md)和[AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md)对象，其中[AbilityDelegator](js-apis-inner-application-abilitydelegator.md)对象提供添加用于监视指定ability的生命周期状态更改的[AbilityMonitor](js-apis-inner-application-abilitymonitor.md#abilitymonitor-1)对象的能力，[AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md)对象提供获取当前测试参数的能力。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../harmonyos-guides/unittest-guidelines.md)中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## AbilityLifecycleState

PhonePC/2in1TabletTVWearable

Ability生命周期状态，该类型为枚举，可配合[AbilityDelegator](js-apis-inner-application-abilitydelegator.md)的[getAbilityState(ability)](js-apis-inner-application-abilitydelegator.md#getabilitystate9)方法返回不同ability生命周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：以下各项对应的系统能力均为SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | 0 | 表示Ability处于无效状态。 |
| CREATE | 1 | 表示Ability处于已创建状态。 |
| FOREGROUND | 2 | 表示Ability处于前台状态。 |
| BACKGROUND | 3 | 表示Ability处于后台状态。 |
| DESTROY | 4 | 表示Ability处于已销毁状态。 |

## abilityDelegatorRegistry.getAbilityDelegator

PhonePC/2in1TabletTVWearable

getAbilityDelegator(): AbilityDelegator

获取应用程序的[AbilityDelegator](js-apis-inner-application-abilitydelegator.md)对象，该对象能够使用调度测试框架的相关功能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityDelegator](js-apis-inner-application-abilitydelegator.md) | [AbilityDelegator](js-apis-inner-application-abilitydelegator.md)对象。可以用来调度测试框架相关功能。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { Want } from '@kit.AbilityKit';

4. let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
5. let want: Want = {
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EntryAbility'
8. };

10. abilityDelegator.startAbility(want, (err) => {
11. if (err) {
12. console.error(`Failed start ability, error: ${JSON.stringify(err)}`);
13. } else {
14. console.info('Success start ability.');
15. }
16. });
```

## abilityDelegatorRegistry.getArguments

PhonePC/2in1TabletTVWearable

getArguments(): AbilityDelegatorArgs

获取单元测试参数[AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md) | [AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md)对象。可以用来获取测试参数。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let args = abilityDelegatorRegistry.getArguments();
4. console.info(`getArguments bundleName: ${args.bundleName}`);
5. console.info(`getArguments parameters: ${JSON.stringify(args.parameters)}`);
6. console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
7. console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```

## AbilityDelegator

PhonePC/2in1TabletTVWearable

type AbilityDelegator = \_AbilityDelegator

提供通过[AbilityMonitor](js-apis-inner-application-abilitymonitor.md)实例来监听和管理[UIAbility](js-apis-app-ability-uiability.md)生命周期变化的能力。例如获取UIAbility当前状态（如是否已创建/是否在前台等）、查询当前获焦的UIAbility、等待UIAbility进入某个生命周期节点（如等待UIAbility进入onForeground）、启动指定UIAbility、设置超时机制等功能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityDelegator](js-apis-inner-application-abilitydelegator.md) | AbilityDelegator模块。 |

## AbilityDelegatorArgs

PhonePC/2in1TabletTVWearable

type AbilityDelegatorArgs = \_AbilityDelegatorArgs

提供在应用程序执行测试用例期间，获取测试用例参数AbilityDelegatorArgs对象的能力。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md) | AbilityDelegatorArgs模块。 |

## AbilityMonitor

PhonePC/2in1TabletTVWearable

type AbilityMonitor = \_AbilityMonitor

提供作为abilityDelegator中的[addAbilityMonitor](js-apis-inner-application-abilitydelegator.md#addabilitymonitor9)的入参来监听指定UIAbility的生命周期变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityMonitor](js-apis-inner-application-abilitymonitor.md) | AbilityMonitor模块。 |

## ShellCmdResult

PhonePC/2in1TabletTVWearable

type ShellCmdResult = \_ShellCmdResult

提供Shell命令执行结果的能力。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ShellCmdResult](js-apis-inner-application-shellcmdresult.md) | ShellCmdResult模块。 |

## AbilityStageMonitor14+

PhonePC/2in1TabletTVWearable

type AbilityStageMonitor = \_AbilityStageMonitor

提供监听指定[AbilityStage](js-apis-app-ability-abilitystage.md)对象的能力。开发者可以将AbilityStageMonitor作为[abilityDelegator.waitAbilityStageMonitor](js-apis-inner-application-abilitydelegator.md#waitabilitystagemonitor9)的入参来注册监听。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStageMonitor](js-apis-inner-application-abilitystagemonitor.md) | AbilityStageMonitor模块。 |
