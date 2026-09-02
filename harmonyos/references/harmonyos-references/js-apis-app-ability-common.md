---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common
title: "@ohos.app.ability.common (Ability公共模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.common (Ability公共模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f3dbf7aae9b9dc842ce0e300444c78c122d556fec9f5aadc6c8ae820e0c69b62
---

本模块提供Ability Kit中常用公共能力的纯类型定义，包含各类上下文对象、回调接口和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## UIAbilityContext

type UIAbilityContext = \_UIAbilityContext.default

[UIAbility](js-apis-app-ability-uiability.md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIAbilityContext.default](js-apis-inner-application-uiabilitycontext.md) | UIAbilityContext组件上下文。 |

## AbilityStageContext

type AbilityStageContext = \_AbilityStageContext.default

[AbilityStage](js-apis-app-ability-abilitystage.md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStageContext.default](js-apis-inner-application-abilitystagecontext.md) | AbilityStage组件上下文。 |

## ApplicationContext

type ApplicationContext = \_ApplicationContext.default

应用上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ApplicationContext.default](js-apis-inner-application-applicationcontext.md) | 应用上下文。 |

## BaseContext

type BaseContext = \_BaseContext.default

所有Context类型的父类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_BaseContext.default](js-apis-inner-application-basecontext.md) | 所有Context的父类。 |

## Context

type Context = \_Context.default

[Stage模型](../harmonyos-guides/ability-terminology.md#stage模型)的上下文基类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_Context.default](js-apis-inner-application-context.md) | Stage模型的上下文基类。 |

## ExtensionContext

type ExtensionContext = \_ExtensionContext.default

[ExtensionAbility](js-apis-app-ability-extensionability.md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ExtensionContext.default](js-apis-inner-application-extensioncontext.md) | ExtensionAbility组件上下文。 |

## FormExtensionContext

type FormExtensionContext = \_FormExtensionContext.default

[FormExtensionAbility](js-apis-app-form-formextensionability.md)组件上下文，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_FormExtensionContext.default](js-apis-inner-application-formextensioncontext.md) | FormExtensionAbility组件上下文。 |

## VpnExtensionContext11+

type VpnExtensionContext = \_VpnExtensionContext.default

[VpnExtensionAbility](js-apis-vpnextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_VpnExtensionContext.default](js-apis-inner-application-vpnextensioncontext.md) | VpnExtensionAbility组件上下文。 |

## EventHub

type EventHub = \_EventHub.default

EventHub是系统提供的基于发布-订阅模式实现的事件通信机制。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_EventHub.default](js-apis-inner-application-eventhub.md) | 系统提供的基于发布-订阅模式实现的事件通信机制。 |

## PacMap

type PacMap = \_PacMap

存储基础数据类型的容器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_PacMap](js-apis-inner-ability-dataabilityhelper.md#pacmap) | 存储基础数据类型的容器。 |

## AbilityResult

type AbilityResult = \_AbilityResult

定义Ability被拉起并退出后返回的结果码和数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityResult](js-apis-inner-ability-abilityresult.md) | 定义Ability被拉起并退出后返回的结果码和数据。 |

## AbilityStartCallback11+

type AbilityStartCallback = \_AbilityStartCallback

定义了拉起UIExtensionAbility的回调结果，通常作为[UIAbilityContext.startAbilityByType](js-apis-inner-application-uiabilitycontext.md#startabilitybytype11)/[UIExtensionContext.startAbilityByType](js-apis-app-ability-uiextensioncontentsession.md#startabilitybytype11)的入参传入。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStartCallback](js-apis-inner-application-abilitystartcallback.md) | 定义拉起UIExtensionAbility的回调结果。 |

## ConnectOptions

type ConnectOptions = \_ConnectOptions

在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ConnectOptions](js-apis-inner-ability-connectoptions.md) | 在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。 |

## UIExtensionContext10+

type UIExtensionContext = \_UIExtensionContext.default

[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIExtensionContext.default](js-apis-inner-application-uiextensioncontext.md) | UIExtensionAbility组件上下文。 |

## EmbeddableUIAbilityContext12+

type EmbeddableUIAbilityContext = \_EmbeddableUIAbilityContext.default

[EmbeddableUIAbility](js-apis-app-ability-embeddableuiability.md)组件上下文，继承自Context。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_EmbeddableUIAbilityContext.default](js-apis-inner-application-embeddableuiabilitycontext.md) | EmbeddableUIAbility组件上下文。 |

## PhotoEditorExtensionContext12+

type PhotoEditorExtensionContext = \_PhotoEditorExtensionContext.default

[PhotoEditorExtensionAbility](js-apis-app-ability-photoeditorextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AppExtension.PhotoEditorExtension

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_PhotoEditorExtensionContext.default](js-apis-app-ability-photoeditorextensioncontext.md) | PhotoEditorExtensionAbility组件上下文。 |

## UIServiceProxy14+

type UIServiceProxy = \_UIServiceProxy.default

UIServiceProxy提供了与UIServiceExtensionAbility服务端数据通信的能力。UIServiceExtensionAbility是一类特殊的ExtensionAbility组件，这类组件由系统提供，通常用于提供浮窗组件相关扩展能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIServiceProxy.default](js-apis-inner-application-uiserviceproxy.md) | 提供与UIServiceExtensionAbility服务端数据通信的能力。 |

