---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-structure
title: 工程目录结构
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 工程目录结构
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f38432f96f66bf4fe14191fc986d8cf89bda6a8031862bd76601e2127544823
---

## ArkTS工程目录结构（Stage模型）

ArkTS Stage模型支持API Version 10及以上版本，其工程目录结构如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/JFz5eq7VSPCwcER4i94RyA/zh-cn_image_0000002583649849.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=978EE084A13F014016B77DD7C400D6B3902A71BFD22A76884E088CAE7AA2DD6B)

* **AppScope > app.json5**：应用的全局配置信息。
* **entry：**应用/元服务模块，编译构建生成一个HAP。
  + **src > main > ets**：用于存放ArkTS源码。
  + **src > main > ets > entryability**：应用/元服务的入口。
  + **src > main > ets > entrybackupability**：用于提供扩展[备份恢复](app-file-backup-extension.md)能力。
  + **src > main > ets > pages**：应用/元服务包含的页面。
  + **src > main > resources：**用于存放应用/元服务模块所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件的详细说明请参考[资源分类与访问](resource-categories-and-access.md)。

    | 资源目录 | 资源文件说明 |
    | --- | --- |
    | base>element | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如：  - boolean.json：布尔型 - color.json：颜色 - float.json：浮点型 - intarray.json：整型数组 - integer.json：整型 - pattern.json：样式 - plural.json：复数形式 - strarray.json：字符串数组 - string.json：字符串值 |
    | base>media | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：**.png**、**.gif**、**.mp3**、**.mp4**等。 |
    | rawfile | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。 |
  + **src > main > module.json5**：Stage模型模块配置文件，主要包含HAP的配置信息、应用在具体设备上的配置信息以及应用的全局配置信息。具体请参考[module.json5配置文件](module-configuration-file.md)。
  + **src > mock****：**配置测试框架的Mock能力。具体请参考[Mock能力](ide-test-mock.md)。
  + **src > ohosTest：**存放Instrument Test测试类。具体请参考[Instrument Test](ide-instrument-test.md)。
  + **src > test：**存放Local Test创建测试类。具体请参考[Local Test](ide-local-test.md)。
  + **build-profile.json5：**当前的模块信息、编译信息配置项，包括buildOption、targets配置等。
  + **hvigorfile.ts**：模块级编译构建任务脚本。
  + **obfuscation-rules.txt**：混淆规则文件。混淆开启后，在使用Release模式进行编译时，会对代码进行编译、混淆及压缩处理，保护代码资产。详见[混淆加固](ide-build-obfuscation.md)。
  + **oh-package.json5**：描述三方包的包名、版本、入口文件（类型声明文件）和依赖项等信息。
* **oh\_modules**：用于存放三方库依赖信息，包含应用/元服务所依赖的第三方库文件。
* **build-profile.json5：**应用级配置信息，包括签名、产品配置等。
* **code-linter.json5：**配置代码检查规则，包括代码检查范围、生效的规则等。
* **hvigorfile.ts：**应用级编译构建任务脚本。
* **oh-package.json5：**描述全局配置，如：依赖覆盖（overrides）、依赖关系重写（overrideDependencyMap）和参数化配置（parameterFile）等。
* **oh-package-lock.json5：**用于锁定应用级依赖的版本，以及缓存依赖的元数据信息。

## C++工程目录结构（Stage模型）

C++ Stage模型支持API Version 10以上版本，支持使用ArkTS和C++进行开发，其工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/sqXqa_uHSfaN_n7uf8wkeg/zh-cn_image_0000002561832763.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=6076DB61694BAE571B6AF81E64F85CCEE4BB6042BB9CF75F3B1A288CD21893DB)

