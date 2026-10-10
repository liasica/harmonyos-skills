---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-project-structure
title: 工程目录结构介绍
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 工程目录结构介绍
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:15+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:44599b3b6c730ce2811c88c178f3302287973d544a26983738ca91ff1b81d541
---

## ArkTS工程目录结构

工程目录结构如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/FYZtnKRLQUmJpSqZgUxmcA/zh-cn_image_0000002750169614.png)

* **AppScope > app.json5**：应用/元服务的全局配置信息。
* **entry：**应用/元服务模块，编译构建生成一个HAP。
  + **src > main > ets**：用于存放ArkTS源码。
  + **src > main > ets > entryability**：应用/元服务的入口。
  + **src > main > ets > pages**：应用/元服务包含的页面。
  + **src > main > resources：**用于存放应用/元服务模块所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件的详细说明请参考[资源分类与访问](resource-categories-and-access.md)。

    | 资源目录 | 资源文件说明 |
    | --- | --- |
    | base>element | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如：  - boolean.json：布尔型 - color.json：颜色 - float.json：浮点型 - intarray.json：整型数组 - integer.json：整型 - pattern.json：样式 - plural.json：复数形式 - strarray.json：字符串数组 - string.json：字符串值 |
    | base>media | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 |
    | rawfile | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。 |
  + **src > main > module.json5**：模块配置文件，主要包含HAP的配置信息、应用/元服务在具体设备上的配置信息，以及应用/元服务的全局配置信息。具体请参考[module.json5配置文件](module-configuration-file.md)。
  + **build-profile.json5：**当前的模块信息、编译信息配置项，包括buildOption、targets配置等。
  + **hvigorfile.ts**：模块级编译构建任务脚本。
  + **oh-package.json5**：描述三方包的包名、版本、入口文件（类型声明文件）和依赖项等信息。
* **oh\_modules**：用于存放三方库依赖信息，包含应用/元服务所依赖的第三方库文件。
* **build-profile.json5：**应用级配置信息，包括签名、产品配置等。
* **hvigorfile.ts：**应用级编译构建任务脚本。
* **oh-package.json5：**描述全局配置，如依赖覆盖（overrides）、依赖关系重写（overrideDependencyMap）和参数化配置（parameterFile）等。

## C++工程目录结构

工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/3hbr0UFgQBS4jc2wFem9EQ/zh-cn_image_0000002779728789.png "点击放大")

* **entry**：应用/元服务模块，编译构建生成一个HAP。
  + **src > main > cpp > types**：用于存放C++的API接口描述文件。
  + **src > main > cpp > types** **> libentry > Index.d.ts**：描述C++ API接口行为，如接口名、入参、返回参数等。
  + **src > main > cpp > types** **> libentry> oh-package.json5**：配置.so三方包声明文件的入口及包名。
  + **src > main > cpp > CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。
  + **src > main > cpp > napi\_init.cpp：**定义C++ API接口的文件**。**
  + **src > main > ets：**用于存放ArkTS源码。
  + **src > main > resources：**用于存放应用所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件的详细说明请参考[资源分类与访问](resource-categories-and-access.md)。

    | 资源目录 | 资源文件说明 |
    | --- | --- |
    | base>element | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如：  - boolean.json：布尔型 - color.json：颜色 - float.json：浮点型 - intarray.json：整型数组 - integer.json：整型 - pattern.json：样式 - plural.json：复数形式 - strarray.json：字符串数组 - string.json：字符串值 |
    | base>media | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 |
    | rawfile | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。 |
  + **src > main > module.json5：**模块配置文件，主要包含HAP的配置信息、应用/元服务在具体设备上的配置信息，以及应用/元服务的全局配置信息。具体请参考[module.json5配置文件](module-configuration-file.md)。
  + **build-profile.json5：**当前的模块信息、编译信息配置项，包括buildOption、targets配置等。
  + **hvigorfile.ts：**模块级编译构建任务脚本。
* **build-profile.json5：**应用级配置信息，包括签名、产品配置等。
* **hvigorfile.ts**：应用级编译构建任务脚本。
