---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-blood-pressure
title: 血压
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 血压
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aaeec259ad2932240d7124a272f1ca8151b67ce6ebb4ed9f03f51bf2b6df708c
---

此数据记录用户在某时刻的血压数据。

Harmony SDK类型常量：[samplePointHelper.bloodPressure.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-1)

说明

Wearable设备暂不支持该数据类型。

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 血压数据

## 采样明细数据

### 明细字段说明

字段定义：[samplePointHelper.bloodPressure.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-1)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| bloodPressureSystolic | 收缩压，即高压 | number | M | mmHg | (0, ∞) |
| bloodPressureDiastolic | 舒张压，即低压 | number | M | mmHg | (0, ∞) |
| sphygmus | 脉搏 | number | O | 次/分钟 | (0, ∞) |
| measurementAnomalyFlag | 测量异常事件 | number | O | - | (0, ∞)  取值参考如下：  1：正常  2：测量时未和心脏平齐  3：测量时有轻微抖动  4：测量前没有至少5min休息 |
| beforeMeasureActivity | 测量前活动 | number | O | - | (0, ∞)  取值参考如下：  1：剧烈运动  2：吸烟  3：进食  4：饮酒  5：喝咖啡  6：无活动  7：起床后  8：睡前  100：自定义 |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 分钟级 | 血压计、血压表等 |