* **entry**：应用模块，编译构建生成一个HAP。
  + **src > main > cpp > types**：用于存放C++的API接口描述文件
  + **src > main > cpp > types** **> libentry > index.d.ts**：描述C++ API接口行为，如接口名、入参、返回参数等。
  + **src > main > cpp > types** **> libentry> oh-package.json5**：配置.so三方包声明文件的入口及包名。
  + **src > main > cpp > CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。
  + **src > main > cpp > napi\_init.cpp：**定义C++ API接口的文件**。**
  + **src > main > ets：**用于存放ArkTS源码。
  + **src > main > resources：**用于存放应用所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件的详细说明请参考[资源分类与访问](resource-categories-and-access.md)。

    | 资源目录 | 资源文件说明 |
    | --- | --- |
    | base>element | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如：  - boolean.json：布尔型 - color.json：颜色 - float.json：浮点型 - intarray.json：整型数组 - integer.json：整型 - pattern.json：样式 - plural.json：复数形式 - strarray.json：字符串数组 - string.json：字符串值。 |
    | base>media | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：**.png**、**.gif**、**.mp3**、**.mp4**等。 |
    | rawfile | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。 |
  + **src > main > module.json5：**Stage模块配置文件，主要包含HAP的配置信息、应用在具体设备上的配置信息以及应用的全局配置信息。具体请参考[module.json5配置文件](module-configuration-file.md)。
  + **build-profile.json5：**当前的模块信息、编译信息配置项，包括buildOption、targets配置等。
  + **hvigorfile.ts：**模块级编译构建任务脚本。
  + **obfuscation-rules.txt**：混淆规则文件。混淆开启后，在使用Release模式进行编译时，会对代码进行编译、混淆及压缩处理，保护代码资产。详见[混淆加固](ide-build-obfuscation.md)。
  + **oh-package.json5**：描述三方包的包名、版本、入口文件（类型声明文件）和依赖项等信息。
  + **oh-package-lock.json5：**用于锁定当前模块依赖的版本，以及缓存依赖的元数据信息。
* **oh\_modules**：用于存放三方库依赖信息，包含应用/元服务所依赖的第三方库文件。
* **build-profile.json5：**应用级配置信息，包括签名、产品配置等。
* **code-linter.json5：**配置代码检查规则，包括代码检查范围、生效的规则等。
* **hvigorfile.ts：**应用级编译构建任务脚本。
* **oh-package.json5：**描述全局配置，如：依赖覆盖（overrides）、依赖关系重写（overrideDependencyMap）和参数化配置（parameterFile）等。
* **oh-package-lock.json5：**用于锁定应用级依赖的版本，以及缓存依赖的元数据信息。

## JS工程目录结构（FA模型）

JS工程只支持FA模型，其工程目录结构如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/m-qZkUMYToW6NFQ0meOuQw/zh-cn_image_0000002561832761.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=0BBDE0D6BEAE27746978CD5E4A39AE1899AE4D5D2A1B200DF40559B19F3DFC5D)

* **entry：**应用/元服务模块，编译构建生成一个HAP。
  + **src > main > js**：用于存放js源码。
  + **src > main > js > MainAbility**：应用/元服务的入口。
  + **src > main > js > MainAbility > i18n**：用于配置不同语言场景资源内容，比如应用文本词条、图片路径等资源。
  + **src > main > js > MainAbility > pages**：MainAbility包含的页面。
  + **src > main > js > MainAbility > app.js**：承载Ability生命周期。
  + **src > main > resources：**用于存放应用/元服务所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件的详细说明请参考[资源分类与访问](resource-categories-and-access.md)。

    | 资源目录 | 资源文件说明 |
    | --- | --- |
    | base>element | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如：  - boolean.json：布尔型 - color.json：颜色 - float.json：浮点型 - intarray.json：整型数组 - integer.json：整型 - pattern.json：样式 - plural.json：复数形式 - strarray.json：字符串数组 - string.json：字符串值 |
    | base>media | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：**.png**、**.gif**、**.mp3**、**.mp4**等。 |
    | rawfile | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。 |
  + **src > main > config.json**：模块配置文件，主要包含HAP的配置信息、应用在具体设备上的配置信息以及应用的全局配置信息。
  + **build-profile.json5：**当前的模块信息、编译信息配置项，包括buildOption、targets配置等。
  + **hvigorfile.ts**：模块级编译构建任务脚本。
  + **oh-package.json5**：配置三方包声明文件的入口及包名。
* **build-profile.json5：**应用级配置信息，包括签名、产品配置等。
* **hvigorfile.ts：**应用级编译构建任务脚本。
