---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-agc
title: 开通支付服务
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 开通支付服务
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:33+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b9a76d5a85a0db0e9086d92bee84d4fab1c142ec49ac4549073aa401f4464290
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

**说明** 

1. 后续接入涉及AppID绑定，仅限企业开发者接入。开发者注册后发起实名认证请选择[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)，并且需要准备企业营业执照等必要材料。
2. 每个应用/元服务最多支持添加4个签名证书指纹。
3. **[配置签名信息](application-dev-overview.md#配置签名信息)需选择手动签名**。

## 开通步骤

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)。
2. 点击“开发者管理”，左侧导航栏选择“ID、证书和Profile > APP ID”，进入“APP ID列表”页签，点击右上角“创建”。在打开的“新建APP ID”页面，创建应用及项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/PBZEmZ--Rp6XsuP78pfGOg/zh-cn_image_0000002793038170.png?HW-CC-KV=V1&HW-CC-Date=20261121T011232Z&HW-CC-Expire=31536000000&HW-CC-Sign=40B3A5C6FDD8C0FAB7C71B09E724096E8E26A6039D3405034CFF908C3042E825)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/mQYm8gL_TxuYRxIL1KyWNg/zh-cn_image_0000002792878200.png?HW-CC-KV=V1&HW-CC-Date=20261121T011232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E5492CD4769433D5E973D03A49675FBA541397F08C23DBCBF7D0384F9A2CB3A)
3. 开通服务，操作路径如下：

   * **元服务**：“应用管理 > 支付与交易 > 鸿蒙支付 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/LCNWhH8-RKGc_-VlTM21aQ/zh-cn_image_0000002821838107.png?HW-CC-KV=V1&HW-CC-Date=20261121T011232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2550599D72C1C8CBDB5170FDFFADD75107CDB192FF3B4DA86C0E4E28DF05A994)
   * **HarmonyOS应用**：“应用管理 > 盈利 > 鸿蒙支付服务 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Eaw2qy7GRKaOqplTj8x0-g/zh-cn_image_0000002821758109.png?HW-CC-KV=V1&HW-CC-Date=20261121T011232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF69FB6B700EA5F48532100697A21C929CBD5D99707D73E3D8952F85751DA88D)
4. 如涉及商户入网，在服务开通后需要为商户号申请绑定AppID，详细参见[商户号绑定AppID](payment-binding-appid-to-merc.md)（如未完成商户入网，可点击“申请支付商户号”先进行商户入网，详细介绍参考[商户入网](payment-merc-regist-apply.md)章节）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/0g1RSc8dTZWr_9t9lRF6Dw/zh-cn_image_0000002793038172.png?HW-CC-KV=V1&HW-CC-Date=20261121T011232Z&HW-CC-Expire=31536000000&HW-CC-Sign=95070013A38123011B5660FDBADAEAC5696288F1A8AAC00B3D7493FE0AAA99D2)
