---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-task-process
title: 构建任务说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 概述 > 构建任务说明
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:56+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:9c6cc8519555a55e8b5c364857ebae3e25aa92dfbcba4066a727f12c1e763982
---

本章节将对构建的任务进行说明，可以更直观地了解到构建的任务流程。

## 任务流程图

### HAP基础任务流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Jz556R9WSLG8WHcxSHpr6g/zh-cn_image_0000002792001002.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F5D75E7356A943436682DC511ADB446221C0AF924A546CC1E16248DD927DA13)

### HSP基础任务流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/VXhfhkkQRX6-xfHZYtPo_g/zh-cn_image_0000002820720971.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=C22B807AA4F07B73B2FB0E78F93C5F8F038401FB946CE08DDCA4C67963D32513)

### HAR基础任务流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Zu19qJzbSGufS5TgZvsocw/zh-cn_image_0000002820720973.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD40F3B1E113DCE2C891A3BA47843C09A98597D34F68ACFE2D717672ADF0C38F "点击放大")

## 使用命令查看任务

在DevEco Studio中可以通过以下命令获得任务相关的信息。

```screen
hvigorw taskTree
```

获取任务树时会根据工程中的模块，将模块中注册的任务以下图形式输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/eLQwtuLKSEi3rMPE29dWOg/zh-cn_image_0000002792001006.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=56FF4E21568CBEE5837384D0860C2653893C84F04D9054ECB583EE7E60B894A5 "点击放大")

执行顺序举例说明：如图所示，assembleHap依赖SignHap，SignHap依赖于PackageHap；则任务执行顺序则为PackageHap->SignHap->assembleHap。

## 任务详细说明

根据任务职能的不同，主要分为以下几种类型任务。

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
* CompileResource 调用restool编译资源。
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
