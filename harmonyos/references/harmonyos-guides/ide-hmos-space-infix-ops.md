---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-space-infix-ops
title: "@typescript-eslint/space-infix-ops"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/space-infix-ops
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c42237d97041300128652751cca2f025c93126c2bf07f345f697399d33ed10e9
---

运算符前后要求有空格。

## 规则配置

```json
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

```ts
declare const a: number;
declare const b: number;
export const c = a + b;
```

## 反例

```ts
declare const a: number;
declare const b: number;
export const c = a+b;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
