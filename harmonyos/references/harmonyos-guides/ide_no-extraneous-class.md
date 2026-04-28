---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extraneous-class
title: @typescript-eslint/no-extraneous-class
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extraneous-class
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a25753d3669e6634680505d2ba86005c794a955313f8f7cd4436c3cd60db2b7e
---

不允许将类用作命名空间，更多规则详情可参考[no-extraneous-class](https://typescript-eslint.nodejs.cn/rules/no-extraneous-class)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-extraneous-class": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-extraneous-class选项](https://typescript-eslint.nodejs.cn/rules/no-extraneous-class/#options)。

## 正例

```
1. export const version = 42;

3. export function isProduction() {
4. return version === 'production'.length;
5. }

7. export function logHelloWorld() {
8. console.log('Hello, world!');
9. }
```

## 反例

```
1. export class StaticConstants {
2. public static readonly version = 'development'.length;

4. public static isProduction() {
5. return StaticConstants.version === 'production'.length;
6. }
7. }

9. export class HelloWorldLogger {
10. public constructor() {
11. console.log('Hello, world!');
12. }
13. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
