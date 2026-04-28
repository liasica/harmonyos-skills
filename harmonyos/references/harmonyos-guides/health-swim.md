---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-swim
title: 游泳
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 游泳
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8921b175fd72240cfa37dcfdb2136641ecb069c51d26d1ed8f3b4b08722fe8d5
---

## 开放水域游泳

### 开放水域游泳相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.openWaterSwim.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-18) | 开放水域游泳 | 手环、手表 |

### 开放水域游泳关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.openWaterSwim.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-17)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| openWaterSwimFeature | 开放水域游泳特征数据 | [OpenWaterSwimFeature](../harmonyos-references/health-api-healthfields.md#openwaterswimfeature) | M |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| swimStrokeRate | 划水频率统计 | [SwimStrokeRateSummary](../harmonyos-references/health-api-healthfields.md#swimstrokeratesummary) | O |
| swolf | SWOLF统计 | [SwolfSummary](../harmonyos-references/health-api-healthfields.md#swolfsummary) | O |

### 开放水域游泳关联的明细数据说明

字段定义：[exerciseSequenceHelper.openWaterSwim.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-17)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| swimStrokeRate | 划水频率详情 | [SwimStrokeRate](../harmonyos-references/health-api-healthfields.md#swimstrokerate)[] | O |
| swolf | SWOLF详情 | [Swolf](../harmonyos-references/health-api-healthfields.md#swolf)[] | O |

## 泳池游泳

### 泳池游泳相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.poolSwim.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-19) | 泳池游泳 | 手环、手表 |

### 泳池游泳关联的统计数据说明

字段定义：[exerciseSequenceHelper.poolSwim.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-18)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| poolSwimFeature | 泳池游泳特征数据 | [PoolSwimFeature](../harmonyos-references/health-api-healthfields.md#poolswimfeature) | M |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |
| speed | 速度统计 | [SpeedSummary](../harmonyos-references/health-api-healthfields.md#speedsummary) | O |
| swimStrokeRate | 划水频率统计 | [SwimStrokeRateSummary](../harmonyos-references/health-api-healthfields.md#swimstrokeratesummary) | O |
| swolf | SWOLF统计 | [SwolfSummary](../harmonyos-references/health-api-healthfields.md#swolfsummary) | O |

### 泳池游泳关联的明细数据说明

字段定义：[exerciseSequenceHelper.poolSwim.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-18)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| swimStrokeRate | 划水频率详情 | [SwimStrokeRate](../harmonyos-references/health-api-healthfields.md#swimstrokerate)[] | O |
| swolf | SWOLF详情 | [Swolf](../harmonyos-references/health-api-healthfields.md#swolf)[] | O |
