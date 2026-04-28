---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-delivering-products
title: 权益发放
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 商品购买 > 消耗型/非消耗型商品购买 > 权益发放
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d03ac5789c9f5904f1582dc42d023387ccdfc84d1291223fbf8851c4a97c86a7
---

## 场景介绍

应用在收到用户购买消耗型/非消耗型商品成功的结果后，需要发放相关权益，并在权益发放后，向IAP Kit确认发货，完成购买流程，具体实现请参见[接入购买](iap-integrate-purchase.md)。此外，还需要补充如下处理，确保权益发放：

* 若应用提供消耗型商品，需要按照[确保权益发放](iap-delivering-products.md#确保权益发放)处理消耗型商品的权益发放。
* 若应用提供非消耗型商品，且为单机应用，则需要按照[单机应用权益发放（非消耗型商品）](iap-delivering-products.md#单机应用权益发放非消耗型商品)处理非消耗型商品的权益发放。其他场景需要按照[确保权益发放](iap-delivering-products.md#确保权益发放)处理非消耗型商品的权益发放。

## 确保权益发放

用户购买商品后，开发者需要及时发放相关权益。但实际应用场景中，若出现异常（网络错误、进程被中止等）将导致应用无法知道用户实际是否支付成功，从而无法及时发放权益，即出现掉单情况。为了确保权益发放，需要在以下场景检查用户是否存在已购未发货的商品：

1. 应用启动时。
2. 购买请求（[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)）返回[iap.IAPErrorCode.PRODUCT\_OWNED](../harmonyos-references/iap-iap.md#iaperrorcode)或[iap.IAPErrorCode.SYSTEM\_ERROR](../harmonyos-references/iap-iap.md#iaperrorcode)时。

如果存在已购未发货商品，则发放相关权益，然后向IAP Kit确认发货，完成购买。

### 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/hQL3KN_kTLaPe3c5nEi_8g/zh-cn_image_0000002552799276.png?HW-CC-KV=V1&HW-CC-Date=20260427T234926Z&HW-CC-Expire=86400&HW-CC-Sign=A8A868F4D105902898773392F2F337C9D0D12B1C70EF155B64A065D640AE0479)

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，查询用户已购买但未确认发货的订单信息。
2. IAP Kit返回[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)为JWS格式的字符串，承载了相关的订单信息。
3. 应用客户端向应用服务器上报[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。
4. 应用服务器需对每个[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsPurchaseOrder进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，验证成功可得到对应的[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)的JSON字符串。
5. 处理权益发放。检查当前[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)是否已发放权益，未发放则发放相关权益，并记录对应的订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。
6. 应用客户端向应用服务器查询订单的发货状态。
7. 应用服务器返回对应的发货状态以及订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。
8. 发货成功后应用客户端向IAP Kit发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)之后，IAP服务器会将相应商品标记为已发货状态。此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订单确认发货](../harmonyos-references/iap-confirm-purchase-for-order.md)接口来确认发货，完成购买流程。

   说明

   * 对于消耗型商品，IAP服务器会将相应商品重新设置为可购买状态，用户即可再次购买该商品。如果不执行此步骤，会导致用户无法再次购买该商品。
   * 确保在发货成功之后再执行此步骤，否则可能导致IAP服务器已经确认发货但是应用没有发货的问题。

### 开发步骤

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，获取用户已购买但未确认发货的订单信息。

   在请求参数[QueryPurchasesParameter](../harmonyos-references/iap-iap.md#querypurchasesparameter)中指定对应的productType，同时指定queryType为[iap.PurchaseQueryType.UNFINISHED](../harmonyos-references/iap-iap.md#purchasequerytype)。当接口请求成功时，IAP Kit将返回一个[QueryPurchaseResult](../harmonyos-references/iap-iap.md#querypurchaseresult)对象，该对象包含承载了订单信息的[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)的列表。
2. 对[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsPurchaseOrder进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)。建议应用客户端将[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata)发送至应用服务器，在应用服务器执行此操作。
3. 验证成功可得到对应的[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)的JSON字符串，如果[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload).purchaseOrderRevocationReasonCode为空，则代表购买成功，需要进行补发货处理。

   建议先检查此笔订单权益的发放状态，未发放则发放权益，成功后记录[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)等信息，用于后续检查权益发放状态。

   注意

   如果开发者在[发起购买](iap-integrate-purchase.md#发起购买)时支持消耗型商品的批量购买，则需要在发货时校验下单的商品数量和[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload).quantity是否一致，避免造成漏发、多发的情况。
4. 发货成功后，应用需调用[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)接口确认发货，以此通知IAP服务器更新商品的发货状态，完成购买流程。

   发起请求时，需在请求参数[FinishPurchaseParameter](../harmonyos-references/iap-iap.md#finishpurchaseparameter)中携带[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中的productType、purchaseToken、purchaseOrderId。

   请求成功后，IAP服务器会将相应商品标记为已发货状态。对于消耗型商品，IAP服务器会将相应商品重新设置为可购买状态，用户即可再次购买该商品。对于非消耗型商品，用户购买后永久拥有，无法再次购买该商品。

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
   10. queryPurchases(context: common.UIAbilityContext,) {
   11. const param: iap.QueryPurchasesParameter = {
   12. // iap.ProductType.CONSUMABLE：消耗型商品
   13. // iap.ProductType.NONCONSUMABLE：非消耗型商品
   14. productType: iap.ProductType.CONSUMABLE,
   15. queryType: iap.PurchaseQueryType.UNFINISHED
   16. };
   17. iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
   18. console.info('Succeeded in querying purchases.');
   19. const purchaseDataList: string[] = res.purchaseDataList;
   20. if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
   21. return;
   22. }
   23. for (let i = 0; i < purchaseDataList.length; i++) {
   24. const jwsPurchaseOrder: string = JSON.parse(purchaseDataList[i]).jwsPurchaseOrder;
   25. if (!jwsPurchaseOrder) {
   26. continue;
   27. }
   28. const purchaseStr = JWSUtil.decodeJwsObj(jwsPurchaseOrder);
   29. // 需自定义PurchaseOrderPayload类，包含的信息请参见PurchaseOrderPayload
   30. const purchaseOrderPayload = JSON.parse(purchaseStr) as PurchaseOrderPayload;
   31. // 处理发货
   32. // ...
   33. // 发货成功后向IAP Kit发送finishPurchase请求，确认发货，完成购买
   34. this.finishPurchase(context, purchaseOrderPayload);
   35. }
   36. }).catch((err: BusinessError) => {
   37. // 请求失败
   38. console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
   39. });
   40. }

   42. finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
   43. const finishPurchaseParam: iap.FinishPurchaseParameter = {
   44. productType: Number(purchaseOrder.productType),
   45. purchaseToken: purchaseOrder.purchaseToken,
   46. purchaseOrderId: purchaseOrder.purchaseOrderId
   47. };
   48. iap.finishPurchase(context, finishPurchaseParam).then(() => {
   49. // 请求成功
   50. console.info('Succeeded in finishing purchase.');
   51. }).catch((err: BusinessError) => {
   52. // 请求失败
   53. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
   54. });
   55. }

   57. build() {}
   58. }
   ```

## 单机应用权益发放（非消耗型商品）

用户在购买非消耗型商品后，将永久拥有该商品的权益。应用需要在用户购买非消耗型商品后，始终为其发放相关权益。

请在以下场景获取用户已购非消耗型商品的信息，并发放相关权益。

1. 应用启动时。
2. 购买请求（[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)）返回[iap.IAPErrorCode.PRODUCT\_OWNED](../harmonyos-references/iap-iap.md#iaperrorcode)或[iap.IAPErrorCode.SYSTEM\_ERROR](../harmonyos-references/iap-iap.md#iaperrorcode)时。

注意

为了在卸载重装、更换设备安装等场景下保障用户权益，需要在应用首次打开时，应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，查询用户已购非消耗型商品，完成权益恢复。

### 开发步骤

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，获取用户已购非消耗型商品的订单状态信息。

   在请求参数[QueryPurchasesParameter](../harmonyos-references/iap-iap.md#querypurchasesparameter)中指定productType为[iap.ProductType.NONCONSUMABLE](../harmonyos-references/iap-iap.md#producttype)，同时指定queryType为[iap.PurchaseQueryType.CURRENT\_ENTITLEMENT](../harmonyos-references/iap-iap.md#purchasequerytype)。当接口请求成功时，IAP Kit将返回一个[QueryPurchaseResult](../harmonyos-references/iap-iap.md#querypurchaseresult)对象，该对象包含承载了订单信息的[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)的列表。
2. 对每个[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsPurchaseOrder进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)。
3. 验证成功可得到对应的[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)的JSON字符串，此时需要发放相关权益。
4. 发放权益后，应用需调用[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)接口确认发货，以此通知IAP服务器更新商品的发货状态，完成购买流程。

   发起请求时，需在请求参数[FinishPurchaseParameter](../harmonyos-references/iap-iap.md#finishpurchaseparameter)中携带[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中的productType、purchaseToken、purchaseOrderId。

   请求成功后，IAP服务器会将相应商品标记为已发货。对于非消耗型商品，用户购买后永久拥有，无法再次购买该商品。

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
10. queryPurchases(context: common.UIAbilityContext) {
11. const param: iap.QueryPurchasesParameter = {
12. productType: iap.ProductType.NONCONSUMABLE,
13. queryType: iap.PurchaseQueryType.CURRENT_ENTITLEMENT
14. };
15. iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
16. console.info('Succeeded in querying purchases.');
17. const purchaseDataList: string[] = res.purchaseDataList;
18. if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
19. return;
20. }
21. for (let i = 0; i < purchaseDataList.length; i++) {
22. const jwsPurchaseOrder: string = JSON.parse(purchaseDataList[i]).jwsPurchaseOrder;
23. if (!jwsPurchaseOrder) {
24. continue;
25. }
26. // 对jwsPurchaseOrder进行解码验签
27. const purchaseStr = JWSUtil.decodeJwsObj(jwsPurchaseOrder);
28. // 需自定义PurchaseOrderPayload类，包含的信息请参见PurchaseOrderPayload
29. const purchaseOrderPayload = JSON.parse(purchaseStr) as PurchaseOrderPayload;
30. // 处理权益发放
31. // ...
32. // 发放权益后向IAP Kit发送finishPurchase请求，确认发货，完成购买
33. if (purchaseOrderPayload && purchaseOrderPayload.finishStatus !== '1') {
34. this.finishPurchase(context, purchaseOrderPayload);
35. }
36. }
37. }).catch((err: BusinessError) => {
38. // 请求失败
39. console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
40. });
41. }

43. finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
44. const finishPurchaseParam: iap.FinishPurchaseParameter = {
45. productType: Number(purchaseOrder.productType),
46. purchaseToken: purchaseOrder.purchaseToken,
47. purchaseOrderId: purchaseOrder.purchaseOrderId
48. };
49. iap.finishPurchase(context, finishPurchaseParam).then(() => {
50. // 请求成功
51. console.info('Succeeded in finishing purchase.');
52. }).catch((err: BusinessError) => {
53. // 请求失败
54. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
55. });
56. }

58. build() {}
59. }
```
