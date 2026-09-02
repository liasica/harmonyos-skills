---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-qualifier
title: "@typescript-eslint/no-unnecessary-qualifier"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-qualifier
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:88b885b55aaa920499ad0f5d3e4d97e3f3c83c466ac204bf7f3f671e287f3ce4
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
