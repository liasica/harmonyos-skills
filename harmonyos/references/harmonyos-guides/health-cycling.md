---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-cycling
title: 骑行
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 骑行
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:423d2dbde71a021ef3f63c3389e59531d0b6b6faf5dc26f015659085c51d3c1b
---

骑行相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.cycling.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-7) | 户外骑行 | 手机、手表、手环 |
| [exerciseSequenceHelper.indoorCycling.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-13) | 室内单车 | 室内自行车、室内骑行台 |
| [exerciseSequenceHelper.spinning.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-27) | 动感单车 | 动感单车 |
| [exerciseSequenceHelper.bmx.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-4) | BMX自行车 | 越野自行车 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.cycling.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-6)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| speed | 速度统计 | [SpeedSummary](../harmonyos-references/health-api-healthfields.md#speedsummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| resistance | 阻力统计 | [ResistanceSummary](../harmonyos-references/health-api-healthfields.md#resistancesummary) | O |
| pedalingCadence | 踏频统计 | [PedalingCadenceSummary](../harmonyos-references/health-api-healthfields.md#pedalingcadencesummary) | O |
| power | 功率统计 | [PowerSummary](../harmonyos-references/health-api-healthfields.md#powersummary) | O |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
| location | 位置统计 | [LocationSummary](../harmonyos-references/health-api-healthfields.md#locationsummary) | O |

## 关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.cycling.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-6)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| pedalingCadence | 踏频详情 | [PedalingCadence](../harmonyos-references/health-api-healthfields.md#pedalingcadence)[] | O |
| power | 功率详情 | [Power](../harmonyos-references/health-api-healthfields.md#power)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |
| resistance | 阻力详情 | [Resistance](../harmonyos-references/health-api-healthfields.md#resistance)[] | O |
