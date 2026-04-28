---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-binding-appid-to-merc
title: 商户号绑定AppID
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 商户号绑定AppID
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0b66df1e4e5e41e647658cc85c81c4ffbb9e222612ea022fc9a7620d32870fbd
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/iHaNixEyRlWDSZ_drDCvyg/zh-cn_image_0000002583479077.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=B35855422E37F890869B7B507296026BFE796CE2123DEC9D358C0DCEFE6A1F6F)
2. 申请绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，在左侧导航栏选择“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”选择对应的商户点击“授权”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/4KfuKWNMRci6jl_LdUl1Cg/zh-cn_image_0000002552799428.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=EC74D4D883DC8937772554FAB688AA7DEC42B99DEB2D0078411C003912DD980E)

## 服务商绑定

服务商绑定AppID涉及如下场景：

1. **服务商绑定**

   服务商需要绑定服务商应用AppID可直接在华为支付商户平台发起绑定申请。
2. **特约商户绑定**

   特约商户需要绑定特约商户应用AppID，需要服务商在华为支付商户平台发起邀请特约商户绑定AppID才可以进行绑定。

### 服务商绑定

1. 服务商登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”，在“服务商绑定的AppID”页签内点击“新增关联AppID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Y55SrbhYQWSj9e_Q7ljDVw/zh-cn_image_0000002583439123.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=7ADBC3CAFE92B8BD625D7E3DE0E455E16A7982A1EEA5A2EA8884D4CABEF12EFB)
2. 申请绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，在左侧导航栏选择“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”选择对应的商户点击“授权”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/RHqZqA-kTJOOtWrZqjqAAw/zh-cn_image_0000002552959078.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=59104E2AC79869FAC177D80D168A3236EFBE12E77DB45CB6D55914E6F5BF1EAE)

### 服务商邀请特约商户绑定

1. 服务商登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”，在“特约商户绑定的AppID”页签内根据服务商下的特约商户列表，选择特约商户发起AppID绑定申请邀请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/vqkgexfYQKqB2pHZont4vw/zh-cn_image_0000002583479079.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=D0856333A87F7BF829164DCB899D269C462D15964777C556EEBBB83BC77E1544)
2. 特约商户登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)进入“商户中心 > 产品功能 > AppID管理”选择“服务商为我绑定的AppID列表”中的数据，点击去确认，对服务商邀请绑定AppID进行确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/A4nK1VcaRoOHWzOzTcd4nQ/zh-cn_image_0000002552799430.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=61414F68F65E6970D5A774920B944D6FD1F18C2621604E7CE68DCA10562D1640)
3. 特约商户确认绑定AppID后，应用管理员登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站选择对应的项目后，在左侧导航栏选择“盈利 > 鸿蒙支付服务（可在‘全部功能’中搜索服务并固定到导航栏）> 支付服务（非虚拟类）> 待关联商户号”选择对应的商户点击“授权”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/aNx3caA5QyWNdpD26DlGwg/zh-cn_image_0000002583439125.png?HW-CC-KV=V1&HW-CC-Date=20260427T235004Z&HW-CC-Expire=86400&HW-CC-Sign=ED2EB4EA36E2E943A4DD441819C6919E6C5B3AD93FCBFDC93C52F498DCFA83ED)
