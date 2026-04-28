---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-b123sp18
title: Payment Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Payment Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:05fb0739f29ef24af59f0d126f4b0981e3281f6f69b11d5102177cbaa3c3de92
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：paymentService；  API声明：function requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult>;  差异内容：function requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult>; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：paymentService；  API声明：function cashierPicker(context: common.UIAbilityContext, paymentInfo: PaymentInfo): Promise<PickerResult>;  差异内容：function cashierPicker(context: common.UIAbilityContext, paymentInfo: PaymentInfo): Promise<PickerResult>; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：paymentService；  API声明： interface PaymentInfo  差异内容： interface PaymentInfo | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PaymentInfo；  API声明：tradeSummary?: string;  差异内容：tradeSummary?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PaymentInfo；  API声明：amount?: number;  差异内容：amount?: number; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PaymentInfo；  API声明：currency?: string;  差异内容：currency?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PaymentInfo；  API声明：extraInfo?: string;  差异内容：extraInfo?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：paymentService；  API声明： interface PickerResult  差异内容： interface PickerResult | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PickerResult；  API声明：selectedPaymentType?: string;  差异内容：selectedPaymentType?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PickerResult；  API声明：clientToken?: string;  差异内容：clientToken?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：paymentService；  API声明： interface PayResult  差异内容： interface PayResult | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PayResult；  API声明：selectedPaymentType?: string;  差异内容：selectedPaymentType?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PayResult；  API声明：clientToken?: string;  差异内容：clientToken?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PayResult；  API声明：nextStep?: string;  差异内容：nextStep?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PayResult；  API声明：extraInfo?: string;  差异内容：extraInfo?: string; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：PayResult；  API声明：payload?: string;  差异内容：payload?: string; | api/@hms.core.payment.paymentService.d.ts |
