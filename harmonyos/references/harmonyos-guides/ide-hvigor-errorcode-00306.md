---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00306
title: 规格错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > 规格错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f62e6cb58b60e4597a04a4b0746c0445693736c32194c24b0db79def8a25a33d
---

## 00306001 文件路径长度超过最大限制

**错误信息**

The length of path exceeds the maximum length: XXX.

**错误描述**

文件路径长度超过最大限制。

**可能原因**

文件路径总长度超过了操作系统的限制。

**处理步骤**

1. 缩短工程根路径。
2. 简化工程名称。
3. 简化模块名称。
4. 简化target名称。

## 00306002 工程路径不能包含中文字符

**错误信息**

The Node directory and node name cannot contain Chinese characters.

**错误描述**

工程路径不能包含中文字符。

**可能原因**

工程路径存在中文字符。

**处理步骤**

移除工程路径中的中文字符。

## 00306003 工程路径无效

**错误信息**

Invalid project path. Current path does not match: XXX.

**错误描述**

工程路径无效。

**可能原因**

工程路径存在中文或特殊字符。

**处理步骤**

修改工程路径，确保路径只包含字母、数字、连字符-、下划线\_、点号.、英文括号()、空格或@符号。

## 00306004 不支持的API版本

**错误信息**

The compatibleSDKVersion XXX cannot be smaller than YYY declared in library ZZZ或

The project's compatibleSdkVersion: XXX cannot be lower than the minimum compatible version YYY required by the dependencies: ZZZ.

**错误描述**

当前项目的compatibleSdkVersion版本号不能小于三方库ZZZ的最低兼容版本YYY。

**可能原因**

项目的compatibleSdkVersion版本小于三方库中打包时声明的compatibleSdkVersion版本（最低兼容版本）。

**处理步骤**

采用以下任意一种方式：

* 尝试更新当前项目的compatibleSdkVersion版本，使其大于或等于三方库中声明的版本。
* 降低三方库的compatibleSdkVersion，在打包前修改工程级build-profile.json5中的compatibleSdkVersion，使其兼容更低版本。
* 移除与项目的compatibleSdkVersion版本不兼容的三方库，或者使用版本更低的三方库。

## 00306005 output名称重复

**错误信息**

Failed to build the app due to duplicate customized output names: XXX. At file: XXX.

**错误描述**

自定义的output名称重复，导致构建应用失败。

**可能原因**

模块的target配置中，自定义的output名称重复。

**处理步骤**

检查模块级build-profile.json5文件的targets配置，确保每个output名称都是唯一的。

## 00306006 API 12及以上支持TargetESVersion

**错误信息**

Unsupported API version. TargetESVersion is supported after API 12. At file: XXX.

**错误描述**

TargetESVersion在API 12及以上版本中支持，当前项目的API版本低于此要求。

**可能原因**

当前项目的compileSdkVersion或compatibleSdkVersion低于API 12。

**处理步骤**

检查工程级build-profile.json5文件中的compileSdkVersion和compatibleSdkVersion配置，确保其版本为API 12或以上。

## 00306007 意图框架工程的runtimeOS只能配置为HarmonyOS

**错误信息**

The runtimeOS that supports the insightintent project can only be HarmonyOS. At file: XXX.

**错误描述**

意图框架工程的runtimeOS只能配置为HarmonyOS。

**可能原因**

意图框架工程的runtimeOS没有配置为HarmonyOS。

**处理步骤**

检查工程级或模块级build-profile.json5文件，确保runtimeOS设置为HarmonyOS。

## 00306008 API 版本不支持意图框架

**错误信息**

Unsupported API version. Insight intent is supported after API 11. At file: XXX.

**错误描述**

API 11及以上工程支持意图框架。

**可能原因**

当前项目的compileSdkVersion或compatibleSdkVersion低于API 11。

**处理步骤**

检查工程级build-profile.json5文件中的compileSdkVersion和compatibleSdkVersion配置，确保其版本为API 11或以上。

## 00306009 SDK版本不支持意图框架

**错误信息**

Unsupported SDK version. Insight intent is supported after API 11. At file: XXX.

