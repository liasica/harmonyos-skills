---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-dh
title: "@security/no-unsafe-dh"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-dh
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e0d25ebaadcbd346dd93af05d3aaf6a458f1e0cf66dad40450af3279d61ba2a3
---

该规则禁止使用不安全的DH密钥协商算法，如DH模数长度小于2048bit。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dh": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp3072');
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp1536');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
