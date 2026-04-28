---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-rsa-sign
title: @security/no-unsafe-rsa-sign
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-rsa-sign
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:56+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:afc043f69e2d30e54164d68e0f179329490adddfaab9ac0861a4bd59f8e99b51
---

该规则禁止不安全的RSA签名算法，如RSA模数长度小于2048bit、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见： [RSA加解密](../AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-rsa-sign": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createSign('RSA3072|PSS|SHA256|MGF1_SHA256');
3. cryptoFramework.createVerify('RSA3072|PSS|SHA256|MGF1_SHA256');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createSign('RSA512|PKCS1|MD5');
3. cryptoFramework.createVerify('RSA512|PKCS1|MD5');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
