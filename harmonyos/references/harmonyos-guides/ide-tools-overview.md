---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview
title: 工具概述
breadcrumb: 指南 > 开发环境搭建 > 工具概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:32+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:b80ea8a6bdee6d28f47e414ec0e12e4eb52a720d80139dbdc19dd2513e1ee002
---

## HarmonyOS应用/元服务开发

### DevEco Studio集成开发环境

HUAWEI DevEco Studio（获取工具请单击[链接下载](https://developer.huawei.com/consumer/cn/download/deveco-studio)，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用/元服务。

* [CodeGenie AI辅助编程](ide-codegenie.md)：提供HarmonyOS应用开发智能知识问答、代码生成&补全、万能卡片生成、UI界面生成等能力。
* 智能代码编辑：[代码编辑](ide-code-edit.md)功能为ArkTS、JS和C/C++编程语言提供代码智能补全、代码重构等能力，帮助你高效编码。
* 多端双向实时预览：[界面预览](ide-previewer-01.md)功能帮助你在UI编码时快速预览界面在多种设备上的显示效果，查看组件布局，提升UI开发效率。
* [Hvigor](ide-hvigor.md)轻量级构建工具：支持源码、资源、构建流程的自定义，可以灵活构建差异化的多目标产物。提供Build Analyzer帮助分析构建性能，提升构建效率。
* [跨语言调试](ide-debug-device.md)：支持ArkTS&C++语言调试、汇编调试、lldb命令调试、反向调试、智能跳转和数据断点等丰富调试能力。
* [Profiler应用调优](ide-insight-description.md)：支持分析多种场景应用性能问题，包括内存泄漏、组件耗时、网络请求、应用启动、界面卡顿等。提供可视化泳道图帮助优化HarmonyOS应用性能。
* [AppAnalyzer应用与元服务体检](ide-app-analyzer.md)：使用体检工具在开发阶段发现可能影响上架的兼容性、性能、功耗、稳定性等问题，并支持场景化检测，提升应用基础体验及上架成功率。
* [本地模拟器](ide-run-emulator.md)：提供手机（包括折叠屏）、平板、PC/2in1等类型的模拟器，可以帮助你在各种HarmonyOS设备上调测应用，以更好地适配不同的机型和HarmonyOS版本。
* 依赖管理：ohpm是DevEco Studio默认的包管理工具，可以使用ohpm安装、更新、删除和管理HAR、HSP或模块之间的依赖关系，帮助开发者简化了代码的共享、分发和依赖管理。同时，提供[ohpm-repo](ide-ohpm-repo.md)工具帮助开发者搭建轻量级的HarmonyOS三方库私有仓服务。它与ohpm兼容，用来存储和管理您独有的三方库，保证这些三方库的私有性的同时，便于这些三方库能在开发团队内部共享复用，从而提升团队的开发效率。

### 开发流程

开发一个应用/元服务流程如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/M5TBJ0w3Sq2CLGat-Iv_YA/zh-cn_image_0000002561753617.png?HW-CC-KV=V1&HW-CC-Date=20260429T054419Z&HW-CC-Expire=86400&HW-CC-Sign=E5E8D02E5B68AE23883EFF016B2D8F5D3A3038A4D30A25BAE0B9E71FC171F39B)

**一、开发准备**

获取HUAWEI DevEco Studio请单击[链接下载](https://developer.huawei.com/consumer/cn/download/)，完成开发工具的安装。

DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。在部分企业网络受限的情况下，需要[配置代理](ide-environment-config.md)信息。

**二、开发应用/元服务**

DevEco Studio集成了Phone、Tablet、2in1、Car等设备的典型场景模板，可以通过工程向导轻松地[创建一个新的工程](ide-create-new-project.md)。

接下来还需要定义应用/元服务的UI、开发业务功能等编码工作，可以根据[应用开发导读](application-dev-guide.md)来查看具体的开发过程，通过查看[API接口文档](../harmonyos-references/development-intro-api.md)查阅需要调用的API接口。

在开发代码的过程中，可以[使用预览器查看应用/元服务效果](ide-previewer-01.md)，支持实时预览、动态预览、双向预览等功能，使编码的过程更高效。

**三、运行、调试和测试应用/元服务**

应用/元服务开发完成后，可以[使用真机进行调试](ide-debug-device.md)（需要申请调测证书进行签名），支持单步调试、跨语言调试等调试手段，使得应用/元服务调试更加高效。

HarmonyOS应用/元服务开发完成后，在发布到应用/元服务市场前，还需要[对应用进行测试](ide-test.md)，主要包含Instrument Test、Local Test，确保HarmonyOS应用/元服务纯净、安全，给用户带来更好的使用体验。

**四、发布应用/元服务**

HarmonyOS应用/元服务开发、测试完成后，需要[将应用/元服务发布至应用市场](ide-publish-app.md#section6406135115814)，以便应用市场对应用/元服务进行分发，普通消费者可以通过应用市场获取到对应的HarmonyOS应用/元服务。需要注意的是，发布到华为应用市场的HarmonyOS应用/元服务，必须使用应用市场颁发的发布证书进行签名。

## 命令行开发

针对流水线或命令行开发场景，推荐使用Command Line Tools[命令行工具](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)，其中集合了HarmonyOS应用开发所用到的系列工具，包括代码检查工具codelinter、三方包管理工具ohpm、堆栈解析工具hstack、命令行构建工具hvigorw。

* [代码检查工具codelinter](ide-command-line-codelinter.md)：对代码进行检查与快速修复，可将codelinter工具集成到门禁或持续集成环境中。
* [三方包管理工具ohpm](ide-ohpm-cli.md)：作为OpenHarmony三方库的包管理工具，支持OpenHarmony共享包的发布、安装和依赖管理。
* [堆栈解析工具hstack](ide-command-line-hstack.md)：用于将Release应用混淆后的crash堆栈还原为源码对应堆栈。
* [命令行构建工具hvigorw](ide-hvigor-commandline.md)：作为Hvigor的wrapper包装工具，支持自动安装Hvigor构建工具和相关插件依赖，以及执行Hvigor构建命令。

## 约束与限制

以下功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）：

1. Partner SDK功能
2. Template Market模板市场
3. Sample导入功能
4. 端云一体化工程创建及开发
5. 软件包及符号表上传功能
6. Collect Logs and Diagnostic Data日志回传功能
7. Operation Analyzer运维服务
8. AppAnalyzer应用与元服务体检
9. AI辅助编程工具DevEco CodeGenie
10. OHPM Index OpenHarmony开源中心仓

## 文档声明

HUAWEI DevEco Studio使用指南配套DevEco Studio[最新版本](https://developer.huawei.com/consumer/cn/download/)。如使用DevEco Studio其它版本，可能存在文档与产品功能界面、操作不一致的情况，请以实际功能界面为准。
