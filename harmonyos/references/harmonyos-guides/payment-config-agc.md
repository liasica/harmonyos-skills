---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-agc
title: 开通支付服务
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 开通支付服务
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:30+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0ebc2e64b8005b68b12187601bcb18b25c0b196e45e4be3af86bcccd4497e715
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

说明

1. 后续接入涉及AppID绑定，仅限企业开发者接入。开发者注册后发起实名认证请选择[企业开发者实名认证](../start/edrna-0000001062678489.md)，并且需要准备企业营业执照等必要材料。
2. 每个应用/元服务最多支持添加4个签名证书指纹。
3. **[配置签名信息](application-dev-overview.md#配置签名信息)需选择手动签名**。

## 开通步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/RkiJAruJQTerMUvv8Ws6qA/zh-cn_image_0000002558605920.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=86D5685CBC5B5C4744CA9A2F74F81C354B99D6241931842255469F77B9F71920)
2. 在项目列表中找到项目（如未创建项目可点击添加项目先完成项目创建），在项目下的应用列表中选择需要开通Payment Kit的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uCnNDP_OQFag3LDRzmqinQ/zh-cn_image_0000002589325447.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=5252FC2D39098AA4011A7914D2795917DE5F90F4439E69A6FCF72AF3756AAED0)
3. 开通服务，操作路径如下：

   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 立即开通”。
   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Hblrb4x_SK2TZll3d4_zww/zh-cn_image_0000002589245385.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=8106B557CE601D6B042519D8774357A80D1DAA30D238C00F28E0A03BCAD75F24)
4. 如涉及商户入网，在服务开通后需要为商户号申请绑定AppID，详细参见[商户号绑定AppID](payment-binding-appid-to-merc.md)（如未完成商户入网，可点击“申请支付商户号”先进行商户入网，详细介绍参考[商户入网](payment-merc-regist-apply.md)章节）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/UsJ0Kd2yQu2rSXTILShUcA/zh-cn_image_0000002558765578.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=50F3938563268CB1AA9DDE7138BC59E895D14144D0352A1B5E3960F9922C5D6A)
