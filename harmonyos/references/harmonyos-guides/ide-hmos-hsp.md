---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:33+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:b36030f39c6ed5a6d27fca9c250280926d80528723e90a3d1d18ebb22ed6c271
---

鸿蒙电脑DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

**说明** 

HSP只支持在应用内共享，不支持跨应用共享。

HSP及其使用方都必须使用[模块化编译](ide-hmos-hvigor-esmodule-compile.md)模式。

## 创建HSP模块

1. 点击菜单栏选择**新建 > 模块**，在工程中添加模块。
2. 模板类型选择**Shared Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/N4qeuKKoQsCbQEWKd_l7ew/zh-cn_image_0000002781311124.png "点击放大")
3. 在**模块信息**界面中，设置新添加的模块信息，设置完成后，单击**确认**完成创建。
   * **模块名**：新增模块的名称，如设置为sharedlibrary。
   * **设备类型**：支持的设备类型。
   * **Enable Native**：是否创建一个用于调用C++代码的模块，勾选表示创建，未勾选表示不创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/gQj-2cQIRS6zP0-onCT2aw/zh-cn_image_0000002810750719.png "点击放大")

   创建完成后，会在工程目录中生成库模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/mZ6VDFVbReO6VJrkCHFyJA/zh-cn_image_0000002810750721.png "点击放大")

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-hmos-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp-0000001774119898.md)开发完库模块后，选中模块名，然后通过鼠标右键点击**构建****模块**，进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/-cy7Fi87SWGr7uJm8qwKFA/zh-cn_image_0000002781471058.png "点击放大")

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/kQ5nJLCcQaCsjk5ZZk1OXg/zh-cn_image_0000002810630613.png "点击放大")
