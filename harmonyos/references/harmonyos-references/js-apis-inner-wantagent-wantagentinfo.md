---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-wantagentinfo
title: WantAgentInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > wantAgent > WantAgentInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fe489f80bea6847d6b9c71a8570a11dbad730eae731da4fa8bd09ef0a3055396
---

WantAgentInfo用于定义触发WantAgent所需要的信息，可作为[getWantAgent](js-apis-app-ability-wantagent.md#wantagentgetwantagent)的入参创建指定的WantAgent对象。适用于需要延迟执行Ability启动、发送公共事件等场景，支持自定义请求码和动作执行属性，帮助开发者灵活控制WantAgent的行为。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { wantAgent as abilityWantAgent } from '@kit.AbilityKit';
```

## WantAgentInfo

定义触发WantAgent所需要的信息，可以作为[getWantAgent](js-apis-app-ability-wantagent.md#wantagentgetwantagent)的入参创建指定的WantAgent对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wants | Array<[Want](js-apis-app-ability-want.md)> | 否 | 否 | wants数组为预留能力，当前只支持一个want。传入多个时只取wants数组的第一个成员。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| operationType(deprecated) | [wantAgent.OperationType](js-apis-wantagent.md#operationtype) | 否 | 是 | 操作类型。不设置时无默认操作类型。  从 API version 7开始支持，从API version 11开始废弃。建议使用actionType11+替代。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| actionType11+ | [abilityWantAgent.OperationType](js-apis-app-ability-wantagent.md#operationtype) | 否 | 是 | 动作类型。不设置时无默认动作类型。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| requestCode | number | 否 | 否 | 开发者自定义的请求码，用于标识将被执行的动作。从API version 7开始支持。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| wantAgentFlags(deprecated) | Array<[wantAgent.WantAgentFlags](js-apis-wantagent.md#wantagentflags)> | 否 | 是 | 动作执行属性。不设置时无执行属性。  从API version 7 开始支持，从API version 11 开始废弃，建议使用actionFlags11+替代。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| actionFlags11+ | Array<[abilityWantAgent.WantAgentFlags](js-apis-app-ability-wantagent.md#wantagentflags)> | 否 | 是 | 动作执行属性。不设置时无执行属性。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| extraInfo | { [key: string]: any } | 否 | 是 | 额外数据，用于传递自定义扩展信息。参数为键值对对象，key为字符串类型的键名，value为任意类型的值。建议优先使用类型安全的extraInfos属性替代本属性。设置extraInfos属性后，本属性将不再生效。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| extraInfos11+ | Record<string, Object> | 否 | 是 | 额外数据，用于传递自定义键值对信息，类型安全。推荐使用该属性替代extraInfo。当需要在触发WantAgent时携带额外的自定义数据时传入此参数，不传入时默认为null，不会携带额外数据。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
