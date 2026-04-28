---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams
title: ContinuationExtraParams
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > continuation > ContinuationExtraParams
category: harmonyos-references
scraped_at: 2026-04-28T07:58:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:15646be3205f5226ac6dcda64a84e17d83ff993944059b2c30836d6c6783c930
---

流转管理入口中设备选择模块所需的过滤参数，可以作为[startContinuationDeviceManager](js-apis-continuation-continuationmanager.md#continuationmanagerstartcontinuationdevicemanagerdeprecated)的入参。

说明

本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](js-apis-distributeddevicemanager.md)替代。

本模块接口仅可在Stage模型下使用。

## ContinuationExtraParams(deprecated)

PhonePC/2in1TabletTV

表示流转管理入口中设备选择模块所需的过滤参数。

说明

从API version 22开始废弃，建议使用[devicebasicinfo](js-apis-distributeddevicemanager.md#devicebasicinfo)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceType | Array<string> | 否 | 是 | 表示设备类型。 |
| targetBundle | string | 否 | 是 | 表示目标Bundle名称。 |
| description | string | 否 | 是 | 表示设备过滤的描述。 |
| filter | any | 否 | 是 | 表示设备过滤的参数。 |
| continuationMode | [continuationManager.ContinuationMode](js-apis-continuation-continuationmanager.md#continuationmodedeprecated) | 否 | 是 | 表示协同的模式。 |
| authInfo | Record<string, Object> | 否 | 是 | 表示认证的信息。 |
