---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-digital-cny-pay
title: 数字人民币支付场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 数字人民币支付场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:32+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:93acb9183d13109e77159a0eaee849344307778ef6d36600c810c15ade2df1b9
---

说明

1. 用户手机端rom版本过低可能导致应用闪退，建议开发者对开放接口抛出的异常错误进行捕获并进行处理。
2. 华为钱包最低版本要求为 **1.0.8.305**。

## 场景介绍

从5.0.1(13)版本开始，新增支持数字人民币支付场景。

例如用户需要通过数字钱包充值话费，此时用户可打开商户APP应用，选好充值金额发起支付，商户通过接入数字人民币支付服务，拉起数字人民币收银台完成订单支付。

支持商户模型：[运营机构或受理服务机构入网的商户](payment-digital-cny-pay-preparations.md)

数字人民币收银台展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/7YoL41WbRMqte9OPiUHN2w/zh-cn_image_0000002558605934.png?HW-CC-KV=V1&HW-CC-Date=20260429T053931Z&HW-CC-Expire=86400&HW-CC-Sign=D180D12E3EF6278EC5FA7B5B607DD75E51B2708774A7DE8AE4E6723BDD8C8433)

## 接入流程

数字人民币支付接入流程如下：

| 步骤 | 说明 |
| --- | --- |
| 开发准备 | 请先完成开发准备后再进行下面的开发接入。  - [数字人民币接入准备](payment-digital-cny-pay-preparations.md) |
| 接入数字人民币支付 | 根据数字人民币支付场景[开发步骤](payment-digital-cny-pay.md#开发步骤)完成接入。 |

## 业务流程

开发者接入数字人民币支付服务，可以快速实现应用的数字人民币支付能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ot8-_tQuTEm65B3_bD3UAA/zh-cn_image_0000002589325461.png?HW-CC-KV=V1&HW-CC-Date=20260429T053931Z&HW-CC-Expire=86400&HW-CC-Sign=153C2742AA7ACF66C774293E78F914A0E315A2C7CE146B471CABBACED59E1BD4)

1. 商户客户端请求商户服务器创建商品订单。
2. 商户服务器按照商户模式（运营机构商户或受理服务机构商户）调用运营机构或受理服务机构提供的下单接口到数字人民币服务端下单，接口详情请参照商户合作的[运营机构或受理服务机构提供的开发指引](payment-faq-27.md)。
3. 数字人民币服务端返回订单加密信息。
4. 商户服务端组建订单信息参数[orderInfo](../harmonyos-references/payment-ecnypaymentservice.md#ecnyorderinfo)返回给商户客户端。
5. 商户客户端调用[requestEcnyPayment](../harmonyos-references/payment-ecnypaymentservice.md#requestecnypayment)接口拉起Payment Kit客户端数字人民币收银台。
6. Payment Kit客户端展示数字人民币支付收银台。
7. 用户通过收银台选择数字人民币钱包完成支付，Payment Kit客户端请求数字人民币服务端处理支付。
8. 数字人民币服务端成功受理支付订单并处理支付。
9. 数字人民币服务端将支付结果返回给Payment Kit客户端。
10. Payment Kit客户端展示支付结果页。
11. 用户关闭支付结果页后Payment Kit客户端会返回支付状态给商户客户端。
12. 支付处理完成后，数字人民币服务端会异步通知支付结果信息给商户服务端。

## 接口说明

接口返回值返回形式为Promise。具体API说明详见[接口文档](../harmonyos-references/payment-ecnypaymentservice.md)。

| 接口名 | 描述 |
| --- | --- |
| requestEcnyPayment(context:common.Context, orderInfo: EcnyOrderInfo): Promise<EcnyPayResult>; | 拉起数字人民币收银台。 |

## 开发步骤

### 获取开发指引

拨打数字人民币客服热线（956196）获取运营机构或受理服务机构提供的开发指引。

### 预下单（服务器开发）

开发者需要按照运营机构或受理服务机构提供的开发指引进行开发。

### 拉起数字人民币收银台（端侧开发）

商户客户端使用[orderInfo](../harmonyos-references/payment-ecnypaymentservice.md#ecnyorderinfo)作为参数调用[requestEcnyPayment](../harmonyos-references/payment-ecnypaymentservice.md#requestecnypayment)接口拉起数字人民币收银台。

当接口通过.then()方法返回时，则表示当前订单支付成功，通过.catch()方法返回表示订单支付失败。

当此次请求有异常时，可通过error.code获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/payment-error-code.md)。

示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ecnyPaymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestEcnyPaymentPromise() {
10. // use your own orderInfo
11. const orderInfo: ecnyPaymentService.EcnyOrderInfo = {
12. merchantAppId: "***",
13. merchantNo: "***",
14. acqAgtInstnId: "***",
15. creditorInstitutionId: "***",
16. encryptedKey: "***",
17. encryptedInfo: "***",
18. encryptionSN: "***",
19. extraInfo: "***",
20. lastWalletId: "***"
21. };
22. ecnyPaymentService.requestEcnyPayment(this.context, orderInfo)
23. .then((result: ecnyPaymentService.EcnyPayResult) => {
24. // pay success
25. console.info(`succeeded in paying, result.orderNo: ${result.orderNo}, result.extraInfo: ${result.extraInfo}`);
26. })
27. .catch((error: BusinessError) => {
28. // failed to pay
29. console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
30. });
31. }

33. build() {
34. Column() {
35. Button('requestEcnyPaymentPromise')
36. .type(ButtonType.Capsule)
37. .width('50%')
38. .margin(20)
39. .onClick(() => {
40. this.requestEcnyPaymentPromise();
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

说明

* 如果初次使用数字人民币收银台，系统会自动通过拉起数字人民币元服务，完成授权登录。
* 支付成功，不建议以客户端返回作为用户的支付结果，需以服务器接收到的结果通知或者查询API返回为准。

### 支付结果回调通知（服务器开发）

开发者需要按照运营机构或受理服务机构提供的开发指引进行开发。
