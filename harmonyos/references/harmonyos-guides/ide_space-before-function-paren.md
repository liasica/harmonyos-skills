---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-before-function-paren
title: @typescript-eslint/space-before-function-paren
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/space-before-function-paren
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a5d54938e84dc2456774dd064cfcf52b84936f554415aa23557fbb43b665eb3c
---

强制在函数名和括号之间保持一致的空格风格。

说明

* 该规则默认要求函数名和括号间有空格。如需修改请参考[选项](ide_space-before-function-paren.md#section182418564158)。
* 该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用[@hw-stylistic/space-before-function-paren](ide-space-before-function-paren-stylistic.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/space-before-function-paren": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/space-before-function-paren选项](https://eslint.nodejs.cn/docs/rules/space-before-function-paren#选项)。

## 正例

```
1. // 默认foo和(之间需要一个空格
2. export function foo () {
3. // ...
4. }
```

## 反例

```
1. // 默认foo和(之间需要一个空格
2. export function foo() {
3. // ...
4. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
