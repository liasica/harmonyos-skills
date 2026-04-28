---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-weight
title: 体重
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 体重
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e90a8461b16ac8e2137e24349f89ef3b74dec4d39da6136ea5b555c8dc9b08f9
---

此数据记录用户在某时刻的体重数据。

Harmony SDK类型常量：[samplePointHelper.weight.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-11)

说明

Wearable设备暂不支持该数据类型。

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 体脂数据

## 采样明细数据

### 明细字段说明

字段定义：[samplePointHelper.weight.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-11)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| bodyWeight | 体重 | number | M | 千克 | [0.1, 500] |
| bmi | 身体质量指数 | number | O | 千克/平方米 | [1, 200] |
| bodyFat | 体脂量 | number | O | 千克 | [0, 500] |
| bodyFatRate | 体脂率 | number | O | 百分比 | [0, 100] |
| muscleMass | 肌肉量 | number | O | 千克 | [0.1, 150] |
| basalMetabolism | 基础代谢 | number | O | 千卡/天 | [0, ∞) |
| moisture | 水分量 | number | O | 千克 | [0, 500] |
| moistureRate | 水分率 | number | O | 百分比 | [0, 100] |
| visceralFatLevel | 内脏脂肪等级 | number | O | - | [1, 59] |
| boneSalt | 骨盐量 | number | O | 千克 | [0.5, 5] |
| proteinRate | 蛋白质率 | number | O | 百分比 | [0, 100] |
| bodyScore | 身体得分 | number | O | 百分比 | [0, 100] |
| bodyAge | 身体年龄 | number | O | - | [5, 99] |
| skeletalMuscleMass | 骨骼肌量 | number | O | 千克 | [1, 150] |
| impedance | 阻抗 | number | O | 欧姆 | [0.1, 100000] |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 分钟级 | 华为体脂秤和三方体脂秤（生态设备） |
