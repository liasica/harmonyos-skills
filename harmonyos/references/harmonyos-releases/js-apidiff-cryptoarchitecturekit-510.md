---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cryptoarchitecturekit-510
title: Crypto Architecture Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Crypto Architecture Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4375971d2d1d6f8c4ce6043eaf52757b94aec52773da18b1458f75fad2d2e453
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：PriKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：NA | 类名：PriKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：801 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PubKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：NA | 类名：PubKey；  API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number;  差异内容：801 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Mac；  API声明：init(key: SymKey, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Mac；  API声明：init(key: SymKey, callback: AsyncCallback<void>): void;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Mac；  API声明：init(key: SymKey): Promise<void>;  差异内容：NA | 类名：Mac；  API声明：init(key: SymKey): Promise<void>;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Mac；  API声明：initSync(key: SymKey): void;  差异内容：NA | 类名：Mac；  API声明：initSync(key: SymKey): void;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Mac；  API声明：update(input: DataBlob, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Mac；  API声明：update(input: DataBlob, callback: AsyncCallback<void>): void;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Mac；  API声明：update(input: DataBlob): Promise<void>;  差异内容：NA | 类名：Mac；  API声明：update(input: DataBlob): Promise<void>;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Mac；  API声明：updateSync(input: DataBlob): void;  差异内容：NA | 类名：Mac；  API声明：updateSync(input: DataBlob): void;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Md；  API声明：update(input: DataBlob, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Md；  API声明：update(input: DataBlob, callback: AsyncCallback<void>): void;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Md；  API声明：update(input: DataBlob): Promise<void>;  差异内容：NA | 类名：Md；  API声明：update(input: DataBlob): Promise<void>;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Md；  API声明：updateSync(input: DataBlob): void;  差异内容：NA | 类名：Md；  API声明：updateSync(input: DataBlob): void;  差异内容：17620001 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：function createMac(macSpec: MacSpec): Mac;  差异内容：function createMac(macSpec: MacSpec): Mac; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface KeyEncodingConfig  差异内容：interface KeyEncodingConfig | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KeyEncodingConfig；  API声明：password: string;  差异内容：password: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：KeyEncodingConfig；  API声明：cipherName: string;  差异内容：cipherName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface MacSpec  差异内容：interface MacSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：MacSpec；  API声明：algName: string;  差异内容：algName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface HmacSpec  差异内容：interface HmacSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：HmacSpec；  API声明：mdName: string;  差异内容：mdName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface CmacSpec  差异内容：interface CmacSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：CmacSpec；  API声明：cipherName: string;  差异内容：cipherName: string; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface ScryptSpec  差异内容：interface ScryptSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ScryptSpec；  API声明：passphrase: string | Uint8Array;  差异内容：passphrase: string | Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ScryptSpec；  API声明：salt: Uint8Array;  差异内容：salt: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ScryptSpec；  API声明：n: number;  差异内容：n: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ScryptSpec；  API声明：r: number;  差异内容：r: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ScryptSpec；  API声明：p: number;  差异内容：p: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ScryptSpec；  API声明：maxMemory: number;  差异内容：maxMemory: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：ScryptSpec；  API声明：keySize: number;  差异内容：keySize: number; | api/@ohos.security.cryptoFramework.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：PriKey；  API声明：getEncodedPem(format: string): string;  差异内容：getEncodedPem(format: string): string; | 类名：PriKey；  API声明：getEncodedPem(format: string, config: KeyEncodingConfig): string;  差异内容：getEncodedPem(format: string, config: KeyEncodingConfig): string; | api/@ohos.security.cryptoFramework.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：AsyKeyGenerator；  API声明：convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>;  差异内容：convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>; | 类名：AsyKeyGenerator；  API声明：convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>;  差异内容：convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>; | api/@ohos.security.cryptoFramework.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：AsyKeyGenerator；  API声明：convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair;  差异内容：convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair; | 类名：AsyKeyGenerator；  API声明：convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair;  差异内容：convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair; | api/@ohos.security.cryptoFramework.d.ts |
