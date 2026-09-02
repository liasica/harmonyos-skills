---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cryptoarchitecturekit-7001
title: Crypto Architecture Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Crypto Architecture Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:05a58e0ce156ef3b6897b27e8335c0636b9e30d955ba89b1919aeb62ef345add
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：PriKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：NA | 类名：PriKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PriKey；  API声明：getEncodedDer(format: string): DataBlob;  差异内容：NA | 类名：PriKey；  API声明：getEncodedDer(format: string): DataBlob;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PriKey；  API声明：getEncodedPem(format: string): string;  差异内容：NA | 类名：PriKey；  API声明：getEncodedPem(format: string): string;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PubKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：NA | 类名：PubKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PubKey；  API声明：getEncodedPem(format: string): string;  差异内容：NA | 类名：PubKey；  API声明：getEncodedPem(format: string): string;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void;  差异内容：NA | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void;  差异内容：NA | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>;  差异内容：NA | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>;  差异内容：NA | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator；  API声明：convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair;  差异内容：NA | 类名：AsyKeyGenerator；  API声明：convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator；  API声明：convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>;  差异内容：NA | 类名：AsyKeyGenerator；  API声明：convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator；  API声明：convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair;  差异内容：NA | 类名：AsyKeyGenerator；  API声明：convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator；  API声明：generateSymKey(callback: AsyncCallback<SymKey>): void;  差异内容：NA | 类名：SymKeyGenerator；  API声明：generateSymKey(callback: AsyncCallback<SymKey>): void;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator；  API声明：generateSymKey(): Promise<SymKey>;  差异内容：NA | 类名：SymKeyGenerator；  API声明：generateSymKey(): Promise<SymKey>;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator；  API声明：generateSymKeySync(): SymKey;  差异内容：NA | 类名：SymKeyGenerator；  API声明：generateSymKeySync(): SymKey;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator；  API声明：convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void;  差异内容：NA | 类名：SymKeyGenerator；  API声明：convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator；  API声明：convertKey(key: DataBlob): Promise<SymKey>;  差异内容：NA | 类名：SymKeyGenerator；  API声明：convertKey(key: DataBlob): Promise<SymKey>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator；  API声明：convertKeySync(key: DataBlob): SymKey;  差异内容：NA | 类名：SymKeyGenerator；  API声明：convertKeySync(key: DataBlob): SymKey;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：init(priKey: PriKey, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Sign；  API声明：init(priKey: PriKey, callback: AsyncCallback<void>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：init(priKey: PriKey): Promise<void>;  差异内容：NA | 类名：Sign；  API声明：init(priKey: PriKey): Promise<void>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：initSync(priKey: PriKey): void;  差异内容：NA | 类名：Sign；  API声明：initSync(priKey: PriKey): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：update(data: DataBlob, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Sign；  API声明：update(data: DataBlob, callback: AsyncCallback<void>): void;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：update(data: DataBlob): Promise<void>;  差异内容：NA | 类名：Sign；  API声明：update(data: DataBlob): Promise<void>;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：updateSync(data: DataBlob): void;  差异内容：NA | 类名：Sign；  API声明：updateSync(data: DataBlob): void;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void;  差异内容：NA | 类名：Sign；  API声明：sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void;  差异内容：NA | 类名：Sign；  API声明：sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：sign(data: DataBlob): Promise<DataBlob>;  差异内容：NA | 类名：Sign；  API声明：sign(data: DataBlob): Promise<DataBlob>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：sign(data: DataBlob | null): Promise<DataBlob>;  差异内容：NA | 类名：Sign；  API声明：sign(data: DataBlob | null): Promise<DataBlob>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：signSync(data: DataBlob | null): DataBlob;  差异内容：NA | 类名：Sign；  API声明：signSync(data: DataBlob | null): DataBlob;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number): void;  差异内容：NA | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign；  API声明：getSignSpec(itemType: SignSpecItem): string | number;  差异内容：NA | 类名：Sign；  API声明：getSignSpec(itemType: SignSpecItem): string | number;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：init(pubKey: PubKey, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Verify；  API声明：init(pubKey: PubKey, callback: AsyncCallback<void>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：init(pubKey: PubKey): Promise<void>;  差异内容：NA | 类名：Verify；  API声明：init(pubKey: PubKey): Promise<void>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：initSync(pubKey: PubKey): void;  差异内容：NA | 类名：Verify；  API声明：initSync(pubKey: PubKey): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：update(data: DataBlob, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Verify；  API声明：update(data: DataBlob, callback: AsyncCallback<void>): void;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：update(data: DataBlob): Promise<void>;  差异内容：NA | 类名：Verify；  API声明：update(data: DataBlob): Promise<void>;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：updateSync(data: DataBlob): void;  差异内容：NA | 类名：Verify；  API声明：updateSync(data: DataBlob): void;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：verify(data: DataBlob, signatureData: DataBlob, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：Verify；  API声明：verify(data: DataBlob, signatureData: DataBlob, callback: AsyncCallback<boolean>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：verify(data: DataBlob | null, signatureData: DataBlob, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：Verify；  API声明：verify(data: DataBlob | null, signatureData: DataBlob, callback: AsyncCallback<boolean>): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：verify(data: DataBlob, signatureData: DataBlob): Promise<boolean>;  差异内容：NA | 类名：Verify；  API声明：verify(data: DataBlob, signatureData: DataBlob): Promise<boolean>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：verify(data: DataBlob | null, signatureData: DataBlob): Promise<boolean>;  差异内容：NA | 类名：Verify；  API声明：verify(data: DataBlob | null, signatureData: DataBlob): Promise<boolean>;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：verifySync(data: DataBlob | null, signatureData: DataBlob): boolean;  差异内容：NA | 类名：Verify；  API声明：verifySync(data: DataBlob | null, signatureData: DataBlob): boolean;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：recover(signatureData: DataBlob): Promise<DataBlob | null>;  差异内容：NA | 类名：Verify；  API声明：recover(signatureData: DataBlob): Promise<DataBlob | null>;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：recoverSync(signatureData: DataBlob): DataBlob | null;  差异内容：NA | 类名：Verify；  API声明：recoverSync(signatureData: DataBlob): DataBlob | null;  差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number): void;  差异内容：NA | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number): void;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify；  API声明：getVerifySpec(itemType: SignSpecItem): string | number;  差异内容：NA | 类名：Verify；  API声明：getVerifySpec(itemType: SignSpecItem): string | number;  差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Result；  API声明：ERR\_INVALID\_CALL = 17620004  差异内容：ERR\_INVALID\_CALL = 17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface AeadParamsSpec  差异内容：interface AeadParamsSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AeadParamsSpec；  API声明：nonce: Uint8Array;  差异内容：nonce: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AeadParamsSpec；  API声明：authenticatedData?: Uint8Array;  差异内容：authenticatedData?: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AeadParamsSpec；  API声明：tagLen?: number;  差异内容：tagLen?: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Key；  API声明：getKeySize(): number;  差异内容：getKeySize(): number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PriKey；  API声明：getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>;  差异内容：getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PriKey；  API声明：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array;  差异内容：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PubKey；  API声明：getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>;  差异内容：getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PubKey；  API声明：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array;  差异内容：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：enum AsyKeyDataItem  差异内容：enum AsyKeyDataItem | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：EC\_PRIVATE\_K = 6  差异内容：EC\_PRIVATE\_K = 6 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：EC\_PRIVATE\_04\_X\_Y\_K = 7  差异内容：EC\_PRIVATE\_04\_X\_Y\_K = 7 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：EC\_PUBLIC\_X\_Y = 8  差异内容：EC\_PUBLIC\_X\_Y = 8 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：EC\_PUBLIC\_04\_X\_Y = 9  差异内容：EC\_PUBLIC\_04\_X\_Y = 9 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem；  API声明：EC\_PUBLIC\_COMPRESS\_X = 10  差异内容：EC\_PUBLIC\_COMPRESS\_X = 10 | api/@ohos.security.cryptoFramework.d.ts |
