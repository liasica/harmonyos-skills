---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-plus-operands
title: @typescript-eslint/restrict-plus-operands
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/restrict-plus-operands
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4c1827235d3cba96077fea5b1bc87c14cc64b11dde98347244fa4fd9189cd3d9
---

要求加法的两个操作数都是相同的类型，并且是“bigint”、“number”或“string”。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/restrict-plus-operands": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/restrict-plus-operands选项](https://typescript-eslint.nodejs.cn/rules/restrict-plus-operands/#options)。

## 正例

```
1. const num = 10;
2. const bigIntNum = 1n;
3. export const foo1 = parseInt('5.5', num) + num;
4. export const foo2 = bigIntNum + bigIntNum;
```

## 反例

```
1. const num = 10;
2. const bigIntNum = 1n;
3. export const foo2 = bigIntNum + num;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
