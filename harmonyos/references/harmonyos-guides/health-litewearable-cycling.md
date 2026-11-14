---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-cycling
title: 户外骑行
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 锻炼记录数据 > 户外骑行
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:281f23f16f92284f416a908419d0f0512df991fa454c2ffe995f80b3117f8141
---

从API版本26.0.1开始，支持该数据类型开放。

户外骑行相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.cycling.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-17) | 户外骑行 | 轻量级智能穿戴（运动表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.cycling.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-16)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
| heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
| trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
| trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
| recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
| calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |
| speed | 速度统计。 | [SpeedSummary](../harmonyos-references/health-api-healthfields-lite.md#speedsummary) | M |
| altitude | 海拔统计。 | [AltitudeSummary](../harmonyos-references/health-api-healthfields-lite.md#altitudesummary) | M |
| distance | 距离统计。 | [DistanceSummary](../harmonyos-references/health-api-healthfields-lite.md#distancesummary) | M |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.cycling.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#detailfields-16)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartrate)[] | O |
