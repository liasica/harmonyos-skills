---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-assignment
title: "@typescript-eslint/no-unsafe-assignment"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-assignment
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fe02410a604b8d80e45089cf7c1c7b2c46c2c823043113250bbcd908cac3ae2d
---

禁止将“any”类型的值赋值给变量和属性。

该规则仅支持对.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-assignment": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
let [x] = ['1'];
[x] = ['1'] as [string];
console.info([x].toString());

// generic position examples
export const a1: Set<string> = new Set<string>();
export const a2: Map<string, string> = new Map<string, string>();
export const a3: Set<string[]> = new Set<string[]>();
export const a4: Set<Set<Set<string>>> = new Set<Set<Set<string>>>();
```

## 反例

```screen
let [x] = ['1'];
[x] = ['1'] as [any];
[x] = '1' as any;
console.info([x].toString());

// generic position examples
export const a1: Set<string> = new Set<any>();
export const a2: Map<string, string> = new Map<any, string>();
export const a3: Set<string[]> = new Set<any[]>();
export const a4: Set<Set<Set<string>>> = new Set<Set<Set<any>>>();
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
