---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-hapmoduleinfo
title: HapModuleInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > bundle > HapModuleInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e48eaaf25b89250fc376163b377a97aaa006dc1e2c5dc504373cd5294becb7c8
---

Hap模块信息，未做特殊说明的属性，均通过[bundle.getBundleInfo](js-apis-bundle.md#bundlegetbundleinfodeprecated)获取。

说明

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md)替代。

## HapModuleInfo(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md#hapmoduleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 模块名称。 |
| description | string | 是 | 否 | 模块描述信息。 |
| descriptionId | number | 是 | 否 | 描述信息ID。 |
| icon | string | 是 | 否 | 模块图标。 |
| label | string | 是 | 否 | 模块标签。 |
| labelId | number | 是 | 否 | 模块标签ID。 |
| iconId | number | 是 | 否 | 模块图标ID。 |
| backgroundImg | string | 是 | 否 | 模块背景图片。 |
| supportedModes | number | 是 | 否 | 模块支持的模式。 |
| reqCapabilities | Array<string> | 是 | 否 | 模块运行需要的能力。 |
| deviceTypes | Array<string> | 是 | 否 | 支持运行的设备类型。 |
| abilityInfo | Array<[AbilityInfo](js-apis-bundle-abilityinfo.md)> | 是 | 否 | Ability信息。 |
| moduleName | string | 是 | 否 | 模块名。 |
| mainAbilityName | string | 是 | 否 | 入口Ability名称。 |
| installationFree | boolean | 是 | 否 | 是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。 |
