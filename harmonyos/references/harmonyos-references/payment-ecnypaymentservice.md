---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-ecnypaymentservice
title: ecnyPaymentService (数字人民币服务)
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > ArkTS API > ecnyPaymentService (数字人民币服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:03:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e516c77f31a1c3e165f61dff4f7102dc5f6ae3c8e44efd751227b1a3076339f0
---

本模块提供数字人民币支付服务。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ECNYPaymentService

**起始版本：** 5.0.1(13)

## 导入模块

```typescript
import { ecnyPaymentService } from '@kit.PaymentKit';
```

## EcnyOrderInfo

拉起数字人民币收银台时传入的订单信息。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ECNYPaymentService

**起始版本：** 5.0.1(13)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| merchantAppId | string | 否 | 否 | 由运营机构分配的APPID。 |
| merchantNo | string | 否 | 否 | 由运营机构分配的商户号。 |
| acqAgtInstnId | string | 否 | 是 | 受理服务机构的金融机构编码（[通过受理服务机构入网](../harmonyos-guides/payment-digital-cny-pay-preparations.md)的商户，此项必填）。若未填写，默认为空。 |
| creditorInstitutionId | string | 否 | 否 | 收款运营机构的金融机构编码。 |
| encryptedKey | string | 否 | 否 | 用于加密订单信息的密钥密文。 |
| encryptedInfo | string | 否 | 否 | 订单加密信息。 |
| encryptionSN | string | 否 | 是 | 收款运营机构加密证书序列号。若未填写，默认为空。 |
| lastWalletId | string | 否 | 是 | 付款钱包编号后四位，如果传可以在数字人民币收银台默认选择该钱包。若未填写，默认为空。 |
| extraInfo | string | 否 | 是 | 保留字段。json string格式。若未填写，默认为空。示例为{"key1":"value1"}。 |

**说明** 

相关参数获取及详细说明参见运营机构或受理服务机构（客服热线956196）提供的开发指引。

## EcnyPayResult

数字人民币支付结果。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ECNYPaymentService

**起始版本：** 5.0.1(13)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| orderNo | string | 否 | 否 | 订单号。 |
| extraInfo | string | 否 | 是 | 保留字段。json string格式。示例为{"key1":"value1"}。 |

## requestEcnyPayment

requestEcnyPayment(context: common.Context, orderInfo: EcnyOrderInfo): Promise<EcnyPayResult>

该方法提供基础支付功能，调用该方法前请确保网络已连接，调用该方法后会拉起数字人民币收银台，支付完成后使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.ECNYPaymentService

**设备行为差异：** 该接口在Phone设备中可正常调用，在其他设备类型中返回1014900005错误码。

**起始版本：** 5.0.1(13)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | 上下文，不传会报401参数错误。 |
| orderInfo | [EcnyOrderInfo](payment-ecnypaymentservice.md#ecnyorderinfo) | 是 | 拉起收银台传入的订单信息。不传会报401参数错误。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[EcnyPayResult](payment-ecnypaymentservice.md#ecnypayresult)> | Promise对象。返回支付结果信息。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-payment.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1014900000 | The operation was canceled by the user. |
| 1014900001 | Payment failed. |
| 1014900002 | The transaction has been processed. |
| 1014900003 | Duplicate request. |
| 1014900004 | Network connection error. |
| 1014900005 | The payment environment is not ready. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)

```typescript
import { ecnyPaymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestEcnyPaymentPromise() {
    // 请使用开发者真实的订单信息（orderInfo）
    const orderInfo: ecnyPaymentService.EcnyOrderInfo = {
      merchantAppId: '***',
      merchantNo: '***',
      acqAgtInstnId: '***',
      creditorInstitutionId: '***',
      encryptedKey: '***',
      encryptedInfo: '***',
      encryptionSN: '***',
      extraInfo: '***',
      lastWalletId: '***'
    };
    ecnyPaymentService.requestEcnyPayment(this.context, orderInfo)
      .then((result: ecnyPaymentService.EcnyPayResult) => {
        // 支付成功
        console.info(`succeeded in paying, result.orderNo: ${result.orderNo}, result.extraInfo: ${result.extraInfo}`);
      });
  }

  build() {
    Column() {
      Button('requestEcnyPaymentPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestEcnyPaymentPromise();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
