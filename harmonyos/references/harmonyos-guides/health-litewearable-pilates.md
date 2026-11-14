---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-pilates
title: 普拉提
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 锻炼记录数据 > 普拉提
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:4fdf21a5f362d78f23904663b8b2df0a5714a2fe26394726939d238f85a3ab51
---

从API版本26.0.1开始，支持该数据类型开放。

普拉提相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.pilates.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-15) | 普拉提 | 轻量级智能穿戴（运动表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.pilates.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-14)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
| heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
| trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
| trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
| recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
| calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.pilates.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#detailfields-14)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartrate)[] | O |
