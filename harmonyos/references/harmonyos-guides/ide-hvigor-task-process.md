---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-task-process
title: 构建任务说明
breadcrumb: 指南 > 构建应用 > 概述 > 构建任务说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ba323fae94a2e9a14bce92288d0e198c6f5b4628cb17a80e66b147e8beb60b8a
---

本章节将对构建的任务进行说明，可以更直观地了解到构建的任务流程。

## 任务流程图

### HAP基础任务流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/pW6GgFocTFueEP4eNFmiyg/zh-cn_image_0000002561832935.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=4CB55980E62D8C1BF7509CD9513DA23C6DA424F6D485F7985E7FFE4C5759EC3C)

### HSP基础任务流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/nbUPRGXHR9WtPTAZE2A_hg/zh-cn_image_0000002561752947.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=3BB606EF0B5BB50EFDCE5BCDB90D846344C707BD1C0DE56C4331987E255371CA)

### HAR基础任务流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/yxiNrPO8SM-nx26SqpVSaw/zh-cn_image_0000002530753016.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=2556E9A8EB4C7A06B7AF513F2520517F1632C65740CB3EFC5D13C92A3CB08601)

## 使用命令查看任务

在DevEco Studio中可以通过以下命令获得任务相关的信息。

```
1. hvigorw taskTree
```

获取任务树时会根据工程中的模块将模块中注册的任务以下图形式输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Q8pIMbpnRkqKFa2Yoi2NpQ/zh-cn_image_0000002530913002.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=9663CF17DBFC05F37A24AB906C82E698C2D2AA8107F8EF6AFB6B1291872CD200)

执行顺序举例说明：如图所示，assembleHap依赖CollectDebugSymbol，CollectDebugSymbol依赖于PackageHap；则任务执行顺序为PackageHap->CollectDebugSymbol->assembleHap。

## 任务详细说明

根据任务职能的不同主要分为以下几个类型的任务。

| 任务类别 | 任务说明 |
| --- | --- |
| Hook | hook任务 |
| ArkTS | ArkTS编译相关任务 |
| JS | JS编译相关任务 |
| Resources | 资源编译、处理、链接、合并相关的任务 |
| Package | 打包相关的任务 |
| Sign | 签名相关的任务 |
| Verification | 验证项目或者依赖项设置等相关的任务 |
| Generate | 生成和转换前置文件等相关的任务 |
| Config | 生成，合并，处理配置文件等相关的任务 |
| Native | Native编译等相关的任务 |
| Help | 查询hvigor帮助信息的相关任务 |
| Other | 未分类的任务 |

### Hook

* assembleHap 编译构建hap模块的Hook任务。
* assembleHsp 编译构建hsp模块的Hook任务。
* assembleHar 编译构建har模块的Hook任务。
* assembleApp 编译构建app模块的Hook任务。
* assembleDevHqf 支持增量部署的Hook任务。
* HotReloadBuild HotReloadArkTS前置Hook任务。
* PreviewBuild PreviewArkTS前置Hook任务。
* buildHotReloadResource 热加载资源相关前置Hook任务。
* PreviewHookCompileResource 预览时资源编译处理是否支持Restool增量方式编译的Hook任务。
* GenerateBuildProfile 生成BuildProfile.ets文件的Hook任务。
* BuildUnitTestHook 单元测试编译资源相关前置Hook任务。
* buildPreviewerResource 预览资源相关前置Hook任务。
* compileNative native资源相关前置Hook任务。
* UnitTestBuild UnitTestArkTS前置Hook任务。
* test 使用命令行执行Local Test的Hook任务。
* onDeviceTest 使用命令行执行Instrument Test的Hook任务。

### ArkTS

