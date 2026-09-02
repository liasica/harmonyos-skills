---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-kdf
title: "@security/no-unsafe-kdf"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-kdf
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7db9769125783a1e73444f0afd3e35baf0132778f92542331fcbf0af2486df69
---

禁止使用不安全的KDF算法，包括PBKDF2|SHA1和HKDF|SHA1。推荐使用PBKDF2|SHA256和HKDF|SHA256，PBKDF2|SHA256算法描述详情参见：[密钥派生算法](../AppGallery-connect-Guides/aegis-key-derivation-0000001861059318.md)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-kdf": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('PBKDF2|SHA256');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('HKDF|SHA256');
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('PBKDF2|SHA1');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('HKDF|SHA1');
```

## 规则集

```screen
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
