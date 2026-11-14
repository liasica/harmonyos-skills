---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3f7d23b436d5a9faaa952be71dec734207d1728a21147d0c15f8f85d914729cb
---

请参考“[应用开发准备](application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息。针对开发调试场景，从DevEco Studio 26.0.0 Beta2版本开始，新增了更高效的自动签名方案，开发者可以选择以下其中一种方式进行调试阶段的应用签名。

   * [自动签名](ide-signing-auto.md)：

     应用运行的HarmonyOS系统版本低于HarmonyOS 6.0.0(20)时，仅未成年人模式接口支持自动签名。

     应用运行的HarmonyOS系统版本为HarmonyOS 6.0.0(20)及以上时，所有接口均支持使用自动签名方式进行配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/XuXa9v6jThSk3e6-1RPRqA/zh-cn_image_0000002788307864.png?HW-CC-KV=V1&HW-CC-Date=20261114T004809Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA5CECC326D19D26183FA06B11BA3AE686100A3091E09916EF5E1ADF29D192F2)
   * [手动签名](ide-signing-manual.md)：

     所有接口均支持使用手动签名方式配置签名。
3. 添加公钥指纹。

   **注意** 

   **发布阶段**，请参考[发布应用](ide-publish-app.md)，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/6n9ek0D0RL-YwUolTHKL0g/zh-cn_image_0000002817427227.png?HW-CC-KV=V1&HW-CC-Date=20261114T004809Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C3DD69FCE1A23A8A63CC14753C10DEB47881D3F5C415422C4EA475EE64787AA)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/0jHB4YA7QwO5SUzJcoZ0OA/zh-cn_image_0000002788467808.png?HW-CC-KV=V1&HW-CC-Date=20261114T004809Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6A6BC7035EFB6858C02DE55BFD41FD91B7888B644FBCE872F530D4022574491)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/XIdcuH1eQJC_e1OAPdnA9Q/zh-cn_image_0000002788467806.png?HW-CC-KV=V1&HW-CC-Date=20261114T004809Z&HW-CC-Expire=31536000000&HW-CC-Sign=A071C2C0B167F4F38A619F92EB0BAF9B7810739CA78842088E96C9ACA6CF0338)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/rVrzrKGETveZssc4a30eHg/zh-cn_image_0000002817507295.png?HW-CC-KV=V1&HW-CC-Date=20261114T004809Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B33653835756F066ABB3C44E786AA61304CED5C731B90BD24A9562530EBC01D)
