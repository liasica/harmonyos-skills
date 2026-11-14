---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-skiing
title: 滑雪
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Wearable应用开发 > 开放数据类型 > 锻炼记录数据 > 滑雪
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:7921140657c6911e8ef5159f431ab4d4227e11bb0b365311a7d050f577343469
---

从API版本26.0.1开始，支持该数据类型开放。

滑雪相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.outdoorSnowboard.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-31) | 户外单板 | 智能穿戴（智能表） |
| [exerciseSequenceHelper.outdoorSkiing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-32) | 户外双板 | 智能穿戴（智能表） |
| [exerciseSequenceHelper.indoorSnowboard.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-33) | 室内单板 | 智能穿戴（智能表） |
| [exerciseSequenceHelper.indoorSkiing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-34) | 室内双板 | 智能穿戴（智能表） |
| [exerciseSequenceHelper.crossCountrySkiing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-35) | 越野滑雪 | 智能穿戴（智能表） |
| [exerciseSequenceHelper.skiMountaineering.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-36) | 滑雪登山 | 智能穿戴（智能表） |

## 关联的统计数据说明

* 户外单板字段定义：[exerciseSequenceHelper.outdoorSnowboard.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-30)
* 户外双板字段定义：[exerciseSequenceHelper.outdoorSkiing.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-31)

  | **字段**列表 | 描述 | **类型** | 可选/必选 |
  | --- | --- | --- | --- |
  | skiDuration | 滑雪时长统计。 | [SkiDurationSummary](../harmonyos-references/health-api-healthfields.md#skidurationsummary) | O |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields.md#heartratezonessummary) | O |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields.md#trainingloadsummary) | O |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields.md#trainingstresssummary) | O |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields.md#recoverytimesummary) | O |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | O |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | O |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields.md#skispeedsummary) | O |
  | tripTimes | 滑雪趟数统计。 | [SkiTripTimeSummary](../harmonyos-references/health-api-healthfields.md#skitriptimesummary) | O |
  | incline | 滑雪坡度统计。 | Omit<[InclineSummary](../harmonyos-references/health-api-healthfields.md#inclinesummary), ‘avgSlopeDegree’ |‘avgUphillSlope’ | ‘avgDownhillSlope’> | O |
  | turns | 转弯统计。 | Omit<[TurnsSummary](../harmonyos-references/health-api-healthfields.md#turnssummary), ‘totalTurnNumber’> | O |
  | gForce | G-Force统计。 | [GForceSummary](../harmonyos-references/health-api-healthfields.md#gforcesummary) | O |
  | altitude | 海拔统计。 | Omit<[AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary), ‘totalAscent’> | O |
  | skiPisteRegion | 雪道区域统计。 | [SkiPisteRegionSummary](../harmonyos-references/health-api-healthfields.md#skipisteregionsummary) | O |
  | temperature | 温度统计。 | [TemperatureSummary](../harmonyos-references/health-api-healthfields.md#temperaturesummary) | O |
  | runwayRatio | 雪道统计。 | [RunwayRatioSummary](../harmonyos-references/health-api-healthfields.md#runwayratiosummary) | O |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields.md#skitechstatssummary) | O |
* 室内单板字段定义：[exerciseSequenceHelper.indoorSnowboard.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-32)
* 室内双板字段定义：[exerciseSequenceHelper.indoorSkiing.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-33)

  | **字段**列表 | 描述 | 类型 | 可选/必选 |
  | --- | --- | --- | --- |
  | skiDuration | 滑雪时长统计。 | [SkiDurationSummary](../harmonyos-references/health-api-healthfields.md#skidurationsummary) | O |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields.md#heartratezonessummary) | O |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields.md#trainingloadsummary) | O |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields.md#trainingstresssummary) | O |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields.md#recoverytimesummary) | O |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | O |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | O |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields.md#skispeedsummary) | O |
  | tripTimes | 滑雪趟数统计。 | [SkiTripTimeSummary](../harmonyos-references/health-api-healthfields.md#skitriptimesummary) | O |
  | incline | 滑雪坡度统计。 | Omit<[InclineSummary](../harmonyos-references/health-api-healthfields.md#inclinesummary), ‘avgSlopeDegree’ | ‘avgUphillSlope’ | ‘avgDownhillSlope’> | O |
  | turns | 转弯统计。 | Omit<[TurnsSummary](../harmonyos-references/health-api-healthfields.md#turnssummary), ‘totalTurnNumber’> | O |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields.md#skitechstatssummary) | O |
* 越野滑雪字段定义：[exerciseSequenceHelper.crossCountrySkiing.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-34)

  | **字段**列表 | 描述 | 类型 | 可选/必选 |
  | --- | --- | --- | --- |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields.md#heartratezonessummary) | O |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields.md#trainingloadsummary) | O |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields.md#trainingstresssummary) | O |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields.md#recoverytimesummary) | O |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | O |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | O |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields.md#skispeedsummary) | O |
  | altitude | 海拔统计。 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
  | temperature | 温度统计。 | [TemperatureSummary](../harmonyos-references/health-api-healthfields.md#temperaturesummary) | O |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields.md#skitechstatssummary) | O |
* 滑雪登山字段定义：[exerciseSequenceHelper.skiMountaineering.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-35)

  | **字段**列表 | 描述 | 类型 | 可选/必选 |
  | --- | --- | --- | --- |
  | exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
  | heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields.md#heartratezonessummary) | O |
  | trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields.md#trainingloadsummary) | O |
  | trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields.md#trainingstresssummary) | O |
  | recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields.md#recoverytimesummary) | O |
  | calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | O |
  | distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | O |
  | speed | 滑雪速度统计。 | [SkiSpeedSummary](../harmonyos-references/health-api-healthfields.md#skispeedsummary) | O |
  | incline | 滑雪坡度统计。 | Omit<[InclineSummary](../harmonyos-references/health-api-healthfields.md#inclinesummary), ‘maxSlopeDegree’ | ‘avgSlopeDegree’> | O |
  | altitude | 海拔统计。 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
  | temperature | 温度统计。 | [TemperatureSummary](../harmonyos-references/health-api-healthfields.md#temperaturesummary) | O |
  | skiTechStats | 滑雪技术数据统计。 | [SkiTechStatsSummary](../harmonyos-references/health-api-healthfields.md#skitechstatssummary) | O |

## 关联的明细数据说明

* 户外单板字段定义：[exerciseSequenceHelper.outdoorSnowboard.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-30)
* 户外双板字段定义：[exerciseSequenceHelper.outdoorSkiing.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-31)
* 室内单板字段定义：[exerciseSequenceHelper.indoorSnowboard.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-32)
* 室内双板字段定义：[exerciseSequenceHelper.indoorSkiing.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-33)
* 越野滑雪字段定义：[exerciseSequenceHelper.crossCountrySkiing.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-34)
* 滑雪登山字段定义：[exerciseSequenceHelper.skiMountaineering.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-35)

  | **字段**列表 | 描述 | **类型** | 可选/必选 |
  | --- | --- | --- | --- |
  | exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
