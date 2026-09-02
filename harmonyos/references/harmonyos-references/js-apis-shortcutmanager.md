---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-shortcutmanager
title: "@ohos.bundle.shortcutManager (shortcutManager模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.bundle.shortcutManager (shortcutManager模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2083c0c4062216beb4099cc917459402a140d9162f9a58060de366610a272a8d
---

本模块提供应用对于[快捷方式](../harmonyos-guides/typical-scenario-configuration.md)的管理能力，包括设置快捷方式是否显示等。通过快捷方式，用户可以从桌面快速启动应用的特定功能，提升应用的使用便捷性和用户粘性。典型使用场景包括：应用向用户提供常用功能的快速入口、根据用户使用习惯动态调整快捷方式的显示等。

**说明** 

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { shortcutManager } from '@kit.AbilityKit';
```

## shortcutManager.setShortcutVisibleForSelf

setShortcutVisibleForSelf(id: string, visible: boolean) : Promise<void>

设置当前应用指定的快捷方式是否显示。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 快捷方式的ID，通过[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的shortcuts标签下的shortcutId字段获取，取值为长度不超过63字节的字符串。 |
| visible | boolean | 是 | 快捷方式是否显示。true：快捷方式显示；false：快捷方式不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17700070 | The specified shortcut id is not exist. |

**示例：**

```ts
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 请替换为module.json5配置文件中的shortcuts标签下实际配置的shortcutId字段
shortcutManager.setShortcutVisibleForSelf("shortcut_id", false)
  .then(() => {
    console.info('setShortcutVisibleForSelf success');
  }).catch((err: BusinessError) => {
  console.error(`setShortcutVisibleForSelf errData is errCode:${err.code}  message:${err.message}`);
});
```

## shortcutManager.getAllShortcutInfoForSelf

getAllShortcutInfoForSelf(): Promise<Array<ShortcutInfo>>

查询当前应用[配置文件](../harmonyos-guides/module-configuration-file.md#shortcuts标签)中定义的所有快捷方式信息。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ShortcutInfo](js-apis-bundlemanager-shortcutinfo.md)>> | Promise对象，返回应用配置文件中定义的所有快捷方式信息。 |

**示例：**

```ts
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

shortcutManager.getAllShortcutInfoForSelf()
  .then((data: shortcutManager.ShortcutInfo[]) => {
    console.info('getAllShortcutInfoForSelf shortcut data is' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
  console.error(`getAllShortcutInfoForSelf errData is errCode:${err.code}  message:${err.message}`);
});
```

## shortcutManager.isShortcutSupported

isShortcutSupported(): boolean

查询当前设备是否支持快捷方式。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前设备是否支持快捷方式。  返回值为true表示当前设备支持快捷方式；返回值为false表示当前设备不支持快捷方式。 |

**示例：**

```ts
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = shortcutManager.isShortcutSupported();
  console.info('isShortcutSupported data is' + JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  console.error(`isShortcutSupported errData is errCode:${err.code}  message:${err.message}`);
}
```

## ShortcutInfo

type ShortcutInfo = \_ShortcutInfo

应用[module.json5配置文件](../harmonyos-guides/module-configuration-file.md#shortcuts标签)中定义的快捷方式信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [\_ShortcutInfo](js-apis-bundlemanager-shortcutinfo.md#shortcutinfo-1) | 应用module.json5配置文件中定义的快捷方式信息。 |

## ShortcutWant

type ShortcutWant = \_ShortcutWant

快捷方式内定义的目标[wants](../harmonyos-guides/module-configuration-file.md#wants标签)信息集合。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [\_ShortcutWant](js-apis-bundlemanager-shortcutinfo.md#shortcutwant) | 快捷方式内定义的目标[wants](../harmonyos-guides/module-configuration-file.md#wants标签)信息集合。 |

## ParameterItem

type ParameterItem = \_ParameterItem

快捷方式配置信息中的自定义数据。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [\_ParameterItem](js-apis-bundlemanager-shortcutinfo.md#parameteritem) | 快捷方式配置信息中的自定义数据。 |
