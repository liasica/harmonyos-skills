---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:886bd01b28a0a48653e6fe5da9d2d7a0b88d1844aac77cfd739375f19b700d75
---

请参考“[应用开发准备](application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息 **（未成年人模式接口支持自动签名，其他接口仅支持手动签名方式）**。
3. 添加公钥指纹。

   注意

   **发布阶段**，请参考[发布流程](ide-publish-app.md#section6406135115814)章节，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/TIabyPDVTUGt7UjAi7yzzQ/zh-cn_image_0000002552958744.png?HW-CC-KV=V1&HW-CC-Date=20260427T234756Z&HW-CC-Expire=86400&HW-CC-Sign=1191A5E74436623FDD7FBF44E69A7AFE9176D4D55FC6319DE5974854594BE83B)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/OwwNHqdiQnqvj-yMNfadhw/zh-cn_image_0000002583478745.png?HW-CC-KV=V1&HW-CC-Date=20260427T234756Z&HW-CC-Expire=86400&HW-CC-Sign=76DAEC27C9AE83ACF6761A10FD6D6B454637C286FBE15E46B1017CAB849DC250)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/aFkomIg-SBeLqx-tJAphDg/zh-cn_image_0000002552799094.png?HW-CC-KV=V1&HW-CC-Date=20260427T234756Z&HW-CC-Expire=86400&HW-CC-Sign=1C858458F98A80B3169DD4364CB85B5292BF0052EE49F6B466DB67040C495175)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/aN9vAgQcTHiyXAAXE3xpLg/zh-cn_image_0000002583438789.png?HW-CC-KV=V1&HW-CC-Date=20260427T234756Z&HW-CC-Expire=86400&HW-CC-Sign=ED11194EB7DCFAE35542470547C082ABFE0E13EBCE54EB5C68C6E205F503D885)
