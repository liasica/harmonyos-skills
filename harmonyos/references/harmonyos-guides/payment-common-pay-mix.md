---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-common-pay-mix
title: 混合支付场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 通用收银台接入 > 混合支付场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74210b43edd2e5403b7d8ce676667ca721ca0729ff9dd17e4ab95ddae19b28d9
---

## 场景介绍

从5.0.2(14)版本开始，新增支持通用收银台混合支付场景。

用户在开发者的应用/元服务中选购完商品，点击确认支付，应用/元服务拉起通用收银台支付时，用户可以在通用收银台支付方式中选择华为支付方式或第三方支付方式完成商品订单的支付。

支持商户模型：直连商户、平台类商户、服务商

通用收银台混合支付页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/O2UhAP2ZQpKQXwrzlSB38w/zh-cn_image_0000002583479091.png?HW-CC-KV=V1&HW-CC-Date=20260427T235008Z&HW-CC-Expire=86400&HW-CC-Sign=C5E7CA70348712F8B1583C252300AF0796EAABB24DA187F56851C707C19F2832)

## 接入流程

华为支付通用收银台混合支付接入流程如下：

| 步骤 | 说明 |
| --- | --- |
| [商户入网及开发准备](payment-merc-regist-apply.md) | - **华为支付商户入网及开发准备**  在准备开发前，商户需要在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)入网及完成开发准备操作。  支持的商户模型：直连商户、平台商户、服务商。  商户模型详细内容请参见[接入模式](../pay-docs/hwzf-hezuoshenfen-0000001725918617.md)。  - **三方支付商户入网（非必选）**  由于三方支付直接连接第三方支付平台完成支付，故可能需要开发者在第三方支付平台注册、创建商户（建议开发者用新申请的商户号与现有商户号做区分）。 |
| [产品开通与配置](payment-common-pay-introduction.md#产品开通与配置) | 接入通用收银台，商户入网后需与华为支付业务侧沟通（合作咨询可[点击此处](payment-service-support.md)）后申请开通三方支付及完成相关支付模式配置。 |
| 通用收银台接入 | 根据混合支付场景[开发步骤](payment-common-pay-mix.md#开发步骤)完成通用收银台支付接入。 |

## 业务流程

混合支付模式，收银台上用户可选择华为支付或三方支付方式支付。具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/0A_bdbgURCum4Wr4nnG3kg/zh-cn_image_0000002552799442.png?HW-CC-KV=V1&HW-CC-Date=20260427T235008Z&HW-CC-Expire=86400&HW-CC-Sign=57DCCF345E4CFE8FFF8773BBD9659960D4AB5DB889BB012D2D77F650ACA96542)

1. 商户客户端请求商户服务器创建订单。
2. 商户服务器按照商户模型调用Payment Kit服务端[直连商户预下单](../harmonyos-references/payment-prepay.md)或[平台类商户/服务商预下单](../harmonyos-references/payment-agent-prepay.md)接口。
3. Payment Kit服务端返回预支付ID（prepayId）。
4. 商户服务端构建**订单支付信息**[orderStr](../harmonyos-references/payment-model.md#orderstr)返回给商户客户端。
5. 商户客户端调用[requestPayment](../harmonyos-references/payment-paymentservice.md#paymentservicerequestpayment)接口拉起Payment Kit通用收银台。
6. Payment Kit客户端展示含华为支付方式的通用收银台，根据用户所选择的不同支付方式完成支付操作。

### 选择华为支付场景

1. 用户选择华为支付方式支付，Payment Kit客户端向Payment Kit服务端发起支付请求。
2. Payment Kit服务端处理支付操作。
3. Payment Kit服务端同步返回支付状态给Payment Kit客户端，Payment Kit客户端展示支付状态后返回商户客户端。
4. Payment Kit服务端通过回调接口将支付结果返回给商户服务端。
5. 商户服务端收到支付结果回调响应后，使用[SM2验签方式](../harmonyos-references/payment-rest-overview.md#验签规则)对支付结果进行验签

### 选择三方支付场景

1. 用户选择三方支付方式并确认支付。
2. Payment Kit客户端将用户在通用收银台选择支付方式并确认支付后的支付信息[PayResult](../harmonyos-references/payment-paymentservice.md#payresult)返回给商户客户端。

**基于URL跳转方式拉起收银台：**

3-1-1. 商户客户端将支付方式通知给商户服务端。

3-1-2. 商户服务端调用三方支付的接口获取支付信息。

3-1-3. 三方支付服务端将支付跳转链接信息返回给商户服务端。

3-1-4. 商户服务端将支付跳转链接信息返回给商户客户端。

3-1-5. 商户客户端构建**订单支付跳转信息**[orderStr](../harmonyos-references/payment-model.md#orderstr)调用Payment Kit的[requestPayment](../harmonyos-references/payment-paymentservice.md#paymentservicerequestpayment)接口跳转三方支付。

3-1-6. Payment Kit客户端根据传递的支付消息拉起三方支付收银台。

3-1-7. 三方支付客户端展示支付收银台。

3-1-8. 用户完成支付操作。

3-1-9. 三方支付服务端处理支付。

3-1-10. 三方支付服务端同步返回支付状态给三方支付客户端，三方支付客户端展示支付状态后返回商户客户端。

3-1-11. 三方支付服务端通过回调接口将支付结果返回给商户服务端。

3-1-12. 商户服务端收到支付结果回调请求后，根据三方支付服务要求对支付结果进行验签。

**基于接口拉起方式拉起收银台：**

3-2-1. 商户客户端将返回的支付方式上送给商户服务端。

3-2-2. 商户服务端获取拉起三方收银台参数，构建[payInfo](../harmonyos-references/payment-model.md#payinfo)（不同三方支付方式拉起收银台参数不同）返回。

3-2-3. 商户服务端返回三方支付信息[payInfo](../harmonyos-references/payment-model.md#payinfo)给商户客户端。

3-2-4. 商户客户端使用[payInfo](../harmonyos-references/payment-model.md#payinfo)调用Payment Kit的[ThirdPayClient.pay](../harmonyos-references/payment-third-payment-service.md#pay)接口拉起三方支付（可同步通过[ThirdPayClient.handlePayCallback](../harmonyos-references/payment-third-payment-service.md#handlepaycallback)接口调用，获取三方支付操作处理结果）。

3-2-5. Payment Kit拉起三方支付收银台。

3-2-6. 三方支付客户端展示支付收银台。

3-2-7. 用户完成支付操作。

3-2-8. 三方支付服务端处理支付。

3-2-9. 三方支付服务端同步返回支付状态给三方支付客户端，三方支付客户端展示支付状态后返回商户客户端。

3-2-10. 三方支付客户端将用户支付操作完成同步给Payment Kit客户端。

3-2-11. Payment Kit客户端通过[ThirdPayClient.handlePayCallback](../harmonyos-references/payment-third-payment-service.md#handlepaycallback)接口，将用户支付操作结果返回给商户客户端。

3-2-12. 三方支付服务端通过回调接口将支付结果返回给商户服务端。

3-2-13. 商户服务端收到支付结果回调请求后，根据三方支付服务要求对支付结果进行验签，同步返回支付结果给客户端。

## 接口说明

混合支付场景拉起通用收银台接口通过Promise返回结果。具体API说明详见[接口文档](../harmonyos-references/payment-paymentservice.md)。

| 接口名 | 描述 |
| --- | --- |
| requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult> | 支持拉起Payment Kit通用收银台（含华为支付）、跳转三方支付收银台。 |
| pay(payInfo: string): Promise<void>; | 拉起三方支付收银台。 |
| handlePayCallback(want: Want): boolean; | 三方支付结果回调同步华为支付收银台。 |

## 开发步骤

### 华为支付预下单（服务端开发）

1. 开发者按照商户模型调用[直连商户预下单](../harmonyos-references/payment-prepay.md)或[平台类商户/服务商预下单](../harmonyos-references/payment-agent-prepay.md)接口获取预支付ID（prepayId）。

   为保证支付订单的安全性和可靠性需要对请求body和请求头PayMercAuth对象内的入参排序拼接进行签名。可参考[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)。
2. 构建订单信息参数[orderStr](../harmonyos-references/payment-model.md#orderstr)并返回给客户端。业务接口请求示例代码可参考[业务接口请求](payment-server-connect.md#业务接口请求)。

### 拉起通用收银台（端侧开发）

商户客户端使用[orderStr](../harmonyos-references/payment-model.md#orderstr)作为参数调用[requestPayment](../harmonyos-references/payment-paymentservice.md#paymentservicerequestpayment)接口拉起Payment Kit支付收银台。

当接口通过.then()方法返回时，则表示当前接口请求响应正常，通过.catch()方法返回表示接口请求响应异常。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/payment-error-code.md)。示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestPaymentPromise() {
10. // used orderStr to pay for an order, use your own orderStr.
11. const orderStr = '{"app_id":"***","merc_no":"***","prepay_id":"xxx","timestamp":"1680259863114","noncestr":"1487b8a60ed9f9ecc0ba759fbec23f4f","sign":"****","auth_id":"***"}';
12. paymentService.requestPayment(this.context, orderStr, "")
13. .then((payResult: paymentService.PayResult) => {
14. // succeeded in paying
15. console.info('succeeded in paying, pay result: ', payResult);
16. })
17. .catch((error: BusinessError) => {
18. // failed to pay
19. console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
20. });
21. }

23. build() {
24. Column() {
25. Button('requestPaymentPromise')
26. .type(ButtonType.Capsule)
27. .width('50%')
28. .margin(20)
29. .onClick(() => {
30. this.requestPaymentPromise();
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

### 支付处理

**场景1：用户选择华为支付方式支付**

用户选择华为支付方式支付，通用收银台会直接处理支付，支付成功后华为支付服务器会调用开发者提供的回调接口，将支付信息返回给开发者的服务器，回调详细信息按商户模式请参见[直连商户支付结果回调通知](../harmonyos-references/payment-pay-notify.md)或[平台类商户/服务商支付结果回调通知](../harmonyos-references/payment-agent-pay-notify.md)。

为保证信息合法性，商户服务器需要对返回的支付信息进行[SM2验签](../harmonyos-references/payment-rest-overview.md#验签规则)，验签注意事项：

1. 需直接使用通知的完整内容进行验签。
2. 验签前需要对返回数据进行排序拼接，sign字段是签名值，排序拼接后的待验签内容需要排除sign字段。
3. 验签公钥使用[华为支付证书](payment-certificates-config.md#华为支付证书)。

说明

* 如果用户没有提前登录，系统会自动拉起华为账号登录页面让用户登录。
* 支付成功，不建议以客户端返回作为用户的支付结果，需以服务器接收到的结果通知或者查询API返回为准。
* 回调接口是开发者调用预下单时的入参字段callbackUrl。

**场景2：用户选择三方支付方式支付**

开发者需要根据[产品开通与配置](payment-common-pay-introduction.md#产品开通与配置)中的所配置的支付方式，参考[拉起三方支付收银台](payment-launch-third-party-payment-url.md)不同方式进行三方支付收银台拉起处理。
