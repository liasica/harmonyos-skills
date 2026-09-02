---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-pluginbundleinfo
title: PluginBundleInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > PluginBundleInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:51:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9c6b82f18d685a7a563c9f567cdccbbb804fd4740c9ada125bfc165cbd7decc1
---

插件信息，通过接口[pluginBundleManager.getAllLocalPluginInfoForSelf](js-apis-pluginbundlemanager.md#pluginbundlemanagergetalllocalplugininfoforself)获取当前应用已通过自分发方式安装的所有插件信息。该信息包含插件的名称、图标、版本号及模块信息，用于管理已安装的插件，并基于版本号和模块信息进行兼容性检查与更新。

**起始版本：** 26.0.0

## 导入模块

```ts
import { pluginBundleManager } from '@kit.AbilityKit';
```

## PluginBundleInfo

插件信息。用于管理已安装的插件，并基于其版本号和模块信息进行兼容性检查与更新。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| label | string | 是 | 否 | 插件的名称。对应[app.json5](../harmonyos-guides/app-configuration-file.md#配置文件标签)中配置的label字段。 |
| labelId | number | 是 | 否 | 插件名称的资源ID值。是编译构建时根据插件配置的label自动生成的资源ID。 |
| icon | string | 是 | 否 | 插件的图标。对应[app.json5](../harmonyos-guides/app-configuration-file.md#配置文件标签)中配置的icon字段。 |
| iconId | number | 是 | 否 | 插件图标的资源ID值。是编译构建时根据插件配置的icon自动生成的资源ID。 |
| pluginBundleName | string | 是 | 否 | 安装插件的应用包名。对应[app.json5](../harmonyos-guides/app-configuration-file.md#配置文件标签)中配置的bundleName字段。 |
| versionCode | number | 是 | 否 | 插件的版本号。对应[app.json5](../harmonyos-guides/app-configuration-file.md#配置文件标签)中配置的versionCode字段。 |
| versionName | string | 是 | 否 | 插件的版本名称。对应[app.json5](../harmonyos-guides/app-configuration-file.md#配置文件标签)中配置的versionName字段。 |
| pluginModuleInfos | Array<[PluginModuleInfo](js-apis-bundlemanager-pluginbundleinfo.md#pluginmoduleinfo)> | 是 | 否 | 插件的模块信息。 |

## PluginModuleInfo

插件的模块信息。用于描述插件模块的名称和功能说明。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 是 | 否 | 插件模块的名称。对应[module.json5配置文件](../harmonyos-guides/module-configuration-file.md#配置文件标签)中配置的name字段。 |
| descriptionId | number | 是 | 否 | 插件模块描述的资源ID值。是编译构建时根据插件配置的description自动生成的资源ID。 |
| description | string | 是 | 否 | 插件模块的描述信息。对应[module.json5配置文件](../harmonyos-guides/module-configuration-file.md#配置文件标签)中配置的description字段。 |
