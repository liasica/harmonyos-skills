---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-daily-activities
title: 日常活动
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 采样数据 > 日常活动
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cc90832dafe5a974dd85b3d878fb55229b86e0b228eaf22593c79a0bda57a19f
---

此数据记录用户在一小段时间内的日常活动数据。

* Harmony SDK类型常量：[samplePointHelper.dailyActivities.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-3)

  说明

  Wearable设备暂不支持该数据类型。读取实时日常活动数据使用[读取实时三环数据](health-wearable-three-ring-read.md)接口。

## OAuth权限

联盟卡片申请的权限名称：日常活动 > 日常活动数据

## 采样明细数据

### 明细字段说明

* 字段定义：[samplePointHelper.dailyActivities.Fields](../harmonyos-references/health-api-samplepointhelper.md#fields-3)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| step | 步数 | number | M | 步 | [0, 500) |
| calorie | 热量 | number | M | 卡 | [0, 65536) |
| distance | 距离 | number | M | 米 | [0, ∞) |
| duration | 时长 | number | O | 分钟 | 0 或 1 |
| status | 状态（走、跑、骑、爬等） | number | O | - | 2： 登山  3： 骑行  4： 跑步  5：走路  9：游泳  10：健身  13：站立 |
| isIntensity | 是否中高强度 | number | O | - | 0：否  1：是 |
| climbHighAltitude | 爬高海拔差（支持正负） | number | O | 米 | - |
| isStand | 是否站立（一个小时有活动记录，就标志这个小时的第一分钟为1） | number | O | - | 0：否  1：是 |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata) | 10分钟级 | 手机、手表、手环等 |

## 采样统计数据

### 聚合统计策略说明

* 字段定义：[samplePointHelper.dailyActivities.AggregateFields](../harmonyos-references/health-api-samplepointhelper.md#aggregatefields-2)

  | **字段**列表 | 描述 | 聚合策略 | **类型** | 单位 |
  | --- | --- | --- | --- | --- |
  | step | 步数 | sum | number | 步 |
  | calorie | 热量 | sum | number | 卡 |
  | distance | 距离 | sum | number | 米 |
  | isIntensity | 是否中高强度（按天聚合对应运动健康App三环数据中锻炼时长） | sum | number | - |
  | climbHighAltitude | 爬高海拔差（支持正负） | sum | number | 米 |
  | isStand | 是否站立（一个小时有活动记录，就标志这个小时的第一分钟为1，按天聚合对应运动健康App三环数据中活动小时数） | sum | number | - |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata) | 10分钟级 | 手机、手表、手环等 |
