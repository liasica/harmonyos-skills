---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-jumping-rope
title: 跳绳
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 跳绳
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f02580430760a3ad9a5f68a70146618ab90af092161447e0d4a3fbe7290e47fc
---

跳绳相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.jumpingRope.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量-16) | 跳绳 | AI跳绳、智能跳绳设备 |

## 关联的统计数据说明

* 字段定义：[exerciseSequenceHelper.jumpingRope.SummaryFields](../harmonyos-references/health-api-exercisedequencehelper.md#summaryfields-15)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| jumpingRopeFeature | 跳绳特征数据 | [JumpingRopeFeature](../harmonyos-references/health-api-healthfields.md#jumpingropefeature) | M |
| calorie | 热量统计 | [CalorieSummary](../harmonyos-references/health-api-healthfields.md#caloriesummary) | M |
| skipSpeed | 跳跃速度统计 | [SkipSpeedSummary](../harmonyos-references/health-api-healthfields.md#skipspeedsummary) | M |
| exerciseHeartRate | 运动心率统计 | [ExerciseHeartRateSummary](../harmonyos-references/health-api-healthfields.md#exerciseheartratesummary) | O |

## 关联的明细数据说明

* 字段定义：[exerciseSequenceHelper.jumpingRope.DetailFields](../harmonyos-references/health-api-exercisedequencehelper.md#detailfields-15)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields.md#exerciseheartrate)[] | O |
| skipSpeed | 跳跃速度详情 | [SkipSpeed](../harmonyos-references/health-api-healthfields.md#skipspeed)[] | O |
