---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:46+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dd5b01908d26d030ba3f47b7b190f9a1adc2a03fcd7047533f9c5c92be1ff5e2
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/j8kRJKIQT9aiwHgvgSnIuw/zh-cn_image_0000002808766405.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=8DFB2BEFA6B7CB58F39739A250C9EFBAC609FB07EB1FBA4A4F8C287817C84C26)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。
   * **Module name**：新增模块的名称，如设置为library。
   * **Device type**：支持的设备类型。
   * **Enable native**：是否创建一个用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。从DevEco Studio 6.0.1 Beta1开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/o7fzfDfQSHuxnNRgRHeC8g/zh-cn_image_0000002808886485.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=65CD133991A6B3B8524F0CC1CEC503884862DA5866C16D5522506222CC1B3892)

   创建完成后，会在工程目录中生成HSP模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/GSWZeunRSCyabpLlHuRI0Q/zh-cn_image_0000002779406848.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EEB8898CAAFB7341C27E3FF1D3F639803FBBD33CA983870B6D0254E96E9DEA6)

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp.md)开发完HSP模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/_zAq2IJtS5iO_zwqDFWseA/zh-cn_image_0000002808766403.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=433F1355EC7B256441B604E3B3D81D36AF8F942BB91D16F1F9A7E36A39B2AB46)

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/xwt7kRJSRsyoCZHJmKTNLw/zh-cn_image_0000002808886487.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=20C07BC34F2892536FF58837CEE5671901840E8FE539D5E58F68E8FC842BEB7F)
