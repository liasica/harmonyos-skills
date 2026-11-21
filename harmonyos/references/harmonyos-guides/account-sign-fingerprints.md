---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ad4ad87d374f9eb128f2a1d26c3fa804ca6178efb72bbe93ec95bf47231ccee0
---

请参考“[应用开发准备](application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息。针对开发调试场景，从DevEco Studio 26.0.0 Beta2版本开始，新增了更高效的自动签名方案，开发者可以选择以下其中一种方式进行调试阶段的应用签名。

   * [自动签名](ide-signing-auto.md)：

     应用运行的HarmonyOS系统版本低于HarmonyOS 6.0.0(20)时，仅未成年人模式接口支持自动签名。

     应用运行的HarmonyOS系统版本为HarmonyOS 6.0.0(20)及以上时，所有接口均支持使用自动签名方式进行配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/31Pg4Os6RkOmzvxMuum1EQ/zh-cn_image_0000002792877846.png?HW-CC-KV=V1&HW-CC-Date=20261121T011215Z&HW-CC-Expire=31536000000&HW-CC-Sign=90B40890FBF97DA7E29C32A5208EF564B780FADC56D1ACFEFDDE3CE284BE3229)
   * [手动签名](ide-signing-manual.md)：

     所有接口均支持使用手动签名方式配置签名。
3. 添加公钥指纹。

   **注意** 

   **发布阶段**，请参考[发布应用](ide-publish-app.md)，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/nJcHBQ81SJigNyXNAENg9w/zh-cn_image_0000002821837753.png?HW-CC-KV=V1&HW-CC-Date=20261121T011215Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5D09678D8118E816070078CA75BF863066B4F586C1DE35A677B1482C63B2AAD)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/gudwWrmXShmeOXKiQH5u4A/zh-cn_image_0000002821757755.png?HW-CC-KV=V1&HW-CC-Date=20261121T011215Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D13362D193572D01D03B75DC565A107DD60D0DF6EFF17A0C6E0E7304F6A974B)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/qFpN-hMlRCmljozbRwAGGg/zh-cn_image_0000002821757753.png?HW-CC-KV=V1&HW-CC-Date=20261121T011215Z&HW-CC-Expire=31536000000&HW-CC-Sign=9960AE324FAC276000BED316EBDE278106D53E999E368E550817FC4C356A3B3A)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/_Oi2UFRFQTuFLGbOJxRSDQ/zh-cn_image_0000002793037816.png?HW-CC-KV=V1&HW-CC-Date=20261121T011215Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C56A4CD1F66CFB77EECA77AB35DBC39026478E150AE3AD26547693274BA52FF)
