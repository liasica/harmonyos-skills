---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting
title: 开通推送服务与接入准备
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 开发准备 > 开通推送服务与接入准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:36+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:e0d0dbe867b77c4775bc82ea49019a4d8f919e62d70ccfd28b830c8e9b69c02e
---

在开通和接入推送服务前，请先参考“[应用开发准备](application-dev-overview.md)”创建项目和应用工程。

**说明** 

从HarmonyOS NEXT Developer Beta2起，开发者接入推送服务无需配置公钥指纹和Client ID。

## 开通步骤

在开发调试或发布使用推送服务能力的应用前，需在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)为项目开通推送服务。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/mak1HM4DTW2y1K-9dBaruw/zh-cn_image_0000002792878232.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=127226DBB5B3833BDE2478F1529E54EA9E7296D16CC8C591BEA6F6152D9EBC63)
2. 在项目列表中找到目标项目，在项目下的应用列表中选择需要配置推送服务参数的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/hYPBjLFDTLyloN-bviBQVA/zh-cn_image_0000002821838139.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=944A1DBC175348DAB04D6F695AAC593A7C17CA7361FCD7D58B1FA3F59FEF53FD)
3. 在左侧导航栏选择“增长 > 推送服务”，点击“立即开通”，在弹出的提示框中点击“确定”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/7sAR9HvHSW-CZ7imaKWDGQ/zh-cn_image_0000002821758141.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=991E696ED8B2B7830AE8934585F6F447C6949EB42F8968C71DF7478A14B9690B)

   **说明** 

   推送服务权益为项目级。如果项目中已有其他应用开通过推送服务，则添加新应用时无需再次开通。
4. 若项目当前未配置数据处理位置，系统会弹出提示，在提示框中点击“确定”，然后在弹出的窗口中完成数据处理位置的设置，最后点击“确定”。

   后续需要重新设置或更新，可以参见[设置数据处理位置](push-config-setting.md#可选设置数据处理位置)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/K1hT__naSX6mnOFDi9SxTQ/zh-cn_image_0000002793038204.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=01D102ED5F7C20E548E786256AD23EBDA9900B7E1DA4B4BB5C7BF9901184943F)

   **说明** 

   * 对于Wearable设备，推送服务支持的国家/地区请参见[支持的国家/地区](push-country.md)，可根据应用的服务范围设定数据处理位置。
   * 对于其他设备，推送服务仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），数据处理位置固定为中国。

完成以上步骤后，即为项目开通了推送服务。后续可在“项目设置 > 开放能力管理”查看**推送服务**，通过“增长 > 推送服务”设置通知、查阅报告或修改配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/fpli_9ZYSa6EN8zPaolR8w/zh-cn_image_0000002792878234.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A70E5F3473BD8437ABEB97590172773E3F6D62E4499D53D2C8ECA30104407F0)

## 开发调试

开发调试前，需完成密钥和证书请求文件生成、调试证书和Profile申请、设备注册及签名配置。从DevEco Studio 6.0.0 Beta5起，可通过更高效的[自动签名](push-config-setting.md#自动签名推荐)方案完成以上配置，而之前版本还是需要通过使用[手动签名](push-config-setting.md#手动签名)方式完成。

### 自动签名（推荐）

[自动签名](ide-signing.md#section18815157237)仅用于开发调试阶段，为开发者提供快速上手的调试测试方案，适用于绝大多数场景。复杂调试场景或应用发布请使用[手动签名](push-config-setting.md#手动签名)。

1. 在DevEco Studio中打开项目，点击右上角**项目结构**，在“签名配置”页签中登录已注册待开发项目的[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)账号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/a6x_xVoQQ-q5Zu4YpuF01g/zh-cn_image_0000002821838141.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC8226D714AC50C7EEFF9680C69004828476FE34D861A8807FAD79716D54A6F8)

   登录成功后界面如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/yrAeIc9JQs-LYngdjVIodg/zh-cn_image_0000002821758143.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A2FCC8CEA6C27E947354ECEC4665B50580F14FDC8490CEA82F8EB0C497CA84F)
