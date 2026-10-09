---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-require-array-sort-compare
title: "@typescript-eslint/require-array-sort-compare"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/require-array-sort-compare
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b70aa2a6e3cce9314352696be9bee22ea22422f496c1ec844e879e5328f6627e
---

要求调用“Array#sort”时，始终提供“compareFunction”。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/require-array-sort-compare": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/require-array-sort-compare选项](https://typescript-eslint.nodejs.cn/rules/require-array-sort-compare/#options)。

## 正例

```ts
declare const array: string[];

array.sort((a, b) => a.length - b.length);
array.sort((a, b) => a.localeCompare(b));
```

## 反例

```ts
declare const array: number[];
declare const stringArray: object[];

array.sort();

// String arrays should be sorted using `String#localeCompare`.
stringArray.sort();
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
