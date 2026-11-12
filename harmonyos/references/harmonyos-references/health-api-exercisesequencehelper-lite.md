---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exercisesequencehelper-lite
title: exerciseSequenceHelper (锻炼记录类型常量)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > exerciseSequenceHelper (锻炼记录类型常量)(Lite)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:19+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fb9f7e5ece7ea81f4854c6c590b1261649b663d062585d912932806967227d5f
---

本模块提供锻炼记录数据类型常量及数据模型。

**起始版本：** 6.1.1(24)

## 导入模块

```javascript
import healthStore from '@hms.health.store';
```

**说明** 

此模块为healthStore子模块，需通过healthStore.exerciseSequenceHelper方式使用。

## 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](health-api-healthstore-lite.md#datatype) | 锻炼记录数据类型。 |

## badminton

羽毛球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 羽毛球子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.BadmintonSummary

羽毛球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.BadmintonSummary](health-api-healthfields-lite.md#badmintonsummary) | 羽毛球统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.BadmintonDetail

羽毛球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.BadmintonDetail](health-api-healthfields-lite.md#badmintondetail) | 羽毛球详情数据字段列表。 |

## tennis

网球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 网球子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.TennisSummary

网球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.TennisSummary](health-api-healthfields-lite.md#tennissummary) | 网球统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.TennisDetail

网球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.TennisDetail](health-api-healthfields-lite.md#tennisdetail) | 网球详情数据字段列表。 |

## stairClimb

爬楼数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 爬楼子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.StairClimbSummary

爬楼统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StairClimbSummary](health-api-healthfields-lite.md#stairclimbsummary) | 爬楼统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.StairClimbDetail

爬楼详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StairClimbDetail](health-api-healthfields-lite.md#stairclimbdetail) | 爬楼详情数据字段列表。 |

## soccer

足球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 足球子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.SoccerSummary

足球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SoccerSummary](health-api-healthfields-lite.md#soccersummary) | 足球统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.SoccerDetail

足球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SoccerDetail](health-api-healthfields-lite.md#soccerdetail) | 足球详情数据字段列表。 |

## pickleBall

匹克球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 匹克球子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.PickleBallSummary

匹克球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PickleBallSummary](health-api-healthfields-lite.md#pickleballsummary) | 匹克球统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.PickleBallDetail

匹克球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PickleBallDetail](health-api-healthfields-lite.md#pickleballdetail) | 匹克球详情数据字段列表。 |

## strengthTraining

力量训练数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 力量训练子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.StrengthTrainingSummary

力量训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StrengthTrainingSummary](health-api-healthfields-lite.md#strengthtrainingsummary) | 力量训练统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.StrengthTrainingDetail

力量训练详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.StrengthTrainingDetail](health-api-healthfields-lite.md#strengthtrainingdetail) | 力量训练详情数据字段列表。 |

## OutdoorSnowboard

户外单板滑雪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外单板滑雪子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.OutdoorSnowboardSummary

户外单板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.OutdoorSnowboardSummary](health-api-healthfields-lite.md#outdoorsnowboardsummary) | 户外单板滑雪统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.OutdoorSnowboardDetail

户外单板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.OutdoorSnowboardDetail](health-api-healthfields-lite.md#outdoorsnowboarddetail) | 户外单板滑雪详情数据字段列表。 |

## OutdoorSkiing

户外双板滑雪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外双板滑雪子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.OutdoorSkiingSummary

户外双板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.OutdoorSkiingSummary](health-api-healthfields-lite.md#outdoorskiingsummary) | 户外双板滑雪统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.OutdoorSnowboardDetail

户外双板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.OutdoorSkiingDetail](health-api-healthfields-lite.md#outdoorskiingdetail) | 户外双板滑雪详情数据字段列表。 |

## IndoorSnowboard

室内单板滑雪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 室内单板滑雪子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.IndoorSnowboardSummary

室内单板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.IndoorSnowboardSummary](health-api-healthfields-lite.md#indoorsnowboardsummary) | 室内单板滑雪统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.IndoorSnowboardDetail

室内单板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.IndoorSnowboardDetail](health-api-healthfields-lite.md#indoorsnowboarddetail) | 室内单板滑雪详情数据字段列表。 |

## IndoorSkiing

室内双板滑雪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 室内双板滑雪子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.IndoorSkiingSummary

室内双板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.IndoorSkiingSummary](health-api-healthfields-lite.md#indoorskiingsummary) | 室内双板滑雪统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.IndoorSkiingDetail

室内双板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.IndoorSkiingDetail](health-api-healthfields-lite.md#indoorskiingdetail) | 室内双板滑雪详情数据字段列表。 |

## CrossCountrySkiing

越野滑雪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 越野滑雪子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.CrossCountrySkiingSummary

越野滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.CrossCountrySkiingSummary](health-api-healthfields-lite.md#crosscountryskiingsummary) | 越野滑雪统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.CrossCountrySkiingDetail

越野滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.CrossCountrySkiingDetail](health-api-healthfields-lite.md#crosscountryskiingdetail) | 越野滑雪详情数据字段列表。 |

## SkiMountaineering

滑雪登山数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 滑雪登山子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.SkiMountaineeringSummary

滑雪登山统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SkiMountaineeringSummary](health-api-healthfields-lite.md#skimountaineeringsummary) | 滑雪登山统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.SkiMountaineeringDetail

滑雪登山详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.SkiMountaineeringDetail](health-api-healthfields-lite.md#skimountaineeringdetail) | 滑雪登山详情数据字段列表。 |

## Padel

笼式网球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 笼式网球子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.PadelSummary

笼式网球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PadelSummary](health-api-healthfields-lite.md#padelsummary) | 笼式网球统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.PadelDetail

笼式网球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PadelDetail](health-api-healthfields-lite.md#padeldetail) | 笼式网球详情数据字段列表。 |

## Running

户外跑步数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外跑步子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.RunningSummary

户外跑步统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningSummary](health-api-healthfields-lite.md#runningsummary) | 户外跑步统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.RunningDetail

户外跑步详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningDetail](health-api-healthfields-lite.md#runningdetail) | 户外跑步详情数据字段列表。 |

## Pilates

普拉提数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 普拉提子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.PilatesSummary

普拉提统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PilatesSummary](health-api-healthfields-lite.md#pilatessummary) | 普拉提统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.PilatesDetail

普拉提详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.PilatesDetail](health-api-healthfields-lite.md#pilatesdetail) | 普拉提详情数据字段列表。 |

## FreeTraining

自由训练数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 自由训练子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.FreeTrainingSummary

自由训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.FreeTrainingSummary](health-api-healthfields-lite.md#freetrainingsummary) | 自由训练统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.FreeTrainingDetail

自由训练详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.FreeTrainingDetail](health-api-healthfields-lite.md#freetrainingdetail) | 自由训练详情数据字段列表。 |

## Cycling

户外骑行数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

### 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外骑行子数据类型。 |

### SummaryFields

type SummaryFields = healthFields.CyclingSummary

户外骑行统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingSummary](health-api-healthfields-lite.md#cyclingsummary) | 户外骑行统计数据字段列表。 |

### DetailFields

type DetailFields = healthFields.CyclingDetail

户外骑行详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingDetail](health-api-healthfields-lite.md#cyclingdetail) | 户外骑行详情数据字段列表。 |
