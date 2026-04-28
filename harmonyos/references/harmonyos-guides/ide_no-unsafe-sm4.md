---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm4
title: @security/no-unsafe-sm4
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:57+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f9d99b88200936ea5161667d291196e3b6d9fcf428f5d4562029b65adae24029
---

此规则禁止不安全的SM4算法，如加密模式ECB。推荐使用SM4\_CBC\_PKCS5Padding等不同算法，详情参见：[对称加解密算法](../AppGallery-connect-Guides/aegis-encryption-and-decryption-symmetry-0000001861247310.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-sm4": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createKdf('SM4_128|CBC|PKCS7')
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createCipher('SM4_128|ECB|PKCS7')
```

## 规则集

```
1. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
