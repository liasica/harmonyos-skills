---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-6101
title: Payment Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Payment Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7366d7c14b433db058aa13a0f63c10fbf5fc9a426d8bf5ff66076fc38066a2ad
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace promotionService  差异内容：declare namespace promotionService | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：class PromotionComponentController  差异内容：class PromotionComponentController | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：PromotionComponentController；  API声明：public startPromotionEntryDialog(mercNo: string, offset?: number): Promise<UserAction>;  差异内容：public startPromotionEntryDialog(mercNo: string, offset?: number): Promise<UserAction>; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：function startPromotionDetailPopup(context: common.Context, mercNo: string): Promise<UserAction>;  差异内容：function startPromotionDetailPopup(context: common.Context, mercNo: string): Promise<UserAction>; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：function startUserChooseCouponsPopup(context: common.Context, orderContext: OrderContext): Promise<CouponDetail[]>;  差异内容：function startUserChooseCouponsPopup(context: common.Context, orderContext: OrderContext): Promise<CouponDetail[]>; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：interface UserAction  差异内容：interface UserAction | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：UserAction；  API声明：doNothing: boolean;  差异内容：doNothing: boolean; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：UserAction；  API声明：useButtonClicked: boolean;  差异内容：useButtonClicked: boolean; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：UserAction；  API声明：receiveButtonClicked: boolean;  差异内容：receiveButtonClicked: boolean; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：interface OrderContext  差异内容：interface OrderContext | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：OrderContext；  API声明：mercNo: string;  差异内容：mercNo: string; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：OrderContext；  API声明：tradeOrderAmount: number;  差异内容：tradeOrderAmount: number; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：OrderContext；  API声明：goodsCodes?: string[];  差异内容：goodsCodes?: string[]; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：OrderContext；  API声明：authId: string;  差异内容：authId: string; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：OrderContext；  API声明：sign: string;  差异内容：sign: string; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：enum CouponCategory  差异内容：enum CouponCategory | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponCategory；  API声明：PLATFORM\_COUPON = 0  差异内容：PLATFORM\_COUPON = 0 | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：enum CouponType  差异内容：enum CouponType | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponType；  API声明：VOUCHER = 0  差异内容：VOUCHER = 0 | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：promotionService；  API声明：interface CouponDetail  差异内容：interface CouponDetail | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：couponCategory: CouponCategory;  差异内容：couponCategory: CouponCategory; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：couponCode: string;  差异内容：couponCode: string; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：batchNo: string;  差异内容：batchNo: string; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：couponType: CouponType;  差异内容：couponType: CouponType; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：effectiveTime: number;  差异内容：effectiveTime: number; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：expireTime: number;  差异内容：expireTime: number; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：amount?: number;  差异内容：amount?: number; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：logoUrl: string;  差异内容：logoUrl: string; | api/@hms.core.payment.promotionService.d.ets |
| 新增API | NA | 类名：CouponDetail；  API声明：couponDesc: string;  差异内容：couponDesc: string; | api/@hms.core.payment.promotionService.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.payment.promotionService.d.ets  差异内容：PaymentKit | api/@hms.core.payment.promotionService.d.ets |
