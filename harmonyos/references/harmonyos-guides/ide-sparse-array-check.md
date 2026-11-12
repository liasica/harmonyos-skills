---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-sparse-array-check
title: "@performance/sparse-array-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/sparse-array-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8759c13c519d6cd068d62ce6c901c2ded5adb75513427c0b3e5e738e7942434c
---

建议避免使用稀疏数组。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```screen
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

```screen
let index = 3;
let result: number[] = [];
result[index] = 0;
```

## 反例

```screen
let count = 100000;
let arr1: number[] = new Array(count);
let arr2 = new Array<number>();
arr2[9999] = 0;
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
