---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-har
title: 开发静态共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 开发静态共享包
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:962f6bdb24c20db7a94fee5e176f8ad67ec68840c68610483a0bdb5a480a2d8a
---

HAR（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不同于HAP，不能独立安装运行在设备上，只能作为应用模块的依赖项被引用。

接下来，将简单介绍库模块的工程结构，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/SucD0HjNTT-M7xFSTGmAvg/zh-cn_image_0000002749483906.png "点击放大")

相关字段的描述如下，其余字段与Entry或Feature模块相关字段相同，可参考[C++工程目录结构](ide-hmos-project-structure.md#section181711599584)。

* **libs**：用于存放.so文件。
* **src > main > cpp > types**：用于存放C++ API描述文件，子目录按照so维度进行划分。
* **src > main > cpp > types** **> liblibrary > Index.d.ts**：描述C++接口的方法名、入参、返回参数等信息。
* **src > main > cpp > types** **> liblibrary > oh-package.json5**：描述so三方包声明文件入口和so包名信息。
* **src > main > cpp >** **CMakeLists.tx****t**：CMake配置文件，提供CMake构建脚本。
* **src > main > cpp > napi\_init.cpp**：共享包C++代码源文件。
* **Index.ets**：共享包导出声明的入口。

本文将介绍如何创建库模块、如何编译共享包、如何引用共享包资源，以及如何发布共享包。

## 创建HAR模块

1. 点击菜单栏选择**新建 > 模块**，在工程中添加模块。
2. 在**新建模块**界面中，选择**Static Library。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/793fXXTpRZCBD0Yby7OgkQ/zh-cn_image_0000002778923123.png "点击放大")
3. 在**模块信息**界面中，设置新添加的模块信息，设置完成后，单击**确认**完成创建。
   * **模块名**：新增模块的名称。
   * **设备类型**：支持的设备类型。
   * **Enable Native**：是否创建一个用于调用C++代码的模块，勾选表示创建，未勾选表示不创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/D-ib5729QTueLH66V0pOVA/zh-cn_image_0000002749483904.png "点击放大")

   创建完成后，会在工程目录中生成库模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/s31C_uToS0CBoOWRCEHNNQ/zh-cn_image_0000002749324032.png "点击放大")

## 编译HAR模块

开发完库模块后，选中模块名，然后通过鼠标右键，点击**构建模块**，生成HAR。

HAR可用于工程其它模块的引用，或将HAR上传至ohpm仓库，供其他开发者下载使用。若部分源码文件不需要打包至HAR中，可通过[创建.ohpmignore文件](ide-hmos-hvigor-build-profile.md#section1744183710558)，配置打包时要忽略的文件/文件夹。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/AX1g9sgEQ6-qcG5R-cfycw/zh-cn_image_0000002778923121.png "点击放大")

编译构建的HAR可在模块下的build目录下获取，包格式为\*.har。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/UsAav6jXRKWEtb0ddIsUbg/zh-cn_image_0000002779082971.png "点击放大")

在编译构建HAR时，请注意以下事项：

* 编译构建HAR的过程中，不会将模块中的C++代码直接打包进.har文件中，而是将C++代码编译成动态依赖库.so文件放置在.har文件中的libs目录下。
* 在编译构建HAR的过程中，会生成资源文件ResourceTable.txt，以便编辑器可以对HAR中的资源文件进行联想。因此，如果不使用鸿蒙电脑DevEco Studio对HAR进行构建，则DevEco Studio的编辑器会无法联想HAR中的资源。
