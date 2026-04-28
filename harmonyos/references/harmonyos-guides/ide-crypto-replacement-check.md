---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-crypto-replacement-check
title: @performance/crypto-replacement-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3547eb2fd3c795f9bbcc42b41569aeae88404dcd49c4e39360528cba74fedad2
---

对于三方库@ohos/crypto-js所提供的大部分接口，SDK中若有对应的系统原生实现（@ohos.security.cryptoFramework），建议使用系统原生接口。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/crypto-replacement-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import cryptoFramework from '@ohos.security.cryptoFramework';
2. // MD5加密
3. let md = cryptoFramework.createMd('MD5');
```

## 反例

```
1. import { CryptoJS } from '@ohos/crypto-js';

3. /**
4. * 安装库：ohpm install @ohos/crypto-js
5. */

7. // MD5加密
8. let mdOutput = CryptoJS.MD5('Message');
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
