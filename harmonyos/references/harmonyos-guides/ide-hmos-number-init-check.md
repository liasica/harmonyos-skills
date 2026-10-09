---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-number-init-check
title: "@performance/number-init-check"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/number-init-check
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5e07a7acd2c518649c17ea67a2a2a6e5cc77ccfd47930d4bb04e89658712bb05
---

该规则将检查number是否正确使用。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/number-init-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
let intNum = 1;
intNum = 2;
let floatNum = 1.3;
floatNum = 2.4;
```

## 反例

```screen
let intNum = 1;
// intNum is declared as int. Avoid changing it to float.
intNum = 1.1; 
let floatNum = 1.3;
// floatNum is declared as float. Avoid changing it to int.
floatNum = 2;
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
