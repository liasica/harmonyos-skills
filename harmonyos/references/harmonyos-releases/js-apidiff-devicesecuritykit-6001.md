---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6001
title: Device Security Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:383424903bc2024bf21b077c4b71fd2da9f97abd74784362a5c7b8911319716f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace dlpAntiPeep  差异内容：declare namespace dlpAntiPeep | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：enum DlpAntiPeepStatus  差异内容：enum DlpAntiPeepStatus | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：DlpAntiPeepStatus；  API声明：PASS = 0  差异内容：PASS = 0 | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：DlpAntiPeepStatus；  API声明：HIDE = 1  差异内容：HIDE = 1 | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：function isDlpAntiPeepSwitchOn(): Promise<boolean>;  差异内容：function isDlpAntiPeepSwitchOn(): Promise<boolean>; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：function on(type: 'dlpAntiPeep', callback: Callback<DlpAntiPeepStatus>): void;  差异内容：function on(type: 'dlpAntiPeep', callback: Callback<DlpAntiPeepStatus>): void; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：function off(type: 'dlpAntiPeep', callback?: Callback<DlpAntiPeepStatus>): void;  差异内容：function off(type: 'dlpAntiPeep', callback?: Callback<DlpAntiPeepStatus>): void; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：function getDlpAntiPeepInfo(): DlpAntiPeepStatus;  差异内容：function getDlpAntiPeepInfo(): DlpAntiPeepStatus; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep；  API声明：function passDlpAntiPeepInfo(): void;  差异内容：function passDlpAntiPeepInfo(): void; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace trustedAuthentication  差异内容：declare namespace trustedAuthentication | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export enum AuthType  差异内容：export enum AuthType | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthType；  API声明：AUTH\_TYPE\_FACE = 2  差异内容：AUTH\_TYPE\_FACE = 2 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthType；  API声明：AUTH\_TYPE\_FINGERPRINT = 4  差异内容：AUTH\_TYPE\_FINGERPRINT = 4 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthType；  API声明：AUTH\_TYPE\_TUI\_PIN = 32  差异内容：AUTH\_TYPE\_TUI\_PIN = 32 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export enum PasswordType  差异内容：export enum PasswordType | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordType；  API声明：PASSWORD\_TYPE\_DIGITAL = 0  差异内容：PASSWORD\_TYPE\_DIGITAL = 0 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordType；  API声明：PASSWORD\_TYPE\_MIXED = 1  差异内容：PASSWORD\_TYPE\_MIXED = 1 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export enum OperateType  差异内容：export enum OperateType | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：OperateType；  API声明：OPERATE\_TYPE\_BIOMETRIC\_AUTH = 1  差异内容：OPERATE\_TYPE\_BIOMETRIC\_AUTH = 1 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：OperateType；  API声明：OPERATE\_TYPE\_CONTENT\_AUTH = 2  差异内容：OPERATE\_TYPE\_CONTENT\_AUTH = 2 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export enum TrustedAuthErrorCode  差异内容：export enum TrustedAuthErrorCode | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NO\_PERMISSION = 1019100001  差异内容：TRUSTED\_AUTH\_ERROR\_NO\_PERMISSION = 1019100001 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_ILLEGAL\_ARGUMENT = 1019100002  差异内容：TRUSTED\_AUTH\_ERROR\_ILLEGAL\_ARGUMENT = 1019100002 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_PWD\_LIMIT\_REACHED = 1019100003  差异内容：TRUSTED\_AUTH\_ERROR\_PWD\_LIMIT\_REACHED = 1019100003 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_PWD\_DELETE\_FAILED = 1019100004  差异内容：TRUSTED\_AUTH\_ERROR\_PWD\_DELETE\_FAILED = 1019100004 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_VERIFY\_FAILED = 1019100005  差异内容：TRUSTED\_AUTH\_ERROR\_VERIFY\_FAILED = 1019100005 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_CHECK\_CONFIRM\_TEXT\_FAILED = 1019100006  差异内容：TRUSTED\_AUTH\_ERROR\_CHECK\_CONFIRM\_TEXT\_FAILED = 1019100006 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_NOT\_SUPPORT\_IMAGE = 1019100007  差异内容：TRUSTED\_AUTH\_ERROR\_NOT\_SUPPORT\_IMAGE = 1019100007 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_USER\_REQ\_CANCEL = 1019100008  差异内容：TRUSTED\_AUTH\_ERROR\_USER\_REQ\_CANCEL = 1019100008 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_EXPORT\_DATA\_FAILED = 1019100009  差异内容：TRUSTED\_AUTH\_ERROR\_EXPORT\_DATA\_FAILED = 1019100009 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_IMPORT\_DATA\_FAILED = 1019100010  差异内容：TRUSTED\_AUTH\_ERROR\_IMPORT\_DATA\_FAILED = 1019100010 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_INVALID\_CONTENT = 1019100011  差异内容：TRUSTED\_AUTH\_ERROR\_INVALID\_CONTENT = 1019100011 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_INVALID\_AUTH\_ID = 1019100012  差异内容：TRUSTED\_AUTH\_ERROR\_INVALID\_AUTH\_ID = 1019100012 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_SET\_PWD\_FAILED = 1019100013  差异内容：TRUSTED\_AUTH\_ERROR\_SET\_PWD\_FAILED = 1019100013 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_MODIFY\_PWD\_FAILED = 1019100014  差异内容：TRUSTED\_AUTH\_ERROR\_MODIFY\_PWD\_FAILED = 1019100014 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_ERROR\_BIO\_RESIGN\_FAILED = 1019100015  差异内容：TRUSTED\_AUTH\_ERROR\_BIO\_RESIGN\_FAILED = 1019100015 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode；  API声明：TRUSTED\_AUTH\_FEATURE\_INITIALIZATION\_FAILED = 1019100016  差异内容：TRUSTED\_AUTH\_FEATURE\_INITIALIZATION\_FAILED = 1019100016 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export interface PasswordInfo  差异内容：export interface PasswordInfo | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo；  API声明：pwdType: PasswordType;  差异内容：pwdType: PasswordType; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo；  API声明：pwdMaxLength: number;  差异内容：pwdMaxLength: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo；  API声明：pwdMinLength: number;  差异内容：pwdMinLength: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo；  API声明：maxAuthFailCount: number;  差异内容：maxAuthFailCount: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export interface AuthReqParams  差异内容：export interface AuthReqParams | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthReqParams；  API声明：reqType: AuthType;  差异内容：reqType: AuthType; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthReqParams；  API声明：authContent: Array<string>;  差异内容：authContent: Array<string>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export interface TUILable  差异内容：export interface TUILable | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TUILable；  API声明：image: ArrayBuffer;  差异内容：image: ArrayBuffer; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TUILable；  API声明：title: string;  差异内容：title: string; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export interface AuthToken  差异内容：export interface AuthToken | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthToken；  API声明：authToken: Uint8Array;  差异内容：authToken: Uint8Array; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export interface AuthInfo  差异内容：export interface AuthInfo | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthInfo；  API声明：authToken: Uint8Array;  差异内容：authToken: Uint8Array; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthInfo；  API声明：authID: bigint;  差异内容：authID: bigint; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：export interface TextCheckResult  差异内容：export interface TextCheckResult | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TextCheckResult；  API声明：result: number;  差异内容：result: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TextCheckResult；  API声明：lastIndex: number;  差异内容：lastIndex: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>;  差异内容：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>;  差异内容：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>;  差异内容：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>;  差异内容：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function importData(data: ArrayBuffer, authID: bigint): Promise<void>;  差异内容：function importData(data: ArrayBuffer, authID: bigint): Promise<void>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>;  差异内容：function exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication；  API声明：function checkConfirmUITextFormat(text: string): Promise<TextCheckResult>;  差异内容：function checkConfirmUITextFormat(text: string): Promise<TextCheckResult>; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：safetyDetect；  API声明：function checkSysIntegrityEnhanced(req: SysIntegrityRequest): Promise<SysIntegrityResponse>;  差异内容：function checkSysIntegrityEnhanced(req: SysIntegrityRequest): Promise<SysIntegrityResponse>; | api/@hms.security.safetyDetect.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.dlpAntiPeep.d.ts  差异内容：DeviceSecurityKit | api/@hms.security.dlpAntiPeep.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.trustedAuthentication.d.ts  差异内容：DeviceSecurityKit | api/@hms.security.trustedAuthentication.d.ts |
