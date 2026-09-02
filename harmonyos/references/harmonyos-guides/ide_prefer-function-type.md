---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-function-type
title: "@typescript-eslint/prefer-function-type"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-function-type
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:afea282d2e7d4edebabcc40562b9cdf4b60d19c881001c5d57405207f9a540fa
---

强制使用函数类型而不是带有签名的对象类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-function-type": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export function foo(example: () => number): number {
  return example();
}

// returns the function itself, not the `this` argument.
export type ReturnsSelf = (arg: string) => ReturnsSelf;

export interface Foo {
  bar: string;
}
```

## 反例

```screen
interface GeneratedTypeLiteralInterface {
  (): number;
}

export function foo(example: GeneratedTypeLiteralInterface): number {
  return example();
}

export interface Foo {
  (bar: string): this;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
