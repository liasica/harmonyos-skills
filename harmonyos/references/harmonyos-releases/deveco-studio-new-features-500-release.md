---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features-500-release
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > DevEco Studio > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f8d4f38420072a629d0ea45dc749cd612f4b2134121225195575a84137921a69
---

## DevEco Studio 5.0.0 Release（5.0.3.910）兼容性配套关系

DevEco Studio 5.0.3.910携带的工具列表、支持的API范围及开发态版本号信息如下：

**表1** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| DevEco Studio | DevEco Studio 5.0.0 Release（5.0.3.910） | - |
| HarmonyOS SDK | HarmonyOS 5.0.0 Release | - |
| HarmonyOS Emulator | HarmonyOS 5.0.0 Release（5.0.3.805） | 模拟器，当前支持手机（包括折叠屏）、平板。 |
| hvigor | 5.8.9 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.8 | OpenHarmony三方库的包管理工具。 |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/服务兼容的最低版本。 |
| modelVersion | 5.0.0 | 开发态版本号。 |

DevEco Studio 5.0.3.910配套使用的命令行工具列表、支持的API范围及开发态版本号信息如下：

**表2** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 5.0.3.906 | 命令行工具集版本。 |
| codelinter | 5.0.8 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 5.8.9 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.8 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 5.0.0 Release | - |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/服务兼容的最低版本。 |
| modelVersion | 5.0.0 | 开发态版本号。 |

## DevEco Studio 5.0.0 Release（5.0.3.906）兼容性配套关系

**表3** DevEco Studio

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| DevEco Studio | DevEco Studio 5.0.0 Release（5.0.3.906） | - |
| HarmonyOS SDK | HarmonyOS 5.0.0 Release | - |
| HarmonyOS Emulator | HarmonyOS 5.0.0 Release（5.0.3.805） | 模拟器，当前支持手机（包括折叠屏）、平板。 |
| hvigor | 5.8.9 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.8 | OpenHarmony三方库的包管理工具。 |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/服务兼容的最低版本。 |
| modelVersion | 5.0.0 | 开发态版本号。 |

**表4** 命令行工具

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Command Line | 5.0.3.906 | 命令行工具集版本。 |
| codelinter | 5.0.8 | 执行代码检查与修复的工具。 |
| hstack | 5.1.0 | 将release应用混淆后的crash堆栈还原为源码对应堆栈的工具。 |
| hvigorw | 5.8.9 | 编译构建工具DevEco Hvigor（以下简称Hvigor），适用于API 10及以上的工程。 |
| ohpm | 5.0.8 | OpenHarmony三方库的包管理工具。 |
| sdk | HarmonyOS 5.0.0 Release | - |
| compatibleSdk | 最低兼容版本：4.0.0(10) | HarmonyOS应用/服务兼容的最低版本。 |
| modelVersion | 5.0.0 | 开发态版本号。 |

## DevEco Studio 5.0.0 Release（5.0.3.910）新增和增强特性

无新增和增强特性。

## DevEco Studio 5.0.0 Release（5.0.3.906）新增和增强特性

### 新增特性

