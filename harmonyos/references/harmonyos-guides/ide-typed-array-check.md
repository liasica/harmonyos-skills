---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-typed-array-check
title: "@performance/typed-array-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/typed-array-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e6c192de6566ae474c604e27d82b4f5533cbd253b1cd88b2a9ea74d9cd848c0e
---

数值数组推荐使用TypedArray。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/typed-array-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
const typedArray1 = new Int8Array([1, 2, 3]); 
const typedArray2 = new Int8Array([4, 5, 6]);  
let res = new Int8Array(3);
for (let i = 0; i < 3; i++) {
     res[i] = typedArray1[i] + typedArray2[i];
}
```

## 反例

```screen
const typedArray1: number[] = new Array(1, 2, 3);
const typedArray2: number[] = new Array(4, 5, 6);
let res: number[] = new Array(3);
for (let i = 0; i < 3; i++) {
     res[i] = typedArray1[i] + typedArray2[i];
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
