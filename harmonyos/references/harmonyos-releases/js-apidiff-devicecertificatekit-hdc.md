---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-hdc
title: Device Certificate Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:000dc1f0362ac5ee8a97e12ad785e2d1915f540022220c6eaa0a6262ae224b81
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：X509Cert；  API声明：getSerialNumber(): number;  差异内容：NA | 类名：X509Cert；  API声明：getSerialNumber(): number;  差异内容：10 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：cert；  API声明： interface X509CrlEntry  差异内容：NA | 类名：cert；  API声明： interface X509CrlEntry  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509CrlEntry；  API声明：getEncoded(callback: AsyncCallback<EncodingBlob>): void;  差异内容：NA | 类名：X509CrlEntry；  API声明：getEncoded(callback: AsyncCallback<EncodingBlob>): void;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509CrlEntry；  API声明：getEncoded(): Promise<EncodingBlob>;  差异内容：NA | 类名：X509CrlEntry；  API声明：getEncoded(): Promise<EncodingBlob>;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509CrlEntry；  API声明：getSerialNumber(): number;  差异内容：NA | 类名：X509CrlEntry；  API声明：getSerialNumber(): number;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509CrlEntry；  API声明：getCertIssuer(): DataBlob;  差异内容：NA | 类名：X509CrlEntry；  API声明：getCertIssuer(): DataBlob;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509CrlEntry；  API声明：getRevocationDate(): string;  差异内容：NA | 类名：X509CrlEntry；  API声明：getRevocationDate(): string;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：cert；  API声明： interface X509Crl  差异内容：NA | 类名：cert；  API声明： interface X509Crl  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：isRevoked(cert: X509Cert): boolean;  差异内容：NA | 类名：X509Crl；  API声明：isRevoked(cert: X509Cert): boolean;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getType(): string;  差异内容：NA | 类名：X509Crl；  API声明：getType(): string;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getEncoded(callback: AsyncCallback<EncodingBlob>): void;  差异内容：NA | 类名：X509Crl；  API声明：getEncoded(callback: AsyncCallback<EncodingBlob>): void;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getEncoded(): Promise<EncodingBlob>;  差异内容：NA | 类名：X509Crl；  API声明：getEncoded(): Promise<EncodingBlob>;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：X509Crl；  API声明：verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：verify(key: cryptoFramework.PubKey): Promise<void>;  差异内容：NA | 类名：X509Crl；  API声明：verify(key: cryptoFramework.PubKey): Promise<void>;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getVersion(): number;  差异内容：NA | 类名：X509Crl；  API声明：getVersion(): number;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getIssuerName(): DataBlob;  差异内容：NA | 类名：X509Crl；  API声明：getIssuerName(): DataBlob;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getLastUpdate(): string;  差异内容：NA | 类名：X509Crl；  API声明：getLastUpdate(): string;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getNextUpdate(): string;  差异内容：NA | 类名：X509Crl；  API声明：getNextUpdate(): string;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getRevokedCert(serialNumber: number): X509CrlEntry;  差异内容：NA | 类名：X509Crl；  API声明：getRevokedCert(serialNumber: number): X509CrlEntry;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getRevokedCertWithCert(cert: X509Cert): X509CrlEntry;  差异内容：NA | 类名：X509Crl；  API声明：getRevokedCertWithCert(cert: X509Cert): X509CrlEntry;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getRevokedCerts(callback: AsyncCallback<Array<X509CrlEntry>>): void;  差异内容：NA | 类名：X509Crl；  API声明：getRevokedCerts(callback: AsyncCallback<Array<X509CrlEntry>>): void;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getRevokedCerts(): Promise<Array<X509CrlEntry>>;  差异内容：NA | 类名：X509Crl；  API声明：getRevokedCerts(): Promise<Array<X509CrlEntry>>;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getTbsInfo(): DataBlob;  差异内容：NA | 类名：X509Crl；  API声明：getTbsInfo(): DataBlob;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getSignature(): DataBlob;  差异内容：NA | 类名：X509Crl；  API声明：getSignature(): DataBlob;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getSignatureAlgName(): string;  差异内容：NA | 类名：X509Crl；  API声明：getSignatureAlgName(): string;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getSignatureAlgOid(): string;  差异内容：NA | 类名：X509Crl；  API声明：getSignatureAlgOid(): string;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：X509Crl；  API声明：getSignatureAlgParams(): DataBlob;  差异内容：NA | 类名：X509Crl；  API声明：getSignatureAlgParams(): DataBlob;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：cert；  API声明：function createX509Crl(inStream: EncodingBlob, callback: AsyncCallback<X509Crl>): void;  差异内容：NA | 类名：cert；  API声明：function createX509Crl(inStream: EncodingBlob, callback: AsyncCallback<X509Crl>): void;  差异内容：11 | api/@ohos.security.cert.d.ts |
| API废弃版本变更 | 类名：cert；  API声明：function createX509Crl(inStream: EncodingBlob): Promise<X509Crl>;  差异内容：NA | 类名：cert；  API声明：function createX509Crl(inStream: EncodingBlob): Promise<X509Crl>;  差异内容：11 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：EncodingFormat；  API声明：FORMAT\_PKCS7 = 2  差异内容：FORMAT\_PKCS7 = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum CertItemType  差异内容： enum CertItemType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertItemType；  API声明：CERT\_ITEM\_TYPE\_TBS = 0  差异内容：CERT\_ITEM\_TYPE\_TBS = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertItemType；  API声明：CERT\_ITEM\_TYPE\_PUBLIC\_KEY = 1  差异内容：CERT\_ITEM\_TYPE\_PUBLIC\_KEY = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertItemType；  API声明：CERT\_ITEM\_TYPE\_ISSUER\_UNIQUE\_ID = 2  差异内容：CERT\_ITEM\_TYPE\_ISSUER\_UNIQUE\_ID = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertItemType；  API声明：CERT\_ITEM\_TYPE\_SUBJECT\_UNIQUE\_ID = 3  差异内容：CERT\_ITEM\_TYPE\_SUBJECT\_UNIQUE\_ID = 3 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertItemType；  API声明：CERT\_ITEM\_TYPE\_EXTENSIONS = 4  差异内容：CERT\_ITEM\_TYPE\_EXTENSIONS = 4 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum ExtensionOidType  差异内容： enum ExtensionOidType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ExtensionOidType；  API声明：EXTENSION\_OID\_TYPE\_ALL = 0  差异内容：EXTENSION\_OID\_TYPE\_ALL = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ExtensionOidType；  API声明：EXTENSION\_OID\_TYPE\_CRITICAL = 1  差异内容：EXTENSION\_OID\_TYPE\_CRITICAL = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ExtensionOidType；  API声明：EXTENSION\_OID\_TYPE\_UNCRITICAL = 2  差异内容：EXTENSION\_OID\_TYPE\_UNCRITICAL = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum ExtensionEntryType  差异内容： enum ExtensionEntryType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ExtensionEntryType；  API声明：EXTENSION\_ENTRY\_TYPE\_ENTRY = 0  差异内容：EXTENSION\_ENTRY\_TYPE\_ENTRY = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ExtensionEntryType；  API声明：EXTENSION\_ENTRY\_TYPE\_ENTRY\_CRITICAL = 1  差异内容：EXTENSION\_ENTRY\_TYPE\_ENTRY\_CRITICAL = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ExtensionEntryType；  API声明：EXTENSION\_ENTRY\_TYPE\_ENTRY\_VALUE = 2  差异内容：EXTENSION\_ENTRY\_TYPE\_ENTRY\_VALUE = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：getCertSerialNumber(): bigint;  差异内容：getCertSerialNumber(): bigint; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：getItem(itemType: CertItemType): DataBlob;  差异内容：getItem(itemType: CertItemType): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：match(param: X509CertMatchParameters): boolean;  差异内容：match(param: X509CertMatchParameters): boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：getCRLDistributionPoint(): DataArray;  差异内容：getCRLDistributionPoint(): DataArray; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：getIssuerX500DistinguishedName(): X500DistinguishedName;  差异内容：getIssuerX500DistinguishedName(): X500DistinguishedName; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：getSubjectX500DistinguishedName(): X500DistinguishedName;  差异内容：getSubjectX500DistinguishedName(): X500DistinguishedName; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：toString(): string;  差异内容：toString(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：hashCode(): Uint8Array;  差异内容：hashCode(): Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509Cert；  API声明：getExtensionsObject(): CertExtension;  差异内容：getExtensionsObject(): CertExtension; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface CertExtension  差异内容： interface CertExtension | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertExtension；  API声明：getEncoded(): EncodingBlob;  差异内容：getEncoded(): EncodingBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertExtension；  API声明：getOidList(valueType: ExtensionOidType): DataArray;  差异内容：getOidList(valueType: ExtensionOidType): DataArray; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertExtension；  API声明：getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob;  差异内容：getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertExtension；  API声明：checkCA(): number;  差异内容：checkCA(): number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertExtension；  API声明：hasUnsupportedCriticalExtension(): boolean;  差异内容：hasUnsupportedCriticalExtension(): boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createCertExtension(inStream: EncodingBlob, callback: AsyncCallback<CertExtension>): void;  差异内容：function createCertExtension(inStream: EncodingBlob, callback: AsyncCallback<CertExtension>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createCertExtension(inStream: EncodingBlob): Promise<CertExtension>;  差异内容：function createCertExtension(inStream: EncodingBlob): Promise<CertExtension>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface X509CRLEntry  差异内容： interface X509CRLEntry | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getEncoded(callback: AsyncCallback<EncodingBlob>): void;  差异内容：getEncoded(callback: AsyncCallback<EncodingBlob>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getEncoded(): Promise<EncodingBlob>;  差异内容：getEncoded(): Promise<EncodingBlob>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getSerialNumber(): bigint;  差异内容：getSerialNumber(): bigint; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getCertIssuer(): DataBlob;  差异内容：getCertIssuer(): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getRevocationDate(): string;  差异内容：getRevocationDate(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getExtensions(): DataBlob;  差异内容：getExtensions(): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：hasExtensions(): boolean;  差异内容：hasExtensions(): boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getCertIssuerX500DistinguishedName(): X500DistinguishedName;  差异内容：getCertIssuerX500DistinguishedName(): X500DistinguishedName; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：toString(): string;  差异内容：toString(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：hashCode(): Uint8Array;  差异内容：hashCode(): Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLEntry；  API声明：getExtensionsObject(): CertExtension;  差异内容：getExtensionsObject(): CertExtension; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface X509CRL  差异内容： interface X509CRL | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：isRevoked(cert: X509Cert): boolean;  差异内容：isRevoked(cert: X509Cert): boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getType(): string;  差异内容：getType(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getEncoded(callback: AsyncCallback<EncodingBlob>): void;  差异内容：getEncoded(callback: AsyncCallback<EncodingBlob>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getEncoded(): Promise<EncodingBlob>;  差异内容：getEncoded(): Promise<EncodingBlob>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void;  差异内容：verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：verify(key: cryptoFramework.PubKey): Promise<void>;  差异内容：verify(key: cryptoFramework.PubKey): Promise<void>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getVersion(): number;  差异内容：getVersion(): number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getIssuerName(): DataBlob;  差异内容：getIssuerName(): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getLastUpdate(): string;  差异内容：getLastUpdate(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getNextUpdate(): string;  差异内容：getNextUpdate(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getRevokedCert(serialNumber: bigint): X509CRLEntry;  差异内容：getRevokedCert(serialNumber: bigint): X509CRLEntry; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getRevokedCertWithCert(cert: X509Cert): X509CRLEntry;  差异内容：getRevokedCertWithCert(cert: X509Cert): X509CRLEntry; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void;  差异内容：getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getRevokedCerts(): Promise<Array<X509CRLEntry>>;  差异内容：getRevokedCerts(): Promise<Array<X509CRLEntry>>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getTBSInfo(): DataBlob;  差异内容：getTBSInfo(): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getSignature(): DataBlob;  差异内容：getSignature(): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getSignatureAlgName(): string;  差异内容：getSignatureAlgName(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getSignatureAlgOid(): string;  差异内容：getSignatureAlgOid(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getSignatureAlgParams(): DataBlob;  差异内容：getSignatureAlgParams(): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getExtensions(): DataBlob;  差异内容：getExtensions(): DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：match(param: X509CRLMatchParameters): boolean;  差异内容：match(param: X509CRLMatchParameters): boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getIssuerX500DistinguishedName(): X500DistinguishedName;  差异内容：getIssuerX500DistinguishedName(): X500DistinguishedName; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：toString(): string;  差异内容：toString(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：hashCode(): Uint8Array;  差异内容：hashCode(): Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRL；  API声明：getExtensionsObject(): CertExtension;  差异内容：getExtensionsObject(): CertExtension; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createX509CRL(inStream: EncodingBlob, callback: AsyncCallback<X509CRL>): void;  差异内容：function createX509CRL(inStream: EncodingBlob, callback: AsyncCallback<X509CRL>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createX509CRL(inStream: EncodingBlob): Promise<X509CRL>;  差异内容：function createX509CRL(inStream: EncodingBlob): Promise<X509CRL>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum GeneralNameType  差异内容： enum GeneralNameType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_OTHER\_NAME = 0  差异内容：GENERAL\_NAME\_TYPE\_OTHER\_NAME = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_RFC822\_NAME = 1  差异内容：GENERAL\_NAME\_TYPE\_RFC822\_NAME = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_DNS\_NAME = 2  差异内容：GENERAL\_NAME\_TYPE\_DNS\_NAME = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_X400\_ADDRESS = 3  差异内容：GENERAL\_NAME\_TYPE\_X400\_ADDRESS = 3 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_DIRECTORY\_NAME = 4  差异内容：GENERAL\_NAME\_TYPE\_DIRECTORY\_NAME = 4 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_EDI\_PARTY\_NAME = 5  差异内容：GENERAL\_NAME\_TYPE\_EDI\_PARTY\_NAME = 5 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_UNIFORM\_RESOURCE\_ID = 6  差异内容：GENERAL\_NAME\_TYPE\_UNIFORM\_RESOURCE\_ID = 6 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_IP\_ADDRESS = 7  差异内容：GENERAL\_NAME\_TYPE\_IP\_ADDRESS = 7 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralNameType；  API声明：GENERAL\_NAME\_TYPE\_REGISTERED\_ID = 8  差异内容：GENERAL\_NAME\_TYPE\_REGISTERED\_ID = 8 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface GeneralName  差异内容： interface GeneralName | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralName；  API声明：type: GeneralNameType;  差异内容：type: GeneralNameType; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：GeneralName；  API声明：name?: Uint8Array;  差异内容：name?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface X509CertMatchParameters  差异内容： interface X509CertMatchParameters | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：subjectAlternativeNames?: Array<GeneralName>;  差异内容：subjectAlternativeNames?: Array<GeneralName>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：matchAllSubjectAltNames?: boolean;  差异内容：matchAllSubjectAltNames?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：authorityKeyIdentifier?: Uint8Array;  差异内容：authorityKeyIdentifier?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：minPathLenConstraint?: number;  差异内容：minPathLenConstraint?: number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：x509Cert?: X509Cert;  差异内容：x509Cert?: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：validDate?: string;  差异内容：validDate?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：issuer?: Uint8Array;  差异内容：issuer?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：extendedKeyUsage?: Array<string>;  差异内容：extendedKeyUsage?: Array<string>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：nameConstraints?: Uint8Array;  差异内容：nameConstraints?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：certPolicy?: Array<string>;  差异内容：certPolicy?: Array<string>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：privateKeyValid?: string;  差异内容：privateKeyValid?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：keyUsage?: Array<boolean>;  差异内容：keyUsage?: Array<boolean>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：serialNumber?: bigint;  差异内容：serialNumber?: bigint; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：subject?: Uint8Array;  差异内容：subject?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：subjectKeyIdentifier?: Uint8Array;  差异内容：subjectKeyIdentifier?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：publicKey?: DataBlob;  差异内容：publicKey?: DataBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters；  API声明：publicKeyAlgID?: string;  差异内容：publicKeyAlgID?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface X509CRLMatchParameters  差异内容： interface X509CRLMatchParameters | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLMatchParameters；  API声明：issuer?: Array<Uint8Array>;  差异内容：issuer?: Array<Uint8Array>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLMatchParameters；  API声明：x509Cert?: X509Cert;  差异内容：x509Cert?: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLMatchParameters；  API声明：updateDateTime?: string;  差异内容：updateDateTime?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLMatchParameters；  API声明：maxCRL?: bigint;  差异内容：maxCRL?: bigint; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CRLMatchParameters；  API声明：minCRL?: bigint;  差异内容：minCRL?: bigint; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface CertCRLCollection  差异内容： interface CertCRLCollection | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertCRLCollection；  API声明：selectCerts(param: X509CertMatchParameters): Promise<Array<X509Cert>>;  差异内容：selectCerts(param: X509CertMatchParameters): Promise<Array<X509Cert>>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertCRLCollection；  API声明：selectCerts(param: X509CertMatchParameters, callback: AsyncCallback<Array<X509Cert>>): void;  差异内容：selectCerts(param: X509CertMatchParameters, callback: AsyncCallback<Array<X509Cert>>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertCRLCollection；  API声明：selectCRLs(param: X509CRLMatchParameters): Promise<Array<X509CRL>>;  差异内容：selectCRLs(param: X509CRLMatchParameters): Promise<Array<X509CRL>>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertCRLCollection；  API声明：selectCRLs(param: X509CRLMatchParameters, callback: AsyncCallback<Array<X509CRL>>): void;  差异内容：selectCRLs(param: X509CRLMatchParameters, callback: AsyncCallback<Array<X509CRL>>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createCertCRLCollection(certs: Array<X509Cert>, crls?: Array<X509CRL>): CertCRLCollection;  差异内容：function createCertCRLCollection(certs: Array<X509Cert>, crls?: Array<X509CRL>): CertCRLCollection; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface X509CertChain  差异内容： interface X509CertChain | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertChain；  API声明：getCertList(): Array<X509Cert>;  差异内容：getCertList(): Array<X509Cert>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertChain；  API声明：validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>;  差异内容：validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertChain；  API声明：validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void;  差异内容：validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertChain；  API声明：toString(): string;  差异内容：toString(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertChain；  API声明：hashCode(): Uint8Array;  差异内容：hashCode(): Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createX509CertChain(inStream: EncodingBlob): Promise<X509CertChain>;  差异内容：function createX509CertChain(inStream: EncodingBlob): Promise<X509CertChain>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createX509CertChain(inStream: EncodingBlob, callback: AsyncCallback<X509CertChain>): void;  差异内容：function createX509CertChain(inStream: EncodingBlob, callback: AsyncCallback<X509CertChain>): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createX509CertChain(certs: Array<X509Cert>): X509CertChain;  差异内容：function createX509CertChain(certs: Array<X509Cert>): X509CertChain; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>;  差异内容：function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>;  差异内容：function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>;  差异内容：function createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>;  差异内容：function createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface X500DistinguishedName  差异内容： interface X500DistinguishedName | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X500DistinguishedName；  API声明：getName(): string;  差异内容：getName(): string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X500DistinguishedName；  API声明：getName(type: string): Array<string>;  差异内容：getName(type: string): Array<string>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X500DistinguishedName；  API声明：getEncoded(): EncodingBlob;  差异内容：getEncoded(): EncodingBlob; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface X509TrustAnchor  差异内容： interface X509TrustAnchor | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509TrustAnchor；  API声明：CACert?: X509Cert;  差异内容：CACert?: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509TrustAnchor；  API声明：CAPubKey?: Uint8Array;  差异内容：CAPubKey?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509TrustAnchor；  API声明：CASubject?: Uint8Array;  差异内容：CASubject?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509TrustAnchor；  API声明：nameConstraints?: Uint8Array;  差异内容：nameConstraints?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum RevocationCheckOptions  差异内容： enum RevocationCheckOptions | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckOptions；  API声明：REVOCATION\_CHECK\_OPTION\_PREFER\_OCSP = 0  差异内容：REVOCATION\_CHECK\_OPTION\_PREFER\_OCSP = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckOptions；  API声明：REVOCATION\_CHECK\_OPTION\_ACCESS\_NETWORK  差异内容：REVOCATION\_CHECK\_OPTION\_ACCESS\_NETWORK | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckOptions；  API声明：REVOCATION\_CHECK\_OPTION\_FALLBACK\_NO\_PREFER  差异内容：REVOCATION\_CHECK\_OPTION\_FALLBACK\_NO\_PREFER | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckOptions；  API声明：REVOCATION\_CHECK\_OPTION\_FALLBACK\_LOCAL  差异内容：REVOCATION\_CHECK\_OPTION\_FALLBACK\_LOCAL | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum ValidationPolicyType  差异内容： enum ValidationPolicyType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ValidationPolicyType；  API声明：VALIDATION\_POLICY\_TYPE\_X509 = 0  差异内容：VALIDATION\_POLICY\_TYPE\_X509 = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：ValidationPolicyType；  API声明：VALIDATION\_POLICY\_TYPE\_SSL  差异内容：VALIDATION\_POLICY\_TYPE\_SSL | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum KeyUsageType  差异内容： enum KeyUsageType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_DIGITAL\_SIGNATURE = 0  差异内容：KEYUSAGE\_DIGITAL\_SIGNATURE = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_NON\_REPUDIATION  差异内容：KEYUSAGE\_NON\_REPUDIATION | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_KEY\_ENCIPHERMENT  差异内容：KEYUSAGE\_KEY\_ENCIPHERMENT | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_DATA\_ENCIPHERMENT  差异内容：KEYUSAGE\_DATA\_ENCIPHERMENT | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_KEY\_AGREEMENT  差异内容：KEYUSAGE\_KEY\_AGREEMENT | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_KEY\_CERT\_SIGN  差异内容：KEYUSAGE\_KEY\_CERT\_SIGN | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_CRL\_SIGN  差异内容：KEYUSAGE\_CRL\_SIGN | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_ENCIPHER\_ONLY  差异内容：KEYUSAGE\_ENCIPHER\_ONLY | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：KeyUsageType；  API声明：KEYUSAGE\_DECIPHER\_ONLY  差异内容：KEYUSAGE\_DECIPHER\_ONLY | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface RevocationCheckParameter  差异内容： interface RevocationCheckParameter | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckParameter；  API声明：ocspRequestExtension?: Array<Uint8Array>;  差异内容：ocspRequestExtension?: Array<Uint8Array>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckParameter；  API声明：ocspResponderURI?: string;  差异内容：ocspResponderURI?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckParameter；  API声明：ocspResponderCert?: X509Cert;  差异内容：ocspResponderCert?: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckParameter；  API声明：ocspResponses?: Uint8Array;  差异内容：ocspResponses?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckParameter；  API声明：crlDownloadURI?: string;  差异内容：crlDownloadURI?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckParameter；  API声明：options?: Array<RevocationCheckOptions>;  差异内容：options?: Array<RevocationCheckOptions>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckParameter；  API声明：ocspDigest?: string;  差异内容：ocspDigest?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface CertChainValidationParameters  差异内容： interface CertChainValidationParameters | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationParameters；  API声明：date?: string;  差异内容：date?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationParameters；  API声明：trustAnchors: Array<X509TrustAnchor>;  差异内容：trustAnchors: Array<X509TrustAnchor>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationParameters；  API声明：certCRLs?: Array<CertCRLCollection>;  差异内容：certCRLs?: Array<CertCRLCollection>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationParameters；  API声明：revocationCheckParam?: RevocationCheckParameter;  差异内容：revocationCheckParam?: RevocationCheckParameter; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationParameters；  API声明：policy?: ValidationPolicyType;  差异内容：policy?: ValidationPolicyType; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationParameters；  API声明：sslHostname?: string;  差异内容：sslHostname?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationParameters；  API声明：keyUsage?: Array<KeyUsageType>;  差异内容：keyUsage?: Array<KeyUsageType>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface CertChainValidationResult  差异内容： interface CertChainValidationResult | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationResult；  API声明：readonly trustAnchor: X509TrustAnchor;  差异内容：readonly trustAnchor: X509TrustAnchor; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidationResult；  API声明：readonly entityCert: X509Cert;  差异内容：readonly entityCert: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface CertChainBuildParameters  差异内容： interface CertChainBuildParameters | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainBuildParameters；  API声明：certMatchParameters: X509CertMatchParameters;  差异内容：certMatchParameters: X509CertMatchParameters; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainBuildParameters；  API声明：maxLength?: number;  差异内容：maxLength?: number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainBuildParameters；  API声明：validationParameters: CertChainValidationParameters;  差异内容：validationParameters: CertChainValidationParameters; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： interface CertChainBuildResult  差异内容： interface CertChainBuildResult | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainBuildResult；  API声明：readonly certChain: X509CertChain;  差异内容：readonly certChain: X509CertChain; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainBuildResult；  API声明：readonly validationResult: CertChainValidationResult;  差异内容：readonly validationResult: CertChainValidationResult; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace certificateManager  差异内容： declare namespace certificateManager | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export enum CMErrorCode  差异内容： export enum CMErrorCode | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_NO\_PERMISSION = 201  差异内容：CM\_ERROR\_NO\_PERMISSION = 201 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_INVALID\_PARAMS = 401  差异内容：CM\_ERROR\_INVALID\_PARAMS = 401 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_GENERIC = 17500001  差异内容：CM\_ERROR\_GENERIC = 17500001 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_NO\_FOUND = 17500002  差异内容：CM\_ERROR\_NO\_FOUND = 17500002 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_INCORRECT\_FORMAT = 17500003  差异内容：CM\_ERROR\_INCORRECT\_FORMAT = 17500003 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_MAX\_CERT\_COUNT\_REACHED = 17500004  差异内容：CM\_ERROR\_MAX\_CERT\_COUNT\_REACHED = 17500004 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_NO\_AUTHORIZATION = 17500005  差异内容：CM\_ERROR\_NO\_AUTHORIZATION = 17500005 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export interface CertInfo  差异内容： export interface CertInfo | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：certAlias: string;  差异内容：certAlias: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：state: boolean;  差异内容：state: boolean; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：issuerName: string;  差异内容：issuerName: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：subjectName: string;  差异内容：subjectName: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：serial: string;  差异内容：serial: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：notBefore: string;  差异内容：notBefore: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：notAfter: string;  差异内容：notAfter: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：fingerprintSha256: string;  差异内容：fingerprintSha256: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertInfo；  API声明：cert: Uint8Array;  差异内容：cert: Uint8Array; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export interface CertAbstract  差异内容： export interface CertAbstract | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertAbstract；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertAbstract；  API声明：certAlias: string;  差异内容：certAlias: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertAbstract；  API声明：state: boolean;  差异内容：state: boolean; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertAbstract；  API声明：subjectName: string;  差异内容：subjectName: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export interface Credential  差异内容： export interface Credential | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：Credential；  API声明：type: string;  差异内容：type: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：Credential；  API声明：alias: string;  差异内容：alias: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：Credential；  API声明：keyUri: string;  差异内容：keyUri: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：Credential；  API声明：certNum: number;  差异内容：certNum: number; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：Credential；  API声明：keyNum: number;  差异内容：keyNum: number; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：Credential；  API声明：credentialData: Uint8Array;  差异内容：credentialData: Uint8Array; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export interface CredentialAbstract  差异内容： export interface CredentialAbstract | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CredentialAbstract；  API声明：type: string;  差异内容：type: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CredentialAbstract；  API声明：alias: string;  差异内容：alias: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CredentialAbstract；  API声明：keyUri: string;  差异内容：keyUri: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export interface CMResult  差异内容： export interface CMResult | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：certList?: Array<CertAbstract>;  差异内容：certList?: Array<CertAbstract>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：certInfo?: CertInfo;  差异内容：certInfo?: CertInfo; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：credentialList?: Array<CredentialAbstract>;  差异内容：credentialList?: Array<CredentialAbstract>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：credential?: Credential;  差异内容：credential?: Credential; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：appUidList?: Array<string>;  差异内容：appUidList?: Array<string>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：uri?: string;  差异内容：uri?: string; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult；  API声明：outData?: Uint8Array;  差异内容：outData?: Uint8Array; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export enum CmKeyPurpose  差异内容： export enum CmKeyPurpose | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyPurpose；  API声明：CM\_KEY\_PURPOSE\_SIGN = 4  差异内容：CM\_KEY\_PURPOSE\_SIGN = 4 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyPurpose；  API声明：CM\_KEY\_PURPOSE\_VERIFY = 8  差异内容：CM\_KEY\_PURPOSE\_VERIFY = 8 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export enum CmKeyDigest  差异内容： export enum CmKeyDigest | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_NONE = 0  差异内容：CM\_DIGEST\_NONE = 0 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_MD5 = 1  差异内容：CM\_DIGEST\_MD5 = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_SHA1 = 2  差异内容：CM\_DIGEST\_SHA1 = 2 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_SHA224 = 3  差异内容：CM\_DIGEST\_SHA224 = 3 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_SHA256 = 4  差异内容：CM\_DIGEST\_SHA256 = 4 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_SHA384 = 5  差异内容：CM\_DIGEST\_SHA384 = 5 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyDigest；  API声明：CM\_DIGEST\_SHA512 = 6  差异内容：CM\_DIGEST\_SHA512 = 6 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export enum CmKeyPadding  差异内容： export enum CmKeyPadding | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyPadding；  API声明：CM\_PADDING\_NONE = 0  差异内容：CM\_PADDING\_NONE = 0 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyPadding；  API声明：CM\_PADDING\_PSS = 1  差异内容：CM\_PADDING\_PSS = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CmKeyPadding；  API声明：CM\_PADDING\_PKCS1\_V1\_5 = 2  差异内容：CM\_PADDING\_PKCS1\_V1\_5 = 2 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export interface CMSignatureSpec  差异内容： export interface CMSignatureSpec | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMSignatureSpec；  API声明：purpose: CmKeyPurpose;  差异内容：purpose: CmKeyPurpose; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMSignatureSpec；  API声明：padding?: CmKeyPadding;  差异内容：padding?: CmKeyPadding; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMSignatureSpec；  API声明：digest?: CmKeyDigest;  差异内容：digest?: CmKeyDigest; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明： export interface CMHandle  差异内容： export interface CMHandle | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMHandle；  API声明：handle: Uint8Array;  差异内容：handle: Uint8Array; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, callback: AsyncCallback<CMResult>): void;  差异内容：function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, callback: AsyncCallback<CMResult>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>;  差异内容：function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function uninstallPrivateCertificate(keyUri: string, callback: AsyncCallback<void>): void;  差异内容：function uninstallPrivateCertificate(keyUri: string, callback: AsyncCallback<void>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function uninstallPrivateCertificate(keyUri: string): Promise<void>;  差异内容：function uninstallPrivateCertificate(keyUri: string): Promise<void>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getPrivateCertificate(keyUri: string, callback: AsyncCallback<CMResult>): void;  差异内容：function getPrivateCertificate(keyUri: string, callback: AsyncCallback<CMResult>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getPrivateCertificate(keyUri: string): Promise<CMResult>;  差异内容：function getPrivateCertificate(keyUri: string): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void;  差异内容：function init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>;  差异内容：function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void;  差异内容：function update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function update(handle: Uint8Array, data: Uint8Array): Promise<void>;  差异内容：function update(handle: Uint8Array, data: Uint8Array): Promise<void>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function finish(handle: Uint8Array, callback: AsyncCallback<CMResult>): void;  差异内容：function finish(handle: Uint8Array, callback: AsyncCallback<CMResult>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function finish(handle: Uint8Array, signature: Uint8Array, callback: AsyncCallback<CMResult>): void;  差异内容：function finish(handle: Uint8Array, signature: Uint8Array, callback: AsyncCallback<CMResult>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function finish(handle: Uint8Array, signature?: Uint8Array): Promise<CMResult>;  差异内容：function finish(handle: Uint8Array, signature?: Uint8Array): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function abort(handle: Uint8Array, callback: AsyncCallback<void>): void;  差异内容：function abort(handle: Uint8Array, callback: AsyncCallback<void>): void; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function abort(handle: Uint8Array): Promise<void>;  差异内容：function abort(handle: Uint8Array): Promise<void>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getPublicCertificate(keyUri: string): Promise<CMResult>;  差异内容：function getPublicCertificate(keyUri: string): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function isAuthorizedApp(keyUri: string): Promise<boolean>;  差异内容：function isAuthorizedApp(keyUri: string): Promise<boolean>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getAllUserTrustedCertificates(): Promise<CMResult>;  差异内容：function getAllUserTrustedCertificates(): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getUserTrustedCertificate(certUri: string): Promise<CMResult>;  差异内容：function getUserTrustedCertificate(certUri: string): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
