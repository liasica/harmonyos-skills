---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-padel
title: 笼式网球
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 锻炼记录数据 > 笼式网球
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:21+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:ff25ff73c58e483760cdf7005e9399cbabdb273196616ee4fbd5c94d63ddad06
---

从API版本26.0.1开始，支持该数据类型开放。

笼式网球相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.padel.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-13) | 笼式网球 | 轻量级智能穿戴（运动表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.padel.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields-12)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率统计。 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartratesummary) | O |
| heartRateZone | 心率区间统计。 | [HeartRateZonesSummary](../harmonyos-references/health-api-healthfields-lite.md#heartratezonessummary) | M |
| trainingLoad | 训练负荷统计。 | [TrainingLoadSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingloadsummary) | M |
| trainingStress | 训练压力统计。 | [TrainingStressSummary](../harmonyos-references/health-api-healthfields-lite.md#trainingstresssummary) | M |
| recoveryTime | 恢复时间统计。 | [RecoveryTimeSummary](../harmonyos-references/health-api-healthfields-lite.md#recoverytimesummary) | M |
| calorie | 热量统计。 | [CalorieSummary](../harmonyos-references/health-api-healthfields-lite.md#caloriesummary) | M |
| serve | 发球统计。 | [ServeSummary](../harmonyos-references/health-api-healthfields-lite.md#servesummary) | M |
| swingSpeed | 挥拍速度统计。 | [SwingSpeedSummary](../harmonyos-references/health-api-healthfields-lite.md#swingspeedsummary) | M |
| padelFeature | 笼式网球特征统计。 | [PadelFeature](../harmonyos-references/health-api-healthfields-lite.md#padelfeature) | M |
| techStats | 技术数据统计。 | [TechStatsSummary](../harmonyos-references/health-api-healthfields-lite.md#techstatssummary) | M |
| scoreStats | 得分数据统计。 | [ScoreStatsSummary](../harmonyos-references/health-api-healthfields-lite.md#scorestatssummary) | M |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.padel.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#detailfields-12)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartrate)[] | O |
