---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-breath-holding-train
title: 潜水闭气训练
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 潜水闭气训练
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:27+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:e7f2ca3ff246eb7e0d60cb0aff6d67f6523049f96a686e55704aedf33e24b50f
---

潜水闭气训练相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.breathHoldingTrain.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-6) | 潜水闭气训练 | 部分专业手表、手环 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.breathHoldingTrain.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-5)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| breathHoldingTrainFeature | 潜水闭气训练特征数据 | [BreathHoldingTrainFeature](../harmonyos-references/health-api-healthfields.md#breathholdingtrainfeature) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

## 关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.breathHoldingTrain.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-5)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
