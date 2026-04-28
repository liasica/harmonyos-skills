---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-b105
title: Payment Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Payment Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:37148b0bcea8a4a464e448b4e390678761cf925f1482d71e1c229e077be1e037
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace ecnyPaymentService  差异内容： declare namespace ecnyPaymentService | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：ecnyPaymentService；  API声明：function requestEcnyPayment(context: common.Context, orderInfo: EcnyOrderInfo): Promise<EcnyPayResult>;  差异内容：function requestEcnyPayment(context: common.Context, orderInfo: EcnyOrderInfo): Promise<EcnyPayResult>; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：ecnyPaymentService；  API声明： interface EcnyOrderInfo  差异内容： interface EcnyOrderInfo | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：merchantAppId: string;  差异内容：merchantAppId: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：merchantNo: string;  差异内容：merchantNo: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：acqAgtInstnId?: string;  差异内容：acqAgtInstnId?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：creditorInstitutionId: string;  差异内容：creditorInstitutionId: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：encryptedKey: string;  差异内容：encryptedKey: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：encryptedInfo: string;  差异内容：encryptedInfo: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：encryptionSN?: string;  差异内容：encryptionSN?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：lastWalletId?: string;  差异内容：lastWalletId?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo；  API声明：extraInfo?: string;  差异内容：extraInfo?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：ecnyPaymentService；  API声明： interface EcnyPayResult  差异内容： interface EcnyPayResult | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyPayResult；  API声明：orderNo: string;  差异内容：orderNo: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyPayResult；  API声明：extraInfo?: string;  差异内容：extraInfo?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
