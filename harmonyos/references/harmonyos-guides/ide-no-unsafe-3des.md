---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-unsafe-3des
title: @security/no-unsafe-3des
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-3des
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:56+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:34aa730f2dc4b865115603de0168b2c381a0e21e7ef8d28d0522f893e851aa6a
---

该规则禁止使用不安全的3DES加密模式，例如3DES|ECB。建议使用安全的3DES加密模式，例如3DES|CBC。详情参考[3DES加密模式](crypto-sym-encrypt-decrypt-spec.md#section3des)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-3des": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createCipher('3DES|CBC');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createCipher('3DES|ECB');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
