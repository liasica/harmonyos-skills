---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features-610
title: 新增和增强特性
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > DevEco Studio > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be665743439713d5f8057d3f502abe84a3f0f4064e228d544ec41557ece5769c
---

当前为DevEco Studio最新版本说明文档，如需查看DevEco Studio其它历史版本的功能新增、变更情况，请在左侧文档目录中选择相应版本。

## DevEco Studio 6.1.0 Release（6.1.0.830）兼容性配套关系

DevEco Studio 6.1.0.830携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 6.1.0 Release SDK | - |
| HarmonyOS Emulator | 6.1.0.410 | 模拟器。 |
| Hvigor | 6.23.5 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1.830 | OpenHarmony三方库的包管理工具。 |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.0.830配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.0.830 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.23.5 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1.830 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 6.1.0 Release SDK | - |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

## DevEco Studio 6.1.0 Release（6.1.0.830）新增和增强特性

阔折叠品类下新增Pura X Max模拟器。

## DevEco Studio 6.1.0 Release（6.1.0.818）兼容性配套关系

DevEco Studio 6.1.0.818携带的工具列表、支持的API范围及开发态版本号信息如下：

**表3** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS Emulator | 6.1.0.400 | 模拟器。 |
| Hvigor | 6.23.4 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1.816 | OpenHarmony三方库的包管理工具。 |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.0.818配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表4** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.0.818 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.23.4 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1.816 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

## DevEco Studio 6.1.0 Release（6.1.0.818）新增和增强特性

AppAnalyzer支持导出、导入体检报告。具体请参考[管理体检报告](../harmonyos-guides/ide-app-analyzer-history-reports.md)。

## DevEco Studio 6.1.0 Beta2（6.1.0.816）兼容性配套关系

DevEco Studio 6.1.0.816携带的工具列表、支持的API范围及开发态版本号信息如下：

**表5** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS Emulator | 6.1.0.300 | 模拟器。 |
| Hvigor | 6.23.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1.816 | OpenHarmony三方库的包管理工具。 |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.0.816配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表6** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.0.816 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.23.3 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1.816 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

## DevEco Studio 6.1.0 Beta2（6.1.0.816）新增和增强特性

**开发环境搭建**

* 在API 23及以上工程，支持Car设备添加RemoteNotificationAbility。具体请参考[在模块中添加Ability](../harmonyos-guides/ide-add-new-ability.md)。
* 在API 23及以上工程，支持Car设备添加Map Page和Payment Page。具体请参考[添加Page](../harmonyos-guides/ide-add-page.md)。

**使用AI智能辅助编程**

* 新增工程问答。具体请参考[工程问答](../harmonyos-guides/ide-project-ask.md)。
* 代码续写时支持使用模型和提示词。具体请参考[代码续写](../harmonyos-guides/ide-code-continuation.md)。
* 支持添加和管理提示词库。具体请参考[自定义提示词库（Prompts）配置](../harmonyos-guides/ide-prompts.md)。

**编写与调试应用**

