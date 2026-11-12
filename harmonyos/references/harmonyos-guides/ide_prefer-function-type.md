---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-function-type
title: "@typescript-eslint/prefer-function-type"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-function-type
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:09c18290600987778be5f85541f0502628b7a6155b62921aa63b75ab15ef6e38
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
