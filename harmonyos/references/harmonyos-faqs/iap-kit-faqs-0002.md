---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/iap-kit-faqs-0002
title: 单机应用与元服务接入IAP Kit支付常见问题
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 常见问题 > 单机应用与元服务接入IAP Kit支付常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:43+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:6c736a97379092983d3156a3b643f9674c18ff6b358b2129b7be42142f4607e5
---

**Q：单机应用、单机元服务，是否可以接入IAP Kit应用内支付服务？**

**A**：单机应用或单机元服务可以接入IAP Kit应用内支付服务。

* 必须使用华为IAP收银台完成支付流程。
* 需通过@kit.IAPKit模块调用系统级支付API，示例代码可参考[开发消耗型商品购买](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_IAPKit-ArkTS#:~:text=7-,开发消耗型商品购买,-本章节为)。

**Q：官网描述必须先开通商户服务，若需在应用内开通此类订阅制会员服务，经营类目具体应该属于哪一类？**

**A**：是的，需要先[开通商户服务](../app/hdc-merchant-service-0000002752616107.md)，具体经营类目应根据App实际情况进行选择，可以参考[经营类目及特殊资质说明](../hwzf-jingyingleimu-0000001426308945.md)进行选择。

**Q：根据[IAP支付文档](../doccenter-capabilities/iap-integrate-purchase.md)，单机应用支持接入IAP支付，但是支付需要联网，断网情况下不能正常支付，这种应该属于单机应用核心功能断裂，是否会在应用上架时被驳回不允许选择为单机应用？**

**A**：如果确定是单机应用仅接入了IAP支付，在备案信息中选择单机应用，应用上架时在备注中说明情况，就不会被驳回不允许选择为单机应用。

**Q：后台调用[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口如何实现业务流程？**

**A**：为了确保权益发放，需要在[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)请求返回[iap.IAPErrorCode.PRODUCT\_OWNED](../harmonyos-references/iap-iap.md#iaperrorcode)或[iap.IAPErrorCode.SYSTEM\_ERROR](../harmonyos-references/iap-iap.md#iaperrorcode)时检查用户是否存在已购但未确认发货的商品，如果存在则发放相关权益，然后向IAP Kit确认发货，完成购买。业务流程详见文档：[确保权益发放](../harmonyos-guides/iap-delivering-subscriptions.md#确保权益发放)。

**Q：Google Billing是否有HarmonyOS适配版本？**

**A**：当前没有Google Billing的HarmonyOS适配版本。应用内支付可使用[IAP Kit（应用内支付服务）](../harmonyos-guides/iap-introduction.md)实现。

**Q：海外的手表设备如何接入IAP Kit应用内支付？**

**A**：在华为IAP覆盖的国家/地区中，海外（中国大陆以外）目前仅支持Wearable（手表）设备使用[IAP Kit（应用内支付服务）](../harmonyos-guides/iap-introduction.md)，接入方式与手机端一致，通过IAP Kit提供的系统级支付API拉起收银台即可完成数字商品购买。需要注意以下两点：商品类型方面，手表设备仅支持消耗型商品和非消耗型商品，自动续期订阅商品和非续期订阅商品均不支持Wearable设备；签约主体方面，接入前需线下签署《华为数字商品及联运服务协议》（联系华为商务），海外仅支持企业开发者签约，个人开发者无法在海外开通。

**Q：接入IAP应用内支付，服务器部署在香港，是否会影响客户付款？**

**A**：不会影响客户付款。服务器部署在香港不影响IAP应用内支付的支付流程。
