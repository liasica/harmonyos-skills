---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-storekit-b031
title: Store Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Store Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d5c92373ac8966fcb4057abb6f0202259370a9094796f8d0126dc240ab76488c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace privacyManager  差异内容： declare namespace privacyManager | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明： export enum AppPrivacyMgmtType  差异内容： export enum AppPrivacyMgmtType | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyMgmtType；  API声明：UNSUPPORTED = 0  差异内容：UNSUPPORTED = 0 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyMgmtType；  API声明：FULL\_MODE = 1  差异内容：FULL\_MODE = 1 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明： export enum AppPrivacyResultType  差异内容： export enum AppPrivacyResultType | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyResultType；  API声明：DISAGREED = 0  差异内容：DISAGREED = 0 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyResultType；  API声明：FULL\_MODE\_AGREED = 1  差异内容：FULL\_MODE\_AGREED = 1 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明： export enum AppPrivacyLinkType  差异内容： export enum AppPrivacyLinkType | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyLinkType；  API声明：PRIVACY\_STATEMENT\_LINK = 1  差异内容：PRIVACY\_STATEMENT\_LINK = 1 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyLinkType；  API声明：USER\_AGREEMENT\_LINK = 2  差异内容：USER\_AGREEMENT\_LINK = 2 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明： export enum AppPrivacyType  差异内容： export enum AppPrivacyType | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyType；  API声明：PRIVACY\_AGREEMENT = 1  差异内容：PRIVACY\_AGREEMENT = 1 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyType；  API声明：USER\_AGREEMENT = 2  差异内容：USER\_AGREEMENT = 2 | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明： export interface AppPrivacyMgmtInfo  差异内容： export interface AppPrivacyMgmtInfo | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyMgmtInfo；  API声明：readonly type: AppPrivacyMgmtType;  差异内容：readonly type: AppPrivacyMgmtType; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyMgmtInfo；  API声明：readonly privacyInfo: AppPrivacyLink[];  差异内容：readonly privacyInfo: AppPrivacyLink[]; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明： export interface AppPrivacyLink  差异内容： export interface AppPrivacyLink | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyLink；  API声明：readonly type: AppPrivacyLinkType;  差异内容：readonly type: AppPrivacyLinkType; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyLink；  API声明：readonly versionCode: number;  差异内容：readonly versionCode: number; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyLink；  API声明：readonly url: string;  差异内容：readonly url: string; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyLink；  API声明：readonly id: string;  差异内容：readonly id: string; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明： export interface AppPrivacyResult  差异内容： export interface AppPrivacyResult | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyResult；  API声明：readonly type: AppPrivacyType;  差异内容：readonly type: AppPrivacyType; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyResult；  API声明：readonly versionCode: number;  差异内容：readonly versionCode: number; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyResult；  API声明：readonly result: AppPrivacyResultType;  差异内容：readonly result: AppPrivacyResultType; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyResult；  API声明：readonly id: string;  差异内容：readonly id: string; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明：function getAppPrivacyMgmtInfo(): AppPrivacyMgmtInfo;  差异内容：function getAppPrivacyMgmtInfo(): AppPrivacyMgmtInfo; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明：function getAppPrivacyResult(): AppPrivacyResult[];  差异内容：function getAppPrivacyResult(): AppPrivacyResult[]; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager；  API声明：function disableService(): void;  差异内容：function disableService(): void; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
