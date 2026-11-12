---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-hmos-new-features-2600
title: 新增和增强特性
breadcrumb: 版本说明 > 更多版本 > 26.0.0 > DevEco Studio（鸿蒙电脑版） > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-11-12T09:50:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d8b2c0d5a37131bbe450ef8323b5c6db0bb85c6b076a98b288a881e2dd4acdb7
---

鸿蒙电脑DevEco Studio提供开发、构建、调试、调优等能力，集成DevEco Code工具，为开发者打造一站式开发体验。和Windows/macOS版DevEco Studio相比，鸿蒙电脑DevEco Studio在部分能力上仍有差异，具体差异请参见[工具能力差异](../harmonyos-guides/ide-hmos-tools-overview.md#section1450195620327)。

## DevEco Studio 26.0.0 Beta2（26.0.0.220）

### 兼容性配套关系

DevEco Studio 26.0.0.220携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 26.0.0 Release SDK | - |
| Hvigor | 7.26.11 | 编译构建工具DevEco Hvigor（以下简称Hvigor）。 |
| ohpm | 6.0.1 | OpenHarmony三方库的包管理工具。 |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：5.0.0(12) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 5.0.0(12)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 26.0.0.220配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 26.0.0.220 | 命令行工具集版本。 |
| codelinter | 6.0.140 | 执行代码检查与修复的工具。 |
| hvigorw | 7.26.11 | 编译构建工具DevEco Hvigor（以下简称Hvigor）。 |
| ohpm | 6.0.1 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 26.0.0 Release SDK | - |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：5.0.0(12) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hmos-hvigor-build-profile-app.md#section45865492619) | 5.0.0(12)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

* 创建工程时，工程模板新增Car/Wearable/TV设备类型。
* 使用本地真机运行应用时支持通过无线连接的方式进行调试。具体请参考[使用无线连接方式](../harmonyos-guides/ide-hmos-run-device.md#section698053961511)。

## DevEco Studio 26.0.0 Beta1（26.0.0.201）

### 兼容性配套关系

DevEco Studio 26.0.0.201携带的工具列表、支持的API范围及开发态版本号信息如下：

**表3** DevEco Studio

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

**表4** 命令行工具

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
