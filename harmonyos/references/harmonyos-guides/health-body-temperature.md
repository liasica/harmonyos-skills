---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-body-temperature
title: 体温
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 体温
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:08c84f99e52baa296860a1848340369ad74671205fd1fca2ffa0a02cb6da9439
---

## 体温

此数据记录用户在一小段时间内的体温数据。

Harmony SDK类型常量：[samplePointHelper.bodyTemperature.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-2)

### OAuth权限

联盟卡片申请的权限名称：健康数据 > 体温数据

### 采样明细数据

**明细字段说明**

* 字段定义：[samplePointHelper.bodyTemperature.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-2)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| bodyTemperature | 体温 | number | M | 摄氏度 | [34, 42] |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 分钟级 | 部分手表支持 |

### 采样统计数据

**聚合统计策略说明**

字段定义：[samplePointHelper.bodyTemperature.AggregateFields](../harmonyos-references/health-api-samplepointhelper.md#aggregatefields-1)

| **字段**列表 | 描述 | 聚合策略 | **类型** | 单位 |
| --- | --- | --- | --- | --- |
| bodyTemperature | 体温 | avg | max | min | count | number | 摄氏度 |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata) | 分钟级 | 部分手表支持 |

## 皮肤体温

此数据记录用户在一小段时间内的皮肤温度数据。

* Harmony SDK类型常量：[samplePointHelper.skinTemperature.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-9)

### OAuth权限

联盟卡片申请的权限名称：健康数据 > 体温数据

### 采样明细数据

**明细字段说明**

* 字段定义：[samplePointHelper.skinTemperature.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-9)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| skinTemperature | 皮肤温度 | number | M | 摄氏度 | [20, 42] |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 分钟级 | 部分手表支持 |

### 采样统计数据

**聚合统计策略说明**

字段定义：[samplePointHelper.skinTemperature.AggregateFields](../harmonyos-references/health-api-samplepointhelper.md#aggregatefields-5)

| **字段**列表 | 描述 | 聚合策略 | **类型** | 单位 |
| --- | --- | --- | --- | --- |
| skinTemperature | 皮肤温度 | avg | max | min | count | number | 摄氏度 |

**数据开放说明**

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata) | 分钟级 | 部分手表支持 |
