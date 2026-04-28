---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-6011
title: Device Certificate Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:58+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e1919d2990d1e7ec2381b0e8a3d64ffe2cdbe530fcd20b92d6e0f4a3a13d4873
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：cert；  API声明：function parsePkcs12(data: Uint8Array, password: string): Promise<Pkcs12Data>;  差异内容：function parsePkcs12(data: Uint8Array, password: string): Promise<Pkcs12Data>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum PbesEncryptionAlgorithm  差异内容：enum PbesEncryptionAlgorithm | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PbesEncryptionAlgorithm；  API声明：AES\_128\_CBC = 0  差异内容：AES\_128\_CBC = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PbesEncryptionAlgorithm；  API声明：AES\_192\_CBC = 1  差异内容：AES\_192\_CBC = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PbesEncryptionAlgorithm；  API声明：AES\_256\_CBC = 2  差异内容：AES\_256\_CBC = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface PbesParams  差异内容：interface PbesParams | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PbesParams；  API声明：saltLen?: number;  差异内容：saltLen?: number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PbesParams；  API声明：iterations?: number;  差异内容：iterations?: number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：PbesParams；  API声明：encryptionAlgorithm?: PbesEncryptionAlgorithm;  差异内容：encryptionAlgorithm?: PbesEncryptionAlgorithm; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：enum Pkcs12MacDigestAlgorithm  差异内容：enum Pkcs12MacDigestAlgorithm | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12MacDigestAlgorithm；  API声明：SHA256 = 0  差异内容：SHA256 = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12MacDigestAlgorithm；  API声明：SHA384 = 1  差异内容：SHA384 = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12MacDigestAlgorithm；  API声明：SHA512 = 2  差异内容：SHA512 = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：interface Pkcs12CreationConfig  差异内容：interface Pkcs12CreationConfig | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12CreationConfig；  API声明：password: string;  差异内容：password: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12CreationConfig；  API声明：keyEncParams?: PbesParams;  差异内容：keyEncParams?: PbesParams; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12CreationConfig；  API声明：encryptCert?: boolean;  差异内容：encryptCert?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12CreationConfig；  API声明：certEncParams?: PbesParams;  差异内容：certEncParams?: PbesParams; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12CreationConfig；  API声明：macSaltLen?: number;  差异内容：macSaltLen?: number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12CreationConfig；  API声明：macIterations?: number;  差异内容：macIterations?: number; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：Pkcs12CreationConfig；  API声明：macDigestAlgorithm?: Pkcs12MacDigestAlgorithm;  差异内容：macDigestAlgorithm?: Pkcs12MacDigestAlgorithm; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createPkcs12Sync(data: Pkcs12Data, config: Pkcs12CreationConfig): Uint8Array;  差异内容：function createPkcs12Sync(data: Pkcs12Data, config: Pkcs12CreationConfig): Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明：function createPkcs12(data: Pkcs12Data, config: Pkcs12CreationConfig): Promise<Uint8Array>;  差异内容：function createPkcs12(data: Pkcs12Data, config: Pkcs12CreationConfig): Promise<Uint8Array>; | api/@ohos.security.cert.d.ts |
