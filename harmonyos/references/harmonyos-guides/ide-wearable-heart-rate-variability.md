---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-wearable-heart-rate-variability
title: 心率变异性
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Wearable应用开发 > 开放数据类型 > 采样数据 > 心率变异性
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:610488eaa9ac31dcbfd4a9b241aa6378e366aa82cd96502bfc3e327e382e7f1a
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
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 智能穿戴（智能表） |
