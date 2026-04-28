---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-empty-function
title: @typescript-eslint/no-empty-function
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-empty-function
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:31+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:69e409b466999406f3b058130107f94c4942e68a3dea4a37bb6b8c79b367ffd0
---

不允许使用空函数。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-empty-function": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-empty-function选项](https://eslint.nodejs.cn/docs/rules/no-empty-function#选项)。

## 正例

该规则旨在消除空函数。如果函数包含注释，则不会将其视为问题。

```
1. /*eslint no-empty-function: "error"*/
2. function foo() {
3. // do nothing.
4. }

6. const baz = () => {
7. foo();
8. };

10. export class Bar {
11. public meth1() {
12. // do something
13. }

15. public meth2() {
16. baz();
17. }
18. }
```

## 反例

```
1. /*eslint no-empty-function: "error"*/
2. function foo() {

4. }

6. const baz = () => {

8. };

10. export class Bar {
11. public meth1() {

13. }

15. public meth2() {

17. }
18. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
