---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-ability
title: "@ohos.ability.ability (Ability模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > @ohos.ability.ability (Ability模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f618a86b76034bd21fb0029befafd98685d3ccbf8d0f3ab6a8563b30d3181e51
---

Ability模块将二级模块API组织在一起方便开发者进行导出。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { ability } from '@kit.AbilityKit';
```

## DataAbilityHelper

type DataAbilityHelper = \_DataAbilityHelper

DataAbilityHelper二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_DataAbilityHelper](js-apis-inner-ability-dataabilityhelper.md) | DataAbilityHelper二级模块。 |

## PacMap

type PacMap = \_PacMap

PacMap二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：

API版本9-10：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_PacMap](js-apis-inner-ability-dataabilityhelper.md#pacmap) | DataAbilityHelper二级模块。 |

## DataAbilityOperation

type DataAbilityOperation = \_DataAbilityOperation

DataAbilityOperation二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_DataAbilityOperation](js-apis-inner-ability-dataabilityoperation.md) | DataAbilityOperation二级模块。 |

## DataAbilityResult

type DataAbilityResult = \_DataAbilityResult

DataAbilityResult二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_DataAbilityResult](js-apis-inner-ability-dataabilityresult.md) | DataAbilityResult二级模块。 |

## AbilityResult

type AbilityResult = \_AbilityResult

AbilityResult二级模块。

**系统能力**：SystemCapability.Ability.AbilityBase

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityResult](js-apis-inner-ability-abilityresult.md) | AbilityResult二级模块。 |

## ConnectOptions

type ConnectOptions = \_ConnectOptions

ConnectOptions二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ConnectOptions](js-apis-inner-ability-connectoptions.md) | ConnectOptions二级模块。 |

## StartAbilityParameter

type StartAbilityParameter = \_StartAbilityParameter

StartAbilityParameter二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_StartAbilityParameter](js-apis-inner-ability-startabilityparameter.md) | StartAbilityParameter二级模块。 |

**示例：**

```ts
import { ability } from '@kit.AbilityKit';

let dataAbilityHelper: ability.DataAbilityHelper;
let pacMap: ability.PacMap;
let dataAbilityOperation: ability.DataAbilityOperation;
let dataAbilityResult: ability.DataAbilityResult;
let abilityResult: ability.AbilityResult;
let connectOptions: ability.ConnectOptions;
let startAbilityParameter: ability.StartAbilityParameter;
```
