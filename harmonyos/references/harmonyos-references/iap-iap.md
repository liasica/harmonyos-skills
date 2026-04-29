---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap
title: IAP
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > ArkTS API > IAP
category: harmonyos-references
scraped_at: 2026-04-29T14:07:37+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:9a8819507f8ab1bdf7225f92d12957b46a42f3f0cbfc0c1ced235b2fa6143e09
---

本模块提供应用内支付的能力。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { iap } from '@kit.IAPKit';
```

## ProductType

PhonePC/2in1TabletTVWearable

商品类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONSUMABLE | 0 | 消耗型商品。 |
| NONCONSUMABLE | 1 | 非消耗型商品。 |
| AUTORENEWABLE | 2 | 自动续期订阅商品。  该属性不支持Wearable设备。  **起始版本：** 4.1.0(11) |
| NONRENEWABLE | 3 | 非续期订阅商品。  该属性不支持Wearable设备。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.2(14) |

## PurchaseQueryType

PhonePC/2in1TabletTVWearable

查询购买信息的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 所有历史购买记录，包括消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。 |
| UNFINISHED | 1 | 已购买但未交付的消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。 |
| CURRENT\_ENTITLEMENT | 2 | 已购非消耗型商品和当前生效的自动续期订阅商品。 |

## PeriodUnit

PhonePC/2in1TabletTVWearable

自动续期订阅商品的周期单位。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DAY | 0 | 天。 |
| WEEK | 1 | 周。 |
| MONTH | 2 | 月。 |
| YEAR | 3 | 年。 |
| MINUTE | 4 | 分（预留参数，暂未支持）。 |

## OfferPaymentMode

PhonePC/2in1TabletTVWearable

促销的付费方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FREE\_TRIAL | 1 | 免费试用。 |
| PAY\_AS\_YOU\_GO | 2 | 随用随付。 |
| PAY\_UP\_FRONT | 3 | 提前支付。 |
| SINGLE\_PROMOTION | 5 | 单次优惠，仅适用于消耗型/非消耗型/非续期订阅商品。  **元服务API：** 从版本5.0.5(17)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.5(17) |

## OfferType

PhonePC/2in1TabletTVWearable

促销类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTRODUCTORY | 0 | 推介促销。 |
| PROMOTIONAL | 1 | 优惠促销。 |

## IAPErrorCode

PhonePC/2in1TabletTVWearable

错误码枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_CANCELED | 1001860000 | 用户取消当前操作。 |
| SYSTEM\_ERROR | 1001860001 | 通用失败错误码。 |
| APP\_NOT\_AUTHORIZED | 1001860002 | 应用未被授权访问接口。 |
| INVALID\_PRODUCT | 1001860003 | 无效的商品信息。 |
| FREQUENT\_CALLS | 1001860004 | 接口访问过频。 |
| NETWORK\_ERROR | 1001860005 | 网络连接异常。 |
| PRODUCT\_TERRITORY\_NOT\_SUPPORTED | 1001860007 | 商品所属的应用未在指定国家/地区上架。 |
| ACCOUNT\_NOT\_LOGGED\_IN | 1001860050 | 未登录华为账号。 |
| PRODUCT\_OWNED | 1001860051 | 由于已经拥有该商品，购买失败。 |
| PURCHASE\_NOT\_PAID | 1001860052 | 由于未拥有该商品，发货失败。 |
| PURCHASE\_FINISHED | 1001860053 | 此次购买已经完成发货，无需重复发货。 |
| ACCOUNT\_TERRITORY\_NOT\_SUPPORTED | 1001860054 | 用户账号所在服务地暂不支持IAP。 |
| USER\_NOT\_ALLOWED | 1001860056 | 用户交易被拒绝。 |
| APP\_NOT\_DEBUG | 1001860057 | 当前应用不是debug签名的应用。  **起始版本：** 5.0.0(12) |
| ACCOUNT\_NOT\_TEST | 1001860058 | 华为账号不是沙盒测试账号。  **起始版本：** 5.0.0(12) |
| INVALID\_PROMOTIONAL\_OFFER | 1001860059 | 无效的优惠信息。  **起始版本：** 5.0.0(12) |
| INVALID\_PURCHASE\_SIGNATURE | 1001860060 | 无效的签名信息。  **起始版本：** 5.0.0(12) |
| PURCHASE\_ALREADY\_REFUNDED | 1001860061 | 商品已退款或退款中。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.3(15) |
| REFUND\_NOT\_ALLOWED | 1001860062 | 不允许退款。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.3(15) |
| PURCHASE\_NOT\_FOUND | 1001860064 | 在登录的华为账号上找不到该笔订单。  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。  **起始版本：** 6.1.0(23) |
| OPERATION\_NOT\_SUPPORTED | 1001860065 | 不支持开票操作。  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。  **起始版本：** 6.1.0(23) |

## WindowScreenMode

PhonePC/2in1TabletTVWearable

界面窗口模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIALOG\_BOX | 1 | 界面窗口弹窗模式。 |
| FULLSCREEN | 2 | 界面窗口全屏模式。 |

## ProductStatus

PhonePC/2in1TabletTVWearable

商品状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VALID | 0 | 生效状态。 |
| CANCELED | 1 | 取消状态，即删除。此状态的商品不可续订，也不可订阅。 |
| OFFLINE | 3 | 下线状态，不能订阅，但老用户仍可续订。 |

## iap.queryEnvironmentStatus

PhonePC/2in1TabletTVWearable

queryEnvironmentStatus(context: common.Context): Promise<void>

查询用户登录的账号服务地是否在IAP Kit支持结算的国家/地区中。当前只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | 上下文。建议使用[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860000 | The operation was canceled by the user. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. iap.queryEnvironmentStatus(this.getUIContext().getHostContext() as common.UIAbilityContext).then(() => {
10. // 请求成功
11. console.info('Succeeded in querying environment status.');
12. }).catch((err: BusinessError) => {
13. // 请求失败
14. console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
15. });
16. }

18. build() {}
19. }
```

## iap.queryEnvironmentStatus

PhonePC/2in1TabletTVWearable

queryEnvironmentStatus(context: common.Context, callback: AsyncCallback<void>): void

查询用户登录的账号服务地是否在IAP Kit支持结算的国家/地区中。当前只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | 上下文。建议使用[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当用户登录的账号服务地在IAP Kit支持结算的国家/地区中时，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860000 | The operation was canceled by the user. |
| 1001860001 | System internal error. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. iap.queryEnvironmentStatus(this.getUIContext().getHostContext() as common.UIAbilityContext, (err: BusinessError) => {
10. if (err) {
11. // 请求失败
12. console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
13. return;
14. }
15. // 请求成功
16. console.info('Succeeded in querying environment status.');
17. });
18. }

