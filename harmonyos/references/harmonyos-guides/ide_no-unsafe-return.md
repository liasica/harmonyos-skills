---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-return
title: "@typescript-eslint/no-unsafe-return"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-return
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d561d14d21e704220e80ee313aa48e37e5f7a9f4f80845893c4c4b8365f4534f
---

函数禁止返回类型为“any”的值。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-return": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export function foo1(): string {
  return '1';
}

export function foo2(): object {
  return Object.create(null) as Record<string, unknown>;
}

export const foo3 = (): object[] => [];
export const foo4 = (): string[] => ['a'];

export function assignability1(): Set<string> {
  return new Set<string>(['foo']);
}
```

## 反例

```screen
export function foo1(): string {
  return '1' as any;
}

export function foo2(): string {
  return Object.create(null) as any;
}

export const foo3 = (): object[] => [] as any;
export const foo4 = (): string[] => ['a'] as any;

export function assignability1(): Set<string> {
  return new Set<string>(['foo']) as any;
}
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
