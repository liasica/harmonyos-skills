---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-template-expressions
title: @typescript-eslint/restrict-template-expressions
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/restrict-template-expressions
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b644b907fb2600fc470d598309eaa6c2ee03daa6422d14729532cbaf57d71ae0
---

要求模板表达式中的变量为“string”类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/restrict-template-expressions": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/restrict-template-expressions选项](https://typescript-eslint.nodejs.cn/rules/restrict-template-expressions/#options)。

## 正例

```
1. const arg: string | undefined = 'foo';
2. export const msg1 = `arg = ${arg}`;
3. export const msg2 = `arg = ${arg || 'default'}`;
```

## 反例

```
1. const arg1 = ['1', '2'];
2. export const msg1 = `arg1 = ${arg1}`;

4. interface GeneratedObjectLiteralInterface {
5. name: string;
6. }

8. const arg2: GeneratedObjectLiteralInterface = { name: 'Foo' };
9. export const msg2 = `arg2 = ${arg2 || null}`;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
