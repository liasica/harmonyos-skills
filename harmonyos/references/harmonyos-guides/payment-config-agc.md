---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-agc
title: 开通支付服务
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 开通支付服务
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:31+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6d62815536c7458db2fa7a17ea3ccec7aead0aaf01aee9e83c3aaeffb0ee840b
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

**说明** 

1. 后续接入涉及AppID绑定，仅限企业开发者接入。开发者注册后发起实名认证请选择[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)，并且需要准备企业营业执照等必要材料。
2. 每个应用/元服务最多支持添加4个签名证书指纹。
3. **[配置签名信息](application-dev-overview.md#配置签名信息)需选择手动签名**。

## 开通步骤

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)。
2. 点击“开发者管理”，左侧导航栏选择“ID、证书和Profile > APP ID”，进入“APP ID列表”页签，点击右上角“创建”。在打开的“新建APP ID”页面，创建应用及项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/wsjabZjWQ7yXB8Fc6qY2pg/zh-cn_image_0000002815399989.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/7uNIWe3WSUeHXCfHBmApgw/zh-cn_image_0000002786520414.png)
3. 开通服务，操作路径如下：

   * **元服务**：“应用管理 > 支付与交易 > 鸿蒙支付 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Ei4sR9eARJqm_BysULwPZQ/zh-cn_image_0000002786360486.png)
   * **HarmonyOS应用**：“应用管理 > 盈利 > 鸿蒙支付服务 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/OvOJj4G3QXSB_T2WH6Aksg/zh-cn_image_0000002815559907.png)
4. 如涉及商户入网，在服务开通后需要为商户号申请绑定AppID，详细参见[商户号绑定AppID](payment-binding-appid-to-merc.md)（如未完成商户入网，可点击“申请支付商户号”先进行商户入网，详细介绍参考[商户入网](payment-merc-regist-apply.md)章节）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/bHTtAQ3GQI6mbjiPsSXGEQ/zh-cn_image_0000002815399991.png)
