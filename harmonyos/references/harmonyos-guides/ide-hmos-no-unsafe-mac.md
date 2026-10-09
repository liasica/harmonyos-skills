---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-mac
title: "@security/no-unsafe-mac"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-mac
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:80e005219ab12b58298126a0eccb86b1f378da972531801a1e7ea53d0f5858d7
---

该规则禁止在MAC消息认证算法中使用不安全的哈希算法，例如SHA1。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-mac": "warn"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMac('SHA256');

import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.HmacSHA256('Message').toString();
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMac('SHA1');

import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.HmacSHA1('Message').toString();
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
