---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-parens
title: @typescript-eslint/no-extra-parens
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extra-parens
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:416bc737c037120b504abaf7129f2a01d68f4e240ae87e7d26323e644033c8c0
---

禁止使用不必要的括号。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-extra-parens": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-extra-parens选项](https://eslint.nodejs.cn/docs/rules/no-extra-parens#选项)。

## 正例

```
1. // 默认不允许在任何表达式中使用不必要的括号
2. (0).toString();

4. const result = (() => {
5. console.info('arrow function');
6. }) ? '1' : '2';

8. (/^a$/).test(result);
```

## 反例

```
1. // 默认不允许在任何表达式中使用不必要的括号
2. const b = 10;
3. const c = 20;
4. export const a = (b * c);

6. export const d = (a * b) + c;

8. export const myType = typeof (a);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
