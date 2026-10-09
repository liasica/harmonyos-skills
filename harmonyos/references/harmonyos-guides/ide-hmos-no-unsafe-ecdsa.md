---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-ecdsa
title: "@security/no-unsafe-ecdsa"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-ecdsa
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c8ed8c14bc39ed9ea0433a30da3e6e255873b4e00822126f94d46e1fd6c991f1
---

该规则禁止在ECDSA签名算法中使用不安全的SHA1摘要算法。推荐使用Petal Aegis SDK中的安全ECDSA接口，详情参见： [ECDSA签名验签](../AppGallery-connect-Guides/aegis-signature-verification-0000001866035345.md#section12984925133517)。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdsa": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC256|SHA256');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createVerify('ECC256|SHA256');
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC224|SHA1');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createVerify('ECC224|SHA1');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
