---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-agent-agentuiextensionability
title: "@ohos.app.ability.AgentUIExtensionAbility (带界面的智能体扩展组件)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.AgentUIExtensionAbility (带界面的智能体扩展组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e40504190b71e5f646d52df44e1e816b4e30612a653e939aff9ff43d2dc6c631
---

AgentUIExtensionAbility继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)，为开发者提供接入端侧Agent UI界面显示能力。

[AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)提供智能体扩展能力，AgentUIExtensionAbility必须与AgentExtensionAbility共进程运行，不支持独立运行。

各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

**说明** 

本模块首批接口从API version 24 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口不支持在[har](../harmonyos-guides/har-package.md)包中使用。

## 约束限制

* 同一个拉起方在同一时间内最多只能拉起来自同一个提供方的5个AgentUIExtensionAbility实例。
* AgentUIExtensionAbility内的窗口和ArkUI组件均不允许创建子窗口，也不支持在子窗口中显示。

## 导入模块

```ts
import { AgentUIExtensionAbility } from '@kit.AbilityKit';
```

## AgentUIExtensionAbility

AgentUIExtensionAbility继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)，为开发者提供接入端侧Agent UI界面显示能力。例如，当Agent开发者希望在其他应用中显示Agent返回的结果时，可以通过接入AgentUIExtensionAbility提供展示嵌入式弹窗的能力。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。
