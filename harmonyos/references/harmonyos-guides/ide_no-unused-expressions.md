---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unused-expressions
title: @typescript-eslint/no-unused-expressions
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unused-expressions
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:42+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d9655dc4c01d2763c9360fe7759d28e50abe9972dc11e9debd078a10231fd9af
---

代码中禁止包含未使用的表达式。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unused-expressions": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-unused-expressions选项](https://eslint.nodejs.cn/docs/rules/no-unused-expressions#选项)。

## 正例

```
1. export const v1 = Number.MAX_VALUE;

3. if ('hello'.length === v1) {
4. console.info('hello');
5. }

7. {
8. const v2 = '0';
9. console.info(v2);
10. }
```

## 反例

```
1. Number.MAX_VALUE;

3. if ('0') '0';

5. {'0';}
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
