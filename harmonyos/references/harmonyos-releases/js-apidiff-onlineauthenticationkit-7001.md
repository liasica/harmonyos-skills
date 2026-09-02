---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-onlineauthenticationkit-7001
title: Online Authentication Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Online Authentication Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:3d6e017fea8aa1db3789ae81e73860f3fff83c9488a0e5c0b4213aff8bff148f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace did  差异内容：declare namespace did | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：enum KeyAlgo  差异内容：enum KeyAlgo | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyAlgo；  API声明：SM2 = 1  差异内容：SM2 = 1 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyAlgo；  API声明：SM4 = 2  差异内容：SM4 = 2 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyAlgo；  API声明：P256 = 3  差异内容：P256 = 3 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyAlgo；  API声明：ED25519 = 4  差异内容：ED25519 = 4 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyAlgo；  API声明：AES128 = 5  差异内容：AES128 = 5 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyAlgo；  API声明：AES256 = 6  差异内容：AES256 = 6 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：enum AuthType  差异内容：enum AuthType | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthType；  API声明：UVM\_PIN = 1  差异内容：UVM\_PIN = 1 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthType；  API声明：UVM\_FINGERPRINT = 4  差异内容：UVM\_FINGERPRINT = 4 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthType；  API声明：UVM\_FACE = 2  差异内容：UVM\_FACE = 2 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：enum KeyPurpose  差异内容：enum KeyPurpose | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyPurpose；  API声明：ENCRYPT = 1  差异内容：ENCRYPT = 1 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyPurpose；  API声明：DECRYPT = 2  差异内容：DECRYPT = 2 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyPurpose；  API声明：SIGN = 3  差异内容：SIGN = 3 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyPurpose；  API声明：VERIFY = 4  差异内容：VERIFY = 4 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：enum CredentialType  差异内容：enum CredentialType | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialType；  API声明：VC = 1  差异内容：VC = 1 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialType；  API声明：VP = 2  差异内容：VP = 2 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialType；  API声明：SELECTIVE\_DISCLOSURE\_VC = 3  差异内容：SELECTIVE\_DISCLOSURE\_VC = 3 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialType；  API声明：SELECTIVE\_DISCLOSURE\_VP = 4  差异内容：SELECTIVE\_DISCLOSURE\_VP = 4 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：enum CryptoScheme  差异内容：enum CryptoScheme | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CryptoScheme；  API声明：IFAA\_FIXED\_ENVELOPE = 1  差异内容：IFAA\_FIXED\_ENVELOPE = 1 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CryptoScheme；  API声明：IFAA\_SEPARATE\_DECLARE\_ENVELOPE = 2  差异内容：IFAA\_SEPARATE\_DECLARE\_ENVELOPE = 2 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：enum ApprovalScheme  差异内容：enum ApprovalScheme | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ApprovalScheme；  API声明：IFAA\_OPERATOR\_APPROVAL = 1  差异内容：IFAA\_OPERATOR\_APPROVAL = 1 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：enum AuthMode  差异内容：enum AuthMode | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthMode；  API声明：SINGLE = 1  差异内容：SINGLE = 1 | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface KeyConfig  差异内容：interface KeyConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyConfig；  API声明：algorithm: KeyAlgo;  差异内容：algorithm: KeyAlgo; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：KeyConfig；  API声明：purposeList: KeyPurpose[];  差异内容：purposeList: KeyPurpose[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface AuthenticatorConfig  差异内容：interface AuthenticatorConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthenticatorConfig；  API声明：authTypeList: AuthType[];  差异内容：authTypeList: AuthType[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthenticatorConfig；  API声明：requireBioId?: boolean;  差异内容：requireBioId?: boolean; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthenticatorConfig；  API声明：authMode?: AuthMode;  差异内容：authMode?: AuthMode; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface GenerateKeyRequest  差异内容：interface GenerateKeyRequest | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyRequest；  API声明：keyAlias: string;  差异内容：keyAlias: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyRequest；  API声明：keyConfig: KeyConfig;  差异内容：keyConfig: KeyConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyRequest；  API声明：authenticatorConfig?: AuthenticatorConfig;  差异内容：authenticatorConfig?: AuthenticatorConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyRequest；  API声明：extension?: string;  差异内容：extension?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface GenerateKeyResponse  差异内容：interface GenerateKeyResponse | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyResponse；  API声明：publicKey: Uint8Array;  差异内容：publicKey: Uint8Array; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyResponse；  API声明：bioId?: string;  差异内容：bioId?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyResponse；  API声明：certChain: Array<Uint8Array>;  差异内容：certChain: Array<Uint8Array>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GenerateKeyResponse；  API声明：extension?: string;  差异内容：extension?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface DidKey  差异内容：interface DidKey | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：DidKey；  API声明：keyAlias?: string;  差异内容：keyAlias?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：DidKey；  API声明：keyId?: string;  差异内容：keyId?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface ImportDidRequest  差异内容：interface ImportDidRequest | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDidRequest；  API声明：isUpdate?: boolean;  差异内容：isUpdate?: boolean; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDidRequest；  API声明：did: string;  差异内容：did: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDidRequest；  API声明：didKeyList: DidKey[];  差异内容：didKeyList: DidKey[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDidRequest；  API声明：didDoc?: string;  差异内容：didDoc?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDidRequest；  API声明：additionalData?: string;  差异内容：additionalData?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface SignRequest  差异内容：interface SignRequest | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：SignRequest；  API声明：inData: Uint8Array;  差异内容：inData: Uint8Array; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：SignRequest；  API声明：keyId: string;  差异内容：keyId: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface SignResponse  差异内容：interface SignResponse | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：SignResponse；  API声明：outData: Uint8Array;  差异内容：outData: Uint8Array; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：SignResponse；  API声明：bioId?: string;  差异内容：bioId?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface QueryDidConfig  差异内容：interface QueryDidConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidConfig；  API声明：requireDidKey?: boolean;  差异内容：requireDidKey?: boolean; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidConfig；  API声明：requireDidDoc?: boolean;  差异内容：requireDidDoc?: boolean; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidConfig；  API声明：requireAdditionalData?: boolean;  差异内容：requireAdditionalData?: boolean; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface QueryDidRequest  差异内容：interface QueryDidRequest | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidRequest；  API声明：did: string;  差异内容：did: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidRequest；  API声明：queryDidConfig?: QueryDidConfig;  差异内容：queryDidConfig?: QueryDidConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface QueryDidResponse  差异内容：interface QueryDidResponse | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidResponse；  API声明：didKeyList?: DidKey[];  差异内容：didKeyList?: DidKey[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidResponse；  API声明：didDoc?: string;  差异内容：didDoc?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDidResponse；  API声明：additionalData?: string;  差异内容：additionalData?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface EncryptConfig  差异内容：interface EncryptConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：EncryptConfig；  API声明：cryptoScheme: CryptoScheme;  差异内容：cryptoScheme: CryptoScheme; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：EncryptConfig；  API声明：encryptKey: Uint8Array;  差异内容：encryptKey: Uint8Array; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：EncryptConfig；  API声明：keyId?: string;  差异内容：keyId?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：EncryptConfig；  API声明：algorithm: KeyAlgo;  差异内容：algorithm: KeyAlgo; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface ApprovalData  差异内容：interface ApprovalData | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ApprovalData；  API声明：approvalScheme: ApprovalScheme;  差异内容：approvalScheme: ApprovalScheme; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ApprovalData；  API声明：data?: string;  差异内容：data?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface DecryptConfig  差异内容：interface DecryptConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：DecryptConfig；  API声明：cryptoScheme: CryptoScheme;  差异内容：cryptoScheme: CryptoScheme; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：DecryptConfig；  API声明：keyId: string;  差异内容：keyId: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：DecryptConfig；  API声明：data?: string;  差异内容：data?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface ApprovalConfig  差异内容：interface ApprovalConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ApprovalConfig；  API声明：approvalScheme: ApprovalScheme;  差异内容：approvalScheme: ApprovalScheme; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ApprovalConfig；  API声明：publicKey: Uint8Array;  差异内容：publicKey: Uint8Array; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ApprovalConfig；  API声明：algorithm: KeyAlgo;  差异内容：algorithm: KeyAlgo; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface CredentialDisplayConfig  差异内容：interface CredentialDisplayConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialDisplayConfig；  API声明：credentialDisplayName: string;  差异内容：credentialDisplayName: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialDisplayConfig；  API声明：issuerDisplayName: string;  差异内容：issuerDisplayName: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialDisplayConfig；  API声明：propertyDisplayName: string;  差异内容：propertyDisplayName: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface AuthConfig  差异内容：interface AuthConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：AuthConfig；  API声明：requireAuth?: boolean;  差异内容：requireAuth?: boolean; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface CredentialSecurityConfig  差异内容：interface CredentialSecurityConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialSecurityConfig；  API声明：approvalConfig?: ApprovalConfig;  差异内容：approvalConfig?: ApprovalConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialSecurityConfig；  API声明：decryptConfig?: DecryptConfig;  差异内容：decryptConfig?: DecryptConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialSecurityConfig；  API声明：authConfig?: AuthConfig;  差异内容：authConfig?: AuthConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface ImportDigitalCredentialRequest  差异内容：interface ImportDigitalCredentialRequest | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialRequest；  API声明：did: string;  差异内容：did: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialRequest；  API声明：credentialType?: CredentialType;  差异内容：credentialType?: CredentialType; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialRequest；  API声明：isUpdate?: boolean;  差异内容：isUpdate?: boolean; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialRequest；  API声明：securityConfig?: CredentialSecurityConfig;  差异内容：securityConfig?: CredentialSecurityConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialRequest；  API声明：credentialData: string;  差异内容：credentialData: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialRequest；  API声明：displayConfig: CredentialDisplayConfig;  差异内容：displayConfig: CredentialDisplayConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialRequest；  API声明：extension?: string;  差异内容：extension?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface ImportDigitalCredentialResponse  差异内容：interface ImportDigitalCredentialResponse | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ImportDigitalCredentialResponse；  API声明：credentialSummary: string;  差异内容：credentialSummary: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface HolderConfig  差异内容：interface HolderConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：HolderConfig；  API声明：holderDid: string;  差异内容：holderDid: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：HolderConfig；  API声明：holderDidKeyId: string;  差异内容：holderDidKeyId: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface CredentialFilter  差异内容：interface CredentialFilter | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter；  API声明：credentialId?: string;  差异内容：credentialId?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter；  API声明：issuerDid?: string;  差异内容：issuerDid?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter；  API声明：credentialProvider?: string;  差异内容：credentialProvider?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter；  API声明：credentialDisclosurePropertyList?: string[];  差异内容：credentialDisclosurePropertyList?: string[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter；  API声明：credentialDisplayConfig?: CredentialDisplayConfig;  差异内容：credentialDisplayConfig?: CredentialDisplayConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter；  API声明：extension?: string;  差异内容：extension?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface PresentDisplayConfig  差异内容：interface PresentDisplayConfig | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：PresentDisplayConfig；  API声明：verifierDisplayName: string;  差异内容：verifierDisplayName: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：PresentDisplayConfig；  API声明：purpose: string;  差异内容：purpose: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：PresentDisplayConfig；  API声明：extension?: string;  差异内容：extension?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface GetDigitalCredentialRequest  差异内容：interface GetDigitalCredentialRequest | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：credentialType?: CredentialType;  差异内容：credentialType?: CredentialType; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：displayConfig: PresentDisplayConfig;  差异内容：displayConfig: PresentDisplayConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：verifierDid?: string;  差异内容：verifierDid?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：encryptConfig?: EncryptConfig;  差异内容：encryptConfig?: EncryptConfig; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：approvalData?: ApprovalData;  差异内容：approvalData?: ApprovalData; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：holderConfigList: HolderConfig[];  差异内容：holderConfigList: HolderConfig[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：credentialFilterList?: CredentialFilter[];  差异内容：credentialFilterList?: CredentialFilter[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialRequest；  API声明：extension?: string;  差异内容：extension?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface QueryDigitalCredentialResponse  差异内容：interface QueryDigitalCredentialResponse | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：QueryDigitalCredentialResponse；  API声明：credentialSummaryList: string[];  差异内容：credentialSummaryList: string[]; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：interface GetDigitalCredentialResponse  差异内容：interface GetDigitalCredentialResponse | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialResponse；  API声明：credentialData: string;  差异内容：credentialData: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：GetDigitalCredentialResponse；  API声明：bioId?: string;  差异内容：bioId?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function generateKey(context: common.Context, generateKeyRequest: GenerateKeyRequest): Promise<GenerateKeyResponse>;  差异内容：function generateKey(context: common.Context, generateKeyRequest: GenerateKeyRequest): Promise<GenerateKeyResponse>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function importDid(context: common.Context, importDidRequest: ImportDidRequest): Promise<void>;  差异内容：function importDid(context: common.Context, importDidRequest: ImportDidRequest): Promise<void>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function queryDid(context: common.Context, queryDidRequest: QueryDidRequest): Promise<QueryDidResponse>;  差异内容：function queryDid(context: common.Context, queryDidRequest: QueryDidRequest): Promise<QueryDidResponse>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function deleteDid(context: common.Context, did: string): Promise<void>;  差异内容：function deleteDid(context: common.Context, did: string): Promise<void>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function sign(context: common.Context, signRequest: SignRequest): Promise<SignResponse>;  差异内容：function sign(context: common.Context, signRequest: SignRequest): Promise<SignResponse>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise<ImportDigitalCredentialResponse>;  差异内容：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise<ImportDigitalCredentialResponse>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function queryDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<QueryDigitalCredentialResponse>;  差异内容：function queryDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<QueryDigitalCredentialResponse>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<void>;  差异内容：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise<void>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：did；  API声明：function getDigitalCredential(context: common.Context, getDigitalCredentialRequest: GetDigitalCredentialRequest): Promise<GetDigitalCredentialResponse>;  差异内容：function getDigitalCredential(context: common.Context, getDigitalCredentialRequest: GetDigitalCredentialRequest): Promise<GetDigitalCredentialResponse>; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ClientCapability；  API声明：EXTENSION\_LARGEBLOB = 'extension:largeblob'  差异内容：EXTENSION\_LARGEBLOB = 'extension:largeblob' | api/@hms.security.fido2.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.did.d.ts  差异内容：OnlineAuthenticationKit | api/@hms.security.did.d.ts |
