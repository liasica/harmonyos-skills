---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-mountain-hike
title: 登山
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 登山
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:572bb9cf473e9e1a35bbc82cc3311942cb92e7320bc904401d67f3ad09342445
---

登山相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.mountainHike.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-17) | 登山 | 手环、手表 |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.mountainHike.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-16)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| step | 步数统计 | [StepSummary](../harmonyos-references/health-api-healthfields.md#stepsummary) | O |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.mountainHike.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-16)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |
