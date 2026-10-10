---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo
title: LauncherAbilityInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > LauncherAbilityInfo
category: harmonyos-references
scraped_at: 2026-10-11T07:23:35+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:04fb613d8cbcf9f4cb5d237b8389c3dbeb7dd6a3d40d5ba5ae7a8ed64c0cdc2d
---

桌面应用的Ability信息，可以通过[getLauncherAbilityInfoSync](js-apis-launcherbundlemanager.md#launcherbundlemanagergetlauncherabilityinfosync)获取。

**说明** 

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { launcherBundleManager } from '@kit.AbilityKit';
```

## LauncherAbilityInfo

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| applicationInfo | [ApplicationInfo](js-apis-bundlemanager-applicationinfo.md) | 是 | 否 | launcher ability的应用程序配置信息。 |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 否 | launcher ability的ElementName信息。 |
| labelId | number | 是 | 否 | launcher ability的名称的资源ID值。 |
| iconId | number | 是 | 否 | launcher ability的图标的资源ID值。 |
| userId | number | 是 | 否 | launcher ability的用户ID。 |
| installTime | number | 是 | 否 | launcher ability的安装时间戳，单位ms。 |
