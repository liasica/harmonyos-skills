---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-appgallerykit-6002
title: AppGallery Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > AppGallery Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:24+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1f937b5da203b9f480d3a792db247953c8e7b2ae380c7b774f436d00966e3cf4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：appInfoManager；  API声明：function selectDynamicIcon(iconId: string): Promise<void>;  差异内容：NA | 类名：appInfoManager；  API声明：function selectDynamicIcon(iconId: string): Promise<void>;  差异内容：1006800013 | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace commentManager  差异内容：declare namespace commentManager | api/@hms.core.appgalleryservice.commentManager.d.ts |
| 新增API | NA | 类名：commentManager；  API声明：function showCommentDialog(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void>;  差异内容：function showCommentDialog(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void>; | api/@hms.core.appgalleryservice.commentManager.d.ts |
| 新增API | NA | 类名：updateManager；  API声明：interface UpdateSessionState  差异内容：interface UpdateSessionState | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：UpdateSessionState；  API声明：readonly code: RequestErrorCode;  差异内容：readonly code: RequestErrorCode; | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：UpdateSessionState；  API声明：readonly checkUpdateResult?: CheckUpdateResult;  差异内容：readonly checkUpdateResult?: CheckUpdateResult; | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：updateManager；  API声明：export enum RequestErrorCode  差异内容：export enum RequestErrorCode | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：RequestErrorCode；  API声明：NO\_UPGRADE = 0  差异内容：NO\_UPGRADE = 0 | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：RequestErrorCode；  API声明：NEED\_UPGRADE = 1  差异内容：NEED\_UPGRADE = 1 | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：RequestErrorCode；  API声明：DOWNLOADED = 2  差异内容：DOWNLOADED = 2 | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：updateManager；  API声明：function on(type: 'updateChange', callback: Callback<UpdateSessionState>, timeout?: number): void;  差异内容：function on(type: 'updateChange', callback: Callback<UpdateSessionState>, timeout?: number): void; | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：updateManager；  API声明：function off(type: 'updateChange', callback?: Callback<UpdateSessionState>): void;  差异内容：function off(type: 'updateChange', callback?: Callback<UpdateSessionState>): void; | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.appgalleryservice.commentManager.d.ts  差异内容：AppGalleryKit | api/@hms.core.appgalleryservice.commentManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace updateManager  差异内容：NA | 类名：global；  API声明：declare namespace updateManager  差异内容：atomicservice | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：updateManager；  API声明：export enum UpdateAvailableCode  差异内容：NA | 类名：updateManager；  API声明：export enum UpdateAvailableCode  差异内容：atomicservice | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：UpdateAvailableCode；  API声明：LATER\_VERSION\_EXIST = 1  差异内容：NA | 类名：UpdateAvailableCode；  API声明：LATER\_VERSION\_EXIST = 1  差异内容：atomicservice | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：UpdateAvailableCode；  API声明：LATER\_VERSION\_NOT\_EXIST = 0  差异内容：NA | 类名：UpdateAvailableCode；  API声明：LATER\_VERSION\_NOT\_EXIST = 0  差异内容：atomicservice | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：updateManager；  API声明：export interface CheckUpdateResult  差异内容：NA | 类名：updateManager；  API声明：export interface CheckUpdateResult  差异内容：atomicservice | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：CheckUpdateResult；  API声明：readonly updateAvailable: UpdateAvailableCode;  差异内容：NA | 类名：CheckUpdateResult；  API声明：readonly updateAvailable: UpdateAvailableCode;  差异内容：atomicservice | api/@hms.core.appgalleryservice.updateManager.d.ts |
