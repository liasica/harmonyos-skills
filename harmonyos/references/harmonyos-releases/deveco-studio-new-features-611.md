---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features-611
title: 新增和增强特性
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > DevEco Studio > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:33+08:00
doc_updated_at: 2026-08-06
content_hash: sha256:f55b9e8b99feead2755ce308fa1750072f5c4e306a431052427f246b54fd3b49
---

## DevEco Studio 6.1.1 Release（6.1.1.300）

### 兼容性配套关系

DevEco Studio 6.1.1.300携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 6.1.1 Release SDK | - |
| HarmonyOS Emulator | 6.1.1.350 | 模拟器。 |
| Hvigor | 6.24.4 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.285 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.1.300配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.1.300 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.24.4 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.285 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 6.1.1 Release SDK | - |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

设备无线连接界面优化，提升调试体验。具体请参考[使用无线连接方式](../harmonyos-guides/ide-run-device.md#section9315596477)。

## DevEco Studio 6.1.1 Release（6.1.1.290）

### 兼容性配套关系

DevEco Studio 6.1.1.290携带的工具列表、支持的API范围及开发态版本号信息如下：

**表3** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 6.1.1 Release SDK | - |
| HarmonyOS Emulator | 6.1.1.300 | 模拟器。 |
| Hvigor | 6.24.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.285 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.1.290配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表4** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.1.290 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.24.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.285 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 6.1.1 Release SDK | - |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

模块级build-profile.json5文件新增widget/transitiveDeps字段，用于指定在卡片依赖字节码HAR的场景下，编译卡片时是否收集字节码HAR的直接和间接依赖。具体请参考[模块级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)。

## DevEco Studio 6.1.1 Release（6.1.1.280）

### 兼容性配套关系

DevEco Studio 6.1.1.280携带的工具列表、支持的API范围及开发态版本号信息如下：

**表5** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 6.1.1 Release SDK | - |
| HarmonyOS Emulator | 6.1.1.200 | 模拟器。 |
| Hvigor | 6.24.2 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.268 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.1.280配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表6** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.1.280 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.24.2 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.268 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 6.1.1 Release SDK | - |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

**构建应用**

* 工程级build-profile.json5文件的strictMode下新增strictCheckerOnly字段，用于指定是否对.ets文件仅执行严格语法检查，仅执行严格语法检查可以减少端到端编译时间，提升编译性能。具体请参考[工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md)。

**优化应用性能**

* All Heap & Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的设置项中新增Sampling Size，用于设置内存数据采样大小。

## DevEco Studio 6.1.1 Beta1（6.1.1.268）

### 兼容性配套关系

DevEco Studio 6.1.1.268携带的工具列表、支持的API范围及开发态版本号信息如下：

**表7** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 6.1.1 Beta1 SDK | - |
| HarmonyOS Emulator | 6.1.1.100 | 模拟器。 |
| Hvigor | 6.24.1 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.268 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.1.268配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表8** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.1.268 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.24.1 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.2.268 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 6.1.1 Beta1 SDK | - |
| modelVersion | 6.1.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.1(24) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.1(24) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

**开发环境搭建**

* DevEco Studio支持开发API 24工程。

**编写与调试应用**

* Hot Reload能力增强，支持修改C++代码和资源文件。具体请参考[Hot Reload](../harmonyos-guides/ide-hot-reload.md)。
* DevEco Studio支持解析更多AppFreeze日志，包括Binder通信信息、主线程任务队列和采样栈数据，提升开发者定位效率。具体请参考[查看AppFreeze（应用冻屏）日志](../harmonyos-guides/ide-faultlog-appfreeze.md)。

**优化应用性能**

* All Heap & Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的配置项新增Record Async Stack，用于开启异步栈缝合，开启后在异步回栈时支持多回一层异步栈帧。具体请参考[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。
* 新增ComMemory模板，用于分析UI界面各组件内存的分配情况，帮助定位UI组件内存泄漏问题。具体请参考[UI组件内存：ComMemory分析](../harmonyos-guides/ide-commemory.md)。
* 在Snapshot模板的Statistics页签中选中一个构造器或实例结点，支持查看该节点构造器下的所有实例到GC Roots的最短路径。具体请参考[Snapshot模板基本操作](../harmonyos-guides/ide-snapshot-basic-operations.md)。

**命令行工具**

* 工程级oh-package.json5文件新增properties字段，用于多环境下的依赖管理。具体请参考[oh-package.json5](../harmonyos-guides/ide-oh-package-json5.md)。
