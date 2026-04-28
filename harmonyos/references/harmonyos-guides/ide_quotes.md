---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_quotes
title: @typescript-eslint/quotes
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/quotes
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:48+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:68d18e6fda2357794608f32418ecaec6233ca6477db35153b14be64e7ec2884d
---

强制使用一致的反引号、双引号或单引号风格。

说明

* 该规则默认检查字符串是否正确使用双引号。如需修改请参考[选项](ide_quotes.md#section182418564158)。
* 该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用[@hw-stylistic/quotes](ide-quotes-stylistic.md)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/quotes": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/quotes选项](https://eslint.nodejs.cn/docs/latest/rules/quotes#选项)。

## 正例

```
1. export const double = "double";
2. export const foo = `back
3. tick`;  // backticks are allowed due to newline
```

## 反例

```
1. // 默认推荐使用双引号
2. export const single = 'single';
3. export const unescaped = 'a string containing "double" quotes';
4. export const backtick = `back\ntick`; // you can use \n in single or double quoted strings
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
