---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-rower
title: 划船机
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 划船机
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45e9b0df691ff9ad116f198387537d83f752b506ccd6f0d943faecade2821768
---

## 划船机

### 划船机相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.rower.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-20) | 划船机 | 划船机等专业设备 |

### 划船机关联的统计数据说明

字段定义：[exerciseSequenceHelper.rower.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-19)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| rowerFeature | 划船机特征数据 | [RowerFeature](../harmonyos-references/health-api-healthfields.md#rowerfeature) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | O |
| speed | 速度统计 | [SpeedSummary](../harmonyos-references/health-api-healthfields.md#speedsummary) | O |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| resistance | 阻力统计 | [ResistanceSummary](../harmonyos-references/health-api-healthfields.md#resistancesummary) | O |
| power | 功率统计 | [PowerSummary](../harmonyos-references/health-api-healthfields.md#powersummary) | O |
| strokeRate | 桨频统计 | [StrokeRateSummary](../harmonyos-references/health-api-healthfields.md#strokeratesummary) | O |

### 划船机关联的明细数据说明

字段定义：[exerciseSequenceHelper.rower.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-19)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| power | 功率详情 | [Power](../harmonyos-references/health-api-healthfields.md#power)[] | O |
| resistance | 阻力详情 | [Resistance](../harmonyos-references/health-api-healthfields.md#resistance)[] | O |
| strokeRate | 桨频详情 | [StrokeRate](../harmonyos-references/health-api-healthfields.md#strokerate)[] | O |

## 赛艇

### 赛艇相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.rowing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-21) | 赛艇 | 手环、手表 |

### 赛艇关联的统计数据说明

字段定义：[exerciseSequenceHelper.rowing.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-20)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| rowingFeature | 赛艇特征数据 | [RowingFeature](../harmonyos-references/health-api-healthfields.md#rowingfeature) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | O |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| strokeRate | 桨频统计 | [StrokeRateSummary](../harmonyos-references/health-api-healthfields.md#strokeratesummary) | O |

### 赛艇关联的明细数据说明

字段定义：[exerciseSequenceHelper.rowing.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-20)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| strokeRate | 桨频详情 | [StrokeRate](../harmonyos-references/health-api-healthfields.md#strokerate)[] | O |
