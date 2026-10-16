---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-10-17T06:42:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b0ee50239fbbe6959d5d5307bd15b2204cb32e40dd8d4122c990c50e0efa821c
---

请参考“[应用开发准备](application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息。针对开发调试场景，从DevEco Studio 26.0.0 Beta2版本开始，新增了更高效的自动签名方案，开发者可以选择以下其中一种方式进行调试阶段的应用签名。

   * [自动签名](ide-signing-auto.md)：

     应用运行的HarmonyOS系统版本低于HarmonyOS 6.0.0(20)时，仅未成年人模式接口支持自动签名。

     应用运行的HarmonyOS系统版本为HarmonyOS 6.0.0(20)及以上时，所有接口均支持使用自动签名方式进行配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/41KSOLkjQumDCU5ccEXunA/zh-cn_image_0000002764972522.png)
   * [手动签名](ide-signing-manual.md)：

     所有接口均支持使用手动签名方式配置签名。
3. 添加公钥指纹。

   **注意** 

   **发布阶段**，请参考[发布应用](ide-publish-app.md)，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/fKe4HcFbQj2UN8QZfAiBsQ/zh-cn_image_0000002765132446.png)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/hwbe7ln4TLuzwjvCIeeOyg/zh-cn_image_0000002794491023.png)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/32W_P9j8QtqFOa2q0f2O-Q/zh-cn_image_0000002794491021.png)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/JXs1nsCkTAaR3wcIqCPeaQ/zh-cn_image_0000002794411241.png)
