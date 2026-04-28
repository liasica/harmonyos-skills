---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-set-options
title: hvigor-config.json5文件
breadcrumb: 指南 > 构建应用 > 配置文件 > hvigor-config.json5文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:59b6baaef53171e1d15e500eb29362424d346efc81b9077d4f45c218678e29a9
---

## 配置文件结构

hvigor-config.json5文件整体的结构如下。

```
1. modelVersion
2. dependencies
3. execution
4. └── analyze
5. └── daemon
6. └── incremental
7. └── parallel
8. └── typeCheck
9. └── optimizationStrategy
10. logging
11. └── level
12. debugging
13. └── stacktrace
14. nodeOptions
15. └── maxOldSpaceSize
16. └── maxSemiSpaceSize
17. └── exposeGC
18. javaOptions
19. └── Xmx
20. properties
21. └── hvigor.cacheDir
22. └── ohos.buildDir
23. └── enableSignTask
24. └── ohos.arkCompile.maxSize
25. └── hvigor.pool.cache.capacity
26. └── hvigor.pool.maxSize
27. └── ohos.pack.compressLevel
28. └── hvigor.analyzeHtml
29. └── hvigor.dependency.useNpm
30. └── ohos.compile.lib.entryfile
31. └── ohos.align.target
32. └── ohos.fallback.target
33. └── ohos.arkCompile.sourceMapDir
34. └── ohos.collect.debugSymbol
35. └── hvigor.enableMemoryCache
36. └── hvigor.memoryThreshold
37. └── ohos.nativeResolver
38. └── ohos.arkCompile.noEmitJs
39. └── ohos.arkCompile.singleFileEmit
40. └── ohos.sign.har
41. └── hvigor.keepDependency
42. └── ohos.arkCompile.emptyBundleName
43. └── ohos.uiTransform.Optimization
44. └── ohos.har.excludeHspDependencies
45. └── ohos.processLib.optimization
46. └── ohos.obfuscationRules.optimization
47. └── hvigor.incremental.optimization
48. └── hvigor.task.schedule.optimization
49. └── ohos.byteCodeHar.integratedOptimization
50. └── ohos.rollupCache.usePathPlaceholder
51. └── ohos.rollupCache.useSourceHash
52. └── ohos.arkCompile.writeRollupCache
53. └── ohos.align.deviceTypes
54. └── ohos.dependencies.types.enable
55. └── ohos.defaults.release.cmakebuildtype
56. └── ohos.defaults.autoLazyImport
57. parameterFile
```

## 配置文件字段说明

hvigor-config.json5配置文件包含以下字段。

