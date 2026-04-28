---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-launcherbundlemanager
title: @ohos.bundle.launcherBundleManager (launcherBundleManager模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.bundle.launcherBundleManager (launcherBundleManager模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:896827c50f36e6535374942066ad6dfbdda8551d79f18485674ab1796bddf2c1
---

本模块支持launcher应用（桌面有图标的应用）所需的查询能力，支持[LauncherAbilityInfo](js-apis-bundlemanager-launcherabilityinfo.md)信息的查询。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { launcherBundleManager } from '@kit.AbilityKit';
```

## launcherBundleManager.getLauncherAbilityInfoSync

PhonePC/2in1TabletTVWearable

getLauncherAbilityInfoSync(bundleName: string, userId: number) : Array<[LauncherAbilityInfo](js-apis-bundlemanager-launcherabilityinfo.md)>

查询指定bundleName及用户的[LauncherAbilityInfo](js-apis-bundlemanager-launcherabilityinfo.md)。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| userId | number | 是 | 被查询的用户ID，可以通过[getOsAccountLocalId接口](js-apis-osaccount.md#getosaccountlocalid9)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[LauncherAbilityInfo](js-apis-bundlemanager-launcherabilityinfo.md)> | Array形式返回bundle包含的[LauncherAbilityInfo](js-apis-bundlemanager-launcherabilityinfo.md)信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ohos.bundle错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Verify permission denied. |
| 801 | Capability not support. |
| 17700001 | The specified bundle name is not found. |
| 17700004 | The specified user ID is not found. |

**示例：**

```
1. import { launcherBundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let data = launcherBundleManager.getLauncherAbilityInfoSync("com.example.demo", 100);
6. console.info("data is " + JSON.stringify(data));
7. } catch (errData) {
8. let code = (errData as BusinessError).code;
9. let message = (errData as BusinessError).message;
10. console.error(`errData is errCode:${code}  message:${message}`);
11. }
```

## LauncherAbilityInfo

PhonePC/2in1TabletTVWearable

type LauncherAbilityInfo = \_LauncherAbilityInfo

LauncherAbilityInfo信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [\_LauncherAbilityInfo](js-apis-bundlemanager-launcherabilityinfo.md) | 桌面应用的Ability信息。 |

## ShortcutInfo20+

PhonePC/2in1TabletTVWearable

type ShortcutInfo = \_ShortcutInfo

应用[module.json5配置文件](../harmonyos-guides/module-configuration-file.md#shortcuts标签)中定义的快捷方式信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [\_ShortcutInfo](js-apis-bundlemanager-shortcutinfo.md#shortcutinfo-1) | 应用module.json5配置文件中定义的快捷方式信息。 |

## ShortcutWant20+

PhonePC/2in1TabletTVWearable

type ShortcutWant = \_ShortcutWant

快捷方式内定义的目标[wants](../harmonyos-guides/module-configuration-file.md#wants标签)信息集合。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [\_ShortcutWant](js-apis-bundlemanager-shortcutinfo.md#shortcutwant) | 快捷方式内定义的目标[wants](../harmonyos-guides/module-configuration-file.md#wants标签)信息集合。 |

## ParameterItem20+

PhonePC/2in1TabletTVWearable

type ParameterItem = \_ParameterItem

快捷方式配置信息中的自定义数据。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [\_ParameterItem](js-apis-bundlemanager-shortcutinfo.md#parameteritem) | 快捷方式配置信息中的自定义数据。 |
