---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting
title: 开通推送服务
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 开发准备 > 开通推送服务
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:37bcbe8eecc6a3eb59cb51cb5e8f2f55abd2371b799a2f2359827b6948dde38f
---

在开通推送服务前，请先参考“[应用开发准备](application-dev-overview.md)”创建项目和应用工程。

说明

从HarmonyOS NEXT Developer Beta2起，开发者无需配置公钥指纹和Client ID。

## 操作步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/lzj2SWnQSYCidwTUlMY1Sg/zh-cn_image_0000002558605952.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=71D9DAD788A564AE9462BF3B7D328B14D5A5C78A8F4A1CFD0699A4E05AD856FA)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要配置推送服务参数的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/OwWO2zymQOy1Ux8RqpPfPA/zh-cn_image_0000002589325479.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=A32521CC771A52398B4B47C8A1C77D6436843B95079B57059D02A892BD73D7CA)
3. 在左侧导航栏选择“增长 > 推送服务”，点击“立即开通”，在弹出的提示框中点击“确定”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/EQYhK61TQySjNXl60PedVA/zh-cn_image_0000002589245417.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=E3CC2F7218F3EA187A7893BAACF90AD941489BA5D40CCFC7F1C02A0E7BB7440D)

   说明

   推送服务权益为项目级，若您已有开通过推送服务的项目，当您在项目中添加新的应用时，无需再次开通推送服务。
4. 若项目当前未配置数据处理位置，请在提示中点击“确定”，会弹出设置数据处理位置的弹窗。完成数据处理位置的设置，点击“确定”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/b6-IksNMTdmeBPAUVpkzdQ/zh-cn_image_0000002558765610.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=2516C5C9B4DDF6C87208CB87AA24444B711A585FDB2AAC7E6E825C38C5422AE8)

   说明

   推送服务当前Wearable设备支持的国家请参见[支持的国家/地区](push-country.md)，数据处理地可根据支持的国家/地区设定；其他设备仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），数据处理地固定为中国。
5. 针对开发调试场景，从DevEco Studio 6.0.0 Beta5版本开始，新增了更高效的自动签名方案，开发者可以选择以下其中一种方式进行调试阶段的应用签名。

   * 手动签名：调试阶段**必须**申请调试证书、[注册调试设备](../app/agc-help-add-device-0000002283189937.md)、确保“增长 > 推送服务”中已开通“推送服务”后**重新**申请调试Profile文件，并完成[手动签名](ide-signing.md#section297715173233)。
   * 自动签名（新增）：请参考[自动签名](ide-signing.md#section18815157237)，开通Push Kit开放能力，点击“OK”后，DevEco Studio将自动重新签名。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/pJVRE903SXixhNVotqKxig/zh-cn_image_0000002558605954.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=CBA9AFF1B03E26192B6198CC681F21D33755E0CA49F541CA0C87DDDFD7B1CD8C)

     5-10分钟后访问[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，“项目设置 > 开放能力管理”中推送服务能力会显示已勾选。同时，“增长 > 推送服务”中“推送服务”会自动开通。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/w03mW20MS5mOZYW3jBTEkQ/zh-cn_image_0000002589325481.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=999DD1E456AFC580AC65A0F8CACBEA8BB57D93A1076AFA6FB70D8EB6903656E0)
6. 应用发布阶段**必须**申请发布证书、确保“增长 > 推送服务”中已开通“推送服务”后重新申请发布Profile文件，并完成手动签名。详情请参考发布应用[配置签名信息](ide-publish-app.md#section280162182818)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/RfA6cfVpS9aVt3sP2rfN8w/zh-cn_image_0000002589245419.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=C7C8CC07DEB7C220E56D080816BEB65F2369D686BB955BC55454A9DA11300C71)
7. 您还可以通过“增长 > 推送服务 > 配置”，在“配置”页签下选择需要申请自分类权益的应用，点击**自分类权益**后的“申请”，详见[申请步骤](push-apply-right.md#申请通知消息自分类权益)。

   说明

   强烈建议您申请通知消息的**自分类权益**，并按对应分类发送通知消息。**否则Push Kit默认您推送的是资讯营销类消息**，会导致单个应用每日每设备推送数量为**2条**或**5条**。
8. （可选）您还可以通过“增长 > 推送服务 > 配置”，在“配置”页签开通或关闭您的项目级和应用级的[消息回执](push-msg-receipt.md)。

   说明

   * 若项目级的消息回执权益开通，应用级的消息回执权益未开通，则该应用消息回执权益取项目级的。
   * 若项目级的消息回执权益开通，应用级的消息回执权益开通，则该应用消息回执权益取应用级的。

## （可选）设置数据处理位置

您可以在“项目设置 > 数据处理位置”页面设置或更新数据处理位置，步骤如下：

说明

如果设置的数据处理位置与您的服务器位置不一致，或者设置的数据处理位置与应用所服务的用户所在地不一致，都会导致推送消息无法下发。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”。
2. 在项目列表中点击您需要设置数据处理位置的项目。
3. 进入“项目设置 > 数据处理位置”页面，点击“管理”。
4. 按需设置数据处理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/32khvcXYQw-q7brMv7wEcA/zh-cn_image_0000002558765612.png?HW-CC-KV=V1&HW-CC-Date=20260429T053952Z&HW-CC-Expire=86400&HW-CC-Sign=A83454A9563320E60FB25AAC6A624DD54E8CAC15866A23AE738C7DE899722A85)
5. 设置完成后，点击“保存”。
