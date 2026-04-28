---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-typed-array-check
title: @performance/typed-array-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/typed-array-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:18+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c4044e1ea9dce58b3c49d1814d7893bf7e26d6e132f371606e342424bcacb5c4
---

数值数组推荐使用TypedArray。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/typed-array-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const typedArray1 = new Int8Array([1, 2, 3]);
2. const typedArray2 = new Int8Array([4, 5, 6]);
3. let res = new Int8Array(3);
4. for (let i = 0; i < 3; i++) {
5. res[i] = typedArray1[i] + typedArray2[i];
6. }
```

## 反例

```
1. const typedArray1: number[] = new Array(1, 2, 3);
2. const typedArray2: number[] = new Array(4, 5, 6);
3. let res: number[] = new Array(3);
4. for (let i = 0; i < 3; i++) {
5. res[i] = typedArray1[i] + typedArray2[i];
6. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
