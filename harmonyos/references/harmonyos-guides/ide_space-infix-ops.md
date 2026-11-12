---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-infix-ops
title: "@typescript-eslint/space-infix-ops"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/space-infix-ops
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8fed0581be52464ece258f5092bd7a0ad217a6b581395c2d467315670ddc2d2f
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
