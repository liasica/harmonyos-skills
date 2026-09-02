---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unused-expressions
title: "@typescript-eslint/no-unused-expressions"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unused-expressions
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d62cf17ed93d5ac79f168a267d336a8eee11dd9534cc6e5f034817e086801864
---

代码中禁止包含未使用的表达式。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unused-expressions": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-unused-expressions选项](https://eslint.nodejs.cn/docs/rules/no-unused-expressions#选项)。

## 正例

```screen
export const v1 = Number.MAX_VALUE;

if ('hello'.length === v1) {
  console.info('hello');
}

{
  const v2 = '0';
  console.info(v2);
}
```

## 反例

```screen
Number.MAX_VALUE;

if ('0') '0';

{'0';}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
