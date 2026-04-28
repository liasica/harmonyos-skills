---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-exercisesequence-summary
title: 简介
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 锻炼记录数据 > 简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb642b15c04948efb79f4ce42d15ef5375b6eb918a8fdfddf0fa79583766c381
---

用户一段持续时间的锻炼记录数据，由运动类型、应用信息、时间范围、关联的详情数据、关联的统计数据等组成，如跑步、跳绳等锻炼记录。

开发者可以通过[锻炼记录数据查询](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-1)接口获取华为运动健康App“运动记录”卡片中的数据。

锻炼记录数据模型组成参考[ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)。

锻炼记录类型常量：[exerciseSequenceHelper.DATA\_TYPE](../harmonyos-references/health-api-exercisedequencehelper.md#常量)

## OAuth权限

联盟卡片申请的权限名称：

锻炼记录 > 锻炼记录概要

锻炼记录 > 锻炼记录详情数据

锻炼记录 > 锻炼记录位置详情数据

说明

* 如需读/写锻炼记录，请申请锻炼记录概要的读/写权限。
* 如需读/写锻炼记录且关联对应的详情数据，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据的读/写权限。
* 如需读/写锻炼记录且关联的详情数据包含位置详情，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据读/写、锻炼记录位置详情数据的读/写权限。

## 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-1) | 分钟级 | 手机、手表、手环等 |
