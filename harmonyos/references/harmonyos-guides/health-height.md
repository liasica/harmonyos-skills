---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-height
title: 身高
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 身高
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea29d87df3a94aa0dbac14c7a2de983dbda55a7e999e39995177d22b5cc344f4
---

此数据记录用户在某时刻的身高数据。

Harmony SDK类型常量：[samplePointHelper.height.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-7)

说明

Wearable设备暂不支持该数据类型。

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 体脂数据

## 采样明细数据

### 明细字段说明

字段定义：[samplePointHelper.height.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-7)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| height | 身高 | number | M | 厘米 | - |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 小时级 | 运动健康App个人信息 |
