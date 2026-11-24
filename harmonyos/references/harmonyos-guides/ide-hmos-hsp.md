---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:28ece640ba686e980fc928fb24a2cd382897d1f16b2b9ec2d01dbb3a49c1524d
---

鸿蒙电脑DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

**说明** 

HSP只支持在应用内共享，不支持跨应用共享。

HSP及其使用方都必须使用[模块化编译](ide-hmos-hvigor-esmodule-compile.md)模式。

## 创建HSP模块

1. 点击菜单栏选择**新建 > 模块**，在工程中添加模块。
2. 模板类型选择**Shared Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/IesHLsR4ST-6AoZHGzNDOw/zh-cn_image_0000002820685367.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=72F09C2E5D83FE48B6F256AEA4913D5A2A77EDAA1244E304E2C17E2245470B08 "点击放大")
3. 在**模块信息**界面中，设置新添加的模块信息，设置完成后，单击**确认**完成创建。
   * **模块名**：新增模块的名称，如设置为sharedlibrary。
   * **设备类型**：支持的设备类型。
   * **Enable Native**：是否创建一个用于调用C++代码的模块，勾选表示创建，未勾选表示不创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/UZ-3q8eIQeGc902746Z0RA/zh-cn_image_0000002792005658.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFAC0A66351B8C435B5713E03D587A8A5E2420CE1408362DD13A2B5CF125B00B "点击放大")

   创建完成后，会在工程目录中生成库模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/y4xca3LWR1mLZep2910dYA/zh-cn_image_0000002792000870.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E17913AF0788163E0068E5F6249799601008E3948CFB39B18281A65580F3702 "点击放大")

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-hmos-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](../doccenter-getting-started/in-app-hsp.md)开发完库模块后，选中模块名，然后通过鼠标右键点击**构建****模块**，进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/qJwDp6HITy2ZyIXhbHCjkQ/zh-cn_image_0000002820680837.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=E25AC8CB9DF307E50C1DDC4212162F6DD98B231A0BD70110674D7C6C1642EB2C "点击放大")

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/XIdY7bi_TI-i9X9lqelXZQ/zh-cn_image_0000002820720845.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3BB4A5A943FC7C30C13EC657056C9E857B0CA8095C3DB57DE68DB0A09811527 "点击放大")
