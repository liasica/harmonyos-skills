---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-performance-no-dynamic-cls-func
title: "@performance/hp-performance-no-dynamic-cls-func"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-performance-no-dynamic-cls-func
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d77db49972258b8a491e690a8953922f023baeb481c515df12dd34e4d3a9cc7d
---

避免动态声明function与class，仅适用于js/ts。

根据[ArkTS编程规范](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-performance-no-dynamic-cls-func": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
function foo(f: boolean, a: number, b: number): number {
  if (f) {
    return add(a, b);
  } else {
    return sub(a, b);
  }
}
function add(c: number, d: number): number {
  return c + d;
}
function sub(e: number, g: number): number {
  return e - g;
}
```

## 反例

```screen
function foo(f: boolean, a: number, b: number): number {
  if (f) {
    function add(c: number, d: number): number {
      return c + d;
    }
    return add(a, b);
  } else {
    function sub(e: number, g: number): number {
      return e - g;
    }
    return sub(a, b);
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
