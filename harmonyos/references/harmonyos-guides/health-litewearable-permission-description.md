---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-permission-description
title: 数据权限总览
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 数据权限总览
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:80cce3fe39d105806ffbac5c532891d5c09abfbd5586b0d62bdd23195e832078
---

运动健康数据读写以及运动接口调用需要相应的权限，权限申请参考[申请运动健康服务](health-apply.md)，数据类型对应权限如下：

## Lite Wearable

| 权限名称 | 权限对应字段和取值 | 说明 |
| --- | --- | --- |
| 运动 | scopes: ['https://www.huawei.com/healthkit/workout'] | 管理运动的开关，打开后可调用运动相关的开关。 |
| 锻炼记录概要读权限 | readDataTypes: [healthStore.healthDataTypes.WORKOUT\_SUMMARY] | 开启后可读取锻炼数据。 |
| 锻炼记录概要写权限 | writeDataTypes: [healthStore.healthDataTypes.WORKOUT\_SUMMARY] | 开启后可写入锻炼数据。 |

**说明** 

* 如需读/写锻炼记录，请申请锻炼记录概要的读/写权限。
* 如需读/写锻炼记录且关联对应的详情数据，则需同时申请锻炼记录读/写权限。
* 如需开启运动，管理运动，则需申请运动权限。
