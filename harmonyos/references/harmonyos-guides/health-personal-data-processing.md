---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-personal-data-processing
title: 个人数据处理说明
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b6ed3fa7e53e5735e6ae2ccbf925240e7009ed425eb538128a616da2575fff1
---

最后修改时间： 2024/5/16

华为是数据处理者，不是数据控制者，数据使用目的和方式由用户自己决定。

此文档针对华为作为最终用户数据处理者，开发者作为最终用户数据控制者的数据处理进行说明，包括：

* 华为处理的个人数据清单。
* 指导开发者如何帮助最终用户实现对数据的控制。

## 华为处理的个人数据清单

| 个人数据 | 使用目的 | 存留期 |
| --- | --- | --- |
| **个人信息**：身高和体重  **运动数据**：日常活动（步数、热量、距离、中高强度、爬高、活动小时数）、锻炼记录、位置数据  **健康数据**：睡眠数据、心率数据、压力数据、血氧数据、体温数据、血压数据 | Health Service Kit为用户提供数据存储和共享的平台，不会主动处理任何用户数据。所有的数据显示和运动健康服务由开发者为用户提供，数据来源于华为运动健康App与三方服务写入，数据存储在运动健康服务本地数据库，会随端云同步到运动健康服务云侧。 | 用户删除华为账号后，其所有个人数据会删除。 |
| 数据源的设备ID（MAC或其他设备标识，由三方服务提供） | 设备ID用于标记数据来源。 | 用户删除华为账号后，其所有个人数据会删除。 |
| 华为账号ID | 最终用户的华为账号绑定三方服务时的用户标识符。 | 用户删除华为账号后，其所有个人数据会删除。 |

## 指导开发者如何帮助最终用户实现对数据的控制

**如何清除最终用户数据**

1. 开发者通过华为运动健康服务API，用户登录并授权后，开发者可以通过接口[healthStore.deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata)删除自己服务写入Health Service Kit的该用户数据。
2. 用户可以通过删除华为账号来删除个人数据，该账号下的所有个人数据将会被删除。

**如何导出最终用户的数据**

开发者通过华为运动健康服务API，可以通过数据访问接口获取用户数据，为用户提供数据导出服务，具体方法见[healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata)，详细使用请参见[运动健康采样数据](health-samplepoint-manage.md)开发指导。