20. build() {}
21. }
```

## iap.queryProducts

PhonePC/2in1TabletTVWearable

queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter): Promise<Array<Product>>

获取在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置的商品详情信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryProductsParameter](iap-iap.md#queryproductsparameter) | 是 | 包含请求信息的[QueryProductsParameter](iap-iap.md#queryproductsparameter)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Product](iap-iap.md#product)>> | Promise对象，返回商品详情信息。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryProductsParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
13. // iap.ProductType.NONRENEWABLE：非续期订阅商品
14. productType: iap.ProductType.CONSUMABLE,
15. // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
16. productIds: ['testConsumeProduct01', 'testConsumeProduct02']
17. }
18. iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: Array<iap.Product>) => {
19. // 请求成功
20. console.info(`Succeeded in querying products. data length: ${data?.length}`);
21. }).catch((err: BusinessError) => {
22. // 请求失败
23. console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
24. });
25. }

27. build() {}
28. }
```

## iap.queryProducts

PhonePC/2in1TabletTVWearable

queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array<Product>>): void

用于获取在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置的商品详情信息。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryProductsParameter](iap-iap.md#queryproductsparameter) | 是 | 包含请求信息的[QueryProductsParameter](iap-iap.md#queryproductsparameter)对象。 |
| callback | AsyncCallback<Array<[Product](iap-iap.md#product)>> | 是 | 回调函数。当查询成功时，err为undefined，data为获取到的Array<[Product](iap-iap.md#product)>；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryProductsParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
13. // iap.ProductType.NONRENEWABLE：非续期订阅商品
14. productType: iap.ProductType.CONSUMABLE,
15. // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
16. productIds: ['testConsumeProduct01', 'testConsumeProduct02']
17. }
18. iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: Array<iap.Product>) => {
19. if (err) {
20. // 请求失败
21. console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
22. return;
23. }
24. // 请求成功
25. console.info(`Succeeded in querying products. data length: ${data?.length}`);
26. });
27. }

29. build() {}
30. }
```

## iap.queryProducts

PhonePC/2in1TabletTVWearable

queryProducts(context: common.UIAbilityContext, productIds: string[]): Promise<Array<Product>>

查询在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置的商品详情信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| productIds | string[] | 是 | 待查询商品ID列表。商品ID必须已经在当前应用中创建且唯一。  商品ID来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中配置商品信息时设置的商品ID，请参见[配置商品信息](../harmonyos-guides/iap-config-product.md)。  **说明：** 一次最多可查询200个商品，商品数量较多时建议分批查询。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Product](iap-iap.md#product)>> | Promise对象，返回商品详情信息。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
10. const productIds: string[] = ['testConsumeProduct01', 'testConsumeProduct02'];
11. iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, productIds).then((data: Array<iap.Product>) => {
12. // 请求成功
13. console.info(`Succeeded in querying products. data length: ${data?.length}`);
14. }).catch((err: BusinessError) => {
15. // 请求失败
16. console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
17. })
18. }

20. build() {}
21. }
```

## iap.purchase(deprecated)

PhonePC/2in1TabletTVWearable

purchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<PurchaseResult>

创建订单，支持消耗型商品和非消耗型商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)创建商品后，应用使用此接口调用华为应用内支付收银台，显示商品、价格和支付方式。

使用Promise异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[createPurchase](iap-iap.md#iapcreatepurchase)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [PurchaseParameter](iap-iap.md#purchaseparameter) | 是 | 包含请求信息的[PurchaseParameter](iap-iap.md#purchaseparameter)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PurchaseResult](iap-iap.md#purchaseresultdeprecated)> | Promise对象，返回购买结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860000 | The operation was canceled by the user. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860051 | Failed to purchase a product because the user already owns the product. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1001860056 | The user is not allowed to make purchase. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.PurchaseParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. productType: iap.ProductType.CONSUMABLE,
13. // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
14. productId: 'testConsumeProduct01',
15. developerPayload: 'test developer payload string.'
16. }
17. iap.purchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.PurchaseResult) => {
18. // 请求成功
19. console.info(`Succeeded in purchasing. data: ${data.inAppPurchaseData}`);
20. }).catch((err: BusinessError) => {
21. // 请求失败
22. console.error(`Failed to purchase. Code is ${err.code}, message is ${err.message}`);
23. });
24. }

26. build() {}
27. }
```

## iap.purchase(deprecated)

PhonePC/2in1TabletTVWearable

purchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<PurchaseResult>): void

创建订单，支持消耗型商品和非消耗型商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)创建商品后，使用此接口调用华为应用内支付收银台，显示商品、价格和支付方式。

使用callback异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[createPurchase](iap-iap.md#iapcreatepurchase-1)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [PurchaseParameter](iap-iap.md#purchaseparameter) | 是 | 包含请求信息的[PurchaseParameter](iap-iap.md#purchaseparameter)对象。 |
| callback | AsyncCallback<[PurchaseResult](iap-iap.md#purchaseresultdeprecated)> | 是 | 回调函数。当购买成功时，err为undefined，data为获取到的[PurchaseResult](iap-iap.md#purchaseresultdeprecated)对象；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860000 | The operation was canceled by the user. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860051 | Failed to purchase a product because the user already owns the product. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1001860056 | The user is not allowed to make purchase. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.PurchaseParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. productType: iap.ProductType.CONSUMABLE,
13. // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
14. productId: 'testConsumeProduct01',
15. developerPayload: 'test developer payload string.'
16. }
17. iap.purchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.PurchaseResult) => {
18. if (err) {
19. // 请求失败
20. console.error(`Failed to purchase. Code is ${err.code}, message is ${err.message}`);
21. return;
22. }
23. // 请求成功
24. console.info(`Succeeded in purchasing. data: ${data.inAppPurchaseData}`);
25. });
26. }

28. build() {}
29. }
```

## iap.createPurchase

PhonePC/2in1TabletTVWearable

createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<CreatePurchaseResult>

发起购买，支持消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)创建商品后，使用此接口拉起华为应用内支付收银台，显示商品名称、商品价格等信息。

