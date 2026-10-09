---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-tools-overview
title: 工具概述
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工具概述
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:27+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:973008f9dc92e69fd2bec2451527b1f30cb10e0bd52a5d2a79b43ca889b9c325
---

## DevEco Studio集成开发环境

华为鸿蒙电脑HUAWEI DevEco Studio（以下简称鸿蒙电脑DevEco Studio或DevEco Studio）是基于毕方技术平台构建的HarmonyOS应用集成开发环境，提供代码编辑、编译构建、代码调试、性能调优、多设备预览等能力，并集成Al Agent工具，帮助你高效开发HarmonyOS应用。

* [代码编辑](ide-hmos-code-edit.md)：为ArkTS、JS和C/C++编程语言提供代码智能补全、代码重构等能力，帮助开发者高效编码。
* [Hvigor](ide-hmos-hvigor.md)轻量级构建工具：支持源码、资源、构建流程的自定义，可以灵活构建差异化的多目标产物。提供Build Analyzer帮助分析构建性能，提升构建效率。
* [代码调试](ide-hmos-debug-app.md)：支持ArkTS&C++语言调试、汇编调试、lldb命令调试、智能跳转和数据断点等丰富的调试能力。
* [多设备预览](ide-hmos-previewer-overview.md)：提供手机（包括折叠屏）、平板等类型的多设备预览器，帮助开发者在多种HarmonyOS设备上调试应用，查看组件布局，提升开发效率。
* [Profiler应用调优](ide-hmos-insight-description.md)：支持分析多种场景应用性能问题，包括内存泄漏、界面卡顿等。提供可视化泳道图帮助优化HarmonyOS应用性能。
* 依赖管理：ohpm是DevEco Studio默认的包管理工具，可以使用ohpm安装、更新、删除和管理HAR、HSP或模块之间的依赖关系，帮助开发者简化了代码的共享、分发和依赖管理。
* Al Agent：集成[DevEco Code](ide-deveco-code-overview.md)工具，覆盖代码生成、问题修复、编译构建、功能验证等开发旅程，通过自然语言快速开发HarmonyOS应用。

## 命令行开发

针对流水线或命令行开发场景，推荐使用[命令行工具](ide-hmos-commandline-get.md)，其中集合了HarmonyOS应用开发所用到的系列工具，包括代码检查工具codelinter、三方包管理工具ohpm、命令行构建工具hvigorw。

* [代码检查工具codelinter](ide-hmos-command-line-codelinter.md)：对代码进行检查与快速修复，可将codelinter工具集成到门禁或持续集成环境中。
* [三方包管理工具ohpm](ide-hmos-ohpm-cli.md)：作为OpenHarmony三方库的包管理工具，支持OpenHarmony共享包的发布、安装和依赖管理。
* [命令行构建工具hvigorw](ide-hmos-hvigor-commandline.md)：作为Hvigor的wrapper包装工具，支持自动安装Hvigor构建工具和相关插件依赖，以及执行Hvigor构建命令。

## 工具能力差异

和Windows/macOS版DevEco Studio相比，鸿蒙电脑DevEco Studio仅支持HarmonyOS应用开发，支持Phone、Tablet、PC/2in1设备，其他差异参见下表。

| 分类 | 能力 | 说明 |
| --- | --- | --- |
| 工程管理 | 工程结构视图 | 暂不支持Ohos视图 |
| 签名 | 调试自动签名暂不支持在DevEco Studio上开通开放能力和添加ACL权限 |
| 代码编辑 | 代码阅读 | 暂不支持代码结构视图 |
| 跨语言代码编辑 | 暂不支持生成胶水代码 |
| 预览器/模拟器 | / | 使用多设备预览器进行预览和调试 |
| 编译构建 | 编译任务管理 | 暂不支持构建任务可视化及执行 |
| 应用调试 | 代码调试 | ArkTS语言暂不支持等待调试、反向调试、状态变量调试 |
| 暂不支持Native子进程调试 |
| 暂不支持跨语言调试 |
| 增量调试能力合并到Hot Reload |
| 暂不支持数据库调试 |
| 布局分析 | ArkUI 界面检查器暂不支持切换3D视图 |
| ArkUI 界面检查器暂不支持查看窗口交互事件 |
| 日志与故障分析 | 暂不支持堆栈跟踪分析、dump文件分析、App Killed日志查看 |
| 设备管理 | 设备投屏可以使用多屏协同能力 |
| 暂不支持无线连接设备 |
| 性能调优 | 性能问题分析 | 暂不支持User Events用户交互事件 |
| 暂不支持Lost Frames泳道数据展示 |
| 资源泄漏问题分析 | 暂不支持ArkTS Callstack泳道数据展示 |
| 暂不支持ArkTS Allocation泳道数据展示 |
| 暂不支持All Heap & Anonymous VM泳道数据展示 |
| 暂不支持All Heap泳道数据展示 |
| 暂不支持All Anonymous VM泳道数据展示 |
| 暂不支持System Resources泳道数据展示 |
| 暂不支持Graphic Memory泳道数据展示 |
| 暂不支持Native Leaks泳道数据展示 |
| 数据实时监控 | 暂不支持温度、整机电流、最大电流、能耗、网络流量监控 |
| 开发自测试 | ArkTS单元测试 | 暂不支持本地单元测试 |
| 应用体检 | 暂不支持 |
| 发起云端测试 | 暂不支持 |
| 上传软件包 | / | 暂不支持 |
| API变更助手 | / | 暂不支持 |

## 文档声明

HUAWEI DevEco Studio使用指南配套DevEco Studio最新版本。如使用DevEco Studio其它版本，可能存在文档与产品功能界面、操作不一致的情况，请以实际功能界面为准。
