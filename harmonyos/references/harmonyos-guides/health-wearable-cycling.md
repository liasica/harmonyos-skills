---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-cycling
title: 户外骑行
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Wearable应用开发 > 开放数据类型 > 锻炼记录数据 > 户外骑行
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:05e593dd5fb436a7bd4dc234cfedae7334505201fafa3961f57fd5986e8c7ab7
---

从API版本5.1.1(19)开始，支持该数据类型开放。

户外骑行相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.cycling.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-7) | 户外骑行 | 智能穿戴（智能表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.cycling.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-6)

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
| resistance | 阻力统计 | [ResistanceSummary](../harmonyos-references/health-api-healthfields.md#resistancesummary) | O |
| pedalingCadence | 踏频统计 | [PedalingCadenceSummary](../harmonyos-references/health-api-healthfields.md#pedalingcadencesummary) | O |
| power | 功率统计 | [PowerSummary](../harmonyos-references/health-api-healthfields.md#powersummary) | O |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
| location | 位置统计 | [LocationSummary](../harmonyos-references/health-api-healthfields.md#locationsummary) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.cycling.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-6)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| pedalingCadence | 踏频详情 | [PedalingCadence](../harmonyos-references/health-api-healthfields.md#pedalingcadence)[] | O |
| power | 功率详情 | [Power](../harmonyos-references/health-api-healthfields.md#power)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |
| resistance | 阻力详情 | [Resistance](../harmonyos-references/health-api-healthfields.md#resistance)[] | O |
