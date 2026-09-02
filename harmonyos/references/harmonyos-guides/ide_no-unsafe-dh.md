---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dh
title: "@security/no-unsafe-dh"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-dh
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:86db059dad8b59ebc0d346d6d22eb57eb3ebdb24f19dc3bb3622a9a90298597a
---

该规则禁止使用不安全的DH密钥协商算法，如DH模数长度小于2048bit。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dh": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp3072');
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp1536');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
