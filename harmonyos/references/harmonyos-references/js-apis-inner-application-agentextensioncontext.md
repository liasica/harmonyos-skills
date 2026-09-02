---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentextensioncontext
title: AgentExtensionContext (智能体扩展组件上下文)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AgentExtensionContext (智能体扩展组件上下文)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9e8803cb440e2f15cecfdda4cbcb0a02914eb93f444e80ef8454c0db1b4dd68d
---

AgentExtensionContext模块是[AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

AgentExtensionContext为开发者提供访问当前[AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)智能体所配置的[AgentCard](js-apis-inner-application-agentcard.md)信息的能力。

**说明** 

* 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 在本文档的示例中，通过this.context来获取AgentExtensionContext，其中this代表继承自AgentExtensionAbility的实例。

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## AgentExtensionContext

### 属性

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| agentCard | [AgentCard](js-apis-inner-application-agentcard.md) | 否 | 否 | 当前[AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)智能体所配置的[AgentCard](js-apis-inner-application-agentcard.md#agentcard-1)信息。 |

**示例：**

```ts
import { AgentExtensionAbility, common } from '@kit.AbilityKit';

export default class AgentExtension extends AgentExtensionAbility {
  onCreate(): void {
    let tmpContext: common.AgentExtensionContext = this.context; // 获取AgentExtensionContext
    console.info(`agentCard info data: ${JSON.stringify(tmpContext.agentCard)}.`);
  }
}
```
