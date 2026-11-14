---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features-2601
title: 新增和增强特性
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > DevEco Studio（Windows/macOS版） > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-11-14T08:45:43+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:6fd26c16b310c685b1b251572d0c5d490ce7f21e885e90b58161ba052f2c5e75
---

当前为DevEco Studio最新版本说明文档，如需查看DevEco Studio其它历史版本的功能新增、变更情况，请在左侧文档目录中选择相应版本。

使用Beta版本的DevEco Studio开发的应用无法上架应用市场，仅可用于本地开发调测。如有应用上架的诉求，请使用Release版本进行开发。

## DevEco Studio 26.0.1 Beta1（26.0.1.290）

### 兼容性配套关系

DevEco Studio 26.0.1.290携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS SDK 26.0.1 Beta1 | - |
| HarmonyOS Emulator | 26.0.1.100 | 模拟器。 |
| Hvigor | 6.26.20 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.1.220 | OpenHarmony三方库的包管理工具。 |
| Node.js | 24.14.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 26.0.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.1 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.1 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 26.0.1.290配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 26.0.1.290 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 6.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.26.20 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.1.220 | OpenHarmony三方库的包管理工具。 |
| HarmonyOS Emulator | 26.0.1.100 | 模拟器。 |
| Node.js | 24.14.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS SDK 26.0.1 Beta1 | - |
| modelVersion | 26.0.1 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.1 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.1 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

**开发环境搭建**

* 支持开发API 26.0.1工程。
* 支持批量导入和批量移除基于CMake工程构建生成的so库。具体请参考[批量导入和批量移除so库](../doccenter-deveco-studio/ide-import-so.md)。

**编写与调试应用**

* Code Linter新增代码检查规则。具体请参考[规则变更说明](../doccenter-deveco-studio/ide-codelinter-rules-change.md)。
* string资源可视化编辑时支持同时选择多个资源、复制和粘贴资源、批量删除资源。具体请参考[string资源可视化编辑](../doccenter-deveco-studio/ide-string-editor.md)。
* 签名信息变更如下。具体请参考[配置调试签名](../doccenter-deveco-studio/ide-signing.md)。
  + 新增的签名配置信息默认会存放至工程目录下的.sign/sign-config.json5文件中，build-profile.json5中原有的签名信息仍生效。
  + 签名方案名称（${default}）下会显示签名信息所在文件为build-profile.json5或sign-config.json5。
  + 若sign-config.json5和build-profile.json5存在同名签名方案时，sign-config.json5优先级高于build-profile.json5。

* 三折叠品类下新增Mate XT2模拟器。
* Phone模拟器支持HiCar投屏能力，通过多屏界面，可模拟手机接入车机后的开发场景，支撑应用适配HiCar模式。具体请参考[使用HiCar能力](../doccenter-deveco-studio/ide-emulator-more-features.md#section14503123943914)。
* 模拟器支持通过共享内存对外输出画面帧数据，为远程服务器开发、自动化测试、画面采集与转码等场景提供实时画面获取能力。具体请参考[获取模拟器实时画面数据](../doccenter-deveco-studio/ide-emulator-video.md)。
* DevEco Studio支持将Lite Wearable应用推包到支持双模式的Wearable设备上运行。具体请参考[使用Wearable设备运行Lite Wearable应用](../doccenter-deveco-studio/ide-run-device.md#section10175654102616)。
* 支持关闭ArkTS反向调试功能。具体请参考[反向调试](../doccenter-deveco-studio/ide-debug-arkts-reverse.md)。
* 使用命令行执行仪器测试时，支持指定设备进行测试。具体请参考[使用命令行执行测试](../doccenter-deveco-studio/ide-instrument-test.md#section14255191913322)。

**优化应用性能**

* ArkTS Snapshot泳道新增特性如下。具体请参考[Snapshot模板基本操作](../doccenter-deveco-studio/ide-snapshot-basic-operations.md)。
  + Statistics区域可查看构造器下的所有实例到GC Roots的最短路径，或者切换方向查看GC Roots到构造器下所有实例的最短路径。
  + Statistics区域支持按不同聚类规则展示更多种类的构造器或对象。
  + Comparison区域新增Retained Size Delta(Allocate/Free)列，用于分析持有内存的大小增量。
* Allocation模板中泳道的新增特性如下。具体请参考[内存分析介绍](../doccenter-deveco-studio/ide-insight-session-allocations-memory.md)。
  + FilePage Other、.so、.ttf、.hap类型的Memory子泳道中的Details区域新增Path列，用于显示各采样点PSS占比最大的文件路径。
  + Native Leaks泳道录制时，支持开启设置中的Statistics Mode（统计模式）。
  + 录制ArkTS Heap泳道数据前，需要勾选设置项中的Record Data Range Options开关。

**命令行工具**

* Command Line Tools集成codescanner工具，用于检查整个项目的资源泄漏问题。开发者可根据扫描结果中的告警提示，手动修复代码缺陷，在代码开发阶段，确保代码质量。具体请参考[跨语言代码检查工具（codescanner）](../doccenter-deveco-studio/ide-command-line-codescanner.md)。
* Command Line Tools集成api-compat工具，支持查询和对比从某个选定的SDK版本开始，当前工程、模块或文件中使用的API接口是否存在行为变更，帮助开发者完成兼容性检查和代码适配修改。具体请参考[API变更查询工具（api-compat）](../doccenter-deveco-studio/ide-command-line-apicompat.md)。
* Command Line Tools集成appanalyzer工具，用于对应用和元服务进行本地测试体检，并给出体检报告、分析指导以及修改建议，帮助开发者提升应用与元服务质量。具体请参考[应用与元服务体检工具（appanalyzer）](../doccenter-deveco-studio/ide-commandline-appanalyzer.md)。
* ohpm publish命令后面配置--readme <p>参数，指定发包时使用的README.md文件路径。具体请参考[ohpm publish](../doccenter-deveco-studio/ide-ohpm-publish.md)。
