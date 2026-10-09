---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-rsa-sign
title: "@security/no-unsafe-rsa-sign"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-rsa-sign
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e618ea31eee898f921707cba602e74e1279c082533149d78655825e542c24169
---

该规则禁止不安全的RSA签名算法，如RSA模数长度小于2048bit、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见： [RSA加解密](../AppGallery-connect-Guides/aegis-signature-verification-0000001866035345.md#section1039727112016)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-rsa-sign": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA3072|PSS|SHA256|MGF1_SHA256');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createVerify('RSA3072|PSS|SHA256|MGF1_SHA256');
```

## 反例

```ts
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA512|PKCS1|MD5');

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createVerify('RSA512|PKCS1|MD5');
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
