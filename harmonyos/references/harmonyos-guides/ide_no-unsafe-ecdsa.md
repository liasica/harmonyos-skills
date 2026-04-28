---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-ecdsa
title: @security/no-unsafe-ecdsa
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-ecdsa
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:55+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:12f2726884817195f9a989b8e55e8f4055d50bbd30f4b0a7b1e850fb848d0adc
---

该规则禁止在ECDSA签名算法中使用不安全的SHA1摘要算法。推荐使用Petal Aegis SDK中的安全ECDSA接口，详情参见： [ECDSA签名验签](../AppGallery-connect-Guides/aegis-signature-verification-0000001866035345.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-ecdsa": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createSign('ECC256|SHA256');
3. cryptoFramework.createVerify('ECC256|SHA256');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createSign('ECC224|SHA1');
3. cryptoFramework.createVerify('ECC224|SHA1');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
