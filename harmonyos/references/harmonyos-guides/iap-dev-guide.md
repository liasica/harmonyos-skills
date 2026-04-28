---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-dev-guide
title: 使用入门
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 使用入门
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d096cd9ddc9b1c9aaa41a57ab77ed90d15cfc36236e4027a86fb4a04766a2af
---

## 快速上手体验

在正式开发应用之前，开发者可以通过[Codelab](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_IAPKit-ArkTS)快速体验一个应用的开发过程。

## 开发流程

开发者需要按照流程来完成应用的开发工作，完整的开发流程如下。

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | [开通商户服务](iap-enable-merchant-service.md) | 在开发应用前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作。其中**配置签名信息**时，请使用**手动签名**方式。  开发者需开通商户服务才能开启应用内购买服务。商户服务里配置的银行卡账号、币种，用于开发者接收华为分成收益。 |
| 2 | [创建项目和应用](iap-create-project-and-application.md) | 在开始应用开发前，开发者需要先在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上完成项目和应用的创建。 |
| 3 | [开启和激活应用内购买服务](iap-enable-in-app-purchases.md) | 开发者需开启和激活应用内购买服务才能使用华为应用内支付服务。 |
| 4 | [（可选）配置应用内购买服务参数](iap-set-necessary-parameters.md) | - 配置订单/订阅通知接收地址。  - 配置密钥。 |
| 5 | [配置商品信息](iap-config-product.md) | 开发者需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中完成相关商品配置。在应用调用购买接口时，需传入此处配置的商品ID和商品类型。 |
| 6 | [配置签名](iap-config-sign.md) | 开发者需要在IDE上完成签名配置，确保能顺利完成项目的编译与开发 |
| 7 | [配置应用身份信息](iap-config-app-identity-info.md) | 在应用工程中配置bundleName、Client ID。 |
| 8 | [商品购买](iap-integrate-purchase.md) | - [开发消耗型、非消耗型商品购买功能](iap-integrate-purchase.md)：接入消耗型、非消耗型商品购买功能，主要包括商品列表展示、购买、权益发放等，具体请参见[接入购买](iap-integrate-purchase.md)。  - [开发自动续期订阅商品购买功能](iap-subscription-functions.md)：开发者可通过[自动续期订阅说明](iap-subscription-functions.md)了解订阅的相关概念以及支持的功能。具体开发过程可参见[接入自动续期订阅](iap-integrate-subscription.md)。  - [开发非续期订阅商品购买功能](iap-integrate-nonrenewable.md)：接入非续期订阅商品购买功能，主要包括商品列表展示、购买、权益发放等，具体请参见[接入购买](iap-integrate-nonrenewable.md)。  **说明：** 在开发过程中，可通过[沙盒测试](iap-sandbox.md)辅助功能测试。沙盒测试允许开发者在接入华为应用内支付调测过程中无需真实支付即可完成购买测试。 |

## 示例代码

开发者可参见[示例代码](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-clientdemo-arkts)了解如何在应用中提供消耗型商品、非消耗型商品、自动续期订阅商品购买能力。
