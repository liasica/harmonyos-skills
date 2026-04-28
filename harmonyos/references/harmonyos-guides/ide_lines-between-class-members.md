---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_lines-between-class-members
title: @typescript-eslint/lines-between-class-members
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/lines-between-class-members
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:28+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2ca170b157f8090c72845ca34796429b65d8136bd9471c8d70b43f92564e845d
---

禁止或者要求类成员之间有空行分隔。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/lines-between-class-members": "error"
5. }
6. }
```

## 选项

该规则有两个选项配置，第一个选项可以是字符串或者对象，第二个选项是对象。详情请参考[eslint/lines-between-class-members选项](https://eslint.nodejs.cn/docs/latest/rules/lines-between-class-members#选项)。

此外，第二个选项支持配置exceptAfterOverload属性，表示是否需要跳过重载类成员后空行的检查。exceptAfterOverload的值为布尔类型，配置为true时表示跳过不检查，配置为false时表示不跳过检查。默认为true。

示例：

```
1. "@typescript-eslint/lines-between-class-members": [
2. "error",
3. "always",
4. {
5. "exceptAfterOverload": true
6. },
7. ]
```

## 正例

```
1. // 默认要求类成员之间有空行分隔
2. export class Foo {
3. public baz() {
4. console.info('baz');
5. }

7. public qux() {
8. console.info('qux');
9. }
10. }
```

## 反例

```
1. // 默认要求类成员之间有空行分隔
2. export class Foo {
3. public baz() {
4. console.info('baz');
5. }
6. public qux() {
7. console.info('qux');
8. }
9. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
