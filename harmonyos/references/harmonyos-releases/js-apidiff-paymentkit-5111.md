---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-5111
title: Payment Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Payment Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7872fd0c96f9b604dbb2170d41b89f29e541b134fae757ae213e1b44965543a1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace realNameService  差异内容：declare namespace realNameService | api/@hms.core.payment.realNameService.d.ts |
| 新增API | NA | 类名：realNameService；  API声明：function startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>;  差异内容：function startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>; | api/@hms.core.payment.realNameService.d.ts |
| 新增API | NA | 类名：realNameService；  API声明：function startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>;  差异内容：function startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>; | api/@hms.core.payment.realNameService.d.ts |
| 新增API | NA | 类名：realNameService；  API声明：function startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>;  差异内容：function startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>; | api/@hms.core.payment.realNameService.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.payment.realNameService.d.ts  差异内容：PaymentKit | api/@hms.core.payment.realNameService.d.ts |
