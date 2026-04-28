---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-commandline
title: 命令行构建工具（hvigorw）
breadcrumb: 指南 > 命令行工具 > 命令行构建工具（hvigorw）
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45adc2e6357be102cc3d9cae1196051c7069d0a4e238eeb4182025194b61baca
---

hvigorw作为Hvigor的wrapper包装工具，支持自动安装Hvigor构建工具和相关插件依赖，以及执行Hvigor构建命令。

执行命令前，需要先配置JDK，配置Node.js、hvigor等环境变量，具体请参考[搭建流水线](ide-command-line-building-app.md)。

## 命令行使用方式

hvigorw命令行格式为：

```
1. hvigorw [taskNames...] <options>
```

其中taskNames是任务，可同时执行多个任务，options是可选参数，具体的任务和可选参数请参考[常用命令](ide-hvigor-commandline.md#section16300629103)。

说明

从hvigorw 5.18.4版本开始，以下命令支持在任意路径下执行，其他hvigorw命令需要在工程根目录下执行。

* hvigorw -v
* hvigorw --version
* hvigorw version
* hvigorw -h
* hvigorw --help

## 常用命令

常见的任务和参数如下，更多任务请参考[任务详细说明](ide-hvigor-task-process.md#section196919100414)。

### 查询

| **参数** | 说明 |
| --- | --- |
| -h, --help | 打印hvigorw的命令帮助信息。 |
| -v, --version, version | 打印hvigorw版本信息。 |

### 编译构建

| 任务 | 说明 |
| --- | --- |
| clean | 清理构建产物build目录。 |
| collectCoverage | 基于打点数据生成覆盖率统计报表。 |
| assembleHap | 构建Hap应用。 |
| assembleApp | 构建App应用。 |
| assembleHsp | 构建Hsp包。 |
| assembleHar | 构建Har包。 |

编译构建命令行常用扩展参数：

| 参数 | 说明 |
| --- | --- |
| -p buildMode={debug | release} | 采用debug/release模式进行编译构建。  缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。  关于构建模式的详细说明，请参考[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。针对HAR构建，请参考[构建HAR](ide-hvigor-build-har.md)。 |
| -p debuggable=true/false | 该配置会覆盖构建模式中对应的buildOption中的debuggable配置。  关于debuggable的合并优先级，请参考[合并编译选项规则](ide-hvigor-compilation-options-customizing-guide.md#section1727865610255)。 |
| -p product={ProductName} | 指定product进行编译, 编译product下配置的module target。  缺省时：默认为default。 |
| -p module={ModuleName}@{TargetName} | 指定模块及target进行编译，可指定多个相同类型的模块进行编译，以逗号隔开；TargetName不指定时默认为default。  限制：此参数需要与--mode module参数搭配使用。  缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。 |
| -p ohos-test-coverage={true | false} | 执行测试框架代码覆盖率插桩编译。 |
| -p coverage={true | false} |
| -p parameterFile=param.json/json5 | 设置oh-package.json5文件的参数配置文件，其中"param"可自行修改为对应配置文件名称。详细使用请参考[parameterFile](ide-oh-package-json5.md#section122411462820)。 |
| -p buildVersion=1 | 设置构建版本号为1，详细使用请参考[app.json5的buildVersion](app-configuration-file.md#配置文件标签)。  该参数从hvigorw 6.23.3版本开始支持。 |

测试相关的命令行：

| 命令行 | 说明 |
| --- | --- |
| hvigorw onDeviceTest -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false} | 通过命令行方式执行Instrument Test。   * module：执行测试的模块，缺省默认是执行所有模块的用例。HAP/HAR/HSP模块都支持。 * coverage：是否需要覆盖率报告，缺省默认为true。 * scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。 * ohos-debug-asan：是否启用ASan检测，缺省默认是false。从hvigorw 5.19.0版本开始支持。   多个module和scope之间用逗号隔开。   * 覆盖率测试报告路径：<module-path>/.test/default/outputs/ohosTest/reports * 测试结果文件：path\_to\_project/module\_name/.test/default/intermediates/ohosTest/coverage\_data/test\_result.txt * ASan日志路径：<module-path>/.test/default/intermediates/ohosTest/coverage\_data |
| hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} | 通过命令行方式执行Local Test。暂不支持在Linux上执行该命令。   * module：执行测试的模块，缺省默认是执行所有模块的用例。HAP/HAR/HSP模块都支持。 * coverage：是否需要覆盖率报告，缺省默认为true。 * scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。   多个module和scope之间用逗号隔开。   * 覆盖率测试结果文件： <module-path>/.test/default/outputs/test/reports * 测试结果文件：path\_to\_project/module\_name/.test/default/intermediates/test/coverage\_data/test\_result.txt |

### 日志

| 参数 | 说明 |
| --- | --- |
| -e, --error | 设置hvigor的日志级别为error。 |
| -w, --warn | 设置Hvigor的日志级别为warn。 |
| -i, --info | 设置Hvigor的日志级别为info。 |
| -d, --debug | 设置Hvigor的日志级别为debug。 |
| --stacktrace，--no-stacktrace | Hvigor默认关闭打印所有异常的堆栈信息，如需开启在命令行后添加--stacktrace。 |

### 可视化

| 参数 | 说明 |
| --- | --- |
| --analyze=normal | 在DevEco Studio中开启Build Analyzer构建分析，设置为普通模式，通过简单打点数据进行分析。 |
| --config properties.hvigor.analyzeHtml=true | 在工程的.hvigor/report目录下生成构建可视化html文件，该文件可直接在浏览器中打开。 |
| --analyze=false | 不启用Build Analyzer构建分析。 |
| --analyze=advanced | 启用Build Analyzer构建分析，并设置为进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。 |
| --analyze=ultrafine | 启用Build Analyzer构建分析，并设置为超精细化模式，与advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。  从hvigorw 6.0.0版本开始支持。 |
| --analyze | 同--analyze=normal命令。  从hvigorw 4.3.0开始废弃，请使用--analyze=normal替换。 |
| --no-analyze | 同--analyze=false命令。  从hvigorw 4.3.0开始废弃，请使用--analyze=false替换。 |
| --verbose-analyze | 同--analyze=advanced命令。  从hvigorw 4.3.0开始废弃，请使用--analyze=advanced替换。 |

### daemon

| 参数 | 说明 |
| --- | --- |
| --daemon | 启用[守护进程](ide-hvigor-daemon.md)。 |
| --no-daemon | Hvigor默认启用守护进程，如需关闭，可在命令行后添加该选项。  命令行模式下推荐使用此参数。 |
| --stop-daemon | 关闭当前工程的守护进程。 |
| --stop-daemon-all | 关闭所有工程的守护进程。 |
| --status-daemon | 查询当前环境中所有的Hvigor守护进程信息。 |
| --max-old-space-size=12345 | 设置守护进程最大的老生代内存大小为12345MB。 |
| --max-semi-space-size=32 | 设置守护进程新生代内存最大的半空间大小为32MB。  该参数从hvigorw 5.18.4版本开始支持。 |

### 性能/内存

| 参数 | 说明 |
| --- | --- |
| --parallel, --no-parallel | Hvigor默认开启[并行构建](ide-hvigor-improve-performance.md)能力，如需关闭在命令行后添加--no-parallel。 |
| --incremental, --no-incremental | Hvigor默认开启[增量构建](ide-hvigor-incremental-build.md)能力，如需关闭在命令行后添加--no-incremental。 |
| --optimization-strategy=performance | 设置构建模式为性能优先模式，可加快构建速度，但会占用更多内存。  从hvigorw 5.19.2版本开始支持。 |
| --optimization-strategy=memory | 设置构建模式为内存优先模式，可以减少编译内存占用，默认使用memory。  从hvigorw 5.19.2版本开始支持。 |

### 公共命令

| 任务 | 说明 |
| --- | --- |
| tasks | 打印工程各模块包含的任务信息。 |
| taskTree | 打印工程各模块的任务依赖关系信息。 |
| prune | 清除30天内未使用的Hvigor缓存文件并从pnpm存储中删除未引用的包。 |
| buildInfo | 打印工程级或模块级build-profile.json5中的配置信息，包含product、module、target、buildMode、buildOption，以树状结构输出。  该功能从hvigorw 5.18.4版本开始支持。 |

buildInfo命令扩展参数：

| 参数 | 说明 |
| --- | --- |
| -p module={ModuleName} | 指定需要打印配置信息的模块名，不指定时会打印工程级的配置信息。 |
| -p buildOption | 命令包含此参数时会打印buildOption配置，不含此参数时将不会展示buildOption配置，输出的buildOption优先级请参考[合并编译选项规则](ide-hvigor-compilation-options-customizing-guide.md#section1727865610255)。 |
| -p json | 将输出结果以json格式展示。 |

### 其他命令

| 参数 | 说明 |
| --- | --- |
| -s,--sync | 处理并持久化Hvigor部分工程信息到工程./hvigor/outputs/sync/output.json中。 |
| -m,--mode | 在对应的目录执行相应的task，例hvigorw clean -m project在工程目录下执行build目录清理（即清理工程级别的build文件夹）。 |
| --enable-build-script-type-check | 开启工程中hvigorfile.ts的类型检查，该字段已废弃，请使用--type-check替换。 |
| --type-check, --no-type-check | Hvigor默认关闭工程中hvigorfile.ts的类型检查，如需开启，可在命令行后添加--type-check。 |
| --no-pnpm-frozen-lockfile，--pnpm-frozen-lockfile | Hvigor默认不忽略pnpm-lock.yaml文件，如需忽略，可在命令行后添加--pnpm-frozen-lockfile。  忽略pnpm-lock.yaml文件，按照hvigor-config.json5的配置安装Hvigor插件的依赖（如果不忽略pnpm-lock.yaml文件，在使用Hvigor 2.0.0及以上版本的CI场景下安装Hvigor插件依赖时将报错）。  说明  该命令在4.1 Release及以上版本中已废弃。在CI场景中将自动配置，无需开发者手动配置。 |
| --config, -c | 指定hvigor-config.json5配置文件中的参数。  当前仅支持设置properties里的参数，具体支持的参数请查看[hvigor-config.json5文件](ide-hvigor-set-options.md)中properties支持的参数。  --config properties.key=value 同 -c properties.key=value |
| --watch | 开启观察模式，主要用于预览和热加载场景。 |
| --generate-build-profile, --no-generate-build-profile | 已废弃。生成BuildProfile.ets文件。 |
| --node-home <string> | 指定nodejs路径。 |
