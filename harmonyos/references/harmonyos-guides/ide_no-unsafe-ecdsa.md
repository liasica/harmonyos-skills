---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-ecdsa
title: "@security/no-unsafe-ecdsa"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-ecdsa
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:62477ee6465154468703f025318f46aed63b27e665eb9be4d1c240513d2a2549
---

该规则禁止在ECDSA签名算法中使用不安全的SHA1摘要算法。推荐使用Petal Aegis SDK中的安全ECDSA接口，详情参见： [ECDSA签名验签](../AppGallery-connect-Guides/aegis-signature-verification-0000001866035345.md)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdsa": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC256|SHA256');
cryptoFramework.createVerify('ECC256|SHA256');
```

## 反例

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC224|SHA1');
cryptoFramework.createVerify('ECC224|SHA1');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
