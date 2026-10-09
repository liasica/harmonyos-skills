---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-as-const
title: "@typescript-eslint/prefer-as-const"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-as-const
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:6b640b1d5da28165ac9274f1cefbf8be31ead28170012c63d90bead548cf3a7a
---

对于字面量类型，强制使用“as const”。

将字面量类型的值转换为对应的字面量类型，有两种方式，一种是“as const”，另一种是“as 字面量类型”，推荐使用“as const”。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-as-const": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export const foo1 = 'bar';
export const foo2 = 'bar' as const;
export const foo3: 'bar' = 'bar' as const;
export const bar4 = 'bar' as string;
export const foo6 = { bar: 'baz' };
```

## 反例

```ts
export const bar: 1 = 1;
export const foo1 = <'bar'>'bar';
export const foo2 = { bar: 'baz' as 'baz' };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
