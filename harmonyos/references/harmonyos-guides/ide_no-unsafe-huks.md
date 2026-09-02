---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-huks
title: "@security/no-unsafe-huks"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-huks
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b35f18e6655408629f3502e3e30552995d4549ed674e206334e335023c14eb6
---

此规则禁止在HUKS中使用不安全的加密模式ECB，不安全的摘要算法MD5、SHA1，填充算法NONE、PKCS1-V1\_5。推荐使用HUKS的AES-GCM算法，详情参见：[对称加解密算法](../AppGallery-connect-Guides/aegis-encryption-and-decryption-symmetry-0000001861247310.md)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-huks": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import {huks} from '@kit.UniversalKeystoreKit';  
let keyAlias: string = 'keyAlias'; 
let properties: Array<huks.HuksParam> = [
  { 
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
       huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
       huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
  }, 
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST, 
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  },
  {
   tag: huks.HuksTag.HUKS_TAG_PADDING,
   value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  }
]; 
let options: huks.HuksOptions = {
    properties: properties
}; 
huks.generateKeyItem(keyAlias, options);
```

## 反例

```screen
import {huks} from '@kit.UniversalKeystoreKit';  
let keyAlias: string = 'keyAlias'; 
let properties: Array<huks.HuksParam> = [
  { 
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
       huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
       huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }, 
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST, 
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA1
  },
  {
   tag: huks.HuksTag.HUKS_TAG_PADDING,
   value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  }
]; 
let options: huks.HuksOptions = {
    properties: properties
}; 
huks.generateKeyItem(keyAlias, options);
```

## 规则集

```screen
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
