---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-mac
title: "@security/no-unsafe-mac"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-mac
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:18cf3a61dfbadaf4c302e0aa2a07abaefa4c1f434e72b6d44a9c11ba468a66d8
---

该规则禁止在[MAC消息认证算法](../AppGallery-connect-Guides/aegis-message-authentication-code-calculation-0000001907018769.md)中使用不安全的哈希算法，例如SHA1。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-mac": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
import { CryptoJS } from '@ohos/crypto-js';
cryptoFramework.createMac('SHA256');
CryptoJS.HmacSHA256('Message').toString();
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
import { CryptoJS } from '@ohos/crypto-js';
cryptoFramework.createMac('SHA1');
CryptoJS.HmacSHA1('Message').toString();
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
