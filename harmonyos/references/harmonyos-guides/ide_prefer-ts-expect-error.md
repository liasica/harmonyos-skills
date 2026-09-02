---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-ts-expect-error
title: "@typescript-eslint/prefer-ts-expect-error"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-ts-expect-error
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ed82138a59a7b5132b1411628a54ca644c60f0e993b7b4baab20b44f26a106b5
---

强制使用“@ts-expect-error”而不是“@ts-ignore”。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-ts-expect-error": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// @ts-expect-error: with description
export const str: string = 1;

/**
 * Explaining comment
 *
 * @ts-expect-error: with description */
export const multiLine: number = 'value';

/** @ts-expect-error: with description */
export const block: string = 1;
```

## 反例

```screen
// @ts-ignore
const str: string = 1;

/**
 * Explaining comment
 *
 * @ts-ignore */
const multiLine: number = 'value';

/** @ts-ignore */
const block: string = 1;

const isOptionEnabled = (key: string): boolean => {
  // @ts-ignore: if key isn't in globalOptions it'll be undefined which is false
  return !!globalOptions[key];
};
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
