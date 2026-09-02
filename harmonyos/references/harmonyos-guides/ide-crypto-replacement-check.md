---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-crypto-replacement-check
title: "@performance/crypto-replacement-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/crypto-replacement-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ff41113b14bf20d6d535cc611225e3bd99afd548a7ec7eeaa204b4b5c3d2b307
---

对于三方库@ohos/crypto-js所提供的大部分接口，SDK中若有对应的系统原生实现（@ohos.security.cryptoFramework），建议使用系统原生接口。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/crypto-replacement-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
// MD5加密
let md = cryptoFramework.createMd('MD5');
```

## 反例

```screen
import { CryptoJS } from '@ohos/crypto-js';

/**
 * 安装库：ohpm install @ohos/crypto-js
 */

// MD5加密
let mdOutput = CryptoJS.MD5('Message');
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
