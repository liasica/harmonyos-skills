---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-parameter-properties
title: @typescript-eslint/no-parameter-properties
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-parameter-properties
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:37+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:43caf17c41d2392718603ee7b8ec62165eb5aba76d9ca9bc561078fa20a0d90d
---

禁止在类构造函数中使用参数属性。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-parameter-properties": "error"
5. }
6. }
```

## 选项

默认禁止在构造函数中使用任何参数属性，如果想要使用某些属性，可以配置额外选项。

allows：接受一个字符串数组，数组中的属性可以使用。字符串支持以下值：

* readonly
* private
* protected
* public
* private readonly
* protected readonly
* public readonly

示例：

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-parameter-properties": ["error", {"allows": ["readonly"]}]
5. }
6. }
```

## 正例

```
1. export class Foo {
2. public name: string;

4. public constructor(name: string) {
5. this.name = name;
6. }
7. }
```

## 反例

```
1. export class Foo {
2. // 默认配置下，参数不允许使用readonly
3. public constructor(public readonly name: string) {}
4. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
