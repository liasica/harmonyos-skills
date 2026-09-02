---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-hash
title: "@security/no-unsafe-hash"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-hash
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ee4bbb108fb95b1d6aafcdbfde821276b87338b888f5aa230580a44af5c8563f
---

该规则禁止使用不安全的哈希算法，例如MD5、SHA1。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-hash": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
//正例1
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA256');

//正例2
/**
 * 下载crypto-js依赖：ohpm install @ohos/crypto-js
 */
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA256('Message').toString();
```

## 反例

```screen
//反例1.1
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('MD5');

//反例1.2
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA1');

//反例2.1
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.MD5('Message').toString();

//反例2.2
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA1('Message').toString();
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
