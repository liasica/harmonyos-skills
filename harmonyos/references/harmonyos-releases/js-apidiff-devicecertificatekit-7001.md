---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-7001
title: Device Certificate Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:d2a31d0539f8d1faa21479a27c04f1389de808332bc09beca9036609a7f28e30
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：certificateManagerDialog；  API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>;  差异内容：NA | 类名：certificateManagerDialog；  API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>;  差异内容：801 | api/@ohos.security.certManagerDialog.d.ts |
| 新增错误码 | 类名：certificateManagerDialog；  API声明：function openAuthorizeDialog(context: common.Context): Promise<string>;  差异内容：NA | 类名：certificateManagerDialog；  API声明：function openAuthorizeDialog(context: common.Context): Promise<string>;  差异内容：801 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CERT\_UNTRUSTED = 19030009  差异内容：ERR\_CERT\_UNTRUSTED = 19030009 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CERT\_HAS\_REVOKED = 19030010  差异内容：ERR\_CERT\_HAS\_REVOKED = 19030010 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_UNKNOWN\_CRITICAL\_EXTENSION = 19030011  差异内容：ERR\_UNKNOWN\_CRITICAL\_EXTENSION = 19030011 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CERT\_HOSTNAME\_MISMATCH = 19030012  差异内容：ERR\_CERT\_HOSTNAME\_MISMATCH = 19030012 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CERT\_EMAIL\_ADDRESS\_MISMATCH = 19030013  差异内容：ERR\_CERT\_EMAIL\_ADDRESS\_MISMATCH = 19030013 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CERT\_KEYUSAGE\_MISMATCH = 19030014  差异内容：ERR\_CERT\_KEYUSAGE\_MISMATCH = 19030014 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CRL\_NOT\_FOUND = 19030015  差异内容：ERR\_CRL\_NOT\_FOUND = 19030015 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CRL\_NOT\_YET\_VALID = 19030016  差异内容：ERR\_CRL\_NOT\_YET\_VALID = 19030016 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CRL\_HAS\_EXPIRED = 19030017  差异内容：ERR\_CRL\_HAS\_EXPIRED = 19030017 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CRL\_SIGNATURE\_FAILURE = 19030018  差异内容：ERR\_CRL\_SIGNATURE\_FAILURE = 19030018 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_CRL\_ISSUER\_NOT\_FOUND = 19030019  差异内容：ERR\_CRL\_ISSUER\_NOT\_FOUND = 19030019 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_OCSP\_RESPONSE\_NOT\_FOUND = 19030020  差异内容：ERR\_OCSP\_RESPONSE\_NOT\_FOUND = 19030020 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_OCSP\_RESPONSE\_INVALID = 19030021  差异内容：ERR\_OCSP\_RESPONSE\_INVALID = 19030021 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_OCSP\_SIGNATURE\_FAILURE = 19030022  差异内容：ERR\_OCSP\_SIGNATURE\_FAILURE = 19030022 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_OCSP\_CERT\_STATUS\_UNKNOWN = 19030023  差异内容：ERR\_OCSP\_CERT\_STATUS\_UNKNOWN = 19030023 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_NETWORK\_TIMEOUT = 19030024  差异内容：ERR\_NETWORK\_TIMEOUT = 19030024 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum CertRevocationFlag  差异内容：enum CertRevocationFlag | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag；  API声明：CERT\_REVOCATION\_PREFER\_OCSP = 0  差异内容：CERT\_REVOCATION\_PREFER\_OCSP = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag；  API声明：CERT\_REVOCATION\_CRL\_CHECK = 1  差异内容：CERT\_REVOCATION\_CRL\_CHECK = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag；  API声明：CERT\_REVOCATION\_OCSP\_CHECK = 2  差异内容：CERT\_REVOCATION\_OCSP\_CHECK = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag；  API声明：CERT\_REVOCATION\_CHECK\_ALL\_CERT = 3  差异内容：CERT\_REVOCATION\_CHECK\_ALL\_CERT = 3 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum OcspDigest  差异内容：enum OcspDigest | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest；  API声明：SHA1 = 0  差异内容：SHA1 = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest；  API声明：SHA224 = 1  差异内容：SHA224 = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest；  API声明：SHA256 = 2  差异内容：SHA256 = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest；  API声明：SHA384 = 3  差异内容：SHA384 = 3 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest；  API声明：SHA512 = 4  差异内容：SHA512 = 4 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface X509CertRevokedParams  差异内容：interface X509CertRevokedParams | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams；  API声明：revocationFlags: Array<CertRevocationFlag>;  差异内容：revocationFlags: Array<CertRevocationFlag>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams；  API声明：crls?: Array<X509CRL>;  差异内容：crls?: Array<X509CRL>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams；  API声明：allowDownloadCrl?: boolean;  差异内容：allowDownloadCrl?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams；  API声明：ocspResponses?: Array<Uint8Array>;  差异内容：ocspResponses?: Array<Uint8Array>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams；  API声明：allowOcspCheckOnline?: boolean;  差异内容：allowOcspCheckOnline?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams；  API声明：ocspDigest?: OcspDigest;  差异内容：ocspDigest?: OcspDigest; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface CertValidationParams  差异内容：interface CertValidationParams | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：untrustedCerts?: Array<X509Cert>;  差异内容：untrustedCerts?: Array<X509Cert>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：trustedCerts?: Array<X509Cert>;  差异内容：trustedCerts?: Array<X509Cert>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：trustSystemCa?: boolean;  差异内容：trustSystemCa?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：partialChain?: boolean;  差异内容：partialChain?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：allowDownloadIntermediateCa?: boolean;  差异内容：allowDownloadIntermediateCa?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：date?: string;  差异内容：date?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：validateDate?: boolean;  差异内容：validateDate?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：ignoreErrs?: Array<CertResult>;  差异内容：ignoreErrs?: Array<CertResult>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：hostnames?: Array<string>;  差异内容：hostnames?: Array<string>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：emailAddresses?: Array<string>;  差异内容：emailAddresses?: Array<string>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：keyUsage?: Array<KeyUsageType>;  差异内容：keyUsage?: Array<KeyUsageType>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：userId?: Uint8Array;  差异内容：userId?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams；  API声明：revokedParams?: X509CertRevokedParams;  差异内容：revokedParams?: X509CertRevokedParams; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface CertValidationResult  差异内容：interface CertValidationResult | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationResult；  API声明：readonly certChain: Array<X509Cert>;  差异内容：readonly certChain: Array<X509Cert>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidator；  API声明：validateCert(cert: X509Cert, params: CertValidationParams): Promise<CertValidationResult>;  差异内容：validateCert(cert: X509Cert, params: CertValidationParams): Promise<CertValidationResult>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：privateKey?: string | Uint8Array;  差异内容：privateKey?: string | Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：AuthorizeRequest；  API声明：keyAlgIDs?: Array<string>;  差异内容：keyAlgIDs?: Array<string>; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：AuthorizeRequest；  API声明：issuers?: Array<Uint8Array>;  差异内容：issuers?: Array<Uint8Array>; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：AuthorizeRequest；  API声明：uri?: string;  差异内容：uri?: string; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：function supportsCACertDialog(): boolean;  差异内容：function supportsCACertDialog(): boolean; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：uriList?: Array<string>;  差异内容：uriList?: Array<string>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：export enum CertFileFormat  差异内容：export enum CertFileFormat | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertFileFormat；  API声明：PEM\_DER = 0  差异内容：PEM\_DER = 0 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertFileFormat；  API声明：P7B = 1  差异内容：P7B = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：export interface CertBlob  差异内容：export interface CertBlob | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertBlob；  API声明：certData: Uint8Array;  差异内容：certData: Uint8Array; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertBlob；  API声明：certFormat?: CertFileFormat;  差异内容：certFormat?: CertFileFormat; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertBlob；  API声明：certScope?: CertScope;  差异内容：certScope?: CertScope; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function installUserTrustedCertificate(certificate: CertBlob): Promise<CMResult>;  差异内容：function installUserTrustedCertificate(certificate: CertBlob): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise<CMResult>;  差异内容：function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>;  差异内容：function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>; | api/@ohos.security.certManager.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X500DistinguishedName；  API声明：getName(): string;  差异内容：getName(): string; | 类名：X500DistinguishedName；  API声明：getName(type: string, encodingType: EncodingType): Array<string>;  差异内容：getName(type: string, encodingType: EncodingType): Array<string>; | api/@ohos.security.cert.d.ts |
