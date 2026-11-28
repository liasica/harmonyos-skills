---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:26+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:95823869971926a1614dca9481803a6d6d05db37e39c193c7855963d9b9d20b2
---

DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

**说明** 

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* 集成态HSP：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名。

## 使用约束

* HSP及其使用方都必须是API 10及以上版本Stage模型。
* HSP及其使用方都必须使用[模块化编译](ide-hvigor-esmodule-compile.md)模式。
* 从DevEco Studio 6.0.1 Beta1开始，创建HSP模块时支持选择C++版本。

## 创建HSP模块

1. 通过如下两种方法，在工程中添加新的Module。
   * 方法1：鼠标移到工程目录顶部，单击鼠标右键，选择**New > Module**，开始创建新的Module。
   * 方法2：选中工程目录中任意文件，然后在菜单栏选择**File > New > Module**，开始创建新的Module。
2. 模板类型选择**Shared Library**，点击**Next**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/GfbytlsNQKi4Rih3_C91fw/zh-cn_image_0000002808766405.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=80D9D0289C15E3BC4CE02DE7908A1B5AE647F63F58C1FA431968D8E2DB85EBF4)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。
   * **Module name**：新增模块的名称，如设置为library。
   * **Device type**：支持的设备类型。
   * **Enable native**：是否创建一个用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。从DevEco Studio 6.0.1 Beta1开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/8Ce8FogTTzya2zL6CTHxpg/zh-cn_image_0000002808886485.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=C145B872D0FB43265C9435C3210FFC845A6BD5FA5FD4EDD5C55811DA8C562055)

   创建完成后，会在工程目录中生成HSP模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/cFDB4g6UTxmI3tm7qeUG_g/zh-cn_image_0000002779406848.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC1CA206EEFDB020D2F61387C65164C012B3B1C5E5B9AE0A8D4A9B5AC6BD095F)

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp.md)开发完HSP模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/87GjaNCFRVCE1Y0VAaZ2iA/zh-cn_image_0000002808766403.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABD6837ED143E6FF157EF2D20C69D4D23336F483C39EED551DC97DE909C5D907)

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/QsPRxC64QVebPAzWlC9OGA/zh-cn_image_0000002808886487.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=542CE352439A63075F231E9DD3C810388BFAAAD3F8B19F3D7D41E6187352E9C3)
