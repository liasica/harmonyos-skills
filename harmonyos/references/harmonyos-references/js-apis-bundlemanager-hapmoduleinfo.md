---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo
title: HapModuleInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > HapModuleInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:47+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:e01dee409a46fbbe8915df4d92c94d3f44f24e6e67f4c337c4723af69b6ccb8b
---

HAP信息，可以通过[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的HAP信息，其中参数[bundleFlags](js-apis-bundlemanager.md#bundleflag)至少包含GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## HapModuleInfo

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 模块名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | string | 是 | 否 | 当前模块入口Ability的[图标](../harmonyos-guides/layered-image.md)，取值为图标资源文件的索引，与模块配置文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)或[extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的icon字段值一致。若未配置入口Ability，则为空。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| iconId | number | 是 | 否 | 当前模块入口Ability的图标[资源ID](../harmonyos-guides/resource-categories-and-access.md#资源目录)值。若未配置入口Ability，则为0。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| label | string | 是 | 否 | 当前模块入口Ability的名称，取值为字符串资源的索引，与模块配置文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)或[extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的label字段值一致。若未配置入口Ability，则为空。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| labelId | number | 是 | 否 | 当前模块入口Ability名称的[资源ID](../harmonyos-guides/resource-categories-and-access.md#资源目录)值。若未配置入口Ability，则为0。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| description | string | 是 | 否 | 模块描述信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| descriptionId | number | 是 | 否 | 描述信息的资源ID值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| mainElementName | string | 是 | 否 | 当前模块的入口UIAbility名称或者ExtensionAbility名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| abilitiesInfo | Array<[AbilityInfo](js-apis-bundlemanager-abilityinfo.md)> | 是 | 否 | 当前模块所有Ability的信息。通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_ABILITY获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| extensionAbilitiesInfo | Array<[ExtensionAbilityInfo](js-apis-bundlemanager-extensionabilityinfo.md)> | 是 | 否 | 当前模块所有ExtensionAbility的信息。通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| metadata | Array<[Metadata](js-apis-bundlemanager-metadata.md)> | 是 | 否 | 当前模块的元数据。通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_METADATA获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| deviceTypes | Array<string> | 是 | 否 | 模块支持安装运行的[设备类型](../harmonyos-guides/module-configuration-file.md#devicetypes标签)的集合。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| installationFree | boolean | 是 | 否 | 模块是否支持免安装（无需用户通过应用市场显式安装），取值为true表示支持免安装，取值为false表示不支持免安装。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| hashValue | string | 是 | 否 | 模块的Hash值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| type | [bundleManager.ModuleType](js-apis-bundlemanager.md#moduletype) | 是 | 否 | 标识当前模块的类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| preloads | Array<[PreloadItem](js-apis-bundlemanager-hapmoduleinfo.md#preloaditem)> | 是 | 否 | 元服务中模块的预加载列表。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| dependencies | Array<[Dependency](js-apis-bundlemanager-hapmoduleinfo.md#dependency)> | 是 | 否 | 模块运行依赖的动态共享库列表。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fileContextMenuConfig11+ | string | 是 | 否 | 模块的文件菜单配置。通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_MENU获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| routerMap12+ | Array<[RouterItem](js-apis-bundlemanager-hapmoduleinfo.md#routeritem12)> | 是 | 否 | [模块的路由表配置](../harmonyos-guides/module-configuration-file.md#routermap标签)。通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_ROUTER\_MAP获取。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| codePath12+ | string | 是 | 否 | 模块的安装路径。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| nativeLibraryPath12+ | string | 是 | 否 | 应用程序内模块本地库文件路径。 |

## PreloadItem

PhonePC/2in1TabletTVWearable

描述元服务中模块的预加载模块信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 是 | 否 | 模块名称。 |

## Dependency

PhonePC/2in1TabletTVWearable

描述模块所依赖的动态共享库信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName10+ | string | 是 | 否 | 标识当前模块依赖的共享包包名。 |
| moduleName | string | 是 | 否 | 标识当前模块依赖的共享包模块名。 |
| versionCode10+ | number | 是 | 否 | 标识当前共享包的版本号。 |

## RouterItem12+

PhonePC/2in1TabletTVWearable

描述模块配置的路由表信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 标识跳转页面的名称。 |
| pageSourceFile | string | 是 | 否 | 标识页面在模块内的路径。 |
| buildFunction | string | 是 | 否 | 标识被@Builder修饰的函数，该函数描述页面的UI。 |
| data | Array<[DataItem](js-apis-bundlemanager-hapmoduleinfo.md#dataitem12)> | 是 | 否 | 标识[路由表配置文件](../harmonyos-guides/module-configuration-file.md#routermap标签)中的字符串自定义数据，即data字段的信息，该字段已由系统解析，无需开发者自行解析。 |
| customData | string | 是 | 否 | 标识[路由表配置文件](../harmonyos-guides/module-configuration-file.md#routermap标签)中的任意类型的自定义数据，即customData字段的JSON字符串，开发者需要调用JSON.parse函数解析出具体内容。 |

## DataItem12+

PhonePC/2in1TabletTVWearable

描述模块配置的路由表中的自定义数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 是 | 否 | 标识路由表自定义数据的键。 |
| value | string | 是 | 否 | 标识路由表自定义数据的值。 |
