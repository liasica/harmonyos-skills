---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-sleeprecord
title: 睡眠
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 健康记录数据 > 睡眠
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef46e24e35a631dfc276633b162a24b195625ee5c5bf56c7458d80761bf02460
---

## 夜间睡眠

从入睡到醒来的一段完整睡眠记录（睡眠时长超过3小时），包括夜间睡眠数据以及每个时刻的睡眠状态采样数据。

健康记录类型如下：

| **健康记录类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [healthSequenceHelper.sleepRecord.DATA\_TYPE](../harmonyos-references/health-api-healthsequencehelper.md#常量) | 夜间睡眠 | 部分手表、手环等 |

### OAuth权限

联盟卡片申请的权限名称：健康数据 > 睡眠数据

### 夜间睡眠数据类型

* 字段定义：[healthSequenceHelper.sleepRecord.Fields](../harmonyos-references/health-api-healthsequencehelper.md#fields)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| fallAsleepTime | 分期睡眠最早入睡时间点 | number | M | 毫秒 | [0，∞） |
| wakeupTime | 分期睡眠最晚醒来时间点 | number | M | 毫秒 | [0，∞） |
| duration | 夜间/普通睡眠时长（不含零星小睡时长） | number | M | 秒 | [0，∞） |
| bedTime | 最早上床时间点 | number | O | - | [0，∞） |
| risingTime | 最晚起床时间点 | number | O | - | [0，∞） |
| prepareSleepTime | 准备入睡时间点 | number | O | 毫秒 | [0，∞） |
| shallowDuration | 浅睡时长 | number | O | 秒 | [0，∞） |
| deepDuration | 深睡时长 | number | O | 秒 | [0，∞） |
| dreamDuration | REM时长 | number | O | 秒 | [0，∞） |
| wakeDuration | 清醒时长 | number | O | 秒 | [0，∞） |
| wakeCount | 清醒次数 | number | O | - | [0，∞） |
| onBedDuration | 卧床时长 | number | O | 秒 | [0，∞） |
| recordDuration | 睡眠记录时长（手动输入睡眠就是总时长） | number | O | 秒 | [0，∞） |
| sleepEfficiency | 睡眠效率 | number | O | - | [0,100] |
| sleepScore | 睡眠得分 | number | O | - | [0,100] |
| deepSleepContinuity | 深睡连续性 | number | O | - | [0,100] |
| respiratoryQualityScore | 呼吸质量分 | number | O | - | [0,100] |
| turnOverCount | 翻身次数 | number | O | - | [0，∞） |
| sleepEndReason | 睡眠结束原因 | number | O | - | [0，∞）  取值参考如下：  0：手动结束睡眠监测  1：自动结束睡眠监测  2：中断睡眠监测  3：电量过低结束 |
| sleepSymptoms | 睡眠症状 | string | O | - | - |
| sleepType | 睡眠数据类型 | number | O | - | 1：科学睡眠  2：普通睡眠  3：手动输入睡眠  4：手机记录睡眠  未设置时，默认值为2。 |

### 关联的明细数据说明

* 字段定义：[healthSequenceHelper.sleepRecord.DetailFields](../harmonyos-references/health-api-healthsequencehelper.md#detailfields)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| sleepSegment | 睡眠状态采样 | [SleepSegment](../harmonyos-references/health-api-healthfields.md#sleepsegment)[] | O |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2) | 分钟级 | 部分手表、手环等 |

## 零星小睡

日间进行的短时间睡眠，包括零星小睡睡眠数据以及每个时刻的睡眠状态采样数据。

健康记录类型如下：

| **健康记录类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [healthSequenceHelper.sleepNapRecord.DATA\_TYPE](../harmonyos-references/health-api-healthsequencehelper.md#常量-1) | 零星小睡 | 部分手表、手环等 |

### OAuth权限

联盟卡片申请的权限名称：健康数据 > 睡眠数据

### 零星小睡数据类型

* 字段定义：[healthSequenceHelper.sleepNapRecord.Fields](../harmonyos-references/health-api-healthsequencehelper.md#fields-1)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| noonDuration | 午睡时长(零星小睡） | number | M | 秒 | [0，∞） |
| noonRecordDuration | 零星小睡记录时长 | number | O | 秒 | [0，∞） |

### 关联的明细数据说明

* 字段定义：[healthSequenceHelper.sleepNapRecord.DetailFields](../harmonyos-references/health-api-healthsequencehelper.md#detailfields-1)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| sleepSegment | 睡眠状态采样 | [SleepSegment](../harmonyos-references/health-api-healthfields.md#sleepsegment)[] | O |

### 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2) | 分钟级 | 部分手表、手环等 |
