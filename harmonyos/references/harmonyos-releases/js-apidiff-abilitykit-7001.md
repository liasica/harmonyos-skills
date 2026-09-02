---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-7001
title: Ability Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:fa995c067f71961e825037b8d54237634b0a8e06fcfb6137cf239a990d9afb24
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace scriptManager  差异内容：declare namespace scriptManager | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：scriptManager；  API声明：interface ArkTSScriptInfo  差异内容：interface ArkTSScriptInfo | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：ArkTSScriptInfo；  API声明：readonly requestCode: string;  差异内容：readonly requestCode: string; | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：ArkTSScriptInfo；  API声明：readonly context: Context;  差异内容：readonly context: Context; | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：scriptManager；  API声明：interface ExecuteResult  差异内容：interface ExecuteResult | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：ExecuteResult；  API声明：code: number;  差异内容：code: number; | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：ExecuteResult；  API声明：result?: Record<string, Object>;  差异内容：result?: Record<string, Object>; | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：ExecuteResult；  API声明：uris?: Array<string>;  差异内容：uris?: Array<string>; | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：ExecuteResult；  API声明：flags?: number;  差异内容：flags?: number; | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：scriptManager；  API声明：function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>;  差异内容：function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>; | api/@ohos.app.ability.scriptManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace agentConstant  差异内容：declare namespace agentConstant | api/@ohos.app.agent.agentConstant.d.ts |
| 新增API | NA | 类名：agentConstant；  API声明：export enum AgentCardType  差异内容：export enum AgentCardType | api/@ohos.app.agent.agentConstant.d.ts |
| 新增API | NA | 类名：AgentCardType；  API声明：APP = 0  差异内容：APP = 0 | api/@ohos.app.agent.agentConstant.d.ts |
| 新增API | NA | 类名：AgentCardType；  API声明：ATOMIC\_SERVICE = 1  差异内容：ATOMIC\_SERVICE = 1 | api/@ohos.app.agent.agentConstant.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace skillManager  差异内容：declare namespace skillManager | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：export enum SkillInfoFlag  差异内容：export enum SkillInfoFlag | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：SkillInfoFlag；  API声明：GET\_SKILL\_INFO\_DEFAULT = 0x00000000  差异内容：GET\_SKILL\_INFO\_DEFAULT = 0x00000000 | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：SkillInfoFlag；  API声明：GET\_SKILL\_INFO\_WITH\_DESCRIPTION = 0x00000001  差异内容：GET\_SKILL\_INFO\_WITH\_DESCRIPTION = 0x00000001 | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：SkillInfoFlag；  API声明：GET\_SKILL\_INFO\_WITH\_SRC\_ENTRIES = 0x00000002  差异内容：GET\_SKILL\_INFO\_WITH\_SRC\_ENTRIES = 0x00000002 | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：SkillInfoFlag；  API声明：GET\_SKILL\_INFO\_WITH\_PERMISSIONS = 0x00000004  差异内容：GET\_SKILL\_INFO\_WITH\_PERMISSIONS = 0x00000004 | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：SkillInfoFlag；  API声明：GET\_SKILL\_INFO\_WITH\_REQUEST\_PERMISSIONS = 0x00000008  差异内容：GET\_SKILL\_INFO\_WITH\_REQUEST\_PERMISSIONS = 0x00000008 | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：function getSkillInfoForSelf(moduleName: string, skillName: string, flags: number): Promise<SkillInfo>;  差异内容：function getSkillInfoForSelf(moduleName: string, skillName: string, flags: number): Promise<SkillInfo>; | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：function getSkillInfosForSelf(flags: number): Promise<Array<SkillInfo>>;  差异内容：function getSkillInfosForSelf(flags: number): Promise<Array<SkillInfo>>; | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：function getSkillInfo(bundleName: string, moduleName: string, skillName: string, flags: number, userId?: number): Promise<SkillInfo>;  差异内容：function getSkillInfo(bundleName: string, moduleName: string, skillName: string, flags: number, userId?: number): Promise<SkillInfo>; | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：function getSkillInfos(bundleName: string, flags: number, userId?: number): Promise<Array<SkillInfo>>;  差异内容：function getSkillInfos(bundleName: string, flags: number, userId?: number): Promise<Array<SkillInfo>>; | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：function getAllSkillInfos(flags: number, userId?: number): Promise<Array<SkillInfo>>;  差异内容：function getAllSkillInfos(flags: number, userId?: number): Promise<Array<SkillInfo>>; | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：export type SkillInfo = \_SkillInfo;  差异内容：export type SkillInfo = \_SkillInfo; | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：skillManager；  API声明：export type SkillType = \_SkillType;  差异内容：export type SkillType = \_SkillType; | api/@ohos.bundle.skillManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SkillInfo  差异内容：export interface SkillInfo | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly bundleName: string;  差异内容：readonly bundleName: string; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly moduleName: string;  差异内容：readonly moduleName: string; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly skillName: string;  差异内容：readonly skillName: string; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly skillType: SkillType;  差异内容：readonly skillType: SkillType; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly skillPath: string;  差异内容：readonly skillPath: string; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly abilityName: string;  差异内容：readonly abilityName: string; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly versionCode: number;  差异内容：readonly versionCode: number; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly description?: string;  差异内容：readonly description?: string; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly srcEntries?: Array<string>;  差异内容：readonly srcEntries?: Array<string>; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly permissions?: Array<string>;  差异内容：readonly permissions?: Array<string>; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillInfo；  API声明：readonly requestPermissions?: Array<string>;  差异内容：readonly requestPermissions?: Array<string>; | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum SkillType  差异内容：export enum SkillType | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillType；  API声明：APP\_SKILL = 0  差异内容：APP\_SKILL = 0 | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：SkillType；  API声明：INDEPENDENT\_SKILL = 1  差异内容：INDEPENDENT\_SKILL = 1 | api/bundleManager/SkillInfo.d.ts |
| 新增API | NA | 类名：abilityManager；  API声明：function isEmbeddedUIExtensionSupported(): boolean;  差异内容：function isEmbeddedUIExtensionSupported(): boolean; | api/@ohos.app.ability.abilityManager.d.ts |
| 新增API | NA | 类名：autoStartupManager；  API声明：function isAutoStartupSupported(): boolean;  差异内容：function isAutoStartupSupported(): boolean; | api/@ohos.app.ability.autoStartupManager.d.ts |
| 新增API | NA | 类名：contextConstant；  API声明：export enum ContextType  差异内容：export enum ContextType | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：ContextType；  API声明：APPLICATION\_CONTEXT = 0  差异内容：APPLICATION\_CONTEXT = 0 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：ContextType；  API声明：ABILITY\_STAGE\_CONTEXT = 1  差异内容：ABILITY\_STAGE\_CONTEXT = 1 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：ContextType；  API声明：UIABILITY\_CONTEXT = 2  差异内容：UIABILITY\_CONTEXT = 2 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：ContextType；  API声明：FORM\_EXTENSION\_CONTEXT = 3  差异内容：FORM\_EXTENSION\_CONTEXT = 3 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：ContextType；  API声明：APP\_SERVICE\_EXTENSION\_CONTEXT = 4  差异内容：APP\_SERVICE\_EXTENSION\_CONTEXT = 4 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：errorManager；  API声明：function setDefaultFreezeObserver(defaultObserver?: FreezeObserver): FreezeObserver;  差异内容：function setDefaultFreezeObserver(defaultObserver?: FreezeObserver): FreezeObserver; | api/@ohos.app.ability.errorManager.d.ts |
| 新增API | NA | 类名：insightIntent；  API声明：enum QueryType  差异内容：enum QueryType | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：QueryType；  API声明：ALL = 'all'  差异内容：ALL = 'all' | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：QueryType；  API声明：BY\_PROPERTY = 'byProperty'  差异内容：BY\_PROPERTY = 'byProperty' | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：insightIntent；  API声明：interface QueryEntityParam  差异内容：interface QueryEntityParam | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：QueryEntityParam；  API声明：queryType: QueryType;  差异内容：queryType: QueryType; | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：QueryEntityParam；  API声明：parameters?: Record<string, Object>;  差异内容：parameters?: Record<string, Object>; | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：insightIntent；  API声明：abstract class AppIntentEntity  差异内容：abstract class AppIntentEntity | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：AppIntentEntity；  API声明：abstract onQueryEntity(params: QueryEntityParam): Promise<Array<T>>;  差异内容：abstract onQueryEntity(params: QueryEntityParam): Promise<Array<T>>; | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：AppIntentEntity；  API声明：displayName: string;  差异内容：displayName: string; | api/@ohos.app.ability.insightIntent.d.ts |
| 新增API | NA | 类名：IntentEntityDecoratorInfo；  API声明：supportedQueryProperties?: string[];  差异内容：supportedQueryProperties?: string[]; | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：StartOptions；  API声明：splitRatio?: window.SplitRatioPreference;  差异内容：splitRatio?: window.SplitRatioPreference; | api/@ohos.app.ability.StartOptions.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getInstalledBundleList(bundleFlags: number): Promise<Array<BundleInfo>>;  差异内容：function getInstalledBundleList(bundleFlags: number): Promise<Array<BundleInfo>>; | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getApplicationLabel(bundleName: string, appIndex: number): Promise<string>;  差异内容：function getApplicationLabel(bundleName: string, appIndex: number): Promise<string>; | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：shortcutManager；  API声明：function isShortcutSupported(): boolean;  差异内容：function isShortcutSupported(): boolean; | api/@ohos.bundle.shortcutManager.d.ts |
| 新增API | NA | 类名：AgentCard；  API声明：type?: agentConstant.AgentCardType;  差异内容：type?: agentConstant.AgentCardType; | api/application/AgentCard.d.ts |
| 新增API | NA | 类名：Context；  API声明：isContextOf(contextType: contextConstant.ContextType): boolean;  差异内容：isContextOf(contextType: contextConstant.ContextType): boolean; | api/application/Context.d.ts |
| 新增API | NA | 类名：ProcessInformation；  API声明：isPreload?: boolean;  差异内容：isPreload?: boolean; | api/application/ProcessInformation.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.ability.scriptManager.d.ts  差异内容：AbilityKit | api/@ohos.app.ability.scriptManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.agent.agentConstant.d.ts  差异内容：AbilityKit | api/@ohos.app.agent.agentConstant.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.bundle.skillManager.d.ts  差异内容：AbilityKit | api/@ohos.bundle.skillManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\bundleManager\SkillInfo.d.ts  差异内容：AbilityKit | api/bundleManager/SkillInfo.d.ts |
