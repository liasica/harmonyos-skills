---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-26011
title: IAP Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > IAP Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:74bb97e97e90dd269e91bdef6fba29d249b4c40b1cbd2dd5ef8deae2f63909fd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：iap；  API声明：interface QueryPaymentPromotionParam  差异内容：interface QueryPaymentPromotionParam | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：QueryPaymentPromotionParam；  API声明：productId: string;  差异内容：productId: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：QueryPaymentPromotionParam；  API声明：microMarkedPrice: number;  差异内容：microMarkedPrice: number; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：QueryPaymentPromotionParam；  API声明：currency: string;  差异内容：currency: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：iap；  API声明：interface PaymentPromotion  差异内容：interface PaymentPromotion | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PaymentPromotion；  API声明：productId: string;  差异内容：productId: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PaymentPromotion；  API声明：microDiscountAmount?: number;  差异内容：microDiscountAmount?: number; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PaymentPromotion；  API声明：currency?: string;  差异内容：currency?: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PaymentPromotion；  API声明：promotionText?: string;  差异内容：promotionText?: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：iap；  API声明：function queryPaymentPromotions(context: common.Context, params: QueryPaymentPromotionParam[]): Promise<Array<PaymentPromotion>>;  差异内容：function queryPaymentPromotions(context: common.Context, params: QueryPaymentPromotionParam[]): Promise<Array<PaymentPromotion>>; | api/@hms.core.iap.d.ts |
