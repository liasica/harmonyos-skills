---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-third-payment-service
title: thirdPaymentService(三方支付服务)
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > ArkTS API > thirdPaymentService(三方支付服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:060fa78a5406e82c13150abe398961254a6f4dd29d904c8aeeced1007335c183
---

本模块提供直接通过依赖包拉起第三方支付方式收银台能力。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1Tablet

```
1. import { thirdPaymentService } from '@kit.PaymentKit';
```

## PayMethod

PhonePC/2in1Tablet

三方支付方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WECHAT\_PAY | wechat\_pay | 微信支付。 |
| ALI\_PAY | ali\_pay | 支付宝支付。 |
| WECHAT\_MINI\_PROGRAM | wechat\_mini\_program | 拉起微信小程序。 |

## ThirdPayClient

PhonePC/2in1Tablet

支付请求客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

### constructor

PhonePC/2in1Tablet

constructor(context: common.UIAbilityContext, payMethod: PayMethod, thirdAppId: string);

构造器，构造三方支付等请求客户端ThirdPayClient实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文。 |
| payMethod | [PayMethod](payment-third-payment-service.md#paymethod) | 是 | 支付方式。 |
| thirdAppId | string | 是 | 三方支付应用appID。 |

**示例**：

```
1. import { thirdPaymentService } from '@kit.PaymentKit';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. thirdPayClient = new thirdPaymentService.ThirdPayClient(this.getUIContext().getHostContext() as common.UIAbilityContext, thirdPaymentService.PayMethod.WECHAT_PAY, "third_appid_123456");

9. build() { }
10. }
```

### pay

PhonePC/2in1Tablet

pay(payInfo: string): Promise<void>;

该方法提供拉起三方支付方式收银台等功能，调用方法前请确保网络已连接，调用该方法后会拉起三方支付收银台，完成后使用Promise异步返回。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| payInfo | string | 是 | 拉起收银台传入的订单信息，payInfo是json字符串的格式（具体参数根据三方支付方式拉起收银台要求传递，参考[payInfo](payment-model.md#payinfo)）。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022830000 | The operation was canceled by the user. |
| 1022830001 | Pay failed. |
| 1022830002 | The payInfo invalid. Possible causes: 1.Data format is not json string; 2.Mandatory parameters are left unspecified. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { thirdPaymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. export let thirdPayClient: thirdPaymentService.ThirdPayClient | undefined = undefined;

7. @Entry
8. @Component
9. struct Index {
10. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
11. thirdPaymentServicePayPromise() {
12. thirdPayClient = new thirdPaymentService.ThirdPayClient(this.context, thirdPaymentService.PayMethod.WECHAT_PAY, "appid_123456");
13. // 不同支付方式参数构建参考示例如下：
14. // PayMethod.WECHAT_PAY：'{"appId":"***","partnerId":"***","prepayId":"***","packageValue":"***","nonceStr":"***","timeStamp":"***","sign":"***","extData":"***","token":"***"}'
15. // PayMethod.ALI_PAY：'{"orderInfo":"***", "token":"***"}'
16. // PayMethod.WECHAT_MINI_PROGRAM：'{"userName":"原始id", "path":"小程序启动路径", "miniProgramType":"小程序的类型，0-正式版 1-开发版 2-体验版 默认0", "extData":"***", "token":"***"}'
17. const payInfo = '{"xxx1":"***", "xxx2":"***", "token":"***"}';
18. thirdPayClient.pay(payInfo).then(() => {
19. // succeeded in paying
20. console.info('succeeded in paying.');
21. }).catch((error: BusinessError) => {
22. // failed to pay
23. console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
24. });
25. }

27. build() {
28. Column() {
29. Button('thirdPaymentServicePayPromise')
30. .type(ButtonType.Capsule)
31. .width('50%')
32. .margin(20)
33. .onClick(() => {
34. this.thirdPaymentServicePayPromise();
35. })
36. }
37. .width('100%')
38. .height('100%')
39. }
40. }
```

### handlePayCallback

PhonePC/2in1Tablet

handlePayCallback(want: Want): boolean;

该方法提供处理支付处理结果回调功能，调用方法前请确保网络已连接，请求处理完成后使用返回布尔类型结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ThirdPaymentService

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| want | common.[Want](js-apis-app-ability-want.md) | 是 | 应用组件间的信息传递的载体。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 回调处理结果（该结果为用户支付操作处理结果，非实际支付结果，实际支付结果以三方支付结果为准）。  - true：用户支付操作成功  - false：用户支付操作失败 |

**示例**：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { UIAbility, Want } from '@kit.AbilityKit';
3. // 需要从thirdPayClient对象定义的代码文件中导入三方支付客户端对象，以下为示例，具体以应用定义路径为准。
4. import { thirdPayClient } from '../pages/thirdPaymentServicetest';

6. // 如果已有Ability实现类，可直接添加onNewWant生命周期方法处理即可。
7. export default class EntryAbility extends UIAbility {
8. onNewWant(want: Want): void {
9. // 需要和拉起支付收银台的三方支付客户端对象为同一个
10. if (thirdPayClient) {
11. hilog.info(0x0000, 'testTag', '%{public}s','clientForThirdPayment handlePayCallback');
12. let handlePayCallback = thirdPayClient.handlePayCallback(want);
13. hilog.info(0x0000, 'testTag', 'clientForThirdPayment handlePayCallback result: %{public}s', handlePayCallback);
14. }
15. }
16. }
```
