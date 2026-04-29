---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-delivering-subscriptions
title: 权益发放
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 商品购买 > 自动续期订阅商品购买 > 权益发放
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bfb8f7fce13080f4d96f497061a30b5fa469516de9a984f3886d05737dfebae5
---

## 对生效中的订阅发放权益

### 场景介绍

用户购买自动续期订阅商品后，若订阅处于生效状态，开发者需要及时给用户发放对应权益。

在应用启动时，获取用户当前处于生效状态的订阅列表，处理此部分订阅的权益发放。建议先检查当前订阅对应权益的发放状态，未发放再补充发放权益。在权益发放成功后，向IAP确认发货，完成购买。

建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。

### 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/qiL9jJvdQvOsYvXkV4NLxA/zh-cn_image_0000002589325299.png?HW-CC-KV=V1&HW-CC-Date=20260429T053837Z&HW-CC-Expire=86400&HW-CC-Sign=21D557430906340F86EDF6EFCAC7FCF6BE0839E650767E86133583A988F4CA5C)

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，查询用户生效中的订阅列表。
2. IAP Kit返回[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)为JWS格式的字符串，承载了相关的订阅信息。
3. 应用客户端向应用服务器上报[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。
4. 应用服务器需对每个[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsSubscriptionStatus进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，验证成功可得到对应的[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload)的JSON字符串。
5. 处理权益发放。检查[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder是否已发放权益，未发放则需发放相关权益，并记录对应的订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。

   说明

   建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。
6. 应用客户端向应用服务器查询订单的发货状态。
7. 应用服务器返回对应的发货状态以及订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。
8. 发放权益后应用客户端向IAP Kit发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)之后，IAP服务器会将相应商品标记为已发货状态。此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口来确认发货，完成购买流程。

   说明

   对于自动续期订阅商品，如果不执行此步骤，会导致后续自动续期无法扣费 ，以及同一个订阅组不同自动续期订阅商品无法切换等问题。

### 开发步骤

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，获取生效中的订阅列表。

   在请求参数[QueryPurchasesParameter](../harmonyos-references/iap-iap.md#querypurchasesparameter)中指定productType为[iap.ProductType.AUTORENEWABLE](../harmonyos-references/iap-iap.md#producttype)，同时指定queryType为[iap.PurchaseQueryType.CURRENT\_ENTITLEMENT](../harmonyos-references/iap-iap.md#purchasequerytype)。当接口请求成功时，IAP Kit将返回一个[QueryPurchaseResult](../harmonyos-references/iap-iap.md#querypurchaseresult)对象，该对象包含承载了订阅信息的[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)的列表。
2. 验证订单信息。对每个[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsSubscriptionStatus进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，验证成功可得到[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload)的JSON字符串。建议应用客户端将[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata)发送至应用服务器，在应用服务器执行此操作。

   为了提高安全性，可从[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder中解析出purchaseToken和purchaseOrderId信息，并通过服务端[订阅状态查询](../harmonyos-references/iap-query-subscription-status.md)接口向IAP服务器查询最新的订阅状态信息，进一步确认订阅信息的准确性。
3. 展示订阅状态。

   * 如果[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.status=1，表示订阅处于生效状态。
   * 如果[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.status=1且[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.renewalInfo.autoRenewStatusCode值为1时，表示订阅处于自动续期状态。此状态的商品无法再次购买，需要屏蔽相关的购买入口。
4. 权益发放。获取[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder（下文标记为[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)），处理权益发放。

   可先检查此笔订单权益的发放状态，未发放则补充发放权益，成功后记录[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)等信息，用于后续检查权益发放状态。

   说明

   建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。
5. 在发放权益后，如果[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload).finishStatus不为1，应用需调用[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)接口确认发货，完成购买流程。

   发起请求时，需在请求参数[FinishPurchaseParameter](../harmonyos-references/iap-iap.md#finishpurchaseparameter)中携带[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中的productType、purchaseToken、purchaseOrderId。请求成功后，IAP服务器会将相应商品标记为已发货。

   说明

   此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口来确认发货，完成购买流程。

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
13. productType: iap.ProductType.AUTORENEWABLE,
14. queryType: iap.PurchaseQueryType.CURRENT_ENTITLEMENT
15. };
16. iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
17. console.info('Succeeded in querying purchases.');
18. const purchaseDataList: string[] = res.purchaseDataList;
19. if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
20. return;
21. }
22. for (let i = 0; i < purchaseDataList.length; i++) {
23. const jwsSubscriptionStatus: string = JSON.parse(purchaseDataList[i]).jwsSubscriptionStatus;
24. if (!jwsSubscriptionStatus) {
25. continue;
26. }
27. // 对jwsSubscriptionStatus进行解码验签
28. const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
29. // 需自定义SubGroupStatusPayload类，包含的信息请参见SubGroupStatusPayload
30. const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
31. const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
32. if (!lastSubscriptionStatus) {
33. continue;
34. }

36. // 根据status判断订阅的状态
37. const status = lastSubscriptionStatus.status;
38. // 更新商品的订阅状态
39. // ...

41. // 处理权益发放
42. const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
43. if (purchaseOrderPayload === undefined) {
44. continue;
45. }
46. if (status === '1') {
47. // 订阅处于生效状态
48. // 处理权益发放。检查此笔订单权益的发放状态，未发放则补充发放权益
49. // ...
50. }
51. // 发放权益后向IAP Kit发送finishPurchase请求，确认发货，完成购买
52. if (purchaseOrderPayload && purchaseOrderPayload.finishStatus !== '1') {
53. this.finishPurchase(context, purchaseOrderPayload);
54. }
55. }
56. }).catch((err: BusinessError) => {
57. // 请求失败
58. console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
59. })
60. }

62. finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
63. const finishPurchaseParam: iap.FinishPurchaseParameter = {
64. productType: Number(purchaseOrder.productType),
65. purchaseToken: purchaseOrder.purchaseToken,
66. purchaseOrderId: purchaseOrder.purchaseOrderId
67. };
68. iap.finishPurchase(context, finishPurchaseParam).then(() => {
69. // 请求成功
70. console.info('Succeeded in finishing purchase.');
71. }).catch((err: BusinessError) => {
72. // 请求失败
73. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
74. });
75. }

77. build() {}
78. }
```

## 确保权益发放

用户购买自动续期订阅成功或者自动续期成功后，开发者需要及时给用户发放相关权益。但实际应用场景中，若出现异常（网络错误等）将导致应用无法知道用户实际是否支付成功，从而无法及时发放权益，即出现掉单情况。

为了确保权益发放，需要在[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)请求返回[iap.IAPErrorCode.PRODUCT\_OWNED](../harmonyos-references/iap-iap.md#iaperrorcode)或[iap.IAPErrorCode.SYSTEM\_ERROR](../harmonyos-references/iap-iap.md#iaperrorcode)时检查用户是否存在已购但未确认发货的商品，如果存在则发放相关权益，然后向IAP Kit确认发货，完成购买。

### 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/gV_SjJhlRyu4EORmAmU5Aw/zh-cn_image_0000002589245235.png?HW-CC-KV=V1&HW-CC-Date=20260429T053837Z&HW-CC-Expire=86400&HW-CC-Sign=915D1C967D935EF4F8B354C87888CD574610FCEC52B489B02F215BE13F713D14)

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，查询用户已购买但未确认发货的订阅列表。
2. IAP Kit返回[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)为JWS格式的字符串，承载了相关的订阅信息。
3. 应用客户端向应用服务器上报[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)列表。
4. 应用服务器需对每个[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsSubscriptionStatus进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，验证成功可得到对应的[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload)的JSON字符串。
5. 处理权益发放。检查[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder是否已发放权益，未发放则需发放相关权益，并记录对应的订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。

   说明

   建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。
6. 应用客户端向应用服务器查询订单的发货状态。
7. 应用服务器返回对应的发货状态以及订单信息（[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)）。
8. 发放权益后应用客户端向IAP Kit发送[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)之后，IAP服务器会将相应商品标记为已发货状态。此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口来确认发货，完成购买流程。

   说明

   对于自动续期订阅商品，如果不执行此步骤，会导致后续自动续期无法扣费 ，以及同一个订阅组不同自动续期订阅商品无法切换等问题。

### 开发步骤

1. 应用客户端向IAP Kit发起[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)请求，获取用户已购但未确认发货的订阅列表。

   在请求参数[QueryPurchasesParameter](../harmonyos-references/iap-iap.md#querypurchasesparameter)中指定productType为[iap.ProductType.AUTORENEWABLE](../harmonyos-references/iap-iap.md#producttype)，同时指定queryType为[iap.PurchaseQueryType.UNFINISHED](../harmonyos-references/iap-iap.md#purchasequerytype)。当接口请求成功时，IAP Kit将返回一个[QueryPurchaseResult](../harmonyos-references/iap-iap.md#querypurchaseresult)对象，该对象包含承载了订阅信息的[PurchaseData](../harmonyos-references/iap-data-model.md#purchasedata)的列表。
2. 验证订单信息。对每个[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata).jwsSubscriptionStatus进行[解码验签](../harmonyos-references/iap-verifying-signature.md#jws解码和验签)，验证成功可得到[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload)的JSON字符串。建议应用客户端将[purchaseData](../harmonyos-references/iap-data-model.md#purchasedata)发送至应用服务器，在应用服务器执行此操作。

   为了提高安全性，可从[SubGroupStatusPayload](../harmonyos-references/iap-data-model.md#subgroupstatuspayload).lastSubscriptionStatus.lastPurchaseOrder中解析出purchaseToken和purchaseOrderId信息，并通过服务端[订阅状态查询](../harmonyos-references/iap-query-subscription-status.md)接口向IAP服务器查询最新的订阅状态信息，进一步确认订阅信息的准确性。
3. 处理权益发放。

   如果SubGroupStatusPayload.lastSubscriptionStatus.status=1，表示订阅处于生效状态。需要对生效状态的订阅处理权益发放。建议先检查此笔订单权益的发放状态，未发放则补充发放权益，成功后记录[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)等信息，用于后续检查权益发放状态。

   建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。
4. 在发放权益后，如果PurchaseOrderPayload.finishStatus不为1，应用需调用[finishPurchase](../harmonyos-references/iap-iap.md#iapfinishpurchase)接口确认发货，完成购买流程。

   发起请求时，需在请求参数[FinishPurchaseParameter](../harmonyos-references/iap-iap.md#finishpurchaseparameter)中携带[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中的productType、purchaseToken、purchaseOrderId。请求成功后，IAP服务器会将相应商品标记为已发货。

   说明

   此步骤也可放到应用服务器处理。应用服务器可通过请求服务端[订阅确认发货](../harmonyos-references/iap-confirm-purchase-for-sub.md)接口来确认发货，完成购买流程。

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
13. productType: iap.ProductType.AUTORENEWABLE,
14. queryType: iap.PurchaseQueryType.UNFINISHED
15. };
16. iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
17. console.info('Succeeded in querying purchases.');
18. const purchaseDataList: string[] = res.purchaseDataList;
19. if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
20. return;
21. }
22. for (let i = 0; i < purchaseDataList.length; i++) {
23. const jwsSubscriptionStatus: string = JSON.parse(purchaseDataList[i]).jwsSubscriptionStatus;
24. if (!jwsSubscriptionStatus) {
25. continue;
26. }
27. // 对jwsSubscriptionStatus进行解码验签
28. const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
29. // 需自定义SubGroupStatusPayload类，包含的信息请参见SubGroupStatusPayload
30. const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
31. const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
32. if (!lastSubscriptionStatus) {
33. continue;
34. }

36. // 根据status判断订阅的状态
37. const status = lastSubscriptionStatus.status;
38. // 更新商品的订阅状态
39. // ...

41. // 处理权益发放
42. const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
43. if (purchaseOrderPayload === undefined) {
44. continue;
45. }
46. if (status === '1') {
47. // 订阅处于生效状态
48. // 处理权益发放。检查此笔订单权益的发放状态，未发放则补充发放权益
49. // ...
50. }
51. // 发放权益后向IAP Kit发送finishPurchase请求，确认发货，完成购买
52. if (purchaseOrderPayload && purchaseOrderPayload.finishStatus !== '1') {
53. this.finishPurchase(context, purchaseOrderPayload);
54. }
55. }
56. }).catch((err: BusinessError) => {
57. // 请求失败
58. console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
59. })
60. }

62. finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
63. const finishPurchaseParam: iap.FinishPurchaseParameter = {
64. productType: Number(purchaseOrder.productType),
65. purchaseToken: purchaseOrder.purchaseToken,
66. purchaseOrderId: purchaseOrder.purchaseOrderId
67. };
68. iap.finishPurchase(context, finishPurchaseParam).then(() => {
69. // 请求成功
70. console.info('Succeeded in finishing purchase.');
71. }).catch((err: BusinessError) => {
72. // 请求失败
73. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
74. });
75. }

77. build() {}
78. }
```