使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [PurchaseParameter](iap-iap.md#purchaseparameter) | 是 | 包含请求信息的[PurchaseParameter](iap-iap.md#purchaseparameter)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CreatePurchaseResult](iap-iap.md#createpurchaseresult)> | Promise对象，返回购买结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860000 | The operation was canceled by the user. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860051 | Failed to purchase a product because the user already owns the product. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1001860056 | The user is not allowed to make purchase. |
| 1001860059 | Invalid promotional offer id. |
| 1001860060 | Invalid purchase signature. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.PurchaseParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
13. // iap.ProductType.NONRENEWABLE：非续期订阅商品
14. productType: iap.ProductType.AUTORENEWABLE,
15. // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
16. productId: 'testProduct01',
17. developerPayload: 'test developer payload string.'
18. }
19. iap.createPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.CreatePurchaseResult) => {
20. // 请求成功
21. console.info(`Succeeded in creating purchase. data: ${data.purchaseData}`);
22. }).catch((err: BusinessError) => {
23. // 请求失败
24. console.error(`Failed to create purchase. Code is ${err.code}, message is ${err.message}`);
25. });
26. }

28. build() {}
29. }
```

## iap.createPurchase

PhonePC/2in1TabletTVWearable

createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void

发起购买，支持消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)创建商品后，使用此接口拉起华为应用内支付收银台，显示商品名称、价格等信息。

使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [PurchaseParameter](iap-iap.md#purchaseparameter) | 是 | 包含请求信息的[PurchaseParameter](iap-iap.md#purchaseparameter)对象。 |
| callback | AsyncCallback<[CreatePurchaseResult](iap-iap.md#createpurchaseresult)> | 是 | 回调函数。当购买成功时，err为undefined，data为获取到的[CreatePurchaseResult](iap-iap.md#createpurchaseresult)对象；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860000 | The operation was canceled by the user. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860051 | Failed to purchase a product because the user already owns the product. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1001860056 | The user is not allowed to make purchase. |
| 1001860059 | Invalid promotional offer id. |
| 1001860060 | Invalid purchase signature. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.PurchaseParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
13. // iap.ProductType.NONRENEWABLE：非续期订阅商品
14. productType: iap.ProductType.AUTORENEWABLE,
15. // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
16. productId: 'testProduct01',
17. developerPayload: 'test developer payload string.'
18. }
19. iap.createPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.CreatePurchaseResult) => {
20. if (err) {
21. // 请求失败
22. console.error(`Failed to create purchase. Code is ${err.code}, message is ${err.message}`);
23. return;
24. }
25. // 请求成功
26. console.info(`Succeeded in creating purchase. data: ${data.purchaseData}`);
27. });
28. }

30. build() {}
31. }
```

## iap.consumePurchase(deprecated)

PhonePC/2in1TabletTVWearable

consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter): Promise<ConsumeResult>

在消耗型商品支付成功后，应用需要在发放商品成功之后调用此接口对消耗型商品执行消耗操作。使用Promise异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[finishPurchase](iap-iap.md#iapfinishpurchase)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [ConsumePurchaseParameter](iap-iap.md#consumepurchaseparameterdeprecated) | 是 | 包含请求信息的[ConsumePurchaseParameter](iap-iap.md#consumepurchaseparameterdeprecated)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ConsumeResult](iap-iap.md#consumeresultdeprecated)> | Promise对象，返回消耗结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860052 | The purchase cannot be finished because the user has not paid for it. |
| 1001860053 | The purchase has been finished and cannot be finished again. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.ConsumePurchaseParameter = {
10. purchaseToken: '***',
11. developerChallenge: 'developerChallenge'
12. }
13. iap.consumePurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.ConsumeResult) => {
14. // 请求成功
15. console.info(`Succeeded in consuming purchases. data: ${data.consumedPurchaseData}`);
16. }).catch((err: BusinessError) => {
17. // 请求失败
18. console.error(`Failed to consume purchase. Code is ${err.code}, message is ${err.message}`);
19. });
20. }

22. build() {}
23. }
```

## iap.consumePurchase(deprecated)

PhonePC/2in1TabletTVWearable

consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter, callback: AsyncCallback<ConsumeResult>): void

在消耗型商品支付成功后，应用需要在发放商品成功之后调用此接口对消耗型商品执行消耗操作。使用callback异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[finishPurchase](iap-iap.md#iapfinishpurchase-1)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [ConsumePurchaseParameter](iap-iap.md#consumepurchaseparameterdeprecated) | 是 | 包含请求信息的[ConsumePurchaseParameter](iap-iap.md#consumepurchaseparameterdeprecated)对象。 |
| callback | AsyncCallback<[ConsumeResult](iap-iap.md#consumeresultdeprecated)> | 是 | 回调函数。当消耗成功时，err为undefined，data为获取到的[ConsumeResult](iap-iap.md#consumeresultdeprecated)对象；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860052 | The purchase cannot be finished because the user has not paid for it. |
| 1001860053 | The purchase has been finished and cannot be finished again. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.ConsumePurchaseParameter = {
10. purchaseToken: '***',
11. developerChallenge: 'developerChallenge'
12. }
13. iap.consumePurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.ConsumeResult) => {
14. if (err) {
15. // 请求失败
16. console.error(`Failed to consume purchase. Code is ${err.code}, message is ${err.message}`);
17. return;
18. }
19. // 请求成功
20. console.info(`Succeeded in consuming purchases. data: ${data.consumedPurchaseData}`);
21. });
22. }

24. build() {}
25. }
```

## iap.finishPurchase

PhonePC/2in1TabletTVWearable

finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter): Promise<void>

应用完成已购商品的发货后，调用此接口确认发货，指明此次购买流程结束。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [FinishPurchaseParameter](iap-iap.md#finishpurchaseparameter) | 是 | 包含请求信息的[FinishPurchaseParameter](iap-iap.md#finishpurchaseparameter)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860052 | The purchase cannot be finished because the user has not paid for it. |
| 1001860053 | The purchase has been finished and cannot be finished again. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const finishPurchaseParam: iap.FinishPurchaseParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
13. // iap.ProductType.NONRENEWABLE：非续期订阅商品
14. productType: iap.ProductType.CONSUMABLE,
15. purchaseToken: '***',
16. purchaseOrderId: '***'
17. };
18. iap.finishPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, finishPurchaseParam).then(() => {
19. // 请求成功
20. console.info('Succeeded in finishing purchase.');
21. }).catch((err: BusinessError) => {
22. // 请求失败
23. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
24. });
25. }

