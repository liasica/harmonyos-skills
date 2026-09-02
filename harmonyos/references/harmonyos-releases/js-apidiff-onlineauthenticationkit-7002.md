---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-onlineauthenticationkit-7002
title: Online Authentication Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Online Authentication Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e78f07988448ef3827e41385913b67a80777e9df10dcda7fbe9cad2215186905
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：did；  API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise<ImportDigitalCredentialResponse>;  差异内容：NA | 类名：did；  API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise<ImportDigitalCredentialResponse>;  差异内容：201 | api/@hms.security.did.d.ts |
| 新增错误码 | 类名：did；  API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<void>;  差异内容：NA | 类名：did；  API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<void>;  差异内容：201 | api/@hms.security.did.d.ts |
| 新增错误码 | 类名：fido；  API声明：function processUAFOperation(context: common.Context, uafRequest: UAFMessage, channelBindings?: ChannelBinding): Promise<UAFMessage>;  差异内容：NA | 类名：fido；  API声明：function processUAFOperation(context: common.Context, uafRequest: UAFMessage, channelBindings?: ChannelBinding): Promise<UAFMessage>;  差异内容：1005900018 | api/@hms.security.fido.d.ts |
| 新增错误码 | 类名：fido2；  API声明：function getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>;  差异内容：NA | 类名：fido2；  API声明：function getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>;  差异内容：1021300009 | api/@hms.security.fido2.d.ts |
| 新增错误码 | 类名：fido2；  API声明：function getPlatformAuthenticators(context: common.Context): Promise<Array<AuthenticatorMetadata>>;  差异内容：NA | 类名：fido2；  API声明：function getPlatformAuthenticators(context: common.Context): Promise<Array<AuthenticatorMetadata>>;  差异内容：1021300009 | api/@hms.security.fido2.d.ts |
| 新增错误码 | 类名：fido2；  API声明：function authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAssertionCredential>;  差异内容：NA | 类名：fido2；  API声明：function authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAssertionCredential>;  差异内容：1021300013 | api/@hms.security.fido2.d.ts |
| 权限变更 | 类名：did；  API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise<ImportDigitalCredentialResponse>;  差异内容：NA | 类名：did；  API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise<ImportDigitalCredentialResponse>;  差异内容：ohos.permission.ACCESS\_DIGITAL\_IDENTITY | api/@hms.security.did.d.ts |
| 权限变更 | 类名：did；  API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<void>;  差异内容：NA | 类名：did；  API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<void>;  差异内容：ohos.permission.ACCESS\_DIGITAL\_IDENTITY | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter；  API声明：credentialCategory?: string;  差异内容：credentialCategory?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ClientCapability；  API声明：EXTENSION\_AUTH\_TYPE\_LIST = 'extension:authTypeList'  差异内容：EXTENSION\_AUTH\_TYPE\_LIST = 'extension:authTypeList' | api/@hms.security.fido2.d.ts |
