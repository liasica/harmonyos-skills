---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features-2600
title: 新增和增强特性
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > DevEco Studio > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8bb9400eb703cd41c2cafdf50b6c3c4a826aaeba21cd3c67664f23b5f8fccc56
---

当前为DevEco Studio最新版本说明文档，如需查看DevEco Studio其它历史版本的功能新增、变更情况，请在左侧文档目录中选择相应版本。

## DevEco Studio 26.0.0 Release（26.0.0.821）

### 兼容性配套关系

DevEco Studio 26.0.0.821携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 26.0.0 Release SDK | - |
| HarmonyOS Emulator | 26.0.0.400 | 模拟器。 |
| Hvigor | 6.26.4 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.0.630 | OpenHarmony三方库的包管理工具。 |
| Node.js | 24.14.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 26.0.0.821配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 26.0.0.821 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 6.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.26.4 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.0.630 | OpenHarmony三方库的包管理工具。 |
| HarmonyOS Emulator | 26.0.0.400 | 模拟器。 |
| Node.js | 24.14.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 26.0.0 Release SDK | - |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

**开发环境搭建**

* 创建工程时，Compatible SDK默认显示设备量累计占比超过90%的最高API版本，以及新增View API version distribution按钮，点击可查看HarmonyOS设备各API版本使用量占比。具体请参考[创建一个新的工程](../harmonyos-guides/ide-create-new-project.md)。

**编写与调试应用**