27. build() {}
28. }
```

## iap.finishPurchase

PhonePC/2in1TabletTVWearable

finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback<void>): void

应用完成已购商品的发货后，调用此接口确认发货，指明此次购买流程结束。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [FinishPurchaseParameter](iap-iap.md#finishpurchaseparameter) | 是 | 包含请求信息的[FinishPurchaseParameter](iap-iap.md#finishpurchaseparameter)对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当确认发货成功时，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860052 | The purchase cannot be finished because the user has not paid for it. |
| 1001860053 | The purchase has been finished and cannot be finished again. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const finishPurchaseParam: iap.FinishPurchaseParameter = {
10. // iap.ProductType.CONSUMABLE：消耗型商品
11. // iap.ProductType.NONCONSUMABLE：非消耗型商品
12. // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
13. // iap.ProductType.NONRENEWABLE：非续期订阅商品
14. productType: iap.ProductType.CONSUMABLE,
15. purchaseToken: '***',
16. purchaseOrderId: '***'
17. };
18. iap.finishPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, finishPurchaseParam, (err: BusinessError) => {
19. if (err) {
20. // 请求失败
21. console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
22. return;
23. }
24. // 请求成功
25. console.info('Succeeded in finishing purchase.');
26. });
27. }

29. build() {}
30. }
```

## iap.queryOwnedPurchases(deprecated)

PhonePC/2in1TabletTVWearable

queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>

查询用户已订购商品的购买数据，包括消耗型商品和非消耗型商品，一次请求只能查询一种类型的商品。

* 若查询消耗型商品，IAP仅返回用户已购未消耗的购买数据。若有购买数据返回，说明可能存在因某些异常而导致未进行发货的情况，需要应用判断是否已发货，未发货则需要进行补发货处理。开发者应用发货成功后调用[consumePurchase](iap-iap.md#iapconsumepurchasedeprecated)接口进行消耗。消耗成功的订单信息将不会在此接口返回，可通过[queryPurchaseRecords](iap-iap.md#iapquerypurchaserecordsdeprecated)接口获取。
* 若查询非消耗型商品，IAP返回用户所有已订购商品的购买数据。

使用Promise异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[queryPurchases](iap-iap.md#iapquerypurchases)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryPurchasesParameter](iap-iap.md#querypurchasesparameter) | 是 | 包含请求信息的[QueryPurchasesParameter](iap-iap.md#querypurchasesparameter)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryPurchasesResult](iap-iap.md#querypurchasesresultdeprecated)> | Promise对象，返回查询的购买数据信息。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860053 | The purchase has been finished and cannot be finished again. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryPurchasesParameter = {
10. productType: iap.ProductType.CONSUMABLE
11. }
12. iap.queryOwnedPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchasesResult) => {
13. // 请求成功
14. console.info(`Succeeded in querying owned purchases. data len: ${data.productList?.length}`);
15. }).catch((err: BusinessError) => {
16. // 请求失败
17. console.error(`Failed to query owned purchases. Code is ${err.code}, message is ${err.message}`);
18. });
19. }

21. build() {}
22. }
```

## iap.queryOwnedPurchases(deprecated)

PhonePC/2in1TabletTVWearable

queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void

查询用户已订购商品的购买数据，包括消耗型商品和非消耗型商品，一次请求只能查询一种类型的商品。

* 若查询消耗型商品，IAP仅返回用户已购未消耗的购买数据。若有购买数据返回，说明可能存在因某些异常而导致未进行发货的情况，需要应用判断是否已发货，未发货则需要进行补发货处理。开发者应用发货成功后调用[consumePurchase](iap-iap.md#iapconsumepurchasedeprecated)接口进行消耗。消耗成功的订单信息将不会在此接口返回，可通过[queryPurchaseRecords](iap-iap.md#iapquerypurchaserecordsdeprecated-1)接口获取。
* 若查询非消耗型商品，IAP返回用户所有已订购商品的购买数据。

使用callback异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[queryPurchases](iap-iap.md#iapquerypurchases-1)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryPurchasesParameter](iap-iap.md#querypurchasesparameter) | 是 | 包含请求信息的[QueryPurchasesParameter](iap-iap.md#querypurchasesparameter)对象。 |
| callback | AsyncCallback<[QueryPurchasesResult](iap-iap.md#querypurchasesresultdeprecated)> | 是 | 回调函数。当查询成功时，err为undefined，data为获取到[QueryPurchasesResult](iap-iap.md#querypurchasesresultdeprecated)对象；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860003 | Invalid product information. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860007 | The app to which the product belongs is not released in a specified location. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860053 | The purchase has been finished and cannot be finished again. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryPurchasesParameter = {
10. productType: iap.ProductType.CONSUMABLE
11. }
12. iap.queryOwnedPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchasesResult) => {
13. if (err) {
14. // 请求失败
15. console.error(`Failed to query owned purchases. Code is ${err.code}, message is ${err.message}`);
16. return;
17. }
18. // 请求成功
19. console.info(`Succeeded in querying owned purchases. data len: ${data.productList?.length}`);
20. });
21. }

23. build() {}
24. }
```

## iap.queryPurchaseRecords(deprecated)

PhonePC/2in1TabletTVWearable

queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>

获取已执行过消耗操作的消耗型商品的购买数据。使用Promise异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[queryPurchases](iap-iap.md#iapquerypurchases)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryPurchasesParameter](iap-iap.md#querypurchasesparameter) | 是 | 包含请求信息的[QueryPurchasesParameter](iap-iap.md#querypurchasesparameter)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryPurchasesResult](iap-iap.md#querypurchasesresultdeprecated)> | Promise对象，返回已执行过消耗操作的消耗型商品的购买数据。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryPurchasesParameter = {
10. productType: iap.ProductType.CONSUMABLE
11. }
12. iap.queryPurchaseRecords(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchasesResult) => {
13. // 请求成功
14. console.info(`Succeeded in querying purchase records. data len: ${data.productList?.length}`);
15. }).catch((err: BusinessError) => {
16. // 请求失败
17. console.error(`Failed to query purchase records. Code is ${err.code}, message is ${err.message}`);
18. });
19. }

21. build() {}
22. }
```

## iap.queryPurchaseRecords(deprecated)

PhonePC/2in1TabletTVWearable

queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void

获取已执行过消耗操作的消耗型商品的购买数据。使用callback异步回调。

**废弃说明：** 从4.1.0(11)开始废弃，建议使用[queryPurchases](iap-iap.md#iapquerypurchases-1)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：** 4.0.0(10)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryPurchasesParameter](iap-iap.md#querypurchasesparameter) | 是 | 包含请求信息的[QueryPurchasesParameter](iap-iap.md#querypurchasesparameter)对象。 |
| callback | AsyncCallback<[QueryPurchasesResult](iap-iap.md#querypurchasesresultdeprecated)> | 是 | 回调函数。当查询成功时，err为undefined，data为获取到[QueryPurchasesResult](iap-iap.md#querypurchasesresultdeprecated)对象；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryPurchasesParameter = {
10. productType: iap.ProductType.CONSUMABLE
11. }
12. iap.queryPurchaseRecords(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchasesResult) => {
13. if (err) {
14. // 请求失败
15. console.error(`Failed to query purchase records. Code is ${err.code}, message is ${err.message}`);
16. return;
17. }
18. // 请求成功
19. console.info(`Succeeded in querying purchase records. data len: ${data.productList?.length}`);
20. });
21. }

23. build() {}
24. }
```

