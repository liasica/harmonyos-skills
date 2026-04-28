---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo
title: LauncherAbilityInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > LauncherAbilityInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:066c4b77bd31459a4f6f0a613357c75b246f2728ecd56dfbf722005e2d4f881d
---

桌面应用的Ability信息，可以通过[getLauncherAbilityInfoSync](js-apis-launcherbundlemanager.md#launcherbundlemanagergetlauncherabilityinfosync)获取。

说明

本模块首批接口从API version 18 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { launcherBundleManager } from '@kit.AbilityKit';
```

## LauncherAbilityInfo

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| applicationInfo | [ApplicationInfo](js-apis-bundlemanager-applicationinfo.md) | 是 | 否 | launcher ability的应用程序配置信息。 |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 否 | launcher ability的ElementName信息。 |
| labelId | number | 是 | 否 | launcher ability的名称的资源ID值。 |
| iconId | number | 是 | 否 | launcher ability的图标的资源ID值。 |
| userId | number | 是 | 否 | launcher ability的用户ID。 |
| installTime | number | 是 | 否 | launcher ability的安装时间戳，单位毫秒。 |
