---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cryptoarchitecturekit-6001
title: Crypto Architecture Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Crypto Architecture Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:37+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fba02e10bb97ea1023020829173adfe07dd5510bbaaf2207d6c3742bd2b02ecf
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：Result；  API声明：ERR\_PARAMETER\_CHECK\_FAILED = 17620003  差异内容：ERR\_PARAMETER\_CHECK\_FAILED = 17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：interface EccSignatureSpec  差异内容：interface EccSignatureSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：EccSignatureSpec；  API声明：r: bigint;  差异内容：r: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：EccSignatureSpec；  API声明：s: bigint;  差异内容：s: bigint; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework；  API声明：class SignatureUtils  差异内容：class SignatureUtils | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignatureUtils；  API声明：static genEccSignatureSpec(data: Uint8Array): EccSignatureSpec;  差异内容：static genEccSignatureSpec(data: Uint8Array): EccSignatureSpec; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：SignatureUtils；  API声明：static genEccSignature(spec: EccSignatureSpec): Uint8Array;  差异内容：static genEccSignature(spec: EccSignatureSpec): Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
