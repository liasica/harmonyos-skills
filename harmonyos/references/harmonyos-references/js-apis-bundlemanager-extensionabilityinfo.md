---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-extensionabilityinfo
title: ExtensionAbilityInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > ExtensionAbilityInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:47+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:99eba8aecc2d09be4a1ee2f53ac834810fb0e3c6a5423c14519d08d3f2c6a0be
---

ExtensionAbility信息，可以通过[bundleManager.getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的ExtensionAbility信息，其中参数[bundleFlags](js-apis-bundlemanager.md#bundleflag)至少包含GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## ExtensionAbilityInfo

PhonePC/2in1TabletTVWearable

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用Bundle名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| moduleName | string | 是 | 否 | ExtensionAbility所属的HAP的名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 是 | 否 | ExtensionAbility名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| labelId | number | 是 | 否 | ExtensionAbility的标签资源ID。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| descriptionId | number | 是 | 否 | ExtensionAbility的描述资源ID。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| iconId | number | 是 | 否 | ExtensionAbility的图标资源ID。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| exported | boolean | 是 | 否 | 判断ExtensionAbility是否可以被其他应用调用，取值为true表示ExtensionAbility可以被其他应用调用，取值为false表示ExtensionAbility不可以被其他应用调用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| extensionAbilityType | [bundleManager.ExtensionAbilityType](js-apis-bundlemanager.md#extensionabilitytype) | 是 | 否 | ExtensionAbility类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| permissions | Array<string> | 是 | 否 | 被其他应用ExtensionAbility调用时需要申请的权限集合。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| applicationInfo | [ApplicationInfo](js-apis-bundlemanager-applicationinfo.md) | 是 | 否 | 应用程序的配置信息。  [getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)或者[getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14)接口获取ExtensionAbilityInfo信息时不会返回该字段内容，可以通过获取[bundleInfo](js-apis-bundlemanager-bundleinfo.md#bundleinfo-1).appInfo对象来获取相关信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| metadata | Array<[Metadata](js-apis-bundlemanager-metadata.md)> | 是 | 否 | ExtensionAbility的元信息。通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE、GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY和GET\_BUNDLE\_INFO\_WITH\_METADATA获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| enabled | boolean | 是 | 否 | ExtensionAbility是否可用，取值为true表示ExtensionAbility可用，取值为false表示ExtensionAbility不可用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| readPermission | string | 是 | 否 | 读取ExtensionAbility数据所需的权限。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| writePermission | string | 是 | 否 | 向ExtensionAbility写数据所需的权限。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| extensionAbilityTypeName11+ | string | 是 | 否 | ExtensionAbility的类型名称，取值请参考[extensionabilities标签下的type字段](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| skills12+ | Array<[Skill](js-apis-bundlemanager-skill.md)> | 是 | 否 | ExtensionAbility的Skills信息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| appIndex12+ | number | 是 | 否 | 应用包的分身索引标识，仅在分身应用中生效。 |
