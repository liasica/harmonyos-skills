---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-freetraining
title: 自由训练
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Wearable应用开发 > 开放数据类型 > 锻炼记录数据 > 自由训练
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:d4d8daaefd95c852481057b550b665debf01180bf3ed189947b66cb023ef318a
---

从API版本26.0.1开始，支持该数据类型开放。

自由训练相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.freeTraining.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-39) | 自由训练 | 智能穿戴（智能表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.freeTraining.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-38)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields.md#heartratezonessummary) | O |
| trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields.md#trainingloadsummary) | O |
| trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields.md#trainingstresssummary) | O |
| recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields.md#recoverytimesummary) | O |
| calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.freeTraining.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-38)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
