---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-performance-no-closures
title: "@performance/hp-performance-no-closures"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-performance-no-closures
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf406c1429e747fce59de12ad260df4ecb7f9e3aa648ba1b3c9b99cbc394b9c1
---

建议函数内部变量尽量使用参数传递。

根据[ArkTS编程规范](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-performance-no-closures": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
let arr = [0, 1, 2];
function foo(array: Array<number>): number {
  // arr 尽量通过参数传递
  return array[0] + array[1];
}
foo(arr);
```

## 反例

```screen
let arr = [0, 1, 2];
function foo() {
  // arr 尽量通过参数传递
  return arr[0] + arr[1];
}
foo();
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
