---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-7002
title: Ability Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:25cde24f6ada229e58a28962e78364b3dd608a249dd6f46f0f93fe307a337ebe
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：export default class ActionExtensionAbility  差异内容：NA | 类名：global；  API声明：export default class ActionExtensionAbility  差异内容：26.0.0 | api/@ohos.app.ability.ActionExtensionAbility.d.ts |
| 新增错误码 | 类名：UIExtensionContentSession；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：UIExtensionContentSession；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void;  差异内容：16000001,16000002,16000004,16200001,201 | api/@ohos.app.ability.UIExtensionContentSession.d.ts |
| 新增错误码 | 类名：UIExtensionContentSession；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback): Promise<void>;  差异内容：NA | 类名：UIExtensionContentSession；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback): Promise<void>;  差异内容：16000001,16000002,16000004,16200001,201 | api/@ohos.app.ability.UIExtensionContentSession.d.ts |
| 新增错误码 | 类名：skillManager；  API声明：function getSkillInfosForSelf(flags: number): Promise<Array<SkillInfo>>;  差异内容：NA | 类名：skillManager；  API声明：function getSkillInfosForSelf(flags: number): Promise<Array<SkillInfo>>;  差异内容：17700101 | api/@ohos.bundle.skillManager.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：UIAbilityContext；  API声明：startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void;  差异内容：16000002,16000010 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：startAbilityByCall(want: Want): Promise<Caller>;  差异内容：NA | 类名：UIAbilityContext；  API声明：startAbilityByCall(want: Want): Promise<Caller>;  差异内容：16000005,16200001 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void;  差异内容：NA | 类名：UIAbilityContext；  API声明：startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void;  差异内容：16000002,16000010 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：terminateSelf(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：UIAbilityContext；  API声明：terminateSelf(callback: AsyncCallback<void>): void;  差异内容：16000001,16000004,16000005 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：terminateSelf(): Promise<void>;  差异内容：NA | 类名：UIAbilityContext；  API声明：terminateSelf(): Promise<void>;  差异内容：16000001,16000004,16000005 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：UIAbilityContext；  API声明：terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void;  差异内容：16000001,16000004,16000005 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：terminateSelfWithResult(parameter: AbilityResult): Promise<void>;  差异内容：NA | 类名：UIAbilityContext；  API声明：terminateSelfWithResult(parameter: AbilityResult): Promise<void>;  差异内容：16000001,16000004,16000005 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：UIAbilityContext；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void;  差异内容：16000001,16000002,16000004,16200001,201 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIAbilityContext；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback): Promise<void>;  差异内容：NA | 类名：UIAbilityContext；  API声明：startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback): Promise<void>;  差异内容：16000001,16000002,16000004,16200001,201 | api/application/UIAbilityContext.d.ts |
| 权限变更 | 类名：appManager；  API声明：function getRunningProcessInformation(): Promise<Array<ProcessInformation>>;  差异内容：NA | 类名：appManager；  API声明：function getRunningProcessInformation(): Promise<Array<ProcessInformation>>;  差异内容：ohos.permission.GET\_RUNNING\_INFO [since 9 - 10] | api/@ohos.app.ability.appManager.d.ts |
| 权限变更 | 类名：appManager；  API声明：function getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void;  差异内容：NA | 类名：appManager；  API声明：function getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void;  差异内容：ohos.permission.GET\_RUNNING\_INFO [since 9 - 10] | api/@ohos.app.ability.appManager.d.ts |
| 权限变更 | 类名：UIAbilityContext；  API声明：startAbilityByCall(want: Want): Promise<Caller>;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：UIAbilityContext；  API声明：startAbilityByCall(want: Want): Promise<Caller>;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC [since 11] | api/application/UIAbilityContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace pluginBundleManager  差异内容：declare namespace pluginBundleManager | api/@ohos.bundle.pluginBundleManager.d.ts |
| 新增API | NA | 类名：pluginBundleManager；  API声明：function installLocalPlugin(pluginFilePaths: Array<string>): Promise<void>;  差异内容：function installLocalPlugin(pluginFilePaths: Array<string>): Promise<void>; | api/@ohos.bundle.pluginBundleManager.d.ts |
| 新增API | NA | 类名：pluginBundleManager；  API声明：function uninstallLocalPlugin(pluginBundleName: string): Promise<void>;  差异内容：function uninstallLocalPlugin(pluginBundleName: string): Promise<void>; | api/@ohos.bundle.pluginBundleManager.d.ts |
| 新增API | NA | 类名：pluginBundleManager；  API声明：function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>;  差异内容：function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>; | api/@ohos.bundle.pluginBundleManager.d.ts |
| 新增API | NA | 类名：pluginBundleManager；  API声明：export type PluginBundleInfo = \_PluginBundleInfo;  差异内容：export type PluginBundleInfo = \_PluginBundleInfo; | api/@ohos.bundle.pluginBundleManager.d.ts |
| 新增API | NA | 类名：pluginBundleManager；  API声明：export type PluginModuleInfo = \_PluginModuleInfo;  差异内容：export type PluginModuleInfo = \_PluginModuleInfo; | api/@ohos.bundle.pluginBundleManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export default interface AutoFillRect  差异内容：export default interface AutoFillRect | api/application/AutoFillRect.d.ts |
| 新增API | NA | 类名：AutoFillRect；  API声明：left: number;  差异内容：left: number; | api/application/AutoFillRect.d.ts |
| 新增API | NA | 类名：AutoFillRect；  API声明：top: number;  差异内容：top: number; | api/application/AutoFillRect.d.ts |
| 新增API | NA | 类名：AutoFillRect；  API声明：width: number;  差异内容：width: number; | api/application/AutoFillRect.d.ts |
| 新增API | NA | 类名：AutoFillRect；  API声明：height: number;  差异内容：height: number; | api/application/AutoFillRect.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface FillRequest  差异内容：export interface FillRequest | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：FillRequest；  API声明：type: AutoFillType;  差异内容：type: AutoFillType; | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：FillRequest；  API声明：viewData: ViewData;  差异内容：viewData: ViewData; | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：FillRequest；  API声明：triggerType?: AutoFillTriggerType;  差异内容：triggerType?: AutoFillTriggerType; | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SaveRequest  差异内容：export interface SaveRequest | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：SaveRequest；  API声明：viewData: ViewData;  差异内容：viewData: ViewData; | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface FillFailureResult  差异内容：export interface FillFailureResult | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：FillFailureResult；  API声明：errCode: number;  差异内容：errCode: number; | api/application/AutoFillRequest.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum AutoFillTriggerType  差异内容：export enum AutoFillTriggerType | api/application/AutoFillTriggerType.d.ts |
| 新增API | NA | 类名：AutoFillTriggerType；  API声明：AUTO\_REQUEST = 0  差异内容：AUTO\_REQUEST = 0 | api/application/AutoFillTriggerType.d.ts |
| 新增API | NA | 类名：AutoFillTriggerType；  API声明：MANUAL\_REQUEST = 1  差异内容：MANUAL\_REQUEST = 1 | api/application/AutoFillTriggerType.d.ts |
| 新增API | NA | 类名：AutoFillTriggerType；  API声明：PASTE\_REQUEST = 2  差异内容：PASTE\_REQUEST = 2 | api/application/AutoFillTriggerType.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum AutoFillType  差异内容：export enum AutoFillType | api/application/AutoFillType.d.ts |
| 新增API | NA | 类名：AutoFillType；  API声明：UNSPECIFIED = 0  差异内容：UNSPECIFIED = 0 | api/application/AutoFillType.d.ts |
| 新增API | NA | 类名：AutoFillType；  API声明：PASSWORD = 1  差异内容：PASSWORD = 1 | api/application/AutoFillType.d.ts |
| 新增API | NA | 类名：AutoFillType；  API声明：USER\_NAME = 2  差异内容：USER\_NAME = 2 | api/application/AutoFillType.d.ts |
| 新增API | NA | 类名：AutoFillType；  API声明：NEW\_PASSWORD = 3  差异内容：NEW\_PASSWORD = 3 | api/application/AutoFillType.d.ts |
| 新增API | NA | 类名：global；  API声明：export default interface PageNodeInfo  差异内容：export default interface PageNodeInfo | api/application/PageNodeInfo.d.ts |
| 新增API | NA | 类名：PageNodeInfo；  API声明：id: number;  差异内容：id: number; | api/application/PageNodeInfo.d.ts |
| 新增API | NA | 类名：PageNodeInfo；  API声明：autoFillType: AutoFillType;  差异内容：autoFillType: AutoFillType; | api/application/PageNodeInfo.d.ts |
| 新增API | NA | 类名：PageNodeInfo；  API声明：value: string;  差异内容：value: string; | api/application/PageNodeInfo.d.ts |
| 新增API | NA | 类名：PageNodeInfo；  API声明：placeholder?: string;  差异内容：placeholder?: string; | api/application/PageNodeInfo.d.ts |
| 新增API | NA | 类名：PageNodeInfo；  API声明：rect: AutoFillRect;  差异内容：rect: AutoFillRect; | api/application/PageNodeInfo.d.ts |
| 新增API | NA | 类名：PageNodeInfo；  API声明：isFocus: boolean;  差异内容：isFocus: boolean; | api/application/PageNodeInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export default interface ViewData  差异内容：export default interface ViewData | api/application/ViewData.d.ts |
| 新增API | NA | 类名：ViewData；  API声明：bundleName: string;  差异内容：bundleName: string; | api/application/ViewData.d.ts |
| 新增API | NA | 类名：ViewData；  API声明：pageUrl: string;  差异内容：pageUrl: string; | api/application/ViewData.d.ts |
| 新增API | NA | 类名：ViewData；  API声明：pageNodeInfos: Array<PageNodeInfo>;  差异内容：pageNodeInfos: Array<PageNodeInfo>; | api/application/ViewData.d.ts |
| 新增API | NA | 类名：ViewData；  API声明：pageRect: AutoFillRect;  差异内容：pageRect: AutoFillRect; | api/application/ViewData.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface PluginBundleInfo  差异内容：export interface PluginBundleInfo | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly label: string;  差异内容：readonly label: string; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly labelId: number;  差异内容：readonly labelId: number; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly icon: string;  差异内容：readonly icon: string; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly iconId: number;  差异内容：readonly iconId: number; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly pluginBundleName: string;  差异内容：readonly pluginBundleName: string; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly versionCode: number;  差异内容：readonly versionCode: number; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly versionName: string;  差异内容：readonly versionName: string; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginBundleInfo；  API声明：readonly pluginModuleInfos: Array<PluginModuleInfo>;  差异内容：readonly pluginModuleInfos: Array<PluginModuleInfo>; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface PluginModuleInfo  差异内容：export interface PluginModuleInfo | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginModuleInfo；  API声明：readonly moduleName: string;  差异内容：readonly moduleName: string; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginModuleInfo；  API声明：readonly descriptionId: number;  差异内容：readonly descriptionId: number; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：PluginModuleInfo；  API声明：readonly description: string;  差异内容：readonly description: string; | api/bundleManager/PluginBundleInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface AlternateIconInfo  差异内容：export interface AlternateIconInfo | api/bundleManager/BundleInfo.d.ts |
| 新增API | NA | 类名：AlternateIconInfo；  API声明：readonly iconName: string;  差异内容：readonly iconName: string; | api/bundleManager/BundleInfo.d.ts |
| 新增API | NA | 类名：AlternateIconInfo；  API声明：readonly iconId: number;  差异内容：readonly iconId: number; | api/bundleManager/BundleInfo.d.ts |
| 新增API | NA | 类名：AlternateIconInfo；  API声明：readonly enabled: boolean;  差异内容：readonly enabled: boolean; | api/bundleManager/BundleInfo.d.ts |
| 新增API | NA | 类名：WindowMode；  API声明：WINDOW\_MODE\_SPLIT = 105  差异内容：WINDOW\_MODE\_SPLIT = 105 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：ApplicationContext；  API声明：enableDelayedProcessExit(): Promise<void>;  差异内容：enableDelayedProcessExit(): Promise<void>; | api/application/ApplicationContext.d.ts |
| 新增API | NA | 类名：ApplicationContext；  API声明：disableDelayedProcessExit(): Promise<void>;  差异内容：disableDelayedProcessExit(): Promise<void>; | api/application/ApplicationContext.d.ts |
| 新增API | NA | 类名：ApplicationContext；  API声明：startSelfUIAbility(want: Want): Promise<void>;  差异内容：startSelfUIAbility(want: Want): Promise<void>; | api/application/ApplicationContext.d.ts |
| 新增API | NA | 类名：ApplicationContext；  API声明：getUIAbilityByInstanceId(instanceId: string): UIAbility;  差异内容：getUIAbilityByInstanceId(instanceId: string): UIAbility; | api/application/ApplicationContext.d.ts |
| 新增API | NA | 类名：UIAbilityContext；  API声明：startSelf(): Promise<void>;  差异内容：startSelf(): Promise<void>; | api/application/UIAbilityContext.d.ts |
| 新增API | NA | 类名：UIAbilityContext；  API声明：startSelfUIAbilityInChildProcess(want: Want, specifiedFlag: string): Promise<void>;  差异内容：startSelfUIAbilityInChildProcess(want: Want, specifiedFlag: string): Promise<void>; | api/application/UIAbilityContext.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：type OnFillSuccessFn = (viewData: ViewData) => void;  差异内容：type OnFillSuccessFn = (viewData: ViewData) => void; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：type OnFillFailureFn = (result: FillFailureResult) => void;  差异内容：type OnFillFailureFn = (result: FillFailureResult) => void; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export interface AutoFillCallback  差异内容：export interface AutoFillCallback | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：AutoFillCallback；  API声明：onSuccess: OnFillSuccessFn;  差异内容：onSuccess: OnFillSuccessFn; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：AutoFillCallback；  API声明：onFailure: OnFillFailureFn;  差异内容：onFailure: OnFillFailureFn; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export function requestAutoFill(context: UIContext, request: FillRequest, callback?: AutoFillCallback): void;  差异内容：export function requestAutoFill(context: UIContext, request: FillRequest, callback?: AutoFillCallback): void; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export type ViewData = \_ViewData.default;  差异内容：export type ViewData = \_ViewData.default; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export type PageNodeInfo = \_PageNodeInfo.default;  差异内容：export type PageNodeInfo = \_PageNodeInfo.default; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export type FillRequest = \_AutoFillRequest.FillRequest;  差异内容：export type FillRequest = \_AutoFillRequest.FillRequest; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export type SaveRequest = \_AutoFillRequest.SaveRequest;  差异内容：export type SaveRequest = \_AutoFillRequest.SaveRequest; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export type FillFailureResult = \_FillFailureResult;  差异内容：export type FillFailureResult = \_FillFailureResult; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：autoFillManager；  API声明：export type AutoFillRect = \_AutoFillRect.default;  差异内容：export type AutoFillRect = \_AutoFillRect.default; | api/@ohos.app.ability.autoFillManager.d.ts |
| 新增API | NA | 类名：childProcessManager；  API声明：function isArkChildProcessSupported(): boolean;  差异内容：function isArkChildProcessSupported(): boolean; | api/@ohos.app.ability.childProcessManager.d.ts |
| 新增API | NA | 类名：childProcessManager；  API声明：function isNativeChildProcessSupported(): boolean;  差异内容：function isNativeChildProcessSupported(): boolean; | api/@ohos.app.ability.childProcessManager.d.ts |
| 新增API | NA | 类名：UIAbility；  API声明：isDestroyed: boolean;  差异内容：isDestroyed: boolean; | api/@ohos.app.ability.UIAbility.d.ts |
| 新增API | NA | 类名：wantConstant；  API声明：export enum Action  差异内容：export enum Action | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Action；  API声明：ACTION\_SEND\_TO\_DATA = 'ohos.want.action.sendToData'  差异内容：ACTION\_SEND\_TO\_DATA = 'ohos.want.action.sendToData' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：MODULAR\_OBJECT = 39  差异内容：MODULAR\_OBJECT = 39 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getAlternateIcons(): Promise<Array<AlternateIconInfo>>;  差异内容：function getAlternateIcons(): Promise<Array<AlternateIconInfo>>; | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function setAlternateIcon(alternateIconName: string): Promise<void>;  差异内容：function setAlternateIcon(alternateIconName: string): Promise<void>; | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：export type AlternateIconInfo = \_BundleInfo.AlternateIconInfo;  差异内容：export type AlternateIconInfo = \_BundleInfo.AlternateIconInfo; | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly version?: string;  差异内容：readonly version?: string; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly visibility?: string;  差异内容：readonly visibility?: string; | api/bundleManager/SkillInfo.d.ts |
| 起始版本有变化 | 类名：global；  API声明：declare namespace launcherBundleManager  差异内容：18 | 类名：global；  API声明：declare namespace launcherBundleManager  差异内容：9 | api/@ohos.bundle.launcherBundleManager.d.ts |
| 起始版本有变化 | 类名：AbilityDelegator；  API声明：print(msg: string, callback: AsyncCallback<void>): void;  差异内容：8 | 类名：AbilityDelegator；  API声明：print(msg: string, callback: AsyncCallback<void>): void;  差异内容：9 | api/application/AbilityDelegator.d.ts |
| 起始版本有变化 | 类名：AbilityDelegator；  API声明：print(msg: string): Promise<void>;  差异内容：8 | 类名：AbilityDelegator；  API声明：print(msg: string): Promise<void>;  差异内容：9 | api/application/AbilityDelegator.d.ts |
| 起始版本有变化 | 类名：AbilityDelegator；  API声明：executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void;  差异内容：8 | 类名：AbilityDelegator；  API声明：executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void;  差异内容：9 | api/application/AbilityDelegator.d.ts |
| 起始版本有变化 | 类名：AbilityDelegator；  API声明：executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void;  差异内容：8 | 类名：AbilityDelegator；  API声明：executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void;  差异内容：9 | api/application/AbilityDelegator.d.ts |
| 起始版本有变化 | 类名：AbilityDelegator；  API声明：executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>;  差异内容：8 | 类名：AbilityDelegator；  API声明：executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>;  差异内容：9 | api/application/AbilityDelegator.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.bundle.pluginBundleManager.d.ts  差异内容：AbilityKit | api/@ohos.bundle.pluginBundleManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\AutoFillRect.d.ts  差异内容：AbilityKit | api/application/AutoFillRect.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\AutoFillRequest.d.ts  差异内容：AbilityKit | api/application/AutoFillRequest.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\AutoFillTriggerType.d.ts  差异内容：AbilityKit | api/application/AutoFillTriggerType.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\AutoFillType.d.ts  差异内容：AbilityKit | api/application/AutoFillType.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\PageNodeInfo.d.ts  差异内容：AbilityKit | api/application/PageNodeInfo.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\ViewData.d.ts  差异内容：AbilityKit | api/application/ViewData.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\bundleManager\PluginBundleInfo.d.ts  差异内容：AbilityKit | api/bundleManager/PluginBundleInfo.d.ts |
