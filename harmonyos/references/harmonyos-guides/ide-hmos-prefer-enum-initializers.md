---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-enum-initializers
title: "@typescript-eslint/prefer-enum-initializers"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-enum-initializers
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:18+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:4bc40e71a387187491d0878da5a1ef6950befa691228d07efbf79a8c30b30054
---

推荐显式初始化每个枚举成员值。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-enum-initializers": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export enum Status {
  open = 'Open',
  close = 'Close'
}

export enum Direction {
  up = '1',
  down = '2'
}

export enum Color {
  red = 'Red',
  green = 'Green',
  blue = 'Blue'
}
```

## 反例

```ts
export enum Status {
  open,
  close
}

export enum Direction {
  up,
  down
}

export enum Color {
  red,
  green = 'Green',
  blue
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