## UIServiceExtensionConnectCallback14+

type UIServiceExtensionConnectCallback = \_UIServiceExtensionConnectCallback.default

在连接指定的UIServiceExtensionAbility服务时作为入参，用于提供UIServiceExtensionAbility连接回调数据能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIServiceExtensionConnectCallback.default](js-apis-inner-application-uiserviceextensionconnectcallback.md) | 提供UIServiceExtensionAbility连接回调数据能力。 |

## AppServiceExtensionContext20+

type AppServiceExtensionContext = \_AppServiceExtensionContext.default

[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AppServiceExtensionContext.default](js-apis-inner-application-appserviceextensioncontext.md) | AppServiceExtensionAbility组件上下文。 |

## FormEditExtensionContext22+

type FormEditExtensionContext = \_FormEditExtensionContext.default

[FormEditExtensionAbility](js-apis-app-form-formeditextensionability.md)组件上下文，继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_FormEditExtensionContext.default](js-apis-inner-application-formeditextensioncontext.md) | FormEditExtensionAbility组件上下文。 |

## LiveFormExtensionContext22+

type LiveFormExtensionContext = \_LiveFormExtensionContext.default

[LiveFormExtensionAbility](js-apis-app-form-liveformextensionability.md)组件上下文，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_LiveFormExtensionContext.default](js-apis-application-liveformextensioncontext.md) | LiveFormExtensionAbility组件上下文。 |

## AgentCard24+

type AgentCard = \_AgentCard

[AgentCard](js-apis-inner-application-agentcard.md)相当于Agent(智能体)的"名片"，用于描述Agent的能力和技能，由开发者在Agent的配置文件agent\_config.json中配置。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentCard](js-apis-inner-application-agentcard.md) | Agent(智能体)的"名片"，用于描述Agent的能力和技能。 |

## AgentProvider24+

type AgentProvider = \_AgentProvider

[AgentProvider](js-apis-inner-application-agentcard.md#agentprovider)表示Agent的服务提供商。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentProvider](js-apis-inner-application-agentcard.md#agentprovider) | Agent的服务提供商。 |

## AgentCapabilities24+

type AgentCapabilities = \_AgentCapabilities

[AgentCapabilities](js-apis-inner-application-agentcard.md#agentcapabilities)用来定义Agent支持的可选能力。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentCapabilities](js-apis-inner-application-agentcard.md#agentcapabilities) | 定义Agent支持的可选能力。 |

## AgentSkill24+

type AgentSkill = \_AgentSkill

[AgentSkill](js-apis-inner-application-agentcard.md#agentskill)表示Agent可以执行的不同能力或功能。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentSkill](js-apis-inner-application-agentcard.md#agentskill) | 表示Agent可以执行的不同能力或功能。 |

## AgentAppInfo24+

type AgentAppInfo = \_AgentAppInfo

[AgentAppInfo](js-apis-inner-application-agentcard.md#agentappinfo)表示Agent所属的应用信息。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentAppInfo](js-apis-inner-application-agentcard.md#agentappinfo) | Agent所属的应用信息。 |

## AgentHostProxy24+

type AgentHostProxy = \_AgentHostProxy

[AgentHostProxy](js-apis-inner-application-agenthostproxy.md)用于从[AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)服务端向客户端发送数据或安全认证请求。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentHostProxy](js-apis-inner-application-agenthostproxy.md) | 用于从[AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)服务端向客户端发送数据或安全认证请求。 |

## AgentExtensionContext24+

type AgentExtensionContext = \_AgentExtensionContext

[AgentExtensionContext](js-apis-inner-application-agentextensioncontext.md)是[AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AgentExtensionContext](js-apis-inner-application-agentextensioncontext.md) | [AgentExtensionAbility](js-apis-app-agent-agentextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

**示例：**

```ts
import { common } from '@kit.AbilityKit';

let uiAbilityContext: common.UIAbilityContext;
let abilityStageContext: common.AbilityStageContext;
let applicationContext: common.ApplicationContext;
let baseContext: common.BaseContext;
let context: common.Context;
let uiExtensionContext: common.UIExtensionContext;
let extensionContext: common.ExtensionContext;
let formExtensionContext: common.FormExtensionContext;
let vpnExtensionContext: common.VpnExtensionContext;
let eventHub: common.EventHub;
let pacMap: common.PacMap;
let abilityResult: common.AbilityResult;
let abilityStartCallback: common.AbilityStartCallback;
let connectOptions: common.ConnectOptions;
let embeddableUIAbilityContext: common.EmbeddableUIAbilityContext;
let photoEditorExtensionContext: common.PhotoEditorExtensionContext;
let uiServiceProxy : common.UIServiceProxy;
let uiServiceExtensionConnectCallback : common.UIServiceExtensionConnectCallback;
let appServiceExtensionContext : common.AppServiceExtensionContext;
let formEditExtensionContext : common.FormEditExtensionContext;
let liveFormExtensionContext : common.LiveFormExtensionContext;
let agentCard: common.AgentCard;
let agentProvider: common.AgentProvider;
let agentCapabilities: common.AgentCapabilities;
let agentSkill: common.AgentSkill;
let agentAppInfo: common.AgentAppInfo;
let agentHostProxy: common.AgentHostProxy;
let agentExtensionContext: common.AgentExtensionContext;
```
