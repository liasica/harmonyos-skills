---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-cashier-component
title: CashierComponent (iap嵌入式收银台组件)
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > ArkTS组件 > CashierComponent (iap嵌入式收银台组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce94ec3a6f3a5aeb6cc54bbceed082f8b536c45d15433f09ef76f8001de0ed94
---

CashierComponent是IAP Kit提供的ArkUI嵌入式收银台组件，需配合cashierComponentManager使用，用于在应用页面内直接展示商品选择与支付界面，无需跳转外部收银台。该组件目前仅适用于TV设备的扫码支付场景，支持通过CashierDisplayOptions配置显示参数，并通过CashierListener回调处理购买结果。

开发者可通过本组件实现以下功能：

* 在应用内直接展示支付页面，完成商品购买和支付全流程。
* 配置收银台显示参数及 UI 样式（如背景色）。
* 监听购买结果并处理交易闭环，获取成功或失败的事件通知。

**起始版本：** 6.1.0(23)

## 导入模块

```typescript
import { CashierComponent, cashierComponentManager } from '@kit.IAPKit';
```

## CashierComponent

该类用来展示嵌入式收银台的UI组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**装饰器类型：** @Component

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP.EmbeddedCashier

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| params | [iap.PurchaseParameter](iap-iap.md#purchaseparameter) | 是 | @Require  @Prop | CashierComponent组件参数。  **说明：**  该参数必须是@State装饰的局部变量。 |
| displayOptions | [cashierComponentManager.CashierDisplayOptions](iap-cashier-component-manager.md#cashierdisplayoptions) | 否 | - | CashierComponent组件的配置参数。 |
| purchaseListener | [cashierComponentManager.CashierListener](iap-cashier-component-manager.md#cashierlistener) | 是 | - | CashierComponent用来接收组件的成功失败的回调事件。 |

### build

build(): void

用于创建[CashierComponent](iap-cashier-component.md#cashiercomponent)对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP.EmbeddedCashier

**起始版本：** 6.1.0(23)

**示例：**

```typescript
import { CashierComponent, cashierComponentManager,iap } from '@kit.IAPKit';
import { BusinessError} from '@kit.BasicServicesKit';

const displayOptions: cashierComponentManager.CashierDisplayOptions = {
  backgroundColor: Color.Grey
}
class PurchaseListener implements cashierComponentManager.CashierListener {
  onPurchaseSuccess: (productId: string, purchaseResult: iap.CreatePurchaseResult) => void;
  onPurchaseFailure: (productId: string, error: BusinessError<void>) => void;

  constructor() {
    this.onPurchaseSuccess = () => {

    };
    this.onPurchaseFailure = () => {

    }
  }
}
const purchaseListener = new PurchaseListener();

@Entry
@Component
struct CashierComponentPage {
  @State params: iap.PurchaseParameter = {
    // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
    productId: 'testProduct01',
    // iap.ProductType.CONSUMABLE：消耗型商品
    // iap.ProductType.NONCONSUMABLE：非消耗型商品
    // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
    // iap.ProductType.NONRENEWABLE：非续期订阅商品
    productType: iap.ProductType.CONSUMABLE,
    developerPayload: 'test developer payload string.'
  };

  build() {
    Column() {
      CashierComponent({
        params: this.params,
        purchaseListener: purchaseListener,
        displayOptions: displayOptions
      });
    }
    .width(360)
    .height(640)
  }
}
```
