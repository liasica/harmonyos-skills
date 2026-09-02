---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentconstant
title: "@ohos.app.agent.agentConstant (Agent常量)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.agent.agentConstant (Agent常量)
category: harmonyos-references
scraped_at: 2026-09-02T14:51:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f32ebee2e6d81b2653e16090de1c72d6fd95b6cadffee8b1ca6c73a92e21df43
---

agentConstant模块提供Agent相关的常量。

**起始版本：** 26.0.0

## 导入模块

```ts
import { agentConstant } from '@kit.AbilityKit';
```

## agentConstant.AgentCardType

Agent卡片的类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**：从API版本26.0.0开始，该枚举支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP | 0 | 应用型Agent卡片，适用于传统安装应用，Agent能力随应用一起安装和卸载，需要用户主动安装应用后才能使用。 |
| ATOMIC\_SERVICE | 1 | 元服务型Agent卡片，适用于免安装的元服务，Agent能力可以即用即离，无需预先安装，支持快速体验和分享。 |
