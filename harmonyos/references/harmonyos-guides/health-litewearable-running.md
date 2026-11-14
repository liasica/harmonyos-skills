---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-running
title: 户外跑步
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 锻炼记录数据 > 户外跑步
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:030e1c7fe6a6f03b375be3d134db248103ce52133d007b6552d8cfca347a26f3
---

从API版本26.0.1开始，支持该数据类型开放。

户外跑步相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.running.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-14) | 户外跑步 | 轻量级智能穿戴（运动表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.running.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-13)

| **字段**列表 | 描述 | 类型 | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
| heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
| trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
| trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
| recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
| calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |
| speed | 速度统计。 | [SpeedSummary](../harmonyos-references/health-api-healthfields-lite.md#speedsummary) | M |
| cadence | 步频统计。 | [CadenceSummary](../harmonyos-references/health-api-healthfields-lite.md#cadencesummary) | M |
| step | 步数统计。 | [StepSummary](../harmonyos-references/health-api-healthfields-lite.md#stepsummary) | M |
| altitude | 海拔统计。 | [AltitudeSummary](../harmonyos-references/health-api-healthfields-lite.md#altitudesummary) | M |
| distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields-lite.md#distancesummary) | M |
| analogPower | 模拟功率统计。 | [AnalogPowerSummary](../harmonyos-references/health-api-healthfields-lite.md#analogpowersummary) | O |
| runningForm | 跑姿统计。 | [RunningFormSummary](../harmonyos-references/health-api-healthfields-lite.md#runningformsummary) | O |
| runPaceZone | 配速区间统计。 | [RunPaceZoneSummary](../harmonyos-references/health-api-healthfields-lite.md#runpacezonesummary) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.running.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#detailfields-13)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartrate)[] | O |
