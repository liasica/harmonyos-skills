---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthservice
title: healthService (运动健康场景化服务)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > healthService (运动健康场景化服务)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:18+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7dd655c990334be360cd583331be0d370683612787f5b6e69138490225b9acba
---

本模块提供运动健康场景化服务。

**说明** 

针对系统能力SystemCapability.Health.HealthService，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { healthService } from '@kit.HealthServiceKit';
```

## SampleEvent

联动控制事件。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 事件ID。 |
| eventLevel | number | 否 | 否 | 事件等级。  取值参考：[0, 255] |
| eventData | string | 否 | 否 | 事件携带的信息。 |
| srcPkgName | string | 否 | 是 | 事件发送源包名，若未填写，默认为空。 |
| destPkgName | string | 否 | 是 | 事件发送目标包名，若未填写，默认为空。 |

## SampleReal

SampleReal<K extends Record<string, [healthStore.HealthValueType](health-api-healthstore.md#healthvaluetype)> = Record<string, [healthStore.HealthValueType](health-api-healthstore.md#healthvaluetype)>>

联动实时运动数据。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [healthStore.DataType](health-api-healthstore.md#datatype) | 否 | 否 | 实时融合数据类型。 |
| time | number | 否 | 否 | 实时融合数据产生时间，Unix时间戳，单位：ms。 |
| fields | Pick<K, keyof K> | 否 | 否 | 实时融合数据字段。 |
| deviceUniqueId | string | 否 | 是 | 实时融合数据来源，若未填写，默认为空。 |
