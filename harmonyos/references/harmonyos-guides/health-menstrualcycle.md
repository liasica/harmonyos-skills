---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-menstrualcycle
title: 生理周期
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据类型 > 健康记录数据 > 生理周期
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:56+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:4e85e7758da297156f3f9196cfa08b7632a1e41b6051467a6345ef8353f365a4
---

记录用户在女性生理周期时间段（默认28天）内一天的身体状态，每一条数据代表该女性用户当天的状态。

**说明** 

从API version 24开始，支持该数据类型开放。

健康记录类型如下：

| **健康记录类型常量** | **描述** | 数据来源 |
| --- | --- | --- |
| [healthSequenceHelper.menstrualCycle.DATA\_TYPE](../harmonyos-references/health-api-healthsequencehelper.md#常量-2) | 生理周期 | 运动健康App |

## OAuth权限

联盟卡片申请的权限名称：健康数据 > 生殖健康数据

## 生理周期数据类型

* 字段定义：[healthSequenceHelper.menstrualCycle.Fields](../harmonyos-references/health-api-healthsequencehelper.md#fields-2)

| **字段**列表 | 描述 | **类型** | 可选/必选 | 单位 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| status | 当日状态 | number | M | - | 取值参考如下：  0：普通状态  100：普通经期  101：经期第一天  102：经期最后一天  2：排卵日  300：普通预测经期  301：预测经期第一天  302：预测经期最后一天  400：普通易孕期  401：易孕期第一天  402：易孕期最后一天  403：易孕期只有一天 |
| remarks | 备注 | string | O | - | - |

## 关联的明细数据说明

* 字段定义：[healthSequenceHelper.menstrualCycle.DetailFields](../harmonyos-references/health-api-healthsequencehelper.md#detailfields-2)

| **字段**列表 | 描述 | **类型** | 可选/必选 |
| --- | --- | --- | --- |
| menstrualFlow | 月经流量采样 | [MenstrualFlow](../harmonyos-references/health-api-healthfields.md#menstrualflow)[] | O |
| dysmenorrhea | 痛经程度采样 | [Dysmenorrhea](../harmonyos-references/health-api-healthfields.md#dysmenorrhea)[] | O |
| physicalSymptoms | 身体状况采样 | [PhysicalSymptoms](../harmonyos-references/health-api-healthfields.md#physicalsymptoms)[] | O |
| mood | 心情采样 | [Mood](../harmonyos-references/health-api-healthfields.md#mood)[] | O |
| skin | 皮肤状态采样 | [Skin](../harmonyos-references/health-api-healthfields.md#skin)[] | O |
| sexuality | 性行为采样 | [Sexuality](../harmonyos-references/health-api-healthfields.md#sexuality)[] | O |
| ovulationTestPaper | 排卵试纸采样 | [OvulationTestPaper](../harmonyos-references/health-api-healthfields.md#ovulationtestpaper)[] | O |
| cervicalMucus | 私处分泌物采样 | [CervicalMucus](../harmonyos-references/health-api-healthfields.md#cervicalmucus)[] | O |

## 数据开放说明

| 开放API | 查询及时性 | 数据源 |
| --- | --- | --- |
| [healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2) | 小时级 | 运动健康App |
