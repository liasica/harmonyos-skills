---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-array-sort-compare
title: @typescript-eslint/require-array-sort-compare
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/require-array-sort-compare
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:77ea0ea34a62781909eafd58e58a7b1727313aabcd88ea016c074e02fc992d8d
---

要求调用“Array#sort”时，始终提供“compareFunction”。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/require-array-sort-compare": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/require-array-sort-compare选项](https://typescript-eslint.nodejs.cn/rules/require-array-sort-compare/#options)。

## 正例

```
1. declare const array: string[];

3. array.sort((a, b) => a.length - b.length);
4. array.sort((a, b) => a.localeCompare(b));
```

## 反例

```
1. declare const array: number[];
2. declare const stringArray: object[];

4. array.sort();

6. // String arrays should be sorted using `String#localeCompare`.
7. stringArray.sort();
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
