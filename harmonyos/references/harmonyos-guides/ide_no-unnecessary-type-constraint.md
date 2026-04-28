---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-constraint
title: @typescript-eslint/no-unnecessary-type-constraint
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-type-constraint
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:40+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:64964f7fafadaf68659d698d0ad5b7510dcba52af7ee73be805a12172e0995a5
---

不允许在泛型中使用不必要的约束条件。

泛型参数（<T>）如果不包含“extends”关键字，默认约束条件是“unknown”（即<T extends unknown>），所以“<T extends any>“、“<T extends unknown>“的写法是多余的。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unnecessary-type-constraint": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export interface Foo<T> {
2. foo: T;
3. }

5. export const bar = <T>(param: T): void => {
6. console.info(`${param as string}`);
7. };

9. export function foo<T>(param: T): void {
10. console.info(`${param as string}`);
11. }
```

## 反例

```
1. // extends any或者extends unknown的写法是多余的
2. export interface Foo<T extends any> {
3. foo: T;
4. }

6. export const bar = <T extends unknown>(param: T): void => {
7. console.info(`${param as string}`);
8. };

10. export function foo<T extends any>(param: T): void {
11. console.info(`${param as string}`);
12. }
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
