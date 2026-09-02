---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-moduleinfo
title: ModuleInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > bundle > ModuleInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:245c8227fd05b3117b970ec0959a26164752cbea82fcf7d791db6881968a13f3
---

应用程序的模块信息。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md)替代。

## ModuleInfo(deprecated)

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md#hapmoduleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 是 | 否 | 模块名称。 |
| moduleSourceDir | string | 是 | 否 | 安装目录。不能拼接路径访问资源文件，请使用[@ohos.resourceManager (资源管理)](js-apis-resource-manager.md)访问资源。 |
