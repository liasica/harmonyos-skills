---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields
title: healthFields(运动健康数据字段)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthFields(运动健康数据字段)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5f94d612f3b2758004536d782f6eb8b44852c5f67afb74536dcb6ed28aef9ecb
---

本模块提供运动健康数据字段列表。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

说明

此模块为healthStore子模块，需通过healthStore.healthFields方式使用。

## AdventuresDetail

PhoneTabletWearable

户外探险详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| markPoint | [MarkPoint](health-api-healthfields.md#markpoint)[] | 否 | 是 | 标记点采样详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |

## AdventuresSummary

PhoneTabletWearable

户外探险统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 探险航点里程统计。 |
| step | [StepSummary](health-api-healthfields.md#stepsummary) | 否 | 是 | 步数统计，若未填写，默认为空。 |
| cadence | [CadenceSummary](health-api-healthfields.md#cadencesummary) | 否 | 是 | 步频统计，若未填写，默认为空。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |

## Altitude

PhoneTabletWearable

海拔详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| altitude | number | 否 | 否 | 海拔。  单位：米 |

## AltitudeSummary

PhoneTabletWearable

海拔统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| max | number | 否 | 否 | 最大值。  单位：米 |
| min | number | 否 | 否 | 最小值。  单位：米 |
| avg | number | 否 | 是 | 平均值，若未填写，默认为空。  单位：米 |
| totalAscent | number | 否 | 是 | 累计爬升，若未填写，默认为空。  单位：米  取值范围：[0, ∞) |
| totalDescent | number | 否 | 是 | 累计下降，若未填写，默认为空。  单位：米  取值范围：[0, ∞) |

## BasketballDetail

PhoneTabletWearable

篮球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| jump | [Jump](health-api-healthfields.md#jump)[] | 否 | 是 | 跳跃详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |

## BasketballFeature

PhoneTabletWearable

篮球特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| overallScore | number | 否 | 否 | 综合评分。 |
| burstScore | number | 否 | 是 | 爆发力得分，若未填写，默认为空。 |
| jumpScore | number | 否 | 是 | 弹跳滞空得分，若未填写，默认为空。 |
| runScore | number | 否 | 是 | 跑动得分，若未填写，默认为空。 |
| breakthroughScore | number | 否 | 是 | 突破移动得分，若未填写，默认为空。 |
| sportIntensityScore | number | 否 | 是 | 运动强度得分，若未填写，默认为空。 |

## BasketballSummary

PhoneTabletWearable

篮球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| basketballFeature | [BasketballFeature](health-api-healthfields.md#basketballfeature) | 否 | 否 | 篮球特征数据。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| jump | [JumpSummary](health-api-healthfields.md#jumpsummary) | 否 | 否 | 跳跃统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## BiathlonDetail

PhoneTabletWearable

冬季两项详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |

## BiathlonSummary

PhoneTabletWearable

冬季两项统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## BloodOxygenSaturation

PhoneTabletWearable

血氧采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| spo2 | number | 否 | 否 | 血氧饱和度。  单位：百分比  取值范围：(0, 100]。 |

## BloodOxygenSaturationAggregation

PhoneTabletWearable

血氧聚合统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| spo2 | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'sum' | 'count'> | 否 | 否 | 血氧饱和度聚合统计。 |

## BloodPressure

PhoneTabletWearable

血压采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bloodPressureSystolic | number | 否 | 否 | 收缩压，即高压。  单位：mmHg  取值范围： (0, ∞) |
| bloodPressureDiastolic | number | 否 | 否 | 舒张压，即低压。  单位：mmHg  取值范围： (0, ∞) |
| sphygmus | number | 否 | 是 | 脉搏，若未填写，默认为空。  单位：次/分钟  取值范围： (0, ∞) |
| measurementAnomalyFlag | number | 否 | 是 | 测量异常事件，若未填写，默认为空。  取值范围： (0, ∞)  取值参考如下：  1：正常  2：测量时未和心脏平齐  3：测量时有轻微抖动  4：测量前没有至少5min休息 |
| beforeMeasureActivity | number | 否 | 是 | 测量前活动，若未填写，默认为空。  取值范围： (0, ∞)  取值参考如下：  1：剧烈运动  2：吸烟  3：进食  4：饮酒  5：喝咖啡  6：无活动  7：起床后  8：睡前  100：自定义 |

## BodyTemperature

PhoneTabletWearable

体温采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bodyTemperature | number | 否 | 否 | 体温。  单位：摄氏度  取值范围：[34, 42]。 |

## BodyTemperatureAggregation

PhoneTabletWearable

体温聚合统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bodyTemperature | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'sum' | 'last'> | 否 | 否 | 体温聚合统计。 |

## BreathHoldingTestDetail

PhoneTabletWearable

闭气测试详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |

## BreathHoldingTestFeature

PhoneTabletWearable

闭气测试特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| diaphragmTime | number | 否 | 否 | 横膈膜打点时间。  单位：秒 |

## BreathHoldingTestSummary

PhoneTabletWearable

闭气测试统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| breathHoldingTestFeature | [BreathHoldingTestFeature](health-api-healthfields.md#breathholdingtestfeature) | 否 | 否 | 闭气测试特征统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## BreathHoldingTrainDetail

PhoneTabletWearable

闭气训练详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |

## BreathHoldingTrainFeature

PhoneTabletWearable

闭气训练特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| breathTime | number | 否 | 否 | 呼吸时间。  单位：秒 |
| breathHoldingTime | number | 否 | 否 | 闭气时间。  单位：秒 |
| breathHoldingTrainRhythm | number | 否 | 是 | 闭气训练节奏数，若未填写，默认为空。  单位：次 |

## BreathHoldingTrainSummary

PhoneTabletWearable

闭气训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| breathHoldingTrainFeature | [BreathHoldingTrainFeature](health-api-healthfields.md#breathholdingtrainfeature) | 否 | 否 | 闭气训练特征统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## Cadence

PhoneTabletWearable

步频详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| cadence | number | 否 | 否 | 步频。  单位：步数/分钟  取值范围：[0, ∞) |

## CadenceSummary

PhoneTabletWearable

步频统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：步数/分钟  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：步数/分钟  取值范围：[0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  单位：步数/分钟  取值范围：[0, ∞) |

## CalorieSummary

PhoneTabletWearable

卡路里统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| totalCalories | number | 否 | 否 | 卡路里总和。  单位：卡  取值范围：(0, ∞) |

## CyclingDetail

PhoneTabletWearable

骑行详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| pedalingCadence | [PedalingCadence](health-api-healthfields.md#pedalingcadence)[] | 否 | 是 | 踏频详情列表，若未填写，默认为空。 |
| power | [Power](health-api-healthfields.md#power)[] | 否 | 是 | 功率详情列表，若未填写，默认为空。 |
| location | [Location](health-api-healthfields.md#location)[] | 否 | 是 | 位置详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |
| resistance | [Resistance](health-api-healthfields.md#resistance)[] | 否 | 是 | 阻力详情列表，若未填写，默认为空。 |

## CyclingSummary

PhoneTabletWearable

骑行统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| speed | [SpeedSummary](health-api-healthfields.md#speedsummary) | 否 | 否 | 速度统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| resistance | [ResistanceSummary](health-api-healthfields.md#resistancesummary) | 否 | 是 | 阻力统计，若未填写，默认为空。 |
| pedalingCadence | [PedalingCadenceSummary](health-api-healthfields.md#pedalingcadencesummary) | 否 | 是 | 踏频统计，若未填写，默认为空。 |
| power | [PowerSummary](health-api-healthfields.md#powersummary) | 否 | 是 | 功率统计，若未填写，默认为空。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |
| location | [LocationSummary](health-api-healthfields.md#locationsummary) | 否 | 是 | 位置统计，若未填写，默认为空。 |

## DailyActivities

PhoneTabletWearable

日常活动采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| step | number | 否 | 否 | 步数。  单位：步  取值范围：[0, 500) |
| calorie | number | 否 | 否 | 热量。  单位：卡  取值范围：[0, 65536) |
| distance | number | 否 | 否 | 距离。  单位：米  取值范围：[0, ∞) |
| duration | number | 否 | 是 | 时长，若未填写，默认为空。  单位：分钟  取值范围：0 或 1 |
| status | number | 否 | 是 | 状态（走、跑、骑、爬等），若未填写，默认为空。  取值范围：  2： 登山  3： 骑行  4： 跑步  5：走路  9：游泳  10：健身  13：站立 |
| isIntensity | number | 否 | 是 | 是否中高强度，若未填写，默认为空。  取值范围：  0：否  1：是 |
| climbHighAltitude | number | 否 | 是 | 爬高海拔差（支持正负），若未填写，默认为空。  单位：米 |
| isStand | number | 否 | 是 | 是否站立（一个小时有活动记录，就标志这个小时的第一分钟为1），若未填写，默认为空。  取值范围：  0：否  1：是 |

## DailyActivitiesAggregation

PhoneTabletWearable

日常活动聚合统计数据字段列表。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| step | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'max' | 'min' | 'avg' | 'last' | 'count'> | 否 | 否 | 步数聚合统计。 |
| calorie | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'max' | 'min' | 'avg' | 'last' | 'count'> | 否 | 否 | 卡路里聚合统计。 |
| distance | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'max' | 'min' | 'avg' | 'last' | 'count'> | 否 | 否 | 距离聚合统计。 |
| climbHighAltitude | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'max' | 'min' | 'avg' | 'last' | 'count'> | 否 | 否 | 爬高海拔差聚合统计。 |
| isIntensity | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'max' | 'min' | 'avg' | 'last' | 'count'> | 否 | 否 | 中高强度聚合统计。 |
| isStand | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'max' | 'min' | 'avg' | 'last' | 'count'> | 否 | 否 | 站立聚合统计。 |

## DistanceSummary

PhoneTabletWearable

距离统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| totalDistance | number | 否 | 否 | 距离统计。  单位：米  取值范围：(0, ∞) |

## DivingDepth

PhoneTabletWearable

潜水深度详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| depth | number | 否 | 否 | 潜水深度。  单位：米 |

## DivingDepthSummary

PhoneTabletWearable

潜水深度统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：米  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：米  取值范围：[0, ∞) |

## DivingDetail

PhoneTabletWearable

自由潜水详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| divingDepth | [DivingDepth](health-api-healthfields.md#divingdepth)[] | 否 | 是 | 潜水深度详情列表，若未填写，默认为空。 |
| waterTemperature | [WaterTemperature](health-api-healthfields.md#watertemperature)[] | 否 | 是 | 水温详情列表，若未填写，默认为空。 |

## DivingFeature

PhoneTabletWearable

自由潜水特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| divingTime | number | 否 | 否 | 潜水时间。  单位：秒 |
| divingCount | number | 否 | 否 | 潜水次数。 |
| divingMode | number | 否 | 否 | 潜水模式。  取值参考如下：  0：自由潜水  1：休闲水肺潜水  2：技术水肺潜水  3：仪表潜水 |
| maxUnderwaterTime | number | 否 | 是 | 单次水下最长时间，若未填写，默认为空。  单位：秒 |
| underwaterTime | number | 否 | 是 | 水下时间，若未填写，默认为空。  单位：秒 |
| noFlyTime | number | 否 | 是 | 禁飞时间，若未填写，默认为空。  单位：小时 |
| waterType | number | 否 | 是 | 水体类型，若未填写，默认为空。  取值参考如下：  0：自定义  1：淡水  2：海水 |
| waterDensity | number | 否 | 是 | 水密度，若未填写，默认为空。  单位：千克/升 |
| maxAscentSpeed | number | 否 | 是 | 最大上升速度，若未填写，默认为空。  单位：米/秒 |
| maxDescentSpeed | number | 否 | 是 | 最大下降速度，若未填写，默认为空。  单位：米/秒 |

## DivingSummary

PhoneTabletWearable

自由潜水统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| divingFeature | [DivingFeature](health-api-healthfields.md#divingfeature) | 否 | 否 | 自由潜水特征数据。 |
| location | [LocationSummary](health-api-healthfields.md#locationsummary) | 否 | 是 | 位置统计，若未填写，默认为空。 |
| divingDepth | [DivingDepthSummary](health-api-healthfields.md#divingdepthsummary) | 否 | 是 | 潜水深度统计，若未填写，默认为空。 |
| waterTemperature | [WaterTemperatureSummary](health-api-healthfields.md#watertemperaturesummary) | 否 | 是 | 水温统计，若未填写，默认为空。 |

## EllipticalDetail

PhoneTabletWearable

椭圆机详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| pedalingCadence | [PedalingCadence](health-api-healthfields.md#pedalingcadence)[] | 否 | 是 | 脚踏节奏详情列表，若未填写，默认为空。 |
| power | [Power](health-api-healthfields.md#power)[] | 否 | 是 | 功率详情列表，若未填写，默认为空。 |
| cadence | [Cadence[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields#cadence) | 否 | 是 | 步频详情列表，若未填写，默认为空。 |

## EllipticalSummary

PhoneTabletWearable

椭圆机统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 是 | 距离统计，若未填写，默认为空。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| speed | [SpeedSummary](health-api-healthfields.md#speedsummary) | 否 | 是 | 速度统计，若未填写，默认为空。 |
| step | [StepSummary](health-api-healthfields.md#stepsummary) | 否 | 是 | 步数统计，若未填写，默认为空。 |
| cadence | [CadenceSummary](health-api-healthfields.md#cadencesummary) | 否 | 是 | 步频统计，若未填写，默认为空。 |
| resistance | [ResistanceSummary](health-api-healthfields.md#resistancesummary) | 否 | 是 | 阻力统计，若未填写，默认为空。 |
| pedalingCadence | [PedalingCadenceSummary](health-api-healthfields.md#pedalingcadencesummary) | 否 | 是 | 脚踏节奏统计，若未填写，默认为空。 |
| power | [PowerSummary](health-api-healthfields.md#powersummary) | 否 | 是 | 功率统计，若未填写，默认为空。 |

## Emotion

PhoneTabletWearable

情绪采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| emotionStatus | number | 否 | 否 | 情绪状态。  取值范围：[0, 100)  当前运动健康App仅展示以下值：  1：不愉悦  2：平静  3：愉悦 |

## ExerciseHeartRate

PhoneTabletWearable

运动心率详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bpm | number | 否 | 否 | 运动心率详情。  单位：次/分钟  取值范围：(0, 255) |

## ExerciseHeartRateSummary

PhoneTabletWearable

运动心率统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：次/分钟  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：次/分钟  取值范围：[0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  单位：次/分钟  取值范围：[0, ∞) |

## GolfCourseModelDetail

PhoneTabletWearable

高尔夫场地模式详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |

## GolfCourseModelFeature

PhoneTabletWearable

高尔夫场地模式特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| golfSwingCount | number | 否 | 否 | 总挥杆数。 |
| courseId | number | 否 | 否 | 球场名称id。 |
| holes | number | 否 | 否 | 球洞个数。 |
| branchId1 | number | 否 | 是 | 上半场分层id，若未填写，默认为空。 |
| branchId2 | number | 否 | 是 | 下半场分层id，若未填写，默认为空。 |
| gir | number | 否 | 是 | 上果岭率，若未填写，默认为空。 |
| doubleEagle | number | 否 | 是 | 信天翁，若未填写，默认为空。 |
| eagle | number | 否 | 是 | 老鹰球，若未填写，默认为空。 |
| birdie | number | 否 | 是 | 小鸟球，若未填写，默认为空。 |
| par | number | 否 | 是 | 标准杆，若未填写，默认为空。 |
| bogey | number | 否 | 是 | 柏忌，若未填写，默认为空。 |
| doubleBogey | number | 否 | 是 | 双柏忌，若未填写，默认为空。 |
| putts | number | 否 | 是 | 总推杆，若未填写，默认为空。 |
| avgPutts | number | 否 | 是 | 平均推杆，若未填写，默认为空。 |
| par3 | number | 否 | 是 | 标准3杆洞平均杆，若未填写，默认为空。 |
| par4 | number | 否 | 是 | 标准4杆洞平均杆，若未填写，默认为空。 |
| par5 | number | 否 | 是 | 标准5杆洞平均杆，若未填写，默认为空。 |
| fairwayHits | number | 否 | 是 | 球道命中数，若未填写，默认为空。 |
| fairwayLeft | number | 否 | 是 | 球道左曲数，若未填写，默认为空。 |
| fairwayRight | number | 否 | 是 | 球道右曲数，若未填写，默认为空。 |
| avgHandicap | number | 否 | 是 | 平均杆差，若未填写，默认为空。 |
| bestHandicap | number | 否 | 是 | 最佳杆差，若未填写，默认为空。 |
| totalHandicap | number | 否 | 是 | 总杆差，若未填写，默认为空。 |

## GolfCourseModelSummary

PhoneTabletWearable

高尔夫场地模式统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| golfCourseModelFeature | [GolfCourseModelFeature](health-api-healthfields.md#golfcoursemodelfeature) | 否 | 否 | 高尔夫场地模式特征数据。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| step | [StepSummary](health-api-healthfields.md#stepsummary) | 否 | 否 | 步数统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 是 | 距离统计，若未填写，默认为空。 |
| cadence | [CadenceSummary](health-api-healthfields.md#cadencesummary) | 否 | 是 | 步频统计，若未填写，默认为空。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |

## GolfPracticeDetail

PhoneTabletWearable

高尔夫练习场模式详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |

## GolfPracticeFeature

PhoneTabletWearable

高尔夫练习场模式特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| golfSwingCount | number | 否 | 否 | 总挥杆数。 |
| golfSwingSpeed | number | 否 | 是 | 平均挥杆速度，若未填写，默认为空。  单位：厘米/秒 |
| golfMaxSwingSpeed | number | 否 | 是 | 最大挥杆速度，若未填写，默认为空。  单位：厘米/秒 |
| golfSwingTempo | number | 否 | 是 | 平均挥杆节奏（平均上杆时间/平均下杆时间），若未填写，默认为空。 |
| golfDownSwingTime | number | 否 | 是 | 平均下杆时间，若未填写，默认为空。  单位：毫秒 |
| golfBackSwingTime | number | 否 | 是 | 平均上杆时间，若未填写，默认为空。  单位：毫秒 |

## GolfPracticeSummary

PhoneTabletWearable

高尔夫练习场模式统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| golfPracticeFeature | [GolfPracticeFeature](health-api-healthfields.md#golfpracticefeature) | 否 | 否 | 高尔夫练习场模式特征数据。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## HeartRate

PhoneTabletWearable

动态心率采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bpm | number | 否 | 否 | 动态心率。  单位：次/分钟  取值范围：[0, ∞) |

## HeartRateAggregation

PhoneTabletWearable

动态心率聚合统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bpm | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'avg' | 'sum' | 'count'> | 否 | 否 | 动态心率聚合统计。 |

## HeartRateVariability

PhoneTabletWearable

心率变异性采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| heartRateVariabilityRMSSD | number | 否 | 否 | 心率变异性。  单位：毫秒  取值范围：(0, 200] |

## Height

PhoneTabletWearable

身高采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| height | number | 否 | 否 | 身高。  单位：厘米 |

## Jump

PhoneTabletWearable

跳跃详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| jumpHeight | number | 否 | 否 | 纵跃高度。  单位：米 |
| passageDuration | number | 否 | 否 | 滞空时间。  单位：毫秒 |

## JumpingRopeDetail

PhoneTabletWearable

跳绳详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| skipSpeed | [SkipSpeed](health-api-healthfields.md#skipspeed)[] | 否 | 是 | 跳跃速度详情列表，若未填写，默认为空。 |

## JumpingRopeFeature

PhoneTabletWearable

跳绳特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| skipNum | number | 否 | 否 | 跳绳个数。  取值范围：[0, ∞) |
| interruptions | number | 否 | 是 | 中断次数，若未填写，默认为空。  取值范围：[0, ∞) |
| longestStreak | number | 否 | 是 | 最多连跳，若未填写，默认为空。  取值范围：[0, ∞) |
| doubleUnders | number | 否 | 是 | 双摇个数，若未填写，默认为空。  取值范围：[0, ∞) |
| tripleUnders | number | 否 | 是 | 三摇个数，若未填写，默认为空。  取值范围：[0, ∞) |

## JumpingRopeSummary

PhoneTabletWearable

跳绳统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| jumpingRopeFeature | [JumpingRopeFeature](health-api-healthfields.md#jumpingropefeature) | 否 | 否 | 跳绳特征数据。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| skipSpeed | [SkipSpeedSummary](health-api-healthfields.md#skipspeedsummary) | 否 | 否 | 跳跃速度统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## JumpSummary

PhoneTabletWearable

跳跃统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| jumpTimes | number | 否 | 否 | 跳跃次数。 |
| maxJumpHeight | number | 否 | 是 | 最大跳跃高度，若未填写，默认为空。  单位：米 |
| maxPassageDuration | number | 否 | 是 | 最大滞空时间，若未填写，默认为空。  单位：毫秒 |

## Location

PhoneTabletWearable

位置详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度。  单位：度  取值范围：[-90, 90] |
| longitude | number | 否 | 否 | 经度。  单位：度  取值范围：[-180, 180] |

## LocationSummary

PhoneTabletWearable

位置统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| coordinate | string | 否 | 否 | 坐标系。  取值参考如下：  'GCJ02'  'WGS84'  'BD09' |
| startLat | number | 否 | 是 | 起始点纬度，若未填写，默认为空。  单位：度  取值范围：[-90, 90] |
| endLat | number | 否 | 是 | 结束点纬度，若未填写，默认为空。  单位：度  取值范围：[-90, 90] |
| startLon | number | 否 | 是 | 起始点经度，若未填写，默认为空。  单位：度  取值范围：[-180, 180] |
| endLon | number | 否 | 是 | 结束点经度，若未填写，默认为空。  单位：度  取值范围：[-180, 180] |

## MarkPoint

PhoneTabletWearable

标记点采样数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| sn | number | 否 | 否 | 序号。 |
| type | number | 否 | 否 | 标记点类型。  取值参考如下：  0：通用  1：起始  2：营地  3：向左  4：向右  5：直行  6：危险  7：野兽  8：医疗  9：水流  10：补给  11：桥梁  12：避险  13：山顶  14：房屋  254：终点  255：自动标记点 |
| longitude | number | 否 | 否 | 经度。  单位：度 |
| latitude | number | 否 | 否 | 纬度。  单位：度 |
| mode | number | 否 | 否 | 标记方式。  取值参考如下：  0：自动  1：手动 |
| color | number | 否 | 是 | 颜色，若未填写，默认为空。  取值参考如下：  0：橙色  1：红色  2：蓝色  3：黄色  4：灰色  5：绿色  255：自动标记点颜色 |

## MountainHikeDetail

PhoneTabletWearable

登山详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| location | [Location](health-api-healthfields.md#location)[] | 否 | 是 | 位置详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |

## MountainHikeSummary

PhoneTabletWearable

登山统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| step | [StepSummary](health-api-healthfields.md#stepsummary) | 否 | 是 | 步数统计，若未填写，默认为空。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |

## OpenWaterSwimDetail

PhoneTabletWearable

开放水域游泳详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| location | [Location](health-api-healthfields.md#location)[] | 否 | 是 | 位置详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| swimStrokeRate | [SwimStrokeRate](health-api-healthfields.md#swimstrokerate)[] | 否 | 是 | 划水频率详情列表，若未填写，默认为空。 |
| swolf | [Swolf](health-api-healthfields.md#swolf)[] | 否 | 是 | SWOLF详情列表，若未填写，默认为空。 |

## OpenWaterSwimFeature

PhoneTabletWearable

开放水域游泳特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| pullTimes | number | 否 | 否 | 划水次数。 |
| swimmingStroke | number | 否 | 是 | 主泳姿，若未填写，默认为空。  取值参考如下：  1：蛙泳  2：自由泳  3：蝶泳  4：仰泳  5：混合泳 |

## OpenWaterSwimSummary

PhoneTabletWearable

开放水域游泳统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| openWaterSwimFeature | [OpenWaterSwimFeature](health-api-healthfields.md#openwaterswimfeature) | 否 | 否 | 开放水域游泳特征数据。 |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| swimStrokeRate | [SwimStrokeRateSummary](health-api-healthfields.md#swimstrokeratesummary) | 否 | 是 | 划水频率统计，若未填写，默认为空。 |
| swolf | [SwolfSummary](health-api-healthfields.md#swolfsummary) | 否 | 是 | SWOLF统计，若未填写，默认为空。 |

## PedalingCadence

PhoneTabletWearable

踏频详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| rpm | number | 否 | 否 | 踏频详情。  单位：转/分钟  取值范围：[0, ∞) |

## PedalingCadenceSummary

PhoneTabletWearable

踏频统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：转/分钟  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：转/分钟  取值范围：[0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  单位：转/分钟  取值范围：[0, ∞) |

## PoolSwimDetail

PhoneTabletWearable

泳池游泳详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| swimStrokeRate | [SwimStrokeRate](health-api-healthfields.md#swimstrokerate)[] | 否 | 是 | 划水频率详情列表，若未填写，默认为空。 |
| swolf | [Swolf](health-api-healthfields.md#swolf)[] | 否 | 是 | SWOLF详情列表，若未填写，默认为空。 |

## PoolSwimFeature

PhoneTabletWearable

泳池游泳特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| pullTimes | number | 否 | 否 | 划水次数。 |
| tripTimes | number | 否 | 否 | 趟数。 |
| poolLength | number | 否 | 是 | 泳池长度，若未填写，默认为空。  单位：米 |
| swimmingStroke | number | 否 | 是 | 主泳姿，若未填写，默认为空。  取值参考如下：  1：蛙泳  2：自由泳  3：蝶泳  4：仰泳  5：混合泳 |

## PoolSwimSummary

PhoneTabletWearable

泳池游泳统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| poolSwimFeature | [PoolSwimFeature](health-api-healthfields.md#poolswimfeature) | 否 | 否 | 泳池游泳特征数据。 |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| speed | [SpeedSummary](health-api-healthfields.md#speedsummary) | 否 | 是 | 速度统计，若未填写，默认为空。 |
| swimStrokeRate | [SwimStrokeRateSummary](health-api-healthfields.md#swimstrokeratesummary) | 否 | 是 | 划水频率统计，若未填写，默认为空。 |
| swolf | [SwolfSummary](health-api-healthfields.md#swolfsummary) | 否 | 是 | SWOLF统计，若未填写，默认为空。 |

## Power

PhoneTabletWearable

功率详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| power | number | 否 | 否 | 功率详情。  单位：瓦  取值范围：[0, ∞) |

## PowerSummary

PhoneTabletWearable

功率统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：瓦  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：瓦  取值范围：[0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  单位：瓦  取值范围：[0, ∞) |

## QuantitySummary

PhoneTabletWearable

统计基类数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  取值范围：[0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  取值范围：[0, ∞) |

## Resistance

PhoneTabletWearable

阻力详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| resLevel | number | 否 | 否 | 阻力等级。  取值范围：[1, 100] |

## ResistanceSummary

PhoneTabletWearable

阻力统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| resLv1LowerLimit | number | 否 | 否 | 阻力区间1下限。  取值范围：[1, 100] |
| resLv2LowerLimit | number | 否 | 否 | 阻力区间2下限。  取值范围：[1, 100] |
| resLv3LowerLimit | number | 否 | 否 | 阻力区间3下限。  取值范围：[1, 100] |
| resLv4LowerLimit | number | 否 | 否 | 阻力区间4下限。  取值范围：[1, 100] |
| resLv5LowerLimit | number | 否 | 否 | 阻力区间5下限。  取值范围：[1, 100] |
| resLv5UpperLimit | number | 否 | 否 | 阻力区间5上限。  取值范围：[1, 100] |
| resLv1Duration | number | 否 | 否 | 在阻力区间1内运动时长。  单位：分钟  取值范围：[0, ∞) |
| resLv2Duration | number | 否 | 否 | 在阻力区间2内运动时长。  单位：分钟  取值范围：[0, ∞) |
| resLv3Duration | number | 否 | 否 | 在阻力区间3内运动时长。  单位：分钟  取值范围：[0, ∞) |
| resLv4Duration | number | 否 | 否 | 在阻力区间4内运动时长。  单位：分钟  取值范围：[0, ∞) |
| resLv5Duration | number | 否 | 否 | 在阻力区间5内运动时长。  单位：分钟  取值范围：[0, ∞) |
| maxRes | number | 否 | 是 | 设备可设置的最大阻力级别，若未填写，默认为空。  取值范围：[1, 100] |
| minRes | number | 否 | 是 | 设备可设置的最小阻力级别，若未填写，默认为空。  取值范围：[1, 100] |

## RestingHeartRate

PhoneTabletWearable

静息心率数据字段列表.

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| restBpm | number | 否 | 否 | 静息心率。  单位：次/分钟  取值范围：[0, ∞) |

## RestingHeartRateAggregation

PhoneTabletWearable

静息心率聚合统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| restBpm | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'sum' | 'count' | 'max' | 'min' | 'avg'> | 否 | 否 | 静息心率聚合统计。 |

## RowerDetail

PhoneTabletWearable

划船机详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| power | [Power](health-api-healthfields.md#power)[] | 否 | 是 | 功率详情列表，若未填写，默认为空。 |
| resistance | [Resistance](health-api-healthfields.md#resistance)[] | 否 | 是 | 阻力详情列表，若未填写，默认为空。 |
| strokeRate | [StrokeRate](health-api-healthfields.md#strokerate)[] | 否 | 是 | 桨频详情列表，若未填写，默认为空。 |

## RowerFeature

PhoneTabletWearable

划船机特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| strokesNum | number | 否 | 否 | 累计桨次。 |

## RowerSummary

PhoneTabletWearable

划船机统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| rowerFeature | [RowerFeature](health-api-healthfields.md#rowerfeature) | 否 | 否 | 划船机特征数据。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 是 | 距离统计，若未填写，默认为空。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| speed | [SpeedSummary](health-api-healthfields.md#speedsummary) | 否 | 是 | 速度统计，若未填写，默认为空。 |
| resistance | [ResistanceSummary](health-api-healthfields.md#resistancesummary) | 否 | 是 | 阻力统计，若未填写，默认为空。 |
| power | [PowerSummary](health-api-healthfields.md#powersummary) | 否 | 是 | 功率统计，若未填写，默认为空。 |
| strokeRate | [StrokeRateSummary](health-api-healthfields.md#strokeratesummary) | 否 | 是 | 桨频统计，若未填写，默认为空。 |

## RowingDetail

PhoneTabletWearable

赛艇详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| strokeRate | [StrokeRate](health-api-healthfields.md#strokerate)[] | 否 | 是 | 桨频详情列表，若未填写，默认为空。 |

## RowingFeature

PhoneTabletWearable

赛艇特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| strokesNum | number | 否 | 否 | 累计桨次。 |

## RowingSummary

PhoneTabletWearable

赛艇统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| rowingFeature | [RowingFeature](health-api-healthfields.md#rowingfeature) | 否 | 否 | 赛艇特征数据。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 卡路里统计。 |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 是 | 距离统计，若未填写，默认为空。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| strokeRate | [StrokeRateSummary](health-api-healthfields.md#strokeratesummary) | 否 | 是 | 桨频统计，若未填写，默认为空。 |

## RunningDetail

PhoneTabletWearable

跑步详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| cadence | [Cadence](health-api-healthfields.md#cadence)[] | 否 | 是 | 步频详情列表，若未填写，默认为空。 |
| runningForm | [RunningForm](health-api-healthfields.md#runningform)[] | 否 | 是 | 跑姿详情列表，若未填写，默认为空。 |
| location | [Location](health-api-healthfields.md#location)[] | 否 | 是 | 位置详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |

## RunningFeature

PhoneTabletWearable

跑步特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avgPace | number | 否 | 否 | 平均配速。  取值范围：[0, ∞)  单位：秒/公里 |
| bestPace | number | 否 | 否 | 最快配速。  取值范围：[0, ∞)  单位：秒/公里 |
| paceMap | [healthStore.PaceValueType](health-api-healthstore.md#pacevaluetype) | 否 | 是 | 每公里的配速，若未填写，默认为空。单位：秒/公里  例如  '1.0':407.945  '2.0':473.98846  '2.170':473.98846  最后不满一公里的部分，按比例换算为整公里的配速存入。 |
| partTimeMap | [healthStore.PaceValueType](health-api-healthstore.md#pacevaluetype) | 否 | 是 | 公制分段数据表（key：公里，value：秒），若未填写，默认为空。  其中公里保留到小数点后4位。  Value是一个累积到当前公里的时间如：  - '1.0':3.0  - '2.0':6.0  - '3.0':9.0  - '21.0975':7020.0  - '42.195':18000.0  其中，21.0975，42.195分别为半马和全马的距离（仅半马全马key值小数点后不为0）。 |

## RunningForm

PhoneTabletWearable

跑姿详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| groundContactTime | number | 否 | 否 | 触地时间。  单位：毫秒  取值范围：[0, 5000] |
| groundImpactAcceleration | number | 否 | 是 | 着地冲击，若未填写，默认为空。  单位：g（重力加速度）  取值范围：[0, 50] |
| swingAngle | number | 否 | 是 | 摆动角度，若未填写，默认为空。  单位：度  取值范围：[0, 360] |
| eversionExcursion | number | 否 | 是 | 外翻幅度，若未填写，默认为空。  单位：度  取值范围：[-100, 100] |
| hangTime | number | 否 | 是 | 腾空时间，若未填写，默认为空。  单位：毫秒  取值范围：[0, 500] |
| groundHangTimeRate | number | 否 | 是 | 触地腾空比，若未填写，默认为空。  取值范围：[0, 500] |
| foreFootStrikePattern | number | 否 | 是 | 触地方式中的前脚掌触地次数，若未填写，默认为空。  取值范围：[0, 100] |
| hindFootStrikePattern | number | 否 | 是 | 触地方式中的后脚掌触地次数，若未填写，默认为空。  取值范围：[0, 100] |
| wholeFootStrikePattern | number | 否 | 是 | 触地方式中的全脚掌触地次数，若未填写，默认为空。  取值范围：[0, 100] |
| impactPeak | number | 否 | 是 | 触地峰值，若未填写，默认为空。  单位：BW（体重倍数）  取值范围：[0, 10] |
| verticalOscillation | number | 否 | 是 | 垂直振幅，若未填写，默认为空。  单位：厘米  取值范围：[0, 25.6] |
| verticalRatio | number | 否 | 是 | 垂直步幅比，若未填写，默认为空。  单位：百分比  取值范围：[0, 100] |
| gcTimeBalance | number | 否 | 是 | 左右触地平衡，若未填写，默认为空。  单位：百分比（返回数据为左脚的触地平衡，右脚需自行计算，二者之和为100%）  取值范围：[0, 100] |

## RunningFormSummary

PhoneTabletWearable

跑姿统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avgGroundContactTime | number | 否 | 否 | 平均触地时间。  单位：毫秒  取值范围：[0, 5000] |
| avgGroundImpactAcceleration | number | 否 | 是 | 平均着地冲击，若未填写，默认为空。  单位：g（重力加速度） |
| avgSwingAngle | number | 否 | 是 | 平均摆动角度，若未填写，默认为空。  单位：度 |
| avgEversionExcursion | number | 否 | 是 | 平均外翻幅度，若未填写，默认为空。  单位：度 |
| avgHangTime | number | 否 | 是 | 平均腾空时间，若未填写，默认为空。  单位：毫秒 |
| avgGroundHangTimeRate | number | 否 | 是 | 平均触地腾空比，若未填写，默认为空。 |
| foreFootStrikePattern | number | 否 | 是 | 触地方式中的前脚掌触地次数，若未填写，默认为空。 |
| hindFootStrikePattern | number | 否 | 是 | 触地方式中的后脚掌触地次数，若未填写，默认为空。 |
| wholeFootStrikePattern | number | 否 | 是 | 触地方式中的全脚掌触地次数，若未填写，默认为空。 |
| avgImpactPeak | number | 否 | 是 | 平均触地峰值，若未填写，默认为空。  单位：BW（体重倍数） |
| avgVerticalImpactRate | number | 否 | 是 | 平均冲击负载率，若未填写，默认为空。  单位：BW/S |
| avgVerticalOscillation | number | 否 | 是 | 平均垂直振幅，若未填写，默认为空。  单位：厘米 |
| avgVerticalRatio | number | 否 | 是 | 平均垂直步幅比，若未填写，默认为空。  单位：百分比 |
| avgGcTimeBalance | number | 否 | 是 | 平均左右触地平衡，若未填写，默认为空。  单位：百分比（返回数据为左脚的触地平衡，右脚需自行计算，二者之和为100%） |

## RunningSummary

PhoneTabletWearable

跑步统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| speed | [SpeedSummary](health-api-healthfields.md#speedsummary) | 否 | 否 | 速度统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| step | [StepSummary](health-api-healthfields.md#stepsummary) | 否 | 是 | 步数统计，若未填写，默认为空。 |
| cadence | [CadenceSummary](health-api-healthfields.md#cadencesummary) | 否 | 是 | 步频统计，若未填写，默认为空。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |
| location | [LocationSummary](health-api-healthfields.md#locationsummary) | 否 | 是 | 位置统计，若未填写，默认为空。 |
| runningForm | [RunningFormSummary](health-api-healthfields.md#runningformsummary) | 否 | 是 | 跑姿统计，若未填写，默认为空。 |
| runningFeature | [RunningFeature](health-api-healthfields.md#runningfeature) | 否 | 是 | 跑步特征数据，若未填写，默认为空。 |

## ScubaDivingDetail

PhoneTabletWearable

水肺潜水详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| divingDepth | [DivingDepth](health-api-healthfields.md#divingdepth)[] | 否 | 是 | 潜水深度详情列表，若未填写，默认为空。 |
| waterTemperature | [WaterTemperature](health-api-healthfields.md#watertemperature)[] | 否 | 是 | 水温详情列表，若未填写，默认为空。 |

## ScubaDivingFeature

PhoneTabletWearable

水肺潜水特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| divingTime | number | 否 | 否 | 潜水时间。  单位：秒 |
| divingCount | number | 否 | 否 | 潜水次数。 |
| divingMode | number | 否 | 否 | 潜水模式。  取值参考如下：  0：自由潜水  1：休闲水肺潜水  2：技术水肺潜水  3：仪表潜水 |
| maxUnderwaterTime | number | 否 | 是 | 单次水下最长时间，若未填写，默认为空。  单位：秒 |
| underwaterTime | number | 否 | 是 | 水下时间，若未填写，默认为空。  单位：秒 |
| noFlyTime | number | 否 | 是 | 禁飞时间，若未填写，默认为空。  单位：小时 |
| cns | number | 否 | 是 | CNS(中枢神经系统毒性等级)，若未填写，默认为空。  等级：  一：0%-79%  二：80%-99%  三：大于等于100% |
| otu | number | 否 | 是 | OTU(氧气毒性单元)，若未填写，默认为空。  等级：  一：0-249  二：250-299  三：大于等于300 |
| waterType | number | 否 | 是 | 水体类型，若未填写，默认为空。  取值参考如下：  0：自定义  1：淡水  2：海水 |
| waterDensity | number | 否 | 是 | 水密度，若未填写，默认为空。  单位：千克/升 |
| maxAscentSpeed | number | 否 | 是 | 最大上升速度，若未填写，默认为空。  单位：米/秒 |
| maxDescentSpeed | number | 否 | 是 | 最大下降速度，若未填写，默认为空。  单位：米/秒 |

## ScubaDivingSummary

PhoneTabletWearable

水肺潜水统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| scubaDivingFeature | [ScubaDivingFeature](health-api-healthfields.md#scubadivingfeature) | 否 | 否 | 水肺潜水特征数据。 |
| location | [LocationSummary](health-api-healthfields.md#locationsummary) | 否 | 是 | 位置统计，若未填写，默认为空。 |
| divingDepth | [DivingDepthSummary](health-api-healthfields.md#divingdepthsummary) | 否 | 是 | 潜水深度统计，若未填写，默认为空。 |
| waterTemperature | [WaterTemperatureSummary](health-api-healthfields.md#watertemperaturesummary) | 否 | 是 | 水温统计，若未填写，默认为空。 |

## SkiingDetail

PhoneTabletWearable

滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| location | [Location](health-api-healthfields.md#location)[] | 否 | 是 | 位置详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |

## SkiingFeature

PhoneTabletWearable

滑雪特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tripTimes | number | 否 | 否 | 趟数。 |
| maxSlopePercent | number | 否 | 是 | 滑雪最大坡度百分比，若未填写，默认为空。 |
| maxSlopeDegree | number | 否 | 是 | 滑雪最大坡，若未填写，默认为空。  单位：度 |
| totalTime | number | 否 | 是 | 滑行时间，若未填写，默认为空。  单位：毫秒 |
| totalDistance | number | 否 | 是 | 滑行距离，若未填写，默认为空。  单位：米 |

## SkiingSummary

PhoneTabletWearable

滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| skiingFeature | [SkiingFeature](health-api-healthfields.md#skiingfeature) | 否 | 否 | 滑雪特征数据。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## SkinTemperature

PhoneTabletWearable

皮肤体温详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| skinTemperature | number | 否 | 否 | 皮肤温度。  单位：摄氏度  取值范围：[20, 42] |

## SkinTemperatureAggregation

PhoneTabletWearable

皮肤体温聚合统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| skinTemperature | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'sum' | 'last'> | 否 | 否 | 皮肤体温聚合统计。 |

## SkipSpeed

PhoneTabletWearable

跳绳速度详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| skipSpeed | number | 否 | 否 | 跳绳速度详情。  单位：个/分钟  取值范围：[0, ∞) |

## SkipSpeedSummary

PhoneTabletWearable

跳绳速度统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：个/分钟  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：个/分钟  取值范围：[0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  单位：个/分钟  取值范围：[0, ∞) |

## SledDetail

PhoneTabletWearable

滑雪橇详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |

## SledSummary

PhoneTabletWearable

滑雪橇统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## Sleep

PhoneTabletWearable

夜间睡眠数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| fallAsleepTime | number | 否 | 否 | 分期睡眠最早入睡时间点。  单位：毫秒  取值范围：[0, ∞) |
| wakeupTime | number | 否 | 否 | 分期睡眠最晚醒来时间点。  单位：毫秒  取值范围：[0, ∞) |
| duration | number | 否 | 否 | 夜间/普通睡眠时长（不含零星小睡时长）。  单位：秒  取值范围：[0, ∞) |
| bedTime | number | 否 | 是 | 最早上床时间点，若未填写，默认为空。  取值范围：[0, ∞) |
| risingTime | number | 否 | 是 | 最晚起床时间点，若未填写，默认为空。  取值范围：[0, ∞) |
| prepareSleepTime | number | 否 | 是 | 准备入睡时间点，若未填写，默认为空。  单位：毫秒  取值范围：[0, ∞) |
| shallowDuration | number | 否 | 是 | 浅睡时长，若未填写，默认为空。  单位：秒  取值范围：[0, ∞) |
| deepDuration | number | 否 | 是 | 深睡时长，若未填写，默认为空。  单位：秒  取值范围：[0, ∞) |
| dreamDuration | number | 否 | 是 | REM时长，若未填写，默认为空。  单位：秒  取值范围：[0, ∞) |
| wakeDuration | number | 否 | 是 | 清醒时长，若未填写，默认为空。  单位：秒  取值范围：[0, ∞) |
| wakeCount | number | 否 | 是 | 清醒次数，若未填写，默认为空。  取值范围：[0, ∞) |
| onBedDuration | number | 否 | 是 | 卧床时长，若未填写，默认为空。  单位：秒  取值范围：[0, ∞) |
| recordDuration | number | 否 | 是 | 睡眠记录时长，若未填写，默认为记录结束时间减去开始时间。  单位：秒  取值范围：[0, ∞) |
| sleepEfficiency | number | 否 | 是 | 睡眠效率，若未填写，默认为空。  取值范围：[0, 100] |
| sleepScore | number | 否 | 是 | 睡眠得分，若未填写，默认为空。  取值范围：[0, 100] |
| deepSleepContinuity | number | 否 | 是 | 深睡连续性，若未填写，默认为空。  取值范围：[0, 100] |
| respiratoryQualityScore | number | 否 | 是 | 呼吸质量分，若未填写，默认为空。  取值范围：[0, 100] |
| turnOverCount | number | 否 | 是 | 翻身次数，若未填写，默认为空。  取值范围：[0, ∞) |
| sleepEndReason | number | 否 | 是 | 睡眠结束原因，若未填写，默认为空。  取值范围：[0, ∞)  取值参考如下：  0：手动结束睡眠监测  1：自动结束睡眠监测  2：中断睡眠监测  3：电量过低结束 |
| sleepSymptoms | string | 否 | 是 | 睡眠症状，若未填写，默认为空。 |
| sleepType | number | 否 | 是 | 睡眠数据类型。  取值范围：  1：科学睡眠  2：普通睡眠  3：手动输入睡眠  4：手机记录睡眠  未设置时，默认值为2。 |

## SleepDetail

PhoneTabletWearable

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| sleepSegment | [SleepSegment](health-api-healthfields.md#sleepsegment)[] | 否 | 是 | 睡眠状态采样列表，若未填写，默认设置覆盖全部睡眠时间的详情，睡眠状态值为7。 |

## SleepNap

PhoneTabletWearable

零星小睡数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| noonDuration | number | 否 | 否 | 午睡时长(零星小睡）。  单位：秒  取值范围：[0, ∞) |
| noonRecordDuration | number | 否 | 是 | 零星小睡记录时长，若未填写，默认为记录结束时间减去开始时间。  单位：秒  取值范围：[0, ∞) |

## SleepSegment

PhoneTabletWearable

睡眠状态采样数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| sleepStatus | number | 否 | 否 | 睡眠状态。  取值范围：  0：未知  1：深睡  2：浅睡  3：REM  4：清醒  5：午睡（零星小睡）  6：卧床  7：睡眠（手工） |
| endTime | number | 否 | 否 | 结束时间。  单位：毫秒  取值范围：[0, ∞) |

## SnowboardingDetail

PhoneTabletWearable

单板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| location | [Location](health-api-healthfields.md#location)[] | 否 | 是 | 位置详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |

## SnowboardingFeature

PhoneTabletWearable

单板滑雪特征数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tripTimes | number | 否 | 否 | 趟数。 |
| maxSlopePercent | number | 否 | 是 | 滑雪最大坡度百分比，若未填写，默认为空。 |
| maxSlopeDegree | number | 否 | 是 | 滑雪最大坡，若未填写，默认为空。  单位：度 |
| totalTime | number | 否 | 是 | 滑行时间，若未填写，默认为空。  单位：毫秒 |
| totalDistance | number | 否 | 是 | 滑行距离，若未填写，默认为空。  单位：米 |

## SnowboardingSummary

PhoneTabletWearable

单板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| snowboardingFeature | [SnowboardingFeature](health-api-healthfields.md#snowboardingfeature) | 否 | 否 | 单板滑雪特征数据。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## Speed

PhoneTabletWearable

速度详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| speed | number | 否 | 否 | 速度详情。  单位：米/秒  取值范围：[0, ∞) |

## SpeedSummary

PhoneTabletWearable

速度统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：米/秒  取值范围：[0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：米/秒  取值范围：[0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  单位：米/秒  取值范围：[0, ∞) |

## SportsDetail

PhoneTabletWearable

通用详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |

## SportsSummary

PhoneTabletWearable

通用统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |

## StepSummary

PhoneTabletWearable

步数统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| totalSteps | number | 否 | 否 | 步数总值。  取值范围：(0, ∞) |

## Stress

PhoneTabletWearable

压力采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| stressScore | number | 否 | 否 | 压力得分。  取值范围：[1, 99] |

## StressAggregation

PhoneTabletWearable

压力得分聚合统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| stressScore | Omit<[AggregateMetrics](health-api-healthstore.md#aggregatemetrics), 'sum'> | 否 | 否 | 压力得分聚合统计。 |

## StrokeRate

PhoneTabletWearable

桨频采样数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| spm | number | 否 | 否 | 桨频。  单位：次/分钟 |

## StrokeRateSummary

PhoneTabletWearable

桨频统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：次/分钟  取值范围: [0, ∞) |
| max | number | 否 | 否 | 最大值。  单位：次/分钟  取值范围: [0, ∞) |

## SwimStrokeRate

PhoneTabletWearable

划水频率采样数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| spm | number | 否 | 否 | 游泳划水频率。  单位：次/分钟 |

## SwimStrokeRateSummary

PhoneTabletWearable

划水频率统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  单位：次/分钟  取值范围: [0, ∞) |

## Swolf

PhoneTabletWearable

SWOLF采样数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| swolf | number | 否 | 否 | SWOLF. |

## SwolfSummary

PhoneTabletWearable

SWOLF统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| avg | number | 否 | 否 | 平均值。  取值范围: [0, ∞) |
| max | number | 否 | 否 | 最大值。  取值范围: [0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  取值范围: [0, ∞) |

## WalkingDetail

PhoneTabletWearable

健走详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields.md#exerciseheartrate)[] | 否 | 是 | 运动心率详情列表，若未填写，默认为空。 |
| speed | [Speed](health-api-healthfields.md#speed)[] | 否 | 是 | 速度详情列表，若未填写，默认为空。 |
| cadence | [Cadence](health-api-healthfields.md#cadence)[] | 否 | 是 | 步频详情列表，若未填写，默认为空。 |
| location | [Location](health-api-healthfields.md#location)[] | 否 | 是 | 位置详情列表，若未填写，默认为空。 |
| altitude | [Altitude](health-api-healthfields.md#altitude)[] | 否 | 是 | 海拔详情列表，若未填写，默认为空。 |

## WalkingSummary

PhoneTabletWearable

健走统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| distance | [DistanceSummary](health-api-healthfields.md#distancesummary) | 否 | 否 | 距离统计。 |
| calorie | [CalorieSummary](health-api-healthfields.md#caloriesummary) | 否 | 否 | 热量统计。 |
| speed | [SpeedSummary](health-api-healthfields.md#speedsummary) | 否 | 否 | 速度统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields.md#exerciseheartratesummary) | 否 | 是 | 运动心率统计，若未填写，默认为空。 |
| step | [StepSummary](health-api-healthfields.md#stepsummary) | 否 | 是 | 步数统计，若未填写，默认为空。 |
| cadence | [CadenceSummary](health-api-healthfields.md#cadencesummary) | 否 | 是 | 步频统计，若未填写，默认为空。 |
| altitude | [AltitudeSummary](health-api-healthfields.md#altitudesummary) | 否 | 是 | 海拔统计，若未填写，默认为空。 |
| location | [LocationSummary](health-api-healthfields.md#locationsummary) | 否 | 是 | 位置统计，若未填写，默认为空。 |

## WaterTemperature

PhoneTabletWearable

水温采样数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| temperature | number | 否 | 否 | 温度。  单位：摄氏度 |

## WaterTemperatureSummary

PhoneTabletWearable

水温统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| max | number | 否 | 否 | 最大值。  单位：摄氏度  取值范围: [0, ∞) |
| min | number | 否 | 是 | 最小值，若未填写，默认为空。  单位：摄氏度  取值范围: [0, ∞) |

## Weight

PhoneTabletWearable

体重采样数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bodyWeight | number | 否 | 否 | 体重。  单位：千克  取值范围：[0.1, 500] |
| bmi | number | 否 | 是 | 身体质量指数，若未填写，默认为空。  单位：千克/平方米  取值范围：[1,200] |
| bodyFat | number | 否 | 是 | 体脂量，若未填写，默认为空。  单位：千克  取值范围：[0, 500] |
| bodyFatRate | number | 否 | 是 | 体脂率，若未填写，默认为空。  单位：百分比  取值范围：[0, 100] |
| muscleMass | number | 否 | 是 | 肌肉量，若未填写，默认为空。  单位：千克  取值范围：[0.1, 150] |
| basalMetabolism | number | 否 | 是 | 基础代谢，若未填写，默认为空。  单位：千卡/天  取值范围：[0, ∞) |
| moisture | number | 否 | 是 | 水分量，若未填写，默认为空。  单位：千克  取值范围：[0, 500] |
| moistureRate | number | 否 | 是 | 水分率，若未填写，默认为空。  单位：百分比  取值范围：[0, 100] |
| visceralFatLevel | number | 否 | 是 | 内脏脂肪等级，若未填写，默认为空。  取值范围：[1, 59] |
| boneSalt | number | 否 | 是 | 骨盐量，若未填写，默认为空。  单位：千克  取值范围：[0.5, 5] |
| proteinRate | number | 否 | 是 | 蛋白质率，若未填写，默认为空。  单位：百分比  取值范围：[0, 100] |
| bodyScore | number | 否 | 是 | 身体得分，若未填写，默认为空。  单位：百分比  取值范围：[0, 100] |
| bodyAge | number | 否 | 是 | 身体年龄，若未填写，默认为空。  取值范围：[5, 99] |
| skeletalMuscleMass | number | 否 | 是 | 骨骼肌量，若未填写，默认为空。  单位：千克  取值范围：[1, 150] |
| impedance | number | 否 | 是 | 阻抗。  单位：欧姆  取值范围：[0.1, 100000] |
