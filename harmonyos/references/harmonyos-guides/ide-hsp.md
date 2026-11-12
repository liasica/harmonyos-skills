---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:28a7ff2c5fffe0bc97cf638cfd8fd37dda55e342616919207bbb1e79ffc52f86
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/dlzC1rNBT76Y7v0sQBwuUw/zh-cn_image_0000002808766405.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9344164B1421F8624427402F77516D6510560FED3A5B281EA4BD4DE584CC0394)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。
   * **Module name**：新增模块的名称，如设置为library。
   * **Device type**：支持的设备类型。
   * **Enable native**：是否创建一个用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。从DevEco Studio 6.0.1 Beta1开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/w9tuIyHESi-ZFN9BefBFrA/zh-cn_image_0000002808886485.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC1274B1389848676C200CED189AC40B3DF41364A500C23C24F7707589C8D375)

   创建完成后，会在工程目录中生成HSP模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/ZPAKjeG2RjKx8NC8lniKdg/zh-cn_image_0000002779406848.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E29C19F39FF043E09A2D5C1F3D96139F0C6798178415C4B7B911D82D277AF6C)

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp.md)开发完HSP模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/MO-Nq_MfTCWbdNX2_L8L8Q/zh-cn_image_0000002808766403.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6714970133FB73418FCCDF8825F270D42B5B08521D746B191E4624CB42729F86)

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/u5sTI2s-R3CG4YrpuoOUJw/zh-cn_image_0000002808886487.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=37F2536E2B1C7DB874BE4870D11456EFD64C775F573C657C8585DA88A5627846)
