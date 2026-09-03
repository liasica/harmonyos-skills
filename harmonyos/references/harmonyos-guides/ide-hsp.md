---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp
title: 开发动态共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:04+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:c374810b72e0ce2a354d48c8351dfcab5efd895d6a0437c038c68177857a3ce8
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/OcNg0LvVTRqCld56UT85Kw/zh-cn_image_0000002731382245.png)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。
   * **Module name**：新增模块的名称，如设置为library。
   * **Device type**：支持的设备类型。
   * **Enable native**：是否创建一个用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。从DevEco Studio 6.0.1 Beta1开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/_ee13dD3Tg2UImaPi0khCg/zh-cn_image_0000002701822944.png)

   创建完成后，会在工程目录中生成HSP模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/6NDl590wQXKeEyEpgWaHGQ/zh-cn_image_0000002701663014.png)

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp.md)开发完HSP模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/TjqaeRO-QhuxvEMogkIH-g/zh-cn_image_0000002701822942.png)

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_LuCfXDVQs2IvL0xnAObZg/zh-cn_image_0000002701663016.png)

如需在应用内共享HSP，请将HSP共享包上传至私仓（请参考[将三方库发布到 ohpm-repo](ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_从ohpm-repo获取三方库)），请先按以下操作编译生成\*.tgz包。

1. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Iios5i5ySjWOm3VokpJ1yg/zh-cn_image_0000002731542213.png)图标将编译模式切换成release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/UMLZ6FRLT2-8Nn15ZeeZng/zh-cn_image_0000002701663024.png)
2. 选中HSP模块的根目录，点击**Build > Make Module ${libraryName}**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/1LRP1nnJRC6JOKdgPOsLRg/zh-cn_image_0000002731542221.png)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/Z2Li4NInTgeRbY_ZHjnfjw/zh-cn_image_0000002701822936.png)
