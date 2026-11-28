---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har
title: 开发静态共享包
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 开发静态共享包
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:26+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4abfcd17db1a8f41883cd7d3f0bb86ee6dd5176ea15caf0bd9ad8808647ae8ed
---

[HAR（Harmony Archive）](har-package.md)是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或工程共享ArkUI组件、资源等相关代码。HAR不同于HAP，不能独立安装运行在设备上，只能作为应用模块的依赖项被引用。本文将介绍如何创建HAR模块、如何编译共享包。

HAR模块的工程结构如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/wfJG90OaQJeYnxMg85Fwng/zh-cn_image_0000002779407174.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A13FC0BE5EC663E6BDCC5B864E1EAD163A6313919E7F849D0F82C51EB2474EC)

相关字段的描述如下，其余字段与Entry或Feature模块相关字段相同，可参考[工程介绍](ide-project-overview.md)。

* **libs**：用于存放.so文件。
* **src > main > cpp > types**：用于存放C++ API描述文件，子目录按照so维度进行划分。
* **src > main > cpp > types** **> liblibrary > Index.d.ts**：描述C++接口的方法名、入参、返回参数等信息。
* **src > main > cpp > types** **> liblibrary > oh-package.json5**：描述so三方包声明文件入口和so包名信息。
* **src > main > cpp >** **CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。
* **src > main > cpp > napi\_init.cpp**：共享包C++代码源文件。
* **Index.ets**：共享包导出声明的入口。

从DevEco Studio 6.0.1 Beta1开始，创建HAR模块时支持选择C++版本。

## 创建HAR模块

1. 鼠标移到工程目录顶部，单击右键，选择**New > Module**，在工程中添加模块。
2. 在**Choose Your Ability Template**界面中，选择**Static Library**，并单击**Next**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/ViNBR8kGQtC60H0Sy3leAA/zh-cn_image_0000002808766731.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F29EF116A2AA5830455FD5E635048F6BD9D45FA5CC9741B20EE68BEF511ED5C)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。
   * **Module name**：新增模块的名称。
   * **Device type**：支持的设备类型。
   * **Enable native**：创建用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14，仅打开Enable native时需要配置。从DevEco Studio 6.0.1 Beta1开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/bN7cD_wqSK6wHQufgynmEw/zh-cn_image_0000002779407170.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBD3631B0BA767A8203A5C0E658D45590BB6D6F896DC00A095DE77569D0B1907)

   创建完成后，会在工程目录中生成HAR模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/_QTxm3OaTk6FCG4nORHb9Q/zh-cn_image_0000002779567152.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=44E100F4694DC69DFA5C40ECFE7725F014C9BC23A2BD27B32FDE75C9C4E32254)

## 编译HAR模块

开发完HAR模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HAR。HAR可供工程其他模块引用，或将HAR上传至ohpm仓库，供其他开发者下载使用。更多使用说明请参考[构建HAR](ide-hvigor-build-har.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/nywfVN3eQyuGKtoBCvxC6Q/zh-cn_image_0000002808766735.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=256630D345D5BFCC0C25E68B092343CBF8DBA381922271A69496E62FCEF6DB22)

编译构建的HAR可在模块下的build目录下获取，包格式为\*.har。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/4WnW3S3TTfWAKDkY7dd0pw/zh-cn_image_0000002808886815.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=612D596041823A1C5B482B3B8AC187933C5718206B618D2C79402E8858D81600)

在编译构建HAR时，请注意以下事项：

* 编译构建HAR的过程中，不会将模块中的C++代码直接打包进.har文件中，而是将C++代码编译成动态依赖库.so文件放置在.har文件中的libs目录下。
* 在编译构建HAR的过程中，会生成资源文件ResourceTable.txt，以便编辑器可以对HAR中的资源文件进行联想。因此，如果不使用DevEco Studio对HAR进行构建，则DevEco Studio的编辑器会无法联想HAR中的资源。
