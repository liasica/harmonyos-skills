---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability
title: @ohos.app.ability.Ability (Ability基类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.Ability (Ability基类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:12+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:5ff62c13835489d227169ce9052425948ddbcfa7a10cec22f7f73248dca81459
---

Ability类是应用生命周期调度的基本单元，是[UIAbility](js-apis-app-ability-uiability.md)和[ExtensionAbility](js-apis-app-ability-extensionability.md)的基类，提供系统配置更新回调和系统内存级别变化回调能力。该基类不支持开发者直接继承，开发者应根据具体的业务场景选择使用[UIAbility](js-apis-app-ability-uiability.md)或[ExtensionAbility](js-apis-app-ability-extensionability.md)，相关指南参见[Ability Kit简介](../harmonyos-guides/abilitykit-overview.md)。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Ability } from '@kit.AbilityKit';
```

## Ability的继承关系说明

PhonePC/2in1TabletTVWearable

Ability基类及其子类的继承关系如下图所示。

说明

部分ExtensionAbility组件（例如[FormExtensionAbility](js-apis-app-form-formextensionability.md)、[InputMethodExtensionAbility](js-apis-inputmethod-extension-ability.md)等）与下图中的ExtensionAbility基类不存在继承关系，均未在图中列出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/JsTlffUcS-OUf8x1mwhjHQ/zh-cn_image_0000002552799744.png?HW-CC-KV=V1&HW-CC-Date=20260427T235811Z&HW-CC-Expire=86400&HW-CC-Sign=02D8C9F62D6078439377CCD8240A840AD22D10981D9E911669840E4AEAFCAEE5)

## Ability.onConfigurationUpdate

PhonePC/2in1TabletTVWearable

onConfigurationUpdate(newConfig: Configuration): void

当系统环境变量发生变化时，系统会触发该回调。开发者可以重写该回调实现对系统环境变量变化时的响应，例如当系统语言类型发生变化时，应用可以在回调中进行定制化的处理等。

说明

该回调方法在实际触发时存在一定限制。例如如果开发者通过[setLanguage](js-apis-inner-application-applicationcontext.md#applicationcontextsetlanguage11)接口设置应用的语言，即便系统语言发生变化，系统也不再触发onConfigurationUpdate回调。详见[使用场景](../harmonyos-guides/subscribe-system-environment-variable-changes.md#使用场景)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newConfig | [Configuration](js-apis-app-ability-configuration.md) | 是 | 表示更新后的配置信息。 |

**示例：**

```
1. // Ability是顶层基类，不支持开发者直接继承。故以派生类UIAbility举例说明。
2. import { UIAbility, Configuration } from '@kit.AbilityKit';

4. class MyUIAbility extends UIAbility {
5. onConfigurationUpdate(config: Configuration) {
6. console.info(`onConfigurationUpdate, config: ${JSON.stringify(config)}`);
7. }
8. }
```

## Ability.onMemoryLevel

PhonePC/2in1TabletTVWearable

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

当整机可用内存变化到指定程度时，系统会触发该回调。开发者可以重写该回调实现对内存级别变化的响应，例如释放缓存数据等。

说明

onMemoryLevel回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务，因此不建议在该回调中释放UI组件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [AbilityConstant.MemoryLevel](js-apis-app-ability-abilityconstant.md#memorylevel) | 是 | 整机可用内存级别，对应的触发场景详见[AbilityConstant.MemoryLevel](js-apis-app-ability-abilityconstant.md#memorylevel)。 |

**示例：**

```
1. // Ability是顶层基类，不支持开发者直接继承。故以派生类UIAbility举例说明。
2. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

4. class MyUIAbility extends UIAbility {
5. onMemoryLevel(level: AbilityConstant.MemoryLevel) {
6. console.info(`onMemoryLevel, level: ${JSON.stringify(level)}`);
7. }
8. }
```
