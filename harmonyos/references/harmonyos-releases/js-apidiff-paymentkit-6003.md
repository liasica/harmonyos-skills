---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-6003
title: Payment Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Payment Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:21+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1300660c4bd4f25ae112cdefb8302f6ceef093b0712458165b9bf2f1c8c1178b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace thirdPaymentService  差异内容：declare namespace thirdPaymentService | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：thirdPaymentService；  API声明：class ThirdPayClient  差异内容：class ThirdPayClient | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：ThirdPayClient；  API声明：handlePayCallback(want: Want): boolean;  差异内容：handlePayCallback(want: Want): boolean; | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：ThirdPayClient；  API声明：pay(payInfo: string): Promise<void>;  差异内容：pay(payInfo: string): Promise<void>; | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：thirdPaymentService；  API声明：enum PayMethod  差异内容：enum PayMethod | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：PayMethod；  API声明：WECHAT\_PAY = 'wechat\_pay'  差异内容：WECHAT\_PAY = 'wechat\_pay' | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：PayMethod；  API声明：ALI\_PAY = 'ali\_pay'  差异内容：ALI\_PAY = 'ali\_pay' | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：PayMethod；  API声明：WECHAT\_MINI\_PROGRAM = 'wechat\_mini\_program'  差异内容：WECHAT\_MINI\_PROGRAM = 'wechat\_mini\_program' | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.payment.thirdPaymentService.d.ts  差异内容：PaymentKit | api/@hms.core.payment.thirdPaymentService.d.ts |
