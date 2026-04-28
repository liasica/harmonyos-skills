---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-aes
title: @security/no-unsafe-aes
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-aes
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:12107fc0b5cd13df78d90a86b02094e47a6171183e9a67c5bd0f4e627c705248
---

该规则禁止在AES加密算法中使用不安全的ECB加密模式。推荐使用Petal Aegis SDK中的安全AES接口，详情请参见[对称加解密](../AppGallery-connect-Guides/aegis-encryption-and-decryption-symmetry-0000001861247310.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-aes": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createCipher('AES128|CBC|PKCS5');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createCipher('AES128|ECB|NoPadding');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
