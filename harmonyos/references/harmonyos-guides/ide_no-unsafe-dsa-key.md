---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dsa-key
title: "@security/no-unsafe-dsa-key"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-dsa-key
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8fa04ebf57ed4ed0365b0d3e8918ccb9f36dc4e72ddbb76bbe5a6720bc71b3f4
---

该规则禁止使用不安全的DSA密钥，如DSA模数长度小于2048bit。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dsa-key": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DSA3072');
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DSA1024');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
