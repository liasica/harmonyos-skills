---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-number-init-check
title: @performance/number-init-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/number-init-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ff54c6fff883fd34c4910af313a373dae79e8dd65348cd829b818f8f4c4c6046
---

该规则将检查number是否正确使用。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/number-init-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. let intNum = 1;
2. intNum = 2;
3. let floatNum = 1.3;
4. floatNum = 2.4;
```

## 反例

```
1. let intNum = 1;
2. // intNum is declared as int. Avoid changing it to float.
3. intNum = 1.1;
4. let floatNum = 1.3;
5. // floatNum is declared as float. Avoid changing it to int.
6. floatNum = 2;
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
