---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-6002
title: Ability Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:23+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:12cb5564f6450c3b8291ff67da90caea93ba9710be42a946ce9c01ecf5cdbbe7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：AppServiceExtensionContext；  API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number;  差异内容：want: Want, options: ConnectOptions | 类名：AppServiceExtensionContext；  API声明：connectServiceExtensionAbility(want: Want, callback: ConnectOptions): number;  差异内容：want: Want, callback: ConnectOptions | api/application/AppServiceExtensionContext.d.ts |
| 函数变更 | 类名：UIAbilityContext；  API声明：connectAppServiceExtensionAbility(want: Want, options: ConnectOptions): number;  差异内容：want: Want, options: ConnectOptions | 类名：UIAbilityContext；  API声明：connectAppServiceExtensionAbility(want: Want, callback: ConnectOptions): number;  差异内容：want: Want, callback: ConnectOptions | api/application/UIAbilityContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace kioskManager  差异内容：declare namespace kioskManager | api/@ohos.app.ability.kioskManager.d.ts |
| 新增API | NA | 类名：kioskManager；  API声明：function enterKioskMode(context: UIAbilityContext): Promise<void>;  差异内容：function enterKioskMode(context: UIAbilityContext): Promise<void>; | api/@ohos.app.ability.kioskManager.d.ts |
| 新增API | NA | 类名：kioskManager；  API声明：function exitKioskMode(context: UIAbilityContext): Promise<void>;  差异内容：function exitKioskMode(context: UIAbilityContext): Promise<void>; | api/@ohos.app.ability.kioskManager.d.ts |
| 新增API | NA | 类名：kioskManager；  API声明：export type KioskStatus = \_KioskStatus;  差异内容：export type KioskStatus = \_KioskStatus; | api/@ohos.app.ability.kioskManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace shortcutManager  差异内容：declare namespace shortcutManager | api/@ohos.bundle.shortcutManager.d.ts |
| 新增API | NA | 类名：shortcutManager；  API声明：function setShortcutVisibleForSelf(id: string, visible: boolean): Promise<void>;  差异内容：function setShortcutVisibleForSelf(id: string, visible: boolean): Promise<void>; | api/@ohos.bundle.shortcutManager.d.ts |
| 新增API | NA | 类名：shortcutManager；  API声明：function getAllShortcutInfoForSelf(): Promise<Array<ShortcutInfo>>;  差异内容：function getAllShortcutInfoForSelf(): Promise<Array<ShortcutInfo>>; | api/@ohos.bundle.shortcutManager.d.ts |
| 新增API | NA | 类名：shortcutManager；  API声明：export type ShortcutInfo = \_ShortcutInfo;  差异内容：export type ShortcutInfo = \_ShortcutInfo; | api/@ohos.bundle.shortcutManager.d.ts |
| 新增API | NA | 类名：shortcutManager；  API声明：export type ShortcutWant = \_ShortcutWant;  差异内容：export type ShortcutWant = \_ShortcutWant; | api/@ohos.bundle.shortcutManager.d.ts |
| 新增API | NA | 类名：shortcutManager；  API声明：export type ParameterItem = \_ParameterItem;  差异内容：export type ParameterItem = \_ParameterItem; | api/@ohos.bundle.shortcutManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface KioskStatus  差异内容：export interface KioskStatus | api/application/KioskStatus.d.ts |
| 新增API | NA | 类名：KioskStatus；  API声明：isKioskMode: boolean;  差异内容：isKioskMode: boolean; | api/application/KioskStatus.d.ts |
| 新增API | NA | 类名：KioskStatus；  API声明：kioskBundleName: string;  差异内容：kioskBundleName: string; | api/application/KioskStatus.d.ts |
| 新增API | NA | 类名：KioskStatus；  API声明：kioskBundleUid: number;  差异内容：kioskBundleUid: number; | api/application/KioskStatus.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ShortcutInfo  差异内容：export interface ShortcutInfo | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：id: string;  差异内容：id: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：moduleName?: string;  差异内容：moduleName?: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：hostAbility?: string;  差异内容：hostAbility?: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：icon?: string;  差异内容：icon?: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：iconId?: number;  差异内容：iconId?: number; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：label?: string;  差异内容：label?: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：labelId?: number;  差异内容：labelId?: number; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：wants?: Array<ShortcutWant>;  差异内容：wants?: Array<ShortcutWant>; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：appIndex: number;  差异内容：appIndex: number; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：sourceType: number;  差异内容：sourceType: number; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutInfo；  API声明：visible?: boolean;  差异内容：visible?: boolean; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ShortcutWant  差异内容：export interface ShortcutWant | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutWant；  API声明：targetBundle: string;  差异内容：targetBundle: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutWant；  API声明：targetModule?: string;  差异内容：targetModule?: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutWant；  API声明：targetAbility: string;  差异内容：targetAbility: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ShortcutWant；  API声明：parameters?: Array<ParameterItem>;  差异内容：parameters?: Array<ParameterItem>; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ParameterItem  差异内容：export interface ParameterItem | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ParameterItem；  API声明：key: string;  差异内容：key: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：ParameterItem；  API声明：value: string;  差异内容：value: string; | api/bundleManager/ShortcutInfo.d.ts |
| 新增API | NA | 类名：abilityManager；  API声明：function restartSelfAtomicService(context: Context): void;  差异内容：function restartSelfAtomicService(context: Context): void; | api/@ohos.app.ability.abilityManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface FormIntentDecoratorInfo  差异内容：declare interface FormIntentDecoratorInfo | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：FormIntentDecoratorInfo；  API声明：formName: string;  差异内容：formName: string; | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const InsightIntentForm: ((intentInfo: FormIntentDecoratorInfo) => ClassDecorator);  差异内容：export declare const InsightIntentForm: ((intentInfo: FormIntentDecoratorInfo) => ClassDecorator); | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface IntentEntityDecoratorInfo  差异内容：declare interface IntentEntityDecoratorInfo | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：IntentEntityDecoratorInfo；  API声明：entityCategory: string;  差异内容：entityCategory: string; | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：IntentEntityDecoratorInfo；  API声明：parameters?: Record<string, Object>;  差异内容：parameters?: Record<string, Object>; | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const InsightIntentEntity: ((intentEntityInfo: IntentEntityDecoratorInfo) => ClassDecorator);  差异内容：export declare const InsightIntentEntity: ((intentEntityInfo: IntentEntityDecoratorInfo) => ClassDecorator); | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增API | NA | 类名：AbilityConstant；  API声明：const REASON\_MESSAGE\_DESKTOP\_SHORTCUT = 'ReasonMessage\_DesktopShortcut';  差异内容：const REASON\_MESSAGE\_DESKTOP\_SHORTCUT = 'ReasonMessage\_DesktopShortcut'; | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：contextConstant；  API声明：export enum Scenarios  差异内容：export enum Scenarios | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：Scenarios；  API声明：SCENARIO\_MOVE\_MISSION\_TO\_FRONT = 0x00000001  差异内容：SCENARIO\_MOVE\_MISSION\_TO\_FRONT = 0x00000001 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：Scenarios；  API声明：SCENARIO\_SHOW\_ABILITY = 0x00000002  差异内容：SCENARIO\_SHOW\_ABILITY = 0x00000002 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：Scenarios；  API声明：SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT = 0x00000004  差异内容：SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT = 0x00000004 | api/@ohos.app.ability.contextConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：ABILITY\_UNIFIED\_DATA\_KEY = 'ohos.param.ability.udKey'  差异内容：ABILITY\_UNIFIED\_DATA\_KEY = 'ohos.param.ability.udKey' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Params；  API声明：ATOMIC\_SERVICE\_SHARE\_ROUTER = 'ohos.params.atomicservice.shareRouter'  差异内容：ATOMIC\_SERVICE\_SHARE\_ROUTER = 'ohos.params.atomicservice.shareRouter' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType；  API声明：DISTRIBUTED = 28  差异内容：DISTRIBUTED = 28 | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：launcherBundleManager；  API声明：export type ShortcutInfo = \_ShortcutInfo;  差异内容：export type ShortcutInfo = \_ShortcutInfo; | api/@ohos.bundle.launcherBundleManager.d.ts |
| 新增API | NA | 类名：launcherBundleManager；  API声明：export type ShortcutWant = \_ShortcutWant;  差异内容：export type ShortcutWant = \_ShortcutWant; | api/@ohos.bundle.launcherBundleManager.d.ts |
| 新增API | NA | 类名：launcherBundleManager；  API声明：export type ParameterItem = \_ParameterItem;  差异内容：export type ParameterItem = \_ParameterItem; | api/@ohos.bundle.launcherBundleManager.d.ts |
| 删除API | 类名：Configuration；  API声明：locale?: Intl.Locale;  差异内容：locale?: Intl.Locale; | NA | api/@ohos.app.ability.Configuration.d.ts |
| 删除API | 类名：IntentDecoratorInfo；  API声明：example?: string;  差异内容：example?: string; | NA | api/@ohos.app.ability.InsightIntentDecorator.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.app.ability.kioskManager.d.ts  差异内容：AbilityKit | api/@ohos.app.ability.kioskManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.bundle.shortcutManager.d.ts  差异内容：AbilityKit | api/@ohos.bundle.shortcutManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\KioskStatus.d.ts  差异内容：AbilityKit | api/application/KioskStatus.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\bundleManager\ShortcutInfo.d.ts  差异内容：AbilityKit | api/bundleManager/ShortcutInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace abilityManager  差异内容：NA | 类名：global；  API声明：declare namespace abilityManager  差异内容：atomicservice | api/@ohos.app.ability.abilityManager.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：AppServiceExtensionContext；  API声明：startAbility(want: Want, options?: StartOptions): Promise<void>;  差异内容：startAbility(want: Want, options?: StartOptions): Promise<void>; | api/application/AppServiceExtensionContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIAbilityContext；  API声明：setOnNewWantSkipScenarios(scenarios: number): Promise<void>;  差异内容：setOnNewWantSkipScenarios(scenarios: number): Promise<void>; | api/application/UIAbilityContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIAbility；  API声明：onWillForeground(): void;  差异内容：onWillForeground(): void; | api/@ohos.app.ability.UIAbility.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIAbility；  API声明：onDidForeground(): void;  差异内容：onDidForeground(): void; | api/@ohos.app.ability.UIAbility.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIAbility；  API声明：onWillBackground(): void;  差异内容：onWillBackground(): void; | api/@ohos.app.ability.UIAbility.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIAbility；  API声明：onDidBackground(): void;  差异内容：onDidBackground(): void; | api/@ohos.app.ability.UIAbility.d.ts |
