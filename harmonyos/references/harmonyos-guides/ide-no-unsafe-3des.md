---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-unsafe-3des
title: "@security/no-unsafe-3des"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-3des
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:12+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:812dcf569e26e15b824f93132eacb5a95df304bc61e76c23df8dbc13631bff0d
---

该规则禁止使用不安全的3DES加密模式，例如3DES|ECB。建议使用安全的3DES加密模式，例如3DES|CBC。详情参考[3DES加密模式](crypto-encryption-decryption.md)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-3des": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|CBC');
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|ECB');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
