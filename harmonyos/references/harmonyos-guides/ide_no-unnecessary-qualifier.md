---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-qualifier
title: "@typescript-eslint/no-unnecessary-qualifier"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-qualifier
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:82b54c46d20079f1e09aeb07c1e174c6056f2e7a29d53185e21284f339eef95f
---

禁止不必要的命名空间限定符。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-qualifier": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export enum A {
  b = 'x',
  c = b
}

export namespace B {
  export type C = number;
  export const x: C = 3;
}
```

## 反例

```screen
export enum A {
  b = 'x',
  c = A.b
}

export namespace B {
  export type C = number;
  export const x: B.C = 3;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
