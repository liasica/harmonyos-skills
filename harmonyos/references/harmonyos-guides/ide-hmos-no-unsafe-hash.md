---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-hash
title: "@security/no-unsafe-hash"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-hash
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:88c3122469e1b268098420456e972f7896ac34bef5fda759a7e95cd31b5f7c50
---

该规则禁止使用不安全的哈希算法，例如MD5、SHA1。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-hash": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA256');

import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA256('Message').toString();
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('MD5');

import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.MD5('Message').toString();
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
