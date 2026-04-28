---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-appgallerykit-6101
title: AppGallery Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > AppGallery Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1e6061f51ff87ca4a02908f5eac34cbb367e03ce257a66f42113f80dc6cbdc20
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：export enum AppPrivacyMgmtType  差异内容：NA | 类名：privacyManager；  API声明：export enum AppPrivacyMgmtType  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyMgmtType；  API声明：UNSUPPORTED = 0  差异内容：NA | 类名：AppPrivacyMgmtType；  API声明：UNSUPPORTED = 0  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyMgmtType；  API声明：FULL\_MODE = 1  差异内容：NA | 类名：AppPrivacyMgmtType；  API声明：FULL\_MODE = 1  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：export enum AppPrivacyLinkType  差异内容：NA | 类名：privacyManager；  API声明：export enum AppPrivacyLinkType  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyLinkType；  API声明：PRIVACY\_STATEMENT\_LINK = 1  差异内容：NA | 类名：AppPrivacyLinkType；  API声明：PRIVACY\_STATEMENT\_LINK = 1  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyLinkType；  API声明：USER\_AGREEMENT\_LINK = 2  差异内容：NA | 类名：AppPrivacyLinkType；  API声明：USER\_AGREEMENT\_LINK = 2  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：export interface AppPrivacyMgmtInfo  差异内容：NA | 类名：privacyManager；  API声明：export interface AppPrivacyMgmtInfo  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyMgmtInfo；  API声明：readonly type: AppPrivacyMgmtType;  差异内容：NA | 类名：AppPrivacyMgmtInfo；  API声明：readonly type: AppPrivacyMgmtType;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyMgmtInfo；  API声明：readonly privacyInfo: AppPrivacyLink[];  差异内容：NA | 类名：AppPrivacyMgmtInfo；  API声明：readonly privacyInfo: AppPrivacyLink[];  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：export interface AppPrivacyLink  差异内容：NA | 类名：privacyManager；  API声明：export interface AppPrivacyLink  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyLink；  API声明：readonly type: AppPrivacyLinkType;  差异内容：NA | 类名：AppPrivacyLink；  API声明：readonly type: AppPrivacyLinkType;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyLink；  API声明：readonly versionCode: number;  差异内容：NA | 类名：AppPrivacyLink；  API声明：readonly versionCode: number;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyLink；  API声明：readonly url: string;  差异内容：NA | 类名：AppPrivacyLink；  API声明：readonly url: string;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyLink；  API声明：readonly id: string;  差异内容：NA | 类名：AppPrivacyLink；  API声明：readonly id: string;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppPrivacyLink；  API声明：readonly name?: string;  差异内容：NA | 类名：AppPrivacyLink；  API声明：readonly name?: string;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：export interface ConsentResult  差异内容：NA | 类名：privacyManager；  API声明：export interface ConsentResult  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ConsentResult；  API声明：readonly results: AppPrivacyResult[];  差异内容：NA | 类名：ConsentResult；  API声明：readonly results: AppPrivacyResult[];  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：function getAppPrivacyMgmtInfo(): AppPrivacyMgmtInfo;  差异内容：NA | 类名：privacyManager；  API声明：function getAppPrivacyMgmtInfo(): AppPrivacyMgmtInfo;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：function disableService(): void;  差异内容：NA | 类名：privacyManager；  API声明：function disableService(): void;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：privacyManager；  API声明：function requestAppPrivacyConsent(context: common.UIAbilityContext): Promise<ConsentResult>;  差异内容：NA | 类名：privacyManager；  API声明：function requestAppPrivacyConsent(context: common.UIAbilityContext): Promise<ConsentResult>;  差异内容：atomicservice | api/@hms.core.appgalleryservice.privacyManager.d.ts |
