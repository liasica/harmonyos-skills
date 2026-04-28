---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-assertion
title: @typescript-eslint/no-unnecessary-type-assertion
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-type-assertion
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:40+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d966dd0abf59ddc87113dd907dbbb31df45a56af574208737bdc03b8f6ebab65
---

禁止不必要的类型断言。

如果类型断言没有更改表达式的类型，也就没有必要使用。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unnecessary-type-assertion": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-unnecessary-type-assertion选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-type-assertion/#options)。

## 正例

```
1. const num = 3;
2. export const foo2 = num as number;
3. export const foo3 = 'foo' as string;
```

## 反例

```
1. const num = 3;
2. export const foo = num;
3. export const bar = foo!;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
