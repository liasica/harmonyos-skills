---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-mac
title: @security/no-unsafe-mac
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-mac
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:55+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:945eec31aec99ca5af1b87c94ae5ed3b0de2f1e62759577040cab7586fd81388
---

该规则禁止在[MAC消息认证算法](../AppGallery-connect-Guides/aegis-message-authentication-code-calculation-0000001907018769.md)中使用不安全的哈希算法，例如SHA1。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-mac": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. import { CryptoJS } from '@ohos/crypto-js';
3. cryptoFramework.createMac('SHA256');
4. CryptoJS.HmacSHA256('Message').toString();
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. import { CryptoJS } from '@ohos/crypto-js';
3. cryptoFramework.createMac('SHA1');
4. CryptoJS.HmacSHA1('Message').toString();
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
