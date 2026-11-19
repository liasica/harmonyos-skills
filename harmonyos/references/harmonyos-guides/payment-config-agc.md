---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-agc
title: 开通支付服务
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 开通支付服务
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:007a364d8e5faa6fe88af6ee5e382da26c184550b3675b54719f163c89d9f5a6
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

**说明** 

1. 后续接入涉及AppID绑定，仅限企业开发者接入。开发者注册后发起实名认证请选择[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)，并且需要准备企业营业执照等必要材料。
2. 每个应用/元服务最多支持添加4个签名证书指纹。
3. **[配置签名信息](application-dev-overview.md#配置签名信息)需选择手动签名**。

## 开通步骤

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)。
2. 点击“开发者管理”，左侧导航栏选择“ID、证书和Profile > APP ID”，进入“APP ID列表”页签，点击右上角“创建”。在打开的“新建APP ID”页面，创建应用及项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/VqBgD_vrSVuTovkxzJgKGQ/zh-cn_image_0000002820526499.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6CB0F349E94B3300F3792C55F1B35AAA50EB7AD7F0CD3DD3E4915D10F17D877)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/PSyvmjgjRt-X2rCHjOl37g/zh-cn_image_0000002820406499.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=63C8ED1BECC38A43770AE754C8CB62A95A7A90479CD3745611C2749C83154EAA)
3. 开通服务，操作路径如下：

   * **元服务**：“应用管理 > 支付与交易 > 鸿蒙支付 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ZOcvw97-Qbqcy1YnVzTnAg/zh-cn_image_0000002791726520.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=62D6A5C8C00EC7BA787FD020B2D8F7DCB4F37521845AAB8601550800D77F45A8)
   * **HarmonyOS应用**：“应用管理 > 盈利 > 鸿蒙支付服务 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/wLD_93cVQqeWtaa-Z4Hl3w/zh-cn_image_0000002791566548.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A4C3C1821A7C593DA2B637E8CDC401DFDB20B4B5C89708256DE6C97CB70555D)
4. 如涉及商户入网，在服务开通后需要为商户号申请绑定AppID，详细参见[商户号绑定AppID](payment-binding-appid-to-merc.md)（如未完成商户入网，可点击“申请支付商户号”先进行商户入网，详细介绍参考[商户入网](payment-merc-regist-apply.md)章节）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/O6k0y8V1SlyyAV5Z46t8Sw/zh-cn_image_0000002820526501.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=34DD2556AD41F85BC990ECDF2573B73459B35BFCF54C32C32E66EE75F504CED1)
