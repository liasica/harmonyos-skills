---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityoperation
title: DataAbilityOperation
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > ability > DataAbilityOperation
category: harmonyos-references
scraped_at: 2026-09-02T15:00:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a6f41727b78546ac097f88a6ab01aee6280c763736132a1ff2328ab8f6ef7d49
---

定义DataAbility数据操作方式，可以作为[executeBatch](js-apis-inner-ability-dataabilityhelper.md#dataabilityhelperexecutebatch)的入参，操作数据库的信息。

**说明** 

本接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此接口仅可在FA模型下使用。

## 导入模块

```ts
import ability from '@ohos.ability.ability';
```

## 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 指示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| type | [featureAbility.DataAbilityOperationType](js-apis-ability-featureability.md#dataabilityoperationtype7) | 否 | 否 | 指示数据操作类型。 |
| valuesBucket | [rdb.ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 否 | 是 | 指示要操作的数据值。 |
| valueBackReferences | [rdb.ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 否 | 是 | 指示数据值的反向引用，用于应用批处理中前一步操作生成的键值。 |
| predicates | [dataAbility.DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 否 | 是 | 指示要设置的筛选条件。如果此参数为空，则操作所有数据记录。 |
| predicatesBackReferences | Map<number, number> | 否 | 是 | 指示用作谓词中筛选条件的反向引用。 |
| interrupted | boolean | 否 | 是 | 指示是否可以中断批处理操作。true表示可以中断批处理操作，false表示不可中断批处理操作。 |
| expectedCount | number | 否 | 是 | 指示要更新或删除的预期行数。 |
