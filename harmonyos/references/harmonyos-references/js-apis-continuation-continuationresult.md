---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult
title: ContinuationResult
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > continuation > ContinuationResult
category: harmonyos-references
scraped_at: 2026-09-02T15:00:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:40e67be64f5bcaa6d8c8c291a241f5addea2a192bad5908ac4da28238522f9f1
---

流转管理入口返回的设备信息。

**说明** 

本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](js-apis-distributeddevicemanager.md)替代。

本模块接口仅可在Stage模型下使用。

## ContinuationResult(deprecated)

ContinuationManager的[on](js-apis-continuation-continuationmanager.md#continuationmanagerondeviceselecteddeprecated)接口返回此对象表示流转管理入口返回的设备信息。

**说明** 

从API version 22开始废弃，建议使用[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示设备标识。 |
| type | string | 否 | 否 | 表示设备类型。 |
| name | string | 否 | 否 | 表示设备名称。 |
