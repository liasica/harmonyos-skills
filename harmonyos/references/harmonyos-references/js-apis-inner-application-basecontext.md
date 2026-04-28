---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext
title: BaseContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > BaseContext
category: harmonyos-references
scraped_at: 2026-04-28T07:58:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5da8b40fdf8059c8fc4c83d5b183467f727eca4a74a73fa2daec316b59886930
---

BaseContext抽象类用于表示继承的子类Context是Stage模型还是FA模型，是所有Context类型的父类。

说明

本模块首批接口从API version 8 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stageMode | boolean | 否 | 否 | 表示是否Stage模型。  true：[Stage模型](../harmonyos-guides/ability-terminology.md#stage模型)。  false：[FA模型](../harmonyos-guides/ability-terminology.md#fa模型)。 |

**示例：**

以Stage模型为例，用户可通过UIAbilityContext访问stageMode字段。

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

3. class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. // EntryAbility onCreate, isStageMode: true
6. console.info(`EntryAbility onCreate, isStageMode: ${this.context.stageMode}`);
7. }
8. }
```
