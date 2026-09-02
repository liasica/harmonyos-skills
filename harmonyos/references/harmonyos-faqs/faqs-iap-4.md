---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-4
title: 单机应用/元服务是否可以接入应用内支付
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 单机应用/元服务是否可以接入应用内支付
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:205bf93745140e0d02d8fd009a48022c171795616f81eb77992d790132e301bc
---

## 问题现象

单机应用、单机元服务，是否可以接入IAP Kit应用内支付服务？

## 背景知识

* [IAP Kit（应用内支付服务）](../harmonyos-guides/iap-introduction.md)为开发者提供便捷的应用内支付体验和简便的接入流程，让开发者聚焦应用本身的业务能力，助力开发者商业变现。开发者应用可通过使用IAP Kit提供的系统级支付API快速启动IAP收银台，即可实现应用内支付。
* 可参考[支付-应用内支付服务（ArkTS）](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_IAPKit-ArkTS)。

## 解决方案

单机应用或单机元服务可以接入IAP Kit应用内支付服务。

* 必须使用华为IAP收银台完成支付流程，禁止直接接入第三方支付（如微信/支付宝）。
* 需通过@kit.IAPKit模块调用系统级支付API，示例代码可参考[开发消耗型商品购买](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_IAPKit-ArkTS#:~:text=7-,开发消耗型商品购买,-本章节为)。

## 常见FAQ

Q：官网描述必须先开通商户服务，若需在应用内开通此类订阅制会员服务，经营类目具体应该属于哪一类？

A：是的，需要先[开通商户服务](../start/merchant-service-0000001053025967.md)，具体经营类目应根据App实际情况进行选择，可以参考[经营类目及特殊资质说明](../hwzf-jingyingleimu-0000001426308945.md)进行选择。

Q：根据[IAP支付文档](../harmonyos-guides/iap-integrate-purchase.md)，单机应用支持接入IAP支付，但是支付需要联网，断网情况下不能正常支付，这种应该属于单机应用核心功能断裂，是否会在应用上架时被驳回不允许选择为单机应用？

A：如果确定是单机应用仅接入了IAP支付，在备案信息中选择单机应用，应用上架时在备注中说明情况，就不会被驳回不允许选择为单机应用。

Q：单机应用如何实现打赏开发者功能？

A：在HarmonyOS中为单机应用实现打赏功能，可通过华为IAP Kit（应用内支付服务）完成支付流程，具体接入方案可参考以上解决方案。

Q：后台调用[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口如何实现业务流程？

A：为了确保权益发放，需要在[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)请求返回[iap.IAPErrorCode.PRODUCT\_OWNED](../harmonyos-references/iap-iap.md#iaperrorcode)或[iap.IAPErrorCode.SYSTEM\_ERROR](../harmonyos-references/iap-iap.md#iaperrorcode)时检查用户是否存在已购但未确认发货的商品，如果存在则发放相关权益，然后向IAP Kit确认发货，完成购买。业务流程详见文档：[确保权益发放](../harmonyos-guides/iap-delivering-subscriptions.md#确保权益发放)。
