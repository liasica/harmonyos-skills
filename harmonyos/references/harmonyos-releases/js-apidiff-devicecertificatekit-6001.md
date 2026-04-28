---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-6001
title: Device Certificate Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:2d11a42f6b7e835b1fe76bd6ac552d1bb5d39db3f611c4a4b6ba0fb203f88e01
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：certificateManager；  API声明：function getCertificateStorePath(property: CertStoreProperty): string;  差异内容：NA | 类名：certificateManager；  API声明：function getCertificateStorePath(property: CertStoreProperty): string;  差异内容：17500009 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertResult；  API声明：ERR\_PARAMETER\_CHECK\_FAILED = 19020003  差异内容：ERR\_PARAMETER\_CHECK\_FAILED = 19020003 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CMErrorCode；  API声明：CM\_ERROR\_STORE\_PATH\_NOT\_SUPPORTED = 17500009  差异内容：CM\_ERROR\_STORE\_PATH\_NOT\_SUPPORTED = 17500009 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：export enum CertAlgorithm  差异内容：export enum CertAlgorithm | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertAlgorithm；  API声明：INTERNATIONAL = 1  差异内容：INTERNATIONAL = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertAlgorithm；  API声明：SM = 2  差异内容：SM = 2 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：function openAuthorizeDialog(context: common.Context): Promise<string>;  差异内容：function openAuthorizeDialog(context: common.Context): Promise<string>; | api/@ohos.security.certManagerDialog.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CertStoreProperty；  API声明：certAlg?: CertAlgorithm;  差异内容：certAlg?: CertAlgorithm; | api/@ohos.security.certManager.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X509Cert；  API声明：getIssuerName(): DataBlob;  差异内容：getIssuerName(): DataBlob; | 类名：X509Cert；  API声明：getIssuerName(encodingType: EncodingType): string;  差异内容：getIssuerName(encodingType: EncodingType): string; | api/@ohos.security.cert.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X509Cert；  API声明：toString(): string;  差异内容：toString(): string; | 类名：X509Cert；  API声明：toString(encodingType: EncodingType): string;  差异内容：toString(encodingType: EncodingType): string; | api/@ohos.security.cert.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X509CRLEntry；  API声明：getCertIssuer(): DataBlob;  差异内容：getCertIssuer(): DataBlob; | 类名：X509CRLEntry；  API声明：getCertIssuer(encodingType: EncodingType): string;  差异内容：getCertIssuer(encodingType: EncodingType): string; | api/@ohos.security.cert.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X509CRL；  API声明：getIssuerName(): DataBlob;  差异内容：getIssuerName(): DataBlob; | 类名：X509CRL；  API声明：getIssuerName(encodingType: EncodingType): string;  差异内容：getIssuerName(encodingType: EncodingType): string; | api/@ohos.security.cert.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X509CRL；  API声明：toString(): string;  差异内容：toString(): string; | 类名：X509CRL；  API声明：toString(encodingType: EncodingType): string;  差异内容：toString(encodingType: EncodingType): string; | api/@ohos.security.cert.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X500DistinguishedName；  API声明：getName(): string;  差异内容：getName(): string; | 类名：X500DistinguishedName；  API声明：getName(encodingType: EncodingType): string;  差异内容：getName(encodingType: EncodingType): string; | api/@ohos.security.cert.d.ts |
