---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:04+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:36cc74b82de5643c483fec8b25b8df103c6e28a17d9904c88aeca13bd3f0b883
---

鸿蒙电脑DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

**说明** 

HSP只支持在应用内共享，不支持跨应用共享。

HSP及其使用方都必须使用[模块化编译](ide-hmos-hvigor-esmodule-compile.md)模式。

## 创建HSP模块

1. 点击菜单栏选择**新建 > 模块**，在工程中添加模块。
2. 模板类型选择**Shared Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/9Z2k_XYkSj2klW7i7gWKrA/zh-cn_image_0000002779728767.png "点击放大")
3. 在**模块信息**界面中，设置新添加的模块信息，设置完成后，单击**确认**完成创建。
   * **模块名**：新增模块的名称，如设置为sharedlibrary。
   * **设备类型**：支持的设备类型。
   * **Enable Native**：是否创建一个用于调用C++代码的模块，勾选表示创建，未勾选表示不创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/zerkl5WCTYGtrofVt7dfYg/zh-cn_image_0000002750009704.png "点击放大")

   创建完成后，会在工程目录中生成库模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/v1IITNy_TZ2eneWLC8oWvw/zh-cn_image_0000002750169592.png "点击放大")

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-hmos-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp.md)开发完库模块后，选中模块名，然后通过鼠标右键点击**构建****模块**，进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/1269NzqeSx26_h9OKOI82Q/zh-cn_image_0000002750169590.png "点击放大")

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/wbMIffOYT7iVybF7eC7S8g/zh-cn_image_0000002779608617.png "点击放大")
