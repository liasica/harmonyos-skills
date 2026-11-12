---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels
title: healthModels (运动健康数据模型)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthModels (运动健康数据模型)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:19+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c34c0bd2beab59405420e761fa9548bea75d53097991d75a2e2533f8722ba8cd
---

本模块提供运动健康数据模型。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { healthStore } from '@kit.HealthServiceKit';
```

**说明** 

此模块为healthStore子模块，需通过healthStore.healthModels方式使用。

## Adventures

type Adventures = healthStore.ExerciseSequence<healthFields.AdventuresSummary, healthFields.AdventuresDetail>

户外探险锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.AdventuresSummary](health-api-healthfields.md#adventuressummary), [healthFields.AdventuresDetail](health-api-healthfields.md#adventuresdetail)> | 户外探险锻炼记录数据模型。 |

## Basketball

type Basketball = healthStore.ExerciseSequence<healthFields.BasketballSummary, healthFields.BasketballDetail>

篮球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.BasketballSummary](health-api-healthfields.md#basketballsummary), [healthFields.BasketballDetail](health-api-healthfields.md#basketballdetail)> | 篮球锻炼记录数据模型。 |

## Biathlon

type Biathlon = healthStore.ExerciseSequence<healthFields.BiathlonSummary, healthFields.BiathlonDetail>

冬季两项锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.BiathlonSummary](health-api-healthfields.md#biathlonsummary), [healthFields.BiathlonDetail](health-api-healthfields.md#biathlondetail)> | 冬季两项锻炼记录数据模型。 |

## BloodOxygenSaturation

type BloodOxygenSaturation = healthStore.SamplePoint<healthFields.BloodOxygenSaturation>

血氧采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.BloodOxygenSaturation](health-api-healthfields.md#bloodoxygensaturation)> | 血氧采样数据模型。 |

## BloodOxygenSaturationAggregateRequest

type BloodOxygenSaturationAggregateRequest = healthStore.AggregateRequest<healthFields.BloodOxygenSaturationAggregation>

血氧采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](health-api-healthstore.md#aggregaterequest)<[healthFields.BloodOxygenSaturationAggregation](health-api-healthfields.md#bloodoxygensaturationaggregation)> | 血氧采样数据聚合统计请求模型。 |

## BloodOxygenSaturationAggregateResult

type BloodOxygenSaturationAggregateResult = healthStore.AggregateResult<healthFields.BloodOxygenSaturationAggregation>

血氧聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](health-api-healthstore.md#aggregateresult)<[healthFields.BloodOxygenSaturationAggregation](health-api-healthfields.md#bloodoxygensaturationaggregation)> | 血氧聚合结果数据模型。 |

## BloodPressure

type BloodPressure = healthStore.SamplePoint<healthFields.BloodPressure>

血压采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.BloodPressure](health-api-healthfields.md#bloodpressure)> | 血压采样数据模型。 |

## Bmx

type Bmx = Cycling

BMX自行车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.Cycling](health-api-healthmodels.md#cycling) | BMX自行车锻炼记录数据模型。 |

## BodyTemperature

type BodyTemperature = healthStore.SamplePoint<healthFields.BodyTemperature>

体温采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.BodyTemperature](health-api-healthfields.md#bodytemperature)> | 体温采样数据模型。 |

## BodyTemperatureAggregateRequest

type BodyTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.BodyTemperatureAggregation>

体温采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](health-api-healthstore.md#aggregaterequest)<[healthFields.BodyTemperatureAggregation](health-api-healthfields.md#bodytemperatureaggregation)> | 体温采样数据聚合统计请求模型。 |

## BodyTemperatureAggregateResult

type BodyTemperatureAggregateResult = healthStore.AggregateResult<healthFields.BodyTemperatureAggregation>

体温聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](health-api-healthstore.md#aggregateresult)<[healthFields.BodyTemperatureAggregation](health-api-healthfields.md#bodytemperatureaggregation)> | 体温聚合结果数据模型。 |

## BreathHoldingTest

type BreathHoldingTest = healthStore.ExerciseSequence<healthFields.BreathHoldingTestSummary, healthFields.BreathHoldingTestDetail>

闭气测试锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.BreathHoldingTestSummary](health-api-healthfields.md#breathholdingtestsummary), [healthFields.BreathHoldingTestDetail](health-api-healthfields.md#breathholdingtestdetail)> | 闭气测试锻炼记录数据模型。 |

## BreathHoldingTrain

type BreathHoldingTrain = healthStore.ExerciseSequence<healthFields.BreathHoldingTrainSummary, healthFields.BreathHoldingTrainDetail>

闭气训练锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.BreathHoldingTrainSummary](health-api-healthfields.md#breathholdingtrainsummary), [healthFields.BreathHoldingTrainDetail](health-api-healthfields.md#breathholdingtraindetail)> | 闭气训练锻炼记录数据模型。 |

## Cycling

type Cycling = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

户外骑行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.CyclingSummary](health-api-healthfields.md#cyclingsummary), [healthFields.CyclingDetail](health-api-healthfields.md#cyclingdetail)> | 户外骑行锻炼记录数据模型。 |

## DailyActivities

type DailyActivities = healthStore.SamplePoint<healthFields.DailyActivities>

日常活动采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.DailyActivities](health-api-healthfields.md#dailyactivities)> | 日常活动采样数据模型。 |

## DailyActivitiesAggregateRequest

type DailyActivitiesAggregateRequest = healthStore.AggregateRequest<healthFields.DailyActivitiesAggregation>

日常活动采样数据聚合统计请求模型。

**元服务API**：从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](health-api-healthstore.md#aggregaterequest)<[healthFields.DailyActivitiesAggregation](health-api-healthfields.md#dailyactivitiesaggregation)> | 日常活动采样数据聚合统计请求模型。 |

## DailyActivitiesAggregateResult

type DailyActivitiesAggregateResult = healthStore.AggregateResult<healthFields.DailyActivitiesAggregation>

日常活动聚合结果数据模型。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](health-api-healthstore.md#aggregateresult)<[healthFields.DailyActivitiesAggregation](health-api-healthfields.md#dailyactivitiesaggregation)> | 日常活动聚合结果数据模型。 |

## Diving

type Diving = healthStore.ExerciseSequence<healthFields.DivingSummary, healthFields.DivingDetail>

自由潜水锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.DivingSummary](health-api-healthfields.md#divingsummary), [healthFields.DivingDetail](health-api-healthfields.md#divingdetail)> | 自由潜水锻炼记录数据模型。 |

## Elliptical

type Elliptical = healthStore.ExerciseSequence<healthFields.EllipticalSummary, healthFields.EllipticalDetail>

椭圆机锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.EllipticalSummary](health-api-healthfields.md#ellipticalsummary), [healthFields.EllipticalDetail](health-api-healthfields.md#ellipticaldetail)> | 椭圆机锻炼记录数据模型。 |

## Emotion

type Emotion = healthStore.SamplePoint<healthFields.Emotion>

情绪采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.Emotion](health-api-healthfields.md#emotion)> | 情绪采样数据模型。 |

## GolfCourseModel

type GolfCourseModel = healthStore.ExerciseSequence<healthFields.GolfCourseModelSummary, healthFields.GolfCourseModelDetail>

高尔夫场地模式锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.GolfCourseModelSummary](health-api-healthfields.md#golfcoursemodelsummary), [healthFields.GolfCourseModelDetail](health-api-healthfields.md#golfcoursemodeldetail)> | 高尔夫场地模式锻炼记录数据模型。 |

## GolfPractice

type GolfPractice = healthStore.ExerciseSequence<healthFields.GolfPracticeSummary, healthFields.GolfPracticeDetail>

高尔夫练习场模式锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.GolfPracticeSummary](health-api-healthfields.md#golfpracticesummary), [healthFields.GolfPracticeDetail](health-api-healthfields.md#golfpracticedetail)> | 高尔夫练习场模式锻炼记录数据模型。 |

## HeartRate

type HeartRate = healthStore.SamplePoint<healthFields.HeartRate>

动态心率采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.HeartRate](health-api-healthfields.md#heartrate)> | 动态心率采样数据模型。 |

## HeartRateAggregateRequest

type HeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.HeartRateAggregation>

动态心率采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](health-api-healthstore.md#aggregaterequest)<[healthFields.HeartRateAggregation](health-api-healthfields.md#heartrateaggregation)> | 动态心率采样数据聚合统计请求模型。 |

## HeartRateAggregateResult

type HeartRateAggregateResult = healthStore.AggregateResult<healthFields.HeartRateAggregation>

动态心率聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](health-api-healthstore.md#aggregateresult)<[healthFields.HeartRateAggregation](health-api-healthfields.md#heartrateaggregation)> | 动态心率聚合结果数据模型。 |

## HeartRateVariability

type HeartRateVariability = healthStore.SamplePoint<healthFields.HeartRateVariability>

心率变异性采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.HeartRateVariability](health-api-healthfields.md#heartratevariability)> | 心率变异性采样数据模型。 |

## Height

type Height = healthStore.SamplePoint<healthFields.Height>

身高采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.Height](health-api-healthfields.md#height)> | 身高采样数据模型。 |

## Hiking

type Hiking = Walking

徒步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.Walking](health-api-healthmodels.md#walking) | 徒步锻炼记录数据模型。 |

## IndoorCycling

type IndoorCycling = Cycling

室内单车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.Cycling](health-api-healthmodels.md#cycling) | 室内单车锻炼记录数据模型。 |

## IndoorRunning

type IndoorRunning = Running

室内跑步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.Running](health-api-healthmodels.md#running) | 室内跑步锻炼记录数据模型。 |

## IndoorWalking

type IndoorWalking = Walking

室内步行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.Walking](health-api-healthmodels.md#walking) | 室内步行锻炼记录数据模型。 |

## JumpingRope

type JumpingRope = healthStore.ExerciseSequence<healthFields.JumpingRopeSummary, healthFields.JumpingRopeDetail>

跳绳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.JumpingRopeSummary](health-api-healthfields.md#jumpingropesummary), [healthFields.JumpingRopeDetail](health-api-healthfields.md#jumpingropedetail)> | 跳绳锻炼记录数据模型。 |

## MenstrualCycle

type MenstrualCycle = healthStore.HealthSequence<healthFields.MenstrualCycle, healthFields.MenstrualCycleDetail>

生理周期健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.HealthSequence](health-api-healthstore.md#healthsequence)<[healthFields.MenstrualCycle](health-api-healthfields.md#menstrualcycle), [healthFields.MenstrualCycleDetail](health-api-healthfields.md#menstrualcycledetail)> | 生理周期健康记录数据模型。 |

## MountainHike

type MountainHike = healthStore.ExerciseSequence<healthFields.MountainHikeSummary, healthFields.MountainHikeDetail>

登山锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.MountainHikeSummary](health-api-healthfields.md#mountainhikesummary), [healthFields.MountainHikeDetail](health-api-healthfields.md#mountainhikedetail)> | 登山锻炼记录数据模型。 |

## OpenWaterSwim

type OpenWaterSwim = healthStore.ExerciseSequence<healthFields.OpenWaterSwimSummary, healthFields.OpenWaterSwimDetail>

开放水域游泳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.OpenWaterSwimSummary](health-api-healthfields.md#openwaterswimsummary), [healthFields.OpenWaterSwimDetail](health-api-healthfields.md#openwaterswimdetail)> | 开放水域游泳锻炼记录数据模型。 |

## PoolSwim

type PoolSwim = healthStore.ExerciseSequence<healthFields.PoolSwimSummary, healthFields.PoolSwimDetail>

泳池游泳锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.PoolSwimSummary](health-api-healthfields.md#poolswimsummary), [healthFields.PoolSwimDetail](health-api-healthfields.md#poolswimdetail)> | 泳池游泳锻炼记录数据模型。 |

## RestingHeartRate

type RestingHeartRate = healthStore.SamplePoint<healthFields.RestingHeartRate>

静息心率采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.RestingHeartRate](health-api-healthfields.md#restingheartrate)> | 静息心率采样数据模型。 |

## RestingHeartRateAggregateRequest

type RestingHeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.RestingHeartRateAggregation>

静息心率采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](health-api-healthstore.md#aggregaterequest)<[healthFields.RestingHeartRateAggregation](health-api-healthfields.md#restingheartrateaggregation)> | 静息心率采样数据聚合统计请求模型。 |

## RestingHeartRateAggregateResult

type RestingHeartRateAggregateResult = healthStore.AggregateResult<healthFields.RestingHeartRateAggregation>

静息心率聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](health-api-healthstore.md#aggregateresult)<[healthFields.RestingHeartRateAggregation](health-api-healthfields.md#restingheartrateaggregation)> | 静息心率聚合结果数据模型。 |

## Rower

type Rower = healthStore.ExerciseSequence<healthFields.RowerSummary, healthFields.RowerDetail>

划船机锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.RowerSummary](health-api-healthfields.md#rowersummary), [healthFields.RowerDetail](health-api-healthfields.md#rowerdetail)> | 划船机锻炼记录数据模型。 |

## Rowing

type Rowing = healthStore.ExerciseSequence<healthFields.RowingSummary, healthFields.RowingDetail>

赛艇锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.RowingSummary](health-api-healthfields.md#rowingsummary), [healthFields.RowingDetail](health-api-healthfields.md#rowingdetail)> | 赛艇锻炼记录数据模型。 |

## Running

type Running = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>

户外跑步锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.RunningSummary](health-api-healthfields.md#runningsummary), [healthFields.RunningDetail](health-api-healthfields.md#runningdetail)> | 户外跑步锻炼记录数据模型。 |

## ScubaDiving

type ScubaDiving = healthStore.ExerciseSequence<healthFields.ScubaDivingSummary, healthFields.ScubaDivingDetail>

水肺潜水锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.ScubaDivingSummary](health-api-healthfields.md#scubadivingsummary), [healthFields.ScubaDivingDetail](health-api-healthfields.md#scubadivingdetail)> | 水肺潜水锻炼记录数据模型。 |

## Skiing

type Skiing = healthStore.ExerciseSequence<healthFields.SkiingSummary, healthFields.SkiingDetail>

滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.SkiingSummary](health-api-healthfields.md#skiingsummary), [healthFields.SkiingDetail](health-api-healthfields.md#skiingdetail)> | 滑雪锻炼记录数据模型。 |

## SkinTemperature

type SkinTemperature = healthStore.SamplePoint<healthFields.SkinTemperature>

皮肤体温采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.SkinTemperature](health-api-healthfields.md#skintemperature)> | 皮肤体温采样数据模型。 |

## SkinTemperatureAggregateRequest

type SkinTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.SkinTemperatureAggregation>

皮肤体温采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](health-api-healthstore.md#aggregaterequest)<[healthFields.SkinTemperatureAggregation](health-api-healthfields.md#skintemperatureaggregation)> | 皮肤体温采样数据聚合统计请求模型。 |

## SkinTemperatureAggregateResult

type SkinTemperatureAggregateResult = healthStore.AggregateResult<healthFields.SkinTemperatureAggregation>

皮肤体温聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](health-api-healthstore.md#aggregateresult)<[healthFields.SkinTemperatureAggregation](health-api-healthfields.md#skintemperatureaggregation)> | 皮肤体温聚合结果数据模型。 |

## Sled

type Sled = healthStore.ExerciseSequence<healthFields.SledSummary, healthFields.SledDetail>

滑雪橇锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.SledSummary](health-api-healthfields.md#sledsummary), [healthFields.SledDetail](health-api-healthfields.md#sleddetail)> | 滑雪橇锻炼记录数据模型。 |

## SleepNapRecord

type SleepNapRecord = healthStore.HealthSequence<healthFields.SleepNap, healthFields.SleepDetail>

零星小睡健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.HealthSequence](health-api-healthstore.md#healthsequence)<[healthFields.SleepNap](health-api-healthfields.md#sleepnap), [healthFields.SleepDetail](health-api-healthfields.md#sleepdetail)> | 零星小睡健康记录数据模型。 |

## SleepRecord

type SleepRecord = healthStore.HealthSequence<healthFields.Sleep, healthFields.SleepDetail>

夜间睡眠健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.HealthSequence](health-api-healthstore.md#healthsequence)<[healthFields.Sleep](health-api-healthfields.md#sleep), [healthFields.SleepDetail](health-api-healthfields.md#sleepdetail)> | 夜间睡眠健康记录数据模型。 |

## Snowboarding

type Snowboarding = healthStore.ExerciseSequence<healthFields.SnowboardingSummary, healthFields.SnowboardingDetail>

单板滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.SnowboardingSummary](health-api-healthfields.md#snowboardingsummary), [healthFields.SnowboardingDetail](health-api-healthfields.md#snowboardingdetail)> | 单板滑雪锻炼记录数据模型。 |

## Spinning

type Spinning = Cycling

动感单车锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.Cycling](health-api-healthmodels.md#cycling) | 动感单车锻炼记录数据模型。 |

## Sports

type Sports = healthStore.ExerciseSequence<healthFields.SportsSummary, healthFields.SportsDetail>

通用锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.SportsSummary](health-api-healthfields.md#sportssummary), [healthFields.SportsDetail](health-api-healthfields.md#sportsdetail)> | 通用锻炼记录数据模型。 |

## Stress

type Stress = healthStore.SamplePoint<healthFields.Stress>

压力采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.Stress](health-api-healthfields.md#stress)> | 压力采样数据模型。 |

## StressAggregateRequest

type StressAggregateRequest = healthStore.AggregateRequest<healthFields.StressAggregation>

压力采样数据聚合统计请求模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateRequest](health-api-healthstore.md#aggregaterequest)<[healthFields.StressAggregation](health-api-healthfields.md#stressaggregation)> | 压力采样数据聚合统计请求模型。 |

## StressAggregateResult

type StressAggregateResult = healthStore.AggregateResult<healthFields.StressAggregation>

压力聚合结果数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.AggregateResult](health-api-healthstore.md#aggregateresult)<[healthFields.StressAggregation](health-api-healthfields.md#stressaggregation)> | 压力聚合结果数据模型。 |

## TrailRunning

type TrailRunning = Running

越野跑锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthModels.Running](health-api-healthmodels.md#running) | 越野跑锻炼记录数据模型。 |

## Walking

type Walking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>

户外步行锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.WalkingSummary](health-api-healthfields.md#walkingsummary), [healthFields.WalkingDetail](health-api-healthfields.md#walkingdetail)> | 户外步行锻炼数据模型记录。 |

## Weight

type Weight = healthStore.SamplePoint<healthFields.Weight>

体重采样数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.SamplePoint](health-api-healthstore.md#samplepoint)<[healthFields.Weight](health-api-healthfields.md#weight)> | 体重采样数据模型。 |

## OutdoorSnowboard

type OutdoorSnowboard = healthStore.ExerciseSequence<healthFields.OutdoorSnowboardSummary, healthFields.OutdoorSnowboardDetail>

户外单板滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.OutdoorSnowboardSummary](health-api-healthfields.md#outdoorsnowboardsummary), [healthFields.OutdoorSnowboardgDetail](health-api-healthfields.md#outdoorsnowboarddetail)> | 户外单板滑雪锻炼记录数据模型。 |

## OutdoorSkiing

type OutdoorSkiing = healthStore.ExerciseSequence<healthFields.OutdoorSkiingSummary, healthFields.OutdoorSkiingDetail>

户外双板滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.OutdoorSkiingSummary](health-api-healthfields.md#outdoorskiingsummary), [healthFields.OutdoorSkiingDetail](health-api-healthfields.md#outdoorskiingdetail)> | 户外双板滑雪锻炼记录数据模型。 |

## IndoorSnowboard

type IndoorSnowboard = healthStore.ExerciseSequence<healthFields.IndoorSnowboardSummary, healthFields.IndoorSnowboardDetail>

室内单板滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.IndoorSnowboardSummary](health-api-healthfields.md#indoorsnowboardsummary), [healthFields.IndoorSnowboardDetail](health-api-healthfields.md#indoorsnowboarddetail)> | 室内单板滑雪锻炼记录数据模型。 |

## IndoorSkiing

type IndoorSkiing = healthStore.ExerciseSequence<healthFields.IndoorSkiingSummary, healthFields.IndoorSkiingDetail>

室内双板滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.IndoorSkiingSummary](health-api-healthfields.md#indoorskiingsummary), [healthFields.IndoorSkiingDetail](health-api-healthfields.md#indoorskiingdetail)> | 室内双板滑雪锻炼记录数据模型。 |

## CrossCountrySkiing

type CrossCountrySkiing = healthStore.ExerciseSequence<healthFields.CrossCountrySkiingSummary, healthFields.CrossCountrySkiingDetail>

越野滑雪锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.CrossCountrySkiingSummary](health-api-healthfields.md#crosscountryskiingsummary), [healthFields.CrossCountrySkiingDetail](health-api-healthfields.md#crosscountryskiingdetail)> | 越野滑雪锻炼记录数据模型。 |

## SkiMountaineering

type SkiMountaineering = healthStore.ExerciseSequence<healthFields.SkiMountaineeringSummary, healthFields.SkiMountaineeringDetail>

滑雪登山锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.SkiMountaineeringSummary](health-api-healthfields.md#skimountaineeringsummary), [healthFields.SkiMountaineeringDetail](health-api-healthfields.md#skimountaineeringdetail)> | 滑雪登山锻炼记录数据模型。 |

## Padel

type Padel = healthStore.ExerciseSequence<healthFields.PadelSummary, healthFields.PadelDetail>

笼式网球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.PadelSummary](health-api-healthfields.md#padelsummary), [healthFields.PadelDetail](health-api-healthfields.md#padeldetail)> | 笼式网球锻炼记录数据模型。 |

## Pilates

type Pilates = healthStore.ExerciseSequence<healthFields.PilatesSummary, healthFields.PilatesDetail>

普拉提锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.PilatesSummary](health-api-healthfields.md#pilatessummary), [healthFields.PilatesDetail](health-api-healthfields.md#pilatesdetail)> | 普拉提锻炼记录数据模型。 |

## FreeTraining

type FreeTraining = healthStore.ExerciseSequence<healthFields.FreeTrainingSummary, healthFields.FreeTrainingDetail>

自由训练锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.FreeTrainingSummary](health-api-healthfields.md#freetrainingsummary), [healthFields.FreeTrainingDetail](health-api-healthfields.md#freetrainingdetail)> | 自由训练锻炼记录数据模型。 |

## StrengthTraining

type StrengthTraining = healthStore.ExerciseSequence<healthFields.StrengthTrainingSummary, healthFields.StrengthTrainingDetail>

力量训练锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | **说明** |
| --- | --- |
| [healthStore.ExerciseSequence](health-api-healthstore.md#exercisesequence)<[healthFields.StrengthTrainingSummary](health-api-healthfields.md#strengthtrainingsummary), [healthFields.StrengthTrainingDetail](health-api-healthfields.md#strengthtrainingdetail)> | 力量训练锻炼记录数据模型。 |
