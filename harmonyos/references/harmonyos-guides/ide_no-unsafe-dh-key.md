---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dh-key
title: @security/no-unsafe-dh-key
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-dh-key
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:54+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dcc6070851a5e0dafae414384ed6161c22bc9b8d715f4e89e3b40deba91c9cfe
---

该规则禁止使用不安全的DH密钥，如DH模数长度小于2048bit。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-dh-key": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('DH_modp3072');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createAsyKeyGenerator('DH_modp1536');
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
