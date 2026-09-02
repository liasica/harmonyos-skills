---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-void-expression
title: "@typescript-eslint/no-confusing-void-expression"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-confusing-void-expression
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:48bebe8e7efdce49b611fe7eb2d4b8a491ba14f354d97f85a9cbdd7e1b45d03c
---

要求void类型的表达式出现在合适的位置。

void指要被忽略的函数返回，如果将void类型的表达式作为值使用，比如分配给变量、作为函数参数传递或者从函数中返回，容易产生误导。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-confusing-void-expression": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-confusing-void-expression选项](https://typescript-eslint.nodejs.cn/rules/no-confusing-void-expression/#options)。

## 正例

```screen
export function func(): void {
  console.info('no return');
}
```

## 反例

```screen
export function func(): void {
  return console.info('no return');
}

console.info(func());
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
