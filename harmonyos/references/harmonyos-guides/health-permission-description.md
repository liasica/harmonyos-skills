---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-permission-description
title: 开放数据和权限总览
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Phone/Tablet应用开发 > 开放数据类型 > 开放数据和权限总览
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:19+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:d0ccb6a4918f71a46160bfb5d77bf7dd1e92e166b174fff94203f72bb58efab2
---

## 开放数据总览

当前提供如下Health Service Kit数据，开发者可申请对应数据权限进行应用开发。开放等级中，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/tK0rPg4QQUW7gW88bbcYNg/zh-cn_image_0000002817427405.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBF5E7BB2DA716EC3628306A124ED9F5F764641E9C40C4E6F340CDCDBA569A16)表示该数据权限为高阶数据，暂不对个人开发者开放。如需使用，请使用企业账号重新注册并申请权限；![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/zm84MX7oRKeZQYw_SyWd9w/zh-cn_image_0000002788467986.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA19EF9ADB387E7B91A172702D77016BF6288C78271553360C9BACF7148E1E76)表示该数据权限为基础数据，个人及企业开发者均可申请查询/使用。

**说明** 

* 数据及时性体验依赖用户使用方式，若穿戴设备未连接至手机蓝牙、华为运动健康App未设置后台保活等情况下，将无法保证数据及时性体验。开发者需考虑数据及时性体验各类极端情况，综合判断合适的数据使用场景，确保给用户提供的产品/服务的稳定性，保证用户体验。
* 相关数据类型对应权限参考[权限说明](health-permission-description.md)。

**表1** **采样数据**

| 数据子类 | 数据项 | 开放等级 | 数据及时性 | 支持读 | 支持写 |
| --- | --- | --- | --- | --- | --- |
| [日常活动](health-daily-activities.md) | 步数、热量、距离等日常活动数据 |  | 小时级 | Y | Y |
| [心率](health-heart-rate.md) | 动态心率、静息心率、心率变异性 |  | 小时级 | Y | Y |
| [血氧](health-blood-oxygen.md) | 瞬时血氧饱和度 |  | 小时级 | Y | Y |
| [压力](health-stress.md) | 压力得分 |  | 小时级 | Y | Y |
| [体温](health-body-temperature.md) | 体温、皮肤体温 |  | 分钟级 | Y | Y |
| [血压](health-blood-pressure.md) | 收缩压、舒张压、脉搏等 |  | 分钟级 | Y | Y |
| [体重](health-weight.md) | 体重、体脂、BMI等 |  | 分钟级 | Y | Y |
| [身高](health-height.md) | 身高 |  | 分钟级 | Y | Y |
| [情绪](health-emotion.md) | 情绪数据 |  | 小时级 | Y | Y |

**表2** **健康记录和锻炼记录**

| 数据子类 | 数据项 | 开放等级 | 数据及时性 | 支持读 | 支持写 |
| --- | --- | --- | --- | --- | --- |
| [睡眠](health-sleeprecord.md) | 睡眠分期采样数据、睡眠记录 |  | 分钟级 | Y | Y |
| [生理周期](health-menstrualcycle.md) | 月经量、痛经程度、身体状况、心情、皮肤状态、排卵检测结果、阴道斑点 |  | 小时级 | Y | N |
| [锻炼记录数据](health-exercisesequence-summary.md) | 跑步、骑行、健走、跳绳、跑步机等运动和健身类型 |  | 分钟级 | Y | Y |

## 权限说明

运动健康数据读写以及运动联动接口调用需要相应的权限，权限申请参考[申请运动健康服务](health-apply.md)，数据类型对应权限如下：

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
| 锻炼记录 | [exerciseSequenceHelper.DATA\_TYPE](../harmonyos-references/health-api-exercisesequencehelper.md#常量) | 锻炼记录概要（读）  锻炼记录详情数据（读）  锻炼记录位置详情数据（读） | 锻炼记录概要（写）  锻炼记录详情数据（写）  锻炼记录位置详情数据（写） |

**说明** 

* 如需读/写锻炼记录，请申请锻炼记录概要的读/写权限。
* 如需读/写锻炼记录且关联对应的详情数据，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据的读/写权限。
* 如需读/写锻炼记录且关联的详情数据包含位置详情，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据读/写、锻炼记录位置详情数据的读/写权限。
