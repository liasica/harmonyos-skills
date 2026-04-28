---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm2-key
title: @security/no-unsafe-sm2-key
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-sm2-key
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:57+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d97951aab91618d0acce42e5366a3b2cf0a981e1686424c346741ce547b1e92c
---

此规则禁止不安全的非对称密钥类型SM2算法。推荐使用SM2\_256|SHA256算法和RSA算法，算法详情参见：[非对称加解密算法](../AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453.md)和[非对称密钥加解密算法规格](crypto-asym-encrypt-decrypt-spec.md#rsa)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-sm2-key": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('SM2_256|SHA256')
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('SM2|SHA256')
```

## 规则集

```
1. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
