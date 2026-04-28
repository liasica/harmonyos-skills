---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exercisedequencehelper
title: exerciseSequenceHelper(锻炼记录类型常量)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > exerciseSequenceHelper(锻炼记录类型常量)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94190674a83edae5ebda45f1e41202864bebafdd9117831da6d43b4fdbe4b985
---

本模块提供锻炼记录数据类型常量及数据模型。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

说明

此模块为healthStore子模块，需通过healthStore.exerciseSequenceHelper方式使用。

## 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA\_TYPE | [healthStore.DataType](health-api-healthstore.md#datatype) | 锻炼记录数据类型。 |

## adventures

PhoneTabletWearable

户外探险数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外探险子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Adventures

户外探险锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Adventures](health-api-healthmodels.md#adventures) | 户外探险锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.AdventuresSummary

户外探险统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.AdventuresSummary](health-api-healthfields.md#adventuressummary) | 户外探险统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.AdventuresDetail

户外探险详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.AdventuresDetail](health-api-healthfields.md#adventuresdetail) | 户外探险详情数据字段列表。 |

## basketball

PhoneTabletWearable

篮球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 篮球子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Basketball

篮球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Basketball](health-api-healthmodels.md#basketball) | 篮球锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.BasketballSummary

篮球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BasketballSummary](health-api-healthfields.md#basketballsummary) | 篮球统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.BasketballDetail

篮球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BasketballDetail](health-api-healthfields.md#basketballdetail) | 篮球详情数据字段列表。 |

## biathlon

PhoneTabletWearable

冬季两项数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冬季两项子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Biathlon

冬季两项锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Biathlon](health-api-healthmodels.md#biathlon) | 冬季两项锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.BiathlonSummary

冬季两项统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BiathlonSummary](health-api-healthfields.md#biathlonsummary) | 冬季两项统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.BiathlonDetail

冬季两项详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BiathlonDetail](health-api-healthfields.md#biathlondetail) | 冬季两项详情数据字段列表。 |

## bmx

PhoneTabletWearable

BMX自行车数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | BMX自行车子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Bmx

BMX自行车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Bmx](health-api-healthmodels.md#bmx) | BMX自行车锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.CyclingSummary

BMX自行车统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingSummary](health-api-healthfields.md#cyclingsummary) | BMX自行车统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.CyclingDetail

BMX自行车详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingDetail](health-api-healthfields.md#cyclingdetail) | BMX自行车详情数据字段列表。 |

## breathHoldingTest

PhoneTabletWearable

闭气测试数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 闭气测试子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.BreathHoldingTest

闭气测试锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BreathHoldingTest](health-api-healthmodels.md#breathholdingtest) | 闭气测试锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.BreathHoldingTestSummary

闭气测试统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BreathHoldingTestSummary](health-api-healthfields.md#breathholdingtestsummary) | 闭气测试统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.BreathHoldingTestDetail

闭气测试详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BreathHoldingTestDetail](health-api-healthfields.md#breathholdingtestdetail) | 闭气测试详情数据字段列表。 |

## breathHoldingTrain

PhoneTabletWearable

闭气训练数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 闭气训练子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.BreathHoldingTrain

闭气训练锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.BreathHoldingTrain](health-api-healthmodels.md#breathholdingtrain) | 闭气训练锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.BreathHoldingTrainSummary

闭气训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BreathHoldingTrainSummary](health-api-healthfields.md#breathholdingtrainsummary) | 闭气训练统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.BreathHoldingTrainDetail

闭气训练详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.BreathHoldingTrainDetail](health-api-healthfields.md#breathholdingtraindetail) | 闭气训练详情数据字段列表。 |

## cycling

PhoneTabletWearable

户外骑行数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外骑行子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Cycling

户外骑行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Cycling](health-api-healthmodels.md#cycling) | 户外骑行锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.CyclingSummary

户外骑行统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingSummary](health-api-healthfields.md#cyclingsummary) | 户外骑行统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.CyclingDetail

户外骑行详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingDetail](health-api-healthfields.md#cyclingdetail) | 户外骑行详情数据字段列表。 |

## diving

PhoneTabletWearable

自由潜水数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 自由潜水子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Diving

自由潜水锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Diving](health-api-healthmodels.md#diving) | 自由潜水锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.DivingSummary

自由潜水统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.DivingSummary](health-api-healthfields.md#divingsummary) | 自由潜水统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.DivingDetail

自由潜水详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.DivingDetail](health-api-healthfields.md#divingdetail) | 自由潜水详情数据字段列表。 |

## elliptical

PhoneTabletWearable

椭圆机数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 椭圆机子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Elliptical

椭圆机锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Elliptical](health-api-healthmodels.md#elliptical) | 椭圆机锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.EllipticalSummary

椭圆机统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.EllipticalSummary](health-api-healthfields.md#ellipticalsummary) | 椭圆机统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.EllipticalDetail

椭圆机详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.EllipticalDetail](health-api-healthfields.md#ellipticaldetail) | 椭圆机详情数据字段列表。 |

## golfCourseModel

PhoneTabletWearable

高尔夫场地模式数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 高尔夫场地模式子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.GolfCourseModel

高尔夫场地模式锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.GolfCourseModel](health-api-healthmodels.md#golfcoursemodel) | 高尔夫场地模式锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.GolfCourseModelSummary

高尔夫场地模式统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.GolfCourseModelSummary](health-api-healthfields.md#golfcoursemodelsummary) | 高尔夫场地模式统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.GolfCourseModelDetail

高尔夫场地模式详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.GolfCourseModelDetail](health-api-healthfields.md#golfcoursemodeldetail) | 高尔夫场地模式详情数据字段列表。 |

## golfPractice

PhoneTabletWearable

高尔夫练习场模式数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 高尔夫练习场模式子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.GolfPractice

高尔夫练习场模式锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.GolfPractice](health-api-healthmodels.md#golfpractice) | 高尔夫练习场模式锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.GolfPracticeSummary

高尔夫练习场模式统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.GolfPracticeSummary](health-api-healthfields.md#golfpracticesummary) | 高尔夫练习场模式统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.GolfPracticeDetail

高尔夫练习场模式详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.GolfPracticeDetail](health-api-healthfields.md#golfpracticedetail) | 高尔夫练习场模式详情数据字段列表。 |

## hiking

PhoneTabletWearable

徒步数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 徒步子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Hiking

徒步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Hiking](health-api-healthmodels.md#hiking) | 徒步锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.WalkingSummary

徒步统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.WalkingSummary](health-api-healthfields.md#walkingsummary) | 徒步统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.WalkingDetail

徒步详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.WalkingDetail](health-api-healthfields.md#walkingdetail) | 徒步详情数据字段列表。 |

## indoorCycling

PhoneTabletWearable

室内骑行数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 室内骑行子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.IndoorCycling

室内骑行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.IndoorCycling](health-api-healthmodels.md#indoorcycling) | 室内骑行锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.CyclingSummary

室内骑行统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingSummary](health-api-healthfields.md#cyclingsummary) | 室内骑行统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.CyclingDetail

室内骑行详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingDetail](health-api-healthfields.md#cyclingdetail) | 室内骑行详情数据字段列表。 |

## indoorRunning

PhoneTabletWearable

室内跑步数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 室内跑步子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.IndoorRunning

室内跑步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.IndoorRunning](health-api-exercisedequencehelper.md#indoorrunning) | 室内跑步锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.RunningSummary

室内跑步统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningSummary](health-api-healthfields.md#runningsummary) | 室内跑步统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.RunningDetail

室内跑步详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningDetail](health-api-healthfields.md#runningdetail) | 室内跑步详情数据字段列表。 |

## indoorWalking

PhoneTabletWearable

室内步行数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 室内步行子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.IndoorWalking

室内步行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.IndoorWalking](health-api-healthmodels.md#indoorwalking) | 室内步行锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.WalkingSummary

室内步行统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.WalkingSummary](health-api-healthfields.md#walkingsummary) | 室内步行统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.WalkingDetail

室内步行详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.WalkingDetail](health-api-healthfields.md#walkingdetail) | 室内步行详情数据字段列表。 |

## jumpingRope

PhoneTabletWearable

跳绳数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跳绳子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.JumpingRope

跳绳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.JumpingRope](health-api-healthmodels.md#jumpingrope) | 跳绳锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.JumpingRopeSummary

跳绳统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.JumpingRopeSummary](health-api-healthfields.md#jumpingropesummary) | 跳绳统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.JumpingRopeDetail

跳绳详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.JumpingRopeDetail](health-api-healthfields.md#jumpingropedetail) | 跳绳详情数据字段列表。 |

## mountainHike

PhoneTabletWearable

登山数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 登山子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.MountainHike

登山锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.MountainHike](health-api-healthmodels.md#mountainhike) | 登山锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.MountainHikeSummary

登山统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.MountainHikeSummary](health-api-healthfields.md#mountainhikesummary) | 登山统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.MountainHikeDetail

登山详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.MountainHikeDetail](health-api-healthfields.md#mountainhikedetail) | 登山详情数据字段列表。 |

## openWaterSwim

PhoneTabletWearable

开放水域游泳数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 开放水域游泳子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.OpenWaterSwim

开放水域游泳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.OpenWaterSwim](health-api-healthmodels.md#openwaterswim) | 开放水域游泳锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.OpenWaterSwimSummary

开放水域游泳统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.OpenWaterSwimSummary](health-api-healthfields.md#openwaterswimsummary) | 开放水域游泳统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.OpenWaterSwimDetail

开放水域游泳详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.OpenWaterSwimDetail](health-api-healthfields.md#openwaterswimdetail) | 开放水域游泳详情数据字段列表。 |

## poolSwim

PhoneTabletWearable

泳池游泳数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 泳池游泳子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.PoolSwim

泳池游泳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.PoolSwim](health-api-healthmodels.md#poolswim) | 泳池游泳锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.PoolSwimSummary

泳池游泳统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.PoolSwimSummary](health-api-healthfields.md#poolswimsummary) | 泳池游泳统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.PoolSwimDetail

泳池游泳详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.PoolSwimDetail](health-api-healthfields.md#poolswimdetail) | 泳池游泳详情数据字段列表。 |

## rower

PhoneTabletWearable

划船机数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 划船机子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Rower

划船机锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Rower](health-api-healthmodels.md#rower) | 划船机锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.RowerSummary

划船机统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RowerSummary](health-api-healthfields.md#rowersummary) | 划船机统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.RowerDetail

划船机详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RowerDetail](health-api-healthfields.md#rowerdetail) | 划船机详情数据字段列表。 |

## rowing

PhoneTabletWearable

赛艇数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 赛艇子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Rowing

赛艇锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Rowing](health-api-healthmodels.md#rowing) | 赛艇锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.RowingSummary

赛艇统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RowingSummary](health-api-healthfields.md#rowingsummary) | 赛艇统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.RowingDetail

赛艇详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RowingDetail](health-api-healthfields.md#rowingdetail) | 赛艇详情数据字段列表。 |

## running

PhoneTabletWearable

户外跑步数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外跑步子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Running

户外跑步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Running](health-api-healthmodels.md#running) | 户外跑步锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.RunningSummary

户外跑步统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningSummary](health-api-healthfields.md#runningsummary) | 户外跑步统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.RunningDetail

户外跑步详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningDetail](health-api-healthfields.md#runningdetail) | 户外跑步详情数据字段列表。 |

## scubaDiving

PhoneTabletWearable

水肺潜水数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 水肺潜水子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.ScubaDiving

水肺潜水锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.ScubaDiving](health-api-healthmodels.md#scubadiving) | 水肺潜水锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.ScubaDivingSummary

水肺潜水统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.ScubaDivingSummary](health-api-healthfields.md#scubadivingsummary) | 水肺潜水统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.ScubaDivingDetail

水肺潜水详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.ScubaDivingDetail](health-api-healthfields.md#scubadivingdetail) | 水肺潜水详情数据字段列表。 |

## skiing

PhoneTabletWearable

滑雪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑雪子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Skiing

滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Skiing](health-api-healthmodels.md#skiing) | 滑雪锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.SkiingSummary

滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SkiingSummary](health-api-healthfields.md#skiingsummary) | 滑雪统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SkiingDetail

滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SkiingDetail](health-api-healthfields.md#skiingdetail) | 滑雪详情数据字段列表。 |

## sled

PhoneTabletWearable

滑雪橇数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑雪橇子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Sled

滑雪橇锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Sled](health-api-healthmodels.md#sled) | 滑雪橇锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.SledSummary

滑雪橇统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SledSummary](health-api-healthfields.md#sledsummary) | 滑雪橇统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SledDetail

滑雪橇详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SledDetail](health-api-healthfields.md#sleddetail) | 滑雪橇详情数据字段列表。 |

## snowboarding

PhoneTabletWearable

单板滑雪数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 单板滑雪子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Snowboarding

单板滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Snowboarding](health-api-healthmodels.md#snowboarding) | 单板滑雪锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.SnowboardingSummary

单板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SnowboardingSummary](health-api-healthfields.md#snowboardingsummary) | 单板滑雪统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SnowboardingDetail

单板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SnowboardingDetail](health-api-healthfields.md#snowboardingdetail) | 单板滑雪详情数据字段列表。 |

## spinning

PhoneTabletWearable

动感单车数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 动感单车子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Spinning

动感单车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Spinning](health-api-healthmodels.md#spinning) | 动感单车锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.CyclingSummary

动感单车统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingSummary](health-api-healthfields.md#cyclingsummary) | 动感单车统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.CyclingDetail

动感单车详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.CyclingDetail](health-api-healthfields.md#cyclingdetail) | 动感单车详情数据字段列表。 |

## sports

PhoneTabletWearable

其他运动数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| AEROBICS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 健美操 |
| AIR\_WALKER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 漫步机 |
| ARCHERY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 射箭 |
| BADMINTON | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 羽毛球 |
| BALLET | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 芭蕾舞 |
| BASEBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 棒球 |
| BEACH\_SOCCER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 沙滩足球 |
| BEACH\_VOLLEYBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 沙滩排球 |
| BELLY\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 肚皮舞 |
| BODY\_COMBAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 搏击操 |
| BOWLING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 保龄球 |
| BOXING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 拳击 |
| BUNGEE\_JUMPING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 蹦极 |
| CANOEING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 皮划艇 |
| CORE\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 核心训练 |
| CRICKET | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 板球 |
| CROSS\_COUNTRY\_SKIING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 越野滑雪 |
| CROSS\_FIT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | Cross fit |
| CURLING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冰壶 |
| DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 舞蹈 |
| DARTS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 飞镖 |
| DODGE\_BALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 躲避球 |
| DRAGON\_BOAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 龙舟 |
| DRIFTING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 漂流 |
| ESPORTS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 电子竞技 |
| FENCING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 击剑 |
| FISHING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 钓鱼 |
| FREE\_SPARRING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 自由搏击 |
| FREE\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 自由训练 |
| FRISBEE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 飞盘 |
| FUNCTIONAL\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 功能性训练 |
| GATEBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 门球 |
| HANDBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 手球 |
| HIIT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | HIIT |
| HOCKEY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 曲棍球 |
| HORSE\_RIDING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 骑马 |
| HULA\_HOOP | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 呼啦圈 |
| HUNTING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 对战游戏 |
| ICE\_HOCKEY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冰球 |
| JAZZ\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 爵士舞 |
| KARATE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 空手道 |
| KENDO | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 剑道 |
| KITE\_FLYING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 放风筝 |
| LATIN\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 拉丁舞 |
| MARTIAL\_ARTS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 武术 |
| MOTORBOAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 摩托艇 |
| OBSTACLE\_RACE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 障碍赛 |
| ORIENTEERING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 定向越野 |
| PADEL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 笼式网球 |
| PARACHUTE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跳伞 |
| PARALLEL\_BARS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 双杠 |
| PARKOUR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跑酷 |
| PHYSICAL\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 体能训练 |
| PILATES | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 普拉提 |
| PLAYGROUND\_RACE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 操场赛跑 |
| PLAZA\_DANCING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 广场舞 |
| POOL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 台球 |
| RACING\_CAR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 赛车 |
| ROCK\_CLIMBING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 攀岩 |
| ROLLER\_SKATING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 轮滑 |
| RUGBY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 橄榄球 |
| SAILBOAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 帆船 |
| SENSE\_SPORT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 体感运动 |
| SEPAKTAKRAW | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 藤球 |
| SHUTTLECOCK | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 毽球 |
| SINGLE\_BAR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 单杠 |
| SKATEBOARD | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑板 |
| SKATING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑冰 |
| SNOWMOBILE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 雪地摩托 |
| SOCCER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 足球 |
| SOFTBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 垒球 |
| SQUASH | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 壁球 |
| STAIR\_CLIMBING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 爬楼 |
| STEPPER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 踏步机 |
| STREET\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 街舞 |
| STRENGTH\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 力量训练 |
| SUP | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 桨板冲浪 |
| SURFING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冲浪 |
| SWINGING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 秋千 |
| TABLE\_TENNIS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 乒乓球 |
| TAEKWONDO | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跆拳道 |
| TAI\_CHI | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 太极拳 |
| TENNIS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 网球 |
| TRIATHLON | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 铁人三项 |
| TUG\_OF\_WAR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 拔河 |
| VOLLEYBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 排球 |
| YOGA | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 瑜伽 |

### Model

PhoneTabletWearable

type Model = healthModels.Sports

通用锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Sports](health-api-healthmodels.md#sports) | 通用锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.SportsSummary

通用统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SportsSummary](health-api-healthfields.md#sportssummary) | 通用统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.SportsDetail

通用详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.SportsDetail](health-api-healthfields.md#sportsdetail) | 通用详情数据字段列表。 |

## trailRunning

PhoneTabletWearable

越野跑数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 越野跑子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.TrailRunning

越野跑锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.TrailRunning](health-api-healthmodels.md#trailrunning) | 越野跑锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.RunningSummary

越野跑统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningSummary](health-api-healthfields.md#runningsummary) | 越野跑统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.RunningDetail

越野跑详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.RunningDetail](health-api-healthfields.md#runningdetail) | 越野跑详情数据字段列表。 |

## walking

PhoneTabletWearable

户外步行数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

### 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE\_TYPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外步行子数据类型。 |

### Model

PhoneTabletWearable

type Model = healthModels.Walking

户外步行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthModels.Walking](health-api-healthmodels.md#walking) | 户外步行锻炼记录数据模型。 |

### SummaryFields

PhoneTabletWearable

type SummaryFields = healthFields.WalkingSummary

户外步行统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.WalkingSummary](health-api-healthfields.md#walkingsummary) | 户外步行统计数据字段列表。 |

### DetailFields

PhoneTabletWearable

type DetailFields = healthFields.WalkingDetail

户外步行详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| [healthFields.WalkingDetail](health-api-healthfields.md#walkingdetail) | 户外步行详情数据字段列表。 |
