---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-infix-ops
title: "@typescript-eslint/space-infix-ops"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/space-infix-ops
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:622895c51a5731d45b88d342576b3459dc6522d9b00c7d7ebafec22ca99b9f0c
---

运算符前后要求有空格。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/space-infix-ops": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/space-infix-ops选项](https://eslint.nodejs.cn/docs/rules/space-infix-ops#选项)。

## 正例

```screen
declare const a: number;
declare const b: number;
export const c = a + b;
```

## 反例

```screen
declare const a: number;
declare const b: number;
export const c = a+b;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
