---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintent
title: @ohos.app.ability.insightIntent (意图框架基础定义)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.insightIntent (意图框架基础定义)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed9283a21e39c3cd150c7daf710b2fdbfdd8a3f690c05cf679673fdb97c7a028
---

本模块提供[意图框架](../harmonyos-guides/insight-intent-overview.md)基础定义。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { insightIntent } from '@kit.AbilityKit';
```

## ExecuteMode

PhonePC/2in1TabletTVWearable

意图执行模式。表示系统入口触发意图执行时传递的执行模式，每个意图支持的执行模式在意图开发时定义。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UI\_ABILITY\_FOREGROUND | 0 | 将UIAbility在前台显示。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| UI\_ABILITY\_BACKGROUND | 1 | 将UIAbility在后台拉起。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| UI\_EXTENSION\_ABILITY | 2 | 拉起UIExtensionAbility。 |

## ExecuteResult

PhonePC/2in1TabletTVWearable

意图执行的返回结果。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 意图执行返回的错误码，由开发者定义。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| result | Record<string, Object> | 否 | 是 | 意图执行返回的结果，通常会包含需要返回给系统入口的数据。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| uris18+ | Array<string> | 否 | 是 | 意图执行返回的URI列表。该字段需要与flags字段配合使用，根据URI列表将flags字段的相应权限授权给系统入口。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| flags18+ | number | 否 | 是 | 意图执行返回给系统入口的URI列表的授权权限。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。  **说明：**  该参数仅支持FLAG\_AUTH\_READ\_URI\_PERMISSION、FLAG\_AUTH\_WRITE\_URI\_PERMISSION、FLAG\_AUTH\_READ\_URI\_PERMISSION|FLAG\_AUTH\_WRITE\_URI\_PERMISSION。权限介绍见[Flags](js-apis-app-ability-wantconstant.md#flags)。 |

## IntentEntity20+

PhonePC/2in1TabletTVWearable

意图实体结构体定义，用于定义意图执行过程中涉及的关键信息对象，包括意图参数和意图执行结果等。

开发者通过继承该类来定义意图实体，继承类需使用[@InsightIntentEntity](js-apis-app-ability-insightintentdecorator.md#insightintententity)装饰。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityId | string | 否 | 否 | 意图实体的ID。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## IntentResult<T>20+

PhonePC/2in1TabletTVWearable

意图执行的返回结果，支持[泛型类型](../harmonyos-guides/introduction-to-arkts.md#泛型类和接口)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 意图执行返回的错误码，由开发者定义。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |
| result | T | 否 | 是 | 意图执行返回的结果，通常会包含需要返回给系统入口的数据。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## ReturnMode23+

PhonePC/2in1TabletTVWearable

意图执行结果返回给意图拉起方的返回形式。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CALLBACK | 0 | 表示意图执行结果将由[意图执行基类](js-apis-app-ability-insightintentexecutor.md)中的[onExecuteInUIAbilityForegroundMode](js-apis-app-ability-insightintentexecutor.md#onexecuteinuiabilityforegroundmode)接口或[onExecuteInUIExtensionAbility](js-apis-app-ability-insightintentexecutor.md#onexecuteinuiextensionability)接口返回。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| FUNCTION | 1 | 表示意图执行结果会延迟返回，直到开发者主动调用[意图提供方管理能力](js-apis-app-ability-insightintentprovider.md)中的[sendExecuteResult](js-apis-app-ability-insightintentprovider.md#insightintentprovidersendexecuteresult)接口或[sendIntentResult](js-apis-app-ability-insightintentprovider.md#insightintentprovidersendintentresult)接口返回意图执行结果。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
