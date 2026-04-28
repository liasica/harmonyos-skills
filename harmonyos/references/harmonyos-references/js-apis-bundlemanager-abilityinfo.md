---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo
title: AbilityInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > AbilityInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:45+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:1b9e0ac36ab3c3aba049ecbf9f4884e690514dfce4f319cf8418e85455b21467
---

Ability信息，可以通过[bundleManager.getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取Ability信息，其中参数[bundleFlags](js-apis-bundlemanager.md#bundleflag)至少包含GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_ABILITY。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## AbilityInfo

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用Bundle名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| moduleName | string | 是 | 否 | Ability所属的模块名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 是 | 否 | Ability名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| label | string | 是 | 否 | Ability对用户显示的名称的资源描述符，对应[module.json5](../harmonyos-guides/module-configuration-file.md)中abilities下配置的label字段。  **说明：** 从API version 20开始，如果是通过[bundleManager.getAbilityInfo](js-apis-bundlemanager.md#bundlemanagergetabilityinfo20)获取Ability信息，该字段为Ability对用户显示的名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| labelId | number | 是 | 否 | Ability的标签资源id，是编译构建时根据应用配置abilities下的label自动生成的资源id。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| description | string | 是 | 否 | Ability的描述，对应[module.json5](../harmonyos-guides/module-configuration-file.md)中abilities下配置的description字段，用于描述当前ability提供的页面内容和功能作用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| descriptionId | number | 是 | 否 | Ability的描述资源id，是编译构建时根据应用配置abilities下的description自动生成的资源id。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | string | 是 | 否 | Ability的图标资源描述符，对应[module.json5](../harmonyos-guides/module-configuration-file.md)中abilities下配置的icon字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| iconId | number | 是 | 否 | Ability的图标资源id，是编译构建时根据应用配置abilities下的icon自动生成的资源id。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| process | string | 是 | 否 | Ability的进程名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| exported | boolean | 是 | 否 | 判断Ability是否可以被其他应用拉起，取值为true表示Ability可以被其他应用拉起，取值为false表示Ability不可以被其他应用拉起。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| type | [bundleManager.AbilityType](js-apis-bundlemanager.md#abilitytype) | 是 | 否 | Ability类型。  **模型约束：** 此接口仅可在FA模型下使用。 |
| orientation | [bundleManager.DisplayOrientation](js-apis-bundlemanager.md#displayorientation) | 是 | 否 | Ability的显示模式。来源于[module.json5](../harmonyos-guides/module-configuration-file.md)中abilities标签下配置的orientation字段，如果module.json5配置文件中orientation配置枚举，orientation属性有值且非0，取值详情参考[显示模式枚举](js-apis-bundlemanager.md#displayorientation)；如果配置文件中配置的是资源索引，orientation属性值为0。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| launchType | [bundleManager.LaunchType](js-apis-bundlemanager.md#launchtype) | 是 | 否 | Ability的启动模式，在启动的时候是否以多实例启动，详情参考[启动模式枚举](js-apis-bundlemanager.md#launchtype) 。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| permissions | Array<string> | 是 | 否 | 被其他应用拉起/访问时，其他应用需要申请的权限集合，只有当前AbilityInfo的exported为true，即当前Ability可以被其他应用拉起时，才会查看其他应用是否存在拉起/访问的权限。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| readPermission | string | 是 | 否 | 读取Ability数据所需的权限。  **模型约束：** 此接口仅可在FA模型下使用。 |
| writePermission | string | 是 | 否 | 向Ability写数据所需的权限。  **模型约束：** 此接口仅可在FA模型下使用。 |
| uri | string | 是 | 否 | 获取Ability的统一资源标识符（URI）。  **模型约束：** 此接口仅可在FA模型下使用。 |
| deviceTypes | Array<string> | 是 | 否 | Ability支持的设备类型，来源于module.json5配置的[deviceTypes](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| applicationInfo | [ApplicationInfo](js-apis-bundlemanager-applicationinfo.md) | 是 | 否 | 应用程序的配置信息。  [getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)或者[getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14)接口获取AbilityInfo信息时不会返回该字段内容，可以通过获取[bundleInfo](js-apis-bundlemanager-bundleinfo.md#bundleinfo-1).appInfo对象来获取相关信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| metadata | Array<[Metadata](js-apis-bundlemanager-metadata.md)> | 是 | 否 | Ability的元信息。可以配置成系统定义的参数，使用系统提供的能力，例如[快捷方式](../harmonyos-guides/module-configuration-file.md#shortcuts标签)、[窗口元数据配置](../harmonyos-guides/window-config-m.md)等。也可以自定义配置参数，通过调用[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE、GET\_BUNDLE\_INFO\_WITH\_ABILITY和GET\_BUNDLE\_INFO\_WITH\_METADATA获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| enabled | boolean | 是 | 否 | Ability是否可用，可用表示可以拉起或者查询，不可用时调用[getAbilityInfo](js-apis-bundlemanager.md#bundlemanagergetabilityinfo20)查询ability需要携带GET\_ABILITY\_INFO\_WITH\_DISABLE的AbilityFlag，取值为true表示Ability可用，取值为false表示Ability不可用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| supportWindowModes | Array<[bundleManager.SupportWindowMode](js-apis-bundlemanager.md#supportwindowmode)> | 是 | 否 | Ability支持的窗口模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowSize | [WindowSize](js-apis-bundlemanager-abilityinfo.md#windowsize) | 是 | 否 | Ability窗口尺寸。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| excludeFromDock12+ | boolean | 是 | 否 | 判断Ability是否可以在dock区域隐藏图标，取值为true表示可以隐藏，取值为false不可以隐藏。  **说明：** 该字段不生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| skills12+ | Array<[Skill](js-apis-bundlemanager-skill.md)> | 是 | 否 | Ability的Skills信息，标识UIAbility组件或者ExtensionAbility组件能够接收的[Want](../harmonyos-guides/want-overview.md)的特征。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| appIndex12+ | number | 是 | 否 | 应用包的分身索引标识，仅在[分身应用](../harmonyos-guides/app-clone.md)中生效。 |
| orientationId14+ | number | 是 | 否 | Ability的显示模式资源id。来源于[module.json5](../harmonyos-guides/module-configuration-file.md)中abilities标签下的orientation字段，如果module.json5配置文件中orientation配置枚举，orientationId属性值为0；如果配置文件中配置的是资源索引，orientationId属性值为非0，为编译构建时生成的资源id索引。当orientationId不为0时表示当前显示模式为自定义配置，需要使用orientationId去资源管理获取对应的资源，当orientationId为0时表示未配置资源。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## WindowSize

PhonePC/2in1TabletTVWearable

描述窗口尺寸。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxWindowRatio | number | 是 | 否 | 表示自由窗口状态下窗口的最大宽高比；取值范围0-1，例如：0.12。 |
| minWindowRatio | number | 是 | 否 | 表示自由窗口状态下窗口的最小宽高比；取值范围0-1，例如：0.5。 |
| maxWindowWidth | number | 是 | 否 | 表示自由窗口状态下窗口的最大宽度，宽度单位为vp。 |
| minWindowWidth | number | 是 | 否 | 表示自由窗口状态下窗口的最小宽度，宽度单位为vp。 |
| maxWindowHeight | number | 是 | 否 | 表示自由窗口状态下窗口的最大高度，高度单位为vp。 |
| minWindowHeight | number | 是 | 否 | 表示自由窗口状态下窗口的最小高度，高度单位为vp。 |
