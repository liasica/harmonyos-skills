---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-6011
title: Ability Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:55+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:971203e9e24b952e0578bb6cb925356744a93b72133e9d3b3de8689de2199bde
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：NA | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：12100014 | api/@ohos.abilityAccessCtrl.d.ts |
| 删除错误码 | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：12100010,401 | 类名：AtManager；  API声明：requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;  差异内容：NA | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace autoStartupManager  差异内容：declare namespace autoStartupManager | api/@ohos.app.ability.autoStartupManager.d.ts |
| 新增API | NA | 类名：autoStartupManager；  API声明：function getAutoStartupStatusForSelf(): Promise<boolean>;  差异内容：function getAutoStartupStatusForSelf(): Promise<boolean>; | api/@ohos.app.ability.autoStartupManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export type OnRequestSuccessFn = (name: string) => void;  差异内容：export type OnRequestSuccessFn = (name: string) => void; | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：global；  API声明：export type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void;  差异内容：export type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void; | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：global；  API声明：export class CompletionHandlerForAbilityStartCallback  差异内容：export class CompletionHandlerForAbilityStartCallback | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：CompletionHandlerForAbilityStartCallback；  API声明：onRequestSuccess?: OnRequestSuccessFn;  差异内容：onRequestSuccess?: OnRequestSuccessFn; | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：CompletionHandlerForAbilityStartCallback；  API声明：onRequestFailure?: OnRequestFailureFn;  差异内容：onRequestFailure?: OnRequestFailureFn; | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum AbilityStartFailureCode  差异内容：export enum AbilityStartFailureCode | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：AbilityStartFailureCode；  API声明：FAILURE\_CODE\_SYSTEM\_MALFUNCTION = 0  差异内容：FAILURE\_CODE\_SYSTEM\_MALFUNCTION = 0 | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：AbilityStartFailureCode；  API声明：FAILURE\_CODE\_USER\_CANCEL = 1  差异内容：FAILURE\_CODE\_USER\_CANCEL = 1 | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 新增API | NA | 类名：application；  API声明：export function exitMasterProcessRole(): Promise<void>;  差异内容：export function exitMasterProcessRole(): Promise<void>; | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function setDefaultErrorHandler(defaultHandler?: ErrorHandler): ErrorHandler;  差异内容：function setDefaultErrorHandler(defaultHandler?: ErrorHandler): ErrorHandler; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：export type ErrorHandler = (errObject: Error) => void;  差异内容：export type ErrorHandler = (errObject: Error) => void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：WEB\_NATIVE\_MESSAGING = 32  差异内容：WEB\_NATIVE\_MESSAGING = 32 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：FAULT\_LOG = 33  差异内容：FAULT\_LOG = 33 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function cleanBundleCacheFilesForSelf(): Promise<void>;  差异内容：function cleanBundleCacheFilesForSelf(): Promise<void>; | api/@ohos.bundle.bundleManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.ability.autoStartupManager.d.ts  差异内容：AbilityKit | api/@ohos.app.ability.autoStartupManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts  差异内容：AbilityKit | api/@ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：AbilityStartCallback；  API声明：completionHandler?: CompletionHandlerForAbilityStartCallback;  差异内容：completionHandler?: CompletionHandlerForAbilityStartCallback; | api/application/AbilityStartCallback.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OpenLinkOptions；  API声明：completionHandler?: CompletionHandler;  差异内容：completionHandler?: CompletionHandler; | api/@ohos.app.ability.OpenLinkOptions.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OpenLinkOptions；  API声明：hideFailureTipDialog?: boolean;  差异内容：hideFailureTipDialog?: boolean; | api/@ohos.app.ability.OpenLinkOptions.d.ts |