* 支持查看更多的ArkUI组件状态变量绑定关系。具体请参考[代码阅读](../harmonyos-guides/ide-editer-overview.md#section2541105019101)。
* 针对跨模块移动文件场景优化了移动符号的导入方式，移入、移出模块时lndex会适配改动。具体请参考[代码重构](../harmonyos-guides/ide-code-refactoring.md#section634374493316)。
* 模拟器支持外接USB摄像头。对于缺少摄像头的场景，模拟器提供虚拟相机功能，用于模拟拍照流程。具体请参考[摄像头](../harmonyos-guides/ide-emulator-more-features.md#section11725194916439)。
* 模拟器支持断网模拟。具体请参考[断网模拟](../harmonyos-guides/ide-emulator-access-network.md#section115741355151910)。
* 模拟器支持通过命令行获取UI布局信息、点击、滑动屏幕和输入文本。具体请参考[通过命令行使用模拟器](../harmonyos-guides/ide-emulator-command-line.md#section830618485420)。
* 穿戴模拟器支持在表冠区域使用鼠标滚轮模拟表冠旋转。具体请参考[表冠](../harmonyos-guides/ide-emulator-more-features.md#section772115543124)。
* DevEco Studio支持位置模拟能力，帮助开发者调试和测试与地理位置相关的应用功能。具体请参考[位置模拟](../harmonyos-guides/ide-mock-location.md)。
* 数据库调试能力增强，支持执行多条SQL，支持选中单条或者多条SQL后执行。具体请参考[数据库调试](../harmonyos-guides/ide-database-inspector.md)。
* DevEco Studio支持解析应用的coredump文件，帮助开发者快速定位问题。具体请参考[解析应用minidump/coredump文件](../harmonyos-guides/ide-analyze-dump.md)。
* HWASan检测支持解析错误堆栈对应的伪代码、方法入参及变量的名称、值。具体请参考[使用HWASan](../harmonyos-guides/ide-hwasan.md#section1080616409587)。
* 仪器/本地/黑盒覆盖率测试支持统计增量代码覆盖率。具体请参考[使用命令行执行仪器测试](../harmonyos-guides/ide-instrument-test.md#section14255191913322)、[使用命令行执行本地测试](../harmonyos-guides/ide-local-test.md#section1722814418378)、[黑盒覆盖率测试](../harmonyos-guides/ide-ui-test.md#section2863134631313)。
* AppAnalyzer支持导入AppGallery上架审核不通过的功耗、性能报告进行诊断分析，帮助定位可能的故障原因并生成体检报告。具体请参考[导入上架检测报告进行诊断](../harmonyos-guides/ide-release-check-report.md)。
* 回传DevEco Studio日志信息时，支持填写问题描述和上传图片/视频文件。具体请参考[日志收集和诊断数据](../harmonyos-guides/ide-log-postback.md)。

**构建应用**

* 工程级build-profile.json5文件的packOptions下新增deduplicateSo字段，用于指定构建APP时，是否去除HAP和HSP中重复的so文件，以减小APP包体积。具体请参考[工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md)。
* 支持将字节码HAR及其所有依赖合并打包，生成一个无外部依赖、可直接使用的独立HAR包。具体请参考[多HAR合并打包](../harmonyos-guides/ide-hvigor-build-har.md#section121297571296)。
* 支持按照target、product和buildMode维度个性化配置依赖，构建多目标产物。具体请参考[使用插件配置多目标依赖](../harmonyos-guides/ide-customized-multi-targets-and-products-guides.md#section8222113911814)。

**优化应用性能**

* ArkTS Snapshot泳道新增如下能力，具体请参考[Snapshot模板基本操作](../harmonyos-guides/ide-snapshot-basic-operations.md)。
  + 支持一键获取节点支配树。通过展示从GC Roots到目标实例在支配树上的支配链，可直接定位到内存泄漏的支配者。断开路径上的支配者即可释放关联内存，从而更精准、高效地解决内存泄漏问题。
  + 支持将shortest Paths页签中的数据导出到本地进行保存。
  + ArkTS堆快照最短路径支持查看混淆前的源码路径，以及支持跳转至工程中的代码位置，方便开发者快速调试。
  + ArkTS Snapshot泳道的Statistics区域支持按不同聚类规则展示构造器或对象。
  + ArkTS Snapshot泳道的Statistics区域支持通过对象id精确定位目标对象。
  + 支持单独导入一个或多个.jsleaklist文件，同时工具会自动导入匹配的.rawheap文件；支持导入一个或多个.rawheap文件后，工具自动导入匹配的.jsleaklist文件。
* Allocation模板新增如下能力，具体请参考[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。
  + 新增Native Leaks泳道，用于标记内存泄漏点。
  + ArkTS Snapshot泳道支持解析内存对象。
  + 支持将Allocation分配栈数据导出到本地进行保存。
  + 无论是否开启统计模式，录制ArkTS Snapshot泳道，框选All Heap & Anonymous VM/All Heap/Native Heap子泳道，单击任一行栈帧，More区域都会显示经过该栈帧的分配内存最大的调用栈和ArkTS对象列表（ArkTS Object List）。
  + 新增Collect Only Unreleased Memory Events配置项，用于控制在录制阶段是否保留已释放内存的调用栈数据。
* 新增FileSystem模板，可以结合应用逻辑IO和物理IO的读写耗时、整机（设备上所有应用）逻辑IO和物理IO的读写耗时等情况，定位IO耗时问题。具体请参考[IO耗时：FileSystem分析](../harmonyos-guides/ide-profiler-filesystem.md)。
* app.json5配置文件中profileable设置为true的release应用支持展示Callstack调用栈。具体请参考[基础耗时：Time分析](../harmonyos-guides/ide-insight-session-time.md)。

**命令行工具**

* hstack工具支持指定文件进行堆栈解析。具体请参考[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)。
* ohpmrc配置文件新增symlink\_for\_local\_dep配置项。执行ohpm install过程中，可以对本地HAR依赖解压后的路径创建软链接。具体请参考[ohpmrc](../harmonyos-guides/ide-ohpmrc.md)。
* 在ohpm命令中，参数类型为Boolean且默认值为true的命令，支持配置--no参数，包括--no-strict\_ssl、--no-resolve\_conflict、--no-install\_all、--no-experimental-concurrently-safe。具体请参考[常用命令](../harmonyos-guides/ide-ohpm-common-commands.md)。
* 新增arktsdoc工具，支持通过命令行将代码文件中的变量、方法、接口、类等需要对外暴露的信息快速生成相应的参考文档。具体请参考[ArkTSDoc文档生成工具（arktsdoc）](../harmonyos-guides/ide-command-line-arktsdoc.md)。

## DevEco Studio 26.0.0 Beta2（26.0.0.621）

### 兼容性配套关系

DevEco Studio 26.0.0.621携带的工具列表、支持的API范围及开发态版本号信息如下：

**表3** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 26.0.0 Beta2 SDK | - |
| HarmonyOS Emulator | 26.0.0.300 | 模拟器。 |
| Hvigor | 6.26.2 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.0.410 | OpenHarmony三方库的包管理工具。 |
| Node.js | 24.14.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 26.0.0.621配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表4** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 26.0.0.621 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 6.0.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.26.2 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.0.410 | OpenHarmony三方库的包管理工具。 |
| HarmonyOS Emulator | 26.0.0.300 | 模拟器。 |
| Node.js | 24.14.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 26.0.0 Beta2 SDK | - |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

**开发环境搭建**

* 支持在API 26.0.0及以上工程的模块中添加Agent和AgentUI，分别用于提供智能体扩展的能力和接入端侧Agent UI界面显示的能力。具体请参考[添加Ability](../harmonyos-guides/ide-add-new-ability.md)。

**编写与调试应用**

* Codelinter新增兼容性规则。具体请参考[规则变更说明](../harmonyos-guides/ide-codelinter-rules-change.md)。
* DevEco Studio支持调试Native子进程。具体请参考[调试Native子进程](../harmonyos-guides/ide-debug-native-child-process.md)。
* coverage-filter.json5文件的include和exclude字段支持通配符过滤文件/文件夹。具体请参考[配置覆盖率过滤文件](../harmonyos-guides/ide-ui-test.md#section13756446154)。
* coverage-filter.json5文件新增两个字段。具体请参考[配置覆盖率过滤文件](../harmonyos-guides/ide-ui-test.md#section13756446154)。
  + 新增includeHar字段，用于配置参与覆盖率测试的远程源码har包。
  + 新增extraAbilities字段，用于配置ability路径生成黑盒覆盖率数据。

**构建应用**

* hvigor-config.json5文件的properties下新增hvigor.daemon.idleTimeout字段，用于设置daemon进程的最大空闲时长，从最后一次构建任务完成时开始计算，超过最大空闲时长则daemon进程退出。具体请参考[hvigor-config.json5文件](../harmonyos-guides/ide-hvigor-set-options.md)。
* 工程级build-profile.json5文件的strictMode下新增disableStrictCheckPaths字段，用于指定不需要严格检查的三方库目录名称。具体请参考[工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md)。
* Hvigor新增接口getOhpmDependencyInfoV2和getOhpmRemoteHspDependencyInfoV2接口，用于替代原有接口getOhpmDependencyInfo和getOhpmRemoteHspDependencyInfo。具体请参考[插件上下文](../harmonyos-guides/ide-build-expanding-context.md)。

**优化应用性能**

* 新增GlobalHandleObject常见对象，位于（handle）标签中，用于记录napi\_ref地址，并建立napi\_ref和ArkTS对象的引用关系。具体请参考[案例：ArkTS内存泄漏分析](../harmonyos-guides/ide-arkts-memory-leak-analysis.md#section135057191135)。

## DevEco Studio 26.0.0 Beta1（26.0.0.461）

### 兼容性配套关系

DevEco Studio 26.0.0.461携带的工具列表、支持的API范围及开发态版本号信息如下：

**表5** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| HarmonyOS SDK | HarmonyOS 26.0.0 Beta1 SDK | - |
| HarmonyOS Emulator | 26.0.0.200 | 模拟器。 |
| Hvigor | 6.26.1 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.0.410 | OpenHarmony三方库的包管理工具。 |
| Node.js | 24.14.1 | Hvigor、ohpm等工具的运行时环境。 |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

DevEco Studio 26.0.0.461配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表6** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 26.0.0.461 | 命令行工具集版本。 |
| codelinter | 6.0.240 | 执行代码检查与修复的工具。 |
| hstack | 6.0.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 6.26.1 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 26.0.0.410 | OpenHarmony三方库的包管理工具。 |
| HarmonyOS Emulator | 26.0.0.200 | 模拟器。 |
| Node.js | 24.14.1 | codelinter、hvigorw、hstack、ohpm等工具的运行时环境。 |
| sdk | HarmonyOS 26.0.0 Beta1 SDK | - |
| modelVersion | 26.0.0 | 开发态版本号。 |
| [compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 最低兼容版本：4.0.0(10) | 标识应用/元服务运行所需兼容的最低SDK版本。 |
| [compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 26.0.0 | 标识编译应用/元服务所使用的SDK版本。 |
| [targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619) | 4.0.0(10)~26.0.0 | 标识应用/元服务运行所需目标SDK版本，介于compatibleSdkVersion和compileSdkVersion之间。 |

### 新增和增强特性

**使用AI智能辅助编程**

* 使用自定义Agent和HarmonyOS Act智能体时，支持展示当前会话token的使用量。
* 选择HarmonyOS Act智能体进行对话、代码生成、代码修改等操作后，将鼠标悬浮在对话框的时间点会弹出Back to This Moment，点击可回退对话。
* 工程问答支持调用MCP Market工具，调用LSP（Language Server Protocol，语言服务器协议）工具，以及ArkTS和C++代码语义检索能力。具体请参考[工程问答](../harmonyos-guides/ide-project-ask.md)。
* 编辑区对话Inline Chat支持内置模型使用快捷指令，如File Comments和Parameter Validation，进行代码文件分析和参数校验等。具体请参考[编辑区对话](../harmonyos-guides/ide-edit-area-code-generation.md)。
* 自定义智能体（Agent）新增UI Verification的内置工具。具体请参考[自定义智能体（Agent）配置和调用](../harmonyos-guides/ide-agent-use.md)。
* 支持创建自定义指令，该功能允许开发者将常用的提示词和工作流封装为可复用的命令，提升日常开发效率。具体请参考[自定义指令（Commands）配置](../harmonyos-guides/ide-commands.md)。

**编写与调试应用**

* 支持开发API 26.0.0工程。
* DevEco Studio提供加载/卸载模块（Load/Unload Modules）的功能，开发者可以按照需求加载模块，从而降低对内存资源占用和提升代码索引效率。具体请参考[卸载和加载模块](../harmonyos-guides/ide-load-unload-modules.md)。
* 编辑器支持状态变量关系查看。具体请参考[查看ArkUI组件状态变量关系](../harmonyos-guides/ide-editer-overview.md#section2541105019101)。
* Codelinter新增正确性规则。具体请参考[规则变更说明](../harmonyos-guides/ide-codelinter-rules-change.md)。
* 新增Code Scanner工具，支持检查整个项目的资源泄漏问题。具体请参考[Code Scanner代码检查](../harmonyos-guides/ide-code-scanner.md)。
* 支持通过自定义的Clang-Tidy对C/C++代码进行静态检查。具体请参考[Clang-Tidy代码检查](../harmonyos-guides/ide-clang-tidy.md)。
* 关联注册应用的调试签名新增部分开放能力，以及支持在DevEco Studio申请ACL权限。具体请参考[配置调试签名](../harmonyos-guides/ide-signing-auto.md#section6333421192714)。
* DevEco Studio支持同时预览应用在8个典型档位断点下的UI效果。具体请参考[多断点预览](../harmonyos-guides/ide-previewer-arkui.md#section384317711155)。
* 新增Car设备模拟器，Car设备模拟器支持多屏能力。具体请参考[Car设备多屏能力](../harmonyos-guides/ide-emulator-more-features.md#section5710121118389)。
* 模拟器命令行支持场景化模拟。具体请参考[场景化模拟](../harmonyos-guides/ide-emulator-command-line.md#section4653134015354)。
* Native调试支持启动加速，首次调试完成时，调试服务器会保持活跃状态，后续再次启动调试时，可以大幅减少调试连接的耗时。具体请参考[Native调试启动加速](../harmonyos-guides/ide-lldb-client-alive.md)。
* 支持将设备投屏到DevEco Studio中使用。具体请参考[设备投屏](../harmonyos-guides/ide-screen-mirroring.md)。
* 数据库调试能力增强，支持SQL语法高亮和关键词、表字段的自动联想补全，支持可视化修改表格中的数据。具体请参考[数据库调试](../harmonyos-guides/ide-database-inspector.md)。
* DevEco Studio支持对应用崩溃生成的minidump文件进行解析，并展示异常堆栈，帮助开发者快速分析定位问题。具体请参考[解析应用minidump文件](../harmonyos-guides/ide-analyze-dump.md)。
* 支持根据日志标签过滤HiLog日志。具体请参考[按日志标签过滤日志](../harmonyos-guides/ide-setup-hilog.md#section87721353233)。
* AppAnalyzer支持导入AppGallery上架审核不通过的UX专项报告并进行诊断分析，获得可能的故障原因并生成体检报告。具体请参考[导入上架检测报告进行诊断](../harmonyos-guides/ide-release-check-report.md)。
* 新增支持对内存溢出、应用冻屏、资源泄漏问题进行定位。具体请参考[运维服务](../harmonyos-guides/ide-operation-and-services.md)。

**构建应用**

* 工程级build-profile.json5文件的strictMode下新增apiCompatibilityCheck字段，用于设置ArkTS API兼容性检测级别。具体请参考[工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md)。
* 工程级build-profile.json5文件的tscConfig下新增tsImportSoCheck字段，用于指定编译时是否对.ts文件中导入.so文件内的符号进行类型解析。具体请参考[工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md)。
* HAP/HSP模块级build-profile.json5文件的nativeLib下新增enableSoDirCollection字段，用于指定ets文件中是否能够加载libs/{ABI}/子目录下的so文件。具体请参考[配置CPP](../harmonyos-guides/ide-hvigor-cpp.md)。
* DevEco Studio的Settings界面新增一个开关，用于提升sync阶段C++编译效率。具体请参考[通过syncNative提升sync阶段C++编译效率](../harmonyos-guides/ide-hvigor-experimental-properties.md#section16637112213911)。
* Hvigor新增getAllDependencyInfo接口，用于获取工程或模块下所有的依赖信息。具体请参考[getAllDependencyInfo（工程）](../harmonyos-guides/ide-build-expanding-context.md#section11559101173916)和[getAllDependencyInfo（模块）](../harmonyos-guides/ide-build-expanding-context.md#section136597864911)。

**优化应用性能**

* Memory泳道新增ArkWeb PA和JS Heap子泳道，分别用于显示Malloc内存分配和ArkWeb Render进程JS堆内存占用。具体请参考[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。
* Memory泳道新增Statistics页签，用于统计虚拟内存区域数量的最小值、虚拟内存区域数量的最大值、虚拟内存区域数量的平均值、PSS内存最小值、PSS内存最大值、PSS内存平均值等。具体请参考[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。

**发布应用**

* 上传软件包支持对应用包进行发布重签名，无需开发者从AGC手动下载证书和Profile，即可在DevEco Studio中完成重签名流程。具体请参考[发布应用](../harmonyos-guides/ide-publish-app.md)。

**命令行工具**

* Linux平台支持使用模拟器。具体请参考[模拟器工具（Emulator）](../harmonyos-guides/ide-commandline-emulator.md)。
* ohpmrc文件新增auto\_skip\_install配置项，作用为若依赖未发生变化时，自动跳过本次安装。具体请参考[ohpmrc](../harmonyos-guides/ide-ohpmrc.md)。
* ohpmrc文件新增metadata\_cache\_effective和metadata\_cache配置项，分别用于设置元数据缓存的过期时间和开启读取缓存的元数据文件。具体请参考[ohpmrc](../harmonyos-guides/ide-ohpmrc.md)。