**错误描述**

API 11及以上工程支持意图框架。

**可能原因**

当前使用的SDK版本低于API 11。

**处理步骤**

在官网上下载新版本的[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00306010 SDK版本不支持ArkData

**错误信息**

The current SDK version does not support ArkData. At file: XXX.

**错误描述**

当前SDK版本不支持ArkData功能。

**可能原因**

当前使用的SDK版本不支持ArkData功能。

**处理步骤**

在官网上下载新版本的[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00306011 SDK版本不支持UI语法

**错误信息**

The current SDK version does not support uiSyntax. At file: XXX.

**错误描述**

当前SDK版本不支持UI语法。

**可能原因**

当前使用的SDK版本不支持UI语法。

**处理步骤**

在官网上下载新版本的[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00306012 不支持动态导入

**错误信息**

Invalid configuration of runtimeOnly in XXX. At file: XXX.

**错误描述**

runtimeOnly配置无效，不支持动态导入。

**可能原因**

仅API 11及以上的Stage模型工程支持配置runtimeOnly。

**处理步骤**

1. 确保工程级build-profile.json5中的compatibleSdkVersion版本为11或以上。
2. 确保模块级build-profile.json5中的apiType为stageMode。

## 00306013 Stage模型的OpenHarmony工程不支持元服务开发

**错误信息**

Atomic service development is not supported for OpenHarmony stage model. At file: XXX

**错误描述**

Stage模型的OpenHarmony工程不支持元服务开发。

**可能原因**

元服务工程的runtimeOS配置为OpenHarmony。

**处理步骤**

如需开发元服务，请将工程级build-profile.json5中的runtimeOS改为HarmonyOS。

## 00306014 API版本不支持元服务开发

**错误信息**

Atomic service development is not supported for compileSdkVersion/compatibleSdkVersion less than api 11. At file: XXX.

**错误描述**

compileSdkVersion或compatibleSdkVersion低于API 11时不支持元服务开发。

**可能原因**

当前工程的compileSdkVersion或compatibleSdkVersion低于API 11，不支持元服务开发。

**处理步骤**

检查工程级build-profile.json5文件的compileSdkVersion和compatibleSdkVersion配置，确保其版本为API 11或以上。

## 00306015 元服务不支持Native开发

**错误信息**

Atomic service development does not support Native development. At file: XXX.

**错误描述**

元服务不支持Native开发。

**可能原因**

当前工程XXX文件中包含了与Native开发相关的选项：externalNativeOptions。

**处理步骤**

确保元服务工程中不包含externalNativeOptions。

## 00306016 元服务开发仅支持ArkTS

**错误信息**

Atomic service development only supported arkTS widget. At file: XXX.

**错误描述**

元服务开发仅支持ArkTS组件。

**可能原因**

工程中使用了JS组件。

**处理步骤**

从工程中移除与JS组件相关的代码和配置。

## 00306017 API版本不支持集成态HSP

**错误信息**

The integratedHsp can only be used in API 12 and later. At file: XXX.

**错误描述**

API 12及以上版本支持使用集成态HSP。

**可能原因**

当前工程的compileSdkVersion或compatibleSdkVersion低于API 12。

**处理步骤**

检查工程级build-profile.json5的compileSdkVersion和compatibleSdkVersion配置，确保版本为API 12或以上。

## 00306018 使用集成态HSP需要将useNormalizedOHMUrl设置为true

**错误信息**

The integratedHsp is available only when useNormalizedOHMUrl is set to true. At file: XXX.

**错误描述**

使用集成态HSP需要将useNormalizedOHMUrl设置为true。

**可能原因**

useNormalizedOHMUrl设置为false。

**处理步骤**

检查工程级build-profile.json5的useNormalizedOHMUrl配置，确保设置为true。

## 00306019 仅字节码HAR支持配置bundledDependencies

**错误信息**

Only the byte code har supports to configure the bundledDependencies. At file: XXX.

**错误描述**

仅字节码HAR支持配置bundledDependencies。

**可能原因**

1. 工程级build-profile.json5的buildOption.strictMode下未配置useNormalizedOHMUrl，或者该属性值设置为false。
2. 在模块级build-profile.json5文件中，buildOption.arkOptions.byteCodeHar设置为false。

**处理步骤**

1. 确保工程级build-profile.json5的buildOption.strictMode包含useNormalizedOHMUrl属性，并将其设置为true。
2. 确保模块级build-profile.json5文件中，buildOption.arkOptions.byteCodeHar设置为true。

## 00306026 LiteWearable穿戴类型只支持JS开发

**错误信息**

Lite wearable only support JS.

**错误描述**

LiteWearable穿戴类型只支持JS开发。

**可能原因**

在LiteWearable穿戴类型的项目中存在TS文件。

**处理步骤**

确保项目中只包含JS文件。

## 00306027 依赖模块不支持设备类型

**错误信息**

The XXX module YYY that the current module depends on does not support the device type: ZZZ, which may cause runtime exception on the device.

**错误描述**

当前模块依赖的YYY模块不支持设备类型ZZZ，可能会导致运行时异常。

**可能原因**

依赖模块的module.json中缺少该设备类型。

**处理步骤**

更新依赖模块，选择支持该设备类型的模块作为依赖。

## 00306030 transformLib不是相对路径

**错误信息**

Invalid transformLib, its value should be a relative path.

**错误描述**

无效的transformLib，该值应该是相对路径。

**可能原因**

配置的transformLib不是相对路径。

**处理步骤**

确保transformLib是相对路径。

## 00306034 buildRoot参数无效

**错误信息**

Invalid buildRoot value XXX.

**错误描述**

buildRoot参数无效。

**可能原因**

执行hvigorw命令时，指定的buildRoot参数..开头。

**处理步骤**

确保buildRoot参数对应的目录在当前模块下，即不允许以..开头。

## 00306035 未知的abiFilter

**错误信息**

Unknown abiFilter XXX.

**错误描述**

未知的abiFilter配置XXX。

**可能原因**

配置的abiFilter不在支持的列表中或者拼写错误。

**处理步骤**

检查工程级或模块级build-profile.json5文件，确保abiFilters只包含以下值：arm64-v8a、x86\_64。

## 00306036 ohosTest不支持作为构建HSP/HAR的target

**错误信息**

Hvigor task 'XXX' not supported for building an 'ohosTest' target 'YYY'.

**错误描述**

构建HSP/HAR时，不支持选择ohosTest作为target。

**可能原因**

通过命令行构建HSP/HAR时，选择ohosTest作为target。

**处理步骤**

* 选择其他target构建HAR/HSP。
* 构建HAP模块时支持使用ohosTest作为target。

## 00306038 Stage模型的模块不允许依赖FA模型的模块

**错误信息**

Stage model module XXX does not allow Harmony library packages or modules in FA model. Build tasks will not be executed, and resources will not be packed.

**错误描述**

XXX为Stage模型模块，不能依赖FA模型的Harmony库或模块，否则会导致构建任务无法执行，资源无法打包。

**可能原因**

Stage模型的模块依赖了FA模型的库或模块。

**处理步骤**

检查XXX的依赖关系，确保没有引用FA模型的Harmony库或模块。

## 00306039 HSP不能依赖本模块

**错误信息**

Shared Library cannot depend on shared module self in module XXX at file: YYY.

**错误描述**

在XXX模块中，HSP（共享库）不能依赖本模块。

**可能原因**

HSP模块依赖了自身。

**处理步骤**

移除HSP的自身依赖。

## 00306040 FA模型模块不允许依赖非源码OpenHarmony npm包

**错误信息**

FA module XXX does not allow OpenHarmony npm packages, which artifactType is not original. Check at file: YYY.

**错误描述**

FA模型模块不允许依赖非源码OpenHarmony npm包。

**可能原因**

XXX模块依赖的OpenHarmony npm包是字节码或混淆的源码。

**处理步骤**

移除XXX模块对非源码OpenHarmony npm包的依赖。

## 00306041 FA模型的模块不允许依赖Stage模型的模块

**错误信息**

FA model module XXX does not allow Harmony library packages or modules in Stage model. Build tasks will not be executed, and resources will not be packed. Check at file: YYY.

**错误描述**

XXX为FA模型模块，不能依赖Stage模型的Harmony库或模块，否则会导致构建任务无法执行，资源无法打包。

**可能原因**

FA模型的模块依赖了Stage模型的库或模块。

**处理步骤**

检查XXX的依赖关系，确保没有引用Stage模型的Harmony库或模块。

## 00306042 API版本格式错误

**错误信息**

In HarmonyOS configuration mode, the value of compileSdkVersion/compatibleSdkVersion/targetSdkVersion must be M.S.F when API level is 10 or later, Example: '4.0.0(10)'; In OpenHarmony configuration mode, the value of compileSdkVersion/compatibleSdkVersion/targetSdkVersion must be a number when API level is 10 or later, Example: 10.

**错误描述**

当API版本为10或以上时，compileSdkVersion/compatibleSdkVersion/targetSdkVersion的格式要求：

* 在HarmonyOS配置模式下，必须使用M.S.F格式，例如 '4.0.0(10)'。
* 在OpenHarmony配置模式下，必须使用数值格式，例如10。

**可能原因**

compileSdkVersion/compatibleSdkVersion/targetSdkVersion字段的格式不符合要求。

**处理步骤**

检查工程级build-profile.json5文件，确保以上字段的格式符合要求。

## 00306043 JS模块不允许依赖ArkTS库

**错误信息**

JS module XXX does not allow ArkTS dependency YYY. Check at file: ZZZ.

**错误描述**

JS模块XXX不能依赖ArkTS YYY。

**可能原因**

JS模块引入了ArkTS依赖YYY。

**处理步骤**

检查XXX模块oh-package.json5的依赖项，确保其不包含ArkTS依赖YYY。

## 00306044 JS堆内存不足

**错误信息**

Worker terminated due to reaching memory limit: JS heap out of memory.

**错误描述**

达到内存限制导致任务终止：JS堆内存不足。

**可能原因**

任务执行过程中堆内存不足。

**处理步骤**

1. 在[hvigor-config.json5](ide-hvigor-set-options.md)中调整线程相关配置：hvigor.pool.maxSize、ohos.arkCompile.maxSize、hvigor.enableMemoryCache。
2. 执行任务时关闭[parallel模式](ide-hvigor-improve-performance.md)。

## 00306045 当compatibleSdkVersion为5.0.0(12)及以上时useNormalizedOHMUrl才可配置为true

**错误信息**

UseNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later.

**错误描述**

当compatibleSdkVersion为5.0.0(12)及以上时，useNormalizedOHMUrl才可配置为true。

**可能原因**

工程级build-profile.json5中compatibleSdkVersion配置为4.1.0(11)或以下，并且useNormalizedOHMUrl设置为true。

**处理步骤**

如果compatibleSdkVersion为4.1.0(11)或以下版本，将useNormalizedOHMUrl设置为false。

## 00306046 useNormalizedOHMUrl为false时不支持字节码HAR

**错误信息**

Bytecode HARs: XXX not supported when useNormalizedOHMUrl is not true.

**错误描述**

useNormalizedOHMUrl为false时不支持字节码HAR。

**可能原因**

工程级build-profile.json5中的useNormalizedOHMUrl配置为false，并且当前编译模块的依赖链上存在字节码HAR。

**处理步骤**

当前编译模块的依赖链上存在字节码HAR，将工程级build-profile.json5中的useNormalizedOHMUrl配置为true。

## 00306047 多个HSP模块依赖同一个HAR

**错误信息**

Found HSPs that have the same HAR.

**错误描述**

多个HSP模块依赖同一个HAR。

**可能原因**

多个HSP模块依赖同一个HAR。

**处理步骤**

参考[最佳实践：模块化设计](../best-practices/bpta-modular-design.md)。

## 00306048 当前API版本不支持配置autoLazyImport

**错误信息**

autoLazyImport cannot be configured for the current API version. autoLazyImport can be used in the beta3 version of API 12 or higher versions.

**错误描述**

当前API版本不支持配置autoLazyImport，API 12 beta3及以上版本支持使用autoLazyImport。

**可能原因**

在API 12 beta3以下的版本中将autoLazyImport配置为true。

**处理步骤**

选择以下一种方式解决：

* 检查工程级build-profile.json5中的compatibleSdkVersion和compatibleSdkVersionStage字段，如果compatibleSdkVersion设置为API 12，则将compatibleSdkVersionStage设置为beta3。
* 将autoLazyImport配置为false。

## 00306049 模块中存在重复的文件

**错误信息**

Duplicated files found in module XXX. This may cause unexpected errors at runtime.

**错误描述**

在模块XXX中存在重复的文件，可能会导致运行时错误。

**可能原因**

模块中存在相同名称的.so文件。

**处理步骤**

选择以下一种方式解决：

* 确保每个.so文件名都是唯一的。

* 通过[pickFirsts、pickLasts或select字段](ide-hvigor-cpp.md#section17675528161517)设置.so文件的优先级。

## 00306050 FA模型的项目不允许依赖外部项目模块

**错误信息**

This project is in the FA model and does not allow for external dependencies.

**错误描述**

FA模型的项目不允许依赖外部项目模块。

**可能原因**

FA模型的项目在build-profile.json5中，srcPath字段依赖了外部项目模块。

**处理步骤**

工程级build-profile.json5中，移除srcPath字段依赖的外部项目模块。

## 00306051 Stage模型的项目不允许依赖FA模型的模块

**错误信息**

This project is in the stage model and does not allow for dependencies of modules in the FA model.

**错误描述**

Stage模型的项目不允许依赖FA模型的模块。

**可能原因**

在Stage模型的工程级build-profile.json5中srcPath字段引入了FA模型的工程模块。

**处理步骤**

工程级build-profile.json5移除对FA模型的工程模块的引用。

## 00306052 不能依赖工程外的HAP模块

**错误信息**

Cannot depend on HAP modules outside of this project.

**错误描述**

不能依赖工程外的HAP模块。

**可能原因**

工程级build-profile.json5中srcPath字段依赖了项目外的HAP模块。

**处理步骤**

使用HSP或HAR模块替换项目外的HAP依赖。

## 00306053 ohpm安装依赖失败

**错误信息**

ohpm install failed.

**错误描述**

ohpm安装依赖失败。

**可能原因**

网络不通，或[ohpm镜像仓库地址](ide-ohpmrc.md#zh-cn_topic_0000001792216397_默认配置项)、oh-package.json5中依赖的包名、版本号不正确。

**处理步骤**

请检查网络，或ohpm镜像仓库地址、oh-package.json5中依赖的包名、版本号是否正确。

## 00306054 构建任务的命令无效

**错误信息**

Task XXX was not found in the project XXX. Invalid command to execute the build task, please verify the parameters in the command and try again.

**错误描述**

在工程中找不到任务，执行构建任务的命令无效，请检查命令行中的参数并重试。

**可能原因**

构建命令中的参数设置错误。

**处理步骤**

1. 执行“hvigorw --help”命令，了解有关hvigor命令的更多信息。
2. 执行“hvigorw tasks”命令，查看可用任务列表。
3. 执行命令时增加“--info”或“--debug”选项，获取更多日志输出。

## 00306055 工程外的模块缺少配置

**错误信息**

Missing module configuration for external module outside the current project.

**错误描述**

工程外的模块缺少配置。

**可能原因**

使用了工程外的模块，但是没有在工程的build-profile.json5中配置模块信息。

**处理步骤**

检查工程级build-profile.json5，确保使用的所有模块都在modules字段中配置。

## 00306056 hvigor守护进程异常退出

**错误信息**

A log of daemon process can be found at file: XXX.

**错误描述**

hvigor守护进程异常退出，可在XXX文件中查看日志。

**可能原因**

守护进程内存不足，具体原因可查看守护进程日志。

**处理步骤**

1. 修改hvigor-config.json5中nodeOptions下的maxOldSpaceSize，增加守护进程的内存。
2. [关闭守护进程](ide-hvigor-daemon.md)后重新编译，验证该问题是否与守护进程有关。
