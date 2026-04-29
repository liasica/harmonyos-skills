---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-binding-appid-to-merc
title: 商户号绑定AppID
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 商户号绑定AppID
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:30+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:593f10f97bb045ce7f086892eedb13e3f77b8fd49d457de60ba0841fec2ecdea
---

说明

商户号绑定AppID的商户需要通过[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)入网，详见[商户入网和获取商户号](payment-merc-regist-apply.md)。通过[华为开发者联盟官网](https://developer.huawei.com/consumer/cn/)开通[商户服务](../app/open-0000001959074873.md)入网的商户暂不支持直接接入华为支付以及绑定AppID操作。

商户（以下所称商户均包含所有商户模型）后续支付交易依赖于[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[创建应用](../app/agc-help-create-app-0000002247955506.md)生成的AppID与商户号的关联关系。商户在请求预下单接口传递AppID入参，后续可以在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上基于应用维度查看交易报表数据。传递AppID参数后，华为支付侧会校验商户号与传递的AppID是否匹配，如不匹配则会直接响应异常。因此，接入鸿蒙支付服务前商户需要为商户号绑定AppID，如无商户号则需要先申请，详细介绍参考[商户入网和获取商户号](payment-merc-regist-apply.md)。

AppID绑定详细可参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。

## 基本概念

**同主体**：商户号与AppID所关联的营业主体信息一致。

**异主体**：商户号与AppID关联的营业主体信息不一致。

## 绑定AppID说明

1. 暂不支持平台子商户及特约商户发起绑定AppID申请。
2. 商户发起绑定AppID申请，异主体绑定需要商户与华为支付侧沟通申请开通异主体绑定权限（可参考[产品开通操作](payment-product-configuration.md#场景一产品开通操作)）后才可在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)发起异主体AppID绑定操作。
3. AppID关联的营业主体与特约商户商户号或与服务商商户号关联的营业主体一致，都认为是同主体，可直接发起绑定。
4. 商户发起绑定申请后，商户应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站才能对商户号绑定AppID进行授权（提示“主体不一致”可[参见这里](payment-faq-26.md)）。

## 直连商户/平台类商户绑定

1. 请登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理 > 新增关联AppID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/zduBdvAjRuK2iaXYYiDATQ/zh-cn_image_0000002558605922.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=965D07AF59F266382E615574387638D2341707F47B79F68C045F4CE5C39F9456)
2. 申请绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，完成对应的商户“授权”操作， 操作路径如下：

   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/127ZDc6ATPSrBcX39P9d7g/zh-cn_image_0000002589325449.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=727F84198D3936E71CC91992325686E373143A5CA07100E408D8BB546F75CC31)
   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/hAw-_OUcQzCY-8yJbhVCNg/zh-cn_image_0000002589245387.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=0133608DC93A9E3729EFD2BED058BD8CA74A02E0CD0149B7B4ED51777ED64255)

## 服务商绑定

服务商绑定AppID涉及如下场景：

1. **服务商绑定**

   服务商需要绑定服务商应用AppID可直接在华为支付商户平台发起绑定申请。
2. **特约商户绑定**

   特约商户需要绑定特约商户应用AppID，需要服务商在华为支付商户平台发起邀请特约商户绑定AppID才可以进行绑定。

### 服务商绑定

1. 服务商登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”，在“服务商绑定的AppID”页签内点击“新增关联AppID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kbQ8Vlf7Q1a5RC-ehsHElg/zh-cn_image_0000002558765580.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=C2EC3B44E0EBC5A5C814C2C4F22C6452A677F5F9DDC03E2F1ECE1BFA1DC106F9)
2. 申请绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，完成对应的商户“授权”操作， 操作路径如下：

   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/Cj5zdVssRZWSpYhng3UDtw/zh-cn_image_0000002589325449.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=D3897D9F303311F8D21B35523821795519A797A9095BE1335192193CB1E88872)
   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/H28AJDLpReO-sFLjPUudjQ/zh-cn_image_0000002589245387.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=B218D65D0EC9B71FB8048CF91955A4899DD08D9B12B76A27E5C3762DEB0E2758)

### 服务商邀请特约商户绑定

1. 服务商登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”，在“特约商户绑定的AppID”页签内根据服务商下的特约商户列表，选择特约商户发起AppID绑定申请邀请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/mOOyxnKERlKjaXtr9RgVtQ/zh-cn_image_0000002558605924.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=A289E96451BFB4C3575956710A65792B3EF7414D7B564C304E6EEA42FB3528B0)
2. 特约商户登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”选择“服务商为我绑定的AppID列表”中的数据，点击去确认，对服务商邀请绑定AppID进行确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/chsdt2QaT1anHom4fpFHUQ/zh-cn_image_0000002589325451.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=43C1A255B8662B698FD4225D7B2FD11CB0ADC37BD7A92C64BCD734EFD8B290E8)
3. 特约商户确认绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，完成对应的商户“授权”操作， 操作路径如下：

   * **HarmonyOS应用**：“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/8bINzuVuRLm4gREzFGEQTg/zh-cn_image_0000002589325449.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=841DCA5FFB2BF65A3C1CD854898F10267A47F730890C6C7519B4E4D730A16F3E)
   * **元服务**：“支付与交易 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/BnANEjkJR0KKpsQ0VYsW4g/zh-cn_image_0000002589245387.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=B67F4D1C00E730DE33FDEDB1C7B117B5082DE13B63093ED97484439994F9B1EB)
