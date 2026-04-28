---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-5032
title: IAP Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > IAP Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ee840b711e738969033a90a0edd6783e919f27815af18cf5a9917a054b1529b3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PurchaseParameter；  API声明：quantity?: number;  差异内容：quantity?: number; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：iap；  API声明：function createRefundRequest(context: common.Context, purchaseOrderId: string): Promise<void>;  差异内容：function createRefundRequest(context: common.Context, purchaseOrderId: string): Promise<void>; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode；  API声明：PURCHASE\_ALREADY\_REFUNDED = 1001860061  差异内容：PURCHASE\_ALREADY\_REFUNDED = 1001860061 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode；  API声明：REFUND\_NOT\_ALLOWED = 1001860062  差异内容：REFUND\_NOT\_ALLOWED = 1001860062 | api/@hms.core.iap.d.ts |
