---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-aes
title: "@security/no-unsafe-aes"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-aes
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:17+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5e6bdd6c20ef5a240462b419f0f192d90bb497113678651fa7a39dd788e12df8
---

该规则禁止在AES加密算法中使用不安全的ECB加密模式。推荐使用Petal Aegis SDK中的安全AES接口，详情请参见[对称加解密](../AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453.md)。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-aes": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('AES128|CBC|PKCS5');
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('AES128|ECB|NoPadding');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