## iap.queryPurchases

PhonePC/2in1TabletTVWearable

queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchaseResult>

查询已购商品的订单信息，包含 ：

* 已购买但是未确认发货的商品的订单信息。
* 当前生效的非消耗型商品、自动续期订阅商品和非续期订阅商品。

使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryPurchasesParameter](iap-iap.md#querypurchasesparameter) | 是 | 包含请求信息的[QueryPurchasesParameter](iap-iap.md#querypurchasesparameter)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryPurchaseResult](iap-iap.md#querypurchaseresult)> | Promise对象，返回已购商品的订单信息。在沙盒场景下，已发货状态的非消耗型商品订单信息将不返回。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryPurchasesParameter = {
10. productType: iap.ProductType.CONSUMABLE,
11. queryType: iap.PurchaseQueryType.UNFINISHED
12. }
13. iap.queryPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchaseResult) => {
14. // 请求成功
15. console.info(`Succeeded in querying purchases. data len: ${data.purchaseDataList?.length}`);
16. }).catch((err: BusinessError) => {
17. // 请求失败
18. console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
19. });
20. }

22. build() {}
23. }
```

## iap.queryPurchases

PhonePC/2in1TabletTVWearable

queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchaseResult>): void

查询已购商品的订单信息，包含 ：

* 已购买但是未确认发货的商品的订单信息。
* 当前生效的非消耗型商品、自动续期订阅商品和非续期订阅商品。

使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)上下文。 |
| parameter | [QueryPurchasesParameter](iap-iap.md#querypurchasesparameter) | 是 | 包含请求信息的[QueryPurchasesParameter](iap-iap.md#querypurchasesparameter)对象。 |
| callback | AsyncCallback<[QueryPurchaseResult](iap-iap.md#querypurchaseresult)> | 是 | 回调函数。当查询成功时，err为undefined，data为获取到[QueryPurchaseResult](iap-iap.md#querypurchaseresult)对象，否则为错误对象。同时，在沙盒场景下，已发货状态的非消耗型商品订单信息将不返回。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const parameter: iap.QueryPurchasesParameter = {
10. productType: iap.ProductType.CONSUMABLE,
11. queryType: iap.PurchaseQueryType.UNFINISHED
12. }
13. iap.queryPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchaseResult) => {
14. if (err) {
15. // 请求失败
16. console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
17. return;
18. }
19. // 请求成功
20. console.info(`Succeeded in querying purchases. data len: ${data.purchaseDataList?.length}`);
21. });
22. }

24. build() {}
25. }
```

## iap.showManagedSubscriptions

PhonePC/2in1TabletTVWearable

showManagedSubscriptions(context: common.Context, uiParameter: UIWindowParameter, groupId?: string): Promise<void>

跳转到订阅页或订阅详情页。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1、TV设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | 上下文。建议使用[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |
| uiParameter | [UIWindowParameter](iap-iap.md#uiwindowparameter) | 是 | 包含界面窗口模式的[UIWindowParameter](iap-iap.md#uiwindowparameter)对象。 |
| groupId | string | 否 | 订阅组ID，来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中配置管理的订阅组，请参见[新增订阅组](../app/non-subscription-0000001958955109.md#section37862471018)。  **说明：**  - 传递groupId，跳转到订阅详情页。  - 不传递groupId，跳转到订阅页。如果用户在应用只有一条订阅数据，此时会跳转到此条订阅的订阅详情页。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. const uiWindowParameter: iap.UIWindowParameter = {
10. windowScreenMode: iap.WindowScreenMode.DIALOG_BOX
11. }
12. const groupId = '***';
13. iap.showManagedSubscriptions(this.getUIContext().getHostContext() as common.UIAbilityContext, uiWindowParameter, groupId).then(() => {
14. // 请求成功
15. console.info('Succeeded in showing subscription page.');
16. }).catch((err: BusinessError) => {
17. // 请求失败
18. console.error(`Failed to show subscription page. Code is ${err.code}, message is ${err.message}`);
19. });
20. }

22. build() {}
23. }
```

## iap.isSandboxActivated

PhonePC/2in1TabletTVWearable

isSandboxActivated(context: common.Context): Promise<boolean>

检查沙盒测试能力是否生效。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | 上下文。建议使用[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示沙盒测试能力生效；返回false表示沙盒测试能力未生效，可根据返回的错误码检查未生效原因。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860050 | The HUAWEI ID is not signed in. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1001860057 | The app provision type is not debug. |
| 1001860058 | The HUAWEI ID is not test account. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. test() {
9. iap.isSandboxActivated(this.getUIContext().getHostContext() as common.UIAbilityContext).then((isActivated: boolean) => {
10. // 请求成功
11. console.info(`Succeeded in checking the sandbox status. is activate: ${isActivated}`);
12. }).catch((err: BusinessError) => {
13. // 请求失败
14. console.error(`Failed to check the sandbox status. Code is ${err.code}, message is ${err.message}`);
15. });
16. }

18. build() {}
19. }
```

## iap.createRefundRequest

PhonePC/2in1TabletTVWearable

createRefundRequest(context: common.Context, purchaseOrderId: string): Promise<void>

