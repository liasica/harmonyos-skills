---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-template-expressions
title: "@typescript-eslint/restrict-template-expressions"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/restrict-template-expressions
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9f5e923b592b1072c636b79f76892f92be3678c7c35329f719a5a6344bd23481
---

要求模板表达式中的变量为“string”类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-template-expressions": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/restrict-template-expressions选项](https://typescript-eslint.nodejs.cn/rules/restrict-template-expressions/#options)。

## 正例

```screen
const arg: string | undefined = 'foo';
export const msg1 = `arg = ${arg}`;
export const msg2 = `arg = ${arg || 'default'}`;
```

## 反例

```screen
const arg1 = ['1', '2'];
export const msg1 = `arg1 = ${arg1}`;

interface GeneratedObjectLiteralInterface {
  name: string;
}

const arg2: GeneratedObjectLiteralInterface = { name: 'Foo' };
export const msg2 = `arg2 = ${arg2 || null}`;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
