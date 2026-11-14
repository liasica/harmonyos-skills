---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-running
title: 户外跑步
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Wearable应用开发 > 开放数据类型 > 锻炼记录数据 > 户外跑步
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:1c3fcd3899b84bab222bdc2b1d49d23299f2b5745ba3b4f1a149cd4e81d0bd0d
---

从API版本5.1.1(19)开始，支持该数据类型开放。

户外跑步相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.running.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-22) | 户外跑步 | 智能穿戴（智能表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.running.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-21)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| speed | 速度统计 | [SpeedSummary](../harmonyos-references/health-api-healthfields.md#speedsummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| trainingLoad | 训练负荷统计。  **起始版本：** 26.0.1。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields.md#trainingloadsummary) | O |
| trainingStress | 训练压力统计。  **起始版本：** 26.0.1。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields.md#trainingstresssummary) | O |
| recoveryTime | 恢复时间统计。  **起始版本：** 26.0.1。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields.md#recoverytimesummary) | O |
| heartRateZone | 心率区间统计。  **起始版本：** 26.0.1。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields.md#heartratezonessummary) | O |
| step | 步数统计 | [StepSummary](../harmonyos-references/health-api-healthfields.md#stepsummary) | O |
| cadence | 步频统计 | [CadenceSummary](../harmonyos-references/health-api-healthfields.md#cadencesummary) | O |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
| location | 位置统计 | [LocationSummary](../harmonyos-references/health-api-healthfields.md#locationsummary) | O |
| runningForm | 跑姿统计 | [RunningFormSummary](../harmonyos-references/health-api-healthfields.md#runningformsummary) | O |
| runningFeature | 跑步特征数据 | [RunningFeature](../harmonyos-references/health-api-healthfields.md#runningfeature) | O |
| analogPower | 模拟功率统计。  **起始版本：** 26.0.1。 | [AnalogPowerSummary](../harmonyos-references/health-api-healthfields.md#analogpowersummary) | O |
| runPaceZone | 配速区间统计。  **起始版本：** 26.0.1。 | [RunPaceZoneSummary](../harmonyos-references/health-api-healthfields.md#runpacezonesummary) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.running.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-21)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| cadence | 步频详情 | [Cadence](../harmonyos-references/health-api-healthfields.md#cadence)[] | O |
| runningForm | 跑姿详情 | [RunningForm](../harmonyos-references/health-api-healthfields.md#runningform)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |
