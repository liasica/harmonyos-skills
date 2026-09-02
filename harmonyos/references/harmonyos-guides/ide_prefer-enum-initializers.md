---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-enum-initializers
title: "@typescript-eslint/prefer-enum-initializers"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-enum-initializers
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b557849181c3cecd403a3ef5b54cdf27703a053b7dca0fa4d2d408949b0b8c63
---

推荐显式初始化每个枚举成员值。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-enum-initializers": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
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

```screen
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
  green,
  blue
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
