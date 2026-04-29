---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-common-pay-external
title: 纯外部支付场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 通用收银台接入 > 纯外部支付场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:33+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8b8c36c714361f51de5d0b0b6dcfcb219f4fc4880f57593fe39731b2a4bc4628
---

## 场景介绍

从5.0.2(14)版本开始，新增支持通用收银台纯外部支付场景。

用户在开发者的应用/元服务中选购完商品，点击下单购买，应用/元服务拉起通用收银台支付仅可以选择三方支付方式完成商品订单的支付。

支持商户模型：不涉及华为支付商户入网。

通用收银台纯外部支付页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/h-BnJoyVQWCk4x98PzRG3g/zh-cn_image_0000002589325463.png?HW-CC-KV=V1&HW-CC-Date=20260429T053932Z&HW-CC-Expire=86400&HW-CC-Sign=475C8E18A0E857AFBE4DE439BBE2B20C3DD52DB4D61A12100E5C41FDA97DB5F8)

## 接入流程

华为支付通用收银台纯外部支付接入流程如下：

| 步骤 | 说明 |
| --- | --- |
| 商户入网（非必选） | **三方支付商户入网（非必选）**  由于三方支付为直接连接第三方支付平台完成支付，故可能涉及需要开发者在第三方支付平台注册、创建商户（建议开发者用新申请的商户号与现有商户号做区分）。 |
| [产品开通与配置](payment-common-pay-introduction.md#产品开通与配置) | 申请开通三方支付及完成相关支付模式配置。 |
| 通用收银台接入 | 根据纯外部支付场景[开发步骤](payment-common-pay-external.md#开发步骤)完成通用收银台支付接入。 |

## 业务流程

纯外部支付模式下，收银台仅支持第三方平台支付，用户无法使用华为支付。具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/_rWgqGHOT2aKZNo8RjkSKQ/zh-cn_image_0000002589245401.png?HW-CC-KV=V1&HW-CC-Date=20260429T053932Z&HW-CC-Expire=86400&HW-CC-Sign=6EA5DBFEFA01C64EA20037C57994C0D396861A5BE8B5D8CEC774794F618003AB)

1. 商户客户端根据商户已开通的支付模式构建[PaymentInfo](../harmonyos-references/payment-paymentservice.md#paymentinfo)参数调用[cashierPicker](../harmonyos-references/payment-paymentservice.md#cashierpicker)接口拉起Payment Kit通用收银台。
2. Payment Kit通用收银台展示可用的三方支付方式，用户选择三方支付方式并确认支付。
3. Payment Kit客户端将用户在通用收银台选择支付方式并确认支付后的支付信息[PickerResult](../harmonyos-references/payment-paymentservice.md#pickerresult)返回给商户客户端。

**基于URL跳转方式拉起收银台：**

1. 商户客户端将支付方式通知给商户服务端。
2. 商户服务端调用三方支付的接口获取支付信息。
3. 三方支付服务端将支付跳转链接信息返回给商户服务端。
4. 商户服务端将支付跳转链接信息返回给商户客户端。
5. 商户客户端构建**订单支付跳转信息**[orderStr](../harmonyos-references/payment-model.md#orderstr)请求Payment Kit的[requestPayment](../harmonyos-references/payment-paymentservice.md#requestpayment)接口跳转三方支付。
6. Payment Kit客户端根据传递的支付消息拉起三方支付收银台。
7. 三方支付客户端展示支付收银台。
8. 用户完成支付操作。
9. 三方支付服务端处理支付。
10. 三方支付服务端同步返回支付状态给三方支付客户端，三方支付客户端展示支付状态后返回商户客户端。
11. 三方支付服务端通过回调接口将支付结果返回给商户服务端。
12. 商户服务端收到支付结果回调请求后，根据三方支付服务要求对支付结果进行验签。

**基于接口拉起方式拉起收银台：**

1. 商户客户端将返回的支付方式上送给商户服务端。
2. 商户服务端获取拉起三方收银台参数，构建[payInfo](../harmonyos-references/payment-model.md#payinfo)（不同三方支付方式拉起收银台参数不同）返回。
3. 商户服务端返回三方支付信息[payInfo](../harmonyos-references/payment-model.md#payinfo)给商户客户端。
4. 商户客户端使用[payInfo](../harmonyos-references/payment-model.md#payinfo)调用Payment Kit的[ThirdPayClient.pay](../harmonyos-references/payment-third-payment-service.md#pay)接口拉起三方支付（可同步通过[ThirdPayClient.handlePayCallback](../harmonyos-references/payment-third-payment-service.md#handlepaycallback)接口调用，获取三方支付操作处理结果）。
5. Payment Kit拉起三方支付收银台。
6. 三方支付客户端展示支付收银台。
7. 用户完成支付操作。
8. 三方支付服务端处理支付。
9. 三方支付服务端同步返回支付状态给三方支付客户端，三方支付客户端展示支付状态后返回商户客户端。
10. 三方支付客户端将用户支付操作完成同步给Payment Kit客户端。
11. Payment Kit客户端通过[ThirdPayClient.handlePayCallback](../harmonyos-references/payment-third-payment-service.md#handlepaycallback)接口，将用户支付操作结果返回给商户客户端。
12. 三方支付服务端通过回调接口将支付结果返回给商户服务端。
13. 商户服务端收到支付结果回调请求后，根据三方支付服务要求对支付结果进行验签，同步返回支付结果给客户端。

## 接口说明

拉起通用收银台接口通过Promise返回结果。具体API说明详见[接口文档](../harmonyos-references/payment-paymentservice.md)。

| 接口名 | 描述 |
| --- | --- |
| cashierPicker(context: common.UIAbilityContext, paymentInfo: PaymentInfo): Promise<PickerResult> | 拉起Payment Kit通用收银台（不含华为支付）。 |
| requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult> | 跳转三方支付收银台。 |
| pay(payInfo: string): Promise<void>; | 拉起三方支付收银台。 |
| handlePayCallback(want: Want): boolean; | 三方支付结果回调同步华为支付收银台。 |

## 开发步骤

### 拉起通用收银台（端侧开发）

商户客户端构建[PaymentInfo](../harmonyos-references/payment-paymentservice.md#paymentinfo)参数调用[cashierPicker](../harmonyos-references/payment-paymentservice.md#cashierpicker)接口拉起Payment Kit通用收银台，用户选择支付方式并确认支付后，Payment Kit客户端将支付信息[PickerResult](../harmonyos-references/payment-paymentservice.md#pickerresult)返回给商户客户端 。

当接口通过.then()方法返回时，则表示当前接口请求响应正常，通过.catch()方法返回表示接口请求响应异常。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/payment-error-code.md)。示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestCashierPickerCallBack() {
10. // use your own paymentInfo
11. const paymentInfo: paymentService.PaymentInfo= {
12. tradeSummary: "***交易",
13. amount: 100,
14. currency: "CNY",
15. extraInfo: '{"***":"***"}'
16. }
17. paymentService.cashierPicker(this.context, paymentInfo)
18. .then((pickerResult: paymentService.PickerResult) => {
19. // succeeded in paying
20. console.info('succeeded in paying, picker result: ', pickerResult);
21. })
22. .catch((error: BusinessError) => {
23. // failed to pay
24. console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
25. });
26. }

28. build() {
29. Column() {
30. Button('requestCashierPickerCallBack')
31. .type(ButtonType.Capsule)
32. .width('50%')
33. .margin(20)
34. .onClick(() => {
35. this.requestCashierPickerCallBack();
36. })
37. }
38. .width('100%')
39. .height('100%')
40. }
41. }
```

### 拉起三方支付收银台（端侧开发）

根据[产品开通与配置](payment-common-pay-introduction.md#产品开通与配置)中的所配置的支付方式，参考[拉起三方支付收银台](payment-launch-third-party-payment-url.md)进行三方支付收银台拉起处理。
