---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-function-type
title: "@typescript-eslint/prefer-function-type"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-function-type
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:18+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:85a5d1bf5fd9322b5dbf1739a0fe0f5d6ae647e7482a482b2ab6eea27bc52ad0
---

强制使用函数类型而不是带有签名的对象类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-function-type": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
