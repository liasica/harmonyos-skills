---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-breath-holding-test
title: 潜水闭气测试
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 潜水闭气测试
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fed3a9473a5e7afecf8a36f6a4c06019ce175c28e8b10d6d4503c006fde780fd
---

潜水闭气测试相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.breathHoldingTest.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-5) | 潜水闭气测试 | 部分专业手表、手环 |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.breathHoldingTest.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-4)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| breathHoldingTestFeature | 潜水闭气测试特征数据 | [BreathHoldingTestFeature](../harmonyos-references/health-api-healthfields.md#breathholdingtestfeature) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.breathHoldingTest.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-4)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
