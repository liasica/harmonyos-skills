---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm4
title: "@security/no-unsafe-sm4"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-sm4
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:76370363306b273b2089ba6f2979b82c639ab0bb707ac340e426e40cc1e04425
---

此规则禁止不安全的SM4算法，如加密模式ECB。推荐使用SM4\_CBC\_PKCS5Padding等不同算法，详情参见：[对称加解密算法](../AppGallery-connect-Guides/aegis-encryption-and-decryption-symmetry-0000001861247310.md)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm4": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('SM4_128|CBC|PKCS7')
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM4_128|ECB|PKCS7')
```

## 规则集

```screen
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
