---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-permission-description
title: 权限说明
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 权限说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1dc6e5fd8b3d041dfdf21bbf756974790097cae7ee12b00b6d994764685534b6
---

运动健康数据读写需要相应的权限，权限申请参考[申请运动健康服务](health-apply.md)，数据类型对应权限如下：

| 数据类型 | Harmony SDK类型常量 | 读权限 | 写权限 |
| --- | --- | --- | --- |
| 日常活动 | [samplePointHelper.dailyActivities.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-3) | 日常活动数据（读） | 日常活动数据（写） |
| 动态心率 | [samplePointHelper.heartRate.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-5) | 心率数据（读） | 心率数据（写） |
| 静息心率 | [samplePointHelper.restingHeartRate.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-8) | 心率数据（读） | 心率数据（写） |
| 血氧 | [samplePointHelper.bloodOxygenSaturation.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量) | 血氧数据（读） | 血氧数据（写） |
| 压力 | [samplePointHelper.stress.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-10) | 压力数据（读） | 压力数据（写） |
| 体温 | [samplePointHelper.bodyTemperature.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-2) | 体温数据（读） | 体温数据（写） |
| 皮肤体温 | [samplePointHelper.skinTemperature.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-9) | 体温数据（读） | 体温数据（写） |
| 血压 | [samplePointHelper.bloodPressure.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-1) | 血压数据（读） | 血压数据（写） |
| 身高 | [samplePointHelper.height.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-7) | 体脂数据（读） | 体脂数据（写） |
| 体重 | [samplePointHelper.weight.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-11) | 体脂数据（读） | 体脂数据（写） |
| 情绪 | [samplePointHelper.emotion.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-4) | 情绪数据（读） | 情绪数据（写） |
| 心率变异性 | [samplePointHelper.heartRateVariability.DATA\_TYPE](../harmonyos-references/health-api-samplepointhelper.md#常量-6) | 心率数据（读） | 心率数据（写） |
| 睡眠 | [healthSequenceHelper.sleepRecord.DATA\_TYPE](../harmonyos-references/health-api-healthsequencehelper.md#常量)  [healthSequenceHelper.sleepNapRecord.DATA\_TYPE](../harmonyos-references/health-api-healthsequencehelper.md#常量-1) | 睡眠数据（读） | 睡眠数据（写） |
| 锻炼记录 | [exerciseSequenceHelper.DATA\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量) | 锻炼记录概要（读）  锻炼记录详情数据（读）  锻炼记录位置详情数据（读） | 锻炼记录概要（写）  锻炼记录详情数据（写）  锻炼记录位置详情数据（写） |

说明

* 如需读/写锻炼记录，请申请锻炼记录概要的读/写权限。
* 如需读/写锻炼记录且关联对应的详情数据，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据的读/写权限。
* 如需读/写锻炼记录且关联的详情数据包含位置详情，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据读/写、锻炼记录位置详情数据的读/写权限。
