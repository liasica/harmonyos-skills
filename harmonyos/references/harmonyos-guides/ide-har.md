---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har
title: 开发静态共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 开发静态共享包
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d6ed2d7bb3c98c78686124908705847c9ed16acdc147bbfb3984e9a43d258a85
---

[HAR（Harmony Archive）](har-package.md)是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或工程共享ArkUI组件、资源等相关代码。HAR不同于HAP，不能独立安装运行在设备上，只能作为应用模块的依赖项被引用。本文将介绍如何创建HAR模块、如何编译共享包。

HAR模块的工程结构如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/qhuOkL-RQg6sviNmumEqzw/zh-cn_image_0000002701663400.png)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/mOrFUIj4SwmFuq_Q-BthyA/zh-cn_image_0000002731382619.png)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。
   * **Module name**：新增模块的名称。
   * **Device type**：支持的设备类型。
   * **Enable native**：创建用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14，仅打开Enable native时需要配置。从DevEco Studio 6.0.1 Beta1开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/tYQc32QgSo-ueVrZYcbQlA/zh-cn_image_0000002701823316.png)

   创建完成后，会在工程目录中生成HAR模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/g2fd_55hQgWo-v95U-YfzA/zh-cn_image_0000002701663392.png)

## 编译HAR模块

开发完HAR模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HAR。HAR可供工程其他模块引用，或将HAR上传至ohpm仓库，供其他开发者下载使用。更多使用说明请参考[构建HAR](ide-hvigor-build-har.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/bWKP1fXwQ_2BU_82F9RjsQ/zh-cn_image_0000002731382613.png)

编译构建的HAR可在模块下的build目录下获取，包格式为\*.har。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/tLUHEbS6QFWU9AqYGuJzUw/zh-cn_image_0000002731542587.png)

在编译构建HAR时，请注意以下事项：

* 编译构建HAR的过程中，不会将模块中的C++代码直接打包进.har文件中，而是将C++代码编译成动态依赖库.so文件放置在.har文件中的libs目录下。
* 在编译构建HAR的过程中，会生成资源文件ResourceTable.txt，以便编辑器可以对HAR中的资源文件进行联想。因此，如果不使用DevEco Studio对HAR进行构建，则DevEco Studio的编辑器会无法联想HAR中的资源。
* 如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，会将dependencies内处于本模块路径下的本地依赖也打包进.har文件中，如果在打包后发现缺少部分本地依赖（如cpp/types目录）请参见[FAQ](../harmonyos-faqs/faqs-compiling-and-building-23.md)。
