---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-customizedata
title: CustomizeData
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > bundle > CustomizeData
category: harmonyos-references
scraped_at: 2026-04-28T07:58:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1193106cdbf46c20f18edd4798153f2b98d115d813268669284593a60f1ba3f8
---

自定义元数据。

说明

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[Metadata](js-apis-bundlemanager-metadata.md)替代。

## CustomizeData(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[Metadata](js-apis-bundlemanager-metadata.md#metadata-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 标识自定义数据项的键名称。 |
| value | string | 否 | 否 | 标识自定义数据项的值名称。 |
| extra8+ | string | 否 | 否 | 标识用户自定义数据格式，标签值为标识该数据的资源的索引值。 |
