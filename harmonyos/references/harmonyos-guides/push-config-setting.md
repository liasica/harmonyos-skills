---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting
title: 开通推送服务
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 开发准备 > 开通推送服务
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:29+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:34d9849d10a39a5f03ae89177536de85572f4b7d95da8d90d90c53c7f22e5386
---

在开通推送服务前，请先参考“[应用开发准备](application-dev-overview.md)”创建项目和应用工程。

**说明** 

从HarmonyOS NEXT Developer Beta2起，开发者无需配置公钥指纹和Client ID。

## 操作步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/agjLx-GIR1yDEgiBAhwnDg/zh-cn_image_0000002788308250.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=48B77B6182E2EB7B669169DD4CB2ECB5DEBF91A609EC1E4319CE032B1A6592C6)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要配置推送服务参数的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/H4hnAdrVSSObkAeyYqbqtQ/zh-cn_image_0000002817427613.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=528185EE758D0C3A61C0EDF0B3398113346A63EBD690FDD0D430910D4EDB1F81)
3. 在左侧导航栏选择“增长 > 推送服务”，点击“立即开通”，在弹出的提示框中点击“确定”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/CXl_W-LlQV2WiOkBl7WRbw/zh-cn_image_0000002788468194.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=D29C673892E805F0443D6AB0B732B858DDEF01B71847F7CC3A059F8ED7EC0AEC)

   **说明** 

   推送服务权益为项目级，若您已有开通过推送服务的项目，当您在项目中添加新的应用时，无需再次开通推送服务。
4. 若项目当前未配置数据处理位置，请在提示中点击“确定”，会弹出设置数据处理位置的弹窗。完成数据处理位置的设置，点击“确定”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/CWgwjD8cR4CL9HEbFw2AxQ/zh-cn_image_0000002817507683.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EE582D29D429E7C964B69F1CE2A9C29A2E661554D801A2791227A0B32A512EB)

   **说明** 

   推送服务当前Wearable设备支持的国家请参见[支持的国家/地区](push-country.md)，数据处理地可根据支持的国家/地区设定；其他设备仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），数据处理地固定为中国。
5. 针对开发调试场景，从DevEco Studio 6.0.0 Beta5版本开始，新增了更高效的自动签名方案，开发者可以选择以下其中一种方式进行调试阶段的应用签名。

   * 手动签名：调试阶段**必须**申请调试证书、[注册调试设备](../app/agc-help-add-device-0000002283189937.md)、确保“增长 > 推送服务”中已开通“推送服务”后**重新**申请调试Profile文件，并完成[手动签名](ide-signing-manual.md)。
   * 自动签名（新增）：请参考[自动签名](ide-signing-auto.md)，开通Push Kit开放能力，点击“OK”后，DevEco Studio将自动重新签名。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/8dtNSQz0Q9magaZJZbZfQQ/zh-cn_image_0000002788308252.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA65DBA5940C0A785A43477E4F87DF92B72DAAE78BCE56FCF6FD718325F657C1)

     5-10分钟后访问[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，“项目设置 > 开放能力管理”中推送服务能力会显示已勾选。同时，“增长 > 推送服务”中“推送服务”会自动开通。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/fG8_eOH0Q-iBOpypEv9KvQ/zh-cn_image_0000002817427615.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CC7EC084AC51A54A2FB3C1A879697724B0B18F21A40389F9B5EB68E5B5F48F4)
6. 应用发布阶段**必须**申请发布证书、确保“增长 > 推送服务”中已开通“推送服务”后重新申请发布Profile文件，并完成手动签名。详情请参考发布应用[配置签名信息](ide-publish-app.md#section945904791115)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/JX2YcPOAQwWAY4M1-UeyPQ/zh-cn_image_0000002788468196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=080366CF3A1E400C8C85361247D79FB7E8C250F81A3C579F564D95372B571240)
7. 您还可以通过“增长 > 推送服务 > 配置”，在“配置”页签下选择需要申请自分类权益的应用，点击**自分类权益**后的“申请”，详见[申请步骤](push-apply-right.md#申请通知消息自分类权益)。

   **说明** 

   强烈建议您申请通知消息的**自分类权益**，并按对应分类发送通知消息。**否则Push Kit默认您推送的是资讯营销类消息**，会导致单个应用每日每设备推送数量为**2条**或**5条**。
8. （可选）您还可以通过“增长 > 推送服务 > 配置”，在“配置”页签开通或关闭您的项目级和应用级的[消息回执](push-msg-receipt.md)。

   **说明** 

   * 若项目级的消息回执权益开通，应用级的消息回执权益未开通，则该应用消息回执权益取项目级的。
   * 若项目级的消息回执权益开通，应用级的消息回执权益开通，则该应用消息回执权益取应用级的。

## （可选）设置数据处理位置

您可以在“项目设置 > 数据处理位置”页面设置或更新数据处理位置，步骤如下：

**说明** 

如果设置的数据处理位置与您的服务器位置不一致，或者设置的数据处理位置与应用所服务的用户所在地不一致，都会导致推送消息无法下发。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”。
2. 在项目列表中点击您需要设置数据处理位置的项目。
3. 进入“项目设置 > 数据处理位置”页面，点击“管理”。
4. 按需设置数据处理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/yCCxXEfxSE22cNPJK509xQ/zh-cn_image_0000002817507685.png?HW-CC-KV=V1&HW-CC-Date=20261114T004644Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D79131194ABAB019FA53B00CFDBDF9955BC8D98920BBD62FAE835FE0B4DA221)
5. 设置完成后，点击“保存”。
