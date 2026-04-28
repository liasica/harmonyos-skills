---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-triggerinfo
title: TriggerInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > wantAgent > TriggerInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4bc5fb4b43c692de966f7ffda89f35cf0f8fc735323f8196dcc1270847f95970
---

作为[trigger](js-apis-app-ability-wantagent.md#wantagenttrigger)的入参定义触发WantAgent所需要的信息。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { wantAgent } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 表示传递的公共事件数据，仅当WantAgent实例的[OperationType](js-apis-app-ability-wantagent.md#operationtype)类型是'SEND\_COMMON\_EVENT'时有效。该字段与发布者使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish-1)发布公共事件时，传递[CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md#属性)公共事件数据中的code字段含义一致。 |
| want | [Want](js-apis-app-ability-want.md) | 否 | 是 | 对象间信息传递的载体，可以用于应用组件间的信息传递。 |
| permission | string | 否 | 是 | 表示公共事件订阅者的权限。仅当WantAgent实例的[OperationType](js-apis-app-ability-wantagent.md#operationtype)类型是'SEND\_COMMON\_EVENT'时，该字段生效。若权限为null，则接收方无需具备任何权限。 |
| extraInfo | { [key: string]: any } | 否 | 是 | 额外数据。 |
| extraInfos11+ | Record<string, Object> | 否 | 是 | 额外数据。推荐使用该属性替代extraInfo，设置该属性后，extraInfo不再生效。 |
