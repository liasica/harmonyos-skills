---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-non-null-assertion
title: "@typescript-eslint/no-extra-non-null-assertion"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extra-non-null-assertion
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e02c44b66ed2db18e31b3d5d82d5a18027579d7771010fe9d852eed0cbc42235
---

不允许多余的非空断言。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-non-null-assertion": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
interface BarType1 {
  bar: number;
}

function getFoo(): BarType1 | null {
  return null;
}
const foo: BarType1 | null = getFoo();
export const bar1: number | undefined = foo?.bar;

export function foo1(bar: number | undefined): void {
  const newBar: number = bar ?? Number.MAX_VALUE;
  console.info(`${newBar}`);
}
```

## 反例

```screen
interface BarType1 {
  bar: number;
}

const foo1: BarType1 | null = null;
export const bar1 = foo1!!!.bar;

export function foo2(bar: number | undefined) {
  const newBar: number = bar!!!;
  console.info(`${newBar}`);
}

interface BarType2 {
  n: number;
}

export function foo(bar?: BarType2) {
  return bar!?.n;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
