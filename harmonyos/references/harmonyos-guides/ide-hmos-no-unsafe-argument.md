---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-argument
title: "@typescript-eslint/no-unsafe-argument"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-argument
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4caee84ec9a29b23ea551562d1b95e5a57910d4ed646d771a103a339f043072e
---

不允许将any类型的值作为函数的参数传入。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-argument": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
