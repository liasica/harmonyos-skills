---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-6101
title: IAP Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > IAP Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:846e8681aa5d801d8377b49793a64d9998790738b9842af28f98acf0c24df937
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context): Promise<void>;  差异内容：NA | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context): Promise<void>;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter): Promise<Array<Product>>;  差异内容：NA | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter): Promise<Array<Product>>;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array<Product>>): void;  差异内容：NA | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array<Product>>): void;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, productIds: string[]): Promise<Array<Product>>;  差异内容：NA | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, productIds: string[]): Promise<Array<Product>>;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<CreatePurchaseResult>;  差异内容：NA | 类名：iap；  API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<CreatePurchaseResult>;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void;  差异内容：NA | 类名：iap；  API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter): Promise<void>;  差异内容：NA | 类名：iap；  API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter): Promise<void>;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：iap；  API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchaseResult>;  差异内容：NA | 类名：iap；  API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchaseResult>;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchaseResult>): void;  差异内容：NA | 类名：iap；  API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchaseResult>): void;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap；  API声明：function isSandboxActivated(context: common.Context): Promise<boolean>;  差异内容：NA | 类名：iap；  API声明：function isSandboxActivated(context: common.Context): Promise<boolean>;  差异内容：801 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：global；  API声明：declare struct CashierComponent  差异内容：declare struct CashierComponent | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent；  API声明：@Require  @Prop  params: iap.PurchaseParameter;  差异内容：@Require  @Prop  params: iap.PurchaseParameter; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent；  API声明：displayOptions?: cashierComponentManager.CashierDisplayOptions;  差异内容：displayOptions?: cashierComponentManager.CashierDisplayOptions; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent；  API声明：purchaseListener: cashierComponentManager.CashierListener;  差异内容：purchaseListener: cashierComponentManager.CashierListener; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent；  API声明：build(): void;  差异内容：build(): void; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare namespace cashierComponentManager  差异内容：declare namespace cashierComponentManager | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：cashierComponentManager；  API声明：interface CashierListener  差异内容：interface CashierListener | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierListener；  API声明：onPurchaseSuccess(productId: string, purchaseResult: iap.CreatePurchaseResult): void;  差异内容：onPurchaseSuccess(productId: string, purchaseResult: iap.CreatePurchaseResult): void; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierListener；  API声明：onPurchaseFailure(productId: string, error: BusinessError<void>): void;  差异内容：onPurchaseFailure(productId: string, error: BusinessError<void>): void; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：cashierComponentManager；  API声明：interface CashierDisplayOptions  差异内容：interface CashierDisplayOptions | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierDisplayOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：iap；  API声明：function showManagedInvoices(context: common.Context, purchaseOrderId: string): Promise<void>;  差异内容：function showManagedInvoices(context: common.Context, purchaseOrderId: string): Promise<void>; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode；  API声明：PURCHASE\_NOT\_FOUND = 1001860064  差异内容：PURCHASE\_NOT\_FOUND = 1001860064 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode；  API声明：OPERATION\_NOT\_SUPPORTED = 1001860065  差异内容：OPERATION\_NOT\_SUPPORTED = 1001860065 | api/@hms.core.iap.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.iap.cashierComponent.d.ets  差异内容：IAPKit | api/@hms.core.iap.cashierComponent.d.ets |
