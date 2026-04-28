---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-paymentservice
title: paymentService (鸿蒙支付服务)
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > ArkTS API > paymentService (鸿蒙支付服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:29ce7a44728116f47628dcad6c5f3b1453abdb48c38a839bd5b4d745b1b068aa
---

本模块提供支付、签约服务能力，包括基础支付、支付并签约、合单支付、签约代扣等。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1Tablet

```
1. import { paymentService } from '@kit.PaymentKit';
```

## PayResult

PhonePC/2in1Tablet

用户在通用收银台选择支付方式并确认支付后的支付信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.2(14)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| selectedPaymentType | string | 否 | 是 | 用户选择的支付方式。  - wechat\_pay：微信支付  - ali\_pay：支付宝支付  - 其他（其他为商户申请配置三方支付方式时所申请的三方支付相关配置） |
| clientToken | string | 否 | 是 | 客户端凭证。 |
| nextStep | string | 否 | 是 | 下一步支付流程。 |
| [extraInfo](payment-model.md#extrainfo) | string | 否 | 是 | 保留字段。json string格式。 |
| [payload](payment-model.md#payload) | string | 否 | 是 | 预留信息，在请求接口时，入参如果传递，接口响应中则会原样返回。  **说明：** 拉起H5支付场景下需要固定传递“AP”。 |

## PaymentInfo

PhonePC/2in1Tablet

三方支付拉起通用收银台时传入的支付订单信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.2(14)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tradeSummary | string | 否 | 是 | 订单的摘要信息。若未填写，默认为空。 |
| amount | number | 否 | 是 | 订单总金额（单位：分）。 |
| currency | string | 否 | 是 | 货币单位。若未填写，默认为空。  **说明：**  - 不传递则收银台不显示货币单位。  - 传递后收银台可以转换成货币符号则显示货币符号（比如￥），转换不了则显示所传递的值。 |
| [extraInfo](payment-model.md#extrainfo) | string | 否 | 是 | 保留字段。json string格式。若未填写，默认为空。  **说明：** 商户可以通过保留字段指定支付方式。指定收银台支付方式列表传递内容示例为{"selectPayType":"wechat\_pay|xxx"}。 |

## PickerResult

PhonePC/2in1Tablet

三方支付拉起通用收银台时响应给开发者的订单支付信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.2(14)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| selectedPaymentType | string | 否 | 是 | 用户选择的支付方式。  - wechat\_pay：微信支付  - ali\_pay：支付宝支付  - 其他（其他为商户申请配置三方支付方式时所申请的相关配置） |
| clientToken | string | 否 | 是 | 客户端凭证。 |

## BindCardResult

PhonePC/2in1Tablet

绑卡结果信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.5(17)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.5(17)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| hasBankCard | boolean | 否 | 否 | 用户当前是否有已绑定的银行卡。  - true：是  - false：否 |
| hasJustBoundCard | boolean | 否 | 是 | 用户在拉起绑卡管理页面后是否完成了绑卡。  - true：是  - false：否 |

## paymentService.requestPayment

PhonePC/2in1Tablet

requestPayment(context: common.UIAbilityContext, orderStr: string): Promise<void>

该方法提供基础支付、支付并签约等功能，调用方法前请确保网络已连接，调用该方法后会拉起Payment Kit收银台，支付完成后使用Promise异步返回。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文，不传会报401参数错误。 |
| [orderStr](payment-model.md#orderstr) | string | 是 | 拉起收银台传入的订单信息，[orderStr](payment-model.md#orderstr)是json字符串的格式。不传会报401参数错误。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001930000 | The operation was canceled by the user. |
| 1001930001 | Pay failed. |
| 1001930002 | The transaction has been processed. |
| 1001930010 | Duplicate request. |
| 1001930011 | Network connection error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestPaymentPromise() {
10. // use your own orderStr
11. const orderStr = '{"app_id":"***","merc_no":"***","prepay_id":"xxx","timestamp":"1680259863114","noncestr":"1487b8a60ed9f9ecc0ba759fbec23f4f","sign":"****","auth_id":"***"}';
12. paymentService.requestPayment(this.context, orderStr)
13. .then(() => {
14. // succeeded in paying
15. console.info('succeeded in paying');
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

## paymentService.requestPayment

PhonePC/2in1Tablet

requestPayment(context: common.UIAbilityContext, orderStr: string, callback: AsyncCallback<void>): void

该方法提供基础支付、支付并签约等功能，调用该方法前请确保网络已连接，调用该方法后会拉起Payment Kit收银台，支付完成后通过AsyncCallback回调结果。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文，不传会报401参数错误。 |
| [orderStr](payment-model.md#orderstr) | string | 是 | 拉起收银台传入的订单信息，[orderStr](payment-model.md#orderstr)是json字符串的格式。不传会报401参数错误。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当支付成功，error为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001930000 | The operation was canceled by the user. |
| 1001930001 | Pay failed. |
| 1001930002 | The transaction has been processed. |
| 1001930010 | Duplicate request. |
| 1001930011 | Network connection error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestPaymentCallBack() {
10. // use your own orderStr
11. const orderStr = '{"app_id":"***","merc_no":"***","prepay_id":"xxx","timestamp":"1680259863114","noncestr":"1487b8a60ed9f9ecc0ba759fbec23f4f","sign":"****","auth_id":"***"}';
12. paymentService.requestPayment(this.context, orderStr, (error: BusinessError) => {
13. if (error) {
14. // failed to pay
15. console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
16. return;
17. }
18. // succeeded in paying
19. console.info('succeeded in paying');
20. })
21. }

23. build() {
24. Column() {
25. Button('requestPaymentCallBack')
26. .type(ButtonType.Capsule)
27. .width('50%')
28. .margin(20)
29. .onClick(() => {
30. this.requestPaymentCallBack();
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

## paymentService.requestContract

PhonePC/2in1Tablet

requestContract(context: common.UIAbilityContext, contractStr: string): Promise<void>

该方法提供签约功能，调用方法前请确保网络已连接，调用该方法后会拉起Payment Kit签约收银台，签约完成后使用Promise异步返回。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文，不传会报401参数错误。 |
| [contractStr](payment-model.md#contractstr) | string | 是 | 拉起签约收银台入参，[contractStr](payment-model.md#contractstr)是json字符串的格式。不传会报401参数错误。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001930000 | The operation was canceled by the user. |
| 1001930002 | The transaction has been processed. |
| 1001930003 | Withhold failed. |
| 1001930010 | Duplicate request. |
| 1001930011 | Network connection error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestContractPromise() {
10. // use your own contractStr
11. const contractStr = '{"appId":"***","preSignNo":"***"}';
12. paymentService.requestContract(this.context, contractStr)
13. .then(() => {
14. // succeeded in signing
15. console.info('succeeded in signing');
16. })
17. .catch((error: BusinessError) => {
18. // failed to sign
19. console.error(`failed to sign, error.code: ${error.code}, error.message: ${error.message}`);
20. });
21. }

23. build() {
24. Column() {
25. Button('requestContractPromise')
26. .type(ButtonType.Capsule)
27. .width('50%')
28. .margin(20)
29. .onClick(() => {
30. this.requestContractPromise();
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

## paymentService.requestContract

PhonePC/2in1Tablet

requestContract(context: common.UIAbilityContext, contractStr: string, callback: AsyncCallback<void>): void

该方法提供签约功能，调用该方法前请确保网络已连接，调用该方法后会拉起Payment Kit签约收银台，签约完成后通过AsyncCallback回调结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文，不传会报401参数错误。 |
| [contractStr](payment-model.md#contractstr) | string | 是 | 拉起签约收银台入参，[contractStr](payment-model.md#contractstr)是json字符串的格式。不传会报401参数错误。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当签约成功，error为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001930000 | The operation was canceled by the user. |
| 1001930002 | The transaction has been processed. |
| 1001930003 | Withhold failed. |
| 1001930010 | Duplicate request. |
| 1001930011 | Network connection error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestContractCallBack() {
10. // use your own contractStr
11. const contractStr = '{"appId":"***","preSignNo":"***"}';
12. paymentService.requestContract(this.context, contractStr, (error: BusinessError) => {
13. if (error) {
14. // failed to sign
15. console.error(`failed to sign, error.code: ${error.code}, error.message: ${error.message}`);
16. return;
17. }
18. // succeeded in signing
19. console.info('succeeded in signing');
20. })
21. }

23. build() {
24. Column() {
25. Button('requestContractCallBack')
26. .type(ButtonType.Capsule)
27. .width('50%')
28. .margin(20)
29. .onClick(() => {
30. this.requestContractCallBack();
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

## paymentService.requestPayment

PhonePC/2in1Tablet

requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult>

该方法提供拉起通用收银台、跳转三方支付功能，调用方法前请确保网络已连接，用户在通用收银台选择支付方式并确认支付后，使用Promise异步返回。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.2(14)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文，不传会报401参数错误。 |
| [orderStr](payment-model.md#orderstr) | string | 是 | 拉起收银台或跳转三方支付传入的订单信息。  orderStr是json字符串的格式，不传会报401参数错误。 |
| [payload](payment-model.md#payload) | string | 是 | 预留信息，在请求接口时，入参如果传递，接口响应中则会原样返回。  **说明：** 拉起华为支付收银台，需传空或空字符。H5支付场景下跳转三方支付收银台需要固定传递“AP”。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[PayResult](payment-paymentservice.md#payresult)> | Promise对象。带[PayResult](payment-paymentservice.md#payresult)返回结果的Promise对象。  **说明：** 华为支付场景下，[PayResult](payment-paymentservice.md#payresult)可能返回为空，支付结果以回调通知或查询结果为准。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001930000 | The operation was canceled by the user. |
| 1001930001 | Pay failed. |
| 1001930002 | The transaction has been processed. |
| 1001930010 | Duplicate request. |
| 1001930011 | Network connection error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestPaymentPromise() {
10. // use orderStr to pay for an order, use your own orderStr.
11. // const orderStr = '{"app_id":"***","merc_no":"***","prepay_id":"xxx","timestamp":"1680259863114","noncestr":"1487b8a60ed9f9ecc0ba759fbec23f4f","sign":"****","auth_id":"***"}';
12. // use orderStr to jump third-party payment, use your own orderStr.
13. const orderStr = '{"nextAction":"L","linkUrl":"https://www.***.pay.com/h5pay?prepay_id=***&sign=***","scheme":"","clientToken":"***"}';
14. paymentService.requestPayment(this.context, orderStr, "AP")
15. .then((payResult: paymentService.PayResult) => {
16. // succeeded in paying
17. console.info('succeeded in paying, pay result: ', payResult);
18. })
19. .catch((error: BusinessError) => {
20. // failed to pay
21. console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
22. });
23. }

25. build() {
26. Column() {
27. Button('requestPaymentPromise')
28. .type(ButtonType.Capsule)
29. .width('50%')
30. .margin(20)
31. .onClick(() => {
32. this.requestPaymentPromise();
33. })
34. }
35. .width('100%')
36. .height('100%')
37. }
38. }
```

## paymentService.cashierPicker

PhonePC/2in1Tablet

cashierPicker(context: common.UIAbilityContext, paymentInfo: PaymentInfo): Promise<PickerResult>

该方法提供拉起通用收银台功能，调用方法前请确保网络已连接，用户在通用收银台选择支付方式并确认支付后，使用Promise异步返回。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.2(14)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文，不传会报401参数错误。 |
| paymentInfo | [PaymentInfo](payment-paymentservice.md#paymentinfo) | 是 | 拉起通用收银台传入的支付信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[PickerResult](payment-paymentservice.md#pickerresult)> | Promise对象。带[PickerResult](payment-paymentservice.md#pickerresult)返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001930000 | The operation was canceled by the user. |
| 1001930001 | Pay failed. |
| 1001930002 | The transaction has been processed. |
| 1001930010 | Duplicate request. |
| 1001930011 | Network connection error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestCashierPicker() {
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
30. Button('requestCashierPicker')
31. .type(ButtonType.Capsule)
32. .width('50%')
33. .margin(20)
34. .onClick(() => {
35. this.requestCashierPicker();
36. })
37. }
38. .width('100%')
39. .height('100%')
40. }
41. }
```

## paymentService.requestBindCard

PhonePC/2in1Tablet

requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult>

该方法提供用户绑卡功能，调用该方法后会拉起Payment Kit用户绑卡页面，绑卡完成后使用Promise异步返回。调用方法前请确保网络已连接。

**元服务API：** 从版本5.0.5(17)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.PaymentService

**起始版本：** 5.0.5(17)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | common.[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md) | 是 | UIAbility上下文，不传会报401参数错误。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[BindCardResult](payment-paymentservice.md#bindcardresult)> | Promise对象。带[BindCardResult](payment-paymentservice.md#bindcardresult)返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001930000 | The operation was canceled by the user. |
| 1001930011 | Network connection error. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { paymentService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestBindCardPromise() {
10. paymentService.requestBindCard(this.context)
11. .then((bindCardResult: paymentService.BindCardResult) => {
12. // succeeded in bind card
13. console.info(`succeeded in binding card. result: ${bindCardResult}`);
14. })
15. .catch((error: BusinessError) => {
16. // failed to bind card
17. console.error(`failed to bind card, error.code: ${error.code}, error.message: ${error.message}`);
18. });
19. }

21. build() {
22. Column() {
23. Button('requestBindCardPromise')
24. .type(ButtonType.Capsule)
25. .width('50%')
26. .margin(20)
27. .onClick(() => {
28. this.requestBindCardPromise();
29. })
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```
