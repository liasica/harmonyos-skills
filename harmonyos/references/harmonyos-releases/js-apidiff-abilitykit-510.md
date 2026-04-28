---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-510
title: Ability Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:59dd5bbbced0175f7bd56ed56ac0fefb0540a8831b1c69ddc58f7a3459ff10ee
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace continueManager  差异内容：declare namespace continueManager | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：continueManager；  API声明：function on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void;  差异内容：function on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void; | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：continueManager；  API声明：function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void;  差异内容：function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void; | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：continueManager；  API声明：interface ContinueResultInfo  差异内容：interface ContinueResultInfo | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：ContinueResultInfo；  API声明：resultState: ContinueStateCode;  差异内容：resultState: ContinueStateCode; | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：ContinueResultInfo；  API声明：resultInfo?: string;  差异内容：resultInfo?: string; | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：continueManager；  API声明：enum ContinueStateCode  差异内容：enum ContinueStateCode | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：ContinueStateCode；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：ContinueStateCode；  API声明：SYSTEM\_ERROR  差异内容：SYSTEM\_ERROR | api/@ohos.app.ability.continueManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace launcherBundleManager  差异内容：declare namespace launcherBundleManager | api/@ohos.bundle.launcherBundleManager.d.ts |
| 新增API | NA | 类名：launcherBundleManager；  API声明：function getLauncherAbilityInfoSync(bundleName: string, userId: number): Array<LauncherAbilityInfo>;  差异内容：function getLauncherAbilityInfoSync(bundleName: string, userId: number): Array<LauncherAbilityInfo>; | api/@ohos.bundle.launcherBundleManager.d.ts |
| 新增API | NA | 类名：launcherBundleManager；  API声明：export type LauncherAbilityInfo = \_LauncherAbilityInfo;  差异内容：export type LauncherAbilityInfo = \_LauncherAbilityInfo; | api/@ohos.bundle.launcherBundleManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface LauncherAbilityInfo  差异内容：export interface LauncherAbilityInfo | api/bundleManager/LauncherAbilityInfo.d.ts |
| 新增API | NA | 类名：LauncherAbilityInfo；  API声明：readonly applicationInfo: ApplicationInfo;  差异内容：readonly applicationInfo: ApplicationInfo; | api/bundleManager/LauncherAbilityInfo.d.ts |
| 新增API | NA | 类名：LauncherAbilityInfo；  API声明：readonly elementName: ElementName;  差异内容：readonly elementName: ElementName; | api/bundleManager/LauncherAbilityInfo.d.ts |
| 新增API | NA | 类名：LauncherAbilityInfo；  API声明：readonly labelId: number;  差异内容：readonly labelId: number; | api/bundleManager/LauncherAbilityInfo.d.ts |
| 新增API | NA | 类名：LauncherAbilityInfo；  API声明：readonly iconId: number;  差异内容：readonly iconId: number; | api/bundleManager/LauncherAbilityInfo.d.ts |
| 新增API | NA | 类名：LauncherAbilityInfo；  API声明：readonly userId: number;  差异内容：readonly userId: number; | api/bundleManager/LauncherAbilityInfo.d.ts |
| 新增API | NA | 类名：LauncherAbilityInfo；  API声明：readonly installTime: number;  差异内容：readonly installTime: number; | api/bundleManager/LauncherAbilityInfo.d.ts |
| 新增API | NA | 类名：screenLockFileManager；  API声明：export enum KeyStatus  差异内容：export enum KeyStatus | api/@ohos.ability.screenLockFileManager.d.ts |
| 新增API | NA | 类名：KeyStatus；  API声明：KEY\_NOT\_EXIST = -2  差异内容：KEY\_NOT\_EXIST = -2 | api/@ohos.ability.screenLockFileManager.d.ts |
| 新增API | NA | 类名：KeyStatus；  API声明：KEY\_RELEASED = -1  差异内容：KEY\_RELEASED = -1 | api/@ohos.ability.screenLockFileManager.d.ts |
| 新增API | NA | 类名：KeyStatus；  API声明：KEY\_EXIST = 0  差异内容：KEY\_EXIST = 0 | api/@ohos.ability.screenLockFileManager.d.ts |
| 新增API | NA | 类名：screenLockFileManager；  API声明：function queryAppKeyState(): KeyStatus;  差异内容：function queryAppKeyState(): KeyStatus; | api/@ohos.ability.screenLockFileManager.d.ts |
| 新增API | NA | 类名：abilityAccessCtrl；  API声明：export enum PermissionStateChangeType  差异内容：export enum PermissionStateChangeType | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：PermissionStateChangeType；  API声明：PERMISSION\_REVOKED\_OPER = 0  差异内容：PERMISSION\_REVOKED\_OPER = 0 | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：PermissionStateChangeType；  API声明：PERMISSION\_GRANTED\_OPER = 1  差异内容：PERMISSION\_GRANTED\_OPER = 1 | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：abilityAccessCtrl；  API声明：interface PermissionStateChangeInfo  差异内容：interface PermissionStateChangeInfo | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：PermissionStateChangeInfo；  API声明：change: PermissionStateChangeType;  差异内容：change: PermissionStateChangeType; | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：PermissionStateChangeInfo；  API声明：tokenID: number;  差异内容：tokenID: number; | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：PermissionStateChangeInfo；  API声明：permissionName: Permissions;  差异内容：permissionName: Permissions; | api/@ohos.abilityAccessCtrl.d.ts |
| 新增API | NA | 类名：AbilityConstant；  API声明：export interface LastExitDetailInfo  差异内容：export interface LastExitDetailInfo | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：pid: number;  差异内容：pid: number; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：processName: string;  差异内容：processName: string; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：uid: number;  差异内容：uid: number; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：exitSubReason: number;  差异内容：exitSubReason: number; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：exitMsg: string;  差异内容：exitMsg: string; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：rss: number;  差异内容：rss: number; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：pss: number;  差异内容：pss: number; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitDetailInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitReason；  API声明：USER\_REQUEST = 9  差异内容：USER\_REQUEST = 9 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：LastExitReason；  API声明：SIGNAL = 10  差异内容：SIGNAL = 10 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：AbilityConstant；  API声明：export enum CollaborateResult  差异内容：export enum CollaborateResult | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：CollaborateResult；  API声明：ACCEPT = 0  差异内容：ACCEPT = 0 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：CollaborateResult；  API声明：REJECT = 1  差异内容：REJECT = 1 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function on(type: 'globalErrorOccurred', observer: GlobalObserver): void;  差异内容：function on(type: 'globalErrorOccurred', observer: GlobalObserver): void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void;  差异内容：function on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function off(type: 'globalErrorOccurred', observer?: GlobalObserver): void;  差异内容：function off(type: 'globalErrorOccurred', observer?: GlobalObserver): void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void;  差异内容：function off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：export type GlobalObserver = (reason: GlobalError) => void;  差异内容：export type GlobalObserver = (reason: GlobalError) => void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：export interface GlobalError  差异内容：export interface GlobalError | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：GlobalError；  API声明：instanceName: string;  差异内容：instanceName: string; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：GlobalError；  API声明：instanceType: InstanceType;  差异内容：instanceType: InstanceType; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：export enum InstanceType  差异内容：export enum InstanceType | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：InstanceType；  API声明：MAIN = 0  差异内容：MAIN = 0 | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：InstanceType；  API声明：WORKER = 1  差异内容：WORKER = 1 | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：InstanceType；  API声明：TASKPOOL = 2  差异内容：TASKPOOL = 2 | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：InstanceType；  API声明：CUSTOM = 3  差异内容：CUSTOM = 3 | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function on(type: 'freeze', observer: FreezeObserver): void;  差异内容：function on(type: 'freeze', observer: FreezeObserver): void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function off(type: 'freeze', observer?: FreezeObserver): void;  差异内容：function off(type: 'freeze', observer?: FreezeObserver): void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：export type FreezeObserver = () => void;  差异内容：export type FreezeObserver = () => void; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：Params；  API声明：LAUNCH\_REASON\_MESSAGE = 'ohos.params.launchReasonMessage'  差异内容：LAUNCH\_REASON\_MESSAGE = 'ohos.params.launchReasonMessage' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Flags；  API声明：FLAG\_ABILITY\_ON\_COLLABORATE = 0x00002000  差异内容：FLAG\_ABILITY\_ON\_COLLABORATE = 0x00002000 | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：FENCE = 24  差异内容：FENCE = 24 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：ASSET\_ACCELERATION = 26  差异内容：ASSET\_ACCELERATION = 26 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：FORM\_EDIT = 27  差异内容：FORM\_EDIT = 27 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getSignatureInfo(uid: number): SignatureInfo;  差异内容：function getSignatureInfo(uid: number): SignatureInfo; | api/@ohos.bundle.bundleManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.ability.continueManager.d.ts  差异内容：AbilityKit | api/@ohos.app.ability.continueManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.bundle.launcherBundleManager.d.ts  差异内容：AbilityKit | api/@ohos.bundle.launcherBundleManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\bundleManager\LauncherAbilityInfo.d.ts  差异内容：AbilityKit | api/bundleManager/LauncherAbilityInfo.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：PermissionRequestResult；  API声明：errorReasons?: Array<number>;  差异内容：errorReasons?: Array<number>; | api/security/PermissionRequestResult.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIAbilityContext；  API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void;  差异内容：setColorMode(colorMode: ConfigurationConstant.ColorMode): void; | api/application/UIAbilityContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIAbility；  API声明：onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult;  差异内容：onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult; | api/@ohos.app.ability.UIAbility.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIExtensionContentSession；  API声明：loadContentByName(name: string, storage?: LocalStorage): void;  差异内容：loadContentByName(name: string, storage?: LocalStorage): void; | api/@ohos.app.ability.UIExtensionContentSession.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Context；  API声明：processName: string;  差异内容：processName: string; | api/application/Context.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Context；  API声明：createAreaModeContext(areaMode: contextConstant.AreaMode): Context;  差异内容：createAreaModeContext(areaMode: contextConstant.AreaMode): Context; | api/application/Context.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIExtensionContext；  API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void;  差异内容：setColorMode(colorMode: ConfigurationConstant.ColorMode): void; | api/application/UIExtensionContext.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AtManager；  API声明：on(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback: Callback<PermissionStateChangeInfo>): void;  差异内容：on(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback: Callback<PermissionStateChangeInfo>): void; | api/@ohos.abilityAccessCtrl.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AtManager；  API声明：off(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback?: Callback<PermissionStateChangeInfo>): void;  差异内容：off(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback?: Callback<PermissionStateChangeInfo>): void; | api/@ohos.abilityAccessCtrl.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LaunchParam；  API声明：launchReasonMessage?: string;  差异内容：launchReasonMessage?: string; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LaunchParam；  API声明：lastExitDetailInfo?: LastExitDetailInfo;  差异内容：lastExitDetailInfo?: LastExitDetailInfo; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ExecuteResult；  API声明：uris?: Array<string>;  差异内容：uris?: Array<string>; | api/@ohos.app.ability.insightIntent.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ExecuteResult；  API声明：flags?: number;  差异内容：flags?: number; | api/@ohos.app.ability.insightIntent.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BundleInfo；  API声明：readonly firstInstallTime?: number;  差异内容：readonly firstInstallTime?: number; | api/bundleManager/BundleInfo.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Metadata；  API声明：readonly valueId?: number;  差异内容：readonly valueId?: number; | api/bundleManager/Metadata.d.ts |
