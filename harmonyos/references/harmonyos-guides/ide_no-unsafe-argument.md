---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-argument
title: @typescript-eslint/no-unsafe-argument
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-argument
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:14dab757650b6bed91925cfa8f76cde6ba4d502e6c05a8f5f869d20a869e018e
---

不允许将any类型的值作为函数的参数传入。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unsafe-argument": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. declare function foo(arg1: string, arg2: number, arg3: string): void;

3. foo('a', Number.MAX_VALUE, 'b');

5. const tuple1 = ['a', Number.MAX_VALUE, 'b'] as const;
6. foo(...tuple1);

8. declare function bar(arg1: string, arg2: number, ...rest: readonly string[]): void;
9. const array: string[] = ['a'];
10. bar('a', Number.MAX_VALUE, ...array);

12. declare function baz(arg1: Readonly<Set<string>>, arg2: Readonly<Map<string, string>>): void;
13. baz(new Set<string>(), new Map<string, string>());
```

## 反例

```
1. declare function foo(arg1: string, arg2: number, arg3: string): void;

3. const anyTyped = Number.MAX_VALUE as any;
4. // 变量anyTyped是any类型，不允许作为参数传入函数中
5. foo(...anyTyped);
6. // 变量anyTyped是any类型，不允许作为参数传入函数中
7. foo(anyTyped, Number.MAX_VALUE, 'a');

9. const anyArray: any[] = [];
10. // 变量anyArray是any类型数组，不允许将数组元素作为参数传入函数中
11. foo(...anyArray);

13. const tuple1 = ['a', anyTyped, 'b'] as const;
14. // 变量anyTyped是any类型数组，不允许将数组元素作为参数传入函数中
15. foo(...tuple1);
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
