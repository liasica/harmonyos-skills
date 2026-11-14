---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-strengthtraining
title: 力量训练
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Wearable应用开发 > 开放数据类型 > 锻炼记录数据 > 力量训练
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:abcb85e151abe4c79102520d4bbbb700c5e00d62d5f8252e8bc547d6cac941e7
---

从API版本26.0.1开始，支持该数据类型开放。

力量训练相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.strengthTraining.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-40) | 力量训练 | 智能穿戴（智能表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.strengthTraining.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-39)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields.md#heartratezonessummary) | O |
| trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields.md#trainingloadsummary) | O |
| trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields.md#trainingstresssummary) | O |
| recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields.md#recoverytimesummary) | O |
| calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | O |
| trainingVolume | 训练容量统计。 | [TrainingVolumeSummary](../harmonyos-references/health-api-healthfields.md#trainingvolumesummary) | O |
| rpe | 主观疲劳等级统计。 | [RpeSummary](../harmonyos-references/health-api-healthfields.md#rpesummary) | O |
| actions | 训练动作统计。 | [ActionsSummary](../harmonyos-references/health-api-healthfields.md#actionssummary) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.strengthTraining.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-39)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
