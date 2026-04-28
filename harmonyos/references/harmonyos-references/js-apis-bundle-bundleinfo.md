---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo
title: BundleInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > bundle > BundleInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:53+08:00
doc_updated_at: 2026-03-30
content_hash: sha256:ea972007340ec1e15ba36a91e3d91b264da87c04aee16c0550356dce764e4a6b
---

应用包的信息，通过[bundle.getBundleInfo](js-apis-bundle.md#bundlegetbundleinfodeprecated)获取。

说明

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-BundleInfo](js-apis-bundlemanager-bundleinfo.md)替代。

## BundleInfo(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-BundleInfo](js-apis-bundlemanager-bundleinfo.md#bundleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 应用包的名称。 |
| type | string | 是 | 否 | 应用包类型。 |
| appId | string | 是 | 否 | 应用包里应用程序的id。 |
| uid | number | 是 | 否 | 应用包里应用程序的uid。 |
| installTime | number | 是 | 否 | HAP安装时间，单位：毫秒。 |
| updateTime | number | 是 | 否 | HAP更新时间，单位：毫秒。 |
| appInfo | [ApplicationInfo](js-apis-bundle-applicationinfo.md) | 是 | 否 | 应用程序的配置信息。 |
| abilityInfos | Array<[AbilityInfo](js-apis-bundle-abilityinfo.md)> | 是 | 否 | Ability的配置信息  通过调用[bundle.getBundleInfo](js-apis-bundle.md#bundlegetbundleinfodeprecated)接口时，传入GET\_BUNDLE\_WITH\_ABILITIES获取。 |
| reqPermissions | Array<string> | 是 | 否 | 应用运行时需向系统申请的权限集合  通过调用[bundle.getBundleInfo](js-apis-bundle.md#bundlegetbundleinfodeprecated)接口时，传入GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION获取。 |
| reqPermissionDetails | Array<[ReqPermissionDetail](js-apis-bundle-bundleinfo.md#reqpermissiondetaildeprecated)> | 是 | 否 | 应用运行时需向系统申请的权限集合的详细信息  通过调用[bundle.getBundleInfo](js-apis-bundle.md#bundlegetbundleinfodeprecated)接口时，传入GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION获取。 |
| vendor | string | 是 | 否 | 应用包的供应商。 |
| versionCode | number | 是 | 否 | 应用包的版本号。 |
| versionName | string | 是 | 否 | 应用包的版本文本描述信息。 |
| compatibleVersion | number | 是 | 否 | 运行应用包所需要最低的SDK版本号。 |
| targetVersion | number | 是 | 否 | 运行应用包所需要最高SDK版本号。 |
| isCompressNativeLibs | boolean | 是 | 否 | 是否压缩应用包的本地库，取值为true表示压缩应用包的本地库，取值为false表示不压缩应用包的本地库。 |
| hapModuleInfos | Array<[HapModuleInfo](js-apis-bundle-hapmoduleinfo.md)> | 是 | 否 | 模块的配置信息。 |
| entryModuleName | string | 是 | 否 | Entry的模块名称。 |
| cpuAbi | string | 是 | 否 | 应用包的cpuAbi信息。 |
| isSilentInstallation | string | 是 | 否 | 是否通过静默安装。 |
| minCompatibleVersionCode | number | 是 | 否 | 分布式场景下的应用包兼容的最低版本。 |
| entryInstallationFree | boolean | 是 | 否 | Entry是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。 |
| reqPermissionStates8+ | Array<number> | 是 | 否 | 申请权限的授予状态。0表示申请成功，-1表示申请失败。 |

## ReqPermissionDetail(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[ReqPermissionDetail](js-apis-bundlemanager-bundleinfo.md#reqpermissiondetail)替代。

应用运行时需向系统申请的权限集合的详细信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 需要使用的权限名称。 |
| reason | string | 否 | 否 | 描述申请权限的原因。 |
| usedScene | [UsedScene](js-apis-bundle-bundleinfo.md#usedscenedeprecated) | 否 | 否 | 权限使用的场景和时机。 |

## UsedScene(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[UsedScene](js-apis-bundlemanager-bundleinfo.md#usedscene)替代。

描述权限使用的场景和时机。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilities | Array<string> | 否 | 否 | 使用到该权限的Ability集合。 |
| when | string | 否 | 否 | 使用该权限的时机。 |
