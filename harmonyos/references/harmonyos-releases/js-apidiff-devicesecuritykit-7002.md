---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-7002
title: Device Security Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:205859317aef3b8041a7c7e3919e63fa346ea7d45d3f8f9bc99f6aaad5c47e4b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>;  差异内容：801 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication；  API声明：function getSecurityLevel(authID?: bigint): Promise<SecurityLevel>;  差异内容：NA | 类名：trustedAuthentication；  API声明：function getSecurityLevel(authID?: bigint): Promise<SecurityLevel>;  差异内容：1019100012 | api/@hms.security.trustedAuthentication.d.ts |
| 删除错误码 | 类名：riskControlEngine；  API声明：function importRiskFactors(data: ImportData): Promise<void>;  差异内容：1010800001 | 类名：riskControlEngine；  API声明：function importRiskFactors(data: ImportData): Promise<void>;  差异内容：NA | api/@hms.security.riskControlEngine.d.ts |
| 删除错误码 | 类名：riskControlEngine；  API声明：function getRiskControlResult(req: RiskControlDetectionRequest): Promise<RiskControlDetectionResponse>;  差异内容：1010800001 | 类名：riskControlEngine；  API声明：function getRiskControlResult(req: RiskControlDetectionRequest): Promise<RiskControlDetectionResponse>;  差异内容：NA | api/@hms.security.riskControlEngine.d.ts |
| 错误码变更兼容 | 类名：safetyDetect；  API声明：function queryRiskFactors(req: RiskFactorRequest): Promise<RiskFactorResponse>;  差异内容：1010800001,1010800004,1010800005,1010800006,1010800007,801 | 类名：safetyDetect；  API声明：function queryRiskFactors(req: RiskFactorRequest): Promise<RiskFactorResponse>;  差异内容：1010800004,1010800005,1010800006,1010800007,1010800011,801 | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace contentTrustVerify  差异内容：declare namespace contentTrustVerify | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：export enum ImageFormat  差异内容：export enum ImageFormat | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageFormat；  API声明：IMAGE\_TYPE\_JPEG = 0  差异内容：IMAGE\_TYPE\_JPEG = 0 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageFormat；  API声明：IMAGE\_TYPE\_DNG = 1  差异内容：IMAGE\_TYPE\_DNG = 1 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageFormat；  API声明：IMAGE\_TYPE\_HEIF = 2  差异内容：IMAGE\_TYPE\_HEIF = 2 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：export enum ImageBufferFormat  差异内容：export enum ImageBufferFormat | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageBufferFormat；  API声明：IMAGE\_DATA\_TYPE\_DATAFLOW = 0  差异内容：IMAGE\_DATA\_TYPE\_DATAFLOW = 0 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageBufferFormat；  API声明：IMAGE\_DATA\_TYPE\_URL = 1  差异内容：IMAGE\_DATA\_TYPE\_URL = 1 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：export enum BufferType  差异内容：export enum BufferType | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：BufferType；  API声明：BUFFER\_TYPE\_DATA = 0  差异内容：BUFFER\_TYPE\_DATA = 0 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：BufferType；  API声明：BUFFER\_TYPE\_URL = 1  差异内容：BUFFER\_TYPE\_URL = 1 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：export enum ContentTrustCredentialsErrorCode  差异内容：export enum ContentTrustCredentialsErrorCode | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_BAD\_IMAGE\_TYPE = 1027200001  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_BAD\_IMAGE\_TYPE = 1027200001 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_OUT\_OF\_STORE = 1027200002  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_OUT\_OF\_STORE = 1027200002 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_WRONG\_SIGN\_CERT\_PARAM = 1027200003  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_WRONG\_SIGN\_CERT\_PARAM = 1027200003 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_CHECK\_IMAGE\_HASH\_FAILED = 1027200004  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_CHECK\_IMAGE\_HASH\_FAILED = 1027200004 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_SIGN\_FAILED = 1027200005  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_SIGN\_FAILED = 1027200005 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_VERIFY\_FAILED = 1027200006  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_VERIFY\_FAILED = 1027200006 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_NO\_SIGN\_ASSERTION = 1027200007  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_NO\_SIGN\_ASSERTION = 1027200007 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_NO\_SIGN\_MANIFEST = 1027200008  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_NO\_SIGN\_MANIFEST = 1027200008 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_WRONG\_CERT\_CHAINS = 1027200009  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_WRONG\_CERT\_CHAINS = 1027200009 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_PLATFORM\_NOT\_SUPPORTED = 1027200010  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_PLATFORM\_NOT\_SUPPORTED = 1027200010 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_BAD\_METADATA = 1027200011  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_BAD\_METADATA = 1027200011 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_CLAIM\_INVALID = 1027200012  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_CLAIM\_INVALID = 1027200012 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_FILE\_OPERATION\_FAILED = 1027200013  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_FILE\_OPERATION\_FAILED = 1027200013 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode；  API声明：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_ILLEGAL\_ARGUMENT = 1027200014  差异内容：CONTENT\_TRUST\_CREDENTIAL\_ERROR\_ILLEGAL\_ARGUMENT = 1027200014 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：export interface ImageAuthData  差异内容：export interface ImageAuthData | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData；  API声明：buffer: Uint8Array;  差异内容：buffer: Uint8Array; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData；  API声明：imageSize: number;  差异内容：imageSize: number; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData；  API声明：bufferType: BufferType;  差异内容：bufferType: BufferType; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData；  API声明：imageFormat: ImageFormat;  差异内容：imageFormat: ImageFormat; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：function hasImageSignature(data: ImageAuthData): Promise<boolean>;  差异内容：function hasImageSignature(data: ImageAuthData): Promise<boolean>; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：function verifyImageSignature(data: ImageAuthData): Promise<Uint8Array>;  差异内容：function verifyImageSignature(data: ImageAuthData): Promise<Uint8Array>; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify；  API声明：function parseImageMetadata(manifests: Uint8Array): Promise<string>;  差异内容：function parseImageMetadata(manifests: Uint8Array): Promise<string>; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function newAuthClient(callback: Callback<AuditEvent>, configuration: AuthClientConfiguration): AuthClient;  差异内容：function newAuthClient(callback: Callback<AuditEvent>, configuration: AuthClientConfiguration): AuthClient; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：BLUETOOTH\_INTERCEPTED = 0x03000200  差异内容：BLUETOOTH\_INTERCEPTED = 0x03000200 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DISC\_BURNING = 0x0F000004  差异内容：DISC\_BURNING = 0x0F000004 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：MEDIA\_FILE\_ACCESS = 0x0F000005  差异内容：MEDIA\_FILE\_ACCESS = 0x0F000005 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：ACCOUNT\_MANAGEMENT = 0x10000103  差异内容：ACCOUNT\_MANAGEMENT = 0x10000103 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DEVICE\_POWER\_ON = 0x16000001  差异内容：DEVICE\_POWER\_ON = 0x16000001 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：DEVICE\_POWER\_OFF = 0x16000002  差异内容：DEVICE\_POWER\_OFF = 0x16000002 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：AUDIO\_INTERFACE\_ACCESS = 0x1A000001  差异内容：AUDIO\_INTERFACE\_ACCESS = 0x1A000001 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：VIDEO\_INTERFACE\_ACCESS = 0x1A000002  差异内容：VIDEO\_INTERFACE\_ACCESS = 0x1A000002 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent；  API声明：SERIAL\_PORT\_INTERCEPTED = 0x30000101  差异内容：SERIAL\_PORT\_INTERCEPTED = 0x30000101 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：PROCESS\_EXEC = 0x1C801400  差异内容：PROCESS\_EXEC = 0x1C801400 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent；  API声明：FILE\_READ\_END = 0x1C801106  差异内容：FILE\_READ\_END = 0x1C801106 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：interface AuthClientConfiguration  差异内容：interface AuthClientConfiguration | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthClientConfiguration；  API声明：timeoutAuthResult: AuthResult;  差异内容：timeoutAuthResult: AuthResult; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function acquireAllAuthClientsInfo(): string;  差异内容：function acquireAllAuthClientsInfo(): string; | api/@hms.security.securityAudit.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.MediaAuthVerify.d.ts  差异内容：DeviceSecurityKit | api/@hms.security.MediaAuthVerify.d.ts |