**表1** hvigor-config.json5文件字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| modelVersion | 必选 | 字符串 | 开发态版本号。 |
| dependencies | 必选 | 对象 | 当前工程执行构建任务时，依赖的构建插件及版本，为npm源组件。  说明  修改dependencies后，请根据界面提示，点击编辑器右上角**Sync Now**安装依赖。 |
| [execution](ide-hvigor-set-options.md#section6901191119219) | 可选 | 对象 | 执行构建的相关配置参数，仅在命令行场景下生效。 |
| [logging](ide-hvigor-set-options.md#section85176471028) | 可选 | 对象 | 日志相关配置参数。 |
| [debugging](ide-hvigor-set-options.md#section76575554217) | 可选 | 对象 | 调测相关配置参数。 |
| [nodeOptions](ide-hvigor-set-options.md#section74431812314) | 可选 | 对象 | Node相关配置参数。 |
| [javaOptions](ide-hvigor-set-options.md#section7929682318) | 可选 | 对象 | java相关配置参数。 |
| [properties](ide-hvigor-set-options.md#section260315160319) | 可选 | 对象 | 额外配置参数。 |
| [parameterFile](ide-hvigor-set-options.md#section24539147532) | 可选 | 字符串 | 自定义的参数化配置文件路径。  从DevEco Studio 6.0.2 Beta1版本开始支持。 |

## execution

execution是执行构建的相关配置参数，除了optimizationStrategy字段外，其他字段仅在命令行构建场景下生效，如果通过DevEco Studio菜单栏构建，需要在**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**中设置。

**表2** execution字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| analyze | 可选 | 字符串/布尔值 | 构建分析模式。   * normal（默认值）：普通模式，通过简单打点数据进行分析。原default模式已废弃。 * advanced：进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。原verbose模式已废弃。 * ultrafine：超精细化模式，与advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。从DevEco Studio 6.0.0 Beta1版本开始支持。 * false：不启用构建分析。 |
| daemon | 可选 | 布尔值 | 是否启用守护进程编译。   * true（缺省默认值）：启用。 * false：不启用。 |
| incremental | 可选 | 布尔值 | 是否启用增量编译。   * true（缺省默认值）：启用。 * false：不启用。 |
| parallel | 可选 | 布尔值 | 是否启用并行编译。   * true（缺省默认值）：启用。 * false：不启用。 |
| typeCheck | 可选 | 布尔值 | 是否启用构建脚本hvigorfile.ts文件的类型检查，启用后构建效率可能会有所降低。   * true：启用。 * false（缺省默认值）：不启用。 |
| optimizationStrategy | 可选 | 字符串 | 指定构建模式。从DevEco Studio 5.1.1 Release版本开始支持。   * performance：性能优先模式，可加快构建速度，但会占用更多内存。 * memory（缺省默认值）：内存优先模式，可以减少编译内存占用。   说明  更改模式后，首次编译会执行全量编译。 |

execution字段示例：

```
1. {
2. "execution": {
3. "analyze": "normal",
4. "daemon": true,
5. "incremental": true,
6. "parallel": true,
7. "typeCheck": false,
8. "optimizationStrategy": "performance",
9. }
10. }
```

## logging

logging是日志相关配置参数。

**表3** logging字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| level | 可选 | 字符串 | 构建时打印日志的级别。   * debug：调测日志。 * info（缺省默认值）：基本信息日志。 * warn：告警日志。 * error：错误日志。 |

logging字段示例：

```
1. {
2. "logging": {
3. "level": "debug"
4. }
5. }
```

## debugging

debugging是调测相关配置参数。

**表4** debugging字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| stacktrace | 可选 | 布尔值 | 是否启用堆栈跟踪。   * true：启用。 * false（缺省默认值）：不启用。 |

debugging字段示例：

```
1. {
2. "debugging": {
3. "stacktrace": true
4. }
5. }
```

## nodeOptions

nodeOptions是Node相关配置参数。

**表5** nodeOptions字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| maxOldSpaceSize | 可选 | 整型数值 | 启用守护进程编译时，为守护进程设置最大的老生代内存大小，单位为MB，默认为8192MB。当工程代码量较大出现JS内存溢出时，可以调整该参数。 |
| maxSemiSpaceSize | 可选 | 整型数值 | 启用守护进程编译时，为守护进程设置新生代内存最大的半空间大小，单位为MB，默认为16MB。增加半空间大小可能会提高Node.js的吞吐量，但会消耗更多内存。  该字段从DevEco Studio 5.1.0 Release版本开始支持。 |
| exposeGC | 可选 | 布尔值 | 是否启用GC（Garbage Collection，内存回收），启用后会优化编译过程的峰值内存。   * true（缺省默认值）：启用。 * false：不启用。 |

nodeOptions字段示例：

```
1. {
2. "nodeOptions": {
3. "maxOldSpaceSize": 8192,
4. "maxSemiSpaceSize": 16,
5. "exposeGC": true,
6. }
7. }
```

## javaOptions

javaOptions是java相关配置参数。

**表6** javaOptions字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| Xmx | 可选 | 整型数值 | 设置JVM最大堆内存，单位为MB，默认为512MB。 |

javaOptions字段示例：

```
1. {
2. "javaOptions": {
3. "Xmx": 512
4. }
5. }
```

## properties

properties是额外配置参数。除了在hvigor-config.json5中配置properties外，还可以通过命令行参数-c或--config指定properties，命令行优先级比hvigor-config.json5更高，命令行配置方式请参考[命令行构建工具（hvigorw）](ide-hvigor-commandline.md#section92386011817)。

**表7** properties字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| hvigor.cacheDir | 可选 | 字符串 | 指定项目根目录下的.hvigor缓存文件夹的存放路径。  说明  同名的不同工程不可指定相同的存放位置。 |
| ohos.buildDir | 可选 | 字符串 | 指定项目的构建产物目录（build目录）存放位置。  说明  同名的不同工程不可指定相同的存放位置。 |
| enableSignTask | 可选 | 布尔值 | 是否启用HAP或HSP签名任务。   * true（缺省默认值）：启用。 * false：不启用。 |
| ohos.arkCompile.maxSize | 可选 | 整型数值 | 指定编译ArkTS线程的数量，默认为5。 |
| hvigor.pool.cache.capacity | 可选 | 整型数值 | 定义内存中缓存数据的容量，默认为4，数值越小，内存中缓存数据越少。配置为0，表示不启用内存缓存配置。 |
| hvigor.pool.maxSize | 可选 | 整型数值 | 指定编译过程中的线程数量，相比ohos.arkCompile.maxSize增加签名、打包等任务的线程。默认值为“工程的模块数”和“电脑虚拟核数-1”两者的较小值。 |
| ohos.pack.compressLevel | 可选 | 字符串 | 设置打包hap（压缩so）或app（压缩hap）时的压缩率等级。压缩率越高，压缩速度越慢。   * fast（缺省默认值）：最低等级的压缩率，压缩速度最快。 * standard：适中等级的压缩率，压缩速度适中。 * ultimate：最高等级的压缩率，压缩速度最慢。 |
| hvigor.analyzeHtml | 可选 | 布尔值 | 是否生成构建可视化html文件。   * true：生成构建可视化html文件。生成的html文件存放在工程的.hvigor/report目录下，该文件可直接在浏览器中打开。 * false（缺省默认值）：不生成构建可视化html文件。 |
| hvigor.dependency.useNpm | 可选 | 布尔值 | 指定是否使用npm下载hvigor依赖。  若未配置该字段，当Node.js版本 ≥ 16时，默认使用pnpm下载依赖。在某些特定场景，可以通过配置该字段指定使用npm下载依赖。   * true：对于任意Node版本，都使用npm下载依赖。 * false（缺省默认值）：Node.js版本 ≥ 16时，使用pnpm下载依赖；Node.js版本 ＜ 16时，使用npm下载依赖。 |
| ohos.compile.lib.entryfile | 可选 | 布尔值 | 指定是否从入口文件开始编译：   * true：表示从模块的入口文件开始编译，将编译入口文件及被引用的文件，没被引用的文件不会参与编译流程。 * false（缺省默认值）：表示将src/main/ets下的ets和ts文件进行全量编译，涉及到以下场景：   1. 构建HSP时，存在于src/main/ets下的ets和ts文件都会被编译到产物中。   2. release模式对HAR混淆或构建字节码HAR时，存在于src/main/ets下的ets和ts文件都会被编译到产物中。   3. 构建HAP/HSP时，存在于动态依赖的HAR模块src/main/ets下的ets和ts文件都会被编译到产物中。 |
| ohos.align.target | 可选 | 字符串 | 指定本次构建任务所有涉及到的模块及其依赖的模块的target。详情请参考[多产物构建target](ide-customized-multi-targets-and-products-guides.md#section7121513141619)。 |
| ohos.fallback.target | 可选 | 字符串数组 | 指定本次构建任务所有涉及到的模块及其依赖模块的fallback target，fallback target是一个特定优先级的target，各target的优先级顺序：align target > 命令行指定target > 被依赖的父模块target > fallback target > default target。详情请参考[多产物构建target](ide-customized-multi-targets-and-products-guides.md#section7121513141619)。 |
| ohos.arkCompile.sourceMapDir | 可选 | 字符串 | 指定sourceMap文件的生成路径，方便开发者进行堆栈的回栈与错误信息的定位，当前仅支持Stage模型。若没有指定路径，默认生成在build/{productName}/outputs/{targetName}/mapping下。  说明  从API 12开始支持。 |
| ohos.collect.debugSymbol | 可选 | 布尔值 | 是否将[sourceMap](ide-exception-stack-parsing-principle.md#section666114451518)、[nameCache](ide-exception-stack-parsing-principle.md#section19215122372720)和带调试信息的so文件归档到产物路径下，根据选择的构建模式，如果是构建HAP/HSP/HAR，会归档到模块的build/{productName}/outputs/{targetName}/symbol的release或debug目录下；如果是构建APP，会将HAP/HSP模块的文件归档到工程的build/outputs/{productName}/symbol的release或debug目录下。   * true：归档。 * false：不归档。   说明  * 如果不配置，release模式时默认值为true，debug模式时默认值为false。 * 仅支持Stage模型。 * nameCache文件仅在release模式下且开启混淆后才会生成，release模式下不开启混淆以及debug模式下均不生成这个文件。 |
| hvigor.enableMemoryCache | 可选 | 布尔值 | 是否开启缓存，开启缓存会加快增量编译速度，关闭缓存能够节省内存占用，但是会增加增量编译时间。   * true（缺省默认值）：开启。 * false：不开启。 |
| hvigor.memoryThreshold | 可选 | 整型数值 | 内存管理阈值，单位为MB，当编译构建占用内存超过此阈值时，新加入的编译任务会等待，直到正在进行的编译任务结束，新的编译任务才能开始，此配置将导致编译时间延长。  说明  * 配置该字段后，即使hvigor.enableMemoryCache配置为true，也不进行缓存。 * 该字段配置为很小的值时，构建任务会串行执行，等效于配置ohos.arkCompile.maxSize:1；配置为很大的值时，与不配置没有差异。 |
| ohos.nativeResolver | 可选 | 布尔值 | ArkTS编译过程中是否使用高性能插件进行依赖寻址，使用高性能插件可以降低编译过程的峰值内存，加快编译速度。   * true（缺省默认值）：使用。 * false：不使用。 |
| ohos.arkCompile.noEmitJs | 可选 | 布尔值 | ArkTS编译过程中是否生成js中间产物，具体方案及开启后的影响请参考[优化编译中间产物生成](ide-hvigor-experimental-properties.md#section11117155101617)。   * true：不生成。 * false（缺省默认值）：生成。 |
| ohos.arkCompile.singleFileEmit | 可选 | 布尔值 | 是否开启单文件解析完成后写入磁盘的能力，具体方案及开启后的影响请参考[文件写入磁盘](ide-hvigor-experimental-properties.md#section1131619813214)。   * true：开启。 * false（缺省默认值）：不开启。 |
| ohos.sign.har | 可选 | 布尔值 | 是否启用HAR签名任务。详情请参考[构建签名HAR](ide-hvigor-build-har.md#section116791730173713)。   * true：启用。 * false（缺省默认值）：不启用。 |
| hvigor.keepDependency | 可选 | 布尔值 | 是否保持hsp中的所有依赖。如果保持则不对依赖进行处理，如果不保持，则只会保留hsp模块中的hsp相关依赖。   * true（缺省默认值）：保持。 * false：不保持。 |
| ohos.arkCompile.emptyBundleName | 可选 | 布尔值 | ArkTS编译转换后的产物，bundleName字段是否为空值。   * true：bundleName字段的值是空值。 * false（缺省默认值）：bundleName字段是应用实际的包名。   说明  * 仅支持在EntryAbility中使用loadContentByName加载首页，同时使用Navigation导航进行页面跳转时设置为true，否则会导致应用闪退。 * 预览时暂不支持配置该字段，字段默认取值为false。 |
| ohos.uiTransform.Optimization | 可选 | 布尔值 | 是否对ArkTS编译转换后的产物中的bundleName字段开启优化。   * true：开启，bundleName字段的值是变量。 * false（缺省默认值）：不开启，bundleName字段是应用实际的包名。   该字段从DevEco Studio 5.0.5 Beta1版本开始支持。  说明  * 该字段对字节码HAR不生效，字节码HAR产物的bundleName字段的值默认是变量。 * 预览时暂不支持配置该字段，字段默认取值为false。 |
| ohos.har.excludeHspDependencies | 可选 | 布尔值 | 构建har包时，产物module.json中是否排除依赖的hsp，排除后，module.json中不包含dependencies字段。   * true：排除。 * false（缺省默认值）：不排除。   该字段从DevEco Studio 5.1.0 Release版本开始支持。 |
| ohos.processLib.optimization | 可选 | 布尔值 | 是否启用[ProcessLibs任务](ide-hvigor-task-process.md#li671313965913)性能优化，启用后可以减少ProcessLibs任务中so增量判定的耗时。   * true：启用。 * false（缺省默认值）：不启用。 |
| ohos.obfuscationRules.optimization | 可选 | 布尔值 | release模式开启混淆时，是否优化三方依赖中混淆配置文件的收集方式，优化后可以减少收集耗时，加快编译速度。   * true：优化。 * false（缺省默认值）：不优化。   该字段从DevEco Studio 5.1.0 Release版本开始支持。 |
| hvigor.incremental.optimization | 可选 | 布尔值 | 是否开启任务增量判断优化，优化方案及开启后的影响请参考[任务增量判断优化](ide-hvigor-experimental-properties.md#section95571022144613)。   * true：开启。 * false（缺省默认值）：不开启。 |
| hvigor.task.schedule.optimization | 可选 | 布尔值 | 是否开启任务调度优化，优化方案及开启后的影响请参考[任务调度优化](ide-hvigor-experimental-properties.md#section09371546164610)。   * true：开启。 * false（缺省默认值）：不开启。 |
| ohos.byteCodeHar.integratedOptimization | 可选 | 布尔值 | 是否开启字节码HAR集成行为优化，开启后，字节码HAR使用的依赖支持配置在工程级oh-package.json5的dependencies或dynamicDependencies中，同时会优化部分依赖收集行为，具体请参考[编译行为差异说明](ide-hvigor-dependencies.md#section957371853712)。   * true：开启。 * false（缺省默认值）：不开启。   从DevEco Studio 5.1.1 Beta1版本开始支持。 |
| ohos.rollupCache.usePathPlaceholder | 可选 | 布尔值 | 是否将build目录下rollup缓存中的绝对路径替换为占位符。该功能是实验特性，开启后会造成读写缓存性能降低。   * true：是，即缓存中是占位符。 * false（缺省默认值）：否，即缓存中是绝对路径。   从DevEco Studio 6.0.0 Beta1版本开始支持。 |
| ohos.rollupCache.useSourceHash | 可选 | 布尔值 | 是否将build目录下rollup缓存中的源码替换为对应的hash内容，减少缓存大小。该功能是实验特性，可以提升缓存对比和读写性能。   * true：是，即缓存源码hash。 * false（缺省默认值）：否，即缓存源码内容。   从DevEco Studio 6.0.0 Beta1版本开始支持。 |
| ohos.arkCompile.writeRollupCache | 可选 | 布尔值 | build目录下是否写入rollup缓存。   * true（缺省默认值）：写缓存。 * false：不写缓存。   从DevEco Studio 6.0.0 Beta2版本开始支持。 |
| ohos.align.deviceTypes | 可选 | 字符串数组 | 指定归一的设备类型，构建APP时，当HAP/HSP的module.json5中的设备类型是ohos.align.deviceTypes的超集时，模块才会被打包到APP中，同时打包后产物中的设备类型会被设置为ohos.align.deviceTypes的值。  从DevEco Studio 6.0.0 Beta2版本开始支持。  说明  仅支持Stage模型。 |
| ohos.dependencies.types.enable | 可选 | 布尔值 | 编译时是否收集依赖的HAR模块/[源码HAR包](ide-hvigor-build-har.md#section197792874110)的[类型声明文件](arkoptions-guide.md#types)参与语法校验。如果HAR中配置了类型声明文件，建议开启。   * true：收集。 * false（缺省默认值）：不收集。   从DevEco Studio 6.0.0 Beta3版本开始支持。 |
| ohos.defaults.release.cmakebuildtype | 可选 | 字符串 | 在release模式下构建时，指定cmake构建类型，对所有模块生效。   * Debug：不优化代码，附加调试信息。 * Release（缺省默认值）：最大化优化代码，但不包含调试信息。 * RelWithDebInfo：近似于Release模式，既进行了代码优化，同时保留部分调试信息。   从DevEco Studio 6.0.1 Beta1版本开始支持。  说明  * 模块级build-profile.json5文件中也可以通过[arguments字段](ide-exception-stack-parsing-principle.md#section147714466283)指定cmake构建类型，例如"arguments": "-DCMAKE\_BUILD\_TYPE=RelWithDebInfo"。arguments字段的优先级比ohos.defaults.release.cmakebuildtype更高。 * 在debug模式下构建时，该字段配置无效，默认使用Debug构建类型。 |
| ohos.defaults.autoLazyImport | 可选 | 布尔值 | 编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。仅支持在源码中添加"lazy"关键字，不包含依赖的字节码HAR包或HSP。关于lazy-import的介绍及相关影响请参考[延迟加载（lazy import）](arkts-lazy-import.md)。   * true：添加。 * false（缺省默认值）：不添加。   从DevEco Studio 6.0.2 Beta1版本开始支持。  说明  * 如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。 * 仅支持Stage模型。 * build-profile.json5文件中也可以通过autoLazyImport字段实现该能力，autoLazyImport的优先级比ohos.defaults.autoLazyImport更高。 |

properties字段示例：

```
1. {
2. "properties": {
3. "hvigor.cacheDir": "D://tmp",
4. "ohos.buildDir": "D://tmp",
5. "enableSignTask": true,
6. "ohos.arkCompile.maxSize": 6,
7. "hvigor.pool.cache.capacity": 2,
8. "hvigor.pool.maxSize": 8,
9. "ohos.pack.compressLevel": "standard",
10. "hvigor.analyzeHtml": true,
11. "hvigor.dependency.useNpm": false,
12. "ohos.compile.lib.entryfile": true,
13. "ohos.align.target": "target1",
14. "ohos.fallback.target": ["target1", "target2"],
15. "ohos.arkCompile.sourceMapDir": "D://MyProject",
16. "ohos.collect.debugSymbol": false,
17. "hvigor.enableMemoryCache": true,
18. "hvigor.memoryThreshold": 1000,
19. "ohos.nativeResolver": true,
20. "ohos.arkCompile.noEmitJs": true,
21. "ohos.arkCompile.singleFileEmit": true,
22. "ohos.sign.har": true,
23. "hvigor.keepDependency": false,
24. "ohos.arkCompile.emptyBundleName": true,
25. "ohos.align.deviceTypes": ["phone", "tablet"],
26. "ohos.defaults.release.cmakebuildtype": "RelWithDebInfo",
27. }
28. }
```

## parameterFile

从DevEco Studio 6.0.2 Beta1版本开始，编译构建新增参数化配置功能。开发者可添加一个参数化文件（json5格式文件），在该文件中维护构建配置文件build-profile.json5中部分字段的值，工程级或者各模块的build-profile.json5将根据该文件中的键值对进行配置，满足不同构建场景下，开发者快速切换构建配置的需要。

### 配置说明

在hvigor-config.json5文件中添加parameterFile配置，并指定parameterFile文件路径。配置规则如下：

* parameterFile文件配置相对路径，并以工程下hvigor-config.json5文件为起点，如："parameterFile": "./parameterFile.json5"。
* parameterFile文件内容采用json5格式，支持多层json对象嵌套。
* parameterFile文件中的参数化key支持自定义，参数化value类型及配置要求和对应要替换的字段保持一致，具体可查看build-profile.json5文件中对应的字段。
* build-profile.json5中支持参数化的字段有：source.sourceRoots，resource.directories，buildProfileFields，其他字段均不支持。
* 在build-profile.json5中以“@param:key”的形式引用parameterFile文件中对应的自定义字段，示例如下。
* 不支持在hvigorfile.ts脚本中使用参数化配置。

### 示例

hvigor-config.json5的parameterFile字段示例：

```
1. {
2. "nodeOptions": {
3. ...
4. },
5. "parameterFile": "./parameterFile.json5"
6. }
```

parameterFile所指向文件的配置示例：

```
1. {
2. "source": {
3. "customizedSourceRoot1": "./src/default1",
4. "customizedSourceRoot2": "./src/default2"
5. }
6. }
```

模块级build-profile.json5示例，以多个har模块为例：

```
1. // har1模块build-profile.json5
2. "targets": [
3. {
4. "name": "default",
5. "source": {
6. "sourceRoots": ["@param:source.customizedSourceRoot1"]   // 使用时必须以'@param:'开头，构建时sourceRoots会被替换为'./src/default1'
7. }
8. }
9. ]
10. // har2模块build-profile.json5
11. "targets": [
12. {
13. "name": "default",
14. "source": {
15. "sourceRoots": ["@param:source.customizedSourceRoot2"]
16. }
17. }
18. ]
```
