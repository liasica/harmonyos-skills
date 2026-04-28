---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthsequencehelper
title: healthSequenceHelper(健康记录类型常量)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthSequenceHelper(健康记录类型常量)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f8bf41baf65bed332e429b1ea186d7cc9b2b33dd6972abcfd50a5c1ab8684e10
---

本模块提供健康记录数据类型常量及数据模型。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

说明

此模块为healthStore子模块，需通过healthStore.healthSequenceHelper方式使用。

## sleepRecord

PhoneTabletWearable

夜间睡眠数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](health-api-healthstore.md#datatype) | 夜间睡眠数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.SleepRecord

夜间睡眠健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.SleepRecord](health-api-healthmodels.md#sleeprecord) | 夜间睡眠健康记录数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.Sleep

夜间睡眠健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.Sleep](health-api-healthfields.md#sleep) | 夜间睡眠健康记录数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepDetail](health-api-healthfields.md#sleepdetail) | 睡眠详情数据字段列表。 |

## sleepNapRecord

PhoneTabletWearable

零星小睡数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](health-api-healthstore.md#datatype) | 零星小睡数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.SleepNapRecord

零星小睡健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.SleepNapRecord](health-api-healthmodels.md#sleepnaprecord) | 零星小睡健康记录数据模型。 |

### Fields

PhoneTabletWearable

type Fields = healthFields.SleepNap

零星小睡健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepNap](health-api-healthfields.md#sleepnap) | 零星小睡健康记录数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepDetail](health-api-healthfields.md#sleepdetail) | 睡眠详情数据字段列表。 |
