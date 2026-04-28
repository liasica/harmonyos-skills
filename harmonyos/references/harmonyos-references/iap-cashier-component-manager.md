---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-cashier-component-manager
title: cashierComponentManager (iap嵌入式收银台组件管理)
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > ArkTS组件 > cashierComponentManager (iap嵌入式收银台组件管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cece09faab5047e2702acfb4dd7d6bdb46346948d5b4bd01d349180dd4c40616
---

本模块提供iap嵌入式收银台组件的逻辑管理，辅助应用通过集成iap嵌入式收银台组件完成应用内支付功能。

**起始版本：** 6.1.0(23)

## 导入模块

TV

```
1. import { cashierComponentManager } from '@kit.IAPKit';
```

## CashierListener

TV

[CashierComponent](iap-cashier-component.md#cashiercomponent)组件的监听，用来回调组件调用的成功、失败事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP.EmbeddedCashier

**起始版本：** 6.1.0(23)

### onPurchaseSuccess

TV

onPurchaseSuccess(productId: string, purchaseResult: iap.CreatePurchaseResult): void

iap嵌入式收银台的支付成功回调。在用户使用iap嵌入式收银台支付成功后，应用可接收此回调，用于后续逻辑处理、记录运营事件等场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP.EmbeddedCashier

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| productId | string | 是 | 支付成功的商品ID。 |
| purchaseResult | [iap.CreatePurchaseResult](iap-iap.md#createpurchaseresult) | 是 | 支付成功回调获取到的[iap.CreatePurchaseResult](iap-iap.md#createpurchaseresult)对象。 |

### onPurchaseFailure

TV

onPurchaseFailure(productId: string, error: BusinessError<void>): void

iap嵌入式收银台的支付失败回调。在用户使用iap嵌入式收银台支付失败后，应用可接收此回调，可用于后续逻辑处理，记录运营事件等场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP.EmbeddedCashier

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| productId | string | 是 | 支付失败的商品ID。 |
| error | [BusinessError<void>](js-apis-base.md#businesserror) | 是 | 支付失败回调获取到的[iap.CreatePurchaseResult](iap-iap.md#createpurchaseresult)对象。 |

### CashierDisplayOptions

TV

该接口定义了收银台的属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP.EmbeddedCashier

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 收银台背景颜色。 |
