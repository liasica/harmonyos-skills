---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-dsa
title: "@security/no-unsafe-dsa"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-dsa
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a50536c68bb1c8f9db4c0553855b6a6d5a0a73ab06e8e2dbc2517b89c0c32ca8
---

该规则禁止使用不安全的DSA签名算法，如DSA模数长度小于2048bit、摘要中使用不安全的SHA1哈希算法。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dsa": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA3072|SHA256');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createVerify('DSA3072|SHA256');
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA1024|SHA256');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createVerify('DSA1024|SHA256');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
