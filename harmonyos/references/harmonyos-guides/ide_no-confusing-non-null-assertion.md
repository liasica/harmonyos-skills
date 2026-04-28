---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-non-null-assertion
title: @typescript-eslint/no-confusing-non-null-assertion
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-confusing-non-null-assertion
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:29+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:31601d9024f74f90701cb2a336da67bc34bfef217850b8715bdf449fd66c2d5b
---

不允许在可能产生混淆的位置使用非空断言。

在赋值或者等于旁边使用非空断言（!）会产生混淆，看起来类似于不等于，不建议这种写法。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-confusing-non-null-assertion": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. interface Foo {
2. bar?: string;
3. num?: number;
4. }

6. function getFoo(): Foo {
7. return {
8. bar: 'bar',
9. num: Number.MAX_VALUE
10. };
11. }
12. const foo: Foo = getFoo();
13. export const isEqualsBar = foo.bar === 'hello';
14. const num = 2;
15. export const isEqualsNum = num + (foo.num!) === num;
```

## 反例

```
1. interface Foo {
2. bar?: string;
3. num?: number;
4. }

6. function getFoo(): Foo {
7. return {
8. bar: 'bar',
9. num: Number.MAX_VALUE
10. };
11. }
12. const foo: Foo = getFoo();
13. // 可能会产生混淆，误以为是不等于
14. export const isEqualsBar = foo.bar! === 'hello';
15. // 可能会产生混淆，误以为是不等于
16. const num = 2;
17. export const isEqualsNum = num + foo.num! === num;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