* ohpm-repo新增use\_reverse\_proxy字段用于配置是否使用反向代理选项。具体请参考[配置项说明](../harmonyos-guides-V5/ide-ohpm-repo-configuration-V5.md#zh-cn_topic_0000001745376470_配置项说明)。
* DevEco Studio提供Generate ArkTSDoc功能，将代码文件中变量、方法、接口、类等需要对外暴露的信息快速生成相应的参考文档。具体请参考[生成ArkTSDoc文档](../harmonyos-guides-V5/ide-arktsdoc-V5.md)。
* hvigor-config.json5文件新增ohos.nativeResolver字段，用于指定ArkTS编译过程中是否使用高性能插件进行依赖寻址，使用高性能插件可以降低编译过程的峰值内存，加快编译速度。具体可参考[hvigor-config.json5](../harmonyos-guides-V5/ide-hvigor-set-options-V5.md)。
* hvigor新增获取远程hsp路径的API：getOhpmRemoteHspDependencyInfo。具体请参考[插件上下文](../harmonyos-guides-V5/ide-build-expanding-context-V5.md)。
* 应用与服务体检新增1条快速性能检测规则和2条最佳实践规则。具体请参考[评分方法及规则](../harmonyos-guides-V5/ide-app-analyzer-V5.md#section7155192511196)。
* 模拟器支持selinux。

* DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程；并提供一体化的历史工程迁移能力，帮助开发者快速完成工程转换。具体请参考[一体化工程迁移](../harmonyos-guides-V5/ide-integrated-project-migration-V5.md)。
* 使用ArkTS语言开发时，代码编辑新增支持Refactor-Convert能力。支持将字面量类型转换为映射类型等高频转换操作，辅助开发者高效重构代码。具体请参考[代码重构](../harmonyos-guides-V5/ide-code-refactoring-V5.md)。
* 端云一体化工程支持创建、开发、调试、部署、调用云对象。具体请参考[开发云对象](../harmonyos-guides-V5/agc-harmonyos-clouddev-cloudobj-V5.md)。
* 编译构建支持通过Build Analyzer工具可视化分析排查构建过程中的性能问题。具体请参考[分析构建性能](../harmonyos-guides-V5/ide-hvigor-build-analyzer-V5.md)。
* Stage模型的ArkTS工程支持代码混淆。具体请参考[代码混淆](../harmonyos-guides-V5/ide-build-obfuscation-V5.md)。
* 支持开发者自定义Hvigor任务和插件。具体请参考[扩展构建](../harmonyos-guides-V5/ide-build-expanding-V5.md)。
* 提供hvigor生命周期的hook，便于开发者使用hook在生命周期中按需进行逻辑处理。具体可供开发者使用的hook请参考[构建生命周期](../harmonyos-guides-V5/ide-hvigor-life-cycle-V5.md)。
* 新增运行时获取编译构建参数的功能。具体请参考[获取自定义编译参数](../harmonyos-guides-V5/ide-hvigor-get-build-profile-para-V5.md)。
* 支持使用ArkUI Inspector分析布局，开发者可以在DevEco Studio上查看应用在真机上的UI显示效果。具体请参考[布局分析](../harmonyos-guides-V5/ide-arkui-inspector-V5.md)。
* 支持使用Device File Explorer访问设备文件，开发者可以在DevEco Studio上对设备文件进行上传、下载等操作。具体请参考使用[查看设备文件](../harmonyos-guides-V5/ide-device-file-explorer-V5.md)。
* 故障分析新增TSan检测和方舟多线程检测。具体可参考[TSan检测](../harmonyos-guides-V5/ide-tsan-V5.md)和[方舟多线程检测](../harmonyos-guides-V5/ide-multi-thread-check-V5.md)。
* 新增hstack工具，可用于将release应用混淆后的crash堆栈还原为源码对应堆栈。具体可参考[hstack](../harmonyos-guides-V5/ide-command-line-hstack-V5.md)。
* 预览器新增Mock数据模拟功能，开发者可以在预览场景中根据实际需要模拟UI组件上的属性或方法，或模拟import的模块methods，增强预览场景下的预览体验。具体请参考[预览数据模拟](../harmonyos-guides-V5/ide-previewer-mock-V5.md)。
* 预览支持轻量化模拟，开发者能够使用预览器进行调试。具体请参考[调试概述](../harmonyos-guides-V5/ide-debug-device-V5.md)。
* 预览启动时新增执行PreviewChecker，检测通过后才可进行预览。具体可参考[PreviewChecker检测规则](../harmonyos-guides-V5/ide-previewer-previewchecker-V5.md)。
* DevEco Profiler性能调优工具提供实时监控能力和场景化调优模板，便于全方位的设备资源监测，采集数据覆盖多个维度，支持ArkUI、组件耗时、并行化、卡顿丢帧、内存资源占用以及函数执行效率等相关的问题优化，为开发者带来高效、直通代码行的调优体验。具体请参考[DevEco Profiler性能调优工具](../harmonyos-guides-V5/ide-insight-description-V5.md)。
* Windows和macOS(ARM)版本模拟器新增支持手机（包括折叠屏）和平板。具体可参考[概述](../harmonyos-guides-V5/ide-emulator-overview-V5.md)。
* 模拟器新增支持网络代理和摇一摇。具体可参考[网络代理](../harmonyos-guides-V5/ide-emulator-more-features-V5.md#section206461549731)和[摇一摇](../harmonyos-guides-V5/ide-emulator-more-features-V5.md#section1241612419541)。
* 支持拖动多个HAP、HSP包到模拟器窗口安装。具体可参考[安装应用程序包和上传文件](../harmonyos-guides-V5/ide-emulator-install-upload-V5.md)。
* 提供全新的应用与服务体检（AppAnalyzer），用于测试并评价HarmonyOS应用/服务的质量，便于开发者对HarmonyOS应用/服务进行自测试。具体请参考[应用与服务体检](../harmonyos-guides-V5/ide-app-analyzer-V5.md)。
* 新增支持通过命令行方式执行测试用例并获取测试报告。具体请参考[使用命令行执行测试](../harmonyos-guides-V5/ide-instrument-test-V5.md#section14255191913322)。
* 测试框架新增本地单元测试(Local Test)，不需要设备或模拟器即可进行测试。具体请参考[Local Test](../harmonyos-guides-V5/ide-local-test-V5.md)。
* ohpm新增依赖版本冲突自动解决功能。具体请参考[resolve\_conflict](../harmonyos-guides-V5/ide-ohpmrc-V5.md)。
* ohpm-repo支持自定义存储插件。具体请参考[自定义存储插件](../harmonyos-guides-V5/ide-ohpm-repo-storageplugin-V5.md)。
* ohpm-repo支持多实例部署，能够提高服务的高可用性、负载均衡能力和系统的可伸缩性，具体请参考[多实例部署](../harmonyos-guides-V5/ide-ohpm-deploy-multiple-instances-V5.md)。
* ohpm-repo支持接口防重放攻击机制，防止请求被恶意重放。具体请参考[前台页面](../harmonyos-guides-V5/ide-ohpm-web-front-page-V5.md)。

* DevEco Studio支持创建API 12的LiteWearable工程。
* 新增支持对崩溃问题进行定位以及对崩溃，卡顿，丢帧，能耗等异常进行数据分析。具体请参考[运维服务](../harmonyos-guides-V5/ide-operation-and-services-V5.md)。
* DevEco Profiler ArkWeb模板支持分析web页面加载问题和web页面渲染丢帧问题。具体请参考[ArkWeb分析](../harmonyos-guides-V5/ide-profiler-arkweb-V5.md)。
* HAR模块build-profile.json5中buildOption/arkOptions下新增byteCodeHar字段，用于指定是否支持字节码HAR。具体请参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 工程级build-profile.json5中buildOption/strictMode下新增harLocalDependencyCheck字段，用于指定是否对HAR产物启用本地依赖校验。具体请参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 新增支持设备录屏功能。具体请参考[录屏](../harmonyos-guides-V5/ide-screen-recording-V5.md)。
* 预览器新增一条PreviewChecker检测规则：不支持调用未定义Mock的HSP。具体请参考[PreviewChecker检测规则](../harmonyos-guides-V5/ide-previewer-previewchecker-V5.md#section1161812252913)。
* 应用与服务体检新增部分最佳实践体检规则，性能Benchmark套餐新增包含部分兼容性规则，支持导出html体检报告。具体请参考[应用与服务体检](../harmonyos-guides-V5/ide-app-analyzer-V5.md#section1012195444613)。
* API12的云开发工程模板支持元服务。具体请参考[创建元服务工程](../harmonyos-guides-V5/agc-harmonyos-create-faproject-V5.md)。
* DevEco Profiler新增Network模板。具体请参考[网络诊断：Network分析](../harmonyos-guides-V5/ide-profiler-network-V5.md)。
* 新增方舟native模块加载异常信息增强功能。具体请参考[方舟native模块加载异常信息增强](../harmonyos-guides-V5/ide-multi-thread-check-V5.md#section12424161546)。
* ArkTS调试新增支持extension调试。具体请参考[extension调试](../harmonyos-guides-V5/ide-debug-arkts-extension-V5.md)。
* ArkTS调试新增支持worker/taskpool调试。具体请参考[worker/taskpool调试](../harmonyos-guides-V5/ide-debug-arkts-worker-taskpool-V5.md)。
* 新增支持多进程调试。具体请参考[多进程调试](../harmonyos-guides-V5/ide-debug-multi-process-V5.md)。
* ArkTS调试支持在代码执行到断点时打印开发者指定的表达式。具体请参考[Evaluate and log](../harmonyos-guides-V5/ide-debug-arkts-evaluate-log-V5.md)。
* ArkTS调试支持smart step into函数。具体请参考[smart step into](../harmonyos-guides-V5/ide-debug-arkts-smart-step-into-V5.md)。
* ArkTS调试新增支持反向调试。具体请参考[反向调试](../harmonyos-guides-V5/ide-debug-arkts-reverse-V5.md)。
* hvigor-config.json5新增以下字段。具体可参考[hvigor-config.json5](../harmonyos-guides-V5/ide-hvigor-set-options-V5.md)。
  + properties下新增ohos.fallback.target字段，当找不到指定target时，如果模块中存在该fallback target，则使用fallback target进行构建。
  + properties下新增hvigor.memoryThreshold字段，当编译构建占用内存超过此阈值时，新加入的编译任务会等待，直到正在进行的编译任务结束，新的编译任务才能开始。
* 模块级build-profile.json5新增librariesInfo字段，用于声明so的透传依赖信息。具体可参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 工程级和模块级build-profile.json5新增compression字段，用于对图片资源进行纹理压缩。具体请参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 工程级build-profile.json5新增compatibleSdkVersionStage字段，用于控制不同版本的兼容。具体可参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 支持在无网络环境下搭建流水线。具体请参考[无网络流水线搭建](../harmonyos-guides-V5/ide-no-network-V5.md#section15767113454814)。
* ARM版本模拟器预置应用新增浏览器。
* 新增支持本地计算机复制的文本在模拟器内粘贴。具体请参考[操控屏幕](../harmonyos-guides-V5/ide-emulator-control-screen-V5.md)。
* 应用与服务体检新增3条快速性能检测规则。具体请参考[评分方法及规则](../harmonyos-guides-V5/ide-app-analyzer-V5.md#section7155192511196)。
* 应用与服务体检支持查看历史体检报告。具体请参考[查看历史报告](../harmonyos-guides-V5/ide-app-analyzer-V5.md#section52734271806)。
* ohpm-repo支持配置匿名访问。具体请参考[系统设置](../harmonyos-guides-V5/ide-ohpm-system-settings-V5.md)。
* hvigor-config.json5中properties下新增hvigor.keepDependency字段，用于指定是否保持hsp模块的所有依赖。具体可参考[hvigor-config.json5](../harmonyos-guides-V5/ide-hvigor-set-options-V5.md)。
* 本地单元测试新增支持mock能力。具体请参考[mock能力](../harmonyos-guides-V5/ide-test-mock-V5.md)。
* 应用与服务体检新增1条快速性能体检规则。具体请参考[评分方法及规则](../harmonyos-guides-V5/ide-app-analyzer-V5.md#section7155192511196)。

### 变更特性

工程级build-profile.json5文件的compatibleSdkVersionStage字段新增枚举值：beta5、beta6、release。具体可参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。

* Refactor-Convert代码转换功能操作由点击编辑器界面灯泡图标在下拉菜单中选择转换类型，变更为右键单击Refactor > Convert选择转换的方式。具体请参考[Refactor-Convert代码转换](../harmonyos-guides-V5/ide-code-refactoring-V5.md#section760818259244)。
* Code Linter部分规则所属规则集或告警等级变更；@performance/hp-arkui-wrap-waterflow-if-else-footer规则下线。具体请参考[规则变更说明](../harmonyos-guides-V5/ide-codelinter-rules-change-V5.md)。
* @security/specified-interface-call-chain-check新增对命名空间namespace、类型别名type、接口interface、枚举enum和结构体struct的支持。具体请参考[@security/specified-interface-call-chain-check](../harmonyos-guides-V5/ide-specified-interface-call-chain-check-V5.md)。
* 已上架应用市场的应用不支持录制ArkTS Callstack、Callstack、Native Allocation、ArkTS Allocation、ArkTS Snapshot、ArkUI Component、ArkUI State泳道。
* HAR包的打包流程新增ProcessHarArtifacts任务。具体请参考[HAR基础任务流程图](../harmonyos-guides-V5/ide-hvigor-task-process-V5.md#section988883610112)。
* DevEco Studio信息中心下线常见问题FAQ功能。如需查看常见问题解决方案，具体请参考[DevEco Studio FAQ](../harmonyos-faqs-V5/faqs-deveco-studio-V5.md)。

* API 11 Stage模型及以上，创建元服务工程或在元服务工程中创建模块时，不再默认创建服务卡片和EntryCard。开发者创建卡片时可任意选择卡片尺寸。
* 新建工程界面以及模板市场下架About Ability、Account、Business Card Ability、Category Ability、Category List Ability、Grid Ability、List Ability、Login Ability、Map Ability、Splash Screen Ability十个工程模板。
* API 12模板依赖的云开发SDK变更为Cloud Foundation Kit，开发者无需再显式引入云开发SDK作为依赖。具体请参考[端云一体化开发](../harmonyos-guides-V5/agc-harmonyos-clouddev-view-V5.md)。
* 仪器测试目录简化，屏蔽与测试开发无关的文件。具体请参考[自定义Ability和Resources](../harmonyos-guides-V5/ide-instrument-test-V5.md#section760061533)。
* DevEco Studio不再支持低代码开发。
* 下架部分与HarmonyOS开发无关的插件。下架插件包含：Package Search、JetBrains maven model api classes、JetBrains Repository Search、JUnit、TestNG、Java、Java Bytecode Decompiler、Java IDE Customization、Java Internationalization、Java Stream Debugger、Groovy。
* Code Linter变更或下架部分规则。具体请参考[规则变更说明](../harmonyos-guides-V5/ide-codelinter-rules-change-V5.md)。
* 工程级build-profile.json5中buildModeSet下的name字段的test模式支持自定义，仅在执行ohosTest测试套件时使用。具体请参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 优化变量高亮操作，由双击修改为单击即可查看变量引用位置等。
* cpp构建的缓存目录增加一层当前buildMode的文件夹，目录结构由.cxx/default/default/arm64-v8a改为.cxx/default/default/debug/arm64-v8a或.cxx/default/default/release/arm64-v8a。
* parameterFile中key值支持的字符与包名的要求一致。具体请参考[parameterFile](../harmonyos-guides-V5/ide-oh-package-json5-V5.md#section122411462820)。
* 应用与服务体检联动Profiler进行性能问题分析时无需手动导入数据，点击profiler文件可直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析。具体请参考[应用与服务体检](../harmonyos-guides-V5/ide-app-analyzer-V5.md)。
* 模块级build-profile.json5文件中的代码混淆开关enable字段默认值由true改为false。具体请参考[代码混淆](../harmonyos-guides-V5/ide-build-obfuscation-V5.md)。
* DevEco Studio下架Intelligent Coding Assistant插件。
* 在进行native调试时，开发者可以同时设置数据断点的最大数量由4个变为2个。

### 增强特性

* ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO权限支持通过自动签名申请。具体请参考[支持ACL权限](../harmonyos-guides-V5/ide-signing-V5.md#section9786111152213)。
* DevEco Profiler中CPU分析统计信息增加。具体请参考[CPU活动分析：CPU分析](../harmonyos-guides-V5/ide-insight-session-cpu-V5.md)。
* UI Generator功能支持快速生成可编译、可运行的HarmonyOS UI工程。具体请参考[UI Generator](../harmonyos-guides-V5/ide-ui-generator-V5.md)。
* DevEco Studio全量页面支持Sync同步。
* Codelinter支持配置预览、安全、性能、一次开发多端部署、ArkTS代码风格规则检查。具体请参考[代码Code Linter检查](../harmonyos-guides-V5/ide-code-linter-V5.md)。
* 编辑器支持通过Quick Fix实现快速修复能力。具体请参考[代码Quick Fix快速修复](../harmonyos-guides-V5/ide-realtime-check-V5.md)。
* 支持区分工程级与模块级oh-package.json5配置。具体请参考[oh-package.json5](../harmonyos-guides-V5/ide-oh-package-json5-V5.md)。
* oh-package.json5支持parameterFile参数化配置文件路径。具体请参考[oh-package.json5文件](../harmonyos-guides-V5/ide-oh-package-json5-V5.md) 。
* HAR支持多目标产物构建。具体请参考[定义HAR多目标构建产物](../harmonyos-guides-V5/ide-customized-multi-targets-and-products-guides-V5.md#section173102213445)。
* Native调试支持堆栈可视化、so信息可视化、Smart Step Into等功能。具体可参考[Native代码调试](../harmonyos-guides-V5/ide-debug-native-V5.md)。
* 模拟器的GPS硬件模拟能力增强，提供场景化数据注入能力。具体可参考[GPS定位](../harmonyos-guides-V5/ide-emulator-more-features-V5.md#section81566471211)。
* 优化了Debug模式下编译构建产物中的调测信息。
* ArkTS代码格式化能力新增句末分号补全。
* Find Usages查找结果支持过滤变量赋值和变量引用位置。具体请参考[代码引用查找](../harmonyos-guides-V5/ide-editer-overview-V5.md#section16665161301116)。
* Code Linter新增安全、性能及风格规范类代码规则。具体请参考[规则变更说明](../harmonyos-guides-V5/ide-codelinter-rules-change-V5.md)。
* DevEco Profiler heapsnapshot文件导入功能支持导入泄漏文件列表，展示泄漏的ArkTS实例。具体请参考[Heap Snapshot离线导入](../harmonyos-guides-V5/ide-snapshot-basic-operations-V5.md#section6760173514388)。
* DevEco Profiler 支持perfdata、sys类型trace数据数据文件导入。具体请参考[会话区](../harmonyos-guides-V5/ide-profiler-session-V5.md)。
* 工程级build-profile.json5中modules的srcPath字段新增支持引用工程外模块。具体请参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 工程级和模块级build-profile.json5中headerPath和arguments字段均支持配置数组。具体请参考[build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md)。
* 编辑器支持查看类和接口的Type Hierarchy层次结构。具体请参考[代码阅读](../harmonyos-guides-V5/ide-editer-overview-V5.md)。
* 创建端云一体化开发工程时从DevEco Studio拉起AGC页面创建HarmonyOS应用的体验优化，具体请参考[创建HarmonyOS应用工程](../harmonyos-guides-V5/agc-harmonyos-create-appproject-V5.md)。
* 构建完成后Build Analyzer会提供一些构建性能优化的建议，开发者可根据界面提示进行设置。
* ohpm-repo支持根据正则表达式导出匹配的包列表。具体请参考[ohpm-repo export\_pkginfo](../harmonyos-guides-V5/ide-ohpm-repo-export-pkginfo-V5.md)。
* ohpm-repo自定义存储插件save接口增加HAR包的name、version数据。具体请参考[自定义存储插件配置](../harmonyos-guides-V5/ide-ohpm-repo-plugin-configuration-V5.md)。
