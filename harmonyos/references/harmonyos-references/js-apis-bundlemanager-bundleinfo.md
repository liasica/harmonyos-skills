---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo
title: BundleInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > BundleInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:64426790dc465ff6746bedb9cc38ebfed41c7429cdb9e1ef5df9c1b1e69beb97
---

应用包信息，可以通过[bundleManager.getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的应用包信息，其中参数[bundleFlags](js-apis-bundlemanager.md#bundleflag)指定所返回的[BundleInfo](js-apis-bundlemanager-bundleinfo.md)中所包含的信息。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## BundleInfo

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 应用包的名称，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的bundleName字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| vendor | string | 是 | 否 | 应用包的供应商，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的vendor字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| versionCode | number | 是 | 否 | 应用包的版本号，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的versionCode字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| versionName | string | 是 | 否 | 应用包的版本文本描述信息，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的versionName字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| minCompatibleVersionCode | number | 是 | 否 | 分布式场景下的应用包兼容的最低版本，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的minCompatibleVersionCode字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| targetVersion | number | 是 | 否 | 应用运行目标版本，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的targetAPIVersion字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| appInfo | [ApplicationInfo](js-apis-bundlemanager-applicationinfo.md) | 是 | 否 | 应用程序的配置信息，通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_APPLICATION获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| hapModulesInfo | Array<[HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md)> | 是 | 否 | 模块的配置信息，通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| reqPermissionDetails | Array<[ReqPermissionDetail](js-apis-bundlemanager-bundleinfo.md#reqpermissiondetail)> | 是 | 否 | 应用运行时需向系统申请的权限集合的详细信息，通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION获取。reqPermissionDetails数组和permissionGrantStates数组的索引顺序一一对应，即reqPermissionDetails[2]的授权状态为permissionGrantStates[2]。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| permissionGrantStates | Array<[bundleManager.PermissionGrantState](js-apis-bundlemanager.md#permissiongrantstate)> | 是 | 否 | 申请权限的授予状态，通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION获取。reqPermissionDetails数组和permissionGrantStates数组的索引顺序一一对应，即reqPermissionDetails[2]的授权状态为permissionGrantStates[2]。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| signatureInfo | [SignatureInfo](js-apis-bundlemanager-bundleinfo.md#signatureinfo) | 是 | 否 | 应用包的签名信息，通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| installTime | number | 是 | 否 | 应用包安装时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：**  设备出厂首次开机时，如果未获取到当前时间，会以Unix时间戳基准（1970-01-01 08:00:00 UTC+8）作为当前系统的起始时间。例如，开机后未获取到时间，等待32s之后安装成功，则应用包安装时间戳为32000。 |
| updateTime | number | 是 | 否 | 应用包更新时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| routerMap12+ | Array<[RouterItem](js-apis-bundlemanager-hapmoduleinfo.md#routeritem12)> | 是 | 否 | 应用的路由表配置，由hapModulesInfo下的routerMap信息，根据RouterItem中的name字段进行去重后合并得到。通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_ROUTER\_MAP获取。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| appIndex12+ | number | 是 | 否 | 应用包的分身索引标识，仅在分身应用中生效。 |
| firstInstallTime18+ | number | 是 | 是 | 应用在当前设备的首次安装时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒，预置应用的首次安装时间戳为1533657660000。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| buildVersion23+ | string | 是 | 是 | 应用包的构建版本号，用于标识相同发布版本下的不同构建版本包，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的buildVersion字段。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## ReqPermissionDetail

PhonePC/2in1TabletTVWearable

应用运行时需向系统申请的权限集合的详细信息。

说明

* 如果应用内多包申请的权限名称一样，但是权限申请理由不一致，系统只会返回一个权限申请理由，优先级从高到低顺序为entry类型HAP、feature类型HAP、应用内HSP。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 需要使用的[权限名称](../harmonyos-guides/app-permissions.md)。 |
| moduleName10+ | string | 否 | 否 | 申请该权限的module名称。 |
| reason | string | 否 | 否 | 描述申请权限的原因。 |
| reasonId | number | 否 | 否 | 描述申请权限的原因ID。 |
| usedScene | [UsedScene](js-apis-bundlemanager-bundleinfo.md#usedscene) | 否 | 否 | 权限使用的场景和时机。 |

## UsedScene

PhonePC/2in1TabletTVWearable

描述权限使用的场景和时机。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilities | Array<string> | 否 | 否 | 使用到该权限的Ability集合。 |
| when | string | 否 | 否 | 使用该权限的时机。支持的取值有inuse（使用时）、always（始终）。 |

## SignatureInfo

PhonePC/2in1TabletTVWearable

描述应用包的签名信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appId | string | 是 | 否 | 应用的appId，表示应用的唯一标识，详情信息可参考[什么是appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fingerprint | string | 是 | 否 | 应用包的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| appIdentifier11+ | string | 是 | 否 | 应用的唯一标识。详情信息可参考[什么是appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| certificate14+ | string | 是 | 是 | 应用的证书公钥。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## AppCloneIdentity14+

PhonePC/2in1TabletTVWearable

描述应用包的身份信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用的bundleName。 |
| appIndex | number | 是 | 否 | 应用包的分身索引信息。 |
