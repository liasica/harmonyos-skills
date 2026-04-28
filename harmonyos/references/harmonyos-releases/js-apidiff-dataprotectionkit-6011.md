---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataprotectionkit-6011
title: Data Protection Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Data Protection Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:58+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0bb08f2ccf2ae99a0779cd98423aa89aa9525e31dccc9eadbc973f66756ce2e2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace identifySensitiveContent  差异内容：declare namespace identifySensitiveContent | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：identifySensitiveContent；  API声明：export interface Policy  差异内容：export interface Policy | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：Policy；  API声明：sensitiveLabel: string;  差异内容：sensitiveLabel: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：Policy；  API声明：keywords: Array<string>;  差异内容：keywords: Array<string>; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：Policy；  API声明：regex: string;  差异内容：regex: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：identifySensitiveContent；  API声明：export interface MatchResult  差异内容：export interface MatchResult | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：MatchResult；  API声明：readonly sensitiveLabel: string;  差异内容：readonly sensitiveLabel: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：MatchResult；  API声明：readonly matchContent: string;  差异内容：readonly matchContent: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：MatchResult；  API声明：readonly matchNumber: number;  差异内容：readonly matchNumber: number; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：identifySensitiveContent；  API声明：function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>;  差异内容：function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export enum AccountType  差异内容：export enum AccountType | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AccountType；  API声明：CLOUD\_ACCOUNT = 1  差异内容：CLOUD\_ACCOUNT = 1 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AccountType；  API声明：DOMAIN\_ACCOUNT = 2  差异内容：DOMAIN\_ACCOUNT = 2 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AccountType；  API声明：ENTERPRISE\_ACCOUNT = 4  差异内容：ENTERPRISE\_ACCOUNT = 4 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export interface AuthUser  差异内容：export interface AuthUser | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser；  API声明：authAccount: string;  差异内容：authAccount: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser；  API声明：authAccountType: AccountType;  差异内容：authAccountType: AccountType; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser；  API声明：dlpFileAccess: DLPFileAccess;  差异内容：dlpFileAccess: DLPFileAccess; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser；  API声明：permExpiryTime: number;  差异内容：permExpiryTime: number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export interface DLPProperty  差异内容：export interface DLPProperty | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：ownerAccount: string;  差异内容：ownerAccount: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：ownerAccountID: string;  差异内容：ownerAccountID: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：ownerAccountType: AccountType;  差异内容：ownerAccountType: AccountType; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：authUserList?: Array<AuthUser>;  差异内容：authUserList?: Array<AuthUser>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：contactAccount: string;  差异内容：contactAccount: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：offlineAccess: boolean;  差异内容：offlineAccess: boolean; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：everyoneAccessList?: Array<DLPFileAccess>;  差异内容：everyoneAccessList?: Array<DLPFileAccess>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：expireTime?: number;  差异内容：expireTime?: number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：actionUponExpiry?: ActionType;  差异内容：actionUponExpiry?: ActionType; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：fileId?: string;  差异内容：fileId?: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty；  API声明：allowedOpenCount?: number;  差异内容：allowedOpenCount?: number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export enum ActionType  差异内容：export enum ActionType | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：ActionType；  API声明：NOT\_OPEN = 0  差异内容：NOT\_OPEN = 0 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：ActionType；  API声明：OPEN = 1  差异内容：OPEN = 1 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export interface CustomProperty  差异内容：export interface CustomProperty | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：CustomProperty；  API声明：enterprise: string;  差异内容：enterprise: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>;  差异内容：function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function queryDlpPolicy(dlpFd: number): Promise<string>;  差异内容：function queryDlpPolicy(dlpFd: number): Promise<string>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>;  差异内容：function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export interface EnterprisePolicy  差异内容：export interface EnterprisePolicy | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：EnterprisePolicy；  API声明：policyString: string;  差异内容：policyString: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function setEnterprisePolicy(policy: EnterprisePolicy): void;  差异内容：function setEnterprisePolicy(policy: EnterprisePolicy): void; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export interface DlpConnPlugin  差异内容：export interface DlpConnPlugin | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpConnPlugin；  API声明：connectServer(requestId: string, requestData: string, callback: Callback<string>): void;  差异内容：connectServer(requestId: string, requestData: string, callback: Callback<string>): void; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export class DlpConnManager  差异内容：export class DlpConnManager | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpConnManager；  API声明：static registerPlugin(plugin: DlpConnPlugin): number;  差异内容：static registerPlugin(plugin: DlpConnPlugin): number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpConnManager；  API声明：static unregisterPlugin(): void;  差异内容：static unregisterPlugin(): void; | api/@ohos.dlpPermission.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.security.identifySensitiveContent.d.ts  差异内容：DataProtectionKit | api/@ohos.security.identifySensitiveContent.d.ts |
