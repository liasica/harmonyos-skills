---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-abilitydelegatorregistry
title: @ohos.application.abilityDelegatorRegistry (AbilityDelegatorRegistry)
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > 已停止维护的接口 > @ohos.application.abilityDelegatorRegistry (AbilityDelegatorRegistry)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4cd2e5b8aee630fe35144bb726eedc1f3e5cb9ca91f54a8bdb89181097ffdcc0
---

AbilityDelegatorRegistry模块提供用于存储已注册的[AbilityDelegator](js-apis-inner-application-abilitydelegator.md)和[AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md)对象的全局寄存器的能力，包括获取应用程序的AbilityDelegator对象、获取单元测试参数AbilityDelegatorArgs对象。该模块中的接口只能用于测试框架中。

说明

本模块首批接口从API version 8开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.abilityDelegatorRegistry](js-apis-app-ability-abilitydelegatorregistry.md)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import AbilityDelegatorRegistry from '@ohos.application.abilityDelegatorRegistry';
```

## AbilityLifecycleState

PhonePC/2in1TabletTVWearable

Ability生命周期状态。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | 0 | 表示无效状态。 |
| CREATE | 1 | 表示Ability处于已创建状态。 |
| FOREGROUND | 2 | 表示Ability处于前台状态。 |
| BACKGROUND | 3 | 表示Ability处于后台状态。 |
| DESTROY | 4 | 表示Ability处于已销毁状态。 |

## abilityDelegatorRegistry.getAbilityDelegator

PhonePC/2in1TabletTVWearable

getAbilityDelegator(): AbilityDelegator

获取应用程序的AbilityDelegator对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityDelegator](js-apis-inner-application-abilitydelegator.md) | [AbilityDelegator](js-apis-inner-application-abilitydelegator.md)对象。可以用来调度测试框架相关功能。 |

**示例：**

```
1. import AbilityDelegatorRegistry from '@ohos.application.abilityDelegatorRegistry';

3. let abilityDelegator = AbilityDelegatorRegistry.getAbilityDelegator();
```

## abilityDelegatorRegistry.getArguments

PhonePC/2in1TabletTVWearable

getArguments(): AbilityDelegatorArgs

获取单元测试参数AbilityDelegatorArgs对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md) | [AbilityDelegatorArgs](js-apis-inner-application-abilitydelegatorargs.md)对象。可以用来获取测试参数。 |

**示例：**

```
1. import AbilityDelegatorRegistry from '@ohos.application.abilityDelegatorRegistry';

3. let args = AbilityDelegatorRegistry.getArguments();
4. console.info(`getArguments bundleName: ${args.bundleName}`);
5. console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
6. console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```
