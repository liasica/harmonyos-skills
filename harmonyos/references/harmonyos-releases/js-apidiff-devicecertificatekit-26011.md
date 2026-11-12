---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-26011
title: Device Certificate Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:308e22352bf0453710649ffc606d8bb4fb1499ab4b9426f5abca624369905f3a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare class UkeyAuthExtensionAbility  差异内容：declare class UkeyAuthExtensionAbility | api/@ohos.security.UkeyAuthExtensionAbility.d.ts |
| 新增API | NA | 类名：UkeyAuthExtensionAbility；  API声明：context: UkeyAuthExtensionContext;  差异内容：context: UkeyAuthExtensionContext; | api/@ohos.security.UkeyAuthExtensionAbility.d.ts |
| 新增API | NA | 类名：UkeyAuthExtensionAbility；  API声明：onCreate(launchParam: AbilityConstant.LaunchParam): void;  差异内容：onCreate(launchParam: AbilityConstant.LaunchParam): void; | api/@ohos.security.UkeyAuthExtensionAbility.d.ts |
| 新增API | NA | 类名：UkeyAuthExtensionAbility；  API声明：onSessionCreate(want: Want, session: UIExtensionContentSession): void;  差异内容：onSessionCreate(want: Want, session: UIExtensionContentSession): void; | api/@ohos.security.UkeyAuthExtensionAbility.d.ts |
| 新增API | NA | 类名：UkeyAuthExtensionAbility；  API声明：onSessionDestroy(session: UIExtensionContentSession): void;  差异内容：onSessionDestroy(session: UIExtensionContentSession): void; | api/@ohos.security.UkeyAuthExtensionAbility.d.ts |
| 新增API | NA | 类名：UkeyAuthExtensionAbility；  API声明：onDestroy(): void | Promise<void>;  差异内容：onDestroy(): void | Promise<void>; | api/@ohos.security.UkeyAuthExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class UkeyAuthExtensionContext  差异内容：declare class UkeyAuthExtensionContext | api/@ohos.security.UkeyAuthExtensionContext.d.ts |
| 新增API | NA | 类名：UkeyAuthExtensionContext；  API声明：terminateSelf(): Promise<void>;  差异内容：terminateSelf(): Promise<void>; | api/@ohos.security.UkeyAuthExtensionContext.d.ts |
| 新增API | NA | 类名：UkeyAuthExtensionContext；  API声明：terminateSelfWithResult(parameter: AbilityResult): Promise<void>;  差异内容：terminateSelfWithResult(parameter: AbilityResult): Promise<void>; | api/@ohos.security.UkeyAuthExtensionContext.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode；  API声明：ERROR\_OPERATION\_TIMEOUT = 29700009  差异内容：ERROR\_OPERATION\_TIMEOUT = 29700009 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode；  API声明：ERROR\_NOT\_CONCURRENT\_SUPPORT = 29700010  差异内容：ERROR\_NOT\_CONCURRENT\_SUPPORT = 29700010 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：UkeyAuthRequest；  API声明：customData?: Uint8Array;  差异内容：customData?: Uint8Array; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：UkeyAuthRequest；  API声明：timeoutDuration?: number;  差异内容：timeoutDuration?: number; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：function openAuthDialogForUkeyProvider(dialogInfo: UkeyAuthDialogInfo, ukeyAuthRequest: UkeyAuthRequest): Promise<void>;  差异内容：function openAuthDialogForUkeyProvider(dialogInfo: UkeyAuthDialogInfo, ukeyAuthRequest: UkeyAuthRequest): Promise<void>; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：export enum AbilityType  差异内容：export enum AbilityType | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：AbilityType；  API声明：UKEY\_AUTH\_EXTENSION\_ABILITY = 1  差异内容：UKEY\_AUTH\_EXTENSION\_ABILITY = 1 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：export interface UkeyAuthDialogInfo  差异内容：export interface UkeyAuthDialogInfo | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：UkeyAuthDialogInfo；  API声明：abilityType: AbilityType;  差异内容：abilityType: AbilityType; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：UkeyAuthDialogInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.security.certManagerDialog.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.security.UkeyAuthExtensionAbility.d.ts  差异内容：DeviceCertificateKit | api/@ohos.security.UkeyAuthExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.security.UkeyAuthExtensionContext.d.ts  差异内容：DeviceCertificateKit | api/@ohos.security.UkeyAuthExtensionContext.d.ts |
