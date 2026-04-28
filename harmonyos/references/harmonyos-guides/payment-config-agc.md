---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-agc
title: 开通支付服务
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 开通支付服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c10ad5070e97d547b9b8d43c2be1ac2a3833a2034f01439a72f6ac83daac06b6
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

说明

1. 后续接入涉及AppID绑定，仅限企业开发者接入。开发者注册后发起实名认证请选择[企业开发者实名认证](../start/edrna-0000001062678489.md)，并且需要准备企业营业执照等必要材料。
2. 每个应用/元服务最多支持添加4个签名证书指纹。
3. **[配置签名信息](application-dev-overview.md#section42841246144813)需选择手动签名**。

## 开通步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/glI8albWTGWbbILb2jhp2w/zh-cn_image_0000002583479075.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=F3726C6E1C2DAFACEDADCD2D07CDC4470EFC81A7B19FA0448475DF9A5D88EF50)
2. 在项目列表中找到项目（如未创建项目可点击添加项目先完成项目创建），在项目下的应用列表中选择需要开通Payment Kit的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/W-28wyUbQ82BaL9yUxI4mA/zh-cn_image_0000002552799426.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=0463A6A2EEF133A6C1076EF01BF5BF885C879484766D38EC28C42EB0CC084763)
3. 在左侧导航栏选择“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏） > 支付服务（非虚拟类）> 立即开通”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/yy7IDZ-nR_S-Gj2b3kySrA/zh-cn_image_0000002583439121.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=54ED3C809107645E2F6B9E431C069325ADF417521DC7601E52722CFFFA64BE84)
4. 如涉及商户入网，在服务开通后需要为商户号申请绑定AppID，详细参见[商户号绑定AppID](payment-binding-appid-to-merc.md)（如未完成商户入网，可点击“申请支付商户号”先进行商户入网，详细介绍参考[商户入网](payment-merc-regist-apply.md)章节）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/o9w3a-WFTmuj7rDrMi5cYg/zh-cn_image_0000002552959076.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=1A0F15A9B5A1EDD0AF03A5DDE0F58B8F68B62CF2A5D736A3A62D01B58D25863E)
