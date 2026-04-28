---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-5051
title: Payment Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > API变更清单 > Payment Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:20+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:40455e0e308767568398710e218861c979e9bf7510fc3b660974bd1a49cdbd38
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：paymentService；  API声明：interface BindCardResult  差异内容：interface BindCardResult | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：BindCardResult；  API声明：hasBankCard: boolean;  差异内容：hasBankCard: boolean; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：BindCardResult；  API声明：hasJustBoundCard?: boolean;  差异内容：hasJustBoundCard?: boolean; | api/@hms.core.payment.paymentService.d.ts |
| 新增API | NA | 类名：paymentService；  API声明：function requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult>;  差异内容：function requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult>; | api/@hms.core.payment.paymentService.d.ts |
