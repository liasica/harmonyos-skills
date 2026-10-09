---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-dsa-key
title: "@security/no-unsafe-dsa-key"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-dsa-key
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a2494a0e0faecc37ae7552da3a64577f5641e232dfb7401723608d2d8b1cd354
---

该规则禁止使用不安全的DSA密钥，如DSA模数长度小于2048bit。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dsa-key": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DSA3072');
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DSA1024');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
