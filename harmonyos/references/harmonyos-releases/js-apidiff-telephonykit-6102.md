---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-6102
title: Telephony Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta2引入的变更 > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b532179220fbd701aa327e6f7c93d7973ca89637fa388bdc649bb34245a4011c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：vcard；  API声明：export enum VCardType  差异内容：export enum VCardType | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：VCardType；  API声明：VERSION\_21 = 0  差异内容：VERSION\_21 = 0 | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：VCardType；  API声明：VERSION\_30 = 1  差异内容：VERSION\_30 = 1 | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：VCardType；  API声明：VERSION\_40 = 2  差异内容：VERSION\_40 = 2 | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：vcard；  API声明：export interface VCardBuilderOptions  差异内容：export interface VCardBuilderOptions | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：VCardBuilderOptions；  API声明：cardType?: VCardType;  差异内容：cardType?: VCardType; | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：VCardBuilderOptions；  API声明：charset?: string;  差异内容：charset?: string; | api/@ohos.telephony.vcard.d.ts |
| 起始版本有变化 | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void;  差异内容：11 | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void;  差异内容：23 | api/@ohos.telephony.vcard.d.ts |
| 起始版本有变化 | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, accountId?: number): Promise<void>;  差异内容：11 | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, accountId?: number): Promise<void>;  差异内容：23 | api/@ohos.telephony.vcard.d.ts |
| 起始版本有变化 | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void;  差异内容：11 | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void;  差异内容：23 | api/@ohos.telephony.vcard.d.ts |
| 起始版本有变化 | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuilderOptions, callback: AsyncCallback<string>): void;  差异内容：11 | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuilderOptions, callback: AsyncCallback<string>): void;  差异内容：23 | api/@ohos.telephony.vcard.d.ts |
| 起始版本有变化 | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>;  差异内容：11 | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>;  差异内容：23 | api/@ohos.telephony.vcard.d.ts |
| 起始版本有变化 | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void;  差异内容：11 | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void;  差异内容：23 | api/@ohos.telephony.vcard.d.ts |
