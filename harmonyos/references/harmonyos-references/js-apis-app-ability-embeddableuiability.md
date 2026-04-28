---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddableuiability
title: @ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:006e9b0b23dbb9d245a8a9b5bfd8fb1e7fd694be08a9917c574d971584972c5b
---

EmbeddableUIAbility组件是为元服务提供可嵌入式的UIAbility组件，继承自[UIAbility](js-apis-app-ability-uiability.md)。

开发者通过实现EmbeddableUIAbility，为其他应用提供跳出式启动和嵌入式启动元服务方式。

各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

说明

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { EmbeddableUIAbility } from '@kit.AbilityKit';
```

## EmbeddableUIAbility

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [EmbeddableUIAbilityContext](-apis-inner-application-embeddableuiabilitycontext.md) | 否 | 否 | EmbeddableUIAbility组件的上下文。 |
