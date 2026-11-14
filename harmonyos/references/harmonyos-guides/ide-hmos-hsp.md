---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hsp
title: 开发动态共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:11+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1b656a749283adb309c531042e730958ffd94c98ceeae812f088cf0d2e345fea
---

鸿蒙电脑DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

**说明** 

HSP只支持在应用内共享，不支持跨应用共享。

HSP及其使用方都必须使用[模块化编译](ide-hmos-hvigor-esmodule-compile.md)模式。

## 创建HSP模块

1. 点击菜单栏选择**新建 > 模块**，在工程中添加模块。
2. 模板类型选择**Shared Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/tMn1VqCBRZm6xIPpNpCLfA/zh-cn_image_0000002781311124.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=051B3086C78FE3DBEEE09D391EA487699AA9CB516C22CB69E592608DA191FBF0 "点击放大")
3. 在**模块信息**界面中，设置新添加的模块信息，设置完成后，单击**确认**完成创建。
   * **模块名**：新增模块的名称，如设置为sharedlibrary。
   * **设备类型**：支持的设备类型。
   * **Enable Native**：是否创建一个用于调用C++代码的模块，勾选表示创建，未勾选表示不创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/TqkYSzMdRxaI4n9KKzfIkg/zh-cn_image_0000002810750719.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=458D7C08D78026C1E4CE8F38EF6B9A70206CE37BAEB0BC9254A8D30B65CBC446 "点击放大")

   创建完成后，会在工程目录中生成库模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/1mKikTcIQAyqLnvbN1kO7w/zh-cn_image_0000002810750721.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=379BC4CEB15E0F27C684FB9F5E2ACF0F65E0FCA67C5A2AC383757D1B55EF6BEA "点击放大")

## 编译HSP模块

**说明** 

如果HSP未开启[混淆](ide-hmos-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](../doccenter-getting-started/in-app-hsp.md)开发完库模块后，选中模块名，然后通过鼠标右键点击**构建****模块**，进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/5HqvdA5vS3WnCNuNMD3NZg/zh-cn_image_0000002781471058.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=23C37BE35FAE59EDD6F024F073DB1AD7C48BB1ED671D29B73179AC23E10A0D3F "点击放大")

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ti4YqjFsSJ2PPhgfsRr4GQ/zh-cn_image_0000002810630613.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=30EFB02291823B00053C1C682219165A7C27E9F0AE87F75218D2792DF027980F "点击放大")
