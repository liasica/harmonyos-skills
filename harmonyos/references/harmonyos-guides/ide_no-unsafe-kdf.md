---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-kdf
title: @security/no-unsafe-kdf
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-kdf
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:57+08:00
doc_updated_at: 2026-01-27
content_hash: sha256:67ac1ef0dbf9d7c1cdf8e1376de846bdcb93ef4daedb97cd6bf0b834c510647e
---

禁止使用不安全的KDF算法，包括PBKDF2|SHA1和HKDF|SHA1。推荐使用PBKDF2|SHA256和HKDF|SHA256，PBKDF2|SHA256算法描述详情参见：[密钥派生算法](../AppGallery-connect-Guides/aegis-key-derivation-0000001861059318.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-kdf": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createKdf('PBKDF2|SHA256');

4. import cryptoFramework from '@ohos.security.cryptoFramework';
5. cryptoFramework.createKdf('HKDF|SHA256');
```

## 反例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. cryptoFramework.createKdf('PBKDF2|SHA1');

4. import cryptoFramework from '@ohos.security.cryptoFramework';
5. cryptoFramework.createKdf('HKDF|SHA1');
```

## 规则集

```
1. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
