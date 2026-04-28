---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features-503-release
title: DevEco Studio
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > DevEco Studio
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:43+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:7794e94a8f5721b2bb94e67d1a5fb96ab0f04424c6680fb6e8040c438ab16603
---

## DevEco Studio 5.0.3 Release（5.0.9.310）兼容性配套关系

DevEco Studio 5.0.9.310携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| DevEco Studio | DevEco Studio 5.0.3 Release（5.0.9.310） | - |
| HarmonyOS SDK | HarmonyOS 5.0.3 Release SDK | - |
| HarmonyOS Emulator | HarmonyOS Emulator 5.0.3 Release（5.0.9.300） | 模拟器，当前支持手机（包括折叠屏）、平板。 |
| Hvigor | 5.15.5 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.12 | OpenHarmony三方库的包管理工具。 |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.3 | 开发态版本号。 |

DevEco Studio 5.0.9.310配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 5.0.9.310 | 命令行工具集版本。 |
| codelinter | 5.0.510 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 5.15.5 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.12 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 5.0.3 Release SDK | - |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.3 | 开发态版本号。 |

## DevEco Studio 5.0.3 Release（5.0.9.300）兼容性配套关系

DevEco Studio 5.0.9.300携带的工具列表、支持的API范围及开发态版本号信息如下：

**表3** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| DevEco Studio | DevEco Studio 5.0.3 Release（5.0.9.300） | - |
| HarmonyOS SDK | HarmonyOS 5.0.3 Release SDK | - |
| HarmonyOS Emulator | HarmonyOS Emulator 5.0.3 Release（5.0.9.300） | 模拟器，当前支持手机（包括折叠屏）、平板。 |
| Hvigor | 5.15.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.12 | OpenHarmony三方库的包管理工具。 |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.3 | 开发态版本号。 |

DevEco Studio 5.0.9.300配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表4** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 5.0.9.300 | 命令行工具集版本。 |
| codelinter | 5.0.510 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 5.15.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.12 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 5.0.3 Release SDK | - |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/元服务兼容的最低SDK版本。 |
| modelVersion | 5.0.3 | 开发态版本号。 |

## DevEco Studio 5.0.3 Release（5.0.9.310）新增和增强特性

无新增和增强特性。

## DevEco Studio 5.0.3 Release（5.0.9.300）新增和增强特性

### 新增特性

* DevEco Studio支持开发API 15工程。
* 新建工程时，将在AppScope/resource/base/media目录下自动生成分层图标配置文件layered\_image.json及前后背景图标foreground.png、background.png，并将app.json5中icon字段值设置为分层图标配置文件。具体请参考[app.json5](../harmonyos-guides/app-configuration-file.md#配置文件标签)中的icon标签。
* AppAnalyzer的场景化体检新增支持三类场景：页面滑动、应用冷启动和页面内转场。具体请参考[体检场景](../harmonyos-guides/ide-app-analyzer-scenes.md)。
* 新增部分ACL权限支持通过自动签名快速申请。具体请参考[支持ACL权限](../harmonyos-guides/ide-signing.md#section5301916183411)。
* 工程级和HAR模块的build-profile.json5中buildOption/arkOptions下新增branchElimination字段，用于指定是否启用代码分支裁剪，减少编译产物大小，开启后，在release编译模式下，不会被执行到的代码分支会被裁剪掉。具体请参考[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile.md)。
* 工程级、模块级build-profile.json5中新增以下参数。具体请参考[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile.md)。
  + buildOption下新增removePermissions数组，用于指定编译时需要删除的依赖包中的冗余权限，模块本身的权限不会被删除，仅对HAP/HSP模块生效。
  + buildOption/resOptions下新增copyCodeResource对象，用于指定是否将src/main/ets目录下的资源文件（非源码文件）打包到产物中，支持根据glob语法排除匹配到的文件，匹配到的文件不会被打包到产物中。
* hvigor-config.json5的properties下新增ohos.arkCompile.emptyBundleName字段，用于指定编译后的产物，bundleName字段是否为空值。具体请参考[hvigor-config.json5](../harmonyos-guides/ide-hvigor-set-options.md)。
* CodeGenie接入DeepSeek智慧体，提供智能问答等AI能力。
* 针对编译构建类报错场景，支持点击报错内容后方的Explain with AI图标，通过CodeGenie分析并提供该报错可能的错误原因和解决方案。具体请参考[编译报错智能分析](../harmonyos-guides/ide-compilation-error-analysis.md)。

### 变更特性

* 应用沙箱支持文件夹的新增、删除、上传、下载等操作，命令行方式访问应用沙箱更改为通过hdc工具进行访问。具体请参考[访问设备文件](../harmonyos-guides/ide-device-file-explorer.md)。
* 混淆助手的打开方式更改为菜单栏**Tools > ObfuscationHelper**。具体可参考[通过混淆助手配置保留选项](../harmonyos-guides/ide-build-obfuscation.md#section19439175917123)。
