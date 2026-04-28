---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-embeddableuiabilitycontext
title: EmbeddableUIAbilityContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > EmbeddableUIAbilityContext
category: harmonyos-references
scraped_at: 2026-04-28T07:58:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ee7dbe5b278edd2283d9eb08c4afd00b7df81700e9ff83ded61c37f334d3dbaf
---

EmbeddableUIAbilityContext是[EmbeddableUIAbility](js-apis-app-ability-embeddableuiability.md)组件的上下文，继承自[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。

每个EmbeddableUIAbility组件实例化时，系统都会自动创建对应的EmbeddableUIAbilityContext。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## EmbeddableUIAbilityContext

PhonePC/2in1TabletTVWearable

开发者可以通过EmbeddableUIAbilityContext获取EmbeddableUIAbility的相关配置信息以及操作EmbeddableUIAbility和ServiceExtensionAbility的方法，如启动EmbeddableUIAbility，停止当前EmbeddableUIAbilityContext所属的EmbeddableUIAbility，启动、停止、连接、断开连接ServiceExtensionAbility等。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。
