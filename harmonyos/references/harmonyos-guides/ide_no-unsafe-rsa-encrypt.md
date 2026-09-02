---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-rsa-encrypt
title: "@security/no-unsafe-rsa-encrypt"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-rsa-encrypt
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a0be1adf43153d5bc7b1b479c478bffbc57316bd2aa2f5ef82b3722c2de12d97
---

该规则禁止使用不安全的RSA非对称加密算法，如RSA模数长度小于2048bit、填充模式为PKCS1、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法，推荐使用Petal Aegis SDK中的安全RSA加密和解密接口，详情参见：[RSA加解密](../AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453.md)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-rsa-encrypt": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('RSA3072|PKCS1_OAEP|SHA256|MGF1_SHA256');
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('RSA512|PKCS1');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
