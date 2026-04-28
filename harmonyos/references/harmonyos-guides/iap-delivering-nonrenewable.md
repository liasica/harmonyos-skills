---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-delivering-nonrenewable
title: 权益发放
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 商品购买 > 非续期订阅商品购买 > 权益发放
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:acf053fc14afbd2a830d52670e9ee37caa75ce03715734d408100e56e0e5fe8d
---

## 场景介绍

用户购买商品后，开发者需要及时发放相关权益。但实际应用场景中，若出现异常（网络错误、进程被中止等）将导致应用无法知道用户实际是否支付成功，从而无法及时发放权益，即出现掉单情况。为了确保权益发放，需要在以下场景检查用户是否存在已购未发货的商品：

1. 应用启动时。
2. 购买请求（[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)）返回[iap.IAPErrorCode.PRODUCT\_OWNED](../harmonyos-references/iap-iap.md#iaperrorcode)或[iap.IAPErrorCode.SYSTEM\_ERROR](../harmonyos-references/iap-iap.md#iaperrorcode)时。

如果存在已购未发货商品，则发放相关权益，然后向IAP Kit确认发货，完成购买。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/l85cjHHCQzygTCsAmOwgWQ/zh-cn_image_0000002552799282.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=251D2FDD463934FD59A774D8EB6CD58D2F4C8F76F5905C122AA49538E36A785B)

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，查询用户已购买但未确认发货的订单信息。
2. IAP Kit返回[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。[数据类型说明](../harmonyos-references/iap-data-model.md)为JWS格式的字符串，承载了相关的订单信息。
3. 应用客户端向应用服务器上报[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。
4. 应用服务器需对每个[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsPurchaseOrder进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，验证成功可得到对应的[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)的JSON字符串。
5. 处理权益发放。检查当前[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)是否已发放权益，未发放则发放相关权益，并记录对应的订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。
6. 应用客户端向应用服务器查询订单的发货状态。
7. 应用服务器返回对应的发货状态以及订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。
8. 发货成功后应用客户端向IAP Kit发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)之后，IAP服务器会将相应商品标记为已发货状态。此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订单确认发货](../harmonyos-references/iap-confirm-purchase-for-order.md)接口来确认发货，完成购买流程。

   说明

   * 对于非续期订阅商品，如果不执行此步骤，会导致用户无法再次购买该商品。
   * 确保在发货成功之后再执行此步骤，否则可能导致IAP服务器已经确认发货但是应用没有发货的问题。

## 开发步骤

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，获取用户已购未发货的非续期订阅商品的购买数据。

   在请求参数[QueryPurchasesParameter](../harmonyos-references/iap-iap.md#querypurchasesparameter)中指定对应的productType为NONRENEWABLE，同时指定queryType为[iap.PurchaseQueryType.UNFINISHED](../harmonyos-references/iap-iap.md#purchasequerytype)。当接口请求成功时，IAP Kit将返回一个[QueryPurchaseResult](../harmonyos-references/iap-iap.md#querypurchaseresult)对象，该对象包含承载了订单信息的[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)的列表。
2. 对[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsPurchaseOrder进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)。建议应用客户端将[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata)发送至应用服务器，在应用服务器执行此操作。
3. 验证成功可得到对应的[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)的JSON字符串，如果[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload).purchaseOrderRevocationReasonCode为空，则代表购买成功，需要进行补发货处理。

   建议先检查此笔订单权益的发放状态，未发放则发放权益，成功后记录[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)等信息，用于后续检查权益发放状态。

   注意

   如果开发者在[发起购买](iap-integrate-nonrenewable.md#发起购买)时支持非续期订阅商品的批量购买，则需要在发货时校验下单的商品数量和[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload).quantity是否一致，避免造成漏发、多发的情况。
4. 发货成功后，应用需调用[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)接口确认发货，以此通知IAP服务器更新商品的发货状态，完成购买流程。

   发起请求时，需在请求参数[FinishPurchaseParameter](../harmonyos-references/iap-iap.md#finishpurchaseparameter)中携带[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中的productType、purchaseToken、purchaseOrderId。

   请求成功后，IAP服务器会将相应商品标记为已发货状态。

   说明

   JWSUtil为自定义类，可参见[示例代码](iap-dev-guide.md#示例代码)。

   ```
   1. import { iap } from '@kit.IAPKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. // JWSUtil为自定义类
   5. import { JWSUtil } from '../common/JWSUtil';

   7. @Entry
   8. @Component
   9. struct Index {

   11. queryPurchases(context: common.UIAbilityContext) {
   12. const param: iap.QueryPurchasesParameter = {
   13. productType: iap.ProductType.NONRENEWABLE,
   14. queryType: iap.PurchaseQueryType.UNFINISHED
   15. };
   16. iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
   17. console.info('Succeeded in querying purchases.');
   18. const purchaseDataList: string[] = res.purchaseDataList;
   19. if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
   20. return;
   21. }
   22. for (let i = 0; i < purchaseDataList.length; i++) {
   23. const jwsPurchaseOrder: string = JSON.parse(purchaseDataList[i]).jwsPurchaseOrder;
   24. if (!jwsPurchaseOrder) {
   25. continue;
   26. }
   27. const purchaseStr = JWSUtil.decodeJwsObj(jwsPurchaseOrder);
   28. // 需自定义PurchaseOrderPayload类，包含的信息请参见PurchaseOrderPayload
   29. const purchaseOrderPayload = JSON.parse(purchaseStr) as PurchaseOrderPayload;
   30. // 处理发货
   31. // ...
   32. // 发货成功后向IAP Kit发送finishPurchase请求，确认发货，完成购买
   33. this.finishPurchase(context, purchaseOrderPayload);
   34. }
   35. }).catch((err: BusinessError) => {
   36. // 请求失败
   37. console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
   38. });
   39. }

   41. finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
   42. const finishPurchaseParam: iap.FinishPurchaseParameter = {
   43. productType: Number(purchaseOrder.productType),
   44. purchaseToken: purchaseOrder.purchaseToken,
   45. purchaseOrderId: purchaseOrder.purchaseOrderId
   46. };
   47. iap.finishPurchase(context, finishPurchaseParam).then(() => {
   48. // 请求成功
   49. console.info('Succeeded in finishing purchase.');
   50. }).catch((err: BusinessError) => {
   51. // 请求失败
   52. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
   53. });
   54. }

   56. build() {}
   57. }
   ```
