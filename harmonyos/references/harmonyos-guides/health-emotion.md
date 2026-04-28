---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-emotion
title: 情绪
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 情绪
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5ea18b14cadd9f24c806f4d6ad8358982e44b7d596f136029df023cf2cefba2d
---

此数据记录用户在某时刻的情绪数据。

Harmony SDK类型常量：[samplePointHelper.emotion.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-4)

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 情绪数据

## 采样明细数据

### 明细字段说明

字段定义：[samplePointHelper.emotion.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-4)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| emotionStatus | 情绪状态 | number | M | - | [0, 100)  当前运动健康App仅展示以下值：  1：不愉悦  2：平静  3：愉悦 |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 手表、手环等 |
