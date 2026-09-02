---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-7002
title: Payment Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Payment Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:92e19ad9620970c5ad61d15fc4f28bf3334fa6b97a5cfa1b70301b6d2df4fc87
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：paymentService；  API声明：function requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult>;  差异内容：NA | 类名：paymentService；  API声明：function requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult>;  差异内容：801 | api/@hms.core.payment.paymentService.d.ts |
| 新增错误码 | 类名：paymentService；  API声明：function requestPayment(context: common.UIAbilityContext, orderStr: string): Promise<void>;  差异内容：NA | 类名：paymentService；  API声明：function requestPayment(context: common.UIAbilityContext, orderStr: string): Promise<void>;  差异内容：801 | api/@hms.core.payment.paymentService.d.ts |
| 新增错误码 | 类名：paymentService；  API声明：function requestPayment(context: common.UIAbilityContext, orderStr: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：paymentService；  API声明：function requestPayment(context: common.UIAbilityContext, orderStr: string, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.core.payment.paymentService.d.ts |
| 新增错误码 | 类名：paymentService；  API声明：function cashierPicker(context: common.UIAbilityContext, paymentInfo: PaymentInfo): Promise<PickerResult>;  差异内容：NA | 类名：paymentService；  API声明：function cashierPicker(context: common.UIAbilityContext, paymentInfo: PaymentInfo): Promise<PickerResult>;  差异内容：801 | api/@hms.core.payment.paymentService.d.ts |
| 新增错误码 | 类名：paymentService；  API声明：function requestContract(context: common.UIAbilityContext, contractStr: string): Promise<void>;  差异内容：NA | 类名：paymentService；  API声明：function requestContract(context: common.UIAbilityContext, contractStr: string): Promise<void>;  差异内容：801 | api/@hms.core.payment.paymentService.d.ts |
| 新增错误码 | 类名：paymentService；  API声明：function requestContract(context: common.UIAbilityContext, contractStr: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：paymentService；  API声明：function requestContract(context: common.UIAbilityContext, contractStr: string, callback: AsyncCallback<void>): void;  差异内容：801 | api/@hms.core.payment.paymentService.d.ts |
| 新增错误码 | 类名：paymentService；  API声明：function requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult>;  差异内容：NA | 类名：paymentService；  API声明：function requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult>;  差异内容：801 | api/@hms.core.payment.paymentService.d.ts |
| 新增错误码 | 类名：realNameService；  API声明：function startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>;  差异内容：NA | 类名：realNameService；  API声明：function startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>;  差异内容：801 | api/@hms.core.payment.realNameService.d.ts |
| 新增错误码 | 类名：realNameService；  API声明：function startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>;  差异内容：NA | 类名：realNameService；  API声明：function startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>;  差异内容：801 | api/@hms.core.payment.realNameService.d.ts |
| 新增错误码 | 类名：realNameService；  API声明：function startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>;  差异内容：NA | 类名：realNameService；  API声明：function startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>;  差异内容：801 | api/@hms.core.payment.realNameService.d.ts |
| 新增错误码 | 类名：ThirdPayClient；  API声明：handlePayCallback(want: Want): boolean;  差异内容：NA | 类名：ThirdPayClient；  API声明：handlePayCallback(want: Want): boolean;  差异内容：801 | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增错误码 | 类名：ThirdPayClient；  API声明：pay(payInfo: string): Promise<void>;  差异内容：NA | 类名：ThirdPayClient；  API声明：pay(payInfo: string): Promise<void>;  差异内容：801 | api/@hms.core.payment.thirdPaymentService.d.ts |
