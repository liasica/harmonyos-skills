---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-personal-data
title: 个人数据处理说明
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3475ec10e3eed087faf5a2c99caf4694d9442ef73cc87c395a75a9f913d45b8a
---

此文档针对华为作为最终用户数据处理者，您作为最终用户数据控制者的数据处理进行说明，包括：

* 华为处理的个人数据清单。
* 指导您如何帮助最终用户实现对数据的控制。

**华为处理的个人数据清单**

| 个人数据清单 | 处理目的 | 存留期 |
| --- | --- | --- |
| 活动状态 | 识别用户的活动状态。 | 不保存。  定位服务在处理个人数据后立即删除。 |

**指导开发者如何帮助最终用户实现对数据的控制**

使用地理围栏功能前开发者应当获得用户同意（具体可参考[向用户申请授权](../harmonyos-guides-V14/location-permission-guidelines-V14.md)），允许开发者的应用始终访问用户的位置信息。

定位服务在处理个人数据后立即删除，不会保存用户的个人数据。因此，华为无需实现对数据的控制。
