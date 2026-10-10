---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unnecessary-qualifier
title: "@typescript-eslint/no-unnecessary-qualifier"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-qualifier
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:17+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:a2806375c6842e970b9e0d159f503dbece895993632e4aab24ed94e7a3772851
---

禁止不必要的命名空间限定符。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-qualifier": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
