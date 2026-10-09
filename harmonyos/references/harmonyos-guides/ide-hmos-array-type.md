---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-array-type
title: "@typescript-eslint/array-type"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/array-type
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:89671d5d2989743bfe263564a0e2a717e1f224442c1f7c6e983283b1cdc2ae7a
---

定义数组类型时，建议使用相同的样式。比如都使用T[]或者都使用Array<T>。

## 规则配置

```json
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
