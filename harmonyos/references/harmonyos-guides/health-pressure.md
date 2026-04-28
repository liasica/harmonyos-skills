---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-pressure
title: 压力
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 压力
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ec3f20aa23123b403fe497d73209fa947c727b39355c1633faca651b4f6aa2a
---

此数据记录用户在某一刻的压力数据，每一条数据都代表该时刻的压力状态。

* Harmony SDK类型常量：[samplePointHelper.stress.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-10)

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 压力数据

## 采样明细数据

### 明细字段说明

* 字段定义：[samplePointHelper.stress.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-10)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| stressScore | 压力得分 | number | M | - | [1, 99] |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 手表、手环等 |

## 采样统计数据

**聚合统计策略说明**

* 字段定义：[samplePointHelper.stress.AggregateFields](../harmonyos-references/health-api-samplepointhelper.md#aggregatefields-6)

| **字段**列表 | 描述 | 聚合策略 | **类型** | 单位 |
| --- | --- | --- | --- | --- |
| stressScore | 压力得分 | avg | max | min | last | count | number | - |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata) | 小时级 | 手表、手环等 |
