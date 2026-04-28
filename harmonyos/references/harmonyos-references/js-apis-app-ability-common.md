---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common
title: @ohos.app.ability.common (Ability公共模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.common (Ability公共模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4beb9c79dc1acc1a8c5080090f754249d385a9eb020db55085893632e72f6b8f
---

本模块提供Ability Kit中常用公共能力的纯类型定义，包含各类上下文对象、回调接口和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## UIAbilityContext

PhonePC/2in1TabletTVWearable

type UIAbilityContext = \_UIAbilityContext.default

[UIAbility](js-apis-app-ability-uiability.md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIAbilityContext.default](js-apis-inner-application-uiabilitycontext.md) | UIAbilityContext组件上下文。 |

## AbilityStageContext

PhonePC/2in1TabletTVWearable

type AbilityStageContext = \_AbilityStageContext.default

[AbilityStage](js-apis-app-ability-abilitystage.md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStageContext.default](js-apis-inner-application-abilitystagecontext.md) | AbilityStage组件上下文。 |

## ApplicationContext

PhonePC/2in1TabletTVWearable

type ApplicationContext = \_ApplicationContext.default

应用上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ApplicationContext.default](js-apis-inner-application-applicationcontext.md) | 应用上下文。 |

## BaseContext

PhonePC/2in1TabletTVWearable

type BaseContext = \_BaseContext.default

所有Context类型的父类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_BaseContext.default](js-apis-inner-application-basecontext.md) | 所有Context的父类。 |

## Context

PhonePC/2in1TabletTVWearable

type Context = \_Context.default

[Stage模型](../harmonyos-guides/ability-terminology.md#stage模型)的上下文基类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_Context.default](js-apis-inner-application-context.md) | Stage模型的上下文基类。 |

## ExtensionContext

PhonePC/2in1TabletTVWearable

type ExtensionContext = \_ExtensionContext.default

[ExtensionAbility](js-apis-app-ability-extensionability.md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ExtensionContext.default](js-apis-inner-application-extensioncontext.md) | ExtensionAbility组件上下文。 |

## FormExtensionContext

PhonePC/2in1TabletTVWearable

type FormExtensionContext = \_FormExtensionContext.default

[FormExtensionAbility](js-apis-app-form-formextensionability.md)组件上下文，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_FormExtensionContext.default](js-apis-inner-application-formextensioncontext.md) | FormExtensionAbility组件上下文。 |

## VpnExtensionContext11+

PhonePC/2in1TabletTVWearable

type VpnExtensionContext = \_VpnExtensionContext.default

[VpnExtensionAbility](js-apis-vpnextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_VpnExtensionContext.default](js-apis-inner-application-vpnextensioncontext.md) | VpnExtensionAbility组件上下文。 |

## EventHub

PhonePC/2in1TabletTVWearable

type EventHub = \_EventHub.default

EventHub是系统提供的基于发布-订阅模式实现的事件通信机制。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_EventHub.default](js-apis-inner-application-eventhub.md) | 系统提供的基于发布-订阅模式实现的事件通信机制。 |

## PacMap

PhonePC/2in1TabletTVWearable

type PacMap = \_PacMap

存储基础数据类型的容器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_PacMap](js-apis-inner-ability-dataabilityhelper.md#pacmap) | 存储基础数据类型的容器。 |

## AbilityResult

PhonePC/2in1TabletTVWearable

type AbilityResult = \_AbilityResult

定义Ability被拉起并退出后返回的结果码和数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityResult](js-apis-inner-ability-abilityresult.md) | 定义Ability被拉起并退出后返回的结果码和数据。 |

## AbilityStartCallback11+

PhonePC/2in1TabletTVWearable

type AbilityStartCallback = \_AbilityStartCallback

定义了拉起UIExtensionAbility的回调结果，通常作为[UIAbilityContext.startAbilityByType](js-apis-inner-application-uiabilitycontext.md#startabilitybytype11)/[UIExtensionContext.startAbilityByType](js-apis-app-ability-uiextensioncontentsession.md#startabilitybytype11)的入参传入。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStartCallback](js-apis-inner-application-abilitystartcallback.md) | 定义拉起UIExtensionAbility的回调结果。 |

## ConnectOptions

PhonePC/2in1TabletTVWearable

type ConnectOptions = \_ConnectOptions

在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ConnectOptions](js-apis-inner-ability-connectoptions.md) | 在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。 |

## UIExtensionContext10+

PhonePC/2in1TabletTVWearable

