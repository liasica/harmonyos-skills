---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dsa
title: @security/no-unsafe-dsa
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-dsa
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:54+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8c3bf53ece5003fb7be70cc5e98b5f2cc98fcd5bb2efb435073838ddf91bc56f
---

该规则禁止使用不安全的DSA签名算法，如DSA模数长度小于2048bit、摘要中使用不安全的SHA1哈希算法。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-dsa": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createSign('DSA3072|SHA256');
3. cryptoFramework.createVerify('DSA3072|SHA256');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createSign('DSA1024|SHA256');
3. cryptoFramework.createVerify('DSA1024|SHA256');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
