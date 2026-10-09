---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-hmos-new-features-2600
title: 新增和增强特性
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > DevEco Studio（鸿蒙电脑版） > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-10-09T08:12:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e758aee51c2d8a78e916da7059cecd108f755eb0e972e4517f108c4967e50bb6
---

鸿蒙电脑DevEco Studio提供开发、构建、调试、调优等能力，集成DevEco Code工具，为开发者打造一站式开发体验。和Windows/macOS版DevEco Studio相比，鸿蒙电脑DevEco Studio在部分能力上仍有差异，具体差异请参见[工具能力差异](../harmonyos-guides/ide-hmos-tools-overview.md#section1450195620327)。

## DevEco Studio 26.0.0 Beta1（26.0.0.201）

### 兼容性配套关系

DevEco Studio 26.0.0.201携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 26.0.0 Release SDK | - |
| Hvigor | 7.26.8 | 编译构建工具DevEco Hvigor（以下简称Hvigor）。 |
| ohpm | 6.0.1 | OpenHarmony三方库的包管理工具。 |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：5.0.0(12) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 5.0.0(12)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 26.0.0.201配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 26.0.0.201 | 命令行工具集版本。 |
| codelinter | 6.0.140 | 执行代码检查与修复的工具。 |
| hvigorw | 7.26.8 | 编译构建工具DevEco Hvigor（以下简称Hvigor）。 |
| ohpm | 6.0.1 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 26.0.0 Release SDK | - |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：5.0.0(12) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 5.0.0(12)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

首次发布！
