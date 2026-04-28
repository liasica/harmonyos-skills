---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-6001
title: Screen Time Guard Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Screen Time Guard Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:51648f6669c6c746d3986c5da13246dba48e909f4dfb2ad892fbc32995ad199c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace appPicker  差异内容：declare namespace appPicker | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增API | NA | 类名：appPicker；  API声明：function startAppPicker(context: common.Context, appSelection: AppInfo): Promise<string[]>;  差异内容：function startAppPicker(context: common.Context, appSelection: AppInfo): Promise<string[]>; | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace guardService  差异内容：declare namespace guardService | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：enum GuardServiceErrorCode  差异内容：enum GuardServiceErrorCode | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：INTERNAL\_ERROR = 1019000001  差异内容：INTERNAL\_ERROR = 1019000001 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：USER\_NOT\_AUTHORIZED = 1019000002  差异内容：USER\_NOT\_AUTHORIZED = 1019000002 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：USER\_CANCELED = 1019000003  差异内容：USER\_CANCELED = 1019000003 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：STRATEGIES\_EXCEED\_LIMIT = 1019000004  差异内容：STRATEGIES\_EXCEED\_LIMIT = 1019000004 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：STRATEGY\_NAME\_ALREADY\_EXIST = 1019000005  差异内容：STRATEGY\_NAME\_ALREADY\_EXIST = 1019000005 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：NONEXISTENT\_STRATEGY = 1019000006  差异内容：NONEXISTENT\_STRATEGY = 1019000006 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：STRATEGY\_ALREADY\_EXECUTED = 1019000007  差异内容：STRATEGY\_ALREADY\_EXECUTED = 1019000007 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode；  API声明：STRATEGY\_NOT\_STARTED = 1019000008  差异内容：STRATEGY\_NOT\_STARTED = 1019000008 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：enum RestrictionType  差异内容：enum RestrictionType | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：RestrictionType；  API声明：TRUSTLIST\_TYPE = 1  差异内容：TRUSTLIST\_TYPE = 1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：RestrictionType；  API声明：BLOCKLIST\_TYPE = 2  差异内容：BLOCKLIST\_TYPE = 2 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：enum TimeStrategyType  差异内容：enum TimeStrategyType | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategyType；  API声明：START\_END\_TIME\_TYPE = 1  差异内容：START\_END\_TIME\_TYPE = 1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategyType；  API声明：TOTAL\_DURATION\_TYPE = 2  差异内容：TOTAL\_DURATION\_TYPE = 2 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：enum AuthStatus  差异内容：enum AuthStatus | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AuthStatus；  API声明：AUTH\_INIT = -1  差异内容：AUTH\_INIT = -1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AuthStatus；  API声明：AUTH\_GRANTED = 0  差异内容：AUTH\_GRANTED = 0 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AuthStatus；  API声明：AUTH\_DENIED = 1  差异内容：AUTH\_DENIED = 1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：interface AppInfo  差异内容：interface AppInfo | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AppInfo；  API声明：appTokens: string[];  差异内容：appTokens: string[]; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：interface TimeStrategy  差异内容：interface TimeStrategy | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy；  API声明：type: TimeStrategyType;  差异内容：type: TimeStrategyType; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy；  API声明：startTime?: string;  差异内容：startTime?: string; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy；  API声明：endTime?: string;  差异内容：endTime?: string; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy；  API声明：totalDuration?: number;  差异内容：totalDuration?: number; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy；  API声明：repeat?: number[];  差异内容：repeat?: number[]; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：interface GuardStrategy  差异内容：interface GuardStrategy | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy；  API声明：name: string;  差异内容：name: string; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy；  API声明：timeStrategy: TimeStrategy;  差异内容：timeStrategy: TimeStrategy; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy；  API声明：appInfo: AppInfo;  差异内容：appInfo: AppInfo; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy；  API声明：appRestrictionType: RestrictionType;  差异内容：appRestrictionType: RestrictionType; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function requestUserAuth(context: common.UIAbilityContext): Promise<void>;  差异内容：function requestUserAuth(context: common.UIAbilityContext): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function revokeUserAuth(): Promise<void>;  差异内容：function revokeUserAuth(): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function getUserAuthStatus(): Promise<AuthStatus>;  差异内容：function getUserAuthStatus(): Promise<AuthStatus>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function addGuardStrategy(guardStrategy: GuardStrategy): Promise<void>;  差异内容：function addGuardStrategy(guardStrategy: GuardStrategy): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise<void>;  差异内容：function updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function queryGuardStrategies(): Promise<GuardStrategy[]>;  差异内容：function queryGuardStrategies(): Promise<GuardStrategy[]>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function removeGuardStrategy(strategyName: string): Promise<void>;  差异内容：function removeGuardStrategy(strategyName: string): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function startGuardStrategy(strategyName: string): Promise<void>;  差异内容：function startGuardStrategy(strategyName: string): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function stopGuardStrategy(strategyName: string): Promise<void>;  差异内容：function stopGuardStrategy(strategyName: string): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>;  差异内容：function setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService；  API声明：function releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>;  差异内容：function releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class TimeGuardExtensionAbility  差异内容：export default class TimeGuardExtensionAbility | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility；  API声明：context: TimeGuardExtensionContext;  差异内容：context: TimeGuardExtensionContext; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility；  API声明：onStart(strategyName: string): Promise<void>;  差异内容：onStart(strategyName: string): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility；  API声明：onStop(strategyName: string): Promise<void>;  差异内容：onStop(strategyName: string): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility；  API声明：onUserAuthSwitchOn(): Promise<void>;  差异内容：onUserAuthSwitchOn(): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility；  API声明：onUserAuthSwitchOff(): Promise<void>;  差异内容：onUserAuthSwitchOff(): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class TimeGuardExtensionContext  差异内容：export default class TimeGuardExtensionContext | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.utilityApplication.screenTimeGuard.appPicker.d.ts  差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.utilityApplication.screenTimeGuard.guardService.d.ts  差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts  差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext.d.ts  差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.ScreenTimeGuardKit.d.ts  差异内容：ScreenTimeGuardKit | kits/@kit.ScreenTimeGuardKit.d.ts |
