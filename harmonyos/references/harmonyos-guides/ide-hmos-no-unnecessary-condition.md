---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unnecessary-condition
title: "@typescript-eslint/no-unnecessary-condition"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-condition
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3745a125cefae4ddfa3713681c45ef714cd44509ca9518fc7280464cc791ebec
---

不允许使用类型始终为真或始终为假的表达式作为判断条件。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-condition": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-unnecessary-condition选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-condition/#options)。

## 正例

```ts
const index = 0;
export function head(items: readonly string[]): string {
  // Necessary, since items.length might be 0
  if (items.length) {
    return items[index].toUpperCase();
  } else {
    return '';
  }
}

export function foo(arg: string): void {
  // Necessary, since foo might be ''.
  if (arg) {
  }
}

export function bar(arg?: string | null) {
  // Necessary, since arg might be nullish
  return arg?.length;
}
```

## 反例

```ts
const index = 0;
export function head(items: readonly string[]) {
  // items can never be nullable, so this is unnecessary
  if (items) {
    return items[index].toUpperCase();
  } else {
    return '';
  }
}

export function foo(arg: 'bar' | 'baz') {
  // arg is never nullable or empty string, so this is unnecessary
  if (arg) {
  }
}

export function bar(arg: string) {
  // arg can never be nullish, so ?. is unnecessary
  return arg?.length;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
