---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3cf662807f187041c5cc8e3838a2e3ffad0df1a54d4e7241450fbadf5b30a53a
---

请参考“[应用开发准备](application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息。针对开发调试场景，从DevEco Studio 26.0.0 Beta2版本开始，新增了更高效的自动签名方案，开发者可以选择以下其中一种方式进行调试阶段的应用签名。

   * [自动签名](ide-signing-auto.md)：

     应用运行的HarmonyOS系统版本低于HarmonyOS 6.0.0(20)时，仅未成年人模式接口支持自动签名。

     应用运行的HarmonyOS系统版本为HarmonyOS 6.0.0(20)及以上时，所有接口均支持使用自动签名方式进行配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/cpMP_oEbRR689JklZnFnsA/zh-cn_image_0000002820406145.png?HW-CC-KV=V1&HW-CC-Date=20261119T014849Z&HW-CC-Expire=31536000000&HW-CC-Sign=75F981930DCC0B672B12DB11812AAE8591C01DD39D07DE09C3BF50527D8CACDB)
   * [手动签名](ide-signing-manual.md)：

     所有接口均支持使用手动签名方式配置签名。
3. 添加公钥指纹。

   **注意** 

   **发布阶段**，请参考[发布应用](ide-publish-app.md)，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/x4rVLQLJTXKwguLD3tckCA/zh-cn_image_0000002791726166.png?HW-CC-KV=V1&HW-CC-Date=20261119T014849Z&HW-CC-Expire=31536000000&HW-CC-Sign=A34F2F92F3AC4CB2C60AE7CEA992B30C5EF18009B3498EF850F7553FBB02C2D1)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/QxlFnFRuTT2NIjpBFhsk9w/zh-cn_image_0000002791566194.png?HW-CC-KV=V1&HW-CC-Date=20261119T014849Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD71B70672628D494F111365F90A95D9979B814EA2478D959512AD3D5EB510D1)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/gG_7ogBCS3aPYxlAoWHtwg/zh-cn_image_0000002791566192.png?HW-CC-KV=V1&HW-CC-Date=20261119T014849Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8CF3B4583BC0209B48FD79B8F5D60F28F1EE6D8EAFC0E04F548C7C93AA5D5A6)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/4Xj3ieqdQoSsm7t51laDoA/zh-cn_image_0000002820526145.png?HW-CC-KV=V1&HW-CC-Date=20261119T014849Z&HW-CC-Expire=31536000000&HW-CC-Sign=A430BB21FC531E4AEF9AED2319219B89516C01011D84FFEE01BEF39DD12205B1)
