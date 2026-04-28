---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi
title: @typescript-eslint/semi
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/semi
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:eff802c43a285cf5134c1646686704571d388e6267f378cc4dd57910e61df43d
---

要求或不允许使用分号。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/semi": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/semi选项](https://eslint.nodejs.cn/docs/rules/semi#选项)。

## 正例

```
1. export const name = 'ESLint';

3. export class Foo {
4. public bar = '1';
5. }
```

## 反例

```
1. // 默认在语句末尾需要加分号
2. export const name = 'ESLint'

4. export class Foo {
5. // 默认在语句末尾需要加分号
6. public bar = '1'
7. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
