---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-walking
title: 健走
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 健走
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2a06c1983f44db1e9db96b7ce2452a7bb7079b3ea75a4931b6825d88af1c911
---

健走相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.walking.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-30) | 户外步行 | 手机、手表、手环 |
| [exerciseSequenceHelper.indoorWalking.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-15) | 室内步行 | 漫步机 |
| [exerciseSequenceHelper.hiking.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-12) | 徒步/远足 | 手机、手表、手环 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.walking.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-29)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| speed | 速度统计 | [SpeedSummary](../harmonyos-references/health-api-healthfields.md#speedsummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| step | 步数统计 | [StepSummary](../harmonyos-references/health-api-healthfields.md#stepsummary) | O |
| cadence | 步频统计 | [CadenceSummary](../harmonyos-references/health-api-healthfields.md#cadencesummary) | O |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
| location | 位置统计 | [LocationSummary](../harmonyos-references/health-api-healthfields.md#locationsummary) | O |

## 关联的详情数据说明

* 字段定义：[exerciseSequenceHelper.walking.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-29)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| cadence | 步频详情 | [Cadence](../harmonyos-references/health-api-healthfields.md#cadence)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |
