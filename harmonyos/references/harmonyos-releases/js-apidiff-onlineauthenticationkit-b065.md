---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-onlineauthenticationkit-b065
title: Online Authentication Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Online Authentication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9be5844d78fae0df43953249e62d2401b2e2d782b53453ec01e9297f2b4393cb
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace soter  差异内容： declare namespace soter | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明： export enum KeyType  差异内容： export enum KeyType | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：KeyType；  API声明：ECC\_P256 = 0  差异内容：ECC\_P256 = 0 | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明： class SignedResult  差异内容： class SignedResult | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：SignedResult；  API声明：message: Uint8Array;  差异内容：message: Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：SignedResult；  API声明：signature: Uint8Array;  差异内容：signature: Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：SignedResult；  API声明：saltLength: number;  差异内容：saltLength: number; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function generateAppSecureKeySync(keyType: KeyType): Uint8Array;  差异内容：function generateAppSecureKeySync(keyType: KeyType): Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function generateAppSecureKey(keyType: KeyType): Promise<Uint8Array>;  差异内容：function generateAppSecureKey(keyType: KeyType): Promise<Uint8Array>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function getAppSecureKeySync(keyType: KeyType): Uint8Array;  差异内容：function getAppSecureKeySync(keyType: KeyType): Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function getAppSecureKey(keyType: KeyType): Promise<Uint8Array>;  差异内容：function getAppSecureKey(keyType: KeyType): Promise<Uint8Array>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function hasAppSecureKeySync(keyType: KeyType): boolean;  差异内容：function hasAppSecureKeySync(keyType: KeyType): boolean; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function hasAppSecureKey(keyType: KeyType): Promise<boolean>;  差异内容：function hasAppSecureKey(keyType: KeyType): Promise<boolean>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function generateAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult;  差异内容：function generateAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function generateAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>;  差异内容：function generateAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function getAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult;  差异内容：function getAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function getAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>;  差异内容：function getAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function hasAuthKeySync(keyAlias: string, keyType: KeyType): boolean;  差异内容：function hasAuthKeySync(keyAlias: string, keyType: KeyType): boolean; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function hasAuthKey(keyAlias: string, keyType: KeyType): Promise<boolean>;  差异内容：function hasAuthKey(keyAlias: string, keyType: KeyType): Promise<boolean>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function generateChallengeSync(keyAlias: string): Uint8Array;  差异内容：function generateChallengeSync(keyAlias: string): Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function generateChallenge(keyAlias: string): Promise<Uint8Array>;  差异内容：function generateChallenge(keyAlias: string): Promise<Uint8Array>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function signWithAuthKeySync(keyAlias: string, authToken: Uint8Array, info: string): SignedResult;  差异内容：function signWithAuthKeySync(keyAlias: string, authToken: Uint8Array, info: string): SignedResult; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function signWithAuthKey(keyAlias: string, authToken: Uint8Array, info: string): Promise<SignedResult>;  差异内容：function signWithAuthKey(keyAlias: string, authToken: Uint8Array, info: string): Promise<SignedResult>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function deleteAuthKeySync(keyAlias: string): void;  差异内容：function deleteAuthKeySync(keyAlias: string): void; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function deleteAuthKey(keyAlias: string): Promise<void>;  差异内容：function deleteAuthKey(keyAlias: string): Promise<void>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function deleteAppSecureKeySync(): void;  差异内容：function deleteAppSecureKeySync(): void; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function deleteAppSecureKey(): Promise<void>;  差异内容：function deleteAppSecureKey(): Promise<void>; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function getVersionSync(): string;  差异内容：function getVersionSync(): string; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter；  API声明：function getVersion(): Promise<string>;  差异内容：function getVersion(): Promise<string>; | api/@hms.security.soter.d.ts |