* CompileArkTS/BuildArkTS 通过rollup调用loader编译ArkTS源码。
* PreviewArkTS 预览模式下，通过rollup调用loader编译ArkTS源码。
* HotReloadArkTS 热加载场景下，通过rollup调用loader编译ArkTS源码。
* OhosTestCompileArkTS/OhosTestBuildArkTS ohos测试场景下，通过rollup调用loader编译ArkTS源码。
* HarCompileArkTS/HarBuildArkTS 构建HAR包场景下，通过rollup调用loader编译ArkTS源码。
* UnitTestArkTS 单元测试场景下，通过rollup调用loader编译ArkTS源码。

### JS

* CompileJS/BuildJS 调用loader编译js源码。
* OhosTestCompileJS/OhosTestBuildJS ohos测试场景下，调用loader编译js源码。

### Resources

* ProcessResource 处理和生成用文件方式编译资源的中间文件。
* PreviewProcessResource 预览场景下，处理和生成用文件方式编译资源的中间文件。
* CompileResource 调用restool 编译资源。
* PreviewCompileResource 预览场景下，调用restool编译资源。
* ProcessLibs 收集hap和har依赖中的.so文件。

### Package

* PackageHap 调用打包工具打hap包。
* PackageHar 调用打包工具打har包。
* PackageHsp 调用打包工具打hsp包。
* PackageApp 调用打包工具打app包。
* PackageHqf 调用打包工具打增量包。
* PackageSharedHar 调用打包工具打hsp模块的har包。
* PackageSharedTgz 调用打包工具将hsp模块生成的未签名hap和har包打包成tgz包。
* PackageSignHar 调用打包工具打带签名的har包，当前仅在daemon模式下生效。

### Sign

* SignHap 调用签名工具给hap包签名。
* SignHsp 调用签名工具给hsp包签名。
* SignApp 调用签名工具给app包签名。
* SignHqf 调用签名工具给增量包签名。
* SignModuleRemoteHsp 调用签名工具给模块级ohpm仓上的hsp包签名。
* SignProjectRemoteHsp 调用签名工具给工程级ohpm仓上的hsp包签名。

### Verification

* PreBuild 模块级预检查任务。
* PreBuildApp 工程级预检查任务。
* PreCheckSyscap syscap相关配置预检查任务。

### Generate

* GenerateLoaderJson 生成loader.json文件。
* GenerateMetadata 生成metadata.json文件。
* SyscapTransform syscap转换任务。
* MakePackInfo 生成模块级别的pack.info。
* MakeProjectPackInfo 生成工程级别的pack.info。
* ProcessPackageJson 对package.json文件进行处理。
* ProcessOHPackageJson 对oh\_package.json5文件进行处理。
* GeneratePackRes 生成pack.res文件。
* CreateBuildProfile 生成hap/hsp的BuildProfile.ets文件。
* CreateHarBuildProfile 生成har的BuildProfile.ets文件。
* PrepareQuickfix 通过校验获取增量文件并输出到quickfix.json文件中。

### Config

* ProcessProfile 处理module.json5文件。
* PrepareSharedHarResource 生成打包shared library的package.json和module.json。
* UnitTestProcessProfile UnitTestBuild场景处理构建中间产物module.json文件。
* MergeProfile 合并module.json5文件。
* PreviewUpdateAssets 预览模式下，Stage模型在编译预览代码前更新前置任务生成的module.json和main\_pages.json文件。

### Native

* BuildNativeWithNinja 将native代码编译成so文件。
* BuildNativeWithCmake 用CMake编译CPP源码。

### Help

* tasks 查看hvigor的全部任务及详情。
* taskTree 查看当前工程涉及的任务树。

### Other

* ReplaceUnitTestIndexFile 单元测试替换入口文件。
* ReplacePreviewerPage 接受预览器提供的参数替换页面文件中的参数。
* OhosTestCopyMockConfigJson 测试框架执行mock时将mock-config.json拷贝到测试包中。
* clean 清理生成的Build目录。
* collectCoverage 基于仪表打点数据生成覆盖率统计报表。

### Sync

* init 初始化工程。

### Init

该任务类型与Sync下的init不同，该过程中无具体任务，主要负责执行调用hvigor前的准备工作。
