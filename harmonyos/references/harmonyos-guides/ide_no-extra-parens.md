---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-parens
title: "@typescript-eslint/no-extra-parens"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extra-parens
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:61937bfdeadb8a82d6f8a844a36399b9a9109ae527a775823dd3042f52475c39
---

禁止使用不必要的括号。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-parens": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-extra-parens选项](https://eslint.nodejs.cn/docs/rules/no-extra-parens#选项)。

## 正例

```screen
// 默认不允许在任何表达式中使用不必要的括号
(0).toString();

const result = (() => {
  console.info('arrow function');
}) ? '1' : '2';

(/^a$/).test(result);
```

## 反例

```screen
// 默认不允许在任何表达式中使用不必要的括号
const b = 10;
const c = 20;
export const a = (b * c);

export const d = (a * b) + c;

export const myType = typeof (a);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
