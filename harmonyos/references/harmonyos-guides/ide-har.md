---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har
title: 开发静态共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发及发布共享包 > 开发静态共享包
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:34daa81dab01dd696f1aa3fc416c950a552b623a849f36b4557fd7c9786c641f
---

HAR（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不同于HAP，不能独立安装运行在设备上，只能作为应用模块的依赖项被引用。

本文将介绍如何创建HAR模块、如何编译共享包。接下来，将简单介绍HAR模块的工程结构，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/SlAapUJcTBC5RWLsABXrlg/zh-cn_image_0000002530753276.png?HW-CC-KV=V1&HW-CC-Date=20260427T235436Z&HW-CC-Expire=86400&HW-CC-Sign=0F0F3592E81F49E13B5912D5B1B3B9B8E3CF62D7A93D9BF0168998FE4ABF9A03)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/fyM3xpNWTQKCzEI6PD1gtg/zh-cn_image_0000002561753217.png?HW-CC-KV=V1&HW-CC-Date=20260427T235436Z&HW-CC-Expire=86400&HW-CC-Sign=4BB16CD31D4266E8725B909B241EC99F2E600EDEF33F72EF42E2575E04397E5E)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。从DevEco Studio 6.0.1 Beta1开始，支持选择C++版本。
   * **Module name**：新增模块的名称。
   * **Device type**：支持的设备类型。
   * **Enable native**：创建用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/kVYDetMxT0CJCwhguTD6PQ/zh-cn_image_0000002561753209.png?HW-CC-KV=V1&HW-CC-Date=20260427T235436Z&HW-CC-Expire=86400&HW-CC-Sign=A979E3E52B1E1C57CA6D31A37971EEA6B444BF92B9B83321541786D932A93362)

   创建完成后，会在工程目录中生成HAR模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/6T6F9Yp8SyidhsWJUxbFXQ/zh-cn_image_0000002530753274.png?HW-CC-KV=V1&HW-CC-Date=20260427T235436Z&HW-CC-Expire=86400&HW-CC-Sign=2C8CE0B11F63E0F6054D0717E6F598011C3106707B78946D08625470A6CD499F)

## 编译HAR模块

开发完HAR模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HAR。HAR可供工程其他模块引用，或将HAR上传至ohpm仓库，供其他开发者下载使用。若部分源码文件不需要打包至HAR中，可通过[创建.ohpmignore文件](ide-hvigor-build-har.md#li5533646204511)，配置打包时要忽略的文件/文件夹。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/BEmrjTFTTL2IAFoFHGSgCQ/zh-cn_image_0000002530753272.png?HW-CC-KV=V1&HW-CC-Date=20260427T235436Z&HW-CC-Expire=86400&HW-CC-Sign=BC85E3FCC40C5E7FC64176CD2D29C5AEA6118C9FEE855E9959F3C6511867687F)

编译构建的HAR可在模块下的build目录下获取，包格式为\*.har。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/c4wGEeL5S4Ox_RtbkBfvDg/zh-cn_image_0000002561753215.png?HW-CC-KV=V1&HW-CC-Date=20260427T235436Z&HW-CC-Expire=86400&HW-CC-Sign=31F55BB74971376692ED1D5213F88D3825DF41FD653B749A69C30C9272119807)

在编译构建HAR时，请注意以下事项：

* 编译构建HAR的过程中，不会将模块中的C++代码直接打包进.har文件中，而是将C++代码编译成动态依赖库.so文件放置在.har文件中的libs目录下。
* 在编译构建HAR的过程中，会生成资源文件ResourceTable.txt，以便编辑器可以对HAR中的资源文件进行联想。因此，如果不使用DevEco Studio对HAR进行构建，则DevEco Studio的编辑器会无法联想HAR中的资源。
* 如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，会将dependencies内处于本模块路径下的本地依赖也打包进.har文件中；如果在打包后发现缺少部分本地依赖（如cpp/types目录），请参见[FAQ](../harmonyos-faqs/faqs-compiling-and-building-23.md)。
