---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp
title: 开发动态共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发及发布共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb568d3f23ec3ed35d0f8b775df52c93d184e062ef68bb2b31895001addc4de4
---

DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

说明

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* 集成态HSP：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名。

## 使用约束

* HSP及其使用方都必须是API 10及以上版本Stage模型。
* HSP及其使用方都必须使用[模块化编译](ide-hvigor-esmodule-compile.md)模式。
* 从DevEco Studio 6.0.1 Beta1开始，创建HSP模块时支持选择C++版本。

## 开发动态共享包

### 创建HSP模块

1. 通过如下两种方法，在工程中添加新的Module。
   * 方法1：鼠标移到工程目录顶部，单击鼠标右键，选择**New > Module**，开始创建新的Module。
   * 方法2：选中工程目录中任意文件，然后在菜单栏选择**File > New > Module**，开始创建新的Module。
2. 模板类型选择**Shared Library**，点击**Next**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/dvg1WrZXRgO-YEl6uMHNww/zh-cn_image_0000002561832851.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=58576B932B7C23DE525B2510E7E1B23C3E168A9AA5CF2A169F980D3913F10967)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。从DevEco Studio 6.0.1 Beta1开始，支持选择C++版本。
   * **Module name**：新增模块的名称，如设置为library。
   * **Device type**：支持的设备类型。
   * **Enable native**：是否创建一个用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/XuRb3AEyRbKPa0_R2cmKDg/zh-cn_image_0000002530912920.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=30FFA09810BB00F1450169B5415F39EEE99C97841EFB2978C0A0F1A457DACC2F)

   创建完成后，会在工程目录中生成HSP模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/M66PCWbSTYyjGqFdlpfJIw/zh-cn_image_0000002530752918.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=110BB121901B8714F2D963104AD6699B29265D552518A0BB812ACE186CBC0DA5)

### 编译HSP模块

说明

如果HSP未开启[混淆](ide-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp.md)开发完HSP模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/lpEtBm4QQXq3NHjJFD_5Ow/zh-cn_image_0000002530912916.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=A5C64EAE68C41D3D2C98B5474A915D4BC3BEB30C6FBDD78D414118CA0DBCE823)

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/bQuDqbZnT_Og5tXWnkS-Yw/zh-cn_image_0000002530912922.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=0D1F4B0DAAEAA9606C110B905563F2B8EDFB8546672221604FD16ACC0B980CB1)

如需在应用内共享HSP，请将HSP共享包上传至私仓（请参考[将三方库发布到 ohpm-repo](ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_从ohpm-repo获取三方库)），请先按以下操作编译生成\*.tgz包。

1. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/v150jsifT-WQktGyFy_S6w/zh-cn_image_0000002530912906.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=61616C9F3CBD86F1DC4FC96C16D31D700C687E91F63342902F7C92F119C60375)图标将编译模式切换成release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MNQdtfIJTiyBNSredZbaPQ/zh-cn_image_0000002530752914.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=C4208596FDA9FBDAB00472E048EC20633606512F9294F4E7892360AEFB7054BB)
2. 选中HSP模块的根目录，点击**Build > Make Module ${libraryName}**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/KXO2dOkGTHWfxo7Qrs-8eA/zh-cn_image_0000002561832835.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=93D388187819393EAFE0A1F1722E6AF0B3757F49EEF584DF29D5C38646246945)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/nMezvcg1S2mycRHTe3Wrog/zh-cn_image_0000002530752934.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=8C835BA86D39F068A30C976AEC78DF6C9FD477C67D82EE33E355E16043DDC839)
