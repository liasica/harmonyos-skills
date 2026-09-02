---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-constraint
title: "@typescript-eslint/no-unnecessary-type-constraint"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-type-constraint
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d02a2d259c92828d5c7be77beeefbed761e63582c2ce6241ef38c1fdf5a46c1f
---

不允许在泛型中使用不必要的约束条件。

泛型参数（<T>）如果不包含“extends”关键字，默认约束条件是“unknown”（即<T extends unknown>），所以“<T extends any>“、“<T extends unknown>“的写法是多余的。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-constraint": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export interface Foo<T> {
  foo: T;
}

export const bar = <T>(param: T): void => {
  console.info(`${param as string}`);
};

export function foo<T>(param: T): void {
  console.info(`${param as string}`);
}
```

## 反例

```screen
// extends any或者extends unknown的写法是多余的
export interface Foo<T extends any> {
  foo: T;
}

export const bar = <T extends unknown>(param: T): void => {
  console.info(`${param as string}`);
};

export function foo<T extends any>(param: T): void {
  console.info(`${param as string}`);
}
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
