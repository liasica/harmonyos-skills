---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-badminton
title: 羽毛球
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 锻炼记录数据 > 羽毛球
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:21+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:ab2073b4c872bcde23bf3678f3ee560c0955e9a55f60d0cb5b9280512dbfa2d8
---

从API版本6.1.1(24)开始，支持该数据类型开放。

羽毛球相关锻炼记录类型如下：

| **锻炼记录子类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [exerciseSequenceHelper.badminton.EXERCISE\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量-1) | 羽毛球 | 轻量级智能穿戴（运动表） |

## 关联的统计数据说明

字段定义：[exerciseSequenceHelper.badminton.SummaryFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#summaryfields)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| startTime | 运动开始时间，Unix时间戳，单位：ms。 | number | M |
| totalTime | 运动总时长，单位：s。 | number | M |
| targetDuration | 目标运动时长，单位：s，默认值：0。 | number | O |
| avgHeartRate | 运动全程平均心率，单位：bpm，默认值：0。 | number | O |
| maxHeartRate | 运动过程最高心率，单位：bpm，默认值：0。 | number | O |
| mHeartrateZoneType | 心率区间类型，0为最大心率区间，1为储备心率区间，默认值：0。 | number | O |
| startHeartRate | 恢复心率测量初始时的心率，单位：bpm，默认值：0。 | number | O |
| endHeartRate | 恢复心率测量结束时的心率，单位：bpm，默认值：0。 | number | O |
| loadPeakLevel | 运动负荷峰值等级，等级越大运动效果越好，默认值：0。 | number | O |
| aerobicTrainingStress | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 | number | O |
| anaerobicTrainingStress | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 | number | O |
| recoveryTime | 预估恢复时间，单位：h，默认值：0。 | number | O |
| totalCalories | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 | number | M |
| activeCalorie | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 | number | M |
| avgShotSpeed | 平均击球速度，单位：km/h，取值范围：[0,500]，默认值：0。 | number | O |
| maxShotSpeed | 最高击球速度，单位：km/h，取值范围：[0,500]，默认值：0。 | number | O |
| shots | 总击球次数，取值范围：[0,20000]，默认值：0。 | number | O |
| maxContinuousRally | 最长连续对打回合数，取值范围：[0,10000]，默认值：0。 | number | O |
| forehandStroke | 正手击球次数，取值范围：[0,10000]，默认值：0。 | number | O |
| backhandStroke | 反手击球次数，取值范围：[0,10000]，默认值：0。 | number | O |
| overhandStroke | 上手击球次数，如发球、扣杀准备动作，取值范围：[0,10000]，默认值：0。 | number | O |
| underhandStroke | 下手击球次数，如挑球、切球，取值范围：[0,10000]，默认值：0。 | number | O |
| smash | 扣杀次数，取值范围：[0,10000]，默认值：0。 | number | O |
| highClear | 高远球次数，取值范围：[0,10000]，默认值：0。 | number | O |

## 关联的明细数据说明

字段定义：[exerciseSequenceHelper.badminton.DetailFields](../harmonyos-references/health-api-exercisesequencehelper-lite.md#detailfields)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| exerciseHeartRate | 运动心率详情 | [ExerciseHeartRate](../harmonyos-references/health-api-healthfields-lite.md#exerciseheartrate)[] | O |
