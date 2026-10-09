---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-sparse-array-check
title: "@performance/sparse-array-check"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/sparse-array-check
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:07b7e6f6b61424cb7da2f24f7c2ab1825c52a33433282462bd738a7c90a2bcd4
---

建议避免使用稀疏数组。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/sparse-array-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
let index = 3;
let result: number[] = [];
result[index] = 0;
```

## 反例

```ts
let count = 100000;
let arr1: number[] = new Array(count);
let arr2 = new Array<number>();
arr2[9999] = 0;
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