type UIExtensionContext = \_UIExtensionContext.default

[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIExtensionContext.default](js-apis-inner-application-uiextensioncontext.md) | UIExtensionAbility组件上下文。 |

## EmbeddableUIAbilityContext12+

PhonePC/2in1TabletTVWearable

type EmbeddableUIAbilityContext = \_EmbeddableUIAbilityContext.default

[EmbeddableUIAbility](js-apis-app-ability-embeddableuiability.md)组件上下文，继承自Context。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_EmbeddableUIAbilityContext.default](-apis-inner-application-embeddableuiabilitycontext.md) | EmbeddableUIAbility组件上下文。 |

## PhotoEditorExtensionContext12+

PhonePC/2in1TabletTV

type PhotoEditorExtensionContext = \_PhotoEditorExtensionContext.default

[PhotoEditorExtensionAbility](js-apis-app-ability-photoeditorextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AppExtension.PhotoEditorExtension

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_PhotoEditorExtensionContext.default](js-apis-app-ability-photoeditorextensioncontext.md) | PhotoEditorExtensionAbility组件上下文。 |

## UIServiceProxy14+

PhonePC/2in1TabletTVWearable

type UIServiceProxy = \_UIServiceProxy.default

UIServiceProxy提供了与UIServiceExtensionAbility服务端数据通信的能力。UIServiceExtensionAbility是一类特殊的ExtensionAbility组件，这类组件由系统提供，通常用于提供浮窗组件相关扩展能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIServiceProxy.default](js-apis-inner-application-uiserviceproxy.md) | 提供与UIServiceExtensionAbility服务端数据通信的能力。 |

## UIServiceExtensionConnectCallback14+

PhonePC/2in1TabletTVWearable

type UIServiceExtensionConnectCallback = \_UIServiceExtensionConnectCallback.default

在连接指定的UIServiceExtensionAbility服务时作为入参，用于提供UIServiceExtensionAbility连接回调数据能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_UIServiceExtensionConnectCallback.default](nner-application-uiserviceextensionconnectcallback.md) | 提供UIServiceExtensionAbility连接回调数据能力。 |

## AppServiceExtensionContext20+

PhonePC/2in1TabletTVWearable

type AppServiceExtensionContext = \_AppServiceExtensionContext.default

[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AppServiceExtensionContext.default](-apis-inner-application-appserviceextensioncontext.md) | AppServiceExtensionAbility组件上下文。 |

## FormEditExtensionContext22+

PhonePC/2in1TabletTVWearable

type FormEditExtensionContext = \_FormEditExtensionContext.default

[FormEditExtensionAbility](js-apis-app-form-formeditextensionability.md)组件上下文，继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_FormEditExtensionContext.default](js-apis-inner-application-formeditextensioncontext.md) | FormEditExtensionAbility组件上下文。 |

## LiveFormExtensionContext22+

PhonePC/2in1TabletTVWearable

type LiveFormExtensionContext = \_LiveFormExtensionContext.default

[LiveFormExtensionAbility](js-apis-app-form-liveformextensionability.md)组件上下文，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_LiveFormExtensionContext.default](js-apis-application-liveformextensioncontext.md) | LiveFormExtensionAbility组件上下文。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. let uiAbilityContext: common.UIAbilityContext;
4. let abilityStageContext: common.AbilityStageContext;
5. let applicationContext: common.ApplicationContext;
6. let baseContext: common.BaseContext;
7. let context: common.Context;
8. let uiExtensionContext: common.UIExtensionContext;
9. let extensionContext: common.ExtensionContext;
10. let formExtensionContext: common.FormExtensionContext;
11. let vpnExtensionContext: common.VpnExtensionContext;
12. let eventHub: common.EventHub;
13. let pacMap: common.PacMap;
14. let abilityResult: common.AbilityResult;
15. let abilityStartCallback: common.AbilityStartCallback;
16. let connectOptions: common.ConnectOptions;
17. let embeddableUIAbilityContext: common.EmbeddableUIAbilityContext;
18. let photoEditorExtensionContext: common.PhotoEditorExtensionContext;
19. let uiServiceProxy : common.UIServiceProxy;
20. let uiServiceExtensionConnectCallback : common.UIServiceExtensionConnectCallback;
21. let appServiceExtensionContext : common.AppServiceExtensionContext;
22. let formEditExtensionContext : common.FormEditExtensionContext;
23. let liveFormExtensionContext : common.LiveFormExtensionContext;
```