* API变更查询接入CodeGenie快速问答功能，CodeGenie提供根据代码文件和变更文档输出非兼容API的修改建议，以及新增筛选API变更类型功能。具体请参考[代码阅读](../harmonyos-guides/ide-editer-overview.md#section234174215231)。
* 如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。同时模拟器会展示在设备列表中，选择模拟器并点击运行按钮，即可一键完成启动模拟器、编译构建、推包运行操作。具体请参考[创建模拟器](../harmonyos-guides/ide-emulator-create.md)。
* 三折叠模拟器的工具栏新增6个按键，用于对屏幕折叠状态进行模拟。具体请参考[使用工具栏](../harmonyos-guides/ide-emulator-toolbar.md)。
* 模拟器支持配置DNS。具体请参考[网络](../harmonyos-guides/ide-emulator-more-features.md#section206461549731)。
* AppAnalyzer支持使用远程真机进行云测试。具体请参考[支持的设备](../harmonyos-guides/ide-app-analyzer-overview.md#section15619122362919)。

**优化应用性能**

* Snapshot支持导入混淆及调试文件，还原文件名称和文件路径；Shortest Paths页签支持实时切换和展示用户选择的对象。具体请参考[Snapshot模板基本操作](../harmonyos-guides/ide-snapshot-basic-operations.md)。
* Allocation分析任务新增支持录制System Resources泳道，All Heap & Anonymous VM泳道中Record JS Stack默认开启。具体请参考[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。

**命令行工具**

* 模块级oh-package.json5新增oh-exports字段，通过该字段控制导出模块中文件，实现包的可见性控制。具体请参考[oh-package.json5](../harmonyos-guides/ide-oh-package-json5.md)。

## DevEco Studio 6.1.0 Beta1（6.1.0.609）兼容性配套关系

DevEco Studio 6.1.0.609携带的工具列表、支持的API范围及开发态版本号信息如下：

**表7** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS Emulator | 6.1.0.200 | 模拟器。 |
| Hvigor | 6.23.2 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1 | OpenHarmony三方库的包管理工具。 |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 6.1.0.609配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表8** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 6.1.0.609 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.23.2 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 6.1.1 | OpenHarmony三方库的包管理工具。 |
| Node.js | 18.20.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| modelVersion | 6.1.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 6.1.0(23) | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~6.1.0(23) | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

## DevEco Studio 6.1.0 Beta1（6.1.0.609）新增和增强特性

**开发环境搭建**

* DevEco Studio支持开发API 23工程。

**使用AI智能辅助编程**

* Inline Edit入口名称变更为Inline Chat。具体请参考[编辑区对话](../harmonyos-guides/ide-edit-area-code-generation.md)。
* 生成页面后，预览时支持切换亮色和暗色模式。具体请参考[页面生成](../harmonyos-guides/ide-page-generation.md)。
* CodeGenie增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄露次数分析等内存问题场景。具体请参考[智慧调优](../harmonyos-guides/ide-ai-profiler.md)。

**编写与调试应用**

* Code Linter新增通过命令行进行代码检查能力。具体请参考[规则变更说明](../harmonyos-guides/ide-codelinter-rules-change.md)。
* ArkTSDoc功能支持多模块导出，以及导出时支持设置不需要被导出的目录。具体请参考[文档生成](../harmonyos-guides/ide-arktsdoc-generation.md#section15845310446)。
* 模拟器支持热启动，即启动时加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。具体请参考[启动和关闭模拟器](../harmonyos-guides/ide-emulator-start-and-close.md)。
* 支持通过命令行创建、删除模拟器，查询、下载或删除模拟器镜像等。具体请参考[通过命令行使用模拟器](../harmonyos-guides/ide-emulator-command-line.md)。
* 新增WearableKid模拟器。具体请参考[设备支持类型](../harmonyos-guides/ide-emulator-devicetype.md)。
* ArkUI Inspector支持查看窗口交互事件，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。具体请参考[查看窗口交互事件](../harmonyos-guides/ide-arkui-inspector.md#section516993011576)。
* DevEco Studio支持对C++编译生成的无源码so文件进行二进制插桩，进而开启HWASan功能。具体请参考[使用HWASan检测内存错误](../harmonyos-guides/ide-hwasan.md)。
* 热重载支持import \*、动态import、lazy import、napi\_load\_module和napi\_load\_module\_with\_info。具体请参考[使用约束](../harmonyos-guides/ide-hot-reload.md#section995453874915)。
* AppAnalyzer新增上架合规体检，针对AppGallery应用的上架合规要求进行检测，提前发现需要重点关注的合规事项，了解应做和不应做的事项，避免常见误区。具体请参考[上架合规体检](../harmonyos-guides/ide-app-analyzer-ag-policy.md)。
* 场景化体检新增前台静置、运行异常场景。具体请参考[场景化体检](../harmonyos-guides/ide-app-analyzer-scenes.md)。

**构建应用**

* Hvigor支持可视化查看和执行任务。具体请参考[任务可视化与执行](../harmonyos-guides/ide-task-visualization.md)。
* 工程级build-profile.json5文件的packOptions下新增enableIncrementalSoCompress字段，用于构建HAP/HSP时，指定是否开启增量压缩，复用上一次构建已经压缩好的so，加快打包速度。具体请参考[工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md)。
* 模块级build-profile.json5文件的resOptions下新增qualifiersConfig字段，用于配置HAP/HSP模块的限定词目录，编译时会进行过滤，匹配到的限定词目录会被打包到产物中。具体请参考[模块级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)。

**优化应用性能**

* 支持进行无线调优。具体请参考[性能问题定界：实时监控](../harmonyos-guides/realtime-monitor.md)。
* Frame场景分析新增查看Session中Frame页面布局信息的开关。具体请参考[Frame分析](../harmonyos-guides/ide-insight-session-frame.md#section58691959194312)。
* Energy Anomaly泳道支持查看能耗异常信息和能耗异常原因。具体请参考[能耗诊断：Energy分析](../harmonyos-guides/ide-profiler-energy.md)。
* Allocation分析任务支持录制All Heap & Anonymous VM泳道，不支持录制Native Allocation泳道。具体请参考[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。

**命令行工具**

* ohpm命令支持查询三方库的版本更新信息。具体请参考[ohpmdependency-check](../harmonyos-guides/ide-ohpm-dependency-check.md)。
