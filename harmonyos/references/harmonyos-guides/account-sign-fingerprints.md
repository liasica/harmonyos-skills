---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints
title: 配置签名和指纹
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置签名和指纹
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5ee2deded6589fe467a37f7f25f254cf14689773bfa56d2c1f403de79f07e07c
---

请参考“[应用开发准备](application-dev-overview.md)”章节，完成以下操作步骤：

1. 创建项目和工程（如已完成，请跳过此步骤）。
2. 配置签名信息 **（未成年人模式接口支持自动签名，其他接口仅支持手动签名方式）**。
3. 添加公钥指纹。

   注意

   **发布阶段**，请参考[发布流程](ide-publish-app.md#section6406135115814)章节，重新配置用于应用发布的签名信息、添加公钥指纹（必选）。

   * 检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/HoFTInMWTDiwIzAD6lm9zg/zh-cn_image_0000002558765244.png?HW-CC-KV=V1&HW-CC-Date=20260429T053606Z&HW-CC-Expire=86400&HW-CC-Sign=2CD5E49F4F805A58E5DE5449616293EDD3A6DCB099BD8440FEDDDF68AC0572DE)
   * 检查公钥指纹是否配置成功：请在[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Zvt2GMpvQ5ahjEai4y6Krg/zh-cn_image_0000002558605588.png?HW-CC-KV=V1&HW-CC-Date=20260429T053606Z&HW-CC-Expire=86400&HW-CC-Sign=76F84ED121EDC0FDD5BBCE2ED4E6DDA194C2139E45805609ECE464AB5A7F0EC7)
   * 公钥指纹最迟会在25小时后生效。

     **（可选）** 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

     **图1** 修改前

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/OlnR0I0YRGSt2a4gd0I_hA/zh-cn_image_0000002589325113.png?HW-CC-KV=V1&HW-CC-Date=20260429T053606Z&HW-CC-Expire=86400&HW-CC-Sign=748F130F2350C13C76B85CA123AAF54B35CDFB99514127C6A1298A4E7ABCC238)

     **图2** 修改后

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/cbbScghaRX2-X6pH9C4AvA/zh-cn_image_0000002589245049.png?HW-CC-KV=V1&HW-CC-Date=20260429T053606Z&HW-CC-Expire=86400&HW-CC-Sign=90415AA9A2DD9B3C175D7F330AE05B9C26E8516FA363A325EF464460A7281AF6)
