---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentcard
title: AgentCard
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AgentCard
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1be8840bc78ed9111613dc8f593fe870b2689ddb1c3faca82c4f8f3c1fbd1bd4
---

AgentCard相当于Agent(智能体)的"名片"，用于描述Agent的能力和技能，由开发者在Agent的配置文件agent\_config.json中配置。

一个Agent就是一个AgentExtensionAbility实例。开发者可以通过AgentExtensionContext中的agentCard属性获取到当前AgentExtensionAbility的AgentCard。

**说明** 

本模块首批接口从API version 24 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## AgentCard

描述Agent的基本信息和能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| agentId | string | 否 | 否 | Agent的唯一标识符，在同一个应用中，agentId不可重复。 |
| name | string | 否 | 否 | Agent的名称。使用方一般用于在UI界面中展示给用户，例如"Recipe Assistant"（食谱助手）。 |
| description | string | 否 | 否 | Agent功能的描述。该描述应清晰说明Agent的核心功能和用途，帮助用户理解Agent能做什么，例如"帮助用户搜索食谱、规划菜单并提供烹饪建议"。 |
| type | [agentConstant.AgentCardType](js-apis-app-agent-agentconstant.md#agentconstantagentcardtype) | 否 | 是 | AgentCard的类型。如果未指定，默认为APP类型。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| provider | [AgentProvider](js-apis-inner-application-agentcard.md#agentprovider) | 否 | 是 | Agent的服务提供商信息，包含提供商的组织名称和官方网站URL，用于标识Agent的来源和版权信息。 |
| version | string | 否 | 否 | Agent的版本号。遵循语义化版本规范（如"1.0.0"），格式由提供商定义。版本号用于标识Agent的功能迭代和兼容性变化。 |
| documentationUrl | string | 否 | 是 | Agent文档的URL。提供详细的Agent使用文档、API说明、示例和最佳实践指南，帮助开发者更好地集成和使用该Agent。 |
| capabilities | [AgentCapabilities](js-apis-inner-application-agentcard.md#agentcapabilities) | 否 | 是 | Agent支持的可选能力集合。定义Agent支持的其他可选能力，如流式响应、推送通知、状态历史查询等。 |
| defaultInputModes | Array<string> | 否 | 否 | Agent在所有[AgentSkill](js-apis-inner-application-agentcard.md#agentskill)上支持的输入模式集。使用MIME类型格式定义支持的输入媒体类型，例如["text/plain"]表示纯文本输入，["application/json"]表示JSON结构化数据输入，["image/png"]表示图片输入。[AgentSkill](js-apis-inner-application-agentcard.md#agentskill)级别的inputModes会覆盖此默认设置。 |
| defaultOutputModes | Array<string> | 否 | 否 | Agent在所有[AgentSkill](js-apis-inner-application-agentcard.md#agentskill)上支持的输出模式集。使用MIME类型格式定义支持的输出媒体类型，例如["text/plain"]表示纯文本输出，["application/html"]表示HTML格式输出，["application/json"]表示JSON数据输出。[AgentSkill](js-apis-inner-application-agentcard.md#agentskill)级别的outputModes会覆盖此默认设置。 |
| skills | Array<[AgentSkill](js-apis-inner-application-agentcard.md#agentskill)> | 否 | 否 | Agent提供的功能集合。描述Agent可以执行的特定功能或技能，每个技能定义了具体的用途、标签和使用示例。Agent必须至少包含一个技能。 |
| iconUrl | string | 否 | 否 | Agent图标的URL。提供Agent的可视化标识图标，用于在UI界面中展示，增强Agent的辨识度和用户体验。  **说明**：系统不校验该字段内容，使用方需自行验证iconUrl的合法性和安全性。 |
| category | string | 否 | 否 | Agent的类别。用于对Agent进行分类管理，常见的类别包括："productivity"（生产力）、"entertainment"（娱乐）、"education"（教育）、"finance"（金融）、"health"（健康）等。 |
| extension | string | 否 | 是 | Agent的扩展配置项。用于存储自定义的扩展配置信息，如Agent开场白、版本协议号等，格式为JSON字符串。 |
| appInfo | [AgentAppInfo](js-apis-inner-application-agentcard.md#agentappinfo) | 否 | 否 | Agent所在的应用信息。包含Agent所属的应用包名、模块名和能力名等标识信息，用于定位和管理AgentExtensionAbility实例。 |

## AgentProvider

表示Agent的服务提供商。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| organization | string | 否 | 否 | Agent提供商的组织名称。标识开发或提供该Agent的公司、组织或个人名称。 |
| url | string | 否 | 否 | Agent提供商的网站或相关文档的URL。提供指向提供商官方网站、产品页面或相关文档的HTTPS链接，用于用户了解更多信息或获取支持。 |

## AgentCapabilities

定义Agent支持的可选能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streaming | boolean | 否 | 是 | Agent是否支持流式响应。  true：表示支持SSE（Server-Sent Events）流式响应，可以实时返回部分结果。  false：表示不支持流式，仅支持一次性返回完整结果。启用流式响应后，客户端可使用stream方法获取实时数据流。 |
| pushNotifications | boolean | 否 | 是 | Agent是否支持为异步任务更新发送推送通知。  true：表示支持，当长时间运行的任务状态发生变化时（如任务完成、失败或进度更新），Agent可以主动推送通知给客户端。  false：表示不支持，客户端需要轮询查询任务状态。 |
| stateTransitionHistory | boolean | 否 | 是 | Agent是否支持查看任务状态变化历史。  true：表示支持，客户端可以查询任务从创建到完成的完整状态转换记录（如pending->running->completed）。  false：表示不支持状态历史查询。 |
| extendedAgentCard | boolean | 否 | 是 | Agent是否支持在认证时提供扩展的AgentCard。  true：表示支持，客户端在通过认证后可以获取包含额外信息（如私有配置、高级能力）的扩展AgentCard。  false：表示仅提供基础AgentCard。 |
| extension | string | 否 | 是 | Agent支持的协议扩展。用于存储自定义的扩展能力配置，格式为JSON字符串，可以包含协议级别的扩展参数和自定义字段，由开发者和Agent使用方约定。 |

## AgentSkill

表示Agent可以执行的不同能力或功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | AgentSkill的唯一标识符，在一个AgentCard中必须唯一。建议使用具有语义的命名格式（如"route-planner"、"recipe-search"），用于在API调用中精确指定要使用的技能。 |
| name | string | 否 | 否 | AgentSkill的名称。用于在UI界面中展示，例如"Route Planning"（路线规划）或"Recipe Search"（食谱搜索）。 |
| description | string | 否 | 否 | AgentSkill的详细描述。应清晰说明该技能的具体功能、适用场景和能解决的问题，例如"帮助用户规划两点之间的出行路线，提供多种交通方式选择和实时路况信息"。 |
| tags | Array<string> | 否 | 否 | 描述AgentSkill能力的关键字标签。用于技能分类、检索和推荐，例如["maps", "routing", "navigation"]或["cooking", "recipe", "food"]。标签应简洁明了，便于用户理解和搜索。 |
| examples | Array<string> | 否 | 是 | AgentSkill可以处理的示例提示或使用场景。提供具体的示例可以帮助用户理解如何使用该技能，例如["规划从上海到北京的路线"]。 |
| inputModes | Array<string> | 否 | 是 | AgentSkill支持的输入模式。使用MIME类型格式定义，例如["text/plain"]。如果未设置，将使用AgentCard级别的defaultInputModes。该字段允许为特定技能自定义输入类型，覆盖默认设置。 |
| outputModes | Array<string> | 否 | 是 | AgentSkill支持的输出模式。使用MIME类型格式定义，例如["text/plain", "application/html", "video/mp4"]。如果未设置，将使用AgentCard级别的defaultOutputModes。该字段允许为特定技能自定义输出类型，覆盖默认设置。 |
| extension | string | 否 | 是 | AgentSkill的扩展配置项。用于存储技能级别的自定义扩展配置，格式为JSON字符串，可以包含技能特有的参数和配置信息。 |

## AgentAppInfo

Agent的应用信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | Agent所属AgentExtensionAbility的Bundle名称。 |
| moduleName | string | 否 | 否 | Agent所属AgentExtensionAbility的Module名称。 |
| abilityName | string | 否 | 否 | Agent所属AgentExtensionAbility的Ability名称。 |
| deviceTypes | Array<string> | 否 | 是 | Agent支持的设备类型列表。取值范围参考[deviceTypes](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。 |
| minAppVersion | string | 否 | 是 | Agent运行的最低应用版本要求。使用语义化版本号格式（如"1.0.0"），指定运行该Agent所需的应用最低版本。低于此版本的应用将无法正确加载和运行该Agent。 |
