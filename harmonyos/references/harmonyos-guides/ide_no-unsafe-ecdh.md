---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-ecdh
title: @security/no-unsafe-ecdh
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-ecdh
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:57+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:618b376dac80bb259357a2421993dbedaedbe75a9dabcc3914f73dba5a217f5c
---

此规则禁止使用不安全的非对称密钥类型ECC。推荐使用ECC256算法，详情参见：[密钥生成算法](../AppGallery-connect-Guides/aegis-key-generation-0000001819355432.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-ecdh": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('ECC256');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('ECC');
```

## 规则集

```
1. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
