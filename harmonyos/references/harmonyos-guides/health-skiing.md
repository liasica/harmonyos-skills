---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-skiing
title: 滑雪
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 滑雪
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d934814cc1f8bccd18f700bbffe9e5544d85e23b2f8fa7c8bee2016f1a687366
---

## 冬季两项

### 冬季两项相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.biathlon.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-3) | 冬季两项 | 手环、手表 |

### 冬季两项关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.biathlon.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-2)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

### 冬季两项关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.biathlon.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-2)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |

## 滑雪

### 滑雪相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.skiing.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-24) | 滑雪 | 手环、手表 |

### 滑雪关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.skiing.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-23)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| skiingFeature | 滑雪特征数据 | [SkiingFeature](../harmonyos-references/health-api-healthfields.md#skiingfeature) | M |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

### 滑雪关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.skiing.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-23)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |

## 单板滑雪

### 单板滑雪相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.snowboarding.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-26) | 单板滑雪 | 手环、手表 |

### 单板滑雪关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.snowboarding.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-25)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| distance | 距离统计 | [DistanceSummary](../harmonyos-references/health-api-healthfields.md#distancesummary) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| snowboardingFeature | 单板滑雪特征数据 | [SnowboardingFeature](../harmonyos-references/health-api-healthfields.md#snowboardingfeature) | M |
| altitude | 海拔统计 | [AltitudeSummary](../harmonyos-references/health-api-healthfields.md#altitudesummary) | O |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

### 单板滑雪关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.snowboarding.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-25)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
| location | 位置详情 | [Location](../harmonyos-references/health-api-healthfields.md#location)[] | O |
| altitude | 海拔详情 | [Altitude](../harmonyos-references/health-api-healthfields.md#altitude)[] | O |

## 滑雪橇

### 滑雪橇相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.sled.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-25) | 滑雪橇 | 手环、手表 |

### 滑雪橇关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.sled.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-24)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

### 滑雪橇关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.sled.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-24)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| speed | 速度详情 | [Speed](../harmonyos-references/health-api-healthfields.md#speed)[] | O |
