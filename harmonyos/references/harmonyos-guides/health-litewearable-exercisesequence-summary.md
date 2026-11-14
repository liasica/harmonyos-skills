---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-exercisesequence-summary
title: 简介
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 开放数据类型 > 锻炼记录数据 > 简介
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:542cf3e121f299c1b445a4740f295f1305c22fcbff785661662979f89fd2f5e5
---

用户一段持续时间的锻炼记录数据，由运动类型、应用信息、时间范围、关联的详情数据、关联的统计数据等组成，如户外跑步、户外骑行等锻炼记录。

开发者可以通过[锻炼记录数据查询](../harmonyos-references/health-api-healthstore-lite.md#healthstorereaddata)接口获取华为运动健康App“运动记录”卡片中的数据。

锻炼记录数据模型组成参考[ExerciseSequence](../harmonyos-references/health-api-healthstore-lite.md#exercisesequence)。

锻炼记录类型常量：[exerciseSequenceHelper.DATA\_TYPE](../harmonyos-references/health-api-exercisesequencehelper-lite.md#常量)

## OAuth权限

联盟卡片申请的权限名称：

锻炼记录 > 锻炼记录概要

锻炼记录 > 锻炼记录详情数据

**说明** 

* 如需读/写锻炼记录，请申请锻炼记录概要的读/写权限。
* 如需读/写锻炼记录且关联对应的详情数据，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据的读/写权限。

## 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore-lite.md#healthstorereaddata) | 分钟级 | 轻量级智能穿戴（运动表） |
