---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-heart-rate-variability
title: 心率变异性
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 心率变异性
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d123e8c83eb3f3b57fc4d3a37aa026672a820370ab464b5562e473c5565d782e
---

此数据记录用户在某时刻的心率变异性数据。

Harmony SDK类型常量：[samplePointHelper.heartRateVariability.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-6)

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 心率数据

## 采样明细数据

### 明细字段说明

字段定义：[samplePointHelper.heartRateVariability.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-6)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| heartRateVariabilityRMSSD | 心率变异性 | number | M | 毫秒 | (0, 200] |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 手表、手环等 |
