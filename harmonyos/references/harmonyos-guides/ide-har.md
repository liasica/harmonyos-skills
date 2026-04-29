---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har
title: 开发静态共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发及发布共享包 > 开发静态共享包
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:35+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b68451aef1b4a9d534201a76cd18cc3eeb8e0cdf6c0566239cdce16d60301091
---

HAR（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不同于HAP，不能独立安装运行在设备上，只能作为应用模块的依赖项被引用。

本文将介绍如何创建HAR模块、如何编译共享包。接下来，将简单介绍HAR模块的工程结构，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/7htw62nBTzW6kPcRK7SSpA/zh-cn_image_0000002530753276.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=FF40DB9069785FEBCA3BC89BB7D952B3919C1F1B13D658792BAEEAFC9CA4F1F7)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/qXaH6uHVRTGxJxMU2FY1bQ/zh-cn_image_0000002561753217.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=0F6CB893D00BDEEF4ED844387AB16C8661BE7FD6163BF48DD647271F6D4FB445)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。从DevEco Studio 6.0.1 Beta1开始，支持选择C++版本。
   * **Module name**：新增模块的名称。
   * **Device type**：支持的设备类型。
   * **Enable native**：创建用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/3cKZxUg7SVaF2AiNRoqVrw/zh-cn_image_0000002561753209.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=8515EFCC212680424E3C3F2E6C54FB8CE8FE2C3E89D5E6C5194A83D292226B0D)

   创建完成后，会在工程目录中生成HAR模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/9iTi_9cASUiGZmvDyrBYnw/zh-cn_image_0000002530753274.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=9533DED285E0D9AB3D1E9FCAA0D1754ED5CCD94A9DC692C51B593D48F72E9D8B)

## 编译HAR模块

开发完HAR模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HAR。HAR可供工程其他模块引用，或将HAR上传至ohpm仓库，供其他开发者下载使用。若部分源码文件不需要打包至HAR中，可通过[创建.ohpmignore文件](ide-hvigor-build-har.md#li5533646204511)，配置打包时要忽略的文件/文件夹。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/nH0mfrOORv6_McKvauK-0Q/zh-cn_image_0000002530753272.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=C6F93C964DB5280D1BD01D3510E7FC6D30A1DBEE3B5C1C740872491E18DF107B)

编译构建的HAR可在模块下的build目录下获取，包格式为\*.har。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/fHigVYarS3Skuulb9n_vZw/zh-cn_image_0000002561753215.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=A4DC3574BC0E6720DC13BCDBEC736A75CBA62C22306D1C3641D67B718CDD3253)

在编译构建HAR时，请注意以下事项：

* 编译构建HAR的过程中，不会将模块中的C++代码直接打包进.har文件中，而是将C++代码编译成动态依赖库.so文件放置在.har文件中的libs目录下。
* 在编译构建HAR的过程中，会生成资源文件ResourceTable.txt，以便编辑器可以对HAR中的资源文件进行联想。因此，如果不使用DevEco Studio对HAR进行构建，则DevEco Studio的编辑器会无法联想HAR中的资源。
* 如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，会将dependencies内处于本模块路径下的本地依赖也打包进.har文件中；如果在打包后发现缺少部分本地依赖（如cpp/types目录），请参见[FAQ](../harmonyos-faqs/faqs-compiling-and-building-23.md)。
