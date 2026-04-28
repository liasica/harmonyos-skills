---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-b031
title: IAP Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > IAP Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:778107865926fa9fcf70251591eeb23dd4a3a440b6ab6ddc119b6b5de00f0ad3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：iap；  API声明： interface ConsumePurchaseParameter  差异内容：NA | 类名：iap；  API声明： interface ConsumePurchaseParameter  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：ConsumePurchaseParameter；  API声明：purchaseToken: string;  差异内容：NA | 类名：ConsumePurchaseParameter；  API声明：purchaseToken: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：ConsumePurchaseParameter；  API声明：developerChallenge?: string;  差异内容：NA | 类名：ConsumePurchaseParameter；  API声明：developerChallenge?: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明： interface QueryPurchasesResult  差异内容：NA | 类名：iap；  API声明： interface QueryPurchasesResult  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：QueryPurchasesResult；  API声明：productList: string[];  差异内容：NA | 类名：QueryPurchasesResult；  API声明：productList: string[];  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：QueryPurchasesResult；  API声明：inAppPurchaseDataList: string[];  差异内容：NA | 类名：QueryPurchasesResult；  API声明：inAppPurchaseDataList: string[];  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：QueryPurchasesResult；  API声明：inAppSignatureList: string[];  差异内容：NA | 类名：QueryPurchasesResult；  API声明：inAppSignatureList: string[];  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：QueryPurchasesResult；  API声明：continuationToken?: string;  差异内容：NA | 类名：QueryPurchasesResult；  API声明：continuationToken?: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：QueryPurchasesResult；  API声明：signatureAlgorithm: string;  差异内容：NA | 类名：QueryPurchasesResult；  API声明：signatureAlgorithm: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：Product；  API声明：price: string;  差异内容：NA | 类名：Product；  API声明：price: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明： interface PurchaseResult  差异内容：NA | 类名：iap；  API声明： interface PurchaseResult  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：PurchaseResult；  API声明：inAppPurchaseData: string;  差异内容：NA | 类名：PurchaseResult；  API声明：inAppPurchaseData: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：PurchaseResult；  API声明：signature: string;  差异内容：NA | 类名：PurchaseResult；  API声明：signature: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：PurchaseResult；  API声明：signatureAlgorithm: string;  差异内容：NA | 类名：PurchaseResult；  API声明：signatureAlgorithm: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明： interface ConsumeResult  差异内容：NA | 类名：iap；  API声明： interface ConsumeResult  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：ConsumeResult；  API声明：consumedPurchaseData: string;  差异内容：NA | 类名：ConsumeResult；  API声明：consumedPurchaseData: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：ConsumeResult；  API声明：signature: string;  差异内容：NA | 类名：ConsumeResult；  API声明：signature: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：ConsumeResult；  API声明：signatureAlgorithm: string;  差异内容：NA | 类名：ConsumeResult；  API声明：signatureAlgorithm: string;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context, callback: AsyncCallback<void>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array<Product>>): void;  差异内容：NA | 类名：iap；  API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array<Product>>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function purchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<PurchaseResult>;  差异内容：NA | 类名：iap；  API声明：function purchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<PurchaseResult>;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function purchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<PurchaseResult>): void;  差异内容：NA | 类名：iap；  API声明：function purchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<PurchaseResult>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void;  差异内容：NA | 类名：iap；  API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>;  差异内容：NA | 类名：iap；  API声明：function queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void;  差异内容：NA | 类名：iap；  API声明：function queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter): Promise<ConsumeResult>;  差异内容：NA | 类名：iap；  API声明：function consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter): Promise<ConsumeResult>;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter, callback: AsyncCallback<ConsumeResult>): void;  差异内容：NA | 类名：iap；  API声明：function consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter, callback: AsyncCallback<ConsumeResult>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：iap；  API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback<void>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>;  差异内容：NA | 类名：iap；  API声明：function queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void;  差异内容：NA | 类名：iap；  API声明：function queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API模型切换 | 类名：iap；  API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchaseResult>): void;  差异内容：NA | 类名：iap；  API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchaseResult>): void;  差异内容：stagemodelonly | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：ConsumePurchaseParameter；  API声明：purchaseToken: string;  差异内容：NA | 类名：ConsumePurchaseParameter；  API声明：purchaseToken: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：ConsumePurchaseParameter；  API声明：developerChallenge?: string;  差异内容：NA | 类名：ConsumePurchaseParameter；  API声明：developerChallenge?: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：QueryPurchasesResult；  API声明：productList: string[];  差异内容：NA | 类名：QueryPurchasesResult；  API声明：productList: string[];  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：QueryPurchasesResult；  API声明：inAppPurchaseDataList: string[];  差异内容：NA | 类名：QueryPurchasesResult；  API声明：inAppPurchaseDataList: string[];  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：QueryPurchasesResult；  API声明：inAppSignatureList: string[];  差异内容：NA | 类名：QueryPurchasesResult；  API声明：inAppSignatureList: string[];  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：QueryPurchasesResult；  API声明：continuationToken?: string;  差异内容：NA | 类名：QueryPurchasesResult；  API声明：continuationToken?: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：QueryPurchasesResult；  API声明：signatureAlgorithm: string;  差异内容：NA | 类名：QueryPurchasesResult；  API声明：signatureAlgorithm: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：PurchaseResult；  API声明：inAppPurchaseData: string;  差异内容：NA | 类名：PurchaseResult；  API声明：inAppPurchaseData: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：PurchaseResult；  API声明：signature: string;  差异内容：NA | 类名：PurchaseResult；  API声明：signature: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：PurchaseResult；  API声明：signatureAlgorithm: string;  差异内容：NA | 类名：PurchaseResult；  API声明：signatureAlgorithm: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：ConsumeResult；  API声明：consumedPurchaseData: string;  差异内容：NA | 类名：ConsumeResult；  API声明：consumedPurchaseData: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：ConsumeResult；  API声明：signature: string;  差异内容：NA | 类名：ConsumeResult；  API声明：signature: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| API废弃版本变更 | 类名：ConsumeResult；  API声明：signatureAlgorithm: string;  差异内容：NA | 类名：ConsumeResult；  API声明：signatureAlgorithm: string;  差异内容：4.1.0(11) | api/@hms.core.iap.d.ts |
| 错误码变更 | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context): Promise<void>;  差异内容：1001860000,1001860001,1001860004,1001860005,1001860050,1001860054,401 | 类名：iap；  API声明：function queryEnvironmentStatus(context: common.Context): Promise<void>;  差异内容：1001860000,1001860001,1001860002,1001860004,1001860005,1001860050,1001860054,401 | api/@hms.core.iap.d.ts |
| 错误码变更 | 类名：iap；  API声明：function showManagedSubscriptions(context: common.Context, uiParameter: UIWindowParameter, groupId?: string): Promise<void>;  差异内容：1001860001,1001860004,1001860005,1001860050,1001860054,401 | 类名：iap；  API声明：function showManagedSubscriptions(context: common.Context, uiParameter: UIWindowParameter, groupId?: string): Promise<void>;  差异内容：1001860001,1001860002,1001860004,1001860005,1001860050,1001860054,401 | api/@hms.core.iap.d.ts |
