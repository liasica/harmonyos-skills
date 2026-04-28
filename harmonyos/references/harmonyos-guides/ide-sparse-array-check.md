---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-sparse-array-check
title: @performance/sparse-array-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/sparse-array-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:17+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0ab09e1a2128156849145870bb635f8b9dff221d3a3cf9bd92868afe32dad632
---

建议避免使用稀疏数组。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/sparse-array-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. let index = 3;
2. let result: number[] = [];
3. result[index] = 0;
```

## 反例

```
1. let count = 100000;
2. let arr1: number[] = new Array(count);
3. let arr2 = new Array<number>();
4. arr2[9999] = 0;
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