退款接口，调用此接口拉起退款流程，仅支持非游戏应用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | 上下文。建议使用[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |
| purchaseOrderId | string | 是 | 具体一笔订单中对应的购买订单号ID。最大长度256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1001860000 | The operation was canceled by the user. |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1001860061 | The purchase has been refunded or in refund. |
| 1001860062 | Refund is not allowed. |

**示例**：

```
1. import { iap } from '@kit.IAPKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct IapTest {
8. /**
9. * 拉起退款界面
10. */
11. createRefundRequest() {
12. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. // 调用iap.createRefundRequest拉起退款，传入context和purchaseOrderId
14. let purchaseOrderId = '';
15. iap.createRefundRequest(context, purchaseOrderId).then(() => {
16. // 退款成功
17. console.info('Succeeded in create refund request.');
18. // ...
19. }).catch((err: BusinessError) => {
20. // 退款失败
21. console.error(`Failed to create refund request. Code is ${err.code}, message is ${err.message}`);
22. // ...
23. });
24. }
25. build() {
26. }
27. }
```

## iap.showManagedInvoices

PhonePC/2in1Tablet

showManagedInvoices(context: common.Context, purchaseOrderId: string): Promise<void>

跳转到发票页，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP.Extension

**设备行为差异：** 该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回1001860065错误码。

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[Context](js-apis-inner-application-context.md) | 是 | 上下文。建议使用[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |
| purchaseOrderId | string | 是 | 具体一笔订单中对应的购买订单号ID。最大长度256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](iap-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1001860001 | System internal error. |
| 1001860002 | The application is not authorized. |
| 1001860004 | Too frequent API calls. |
| 1001860005 | Network connection error. |
| 1001860054 | The country or region of the signed-in HUAWEI ID does not support IAP. |
| 1001860064 | The purchase order is not found for the signed-in HUAWEI ID. |
| 1001860065 | The operation is not supported. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import { iap } from '@kit.IAPKit';

5. @Entry
6. @Component
7. struct IapTest {
8. /**
9. * 拉起开发票界面
10. */
11. showManagedInvoices() {
12. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. // 调用iap.showManagedInvoices拉起开发票页面，传入context和purchaseOrderId
14. let purchaseOrderId = '';
15. iap.showManagedInvoices(context, purchaseOrderId).then(() => {
16. // 请求成功
17. console.info('Succeeded in showing invoice page.');
18. // ...
19. }).catch((err: BusinessError) => {
20. // 请求失败
21. console.error(`Failed to show invoice page. Code is ${err.code}, message is ${err.message}`);
22. // ...
23. });
24. }
25. build() {
26. }
27. }
```

## QueryProductsParameter

PhonePC/2in1TabletTVWearable

[queryProducts](iap-iap.md#iapqueryproducts)接口的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| productType | [ProductType](iap-iap.md#producttype) | 否 | 否 | 需要查询的商品类型。  - CONSUMABLE：消耗型商品  - NONCONSUMABLE：非消耗型商品  - AUTORENEWABLE：自动续期订阅商品  - NONRENEWABLE：非续期订阅商品 |
| productIds | string[] | 否 | 否 | 待查询商品ID列表。商品ID必须已经在当前应用中创建且唯一。  商品ID来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中配置商品信息时设置的商品ID，请参见[配置商品信息](../harmonyos-guides/iap-config-product.md)。  **说明：** 一次查询最多支持200个商品，商品数量较多时建议分批查询。 |

## Product

PhonePC/2in1TabletTVWearable

包含单个商品详细信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 商品ID。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| type | [ProductType](iap-iap.md#producttype) | 否 | 否 | 商品类型。  - CONSUMABLE：消耗型商品  - NONCONSUMABLE：非消耗型商品  - AUTORENEWABLE：自动续期订阅商品  - NONRENEWABLE：非续期订阅商品  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| name | string | 否 | 否 | 商品名称，为配置商品信息时配置的名称。用于显示在应用内支付收银台。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| description | string | 否 | 否 | 商品描述，即配置商品信息时配置的描述信息。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| price(deprecated) | string | 否 | 否 | 商品的展示价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。此价格含税。  - 当商品为消耗型/非消耗型商品时，若[设置促销价格](../app/promotion-non-subscription-0000001931836332.md#section1429175616582)，该字段为商品的促销价格，未设置则为商品原价。  - 当商品为自动续期订阅商品时，该字段为商品的原价。  **说明：** 从4.1.0(11)开始废弃，建议使用localPrice替代。 |
| localPrice | string | 否 | 是 | 商品的展示价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。此价格含税。  - 当商品为消耗型/非消耗型商品/非续期订阅商品，若设置促销价格，该字段为商品的促销价格，未设置则为商品原价。（促销价格能力已调整为[临时价格调整](../app/revise-non-subscription-0000001931836328.md#section1730052050)，临时价格调整场景下该字段为商品原价）  - 当商品为自动续期订阅商品时，该字段为商品的原价。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **起始版本：** 4.1.0(11) |
| microPrice | number | 否 | 否 | 商品实际价格乘以1,000,000后的微单位价格。例如某个商品实际价格是1.99美元，则该商品对应的微单位价格为：1.99\*1000000=1990000。  - 当商品为消耗型/非消耗型商品/非续期订阅商品，若设置促销价格，该字段为商品微单位促销价格，未设置则为商品微单位原价。（促销价格能力已调整为[临时价格调整](../app/revise-non-subscription-0000001931836328.md#section1730052050)，临时价格调整场景下该字段为商品原价）  - 当商品为自动续期订阅商品时，该字段为商品微单位原价。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| originalLocalPrice | string | 否 | 否 | 商品的原价，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。此价格含税。  - 当商品为消耗型/非消耗型商品或者非续期订阅商品，无论是否[设置促销价格](../app/promotion-non-subscription-0000001931836332.md#section1429175616582)，该字段均为商品原价。  - 当商品为自动续期订阅商品时，无此字段返回，开发者无需关注。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| originalMicroPrice | number | 否 | 否 | 商品原价的微单位价格。商品原价乘以1,000,000后的微单位价格。例如某个商品原价是1.99美元，则该商品对应的微单位价格为：1.99\*1000000=1990000。  - 当商品为消耗型/非消耗型商品或者非续期订阅商品，无论是否[设置促销价格](../app/promotion-non-subscription-0000001931836332.md#section1429175616582)，该字段均为商品微单位原价。  - 当商品为自动续期订阅商品时，无此字段返回，开发者无需关注。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| currency | string | 否 | 否 | 用于支付该商品的币种，例如CNY。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| status | [ProductStatus](iap-iap.md#productstatus) | 否 | 是 | 商品状态。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.0(12) |
| subscriptionInfo | [SubscriptionInfo](iap-iap.md#subscriptioninfo) | 否 | 是 | 自动续期订阅商品相关的信息。可选。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **起始版本：** 4.1.0(11) |
| promotionalOffers | [PromotionalOffer[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap#promotionaloffer) | 否 | 是 | 商品自定义人群优惠促销信息列表。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.0(12) |
| jsonRepresentation | string | 否 | 是 | 商品详细信息的原始JSON字符串。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **起始版本：** 4.1.0(11) |

## PromotionalOffer

PhonePC/2in1TabletTVWearable

订阅商品支持的自定义优惠信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| offerId | string | 否 | 否 | 优惠ID |
| paymentMode | [OfferPaymentMode](iap-iap.md#offerpaymentmode) | 否 | 否 | 促销的付费方式 |
| periodUnit | [PeriodUnit](iap-iap.md#periodunit) | 否 | 是 | 订阅周期单位。 |
| periodCount | number | 否 | 是 | 订阅周期数量。 |
| localPrice | string | 否 | 否 | 显示的优惠商品价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。 |
| microPrice | number | 否 | 否 | 显示的优惠商品实际价格乘以1,000,000后的微单位价格。例如某个商品实际价格是1.99美元，则该商品对应的微单位价格为：1.99\*1000000=1990000。 |

## SubscriptionInfo

PhonePC/2in1TabletTVWearable

订阅信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| periodUnit | [PeriodUnit](iap-iap.md#periodunit) | 否 | 否 | 订阅周期单位。 |
| periodCount | number | 否 | 否 | 订阅周期数量。 |
| groupId | string | 否 | 否 | 订阅组ID。 |
| groupLevel | number | 否 | 否 | 商品的订阅等级。 |
| hasEligibilityForIntroOffer | boolean | 否 | 是 | 用户是否享受过推介促销。取值如下：  - true：已享受过  - false：未享受过  其他：未获取到状态 |
| introductoryOffer | [SubscriptionOffer](iap-iap.md#subscriptionoffer) | 否 | 是 | 促销信息。 |

## SubscriptionOffer

PhonePC/2in1TabletTVWearable

促销信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| paymentMode | [OfferPaymentMode](iap-iap.md#offerpaymentmode) | 否 | 否 | 促销的付费方式。 |
| periodUnit | [PeriodUnit](iap-iap.md#periodunit) | 否 | 否 | 订阅周期单位。 |
| periodCount | number | 否 | 否 | 促销期数。 |
| localPrice | string | 否 | 否 | 促销价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。 |
| microPrice | number | 否 | 否 | 促销价格的微单位价格。促销价格乘以1,000,000后的微单位价格。 |
| offerType | [OfferType](iap-iap.md#offertype) | 否 | 否 | 促销类型。 |

## PurchaseParameter

PhonePC/2in1TabletTVWearable

[purchase](iap-iap.md#iappurchasedeprecated)接口和[createPurchase](iap-iap.md#iapcreatepurchase)接口的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| productId | string | 否 | 否 | 待支付的商品ID。每个产品ID必须在当前应用中存在且唯一。商品ID来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中配置商品信息时设置的“商品ID”，具体请参见[配置商品信息](../harmonyos-guides/iap-config-product.md)。 |
| productType | [ProductType](iap-iap.md#producttype) | 否 | 否 | 需要查询的商品类型。  - CONSUMABLE：消耗型商品  - NONCONSUMABLE：非消耗型商品  - AUTORENEWABLE：自动续期订阅商品  - NONRENEWABLE：非续期订阅商品 |
| developerPayload | string | 否 | 是 | 商户侧保留信息。  若该字段有值，在支付成功后的回调结果中会原样返回给应用。  **说明：** 该参数长度限制为[0, 256]。如超过长度限制，在支付成功后将返回被截断的数据。建议在发起请求前自行验证字段长度，避免非预期截断。 |
| reservedInfo | string | 否 | 是 | 要求JSON String格式，商户可以将额外需要传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  例如：let reservedInfo = "{\"key1\":\"value1\",\"key2\":\"value2\"}";  **说明：** 该字段为预留字段，可选传入，开发者暂时无需关注。 |
| promotionalOfferId | string | 否 | 是 | 优惠ID。优惠ID来源于开发者为商品[提供优惠-配置优惠促销](../harmonyos-guides/iap-subscription-functions.md#提供优惠)时设置的促销优惠标志符。在传递jwsRepresentation（[生成优惠签名购买参数](iap-server-subscribe-offer-sign.md)）使用促销优惠时必须同时传递本字段，否则将报错。  **起始版本：** 5.0.0(12) |
| applicationUserName | string | 否 | 是 | 用户账户相关联的混淆字符串，唯一标识用户。传递优惠ID场景，可以传递该字段。在传递jwsRepresentation（[生成优惠签名购买参数](iap-server-subscribe-offer-sign.md)）使用促销优惠时，若jwsRepresentation中包含[applicationUserName](iap-server-data-model.md#offerinfo)则必须传递本字段，否则将报错。  **起始版本：** 5.0.0(12) |
| jwsRepresentation | string | 否 | 是 | 包含购买参数信息的JWS格式签名数据。购买参数，如优惠促销等。详细说明见[生成优惠签名购买参数](iap-server-subscribe-offer-sign.md)。  **起始版本：** 5.0.0(12) |
| quantity | number | 否 | 是 | 购买参数。表示所购买消耗型/非续期订阅商品的数量，需满足以下限制。  - 一次仅针对单商品类型，不支持不同类型混合  - 一次请求数量不超过10个  **说明：** 如果开发者使用了quantity参数以支持商品的批量购买，则需要在发货时校验下单的商品数量和最终发货商品数量是否一致，避免造成漏发、多发的情况。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.3(15) |

## PurchaseResult(deprecated)

PhonePC/2in1TabletTVWearable

[purchase](iap-iap.md#iappurchasedeprecated)接口的返回结果。

**废弃说明：** 从4.1.0(11)开始废弃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| inAppPurchaseData | string | 否 | 否 | 订单数据的JSON字符串，包含的参数请参见[InAppPurchaseData](iap-data-model.md#inapppurchasedata)。 |
| signature | string | 否 | 否 | 返回使用IAP私钥签署paymentData字符串生成的签名字符串。 |
| signatureAlgorithm | string | 否 | 否 | 签名算法，固定为SHA256WithRSA/PSS。 |

## CreatePurchaseResult

PhonePC/2in1TabletTVWearable

[createPurchase](iap-iap.md#iapcreatepurchase)接口的返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| purchaseData | string | 否 | 否 | 包含支付结果的JSON字符串，包含的参数请参见[PurchaseData](iap-data-model.md#purchasedata)。 |

## ConsumePurchaseParameter(deprecated)

PhonePC/2in1TabletTVWearable

[consumePurchase](iap-iap.md#iapconsumepurchasedeprecated)接口的请求参数。

**废弃说明：** 从4.1.0(11)开始废弃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| purchaseToken | string | 否 | 否 | 用户购买商品的标识，在支付完成时由IAP服务器生成。  **说明：** purchaseToken需从购买数据[InAppPurchaseData](iap-data-model.md#inapppurchasedata)中获取。支付成功或者请求[queryOwnedPurchases](iap-iap.md#iapqueryownedpurchasesdeprecated)接口均会返回[InAppPurchaseData](iap-data-model.md#inapppurchasedata)的JSON字符串。 |
| developerChallenge | string | 否 | 是 | 开发者自定义的挑战字，唯一标识此次消耗请求。消耗成功后此挑战字会记录在购买数据中并返回。  **说明：** 该参数长度限制为[0, 64]。 |

## ConsumeResult(deprecated)

PhonePC/2in1TabletTVWearable

[consumePurchase](iap-iap.md#iapconsumepurchasedeprecated)接口的返回结果。

**废弃说明：** 从4.1.0(11)开始废弃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| consumedPurchaseData | string | 否 | 否 | 包含消耗结果数据的JSON字符串。字符串中包含参数请参见[InAppPurchaseData](iap-data-model.md#inapppurchasedata)。 |
| signature | string | 否 | 否 | 使用IAP私钥签署消耗数据consumedPurchaseData生成的签名字符串。签名算法为参考signatureAlgorithm字段。  应用在收到此签名字符串后，请参见[对返回结果验签](iap-verifying-signature.md)对consumedPurchaseData的JSON字符串进行验签。 |
| signatureAlgorithm | string | 否 | 否 | 签名算法，固定为SHA256WithRSA/PSS。 |

## FinishPurchaseParameter

PhonePC/2in1TabletTVWearable

[finishPurchase](iap-iap.md#iapfinishpurchase)接口请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| productType | [ProductType](iap-iap.md#producttype) | 否 | 否 | 商品类型。  - CONSUMABLE：消耗型商品  - NONCONSUMABLE：非消耗型商品  - AUTORENEWABLE：自动续期订阅商品  - NONRENEWABLE：非续期订阅商品 |
| purchaseToken | string | 否 | 否 | 购买订单中返回的购买token。  单次购买中与具体购买订单一一对应，订阅购买中与订阅Id一一对应。  **说明：** purchaseToken需从购买数据[PurchaseOrderPayload](iap-data-model.md#purchaseorderpayload)中获取。请求[createPurchase](iap-iap.md#iapcreatepurchase)或[queryPurchases](iap-iap.md#iapquerypurchases)接口均会返回[PurchaseOrderPayload](iap-data-model.md#purchaseorderpayload)。 |
| purchaseOrderId | string | 否 | 否 | 购买订单中返回的购买订单ID。最大长度256。  **说明：** purchaseOrderId需从购买数据[PurchaseOrderPayload](iap-data-model.md#purchaseorderpayload)中获取。请求[createPurchase](iap-iap.md#iapcreatepurchase)或[queryPurchases](iap-iap.md#iapquerypurchases)接口均会返回[PurchaseOrderPayload](iap-data-model.md#purchaseorderpayload)。 |

## QueryPurchasesParameter

PhonePC/2in1TabletTVWearable

[queryOwnedPurchases](iap-iap.md#iapqueryownedpurchasesdeprecated)、[queryPurchaseRecords](iap-iap.md#iapquerypurchaserecordsdeprecated)和[queryPurchases](iap-iap.md#iapquerypurchases)接口的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| productType | [ProductType](iap-iap.md#producttype) | 否 | 否 | 需要查询的商品类型。  - CONSUMABLE：消耗型商品  - NONCONSUMABLE：非消耗型商品  - AUTORENEWABLE：自动续期订阅商品  - NONRENEWABLE：非续期订阅商品 |
| continuationToken | string | 否 | 是 | 支持分页查询的数据定位标志。  第1次查询时可以不传该参数。如果用户拥有的商品数量非常大，当响应中存在continuationToken时，应用必须对当前方法发起另一个调用，并传入本次接收到的continuationToken。如果商品仍未查完，仍需要继续发起调用，直到不再返回continuationToken，表示已经返回全部商品。 |
| queryType | [PurchaseQueryType](iap-iap.md#purchasequerytype) | 否 | 是 | 查询类型。默认值为UNFINISHED。  - ALL：消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品的所有购买记录。  - UNFINISHED：已购买但未交付的消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。  - CURRENT\_ENTITLEMENT：购买的非消耗型商品或当前有效的自动续期订阅商品。  **说明：** [queryOwnedPurchases](iap-iap.md#iapqueryownedpurchasesdeprecated)、[queryPurchaseRecords](iap-iap.md#iapquerypurchaserecordsdeprecated)场景无需关注此字段。  **起始版本：** 4.1.0(11) |

## QueryPurchasesResult(deprecated)

PhonePC/2in1TabletTVWearable

[queryOwnedPurchases](iap-iap.md#iapqueryownedpurchasesdeprecated)和[queryPurchaseRecords](iap-iap.md#iapquerypurchaserecordsdeprecated)接口的返回结果。

**废弃说明：** 从4.1.0(11)开始废弃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| productList | string[] | 否 | 否 | 商品ID的数组。 |
| inAppPurchaseDataList | string[] | 否 | 否 | 该字段以JSON字符串的形式记录[InAppPurchaseData](iap-data-model.md#inapppurchasedata)的数据，用于配合inAppSignatureList验签。每个JSON字符串包含的参数请参见[InAppPurchaseData](iap-data-model.md#inapppurchasedata)。 |
| inAppSignatureList | string[] | 否 | 否 | 对应inAppPurchaseDataList中每一个字符串的签名字符串。过程中使用IAP私钥签署，签名算法请参考signatureAlgorithm字段。  应用需要对inAppPurchaseDataList中的每个JSON字符串都进行验签，验签方法请参见[对返回结果验签](iap-verifying-signature.md)。 |
| continuationToken | string | 否 | 是 | 支持分页查询的数据定位标志。  如果用户拥有的商品数量非常大，当响应中存在continuationToken时，应用必须对当前方法发起另一个调用，并传入本次接收到的continuationToken。如果商品仍未查完，仍需要继续发起调用，直到不再返回continuationToken，表示已经返回全部商品。 |
| signatureAlgorithm | string | 否 | 否 | 签名算法，固定为SHA256WithRSA/PSS。 |

## QueryPurchaseResult

PhonePC/2in1TabletTVWearable

[queryPurchases](iap-iap.md#iapquerypurchases)接口的返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| purchaseDataList | string[] | 否 | 否 | [PurchaseData](iap-data-model.md#purchasedata)字符串的数组。 |
| continuationToken | string | 否 | 是 | 支持分页查询的数据定位标志。  如果用户拥有的商品数量非常大，当响应中存在continuationToken时，应用必须对当前方法发起另一个调用，并传入本次接收到的continuationToken。如果商品仍未查完，仍需要继续发起调用，直到不再返回continuationToken，表示已经返回全部商品。 |

## UIWindowParameter

PhonePC/2in1TabletTVWearable

[iap.showManagedSubscriptions](iap-iap.md#iapshowmanagedsubscriptions)接口界面窗口参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.IAP

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| windowScreenMode | [WindowScreenMode](iap-iap.md#windowscreenmode) | 否 | 否 | 界面窗口模式。  - DIALOG\_BOX：弹窗模式  - FULLSCREEN：全屏模式 |
