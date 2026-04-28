---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-510
title: Device Certificate Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fdc129acdcf1b1ae284a414060d06ee792bc5278a267e09eacfa9e0f340d5c92
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：cert；  API声明：function createX509Cert(inStream: EncodingBlob, callback: AsyncCallback<X509Cert>): void;  差异内容：NA | 类名：cert；  API声明：function createX509Cert(inStream: EncodingBlob, callback: AsyncCallback<X509Cert>): void;  差异内容：19030001 | api/@ohos.security.cert.d.ts |
| 新增错误码 | 类名：cert；  API声明：function createX509Cert(inStream: EncodingBlob): Promise<X509Cert>;  差异内容：NA | 类名：cert；  API声明：function createX509Cert(inStream: EncodingBlob): Promise<X509Cert>;  差异内容：19030001 | api/@ohos.security.cert.d.ts |
| 新增错误码 | 类名：cert；  API声明：function createCertExtension(inStream: EncodingBlob, callback: AsyncCallback<CertExtension>): void;  差异内容：NA | 类名：cert；  API声明：function createCertExtension(inStream: EncodingBlob, callback: AsyncCallback<CertExtension>): void;  差异内容：19030001 | api/@ohos.security.cert.d.ts |
| 新增错误码 | 类名：cert；  API声明：function createCertExtension(inStream: EncodingBlob): Promise<CertExtension>;  差异内容：NA | 类名：cert；  API声明：function createCertExtension(inStream: EncodingBlob): Promise<CertExtension>;  差异内容：19030001 | api/@ohos.security.cert.d.ts |
| 新增错误码 | 类名：certificateManagerDialog；  API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>;  差异内容：NA | 类名：certificateManagerDialog；  API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>;  差异内容：29700005 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_MAYBE\_WRONG\_PASSWORD = 19030008  差异内容：ERR\_MAYBE\_WRONG\_PASSWORD = 19030008 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum EncodingBaseFormat  差异内容：enum EncodingBaseFormat | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：EncodingBaseFormat；  API声明：PEM = 0  差异内容：PEM = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：EncodingBaseFormat；  API声明：DER = 1  差异内容：DER = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface Pkcs12Data  差异内容：interface Pkcs12Data | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12Data；  API声明：privateKey?: string | Uint8Array;  差异内容：privateKey?: string | Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12Data；  API声明：cert?: X509Cert;  差异内容：cert?: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12Data；  API声明：otherCerts?: Array<X509Cert>;  差异内容：otherCerts?: Array<X509Cert>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface Pkcs12ParsingConfig  差异内容：interface Pkcs12ParsingConfig | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12ParsingConfig；  API声明：password: string;  差异内容：password: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12ParsingConfig；  API声明：needsPrivateKey?: boolean;  差异内容：needsPrivateKey?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12ParsingConfig；  API声明：privateKeyFormat?: EncodingBaseFormat;  差异内容：privateKeyFormat?: EncodingBaseFormat; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12ParsingConfig；  API声明：needsCert?: boolean;  差异内容：needsCert?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12ParsingConfig；  API声明：needsOtherCerts?: boolean;  差异内容：needsOtherCerts?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function parsePkcs12(data: Uint8Array, config: Pkcs12ParsingConfig): Pkcs12Data;  差异内容：function parsePkcs12(data: Uint8Array, config: Pkcs12ParsingConfig): Pkcs12Data; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum CmsContentType  差异内容：enum CmsContentType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsContentType；  API声明：SIGNED\_DATA = 0  差异内容：SIGNED\_DATA = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum CmsContentDataFormat  差异内容：enum CmsContentDataFormat | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsContentDataFormat；  API声明：BINARY = 0  差异内容：BINARY = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsContentDataFormat；  API声明：TEXT = 1  差异内容：TEXT = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum CmsFormat  差异内容：enum CmsFormat | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsFormat；  API声明：PEM = 0  差异内容：PEM = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsFormat；  API声明：DER = 1  差异内容：DER = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface PrivateKeyInfo  差异内容：interface PrivateKeyInfo | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PrivateKeyInfo；  API声明：key: string | Uint8Array;  差异内容：key: string | Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PrivateKeyInfo；  API声明：password?: string;  差异内容：password?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface CmsSignerConfig  差异内容：interface CmsSignerConfig | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsSignerConfig；  API声明：mdName: string;  差异内容：mdName: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsSignerConfig；  API声明：addCert?: boolean;  差异内容：addCert?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsSignerConfig；  API声明：addAttr?: boolean;  差异内容：addAttr?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsSignerConfig；  API声明：addSmimeCapAttr?: boolean;  差异内容：addSmimeCapAttr?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface CmsGeneratorOptions  差异内容：interface CmsGeneratorOptions | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGeneratorOptions；  API声明：contentDataFormat?: CmsContentDataFormat;  差异内容：contentDataFormat?: CmsContentDataFormat; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGeneratorOptions；  API声明：outFormat?: CmsFormat;  差异内容：outFormat?: CmsFormat; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGeneratorOptions；  API声明：isDetached?: boolean;  差异内容：isDetached?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface CmsGenerator  差异内容：interface CmsGenerator | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGenerator；  API声明：addSigner(cert: X509Cert, keyInfo: PrivateKeyInfo, config: CmsSignerConfig): void;  差异内容：addSigner(cert: X509Cert, keyInfo: PrivateKeyInfo, config: CmsSignerConfig): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGenerator；  API声明：addCert(cert: X509Cert): void;  差异内容：addCert(cert: X509Cert): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGenerator；  API声明：doFinal(data: Uint8Array, options?: CmsGeneratorOptions): Promise<Uint8Array | string>;  差异内容：doFinal(data: Uint8Array, options?: CmsGeneratorOptions): Promise<Uint8Array | string>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGenerator；  API声明：doFinalSync(data: Uint8Array, options?: CmsGeneratorOptions): Uint8Array | string;  差异内容：doFinalSync(data: Uint8Array, options?: CmsGeneratorOptions): Uint8Array | string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createCmsGenerator(contentType: CmsContentType): CmsGenerator;  差异内容：function createCmsGenerator(contentType: CmsContentType): CmsGenerator; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface CsrAttribute  差异内容：interface CsrAttribute | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CsrAttribute；  API声明：type: string;  差异内容：type: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CsrAttribute；  API声明：value: string;  差异内容：value: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface CsrGenerationConfig  差异内容：interface CsrGenerationConfig | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CsrGenerationConfig；  API声明：subject: X500DistinguishedName;  差异内容：subject: X500DistinguishedName; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CsrGenerationConfig；  API声明：mdName: string;  差异内容：mdName: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CsrGenerationConfig；  API声明：attributes?: Array<CsrAttribute>;  差异内容：attributes?: Array<CsrAttribute>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CsrGenerationConfig；  API声明：outFormat?: EncodingBaseFormat;  差异内容：outFormat?: EncodingBaseFormat; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function generateCsr(keyInfo: PrivateKeyInfo, config: CsrGenerationConfig): string | Uint8Array;  差异内容：function generateCsr(keyInfo: PrivateKeyInfo, config: CsrGenerationConfig): string | Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>;  差异内容：function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>;  差异内容：function getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_DEVICE\_ENTER\_ADVSECMODE = 17500007  差异内容：CM\_ERROR\_DEVICE\_ENTER\_ADVSECMODE = 17500007 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_SM3 = 7  差异内容：CM\_DIGEST\_SM3 = 7 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：export enum CertType  差异内容：export enum CertType | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertType；  API声明：CA\_CERT\_SYSTEM = 0  差异内容：CA\_CERT\_SYSTEM = 0 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertType；  API声明：CA\_CERT\_USER = 1  差异内容：CA\_CERT\_USER = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：export enum CertScope  差异内容：export enum CertScope | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertScope；  API声明：CURRENT\_USER = 1  差异内容：CURRENT\_USER = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertScope；  API声明：GLOBAL\_USER = 2  差异内容：GLOBAL\_USER = 2 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：export interface CertStoreProperty  差异内容：export interface CertStoreProperty | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertStoreProperty；  API声明：certType: CertType;  差异内容：certType: CertType; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertStoreProperty；  API声明：certScope?: CertScope;  差异内容：certScope?: CertScope; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getCertificateStorePath(property: CertStoreProperty): string;  差异内容：function getCertificateStorePath(property: CertStoreProperty): string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult;  差异内容：function installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function uninstallUserTrustedCertificateSync(certUri: string): void;  差异内容：function uninstallUserTrustedCertificateSync(certUri: string): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：export enum AuthStorageLevel  差异内容：export enum AuthStorageLevel | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：AuthStorageLevel；  API声明：EL1 = 1  差异内容：EL1 = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：AuthStorageLevel；  API声明：EL2 = 2  差异内容：EL2 = 2 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：AuthStorageLevel；  API声明：EL4 = 4  差异内容：EL4 = 4 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode；  API声明：ERROR\_NOT\_COMPLY\_SECURITY\_POLICY = 29700005  差异内容：ERROR\_NOT\_COMPLY\_SECURITY\_POLICY = 29700005 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateScope；  API声明：NOT\_SPECIFIED = 0  差异内容：NOT\_SPECIFIED = 0 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateScope；  API声明：GLOBAL\_USER = 2  差异内容：GLOBAL\_USER = 2 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：function openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>;  差异内容：function openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：export interface CertificateDialogProperty  差异内容：export interface CertificateDialogProperty | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogProperty；  API声明：showInstallButton: boolean;  差异内容：showInstallButton: boolean; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：function openCertificateDetailDialog(context: common.Context, cert: Uint8Array, property: CertificateDialogProperty): Promise<void>;  差异内容：function openCertificateDetailDialog(context: common.Context, cert: Uint8Array, property: CertificateDialogProperty): Promise<void>; | api/@ohos.security.certManagerDialog.d.ts |
