---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-integrate-subscription
title: 接入自动续期订阅
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 商品购买 > 自动续期订阅商品购买 > 接入自动续期订阅
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:39164832f2ae0a53ad68afa07683b7a8df1cb9efe4c595ebca678a268c7e42d0
---

## 约束与限制

自动续期订阅能力支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19）版本开始，新增支持TV设备。

## 业务流程

说明

如下业务流程对于单机应用同样适用。在单机应用中，应用服务器和应用客户端的交互放在应用客户端完成，应用服务器和IAP服务器交互的部分可不处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Ctp120yjQsqaF7f7uBuRGw/zh-cn_image_0000002558605772.png?HW-CC-KV=V1&HW-CC-Date=20260429T053837Z&HW-CC-Expire=86400&HW-CC-Sign=0378BA60BD500DD9AF3574349D7BEAE957A7A8E9C05739E7567C5D47F9DA42BB)

**展示商品**

1. 应用客户端向IAP Kit发起[queryEnvironmentStatus](../harmonyos-references/iap-iap.md#iapqueryenvironmentstatus)请求，检查当前用户登录的华为账号所在的服务地是否在IAP Kit支持结算的国家/地区中。
2. 应用客户端向IAP Kit发起[queryProducts](../harmonyos-references/iap-iap.md#iapqueryproducts)请求来获取在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置的商品信息。
3. 应用客户端根据返回的商品信息展示可供购买的商品列表，包含商品名称、价格等信息。

**检查权益发放状态**

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，获取当前生效中的订阅列表。IAP Kit返回[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)为JWS格式的字符串，承载了相关的订阅信息。
2. 应用客户端展示商品的订阅状态，需要屏蔽处于自动续期状态的商品的购买入口。同时处理商品的权益发放。
3. 若商品未确认发货，需要在权益发放后，向IAP Kit发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)之后，IAP服务器会将相应商品标记为已发货状态。

   此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口来确认发货，完成购买流程。

具体请参见[对生效中的订阅发放权益](iap-delivering-subscriptions.md#对生效中的订阅发放权益)。

**购买及结果确认**

1. 用户发起购买后，应用客户端向IAP Kit发起[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)购买请求或通过[IAP嵌入式收银台组件](../harmonyos-references/iap-cashier-component.md)发起购买请求（只支持TV），请求中携带商品ID、商品类型等信息。IAP Kit创建订单并展示收银台。
2. 购买结果确认。如购买成功，可通过应用客户端或应用服务器接收购买结果，建议通过应用服务器接收购买结果。

   **方式一：通过客户端接收购买结果**

   1. 用户购买成功时，IAP Kit返回包含订阅状态信息的[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)数据。
   2. 应用客户端向应用服务器上报[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)数据。
   3. 应用服务器对[PurchaseData.jwsSubscriptionStatus](../harmonyos-references/iap-data-model.md#purchasedata)进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，成功后可得到[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload)的JSON字符串。

   **（建议）方式二：通过服务器接收购买结果**

   1. 为了提高安全性，开发者可以接入[服务端关键事件通知](../harmonyos-references/iap-key-event-notifications.md)，在用户购买成功时，IAP服务器将发送订单关键事件通知。
   2. 应用服务器可从NotificationPayload.[NotificationMetaData](../harmonyos-references/iap-key-event-notifications.md#notificationmetadata)中解析出purchaseToken和purchaseOrderId信息，并通过服务端[订阅状态查询](../harmonyos-references/iap-query-subscription-status.md)接口向IAP服务器查询最新的订阅状态信息，进一步确认订阅信息的准确性。
   3. IAP服务器返回订阅组相关订阅状态数据[jwsSubGroupStatus](../harmonyos-references/iap-query-subscription-status.md#response-body)。
   4. 应用服务器对[jwsSubGroupStatus](../harmonyos-references/iap-query-subscription-status.md#response-body)进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，成功后可得到[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload)的JSON字符串。

说明

如果购买失败，请参见[确保权益发放](iap-delivering-subscriptions.md#确保权益发放)处理，及时发放权益。

**发放权益**

1. 确认购买成功后，需要处理权益发放。检查[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder是否已发放权益，未发放则需发放相关权益，并记录对应的订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)），用于后续检查权益发放状态。

   说明

   建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。
2. 应用客户端向应用服务器查询订单的发货状态。
3. 应用服务器返回对应的发货状态以及订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。
4. 发货成功后应用客户端向IAP Kit发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)之后，IAP服务器会将相应商品标记为已发货状态，后续该商品即可正常续期。

   此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口来确认发货，完成购买流程。

   说明

   对于自动续期订阅商品，如果不执行此步骤，会导致后续自动续期无法扣费，以及同一个订阅组不同自动续期订阅商品无法切换等问题。

## 开发步骤

### 展示商品

1. 检查应用引入IAP Kit的可用性。

   在使用应用内支付之前，应用客户端需要向IAP Kit发送[queryEnvironmentStatus](../harmonyos-references/iap-iap.md#iapqueryenvironmentstatus)请求，以此判断用户当前登录的华为账号所在的服务地是否在IAP Kit支持结算的国家/地区中。

   说明

   当前IAP Kit支持结算的国家/地区仅有中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

   ```
   1. import { iap } from '@kit.IAPKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. queryEnvironmentStatus(context: common.UIAbilityContext) {
   9. iap.queryEnvironmentStatus(context).then(() => {
   10. // 请求成功
   11. console.info('Succeeded in querying environment status.');
   12. }).catch((err: BusinessError) => {
   13. // 请求失败
   14. // 如果接口返回错误码“1001860054 用户账号所在服务地不在IAP Kit支持结算的国家/地区中”，应用需隐藏相关IAP功能入口
   15. console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
   16. });
   17. }

   19. build() {}
   20. }
   ```
2. 展示商品列表。

   应用客户端通过[queryProducts](../harmonyos-references/iap-iap.md#iapqueryproducts)来获取在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置的商品信息。发起请求时，需在请求参数[QueryProductsParameter](../harmonyos-references/iap-iap.md#queryproductsparameter)中携带相关的商品ID，并指定其productType为[iap.ProductType.AUTORENEWABLE](../harmonyos-references/iap-iap.md#producttype)。

   当接口请求成功时，IAP Kit将返回商品信息[Product](../harmonyos-references/iap-iap.md#product)的列表。 应用可以使用[Product](../harmonyos-references/iap-iap.md#product)包含的商品价格、名称和描述等信息，向用户展示可供购买的商品列表。

   说明

   [queryProducts](../harmonyos-references/iap-iap.md#iapqueryproducts)每次只能查询一种商品类型的商品，每次最多查询200个商品，否则请求将报错。

   ```
   1. import { iap } from '@kit.IAPKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {

   9. queryProducts(context: common.UIAbilityContext) {
   10. const queryProductParam: iap.QueryProductsParameter = {
   11. productType: iap.ProductType.AUTORENEWABLE,
   12. // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
   13. productIds: ['product1', 'product2', 'product3']
   14. };
   15. iap.queryProducts(context, queryProductParam).then((result) => {
   16. // 请求成功
   17. console.info('Succeeded in querying products.');
   18. // 展示商品信息
   19. // ...
   20. }).catch((err: BusinessError) => {
   21. // 请求失败
   22. console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
   23. });
   24. }

   26. build() {}
   27. }
   ```

### 展示订阅状态、发放权益

1. 应用获取用户当前生效中的订阅列表。
2. 应用客户端展示对应商品的订阅状态。此处需要屏蔽处于自动续期状态的商品的购买入口。
3. 处理生效中的订阅的权益发放。

具体可参见[对生效中的订阅发放权益](iap-delivering-subscriptions.md#对生效中的订阅发放权益)。

### 发起购买

用户发起购买时，应用可通过向IAP Kit发送[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)请求来拉起IAP Kit收银台或通过[IAP嵌入式收银台组件](../harmonyos-references/iap-cashier-component.md)发起购买请求（只支持TV）。发起请求时，应用需在请求参数[PurchaseParameter](../harmonyos-references/iap-iap.md#purchaseparameter)中携带此前已在华为[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站上配置并生效的自动续期订阅的商品ID，并指定其productType为[iap.ProductType.AUTORENEWABLE](../harmonyos-references/iap-iap.md#producttype)。

说明

开发过程中易出现频繁调用接口的现象，建议控制接口调用频度，具体可参见[1001860004 接口访问过频](../harmonyos-references/iap-error-code.md#section1001860004-接口访问过频)。

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {

9. subscribe(context: common.UIAbilityContext) {
10. const createPurchaseParam: iap.PurchaseParameter = {
11. productType: iap.ProductType.AUTORENEWABLE,
12. // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
13. productId: 'test001'
14. };
15. iap.createPurchase(context, createPurchaseParam).then((result) => {
16. console.info('Succeeded in creating purchase.');
17. // 购买成功，处理购买结果
18. // dealPurchaseResult实现请参见下一步
19. this.dealPurchaseResult(result);
20. }).catch((err: BusinessError) => {
21. // 购买失败
22. console.error(`Failed to create purchase. Code is ${err.code}, message is ${err.message}`);
23. // dealPurchaseError实现请参见下一步
24. this.dealPurchaseError(err);
25. })
26. }

28. build() {}
29. }
```

### 购买结果处理

**【结果1：购买成功】**

说明

1. 为了提高安全性，建议应用服务器接入[服务端关键事件通知](../harmonyos-references/iap-key-event-notifications.md)以接收购买成功结果并通过应用服务器来处理[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)、完成购买等操作。
2. 请务必确保发货成功后再执行完成购买步骤，本步骤可通过请求服务端[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口来确认发货，完成购买流程。

以下内容为**通过客户端接收购买结果**及处理的步骤说明。

1. 当用户购买成功时，应用将接收到一个[CreatePurchaseResult](../harmonyos-references/iap-iap.md#createpurchaseresult)对象，其[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata)字段包括了此次购买的结果信息。
2. 对[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsSubscriptionStatus进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，验证成功可得到[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload)的JSON字符串。建议应用客户端将[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata)发送至应用服务器，在应用服务器执行此操作。
3. 验签成功后，检查[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.status是否为1（生效中），是则发放相关权益。

   建议先检查此笔订单权益的发放状态，未发放则发放权益，成功后记录[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder等信息，用于后续检查权益发放状态。
4. 完成购买。

   发放权益后，应用需发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求确认发货，以此通知IAP服务器更新商品的发货状态，完成购买流程。发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求时，需在请求参数[FinishPurchaseParameter](../harmonyos-references/iap-iap.md#finishpurchaseparameter)中携带[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中的productType、purchaseToken、purchaseOrderId，其中[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)为[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder。请求成功后，IAP服务器会将相应商品标记为已发货。

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

11. /**
12. * 购买结果处理
13. *
14. * @param result 商品购买结果
15. */
16. dealPurchaseResult(context: common.UIAbilityContext, result: iap.CreatePurchaseResult) {
17. const jwsSubscriptionStatus: string = JSON.parse(result.purchaseData).jwsSubscriptionStatus;
18. if (!jwsSubscriptionStatus) {
19. return;
20. }
21. const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
22. if (!subscriptionStatus) {
23. return;
24. }
25. // 需自定义SubGroupStatusPayload类，包含的信息请参见SubGroupStatusPayload
26. const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
27. const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
28. if (!lastSubscriptionStatus || lastSubscriptionStatus.status !== '1') {
29. return;
30. }
31. const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
32. if (purchaseOrderPayload === undefined) {
33. return;
34. }
35. // 处理发货
36. // ...
37. // 发货成功后向IAP Kit发送finishPurchase请求，确认发货，完成购买
38. this.finishPurchase(context, purchaseOrderPayload);
39. }

41. /**
42. * 确认发货，完成购买
43. *
44. * @param purchaseOrder 订单信息，来源于购买请求
45. */
46. finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
47. const finishPurchaseParam: iap.FinishPurchaseParameter = {
48. productType: Number(purchaseOrder.productType),
49. purchaseToken: purchaseOrder.purchaseToken,
50. purchaseOrderId: purchaseOrder.purchaseOrderId
51. };
52. iap.finishPurchase(context, finishPurchaseParam).then(() => {
53. // 请求成功
54. console.info('Succeeded in finishing purchase.');
55. }).catch((err: BusinessError) => {
56. // 请求失败
57. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
58. });
59. }

61. build() {}
62. }
```

**【结果2：购买失败】**

当用户购买失败时，需要针对code为[iap.IAPErrorCode.PRODUCT\_OWNED](../harmonyos-references/iap-iap.md#iaperrorcode)和[iap.IAPErrorCode.SYSTEM\_ERROR](../harmonyos-references/iap-iap.md#iaperrorcode)的场景，检查是否需要补发货，确保权益发放，具体请参见[确保权益发放](iap-delivering-subscriptions.md#确保权益发放)。

```
1. import { iap } from '@kit.IAPKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. dealPurchaseError(err: BusinessError) {
5. if (err.code === iap.IAPErrorCode.PRODUCT_OWNED || err.code === iap.IAPErrorCode.SYSTEM_ERROR) {
6. // 参见确保权益发放检查是否需要补发货，确保权益发放
7. // ...
8. }
9. }
```
