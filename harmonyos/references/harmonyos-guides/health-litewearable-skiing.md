---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-skiing
title: 滑雪
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 锻炼记录数据 > 滑雪
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:21+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:c8f0f64d5240be6809e027261bed43b9f34baadbb0520239c77850d21b8ec3cc
---

从API版本26.0.1开始，支持该数据类型开放。

滑雪相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.outdoorSnowboard.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-7) | 户外单板 | 轻量级智能穿戴（运动表） |
| [exerciseSequenceHelper.outdoorSkiing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-8) | 户外双板 | 轻量级智能穿戴（运动表） |
| [exerciseSequenceHelper.indoorSnowboard.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-9) | 室内单板 | 轻量级智能穿戴（运动表） |
| [exerciseSequenceHelper.indoorSkiing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-10) | 室内双板 | 轻量级智能穿戴（运动表） |
| [exerciseSequenceHelper.crossCountrySkiing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-11) | 越野滑雪 | 轻量级智能穿戴（运动表） |
| [exerciseSequenceHelper.skiMountaineering.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-12) | 滑雪登山 | 轻量级智能穿戴（运动表） |

## 关联的统计数据说明

* 户外单板字段定义：[exerciseSequenceHelper.outdoorSnowboard.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-6)
* 户外双板字段定义：[exerciseSequenceHelper.outdoorSkiing.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-7)

  | **字段**列表 | 描述 | **类型** | 可选/必选 |
  | --- | --- | --- | --- |
  | skiDuration | 滑雪时长统计。 | [SkiDurationSummary](../harmonyos-references/health-api-healthfields-lite.md#skidurationsummary) | M |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields-lite.md#distancesummary) | M |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields-lite.md#skispeedsummary) | M |
  | tripTimes | 滑雪趟数统计。 | [SkiTripTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#skitriptimesummary) | M |
  | incline | 滑雪坡度统计。 | [InclineSummary](../harmonyos-references/health-api-healthfields-lite.md#inclinesummary) | M |
  | turns | 转弯统计。 | [TurnsSummary](../harmonyos-references/health-api-healthfields-lite.md#turnssummary) | M |
  | gForce | G-Force统计。 | [GForceSummary](../harmonyos-references/health-api-healthfields-lite.md#gforcesummary) | M |
  | altitude | 海拔统计。 | [AltitudeSummary](../harmonyos-references/health-api-healthfields-lite.md#altitudesummary) | M |
  | skiPisteRegion | 雪道区域统计。 | [SkiPisteRegionSummary](../harmonyos-references/health-api-healthfields-lite.md#skipisteregionsummary) | M |
  | temperature | 温度统计。 | [TemperatureSummary](../harmonyos-references/health-api-healthfields-lite.md#temperaturesummary) | M |
  | runwayRatio | 雪道统计。 | [RunwayRatioSummary](../harmonyos-references/health-api-healthfields-lite.md#runwayratiosummary) | M |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields-lite.md#skitechstatssummary) | M |
* 室内单板字段定义：[exerciseSequenceHelper.indoorSnowboard.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-8)
* 室内双板字段定义：[exerciseSequenceHelper.indoorSkiing.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-9)

  | **字段**列表 | 描述 | 类型 | 可选/必选 |
  | --- | --- | --- | --- |
  | skiDuration | 滑雪时长统计。 | [SkiDurationSummary](../harmonyos-references/health-api-healthfields-lite.md#skidurationsummary) | M |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields-lite.md#distancesummary) | M |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields-lite.md#skispeedsummary) | M |
  | tripTimes | 滑雪趟数统计。 | [SkiTripTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#skitriptimesummary) | M |
  | incline | 滑雪坡度统计。 | Omit<[InclineSummary](../harmonyos-references/health-api-healthfields-lite.md#inclinesummary), ‘avgSlopeDegree’ |‘avgUphillSlope’ | ‘avgDownhillSlope’> | M |
  | turns | 转弯统计。 | Omit<[TurnsSummary](../harmonyos-references/health-api-healthfields-lite.md#turnssummary), ‘totalTurnNumber’> | M |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields-lite.md#skitechstatssummary) | M |
* 越野滑雪字段定义：[exerciseSequenceHelper.crossCountrySkiing.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-10)

  | **字段**列表 | 描述 | 类型 | 可选/必选 |
  | --- | --- | --- | --- |
  | 字段列表 | 描述 | 类型 | 可选/必选 |
  | -------- | -------- | -------- | -------- |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields-lite.md#distancesummary) | M |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields-lite.md#skispeedsummary) | M |
  | altitude | 海拔统计。 | [AltitudeSummary](../harmonyos-references/health-api-healthfields-lite.md#altitudesummary) | M |
  | temperature | 温度统计。 | [TemperatureSummary](../harmonyos-references/health-api-healthfields-lite.md#temperaturesummary) | M |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields-lite.md#skitechstatssummary) | M |
* 滑雪登山字段定义：[exerciseSequenceHelper.skiMountaineering.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-11)

  | **字段**列表 | 描述 | 类型 | 可选/必选 |
  | --- | --- | --- | --- |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields-lite.md#distancesummary) | M |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields-lite.md#skispeedsummary) | M |
  | incline | 滑雪坡度统计。 | Omit<[InclineSummary](../harmonyos-references/health-api-healthfields-lite.md#inclinesummary), maxSlopeDegree | avgSlopeDegree> | M |
  | altitude | 海拔统计。 | [AltitudeSummary](../harmonyos-references/health-api-healthfields-lite.md#altitudesummary) | M |
  | temperature | 温度统计。 | [TemperatureSummary](../harmonyos-references/health-api-healthfields-lite.md#temperaturesummary) | M |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields-lite.md#skitechstatssummary) | M |

## 关联的明细数据说明

* 户外单板字段定义：[exerciseSequenceHelper.outdoorSnowboard.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-6)
* 户外双板字段定义：[exerciseSequenceHelper.outdoorSkiing.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-7)
* 室内单板字段定义：[exerciseSequenceHelper.indoorSnowboard.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-8)
* 室内双板字段定义：[exerciseSequenceHelper.indoorSkiing.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-9)
* 越野滑雪字段定义：[exerciseSequenceHelper.crossCountrySkiing.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-10)
* 滑雪登山字段定义：[exerciseSequenceHelper.skiMountaineering.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-11)

  | **字段**列表 | 描述 | **类型** | 可选/必选 |
  | --- | --- | --- | --- |
  | exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
