---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-blood-oxygen
title: 血氧
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 血氧
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5c4fade765935dcdbf902da269ee9971ec652c8a5108157add750d18b4988fd1
---

此数据记录用户在某时刻的血氧，每一条数据都代表该时刻的血氧值。每条数据不能存在交叉，后一条数据的开始时间应该大于或等于前一条数据的结束时间。

* Harmony SDK类型常量：[samplePointHelper.bloodOxygenSaturation.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量)

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 血氧数据

## 采样明细数据

### 明细字段说明

* 字段定义：[samplePointHelper.bloodOxygenSaturation.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| spo2 | 血氧饱和度 | number | M | 百分比 | (0, 100] |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 部分手表、手环等 |

## 采样统计数据

**聚合统计策略说明**

字段定义：[samplePointHelper.bloodOxygenSaturation.AggregateFields](../harmonyos-references/health-api-samplepointhelper.md#aggregatefields)

| **字段**列表 | 描述 | 聚合策略 | **类型** | 单位 |
| --- | --- | --- | --- | --- |
| spo2 | 血氧饱和度 | avg | max | min | last | number | 百分比 |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata) | 小时级 | 部分手表、手环等 |
