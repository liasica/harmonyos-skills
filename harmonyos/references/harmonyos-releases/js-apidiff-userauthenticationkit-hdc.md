---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-hdc
title: User Authentication Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > User Authentication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:051c3ea1f991d46779e70dc498c1d019dad0b5259aff279eaf061e446d87c2c3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：Authenticator；  API声明：execute(type: AuthType, level: SecureLevel): Promise<number>;  差异内容：NA | 类名：Authenticator；  API声明：execute(type: AuthType, level: SecureLevel): Promise<number>;  差异内容：8 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthResult；  API声明：token?: Uint8Array;  差异内容：NA | 类名：AuthResult；  API声明：token?: Uint8Array;  差异内容：9 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthResult；  API声明：remainTimes?: number;  差异内容：NA | 类名：AuthResult；  API声明：remainTimes?: number;  差异内容：9 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthResult；  API声明：freezingTime?: number;  差异内容：NA | 类名：AuthResult；  API声明：freezingTime?: number;  差异内容：9 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明： enum FaceTips  差异内容：NA | 类名：userAuth；  API声明： enum FaceTips  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_BRIGHT = 1  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_BRIGHT = 1  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_DARK = 2  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_DARK = 2  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_CLOSE = 3  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_CLOSE = 3  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_FAR = 4  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_FAR = 4  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_HIGH = 5  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_HIGH = 5  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_LOW = 6  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_LOW = 6  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_RIGHT = 7  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_RIGHT = 7  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_LEFT = 8  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_LEFT = 8  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_MUCH\_MOTION = 9  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_TOO\_MUCH\_MOTION = 9  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_POOR\_GAZE = 10  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_POOR\_GAZE = 10  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_NOT\_DETECTED = 11  差异内容：NA | 类名：FaceTips；  API声明：FACE\_AUTH\_TIP\_NOT\_DETECTED = 11  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明： enum FingerprintTips  差异内容：NA | 类名：userAuth；  API声明： enum FingerprintTips  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_GOOD = 0  差异内容：NA | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_GOOD = 0  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_DIRTY = 1  差异内容：NA | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_DIRTY = 1  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_INSUFFICIENT = 2  差异内容：NA | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_INSUFFICIENT = 2  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_PARTIAL = 3  差异内容：NA | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_PARTIAL = 3  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_TOO\_FAST = 4  差异内容：NA | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_TOO\_FAST = 4  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_TOO\_SLOW = 5  差异内容：NA | 类名：FingerprintTips；  API声明：FINGERPRINT\_AUTH\_TIP\_TOO\_SLOW = 5  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明：type AuthEventKey = "result" | "tip";  差异内容：NA | 类名：userAuth；  API声明：type AuthEventKey = 'result' | 'tip';  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明：type EventInfo = AuthResultInfo | TipInfo;  差异内容：NA | 类名：userAuth；  API声明：type EventInfo = AuthResultInfo | TipInfo;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明： interface AuthEvent  差异内容：NA | 类名：userAuth；  API声明： interface AuthEvent  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthEvent；  API声明：callback(result: EventInfo): void;  差异内容：NA | 类名：AuthEvent；  API声明：callback(result: EventInfo): void;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明： interface AuthResultInfo  差异内容：NA | 类名：userAuth；  API声明： interface AuthResultInfo  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthResultInfo；  API声明：result: number;  差异内容：NA | 类名：AuthResultInfo；  API声明：result: number;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthResultInfo；  API声明：token?: Uint8Array;  差异内容：NA | 类名：AuthResultInfo；  API声明：token?: Uint8Array;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthResultInfo；  API声明：remainAttempts?: number;  差异内容：NA | 类名：AuthResultInfo；  API声明：remainAttempts?: number;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthResultInfo；  API声明：lockoutDuration?: number;  差异内容：NA | 类名：AuthResultInfo；  API声明：lockoutDuration?: number;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明： interface TipInfo  差异内容：NA | 类名：userAuth；  API声明： interface TipInfo  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：TipInfo；  API声明：module: number;  差异内容：NA | 类名：TipInfo；  API声明：module: number;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：TipInfo；  API声明：tip: number;  差异内容：NA | 类名：TipInfo；  API声明：tip: number;  差异内容：11 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明： interface AuthInstance  差异内容：NA | 类名：userAuth；  API声明： interface AuthInstance  差异内容：10 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthInstance；  API声明：on: (name: AuthEventKey, callback: AuthEvent) => void;  差异内容：NA | 类名：AuthInstance；  API声明：on: (name: AuthEventKey, callback: AuthEvent) => void;  差异内容：10 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthInstance；  API声明：off: (name: AuthEventKey) => void;  差异内容：NA | 类名：AuthInstance；  API声明：off: (name: AuthEventKey) => void;  差异内容：10 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthInstance；  API声明：start: () => void;  差异内容：NA | 类名：AuthInstance；  API声明：start: () => void;  差异内容：10 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：AuthInstance；  API声明：cancel: () => void;  差异内容：NA | 类名：AuthInstance；  API声明：cancel: () => void;  差异内容：10 | api/@ohos.userIAM.userAuth.d.ts |
| API废弃版本变更 | 类名：userAuth；  API声明：function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance;  差异内容：NA | 类名：userAuth；  API声明：function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance;  差异内容：10 | api/@ohos.userIAM.userAuth.d.ts |
| 权限变更 | 类名：Authenticator；  API声明：execute(type: AuthType, level: SecureLevel): Promise<number>;  差异内容：NA | 类名：Authenticator；  API声明：execute(type: AuthType, level: SecureLevel): Promise<number>;  差异内容：ohos.permission.ACCESS\_BIOMETRIC | api/@ohos.userIAM.userAuth.d.ts |
| 自定义类型变更 | 类名：userAuth；  API声明：type AuthType = "ALL" | "FACE\_ONLY";  差异内容："ALL" | "FACE\_ONLY" | 类名：userAuth；  API声明：type AuthType = 'ALL' | 'FACE\_ONLY';  差异内容：'ALL' | 'FACE\_ONLY' | api/@ohos.userIAM.userAuth.d.ts |
| 自定义类型变更 | 类名：userAuth；  API声明：type SecureLevel = "S1" | "S2" | "S3" | "S4";  差异内容："S1" | "S2" | "S3" | "S4" | 类名：userAuth；  API声明：type SecureLevel = 'S1' | 'S2' | 'S3' | 'S4';  差异内容：'S1' | 'S2' | 'S3' | 'S4' | api/@ohos.userIAM.userAuth.d.ts |
| 自定义类型变更 | 类名：userAuth；  API声明：type AuthEventKey = "result" | "tip";  差异内容："result" | "tip" | 类名：userAuth；  API声明：type AuthEventKey = 'result' | 'tip';  差异内容：'result' | 'tip' | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：const MAX\_ALLOWABLE\_REUSE\_DURATION: 300000;  差异内容：const MAX\_ALLOWABLE\_REUSE\_DURATION: 300000; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthType；  API声明：PIN = 1  差异内容：PIN = 1 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： interface EnrolledState  差异内容： interface EnrolledState | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：EnrolledState；  API声明：credentialDigest: number;  差异内容：credentialDigest: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：EnrolledState；  API声明：credentialCount: number;  差异内容：credentialCount: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：function getEnrolledState(authType: UserAuthType): EnrolledState;  差异内容：function getEnrolledState(authType: UserAuthType): EnrolledState; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： enum ReuseMode  差异内容： enum ReuseMode | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：ReuseMode；  API声明：AUTH\_TYPE\_RELEVANT = 1  差异内容：AUTH\_TYPE\_RELEVANT = 1 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：ReuseMode；  API声明：AUTH\_TYPE\_IRRELEVANT = 2  差异内容：AUTH\_TYPE\_IRRELEVANT = 2 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： interface ReuseUnlockResult  差异内容： interface ReuseUnlockResult | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：ReuseUnlockResult；  API声明：reuseMode: ReuseMode;  差异内容：reuseMode: ReuseMode; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：ReuseUnlockResult；  API声明：reuseDuration: number;  差异内容：reuseDuration: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： interface AuthParam  差异内容： interface AuthParam | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthParam；  API声明：challenge: Uint8Array;  差异内容：challenge: Uint8Array; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthParam；  API声明：authType: UserAuthType[];  差异内容：authType: UserAuthType[]; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthParam；  API声明：authTrustLevel: AuthTrustLevel;  差异内容：authTrustLevel: AuthTrustLevel; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthParam；  API声明：reuseUnlockResult?: ReuseUnlockResult;  差异内容：reuseUnlockResult?: ReuseUnlockResult; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： interface WidgetParam  差异内容： interface WidgetParam | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：WidgetParam；  API声明：title: string;  差异内容：title: string; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：WidgetParam；  API声明：navigationButtonText?: string;  差异内容：navigationButtonText?: string; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： interface UserAuthResult  差异内容： interface UserAuthResult | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：result: number;  差异内容：result: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：token?: Uint8Array;  差异内容：token?: Uint8Array; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：authType?: UserAuthType;  差异内容：authType?: UserAuthType; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：enrolledState?: EnrolledState;  差异内容：enrolledState?: EnrolledState; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： interface IAuthCallback  差异内容： interface IAuthCallback | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：IAuthCallback；  API声明：onResult(result: UserAuthResult): void;  差异内容：onResult(result: UserAuthResult): void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明： interface UserAuthInstance  差异内容： interface UserAuthInstance | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthInstance；  API声明：on(type: 'result', callback: IAuthCallback): void;  差异内容：on(type: 'result', callback: IAuthCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthInstance；  API声明：off(type: 'result', callback?: IAuthCallback): void;  差异内容：off(type: 'result', callback?: IAuthCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthInstance；  API声明：start(): void;  差异内容：start(): void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthInstance；  API声明：cancel(): void;  差异内容：cancel(): void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth；  API声明：function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance;  差异内容：function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResultCode；  API声明：CANCELED\_FROM\_WIDGET = 12500011  差异内容：CANCELED\_FROM\_WIDGET = 12500011 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：global；  API声明： export default struct UserAuthIcon  差异内容： export default struct UserAuthIcon | api/@ohos.userIAM.userAuthIcon.d.ets |
| 新增API | NA | 类名：UserAuthIcon；  API声明：authParam: userAuth.AuthParam;  差异内容：authParam: userAuth.AuthParam; | api/@ohos.userIAM.userAuthIcon.d.ets |
| 新增API | NA | 类名：UserAuthIcon；  API声明：widgetParam: userAuth.WidgetParam;  差异内容：widgetParam: userAuth.WidgetParam; | api/@ohos.userIAM.userAuthIcon.d.ets |
| 新增API | NA | 类名：UserAuthIcon；  API声明：iconHeight?: Dimension;  差异内容：iconHeight?: Dimension; | api/@ohos.userIAM.userAuthIcon.d.ets |
| 新增API | NA | 类名：UserAuthIcon；  API声明：iconColor?: ResourceColor;  差异内容：iconColor?: ResourceColor; | api/@ohos.userIAM.userAuthIcon.d.ets |
| 新增API | NA | 类名：UserAuthIcon；  API声明：onAuthResult: (result: userAuth.UserAuthResult) => void;  差异内容：onAuthResult: (result: userAuth.UserAuthResult) => void; | api/@ohos.userIAM.userAuthIcon.d.ets |
| 新增API | NA | 类名：UserAuthIcon；  API声明：onIconClick?: () => void;  差异内容：onIconClick?: () => void; | api/@ohos.userIAM.userAuthIcon.d.ets |
| 起始版本有变化 | 类名：AuthInstance；  API声明：on: (name: AuthEventKey, callback: AuthEvent) => void;  差异内容：since | 类名：AuthInstance；  API声明：on: (name: AuthEventKey, callback: AuthEvent) => void;  差异内容：9 | api/@ohos.userIAM.userAuth.d.ts |
| 起始版本有变化 | 类名：AuthInstance；  API声明：off: (name: AuthEventKey) => void;  差异内容：since | 类名：AuthInstance；  API声明：off: (name: AuthEventKey) => void;  差异内容：9 | api/@ohos.userIAM.userAuth.d.ts |
| 起始版本有变化 | 类名：AuthInstance；  API声明：start: () => void;  差异内容：since | 类名：AuthInstance；  API声明：start: () => void;  差异内容：9 | api/@ohos.userIAM.userAuth.d.ts |
| 起始版本有变化 | 类名：AuthInstance；  API声明：cancel: () => void;  差异内容：since | 类名：AuthInstance；  API声明：cancel: () => void;  差异内容：9 | api/@ohos.userIAM.userAuth.d.ts |
