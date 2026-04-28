---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-elementname
title: ElementName
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > bundle > ElementName
category: harmonyos-references
scraped_at: 2026-04-28T07:58:53+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:4967a87d43bb096ba221ced8a1b06794ab59d0fba1c18c9ebf740e23654d59da
---

ElementName信息，通过接口[Context.getElementName](js-apis-inner-app-context.md#contextgetelementname7)获取。

说明

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-ElementName](js-apis-bundlemanager-elementname.md)替代。

## ElementName(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-ElementName](js-apis-bundlemanager-elementname.md#elementname-1)替代。

ElementName信息，标识Ability的基本信息，通过接口[Context.getElementName](js-apis-inner-app-context.md#contextgetelementname7)获取。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 设备id值。 |
| bundleName | string | 否 | 否 | 应用Bundle的名称。 |
| abilityName | string | 否 | 否 | Ability的名称。 |
| uri | string | 否 | 是 | 资源标识符。 |
| shortName | string | 否 | 是 | Ability的短名称。 |
