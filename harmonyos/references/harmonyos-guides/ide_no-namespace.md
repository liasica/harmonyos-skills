---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-namespace
title: @typescript-eslint/no-namespace
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-namespace
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:37+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b1d3ba5ceaf61b48c43058b6bc31879445553b0d90f55323fbabadaec01d9c9c
---

禁止使用 TypeScript语法中的命名空间。

命名空间是一种过时的语法，推荐使用import/export。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-namespace": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-namespace选项](https://typescript-eslint.nodejs.cn/rules/no-namespace/#options)。

## 正例

```
1. // foo为模块名
2. declare module 'foo' {}
3. // anything inside a d.ts file
```

## 反例

```
1. module foo {}
2. namespace foo {}

4. declare module foo {}
5. declare namespace foo {}
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
