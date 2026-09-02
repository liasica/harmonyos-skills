---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-promotionservice
title: promotionService(营销服务)
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > ArkTS API > promotionService(营销服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:03:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8ecd28f78116b45d7335d521bd85253b55d0bb7d014cfaafecb8a8f8288dfa1f
---

本模块支持拉起营销服务，包括活动入口组件以及选券组件。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

## 导入模块

```typescript
import { promotionService } from '@kit.PaymentKit';
```

## UserAction

用户行为，包括关闭组件、点击领取按钮以及点击去使用按钮。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| doNothing | boolean | 否 | 否 | 表示是否关闭组件。  - true:是  - false：否（默认）。 |
| useButtonClicked | boolean | 否 | 否 | 表示是否点击“去使用”按钮。  - true:是  - false：否（默认）。 |
| receiveButtonClicked | boolean | 否 | 否 | 表示是否点击“领取”按钮。  - true:是  - false：否（默认）。 |

## OrderContext

订单上下文信息，用于拉起选券组件。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| mercNo | string | 否 | 否 | 商户号。获取商户号请参见[查询商户号信息](../pay-docs/hwzf-shanghuhao-0000001725982508.md)。 |
| tradeOrderAmount | number | 否 | 否 | 订单交易金额，单位为分。取值必须大于0，传递非取值范围内的值会导致请求异常。 |
| goodsCodes | string[] | 否 | 是 | 商品编码列表。 |
| authId | string | 否 | 否 | 商户证书ID。一个商户可配置多套证书，请妥善保管。获取可参见[准备证书](../harmonyos-guides/payment-certificates-config.md)。 |
| sign | string | 否 | 否 | 签名，使用除了sign字段以外的其他字段计算签名值。可参考[签名规则](payment-rest-overview.md#签名规则)。 |

## CouponCategory

优惠券品类枚举类型。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PLATFORM\_COUPON | 0 | 平台券。 |

## CouponType

优惠券类型枚举。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| VOUCHER | 0 | 满减券类型。 |

## CouponDetail

券详情信息。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| couponCategory | [CouponCategory](payment-promotionservice.md#couponcategory) | 否 | 否 | 优惠券品类枚举类型。 |
| couponCode | string | 否 | 否 | 券码。 |
| batchNo | string | 否 | 否 | 批次号。 |
| couponType | [CouponType](payment-promotionservice.md#coupontype) | 否 | 否 | 券类型。 |
| effectiveTime | number | 否 | 否 | 优惠券生效时间。 |
| expireTime | number | 否 | 否 | 优惠券过期时间。 |
| amount | number | 否 | 是 | 优惠券面额，单位为分。 |
| logoUrl | string | 否 | 否 | 优惠券图标地址。 |
| couponDesc | string | 否 | 否 | 优惠券描述信息。最大长度3096。 |

## PromotionComponentController

该类为营销组件控制器。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

### constructor

constructor(context: UIContext)

该方法实例化营销组件控制器对象，通过该接口可以拉起活动入口组件。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该实例方法支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | UI上下文对象。 |

**示例**：

```typescript
import { promotionService } from '@kit.PaymentKit';

@Component
struct StartPromotionEntryDialogDemo {
    controller: promotionService.PromotionComponentController = new promotionService.PromotionComponentController(this.getUIContext());

    build() {}
}
```

### startPromotionEntryDialog

startPromotionEntryDialog(mercNo: string, offset?: number): Promise<UserAction>

拉起活动入口组件，使用Promise异步回调。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| mercNo | string | 是 | 商户号。 |
| offset | number | 否 | 活动入口组件底部到屏幕边框底部的距离差，默认为100px。 |

**返回值**：

| 类型 | **说明** |
| --- | --- |
| Promise<[UserAction](payment-promotionservice.md#useraction)> | Promise对象，返回用户行为信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-payment.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1019200001 | System internal error. |
| 1019200002 | Network connection error. |

**示例**：

```typescript
import { promotionService } from '@kit.PaymentKit';

@Component
struct StartPromotionEntryDialogDemo {
  controller: promotionService.PromotionComponentController = new promotionService.PromotionComponentController(this.getUIContext());
  
  build() {
    Column() {
      Button('拉起活动入口组件')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(async () => {
          try {
            // 拉起活动入口组件
            let userAction = await this.controller.startPromotionEntryDialog('', 10);
            // 点击关闭、去使用后会分别返回doNothing、useButtonClicked为true
            console.info(`userAction ${JSON.stringify(userAction)}`);
          } catch (e) {
            console.error(`startUserSelectCouponsPopup error ${JSON.stringify(e)}`);
          }
        })
    }
  }
}
```

## startUserChooseCouponsPopup

startUserChooseCouponsPopup(context: common.Context, orderContext: OrderContext): Promise<CouponDetail[]>

选券组件拉起方法，调用后使用Promise异步回调。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 上下文。 |
| orderContext | [OrderContext](payment-promotionservice.md#ordercontext) | 是 | 用户订单上下文。 |

**返回值**：

| 类型 | **说明** |
| --- | --- |
| Promise<[CouponDetail](payment-promotionservice.md#coupondetail)[]> | Promise对象，返回券详情信息。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-payment.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1019200001 | System internal error. |
| 1019200002 | Network connection error. |
| 1019200003 | Trade amount is invalid. |

**示例**：

```typescript
import { promotionService } from '@kit.PaymentKit';

@Entry
@Component
export struct StartUserChooseCouponsPopupDemo {
    build() {
        Column() {
            Button('选券页面')
                .type(ButtonType.Capsule)
                .width('50%')
                .margin(20)
                .onClick(() => {
                    let req: promotionService.OrderContext = {
                        // 商户号
                        mercNo: '',
                        // 订单金额，单位为分
                        tradeOrderAmount: 15,
                        // 商品编码
                        goodsCodes: ['', ''],
                        // 商户证书ID
                        authId: '',
                        // 签名内容调云侧接口获取
                        sign: 'MEQCIEIWzdpziRyTi8vhwWHFuDdxf********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ=='
                    }
                    console.info(`req ${JSON.stringify(req)}`);
                    promotionService.startUserChooseCouponsPopup(this.getUIContext().getHostContext()!, req).then(res => {
                        console.info(`startUserChooseCouponsPopup res ${JSON.stringify(res)}.`);
                    });
                })
        }
    }
}
```

## startPromotionDetailPopup

startPromotionDetailPopup(context: common.Context, mercNo: string): Promise<UserAction>

拉起营销详情，使用Promise异步回调。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 上下文。 |
| mercNo | string | 是 | 商户号。 |

**返回值**：

| 类型 | **说明** |
| --- | --- |
| Promise<[UserAction](payment-promotionservice.md#useraction)> | Promise对象，返回用户行为信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-payment.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1019200001 | System internal error. |
| 1019200002 | Network connection error. |

**示例**：

```typescript
import { promotionService } from '@kit.PaymentKit';

@Entry
@Component
export struct StartPromotionDetailPopupDemo {
    build() {
        Column() {
            Button('拉起营销详情')
                .type(ButtonType.Capsule)
                .width('50%')
                .margin(20)
                .onClick(() => {
                    console.info(`click enter`);
                    promotionService.startPromotionDetailPopup(this.getUIContext().getHostContext()!, 'mercNo123')
                        .then((val) => {
                            console.info(`receive resulr is ${JSON.stringify(val)}`);
                        }).catch((e: BusinessError) => {
                            console.error(`sendMessageRequest failed, message: ${JSON.stringify(e)}`)
                        });
                })
        }
    }
}
```

## getOrderAvailableCoupons

getOrderAvailableCoupons(context: common.Context, orderContext: OrderContext): Promise<CouponDetail[]>

查询当前订单可用券。使用Promise异步回调。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.1(24)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Promotion

**起始版本：** 6.1.1(24)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 上下文。 |
| orderContext | [OrderContext](payment-promotionservice.md#ordercontext) | 是 | 用户订单上下文。 |

**返回值**：

| 类型 | **说明** |
| --- | --- |
| Promise<[CouponDetail](payment-promotionservice.md#coupondetail)[]> | Promise对象，返回券详情信息。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-payment.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1019200001 | System internal error. |
| 1019200002 | Network connection error. |
| 1019200003 | Trade amount is invalid. |
| 1019200005 | AuthId is invalid. |
| 1019200006 | Sign is invalid. |
| 1019200007 | OrderContext is invalid. |
| 1019200008 | The HUAWEI ID is not signed in. |
| 1019200009 | The user did not accept the agreement. |
| 1019200010 | Merchant no is invalid. |

**示例**：

```typescript
import { promotionService } from '@kit.PaymentKit';
 
@Component
export struct GetOrderAvailableCouponsDemo {
  build() {
    Column() {
      Button('查询可用券')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          let req: promotionService.OrderContext = {
            // 商户号
            mercNo: '',
            // 订单金额，单位为分
            tradeOrderAmount: 15,
            // 商品编码
            goodsCodes: ['', ''],
            // 商户证书ID
            authId: '',
            // 签名内容调云侧接口获取
            sign: 'MEQCIEIWzdpziRyTi8vhwWHFuDdxf********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ=='
          }
          console.info(`req ${JSON.stringify(req)}`);
          promotionService.getOrderAvailableCoupons(this.getUIContext().getHostContext()!, req).then(res => {
            console.info(`getOrderAvailableCoupons res ${JSON.stringify(res)}.`);
          }).catch((e: BusinessError) => {
            console.error(`getOrderAvailableCoupons error ${JSON.stringify(e)}`);
          });
        })
    }
  }
}
```
