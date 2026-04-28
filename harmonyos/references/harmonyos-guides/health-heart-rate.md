---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-heart-rate
title: 心率
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 心率
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f0fb0ec0b538a29da4785c9ff9f9d8458f03e09e04357a459ca468d817f80bb
---

## 动态心率

此数据记录用户在一段时间内的动态心率。

* Harmony SDK类型常量：[samplePointHelper.heartRate.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-5)

### OAuth权限

联盟卡片申请的权限名称：健康数据 > 心率数据

### 采样明细数据

**明细字段说明**

字段定义：[samplePointHelper.heartRate.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-5)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| bpm | 心率 | number | M | 次/分钟 | [0, ∞) |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 手表、手环等 |

### 采样统计数据

**聚合统计策略说明**

* 字段定义：[samplePointHelper.heartRate.AggregateFields](../harmonyos-references/health-api-samplepointhelper.md#aggregatefields-3)

| **字段**列表 | 描述 | 聚合策略 | **类型** | 单位 |
| --- | --- | --- | --- | --- |
| bpm | 心率 | max | min | last | number | 次/分钟 |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata) | 小时级 | 手表、手环等 |

## 静息心率

此数据记录用户一天中在静止且清醒状态下静息心率值。

Harmony SDK类型常量：[samplePointHelper.restingHeartRate.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-8)

### OAuth权限

联盟卡片申请的权限名称：健康数据 > 心率数据

### 采样明细数据

**明细字段说明**

字段定义：[samplePointHelper.restingHeartRate.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-8)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| restBpm | 静息心率 | number | M | 次/分钟 | [0, ∞) |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 手表、手环等 |

### 采样统计数据

**聚合统计策略说明**

字段定义：[samplePointHelper.restingHeartRate.AggregateFields](../harmonyos-references/health-api-samplepointhelper.md#aggregatefields-4)

| **字段**列表 | 描述 | 聚合策略 | **类型** | 单位 |
| --- | --- | --- | --- | --- |
| restBpm | 静息心率 | last | number | 次/分钟 |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata) | 小时级 | 手表、手环等 |
