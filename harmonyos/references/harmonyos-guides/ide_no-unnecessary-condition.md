---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-condition
title: "@typescript-eslint/no-unnecessary-condition"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-condition
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8f314eca0b8b3deada09f515b0e4c457db7d06ebedee2de2b1bf6ff2f7b1f958
---

不允许使用类型始终为真或始终为假的表达式作为判断条件。

## 规则配置

```screen
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

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
