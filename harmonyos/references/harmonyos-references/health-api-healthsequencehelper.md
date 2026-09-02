---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthsequencehelper
title: healthSequenceHelper (健康记录类型常量)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthSequenceHelper (健康记录类型常量)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3ec346ec8f00afd72a076c735e8bcf627512ec7e4cc8c6918b9504de03872914
---

本模块提供健康记录数据类型常量及数据模型。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { healthStore } from '@kit.HealthServiceKit';
```

**说明** 

此模块为healthStore子模块，需通过healthStore.healthSequenceHelper方式使用。

## sleepRecord

夜间睡眠数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](health-api-healthstore.md#datatype) | 夜间睡眠数据类型。 |

### Model

type Model = healthModels.SleepRecord

夜间睡眠健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.SleepRecord](health-api-healthmodels.md#sleeprecord) | 夜间睡眠健康记录数据模型。 |

### Fields

type Fields = healthFields.Sleep

夜间睡眠健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.Sleep](health-api-healthfields.md#sleep) | 夜间睡眠健康记录数据字段列表。 |

### DetailFields

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepDetail](health-api-healthfields.md#sleepdetail) | 睡眠详情数据字段列表。 |

## sleepNapRecord

零星小睡数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](health-api-healthstore.md#datatype) | 零星小睡数据类型。 |

### Model

type Model = healthModels.SleepNapRecord

零星小睡健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.SleepNapRecord](health-api-healthmodels.md#sleepnaprecord) | 零星小睡健康记录数据模型。 |

### Fields

type Fields = healthFields.SleepNap

零星小睡健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepNap](health-api-healthfields.md#sleepnap) | 零星小睡健康记录数据字段列表。 |

### DetailFields

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SleepDetail](health-api-healthfields.md#sleepdetail) | 睡眠详情数据字段列表。 |

## menstrualCycle

生理周期数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](health-api-healthstore.md#datatype) | 生理周期数据类型。 |

### Model

type Model = healthModels.MenstrualCycle

生理周期健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.MenstrualCycle](health-api-healthmodels.md#menstrualcycle) | 生理周期健康记录数据模型。 |

### Fields

type Fields = healthFields.MenstrualCycle

生理周期健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.MenstrualCycle](health-api-healthfields.md#menstrualcycle) | 生理周期健康记录数据字段列表。 |

### DetailFields

type DetailFields = healthFields.MenstrualCycleDetail

生理周期详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.MenstrualCycleDetail](health-api-healthfields.md#menstrualcycledetail) | 生理周期详情数据字段列表。 |
