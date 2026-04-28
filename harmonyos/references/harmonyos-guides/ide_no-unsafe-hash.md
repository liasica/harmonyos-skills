---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-hash
title: @security/no-unsafe-hash
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-hash
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:55+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:8355d6a38ef3400d70dfaffaa01ba4c8451bedad7c55a6d93829f100fd704218
---

该规则禁止不安全的哈希算法，例如MD5、SHA1。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-hash": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. //正例1
2. import cryptoFramework from '@ohos.security.cryptoFramework';
3. cryptoFramework.createMd('SHA256');

5. //正例2
6. /**
7. * 下载crypto-js依赖：ohpm install @ohos/crypto-js
8. */
9. import { CryptoJS } from '@ohos/crypto-js';
10. CryptoJS.SHA256('Message').toString();
```

## 反例

```
1. //反例1.1
2. import cryptoFramework from '@ohos.security.cryptoFramework';
3. cryptoFramework.createMd('MD5');

5. //反例1.2
6. import cryptoFramework from '@ohos.security.cryptoFramework';
7. cryptoFramework.createMd('SHA1');

9. //反例2.1
10. import { CryptoJS } from '@ohos/crypto-js';
11. CryptoJS.MD5('Message').toString();

13. //反例2.2
14. import { CryptoJS } from '@ohos/crypto-js';
15. CryptoJS.SHA1('Message').toString();
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
