---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-basketball
title: 篮球
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 篮球
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:27+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:34ac5b2d37ddca89c50cac77c3e039be7952c655c8b06d9d43a014a5981b1bf6
---

篮球相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.basketball.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量-2) | 篮球 | 篮球精灵手环 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.basketball.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper.md#summaryfields-1)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| basketballFeature | 篮球特征数据 | [BasketballFeature](../harmonyos-references/health-api-healthfields.md#basketballfeature) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| jump | 跳跃统计 | [JumpSummary](../harmonyos-references/health-api-healthfields.md#jumpsummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

## 关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.basketball.DetailFields](../harmonyos-references/health-api-exercisesequencehelper.md#detailfields-1)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| jump | 跳跃详情 | [Jump](../harmonyos-references/health-api-healthfields.md#jump)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
