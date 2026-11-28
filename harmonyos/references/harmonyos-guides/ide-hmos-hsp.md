---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:49+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:380aaf96c19fc2943359299acdb24981b79cf15ac550be4f61b8a7d1803b9060
---

鸿蒙电脑DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

**说明** 

HSP只支持在应用内共享，不支持跨应用共享。

HSP及其使用方都必须使用[模块化编译](ide-hmos-hvigor-esmodule-compile.md)模式。

## 创建HSP模块

1. 点击菜单栏选择**新建 > 模块**，在工程中添加模块。
2. 模板类型选择**Shared Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/J1fidYj2QuqhLqqeSj0Flg/zh-cn_image_0000002820685367.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FA3D12E93766118BE58D1018F6FF14BB0815DA4F518578C2C878D0CA760F605 "点击放大")
3. 在**模块信息**界面中，设置新添加的模块信息，设置完成后，单击**确认**完成创建。
   * **模块名**：新增模块的名称，如设置为sharedlibrary。
   * **设备类型**：支持的设备类型。
   * **Enable Native**：是否创建一个用于调用C++代码的模块，勾选表示创建，未勾选表示不创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/96CcR_tFSZGCUvuEyM5-2Q/zh-cn_image_0000002792005658.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9D59A44A6ADD3AE6C8BA72AB9CDD9A832812B266551FA464C769D03E9EC393B "点击放大")

   创建完成后，会在工程目录中生成库模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/xdEI4QojT0SBNDKmteQjIQ/zh-cn_image_0000002792000870.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=B09D986F79417180144BF06C5FEED551FF45FE70B8817CFC5A7B9E93C0F640B9 "点击放大")

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-hmos-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](../doccenter-getting-started/in-app-hsp.md)开发完库模块后，选中模块名，然后通过鼠标右键点击**构建****模块**，进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/ChyqDsc2TXK0kiN-i--gig/zh-cn_image_0000002820680837.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FC6C37CBC8D996BA5B3CFFDEC4AC962B0B6ADD53C7C5AC8E3733B118F8EA105 "点击放大")

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/fYaI-c0DSiG8xOaQzXXJhw/zh-cn_image_0000002820720845.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=15F150BC922C2CDA1625E90820CB2910B3C0CB102B0A3B27070DF3F6EFED91AE "点击放大")
