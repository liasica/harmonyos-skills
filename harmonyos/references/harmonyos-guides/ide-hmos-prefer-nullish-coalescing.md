---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-nullish-coalescing
title: "@typescript-eslint/prefer-nullish-coalescing"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-nullish-coalescing
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:18+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:8e6e9b15d3d8b0641d23b3e22d4db42646076d6295f91ee3e4a78904fef86511
---

强制使用空合并运算符（??）而不是逻辑运算符。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-nullish-coalescing": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/prefer-nullish-coalescing选项](https://typescript-eslint.nodejs.cn/rules/prefer-nullish-coalescing/#options)。

## 正例

```ts
function getText1(): string | undefined {
  return 'bar';
}

function getText2(): string | null {
  return 'bar';
}

const foo1: string | undefined = getText1();
export const v1 = foo1 ?? 'a string';

const foo2: string | null = getText2();
export const v2 = foo2 ?? 'a string';
```

## 反例

```screen
declare const a: string | null;
declare const b: string | null;

export const c = a || b;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
