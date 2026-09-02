---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-type
title: "@typescript-eslint/array-type"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/array-type
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dcb74e7a9d9afa71e43fd967feb3f9bd3428535175912f7d1d448098c426380e
---

定义数组类型时，建议使用相同的样式。比如都使用T[]或者都使用Array<T>。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/array-type": "error"
  }
}
```

## 选项

详情请参考[typescript/array-type 选项](https://typescript-eslint.nodejs.cn/rules/array-type#options)。

## 正例

```screen
const x: string[] = ['a', 'b'];
const y: readonly string[] = ['a', 'b'];

export { x, y };
```

## 反例

```screen
const x: Array<string> = ['a', 'b'];
const y: ReadonlyArray<string> = ['a', 'b'];

export { x, y };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
