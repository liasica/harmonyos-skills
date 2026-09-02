---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-argument
title: "@typescript-eslint/no-unsafe-argument"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-argument
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b28473f13d92090628d6b7eed194c30bf5df7bb2ee09f0eb0d28855b342d8640
---

不允许将any类型的值作为函数的参数传入。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-argument": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
declare function foo(arg1: string, arg2: number, arg3: string): void;

foo('a', Number.MAX_VALUE, 'b');

const tuple1 = ['a', Number.MAX_VALUE, 'b'] as const;
foo(...tuple1);

declare function bar(arg1: string, arg2: number, ...rest: readonly string[]): void;
const array: string[] = ['a'];
bar('a', Number.MAX_VALUE, ...array);

declare function baz(arg1: Readonly<Set<string>>, arg2: Readonly<Map<string, string>>): void;
baz(new Set<string>(), new Map<string, string>());
```

## 反例

```screen
declare function foo(arg1: string, arg2: number, arg3: string): void;

const anyTyped = Number.MAX_VALUE as any;
// 变量anyTyped是any类型，不允许作为参数传入函数中
foo(...anyTyped);
// 变量anyTyped是any类型，不允许作为参数传入函数中
foo(anyTyped, Number.MAX_VALUE, 'a');

const anyArray: any[] = [];
// 变量anyArray是any类型数组，不允许将数组元素作为参数传入函数中
foo(...anyArray);

const tuple1 = ['a', anyTyped, 'b'] as const;
// 变量anyTyped是any类型数组，不允许将数组元素作为参数传入函数中
foo(...tuple1);
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
