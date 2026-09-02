---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cryptoarchitecturekit-7002
title: Crypto Architecture Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Crypto Architecture Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:bd050b6010fe94127ffc0d863550dcd66e6f847fb1261ffb927bc8df1b868d25
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：PubKey；  API声明：getEncodedDer(format: string): DataBlob;  差异内容：NA | 类名：PubKey；  API声明：getEncodedDer(format: string): DataBlob;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：NA | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：17620002,17620003,17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：NA | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：17620002,17620003,17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：ML\_DSA\_DETERMINISTIC\_BOOL = 106  差异内容：ML\_DSA\_DETERMINISTIC\_BOOL = 106 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：ML\_DSA\_MU\_BOOL = 107  差异内容：ML\_DSA\_MU\_BOOL = 107 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：ML\_DSA\_CONTEXT\_UINT8ARR = 108  差异内容：ML\_DSA\_CONTEXT\_UINT8ARR = 108 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：ML\_DSA\_PRIVATE\_SEED = 0  差异内容：ML\_DSA\_PRIVATE\_SEED = 0 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：ML\_DSA\_PRIVATE\_RAW = 1  差异内容：ML\_DSA\_PRIVATE\_RAW = 1 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：ML\_DSA\_PUBLIC\_RAW = 2  差异内容：ML\_DSA\_PUBLIC\_RAW = 2 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：ML\_KEM\_PRIVATE\_SEED = 3  差异内容：ML\_KEM\_PRIVATE\_SEED = 3 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：ML\_KEM\_PRIVATE\_RAW = 4  差异内容：ML\_KEM\_PRIVATE\_RAW = 4 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：ML\_KEM\_PUBLIC\_RAW = 5  差异内容：ML\_KEM\_PUBLIC\_RAW = 5 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：enum KemAlgNameId  差异内容：enum KemAlgNameId | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KemAlgNameId；  API声明：ML\_KEM\_512 = 0  差异内容：ML\_KEM\_512 = 0 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KemAlgNameId；  API声明：ML\_KEM\_768 = 1  差异内容：ML\_KEM\_768 = 1 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KemAlgNameId；  API声明：ML\_KEM\_1024 = 2  差异内容：ML\_KEM\_1024 = 2 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface KemEncapResult  差异内容：interface KemEncapResult | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KemEncapResult；  API声明：sharedSecret: Uint8Array;  差异内容：sharedSecret: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KemEncapResult；  API声明：wrappedKey: Uint8Array;  差异内容：wrappedKey: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface Kem  差异内容：interface Kem | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kem；  API声明：encapsulate(pubKey: PubKey, ikme: Uint8Array | null): Promise<KemEncapResult>;  差异内容：encapsulate(pubKey: PubKey, ikme: Uint8Array | null): Promise<KemEncapResult>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kem；  API声明：encapsulateSync(pubKey: PubKey, ikme: Uint8Array | null): KemEncapResult;  差异内容：encapsulateSync(pubKey: PubKey, ikme: Uint8Array | null): KemEncapResult; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kem；  API声明：decapsulate(priKey: PriKey, wrappedKey: Uint8Array): Promise<Uint8Array>;  差异内容：decapsulate(priKey: PriKey, wrappedKey: Uint8Array): Promise<Uint8Array>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kem；  API声明：decapsulateSync(priKey: PriKey, wrappedKey: Uint8Array): Uint8Array;  差异内容：decapsulateSync(priKey: PriKey, wrappedKey: Uint8Array): Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：function createKem(algNameId: KemAlgNameId): Kem;  差异内容：function createKem(algNameId: KemAlgNameId): Kem; | api/@ohos.security.cryptoFramework.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void; | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array | boolean): void;  差异内容：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array | boolean): void; | api/@ohos.security.cryptoFramework.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void; | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array | boolean): void;  差异内容：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array | boolean): void; | api/@ohos.security.cryptoFramework.d.ts |