2. 勾选**自动生成签名文件**和**关联已注册应用**（确保包名与项目中的应用包名一致）。
3. 滚动至页面底部，点击**开通开放能力**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/WYWSd4YRS22fdelorc2bNQ/zh-cn_image_0000002793038206.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=49C8E7F7C5C6827B19A3ADE3FD41343175FFA7B2FD41A1845C146C5215B9EC72)

   在**能力管理**页面勾选**Push Kit**并确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/llqau7ywSkC1urQeGP9CWw/zh-cn_image_0000002792878236.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=339500D50A3142F0F4AD1A6734041C03CBA209506123A81DFF1F4A73C47D4E23)

至此，即可在DevEco Studio中开始调试客户端代码。

### 手动签名

在[自动签名适用限制](ide-signing.md#section54361623194519)场景下或涉及[应用发布](push-config-setting.md#应用发布)时，请使用[手动签名](ide-signing.md#section297715173233)。

1. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)官网上[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)。
2. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)官网上[注册调试设备](../app/agc-help-add-device-0000002283189937.md)。
3. 确保已按[开通步骤](push-config-setting.md#开通步骤)开通推送服务。
4. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)官网上[申请调试Profile文件](../doccenter-getting-started/agc-help-debug-profile-0000002248181278.md)。
5. 在DevEco Studio中[配置签名信息](ide-signing.md#section1240072619462)。

详细步骤请参见[手动签名](ide-signing.md#section297715173233)。

## 应用发布

应用发布前，需完成发布签名的配置。先确保已按[开通步骤](push-config-setting.md#开通步骤)开通推送服务，然后重新[申请发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)并完成[手动签名](push-config-setting.md#手动签名)。详情请参见[配置签名信息](ide-publish-app.md#section945904791115)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/FTfcyBrQSw6ksxTIhMTo8Q/zh-cn_image_0000002792878234.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=89CAA36099DE22212883357DBDBB7CFB0124432817A7FB5619E8984EAB6B3C2A)

## 申请推送场景化消息权益

推送服务支持多种场景化消息类型，其中部分场景化消息类型需要申请特殊权益才能正常发送，具体包括：通知消息自分类权益、推送语音播报消息权益和推送应用内通话消息权益。各权益申请方法详见[申请推送场景化消息权益](push-apply-right.md)。

**说明** 

未申请通知消息自分类权益时，**Push Kit默认将通知消息分类为资讯营销类消息**。资讯营销类消息每天可发送消息数量根据应用类型分为**2条**或**5条**。若发送通知消息被频控，请尝试发送测试消息或申请自分类权益。

## （可选）配置消息回执

开发者可借助[消息回执](push-msg-receipt.md)获取消息下达端侧后的状态，定位问题等。通过“增长 > 推送服务 > 配置”，在“配置”页签开通或关闭项目级和应用级的[消息回执](push-msg-receipt.md)。

**说明** 

* 若项目级的消息回执权益开通，应用级的消息回执权益未开通，则该应用消息回执权益取项目级的。
* 若项目级的消息回执权益开通，应用级的消息回执权益开通，则该应用消息回执权益取应用级的。

## （可选）设置数据处理位置

在[开通推送服务](push-config-setting.md#开通步骤)时会第一次设置数据处理位置，后续开发者可以在“项目设置 > 数据处理位置”页面重新设置或更新数据处理位置。

**说明** 

如果设置的数据处理位置与服务器位置不一致，或者与应用所服务的用户所在地不一致，都可能导致推送消息无法下发。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”。
2. 在项目列表中点击需要设置数据处理位置的项目。
3. 进入“项目设置 > 数据处理位置”页面，点击“管理”。
4. 按需设置数据处理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/STOXCh2FTBOG-HSnWs1FeQ/zh-cn_image_0000002821838143.png?HW-CC-KV=V1&HW-CC-Date=20261121T011235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0444ED7B7220EB8CCDF5D5AA60614221F3C3E15FB69A1C322DB95673DA5EBE1A)
5. 设置完成后，点击“保存”。
