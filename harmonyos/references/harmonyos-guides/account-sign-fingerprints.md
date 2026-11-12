---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e569e9a8313a927b425c9c3e6e34f355d8bea9cfd33d1a98cb8689604816c1a5
---

请参考“[应用开发准备](application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息。针对开发调试场景，从DevEco Studio 26.0.0 Beta2版本开始，新增了更高效的自动签名方案，开发者可以选择以下其中一种方式进行调试阶段的应用签名。

   * [自动签名](ide-signing-auto.md)：

     应用运行的HarmonyOS系统版本低于HarmonyOS 6.0.0(20)时，仅未成年人模式接口支持自动签名。

     应用运行的HarmonyOS系统版本为HarmonyOS 6.0.0(20)及以上时，所有接口均支持使用自动签名方式进行配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/OxMCaL4-RIiABLlZa_Wgyw/zh-cn_image_0000002786520060.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E66A402FDFC15BA3FB2C57D68BBEBB18EDE1D255D8ED730472C4C6ABD7DB5D5)
   * [手动签名](ide-signing-manual.md)：

     所有接口均支持使用手动签名方式配置签名。
3. 添加公钥指纹。

   **注意** 

   **发布阶段**，请参考[发布应用](ide-publish-app.md)，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/cOvgKsQ0S-OP7tip7gMeuA/zh-cn_image_0000002786360132.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFFEADBF61E79E5A5E69199595EEF283F75DD0D12C4A2C1E46D5B2FD849B75FC)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/2pPaOmwIQnq-_XtDuPmPlQ/zh-cn_image_0000002815559553.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=52FA6D7859E44F5046CB2960433DF2A55ABC7F7229B92BF0FD40B4BC9CF862FC)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/rnukmfXBTriEBDgnHUfF7Q/zh-cn_image_0000002815559551.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D770E508E037F3EB9DB94AB3A87924F40BBC2C97406D441C971AA974810CD26)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/kU8EO5yESuWNU32SJuPRAw/zh-cn_image_0000002815399635.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C27B3699D42401BC34AB1C26938B74B6667948C0132432256CDEB561E344661)
