---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cryptoarchitecturekit-hdc
title: Crypto Architecture Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Crypto Architecture Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6dc361b238526dc01ba879fd8d465dcc80aa4a25b4fdfb42e7f2f8ba731a13e0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明： export interface CipherResponse  差异内容：NA | 类名：global；  API声明： export interface CipherResponse  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherResponse；  API声明：text: string;  差异内容：NA | 类名：CipherResponse；  API声明：text: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：global；  API声明： export interface CipherRsaOptions  差异内容：NA | 类名：global；  API声明： export interface CipherRsaOptions  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherRsaOptions；  API声明：action: string;  差异内容：NA | 类名：CipherRsaOptions；  API声明：action: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherRsaOptions；  API声明：text: string;  差异内容：NA | 类名：CipherRsaOptions；  API声明：text: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherRsaOptions；  API声明：key: string;  差异内容：NA | 类名：CipherRsaOptions；  API声明：key: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherRsaOptions；  API声明：transformation?: string;  差异内容：NA | 类名：CipherRsaOptions；  API声明：transformation?: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherRsaOptions；  API声明：success: (data: CipherResponse) => void;  差异内容：NA | 类名：CipherRsaOptions；  API声明：success: (data: CipherResponse) => void;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherRsaOptions；  API声明：fail: (data: string, code: number) => void;  差异内容：NA | 类名：CipherRsaOptions；  API声明：fail: (data: string, code: number) => void;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherRsaOptions；  API声明：complete: () => void;  差异内容：NA | 类名：CipherRsaOptions；  API声明：complete: () => void;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：global；  API声明： export interface CipherAesOptions  差异内容：NA | 类名：global；  API声明： export interface CipherAesOptions  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：action: string;  差异内容：NA | 类名：CipherAesOptions；  API声明：action: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：text: string;  差异内容：NA | 类名：CipherAesOptions；  API声明：text: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：key: string;  差异内容：NA | 类名：CipherAesOptions；  API声明：key: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：transformation?: string;  差异内容：NA | 类名：CipherAesOptions；  API声明：transformation?: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：iv?: string;  差异内容：NA | 类名：CipherAesOptions；  API声明：iv?: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：ivOffset?: string;  差异内容：NA | 类名：CipherAesOptions；  API声明：ivOffset?: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：ivLen?: string;  差异内容：NA | 类名：CipherAesOptions；  API声明：ivLen?: string;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：success: (data: CipherResponse) => void;  差异内容：NA | 类名：CipherAesOptions；  API声明：success: (data: CipherResponse) => void;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：fail: (data: string, code: number) => void;  差异内容：NA | 类名：CipherAesOptions；  API声明：fail: (data: string, code: number) => void;  差异内容：11 | api/@system.cipher.d.ts |
| API废弃版本变更 | 类名：CipherAesOptions；  API声明：complete: () => void;  差异内容：NA | 类名：CipherAesOptions；  API声明：complete: () => void;  差异内容：11 | api/@system.cipher.d.ts |
| 错误码变更 | 类名：Key；  API声明：getEncoded(): DataBlob;  差异内容：NA | 类名：Key；  API声明：getEncoded(): DataBlob;  差异内容：17620001,17630001,801 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：Random；  API声明：generateRandom(len: number): Promise<DataBlob>;  差异内容：NA | 类名：Random；  API声明：generateRandom(len: number): Promise<DataBlob>;  差异内容：17620001,17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：Mac；  API声明：init(key: SymKey): Promise<void>;  差异内容：NA | 类名：Mac；  API声明：init(key: SymKey): Promise<void>;  差异内容：17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：Mac；  API声明：update(input: DataBlob): Promise<void>;  差异内容：NA | 类名：Mac；  API声明：update(input: DataBlob): Promise<void>;  差异内容：17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：Mac；  API声明：doFinal(): Promise<DataBlob>;  差异内容：NA | 类名：Mac；  API声明：doFinal(): Promise<DataBlob>;  差异内容：17620001,17630001 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：Md；  API声明：update(input: DataBlob): Promise<void>;  差异内容：NA | 类名：Md；  API声明：update(input: DataBlob): Promise<void>;  差异内容：17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：Md；  API声明：digest(): Promise<DataBlob>;  差异内容：NA | 类名：Md；  API声明：digest(): Promise<DataBlob>;  差异内容：17620001,17630001 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：cryptoFramework；  API声明：function createAsyKeyGenerator(algName: string): AsyKeyGenerator;  差异内容：401 | 类名：cryptoFramework；  API声明：function createAsyKeyGenerator(algName: string): AsyKeyGenerator;  差异内容：17620001,401,801 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：cryptoFramework；  API声明：function createCipher(transformation: string): Cipher;  差异内容：401,801 | 类名：cryptoFramework；  API声明：function createCipher(transformation: string): Cipher;  差异内容：17620001,401,801 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：cryptoFramework；  API声明：function createSign(algName: string): Sign;  差异内容：401 | 类名：cryptoFramework；  API声明：function createSign(algName: string): Sign;  差异内容：17620001,401,801 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：cryptoFramework；  API声明：function createVerify(algName: string): Verify;  差异内容：401 | 类名：cryptoFramework；  API声明：function createVerify(algName: string): Verify;  差异内容：17620001,401,801 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：cryptoFramework；  API声明：function createKeyAgreement(algName: string): KeyAgreement;  差异内容：401 | 类名：cryptoFramework；  API声明：function createKeyAgreement(algName: string): KeyAgreement;  差异内容：17620001,401,801 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：AsyKeyGenerator；  API声明：generateKeyPair(callback: AsyncCallback<KeyPair>): void;  差异内容：17620001,401 | 类名：AsyKeyGenerator；  API声明：generateKeyPair(callback: AsyncCallback<KeyPair>): void;  差异内容：17620001,17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：AsyKeyGenerator；  API声明：generateKeyPair(): Promise<KeyPair>;  差异内容：17620001,401 | 类名：AsyKeyGenerator；  API声明：generateKeyPair(): Promise<KeyPair>;  差异内容：17620001,17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void;  差异内容：17620001,401 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void;  差异内容：17620001,17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 错误码变更 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>;  差异内容：17620001,401 | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>;  差异内容：17620001,17630001,401 | api/@ohos.security.cryptoFramework.d.ts |
| 权限变更 | 类名：global；  API声明： export interface CipherResponse  差异内容：N/A | 类名：global；  API声明： export interface CipherResponse  差异内容：NA | api/@system.cipher.d.ts |
| 权限变更 | 类名：global；  API声明： export interface CipherRsaOptions  差异内容：N/A | 类名：global；  API声明： export interface CipherRsaOptions  差异内容：NA | api/@system.cipher.d.ts |
| 权限变更 | 类名：global；  API声明： export interface CipherAesOptions  差异内容：N/A | 类名：global；  API声明： export interface CipherAesOptions  差异内容：NA | api/@system.cipher.d.ts |
| 权限变更 | 类名：global；  API声明： export default class Cipher  差异内容：N/A | 类名：global；  API声明： export default class Cipher  差异内容：NA | api/@system.cipher.d.ts |
| 新增API | NA | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void;  差异内容：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGenerator；  API声明：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>;  差异内容：convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec | null, callback: AsyncCallback<void>): void;  差异内容：init(opMode: CryptoMode, key: Key, params: ParamsSpec | null, callback: AsyncCallback<void>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec | null): Promise<void>;  差异内容：init(opMode: CryptoMode, key: Key, params: ParamsSpec | null): Promise<void>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：doFinal(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void;  差异内容：doFinal(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：doFinal(data: DataBlob | null): Promise<DataBlob>;  差异内容：doFinal(data: DataBlob | null): Promise<DataBlob>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void;  差异内容：sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：sign(data: DataBlob | null): Promise<DataBlob>;  差异内容：sign(data: DataBlob | null): Promise<DataBlob>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：verify(data: DataBlob | null, signatureData: DataBlob, callback: AsyncCallback<boolean>): void;  差异内容：verify(data: DataBlob | null, signatureData: DataBlob, callback: AsyncCallback<boolean>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：verify(data: DataBlob | null, signatureData: DataBlob): Promise<boolean>;  差异内容：verify(data: DataBlob | null, signatureData: DataBlob): Promise<boolean>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PriKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PriKey；  API声明：getEncodedDer(format: string): DataBlob;  差异内容：getEncodedDer(format: string): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PriKey；  API声明：getEncodedPem(format: string): string;  差异内容：getEncodedPem(format: string): string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PubKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PubKey；  API声明：getEncodedDer(format: string): DataBlob;  差异内容：getEncodedDer(format: string): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PubKey；  API声明：getEncodedPem(format: string): string;  差异内容：getEncodedPem(format: string): string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Random；  API声明：generateRandomSync(len: number): DataBlob;  差异内容：generateRandomSync(len: number): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Random；  API声明：readonly algName: string;  差异内容：readonly algName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGenerator；  API声明：generateKeyPairSync(): KeyPair;  差异内容：generateKeyPairSync(): KeyPair; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGenerator；  API声明：convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair;  差异内容：convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGenerator；  API声明：convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>;  差异内容：convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGenerator；  API声明：convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair;  差异内容：convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SymKeyGenerator；  API声明：generateSymKeySync(): SymKey;  差异内容：generateSymKeySync(): SymKey; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SymKeyGenerator；  API声明：convertKeySync(key: DataBlob): SymKey;  差异内容：convertKeySync(key: DataBlob): SymKey; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Mac；  API声明：initSync(key: SymKey): void;  差异内容：initSync(key: SymKey): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Mac；  API声明：updateSync(input: DataBlob): void;  差异内容：updateSync(input: DataBlob): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Mac；  API声明：doFinalSync(): DataBlob;  差异内容：doFinalSync(): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Md；  API声明：updateSync(input: DataBlob): void;  差异内容：updateSync(input: DataBlob): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Md；  API声明：digestSync(): DataBlob;  差异内容：digestSync(): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： enum CipherSpecItem  差异内容： enum CipherSpecItem | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：CipherSpecItem；  API声明：OAEP\_MD\_NAME\_STR = 100  差异内容：OAEP\_MD\_NAME\_STR = 100 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：CipherSpecItem；  API声明：OAEP\_MGF\_NAME\_STR = 101  差异内容：OAEP\_MGF\_NAME\_STR = 101 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：CipherSpecItem；  API声明：OAEP\_MGF1\_MD\_STR = 102  差异内容：OAEP\_MGF1\_MD\_STR = 102 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：CipherSpecItem；  API声明：OAEP\_MGF1\_PSRC\_UINT8ARR = 103  差异内容：OAEP\_MGF1\_PSRC\_UINT8ARR = 103 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：CipherSpecItem；  API声明：SM2\_MD\_NAME\_STR = 104  差异内容：SM2\_MD\_NAME\_STR = 104 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： enum SignSpecItem  差异内容： enum SignSpecItem | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：PSS\_MD\_NAME\_STR = 100  差异内容：PSS\_MD\_NAME\_STR = 100 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：PSS\_MGF\_NAME\_STR = 101  差异内容：PSS\_MGF\_NAME\_STR = 101 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：PSS\_MGF1\_MD\_STR = 102  差异内容：PSS\_MGF1\_MD\_STR = 102 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：PSS\_SALT\_LEN\_NUM = 103  差异内容：PSS\_SALT\_LEN\_NUM = 103 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：PSS\_TRAILER\_FIELD\_NUM = 104  差异内容：PSS\_TRAILER\_FIELD\_NUM = 104 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignSpecItem；  API声明：SM2\_USER\_ID\_UINT8ARR = 105  差异内容：SM2\_USER\_ID\_UINT8ARR = 105 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：initSync(opMode: CryptoMode, key: Key, params: ParamsSpec | null): void;  差异内容：initSync(opMode: CryptoMode, key: Key, params: ParamsSpec | null): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：updateSync(data: DataBlob): DataBlob;  差异内容：updateSync(data: DataBlob): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：doFinalSync(data: DataBlob | null): DataBlob;  差异内容：doFinalSync(data: DataBlob | null): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：setCipherSpec(itemType: CipherSpecItem, itemValue: Uint8Array): void;  差异内容：setCipherSpec(itemType: CipherSpecItem, itemValue: Uint8Array): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Cipher；  API声明：getCipherSpec(itemType: CipherSpecItem): string | Uint8Array;  差异内容：getCipherSpec(itemType: CipherSpecItem): string | Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：initSync(priKey: PriKey): void;  差异内容：initSync(priKey: PriKey): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：updateSync(data: DataBlob): void;  差异内容：updateSync(data: DataBlob): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：signSync(data: DataBlob | null): DataBlob;  差异内容：signSync(data: DataBlob | null): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number): void;  差异内容：setSignSpec(itemType: SignSpecItem, itemValue: number): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Sign；  API声明：getSignSpec(itemType: SignSpecItem): string | number;  差异内容：getSignSpec(itemType: SignSpecItem): string | number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：initSync(pubKey: PubKey): void;  差异内容：initSync(pubKey: PubKey): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：updateSync(data: DataBlob): void;  差异内容：updateSync(data: DataBlob): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：verifySync(data: DataBlob | null, signatureData: DataBlob): boolean;  差异内容：verifySync(data: DataBlob | null, signatureData: DataBlob): boolean; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：recover(signatureData: DataBlob): Promise<DataBlob | null>;  差异内容：recover(signatureData: DataBlob): Promise<DataBlob | null>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：recoverSync(signatureData: DataBlob): DataBlob | null;  差异内容：recoverSync(signatureData: DataBlob): DataBlob | null; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number): void;  差异内容：setVerifySpec(itemType: SignSpecItem, itemValue: number): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void;  差异内容：setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Verify；  API声明：getVerifySpec(itemType: SignSpecItem): string | number;  差异内容：getVerifySpec(itemType: SignSpecItem): string | number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KeyAgreement；  API声明：generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob;  差异内容：generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： enum AsyKeySpecItem  差异内容： enum AsyKeySpecItem | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DSA\_P\_BN = 101  差异内容：DSA\_P\_BN = 101 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DSA\_Q\_BN = 102  差异内容：DSA\_Q\_BN = 102 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DSA\_G\_BN = 103  差异内容：DSA\_G\_BN = 103 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DSA\_SK\_BN = 104  差异内容：DSA\_SK\_BN = 104 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DSA\_PK\_BN = 105  差异内容：DSA\_PK\_BN = 105 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_FP\_P\_BN = 201  差异内容：ECC\_FP\_P\_BN = 201 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_A\_BN = 202  差异内容：ECC\_A\_BN = 202 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_B\_BN = 203  差异内容：ECC\_B\_BN = 203 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_G\_X\_BN = 204  差异内容：ECC\_G\_X\_BN = 204 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_G\_Y\_BN = 205  差异内容：ECC\_G\_Y\_BN = 205 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_N\_BN = 206  差异内容：ECC\_N\_BN = 206 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_H\_NUM = 207  差异内容：ECC\_H\_NUM = 207 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_SK\_BN = 208  差异内容：ECC\_SK\_BN = 208 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_PK\_X\_BN = 209  差异内容：ECC\_PK\_X\_BN = 209 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_PK\_Y\_BN = 210  差异内容：ECC\_PK\_Y\_BN = 210 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_FIELD\_TYPE\_STR = 211  差异内容：ECC\_FIELD\_TYPE\_STR = 211 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_FIELD\_SIZE\_NUM = 212  差异内容：ECC\_FIELD\_SIZE\_NUM = 212 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ECC\_CURVE\_NAME\_STR = 213  差异内容：ECC\_CURVE\_NAME\_STR = 213 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：RSA\_N\_BN = 301  差异内容：RSA\_N\_BN = 301 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：RSA\_SK\_BN = 302  差异内容：RSA\_SK\_BN = 302 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：RSA\_PK\_BN = 303  差异内容：RSA\_PK\_BN = 303 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DH\_P\_BN = 401  差异内容：DH\_P\_BN = 401 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DH\_G\_BN = 402  差异内容：DH\_G\_BN = 402 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DH\_L\_NUM = 403  差异内容：DH\_L\_NUM = 403 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DH\_SK\_BN = 404  差异内容：DH\_SK\_BN = 404 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：DH\_PK\_BN = 405  差异内容：DH\_PK\_BN = 405 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ED25519\_SK\_BN = 501  差异内容：ED25519\_SK\_BN = 501 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：ED25519\_PK\_BN = 502  差异内容：ED25519\_PK\_BN = 502 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：X25519\_SK\_BN = 601  差异内容：X25519\_SK\_BN = 601 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecItem；  API声明：X25519\_PK\_BN = 602  差异内容：X25519\_PK\_BN = 602 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： enum AsyKeySpecType  差异内容： enum AsyKeySpecType | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecType；  API声明：COMMON\_PARAMS\_SPEC = 0  差异内容：COMMON\_PARAMS\_SPEC = 0 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecType；  API声明：PRIVATE\_KEY\_SPEC = 1  差异内容：PRIVATE\_KEY\_SPEC = 1 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecType；  API声明：PUBLIC\_KEY\_SPEC = 2  差异内容：PUBLIC\_KEY\_SPEC = 2 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpecType；  API声明：KEY\_PAIR\_SPEC = 3  差异内容：KEY\_PAIR\_SPEC = 3 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface AsyKeySpec  差异内容： interface AsyKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpec；  API声明：algName: string;  差异内容：algName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeySpec；  API声明：specType: AsyKeySpecType;  差异内容：specType: AsyKeySpecType; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface DSACommonParamsSpec  差异内容： interface DSACommonParamsSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSACommonParamsSpec；  API声明：p: bigint;  差异内容：p: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSACommonParamsSpec；  API声明：q: bigint;  差异内容：q: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSACommonParamsSpec；  API声明：g: bigint;  差异内容：g: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface DSAPubKeySpec  差异内容： interface DSAPubKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSAPubKeySpec；  API声明：params: DSACommonParamsSpec;  差异内容：params: DSACommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSAPubKeySpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface DSAKeyPairSpec  差异内容： interface DSAKeyPairSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSAKeyPairSpec；  API声明：params: DSACommonParamsSpec;  差异内容：params: DSACommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSAKeyPairSpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DSAKeyPairSpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ECField  差异内容： interface ECField | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECField；  API声明：fieldType: string;  差异内容：fieldType: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ECFieldFp  差异内容： interface ECFieldFp | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECFieldFp；  API声明：p: bigint;  差异内容：p: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface Point  差异内容： interface Point | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Point；  API声明：x: bigint;  差异内容：x: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Point；  API声明：y: bigint;  差异内容：y: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ECCCommonParamsSpec  差异内容： interface ECCCommonParamsSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCCommonParamsSpec；  API声明：field: ECField;  差异内容：field: ECField; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCCommonParamsSpec；  API声明：a: bigint;  差异内容：a: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCCommonParamsSpec；  API声明：b: bigint;  差异内容：b: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCCommonParamsSpec；  API声明：g: Point;  差异内容：g: Point; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCCommonParamsSpec；  API声明：n: bigint;  差异内容：n: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCCommonParamsSpec；  API声明：h: number;  差异内容：h: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ECCPriKeySpec  差异内容： interface ECCPriKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCPriKeySpec；  API声明：params: ECCCommonParamsSpec;  差异内容：params: ECCCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCPriKeySpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ECCPubKeySpec  差异内容： interface ECCPubKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCPubKeySpec；  API声明：params: ECCCommonParamsSpec;  差异内容：params: ECCCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCPubKeySpec；  API声明：pk: Point;  差异内容：pk: Point; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ECCKeyPairSpec  差异内容： interface ECCKeyPairSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCKeyPairSpec；  API声明：params: ECCCommonParamsSpec;  差异内容：params: ECCCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCKeyPairSpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCKeyPairSpec；  API声明：pk: Point;  差异内容：pk: Point; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： class ECCKeyUtil  差异内容： class ECCKeyUtil | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCKeyUtil；  API声明：static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec;  差异内容：static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCKeyUtil；  API声明：static convertPoint(curveName: string, encodedPoint: Uint8Array): Point;  差异内容：static convertPoint(curveName: string, encodedPoint: Uint8Array): Point; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ECCKeyUtil；  API声明：static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array;  差异内容：static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface DHCommonParamsSpec  差异内容： interface DHCommonParamsSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHCommonParamsSpec；  API声明：p: bigint;  差异内容：p: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHCommonParamsSpec；  API声明：g: bigint;  差异内容：g: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHCommonParamsSpec；  API声明：l: number;  差异内容：l: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface DHPriKeySpec  差异内容： interface DHPriKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHPriKeySpec；  API声明：params: DHCommonParamsSpec;  差异内容：params: DHCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHPriKeySpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface DHPubKeySpec  差异内容： interface DHPubKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHPubKeySpec；  API声明：params: DHCommonParamsSpec;  差异内容：params: DHCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHPubKeySpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface DHKeyPairSpec  差异内容： interface DHKeyPairSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHKeyPairSpec；  API声明：params: DHCommonParamsSpec;  差异内容：params: DHCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHKeyPairSpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHKeyPairSpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： class DHKeyUtil  差异内容： class DHKeyUtil | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：DHKeyUtil；  API声明：static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec;  差异内容：static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ED25519PriKeySpec  差异内容： interface ED25519PriKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ED25519PriKeySpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ED25519PubKeySpec  差异内容： interface ED25519PubKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ED25519PubKeySpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface ED25519KeyPairSpec  差异内容： interface ED25519KeyPairSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ED25519KeyPairSpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ED25519KeyPairSpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface X25519PriKeySpec  差异内容： interface X25519PriKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：X25519PriKeySpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface X25519PubKeySpec  差异内容： interface X25519PubKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：X25519PubKeySpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface X25519KeyPairSpec  差异内容： interface X25519KeyPairSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：X25519KeyPairSpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：X25519KeyPairSpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface RSACommonParamsSpec  差异内容： interface RSACommonParamsSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：RSACommonParamsSpec；  API声明：n: bigint;  差异内容：n: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface RSAPubKeySpec  差异内容： interface RSAPubKeySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：RSAPubKeySpec；  API声明：params: RSACommonParamsSpec;  差异内容：params: RSACommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：RSAPubKeySpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface RSAKeyPairSpec  差异内容： interface RSAKeyPairSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：RSAKeyPairSpec；  API声明：params: RSACommonParamsSpec;  差异内容：params: RSACommonParamsSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：RSAKeyPairSpec；  API声明：sk: bigint;  差异内容：sk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：RSAKeyPairSpec；  API声明：pk: bigint;  差异内容：pk: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface AsyKeyGeneratorBySpec  差异内容： interface AsyKeyGeneratorBySpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generateKeyPair(callback: AsyncCallback<KeyPair>): void;  差异内容：generateKeyPair(callback: AsyncCallback<KeyPair>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generateKeyPair(): Promise<KeyPair>;  差异内容：generateKeyPair(): Promise<KeyPair>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generateKeyPairSync(): KeyPair;  差异内容：generateKeyPairSync(): KeyPair; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generatePriKey(callback: AsyncCallback<PriKey>): void;  差异内容：generatePriKey(callback: AsyncCallback<PriKey>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generatePriKey(): Promise<PriKey>;  差异内容：generatePriKey(): Promise<PriKey>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generatePriKeySync(): PriKey;  差异内容：generatePriKeySync(): PriKey; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generatePubKey(callback: AsyncCallback<PubKey>): void;  差异内容：generatePubKey(callback: AsyncCallback<PubKey>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generatePubKey(): Promise<PubKey>;  差异内容：generatePubKey(): Promise<PubKey>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：generatePubKeySync(): PubKey;  差异内容：generatePubKeySync(): PubKey; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyGeneratorBySpec；  API声明：readonly algName: string;  差异内容：readonly algName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：function createAsyKeyGeneratorBySpec(asyKeySpec: AsyKeySpec): AsyKeyGeneratorBySpec;  差异内容：function createAsyKeyGeneratorBySpec(asyKeySpec: AsyKeySpec): AsyKeyGeneratorBySpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface KdfSpec  差异内容： interface KdfSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KdfSpec；  API声明：algName: string;  差异内容：algName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface PBKDF2Spec  差异内容： interface PBKDF2Spec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PBKDF2Spec；  API声明：password: string | Uint8Array;  差异内容：password: string | Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PBKDF2Spec；  API声明：salt: Uint8Array;  差异内容：salt: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PBKDF2Spec；  API声明：iterations: number;  差异内容：iterations: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PBKDF2Spec；  API声明：keySize: number;  差异内容：keySize: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface HKDFSpec  差异内容： interface HKDFSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：HKDFSpec；  API声明：key: string | Uint8Array;  差异内容：key: string | Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：HKDFSpec；  API声明：salt: Uint8Array;  差异内容：salt: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：HKDFSpec；  API声明：info: Uint8Array;  差异内容：info: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：HKDFSpec；  API声明：keySize: number;  差异内容：keySize: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface Kdf  差异内容： interface Kdf | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kdf；  API声明：generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void;  差异内容：generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kdf；  API声明：generateSecret(params: KdfSpec): Promise<DataBlob>;  差异内容：generateSecret(params: KdfSpec): Promise<DataBlob>; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kdf；  API声明：generateSecretSync(params: KdfSpec): DataBlob;  差异内容：generateSecretSync(params: KdfSpec): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Kdf；  API声明：readonly algName: string;  差异内容：readonly algName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：function createKdf(algName: string): Kdf;  差异内容：function createKdf(algName: string): Kdf; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： interface SM2CipherTextSpec  差异内容： interface SM2CipherTextSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SM2CipherTextSpec；  API声明：xCoordinate: bigint;  差异内容：xCoordinate: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SM2CipherTextSpec；  API声明：yCoordinate: bigint;  差异内容：yCoordinate: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SM2CipherTextSpec；  API声明：cipherTextData: Uint8Array;  差异内容：cipherTextData: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SM2CipherTextSpec；  API声明：hashData: Uint8Array;  差异内容：hashData: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明： class SM2CryptoUtil  差异内容： class SM2CryptoUtil | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SM2CryptoUtil；  API声明：static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob;  差异内容：static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SM2CryptoUtil；  API声明：static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec;  差异内容：static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec; | api/@ohos.security.cryptoFramework.d.ts |
