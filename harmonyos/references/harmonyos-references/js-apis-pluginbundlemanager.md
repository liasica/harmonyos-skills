---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pluginbundlemanager
title: "@ohos.bundle.pluginBundleManager (pluginBundleManager模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.bundle.pluginBundleManager (pluginBundleManager模块)
category: harmonyos-references
scraped_at: 2026-09-02T14:51:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4162b1e9b78c3c9f1c3ca7ff52d10acbd5268742eeb4b3f609afd160f7c0ad13
---

本模块提供应用对自分发插件的管理能力，包括安装、卸载本地插件。

**起始版本：** 26.0.0

## 导入模块

```ts
import { pluginBundleManager } from '@kit.AbilityKit';
```

## pluginBundleManager.installLocalPlugin

installLocalPlugin(pluginFilePaths: Array<string>): Promise<void>

为当前应用安装自分发插件（即应用通过自有渠道分发、自主管理的插件）。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pluginFilePaths | Array<string> | 是 | 插件文件路径数组，表示要安装的插件文件的路径列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Calling interface without permission 'ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN'. |
| 17700010 | Failed to install the plugin because the plugin fails to be parsed. |
| 17700011 | Failed to install the plugin because the plugin signature fails to be verified. |
| 17700012 | Failed to install the plugin because the HSP path is invalid or the HSP is too large. |
| 17700015 | Failed to install the plugin because they have different configuration information. |
| 17700016 | Failed to install the plugin because of insufficient system disk space. |
| 17700017 | Failed to install the plugin since the version of the plugin to install is too early. |
| 17700048 | Failed to install the plugin because the code signature verification failed. |
| 17700052 | Failed to install the plugin because debug bundle cannot be installed under non-developer mode. |
| 17700073 | Failed to install the plugin because a plugin with the same bundle name but different signature information exists on the device. |
| 17700087 | Failed to install the plugin because the current device does not support plugins. |
| 17700091 | Failed to install the plugin because the plugin name is the same as the host bundle name. |

**示例：**

```ts
import { pluginBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 请替换为实际的插件文件路径
let pluginPaths: Array<string> = ["/data/storage/el2/base/haps/entry/plugin.hsp"];

pluginBundleManager.installLocalPlugin(pluginPaths)
  .then(() => {
    console.info('installLocalPlugin success');
  }).catch((err: BusinessError) => {
  console.error(`installLocalPlugin errData is errCode:${err.code}  message:${err.message}`);
});
```

## pluginBundleManager.uninstallLocalPlugin

uninstallLocalPlugin(pluginBundleName: string): Promise<void>

卸载当前应用已通过自分发方式安装的指定插件。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pluginBundleName | string | 是 | 插件的Bundle名称，表示要卸载的插件的应用包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Calling interface without permission 'ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN'. |
| 17700092 | Failed to uninstall the plugin because the specified plugin is not found. |

**示例：**

```ts
import { pluginBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 请替换为实际的插件Bundle名称
let pluginBundleName = "com.example.plugin";

pluginBundleManager.uninstallLocalPlugin(pluginBundleName)
  .then(() => {
    console.info('uninstallLocalPlugin success');
  }).catch((err: BusinessError) => {
  console.error(`uninstallLocalPlugin errData is errCode:${err.code}  message:${err.message}`);
});
```

## pluginBundleManager.getAllLocalPluginInfoForSelf

getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>

查询当前应用中所有自分发插件的信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[PluginBundleInfo](js-apis-bundlemanager-pluginbundleinfo.md#pluginbundleinfo-1)>> | Promise对象，返回当前应用已安装的所有本地插件信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Calling interface without permission 'ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN'. |

**示例：**

```ts
import { pluginBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

pluginBundleManager.getAllLocalPluginInfoForSelf().then((data): void => {
  console.info('getAllLocalPluginInfoForSelf plugin data is' + JSON.stringify(data));
}).catch((err: Error): void => {
  const businessErr = err as BusinessError;
  console.error(`getAllLocalPluginInfoForSelf errData is errCode:${businessErr.code}  message:${businessErr.message}`);
});
```

## PluginBundleInfo

type PluginBundleInfo = \_PluginBundleInfo

插件信息。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_PluginBundleInfo](js-apis-bundlemanager-pluginbundleinfo.md#pluginbundleinfo-1) | 插件信息。 |

## PluginModuleInfo

type PluginModuleInfo = \_PluginModuleInfo

插件的模块信息。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_PluginModuleInfo](js-apis-bundlemanager-pluginbundleinfo.md#pluginmoduleinfo) | 插件的模块信息。 |
