---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-adventures
title: 户外探险
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 户外探险
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4111c3b614eaa457957f79994f56807fc06714e864db5aa7a1afca1bc682aae
---

户外探险相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.adventures.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-1) | 户外探险 | 部分专业手表 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.adventures.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| step | 步数统计 | [StepSummary](../harmonyos-references/health-api-healthfields.md#stepsummary) | O |
| cadence | 步频统计 | [CadenceSummary](../harmonyos-references/health-api-healthfields.md#cadencesummary) | O |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |

## 关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.adventures.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| markPoint | 标记点采样详情 | [MarkPoint](../harmonyos-references/health-api-healthfields.md#markpoint)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |
